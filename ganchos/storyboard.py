"""STORYBOARD AUTOMATICO: cada frase del guion se convierte en una ESCENA con su recurso, listo para producir.

Por frase: que se ve, que recurso usa, como se mueve, texto en pantalla, sonido y para que sirve en la retencion.
Recursos permitidos (regla fija, sin excepciones):
  - toma_propia   GTA: grabacion propia del juego -> genera la LISTA DE GRABACION para Tao (donde, que hacer, camara, segundos)
  - oficial       material oficial (Rockstar: kit de prensa / trailers oficiales; NASA; etc.)
  - chatgpt       imagen generada en ChatGPT (rotulada como recreacion; sin caras reales, sin logos) -> prompts en hojas de 3 paneles
  - animacion     animacion hecha con codigo (graficos, mapas, contadores, comparaciones)
  - grafico       texto/grafico en pantalla sobre fondo
  Nunca: material de otros creadores, deepfakes, caras reales, logos de marcas.
Usa: perfil del canal (identidad visual), anatomia temporal de los top, piezas 'visual' del arsenal y reglas vigentes.

Uso:  python storyboard.py C2026112001          (todos los guiones del lote)
      python storyboard.py guiones/R2026112401_01.json
Salidas: campo "storyboard" en el guion · storyboards/<guion>.md · prompts ChatGPT (hojas_<LOTE>_A/B/C + portada) en
         datos/prompts/cola_<LOTE>.json y .md · GTA: datos/grabar/<LOTE>.md (lista de grabacion)
"""
import sys, json, sqlite3, subprocess, datetime as dt
from pathlib import Path

CEREBRO = Path("datos/cerebro.db")
PERFILES = Path("datos/perfiles")
OUT_MD = Path("storyboards")
PROMPTS = Path("datos/prompts")
GRABAR = Path("datos/grabar")
BASE_HOJA = ("Horizontal 3:2 image split into 3 tall vertical panels side by side, separated by thin white borders. "
             "No text, no letters, no numbers, no logos, no real people. ")
CANAL_PERFIL = {"gta": "gta", "es": "gta", "en": "en", "rabbit": "rabbit", "mdm": "mdm", "cafe": "cafe"}

PROMPT = """Eres DIRECTOR DE ARTE y STORYBOARDER de YouTube Shorts verticales (9:16). Convierte el guion en escenas, una por frase.
Te paso el guion, el perfil visual del canal, la anatomia temporal de los videos top (si hay), piezas visuales del arsenal y reglas.
Recursos permitidos: toma_propia (solo GTA: grabacion propia del juego), oficial (material oficial: Rockstar, NASA...),
chatgpt (imagen generada, como recreacion; sin caras reales, sin logos, sin texto), animacion (hecha con codigo: graficos,
mapas, contadores, comparaciones), grafico (texto/grafico en pantalla).
PROHIBIDO: material de otros creadores, caras reales, logos, deepfakes. GTA: lo que se muestre del juego debe ser toma_propia u
oficial (nunca imagen generada simulando el juego); chatgpt solo para ilustraciones genericas y rotuladas.
Devuelve SOLO un objeto JSON:
{"estilo":"estilo visual comun para todas las imagenes (luz, paleta, epoca, textura) en ingles, 1 frase",
 "escenas":[{"n":1,"escena":"que se ve, concreto","recurso":"toma_propia|oficial|chatgpt|animacion|grafico",
   "toma":{"donde":"lugar del mapa/juego","accion":"que hacer","camara":"plano, angulo, movimiento","segundos":N} o null,
   "prompt_panel":"descripcion del panel en ingles, sin texto ni caras reales (ver MODO)" o "",
   "animacion":"animacion o grafico de codigo que va (como capa) en esta escena" o "",
   "movimiento":"zoom lento | paneo | punch-in | estatico | ...","texto_pantalla":"2-5 palabras o ''",
   "sonido":"efecto o '' (whoosh, golpe, riser...)","funcion":"interrupcion|curiosidad|desarrollo|escalada|giro|payoff|loop",
   "por_que":"por que esta escena retiene en ese momento","nota_legal":"'' o advertencia"}],
 "portada":{"texto":"2-5 palabras GRANDES","imagen":"que se ve (en ingles)","recurso":"chatgpt|toma_propia|oficial"},
 "riesgos":["escenas dificiles de mostrar legalmente o que no calzan con la frase"]}
__MODO__
Reglas: la escena debe MOSTRAR lo que dice la frase o agregar algo que la complemente (no decorar); primer cuadro = interrupcion
visual fuerte; al menos 1 reenganche visual a mitad; la ultima escena debe poder conectar con la primera (loop) si se puede."""


def leer(p):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return {}


