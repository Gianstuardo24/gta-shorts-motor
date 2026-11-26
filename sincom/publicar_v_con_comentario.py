import sys, re, json, shutil, subprocess
from datetime import datetime
from pathlib import Path
from utilidades import extraer_json
import horario

from utilidades import cfg
CFG = cfg()
CANAL = CFG.get("canal", "")
# Carpeta donde quedan los Shorts listos para subir, ordenados por canal y dia
CARPETA = Path(CFG.get("carpeta_youtube", "~/Desktop/YouTube")).expanduser() / (CANAL.lstrip("@") or "Canal")


def ocupados():
    """Horarios ya usados por Shorts que estan en la carpeta del canal (para no repetirlos)."""
    out = []
    if CARPETA.exists():
        for f in CARPETA.glob("**/*.mp4"):  # incluye Subidos/
            m = re.match(r"(\d{4}-\d{2}-\d{2}) .*", f.parent.name)
            h = re.match(r"(\d{2})h - ", f.name)
            if m and h:
                out.append(datetime.strptime(f"{m.group(1)} {h.group(1)}", "%Y-%m-%d %H").replace(tzinfo=horario.MI_ZONA))
    return out


REGISTRO = Path("horarios.json")   # que Short sale cuando, en cada canal (para intercalar idiomas)


def registro():
    return json.loads(REGISTRO.read_text()) if REGISTRO.exists() else {}


def asignar(slots, evitar):
    """Ordena los videos en los horarios sin que un video salga el MISMO DIA que su version en el otro idioma.
    slots: horarios en orden · evitar[i]: fecha (date) en que sale la otra version del video i (o None).
    Busca la asignacion mas parecida al orden original (prueba en orden y retrocede si choca)."""
    n = len(slots)
    usado, orden = [False] * n, []

    def probar(k):
        if k == n:
            return True
        for i in range(n):
            if not usado[i] and evitar[i] != slots[k].date():
                usado[i] = True
                orden.append(i)
                if probar(k + 1):
                    return True
                usado[i] = False
                orden.pop()
        return False

    if any(evitar) and probar(0):
        return orden          # orden[k] = indice del video que va en el horario k
    return list(range(n))


def nombre_corto(titulo, largo=50):
    t = titulo.replace("¿", "")
    if len(t) > largo:                       # corta en ":" o "?" solo si queda algo con sentido
        corto = re.split(r"[:?]", t)[0]
        t = corto if len(corto) >= 25 else t
    t = re.sub(r'[\\/:*?"<>|¿¡!]', "", t).strip()
    while len(t) > largo and " " in t:
        t = t.rsplit(" ", 1)[0]
    return t


NUEVOS = "--nuevos" in sys.argv   # todo a una carpeta "Nuevos <lote>" para revisar a mano (sin dias)


def exportar(video, slot, d, desc, num=None, base=""):
    if NUEVOS:
        carpeta = CARPETA / f"Nuevos {base}"
        nombre = f"{num:02d} - {nombre_corto(d.get('titulo', 'Short'))}"
    else:
        carpeta = CARPETA / f"{slot:%Y-%m-%d} {horario.DIAS[slot.weekday()]}"
        nombre = f"{slot.hour:02d}h - {nombre_corto(d.get('titulo', 'Short'))}"
    carpeta.mkdir(parents=True, exist_ok=True)
    if Path(video).exists():
        shutil.copy2(video, carpeta / f"{nombre}.mp4")
    (carpeta / f"{nombre}.txt").write_text(
        f"{'HORARIO SUGERIDO' if NUEVOS else 'PUBLICAR'}: {horario.formato(slot)} (hora de Chile)\n\nTÍTULO:\n{d.get('titulo', '')}\n\n"
        f"DESCRIPCIÓN:\n{desc}\n\nCOMENTARIO FIJADO:\n{d.get('comentario_fijado', '')}\n", encoding="utf-8")
    return carpeta / f"{nombre}.mp4"

PROMPT = """Eres experto en YouTube Shorts de gaming en espanol. Para cada Short te paso su guion.
Genera para cada uno:
- "titulo": maximo 70 caracteres, con gancho y curiosidad, que incluya "GTA 6". Sin clickbait falso: debe cumplir lo que promete el video.
  El titulo ABRE una pregunta y NO da la respuesta (el dato clave se revela en el video, no en el titulo).
  Usa exclusividad o curiosidad ("antes que nadie", "esto es lo que...", "lo que nadie dijo"). Si el video trata de una
  persona famosa, su NOMBRE va AL PRINCIPIO del titulo (ej: "Rubius vio GTA 6 antes que nadie: esto es lo que conto").
- "descripcion": 1 o 2 frases cortas que resuman y enganchen, y al final una pregunta para comentarios.
- "hashtags": 5 a 8 hashtags relevantes (siempre incluye #GTA6 y #Shorts).
- "comentario_fijado": un comentario corto para fijar que invite a responder.
Responde SOLO con un array JSON, un objeto por Short y en el mismo orden:
[{"titulo": "...", "descripcion": "...", "hashtags": ["#GTA6", "#Shorts"], "comentario_fijado": "..."}]"""


PROMPT_EN = """You are a YouTube Shorts expert for a US gaming channel. For each Short I give you its script.
Generate for each one:
- "titulo": max 70 characters, curiosity hook, includes "GTA 6". No fake clickbait: it must deliver what it promises.
  The title OPENS a question and does NOT give the answer (the key fact is revealed in the video, not the title).
  Use exclusivity or curiosity ("before anyone else", "here's what...", "what nobody said"). If the video is about a
  famous person, their NAME goes FIRST in the title.
- "descripcion": 1 or 2 short punchy sentences, ending with a question for comments.
- "hashtags": 5 to 8 relevant hashtags (always #GTA6 and #Shorts).
- "comentario_fijado": a short comment to pin that invites replies.
Reply ONLY with a JSON array, one object per Short, same order:
[{"titulo": "...", "descripcion": "...", "hashtags": ["#GTA6", "#Shorts"], "comentario_fijado": "..."}]"""
if CFG.get("idioma") == "en":
    PROMPT = PROMPT_EN
