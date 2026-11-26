"""Revision automatica de un video largo antes de entregarlo.
Uso: python3 revisar_largo.py datos.json salida_dir
Revisa: planos muy largos (>4.5 s en escenario) o muy cortos (<0.7 s), el mismo plano de afuera repetido en menos de 30 s,
cifras grandes con la camara acercada (tapan caras), y fondo cargado detras de los subtitulos (texto u objetos con mucho contraste).
Deja reporte.txt y revisar.jpg (cuadros con problema)."""
import sys, json, os, io, base64, pathlib, re
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from playwright.sync_api import sync_playwright
fd, out = sys.argv[1:3]; os.makedirs(out, exist_ok=True)
D = json.load(open(fd)); T = D["T"]; e = D["escenas"][0]
tt = lambda k: float(k) if isinstance(k, (int, float)) else (T.get(k) if k in T else None)
FIN = max(f["b"] for f in D["frases"])
pans = sorted([p for p in e["pan"] if tt(p["k"]) is not None], key=lambda p: tt(p["k"]))
zset = {z["x0"] + 537: z.get("set") for z in e["zonas"] if z["x0"] >= 99000}
def dentro(t):
    x = 0
    for p in pans:
        if tt(p["k"]) <= t: x = p["x"]
    return x
cortes = sorted({round(tt(p["k"]), 2) for p in pans} | {round(tt(z["k"]), 2) for z in e["zoom"] if z.get("dur", 1) <= 0.02 and tt(z["k"]) is not None})
cortes = [c for c in cortes if 0 <= c < FIN]
planos = []
FIN = min(FIN, T.get("s_end", FIN))
desl = {round(tt(p["k"]), 2) for p in pans if not p.get("corte")}
cortes = [c for c in cortes if c < FIN]
for a, b in zip(cortes, cortes[1:] + [FIN]):
    if b - a < 0.05 or round(a, 2) in desl: continue
    if planos and abs(planos[-1][1] - a) > 0.01: pass
    planos.append((a, b, dentro(a + 0.01)))
# fusionar cortes de zoom que caen dentro de un inserto (son movimientos de camara, no planos nuevos)
fus = []
for a, b, x in planos:
    if fus and x >= 99000 and fus[-1][2] == x: fus[-1] = (fus[-1][0], b, x)
    else: fus.append((a, b, x))
planos = fus
nums = [(tt(n["k"]), tt(n["fin"]) if n.get("fin") is not None else tt(n["k"]) + 4) for n in e.get("numeros", []) if tt(n["k"]) is not None]
prob = []
ultimo = {}
for a, b, x in planos:
    L = b - a
    if x < 99000 and L > 4.5: prob.append((a, f"plano largo en escenario ({L:.1f} s)"))
    if L < 0.7 and a > 0.5: prob.append((a, f"plano muy corto ({L:.2f} s)"))
    if x >= 99000:
        st = zset.get(x)
        if st in ultimo and a - ultimo[st] < 30 and st not in ("capituloH", "vitrina", "mesaCenital"): prob.append((a, f"'{st}' repetido a {a - ultimo[st]:.0f} s"))
        ultimo[st] = a
# render: zoom real y fondo detras de los subtitulos
aqui = pathlib.Path(__file__).parent / "escena"
med = [((a + b) / 2, a, b, x) for a, b, x in planos]
scores, Z, imgs = [], [], {}
with sync_playwright() as p:
    br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    pg.add_init_script(f"window.DATOS={json.dumps(D)};")
    pg.goto((aqui / "escena_h.html").as_uri()); pg.wait_for_function("window.LISTO===true", timeout=20000)
    for t, a, b, x in med:
        r = pg.evaluate(f"(()=>{{const c=document.getElementById('c');window.SIN_SUBS=true;render({t});const a=c.toDataURL('image/jpeg',0.9);window.SIN_SUBS=false;render({t});return [a,window.__Z||1,c.toDataURL('image/jpeg',0.9)]}})()")
        sin = Image.open(io.BytesIO(base64.b64decode(r[0].split(",", 1)[1]))).convert("L").crop((200, 0, 1720, 200))
        con = Image.open(io.BytesIO(base64.b64decode(r[2].split(",", 1)[1]))).convert("L").crop((200, 0, 1720, 200))
        A, B = np.asarray(sin, np.float32), np.asarray(con, np.float32)
        mask = np.asarray(Image.fromarray(((np.abs(A - B) > 40) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(15))) > 0
        ed = np.asarray(sin.filter(ImageFilter.FIND_EDGES), np.float32) > 50
        scores.append(float(ed[mask].mean()) if mask.sum() > 500 else 0.0); Z.append(r[1])
    def foto(t):
        r = pg.evaluate(f"(()=>{{window.SIN_SUBS=false;render({t});return document.getElementById('c').toDataURL('image/jpeg',0.85)}})()")
        return Image.open(io.BytesIO(base64.b64decode(r.split(",", 1)[1]))).resize((480, 270))
    sc = np.array(scores); umbral = max(0.06, float(np.median(sc)) * 3)
    for (t, a, b, x), s_, z in zip(med, scores, Z):
        if s_ > umbral: prob.append((a, f"fondo cargado detras de los subtitulos ({s_ * 100:.0f}% bordes)"))
        if z > 1.15 and any(n0 - 0.1 <= t <= n1 for n0, n1 in nums) and x < 99000: prob.append((a, f"cifra grande con zoom {z:.2f}"))
    prob.sort()
    fotos = [foto(min(b - 0.05, a + (b - a) / 2)) for a, m in prob for (t0, aa, b, x) in med if abs(aa - a) < 0.01][:40]
    br.close()
rep = [f"{len(planos)} planos, {len(prob)} avisos (umbral subtitulos {umbral * 100:.1f}%)"] + [f"{int(a // 60)}:{a % 60:05.2f}  {m}" for a, m in prob]
open(os.path.join(out, "reporte.txt"), "w").write("\n".join(rep)); print("\n".join(rep[:60]))
if fotos:
    cols = 4; hoja = Image.new("RGB", (cols * 480, ((len(fotos) + cols - 1) // cols) * 270))
    for i, (im, (a, m)) in enumerate(zip(fotos, prob)):
        d = ImageDraw.Draw(im); d.rectangle([0, 248, 480, 270], fill=(0, 0, 0)); d.text((4, 252), f"{int(a // 60)}:{a % 60:04.1f} {m[:60]}", fill=(255, 220, 0))
        hoja.paste(im, ((i % cols) * 480, (i // cols) * 270))
    hoja.save(os.path.join(out, "revisar.jpg"), quality=85)
