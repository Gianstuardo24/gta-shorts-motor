"""ANALISIS COMPLETO: un solo comando que hace todo y va guardando lo aprendido (el "cerebro" crece cada dia).

  1. Nuestros videos: hook, palanca, vistas a 24 h, % visto.
  2. Busca en YouTube (API oficial, ES + EN, todos los temas) y RECORRE los canales que encuentra:
     cada Short se compara con lo NORMAL DE SU CANAL (mediana de sus ultimos Shorts).
  3. Guarda todo en datos/cerebro.db (canales, virales, corridas): cada corrida suma, nada se repite.
  4. Los MEJORES de los mejores (x20 o mas y 100.000+ vistas; primero los x100+) se bajan y Claude los mira
     en profundidad (motor de la Biblioteca), DE A 1, con pausas y control de temperatura. Solo para entender:
     nunca se usa su material.
  5. Expertos de marketing: videos de estrategia de canales grandes (200k+ subs), 2 por corrida, se acumulan.
  6. Cierra el ciclo: formulas y hooks por tema (patrones.py, hooks.py) + REGLAS VIGENTES (datos/estrategia/reglas_vigentes.md).
     lote.py las inyecta solas al guionista: lo aprendido se USA en los proximos guiones.
  7. Un informe: veredicto, que hace la diferencia en los top, psicologia del gancho, plantillas e ideas por canal.

Uso (cd ~/gta-shorts && source venv/bin/activate):
  python analisis.py                 completo (con pausas; tope 3 h por corrida: lo que falte queda en cola)
  python analisis.py --rapido        sin bajar videos (~8-10 min)
  python analisis.py --horas 6       mas tiempo (ideal de noche)
Opciones: --min-ratio 20  --min-vistas 100000  --cuota 4000 (unidades de YouTube por corrida)
Resultado: Estudio > 📡 Radar  (datos/estrategia/6-analisis.md) + historial en analisis/
"""
import re, sys, json, time, random, sqlite3, argparse, statistics, subprocess, datetime as dt
from collections import Counter
from pathlib import Path

import ganchos as G
import puntaje as P
import clasificar as C

CEREBRO = Path("datos/cerebro.db")
INFORME = Path("datos/estrategia/6-analisis.md")
HIST = Path("analisis")
TEMA_BIBLIOTECA = {"gta": "gta6", "aliens": "rabbit", "negocios": "mdm", "cafe": "cafe", "suerte": "suerte"}
BUSQUEDAS = {   # se rotan 3 por dia por tema e idioma, para ir descubriendo canales nuevos
    "gta": {"es": ["GTA 6", "GTA 6 guía", "GTA 6 trucos", "GTA 6 dinero rápido", "GTA 6 secretos", "GTA 6 consejos", "GTA 6 detalles", "GTA 6 easter egg"],
            "en": ["GTA 6", "GTA 6 guide", "GTA 6 tips", "GTA 6 money", "GTA 6 cheats", "GTA 6 secrets", "GTA 6 details", "GTA 6 easter egg"]},
    "aliens": {"es": ["ovni", "extraterrestres", "alienígenas", "ovni grabado", "misterio espacio", "señal extraterrestre"],
               "en": ["UFO", "aliens", "UFO caught on camera", "alien signal", "UAP", "space mystery"]},
    "cafe": {"es": ["café curiosidades", "historia del café", "datos del café", "café barista", "tipos de café", "por qué el café"],
             "en": ["coffee facts", "coffee history", "barista tips", "why coffee", "coffee explained", "coffee myths"]},
    "suerte": {"es": ["mensaje del universo", "señal de suerte", "si ves este video", "mensaje para ti hoy", "11:11", "tu señal"],
               "en": ["sign from the universe", "if you see this video", "message for you today", "11:11", "lucky sign", "this is your sign"]},
    "negocios": {"es": ["error de empresa", "empresa quebró", "peor decisión negocio", "historia de empresa", "error millonario", "marca fracasó"],
                 "en": ["business mistake", "billion dollar mistake", "company went bankrupt", "worst business decision", "brand failed", "business story"]},
}
EXPERTOS = {"en": ["YouTube Shorts strategy", "how to go viral on YouTube Shorts", "YouTube Shorts algorithm explained",
                    "short form video retention", "viral hooks short form", "faceless YouTube channel strategy",
                    "how to make viral Instagram Reels", "Instagram Reels algorithm", "sales psychology",
                    "marketing strategy that works", "copywriting hooks", "AI tools for content creators"],
            "es": ["estrategia YouTube Shorts", "cómo hacerse viral en Shorts", "algoritmo de YouTube Shorts", "retención en videos cortos",
                   "cómo hacer reels virales", "cómo vender más", "marketing digital estrategia", "herramientas de IA para creadores"]}
EXPERTOS_BUSQUEDAS = 2     # por idioma y corrida: rotan dia a dia (se acumulan)
EXPERTOS_SUBS = 200_000    # solo canales grandes (expertos con resultados propios)
EXPERTOS_POR_CORRIDA = 2   # videos largos: pesados, pocos por corrida (se acumulan dia a dia)
REGLAS = Path("datos/estrategia/reglas_vigentes.md")
VENTANA_DIAS = 60          # Shorts de los canales recorridos: solo los de los ultimos N dias
RESCANEAR_DIAS = 3         # un canal se vuelve a recorrer cada N dias
ORIGEN = {}                # canal_id -> como lo encontramos esta corrida (busqueda | destacado | lista)
PAUSA_ENTRE = 60           # segundos de descanso entre videos analizados
PAUSA_LARGA = (5, 300)     # cada 5 videos, 5 min de enfriamiento


def log(m):
    print(m, flush=True)


