"""Hoja de objetos: python3 hoja_props.py salida.jpg tipo1 tipo2 ...  (cada uno en su celda, t=2.5)"""
import sys, base64, pathlib, io, json
from playwright.sync_api import sync_playwright
from PIL import Image
datos = pathlib.Path("/home/claude/d24/c17n/datos.json").read_text()
out, tipos = sys.argv[1], sys.argv[2:]
JS = r"""([tipos,opts])=>{X.setTransform(1,0,0,1,0,0);X.fillStyle='#39425a';X.fillRect(0,0,1080,1920);window.__A=0;
 tipos.forEach((tp,i)=>{const cx=270+(i%2)*540,cy=560+Math.floor(i/2)*620;X.save();X.beginPath();X.rect(cx-270,cy-560,540,620);X.clip();
  try{UTILERIA[tp](cx,cy,(opts[tp]&&opts[tp].s)||0.8,2.5,opts[tp]||{})}catch(e){X.fillStyle='red';X.fillText(String(e),cx-200,cy)}
  X.restore();X.fillStyle='#fff';X.font='700 28px sans-serif';X.textAlign='center';X.fillText(tp,cx,cy+40)});
 return document.getElementById('c').toDataURL('image/jpeg',0.9)}"""
OP = {"capas": {"s": 1.0, "etiquetas": 1, "nombre": "FLAT WHITE"}, "bote": {"s": .8, "nombre": "THE LEONIDA"}, "bokehNV": {"s": .7},
      "nvPantalla": {"s": .8}, "mitad": {"s": .7, "n0": 0, "n1": .15, "half": "15%", "sinReloj": 1, "de": 0, "a": 1},
      "cajaGato": {"s": 1.0, "texto": "BOX"}, "zapatilla": {"s": .9}, "anillo": {"s": 1.2}, "dron": {"s": 1.5}, "rebota": {"s": .55, "texto": "HOW THEY MOVED"}, "pelota": {"s": 3, "color": "#1e88e5"}, "cajita": {"s": 2.0, "color": "#ef9a9a", "texto": "STRESS"}, "nariz": {"s": 1.2}}
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920}); pg.add_init_script(f"window.DATOS={datos};")
    pg.goto(pathlib.Path("/home/claude/escena/escena.html").as_uri()); pg.wait_for_function("window.LISTO===true", timeout=20000)
    d = pg.evaluate(JS, [tipos, OP]); b.close()
Image.open(io.BytesIO(base64.b64decode(d.split(",", 1)[1]))).resize((540, 960)).save(out, quality=88); print("ok", out)
