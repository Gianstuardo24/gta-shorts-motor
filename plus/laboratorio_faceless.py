"""LABORATORIO FACELESS (22-nov): baja videos de YouTube SOLO PARA ESTUDIARLOS y prepara su análisis.

Por cada video de estudio_faceless/lista.txt deja en estudio_faceless/analisis/<id>/:
  info.json        título, canal, vistas, duración, fecha, capítulos, descripción
  transcripcion.txt  lo que se dice, con la marca [mm:ss] cada ~30 s (de los subtítulos de YouTube)
  hoja.jpg         ~42 cuadros de todo el video (para "verlo" de una mirada)
  gancho.jpg       1 cuadro por segundo de los primeros 12 s
  cortes.json      cambios de plano detectados y cortes por minuto
El video queda en estudio_faceless/videos/ (360p). Es material ajeno: SOLO para entender; nunca se usa en un video nuestro.

Uso (desde ~/gta-shorts):
  ./venv/bin/pip install -U yt-dlp            (una vez, para tener la versión al día)
  ./venv/bin/python3 laboratorio_faceless.py  (baja y analiza lo que falte; se puede cortar y repetir)
"""
import re, sys, json, time, subprocess
from pathlib import Path

BASE = Path("estudio_faceless")
LISTA = BASE / "lista.txt"
VIDEOS = BASE / "videos"
ANALISIS = BASE / "analisis"


def cookies():
    try:
        nav = json.loads(Path("config.json").read_text()).get("cookies_navegador")
        return {"cookiesfrombrowser": (nav,)} if nav else {}
    except Exception:
        return {}


def lista():
    out = []
    for l in LISTA.read_text(encoding="utf-8").splitlines():
        m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", l)
        if m and not l.strip().startswith("#"):
            grupo = l.split("|")[0].strip() if "|" in l else ""
            out.append((m.group(1), grupo))
    return list(dict.fromkeys(out))


def bajar(vid):
    """Video 360p + datos. Los subtítulos van aparte (si YouTube los limita, el video igual queda)."""
    from yt_dlp import YoutubeDL
    (ANALISIS / vid).mkdir(parents=True, exist_ok=True)
    url = f"https://www.youtube.com/watch?v={vid}"
    base = {"quiet": True, "no_warnings": True, "outtmpl": str(VIDEOS / "%(id)s.%(ext)s"),
            "format": "bv*[height<=360][ext=mp4]+ba[ext=m4a]/b[height<=360][ext=mp4]/b[height<=480]/b",
            "merge_output_format": "mp4"}
    info, ultimo = None, None
    for extra in ({}, cookies()):
        try:
            with YoutubeDL({**base, **extra}) as y:
                info = y.extract_info(url, download=True)
            break
        except Exception as e:
            ultimo = e
    if not info:
        raise RuntimeError(str(ultimo)[:200])
    lang = (info.get("language") or "es")[:2]
    for extra in ({}, cookies()):
        try:
            with YoutubeDL({**base, **extra, "skip_download": True, "writesubtitles": True, "writeautomaticsub": True,
                            "subtitleslangs": [lang, f"{lang}-orig"], "subtitlesformat": "vtt"}) as y:
                y.download([url])
            if list(VIDEOS.glob(f"{vid}*.vtt")):
                break
        except Exception:
            time.sleep(5)
    return info


def vtt_a_texto(vid, idioma):
    """Subtítulos automáticos → texto limpio sin repeticiones, con [mm:ss] cada ~30 s."""
    cands = sorted(VIDEOS.glob(f"{vid}*.vtt"), key=lambda p: (idioma not in p.name, "orig" not in p.name))
    if not cands:
        return ""
    lineas, vistas, ult = [], set(), -99
    t = 0
    for l in cands[0].read_text(encoding="utf-8", errors="ignore").splitlines():
        m = re.match(r"(\d+):(\d+):(\d+)\.\d+ -->", l)
        if m:
            t = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            continue
        l = re.sub(r"<[^>]+>", "", l).strip()
        if not l or l.startswith(("WEBVTT", "Kind:", "Language:")) or l in vistas:
            continue
        vistas.add(l)
        if t - ult >= 30:
            lineas.append(f"\n[{t // 60:02d}:{t % 60:02d}] ")
            ult = t
        lineas.append(l + " ")
    return "".join(lineas).strip()


def ffmpeg(*a):
    return subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *a], capture_output=True, text=True)


def visual(vid, dur):
    v = VIDEOS / f"{vid}.mp4"
    d = ANALISIS / vid
    paso = max(4, dur / 42)
    ffmpeg("-i", str(v), "-vf", f"fps=1/{paso:.2f},scale=320:-2,tile=6x7:padding=4:color=black", "-frames:v", "1", "-q:v", "4", str(d / "hoja.jpg"))
    ffmpeg("-i", str(v), "-t", "12", "-vf", "fps=1,scale=360:-2,tile=4x3:padding=4:color=black", "-frames:v", "1", "-q:v", "4", str(d / "gancho.jpg"))
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(v), "-filter:v", "select='gt(scene,0.30)',showinfo", "-an", "-f", "null", "-"],
                       capture_output=True, text=True)
    cortes = [round(float(x), 1) for x in re.findall(r"pts_time:([\d.]+)", r.stderr)]
    primeros = [c for c in cortes if c <= 30]
    (d / "cortes.json").write_text(json.dumps({
        "cortes_total": len(cortes), "cortes_por_min": round(len(cortes) / max(dur / 60, 0.1), 1),
        "cortes_primeros_30s": len(primeros), "tiempos": cortes[:400]}, ensure_ascii=False))


def main():
    VIDEOS.mkdir(parents=True, exist_ok=True)
    ANALISIS.mkdir(parents=True, exist_ok=True)
    pendientes = [(v, g) for v, g in lista() if not (ANALISIS / v / "hoja.jpg").exists()]
    print(f"🎞️  {len(pendientes)} video(s) por estudiar")
    for i, (vid, grupo) in enumerate(pendientes, 1):
        print(f"[{i}/{len(pendientes)}] {vid} … ", end="", flush=True)
        try:
            info = bajar(vid)
        except Exception as e:
            print(f"⛔ no se pudo bajar: {e}")
            continue
        dur = info.get("duration") or 0
        lang = (info.get("language") or "es")[:2]
        d = ANALISIS / vid
        (d / "info.json").write_text(json.dumps({
            "id": vid, "grupo": grupo, "titulo": info.get("title"), "canal": info.get("channel"),
            "subs_canal": info.get("channel_follower_count"), "vistas": info.get("view_count"),
            "likes": info.get("like_count"), "comentarios": info.get("comment_count"), "duracion_s": dur,
            "fecha": info.get("upload_date"), "idioma": lang, "capitulos": info.get("chapters"),
            "tags": (info.get("tags") or [])[:20], "descripcion": (info.get("description") or "")[:3000]},
            ensure_ascii=False, indent=1))
        (d / "transcripcion.txt").write_text(vtt_a_texto(vid, lang), encoding="utf-8")
        visual(vid, dur)
        print(f"✅ {info.get('title', '')[:60]}")
        time.sleep(3)
    hechos = len([p for p in ANALISIS.glob("*/hoja.jpg")])
    print(f"\nListo: {hechos} videos con análisis en {ANALISIS}/  (avísale a Claude)")


if __name__ == "__main__":
    main()
