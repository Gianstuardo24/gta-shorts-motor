#!/usr/bin/env python3
"""Prueba de cobertura de sets (27i, bloque 1b). Solo lee: no modifica el motor ni los datos.

Para cada set que usan los 7 videos del corpus, dibuja la zona sola sobre un lienzo pintado de un color testigo
(magenta) y cuenta los píxeles que quedan sin cubrir dentro del área que puede encuadrar la cámara:
  x de -60 a 1.140 (ancho de un encuadre más margen por la respiración y la cámara en mano)
  y de -300 a 2.800 (más abajo que el encuadre más bajo medido: 2.255 en wk2)
Se mide con perfil de fondos (DATOS.fondos) y sin él.

Uso:  python3 cobertura_sets.py [--motor RUTA/escena.html] [--salida informe.json]
"""
import argparse, json, pathlib, sys
sys.path.insert(0, "/home/claude/pruebas"); import regresion as R
from playwright.sync_api import sync_playwright

CORPUS = pathlib.Path("/home/claude/pruebas/corpus/produccion")
SLOTS = ["wd2", "wk2", "wc1", "wm2", "wr1", "wge2", "wgs1"]
VENTANAS = [(-300, 1620), (880, 2800)]
ESCALAS = [1.03, 1.27, 1.49]            # escalas reales de la cámara (exterior, acercamientos típicos y máximo medido)
SUBPIXEL = [0.0, 0.37, 0.71]
JS = """window.__cobS=function(z,s,dy,perfil){
  const prev=DATOS.fondos; DATOS.fondos=perfil?(prev||{base:'pedido'}):undefined; window.__A=0;let n=0,ys=[];
  for(let y0=-250;y0<2800;y0+=Math.floor(1700/s)){X.setTransform(1,0,0,1,0,0);X.globalAlpha=1;X.fillStyle='#ff00ff';X.fillRect(0,0,W,H);
    X.setTransform(s,0,0,s,60*s+dy,-y0*s+dy);zonaDeco(z,5,1);X.setTransform(1,0,0,1,0,0);
    const vis=Math.min(H,Math.round((2800-y0)*s));const d=X.getImageData(0,0,W,vis).data;
    for(let i=0;i<d.length;i+=4){if(d[i]>200&&d[i+1]<60&&d[i+2]>200){n++;const py=((i/4)/W)|0;ys.push(Math.round(y0+py/s))}}}
  DATOS.fondos=prev;return {n,y:ys.length?[Math.min(...ys.slice(0,50000)),Math.max(...ys.slice(0,50000))]:null}};
window.__cob=function(z,y0,y1,perfil){
  const prev=DATOS.fondos; DATOS.fondos=perfil?(prev||{base:'pedido'}):undefined; window.__A=0;
  X.setTransform(1,0,0,1,0,0);X.globalAlpha=1;X.fillStyle='#ff00ff';X.fillRect(0,0,W,H);
  const wx0=-60,wx1=1140,sx=W/(wx1-wx0),sy=H/(y1-y0);X.setTransform(sx,0,0,sy,-wx0*sx,-y0*sy);
  zonaDeco(z,5,1);X.setTransform(1,0,0,1,0,0);DATOS.fondos=prev;
  const d=X.getImageData(0,0,W,H).data;let n=0,ymin=1e9,ymax=-1e9,xmin=1e9,xmax=-1e9;
  for(let i=0;i<d.length;i+=4){if(d[i]>200&&d[i+1]<60&&d[i+2]>200){n++;const p=i/4,px=p%W,py=(p/W)|0;const wy=y0+py/sy,wx=wx0+px/sx;
    if(wy<ymin)ymin=wy;if(wy>ymax)ymax=wy;if(wx<xmin)xmin=wx;if(wx>xmax)xmax=wx}}
  return {n,pct:+(100*n/(W*H)).toFixed(3),y:[Math.round(ymin),Math.round(ymax)],x:[Math.round(xmin),Math.round(xmax)]}};true;"""


def zonas_del_corpus():
    vistos = {}
    for s in SLOTS:
        d = json.loads((CORPUS / s / "datos_render.json").read_text())
        for e in d["escenas"]:
            for z in e.get("zonas") or []:
                clave = (z["set"], json.dumps(z.get("o", {}), sort_keys=True))
                vistos.setdefault(clave, {"set": z["set"], "o": z.get("o", {}), "videos": []})["videos"].append(s)
    return list(vistos.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--motor", default="/home/claude/.ramas/fondos-v2/escena/escena.html")
    ap.add_argument("--salida")
    a = ap.parse_args()
    it = next(i for i in R.items_del_corpus(["wk2"]))
    zonas = zonas_del_corpus(); res = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}); pg.add_init_script(R.SEMILLA_JS)
        pg.add_init_script(f"window.DATOS={it['datos'].read_text()};")
        pg.goto(pathlib.Path(a.motor).resolve().as_uri()); pg.wait_for_function("window.LISTO===true", timeout=30000); pg.evaluate(JS)
        for zi in zonas:
            z = {"x0": 0, "x1": 1300, "set": zi["set"], "cam": 0}
            if zi["o"]: z["o"] = zi["o"]
            fila = {"set": zi["set"], "o": zi["o"], "videos": sorted(set(zi["videos"]))}
            for perfil in (False, True):
                fila["con_perfil" if perfil else "sin_perfil"] = [pg.evaluate(f"window.__cob({json.dumps(z)},{y0},{y1},{'true' if perfil else 'false'})") for y0, y1 in VENTANAS]
            fila["barrido_con_perfil"] = [pg.evaluate(f"window.__cobS({json.dumps(z)},{s},{dy},true)") for s in ESCALAS for dy in SUBPIXEL]
            res.append(fila)
            sp, cp = fila["sin_perfil"], fila["con_perfil"]
            print(f"{zi['set']:15} {','.join(fila['videos']):22} sin perfil: {sp[0]['n']+sp[1]['n']:7} px sin cubrir (y {sp[1]['y'] if sp[1]['n'] else '—'})"
                  f" · con perfil: {cp[0]['n']+cp[1]['n']:7} px (y {cp[1]['y'] if cp[1]['n'] else '—'})", flush=True)
        b.close()
    if a.salida: json.dump(res, open(a.salida, "w"), ensure_ascii=False, indent=1)
    malos = [r["set"] for r in res if sum(v["n"] for v in r["con_perfil"]) + sum(v["n"] for v in r["barrido_con_perfil"]) > 0]
    for r in res:
        b = [v for v in r["barrido_con_perfil"] if v["n"]]
        if b: print(f"  costura o hueco en {r['set']}: {sum(v['n'] for v in b)} px en {len(b)} de {len(r['barrido_con_perfil'])} encuadres · y {b[0]['y']}")
    print("sets con huecos (con perfil):", malos or "ninguno")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()
