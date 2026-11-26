"""LABORATORIO DE EXPERIMENTOS: pasar de 'creemos' a 'comprobado'.

Un experimento = UNA variable (ej: tipo de hook), 2 variantes (A = control, B = la idea nueva), en UN canal.
Diseño para nuestro volumen (pocos videos, mucho ruido):
  - minimo 6 videos por variante (replicas). 2 videos no prueban nada.
  - asignacion ALTERNADA (A, B, A, B...) para repartir horarios y dias por igual.
  - metrica principal: vistas a 24 h RELATIVAS a la mediana del canal en los 14 dias previos (corrige que el canal crezca o caiga).
    secundaria: % visto.
  - decision: permutacion (10.000) sobre log(relativo) + tamaño del efecto (mediana B / mediana A).
      B gana si efecto >= 1.25 y p < 0.10 · A gana si efecto <= 0.80 y p < 0.10 · si no: sin diferencia clara.
  - 1 experimento activo por canal a la vez (para poder atribuir el resultado).
  - SIEMPRE se registran las limitaciones (n, temas distintos, horario, novedad del canal).
Si el experimento esta ligado a una pieza del arsenal: B gana -> la pieza queda 🧪✅ COMPROBADA; A gana -> 🧪❌ (con historial).
El Director propone experimentos (quedan 'propuesto'); Tao los activa.

Uso:  python laboratorio.py                 evalua los activos y actualiza el informe
      python laboratorio.py activar 3       activa el experimento #3      · descartar 3 · cerrar 3
      python laboratorio.py nuevo           (interactivo) crear uno a mano
Los guiones llevan "exp_ab": {"id": N, "variante": "A"|"B"} (el campo "experimento" de texto libre se respeta) (lote.py lo asigna solo; a mano: python laboratorio.py asignar <guion.json> <id>)
Salida: Estudio › 🧠 Director › 🧪 Laboratorio (datos/estrategia/9-laboratorio.md) + tablas experimentos/exp_videos en datos/cerebro.db
"""
import sys, json, math, random, sqlite3, statistics, datetime as dt
from pathlib import Path

import ganchos as G

CEREBRO = Path("datos/cerebro.db")
DOC = Path("datos/estrategia/9-laboratorio.md")
CANALES = {"gta_es": "viceversogg", "gta_en": "theviceversegg", "rabbit": "therabbitloop", "mdm": "mdollarmistake", "cafe": "cafe"}
REPLICAS = 6


def abrir():
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS experimentos (id INTEGER PRIMARY KEY AUTOINCREMENT, creado TEXT, canal TEXT, hipotesis TEXT,
        variable TEXT, variante_a TEXT, variante_b TEXT, metrica TEXT, replicas INTEGER, criterio TEXT, pieza_arsenal INTEGER,
        origen TEXT, estado TEXT DEFAULT 'propuesto', activado TEXT, cerrado TEXT, resultado TEXT, efecto REAL, p REAL,
        conclusion TEXT, limitaciones TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS exp_videos (exp_id INTEGER, guion TEXT, variante TEXT, video_id TEXT, titulo TEXT,
        publicado TEXT, vistas_24h INTEGER, mediana_ref REAL, relativo REAL, pct_visto REAL, PRIMARY KEY (exp_id, guion))""")
    cols = {r[1] for r in c.execute("PRAGMA table_info(arsenal)")} if c.execute(
        "SELECT name FROM sqlite_master WHERE name='arsenal'").fetchone() else set()
    if cols and "comprobada" not in cols:
        c.execute("ALTER TABLE arsenal ADD COLUMN comprobada TEXT")
    c.commit()
    return c


# ---------------- crear / activar ----------------
def importar(propuestas, origen="director"):
    """Experimentos que propone el Director -> 'propuesto' (sin duplicar hipotesis)."""
    c = abrir()
    ya = {r[0].strip().lower() for r in c.execute("SELECT hipotesis FROM experimentos")}
    n = 0
    for x in propuestas or []:
        h = (x.get("hipotesis") or "").strip()
        if not h or h.lower() in ya:
            continue
        canal = x.get("canal") if x.get("canal") in CANALES else next((k for k in CANALES if k in str(x.get("canal", "")).lower()), "gta_es")
        c.execute("""INSERT INTO experimentos (creado, canal, hipotesis, variable, variante_a, variante_b, metrica, replicas, criterio,
                     pieza_arsenal, origen) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                  (dt.datetime.now().isoformat(timespec="minutes"), canal, h, x.get("variable"), x.get("variante_a") or "control (como hacemos hoy)",
                   x.get("variante_b") or x.get("variable"), x.get("metrica") or "vistas 24 h relativas a la mediana del canal",
                   max(int(x.get("replicas") or REPLICAS), REPLICAS), x.get("criterio"), x.get("pieza_arsenal"), origen))
        n += 1
    c.commit()
    return n


