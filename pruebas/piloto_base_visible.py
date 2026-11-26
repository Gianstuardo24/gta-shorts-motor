#!/usr/bin/env python3
"""Piloto 27i, caso C: dónde se VE el fondo base de CTA (pintarBase se reemplaza por un color testigo, solo en la memoria de la página).
Uso: python3 piloto_base_visible.py MOTOR DATOS SALIDA.json MEDICION.json"""
import json, pathlib, sys
sys.path.insert(0, "/home/claude/pruebas"); import regresion as R
from playwright.sync_api import sync_playwright
motor, datos, salida = sys.argv[1], sys.argv[2], sys.argv[3]
M = json.load(open(sys.argv[4])); ns = [c["n"] for c in M["cuadros"]]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920}); pg.add_init_script(R.SEMILLA_JS)
    pg.add_init_script(f"window.DATOS={pathlib.Path(datos).read_text()};"); pg.goto(pathlib.Path(motor).resolve().as_uri()); pg.wait_for_function("window.LISTO===true", timeout=30000)
    pg.evaluate("""(()=>{pintarBase=function(){X.save();X.setTransform(1,0,0,1,0,0);X.fillStyle='#ff00ff';X.fillRect(0,0,W,H);X.restore()};
      window.__vis=function(t){render(t);const d=X.getImageData(0,0,W,H).data;let n=0;for(let y=0;y<H;y+=2)for(let x=0;x<W;x+=2){const i=(y*W+x)*4;if(d[i]>200&&d[i+1]<60&&d[i+2]>200)n++}return +(100*n*4/(W*H)).toFixed(2)};return true})()""")
    res = {n: pg.evaluate(f"window.__vis({n/30})") for n in ns}
    b.close()
json.dump(res, open(salida, "w"))
vis = [n for n, v in res.items() if v > 0]
print("cuadros con el fondo base de CTA visible:", len(vis))
runs = []
for n in sorted(vis):
    if runs and n == runs[-1][1] + 1: runs[-1][1] = n
    else: runs.append([n, n])
for a, b2 in runs: print(f"  {a}–{b2} ({a/30:.2f}–{b2/30:.2f} s) · máx {max(res[n] for n in range(a, b2+1))} % del cuadro")
