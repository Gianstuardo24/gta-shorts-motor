"""rev.py SLOT -> /tmp/rev_SLOT.jpg: un cuadro al 60% de cada plano + uno del cierre (4 columnas)."""
import sys, re, subprocess
S = sys.argv[1]; D = f"/home/claude/d24/{S}"
ts = []
for l in open(f"{D}/planos.log"):
    m = re.match(r"\s*([\d.]+)-\s*([\d.]+)", l)
    if m: a, b = float(m[1]), float(m[2]); ts.append(a + (b - a) * 0.6)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{D}/v1.mp4"], capture_output=True, text=True).stdout)
ts.append(dur - 1.5)
sel = "+".join(f"eq(n\\,{int(t*30)})" for t in ts)
rows = (len(ts) + 3) // 4
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", f"{D}/v1.mp4", "-vf", f"select='{sel}',scale=432:-2,tile=4x{rows}:padding=4", "-vsync", "0", "-frames:v", "1", "-q:v", "3", f"/tmp/rev_{S}.jpg"])
print(f"/tmp/rev_{S}.jpg", [round(t, 1) for t in ts])
