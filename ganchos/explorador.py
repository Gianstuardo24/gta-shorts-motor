"""EXPLORADOR DE NICHOS: donde conviene estar o migrar. Mide la FUERZA y la CONSTANCIA de cada nicho en YouTube Shorts.

Por cada nicho e idioma (API oficial): busca Shorts de las ultimas 2 semanas, recorre sus canales y compara cada Short con
lo NORMAL DE SU CANAL. Mide:
  - puerta de entrada: % de canales CHICOS (<10k subs) con algun Short x10+ y 50k+ vistas  (se puede crecer desde cero)
  - constancia: % de Shorts que pasan x3 lo normal de su canal + % de canales "sanos" (mediana >= 5k vistas)
  - techo: vistas del percentil 90
  - saturacion: % de las vistas que se llevan canales de 1M+ subs
  - estabilidad: cuanto cambia la constancia entre corridas (se acumula dia a dia)
  - apto para nosotros: sin caras, material legal, datos verificables
Rota ~10 nichos-idioma por corrida (≈1.500-2.000 unidades de cuota): el mapa completo se arma en 4-5 dias y despues se refresca.

Uso:  python explorador.py            (siguientes 10 nichos-idioma menos recientes)
      python explorador.py --n 20     (mas por corrida)
      python explorador.py --nicho historia
Salida: Estudio › 📡 Radar › 🧭 Nichos (datos/estrategia/8-nichos.md) + tabla nichos_scan en datos/cerebro.db
"""
import sys, json, sqlite3, argparse, statistics, datetime as dt
from pathlib import Path

import ganchos as G

CEREBRO = Path("datos/cerebro.db")
INFORME = Path("datos/estrategia/8-nichos.md")
# nicho -> (busqueda ES, busqueda EN, apto para nosotros: sin caras / material legal / datos verificables)
NICHOS = {
    "historia": ("historia curiosidades", "history facts", True),
    "historia oscura": ("historia oscura", "dark history", True),
    "psicologia": ("datos psicológicos", "psychology facts", True),
    "misterios": ("misterios sin resolver", "unsolved mysteries", True),
    "espacio": ("datos del espacio", "space facts", True),
    "aliens / ovnis": ("ovnis", "UFO", True),
    "ciencia": ("ciencia curiosidades", "science facts", True),
    "animales": ("datos de animales", "animal facts", True),
    "oceano": ("misterios del océano", "ocean facts", True),
    "geografia / mapas": ("geografía curiosidades", "geography facts", True),
    "paises / culturas": ("curiosidades de países", "country facts", True),
    "datos curiosos": ("datos curiosos", "did you know facts", True),
    "negocios / empresas": ("historias de empresas", "business stories", True),
    "finanzas personales": ("finanzas personales tips", "personal finance tips", True),
    "dinero / lujo": ("datos de millonarios", "billionaire facts", True),
    "marcas / logos": ("historia de marcas", "brand history", True),
    "tecnologia": ("tecnología curiosidades", "tech facts", True),
    "inteligencia artificial": ("inteligencia artificial noticias", "AI news", True),
    "gaming noticias": ("noticias videojuegos", "gaming news", True),
    "gta": ("GTA 6", "GTA 6", True),
    "minecraft": ("minecraft curiosidades", "minecraft facts", True),
    "roblox": ("roblox", "roblox facts", True),
    "autos": ("autos curiosidades", "car facts", True),
    "aviones": ("aviones curiosidades", "aviation facts", True),
    "comida / historia": ("historia de la comida", "food history", True),
    "cafe": ("café curiosidades", "coffee facts", True),
    "cocina rapida": ("recetas rápidas", "quick recipes", False),
    "deportes curiosidades": ("fútbol curiosidades", "sports facts", True),
    "true crime": ("casos reales crimen", "true crime", False),
    "terror / creepy": ("datos perturbadores", "creepy facts", True),
    "motivacion": ("motivación", "motivation", True),
    "estoicismo / filosofia": ("estoicismo", "stoicism", True),
    "suerte / señales": ("mensaje del universo", "sign from the universe", True),
    "numerologia": ("numerología", "numerology", True),
    "numeros angelicales": ("números angelicales", "angel numbers", True),
    "idiomas": ("aprender inglés", "learn spanish", True),
    "productividad": ("productividad tips", "productivity tips", True),
    "salud / cuerpo humano": ("cuerpo humano curiosidades", "human body facts", True),
    "ingenieria": ("ingeniería curiosidades", "engineering facts", True),
    "arquitectura": ("arquitectura curiosidades", "architecture facts", True),
    "satisfying / asmr": ("videos satisfactorios", "satisfying video", False),
    "manualidades / diy": ("trucos caseros", "life hacks", False),
}


