"""Cuadros sueltos para revisar: python muestras.py datos.json salida.png t1 t2 ..."""
import sys, base64, pathlib, io, os
A = int(os.environ.get("ANCHO", 480)); B = A * 9 // 16
from playwright.sync_api import sync_playwright
from PIL import Image
aqui = pathlib.Path(__file__).parent.resolve()
datos = pathlib.Path(sys.argv[1]).read_text(); out = sys.argv[2]; ts = [float(x) for x in sys.argv[3:]]
ims = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.add_init_script(f"window.DATOS={datos};")
    pg.goto((aqui / "escena_h.html").as_uri())
    pg.wait_for_function("window.LISTO===true", timeout=20000)
    for t in ts:
        d = pg.evaluate(f"(()=>{{render({t});return document.getElementById('c').toDataURL('image/jpeg',0.9)}})()")
        ims.append(Image.open(io.BytesIO(base64.b64decode(d.split(",", 1)[1]))).resize((A, B)))
    b.close()
n = len(ims); cols = min(4, n); rows = (n + cols - 1) // cols
hoja = Image.new("RGB", (cols * A, rows * B))
for i, im in enumerate(ims):
    hoja.paste(im, ((i % cols) * A, (i // cols) * B))
hoja.save(out)
print("ok", out)
