"""MULTIPLATAFORMA: TikTok e Instagram entran al mismo cerebro que YouTube (datos/cerebro.db, tabla virales, columna plataforma).

Fuentes (cualquiera sirve; todas terminan en el mismo formato):
  1) Instagram oficial: API de Meta, busqueda de hashtags (cuenta Business/Creator conectada a una pagina de Facebook).
     Limite de Meta: 30 hashtags unicos por cuenta cada 7 dias -> se rotan.  Token en secretos/instagram.json (nunca se imprime).
  2) TikTok Creative Center (panel PUBLICO de tendencias para anunciantes): lo muestrea Claude desde el navegador o un export.
  3) Links a mano: datos/plataformas/entrada.csv  (plataforma,url,tema,idioma,vistas,likes,comentarios,compartidos,seguidores,titulo)
  4) Cualquier export JSON/CSV con esas columnas:  python plataformas.py importar archivo.json

Como se mide (no hay "mediana del canal" en TikTok/IG sin recorrer el perfil):
  - TikTok: veces = vistas / seguidores del creador (proxy de "lo normal"); si viene la mediana del perfil, se usa esa.
  - Instagram: veces = (likes + comentarios) / (seguidores x 3%)  (3% ~ interaccion normal); confianza 'media'.
  Despues, puntaje.py los clasifica igual que a YouTube y entran al Director, al arsenal y a la Biblioteca (si hay video).

Uso:  python plataformas.py                         importa entrada.csv + todo lo que haya en datos/plataformas/*.json
      python plataformas.py importar export.json
      python plataformas.py instagram --tema cafe    (hashtags top+recientes del tema + cuentas de referencia)
      python plataformas.py cuentas --tema cafe      (solo cuentas de referencia: outliers contra la mediana de cada cuenta)
      python plataformas.py instagram --tema todos   (todos los temas)
"""
import re, sys, csv, json, sqlite3, datetime as dt
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode

CEREBRO = Path("datos/cerebro.db")
DIR = Path("datos/plataformas")
HASHTAGS = {   # Instagram: cada idioma usa su cuenta (repers.en -> en, repers.es -> es); cada cuenta tiene 30 hashtags por semana
    "cafe": {"en": ["coffeefacts", "coffeetime", "barista"], "es": ["datosdecafe", "curiosidadesdelcafe", "cafeteria"]},
    "aliens": {"en": ["ufo", "aliens", "uap"], "es": ["ovni", "extraterrestres", "misterios"]},
    "gta": {"en": ["gta6", "gtavi", "gta6news"], "es": ["gta6español", "gta6latino", "gtavi"]},
    "suerte": {"en": ["angelnumbers", "numerology", "1111"], "es": ["numerologia", "numerosangelicales", "1111"]},
    "negocios": {"en": ["businessfacts", "entrepreneurstory"], "es": ["emprendimiento", "historiasdeempresas"]},
}

CUENTAS = DIR / "cuentas_ig.json"   # cuentas grandes por tema/idioma; el script avisa cuales no existen o no son Business/Creator
CUENTAS_INICIO = {
    "_nota": "Cuentas de Instagram de referencia por tema. Solo sirven cuentas Business/Creator. Agrega o borra libremente.",
    "cafe": {"en": ["jameshoffmann", "roasterdaily", "baristadaily", "bluebottle"], "es": []},
    "aliens": {"en": ["uapnow", "ancientaliens"], "es": []},
    "suerte": {"en": ["mysticmichaela"], "es": []},
    "gta": {"en": ["rockstargames"], "es": []},
    "negocios": {"en": [], "es": []},
}


