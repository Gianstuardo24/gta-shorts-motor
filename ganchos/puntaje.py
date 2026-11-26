"""PUNTAJE COMPUESTO de virales: que merece estudiarse de verdad (no solo 'xN lo normal').

Un solo multiplicador engana: un x100 de un canal que normalmente saca 200 vistas no es lo mismo que un x8 con 5 millones.
Por eso cada Short de datos/cerebro.db (tabla virales) recibe:

  Componentes (0 a 1 cada uno)                         peso
  - relativo      log10(veces lo normal) / 3  (x10=0.33, x100=0.67, x1000=1, x1650=1.07... sin tope practico)   30%
  - alcance       (log10(vistas) - 4) / 3     (10k=0, 10M=1)  25%
  - velocidad     log10(vistas por hora) / 4  (10k/h=1)  15%
  - impulso       aceleracion y persistencia (necesita 2+ mediciones; si no hay, 0.5)  15%
  - reproducible  % de Shorts del MISMO canal que pasan x3 (el canal sabe repetir)  15%

  Confianza: baja si el canal es muy chico (mediana < 500 vistas) o hay pocos Shorts para comparar (< 8).

  Tipos (puede tener varios):
  - outlier       x20+ lo normal y 100k+ vistas
  - breakout      canal chico (<10k subs) que logra 100k+ vistas o 10x sus suscriptores
  - evergreen     30+ dias de vida y sigue sumando (velocidad reciente >= 30% de su promedio)
  - tendencia     <= 10 dias, comparte palabra clave con 3+ virales de OTROS canales del mismo tema esa semana, y esa palabra
                  aparece 3x mas esta semana que en la historia del tema (no cuenta 'secrets', 'details' y otras comunes)
  - reproducible  el video rinde (x3+) y su canal tiene 3+ Shorts x5 o mas en la ventana
  - posible_pagado  100k+ vistas con < 0,05% de likes (anuncio: vistas compradas) -> NO se estudia, confianza baja
  - otra_escritura  titulo en arabe, devanagari, telugu, cirilico, CJK... -> no es ES ni EN, no se estudia

Historial: tabla virales_fotos (cada medicion de cada viral). seguimiento() re-mide los candidatos (cuesta 1 unidad
por cada 50 videos) para calcular velocidad reciente, aceleracion y persistencia.
"""
import re, math, json, sqlite3, statistics, datetime as dt
from collections import Counter, defaultdict

import ganchos as G

PESOS = {"relativo": 0.30, "alcance": 0.25, "velocidad": 0.15, "impulso": 0.15, "reproducible": 0.15}
STOP = set("""the a an of to and is in this that you your why what how it was are for on with they he she we i my me de la el los las
del que qué por para con una un es no se lo esto este esta su tu te y en al como cómo shorts short gta gta6 vi 6 new nuevo
video ever most all just like de las"""
           .split())


def migrar(c):
    c.execute("""CREATE TABLE IF NOT EXISTS virales_fotos (id TEXT, ts TEXT, vistas INTEGER, likes INTEGER, comentarios INTEGER,
                 PRIMARY KEY (id, ts))""")
    cols = {r[1] for r in c.execute("PRAGMA table_info(virales)")}
    for col, tipo in [("subs_canal", "INTEGER"), ("vph", "REAL"), ("vph_reciente", "REAL"), ("aceleracion", "REAL"),
                      ("reproducible_canal", "REAL"), ("puntaje", "REAL"), ("componentes", "TEXT"), ("tipos", "TEXT"),
                      ("confianza", "TEXT"), ("n_canal", "INTEGER")]:
        if col not in cols:
            c.execute(f"ALTER TABLE virales ADD COLUMN {col} {tipo}")
    c.commit()


def foto(c, vid, vistas, likes=0, comentarios=0):
    c.execute("INSERT OR IGNORE INTO virales_fotos VALUES (?,?,?,?,?)",
              (vid, dt.datetime.now().isoformat(timespec="minutes"), vistas, likes, comentarios))


