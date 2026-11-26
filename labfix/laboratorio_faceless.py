"""LABORATORIO FACELESS (22-nov, v2): baja videos de YouTube SOLO PARA ESTUDIARLOS y prepara su análisis.

Por cada video de estudio_faceless/lista.txt deja en estudio_faceless/analisis/<id>/:
  info.json        título, canal, vistas, duración, fecha, capítulos, descripción
  transcripcion.txt  lo que se dice, con la marca [mm:ss] cada ~30 s (de los subtítulos de YouTube)
  hoja.jpg         ~42 cuadros de todo el video (para "verlo" de una mirada)
  gancho.jpg       1 cuadro por segundo de los primeros 12 s
  cortes.json      cambios de plano detectados y cortes por minuto
El video queda en estudio_faceless/videos/ (360p). Es material ajeno: SOLO para entender; nunca se usa en un video nuestro.

v2:
  - Un video cuenta como listo solo si tiene hoja.jpg Y transcripción. Si falta algo → ⚠️ y se reintenta la próxima vez
    (si a un video ya tiene hoja, solo se piden los subtítulos; no se vuelve a bajar).
  - Subtítulos con pausas y reintentos (evita el "429 Too Many Requests"). Si YouTube no tiene subtítulos
    después de 3 corridas, se deja como "sin subtítulos" y no se insiste más.
  - Los avisos internos de yt-dlp ya no ensucian la pantalla: se ve una línea por video y un resumen al final.

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
ESPERAS_SUBS = (0, 15, 45)      # segundos antes de cada intento de subtítulos
MAX_CORRIDAS_SIN_SUBS = 3       # después de esto se acepta que el video no tiene subtítulos


class Silencio:
    """Recibe los mensajes de yt-dlp en vez de imprimirlos; guarda el último error."""
    def __init__(self):
        self.ultimo = ""

    def debug(self, m):
        pass

    def info(self, m):
        pass

    def warning(self, m):
        pass

    def error(self, m):
        self.ultimo = re.sub(r"^ERROR:\s*", "", str(m))[:160]


def cookies():
    try:
        nav = json.loads(Path("config.json").read_text()).get("cookies_navegador")
        return {"cookiesfrombrowser": (nav,)} if nav else {}
    except Exception:
        return {}


def variantes():
    """Primero sin cookies; si falla, con las cookies del navegador (si están configuradas)."""
    c = cookies()
    return [{}, c] if c else [{}]


def lista():
    out = []
    for l in LISTA.read_text(encoding="utf-8").splitlines():
        m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", l)
        if m and not l.strip().startswith("#"):
            grupo = l.split("|")[0].strip() if "|" in l else ""
            out.append((m.group(1), grupo))
    return list(dict.fromkeys(out))


def opciones_base():
    return {"quiet": True, "no_warnings": True, "noprogress": True,
            "outtmpl": str(VIDEOS / "%(id)s.%(ext)s"), "retries": 5, "extractor_retries": 3,
            "format": "bv*[height<=360][ext=mp4]+ba[ext=m4a]/b[height<=360][ext=mp4]/b[height<=480]/b",
            "merge_output_format": "mp4"}


def bajar_video(vid):
    """Video 360p + datos. Devuelve info de yt-dlp."""
    from yt_dlp import YoutubeDL
    url = f"https://www.youtube.com/watch?v={vid}"
    ultimo = ""
    for extra in variantes():
        log = Silencio()
        try:
            with YoutubeDL({**opciones_base(), **extra, "logger": log}) as y:
                info = y.extract_info(url, download=True)
            if info and (VIDEOS / f"{vid}.mp4").exists():
                return info
        except Exception as e:
            ultimo = log.ultimo or str(e)[:160]
    raise RuntimeError(ultimo or "no se pudo bajar")


def subtitulos(vid, lang):
    """Pide los subtítulos con pausas entre intentos. True si quedó algún .vtt."""
    from yt_dlp import YoutubeDL
    if list(VIDEOS.glob(f"{vid}*.vtt")):
        return True
    url = f"https://www.youtube.com/watch?v={vid}"
    for espera in ESPERAS_SUBS:
        if espera:
            time.sleep(espera)
        for extra in variantes():
            try:
                with YoutubeDL({**opciones_base(), **extra, "logger": Silencio(), "skip_download": True,
                                "writesubtitles": True, "writeautomaticsub": True,
                                "subtitleslangs": [lang, f"{lang}-orig"], "subtitlesformat": "vtt",
                                "sleep_interval_subtitles": 2}) as y:
                    y.download([url])
            except Exception:
                pass
            if list(VIDEOS.glob(f"{vid}*.vtt")):
                return True
    return False


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
    return (d / "hoja.jpg").exists()


def estado(vid):
    """(tiene hoja, tiene transcripción o se aceptó que no hay subtítulos)."""
    d = ANALISIS / vid
    t = d / "transcripcion.txt"
    texto = (t.exists() and t.stat().st_size > 50) or corridas_sin_subs(vid) >= MAX_CORRIDAS_SIN_SUBS
    return (d / "hoja.jpg").exists(), texto


def corridas_sin_subs(vid):
    f = ANALISIS / vid / "sin_subtitulos.txt"
    try:
        return int(f.read_text().strip() or 0)
    except Exception:
        return 0


def main():
    VIDEOS.mkdir(parents=True, exist_ok=True)
    ANALISIS.mkdir(parents=True, exist_ok=True)
    todos = lista()
    pendientes = [(v, g) for v, g in todos if not all(estado(v))]
    print(f"🎞️  {len(pendientes)} video(s) por estudiar (de {len(todos)} en la lista)")
    completos, parciales, fallidos = [], [], []
    for i, (vid, grupo) in enumerate(pendientes, 1):
        print(f"[{i}/{len(pendientes)}] {vid} … ", end="", flush=True)
        d = ANALISIS / vid
        d.mkdir(parents=True, exist_ok=True)
        tiene_hoja, _ = estado(vid)
        try:
            if tiene_hoja and (d / "info.json").exists():
                datos = json.loads((d / "info.json").read_text(encoding="utf-8"))
                titulo, lang = datos.get("titulo") or vid, datos.get("idioma") or "es"
            else:
                info = bajar_video(vid)
                dur = info.get("duration") or 0
                lang = (info.get("language") or "es")[:2]
                titulo = info.get("title") or vid
                (d / "info.json").write_text(json.dumps({
                    "id": vid, "grupo": grupo, "titulo": titulo, "canal": info.get("channel"),
                    "subs_canal": info.get("channel_follower_count"), "vistas": info.get("view_count"),
                    "likes": info.get("like_count"), "comentarios": info.get("comment_count"), "duracion_s": dur,
                    "fecha": info.get("upload_date"), "idioma": lang, "capitulos": info.get("chapters"),
                    "tags": (info.get("tags") or [])[:20], "descripcion": (info.get("description") or "")[:3000]},
                    ensure_ascii=False, indent=1))
                if not visual(vid, dur):
                    raise RuntimeError("ffmpeg no pudo armar la hoja de cuadros")
        except Exception as e:
            print(f"⛔ {str(e)[:120]}  (se reintenta la próxima vez)")
            fallidos.append(vid)
            continue
        if subtitulos(vid, lang):
            (d / "transcripcion.txt").write_text(vtt_a_texto(vid, lang), encoding="utf-8")
        if all(estado(vid)):
            print(f"✅ {titulo[:60]}")
            completos.append(vid)
        else:
            n = corridas_sin_subs(vid) + 1
            (d / "sin_subtitulos.txt").write_text(str(n))
            queda = "no se insiste más" if n >= MAX_CORRIDAS_SIN_SUBS else "se reintenta la próxima vez"
            print(f"⚠️  {titulo[:50]} — sin transcripción ({queda})")
            parciales.append(vid)
        time.sleep(3)
    listos = len([v for v, _ in todos if all(estado(v))])
    print(f"\nResumen: ✅ {len(completos)} nuevos completos · ⚠️ {len(parciales)} sin transcripción · ⛔ {len(fallidos)} sin bajar")
    for etiqueta, ids in (("⚠️  sin transcripción", parciales), ("⛔ sin bajar", fallidos)):
        if ids:
            print(f"   {etiqueta}: {', '.join(ids)}")
    print(f"Listo: {listos}/{len(todos)} videos completos en {ANALISIS}/  (avísale a Claude)")


if __name__ == "__main__":
    main()
