"""Hoja de poses de regresion (motor de Shorts): python3 hoja_poses.py salida.jpg  -> todas las poses en una imagen.
Usar cada vez que se toca figura() en escena.html (regla R-13 / doc 12)."""
import sys, base64, pathlib, io, glob
from playwright.sync_api import sync_playwright
from PIL import Image
esc = pathlib.Path("/home/claude/escena")
datos = pathlib.Path(sorted(glob.glob("/home/claude/d24/c17n/datos.json"))[0]).read_text()
out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/poses.jpg"
JS = r"""([tt,real])=>{DATOS.cuerpo=real;X.setTransform(1,0,0,1,0,0);X.globalAlpha=1;X.fillStyle='#39425a';X.fillRect(0,0,1080,1920);
 const P=[['parado'],['sostiene','taza'],['bebe','taza'],['lee','documento'],['explica'],['apunta'],['ofrece'],['ofrece','taza'],['saluda'],['piensa'],['telefono'],['celebra'],['arriba'],['cruzado'],['aplaude'],['teclea'],['camina'],['sentado'],['empuja'],['golpea']];const LK=['ejecutivo','cliente','vendedor','inventor','jugadora','gamer','sabio'];;
 P.forEach((p,i)=>{const cx=110+(i%5)*215,cy=430+Math.floor(i/5)*470;const ob=p[1]&&UTILERIA[p[1]]?(t)=>UTILERIA[p[1]](0,40,.5,t,{}):null;
  figura(cx,cy,.78,{look:LK[i%7],var:i%3?undefined:60+i},tt,p[0],i%4==3?'sorpresa':'feliz',1,ob);
  X.fillStyle='#fff';X.font='700 26px sans-serif';X.textAlign='center';X.fillText(p[0]+(p[1]?' + '+p[1]:''),cx,cy+44)});
 return document.getElementById('c').toDataURL('image/jpeg',0.92)}"""
ims = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.add_init_script(f"window.DATOS={datos};")
    pg.goto((esc / "escena.html").as_uri()); pg.wait_for_function("window.LISTO===true", timeout=20000)
    for t in ((1.26, "real"), (1.26, "pro")):
        d = pg.evaluate(JS, list(t)); ims.append(Image.open(io.BytesIO(base64.b64decode(d.split(",", 1)[1]))))
    b.close()
h = Image.new("RGB", (2160, 1920)); h.paste(ims[0], (0, 0)); h.paste(ims[1], (1080, 0)); h.save(out, quality=88); print("ok", out)
