"""REGLAS VIGENTES con procedencia: tabla en datos/cerebro.db, no texto libre reescrito.

Claude NO reescribe el documento: propone operaciones (mantener, ajustar, nueva, archivar) con motivo y fuentes.
Cada operacion queda en conocimiento_log (como era antes, como quedo, por que, desde que videos, con que prompt).
Lo archivado no se borra. El documento datos/estrategia/reglas_vigentes.md se arma desde la tabla (lo lee lote.py).
"""
import json, sqlite3, datetime as dt
from pathlib import Path

import ganchos as G
import procedencia as PR

CEREBRO = Path("datos/cerebro.db")
DOC = Path("datos/estrategia/reglas_vigentes.md")
SECCIONES = {"general": "Generales (todos los canales)", "gta_es": "GTA ES", "gta_en": "GTA EN", "rabbit": "Rabbit (aliens)",
             "mdm": "MDM / suerte", "cafe": "Café"}
MAX_ACTIVAS = 80

PROMPT = """Eres el editor del 'cerebro' de una fabrica de Shorts. Mantienes las REGLAS VIGENTES: reglas concretas y accionables
que el guionista aplica. Te paso (1) las reglas actuales (id | seccion | regla | evidencia | confianza) — o, si aun no hay tabla,
el documento viejo de reglas para migrarlo —, (2) el informe de hoy y (3) consejos de expertos de marketing.
Devuelve SOLO un array JSON de operaciones:
 {"op":"mantener","id":N}                                           (opcional; lo no mencionado se mantiene igual)
 {"op":"ajustar","id":N,"texto":"..","evidencia":"..","confianza":"alta|media|baja","motivo":"..","fuentes":["videoId",..]}
 {"op":"nueva","seccion":"general|gta_es|gta_en|rabbit|mdm|cafe","texto":"..","evidencia":"xN / n casos / experto",
  "confianza":"alta|media|baja","motivo":"..","fuentes":["videoId",..]}
 {"op":"archivar","id":N,"motivo":"que datos la contradicen"}
Reglas: maximo __MAX__ activas en total; una regla = 1 linea concreta (no generalidades); no dupliques (ajusta la existente);
archiva solo con evidencia en contra; sube o baja la confianza segun los datos de hoy. Nunca: urgencia falsa, promesas,
'comparte o mala suerte', material ajeno, ni REPUBLICAR el mismo video (regla fija del dueño). GTA: el juego ya salio, solo tomas reales del juego.
PROFUNDIDAD Y PERSPECTIVA: cada regla debe sostenerse en evidencia (n casos, xN), contrastarse con lo normal (si lo normal tambien
lo hace no es una regla), considerar explicaciones alternativas (tendencia, canal grande, suerte) y decir su limite en 'evidencia'."""


