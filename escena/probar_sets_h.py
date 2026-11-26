"""Hoja de prueba de sets horizontales: python probar_sets_h.py base_datos.json salida.png set1[:opcJSON] set2 ...
Usa la escena 0 del datos base, reemplaza la zona 0 por el set, quita actores/props y renderiza t=T (env, 3.0)."""
import sys, json, base64, io, os, pathlib, copy
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
aqui = pathlib.Path(__file__).parent.resolve()
base = json.load(open(sys.argv[1])); out = sys.argv[2]; specs = sys.argv[3:]
T = float(os.environ.get("T", 3.0)); A = 640; B = 360
ims = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    for sp in specs:
        nom, _, op = sp.partition(":")
        d = copy.deepcopy(base)
        e = d["escenas"][0]
        z0 = dict(e["zonas"][0]); z0["set"] = nom
        if op: z0["o"] = json.loads(op)
        e["zonas"] = [z0]; e["pan"] = []; e["props"] = []; e["actores"] = []
        for k in ("grupos", "extras", "multitud"):
            e.pop(k, None)
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        msgs = []
        pg.on("pageerror", lambda ex: msgs.append(str(ex)))
        pg.add_init_script(f"window.DATOS={json.dumps(d)};")
        pg.goto((aqui / "escena_h.html").as_uri())
        pg.wait_for_function("window.LISTO===true", timeout=20000)
        url = pg.evaluate(f"(()=>{{render({T});return document.getElementById('c').toDataURL('image/jpeg',0.9)}})()")
        im = Image.open(io.BytesIO(base64.b64decode(url.split(',', 1)[1]))).resize((A, B))
        dr = ImageDraw.Draw(im); dr.rectangle([0, 0, 200, 22], fill=(0, 0, 0)); dr.text((6, 5), nom + (" ERR" if msgs else ""), fill=(255, 255, 0))
        if msgs: print(nom, "ERROR:", msgs[:2])
        ims.append(im); pg.close()
    b.close()
cols = 3; rows = (len(ims) + cols - 1) // cols
h = Image.new("RGB", (cols * A, rows * B))
for i, im in enumerate(ims): h.paste(im, ((i % cols) * A, (i // cols) * B))
h.save(out); print("ok", out)
