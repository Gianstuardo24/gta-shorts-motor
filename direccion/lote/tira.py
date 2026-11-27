"""Hoja de contacto de un video del lote. Uso: python3 tira.py <id> <nombre> t1 t2 ... (deja /tmp/fv2/lote/<id>/<nombre>.jpg)"""
import sys, subprocess, glob, os, pathlib
from PIL import Image
vid, nombre, ts = sys.argv[1], sys.argv[2], sys.argv[3:]
AQUI = pathlib.Path(__file__).resolve().parent; TMP = pathlib.Path(f"/tmp/fv2/lote/{vid}"); TMP.mkdir(parents=True, exist_ok=True)
for f in glob.glob(str(TMP / "q__*.png")): os.remove(f)
r = subprocess.run(["flock", "/tmp/render.lock", "python3", "/home/claude/prueba27/cuadros.py", f"/tmp/rr.lote_{vid}/escena.html", str(AQUI / vid / "datos.json"), str(TMP / "q_")] + ts, capture_output=True, text=True)
if r.returncode: print(r.stdout[-600:], r.stderr[-1200:])
fs = sorted(glob.glob(str(TMP / "q__*.png"))); W, H = (270, 480) if len(fs) <= 6 else (216, 384)
im = Image.new("RGB", (W * len(fs), H))
for i, f in enumerate(fs): im.paste(Image.open(f).resize((W, H)), (i * W, 0))
im.save(TMP / f"{nombre}.jpg", quality=85); print(nombre, [f[-10:-4] for f in fs])
for f in fs: os.remove(f)
