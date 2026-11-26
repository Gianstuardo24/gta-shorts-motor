"""GANCHOS: que hooks funcionan, como estan escritos y que psicologia activan.

Mira 2 cosas y las cruza:
  1. NUESTROS videos (datos/metricas.db + guiones/): hook real, vistas a 24 h, % visto.
  2. Shorts VIRALES de cada tema (YouTube Data API, ES y EN): vistas / lo normal de SU canal.
Claude etiqueta cada hook (palanca, estructura, mecanismo psicologico, riesgo de engano)
y escribe el informe: que funciona, como se redacta, por que, plantillas por canal e hipotesis a probar.

Uso (cd ~/gta-shorts && source venv/bin/activate):
  python ganchos.py                          -> nuestros + radar de todos los temas, ES+EN
  python ganchos.py --tema gta --idioma es   -> solo un tema / idioma
  python ganchos.py --solo-propios           -> sin gastar cuota de YouTube
Salida: datos/estrategia/5-ganchos.md (Estudio > Analisis > Ganchos), ganchos/ (historial)
        y tabla `ganchos` en datos/metricas.db.
Cuota YouTube: ~100 unidades por busqueda + ~2 por canal revisado (todo: ~1.900 de 10.000 diarias).
La API key se lee de secretos/youtube.json (nunca se imprime).
"""
import re, sys, json, sqlite3, argparse, difflib, statistics, subprocess, datetime as dt
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor

from utilidades import extraer_json

DB = Path("datos/metricas.db")
INFORME = Path("datos/estrategia/5-ganchos.md")
HIST = Path("ganchos")
API = "https://www.googleapis.com/youtube/v3/"
AHORA = dt.datetime.now(dt.timezone.utc)

BUSQUEDAS = {   # tema -> idioma -> busquedas (2 por defecto: cada una cuesta 100 unidades)
    "gta":      {"es": ["GTA 6", "GTA 6 gameplay"], "en": ["GTA 6", "GTA 6 gameplay"]},
    "aliens":   {"es": ["ovni", "extraterrestres"], "en": ["UFO", "aliens"]},
    "cafe":     {"es": ["café curiosidades", "historia del café"], "en": ["coffee facts", "coffee but why"]},
    "suerte":   {"es": ["mensaje del universo", "señal de suerte"], "en": ["sign from the universe", "lucky message today"]},
    "negocios": {"es": ["error de empresa millones"], "en": ["billion dollar mistake", "business mistake"]},
}
POR_DEFECTO = ["gta", "aliens", "cafe", "suerte"]
NUESTRO = {"viceversogg": ("gta", "es"), "theviceversegg": ("gta", "en"),
           "therabbitloop": ("aliens", "en"), "mdollarmistake": ("negocios", "en")}
GTA = re.compile(r"gta\s*-?\s*(6|vi)\b|grand\s+theft\s+auto", re.I)
# Vocabulario minimo por tema: un video entra al tema SOLO si su titulo / descripcion / tags hablan de eso
# (evita que un canal de cocina que subio un cafe meta sus recetas virales en "cafe").
TEMAS_RE = {
    "gta": GTA,
    "aliens": re.compile(r"\b(ufos?|uaps?|ovnis?|aliens?|alien[ií]genas?|extraterrestres?|et\b|area\s*51|roswell|abduc\w*|"
                         r"space|espacio|nasa|planet\w*|galax\w*|asteroid\w*|cosmos|c[oó]smic\w*|universe|universo|"
                         r"signal|se[ñn]al|telescop\w*|meteor\w*|mars|marte|moon|luna|orbit\w*|"
                         r"myster\w*|misterio\w*|unexplained|inexplicable|paranormal|anomal\w*)\b", re.I),
    "cafe": re.compile(r"\b(coffee|caf[eé]s?|espresso|expreso|barista\w*|latte|cappuccino|capuchino|mocha|moka|americano|"
                       r"cold\s*brew|caffeine|cafe[ií]na|arabica|ar[aá]bica|robusta|roast\w*|tostad\w*|french\s*press|"
                       r"pour\s*over|v60|aeropress|cafeter[ií]a)\b", re.I),
    "suerte": re.compile(r"(11:11|\b(111|222|333|444|555|666|777|888|999|1111|1212)\b|angel\s*numbers?|n[uú]meros?\s*angelical\w*|"
                         r"numerolog\w*|\buniverse\b|\buniverso\b|\bluck\w*|\bsuerte\b|manifest\w*|"
                         r"\byour\s+sign\b|\btu\s+se[ñn]al\b|\bsign\s+from\b|\bse[ñn]al\s+del\b|\bdestin\w*|\bdestiny\b|\bfortun\w*)", re.I),
    "negocios": re.compile(r"\b(business\w*|compan(y|ies)|empresas?|brands?|marcas?|startups?|ceo|founders?|fundador\w*|"
                           r"billion\w*|million\w*|mill[oó]n\w*|millonari\w*|bankrupt\w*|quiebra|quebr[oó]|negocio\w*|"
                           r"money|dinero|market\w*|mercado|invest\w*|inversi[oó]n|acquisi\w*|deal|stock\w*|bolsa|"
                           r"profit\w*|ganancia\w*|ventas?|sales|fortune|fortuna|entrepreneur\w*|emprend\w*)\b", re.I),
}


