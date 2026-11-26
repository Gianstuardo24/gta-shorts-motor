import sys, json, subprocess
from pathlib import Path
from utilidades import extraer_json

CFG = json.loads(Path("config.json").read_text()) if Path("config.json").exists() else {}
CANAL = CFG.get("canal", "")

PROMPT = """Eres experto en YouTube Shorts de gaming en espanol. Para cada Short te paso su guion.
Genera para cada uno:
- "titulo": maximo 70 caracteres, con gancho y curiosidad, que incluya "GTA 6". Sin clickbait falso: debe cumplir lo que promete el video.
- "descripcion": 1 o 2 frases cortas que resuman y enganchen, y al final una pregunta para comentarios.
- "hashtags": 5 a 8 hashtags relevantes (siempre incluye #GTA6 y #Shorts).
- "comentario_fijado": un comentario corto para fijar que invite a responder.
Responde SOLO con un array JSON, un objeto por Short y en el mismo orden:
[{"titulo": "...", "descripcion": "...", "hashtags": ["#GTA6", "#Shorts"], "comentario_fijado": "..."}]"""


def main():
    if len(sys.argv) < 2:
        print("Uso: python publicar.py ID_DEL_VIDEO   (ej: python publicar.py 7c28StUD66k)")
        sys.exit(1)
    base = sys.argv[1]
    guiones = sorted(Path("guiones").glob(f"{base}_[0-9][0-9].json"))
    if not guiones:
        print(f"⚠️ No hay guiones para {base}")
        sys.exit(1)

    entrada = "\n\n".join(f"SHORT {i}:\n" + " ".join(json.loads(g.read_text())["frases"])
                          for i, g in enumerate(guiones, 1))
    print(f"📝 Generando títulos, descripciones y hashtags para {len(guiones)} Shorts...")
    r = subprocess.run(["claude", "-p", PROMPT], input=entrada, capture_output=True, text=True)
    try:
        datos = extraer_json(r.stdout)
    except ValueError:
        print("⚠️ Claude no devolvio JSON. Respuesta:\n", r.stdout[:500])
        sys.exit(1)

    md = [f"# Publicación: {base}", ""]
    for i, (g, d) in enumerate(zip(guiones, datos), 1):
        guion = json.loads(g.read_text())
        desc = d.get("descripcion", "")
        if CANAL:
            desc += f"\n\nSíguenos en {CANAL} para más GTA 6 todos los días 🎮"
        desc += "\n\n" + " ".join(d.get("hashtags", []))
        md += ["---", "", f"## Short {i}", f"🎬 Archivo: salida/{base}_narrado_{i:02d}.mp4", "",
               "### Título", "```", d.get("titulo", ""), "```", "",
               "### Descripción", "```", desc, "```", "",
               "### Comentario fijado", "```", d.get("comentario_fijado", ""), "```", ""]
        if guion.get("fuentes"):
            md += ["Fuentes verificadas (solo para ti): " + " · ".join(guion["fuentes"]), ""]
        print(f"   {i}. {d.get('titulo', '')}")

    salida = Path("salida") / f"{base}_publicacion.md"
    salida.write_text("\n".join(md), encoding="utf-8")
    print(f"\n✅ Todo listo para copiar y pegar en: {salida}")


if __name__ == "__main__":
    main()
