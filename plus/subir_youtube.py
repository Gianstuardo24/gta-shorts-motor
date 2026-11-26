"""SUBIR A YOUTUBE (22-nov): sube los videos del día a TUS canales y los deja programados a la hora del .txt.

Lee ~/Desktop/YouTube/<carpeta>/<AAAA-MM-DD Día>/HHh - Título.mp4 y su .txt (TÍTULO, DESCRIPCIÓN completa, PUBLICAR).
Sube cada uno como PRIVADO con fecha de publicación (publishAt): YouTube lo publica solo a esa hora.
Después lo marca como subido igual que el botón "✓ Subido" del Estudio (lo mueve a Subidos/ y lo anota).

Uso (desde ~/gta-shorts):
  ./venv/bin/python3 subir_youtube.py --autorizar                  una vez por canal (permiso SOLO para subir)
  ./venv/bin/python3 subir_youtube.py --dia 2026-11-23             muestra qué subiría (NO sube nada)
  ./venv/bin/python3 subir_youtube.py --dia 2026-11-23 --subir     sube y programa
  ./venv/bin/python3 subir_youtube.py --dia 2026-11-23 --canal DogDecoded --subir      solo esa carpeta
  ./venv/bin/python3 subir_youtube.py --dia 2026-11-23 --subir --ahora   los que ya pasaron su hora salen al tiro
                                                                      (sin --ahora esos se saltan)
Importante:
  · El permiso para subir va APARTE del de métricas: secretos/subir/<canal>.json (metricas.py no lo ve ni lo usa).
  · Desde el 2-nov-2026 YouTube ya NO bloquea como privado lo que suben proyectos sin auditar. Cupo por defecto:
    100 subidas al día por proyecto (sobra para 14 al día). Ver GUIA_SUBIDA_API.md.
  · Si la pantalla de permisos de Google está en "Testing", el permiso vence a los 7 días: pásala a "In production".
  · Nunca sube dos veces lo mismo: lo ya subido queda en datos/subidas_api.json y se salta.
"""
import re, sys, json, time, datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path("~/Desktop/YouTube").expanduser()
SECRETOS = Path("secretos")
CLIENTE = SECRETOS / "oauth_cliente.json"
TOKENS = SECRETOS / "subir"
REGISTRO = Path("datos/subidas_api.json")
MAPA = Path("datos/mapa_canales.json")
ZONA = ZoneInfo("America/Santiago")
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.readonly"]
MAPA_BASE = {"TheViceVerseGG": "theviceversegg", "ViceVersoGG": "viceversogg", "TheRabbitLoop": "therabbitloop",
             "MillionDollarMistake": "mdollarmistake", "ChiChibitsTV": "chichibitstv",
             "DogDecoded": "thedogsdecoder", "CatDecoded": "thecatsdecoder"}
# Categoría de YouTube por carpeta (20 Gaming · 15 Mascotas y animales · 27 Educación · 24 Entretenimiento)
CATEGORIA = {"TheViceVerseGG": "20", "ViceVersoGG": "20", "DogDecoded": "15", "CatDecoded": "15",
             "MillionDollarMistake": "27", "ChiChibitsTV": "27", "TheRabbitLoop": "24"}
MARGEN_MIN = 20      # publishAt tiene que quedar al menos 20 min en el futuro


def mapa():
    try:
        return {**MAPA_BASE, **json.loads(MAPA.read_text())}
    except Exception:
        return dict(MAPA_BASE)


def registro():
    try:
        return json.loads(REGISTRO.read_text())
    except Exception:
        return {}


def anotar(rel, datos):
    d = registro()
    d[rel] = datos
    REGISTRO.parent.mkdir(exist_ok=True)
    REGISTRO.write_text(json.dumps(d, ensure_ascii=False, indent=1))


