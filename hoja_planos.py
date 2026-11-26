"""Hoja de planos: un cuadro por plano (mitad del plano), con minuto y lo que se ve. Para aprobar antes del render final.
Uso: python3 hoja_planos.py datos.json salida_prefijo [por_hoja=30]"""
import sys, json, io, base64, pathlib
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
fd, pre = sys.argv[1:3]; N = int(sys.argv[3]) if len(sys.argv) > 3 else 30
D = json.load(open(fd)); T = D["T"]; e = D["escenas"][0]
tt = lambda k: float(k) if isinstance(k, (int, float)) else T.get(k)
FIN = min(max(f["b"] for f in D["frases"]), T.get("s_end", 1e9))
pans = sorted([p for p in e["pan"] if tt(p["k"]) is not None], key=lambda p: tt(p["k"]))
zset = {z["x0"] + 537: z.get("set") for z in e["zonas"]}
def cam(t):
    x = 0
    for p in pans:
        if tt(p["k"]) <= t: x = p["x"]
    return x
desl = {round(tt(p["k"]), 2) for p in pans if not p.get("corte")}
cortes = sorted({round(tt(p["k"]), 2) for p in pans} | {round(tt(z["k"]), 2) for z in e["zoom"] if z.get("dur", 1) <= 0.02 and tt(z["k"]) is not None})
cortes = [c for c in cortes if 0 <= c < FIN]
pl = []
for a, b in zip(cortes, cortes[1:] + [FIN]):
    if b - a < 0.3 or a in desl: continue
    x = cam(a + 0.01)
    if pl and x >= 99000 and pl[-1][2] == x: pl[-1] = (pl[-1][0], b, x); continue
    pl.append((a, b, x))
ims = []
aqui = pathlib.Path(__file__).parent / "escena"
with sync_playwright() as p:
    br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    pg.add_init_script(f"window.DATOS={json.dumps(D)};")
    pg.goto((aqui / "escena_h.html").as_uri()); pg.wait_for_function("window.LISTO===true", timeout=20000)
    for a, b, x in pl:
        t = a + min(1.2, (b - a) * 0.6)
        r = pg.evaluate(f"(()=>{{render({t});return document.getElementById('c').toDataURL('image/jpeg',0.85)}})()")
        im = Image.open(io.BytesIO(base64.b64decode(r.split(",", 1)[1]))).resize((400, 225))
        d = ImageDraw.Draw(im); lab = f"{int(a // 60)}:{a % 60:04.1f}  {b - a:.1f}s  " + ("AFUERA " + (zset.get(x) or "") if x >= 99000 else "escena")
        d.rectangle([0, 205, 400, 225], fill=(0, 0, 0)); d.text((4, 209), lab, fill=(255, 220, 0) if x >= 99000 else (200, 230, 255))
        ims.append(im)
    br.close()
cols = 5
for h in range(0, len(ims), N):
    grupo = ims[h:h + N]; hoja = Image.new("RGB", (cols * 400, ((len(grupo) + cols - 1) // cols) * 225))
    for i, im in enumerate(grupo): hoja.paste(im, ((i % cols) * 400, (i // cols) * 225))
    hoja.save(f"{pre}_{h // N + 1}.jpg", quality=82); print(f"{pre}_{h // N + 1}.jpg", len(grupo))
print("planos", len(pl))
