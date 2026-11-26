import json, subprocess, datetime as dt
from pathlib import Path
from yt_dlp import YoutubeDL

# ---------------- configuracion (opcional en config.json -> "radar") ----------------
CFG = json.loads(Path("config.json").read_text()) if Path("config.json").exists() else {}
R = CFG.get("radar", {})
BUSQUEDAS = R.get("busquedas", ["GTA 6", "GTA 6 noticias", "GTA 6 secretos", "GTA 6 gameplay",
                                "GTA 6 shorts", "GTA VI news"])
POR_BUSQUEDA = R.get("por_busqueda", 30)   # resultados recientes por busqueda
REVISAR = R.get("revisar", 30)             # cuantos candidatos revisar en detalle
DIAS = R.get("dias", 7)                    # solo videos de los ultimos N dias

PROMPT = """Eres estratega de YouTube Shorts de gaming para un canal en espanol sobre GTA 6.
Te paso los videos de GTA 6 con MAS VISTAS POR HORA de los ultimos dias (ranking numerado).
Analiza, breve y esquematico, en markdown:
1. Temas calientes (3 a 5): cual es y por que esta funcionando.
2. Patrones de titulos y hooks que se repiten en los que mas crecen.
3. 6 ideas de Shorts PROPIOS para nuestro canal. Para cada una: titulo, hook (primera frase),
   el angulo diferente que aportamos (no copiar al otro creador) y el numero del video que la inspira.
No inventes datos: si algo es rumor, dilo."""


def buscar():
    vistos = {}
    with YoutubeDL({"quiet": True, "extract_flat": True, "skip_download": True,
                    "ignoreerrors": True}) as y:
        for q in BUSQUEDAS:
            print(f"🔎 Buscando: {q}")
            info = y.extract_info(f"ytsearchdate{POR_BUSQUEDA}:{q}", download=False) or {}
            for e in info.get("entries") or []:
                if e and e.get("id") and e["id"] not in vistos:
                    vistos[e["id"]] = e
    cand = sorted(vistos.values(), key=lambda e: e.get("view_count") or 0, reverse=True)
    return cand[:REVISAR]


def pico_mas_visto(heatmap):
    if not heatmap:
        return None
    h = max(heatmap, key=lambda x: x.get("value", 0))
    return round(h.get("start_time", 0))


def detalles(candidatos):
    ahora = dt.datetime.now(dt.timezone.utc).timestamp()
    out = []
    with YoutubeDL({"quiet": True, "skip_download": True, "ignoreerrors": True,
                    "noplaylist": True}) as y:
        for k, e in enumerate(candidatos, 1):
            print(f"   📊 {k}/{len(candidatos)}  {(e.get('title') or '')[:60]}")
            i = y.extract_info(f"https://www.youtube.com/watch?v={e['id']}", download=False)
            if not i:
                continue
            ts = i.get("timestamp")
            if not ts and i.get("upload_date"):
                ts = dt.datetime.strptime(i["upload_date"], "%Y%m%d").replace(
                    tzinfo=dt.timezone.utc).timestamp()
            if not ts:
                continue
            horas = max(1.0, (ahora - ts) / 3600)
            if horas > DIAS * 24:
                continue
            vistas = i.get("view_count") or 0
            dur = i.get("duration") or 0
            out.append({
                "titulo": i.get("title", ""), "canal": i.get("channel") or i.get("uploader") or "",
                "vistas": vistas, "likes": i.get("like_count") or 0,
                "comentarios": i.get("comment_count") or 0, "horas": round(horas, 1),
                "vph": round(vistas / horas), "duracion": dur,
                "tipo": "Short" if dur <= 180 else "Largo",
                "pico": pico_mas_visto(i.get("heatmap")),
                "url": f"https://www.youtube.com/watch?v={i['id']}",
            })
    return sorted(out, key=lambda v: v["vph"], reverse=True)


def mm_ss(s):
    return f"{s // 60}:{s % 60:02d}" if s is not None else "-"


def main():
    candidatos = buscar()
    print(f"\n📋 {len(candidatos)} candidatos. Revisando detalles...")
    videos = detalles(candidatos)
    if not videos:
        print("⚠️ No encontre videos recientes. Prueba subir 'dias' en config.json")
        return

    fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    filas = ["| # | Vistas/hora | Vistas | Tipo | Pico más visto | Título | Canal |",
             "|---|---|---|---|---|---|---|"]
    lista = []
    for n, v in enumerate(videos, 1):
        titulo = v["titulo"].replace("|", "/")
        filas.append(f"| {n} | **{v['vph']:,}** | {v['vistas']:,} | {v['tipo']} | {mm_ss(v['pico'])} "
                     f"| [{titulo}]({v['url']}) | {v['canal']} |")
        lista.append(f"{n}. [{v['tipo']}] {v['titulo']} | canal: {v['canal']} | vistas: {v['vistas']} "
                     f"| hace {v['horas']} h | vistas/hora: {v['vph']} | likes: {v['likes']} "
                     f"| comentarios: {v['comentarios']}")

    print("\n🧠 Claude analizando tendencias...")
    r = subprocess.run(["claude", "-p", PROMPT], input="\n".join(lista),
                       capture_output=True, text=True)
    analisis = r.stdout.strip() or "_(No se pudo generar el análisis)_"

    Path("radar").mkdir(exist_ok=True)
    salida = Path("radar") / f"gta_{dt.datetime.now().strftime('%Y%m%d_%H%M')}.md"
    salida.write_text("\n".join([
        f"# 📡 Radar GTA 6: {fecha}", "",
        f"Videos de los últimos {DIAS} días, ordenados por **vistas por hora** (lo que crece más rápido ahora).",
        "", *filas, "", "---", "", "## 🧠 Análisis e ideas", "", analisis, ""]), encoding="utf-8")

    print("\n🔥 Top 10 por vistas/hora:")
    for n, v in enumerate(videos[:10], 1):
        print(f"  {n:>2}. {v['vph']:>8,}/h  [{v['tipo']}]  {v['titulo'][:70]}")
    print(f"\n✅ Radar completo en: {salida}")


if __name__ == "__main__":
    main()
