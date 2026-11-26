"""📡 RADAR 2.0 · VERIFICACION BARATA (capa 2) + AUDITORIA automatica + COMPARACION antes/ahora.

Para saber de que trata un Short SIN gastar una ficha completa:
  subtitulos automaticos (no se baja nada) → miniatura (una imagen) → si no hay voz: 4 cuadros en 360p (se baja, se cortan 4 cuadros
  y el video se borra al tiro). Claude los mira en lotes de 20 y dice el tema real.

Usos:
  - verificar(c, dudosos)   → resuelve los dudosos antes del analisis profundo (lo llama analisis.py).
  - auditar(c, n=30)        → 30 videos al azar ya clasificados; Claude los revisa SIN saber que decidio el filtro y se mide
                              cuanto acierta cada capa. Si una capa acierta < 85 %, queda la alerta en 13-clasificacion.md.
  - comparar(c)             → que habria elegido la version de antes vs la de ahora, con el mismo auditor ciego.
CLI:  python verificar.py auditar [30]      python verificar.py comparar [30]   (~15 min: no hace fichas)
"""
import sys, json, time, random, shutil, sqlite3, subprocess, datetime as dt
from pathlib import Path
from urllib.request import urlopen, Request

import ganchos as G
import clasificar as C

TMP = Path("biblioteca/_verificar")
INFORME = Path("datos/estrategia/13-clasificacion.md")
LOTE = 20
UMBRAL_ALERTA = 0.85
TEMAS = ["gta", "aliens", "cafe", "suerte", "negocios"]
NOMBRES = {"gta": "GTA 6 (el videojuego)", "aliens": "aliens, ovnis, espacio y misterios", "cafe": "café",
           "suerte": "suerte, numerología, señales y números angelicales", "negocios": "negocios, empresas y dinero"}

PROMPT = """Clasificas Shorts de YouTube por TEMA REAL, mirando su contenido (no te fies solo del titulo: puede ser vago o enganoso).
Temas posibles: gta = GTA 6 (videojuego) · aliens = aliens/ovnis/espacio/misterios · cafe = café · suerte = suerte/numerologia/senales ·
negocios = negocios/empresas/dinero · otro = cualquier otra cosa (di cual en 1-3 palabras).
De cada video te paso: titulo, descripcion, un extracto de los subtitulos (si tiene voz) y rutas de imagenes (miniatura y, si no hay voz,
4 cuadros del video en una grilla 2x2). Usa la herramienta Read para MIRAR las imagenes.
Un video es de un tema si de verdad TRATA de eso (una receta que usa una taza de cafe de fondo NO es de cafe; un video de ovnis con
titulo "you won't believe this" SI es de aliens).
Responde SOLO un array JSON, un objeto por video, en el mismo orden:
[{"id":"...","tema_real":"gta|aliens|cafe|suerte|negocios|otro","otro_cual":"si es otro: de que trata","confianza":0.0,
  "motivo":"1 frase: que viste o leiste que lo decide"}]"""


def log(m):
    print(m, flush=True)


def _bajar_360(url, carpeta):
    from yt_dlp import YoutubeDL
    import biblioteca as B
    o = {"quiet": True, "logger": B.Silencio(), "noplaylist": True, "retries": 2,
         "format": "b[height<=360]/bv*[height<=360]+ba/w", "merge_output_format": "mp4",
         "outtmpl": str(carpeta / "v360.%(ext)s")}
    if B.NAV:
        o["cookiesfrombrowser"] = (B.NAV,)
    with YoutubeDL(o) as y:
        y.download([url])
    return next((p for p in carpeta.glob("v360.*") if p.suffix in (".mp4", ".webm", ".mkv")), None)


