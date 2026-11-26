"""METRICAS de tus canales (YouTube Data API + YouTube Analytics API) para saber QUE funciona y A QUE HORA.

Uso (desde la carpeta del kit):
  ./venv/bin/python3 metricas/metricas.py --autorizar   abre Google para dar permiso a UN canal (una vez por canal)
  ./venv/bin/python3 metricas/metricas.py               toma una "foto" de las métricas de todos los canales autorizados
  ./venv/bin/python3 metricas/metricas.py --resumen     muestra el análisis en la terminal
  bash metricas/programar.sh                            la foto sola cada hora + extras diarios + reporte los domingos

Secretos (NUNCA se suben ni se pegan en el chat):  secretos/oauth_cliente.json, secretos/youtube.json, secretos/token_<canal>.json
Datos: datos/metricas.db
"""
import sys, json, sqlite3, datetime as dt
import os as _os, sys as _sys
from pathlib import Path as _P
_KIT = _P(__file__).resolve().parents[1]
_sys.path.insert(0, str(_KIT))
_os.chdir(_KIT)                       # datos/ y secretos/ quedan en la carpeta del kit
import kit
from pathlib import Path
from zoneinfo import ZoneInfo

SECRETOS = Path("secretos")
CLIENTE = SECRETOS / "oauth_cliente.json"
BD = Path("datos/metricas.db")
ZONA = kit.zona()
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/yt-analytics.readonly"]
EDADES = (2, 6, 24, 48)                       # horas a las que se comparan los videos
ESTADO = Path("datos/metricas_estado.json")   # canales autorizados / que piden reautorizar