def del_tema(tema, *textos):
    """True si el video habla del tema (titulo + descripcion + tags). Temas sin vocabulario: siempre True."""
    rx = TEMAS_RE.get(tema)
    return True if rx is None else bool(rx.search(" ".join(t for t in textos if t)))
PALANCAS = {
    "perdida": "pierdes algo que ya es tuyo (dinero, partida, preventa, tiempo, espacio)",
    "primeros": "otros ya lo tienen / ser de los primeros (FOMO)",
    "curiosidad": "hueco concreto: algo raro + por que / que paso",
    "ventana": "algo que se acaba o cambia en una fecha real (escasez nueva)",
    "identidad": "te pone a ti a prueba: eres uno, te pasa, calificas",
    "prueba_social": "todos lo comparten / miles lo vieron",
    "seleccion": "este video te encontro a ti / mensaje para ti",
    "plano": "dato o noticia sin pregunta ni nada en juego",
    "otro": "otra cosa",
}


# ---------------- YouTube Data API ----------------
def _clave():
    """API key si existe (secretos/youtube_api_key.txt o una 'AIza...' dentro de secretos/youtube.json).
    Si no hay, usa el MISMO permiso OAuth de metricas.py (secretos/token_<canal>.json). Nunca se imprime nada secreto."""
    for p in (Path("secretos/youtube_api_key.txt"), Path("secretos/youtube.json")):
        if not p.exists():
            continue
        txt = p.read_text().strip()
        if txt.startswith("AIza"):
            return txt
        try:
            def buscar(o):
                if isinstance(o, str) and o.startswith("AIza"):
                    return o
                for v in (o.values() if isinstance(o, dict) else o if isinstance(o, list) else []):
                    r = buscar(v)
                    if r:
                        return r
            k = buscar(json.loads(txt))
            if k:
                return k
        except Exception:
            pass
    try:
        import metricas
        creds = metricas.credenciales()
    except Exception as e:
        creds = {}
        print(f"   ⚠️ OAuth: {str(e)[:80]}")
    if creds:
        OAUTH["creds"] = next(iter(creds.values()))
        print(f"🔐 YouTube API con el permiso OAuth de {next(iter(creds))} (el mismo de métricas)", flush=True)
        return None
    sys.exit("⛔ No hay API key ni permiso OAuth de YouTube. Corre:  python metricas.py --autorizar")


OAUTH = {"creds": None}
KEY = None
CUOTA = {"u": 0}