def abrir():
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS reglas (id INTEGER PRIMARY KEY AUTOINCREMENT, seccion TEXT, texto TEXT, evidencia TEXT,
                 confianza TEXT, estado TEXT DEFAULT 'activa', alta TEXT, actualizado TEXT, motivo_archivo TEXT)""")
    PR.migrar(c)
    return c


def _fila(c, i):
    f = c.execute("SELECT id, seccion, texto, evidencia, confianza, estado FROM reglas WHERE id=?", (i,)).fetchone()
    return dict(zip(("id", "seccion", "texto", "evidencia", "confianza", "estado"), f)) if f else None


def actuales(c):
    return "\n".join(f"{i} | {s} | {t} | {e} | {cf}" for i, s, t, e, cf in
                     c.execute("SELECT id, seccion, texto, evidencia, confianza FROM reglas WHERE estado='activa' ORDER BY seccion, id"))


def aplicar(c, ops, corrida, pv):
    ahora = dt.datetime.now().isoformat(timespec="minutes")
    n = {"nueva": 0, "ajustar": 0, "archivar": 0}
    for o in ops if isinstance(ops, list) else []:
        if not isinstance(o, dict):
            continue
        op, fuentes = o.get("op"), [f for f in (o.get("fuentes") or []) if isinstance(f, str)]
        if op == "nueva" and o.get("texto") and o.get("seccion") in SECCIONES:
            if c.execute("SELECT COUNT(*) FROM reglas WHERE estado='activa'").fetchone()[0] >= MAX_ACTIVAS:
                continue
            cur = c.execute("INSERT INTO reglas (seccion, texto, evidencia, confianza, alta, actualizado) VALUES (?,?,?,?,?,?)",
                            (o["seccion"], o["texto"], o.get("evidencia"), o.get("confianza") or "baja", ahora, ahora))
            PR.registrar(c, corrida, "regla", cur.lastrowid, "nueva", None, _fila(c, cur.lastrowid), o.get("motivo"), fuentes, pv)
            n["nueva"] += 1
        elif op in ("ajustar", "archivar") and isinstance(o.get("id"), int):
            antes = _fila(c, o["id"])
            if not antes or antes["estado"] != "activa":
                continue
            if op == "ajustar":
                c.execute("UPDATE reglas SET texto=?, evidencia=?, confianza=?, actualizado=? WHERE id=?",
                          (o.get("texto") or antes["texto"], o.get("evidencia") or antes["evidencia"],
                           o.get("confianza") or antes["confianza"], ahora, o["id"]))
            else:
                c.execute("UPDATE reglas SET estado='archivada', motivo_archivo=?, actualizado=? WHERE id=?", (o.get("motivo"), ahora, o["id"]))
            PR.registrar(c, corrida, "regla", o["id"], op, antes, _fila(c, o["id"]), o.get("motivo"), fuentes, pv)
            n[op] += 1
    c.commit()
    return n


def exportar(c, corrida):
    tocadas = {i: a for i, a in c.execute("SELECT objeto_id, accion FROM conocimiento_log WHERE corrida=? AND objeto='regla'", (corrida,))}
    L = [f"_Actualizado {dt.datetime.now():%d/%m %H:%M} · lo leen el guionista (lote.py) y Claude · historial de una regla: "
         f"`python procedencia.py regla <#>`_", ""]
    for sec, nombre in SECCIONES.items():
        filas = c.execute("SELECT id, texto, evidencia, confianza FROM reglas WHERE estado='activa' AND seccion=? ORDER BY id", (sec,)).fetchall()
        if not filas:
            continue
        L += [f"## {nombre}", ""]
        for i, t, e, cf in filas:
            marca = {"nueva": " (NUEVA)", "ajustar": " (CAMBIA)"}.get(tocadas.get(i), "")
            L.append(f"- #{i} **{t}**{marca} · {e or '—'} · confianza {cf}")
        L.append("")
    L.append(PR.cambios_md(c, corrida, "regla"))
    arch = c.execute("SELECT id, texto, motivo_archivo, actualizado FROM reglas WHERE estado='archivada' ORDER BY actualizado DESC LIMIT 15").fetchall()
    if arch:
        L += ["## 🗄️ Archivadas recientes (no se usan)", ""] + [f"- #{i} {t} — _{m}_ ({u[:10]})" for i, t, m, u in arch]
    DOC.parent.mkdir(parents=True, exist_ok=True)
    DOC.write_text("\n".join(L), encoding="utf-8")


def actualizar(texto_informe, expertos, corrida):
    c = abrir()
    prompt = PROMPT.replace("__MAX__", str(MAX_ACTIVAS))
    pv = PR.version_prompt(c, "reglas", prompt)
    base = actuales(c)
    if not base and DOC.exists():
        base = "(TABLA VACIA: migra estas reglas del documento viejo como operaciones 'nueva')\n" + DOC.read_text(encoding="utf-8")[:20000]
    entrada = (f"## (1) Reglas actuales\n{base or '(todavia no hay reglas)'}\n\n## (2) Informe de hoy\n{texto_informe[:60000]}\n\n"
               f"## (3) Expertos\n" + "\n".join(expertos))
    try:
        ops = G.extraer_json(G.claude(prompt, entrada, timeout=900))
    except Exception as e:
        print(f"   ⚠️ reglas: {e}", flush=True)
        ops = []
    n = aplicar(c, ops, corrida, pv)
    exportar(c, corrida)
    act = c.execute("SELECT COUNT(*) FROM reglas WHERE estado='activa'").fetchone()[0]
    print(f"   📏 Reglas: +{n['nueva']} nuevas · {n['ajustar']} ajustadas · {n['archivar']} archivadas · {act} activas "
          "(entran solas a los próximos guiones)", flush=True)
