"""Clip de demostración de planos: python clip_planos.py base_datos.json salida.mp4 seg set1[:opcJSON] set2 ...
Cada plano dura 'seg' segundos, con empuje lento de cámara (zoom 1.0 -> 1.10). Sin subtítulos ni chips."""
import sys, json, base64, os, pathlib, copy, subprocess, tempfile
from playwright.sync_api import sync_playwright
aqui = pathlib.Path(__file__).parent.resolve()
base = json.load(open(sys.argv[1])); out = sys.argv[2]; seg = float(sys.argv[3]); specs = sys.argv[4:]
FPS = 30; tmp = tempfile.mkdtemp(); n = 0
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    for sp in specs:
        nom, _, op = sp.partition(":")
        d = copy.deepcopy(base)
        e = d["escenas"][0]; a0 = d["T"].get(str(e["desde"]), 0)
        z0 = dict(e["zonas"][0]); z0["set"] = nom; z0.pop("k", None)
        z0["o"] = json.loads(op) if op else {}
        e["zonas"] = [z0]; e["pan"] = []
        for k in ("props", "actores", "burbujas", "numeros", "sacudidas", "titulos", "chips"): e[k] = []
        e["zoom"] = [{"k": 0, "s": 1.0, "dur": 0.01, "y": 1250}, {"k": 0.02, "s": 1.06, "dur": seg, "y": 1250}]
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        pg.add_init_script(f"window.DATOS={json.dumps(d)};")
        pg.goto((aqui / "escena_h.html").as_uri())
        pg.wait_for_function("window.LISTO===true", timeout=20000)
        for f in range(int(seg * FPS)):
            url = pg.evaluate(f"(()=>{{render({a0 + f / FPS:.4f});return document.getElementById('c').toDataURL('image/jpeg',0.92)}})()")
            open(f"{tmp}/{n:05d}.jpg", "wb").write(base64.b64decode(url.split(',', 1)[1])); n += 1
        pg.close(); print(nom, "ok", flush=True)
    b.close()
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/%05d.jpg", "-vf", "scale=1920:1080",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", out], check=True)
print("ok", out, n, "cuadros")
