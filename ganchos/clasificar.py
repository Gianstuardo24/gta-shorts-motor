"""📡 RADAR 2.0 · CLASIFICACION: de que tema es cada video y que puede enseñar.

Tres tipos de video:
  - tema         → del nicho: alimenta la anatomia y el arsenal DE ESE TEMA.
  - transversal  → de otro nicho pero enorme: solo el arsenal GENERAL (ganchos, psicologia, estructura, ritmo),
                   marcado "de otro nicho: probar antes de confiar". Nunca se vuelve regla de un canal sin validarse en ese canal.
  - ruido        → anuncios pagados, otro idioma/escritura: no se analiza.
  (+ dudoso: aun no se sabe; la verificacion barata lo resuelve antes de gastar una ficha.)

Capas (de la mas barata a la mas cara):
  1. Canal + palabras (gratis): % del tema en sus ULTIMOS 30 Shorts → dedicado ≥80 % · especializado 60-79 % · mixto 40-59 % · no <40 %.
     El titulo/descripcion/tags nombran el tema → del tema. Si no lo nombran: dedicado → del tema; especializado → dudoso;
     mixto/no → transversal.
  2. Verificacion barata (solo dudosos que podrian ir a ficha): subtitulos automaticos + miniatura + 4 cuadros en 360p (se borra al tiro);
     Claude clasifica en lotes de 20. (verificar.py)
  3. La ficha confirma: el analista ve el video completo y devuelve tema_real; si no coincide, la ficha pasa a transversal.
Cada video guarda su MOTIVO (clase_info): tipo, confianza, evidencia, tema_real, capa que decidio.
Nada se borra: lo de otro tema queda como tema 'x_<tema>' (fuera de las consultas del tema) y se puede reevaluar.
"""
import re, json, sqlite3, statistics, datetime as dt
from pathlib import Path

import ganchos as G

ULTIMOS = 30                       # Shorts recientes que definen de que es un canal
NIVELES = [(0.80, "dedicado"), (0.60, "especializado"), (0.40, "mixto"), (0.0, "no_especializado")]
TEMA_BIB = {"gta": "gta6", "aliens": "rabbit", "negocios": "mdm", "cafe": "cafe", "suerte": "suerte"}
BIB_TEMA = {v: k for k, v in TEMA_BIB.items()}

# Subtemas por nicho (para diversidad): palabras → subtema. El primero que calza gana; sin calce → "otro".
SUBTEMAS = {
    "cafe": [("preparacion", r"latte|espresso|expreso|receta|recipe|how to make|c[oó]mo (hacer|preparar)|cold brew|v60|pour over|french press|aeropress|frapp|iced|helado|art"),
             ("equipos", r"machine|m[aá]quina|grinder|molinillo|cafetera|moka|kettle|tamper|portafilter"),
             ("ciencia", r"caffeine|cafe[ií]na|science|ciencia|why does|por qu[eé]|chemistry|qu[ií]mica|brain|cerebro|sleep|sue[ñn]o"),
             ("historia", r"history|historia|origin|origen|invent|ancient|antig|king|rey|ban|prohib"),
             ("cultura", r"italy|italia|japan|jap[oó]n|ethiopia|etiop|colombia|brazil|brasil|turkish|turco|vietnam|culture|cultura|country|pa[ií]s"),
             ("comparaciones", r"\bvs\.?\b|versus|differen|diferenc|types of|tipos de|ranking|tier"),
             ("errores", r"mistake|wrong|error|never|nunca|stop|deja de|myth|mito"),
             ("curiosidades", r"fact|dato|did you know|sab[ií]as|curios|secret|secreto")],
    "aliens": [("avistamientos", r"caught|grabad|footage|video|sighting|avistamiento|camera|c[aá]mara|pilot|piloto|sky|cielo"),
               ("gobierno", r"pentagon|pent[aá]gono|government|gobierno|congress|congreso|files|archivos|nasa says|whistleblow|declassif|desclasif|area\s*51"),
               ("espacio", r"nasa|planet|planeta|asteroid|asteroide|galax|telescope|telescopio|mars|marte|moon|luna|signal|se[ñn]al|space|espacio"),
               ("historia", r"ancient|antig|roswell|history|historia|pyramid|pir[aá]mide|1947|nazca"),
               ("teorias", r"theory|teor[ií]a|conspir|truth|verdad|hidden|oculto|real\b")],
    "gta": [("guias", r"guide|gu[ií]a|how to|c[oó]mo|tips|trucos|cheat|money|dinero|best way|mejor forma"),
            ("detalles", r"detail|detalle|easter|secret|secreto|hidden|oculto|noticed|notaste"),
            ("mapa", r"map|mapa|leonida|vice city|region|regi[oó]n|location|ubicaci"),
            ("comparacion", r"\bvs\.?\b|gta\s*5|gta\s*v\b|compar"),
            ("noticias", r"trailer|tr[aá]iler|release|lanzamiento|price|precio|leak|filtra|rockstar|news|noticia")],
    "suerte": [("numeros", r"\d{3,4}|11:11|angel number|n[uú]mero|numerolog"),
               ("mensajes", r"message|mensaje|sign|se[ñn]al|universe|universo|if you see|si ves"),
               ("rituales", r"manifest|ritual|affirm|afirmaci|law of attraction|ley de atracci"),
               ("suenos", r"dream|sue[ñn]o|so[ñn]ar")],
    "negocios": [("fracasos", r"fail|fracas|bankrupt|quiebra|quebr|mistake|error|lost|perdi|collapse"),
                 ("exitos", r"success|[eé]xito|billion|mill[oó]n|million|rich|rico|grew|creci"),
                 ("marcas", r"brand|marca|logo|company|empresa|ceo|founder|fundador"),
                 ("dinero", r"money|dinero|invest|inversi|stock|bolsa|price|precio")],
}
_SUB_RE = {t: [(n, re.compile(p, re.I)) for n, p in lst] for t, lst in SUBTEMAS.items()}