def abrir():
    import puntaje as P
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS ig_uso (cuenta TEXT, hashtag TEXT, usado TEXT, PRIMARY KEY (cuenta, hashtag))""")
    P.migrar(c)
    return c


def id_de(plataforma, url):
    pats = {"tiktok": r"/video/(\d+)", "instagram": r"/(?:reel|p)/([\w-]+)", "youtube": r"(?:shorts/|v=)([\w-]{11})"}
    m = re.search(pats.get(plataforma, r"([\w-]{6,})$"), url or "")
    return f"{plataforma[:2]}_{m.group(1)}" if m else None


def normal(x):
    """Fila de cualquier fuente -> formato comun."""
    pl = (x.get("plataforma") or ("tiktok" if "tiktok" in str(x.get("url")) else "instagram" if "instagram" in str(x.get("url")) else "")).lower()
    def num(k):        # 1200000 · "1,2M" · "850K" · "1.5m" -> entero
        v = x.get(k)
        if isinstance(v, (int, float)):
            return int(v)
        t = str(v or "").strip().lower().replace(" ", "")
        m = re.match(r"^([\d.,]+)([kmb]?)$", t)
        if not m:
            return 0
        n = m.group(1)
        n = n.replace(",", ".") if m.group(2) and n.count(",") == 1 and "." not in n else n.replace(",", "")
        try:
            return int(float(n) * {"": 1, "k": 1e3, "m": 1e6, "b": 1e9}[m.group(2)])
        except ValueError:
            return 0
    vid = x.get("id") or id_de(pl, x.get("url"))
    if not pl or not vid:
        return None
    return {"id": vid if str(vid).startswith(pl[:2] + "_") else f"{pl[:2]}_{vid}", "plataforma": pl, "url": x.get("url"),
            "titulo": (x.get("titulo") or x.get("caption") or x.get("desc") or "")[:300], "autor": x.get("autor") or x.get("creator") or "",
            "seguidores": num("seguidores") or num("followers"), "vistas": num("vistas") or num("views") or num("plays"),
            "likes": num("likes"), "comentarios": num("comentarios") or num("comments"), "compartidos": num("compartidos") or num("shares"),
            "mediana_perfil": num("mediana_perfil"), "fecha": x.get("fecha") or x.get("timestamp") or "",
            "tema": x.get("tema") or "general", "idioma": x.get("idioma") or _idioma(x)}


def _idioma(x):
    import ganchos as G
    t = G.idioma_de(x.get("titulo") or x.get("caption") or x.get("desc") or "")
    return t if t in ("es", "en") else "en"


def guardar(c, filas, fuente):
    import ganchos as G
    n = 0
    ahora = dt.datetime.now(dt.timezone.utc).isoformat()
    for f in filter(None, map(normal, filas)):
        if f["plataforma"] == "instagram":
            inter = f["likes"] + f["comentarios"]
            if f["mediana_perfil"]:                      # Business Discovery: contra lo normal de ESA cuenta
                ratio = round(inter / max(f["mediana_perfil"], 1), 1)
            else:                                        # hashtag: sin autor -> 3% de seguidores (si los hay)
                ratio = round(inter / max(f["seguidores"] * 0.03, 1), 1) if f["seguidores"] else None
            alcance = f["vistas"] or (f["likes"] + f["comentarios"]) * 30
        else:
            ref = f["mediana_perfil"] or f["seguidores"]
            ratio = round(f["vistas"] / max(ref, 1), 1) if ref else None
            alcance = f["vistas"]
        if f["titulo"] and not G.escritura_latina(f["titulo"]):
            continue
        c.execute("""INSERT INTO virales (id, plataforma, canal_id, tema, idioma, titulo, descripcion, publicado, duracion, vistas, likes,
                     comentarios, mediana_canal, ratio, nivel, visto_primero, actualizado, subs_canal)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                     ON CONFLICT(id) DO UPDATE SET vistas=excluded.vistas, likes=excluded.likes, comentarios=excluded.comentarios,
                     ratio=excluded.ratio, actualizado=excluded.actualizado""",
                  (f["id"], f["plataforma"], f"{f['plataforma'][:2]}@{f['autor']}", f["tema"], f["idioma"], f["titulo"], f.get("url") or "",
                   f["fecha"] or ahora, None, alcance, f["likes"], f["comentarios"], f["mediana_perfil"] or f["seguidores"], ratio,
                   "plataforma", ahora, ahora, f["seguidores"]))
        n += 1
    c.commit()
    print(f"   📥 {n} videos de {fuente} al cerebro", flush=True)
    return n


def importar(path):
    p = Path(path)
    if p.suffix == ".csv":
        with open(p, newline="", encoding="utf-8") as fh:
            filas = [r for r in csv.DictReader(fh) if r.get("url") and not r["url"].startswith("#")]
    else:
        d = json.loads(p.read_text(encoding="utf-8"))
        filas = d if isinstance(d, list) else d.get("items") or d.get("data") or []
    return guardar(abrir(), filas, p.name)


def _conexion():
    sec = Path("secretos/instagram.json")
    if not sec.exists():
        sys.exit("⛔ Falta secretos/instagram.json. Corre:  python configurar_instagram.py")
    s = json.loads(sec.read_text())
    tok = s.get("token")
    cuentas = s.get("cuentas") or [{"ig_user_id": s.get("ig_user_id"), "usuario": s.get("usuario") or ""}]

    def cuenta_para(idi):
        return next((x for x in cuentas if (x.get("usuario") or "").lower().endswith("." + idi)), cuentas[0])

    def g(ruta, **p):
        """GET al Graph API con 2 reintentos si Meta da su error pasajero (code 1/2 o 5xx)."""
        import time
        from urllib.error import HTTPError
        for intento in range(3):
            try:
                return json.loads(urlopen("https://graph.facebook.com/v21.0/" + ruta + "?" + urlencode(dict(p, access_token=tok)), timeout=40).read())
            except HTTPError as e:
                cuerpo = e.read().decode(errors="ignore")[:300]
                pasajero = e.code >= 500 or '"code":1,' in cuerpo or '"code":2,' in cuerpo
                if pasajero and intento < 2:
                    time.sleep(4 * (intento + 1))
                    continue
                raise RuntimeError(cuerpo or str(e))
    return g, cuenta_para


CAMPOS = "id,caption,like_count,comments_count,media_type,media_product_type,permalink,timestamp"


def _es_video(m):
    return m.get("media_product_type") == "REELS" or m.get("media_type") == "VIDEO"


def instagram(tema):
    """Hashtags: top_media + recent_media. Cada idioma con su cuenta; cada cuenta respeta 30 hashtags unicos por 7 dias."""
    g, cuenta_para = _conexion()
    c = abrir()
    hace7 = (dt.datetime.now() - dt.timedelta(days=7)).isoformat()
    filas, vistos = [], set()
    tags = HASHTAGS.get(tema, {})
    for idi, lista in (tags.items() if isinstance(tags, dict) else [("en", tags)]):
        cu = cuenta_para(idi)
        uid, nombre = cu["ig_user_id"], cu.get("usuario") or cu["ig_user_id"]
        usados = {h for (h,) in c.execute("SELECT hashtag FROM ig_uso WHERE cuenta=? AND usado > ?", (nombre, hace7))}
        for h in lista:
            if h not in usados and len(usados) >= 30:
                print(f"   ⛔ @{nombre}: llegó a 30 hashtags esta semana (límite de Meta). Sigue la próxima semana.")
                break
            try:
                hid = g("ig_hashtag_search", user_id=uid, q=h)["data"][0]["id"]
            except Exception as e:
                print(f"   ⚠️ #{h} (@{nombre}): {str(e)[:160]}")
                continue
            c.execute("INSERT OR REPLACE INTO ig_uso VALUES (?,?,?)", (nombre, h, dt.datetime.now().isoformat()))
            usados.add(h)
            cuenta = {}
            for borde in ("top_media", "recent_media"):       # mismo hashtag = no gasta cupo extra
                try:
                    datos = g(f"{hid}/{borde}", user_id=uid, fields=CAMPOS, limit=50).get("data", [])
                except Exception as e:
                    print(f"   ⚠️ #{h} {borde}: {str(e)[:160]}")
                    continue
                n = 0
                for m in datos:
                    if _es_video(m) and m.get("id") not in vistos:
                        vistos.add(m.get("id"))
                        filas.append({"plataforma": "instagram", "url": m.get("permalink"), "id": m.get("id"), "titulo": m.get("caption") or "",
                                      "likes": m.get("like_count") or 0, "comentarios": m.get("comments_count") or 0,
                                      "fecha": m.get("timestamp"), "tema": tema, "idioma": idi})
                        n += 1
                cuenta[borde] = (len(datos), n)
            txt = " · ".join(f"{b.split('_')[0]} {t}→{v} reels" for b, (t, v) in cuenta.items())
            print(f"   #{h} [{idi}, @{nombre}]: {txt}", flush=True)
    c.commit()
    return guardar(c, filas, f"Instagram #{tema}")


def mediana(xs):
    xs = sorted(xs)
    return (xs[len(xs) // 2] if len(xs) % 2 else (xs[len(xs) // 2 - 1] + xs[len(xs) // 2]) / 2) if xs else 0


def cuentas(tema):
    """Business Discovery: ultimos 50 posts de cuentas grandes del nicho -> cada Reel contra la mediana de ESA cuenta (outliers reales)."""
    import time
    if not CUENTAS.exists():
        DIR.mkdir(parents=True, exist_ok=True)
        CUENTAS.write_text(json.dumps(CUENTAS_INICIO, indent=1, ensure_ascii=False), encoding="utf-8")
    lista = json.loads(CUENTAS.read_text(encoding="utf-8")).get(tema, {})
    if not any(lista.values()):
        print(f"   (sin cuentas de referencia para '{tema}' en {CUENTAS})")
        return 0
    g, cuenta_para = _conexion()
    c = abrir()
    filas = []
    for idi, usuarios in lista.items():
        uid = cuenta_para(idi)["ig_user_id"]
        for u in usuarios:
            campos = (f"business_discovery.username({u}){{username,followers_count,media_count,"
                      f"media.limit(50){{{CAMPOS}}}}}")
            try:
                bd = g(uid, fields=campos)["business_discovery"]
            except Exception as e:
                print(f"   ⚠️ @{u}: no disponible (no existe o no es Business/Creator) · {str(e)[:90]}")
                continue
            posts = (bd.get("media") or {}).get("data", [])
            reels = [m for m in posts if _es_video(m) and "like_count" in m]   # sin like_count = likes ocultos
            if len(reels) < 5:
                print(f"   @{u}: {len(reels)} reels con likes visibles (muy pocos para medir)")
                continue
            med = mediana([(m.get("like_count") or 0) + (m.get("comments_count") or 0) for m in reels])
            top = 0
            for m in reels:
                inter = (m.get("like_count") or 0) + (m.get("comments_count") or 0)
                top = max(top, inter / max(med, 1))
                filas.append({"plataforma": "instagram", "url": m.get("permalink"), "id": m.get("id"), "titulo": m.get("caption") or "",
                              "likes": m.get("like_count") or 0, "comentarios": m.get("comments_count") or 0, "fecha": m.get("timestamp"),
                              "autor": bd.get("username") or u, "seguidores": bd.get("followers_count") or 0,
                              "mediana_perfil": int(med) or 1, "tema": tema, "idioma": idi})
            print(f"   @{u} [{idi}]: {bd.get('followers_count', 0):,} seguidores · {len(reels)} reels · mediana {int(med):,} · mejor ×{top:.1f}", flush=True)
            time.sleep(2)       # Business Discovery tiene limite por hora: sin apuro
    return guardar(c, filas, f"Instagram cuentas #{tema}")


def main():
    a = sys.argv[1:]
    DIR.mkdir(parents=True, exist_ok=True)
    ent = DIR / "entrada.csv"
    if not ent.exists():
        ent.write_text("plataforma,url,tema,idioma,vistas,likes,comentarios,compartidos,seguidores,titulo\n"
                       "# ej: tiktok,https://www.tiktok.com/@x/video/123,cafe,en,1200000,90000,800,5000,15000,Why coffee...\n", encoding="utf-8")
    if a and a[0] == "importar":
        importar(a[1])
    elif a and a[0] in ("instagram", "cuentas"):
        t = a[a.index("--tema") + 1] if "--tema" in a else "cafe"
        temas = [k for k in HASHTAGS] if t == "todos" else [t]
        for tm in temas:
            print(f"📸 Instagram · {tm}", flush=True)
            if a[0] == "instagram" and "--solo-cuentas" not in a:
                instagram(tm)
            cuentas(tm)
    else:
        importar(ent)
        for f in sorted(DIR.glob("*.json")):
            importar(f)
    import puntaje as P
    P.clasificar(abrir())
    print("✅ Listo: los videos de TikTok/Instagram ya cuentan en el 📡 Radar y el 🧠 Director", flush=True)


if __name__ == "__main__":
    main()
