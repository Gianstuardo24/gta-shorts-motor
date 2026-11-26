"""REPORTE SEMANAL (22-nov): qué funcionó la última semana en cada canal, con la regla del MANUAL §3.

Compara los videos publicados en los últimos 7 días contra los 14 días anteriores, canal por canal:
  1) % que lo vio vs. lo deslizó  (enganchadas / vistas; si aún no hay enganche, no se usa)
  2) % promedio visto
  3) suscriptores por cada 1.000 vistas
  Mejora en 2 de 3 → SE QUEDA · empeora en las 3 → NICHO DE RESERVA · lo demás → AJUSTAR.
Suma: vistas a las 24 h, rendimiento por hora de subida, mejores/peores con su gancho (de la ficha),
retención a los ~3 s, % que llega desde el feed de Shorts y un bloque de Repers (IG/TikTok/YT).

Uso (desde ~/gta-shorts):
  ./venv/bin/python3 reporte_semanal.py                    semana que termina hoy
  ./venv/bin/python3 reporte_semanal.py --hasta 2026-11-29 semana que termina ese día
  ./venv/bin/python3 reporte_semanal.py --sin-repers       no refresca ni muestra Repers
Sale en: analisis/reporte_AAAA-MM-DD.md (y un resumen corto en la terminal).
Antes conviene correr:  metricas_plus.py  y  fichas.py  (lo hace solo programar_reporte.sh).
"""
import sys, json, sqlite3, statistics as st, datetime as dt
from pathlib import Path

import metricas as M

SALIDA = Path("analisis")
NOMBRES = {"theviceversegg": "GTA EN", "viceversogg": "GTA ES", "therabbitloop": "Rabbit Loop",
           "mdollarmistake": "MDM", "chichibitstv": "Café (ChiChibits)", "thedogsdecoder": "Perros",
           "thecatsdecoder": "Gatos"}
MIN_N = 3          # menos videos que esto en un lado → no se decide, se informa
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]


def med(xs):
    xs = [x for x in xs if x is not None]
    return st.median(xs) if xs else None


def f(x, d=1, pct=False):
    if x is None:
        return "–"
    return f"{x:.{d}f}{' %' if pct else ''}" if isinstance(x, float) else f"{x}{' %' if pct else ''}"


def existe(c, tabla):
    return c.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (tabla,)).fetchone() is not None


def videos(c, desde, hasta, ahora):
    """Todos los videos publicados entre desde y hasta (UTC), con sus cifras."""
    hay = {t: existe(c, t) for t in ("enganche", "retencion", "trafico", "fichas")}
    out = []
    for vid, canal, titulo, pub, dur in c.execute("SELECT * FROM videos").fetchall():
        p = dt.datetime.fromisoformat(pub.replace("Z", "+00:00"))
        if not (desde <= p < hasta):
            continue
        fotos = [(dt.datetime.fromisoformat(t), v) for t, v in
                 c.execute("SELECT ts, vistas FROM fotos WHERE id=? ORDER BY ts", (vid,))]
        a = c.execute("SELECT vistas, pct_prom, subs FROM analytics WHERE id=?", (vid,)).fetchone()
        e = c.execute("SELECT vistas, enganchadas, pct_prom, subs FROM enganche WHERE id=?", (vid,)).fetchone() \
            if hay["enganche"] else None
        vistas_a = (e[0] if e and e[0] else None) or (a[0] if a and a[0] else None) or (fotos[-1][1] if fotos else 0)
        pct = (e[2] if e and e[2] is not None else None) or (a[1] if a else None)
        subs = (e[3] if e and e[3] is not None else None)
        if subs is None and a:
            subs = a[2]
        v = {"id": vid, "canal": canal, "titulo": titulo, "dur": dur,
             "local": p.astimezone(M.ZONA), "edad_h": (ahora - p).total_seconds() / 3600,
             "vistas": fotos[-1][1] if fotos else (vistas_a or 0),
             "v24": M.vistas_a(fotos, p, 24),
             "pct": pct,
             "eng": (100 * e[1] / e[0]) if e and e[0] and e[1] is not None else None,
             "subs1k": (1000 * subs / vistas_a) if subs is not None and vistas_a else None,
             "ret3": None, "feed": None, "gancho": None, "formato": None, "voz": None}
        if hay["retencion"] and dur:
            pts = c.execute("SELECT punto, ver FROM retencion WHERE id=? ORDER BY punto", (vid,)).fetchall()
            if pts:
                obj = min(1.0, 3.0 / dur)
                v["ret3"] = 100 * min(pts, key=lambda x: abs(x[0] - obj))[1]
        if hay["trafico"]:
            tr = dict(c.execute("SELECT fuente, vistas FROM trafico WHERE id=?", (vid,)).fetchall())
            if sum(tr.values()):
                v["feed"] = 100 * tr.get("SHORTS", 0) / sum(tr.values())
        if hay["fichas"]:
            fi = c.execute("SELECT gancho, formato, voz FROM fichas WHERE id=?", (vid,)).fetchone()
            if fi:
                v["gancho"], v["formato"], v["voz"] = fi
        out.append(v)
    return out