def get(ruta, costo=1, **p):
    from urllib.request import Request as Req
    if CUOTA.get("agotada"):
        return {}
    CUOTA["u"] += costo
    headers = {}
    if KEY:
        p["key"] = KEY
    elif OAUTH["creds"] is not None:
        c = OAUTH["creds"]
        if not c.valid:
            from google.auth.transport.requests import Request
            c.refresh(Request())
        headers["Authorization"] = f"Bearer {c.token}"
    import time as _t
    from urllib.error import URLError
    for intento in range(5):     # cortes puntuales de red / SSL / 5xx: reintenta con espera creciente
        try:
            with urlopen(Req(API + ruta + "?" + urlencode(p), headers=headers), timeout=40) as r:
                return json.loads(r.read())
        except HTTPError as e:
            if e.code >= 500 and intento < 4:
                _t.sleep(3 * (intento + 1))
                continue
            return _error_http(e, ruta)
        except (URLError, TimeoutError, ConnectionError, OSError) as e:
            if intento < 4:
                print(f"   ↻ {ruta}: corte de conexión ({str(e)[:50]}), reintento {intento + 1}/4...", flush=True)
                _t.sleep(4 * (intento + 1))
                continue
            print(f"   ⚠️ {ruta}: sin conexión tras 5 intentos, sigo con lo que hay", flush=True)
            return {}
    return {}


class CuotaAgotada(SystemExit):
    """Cuota diaria de YouTube agotada. Hereda de SystemExit: los scripts viejos se detienen igual que antes;
    el Radar completo la atrapa y sigue con lo que ya tiene guardado (el analisis profundo no usa la API)."""


def _error_http(e, ruta):
    if True:
        msg = e.read().decode(errors="ignore")[:300]
        if KEY:
            msg = msg.replace(KEY, "***")
        if "quota" in msg.lower():
            CUOTA["agotada"] = True
            raise CuotaAgotada("⛔ Se acabo la cuota diaria de YouTube (se renueva a las ~05:00 de Chile).")
        print(f"   ⚠️ {ruta}: HTTP {e.code} {msg[:120]}")
        return {}


def segundos(iso):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def fecha(s):
    d = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)      # fechas sin zona (TikTok/IG/exports) = UTC


ES = set("el la los las de del que qué por para con una un es no se lo esto este esta su tu te y en al como cómo".split())
EN = set("the a an of to and is in this that you your why what how it was are for on with they".split())


def escritura_latina(t):
    """False si el titulo esta mayormente en otra escritura (arabe, devanagari, telugu, cirilico, CJK...)."""
    letras = [ch for ch in (t or "") if ch.isalpha()]
    if not letras:
        return True
    latinas = sum(1 for ch in letras if ord(ch) < 0x0250)
    return latinas / len(letras) >= 0.7


def idioma_video(sn, por_defecto):
    """Idioma del VIDEO (audio declarado > idioma declarado > titulo > el del canal). None si es otro idioma (hi, ar, pt...)."""
    l = (sn.get("defaultAudioLanguage") or sn.get("defaultLanguage") or "")[:2].lower()
    if l in ("es", "en"):
        return l
    if l and l not in ("zx", "un"):
        return None
    t = idioma_de(sn.get("title", ""))
    return t if t in ("es", "en") else por_defecto


def idioma_de(t):
    w = re.findall(r"[a-záéíóúñü]+", (t or "").lower())
    es = sum(x in ES for x in w) + (2 if re.search(r"[ñ¿¡áéíóú]", (t or "").lower()) else 0)
    en = sum(x in EN for x in w)
    return "es" if es > en else "en" if en > es else "?"


def videos_info(ids):
    out = {}
    for i in range(0, len(ids), 50):
        r = get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]))
        for it in r.get("items", []):
            out[it["id"]] = it
    return out


def normal_de_canales(cids):
    """Mediana de vistas de los ultimos Shorts de cada canal (lo 'normal' para ese canal)."""
    subs, uploads = {}, {}
    for i in range(0, len(cids), 50):
        r = get("channels", part="contentDetails,statistics", id=",".join(cids[i:i + 50]))
        for it in r.get("items", []):
            uploads[it["id"]] = it["contentDetails"]["relatedPlaylists"]["uploads"]
            subs[it["id"]] = int(it["statistics"].get("subscriberCount") or 0)

    def uno(cid):
        r = get("playlistItems", part="contentDetails", playlistId=uploads[cid], maxResults=30)
        ids = [x["contentDetails"]["videoId"] for x in r.get("items", [])]
        info = videos_info(ids)
        vs = [int(v["statistics"].get("viewCount") or 0) for v in info.values()
              if segundos(v["contentDetails"]["duration"]) <= 180]
        return cid, vs

    norm = {}
    with ThreadPoolExecutor(6) as ex:
        for cid, vs in ex.map(uno, [c for c in cids if c in uploads]):
            norm[cid] = vs
    return norm, subs


