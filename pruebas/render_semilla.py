"""Camino real de producción con semilla fija (decisión D4: opcional y SOLO para pruebas).
Ejecuta escena/render.py tal cual, sin modificarlo; solo agrega la semilla al abrir la página.
Uso: python3 render_semilla.py t0 t1 fps salida.mp4 datos.json  (mismos argumentos que render.py)"""
import sys, runpy
import playwright.sync_api._generated as gen
SEMILLA_JS = "(()=>{let s=12345;Math.random=()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}})();"
_orig = gen.Browser.new_page
def _new_page(self, *a, **k):
    pg = _orig(self, *a, **k); pg.add_init_script(SEMILLA_JS); return pg
gen.Browser.new_page = _new_page
sys.argv = ["render.py"] + sys.argv[1:]
runpy.run_path("/home/claude/escena/render.py", run_name="__main__")
