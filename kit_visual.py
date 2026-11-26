"""KIT VISUAL POR VIDEO: una sola imagen generada en ChatGPT con 6-9 elementos PROPIOS de ese guion
(no stickers genericos), que luego se recortan y entran en el video cuando se nombran, con movimiento y reaccion.

Flujo:
  1) python kit_visual.py BASE            -> por cada guion BASE_NN: Claude escribe el prompt de la imagen y el plan de uso
                                             (que elemento, en que frase, como entra, a que reacciona). Queda en el guion ("kit").
  2) En el Estudio (pestaña Videos) cada video muestra "🎨 Kit": copias el prompt, generas la imagen en ChatGPT
     y la ARRASTRAS a la tarjeta. Se guarda como assets/stickers/entrada/kit_<guion>.png y se recorta sola.
  3) subtitular.py usa primero los elementos del kit del video; si no hay kit, los stickers del canal.
"""
import sys, json, subprocess, re
from pathlib import Path
from utilidades import cfg, extraer_json

CFG = cfg()
ESTILOS = {
    "gta": "glossy 3D render, thick clean shapes, vivid Miami neon palette (hot pink, cyan, purple, sunset orange), slight cel-shading, "
           "consistent studio lighting, NO white outline, NO drop shadow",
    "rabbit": "mysterious dark retro 3D render, palette deep navy, burnt orange, cream, eerie green glow, cinematic rim light, "
              "slightly vintage texture, NO white outline, NO drop shadow",
}

PROMPT = """Eres director de arte de Shorts. Canal: __NICHO__ (idioma del video: __IDIOMA__). Te paso guiones numerados.
Para CADA guion disena un KIT VISUAL: 6 a 9 objetos/iconos/escenas en miniatura que ilustren EXACTAMENTE lo que dice ese guion
(nada generico: si habla de 212 GB, una consola reventando de datos y una barra de carga marcada 212; si habla de una rata
en una foto, una lupa sobre una silueta de rata; si habla de una fecha, un calendario con ese dia). Prohibido: logos y marcas
reales (nada de PlayStation/Xbox/Rockstar escritos: usa "consola generica"), personas reales, texto largo (solo numeros o 1-2
palabras cortas si hacen falta, y dilo asi: 'with the number 212 printed on it').
Devuelve para cada guion:
- "elementos": lista de 6 a 9 objetos; cada uno {"nombre": snake_case corto en ingles, "descripcion": como se ve (1 frase, en ingles),
   "frase": indice (0..n-1) de la frase del guion donde debe aparecer, "entrada": "rebote | caida | costado | zoom | apuntar",
   "reaccion": "" o que hace cuando pasa algo ("tiembla cuando cae la cifra", "se llena cuando dice borrar")}.
   Que aparezca ALGO en al menos 5 frases distintas, y el hook (frase 0) siempre tenga su elemento.
- "prompt": el prompt COMPLETO en ingles para generar la hoja en ChatGPT: empieza con
  "Sticker sheet, __N__ separate objects in a __GRID__ grid with lots of empty space between them, none touching, on a flat solid
  pure chroma-key green background (#00FF00). Style: __ESTILO__. No text except the numbers mentioned. Objects: 1) ... 2) ..."
  (numera los objetos EN EL MISMO ORDEN que "elementos", con su descripcion).
Responde SOLO un array JSON, un objeto por guion, en el mismo orden: [{"elementos": [...], "prompt": "..."}]"""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    base = sys.argv[1]
    guiones = sorted(Path("guiones").glob(f"{base}_[0-9][0-9].json"))
    if "--num" in sys.argv:
        sel = {int(x) for x in sys.argv[sys.argv.index("--num") + 1].split(",")}
        guiones = [g for g in guiones if int(g.stem[-2:]) in sel]
    guiones = [g for g in guiones if "--rehacer" in sys.argv or "kit" not in json.loads(g.read_text())]
    if not guiones:
        print("✔ Todos los guiones ya tienen kit (usa --rehacer para repetir)")
        return
    estilo = ESTILOS.get(CFG.get("stickers", "gta"), ESTILOS["gta"])
    entrada = "\n\n".join(f"GUION {i} ({g.stem}):\n" + "\n".join(f"  [{k}] {fr}" for k, fr in enumerate(json.loads(g.read_text())["frases"]))
                          for i, g in enumerate(guiones, 1))
    pr = (PROMPT.replace("__NICHO__", CFG.get("nicho", "GTA 6")).replace("__IDIOMA__", "ingles" if CFG.get("idioma") == "en" else "espanol")
          .replace("__ESTILO__", estilo).replace("__N__", "6-9").replace("__GRID__", "3x3"))
    print(f"🎨 Disenando kit visual para {len(guiones)} guiones...")
    r = subprocess.run(["claude", "-p", pr], input=entrada, capture_output=True, text=True, timeout=900)
    try:
        datos = extraer_json(r.stdout)
    except ValueError:
        print("⚠️ Claude no devolvio el kit:", (r.stdout or "")[:300])
        return
    for g, d in zip(guiones, datos):
        if not isinstance(d, dict) or not d.get("elementos"):
            continue
        j = json.loads(g.read_text())
        els = []
        for e in d["elementos"][:9]:
            n = re.sub(r"[^a-z0-9]+", "_", str(e.get("nombre", "")).lower()).strip("_")[:30] or f"el{len(els) + 1}"
            els.append({**e, "nombre": n})
        j["kit"] = {"elementos": els, "prompt": d.get("prompt", ""), "imagen": f"kit_{g.stem}.png", "estado": "sin imagen"}
        g.write_text(json.dumps(j, ensure_ascii=False, indent=1), encoding="utf-8")
        # el .txt de nombres para stickers.py (orden = orden de la hoja)
        ent = Path("assets/stickers/entrada")
        ent.mkdir(parents=True, exist_ok=True)
        (ent / f"kit_{g.stem}.txt").write_text("\n".join(e["nombre"] for e in els) + "\n")
        print(f"   ✅ {g.stem}: {', '.join(e['nombre'] for e in els)}")
    print("\n📋 Ahora, en el Estudio: 🎨 Kit → copiar prompt → generar en ChatGPT → arrastrar la imagen a la tarjeta.")


if __name__ == "__main__":
    main()