# ---------------- permisos ----------------
def autorizar():
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    if not CLIENTE.exists():
        print("⚠️ Falta secretos/oauth_cliente.json")
        return
    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENTE), SCOPES)
    print("🌐 Se abre Google: elige tu cuenta y luego EL CANAL al que se va a subir.")
    creds = flow.run_local_server(port=0, prompt="consent", authorization_prompt_message="")
    yt = build("youtube", "v3", credentials=creds, cache_discovery=False)
    ch = yt.channels().list(part="snippet", mine=True).execute().get("items", [])
    if not ch:
        print("⚠️ Esa cuenta no tiene canal. Repite y elige el canal (no la cuenta personal).")
        return
    nombre = (ch[0]["snippet"].get("customUrl") or ch[0]["snippet"]["title"]).lstrip("@").replace(" ", "").lower()
    TOKENS.mkdir(parents=True, exist_ok=True)
    (TOKENS / f"{nombre}.json").write_text(creds.to_json())
    print(f"✅ Permiso de subida guardado para {ch[0]['snippet']['title']} (@{nombre}). Repite para el siguiente canal.")
    if nombre not in mapa().values():
        print(f"   ⚠️ @{nombre} no está en datos/mapa_canales.json: agrégalo ahí con el nombre de su carpeta.")


def credenciales(handle):
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    t = TOKENS / f"{handle}.json"
    if not t.exists():
        return None, "sin permiso (corre --autorizar y elige ese canal)"
    try:
        c = Credentials.from_authorized_user_file(str(t), SCOPES)
        if not c.valid:
            c.refresh(Request())
            t.write_text(c.to_json())
        return c, "ok"
    except Exception as e:
        return None, f"el permiso venció ({str(e)[:50]}): corre --autorizar otra vez"


# ---------------- leer lo que hay que subir ----------------
def leer_txt(p):
    s = p.read_text(encoding="utf-8") if p.exists() else ""
    tit = re.search(r"TÍTULO:\s*\n(.+)", s)
    desc = s.split("DESCRIPCIÓN:", 1)[1].strip() if "DESCRIPCIÓN:" in s else ""
    hm = re.search(r"PUBLICAR:.*?(\d{1,2}):(\d{2})", s)
    return (tit.group(1).strip() if tit else ""), desc, ((int(hm.group(1)), int(hm.group(2))) if hm else None)


def pendientes(dia, solo=None):
    """Videos de ese día que aún no están en Subidos/."""
    out = []
    for carpeta, handle in mapa().items():
        if solo and carpeta != solo:
            continue
        for d in sorted((RAIZ / carpeta).glob(f"{dia} *")):
            if not d.is_dir():
                continue
            for mp4 in sorted(d.glob("[0-2][0-9]h - *.mp4")):
                titulo, desc, hm = leer_txt(mp4.with_suffix(".txt"))
                h, m = hm or (int(mp4.name[:2]), 0)
                y, mo, da = map(int, dia.split("-"))
                cuando = dt.datetime(y, mo, da, h, m, tzinfo=ZONA)
                out.append({"carpeta": carpeta, "handle": handle, "mp4": mp4, "dia": d.name,
                            "hora": f"{mp4.name[:2]}:00", "rel": str(mp4.relative_to(RAIZ)),
                            "titulo": titulo, "desc": desc, "cuando": cuando})
    return out


def problemas(v):
    p = []
    if not v["titulo"]:
        p.append("el .txt no tiene TÍTULO")
    if len(v["titulo"]) > 100:
        p.append(f"título de {len(v['titulo'])} caracteres (máx. 100)")
    if len(v["desc"]) > 5000:
        p.append("descripción de más de 5.000 caracteres")
    if "<" in v["titulo"] + v["desc"] or ">" in v["titulo"] + v["desc"]:
        p.append("tiene < o > (YouTube no los acepta)")
    if v["rel"] in registro():
        p.append("YA SE SUBIÓ por API (no se repite)")
    return p


