"""Prueba escenarios en un Short: cambia los sets de sus zonas y saca cuadros a una hoja.
Uso: python3 probar_sets.py datos.json salida.png 'set1|{"hora":"noche"}' 'set2' ...   (uno por zona; '-' deja el original)
Opcional: TIEMPOS='3,12.5,...' fuerza los tiempos de cada cuadro."""
import sys, json, os, base64, pathlib, io
from playwright.sync_api import sync_playwright
from PIL import Image

datos = json.load(open(sys.argv[1])); out = sys.argv[2]; specs = sys.argv[3:]
e = datos["escenas"][0]; T = datos["T"]
pans = {p["k"]: p["x"] for p in e.get("pan", [])}
for i, z in enumerate(e["zonas"]):
    if i < len(specs) and specs[i] != "-":
        nombre, _, op = specs[i].partition("|")
        z["set"] = nombre; z.pop("luz", None); z.pop("neon", None)
        if op: z["o"] = json.loads(op)
    z.setdefault("cam", pans.get(z.get("k"), 0 if z["x0"] < 0 else z["x0"]))
ts = [float(x) for x in os.environ["TIEMPOS"].split(",")] if os.environ.get("TIEMPOS") else \
     [(T.get(z["k"], 0) if z.get("k") else 0) + 2.2 for z in e["zonas"]]
aqui = pathlib.Path("/home/claude/escena")
ims = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.add_init_script(f"window.DATOS={json.dumps(datos)};")
    pg.on("pageerror", lambda ex: print("ERROR JS:", ex))
    pg.goto((aqui / "escena.html").as_uri()); pg.wait_for_function("window.LISTO===true", timeout=20000)
    for t in ts:
        d = pg.evaluate(f"(()=>{{render({t});return document.getElementById('c').toDataURL('image/jpeg',0.85)}})()")
        ims.append(Image.open(io.BytesIO(base64.b64decode(d.split(',', 1)[1]))).resize((360, 640)))
    b.close()
hoja = Image.new("RGB", (360 * len(ims), 640))
for i, im in enumerate(ims): hoja.paste(im, (i * 360, 0))
hoja.save(out); print("ok", out, [round(t, 1) for t in ts])