def subtema(tema, *textos):
    tema = (tema or "").removeprefix("x_")
    tx = " ".join(t for t in textos if t)
    for n, rx in _SUB_RE.get(tema, []):
        if rx.search(tx):
            return n
    return "otro"


def nivel_de(pct):
    if pct is None:
        return None
    return next(n for umbral, n in NIVELES if pct >= umbral)


def migrar(c):
    cols = {r[1] for r in c.execute("PRAGMA table_info(virales)")}
    for col, tipo in [("clase", "TEXT"), ("clase_info", "TEXT"), ("subtema", "TEXT"), ("tema_buscado", "TEXT")]:
        if col not in cols:
            c.execute(f"ALTER TABLE virales ADD COLUMN {col} {tipo}")
    cols = {r[1] for r in c.execute("PRAGMA table_info(canales)")}
    for col, tipo in [("pct_tema", "REAL"), ("pct_tema_previo", "REAL"), ("nivel_canal", "TEXT"), ("ultima_pub", "TEXT"),
                      ("activo", "INTEGER"), ("confiable", "REAL"), ("origen", "TEXT"), ("destacados_revisado", "TEXT"),
                      ("rel_rendimiento", "REAL")]:
        if col not in cols:
            c.execute(f"ALTER TABLE canales ADD COLUMN {col} {tipo}")
    c.execute("""CREATE TABLE IF NOT EXISTS auditoria (id TEXT, fecha TEXT, clase TEXT, capa TEXT, tema_objetivo TEXT,
                 tema_auditor TEXT, correcto INTEGER, motivo TEXT, PRIMARY KEY (id, fecha))""")
    c.commit()


def perfil_canal(tema, shorts):
    """shorts: [(snippet, ...)] del canal. Usa los ULTIMOS 30 por fecha. Devuelve dict con pct, nivel, tendencia, ultima_pub, activo."""
    orden = sorted(shorts, key=lambda s: s.get("publishedAt") or "", reverse=True)
    rec = orden[:ULTIMOS]
    hit = lambda s: G.del_tema(tema, s.get("title", ""), (s.get("description") or "")[:500], " ".join(s.get("tags") or []))
    pct = round(sum(map(hit, rec)) / len(rec), 2) if rec else None
    mitad = len(rec) // 2
    nuevo = round(sum(map(hit, rec[:mitad])) / mitad, 2) if mitad >= 5 else None      # los 15 mas recientes
    viejo = round(sum(map(hit, rec[mitad:])) / (len(rec) - mitad), 2) if mitad >= 5 else None
    ult = orden[0].get("publishedAt") if orden else None
    activo = None
    if ult:
        activo = int((G.AHORA - G.fecha(ult)).days <= 30)
    return {"pct": pct, "nivel": nivel_de(pct), "pct_reciente": nuevo, "pct_previo": viejo, "ultima_pub": ult, "activo": activo}


def clasificar_video(tema, nivel, sn):
    """Capa 1 (gratis). sn = snippet del video. Devuelve (clase, info)."""
    nombra = G.del_tema(tema, sn.get("title", ""), (sn.get("description") or "")[:500], " ".join(sn.get("tags") or []))
    ev = []
    if nombra:
        ev.append("vocabulario")
    if nivel:
        ev.append(f"canal_{nivel}")
    if nombra:
        clase, conf = "tema", 0.97 if nivel == "dedicado" else 0.9 if nivel == "especializado" else 0.8
    elif nivel == "dedicado":
        clase, conf = "tema", 0.8
    elif nivel == "especializado":
        clase, conf = "dudoso", 0.5
    else:
        clase, conf = "transversal", 0.75 if nivel in ("mixto", "no_especializado") else 0.6
    return clase, {"tema_objetivo": tema, "tipo": clase, "confianza": conf, "evidencia": ev, "tema_real": tema if clase == "tema" else None,
                   "capa": 1, "fecha": dt.date.today().isoformat()}


def tema_guardado(tema, clase):
    """tema que se guarda en virales: el del nicho si es del tema o dudoso; x_<tema> si es transversal."""
    return tema if clase in ("tema", "dudoso") else f"x_{tema}"