def contexto(perfil_key):
    perfil = leer(PERFILES / f"{perfil_key}.json")
    ana = Path("datos/estrategia/anatomia.md")
    reg = Path("datos/estrategia/reglas_vigentes.md")
    vis = ""
    try:
        c = sqlite3.connect(CEREBRO)
        vis = "\n".join(f"- #{i} {n}: {p} (condicion: {co})" for i, n, p, co in c.execute(
            "SELECT id, nombre, pieza, condicion FROM arsenal WHERE estado='activa' AND area IN ('visual','ritmo_audio','formato') "
            "ORDER BY evidencia DESC LIMIT 15"))
    except Exception:
        pass
    return (f"PERFIL: {json.dumps(perfil, ensure_ascii=False)[:2500]}\n\nANATOMIA DE LOS TOP:\n"
            f"{ana.read_text(encoding='utf-8')[:2000] if ana.exists() else '(sin datos aun)'}\n\nPIEZAS VISUALES DEL ARSENAL:\n{vis or '(sin piezas aun)'}\n\n"
            f"REGLAS (extracto):\n{reg.read_text(encoding='utf-8')[:2500] if reg.exists() else ''}")


MODO_IA = ("MODO IMAGEN POR FRASE (este canal): TODAS las escenas llevan recurso 'chatgpt' con su prompt_panel (la imagen base de "
           "esa frase, en orden). Las animaciones o graficos van ENCIMA de esa imagen: descríbelos en 'animacion'.")
MODO_GTA = ("MODO GTA: lo que se muestre del juego es toma_propia (graba Tao) u oficial; usa chatgpt solo para ilustraciones genericas "
            "rotuladas y pon su prompt_panel; animacion/grafico para datos.")
MODO_GTA_SIN_JUEGO = ("MODO GTA SIN JUEGO (Tao no tiene el juego): NO uses toma_propia. Cada escena es 'animacion' (mapa, ruta, pasos, contador, "
                      "comparacion hecha con codigo: describela en 'animacion'), 'oficial' (captura/trailer oficial de Rockstar: describe cual) o "
                      "'chatgpt' (ilustracion generica rotulada, sin simular el juego). Prioriza animacion: es lo que hace la guia clara.")


def pedir(g, perfil_key):
    perfil = leer(PERFILES / f"{perfil_key}.json")
    modo = (MODO_GTA if perfil.get("tiene_juego", True) else MODO_GTA_SIN_JUEGO) if perfil_key in ("gta", "en") else MODO_IA
    prompt = PROMPT.replace("__MODO__", modo)
    entrada = contexto(perfil_key) + "\n\nGUION:\n" + json.dumps(
        {k: g.get(k) for k in ("titulo", "texto_pantalla", "frases", "tema", "canal")}, ensure_ascii=False, indent=1)
    r = subprocess.run(["claude", "-p", prompt], input=entrada, capture_output=True, text=True, timeout=900)
    i = r.stdout.find("{")
    dec = json.JSONDecoder()
    while i != -1:
        try:
            obj, _ = dec.raw_decode(r.stdout, i)
            if isinstance(obj, dict) and "escenas" in obj:
                return obj
        except json.JSONDecodeError:
            pass
        i = r.stdout.find("{", i + 1)
    raise ValueError("Claude no devolvio un storyboard valido")