def activar(i):
    c = abrir()
    canal = c.execute("SELECT canal FROM experimentos WHERE id=?", (i,)).fetchone()
    if not canal:
        sys.exit(f"No existe el experimento #{i}")
    otro = c.execute("SELECT id FROM experimentos WHERE canal=? AND estado='activo' AND id!=?", (canal[0], i)).fetchone()
    if otro:
        sys.exit(f"⛔ {canal[0]} ya tiene el experimento #{otro[0]} activo. Ciérralo o descártalo antes (1 por canal).")
    c.execute("UPDATE experimentos SET estado='activo', activado=? WHERE id=?", (dt.datetime.now().isoformat(timespec="minutes"), i))
    c.commit()
    print(f"🧪 Experimento #{i} activo en {canal[0]}. Los próximos guiones de ese canal alternan A/B.")


def activo(canal_perfil):
    c = abrir()
    f = c.execute("SELECT id, hipotesis, variable, variante_a, variante_b FROM experimentos WHERE canal=? AND estado='activo'",
                  (canal_perfil,)).fetchone()
    return dict(zip(("id", "hipotesis", "variable", "variante_a", "variante_b"), f)) if f else None


def siguiente_variante(exp_id):
    c = abrir()
    asignados = []
    for g in Path("guiones").glob("*.json"):
        try:
            ex = json.loads(g.read_text()).get("exp_ab") or {}
        except Exception:
            continue
        if ex.get("id") == exp_id:
            asignados.append(ex.get("variante"))
    return "A" if asignados.count("A") <= asignados.count("B") else "B"


def asignar(archivo, exp_id, variante=None):
    p = Path(archivo)
    g = json.loads(p.read_text())
    variante = variante or siguiente_variante(exp_id)
    g["exp_ab"] = {"id": int(exp_id), "variante": variante}
    p.write_text(json.dumps(g, ensure_ascii=False, indent=2))
    return variante


def instruccion_guionista(canal_perfil, n_guiones):
    """Texto para lote.py: que guion usa que variante (el codigo asigna igual al guardar)."""
    e = activo(canal_perfil)
    if not e:
        return "", None
    orden = []
    v = siguiente_variante(e["id"])
    for k in range(1, n_guiones + 1):
        orden.append((k, v))
        v = "B" if v == "A" else "A"
    txt = (f"EXPERIMENTO ACTIVO #{e['id']} ({e['hipotesis']}). Variable: {e['variable']}. "
           f"Variante A: {e['variante_a']}. Variante B: {e['variante_b']}. "
           + " · ".join(f"guion {k} = {v}" for k, v in orden) + ". Cambia SOLO esa variable; todo lo demas igual de bien hecho.\n\n")
    return txt, (e["id"], orden)


# ---------------- evaluar ----------------
def permutacion(a, b, n=10000):
    """p bilateral de la diferencia de medianas de log(relativo)."""
    la, lb = [math.log(max(x, 1e-3)) for x in a], [math.log(max(x, 1e-3)) for x in b]
    obs = abs(statistics.median(lb) - statistics.median(la))
    todo, na, cnt = la + lb, len(la), 0
    rnd = random.Random(42)
    for _ in range(n):
        rnd.shuffle(todo)
        if abs(statistics.median(todo[na:]) - statistics.median(todo[:na])) >= obs - 1e-12:
            cnt += 1
    return (cnt + 1) / (n + 1)


