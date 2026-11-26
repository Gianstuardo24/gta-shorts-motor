"""FICHAS: une cada video publicado con lo que tiene adentro (gancho, tema, formato, voz, hora...).

Lee <carpeta_salida>/<carpeta del canal>/(Subidos/)<día>/HHh - Título.mp4 con su .txt y su ficha
(la escribe motor/producir.py en datos/fichas/<carpeta>/<día>_<HH>h.json). Busca el mismo video en datos/metricas.db
por canal y título, y guarda todo en la tabla 'fichas'. Así el reporte semanal puede decir QUÉ funciona, no solo cuánto.

Uso (desde la carpeta del kit):   ./venv/bin/python3 metricas/fichas.py
"""
import re, json, sqlite3, difflib, unicodedata
from pathlib import Path
import os as _os, sys as _sys
from pathlib import Path as _P
_KIT = _P(__file__).resolve().parents[1]
_sys.path.insert(0, str(_KIT))
_os.chdir(_KIT)                       # datos/ y secretos/ quedan en la carpeta del kit
import kit

RAIZ = kit.salida()
BD = Path("datos/metricas.db")
FICHAS = Path("datos/fichas")
CAMPOS = ["gancho", "texto_pantalla", "tema", "micronicho", "formato", "voz", "musica", "duracion_s",
          "pregunta_cierre", "idioma", "lote"]
mapa = kit.mapa


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
    if not BD.exists():
        print("Aún no hay métricas: corre primero  ./venv/bin/python3 metricas/metricas.py")
        return
    c = sqlite3.connect(BD)
    c.execute("CREATE TABLE IF NOT EXISTS videos (id TEXT PRIMARY KEY, canal TEXT, titulo TEXT, publicado TEXT, duracion_s REAL)")
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