def hojas(lote, sb, por_frase=True):
    """Paneles -> hojas de 3 (formato de imagenes_ia.py: hoja A = frases 1-3, B = 4-6, C = 7-9) + portada.
    por_frase=True (canales no GTA): una imagen por frase, EN ORDEN (si falta prompt, se usa la descripcion de la escena)."""
    esc = sorted(sb.get("escenas", []), key=lambda e: e.get("n") or 0)
    if por_frase:
        paneles = [dict(e, prompt_panel=e.get("prompt_panel") or e.get("escena", "")) for e in esc]
    else:
        paneles = [e for e in esc if e.get("recurso") == "chatgpt" and e.get("prompt_panel")]
    estilo = sb.get("estilo") or "Cinematic photorealistic"
    cola, md = [], []
    for k in range(0, len(paneles), 3):
        trio = paneles[k:k + 3]
        while len(trio) < 3:
            trio.append({"prompt_panel": trio[-1]["prompt_panel"] + ", alternate angle, closer framing", "n": trio[-1].get("n")})
        letra = "ABCDEFGH"[k // 3]
        p = BASE_HOJA + estilo.rstrip(".") + ". " + " ".join(f"Panel {j + 1}: {t['prompt_panel'].rstrip('.')}." for j, t in enumerate(trio))
        n = f"hoja_{lote}_{letra}.png"
        cola.append({"n": n, "p": "Generate this image now, no questions: " + p})
        md += [f"**{n}** (frases {', '.join(str(t.get('n')) for t in trio)})", "```", p, "```"]
    pt = sb.get("portada") or {}
    if pt.get("recurso", "chatgpt") == "chatgpt" and pt.get("imagen"):
        p = (f'Vertical 2:3 YouTube Shorts cover. Big bold white title text at the top: "{pt.get("texto", "")}". Below it, {pt["imagen"].rstrip(".")}, '
             f"{estilo.rstrip('.')}. The bottom 30% must be calm, dark and empty of details. No logos, no real people.")
        n = f"portada_{lote}.png"
        cola.append({"n": n, "p": "Generate this image now, no questions: " + p})
        md += [f"**{n}**", "```", p, "```"]
    return cola, md


def lista_grabacion(lote, g, sb):
    tomas = [e for e in sb.get("escenas", []) if e.get("recurso") == "toma_propia" and e.get("toma")]
    if not tomas:
        return None
    L = [f"# 🎮 Lista de grabación · {lote} · {g.get('titulo')}", "",
         "_Graba en el juego (botón Compartir / capturadora). 1080p o más, sin HUD si se puede, 2–3 s extra al inicio y al final de cada toma._", "",
         "| Frase | Dónde | Qué hacer | Cámara | Segundos |", "|---|---|---|---|---|"]
    for e in tomas:
        t = e["toma"]
        L.append(f"| {e['n']} | {t.get('donde', '')} | {t.get('accion', '')} | {t.get('camara', '')} | {t.get('segundos', '')} |")
    L += ["", "Guarda los clips como `tomas_propias/<lote>_<frase>.mp4` (ej: " + f"`{lote}_03.mp4`)."]
    GRABAR.mkdir(parents=True, exist_ok=True)
    f = GRABAR / f"{lote}.md"
    f.write_text("\n".join(L), encoding="utf-8")
    return f


def md_storyboard(a, g, sb):
    L = [f"# 🎬 Storyboard · {a.stem} · {g.get('titulo')}", "", f"_Estilo: {sb.get('estilo', '')}_", "",
         "| # | Frase | Escena | Recurso | Movimiento | Texto | Sonido | Función |", "|---|---|---|---|---|---|---|---|"]
    fr = g.get("frases") or []
    for e in sb.get("escenas", []):
        n = e.get("n") or 0
        cel = lambda s: str(s or "").replace("|", "/")
        L.append(f"| {n} | {cel(fr[n - 1] if 0 < n <= len(fr) else '')} | {cel(e.get('escena'))}{' + capa: ' + cel(e.get('animacion')) if e.get('animacion') else ''} | **{e.get('recurso')}** | {cel(e.get('movimiento'))} | "
                 f"{cel(e.get('texto_pantalla'))} | {cel(e.get('sonido'))} | {e.get('funcion')} |")
    if sb.get("riesgos"):
        L += ["", "**⚠️ Riesgos:** " + " · ".join(sb["riesgos"])]
    OUT_MD.mkdir(exist_ok=True)
    (OUT_MD / f"{a.stem}.md").write_text("\n".join(L), encoding="utf-8")


def main():
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    if not args:
        sys.exit("Uso: python storyboard.py <LOTE | guiones/archivo.json>")
    obj = args[0]
    archivos = [Path(obj)] if obj.endswith(".json") else sorted(Path("guiones").glob(f"{obj}_[0-9][0-9].json"))
    for a in archivos:
        g = leer(a)
        canal = g.get("canal") or "gta"
        perfil_key = CANAL_PERFIL.get(canal, canal)
        print(f"🎬 Storyboard {a.name}: {g.get('titulo')}", flush=True)
        try:
            sb = pedir(g, perfil_key)
        except Exception as e:
            print(f"   ⚠️ {e}")
            continue
        g["storyboard"] = dict(sb, fecha=dt.datetime.now().isoformat(timespec="minutes"))
        a.write_text(json.dumps(g, ensure_ascii=False, indent=2))
        md_storyboard(a, g, sb)
        lote = a.stem.rsplit("_", 1)[0]
        cola, md = hojas(lote, sb, por_frase=perfil_key not in ("gta", "en"))
        if cola:
            PROMPTS.mkdir(parents=True, exist_ok=True)
            (PROMPTS / f"cola_{lote}.json").write_text(json.dumps(cola, ensure_ascii=False), encoding="utf-8")
            (PROMPTS / f"prompts_{lote}.md").write_text(f"# Prompts ChatGPT · {lote}\n\n" + "\n".join(md), encoding="utf-8")
        gr = lista_grabacion(lote, g, sb)
        cuenta = {}
        for e in sb.get("escenas", []):
            cuenta[e.get("recurso")] = cuenta.get(e.get("recurso"), 0) + 1
        print(f"   ✅ {len(sb.get('escenas', []))} escenas · " + " · ".join(f"{k} {v}" for k, v in cuenta.items())
              + (f" · {len(cola)} imágenes para ChatGPT" if cola else "") + (f" · lista de grabación: {gr}" if gr else ""), flush=True)
        for r in sb.get("riesgos") or []:
            print(f"   ⚠️ {r}", flush=True)


if __name__ == "__main__":
    main()