def radar(temas, idiomas, dias, por_combo):
    filas, desde = [], (AHORA - dt.timedelta(days=dias)).strftime("%Y-%m-%dT%H:%M:%SZ")
    for tema in temas:
        for idi in idiomas:
            ids = []
            for q in BUSQUEDAS[tema][idi]:
                print(f"🔎 [{tema}/{idi}] {q}")
                r = get("search", costo=100, part="snippet", q=q, type="video", videoDuration="short",
                        order="viewCount", publishedAfter=desde, maxResults=25, relevanceLanguage=idi)
                ids += [it["id"]["videoId"] for it in r.get("items", []) if it.get("id", {}).get("videoId")]
            info = videos_info(list(dict.fromkeys(ids)))
            cand = []
            for vid, v in info.items():
                sn, st = v["snippet"], v["statistics"]
                if segundos(v["contentDetails"]["duration"]) > 180 or sn.get("liveBroadcastContent") != "none":
                    continue
                if sn["channelTitle"].lower().startswith(tuple(NUESTRO)):
                    continue
                lang = (sn.get("defaultAudioLanguage") or sn.get("defaultLanguage") or "")[:2] or idioma_de(sn["title"])
                if lang not in (idi, "?"):
                    continue
                if tema == "gta" and not GTA.search(sn["title"] + " " + sn.get("description", "")[:300]):
                    continue
                horas = max((AHORA - fecha(sn["publishedAt"])).total_seconds() / 3600, 1)
                cand.append({"id": vid, "tema": tema, "idioma": idi, "titulo": sn["title"],
                             "descripcion": sn.get("description", "")[:200], "canal_id": sn["channelId"],
                             "canal_nombre": sn["channelTitle"], "vistas": int(st.get("viewCount") or 0),
                             "likes": int(st.get("likeCount") or 0), "comentarios": int(st.get("commentCount") or 0),
                             "horas": round(horas), "duracion": segundos(v["contentDetails"]["duration"])})
            cand.sort(key=lambda c: c["vistas"], reverse=True)
            filas += cand[:por_combo]
    if filas:
        print(f"📏 Midiendo lo normal de {len({f['canal_id'] for f in filas})} canales...")
        norm, subs = normal_de_canales(list({f["canal_id"] for f in filas}))
        for f in filas:
            otros = [x for x in norm.get(f["canal_id"], []) if x != f["vistas"]]
            f["normal_canal"] = int(statistics.median(otros)) if len(otros) >= 3 else None
            f["ratio"] = round(f["vistas"] / max(f["normal_canal"], 1), 1) if f["normal_canal"] else None
            f["subs"] = subs.get(f["canal_id"])
    return filas


# ---------------- nuestros videos ----------------
def propios():
    c = sqlite3.connect(DB)
    guiones = {}
    for g in Path("guiones").glob("*.json"):
        try:
            d = json.loads(g.read_text())
            guiones[d.get("titulo", "").strip()] = d
        except Exception:
            pass
    titulos = list(guiones)
    out = []
    for vid, canal, tit, pub in c.execute("select id, canal, titulo, publicado from videos"):
        g = guiones.get((tit or "").strip())
        if not g:
            m = difflib.get_close_matches(tit or "", titulos, 1, 0.6)
            g = guiones[m[0]] if m else {}
        p = fecha(pub)
        horas = (AHORA - p).total_seconds() / 3600
        fotos = [(fecha(ts), v) for ts, v in c.execute("select ts, vistas from fotos where id=?", (vid,))]
        v24 = None
        if horas >= 20 and fotos:
            ts, v = min(fotos, key=lambda x: abs((x[0] - p).total_seconds() - 86400))
            if abs((ts - p).total_seconds() - 86400) < 8 * 3600:
                v24 = v
        an = c.execute("select pct_prom, dur_prom from analytics where id=?", (vid,)).fetchone()
        tema, idi = NUESTRO.get(canal, ("?", "?"))
        out.append({"id": vid, "origen": "propio", "canal": canal, "tema": tema, "idioma": idi, "titulo": tit,
                    "hook": (g.get("frases") or [""])[0], "texto_pantalla": g.get("texto_pantalla", ""),
                    "palanca_declarada": g.get("palanca", ""), "formato": g.get("formato", ""),
                    "vistas_24h": v24, "vistas": max([v for _, v in fotos], default=0),
                    "pct_visto": round(an[0], 1) if an and an[0] is not None else None, "horas": round(horas)})
    c.close()
    return out