def decidir(sem, base):
    """Regla del MANUAL §3 con las 3 cifras. Devuelve (decision, detalle por cifra)."""
    detalle, mejor, peor, usadas = [], 0, 0, 0
    for clave, nombre in (("eng", "% lo vio vs. deslizó"), ("pct", "% promedio visto"), ("subs1k", "subs / 1.000 vistas")):
        a, b = med([v[clave] for v in sem]), med([v[clave] for v in base])
        if a is None or b is None:
            detalle.append((nombre, a, b, "sin dato"))
            continue
        usadas += 1
        if a > b * 1.05:
            mejor += 1; flecha = "▲ mejora"
        elif a < b * 0.95:
            peor += 1; flecha = "▼ empeora"
        else:
            flecha = "= igual"
        detalle.append((nombre, a, b, flecha))
    if len(sem) < MIN_N:
        return "⏳ POCOS VIDEOS (se decide la próxima semana)", detalle
    if len(base) < MIN_N:
        return "🆕 PRIMERA SEMANA (queda como base)", detalle
    if usadas < 2:
        return "SIN DATOS (faltan cifras de YouTube Analytics)", detalle
    if mejor >= 2:
        return "✅ SE QUEDA", detalle
    if peor == usadas:
        return "🔁 NICHO DE RESERVA", detalle
    return "🛠️ AJUSTAR", detalle


def repers(hasta, refrescar=True):
    """Bloque Repers desde datos/redes_snapshot.json (lo trae repers_estudio.refrescar, de solo lectura)."""
    snap = {}
    try:
        import repers_estudio as R
        snap = R.snapshot(forzar=refrescar)
    except Exception:
        p = Path("datos/redes_snapshot.json")
        snap = json.loads(p.read_text()) if p.exists() else {}
    posts = snap.get("posts") or []
    if not posts:
        return ["_Sin datos de Repers (no se encontró datos/redes_snapshot.json)._"]
    l = [f"Datos al **{(snap.get('sincronizado') or '?')[:16].replace('T', ' ')} UTC**.", "",
         "| Cuenta | Seguidores | Posts 7 d | Vistas (mediana) | Seg. vistos (mediana) | Compartidos + guardados | Mejor post |",
         "|---|---|---|---|---|---|---|"]
    seg = {(c["plataforma"], c["usuario"]): c.get("seguidores") for c in snap.get("cuentas", [])}
    desde = hasta - dt.timedelta(days=7)
    grupos = {}
    for p in posts:
        try:
            t = dt.datetime.fromisoformat(p["publicado_en"].replace("Z", "+00:00"))
        except Exception:
            continue
        if desde <= t < hasta:
            grupos.setdefault((p["plataforma"], p["usuario"]), []).append(p)
    for (plat, user), ps in sorted(grupos.items()):
        u = [p.get("ultima") or {} for p in ps]
        mejor = max(ps, key=lambda p: (p.get("ultima") or {}).get("vistas") or 0)
        cap = (mejor.get("caption") or "").replace("\n", " ").replace("|", "/")[:45]
        l.append(f"| {plat} {user} | {seg.get((plat, user), '–')} | {len(ps)} | {f(med([x.get('vistas') for x in u]), 0)} | "
                 f"{f(med([x.get('tiempo_prom_vista_s') for x in u]))} | "
                 f"{sum((x.get('compartidos') or 0) + (x.get('guardados') or 0) for x in u)} | "
                 f"{(mejor.get('ultima') or {}).get('vistas', '–')} · {cap} |")
    if not grupos:
        l.append("| – | – | 0 | – | – | – | sin posts esta semana en el snapshot |")
    return l


