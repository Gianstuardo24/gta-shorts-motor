"""E0 · control de cordura: el corpus congelado + el motor actual reproducen los videos ENTREGADOS el 25-nov.
Los entregados se renderizaron sin semilla (el grano del acabado "pro" es aleatorio) y pasaron por x264, así que no pueden
ser idénticos bit a bit: se compara con tolerancia. Se promedian bloques de 8x8 píxeles para quitar el grano y la compresión;
una escena, un texto o un objeto distinto deja diferencias grandes en algún bloque."""
import json, pathlib, subprocess, base64, io, numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright
A = pathlib.Path(__file__).parent; C = A / "corpus"
SEM = "(()=>{let s=12345;Math.random=()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}})();"
man = json.loads((C / "manifiesto.json").read_text()); res = {}
def bloques(a, b=8):
    h, w = a.shape[0] // b * b, a.shape[1] // b * b
    return a[:h, :w].reshape(h // b, b, w // b, b, 3).mean(axis=(1, 3))
with sync_playwright() as p:
    br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    for it in [i for i in man["items"] if i["tipo"] == "produccion"]:
        n = it["render"]["cuadros"]; idx = [int(n * k / 12) for k in range(12)] + [n - 1]
        pg = br.new_page(viewport={"width": 1080, "height": 1920}); pg.add_init_script(SEM)
        pg.add_init_script("window.DATOS=" + (C / "produccion" / it["id"] / "datos_render.json").read_text() + ";")
        pg.goto("file:///home/claude/escena/escena.html"); pg.wait_for_function("window.LISTO===true", timeout=30000)
        v = A / it["video"]["archivo"]; filas = []
        for i in idx:
            raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(v), "-vf", f"select=eq(n\\,{i})", "-vsync", "0", "-frames:v", "1",
                                  "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
            e = np.frombuffer(raw, np.uint8).reshape(1920, 1080, 3).astype(float)
            pg.evaluate(f"render({i / 30})")
            png = pg.evaluate("document.getElementById('c').toDataURL('image/png')")
            r = np.asarray(Image.open(io.BytesIO(base64.b64decode(png.split(',', 1)[1]))).convert("RGB")).astype(float)
            d = np.abs(e - r); db = np.abs(bloques(e) - bloques(r))
            mse = (d ** 2).mean(); psnr = 99 if mse == 0 else 10 * np.log10(255 ** 2 / mse)
            filas.append({"cuadro": i, "dif_media": round(d.mean(), 2), "dif_bloques_media": round(db.mean(), 2), "dif_bloque_max": round(db.max(), 1), "psnr": round(psnr, 1)})
        pg.close(); res[it["id"]] = filas
        print(f"{it['id']:5} PSNR mín {min(f['psnr'] for f in filas):5.1f} dB · dif. media máx {max(f['dif_media'] for f in filas):5.2f} · "
              f"bloques 8x8: media máx {max(f['dif_bloques_media'] for f in filas):5.2f}, peor bloque {max(f['dif_bloque_max'] for f in filas):5.1f}", flush=True)
    br.close()
(A / "informes" / "entregados_tolerancia.json").write_text(json.dumps(res, indent=1))
