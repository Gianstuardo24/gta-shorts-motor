"""🔭 VIGIA: una vez por semana mira que hay de nuevo en herramientas, IA, apps baratas, marketing y entretenimiento gratis LEGAL.

Fuentes publicas (sin cuenta): Reddit (top de la semana en subreddits elegidos) y Hacker News (lo mas votado de la semana).
Claude filtra el ruido y deja solo lo util para Tao: que es, para que nos sirve, cuanto cuesta, y si vale probarlo.
Nunca recomienda pirateria, cracks, cuentas compartidas ni trampas; si algo huele a eso, lo descarta.

Salida:  datos/estrategia/11-vigia.md  (lo ultimo)  +  datos/vigia/AAAA-MM-DD.md  (se acumula semana a semana)
Uso:     python vigia.py            (corre si la ultima vigia tiene 6+ dias)
         python vigia.py --ya       (corre igual)
analisis.py la llama sola en el modo Completo cuando toca.
"""
import sys, json, time, datetime as dt
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode

SALIDA = Path("datos/estrategia/11-vigia.md")
HIST = Path("datos/vigia")
UA = {"User-Agent": "gta-shorts-vigia/1.0 (lectura personal)"}
SUBREDDITS = {
    "ia": ["artificial", "LocalLLaMA", "StableDiffusion", "ChatGPTPro"],
    "herramientas": ["software", "macapps", "SideProject", "selfhosted", "productivity"],
    "creadores": ["NewTubers", "youtubers", "InstagramMarketing", "socialmedia", "VideoEditing"],
    "negocio": ["marketing", "Entrepreneur", "copywriting"],
    "entretenimiento_legal": ["cordcutters", "FreeGameFindings"],
}
DIAS = 6

PROMPT = """Eres el vigia de herramientas de un creador que tiene una fabrica de YouTube Shorts automatizada en Python en un Mac
(voz IA, imagenes ChatGPT, montaje con ffmpeg, analisis con la API de YouTube y Claude), canales de GTA (guias), aliens, cafe,
negocios y suerte/numerologia, y una app movil de fitness (Repers) con cuentas de Instagram y TikTok.

Te paso lo mas votado de la semana en Reddit y Hacker News (titulo, puntos, comentarios, link, extracto).
Devuelve SOLO markdown en espanol neutro, breve y esquematico:

## 🧪 Vale probar esta semana (max 5)
- **Nombre** — que es en 1 linea · **para que nos sirve** (concreto: que parte de la fabrica, canal o app mejora) · **costo** (gratis / $ / desconocido) · [link]

## 🤖 IA para crear contenido
## 🛠️ Apps y herramientas (gratis o baratas, ojala Mac)
## 📈 Marketing, Shorts, Reels y crecimiento (ideas o datos accionables)
## 🎬 Entretenimiento gratis y LEGAL (streaming con anuncios, juegos regalados oficialmente, etc.)
## 👀 Para vigilar (tendencias que aun no conviene usar)

Reglas:
- Solo lo que sirve de verdad; si una seccion no tiene nada bueno, escribe "— nada esta semana".
- Cada item con su link. No inventes funciones, precios ni datos: si el extracto no lo dice, pon "por confirmar".
- DESCARTA sin mencionarlo: pirateria, sitios para ver peliculas/series sin licencia, cracks, keys revendidas, cuentas compartidas,
  bots de vistas/seguidores, trampas o exploits, y promesas de dinero facil.
- Marca con ⚠️ lo que tenga letra chica (licencia no comercial, datos que se van a un tercero, beta inestable).
"""


def leer(url):
    return json.loads(urlopen(Request(url, headers=UA), timeout=30).read())


def reddit(sub):
    for base in ("https://www.reddit.com", "https://old.reddit.com"):
        try:
            d = leer(f"{base}/r/{sub}/top.json?" + urlencode({"t": "week", "limit": 20}))
            return [{"fuente": f"r/{sub}", "titulo": p["data"]["title"], "puntos": p["data"].get("score", 0),
                     "comentarios": p["data"].get("num_comments", 0),
                     "link": p["data"].get("url_overridden_by_dest") or "https://www.reddit.com" + p["data"]["permalink"],
                     "hilo": "https://www.reddit.com" + p["data"]["permalink"],
                     "extracto": (p["data"].get("selftext") or "")[:400]}
                    for p in d["data"]["children"] if not p["data"].get("over_18")]
        except Exception as e:
            err = str(e)[:80]
    print(f"   ⚠️ r/{sub}: no respondio ({err})", flush=True)
    return []


def hacker_news():
    desde = int((dt.datetime.now() - dt.timedelta(days=7)).timestamp())
    try:
        d = leer("https://hn.algolia.com/api/v1/search?" + urlencode(
            {"tags": "story", "numericFilters": f"created_at_i>{desde},points>150", "hitsPerPage": 40}))
    except Exception as e:
        print(f"   ⚠️ Hacker News: no respondio ({str(e)[:80]})", flush=True)
        return []
    return [{"fuente": "Hacker News", "titulo": h.get("title"), "puntos": h.get("points", 0), "comentarios": h.get("num_comments", 0),
             "link": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
             "hilo": f"https://news.ycombinator.com/item?id={h['objectID']}", "extracto": ""} for h in d.get("hits", [])]


def toca():
    if not SALIDA.exists():
        return True
    return (time.time() - SALIDA.stat().st_mtime) / 86400 >= DIAS


def main(forzar=False):
    if not forzar and not toca():
        print("🔭 Vigía: la última tiene menos de 6 días; se salta (usa --ya para forzar).", flush=True)
        return None
    import ganchos as G
    print("🔭 Vigía semanal: Reddit + Hacker News...", flush=True)
    items = []
    for cat, subs in SUBREDDITS.items():
        for s in subs:
            filas = reddit(s)
            for f in filas:
                f["categoria"] = cat
            items += filas
            time.sleep(2)           # Reddit sin cuenta: suave
    items += hacker_news()
    items = [x for x in items if x.get("titulo")]
    items.sort(key=lambda x: -(x["puntos"] or 0))
    print(f"   {len(items)} publicaciones de la semana → Claude filtra lo útil", flush=True)
    if not items:
        print("   (sin datos: revisa la conexión)")
        return None
    entrada = "\n".join(f"- [{x['fuente']}] {x['titulo']} · {x['puntos']} pts · {x['comentarios']} com · {x['link']}"
                        + (f"\n  extracto: {x['extracto']}" if x["extracto"] else "") for x in items[:220])
    texto = G.claude(PROMPT, entrada, timeout=900).strip()
    hoy = dt.date.today().isoformat()
    doc = f"# 🔭 Vigía · semana al {hoy}\n\n_{len(items)} publicaciones revisadas (Reddit + Hacker News)._\n\n{texto}\n"
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    HIST.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(doc, encoding="utf-8")
    (HIST / f"{hoy}.md").write_text(doc, encoding="utf-8")
    print(f"✅ Vigía lista: {SALIDA}", flush=True)
    return SALIDA


if __name__ == "__main__":
    main("--ya" in sys.argv)