def abrir():
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS nichos_scan (nicho TEXT, idioma TEXT, fecha TEXT, canales INTEGER, shorts INTEGER,
        mediana INTEGER, pct_x3 REAL, pct_x10 REAL, puerta REAL, sanos REAL, techo INTEGER, saturacion REAL, ejemplos TEXT,
        PRIMARY KEY (nicho, idioma, fecha))""")
    return c


def medir(nicho, idi, q, cuota):
    desde = (G.AHORA - dt.timedelta(days=14)).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = G.get("search", costo=100, part="snippet", q=q, type="video", videoDuration="short", order="viewCount",
              publishedAfter=desde, maxResults=50, relevanceLanguage=idi)
    cids = list(dict.fromkeys(it["snippet"]["channelId"] for it in r.get("items", []) if it.get("snippet")))[:25]
    canales, shorts = [], []
    for i in range(0, len(cids), 50):
        ch = G.get("channels", part="contentDetails,statistics", id=",".join(cids[i:i + 50]))
        for x in ch.get("items", []):
            if G.CUOTA["u"] + 2 > cuota:
                break
            pl = G.get("playlistItems", part="contentDetails", playlistId=x["contentDetails"]["relatedPlaylists"]["uploads"], maxResults=50)
            info = G.videos_info([y["contentDetails"]["videoId"] for y in pl.get("items", [])])
            vs = []
            for vid, v in info.items():
                if 0 < G.segundos(v["contentDetails"]["duration"]) <= 180:
                    vs.append((vid, int(v["statistics"].get("viewCount") or 0), v["snippet"]["title"],
                               (G.AHORA - G.fecha(v["snippet"]["publishedAt"])).days))
            if len(vs) < 5:
                continue
            med = statistics.median(v for _, v, _, _ in vs)
            subs = int(x["statistics"].get("subscriberCount") or 0)
            recientes = [(vid, v, t, round(v / max(med, 1), 1)) for vid, v, t, d in vs if d <= 60]
            canales.append({"subs": subs, "mediana": med, "shorts": recientes,
                            "brecha": any(rr >= 10 and v >= 50_000 for _, v, _, rr in recientes)})
            shorts += [(vid, v, t, rr, subs) for vid, v, t, rr in recientes]
    if not canales or not shorts:
        return None
    vistas = sorted(v for _, v, _, _, _ in shorts)
    chicos = [k for k in canales if k["subs"] < 10_000]
    tot = sum(vistas) or 1
    grandes = sum(v for _, v, _, _, s in shorts if s >= 1_000_000)
    top = sorted(shorts, key=lambda s: -s[3])[:5]
    return {"canales": len(canales), "shorts": len(shorts), "mediana": int(statistics.median(vistas)),
            "pct_x3": round(100 * sum(s[3] >= 3 for s in shorts) / len(shorts), 1),
            "pct_x10": round(100 * sum(s[3] >= 10 for s in shorts) / len(shorts), 1),
            "puerta": round(100 * sum(k["brecha"] for k in chicos) / len(chicos), 1) if chicos else None,
            "sanos": round(100 * sum(k["mediana"] >= 5000 for k in canales) / len(canales), 1),
            "techo": int(vistas[int(len(vistas) * 0.9) - 1]) if len(vistas) >= 10 else vistas[-1],
            "saturacion": round(100 * grandes / tot, 1),
            "ejemplos": [{"id": i, "titulo": t, "vistas": v, "ratio": rr} for i, v, t, rr, _ in top]}


def puntaje(m, apto):
    if not m:
        return 0
    p = (0.35 * min((m["puerta"] or 0) / 30, 1) + 0.25 * min(m["pct_x3"] / 25, 1) + 0.2 * (m["sanos"] / 100)
         + 0.1 * min(m["techo"] / 1_000_000, 1) + 0.1 * (1 - m["saturacion"] / 100))
    return round(100 * p * (1 if apto else 0.5))


PROMPT = """Eres analista de mercado de YouTube Shorts para una fabrica de canales faceless (voz + imagenes legales + datos verificables).
Canales actuales: GTA 6 (ES y EN), The Rabbit Loop (aliens/misterios, EN), MDM (negocios, EN; evaluando suerte), cafe (EN, nuevo).
Te paso la tabla acumulada de nichos (puntaje, puerta de entrada para canales chicos, constancia, techo, saturacion, estabilidad entre
corridas) y ejemplos top. Escribe en espanol, markdown esquematico, sin relleno ni datos inventados:
1. **Top 10 nichos de oportunidad** (tabla: nicho, idioma, por que, riesgo, formato que gana segun los ejemplos).
2. **Los mas constantes** (rinden siempre) vs **los explosivos** (pocos casos enormes).
3. **ES vs EN**: donde conviene cada idioma.
4. **Recomendacion por canal nuestro**: quedarse, ajustar el angulo o migrar (a que nicho y por que). Especial: MDM y cafe.
5. **Nichos a vigilar** (pocos datos todavia) y **nichos a evitar**.
Di cuantas corridas respaldan cada conclusion; si hay pocas, dilo.
PROFUNDIDAD Y PERSPECTIVA (obligatorio en cada afirmacion importante):
- Evidencia: cuantos casos y que tan fuertes (xN, vistas); separa lo observado de lo que interpretas.
- Contraste: compara los TOP con videos NORMALES del mismo canal o tema (si lo normal tambien lo hace, NO es lo que hizo la diferencia).
- Hipotesis alternativas: tema caliente, momento, canal grande, algoritmo, suerte. Di cual explica mejor y por que.
- Mecanismo: que pasa en la cabeza del espectador, segundo a segundo, y por que lo hace quedarse o compartir.
- Condicion y limite: cuando funciona, cuando falla, que lo refutaria.
- Confianza: alta / media / baja segun n y consistencia. Nada de generalidades ni frases de manual."""


def informe(c):
    filas = c.execute("""SELECT nicho, idioma, COUNT(*), AVG(canales), AVG(shorts), AVG(mediana), AVG(pct_x3), AVG(pct_x10),
        AVG(puerta), AVG(sanos), AVG(techo), AVG(saturacion), MAX(fecha) FROM nichos_scan GROUP BY nicho, idioma""").fetchall()
    tabla, entrada = [], []
    for n, l, k, ca, sh, me, x3, x10, pu, sa, te, sat, fe in filas:
        hist = [r[0] for r in c.execute("SELECT pct_x3 FROM nichos_scan WHERE nicho=? AND idioma=? ORDER BY fecha", (n, l))]
        est = round(statistics.pstdev(hist), 1) if len(hist) > 1 else None
        apto = NICHOS.get(n, ("", "", True))[2]
        m = {"puerta": pu, "pct_x3": x3 or 0, "sanos": sa or 0, "techo": te or 0, "saturacion": sat or 0}
        pts = puntaje(m, apto)
        ej = json.loads(c.execute("SELECT ejemplos FROM nichos_scan WHERE nicho=? AND idioma=? ORDER BY fecha DESC LIMIT 1", (n, l)).fetchone()[0] or "[]")
        tabla.append((pts, n, l, k, int(me or 0), x3, x10, pu, sa, int(te or 0), sat, est, apto, ej))
    tabla.sort(key=lambda t: -t[0])
    for t in tabla:
        entrada.append(f"- {t[1]} [{t[2]}] puntaje {t[0]} · corridas {t[3]} · mediana {t[4]:,} · x3+ {t[5]:.0f}% · x10+ {t[6]:.0f}% · "
                       f"puerta {t[7] if t[7] is not None else '—'}% · sanos {t[8]:.0f}% · techo {t[9]:,} · saturacion {t[10]:.0f}% · "
                       f"estabilidad ±{t[11] if t[11] is not None else '—'} · apto {t[12]} · top: "
                       + "; ".join(f"\"{e['titulo'][:60]}\" x{e['ratio']} ({e['vistas']:,})" for e in t[13][:3]))
    print("✍️  Claude leyendo el mapa de nichos...", flush=True)
    try:
        texto = G.claude(PROMPT, "\n".join(entrada), timeout=1200)
    except Exception as e:
        texto = f"⚠️ No se pudo generar el análisis: {e}"
    faltan = [f"{n} ({l})" for n in NICHOS for l in ("es", "en")
              if not c.execute("SELECT 1 FROM nichos_scan WHERE nicho=? AND idioma=?", (n, l)).fetchone()]
    filas_md = "\n".join(f"| {t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]:,} | {t[5]:.0f}% | {t[7] if t[7] is not None else '—'}% | "
                         f"{t[8]:.0f}% | {t[9]:,} | {t[10]:.0f}% | {'±' + str(t[11]) if t[11] is not None else '—'} | {'✅' if t[12] else '⚠️'} |"
                         for t in tabla)
    md = (f"# 🧭 Nichos — {dt.datetime.now():%d/%m %H:%M}\n\n_{len(tabla)} nichos-idioma medidos · faltan {len(faltan)} "
          f"(se completan en las próximas corridas) · cuota de esta corrida ≈ {G.CUOTA['u']}_\n\n{texto.strip()}\n\n"
          "## Mapa completo\n\n| Puntaje | Nicho | Idioma | Corridas | Mediana vistas | Shorts x3+ | Puerta canales chicos | "
          "Canales sanos | Techo (p90) | Saturación | Estabilidad | Apto |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"
          f"{filas_md}\n\n**Cómo leerlo:** puerta = % de canales chicos (<10k subs) con algún Short x10+ · sanos = % de canales con "
          "mediana ≥ 5k vistas · saturación = % de vistas de canales 1M+ · estabilidad = cuánto varía 'x3+' entre corridas (menos = más constante).\n"
          + (f"\n_Faltan: {', '.join(faltan[:30])}{'…' if len(faltan) > 30 else ''}_\n" if faltan else ""))
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    INFORME.write_text(md, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--nicho")
    ap.add_argument("--cuota", type=int, default=2500)
    a = ap.parse_args()
    G.KEY = G._clave()
    c = abrir()
    hoy = dt.date.today().isoformat()
    pares = [(n, l) for n in NICHOS for l in ("es", "en")]
    if a.nicho:
        pares = [(n, l) for n, l in pares if n == a.nicho]
    ultima = {(n, l): f for n, l, f in c.execute("SELECT nicho, idioma, MAX(fecha) FROM nichos_scan GROUP BY nicho, idioma")}
    pares = [p for p in pares if ultima.get(p) != hoy]
    pares.sort(key=lambda p: ultima.get(p, ""))
    for n, l in pares[:a.n]:
        if G.CUOTA["u"] + 150 > a.cuota:
            print("⛔ Tope de cuota de esta corrida: sigo mañana.")
            break
        q = NICHOS[n][0 if l == "es" else 1]
        print(f"🧭 [{l}] {n} — \"{q}\"", flush=True)
        m = medir(n, l, q, a.cuota)
        if not m:
            print("   (sin datos suficientes)")
            continue
        c.execute("INSERT OR REPLACE INTO nichos_scan VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (n, l, hoy, m["canales"], m["shorts"], m["mediana"], m["pct_x3"], m["pct_x10"], m["puerta"], m["sanos"],
                   m["techo"], m["saturacion"], json.dumps(m["ejemplos"], ensure_ascii=False)))
        c.commit()
        print(f"   {m['canales']} canales · {m['shorts']} Shorts · x3+ {m['pct_x3']}% · puerta {m['puerta']}% · cuota ≈ {G.CUOTA['u']}", flush=True)
    informe(c)
    print("✅ Listo: Estudio › 📡 Radar › 🧭 Nichos", flush=True)


if __name__ == "__main__":
    main()
