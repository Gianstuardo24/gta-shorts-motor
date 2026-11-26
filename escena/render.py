"""Renderiza escena.html cuadro a cuadro (tiempo fijo, 30 fps) y arma un mp4 con ffmpeg.
Uso: python render.py [desde] [hasta] [fps] [salida.mp4]
"""
import sys, base64, subprocess, pathlib
from playwright.sync_api import sync_playwright

aqui = pathlib.Path(__file__).parent.resolve()
t0 = float(sys.argv[1]) if len(sys.argv) > 1 else 0
t1 = float(sys.argv[2]) if len(sys.argv) > 2 else None
fps = int(sys.argv[3]) if len(sys.argv) > 3 else 30
out = sys.argv[4] if len(sys.argv) > 4 else str(aqui / "escena.mp4")
datos = pathlib.Path(sys.argv[5]).read_text() if len(sys.argv) > 5 else None

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    if datos:
        pg.add_init_script(f"window.DATOS={datos};")
    pg.goto((aqui / "escena.html").as_uri())
    pg.wait_for_function("window.LISTO===true", timeout=20000)
    if t1 is None:
        t1 = pg.evaluate("window.DUR")
    n = int((t1 - t0) * fps)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(n):
        d = pg.evaluate(f"(()=>{{render({t0 + i / fps});return document.getElementById('c').toDataURL('image/jpeg',0.92)}})()")
        ff.stdin.write(base64.b64decode(d.split(",", 1)[1]))
        if i % 60 == 0:
            print(f"{i}/{n}", flush=True)
    ff.stdin.close()
    ff.wait()
    b.close()
print("ok", out)