# ---------------- memoria ----------------
def abrir():
    CEREBRO.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(CEREBRO)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS canales (id TEXT PRIMARY KEY, plataforma TEXT DEFAULT 'youtube', nombre TEXT, tema TEXT,
        idioma TEXT, subs INTEGER, mediana INTEGER, n_shorts INTEGER, recorrido TEXT);
    CREATE TABLE IF NOT EXISTS virales (id TEXT PRIMARY KEY, plataforma TEXT DEFAULT 'youtube', canal_id TEXT, tema TEXT,
        idioma TEXT, titulo TEXT, descripcion TEXT, publicado TEXT, duracion INTEGER, vistas INTEGER, likes INTEGER,
        comentarios INTEGER, mediana_canal INTEGER, ratio REAL, nivel TEXT, visto_primero TEXT, actualizado TEXT,
        biblioteca TEXT);
    CREATE TABLE IF NOT EXISTS corridas (fecha TEXT, modo TEXT, cuota INTEGER, canales INTEGER, shorts INTEGER,
        top INTEGER, top_top INTEGER, analizados INTEGER, minutos REAL);
    """)
    P.migrar(c)
    C.migrar(c)
    return c


def nivel(r, vistas, min_ratio, min_vistas):
    if r is None or vistas < min_vistas:
        return "normal"
    return "top_top" if r >= 100 else "top" if r >= min_ratio else "alto" if r >= 3 else "normal"


# ---------------- descubrir ----------------
CUOTA_REPARTO = {"conocidos": 0.65, "descubrir": 0.25, "reserva": 0.10}   # de la cuota de la corrida
DESCUBRIR_BUSQUEDA = 0.6      # dentro de "descubrir": 60 % busquedas por palabra, 40 % expansion por canales destacados
ARRANQUE_CANALES = 150        # mientras la lista del nicho tenga menos canales, se reparte 45 / 45 / 10


def _recorrer(c, cids, canales, min_ratio, min_vistas, tope, etiqueta):
    """Recorre canales (≈2-3 unidades cada uno) hasta gastar 'tope' de cuota."""
    hechos, tot = 0, 0
    for i in range(0, len(cids), 50):
        if G.CUOTA["u"] + 60 > tope:
            log(f"   ({etiqueta}: tope de cuota; el resto queda para la próxima corrida)")
            break
        r = G.get("channels", part="contentDetails,statistics,snippet", id=",".join(cids[i:i + 50]))
        for ch in r.get("items", []):
            if G.CUOTA["u"] + 3 > tope:
                break
            try:
                tot += recorrer_canal(c, ch, canales, min_ratio, min_vistas)
                hechos += 1
            except Exception as e:
                log(f"   ⚠️ canal {ch.get('id')}: {str(e)[:80]} (se salta)")
        c.commit()
        log(f"   {etiqueta}: {min(i + 50, len(cids))}/{len(cids)} canales · {tot} Shorts · cuota ≈ {G.CUOTA['u']}")
    return hechos, tot


def destacados(c, tope, maximo=150):
    """Canales que los canales del nicho muestran como parecidos (channelSections, 1 unidad c/u). Heredan el tema de quien los muestra."""
    fuentes = c.execute("""SELECT id, tema, idioma FROM canales WHERE nivel_canal IN ('dedicado','especializado')
                           AND destacados_revisado IS NULL ORDER BY confiable DESC, mediana DESC LIMIT ?""", (maximo,)).fetchall()
    nuevos = {}
    conocidos = {r[0] for r in c.execute("SELECT id FROM canales")}
    for cid, tema, idi in fuentes:
        if G.CUOTA["u"] + 2 > tope:
            break
        try:
            r = G.get("channelSections", part="contentDetails", channelId=cid)
            for sec in r.get("items", []):
                for x in (sec.get("contentDetails") or {}).get("channels") or []:
                    if x not in conocidos and x != cid:
                        nuevos.setdefault(x, (tema, idi))
        except Exception as e:
            log(f"   ⚠️ destacados de {cid}: {str(e)[:60]}")
        c.execute("UPDATE canales SET destacados_revisado=? WHERE id=?", (dt.datetime.now().isoformat(), cid))
    c.commit()
    return nuevos, len(fuentes)


def descubrir(c, cuota, min_ratio, min_vistas, max_canales=400, buscar=True):
    """Radar 2.0: cuota repartida 65 % canales conocidos del nicho · 25 % descubrir (busquedas + destacados) · 10 % reserva."""
    hoy = dt.date.today().toordinal()
    base = G.CUOTA["u"]
    n_lista = c.execute("SELECT COUNT(*) FROM canales WHERE nivel_canal IN ('dedicado','especializado')").fetchone()[0]
    reparto = dict(CUOTA_REPARTO)
    if n_lista < ARRANQUE_CANALES:            # arranque: la lista del nicho aun es chica → mas cuota para descubrir
        reparto.update(conocidos=0.45, descubrir=0.45)
        log(f"   (arranque: solo {n_lista} canales del nicho en la lista → 45 % de la cuota para descubrir)")
    tope_desc = base + cuota * reparto["descubrir"]
    tope_busq = base + cuota * reparto["descubrir"] * DESCUBRIR_BUSQUEDA
    hallados, canales = {}, {}
    desde = (G.AHORA - dt.timedelta(days=14)).strftime("%Y-%m-%dT%H:%M:%SZ")
    # --- 1) descubrir por busqueda: rota entre TODAS las combinaciones tema/idioma/frase (pocas por corrida) ---
    pares = [(t, idi, qs) for t, por in BUSQUEDAS.items() for idi, qs in por.items()]
    pares = pares[hoy % len(pares):] + pares[:hoy % len(pares)]          # cada dia empieza por otro tema/idioma
    combos = [(t, idi, qs[(hoy + r) % len(qs)]) for r in range(max(len(qs) for *_, qs in pares)) for t, idi, qs in pares]
    k0 = 0                                                                # ronda 1 = una frase por cada tema/idioma
    n_busq = 0
    if buscar:
        for k in range(len(combos)):
            if G.CUOTA["u"] + 100 > tope_busq:
                break
            tema, idi, q = combos[k]
            log(f"🔎 [{tema}/{idi}] {q}")
            n_busq += 1
            r = G.get("search", costo=100, part="snippet", q=q, type="video", videoDuration="short",
                      order="viewCount", publishedAfter=desde, maxResults=50, relevanceLanguage=idi)
            for it in r.get("items", []):
                sn = it.get("snippet", {})
                cid = sn.get("channelId")
                if not cid or sn.get("channelTitle", "").lower().replace(" ", "").startswith(tuple(G.NUESTRO)):
                    continue
                if not G.del_tema(tema, sn.get("title", ""), sn.get("description", "")):
                    continue                  # el video encontrado no es del tema: su canal no entra por este tema
                canales.setdefault(cid, (tema, idi))
                ORIGEN.setdefault(cid, "busqueda")
                if it.get("id", {}).get("videoId"):
                    hallados[it["id"]["videoId"]] = cid
    else:
        log("   (--sin-buscar: sin búsquedas por palabra; sigo con destacados y canales conocidos)")
    log(f"📺 Descubrir: {n_busq} búsquedas → {len(canales)} canales candidatos · cuota ≈ {G.CUOTA['u']}")
    mejor = {}
    info0 = G.videos_info(list(hallados))
    for vid, v in info0.items():
        cid = hallados.get(vid)
        if cid and G.segundos(v["contentDetails"]["duration"]) <= 180:
            mejor[cid] = max(mejor.get(cid, 0), int(v["statistics"].get("viewCount") or 0))
    limite = (dt.datetime.now() - dt.timedelta(days=RESCANEAR_DIAS)).isoformat()
    vistos = {r[0] for r in c.execute("SELECT id FROM canales WHERE recorrido > ?", (limite,))}
    nuevos = sorted([x for x in canales if x not in vistos and mejor.get(x, 0) >= 10_000], key=lambda x: -mejor.get(x, 0))[:max_canales]
    log(f"🧭 Canales nuevos de las búsquedas: {len(nuevos)}")
    h1, s1 = _recorrer(c, nuevos, canales, min_ratio, min_vistas, tope_desc, "búsqueda")
    # --- 2) descubrir por destacados de los canales del nicho (incluye los que se acaban de clasificar) ---
    dest, n_fuentes = destacados(c, tope_desc)
    dnuevos = [x for x in dest if x not in vistos and x not in canales][:max_canales]
    for cid in dnuevos:
        canales[cid] = dest[cid]
        ORIGEN.setdefault(cid, "destacado")
    log(f"🔗 Destacados de {n_fuentes} canales del nicho → {len(dnuevos)} canales nuevos")
    h1b, s1b = _recorrer(c, dnuevos, canales, min_ratio, min_vistas, tope_desc, "destacados")
    h1, s1 = h1 + h1b, s1 + s1b
    # --- 3) canales conocidos del nicho (65 %): dedicados y especializados activos, los mas confiables primero ---
    tope_con = G.CUOTA["u"] + cuota * reparto["conocidos"]
    con = c.execute("""SELECT id, tema, idioma FROM canales WHERE nivel_canal IN ('dedicado','especializado')
                       AND COALESCE(activo,1)=1 AND recorrido <= ? ORDER BY confiable DESC, mediana DESC""", (limite,)).fetchall()
    for cid, tema, idi in con:
        canales[cid] = (tema, idi)
        ORIGEN.setdefault(cid, "lista")
    log(f"📚 Canales conocidos del nicho para re-revisar: {len(con)}")
    h2, s2 = _recorrer(c, [x[0] for x in con], canales, min_ratio, min_vistas, tope_con, "conocidos")
    log(f"   reserva sin tocar: ≈{int(cuota * reparto['reserva'])} de cuota")
    return h1 + h2, s1 + s2


def recorrer_canal(c, ch, canales, min_ratio, min_vistas):
    if True:
            n_sh = 0
            cid = ch["id"]
            tema, idi = canales[cid]
            up = ch["contentDetails"]["relatedPlaylists"]["uploads"]
            pl = G.get("playlistItems", part="contentDetails", playlistId=up, maxResults=50)
            ids = [x["contentDetails"]["videoId"] for x in pl.get("items", [])]
            info = G.videos_info(ids)
            shorts = []
            for vid, v in info.items():
                d = G.segundos(v["contentDetails"]["duration"])
                if 0 < d <= 180:
                    shorts.append((vid, v, d))
            vs = [int(v["statistics"].get("viewCount") or 0) for _, v, _ in shorts]
            med = int(statistics.median(vs)) if len(vs) >= 5 else None
            perfil = C.perfil_canal(tema, [v["snippet"] for _, v, _ in shorts])      # % del tema en sus ULTIMOS 30 Shorts
            subs = int(ch["statistics"].get("subscriberCount") or 0)
            previo = c.execute("SELECT origen FROM canales WHERE id=?", (cid,)).fetchone()
            c.execute("""INSERT OR REPLACE INTO canales (id, plataforma, nombre, tema, idioma, subs, mediana, n_shorts, recorrido,
                         pct_tema, pct_tema_previo, nivel_canal, ultima_pub, activo, confiable, origen, rel_rendimiento, destacados_revisado)
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,(SELECT destacados_revisado FROM canales WHERE id=?))""",
                      (cid, "youtube", ch["snippet"]["title"], tema, idi, subs, med, len(vs), dt.datetime.now().isoformat(),
                       perfil["pct"], perfil["pct_previo"], perfil["nivel"], perfil["ultima_pub"], perfil["activo"],
                       None if perfil["pct"] is None else round(perfil["pct"] * (1 if perfil["activo"] else 0.5), 2),
                       (previo[0] if previo and previo[0] else ORIGEN.get(cid, "busqueda")),
                       round(med / max(subs, 1), 3) if med else None, cid))
            if not med:
                return 0
            for vid, v, d in shorts:
                sn, st = v["snippet"], v["statistics"]
                pub = G.fecha(sn["publishedAt"])
                if (G.AHORA - pub).days > VENTANA_DIAS:
                    continue
                clase, cinfo = C.clasificar_video(tema, perfil["nivel"], sn)      # tema / dudoso / transversal (capa 1)
                if not G.escritura_latina(sn["title"]):       # otro idioma/escritura: no es ES ni EN
                    continue
                idi_v = G.idioma_video(sn, idi)                 # idioma del VIDEO, no del canal
                if not idi_v:
                    continue
                vistas = int(st.get("viewCount") or 0)
                otros = [x for x in vs if x != vistas]
                m2 = int(statistics.median(otros)) if len(otros) >= 4 else med
                ratio = round(vistas / max(m2, 1), 1)
                n_sh += 1
                c.execute("""INSERT INTO virales (id, plataforma, canal_id, tema, idioma, titulo, descripcion, publicado, duracion,
                    vistas, likes, comentarios, mediana_canal, ratio, nivel, visto_primero, actualizado, clase, clase_info, subtema, tema_buscado)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(id) DO UPDATE SET vistas=excluded.vistas, likes=excluded.likes, comentarios=excluded.comentarios,
                    mediana_canal=excluded.mediana_canal, ratio=excluded.ratio, nivel=excluded.nivel, idioma=excluded.idioma,
                    actualizado=excluded.actualizado, subtema=excluded.subtema,
                    clase=CASE WHEN COALESCE(json_extract(virales.clase_info,'$.capa'),1) >= 2 THEN virales.clase ELSE excluded.clase END,
                    clase_info=CASE WHEN COALESCE(json_extract(virales.clase_info,'$.capa'),1) >= 2 THEN virales.clase_info ELSE excluded.clase_info END,
                    tema=CASE WHEN COALESCE(json_extract(virales.clase_info,'$.capa'),1) >= 2 THEN virales.tema ELSE excluded.tema END""",
                          (vid, "youtube", cid, C.tema_guardado(tema, clase), idi_v, sn["title"], sn.get("description", "")[:300], sn["publishedAt"], d,
                           vistas, int(st.get("likeCount") or 0), int(st.get("commentCount") or 0), m2, ratio,
                           nivel(ratio, vistas, min_ratio, min_vistas), dt.datetime.now().isoformat(), dt.datetime.now().isoformat(),
                           clase, json.dumps(cinfo, ensure_ascii=False),
                           C.subtema(tema, sn["title"], sn.get("description", "")[:300], " ".join(sn.get("tags") or [])), tema))
                P.foto(c, vid, vistas, int(st.get("likeCount") or 0), int(st.get("commentCount") or 0))
            return n_sh


# ---------------- expertos de marketing ----------------
def expertos(c, cuota):
    """Busca videos de estrategia de canales GRANDES (200k+ subs) con muchas vistas. Van a la Biblioteca en modo tutorial."""
    hoy = dt.date.today().toordinal()
    desde = (G.AHORA - dt.timedelta(days=730)).strftime("%Y-%m-%dT%H:%M:%SZ")
    ids = []
    for idi, qs in EXPERTOS.items():
        if G.CUOTA["u"] + 100 > cuota:
            break
        for j in range(EXPERTOS_BUSQUEDAS):
            if G.CUOTA["u"] + 100 > cuota:
                break
            q = qs[(hoy * EXPERTOS_BUSQUEDAS + j) % len(qs)]
            log(f"🎓 Expertos [{idi}] {q}")
            r = G.get("search", costo=100, part="snippet", q=q, type="video", order="viewCount", publishedAfter=desde,
                      maxResults=25, relevanceLanguage=idi)
            ids += [it["id"]["videoId"] for it in r.get("items", []) if it.get("id", {}).get("videoId")]
    info = G.videos_info(list(dict.fromkeys(ids)))
    cids = list({v["snippet"]["channelId"] for v in info.values()})
    subs = {}
    for i in range(0, len(cids), 50):
        r = G.get("channels", part="statistics", id=",".join(cids[i:i + 50]))
        subs.update({x["id"]: int(x["statistics"].get("subscriberCount") or 0) for x in r.get("items", [])})
    out = []
    for vid, v in info.items():
        d = G.segundos(v["contentDetails"]["duration"])
        s_ = subs.get(v["snippet"]["channelId"], 0)
        if s_ >= EXPERTOS_SUBS and 180 < d <= 3600:
            out.append({"id": vid, "url": f"https://www.youtube.com/watch?v={vid}", "tema": "estrategia_youtube", "tipo": "Largo",
                        "titulo": v["snippet"]["title"], "vistas": int(v["statistics"].get("viewCount") or 0), "veces": None,
                        "categoria": "experto", "subs": s_, "canal": v["snippet"]["channelTitle"]})
    out.sort(key=lambda x: -x["vistas"])
    log(f"   {len(out)} videos de expertos (canales 200k+ subs)")
    return out


# ---------------- fuentes de DATOS para guias de GTA (no imagenes) ----------------
def fuentes_gta(cuota):
    """Guias/walkthroughs largos con muchas vistas -> la Biblioteca lee sus subtitulos y extrae datos con minuto (confirmado/rumor).
    Solo para APRENDER los datos; nunca se usan sus imagenes. Van con tema gta6 para que el guionista los reciba solo."""
    desde = (G.AHORA - dt.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    ids = []
    for q, l in (("GTA 6 guide", "en"), ("GTA 6 guía", "es")):
        if G.CUOTA["u"] + 100 > cuota:
            break
        r = G.get("search", costo=100, part="snippet", q=q, type="video", videoDuration="medium", order="viewCount",
                  publishedAfter=desde, maxResults=15, relevanceLanguage=l)
        ids += [it["id"]["videoId"] for it in r.get("items", []) if it.get("id", {}).get("videoId")]
    out = []
    for vid, v in G.videos_info(ids).items():
        if G.GTA.search(v["snippet"]["title"]) and G.escritura_latina(v["snippet"]["title"]):
            out.append({"id": vid, "url": f"https://www.youtube.com/watch?v={vid}", "tema": "gta6", "tipo": "Largo",
                        "titulo": v["snippet"]["title"], "vistas": int(v["statistics"].get("viewCount") or 0), "veces": None, "categoria": "guia"})
    out.sort(key=lambda x: -x["vistas"])
    log(f"📘 {len(out)} guías de GTA como fuente de datos (se leen los subtítulos, no se usan imágenes)")
    return out[:6]


# ---------------- analisis profundo (motor de la Biblioteca) ----------------
def caliente():
    """True si macOS esta limitando la CPU por temperatura."""
    try:
        t = subprocess.run(["pmset", "-g", "therm"], capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return False
    m = re.search(r"CPU_Speed_Limit\s*=\s*(\d+)", t)
    return bool(m and int(m.group(1)) < 100) or bool(re.search(r"thermal warning level.*[1-9]", t, re.I))


def enfriar():
    espera = 0
    while caliente() and espera < 30 * 60:
        log("🌡️  El Mac está caliente: espero 3 min a que se enfríe...")
        time.sleep(180)
        espera += 180


def profundo(c, min_ratio, min_vistas, horas, expertos_nuevos=()):
    import biblioteca as B
    bd = B.abrir_bd()
    hechos = B.ya_analizados(bd)
    B.encolar(bd, [e for e in expertos_nuevos if e["id"] not in hechos][:EXPERTOS_POR_CORRIDA * 3], None)
    colas = P.seleccion(c, min_ratio, min_vistas, excluir=hechos)
    if colas["dudoso"]:                       # capa 2: resolver los dudosos ANTES de gastar fichas
        import verificar as V
        a_tema, a_trans = V.verificar(c, colas["dudoso"])
        colas["tema"] = sorted(colas["tema"] + a_tema, key=lambda x: (-(x["ratio"] or 0) if (x["ratio"] or 0) >= 100 else 0,
                                                                     -(x.get("puntaje") or 0)))
        espacio = max(0, 10 - len(colas["transversal"]))
        colas["transversal"] += sorted(a_trans, key=lambda x: -(x["ratio"] or 0))[:espacio]
    cand = colas["tema"] + colas["transversal"]          # del tema primero; transversales (otro nicho, max 10) despues
    nuevos = [{"id": x["id"], "url": f"https://www.youtube.com/shorts/{x['id']}",
               "tema": "transversal" if x["clase"] == "transversal" else TEMA_BIBLIOTECA.get(x["tema"], x["tema"]),
               "tipo": "Short", "titulo": x["titulo"], "vistas": x["vistas"], "veces": x["ratio"],
               "categoria": "transversal" if x["clase"] == "transversal" else "viral", "puntaje": x["puntaje"]} for x in cand]
    orden = {x["id"]: len(cand) - k for k, x in enumerate(cand)}     # el orden de seleccion manda
    B.encolar(bd, nuevos, None)
    for x in colas["transversal"]:            # si ya estaba en la cola como 'viral', pasa a transversal
        bd.execute("UPDATE cola SET categoria='transversal', tema='transversal' WHERE id=? AND estado IN ('pendiente','preparado')", (x["id"],))
    bd.commit()
    todo = B.de_la_cola(bd, "pendiente") + B.de_la_cola(bd, "preparado")
    cola = [v for v in todo if v["id"] in orden or (v.get("categoria") == "viral" and (v.get("veces") or 0) >= min_ratio)]
    cola.sort(key=lambda v: -orden.get(v["id"], 0))
    cola += [v for v in todo if v.get("categoria") == "experto"][:EXPERTOS_POR_CORRIDA]
    cola += [v for v in todo if v.get("categoria") == "guia"][:3]
    n100 = sum(1 for x in colas["tema"] if (x["ratio"] or 0) >= 100)
    log(f"🔬 Para mirar a fondo: {len(cola)} · 🎯 del tema {len(colas['tema'])} (primero los x100+: {n100}, intercalando subtemas) · "
        f"🌐 transversales {len(colas['transversal'])} · tope {horas} h")
    fin, hechos_hoy, formulas = time.time() + horas * 3600, [], {}
    for n, v in enumerate(cola, 1):
        if time.time() > fin:
            log(f"⏱️  Tope de {horas} h: quedan {len(cola) - n + 1} en cola para la próxima corrida.")
            break
        enfriar()
        log(f"[{n}/{len(cola)}] {'🌐 ' if v.get('categoria') == 'transversal' else ''}x{v.get('veces')} · {(v.get('titulo') or v['id'])[:60]}")
        try:
            est = bd.execute("SELECT estado FROM cola WHERE id=?", (v["id"],)).fetchone()[0]
            if est == "pendiente":
                estado, err = B.preparar_uno(v)
                if estado != "preparado":
                    nint = bd.execute("SELECT intentos FROM cola WHERE id=?", (v["id"],)).fetchone()[0]
                    B.marcar(bd, v["id"], "error" if nint >= 2 else "pendiente", err, intento=True)
                    log(f"   ⚠️ {err}")
                    continue
                B.marcar(bd, v["id"], "preparado")
            tema = v.get("tema")
            formulas.setdefault(tema, B.formulas_conocidas(bd, tema))
            r = B.observar_uno(v, formulas[tema])
            if not r:
                B.marcar(bd, v["id"], "preparado", "ficha invalida", intento=True)
                continue
            real = ((r.get("ficha") or {}).get("tema_real") or "").split(":")[0].strip().lower()
            esperado = C.BIB_TEMA.get(tema)
            if v.get("categoria") == "viral" and esperado and real and real != esperado:      # capa 3: no era del tema
                r["v"]["tema"], r["v"]["categoria"] = "transversal", "transversal"
                C.marcar(c, v["id"], "transversal", esperado, 3, None, ["ficha"], real, "la ficha vio el video completo")
                log(f"   ↪️ la ficha dice que es de '{real}', no de '{esperado}': queda como 🌐 transversal")
                tema = "transversal"
            B.guardar(bd, tema, r)
            B.marcar(bd, v["id"], "analizado")
            import shutil
            shutil.rmtree(B.PREP / v["id"], ignore_errors=True)
            c.execute("UPDATE virales SET biblioteca='analizado' WHERE id=?", (v["id"],))
            c.commit()
            hechos_hoy.append(v.get("tema"))
            log(f"   ✅ ficha lista ({len(hechos_hoy)})")
        except B.Bloqueo:
            log("⏸️  YouTube frenó las descargas: pausa de 30 min.")
            time.sleep(1800)
        except B.LimiteClaude:
            log("⏸️  Se acabó el uso de Claude por ahora: lo preparado queda guardado para la próxima corrida.")
            break
        except Exception as e:
            log(f"   ⚠️ {str(e)[:150]}")
        time.sleep(PAUSA_LARGA[1] if len(hechos_hoy) and len(hechos_hoy) % PAUSA_LARGA[0] == 0 else PAUSA_ENTRE)
    B.shutil.rmtree(B.TEMP, ignore_errors=True) if hasattr(B, "shutil") else None
    return hechos_hoy


def cerrar_ciclo(temas):
    """Lo nuevo de la Biblioteca se destila en formulas y hooks: lote.py los inyecta solos al guionista."""
    for t in sorted({t for t in temas if t and t != "estrategia_youtube"}):
        for script in ("patrones.py", "hooks.py"):
            log(f"   🔁 {script} --tema {t}")
            try:
                subprocess.run([sys.executable, script, "--tema", t], timeout=1800)
            except Exception as e:
                log(f"   ⚠️ {script} {t}: {e}")


def consejos_expertos():
    p = Path("datos/inteligencia.db")
    if not p.exists():
        return []
    b = sqlite3.connect(p)
    out = []
    for ti, ca, f in b.execute("SELECT titulo, canal, ficha FROM analisis WHERE tema='estrategia_youtube' ORDER BY fecha DESC LIMIT 25"):
        try:
            f = json.loads(f or "{}")
        except Exception:
            continue
        tec = "; ".join(f"{t.get('nombre')}: {' > '.join(t.get('pasos') or [])} ({t.get('evidencia')})" for t in (f.get("tecnicas") or [])[:8])
        aju = "; ".join(f"{x.get('ajuste')}: {x.get('recomendacion')}" for x in (f.get("ajustes_youtube") or [])[:5])
        out.append(f"- \"{ti}\" ({ca}): {f.get('resumen', '')} · tecnicas: {tec} · ajustes: {aju}"[:1500])
    return out


def actualizar_reglas(texto_informe, corrida):
    import reglas
    reglas.actualizar(texto_informe, consejos_expertos(), corrida)


def material_arsenal(t0, items=None, min_ratio=20):
    """Lo nuevo para el arsenal: fichas profundas recientes (o las mejores si t0=0), expertos, nuestros videos y titulos top."""
    partes = []
    p = Path("datos/inteligencia.db")
    if p.exists():
        b = sqlite3.connect(p)
        q = ("SELECT id, tema, categoria, titulo, veces, vistas, ficha FROM analisis WHERE fecha >= ? AND categoria != 'control' ORDER BY veces DESC LIMIT 40"
             if t0 else "SELECT id, tema, categoria, titulo, veces, vistas, ficha FROM analisis WHERE categoria != 'control' ORDER BY COALESCE(veces,0) DESC LIMIT 40")
        for i, t, cat, ti, ve, vi, f in b.execute(q, (t0,) if t0 else ()):
            try:
                f = json.loads(f or "{}")
            except Exception:
                continue
            if t == "estrategia_youtube":
                tec = "; ".join(f"{x.get('nombre')}: {' > '.join(x.get('pasos') or [])} ({x.get('evidencia')})" for x in (f.get("tecnicas") or [])[:10])
                partes.append(f"- EXPERTO \"{ti}\": {f.get('resumen', '')} · tecnicas: {tec}"[:2500])
            else:
                clave = {k: f.get(k) for k in ("hook", "estructura", "emocion", "edicion", "texto_pantalla", "audio", "payoff", "loop",
                                                 "interaccion", "formula", "hipotesis_viral", "curva", "contraste_con_lo_normal")}
                partes.append(f"- TOP [{t}] id {i} \"{ti}\" x{ve} · {vi or 0:,} vistas · " + json.dumps(clave, ensure_ascii=False)[:2500])
    for it in sorted(items or [], key=lambda x: -(x.get("ratio") or 0)):
        if it["origen"] == "externo" and (it.get("ratio") or 0) >= min_ratio:
            partes.append(f"- TITULO TOP [{it['tema']}/{it['idioma']}] id {it['id']} x{it['ratio']} \"{it['titulo']}\" · palanca {it.get('palanca')} · "
                          f"estructura {it.get('estructura')} · mecanismo {it.get('mecanismo')}")
    pro = [i for i in items or [] if i["origen"] == "propio" and i.get("vistas_24h") is not None]
    pro.sort(key=lambda x: -x["vistas_24h"])
    for i in pro[:8] + pro[-5:]:
        partes.append(f"- NUESTRO [{i['canal']}] \"{i['titulo']}\" · hook: {i.get('hook')} · palanca {i.get('palanca')} · 24h {i['vistas_24h']} · %visto {i.get('pct_visto')}")
    return "\n".join(partes)


TEMA_DE_BIBLIOTECA = {v: k for k, v in TEMA_BIBLIOTECA.items()}


def limpiar_fuera_de_tema(c):
    """Radar 2.0: reevalua lo guardado con las reglas de clasificacion (canal + palabras). No se borra nada."""
    n, cuenta, m = C.reevaluar(c)
    log(f"🧹 Clasificación: {n} cambios · " + " · ".join(f"{k} {v}" for k, v in sorted(cuenta.items(), key=lambda x: -x[1]))
        + f" · {m} fichas/cola de la Biblioteca pasan a transversal")


def anatomia(min_ratio=20):
    """Anatomia temporal de los top (fichas v2): cuando llega la revelacion, cuantas preguntas abren/cierran, tension por tramo."""
    p = Path("datos/inteligencia.db")
    if not p.exists():
        return ""
    b = sqlite3.connect(p)
    por_tema = {}
    for tema, f in b.execute("SELECT tema, ficha FROM analisis WHERE tipo='Short' AND version >= 2 AND COALESCE(veces,0) >= ?", (min_ratio,)):
        try:
            f = json.loads(f or "{}")
        except Exception:
            continue
        cu, lt = f.get("curva") or {}, f.get("linea_temporal") or []
        d = por_tema.setdefault(tema, {"n": 0, "rev": [], "preg": [], "cvs": [], "tension": [[], [], [], []]})
        d["n"] += 1
        if isinstance(cu.get("revelacion_pct"), (int, float)):
            d["rev"].append(cu["revelacion_pct"])
        d["preg"].append(len(cu.get("preguntas") or []))
        if isinstance(cu.get("cambios_visuales_por_s"), (int, float)):
            d["cvs"].append(cu["cambios_visuales_por_s"])
        fin = max([x.get("hasta") or 0 for x in lt] + [1])
        for x in lt:
            if isinstance(x.get("tension"), (int, float)):
                q = min(int(4 * (x.get("desde") or 0) / fin), 3)
                d["tension"][q].append(x["tension"])
    med = lambda xs: round(statistics.median(xs), 1) if xs else "—"
    L = []
    for t, d in sorted(por_tema.items(), key=lambda x: -x[1]["n"]):
        L.append(f"- {t}: {d['n']} top con linea temporal · revelacion principal al {med(d['rev'])}% del video · "
                 f"{med(d['preg'])} preguntas abiertas · {med(d['cvs'])} cambios visuales/s · tension por cuartos: "
                 + " → ".join(str(med(q)) for q in d["tension"]))
    return "\n".join(L)


def fichas_top(min_ratio):
    p = Path("datos/inteligencia.db")
    if not p.exists():
        return []
    b = sqlite3.connect(p)
    filas = b.execute("SELECT id, tema, titulo, veces, vistas, ficha FROM analisis WHERE veces >= ? ORDER BY veces DESC LIMIT 60",
                      (min_ratio,)).fetchall()
    out = []
    for i, t, ti, ve, vi, f in filas:
        try:
            f = json.loads(f or "{}")
        except Exception:
            f = {}
        clave = {k: f.get(k) for k in ("hook", "idea_central", "angulo", "estructura", "emocion", "edicion", "texto_pantalla",
                                         "audio", "payoff", "loop", "interaccion", "formula", "hipotesis_viral", "para_nosotros",
                                         "linea_temporal", "curva", "contraste_con_lo_normal")}
        out.append(f"- [{t}] \"{ti}\" x{ve} · {vi:,} vistas · " + json.dumps(clave, ensure_ascii=False)[:2600])
    return out


INFORME_PROMPT = """Eres el director de estrategia de una fabrica de YouTube Shorts. Canales nuestros: GTA 6 en ES y EN (el juego YA
salio: solo tomas reales del juego, nada de expectativa), The Rabbit Loop (aliens, EN), MDM (negocios / quizas suerte, EN),
cafe (EN, formato 'But why?'). Te paso: (A) nuestros videos con hook y metricas; (B) los virales mejor rankeados por PUNTAJE COMPUESTO
(relativo, alcance, velocidad, impulso, reproducible), con sus TIPOS (outlier, breakout, evergreen, tendencia, reproducible), confianza
y palanca psicologica. Distingue SIEMPRE lo que es tendencia (no se replica) de lo reproducible (si se replica); trata con cautela la confianza baja; (C) fichas de observacion profunda de los top (hook, edicion,
texto en pantalla, audio, payoff, loop...); (D) resumen de la base acumulada.
Escribe en espanol, markdown esquematico (titulos, tablas, negritas), sin relleno, sin inventar datos:
1. **Veredicto del dia** (5 lineas).
2. **Que hace la diferencia en los TOP** (y no en los normales): patrones de hook, primer segundo, texto en pantalla, ritmo, audio,
   payoff, loop. Cada patron con 1-2 ejemplos reales (titulo + xN).