def seguimiento(c, dias=90, ratio_min=5, maximo=1500):
    """Re-mide los candidatos ya conocidos (barato: 1 unidad por 50 videos)."""
    desde = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=dias)).isoformat()
    ids = [r[0] for r in c.execute("SELECT id FROM virales WHERE ratio >= ? AND publicado >= ? ORDER BY ratio DESC LIMIT ?",
                                   (ratio_min, desde, maximo))]
    if not ids:
        return 0
    info = G.videos_info(ids)
    for vid, v in info.items():
        st = v["statistics"]
        vi, li, co = int(st.get("viewCount") or 0), int(st.get("likeCount") or 0), int(st.get("commentCount") or 0)
        foto(c, vid, vi, li, co)
        c.execute("UPDATE virales SET vistas=?, likes=?, comentarios=?, ratio=ROUND(? * 1.0 / MAX(mediana_canal, 1), 1), actualizado=? WHERE id=?",
                  (vi, li, co, vi, dt.datetime.now().isoformat(), vid))
        actual = c.execute("SELECT idioma FROM virales WHERE id=?", (vid,)).fetchone()
        nuevo = G.idioma_video(v["snippet"], actual[0] if actual else None)
        if nuevo is None:       # resulto ser otro idioma: se marca para no estudiarlo
            c.execute("UPDATE virales SET idioma='otro' WHERE id=?", (vid,))
        elif actual and nuevo != actual[0]:
            c.execute("UPDATE virales SET idioma=? WHERE id=?", (nuevo, vid))
    c.commit()
    return len(info)


def _palabras(t):
    return {w for w in re.findall(r"[a-záéíóúñü0-9']{4,}", (t or "").lower()) if w not in STOP}