# ---------------- subir ----------------
def subir_uno(yt, v, publicar_ya):
    from googleapiclient.http import MediaFileUpload
    estado = {"privacyStatus": "public"} if publicar_ya else \
        {"privacyStatus": "private", "publishAt": v["cuando"].astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    cuerpo = {"snippet": {"title": v["titulo"], "description": v["desc"], "categoryId": CATEGORIA.get(v["carpeta"], "24")},
              "status": {**estado, "selfDeclaredMadeForKids": False}}
    media = MediaFileUpload(str(v["mp4"]), mimetype="video/mp4", chunksize=8 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=cuerpo, media_body=media, notifySubscribers=True)
    resp = None
    while resp is None:
        prog, resp = req.next_chunk(num_retries=3)
        if prog:
            print(f"      {int(prog.progress() * 100)} %", end="\r")
    return resp


def correr(dia, solo=None, subir=False, ahora_si=False):
    vids = pendientes(dia, solo)
    if not vids:
        print(f"No hay videos pendientes para {dia}" + (f" en {solo}" if solo else "") + ".")
        return
    ahora = dt.datetime.now(ZONA)
    print(f"{'SUBIENDO' if subir else 'VISTA PREVIA (no sube nada; agrega --subir)'} · {dia}\n")
    servicios, hechos = {}, 0
    for v in vids:
        falta = (v["cuando"] - ahora).total_seconds() / 60
        ya = falta < MARGEN_MIN
        p = problemas(v)
        if ya and not ahora_si:
            p.append(f"su hora ({v['cuando']:%H:%M}) ya pasó o falta muy poco (usa --ahora para publicarlo al tiro)")
        marca = "⛔" if p else ("🚀 al tiro" if ya else f"🗓️ {v['cuando']:%d/%m %H:%M}")
        print(f"  {marca}  {v['carpeta']:<20} {v['titulo'][:60]}")
        for x in p:
            print(f"        · {x}")
        if p or not subir:
            continue
        if v["handle"] not in servicios:
            c, msg = credenciales(v["handle"])
            if not c:
                print(f"        · @{v['handle']}: {msg}")
                servicios[v["handle"]] = None
                continue
            from googleapiclient.discovery import build
            yt = build("youtube", "v3", credentials=c, cache_discovery=False)
            ch = yt.channels().list(part="snippet", mine=True).execute().get("items", [])
            real = (ch[0]["snippet"].get("customUrl") or "").lstrip("@").lower() if ch else ""
            if real != v["handle"]:
                print(f"        · el permiso es de @{real or '?'}, no de @{v['handle']}: no se sube (revisa --autorizar)")
                servicios[v["handle"]] = None
                continue
            servicios[v["handle"]] = yt
        yt = servicios[v["handle"]]
        if yt is None:
            continue
        try:
            r = subir_uno(yt, v, ya)
        except Exception as e:
            txt = str(e)
            print(f"        · ❌ falló: {txt[:160]}")
            if "quota" in txt.lower() or "uploadLimitExceeded" in txt:
                print("        · Se acabó el cupo diario de la API: sigue mañana o a mano.")
                break
            continue
        st = r.get("status", {})
        anotar(v["rel"], {"id": r.get("id"), "subido": ahora.isoformat(timespec="seconds"),
                          "publishAt": st.get("publishAt"), "privacidad": st.get("privacyStatus")})
        print(f"        ✅ https://youtube.com/shorts/{r.get('id')}  ({st.get('privacyStatus')}"
              f"{', sale ' + v['cuando'].strftime('%H:%M') if st.get('publishAt') else ''})")
        if not ya and not st.get("publishAt"):
            print("        ⚠️ YouTube no devolvió la hora de publicación: revisa ese video en YouTube Studio.")
        try:
            import estudio
            if estudio.video_subido(v["rel"], v["dia"], v["hora"]):
                estudio.registrar_subida(v["rel"], v["dia"], v["hora"])
        except Exception as e:
            print(f"        · (subido, pero no pude marcarlo en el Estudio: {str(e)[:80]}; márcalo a mano)")
        hechos += 1
        time.sleep(2)
    if subir:
        print(f"\nListo: {hechos} subido(s).")


if __name__ == "__main__":
    a = sys.argv
    if "--autorizar" in a:
        autorizar()
    else:
        dia = a[a.index("--dia") + 1] if "--dia" in a else dt.datetime.now(ZONA).strftime("%Y-%m-%d")
        solo = a[a.index("--canal") + 1] if "--canal" in a else None
        correr(dia, solo, subir="--subir" in a, ahora_si="--ahora" in a)