# ---------------- Claude ----------------
def claude(prompt, entrada, timeout=1200):
    r = subprocess.run(["claude", "-p", prompt], input=entrada, capture_output=True, text=True, timeout=timeout)
    if r.returncode:
        raise RuntimeError((r.stderr or r.stdout)[-400:])
    return r.stdout


ETIQUETAR = """Eres psicologo del consumidor y guionista de YouTube Shorts. Te paso hooks numerados (titulo + primera frase si la hay).
Para CADA uno devuelve SOLO un array JSON con objetos:
{"n": numero, "palanca": una de [PALANCAS], "palanca2": otra o "",
 "estructura": "plantilla de redaccion con [huecos], ej: '¿Por que [actor] hizo [accion rara]?'",
 "pregunta": "la pregunta exacta que queda abierta en la cabeza del espectador",
 "mecanismo": "1 frase: que siente el espectador y que sesgo o necesidad se activa (curiosidad por hueco, aversion a perder algo propio, FOMO social, escasez nueva, identidad/autoevaluacion, prueba social, seleccion personal...)",
 "en_juego": "que tiene el espectador en juego (o 'nada')",
 "riesgo": "ninguno | promesa_exagerada | urgencia_falsa | enganoso | supersticion",
 "tema_ok": true si es del tema indicado, false si no}
Palancas: __DEF__
No inventes: juzga solo por el texto. 'mecanismo' debe ser especifico a ESTE hook (no una definicion de manual)."""

INFORMAR = """Eres el estratega de contenido de una fabrica de YouTube Shorts (canales: GTA 6 en ES y EN, aliens en EN,
negocios/suerte en EN, cafe en EN). Te paso: (A) tablas de rendimiento por palanca psicologica, de NUESTROS videos y de
virales externos; (B) nuestros videos con su hook, palanca y metricas; (C) los virales externos con mas 'veces lo normal'.
Escribe en espanol, markdown, esquematico, con negritas y tablas, sin relleno:
1. **Veredicto en 5 lineas**: que palancas rinden, en que tema e idioma, y cuales no.
2. **Nuestros datos**: que hooks propios funcionaron y cuales murieron, y POR QUE (estructura + mecanismo). Si n es chico, dilo.
3. **Como se escriben los que funcionan**: 6-10 patrones de redaccion con 1 ejemplo real cada uno (titulo exacto + 'veces lo normal').
4. **La psicologia detras**: para cada palanca que funciona, que se activa en la cabeza, en que condicion funciona y cuando falla
   (ej: la perdida solo pesa si el espectador ya siente que eso es suyo; la curiosidad necesita un hueco concreto y cerrable;
   la escasez sirve si es nueva y real). Usa solo lo que muestran los datos + estos principios; no cites estudios que no te pase.
5. **ES vs EN**: que cambia entre idiomas en el mismo tema. Propon angulos DISTINTOS para ES y EN del mismo tema de GTA.
6. **Plantillas listas por canal** (GTA ES, GTA EN, Rabbit aliens, suerte, cafe): 5 hooks cada uno, con su palanca y la condicion
   de verdad que debe cumplirse para usarlo. GTA: el juego ya salio, todo debe ser sobre lo que REALMENTE hay en el juego.
7. **Hipotesis para la proxima semana**: 5 pruebas concretas (palanca, canal, que medir, cuantos videos).
8. **Alertas**: hooks con riesgo de engano, urgencia falsa o supersticion. Regla: la palanca debe ser verdad y el video debe responder la pregunta.
No inventes metricas."""