def reevaluar(c):
    """Aplica las reglas a lo ya guardado (incluidos los x_ de la limpieza anterior). Barato: usa la base, no la API.
    Nivel del canal: el guardado en canales; si falta, se estima con sus Shorts guardados (ultimos 30)."""
    migrar(c)
    filas = c.execute("""SELECT id, canal_id, tema, titulo, descripcion, publicado, clase, clase_info FROM virales
                         WHERE COALESCE(plataforma,'youtube')='youtube'""").fetchall()
    por_canal = {}
    for f in filas:
        por_canal.setdefault(f[1], []).append(f)
    niveles = {cid: n for cid, n in c.execute("SELECT id, nivel_canal FROM canales WHERE nivel_canal IS NOT NULL")}
    n_cambios, cuenta = 0, {}
    for cid, vs in por_canal.items():
        base = (vs[0][2] or "").removeprefix("x_")
        if base not in G.TEMAS_RE:
            continue
        nivel = niveles.get(cid)
        if not nivel:
            rec = sorted(vs, key=lambda f: f[5] or "", reverse=True)[:ULTIMOS]
            pct = sum(G.del_tema(base, f[3], f[4]) for f in rec) / len(rec)
            nivel = nivel_de(pct) if len(rec) >= 5 else None
            c.execute("UPDATE canales SET pct_tema=?, nivel_canal=? WHERE id=? AND nivel_canal IS NULL",
                      (round(pct, 2), nivel, cid))
        for vid, _, tema, tit, desc, _, clase0, info0 in vs:
            info0 = json.loads(info0 or "{}")
            if info0.get("capa", 1) >= 2:          # ya lo decidio una capa mas cara: no se pisa
                cuenta[clase0] = cuenta.get(clase0, 0) + 1
                continue
            clase, info = clasificar_video(base, nivel, {"title": tit, "description": desc})
            t = tema_guardado(base, clase)
            if clase != clase0 or t != tema:
                n_cambios += 1
            c.execute("UPDATE virales SET clase=?, clase_info=?, tema=?, tema_buscado=?, subtema=? WHERE id=?",
                      (clase, json.dumps(info, ensure_ascii=False), t, base, subtema(base, tit, desc), vid))
            cuenta[clase] = cuenta.get(clase, 0) + 1
    c.commit()
    # Biblioteca: fichas y cola de videos que resultaron transversales → tema 'transversal' (siguen ensenando, aparte)
    m = 0
    p = Path("datos/inteligencia.db")
    if p.exists():
        clases = {vid: (cl, (t or "").removeprefix("x_")) for vid, cl, t in c.execute("SELECT id, clase, tema FROM virales")}
        b = sqlite3.connect(p)
        for vid, tema_b, cat, est in b.execute("SELECT id, tema, categoria, estado FROM cola").fetchall():
            cl = clases.get(vid, (None,))[0]
            if cat == "viral" and cl == "transversal":
                b.execute("UPDATE cola SET categoria='transversal', tema='transversal', estado=CASE WHEN estado='fuera_de_tema' THEN 'pendiente' ELSE estado END WHERE id=?", (vid,))
                m += 1
            elif est == "fuera_de_tema" and cl in ("tema", "dudoso"):            # la limpieza anterior se equivoco: vuelve
                b.execute("UPDATE cola SET estado='pendiente' WHERE id=?", (vid,))
        for vid, tema_b in b.execute("SELECT id, tema FROM analisis WHERE categoria='viral' OR tema LIKE 'x_%'").fetchall():
            cl, base = clases.get(vid, (None, None))
            if cl == "transversal" and tema_b != "transversal":
                b.execute("UPDATE analisis SET tema='transversal', categoria='transversal' WHERE id=?", (vid,))
                m += 1
            elif cl in ("tema", "dudoso") and (tema_b or "").startswith("x_"):
                b.execute("UPDATE analisis SET tema=? WHERE id=?", (TEMA_BIB.get(base, base), vid))
        b.commit()
    return n_cambios, cuenta, m


def marcar(c, vid, clase, tema_obj, capa, confianza, evidencia, tema_real=None, motivo=""):
    """Decision de una capa cara (2 = verificacion, 3 = ficha): actualiza clase, tema y motivo."""
    info = {"tema_objetivo": tema_obj, "tipo": clase, "confianza": confianza, "evidencia": evidencia,
            "tema_real": tema_real, "capa": capa, "motivo": motivo[:200], "fecha": dt.date.today().isoformat()}
    c.execute("UPDATE virales SET clase=?, clase_info=?, tema=? WHERE id=?",
              (clase, json.dumps(info, ensure_ascii=False), tema_guardado(tema_obj, clase), vid))


def resumen(c):
    tot = dict(c.execute("SELECT COALESCE(clase,'sin_clase'), COUNT(*) FROM virales GROUP BY 1").fetchall())
    niv = dict(c.execute("SELECT COALESCE(nivel_canal,'sin_nivel'), COUNT(*) FROM canales GROUP BY 1").fetchall())
    return tot, niv
