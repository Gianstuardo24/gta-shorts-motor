"""Prueba 27 · saca cuadros PNG exactos de escena.html para comparar producción antes/después.
Uso: python3 cuadros.py ESCENA_HTML DATOS_JSON SALIDA_PREFIJO t1 [t2 ...]
"""
import sys, base64, pathlib, hashlib
from playwright.sync_api import sync_playwright

html = pathlib.Path(sys.argv[1]).resolve()
datos = pathlib.Path(sys.argv[2]).read_text()
pref = sys.argv[3]
ts = [float(x) for x in sys.argv[4:]]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    # semilla fija SOLO en esta herramienta (el grano de película usa Math.random)
    pg.add_init_script("(()=>{let s=12345;Math.random=()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}})();")
    pg.add_init_script(f"window.DATOS={datos};")
    pg.goto(html.as_uri())
    pg.wait_for_function("window.LISTO===true", timeout=20000)
    for t in ts:
        d = pg.evaluate(f"(()=>{{render({t});return document.getElementById('c').toDataURL('image/png')}})()")
        raw = base64.b64decode(d.split(",", 1)[1])
        f = pathlib.Path(f"{pref}_{t:06.2f}.png")
        f.write_bytes(raw)
        # hash de píxeles (no del PNG) para no depender de la compresión
        px = pg.evaluate("(()=>{const c=document.getElementById('c');const a=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let h=0x811c9dc5;for(let i=0;i<a.length;i+=1){h^=a[i];h=Math.imul(h,16777619)>>>0}return h.toString(16)})()")
        print(f.name, px)
    b.close()