def etiquetar(items):
    prompt = ETIQUETAR.replace("[PALANCAS]", ", ".join(PALANCAS)).replace(
        "__DEF__", "; ".join(f"{k} = {v}" for k, v in PALANCAS.items()))
    lotes = [items[i:i + 40] for i in range(0, len(items), 40)]

    def uno(lote):
        txt = "\n".join(f"[{it['_n']}] ({it['origen']}, tema {it['tema']}, {it['idioma']}) TITULO: {it['titulo']}"
                        + (f" | HOOK: {it['hook']}" if it.get("hook") else "")
                        + (f" | PANTALLA: {it['texto_pantalla']}" if it.get("texto_pantalla") else "") for it in lote)
        try:
            return extraer_json(claude(prompt, txt))
        except Exception as e:
            print(f"   ⚠️ Claude no etiqueto un lote: {e}")
            return []

    with ThreadPoolExecutor(3) as ex:
        res = [x for r in ex.map(uno, lotes) for x in r]
    por_n = {r.get("n"): r for r in res if isinstance(r, dict)}
    for it in items:
        it.update({k: v for k, v in por_n.get(it["_n"], {}).items() if k != "n"})


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def tablas(items):
    L = ["## Tablas (datos crudos)", "", "### Nuestros videos por palanca", "",
         "| Palanca | n | Mediana vistas 24 h | Mediana % visto |", "|---|---|---|---|"]
    pro = [i for i in items if i["origen"] == "propio"]
    for p in PALANCAS:
        g = [i for i in pro if i.get("palanca") == p]
        if g:
            m24, mp = med([i["vistas_24h"] for i in g]), med([i["pct_visto"] for i in g])
            L.append(f"| {p} | {len(g)} | {int(m24) if m24 is not None else '—'} | {f'{mp:.0f}%' if mp is not None else '—'} |")
    ext = [i for i in items if i["origen"] == "externo" and i.get("tema_ok", True) and i.get("ratio")]
    L += ["", "### Virales externos: veces lo normal de su canal, por tema, idioma y palanca", "",
          "| Tema | Idioma | Palanca | n | Mediana veces lo normal | Virales ≥3x |", "|---|---|---|---|---|---|"]
    for tema in BUSQUEDAS:
        for idi in ("es", "en"):
            for p in PALANCAS:
                g = [i for i in ext if i["tema"] == tema and i["idioma"] == idi and i.get("palanca") == p]
                if g:
                    L.append(f"| {tema} | {idi} | {p} | {len(g)} | ×{med([i['ratio'] for i in g]):.1f} | "
                             f"{sum(i['ratio'] >= 3 for i in g)}/{len(g)} |")
    return "\n".join(L)


def guardar_db(items):
    c = sqlite3.connect(DB)
    c.execute("""create table if not exists ganchos (id TEXT, fecha TEXT, origen TEXT, tema TEXT, idioma TEXT, canal TEXT,
        titulo TEXT, hook TEXT, palanca TEXT, palanca2 TEXT, estructura TEXT, pregunta TEXT, mecanismo TEXT, en_juego TEXT,
        riesgo TEXT, vistas INTEGER, vistas_24h INTEGER, pct_visto REAL, ratio REAL, PRIMARY KEY (id, fecha))""")
    hoy = AHORA.strftime("%Y-%m-%d")
    for i in items:
        c.execute("insert or replace into ganchos values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (i["id"], hoy, i["origen"], i["tema"], i["idioma"], i.get("canal") or i.get("canal_nombre"),
                   i["titulo"], i.get("hook", ""), i.get("palanca"), i.get("palanca2"), i.get("estructura"),
                   i.get("pregunta"), i.get("mecanismo"), i.get("en_juego"), i.get("riesgo"), i.get("vistas"),
                   i.get("vistas_24h"), i.get("pct_visto"), i.get("ratio")))
    c.commit()
    c.close()


