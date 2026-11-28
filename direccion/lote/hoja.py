"""Vista previa secuencial de un video del lote: una lámina con un cuadro por plano (o por momento), rotulado.
Uso: python3 hoja.py <id>   (lee PREVIA = [(segundo, "rótulo"), ...] de <id>/video.py y el video montado)"""
import sys, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont
import kit
v = kit.cargar(sys.argv[1]); video = v.TMP / "montado.mp4"
if v.PREVIA == "auto":
    import json
    T = json.loads((v.DIR / "datos.json").read_text())["T"]; ini = [0.0] + [T["c" + pl[0]] for pl in v.PLANOS[1:]] + [T["fin"]]
    v.PREVIA = [(round(ini[i] + (ini[i + 1] - ini[i]) * 0.55, 2), v.PLANOS[i][0]) for i in range(len(v.PLANOS))]
W, H, COLS = 270, 480, 7
fil = -(-len(v.PREVIA) // COLS); im = Image.new("RGB", (W * COLS, (H + 34) * fil), "#14110f"); d = ImageDraw.Draw(im)
try: f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
except Exception: f = ImageFont.load_default()
for i, (t, r) in enumerate(v.PREVIA):
    q = v.TMP / "hq.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", str(video), "-frames:v", "1", str(q)], check=True)
    x, y = (i % COLS) * W, (i // COLS) * (H + 34)
    im.paste(Image.open(q).resize((W, H)), (x, y + 34)); d.text((x + 8, y + 8), f"{r} · {t:.1f} s", fill="#f3ecd9", font=f)
sal = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else v.TMP / "previa.jpg"; im.save(sal, quality=88); print(sal)
