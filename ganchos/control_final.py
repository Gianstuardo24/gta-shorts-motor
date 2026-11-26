"""CONTROL FINAL del video antes de subirlo: lo tecnico que, si falla, mata el video aunque el guion sea bueno.

Revisa (con ffmpeg/ffprobe):
  - formato: vertical 9:16, 1080x1920 o mas, 24-60 fps, duracion <= 180 s (y avisa si pasa del objetivo del perfil)
  - audio: loudness integrado ~ -14 LUFS (±2), pico real <= -1 dBTP, que haya audio
  - inicio: sin negro ni silencio en el primer segundo (el hook tiene que arrancar YA)
  - cuerpo: silencios largos (> 1,5 s) y video congelado (> 2 s) en el medio
  - metadatos (.txt al lado): titulo <= 100 caracteres, 3-5 hashtags, sin palabras de urgencia falsa
  - portada (.portada.jpg/.png) presente
Resultado: ✅ / ⚠️ / ❌ por punto y un JSON al lado del video (<video>.control.json). Codigo de salida 1 si hay ❌.

Uso:  python control_final.py "~/Desktop/YouTube/MillionDollarMistake/2026-11-23 Lun/20h - ....mp4"
      python control_final.py --nuevos 30     (todos los .mp4 de ~/Desktop/YouTube de los ultimos 30 min)
"""
import re, sys, json, time, subprocess
from pathlib import Path

RAIZ = Path("~/Desktop/YouTube").expanduser()
URGENCIA = re.compile(r"\b(last chance|before it'?s gone|hurry|ultima oportunidad|antes de que lo borren|corre|ya mismo|share or|comparte o)\b", re.I)


def ff(args, timeout=300):
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout)


