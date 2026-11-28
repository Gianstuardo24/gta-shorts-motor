"""Lámina rápida de un video del lote: un cuadro por plano tomado del motor (sin render completo).
Uso: python3 previa28.py <id> [fracción=0.55] [planos separados por coma]  → /tmp/fv2/lote/<id>/rapida.jpg"""
import sys, subprocess, glob, os, pathlib, json
from PIL import Image, ImageDraw, ImageFont
import kit
v = kit.cargar(sys.argv[1]); fr = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
solo = sys.argv[3].split(",") if len(sys.argv) > 3 else None
T = json.loads((v.DIR / "datos.json").read_text())["T"]; ini = [0.0] + [T["c" + pl[0]] for pl in v.PLANOS[1:]] + [T["fin"]]
ts = [(round(ini[i] + (ini[i + 1] - ini[i]) * fr, 2), v.PLANOS[i][0]) for i in range(len(v.PLANOS)) if not solo or v.PLANOS[i][0] in solo]
for f in glob.glob(str(v.TMP / "q__*.png")): os.remove(f)
r = subprocess.run(["flock", "/tmp/render.lock", "python3", "/home/claude/prueba27/cuadros.py", f"/tmp/rr.lote_{v.ID}/escena.html", str(v.DIR / "datos.json"), str(v.TMP / "q_")] + [str(t) for t, _ in ts], capture_output=True, text=True)
if r.returncode: print(r.stdout[-600:], r.stderr[-1500:])
fs = sorted(glob.glob(str(v.TMP / "q__*.png"))); W, H, COLS = 270, 480, 7
fil = -(-len(fs) // COLS); im = Image.new("RGB", (W * min(COLS, max(1, len(fs))), (H + 30) * max(1, fil)), "#14110f"); d = ImageDraw.Draw(im)
try: f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
except Exception: f = ImageFont.load_default()
for i, q in enumerate(fs):
    x, y = (i % COLS) * W, (i // COLS) * (H + 30); im.paste(Image.open(q).resize((W, H)), (x, y + 30)); d.text((x + 8, y + 7), f"{ts[i][1]} · {ts[i][0]:.1f} s", fill="#f3ecd9", font=f)
im.save(v.TMP / "rapida.jpg", quality=86); print(v.TMP / "rapida.jpg", len(fs), "cuadros")
for q in fs: os.remove(q)