def clasificar(c, min_ratio=20, min_vistas=100_000):
    migrar(c)
    ahora = dt.datetime.now(dt.timezone.utc)
    subs = dict(c.execute("SELECT id, subs FROM canales"))
    filas = c.execute("""SELECT id, canal_id, tema, titulo, publicado, vistas, mediana_canal, ratio FROM virales""").fetchall()
    interaccion = {i: (l or 0, co or 0) for i, l, co in c.execute("SELECT id, likes, comentarios FROM virales")}
    por_canal = defaultdict(list)
    for f in filas:
        por_canal[f[1]].append(f[7] or 0)
    # tendencias: palabras clave compartidas por virales recientes de distintos canales del mismo tema
    recientes = [(f[0], f[1], f[2], _palabras(f[3])) for f in filas
                 if (f[7] or 0) >= 5 and f[4] and (ahora - G.fecha(f[4])).days <= 10]
    clave = defaultdict(set)
    for vid, cid, tema, ws in recientes:
        for w in ws:
            clave[(tema, w)].add(cid)
    # una palabra es TENDENCIA solo si esta semana aparece mucho mas que en la historia del tema (no palabras comunes)
    hist_tema, hist_doc = Counter(), Counter()
    rec_tema, rec_doc = Counter(), Counter()
    for f in filas:
        reciente = f[4] and (ahora - G.fecha(f[4])).days <= 10
        for w in _palabras(f[3]):
            (rec_doc if reciente else hist_doc)[(f[2], w)] += 1
        (rec_tema if reciente else hist_tema)[f[2]] += 1
    def es_tendencia(tema, w):
        r = rec_doc[(tema, w)] / max(rec_tema[tema], 1)
        h = (hist_doc[(tema, w)] + 1) / max(hist_tema[tema] + 20, 1)      # suavizado: sin historia no hay 'tendencia' falsa
        return r >= 3 * h and r <= 0.5
    fotos = defaultdict(list)
    for vid, ts, vi in c.execute("SELECT id, ts, vistas FROM virales_fotos ORDER BY ts"):
        fotos[vid].append((dt.datetime.fromisoformat(ts), vi))
    for vid, cid, tema, titulo, pub, vistas, med, ratio in filas:
        if not pub:
            continue
        edad_h = max((ahora - G.fecha(pub)).total_seconds() / 3600, 1)
        vistas = vistas or 0
        vph = vistas / edad_h
        hist = fotos.get(vid, [])
        vph_rec, acel = None, None
        if len(hist) >= 2:
            (t1, v1), (t2, v2) = hist[-2], hist[-1]
            dh = max((t2 - t1).total_seconds() / 3600, 0.5)
            vph_rec = max(v2 - v1, 0) / dh
            acel = round(vph_rec / max(vph, 1e-6), 2)
        rs = por_canal.get(cid, [])
        repro = (sum(r >= 3 for r in rs) / len(rs)) if rs else 0
        comp = {
            "relativo": min(math.log10(max(ratio or 1, 1)) / 3, 1.5),   # sin tope practico: x1000=1.0, x1650=1.07, x10000=1.33
            "alcance": min(max((math.log10(max(vistas, 1)) - 4) / 3, 0), 1),
            "velocidad": min(max(math.log10(max(vph, 1)) / 4, 0), 1),
            "impulso": 0.5 if acel is None else min(acel, 2) / 2,
            "reproducible": min(repro / 0.3, 1),
        }
        pts = round(100 * sum(PESOS[k] * v for k, v in comp.items()), 1)
        s = subs.get(cid) or 0
        tipos = []
        if (ratio or 0) >= min_ratio and vistas >= min_vistas:
            tipos.append("outlier")
        if (ratio or 0) >= 1000 and vistas >= min_vistas:
            tipos.append("x1000+")
        elif (ratio or 0) >= 100 and vistas >= min_vistas:
            tipos.append("x100+")
        if s and s < 10_000 and (vistas >= 100_000 or vistas >= 10 * s) and vistas >= 20_000:
            tipos.append("breakout")
        if edad_h >= 30 * 24 and vph_rec is not None and vph_rec >= 0.3 * vph:
            tipos.append("evergreen")
        if edad_h <= 10 * 24 and any(len(clave[(tema, w)] - {cid}) >= 3 and es_tendencia(tema, w) for w in _palabras(titulo)):
            tipos.append("tendencia")
        if (ratio or 0) >= 3 and sum(r >= 5 for r in rs) >= 3:      # el video rinde Y su canal lo repite
            tipos.append("reproducible")
        li, co = interaccion.get(vid, (0, 0))
        pagado = vistas >= 100_000 and ((li > 0 and li / vistas < 0.0005) or (li == 0 and co / vistas < 0.00002))
        if pagado:       # anuncio pagado (vistas compradas: casi sin likes ni comentarios) -> no enseña nada de contenido
            tipos = ["posible_pagado"]
        if not G.escritura_latina(titulo):
            tipos.append("otra_escritura")
        conf = "baja" if pagado or (med or 0) < 500 or len(rs) < 8 else ("alta" if len(rs) >= 20 and hist else "media")
        c.execute("""UPDATE virales SET subs_canal=?, vph=?, vph_reciente=?, aceleracion=?, reproducible_canal=?, puntaje=?,
                     componentes=?, tipos=?, confianza=?, n_canal=? WHERE id=?""",
                  (s, round(vph, 1), round(vph_rec, 1) if vph_rec is not None else None, acel, round(repro, 2), pts,
                   json.dumps({k: round(v, 2) for k, v in comp.items()}), ",".join(tipos), conf, len(rs), vid))
    c.commit()


