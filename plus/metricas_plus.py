"""MÉTRICAS EXTRA (22-nov): enganche real, curva de retención y de dónde llegan las vistas.

No reemplaza ni modifica metricas.py: usa sus mismos permisos (secretos/token_<canal>.json)
y su misma base (datos/metricas.db), y solo agrega tablas nuevas.

Uso (desde ~/gta-shorts):
  ./venv/bin/python3 metricas_plus.py            videos de los últimos 21 días
  ./venv/bin/python3 metricas_plus.py --dias 45  mira más atrás
  ./venv/bin/python3 metricas_plus.py --canal thedogsdecoder   solo un canal

Tablas nuevas en datos/metricas.db:
  enganche  (id, ts, vistas, enganchadas, pct_prom, dur_prom, subs, compartidos, comentarios)
            enganchadas = engagedViews: vistas que pasaron los primeros segundos.
            enganchadas / vistas ≈ "lo vio vs. lo deslizó" (YouTube cuenta como vista cada inicio de un Short).
  retencion (id, ts, punto, ver, relativo)   curva: en el punto 0.10 del video queda 'ver' (1.0 = 100 %)
  trafico   (id, ts, fuente, vistas)         SHORTS = feed de Shorts, YT_SEARCH = búsqueda, etc.
Los datos de YouTube Analytics llegan con 1-2 días de atraso: correrlo 1 vez al día basta.
"""
import sys, datetime as dt

import metricas as M


def tablas(c):
    c.executescript("""
    CREATE TABLE IF NOT EXISTS enganche (id TEXT PRIMARY KEY, ts TEXT, vistas INTEGER, enganchadas INTEGER,
        pct_prom REAL, dur_prom REAL, subs INTEGER, compartidos INTEGER, comentarios INTEGER);
    CREATE TABLE IF NOT EXISTS retencion (id TEXT, ts TEXT, punto REAL, ver REAL, relativo REAL, PRIMARY KEY (id, punto));
    CREATE TABLE IF NOT EXISTS trafico (id TEXT, ts TEXT, fuente TEXT, vistas INTEGER, PRIMARY KEY (id, fuente));
    """)


def enganche_canal(c, ya, ahora, hoy):
    """Una sola consulta por canal: todas las cifras por video."""
    base = dict(ids="channel==MINE", startDate="2026-01-01", endDate=hoy, dimensions="video", sort="-views", maxResults=200)
    try:
        r = ya.reports().query(metrics="views,engagedViews,averageViewPercentage,averageViewDuration,"
                                       "subscribersGained,shares,comments", **base).execute()
        filas = [(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]) for f in r.get("rows", [])]
    except Exception as e:                       # por si la API no acepta engagedViews con este corte
        print(f"   (engagedViews no disponible: {str(e)[:70]}) → sin enganche real")
        r = ya.reports().query(metrics="views,averageViewPercentage,averageViewDuration,subscribersGained,shares,comments",
                               **base).execute()
        filas = [(f[0], f[1], None, f[2], f[3], f[4], f[5], f[6]) for f in r.get("rows", [])]
    for vid, vistas, eng, pct, dur, subs, comp, com in filas:
        c.execute("INSERT OR REPLACE INTO enganche VALUES (?,?,?,?,?,?,?,?,?)",
                  (vid, ahora, vistas, eng, pct, dur, subs, comp, com))
    return len(filas)


def detalle_video(c, ya, vid, desde, hoy, ahora):
    """Curva de retención y fuentes de tráfico de UN video. Videos con pocas vistas pueden venir vacíos."""
    n_ret = n_tra = 0
    try:
        r = ya.reports().query(ids="channel==MINE", startDate=desde, endDate=hoy,
                               metrics="audienceWatchRatio,relativeRetentionPerformance",
                               dimensions="elapsedVideoTimeRatio", filters=f"video=={vid}").execute()
        for punto, ver, rel in r.get("rows", []):
            c.execute("INSERT OR REPLACE INTO retencion VALUES (?,?,?,?,?)", (vid, ahora, punto, ver, rel))
            n_ret += 1
    except Exception as e:
        print(f"   (retención {vid}: {str(e)[:60]})")
    try:
        r = ya.reports().query(ids="channel==MINE", startDate=desde, endDate=hoy, metrics="views",
                               dimensions="insightTrafficSourceType", filters=f"video=={vid}", sort="-views").execute()
        for fuente, vistas in r.get("rows", []):
            c.execute("INSERT OR REPLACE INTO trafico VALUES (?,?,?,?)", (vid, ahora, fuente, vistas))
            n_tra += 1
    except Exception as e:
        print(f"   (tráfico {vid}: {str(e)[:60]})")
    return n_ret, n_tra


def correr(dias=21, solo=None):
    creds = M.credenciales()
    if not creds:
        print("⚠️ No hay canales autorizados. Corre:  ./venv/bin/python3 metricas.py --autorizar")
        return
    c = M.bd()
    tablas(c)
    ahora = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    hoy = dt.date.today().isoformat()
    limite = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=dias)).isoformat()
    for canal, cr in creds.items():
        if solo and canal != solo:
            continue
        try:
            _, ya = M.servicios(cr)
            n = enganche_canal(c, ya, ahora, hoy)
            vids = c.execute("SELECT id, publicado FROM videos WHERE canal=? AND publicado>=? ORDER BY publicado",
                             (canal, limite)).fetchall()
            tr = tt = 0
            for vid, pub in vids:
                a, b = detalle_video(c, ya, vid, pub[:10], hoy, ahora)
                tr += a > 0
                tt += b > 0
            c.commit()
            print(f"📊 {canal}: enganche de {n} videos · retención {tr}/{len(vids)} · tráfico {tt}/{len(vids)}")
        except Exception as e:
            print(f"⚠️ {canal}: {str(e)[:120]}")
    M.estado({"_ultima_plus": dt.datetime.now(M.ZONA).isoformat(timespec="minutes")})


if __name__ == "__main__":
    a = sys.argv[1:]
    dias = int(a[a.index("--dias") + 1]) if "--dias" in a else 21
    solo = a[a.index("--canal") + 1] if "--canal" in a else None
    correr(dias, solo)
