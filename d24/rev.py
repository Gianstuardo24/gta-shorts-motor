"""rev.py SLOT -> /tmp/rev_SLOT.jpg: un cuadro al 60% de cada plano + uno del cierre (4 columnas).
27i bloque 4 (opcional; sin opciones hace exactamente lo de antes):
  --dir CARPETA   el slot está en otra carpeta (por ejemplo, rehacer/<slot>); la hoja queda en esa carpeta
  --tiempos       escribe el segundo de cada cuadro
  --movil         además, vista de teléfono: los mismos cuadros a 390 px de ancho, en color y en gris"""
import sys, re, subprocess, argparse
ap = argparse.ArgumentParser(); ap.add_argument("slot"); ap.add_argument("--dir"); ap.add_argument("--tiempos", action="store_true")
ap.add_argument("--movil", action="store_true"); a = ap.parse_args()
S = a.slot; D = a.dir or f"/home/claude/d24/{S}"
ts = []
for l in open(f"{D}/planos.log"):
    m = re.match(r"\s*([\d.]+)-\s*([\d.]+)", l)
    if m: a_, b = float(m[1]), float(m[2]); ts.append(a_ + (b - a_) * 0.6)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{D}/v1.mp4"], capture_output=True, text=True).stdout)
ts.append(dur - 1.5)
sel = "+".join(f"eq(n\\,{int(t*30)})" for t in ts)
rows = (len(ts) + 3) // 4
FUENTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
tiempo = f",drawtext=fontfile={FUENTE}:text='%{{pts\\:hms}}':x=10:y=10:fontsize=30:fontcolor=white:box=1:boxcolor=black@0.55" if a.tiempos else ""
salida = f"{a.dir}/rev_{S}.jpg" if a.dir else f"/tmp/rev_{S}.jpg"
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", f"{D}/v1.mp4", "-vf", f"select='{sel}',scale=432:-2{tiempo},tile=4x{rows}:padding=4", "-vsync", "0", "-frames:v", "1", "-q:v", "3", salida])
print(salida, [round(t, 1) for t in ts])
if a.movil:
    for nombre, gris in (("movil", ""), ("movil_gris", ",hue=s=0")):
        out = salida.replace(".jpg", f"_{nombre}.jpg")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", f"{D}/v1.mp4", "-vf",
                        f"select='{sel}',scale=390:-2{gris}{tiempo},tile=4x{rows}:padding=6:color=white", "-vsync", "0", "-frames:v", "1", "-q:v", "3", out])
        print(out)