def probe(v):
    r = ff(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate:format=duration", "-of", "json", str(v)])
    return json.loads(r.stdout or "{}")


def revisar(v):
    v = Path(v).expanduser()
    res = []
    ok = lambda k, m: res.append(("✅", k, m))
    warn = lambda k, m: res.append(("⚠️", k, m))
    bad = lambda k, m: res.append(("❌", k, m))
    info = probe(v)
    vs = [s for s in info.get("streams", []) if s.get("codec_type") == "video"]
    au = [s for s in info.get("streams", []) if s.get("codec_type") == "audio"]
    dur = float((info.get("format") or {}).get("duration") or 0)
    if not vs:
        bad("video", "no hay pista de video")
        return res
    w, h = vs[0].get("width") or 0, vs[0].get("height") or 0
    num, den = (vs[0].get("r_frame_rate") or "0/1").split("/")
    fps = float(num) / max(float(den), 1)
    (ok if h > w and abs(w / h - 9 / 16) < 0.02 else bad)("formato", f"{w}x{h} ({'vertical 9:16' if h > w else 'NO es vertical'})")
    (ok if h >= 1920 else warn)("resolucion", f"{h}p" + ("" if h >= 1920 else " (ideal 1920)"))
    (ok if 24 <= fps <= 60 else warn)("fps", f"{fps:.0f}")
    (ok if 0 < dur <= 60 else warn if dur <= 180 else bad)("duracion", f"{dur:.1f} s" + (" (Shorts: max 180 s)" if dur > 180 else ""))
    if not au:
        bad("audio", "no hay audio")
    else:
        r = ff(["ffmpeg", "-nostats", "-i", str(v), "-af", "ebur128=peak=true", "-f", "null", "-"])
        m_i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
        m_p = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
        if m_i:
            lufs = float(m_i[-1])
            (ok if -16 <= lufs <= -12 else warn)("volumen", f"{lufs:.1f} LUFS (objetivo -14)")
        if m_p:
            pk = float(m_p[-1])
            (ok if pk <= -1 else warn)("pico", f"{pk:.1f} dBTP (max -1)")
        r = ff(["ffmpeg", "-nostats", "-i", str(v), "-af", "silencedetect=noise=-40dB:d=0.5", "-f", "null", "-"])
        sil = [(float(a), float(b)) for a, b in zip(re.findall(r"silence_start: (-?[\d.]+)", r.stderr), re.findall(r"silence_end: ([\d.]+)", r.stderr))]
        ini = [x for x in sil if x[0] <= 0.1 and x[1] > 0.6]
        (bad if ini else ok)("inicio audio", f"silencio hasta {ini[0][1]:.1f} s: el hook arranca tarde" if ini else "la voz arranca de inmediato")
        largos = [x for x in sil if x[0] > 1 and x[1] - x[0] > 1.5 and x[1] < dur - 0.5]
        (warn if largos else ok)("silencios", ", ".join(f"{a:.1f}-{b:.1f} s" for a, b in largos[:4]) if largos else "sin silencios largos")
    r = ff(["ffmpeg", "-nostats", "-i", str(v), "-vf", "blackdetect=d=0.3:pix_th=0.10,freezedetect=n=0.003:d=2", "-an", "-f", "null", "-"])
    neg = [float(x) for x in re.findall(r"black_start:(-?[\d.]+)", r.stderr)]
    (bad if any(x <= 0.1 for x in neg) else ok)("inicio imagen", "empieza en NEGRO" if any(x <= 0.1 for x in neg) else "primer cuadro con imagen")
    cong = re.findall(r"freeze_start: ([\d.]+)", r.stderr)
    (warn if cong else ok)("imagen congelada", f"desde {', '.join(c[:5] + ' s' for c in cong[:3])}" if cong else "no")
    txt = v.with_suffix(".txt")
    if txt.exists():
        t = txt.read_text(encoding="utf-8", errors="ignore")
        lineas = [x.strip() for x in t.splitlines()]
        tit = ""
        for k, x in enumerate(lineas):            # formato de publicar.py: "TÍTULO:" y el titulo en la linea siguiente
            if re.match(r"^(t[ií]tulo|title)\s*:", x, re.I):
                resto = re.sub(r"^(t[ií]tulo|title)\s*:\s*", "", x, flags=re.I)
                tit = resto or next((y for y in lineas[k + 1:] if y), "")
                break
        if not tit:
            tit = next((y for y in lineas if y), "")
        (ok if 0 < len(tit) <= 100 else bad)("titulo", f"{len(tit)} caracteres")
        tags = re.findall(r"#\w+", t)
        (ok if 3 <= len(tags) <= 5 else warn)("hashtags", f"{len(tags)} (ideal 3-5)")
        u = URGENCIA.search(t)
        (bad if u else ok)("urgencia falsa", f"aparece '{u.group(0)}'" if u else "no")
    else:
        warn("metadatos", "no encontre el .txt con titulo y descripcion")
    portada = [p for p in (v.with_suffix(".portada.jpg"), v.with_suffix(".portada.png"), v.parent / (v.stem + ".portada.jpg")) if p.exists()]
    (ok if portada else warn)("portada", "lista" if portada else "falta (.portada.jpg); se usará el primer cuadro")
    return res


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--nuevos":
        mins = float(a[1]) if len(a) > 1 else 30
        videos = [p for p in RAIZ.rglob("*.mp4") if time.time() - p.stat().st_mtime < mins * 60]
    else:
        videos = [Path(x).expanduser() for x in a]
    malos = 0
    for v in videos:
        res = revisar(v)
        print(f"\n🎞️ {v.name}")
        for s, k, m in res:
            print(f"   {s} {k}: {m}")
        hay_mal = any(s == "❌" for s, _, _ in res)
        malos += hay_mal
        print("   → " + ("❌ NO subir hasta corregir" if hay_mal else "✅ listo para subir" if not any(s == "⚠️" for s, _, _ in res) else "⚠️ se puede subir; revisa los avisos"))
        v.with_suffix(".control.json").write_text(json.dumps([{"estado": s, "punto": k, "detalle": m} for s, k, m in res], ensure_ascii=False, indent=1))
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()
