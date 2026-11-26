"""Prueba 27 · vuelca la hoja de textura (solo lectura) a PNG para diseñar el plano 06."""
import sys, base64, pathlib
from playwright.sync_api import sync_playwright
html = pathlib.Path("/home/claude/escena/escena.html").resolve()
datos = pathlib.Path("/home/claude/prueba27/p05/datos.json").read_text()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.add_init_script(f"window.DATOS={datos};")
    pg.goto(html.as_uri()); pg.wait_for_function("window.LISTO===true", timeout=20000)
    d = pg.evaluate("window.__p27.hoja(1).toDataURL('image/png')")
    pathlib.Path(sys.argv[1]).write_bytes(base64.b64decode(d.split(",",1)[1]))
    print(pg.evaluate("JSON.stringify(window.__p27.HOJA)"))
    b.close()