2b. **Anatomia temporal**: como se mueve la experiencia del espectador en los top (interrupcion → curiosidad → escalada → payoff
   → loop): en que % llega la revelacion, cuantas preguntas se abren y cuando se cierran, como sube la tension, que pasa cuando
   lo que se muestra agrega algo a lo que se dice. Compara por tema. Traduce a una plantilla de segundos para nuestros canales.
3. **Psicologia**: que palanca activan los top (curiosidad con hueco concreto, perdida de algo propio, FOMO 'otros ya lo tienen',
   escasez nueva y real, identidad, seleccion) y en que condicion funciona. Sin citar estudios que no te pase.
4. **Por tema e idioma**: tabla (tema, idioma, palanca que mas rinde, formato que mas rinde, ejemplo top). ES vs EN.
5. **Nuestros videos**: que funciono, que murio y por que, comparado con los top.
6. **Plantillas por canal** (GTA ES, GTA EN con angulo distinto, Rabbit aliens, MDM/suerte, cafe): 5 hooks + 1 estructura de
   9 frases cada uno, con la condicion de verdad que debe cumplirse.
7. **5 ideas de guion por canal** listas para producir (titulo, hook, palanca, de que top se inspira, que hacemos distinto).
8. **Pruebas de la semana**: 5 experimentos (variable, canal, metrica, cuantos videos).
9. **Alertas**: urgencia falsa, promesas, supersticion, contenido que no podemos usar. (Regla fija: nunca republicar el mismo video.)
Si algun tema tiene pocos datos, dilo.
PROFUNDIDAD Y PERSPECTIVA (obligatorio en cada afirmacion importante):
- Evidencia: cuantos casos y que tan fuertes (xN, vistas); separa lo observado de lo que interpretas.
- Contraste: compara los TOP con videos NORMALES del mismo canal o tema (si lo normal tambien lo hace, NO es lo que hizo la diferencia).
- Hipotesis alternativas: tema caliente, momento, canal grande, algoritmo, suerte. Di cual explica mejor y por que.
- Mecanismo: que pasa en la cabeza del espectador, segundo a segundo, y por que lo hace quedarse o compartir.
- Condicion y limite: cuando funciona, cuando falla, que lo refutaria.
- Confianza: alta / media / baja segun n y consistencia. Nada de generalidades ni frases de manual."""


def informe(c, items, nuevos_top, analizados, args, mins):
    top = c.execute("""SELECT v.id, CASE WHEN COALESCE(v.plataforma,'youtube')='youtube' THEN v.tema ELSE v.plataforma || ':' || v.tema END,
                       v.idioma, v.titulo, v.ratio, v.vistas, COALESCE(ca.nombre, v.canal_id), COALESCE(ca.subs, v.subs_canal), v.nivel, v.puntaje, v.tipos,
                       v.confianza, v.vph, v.aceleracion FROM virales v LEFT JOIN canales ca ON ca.id=v.canal_id
                       WHERE v.puntaje IS NOT NULL AND (v.tipos != '' OR v.nivel IN ('top','top_top')) AND substr(v.tema,1,2) != 'x_'
                       ORDER BY v.puntaje DESC LIMIT 150""").fetchall()
    etiq = {i["id"]: i for i in items}
    resumen = c.execute("""SELECT tema, idioma, COUNT(*), SUM(nivel='alto'), SUM(nivel='top'), SUM(nivel='top_top')
                           FROM virales WHERE substr(tema,1,2) != 'x_' GROUP BY tema, idioma""").fetchall()
    tot_c = c.execute("SELECT COUNT(*) FROM canales").fetchone()[0]
    pro = [i for i in items if i["origen"] == "propio"]
    A = "\n".join(f"- [{i['canal']}] \"{i['titulo']}\" · palanca {i.get('palanca')} · hook: {i.get('hook')} · 24h: {i.get('vistas_24h')} · "
                  f"total {i.get('vistas')} · %visto {i.get('pct_visto')}" for i in pro)
    B_ = "\n".join(f"- [{t}/{l}] puntaje {pt} · tipos {tp or '—'} · confianza {cf} · x{r} · {vi:,} vistas · {int(vph or 0):,}/h"
                   f"{f' · aceleracion {ac}' if ac is not None else ''} · canal {cn} ({cs} subs) · \"{ti}\" · palanca {etiq.get(i, {}).get('palanca')} · "
                   f"estructura {etiq.get(i, {}).get('estructura')} · mecanismo {etiq.get(i, {}).get('mecanismo')}"
                   for i, t, l, ti, r, vi, cn, cs, nv, pt, tp, cf, vph, ac in top)
    D = "\n".join(f"- {t}/{l}: {n} Shorts medidos · x3+ {a or 0} · x20+ {b or 0} · x100+ {cc or 0}" for t, l, n, a, b, cc in resumen)
    perf = "\n".join(f"- {f.stem}: " + f.read_text(encoding="utf-8")[:1500].replace("\n", " ")
                      for f in sorted(Path("datos/perfiles").glob("*.json"))) if Path("datos/perfiles").exists() else ""
    entrada = f"## (E) Perfiles de nuestros canales (no mezclar aprendizajes entre canales)\n{perf}\n\n## (A) Nuestros videos\n{A}\n\n## (B) Top y top top\n{B_}\n\n## (C) Fichas profundas\n" + "\n".join(fichas_top(args.min_ratio)) + "\n\n## (C2) Anatomia temporal de los top (por tema)\n" + anatomia(args.min_ratio) + f"\n\n## (D) Base acumulada ({tot_c} canales)\n{D}"
    log("✍️  Claude escribiendo el informe...")
    try:
        texto = G.claude(INFORME_PROMPT, entrada[:180000], timeout=1800)
    except Exception as e:
        texto = f"⚠️ No se pudo generar el informe: {e}"
    filas = "\n".join(f"| {pt} | {tp or '—'} | {t} | {l} | [{ti[:65]}](https://youtube.com/shorts/{i}) | x{r} | {vi:,} | {cf} | {etiq.get(i, {}).get('palanca') or '—'} |"
                      for i, t, l, ti, r, vi, cn, cs, nv, pt, tp, cf, vph, ac in top[:40])
    base = "\n".join(f"| {t} | {l} | {n} | {a or 0} | {b or 0} | {cc or 0} |" for t, l, n, a, b, cc in resumen)
    sello = dt.datetime.now().strftime("%d/%m %H:%M")
    md = (f"# 🧠 Análisis completo — {sello}\n\n_{'rápido' if args.rapido else 'completo'} · {mins:.0f} min · cuota ≈ {G.CUOTA['u']} · "
          f"{nuevos_top} top nuevos hoy · {len(analizados)} mirados en profundidad hoy · base: {tot_c} canales_\n\n{texto.strip()}\n\n"
          f"## 🔥 Top de la base por puntaje compuesto\n\n_puntaje = relativo 30% + alcance 25% + velocidad 15% + impulso 15% + reproducible 15% · "
          f"tipos: x1000+, x100+, outlier, breakout, evergreen, tendencia, reproducible · los x100+ se miran todos, de mayor a menor_\n\n| Puntaje | Tipos | Tema | Idioma | Video | Veces lo normal | Vistas | Confianza | Palanca |\n"
          f"|---|---|---|---|---|---|---|---|---|\n{filas}\n\n"
          f"## 🗄️ Lo que lleva acumulado el cerebro\n\n| Tema | Idioma | Shorts medidos | x3+ | x20+ | x100+ |\n|---|---|---|---|---|---|\n{base}\n\n"
          + G.tablas(items) + "\n")
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    INFORME.write_text(md, encoding="utf-8")
    an = anatomia(args.min_ratio)
    if an:     # referencia para revisar.py: como se mueve la experiencia en los top de cada tema
        (INFORME.parent / "anatomia.md").write_text("ANATOMIA TEMPORAL DE LOS TOP (fichas v2):\n" + an, encoding="utf-8")
    HIST.mkdir(exist_ok=True)
    (HIST / f"analisis_{dt.datetime.now():%Y%m%d_%H%M}.md").write_text(md, encoding="utf-8")
    return texto


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rapido", action="store_true")
    ap.add_argument("--horas", type=float, default=3)
    ap.add_argument("--min-ratio", type=float, default=20)
    ap.add_argument("--min-vistas", type=int, default=100_000)
    ap.add_argument("--cuota", type=int, default=4000)
    ap.add_argument("--comparar", action="store_true", help="prueba sin fichas: antes vs ahora con auditor ciego (~15 min) y termina")
    ap.add_argument("--sin-buscar", action="store_true", help="sin busquedas por palabra (igual expande por destacados y re-revisa los canales del nicho)")
    args = ap.parse_args()
    t0 = time.time()
    corrida = dt.datetime.now().isoformat(timespec="minutes")
    c = abrir()
    import procedencia as PR
    pv_inf = PR.version_prompt(c, "informe", INFORME_PROMPT)
    pv_eti = PR.version_prompt(c, "etiquetar", G.ETIQUETAR)
    c.commit()
    antes = c.execute("SELECT COUNT(*) FROM virales WHERE nivel IN ('top','top_top')").fetchone()[0]
    limpiar_fuera_de_tema(c)

    log("📊 1/5 Actualizando nuestras métricas...")
    try:
        subprocess.run([sys.executable, "metricas.py"], timeout=600)
    except Exception as e:
        log(f"   (métricas: {e}; sigo con lo guardado)")
    items = G.propios()
    log(f"   {len(items)} videos propios")
    try:      # TikTok / Instagram: links a mano, exports y muestras del navegador (datos/plataformas/)
        import plataformas
        plataformas.DIR.mkdir(parents=True, exist_ok=True)
        if (plataformas.DIR / "entrada.csv").exists():
            plataformas.importar(plataformas.DIR / "entrada.csv")
        for f in sorted(plataformas.DIR.glob("*.json")):
            plataformas.importar(f)
    except Exception as e:
        log(f"   (TikTok/Instagram: {str(e)[:80]})")

    log("🌐 2/5 Buscando en YouTube y recorriendo canales...")
    G.KEY = G._clave()
    try:
        ncan, nsh = descubrir(c, args.cuota, args.min_ratio, args.min_vistas, 120 if args.rapido else 400, buscar=not args.sin_buscar)
    except G.CuotaAgotada as e:
        c.commit()
        log(f"{e} → sigo con lo que ya está guardado (el análisis profundo no usa la API)")
        ncan, nsh = 0, 0
    log("📈 Re-midiendo virales conocidos (velocidad, aceleración, persistencia)...")
    try:
        log(f"   {P.seguimiento(c)} re-medidos · cuota ≈ {G.CUOTA['u']}")
    except G.CuotaAgotada:
        c.commit()
        log("   (sin cuota: no se re-miden hoy)")
    P.clasificar(c, args.min_ratio, args.min_vistas)
    tipos = Counter(t for (ts,) in c.execute("SELECT tipos FROM virales WHERE tipos != ''") for t in ts.split(","))
    log("   tipos: " + " · ".join(f"{k} {v}" for k, v in tipos.most_common()))
    tt = c.execute("SELECT COUNT(*) FROM virales WHERE nivel='top_top'").fetchone()[0]
    t_ = c.execute("SELECT COUNT(*) FROM virales WHERE nivel='top'").fetchone()[0]
    log(f"   {ncan} canales recorridos · {nsh} Shorts medidos · en la base: {tt} 🔥 x100+ y {t_} ⭐ x20-100")
    tot_c, niv_c = C.resumen(c)
    log("   🏷️  videos: " + " · ".join(f"{k} {v}" for k, v in sorted(tot_c.items(), key=lambda x: -x[1]))
        + " · canales: " + " · ".join(f"{k} {v}" for k, v in sorted(niv_c.items(), key=lambda x: -x[1])))
    if args.comparar:
        import verificar as V
        V.comparar(c)
        log(f"✅ Comparación lista en {(time.time() - t0) / 60:.0f} min: datos/estrategia/14-comparacion.md (no se hicieron fichas)")
        return

    log("🧲 3/5 Etiquetando ganchos (palanca, estructura, psicología)...")
    ya = sqlite3.connect(G.DB)
    try:
        etiquetados = {r[0] for r in ya.execute("SELECT id FROM ganchos WHERE origen='externo'")}
    except sqlite3.OperationalError:
        etiquetados = set()
    ya.close()
    ext = c.execute("""SELECT v.id, v.tema, v.idioma, v.titulo, v.descripcion, v.vistas, v.ratio, ca.nombre FROM virales v
                       LEFT JOIN canales ca ON ca.id=v.canal_id WHERE v.ratio >= 3 AND v.vistas >= ? ORDER BY v.ratio DESC LIMIT 400""",
                    (args.min_vistas // 4,)).fetchall()
    for i, t, l, ti, de, vi, r, cn in ext:
        items.append({"id": i, "origen": "externo", "tema": t, "idioma": l, "titulo": ti, "descripcion": de, "vistas": vi,
                      "ratio": r, "canal_nombre": cn, "hook": "", "texto_pantalla": ""})
    nuevos_et = [it for it in items if it["origen"] == "propio" or it["id"] not in etiquetados]
    for n, it in enumerate(items, 1):
        it["_n"] = n
    G.etiquetar(nuevos_et)
    viejos = {}
    try:
        ya = sqlite3.connect(G.DB)
        for row in ya.execute("SELECT id, palanca, palanca2, estructura, pregunta, mecanismo, en_juego, riesgo FROM ganchos WHERE origen='externo'"):
            viejos[row[0]] = dict(zip(("palanca", "palanca2", "estructura", "pregunta", "mecanismo", "en_juego", "riesgo"), row[1:]))
        ya.close()
    except sqlite3.OperationalError:
        pass
    for it in items:
        if it["origen"] == "externo" and it["id"] in viejos and not it.get("palanca"):
            it.update(viejos[it["id"]])
    G.guardar_db(nuevos_et)

    analizados = []
    if not args.rapido:
        try:
            exp = expertos(c, args.cuota + 300) + fuentes_gta(args.cuota + 500)
        except G.CuotaAgotada as e:
            log(f"{e} → hoy sin expertos ni guías nuevas; sigo con el análisis profundo")
            exp = []
        log("🔬 4/5 Mirando en profundidad los mejores de los mejores + expertos (de a 1, con pausas)...")
        analizados = profundo(c, args.min_ratio, args.min_vistas, args.horas, exp)
        cerrar_ciclo(analizados)
        try:
            import verificar as V
            V.auditar(c, 30)                  # control de calidad de la clasificacion (ciego, automatico)
        except Exception as e:
            log(f"   ⚠️ auditoría: {str(e)[:120]}")
    else:
        log("⏭️  4/5 Modo rápido: sin bajar videos.")

    log("🧠 5/5 Informe...")
    despues = c.execute("SELECT COUNT(*) FROM virales WHERE nivel IN ('top','top_top')").fetchone()[0]
    mins = (time.time() - t0) / 60
    texto = informe(c, items, despues - antes, analizados, args, mins)
    log("📏 Actualizando reglas (con procedencia)...")
    actualizar_reglas(texto, corrida)
    if not args.rapido:
        try:
            import vigia
            vigia.main()                      # se salta solo si la ultima tiene menos de 6 dias
        except Exception as e:
            log(f"⚠️ Vigía: {str(e)[:120]}")
    log("🗃️  Alimentando el arsenal...")
    import arsenal
    arsenal.alimentar(material_arsenal(t0, items, args.min_ratio), corrida)
    cols = {r[1] for r in c.execute("PRAGMA table_info(corridas)")}
    if "prompts" not in cols:
        c.execute("ALTER TABLE corridas ADD COLUMN prompts TEXT")
    c.execute("INSERT INTO corridas (fecha, modo, cuota, canales, shorts, top, top_top, analizados, minutos, prompts) VALUES (?,?,?,?,?,?,?,?,?,?)",
              (corrida, "rapido" if args.rapido else "completo", G.CUOTA["u"], ncan, nsh, t_, tt,
               len(analizados), round(mins, 1), json.dumps([pv_inf, pv_eti])))
    c.commit()
    log("🧠 Director: decisiones para mañana...")
    try:
        import director
        director.main()
    except Exception as e:
        log(f"   ⚠️ director: {e}")
    log(f"✅ Listo en {mins:.0f} min: Estudio > 🧠 Director y 📡 Radar")


if __name__ == "__main__":
    main()