def reporte(hasta_local, con_repers=True):
    c = M.bd()
    ahora = dt.datetime.now(dt.timezone.utc)
    hasta = min(ahora, hasta_local.astimezone(dt.timezone.utc))
    ini_sem, ini_base = hasta - dt.timedelta(days=7), hasta - dt.timedelta(days=21)
    todos = videos(c, ini_base, hasta, ahora)
    canales = sorted({v["canal"] for v in todos}, key=lambda k: list(NOMBRES).index(k) if k in NOMBRES else 99)
    fecha = hasta.astimezone(M.ZONA).strftime("%Y-%m-%d")
    L = [f"# Reporte semanal · {fecha}", "",
         f"Semana: **{ini_sem.astimezone(M.ZONA):%d/%m} → {hasta.astimezone(M.ZONA):%d/%m}** · "
         f"comparada con los 14 días anteriores. Regla del MANUAL §3 (mejora 2 de 3 → se queda; empeora las 3 → reserva).",
         "", "> Las cifras de YouTube Analytics llegan con 1–2 días de atraso: los videos de ayer y hoy aún no cuentan bien.", ""]
    resumen = ["", "## Resumen", "", "| Canal | Videos (sem / base) | Vistas 24 h (mediana) | Decisión |", "|---|---|---|---|"]
    for k in canales:
        sem = [v for v in todos if v["canal"] == k and v["local"] >= ini_sem.astimezone(M.ZONA)]
        base = [v for v in todos if v["canal"] == k and v["local"] < ini_sem.astimezone(M.ZONA)]
        decision, det = decidir(sem, base)
        nombre = NOMBRES.get(k, k)
        resumen.append(f"| {nombre} | {len(sem)} / {len(base)} | {f(med([v['v24'] for v in sem]), 0)} | {decision} |")
        L += [f"## {nombre}", "", f"**Decisión: {decision}**", "",
              "| Cifra | Esta semana | 14 días antes | |", "|---|---|---|---|"]
        for nom, a, b, fl in det:
            L.append(f"| {nom} | {f(a)} | {f(b)} | {fl} |")
        L.append(f"| vistas a las 24 h | {f(med([v['v24'] for v in sem]), 0)} | {f(med([v['v24'] for v in base]), 0)} | |")
        r3, fd = med([v["ret3"] for v in sem]), med([v["feed"] for v in sem])
        if r3 is not None or fd is not None:
            L.append(f"| quedan a los ~3 s | {f(r3, pct=True)} | {f(med([v['ret3'] for v in base]), pct=True)} | |")
            L.append(f"| vistas desde el feed de Shorts | {f(fd, pct=True)} | {f(med([v['feed'] for v in base]), pct=True)} | |")
        horas = {}
        for v in sem + base:
            if v["v24"] is not None:
                horas.setdefault(v["local"].hour, []).append(v["v24"])
        if horas:
            L += ["", "**Por hora de subida** (mediana de vistas a las 24 h, 3 semanas): " +
                  " · ".join(f"{h:02d}h → {f(med(xs), 0)} (n={len(xs)})" for h, xs in sorted(horas.items()))]
        orden = sorted([v for v in sem if v["v24"] is not None], key=lambda v: -v["v24"])
        if orden:
            L += ["", "| | Video | 24 h | % visto | Lo vio % | Gancho |", "|---|---|---|---|---|---|"]
            sel = orden[:3] + [v for v in orden[-2:] if v not in orden[:3]]
            for i, v in enumerate(sel):
                tag = "🔝" if i < min(3, len(orden)) else "⬇️"
                g = (v["gancho"] or "–").replace("|", "/").replace("\n", " ")[:60]
                L.append(f"| {tag} | {DIAS[v['local'].weekday()]} {v['local']:%d %Hh} · {v['titulo'][:45]} | {v['v24']} | {f(v['pct'])} | {f(v['eng'])} | {g} |")
        pend = [v for v in sem if v["v24"] is None]
        if pend:
            L.append(f"\n_{len(pend)} video(s) aún sin 24 h medidas._")
        L.append("")
    # qué funciona según la ficha (todos los canales juntos)
    con_ficha = [v for v in todos if v["formato"] and v["v24"] is not None]
    if len(con_ficha) >= 6:
        L += ["## Según la ficha (todos los canales, 3 semanas)", ""]
        for campo, nombre in (("formato", "Formato"), ("voz", "Voz")):
            g = {}
            for v in con_ficha:
                g.setdefault(v[campo], []).append(v["v24"])
            L.append(f"- **{nombre}:** " + " · ".join(f"{k} → {f(med(xs), 0)} (n={len(xs)})" for k, xs in sorted(g.items())))
        L.append("")
    if con_repers:
        L += ["## Repers (IG / TikTok / YouTube)", ""] + repers(hasta) + [""]
    L[5:5] = resumen + [""]
    SALIDA.mkdir(exist_ok=True)
    out = SALIDA / f"reporte_{fecha}.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(resumen[2:]))
    print(f"\n📄 {out}")
    return out


if __name__ == "__main__":
    hasta = dt.datetime.now(M.ZONA)
    if "--hasta" in sys.argv:
        d = dt.date.fromisoformat(sys.argv[sys.argv.index("--hasta") + 1])
        hasta = dt.datetime(d.year, d.month, d.day, 23, 59, tzinfo=M.ZONA)
    reporte(hasta, con_repers="--sin-repers" not in sys.argv)