if CFG.get("nicho"):        # otro canal (ej. The Rabbit Loop): mismo formato, su propio tema y hashtags
    _tags = " and ".join(CFG.get("hashtags_base", ["#Shorts"]))
    PROMPT = (PROMPT.replace("de gaming en espanol", f"sobre {CFG['nicho']}").replace("for a US gaming channel", f"about {CFG['nicho']}")
              .replace(', que incluya "GTA 6"', "").replace(', includes "GTA 6"', "")
              .replace("(siempre incluye #GTA6 y #Shorts)", f"(siempre incluye {_tags})")
              .replace("(always #GTA6 and #Shorts)", f"(always {_tags})")
              .replace('"#GTA6", "#Shorts"', ", ".join(f'"{h}"' for h in CFG.get("hashtags_base", ["#Shorts"]))))


def main():
    if len(sys.argv) < 2:
        print("Uso: python publicar.py ID_DEL_VIDEO   (ej: python publicar.py 7c28StUD66k)")
        sys.exit(1)
    base = [a for a in sys.argv[1:] if not a.startswith("--")][0]
    guiones = sorted(Path("guiones").glob(f"{base}_[0-9][0-9].json"))
    if not guiones:
        print(f"⚠️ No hay guiones para {base}")
        sys.exit(1)

    entrada = "\n\n".join(f"SHORT {i}:\n" + " ".join(json.loads(g.read_text())["frases"])
                          for i, g in enumerate(guiones, 1))
    print(f"📝 Generando títulos, descripciones y hashtags para {len(guiones)} Shorts...")
    try:                      # lecciones (titulos cortos e intensos, errores a no repetir) + historial
        import lecciones
        entrada = lecciones.bloque() + entrada
    except Exception as e:
        print("⚠️ No se pudieron cargar las lecciones:", e)
    r = subprocess.run(["claude", "-p", PROMPT], input=entrada, capture_output=True, text=True)
    try:
        datos = extraer_json(r.stdout)
    except ValueError:
        print("⚠️ Claude no devolvio JSON. Respuesta:\n", r.stdout[:500])
        sys.exit(1)

    slots = horario.calendario(len(guiones), CFG.get("idioma", "es"), CFG.get("por_dia", 2),
                               ocupados=ocupados())
    reg = registro()
    evitar = []
    for g in guiones:  # si es la version en otro idioma, que no salga el mismo dia que la original
        origen = json.loads(g.read_text()).get("adaptado_de")
        fecha = reg.get(origen, {}).get("slot") if origen else None
        evitar.append(datetime.fromisoformat(fecha).date() if fecha else None)
    orden = asignar(slots, evitar)
    por_video = [None] * len(guiones)
    for k, i in enumerate(orden):
        por_video[i] = slots[k]
    slots = por_video
    if any(evitar):
        print("🔀 Intercalado: ninguna version sale el mismo dia que la original en el otro idioma")
    md = [f"# Publicación: {base}", "",
          f"Horarios sugeridos en hora de {horario.MI_ZONA.key}, según la audiencia ({CFG.get('idioma', 'es')}). "
          "Cuando el canal tenga ~28 días, revisa YouTube Studio → Estadísticas → Audiencia.", ""]
    for i, (g, d) in enumerate(zip(guiones, datos), 1):
        guion = json.loads(g.read_text())
        desc = d.get("descripcion", "")
        if CFG.get("firma"):
            desc += "\n\n" + CFG["firma"]
        elif CANAL:
            desc += (f"\n\nFollow {CANAL} for daily GTA 6 content 🎮" if CFG.get("idioma") == "en"
                     else f"\n\nSíguenos en {CANAL} para más GTA 6 todos los días 🎮")
        desc += "\n\n" + " ".join(d.get("hashtags", []))
        md += ["---", "", f"## Short {i}", f"🎬 Archivo: salida/{base}_narrado_{i:02d}.mp4",
               f"🕒 Programar: {horario.formato(slots[i - 1])}", "",
               "### Título", "```", d.get("titulo", ""), "```", "",
               "### Descripción", "```", desc, "```", "",
               "### Comentario fijado", "```", d.get("comentario_fijado", ""), "```", ""]
        if guion.get("fuentes"):
            md += ["Fuentes verificadas (solo para ti): " + " · ".join(guion["fuentes"]), ""]
        exportar(f"salida/{base}_narrado_{i:02d}.mp4", slots[i - 1], d, desc, i, base)
        print(f"   {i}. [{horario.formato(slots[i - 1])}]  {d.get('titulo', '')}")

    for g, s in zip(guiones, slots):
        reg[g.stem] = {"canal": CANAL, "slot": s.isoformat()}
    REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=1))
    salida = Path("salida") / f"{base}_publicacion.md"
    salida.write_text("\n".join(md), encoding="utf-8")
    print(f"\n✅ Todo listo para copiar y pegar en: {salida}")
    print(f"📁 Videos + textos en: {CARPETA / f'Nuevos {base}' if NUEVOS else CARPETA}")
    try:
        import panel
        print(f"🖥️  Panel actualizado: {panel.generar()}")
    except Exception as err:
        print("(no se pudo actualizar el panel:", err, ")")


if __name__ == "__main__":
    main()
