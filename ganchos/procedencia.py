"""PROCEDENCIA: de donde salio cada cosa que el sistema 'cree', y como cambio en el tiempo.

Separa 3 capas (no mezclar):
  DATOS        lo que paso          -> canales, virales, virales_fotos, metricas.db
  CONOCIMIENTO lo que creemos       -> arsenal, reglas (con evidencia a favor y en contra)
  DECISIONES   lo que haremos       -> guiones, experimentos (fases siguientes)

Tabla conocimiento_log (datos/cerebro.db): cada cambio de arsenal o reglas con fecha, corrida, accion, como era ANTES,
como quedo DESPUES, motivo, videos de origen y version del prompt que lo produjo. Nada se borra: lo viejo se archiva.
Con esto se puede reconstruir cualquier conclusion sin depender de la memoria de un modelo.
"""
import json, hashlib, sqlite3, datetime as dt
from pathlib import Path

CEREBRO = Path("datos/cerebro.db")


def migrar(c):
    c.execute("""CREATE TABLE IF NOT EXISTS conocimiento_log (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha TEXT, corrida TEXT,
        objeto TEXT, objeto_id INTEGER, accion TEXT, antes TEXT, despues TEXT, motivo TEXT, fuentes TEXT, prompt TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS prompts (version TEXT PRIMARY KEY, nombre TEXT, texto TEXT, primera_vez TEXT)""")
    c.commit()


def version_prompt(c, nombre, texto):
    """Guarda el texto exacto del prompt y devuelve su version (hash corto). Si el prompt cambia, cambia la version."""
    migrar(c)
    v = nombre + "@" + hashlib.sha1(texto.encode()).hexdigest()[:8]
    c.execute("INSERT OR IGNORE INTO prompts VALUES (?,?,?,?)", (v, nombre, texto, dt.datetime.now().isoformat(timespec="minutes")))
    return v


def registrar(c, corrida, objeto, objeto_id, accion, antes=None, despues=None, motivo="", fuentes=(), prompt=""):
    migrar(c)
    j = lambda x: x if isinstance(x, str) or x is None else json.dumps(x, ensure_ascii=False)
    c.execute("""INSERT INTO conocimiento_log (fecha, corrida, objeto, objeto_id, accion, antes, despues, motivo, fuentes, prompt)
                 VALUES (?,?,?,?,?,?,?,?,?,?)""",
              (dt.datetime.now().isoformat(timespec="minutes"), corrida, objeto, objeto_id, accion, j(antes), j(despues),
               motivo or "", json.dumps([f for f in fuentes if f], ensure_ascii=False), prompt))


def cambios_md(c, corrida, objeto, titulo="Cambios de esta corrida"):
    migrar(c)
    filas = c.execute("""SELECT objeto_id, accion, despues, antes, motivo, fuentes FROM conocimiento_log
                         WHERE corrida=? AND objeto=? ORDER BY id""", (corrida, objeto)).fetchall()
    if not filas:
        return ""
    icono = {"nueva": "🆕", "refuerzo": "➕", "matiz": "✏️", "ajustar": "✏️", "contradice": "⚠️", "archivar": "🗄️",
             "relacion": "🔗", "mantener": "✔️", "confianza": "📶", "uso": "🧪"}
    L = [f"## 🧾 {titulo} ({len(filas)})", ""]
    for oid, acc, des, ant, mot, fue in filas:
        if acc in ("mantener", "uso"):
            continue
        try:
            d = json.loads(des) if des else {}
        except Exception:
            d = {"texto": des}
        nombre = (d.get("nombre") or d.get("texto") or "")[:110] if isinstance(d, dict) else str(d)[:110]
        n_f = len(json.loads(fue or "[]"))
        L.append(f"- {icono.get(acc, '•')} **{acc}** #{oid}: {nombre}" + (f" — _{mot}_" if mot else "") + (f" · {n_f} fuentes" if n_f else ""))
    return "\n".join(L) + "\n"


def historial(c, objeto, objeto_id):
    """Todo lo que le paso a una pieza o regla, en orden (para reconstruir como se llego a la conclusion)."""
    return c.execute("SELECT fecha, corrida, accion, antes, despues, motivo, fuentes, prompt FROM conocimiento_log "
                     "WHERE objeto=? AND objeto_id=? ORDER BY id", (objeto, objeto_id)).fetchall()


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:            # python procedencia.py arsenal 12   -> historial de esa pieza
        c = sqlite3.connect(CEREBRO)
        for f in historial(c, sys.argv[1], int(sys.argv[2])):
            print(" | ".join(str(x)[:200] for x in f))