def resumen():
    """Para el Director: estado del laboratorio en pocas lineas."""
    c = abrir()
    L = []
    for i, canal, h, est, res, ef, p in c.execute("SELECT id, canal, hipotesis, estado, resultado, efecto, p FROM experimentos ORDER BY id DESC LIMIT 15"):
        na = c.execute("SELECT COUNT(*) FROM exp_videos WHERE exp_id=? AND variante='A'", (i,)).fetchone()[0]
        nb = c.execute("SELECT COUNT(*) FROM exp_videos WHERE exp_id=? AND variante='B'", (i,)).fetchone()[0]
        L.append(f"- #{i} [{canal}] {est}: {h} · A {na} / B {nb}" + (f" · {res} (x{ef}, p={p})" if res else ""))
    return "\n".join(L) or "(sin experimentos todavia)"


def evaluar():
    c = abrir()
    pro = G.propios()
    por_titulo = {p["titulo"]: p for p in pro}
    # 1) registrar videos de guiones con experimento
    for g in Path("guiones").glob("*.json"):
        try:
            d = json.loads(g.read_text())
        except Exception:
            continue
        ex = d.get("exp_ab") or {}
        p = por_titulo.get(d.get("titulo"))
        if not ex.get("id") or not p or p.get("vistas_24h") is None:
            continue
        ref = [q["vistas_24h"] for q in pro if q["canal"] == p["canal"] and q["id"] != p["id"] and q.get("vistas_24h") is not None
               and 0 < (q["horas"] - p["horas"]) <= 14 * 24]
        med = statistics.median(ref) if len(ref) >= 3 else statistics.median(
            [q["vistas_24h"] for q in pro if q["canal"] == p["canal"] and q.get("vistas_24h") is not None])
        c.execute("INSERT OR REPLACE INTO exp_videos VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (ex["id"], g.stem, ex.get("variante"), p["id"], p["titulo"], None, p["vistas_24h"], med,
                   round(p["vistas_24h"] / max(med, 1), 3), p.get("pct_visto")))
    c.commit()
    # 2) decidir los que llegaron a las replicas
    for i, canal, h, rep, pieza in c.execute("SELECT id, canal, hipotesis, replicas, pieza_arsenal FROM experimentos WHERE estado='activo'").fetchall():
        a = [r[0] for r in c.execute("SELECT relativo FROM exp_videos WHERE exp_id=? AND variante='A'", (i,))]
        b = [r[0] for r in c.execute("SELECT relativo FROM exp_videos WHERE exp_id=? AND variante='B'", (i,))]
        if len(a) < rep or len(b) < rep:
            continue
        ef = statistics.median(b) / max(statistics.median(a), 1e-6)
        p = permutacion(a, b)
        res = "B gana" if ef >= 1.25 and p < 0.10 else "A gana" if ef <= 0.80 and p < 0.10 else "sin diferencia clara"
        lim = (f"n={len(a)}+{len(b)} videos; cada video trata un tema distinto (el tema tambien influye); horarios alternados A/B; "
               f"vale para {canal}: no se generaliza a otros canales sin repetirlo alli")
        concl = {"B gana": f"La variante B mejora las vistas a 24 h relativas ×{ef:.2f} (p={p:.3f}).",
                 "A gana": f"La variante B empeora: ×{ef:.2f} (p={p:.3f}). Mantener A.",
                 "sin diferencia clara": f"Efecto ×{ef:.2f} con p={p:.3f}: no alcanza para concluir. Se puede extender con más réplicas."}[res]
        c.execute("UPDATE experimentos SET estado='concluido', cerrado=?, resultado=?, efecto=?, p=?, conclusion=?, limitaciones=? WHERE id=?",
                  (dt.datetime.now().isoformat(timespec="minutes"), res, round(ef, 3), round(p, 4), concl, lim, i))
        if pieza and res != "sin diferencia clara":
            import procedencia as PR
            antes = c.execute("SELECT comprobada FROM arsenal WHERE id=?", (pieza,)).fetchone()
            nuevo = "si" if res == "B gana" else "no"
            c.execute("UPDATE arsenal SET comprobada=? WHERE id=?", (nuevo, pieza))
            PR.registrar(c, f"experimento#{i}", "arsenal", pieza, "comprobada" if nuevo == "si" else "contradice",
                         {"comprobada": antes[0] if antes else None}, {"comprobada": nuevo}, concl,
                         [r[0] for r in c.execute("SELECT video_id FROM exp_videos WHERE exp_id=?", (i,))], "laboratorio")
        print(f"🧪 #{i} concluido: {res} · {concl}")
    c.commit()
    exportar(c)


