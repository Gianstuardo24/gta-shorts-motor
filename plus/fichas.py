"""FICHAS (22-nov): une cada video publicado con lo que tiene adentro (gancho, tema, formato, voz, hora...).

Lee ~/Desktop/YouTube/<carpeta>/(Subidos/)<día>/HHh - Título.mp4 con su .txt y, si existe, su ficha
(la ficha la escribe la fábrica al hacer el video, en datos/fichas/<carpeta>/<día>_<HH>h.json,
así no se pierde cuando el Estudio mueve el video a Subidos). Busca el mismo video en datos/metricas.db por canal y
título, y guarda todo en la tabla 'fichas'. Así el reporte semanal puede decir QUÉ funciona, no solo cuánto.

Uso (desde ~/gta-shorts):   ./venv/bin/python3 fichas.py
Carpeta → canal: datos/mapa_canales.json (se crea solo con los canales actuales; edítalo si agregas uno).
"""
import re, json, sqlite3, difflib, unicodedata
from pathlib import Path

RAIZ = Path("~/Desktop/YouTube").expanduser()
BD = Path("datos/metricas.db")
MAPA = Path("datos/mapa_canales.json")
FICHAS = Path("datos/fichas")
MAPA_BASE = {"TheViceVerseGG": "theviceversegg", "ViceVersoGG": "viceversogg", "TheRabbitLoop": "therabbitloop",
             "MillionDollarMistake": "mdollarmistake", "ChiChibitsTV": "chichibitstv",
             "DogDecoded": "thedogsdecoder", "CatDecoded": "thecatsdecoder"}
CAMPOS = ["gancho", "texto_pantalla", "tema", "micronicho", "formato", "voz", "musica", "duracion_s",
          "pregunta_cierre", "idioma", "lote"]


def mapa():
    if not MAPA.exists():
        MAPA.parent.mkdir(exist_ok=True)
        MAPA.write_text(json.dumps(MAPA_BASE, ensure_ascii=False, indent=1))
    return json.loads(MAPA.read_text())


def norm(t):
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    t = re.sub(r"[^a-z0-9$ ]+", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def leer_txt(p):
    """Devuelve (titulo, publicar) desde el .txt de la fábrica."""
    if not p.exists():
        return None, None
    s = p.read_text(errors="ignore")
    m = re.search(r"T[IÍ]TULO:\s*\n(.+)", s)
    pub = re.search(r"PUBLICAR:\s*(.+?)\s*\(", s)
    return (m.group(1).strip() if m else None), (pub.group(1).strip() if pub else None)


def correr():
    c = sqlite3.connect(BD)
    c.execute("CREATE TABLE IF NOT EXISTS fichas (ruta TEXT PRIMARY KEY, id TEXT, canal TEXT, dia TEXT, hora INTEGER, titulo TEXT, "
              + ", ".join(f"{k} TEXT" for k in CAMPOS) + ")")
    vids = {}
    for vid, canal, titulo in c.execute("SELECT id, canal, titulo FROM videos"):
        vids.setdefault(canal, []).append((vid, titulo, norm(titulo)))
    total = unidos = con_ficha = 0
    for carpeta, canal in mapa().items():
        base = RAIZ / carpeta
        for mp4 in sorted(base.glob("**/*.mp4")) if base.exists() else []:
            if any(x.startswith("_") for x in mp4.relative_to(base).parts[:-1]):
                continue                                   # _eliminados, _reemplazados, etc.
            dia = re.match(r"(\d{4}-\d{2}-\d{2})", mp4.parent.name)
            hh = re.match(r"(\d{2})h - (.+)", mp4.stem)
            if not (dia and hh):
                continue
            titulo, _ = leer_txt(mp4.with_suffix(".txt"))
            titulo = titulo or hh.group(2)
            fj = FICHAS / carpeta / f"{dia.group(1)}_{hh.group(1)}h.json"
            f = json.loads(fj.read_text()) if fj.exists() else {}
            con_ficha += bool(f)
            vid, n = None, norm(titulo)
            cand = vids.get(canal, [])
            exactos = [v for v in cand if v[2] == n]
            if exactos:
                vid = exactos[0][0]
            elif cand:
                mejor = max(cand, key=lambda v: difflib.SequenceMatcher(None, v[2], n).ratio())
                if difflib.SequenceMatcher(None, mejor[2], n).ratio() >= 0.8:
                    vid = mejor[0]
            unidos += bool(vid)
            total += 1
            c.execute(f"INSERT OR REPLACE INTO fichas VALUES ({','.join('?' * (6 + len(CAMPOS)))})",
                      (str(mp4.relative_to(RAIZ)), vid, canal, dia.group(1), int(hh.group(1)), titulo,
                       *[None if f.get(k) is None else str(f.get(k)) for k in CAMPOS]))
    c.commit()
    print(f"🗂️  {total} videos en carpetas · {unidos} unidos a sus métricas · {con_ficha} con ficha completa")


if __name__ == "__main__":
    correr()