def seleccion(c, min_ratio=20, min_vistas=100_000, por_tema=12, umbral=55, excluir=(), plataforma="youtube",
              transversales=10, por_subtema=3, dudosos_max=40):
    """Radar 2.0 · tres colas, cada una con su presupuesto. Devuelve {"tema": [...], "dudoso": [...], "transversal": [...]}.
      tema        1) TODOS los x100+ con 100k+ vistas, de mayor a menor (un x1650 va antes que un x102), intercalando subtemas
                     para que los primeros no sean todos iguales; 2) el resto por puntaje: max 12 por tema e idioma y max 3 por subtema.
      dudoso      candidatos que irian a ficha pero aun no se sabe si son del tema → se verifican antes (verificar.py), max 40.
      transversal de otro nicho pero enormes (x100+ y 100k+): max 10, max 2 por canal y 2 por subtema, + 1 atipico.
    Ruido (posible pagado, otra escritura, idioma fuera de es/en) no entra en ninguna."""
    filas = c.execute("""SELECT id, tema, idioma, titulo, vistas, ratio, puntaje, tipos, confianza, COALESCE(clase,'tema'),
                         COALESCE(subtema,'otro'), canal_id, tema_buscado FROM virales
                         WHERE puntaje IS NOT NULL AND COALESCE(plataforma, 'youtube') = ?""", (plataforma,)).fetchall()
    dic = lambda f: {"id": f[0], "tema": (f[1] or "").removeprefix("x_"), "idioma": f[2], "titulo": f[3], "vistas": f[4], "ratio": f[5],
                     "puntaje": f[6], "tipos": f[7] or "", "confianza": f[8], "clase": f[9], "subtema": f[10], "canal": f[11]}
    filas = [f for f in filas if f[0] not in excluir and "posible_pagado" not in (f[7] or "") and "otra_escritura" not in (f[7] or "")
             and f[2] in ("es", "en")]
    grande = lambda f: (f[5] or 0) >= 100 and (f[4] or 0) >= min_vistas
    fuerte = lambda f: (any(t in (f[7] or "") for t in ("outlier", "breakout", "reproducible", "evergreen")) and (f[6] or 0) >= umbral) \
        or ((f[4] or 0) >= 1_000_000 and (f[5] or 0) >= 5)
    # --- cola del tema (y dudosos, que compiten por el mismo lugar hasta verificarse) ---
    del_tema = [f for f in filas if f[9] in ("tema", "dudoso") and not (f[1] or "").startswith("x_")]
    mega = sorted([f for f in del_tema if grande(f)], key=lambda f: -(f[5] or 0))
    # intercalar subtemas dentro de cada tema sin perder el orden por xN: ronda 1 = el mejor de cada subtema, ronda 2 = el segundo...
    rango, visto = {}, Counter()
    for f in mega:
        visto[(f[1], f[10])] += 1
        rango[f[0]] = visto[(f[1], f[10])]
    mega.sort(key=lambda f: (rango[f[0]], -(f[5] or 0)))     # ronda por ronda, cada ronda de mayor a menor xN
    tema_l, dud_l, ya = [], [], set()
    for f in mega:
        (dud_l if f[9] == "dudoso" else tema_l).append(dic(f))
        ya.add(f[0])
    cuenta, cuenta_sub = Counter(), Counter()
    for f in sorted(del_tema, key=lambda f: (-(f[6] or 0), -(f[5] or 0))):
        if f[0] in ya or not fuerte(f):
            continue
        if f[8] == "baja" and (f[4] or 0) < min_vistas:
            continue
        if cuenta[(f[1], f[2])] >= por_tema or cuenta_sub[(f[1], f[2], f[10])] >= por_subtema:
            continue
        cuenta[(f[1], f[2])] += 1
        cuenta_sub[(f[1], f[2], f[10])] += 1
        (dud_l if f[9] == "dudoso" else tema_l).append(dic(f))
        ya.add(f[0])
    # --- cola transversal: diversa y con tope ---
    trans = sorted([f for f in filas if f[9] == "transversal" and grande(f) and f[0] not in ya], key=lambda f: -(f[5] or 0))
    tr_l, por_canal, por_sub = [], Counter(), Counter()
    for f in trans:
        if len(tr_l) >= transversales - 1:
            break
        clave_sub = (f[12] or f[1], f[10])
        if por_canal[f[11]] >= 2 or por_sub[clave_sub] >= 2:
            continue
        por_canal[f[11]] += 1
        por_sub[clave_sub] += 1
        tr_l.append(dic(f))
    resto = [f for f in trans if f[0] not in {x["id"] for x in tr_l}]
    vistos_sub = {(x.get("tema"), x.get("subtema")) for x in tr_l}
    atipico = next((f for f in resto if ((f[12] or f[1]), f[10]) not in vistos_sub and por_canal[f[11]] == 0), None)
    if atipico:
        d = dic(atipico)
        d["atipico"] = True
        tr_l.append(d)
    return {"tema": tema_l, "dudoso": dud_l[:dudosos_max], "transversal": tr_l}