def exportar(c):
    ic = {"propuesto": "💡", "activo": "🧪", "concluido": "✅", "descartado": "🗑️"}
    L = [f"# 🧪 Laboratorio — {dt.datetime.now():%d/%m %H:%M}", "",
         f"_1 variable · A (control) vs B · mínimo {REPLICAS} videos por variante · alternado A/B · métrica: vistas 24 h relativas a la "
         "mediana del canal · decisión por permutación + tamaño del efecto · 1 experimento activo por canal_", ""]
    for estado in ("activo", "propuesto", "concluido", "descartado"):
        filas = c.execute("""SELECT id, canal, hipotesis, variable, variante_a, variante_b, replicas, criterio, pieza_arsenal, resultado,
                             efecto, p, conclusion, limitaciones FROM experimentos WHERE estado=? ORDER BY id DESC""", (estado,)).fetchall()
        if not filas:
            continue
        L += [f"## {ic[estado]} {estado.capitalize()}s ({len(filas)})", ""]
        for i, canal, h, var, va, vb, rep, cr, pz, res, ef, p, con, lim in filas:
            na = c.execute("SELECT COUNT(*) FROM exp_videos WHERE exp_id=? AND variante='A'", (i,)).fetchone()[0]
            nb = c.execute("SELECT COUNT(*) FROM exp_videos WHERE exp_id=? AND variante='B'", (i,)).fetchone()[0]
            L.append(f"### #{i} · {canal} · {h}")
            L.append(f"- **Variable:** {var} · **A:** {va} · **B:** {vb}" + (f" · pieza del arsenal #{pz}" if pz else ""))
            L.append(f"- **Progreso:** A {na}/{rep} · B {nb}/{rep}" + (f" · criterio: {cr}" if cr else ""))
            if res:
                L.append(f"- **Resultado:** {res} — {con}")
                L.append(f"- **Limitaciones:** {lim}")
            if estado == "propuesto":
                L.append(f"- Para activarlo: escribe {i} arriba y toca **Activar**")
            L.append("")
    if len(L) <= 4:
        L.append("_Todavía no hay experimentos. El 🧠 Director los propone; también puedes crear uno con `python laboratorio.py nuevo`._")
    DOC.parent.mkdir(parents=True, exist_ok=True)
    DOC.write_text("\n".join(L), encoding="utf-8")


def nuevo():
    x = {k: input(f"{k}: ").strip() for k in ("canal (gta_es/gta_en/rabbit/mdm/cafe)", "hipotesis", "variable", "variante_a", "variante_b")}
    x = {k.split(" ")[0]: v for k, v in x.items()}
    print(f"Creado: {importar([x], 'manual')} experimento(s). Actívalo con: python laboratorio.py activar <id>")


def main():
    a = sys.argv[1:]
    if not a:
        return evaluar()
    if a[0] == "activar":
        activar(int(a[1]))
    elif a[0] in ("descartar", "cerrar"):
        c = abrir()
        c.execute("UPDATE experimentos SET estado=?, cerrado=? WHERE id=?",
                  ("descartado" if a[0] == "descartar" else "concluido", dt.datetime.now().isoformat(timespec="minutes"), int(a[1])))
        c.commit()
    elif a[0] == "asignar":
        print("variante", asignar(a[1], int(a[2]), a[3] if len(a) > 3 else None))
    elif a[0] == "nuevo":
        nuevo()
    exportar(abrir())


if __name__ == "__main__":
    main()