# ---------------- base de datos ----------------
def bd():
    BD.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(BD)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS videos (id TEXT PRIMARY KEY, canal TEXT, titulo TEXT, publicado TEXT, duracion_s REAL);
    CREATE TABLE IF NOT EXISTS fotos (id TEXT, ts TEXT, vistas INTEGER, likes INTEGER, comentarios INTEGER);
    CREATE INDEX IF NOT EXISTS fotos_id ON fotos(id, ts);
    CREATE TABLE IF NOT EXISTS analytics (id TEXT PRIMARY KEY, ts TEXT, vistas INTEGER, minutos REAL, dur_prom REAL,
        pct_prom REAL, likes INTEGER, compartidos INTEGER, subs INTEGER);
    """)
    return c


def estado(cambios=None):
    d = json.loads(ESTADO.read_text()) if ESTADO.exists() else {}
    if cambios:
        d.update(cambios)
        ESTADO.parent.mkdir(exist_ok=True)
        ESTADO.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    return d


# ---------------- Google ----------------
def servicios(creds):
    from googleapiclient.discovery import build
    return (build("youtube", "v3", credentials=creds, cache_discovery=False),
            build("youtubeAnalytics", "v2", credentials=creds, cache_discovery=False))


def autorizar():
    """Abre el navegador: eliges la cuenta y luego EL CANAL. Guarda el permiso con el nombre del canal."""
    from google_auth_oauthlib.flow import InstalledAppFlow
    if not CLIENTE.exists():
        print("⚠️ Falta secretos/oauth_cliente.json")
        return
    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENTE), SCOPES)
    print("🌐 Se abre Google: elige tu cuenta y luego EL CANAL que quieres autorizar.")
    creds = flow.run_local_server(port=0, prompt="consent", authorization_prompt_message="")
    yt, _ = servicios(creds)
    ch = yt.channels().list(part="snippet", mine=True).execute().get("items", [])
    if not ch:
        print("⚠️ Esa cuenta no tiene canal. Vuelve a intentar y elige el canal (no la cuenta personal).")
        return
    handle = ch[0]["snippet"].get("customUrl") or ch[0]["snippet"]["title"]
    nombre = handle.lstrip("@").replace(" ", "").lower()
    SECRETOS.mkdir(exist_ok=True)
    (SECRETOS / f"token_{nombre}.json").write_text(creds.to_json())
    estado({nombre: {"ok": True, "desde": dt.datetime.now(ZONA).isoformat(timespec="minutes"), "titulo": ch[0]["snippet"]["title"]}})
    print(f"✅ Autorizado: {ch[0]['snippet']['title']} ({handle}). Repite para el siguiente canal.")


def credenciales():
    """Permisos guardados -> {canal: creds}. Si alguno vencio (modo Testing: cada 7 dias) lo marca para reautorizar."""
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    out = {}
    for t in sorted(SECRETOS.glob("token_*.json")):
        canal = t.stem[len("token_"):]
        try:
            c = Credentials.from_authorized_user_file(str(t), SCOPES)
            if not c.valid:
                c.refresh(Request())
                t.write_text(c.to_json())
            out[canal] = c
            estado({canal: {**estado().get(canal, {}), "ok": True}})
        except Exception as e:
            print(f"⚠️ {canal}: el permiso vencio ({str(e)[:60]}). Corre:  python metricas.py --autorizar")
            estado({canal: {**estado().get(canal, {}), "ok": False}})
    return out


def iso_dur(s):
    import re
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return None
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def foto_canal(c, canal, creds, ahora):
    yt, ya = servicios(creds)
    ch = yt.channels().list(part="contentDetails", mine=True).execute()["items"][0]
    subidas = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    while len(ids) < 200:
        r = yt.playlistItems().list(part="contentDetails", playlistId=subidas, maxResults=50, pageToken=token).execute()
        ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
        token = r.get("nextPageToken")
        if not token:
            break
    for k in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,statistics,contentDetails,status", id=",".join(ids[k:k + 50])).execute()
        for v in r.get("items", []):
            st = v.get("statistics", {})
            publicado = v["snippet"]["publishedAt"]       # al salir publico, es la hora real de publicacion
            if v["status"].get("privacyStatus") != "public":
                continue                         # programados o privados: todavia no cuentan
            c.execute("INSERT OR REPLACE INTO videos VALUES (?,?,?,?,?)",
                      (v["id"], canal, v["snippet"]["title"], publicado, iso_dur(v["contentDetails"].get("duration"))))
            c.execute("INSERT INTO fotos VALUES (?,?,?,?,?)", (v["id"], ahora, int(st.get("viewCount", 0)),
                      int(st.get("likeCount", 0)), int(st.get("commentCount", 0))))
    # Analytics (retencion, compartidos, suscriptores): YouTube lo entrega con 1-2 dias de atraso
    hoy = dt.date.today()
    try:
        r = ya.reports().query(ids="channel==MINE", startDate=(hoy - dt.timedelta(days=365)).isoformat(), endDate=hoy.isoformat(),
                               metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,likes,shares,subscribersGained",
                               dimensions="video", sort="-views", maxResults=200).execute()
        for fila in r.get("rows", []):
            c.execute("INSERT OR REPLACE INTO analytics VALUES (?,?,?,?,?,?,?,?,?)", (fila[0], ahora, *fila[1:]))
    except Exception as e:
        print(f"   (analytics {canal}: {str(e)[:80]})")
    c.commit()
    return len(ids)


def tomar_foto():
    if not list(SECRETOS.glob("token_*.json")):
        print("⚠️ No hay canales autorizados. Corre:  python metricas.py --autorizar   (una vez por canal)")
        return
    c = bd()
    ahora = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    for canal, creds in credenciales().items():
        try:
            n = foto_canal(c, canal, creds, ahora)
            print(f"📸 {canal}: {n} videos")
        except Exception as e:
            print(f"⚠️ {canal}: {str(e)[:120]}")
    estado({"_ultima_foto": dt.datetime.now(ZONA).isoformat(timespec="minutes")})


# ---------------- analisis ----------------
def vistas_a(fotos, pub, horas):
    """Vistas que tenia el video a las N horas de publicado (interpolando entre fotos). None si aun no se sabe."""
    objetivo = pub + dt.timedelta(hours=horas)
    antes = [(t, v) for t, v in fotos if t <= objetivo]
    despues = [(t, v) for t, v in fotos if t >= objetivo]
    if not despues:
        return None
    t1, v1 = despues[0]
    if not antes:
        return v1 if (t1 - objetivo) <= dt.timedelta(hours=1) else None
    t0, v0 = antes[-1]
    if t1 == t0:
        return v0
    if (t1 - t0) > dt.timedelta(hours=max(3, horas / 2)):
        return None                              # hueco muy grande sin fotos: no se inventa
    return round(v0 + (v1 - v0) * (objetivo - t0) / (t1 - t0))


def resumen():
    if not BD.exists():
        return {"canales": [], "estado": estado()}
    c = bd()
    ahora = dt.datetime.now(dt.timezone.utc)
    canales = {}
    for vid, canal, titulo, pub, dur in c.execute("SELECT * FROM videos ORDER BY publicado DESC"):
        p = dt.datetime.fromisoformat(pub.replace("Z", "+00:00"))
        fotos = [(dt.datetime.fromisoformat(t), v) for t, v in c.execute("SELECT ts, vistas FROM fotos WHERE id=? ORDER BY ts", (vid,))]
        a = c.execute("SELECT pct_prom, dur_prom, compartidos, subs, likes FROM analytics WHERE id=?", (vid,)).fetchone()
        local = p.astimezone(ZONA)
        canales.setdefault(canal, []).append({
            "id": vid, "titulo": titulo, "publicado": local.strftime("%Y-%m-%d %H:%M"), "dia": local.strftime("%a"),
            "hora": local.hour, "edad_h": round((ahora - p).total_seconds() / 3600, 1), "duracion": dur,
            "vistas": fotos[-1][1] if fotos else 0,
            "a": {str(h): vistas_a(fotos, p, h) for h in EDADES},
            "retencion": round(a[0], 1) if a and a[0] is not None else None,
            "dur_prom": round(a[1], 1) if a and a[1] is not None else None,
            "compartidos": a[2] if a else None, "subs": a[3] if a else None})
    out = []
    for canal, vids in canales.items():
        franjas = {}
        for v in vids:                            # rendimiento por hora de publicacion (vistas a las 24 h)
            x = v["a"]["24"]
            if x is not None:
                franjas.setdefault(v["hora"], []).append(x)
        out.append({"canal": canal, "videos": vids,
                    "por_hora": {h: {"n": len(xs), "mediana": sorted(xs)[len(xs) // 2]} for h, xs in sorted(franjas.items())}})
    return {"canales": out, "estado": estado()}


def imprimir():
    r = resumen()
    for k in r["canales"]:
        print(f"\n===== {k['canal']} =====")
        print(f"{'publicado':16}  {'vistas':>7}  {'2h':>6} {'6h':>6} {'24h':>6} {'48h':>6}  {'ret%':>5}  titulo")
        for v in k["videos"][:30]:
            f = lambda x: "-" if x is None else str(x)
            print(f"{v['publicado']:16}  {v['vistas']:>7}  {f(v['a']['2']):>6} {f(v['a']['6']):>6} {f(v['a']['24']):>6} "
                  f"{f(v['a']['48']):>6}  {f(v['retencion']):>5}  {v['titulo'][:50]}")
        if k["por_hora"]:
            print("Por hora de publicacion (mediana de vistas a las 24 h):")
            for h, d in k["por_hora"].items():
                print(f"   {int(h):02d}:00  {d['mediana']:>7}  (n={d['n']})")


if __name__ == "__main__":
    if "--autorizar" in sys.argv:
        autorizar()
    elif "--resumen" in sys.argv:
        imprimir()
    else:
        tomar_foto()