def material(vid):
    """Lo minimo para saber de que trata: subtitulos, miniatura y (si no hay voz) 4 cuadros. Devuelve dict o None."""
    import biblioteca as B
    url = f"https://www.youtube.com/shorts/{vid}"
    carpeta = TMP / vid
    carpeta.mkdir(parents=True, exist_ok=True)
    info = B.info_video(url)                     # sin bajar el video (lanza B.Bloqueo si YouTube frena)
    if not info:
        return None
    subs = ""
    try:
        subs = B.subtitulos_largo(info)[:1500]
    except Exception:
        pass
    imgs = []
    mini = info.get("thumbnail")
    if mini:
        try:
            ext = ".webp" if ".webp" in mini.split("?")[0] else ".png" if ".png" in mini.split("?")[0] else ".jpg"
            (carpeta / f"miniatura{ext}").write_bytes(urlopen(Request(mini, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read())
            imgs.append(carpeta / f"miniatura{ext}")
        except Exception:
            pass
    fuentes = ["subtitulos"] if len(subs) >= 80 else []
    if len(subs) < 80:                            # sin voz (o casi): se miran 4 cuadros del video
        v = None
        try:
            v = _bajar_360(url, carpeta)
            if v:
                D = float(info.get("duration") or 30)
                for k, f in enumerate((0.2, 0.4, 0.6, 0.8)):
                    subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", f"{D * f:.2f}", "-i", str(v),
                                    "-frames:v", "1", "-vf", "scale=-2:360", str(carpeta / f"c{k}.jpg")])
                partes = sorted(carpeta.glob("c[0-3].jpg"))
                if partes:
                    from PIL import Image
                    ims = [Image.open(x).convert("RGB") for x in partes]
                    w, h = ims[0].size
                    hoja = Image.new("RGB", (w * 2, h * ((len(ims) + 1) // 2)), "white")
                    for k, im in enumerate(ims):
                        hoja.paste(im.resize((w, h)), ((k % 2) * w, (k // 2) * h))
                    hoja.save(carpeta / "cuadros.jpg", quality=80)
                    imgs.append(carpeta / "cuadros.jpg")
                    fuentes.append("cuadros")
        except B.Bloqueo:
            raise
        except Exception:
            pass
        finally:
            if v and v.exists():
                v.unlink()                       # el video se borra SIEMPRE
            for p in carpeta.glob("c[0-3].jpg"):
                p.unlink()
    if imgs and imgs[0].name.startswith("miniatura"):
        fuentes.append("miniatura")
    return {"id": vid, "titulo": info.get("title") or "", "descripcion": (info.get("description") or "")[:400],
            "subs": subs, "imagenes": [str(p.resolve()) for p in imgs], "fuentes": fuentes}


def preguntar(mats):
    """Un lote (hasta 20) a Claude → {id: respuesta}."""
    bloques = []
    for m in mats:
        bloques.append(f"### id {m['id']}\nTitulo: {m['titulo']}\nDescripcion: {m['descripcion']}\n"
                       f"Subtitulos: {m['subs'] or '(sin voz)'}\nImagenes: {', '.join(m['imagenes']) or '(ninguna)'}")
    r = subprocess.run(["claude", "-p", PROMPT, "--allowedTools", "Read"], input="\n\n".join(bloques),
                       capture_output=True, text=True, timeout=1500)
    try:
        lst = G.extraer_json(r.stdout)
    except Exception:
        return {}
    return {str(x.get("id")): x for x in lst if isinstance(x, dict)}


def revisar(vids, etiqueta="verificación", pausa=(2, 5)):
    """Material + Claude para una lista de ids. Devuelve {id: {"tema_real","confianza","motivo","fuentes"}} (parcial si YouTube frena)."""
    import biblioteca as B
    out, mats = {}, []
    for k, vid in enumerate(vids, 1):
        try:
            m = material(vid)
        except B.Bloqueo:
            log(f"   ⏸️ {etiqueta}: YouTube frenó las consultas; sigo con lo que alcancé ({len(out) + len(mats)}).")
            break
        except Exception as e:
            log(f"   ⚠️ {vid}: {str(e)[:80]}")
            m = None
        if m:
            mats.append(m)
        if len(mats) >= LOTE or (k == len(vids) and mats):
            res = preguntar(mats)
            for x in mats:
                if x["id"] in res:
                    out[x["id"]] = {**res[x["id"]], "fuentes": x["fuentes"]}
            log(f"   🔎 {etiqueta}: {len(out)}/{len(vids)} revisados")
            mats = []
        time.sleep(random.uniform(*pausa))
    if mats:
        res = preguntar(mats)
        for x in mats:
            if x["id"] in res:
                out[x["id"]] = {**res[x["id"]], "fuentes": x["fuentes"]}
    shutil.rmtree(TMP, ignore_errors=True)
    return out


def verificar(c, dudosos):
    """Capa 2: resuelve los dudosos. Devuelve (a_tema, a_transversal) como listas de dicts de la seleccion."""
    if not dudosos:
        return [], []
    log(f"🔎 Verificando {len(dudosos)} dudosos (subtítulos → miniatura → 4 cuadros en 360p; lotes de {LOTE})...")
    res = revisar([d["id"] for d in dudosos])
    a_tema, a_trans = [], []
    for d in dudosos:
        r = res.get(d["id"])
        if not r:
            continue
        es = r.get("tema_real") == d["tema"]
        clase = "tema" if es else "transversal"
        C.marcar(c, d["id"], clase, d["tema"], 2, r.get("confianza"), r.get("fuentes") or [], r.get("tema_real"), r.get("motivo") or "")
        (a_tema if es else a_trans).append({**d, "clase": clase})
    c.commit()
    log(f"   ✅ dudosos: {len(a_tema)} eran del tema · {len(a_trans)} de otro nicho (transversal) · {len(dudosos) - len(res)} sin resolver")
    return a_tema, a_trans


def _correcto(clase, tema_obj, tema_aud):
    return (tema_aud == tema_obj) == (clase == "tema")


def auditar(c, n=30, guardar=True):
    """30 al azar entre los clasificados con 20x+ (los que pueden ir a ficha). El auditor NO sabe que decidio el filtro."""
    C.migrar(c)
    filas = c.execute("""SELECT id, clase, clase_info FROM virales WHERE clase IN ('tema','transversal') AND ratio >= 20
                         AND COALESCE(plataforma,'youtube')='youtube'""").fetchall()
    if not filas:
        return None
    random.shuffle(filas)
    tema_f = [f for f in filas if f[1] == "tema"][: n * 2 // 3]
    trans_f = [f for f in filas if f[1] == "transversal"][: n - len(tema_f)]
    muestra = tema_f + trans_f
    log(f"🧪 Auditoría ciega: {len(muestra)} videos al azar ({len(tema_f)} 'del tema' · {len(trans_f)} 'transversal')...")
    res = revisar([f[0] for f in muestra], "auditoría")
    hoy = dt.datetime.now().isoformat(timespec="minutes")
    por_capa, ok_tot, n_tot = {}, 0, 0
    for vid, clase, info in muestra:
        r = res.get(vid)
        if not r:
            continue
        info = json.loads(info or "{}")
        tema_obj = info.get("tema_objetivo")
        ok = _correcto(clase, tema_obj, r.get("tema_real"))
        capa = f"capa {info.get('capa', 1)} · " + ("+".join(info.get("evidencia") or []) or "sin evidencia")
        por_capa.setdefault(capa, [0, 0])
        por_capa[capa][0] += ok
        por_capa[capa][1] += 1
        ok_tot += ok
        n_tot += 1
        if guardar:
            c.execute("INSERT OR REPLACE INTO auditoria VALUES (?,?,?,?,?,?,?,?)",
                      (vid, hoy, clase, capa, tema_obj, r.get("tema_real"), int(ok), (r.get("motivo") or "")[:200]))
    c.commit()
    if not n_tot:
        return None
    alertas = [f"{k}: acierta {a / t:.0%} ({a}/{t})" for k, (a, t) in por_capa.items() if t >= 3 and a / t < UMBRAL_ALERTA]
    L = [f"# 🧪 Calidad de la clasificación ({hoy})", "",
         f"Auditoría ciega de {n_tot} videos: **{ok_tot / n_tot:.0%} bien clasificados**.", "",
         "| Capa · evidencia | Aciertos | % |", "|---|---|---|"]
    L += [f"| {k} | {a}/{t} | {a / t:.0%} |" for k, (a, t) in sorted(por_capa.items(), key=lambda x: -x[1][1])]
    if alertas:
        L += ["", "## ⚠️ Alertas (menos de 85 %)", ""] + [f"- {a}: subir el umbral o mandar esos casos a verificación" for a in alertas]
    errores = c.execute("SELECT v.titulo, a.clase, a.tema_objetivo, a.tema_auditor, a.motivo FROM auditoria a JOIN virales v ON v.id=a.id "
                        "WHERE a.fecha=? AND a.correcto=0 LIMIT 10", (hoy,)).fetchall()
    if errores:
        L += ["", "## Errores de esta auditoría", "", "| Video | Filtro dijo | Auditor dice | Por qué |", "|---|---|---|---|"]
        L += [f"| {t[:60]} | {cl} ({to}) | {ta} | {m[:80]} |" for t, cl, to, ta, m in errores]
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    INFORME.write_text("\n".join(L) + "\n", encoding="utf-8")
    log(f"   🧪 Clasificación: {ok_tot / n_tot:.0%} bien ({ok_tot}/{n_tot})" + (f" · ⚠️ {len(alertas)} alertas" if alertas else ""))
    return {"pct": ok_tot / n_tot, "alertas": alertas}


def seleccion_antes(c, min_ratio=20, min_vistas=100_000, por_tema=12, umbral=55):
    """La seleccion de ANTES (sin clases ni filtro de tema), sobre los mismos datos: para comparar."""
    filas = c.execute("""SELECT id, tema, idioma, titulo, vistas, ratio, puntaje, tipos, confianza FROM virales
                         WHERE puntaje IS NOT NULL AND COALESCE(plataforma,'youtube')='youtube'""").fetchall()
    filas = [f for f in filas if "posible_pagado" not in (f[7] or "") and "otra_escritura" not in (f[7] or "") and f[2] in ("es", "en")]
    mega = sorted([f for f in filas if (f[5] or 0) >= 100 and (f[4] or 0) >= min_vistas], key=lambda f: -(f[5] or 0))
    out, ya, cuenta = [f for f in mega], {f[0] for f in mega}, {}
    for f in sorted(filas, key=lambda f: (-(f[6] or 0), -(f[5] or 0))):
        tema = (f[1] or "").removeprefix("x_")
        fuerte = any(t in (f[7] or "") for t in ("outlier", "breakout", "reproducible", "evergreen")) and (f[6] or 0) >= umbral
        if f[0] in ya or not (fuerte or ((f[4] or 0) >= 1_000_000 and (f[5] or 0) >= 5)):
            continue
        if f[8] == "baja" and (f[4] or 0) < min_vistas or cuenta.get((tema, f[2]), 0) >= por_tema:
            continue
        cuenta[(tema, f[2])] = cuenta.get((tema, f[2]), 0) + 1
        out.append(f)
    return [{"id": f[0], "tema": (f[1] or "").removeprefix("x_"), "titulo": f[3], "ratio": f[5]} for f in out]


def comparar(c, n=30):
    """Primeros N que analizaria cada version (≈ lo que cabe en 3 h) → auditor ciego → % del tema, diversidad, transversales."""
    import puntaje as P
    antes = seleccion_antes(c)[:n]
    q = P.seleccion(c)
    ahora_tema = (q["tema"] + q["dudoso"])[: max(0, n - len(q["transversal"]))]
    ahora = [{**x, "cola": "tema"} for x in ahora_tema] + [{**x, "cola": "transversal"} for x in q["transversal"]]
    ids = list(dict.fromkeys([x["id"] for x in antes] + [x["id"] for x in ahora]))
    log(f"⚖️  Comparación: {len(antes)} de ANTES vs {len(ahora)} de AHORA ({len(ids)} videos distintos) · auditor ciego...")
    res = revisar(ids, "comparación")
    sub = {r[0]: r[1] for r in c.execute("SELECT id, COALESCE(subtema,'otro') FROM virales")}
    can = {r[0]: r[1] for r in c.execute("SELECT id, canal_id FROM virales")}

    def medir(lista, solo_tema=False):
        l = [x for x in lista if (not solo_tema or x.get("cola", "tema") == "tema") and x["id"] in res]
        del_t = sum(1 for x in l if res[x["id"]].get("tema_real") == x["tema"])
        return {"n": len(l), "del_tema": del_t, "pct": del_t / len(l) if l else 0,
                "subtemas": len({(x["tema"], sub.get(x["id"])) for x in l}), "canales": len({can.get(x["id"]) for x in l})}

    a, b = medir(antes), medir(ahora, solo_tema=True)
    tr = [x for x in ahora if x.get("cola") == "transversal"]
    gana = b["pct"] >= a["pct"]
    L = [f"# ⚖️ Antes vs ahora: qué se analizaría a fondo ({dt.datetime.now():%d/%m %H:%M})", "",
         f"Mismos datos, primeros {n} videos de cada versión, revisados por un auditor que no sabe qué versión los eligió.", "",
         "| | Antes | Ahora (cola del tema) |", "|---|---|---|",
         f"| Videos revisados | {a['n']} | {b['n']} |",
         f"| **De verdad del tema** | **{a['del_tema']} ({a['pct']:.0%})** | **{b['del_tema']} ({b['pct']:.0%})** |",
         f"| Subtemas distintos | {a['subtemas']} | {b['subtemas']} |",
         f"| Canales distintos | {a['canales']} | {b['canales']} |", "",
         f"Además, ahora van **{len(tr)} transversales** aparte (otro nicho, solo para el arsenal general).", "",
         f"**Veredicto:** {'✅ la versión nueva elige más videos del tema' if gana else '❌ la versión nueva NO mejora: no subirla'}."]
    malos = [x for x in antes if x["id"] in res and res[x["id"]].get("tema_real") != x["tema"]][:8]
    if malos:
        L += ["", "Ejemplos que la versión de ANTES habría analizado como del tema y no lo eran:", ""]
        L += [f"- x{x['ratio']} \"{(x['titulo'] or '')[:70]}\" ({x['tema']} → {res[x['id']].get('tema_real')} {res[x['id']].get('otro_cual') or ''})" for x in malos]
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    Path("datos/estrategia/14-comparacion.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    return {"antes": a, "ahora": b, "transversales": len(tr), "gana": gana}


if __name__ == "__main__":
    a = sys.argv[1:]
    con = sqlite3.connect("datos/cerebro.db")
    if a and a[0] == "auditar":
        auditar(con, int(a[1]) if len(a) > 1 else 30)
    elif a and a[0] == "comparar":
        comparar(con, int(a[1]) if len(a) > 1 else 30)
    else:
        print(__doc__)