def main():
    global KEY
    ap = argparse.ArgumentParser()
    ap.add_argument("--tema", default="todos", help="gta, aliens, cafe, suerte, negocios o todos")
    ap.add_argument("--idioma", default="ambos", help="es, en o ambos")
    ap.add_argument("--dias", type=int, default=14)
    ap.add_argument("--por", type=int, default=15, help="virales por tema e idioma")
    ap.add_argument("--solo-propios", action="store_true")
    a = ap.parse_args()
    temas = POR_DEFECTO if a.tema == "todos" else [t.strip() for t in a.tema.split(",")]
    idiomas = ["es", "en"] if a.idioma == "ambos" else [a.idioma]

    print("📚 Leyendo nuestros videos...")
    items = propios()
    print(f"   {len(items)} videos propios")
    if not a.solo_propios:
        KEY = _clave()
        items += [dict(f, origen="externo") for f in radar(temas, idiomas, a.dias, a.por)]
        print(f"   {sum(i['origen'] == 'externo' for i in items)} virales externos · cuota usada ≈ {CUOTA['u']} unidades")
    for n, it in enumerate(items, 1):
        it["_n"] = n
    print("🧠 Claude etiquetando hooks (palanca, estructura, psicologia)...")
    etiquetar(items)
    guardar_db(items)

    tab = tablas(items)
    pro = sorted([i for i in items if i["origen"] == "propio"], key=lambda i: -(i.get("vistas_24h") or i["vistas"] or 0))
    ext = sorted([i for i in items if i["origen"] == "externo" and i.get("tema_ok", True) and i.get("ratio")],
                 key=lambda i: -i["ratio"])
    linea = lambda i: (f"- [{i['tema']}/{i['idioma']}] \"{i['titulo']}\" · palanca {i.get('palanca')} · "
                       f"estructura: {i.get('estructura')} · mecanismo: {i.get('mecanismo')} · riesgo: {i.get('riesgo')}")
    entrada = (tab + "\n\n## (B) Nuestros videos\n" + "\n".join(
        linea(i) + f" · hook: {i['hook']} · 24h: {i['vistas_24h']} · total: {i['vistas']} · %visto: {i['pct_visto']} · edad {i['horas']} h"
        for i in pro) + "\n\n## (C) Virales externos (top por veces lo normal)\n" + "\n".join(
        linea(i) + f" · {i['vistas']} vistas · ×{i['ratio']} lo normal · canal {i['canal_nombre']} ({i.get('subs')} subs)"
        for i in ext[:60]))
    print("✍️  Claude escribiendo el informe...")
    try:
        informe = claude(INFORMAR, entrada)
    except Exception as e:
        informe = f"⚠️ No se pudo generar el informe: {e}"

    sello = AHORA.astimezone().strftime("%d/%m %H:%M")
    top = "\n".join(f"| {i['tema']} | {i['idioma']} | [{i['titulo'][:70]}](https://youtube.com/shorts/{i['id']}) | "
                    f"×{i['ratio']} | {i['vistas']:,} | {i.get('palanca')} |" for i in ext[:25])
    md = (f"# 🧲 Ganchos — {sello}\n\n_{len(pro)} videos propios · {len(ext)} virales externos medidos contra su canal · "
          f"temas: {', '.join(temas) if not a.solo_propios else '—'} · idiomas: {', '.join(idiomas)}_\n\n{informe.strip()}\n\n"
          f"## Top virales (veces lo normal de su canal)\n\n| Tema | Idioma | Video | Veces lo normal | Vistas | Palanca |\n"
          f"|---|---|---|---|---|---|\n{top}\n\n{tab}\n")
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    INFORME.write_text(md, encoding="utf-8")
    HIST.mkdir(exist_ok=True)
    marca = AHORA.astimezone().strftime("%Y%m%d_%H%M")
    (HIST / f"ganchos_{marca}.md").write_text(md, encoding="utf-8")
    (HIST / "ultimo.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"✅ Listo: Estudio > Análisis > 🧲 Ganchos  ({INFORME})")


if __name__ == "__main__":
    main()
