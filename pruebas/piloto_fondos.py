#!/usr/bin/env python3
"""Piloto técnico del 27i (bloque 1): wk2 con el perfil de fondos, en la rama fondos-v2.
Solo pruebas: no toca producción, el corpus congelado ni la E0. Los cuadros quedan en /tmp/fv2; los informes, en
pruebas/informes/fondos/.

Pasos:
  datos      arma los datos del piloto (wk2 con la corrección 27g + perfil del canal + campos por plano) y la variante C
  render     dibuja todos los cuadros del piloto con el motor de la rama (semilla de prueba) y arma el video con el audio entregado
  medir      cuadro a cuadro: huecos (dos colores testigo), fondo base pintado, plano en pantalla y primer cuadro
  hoja       antes (producción) y después (piloto) en los momentos clave
  sintetico  variante C (todas las opciones): cuadros alrededor de cada transición y medición
"""
import argparse, base64, copy, hashlib, json, pathlib, subprocess, sys
RAMA = pathlib.Path(__file__).resolve().parent.parent
VIVO = pathlib.Path("/home/claude")
sys.path.insert(0, str(VIVO / "pruebas")); import regresion as R

MOTOR = {"antes": VIVO / "escena" / "escena.html", "despues": RAMA / "escena" / "escena.html"}
DATOS_27G = pathlib.Path("/tmp/prueba_corte/wk2/despues/datos_render.json")      # datos de wk2 con la corrección 27g (planificador de la rama 27g)
INF = RAMA / "pruebas" / "informes" / "fondos"
TMP = pathlib.Path("/tmp/fv2/piloto")
SLOT = "wk2"
# perfil de fondos del canal (27i § 2.1): iguales en los 7 canales salvo el fondo base
PERFIL = {"version": 1, "base": "mascotas", "inicio": "escena", "cierre": "base", "escenas": "solo_si_la_piden",
          "transicion": "corte", "cobertura": "completa"}
SEMILLA = "window.__semilla=v=>{let s=v>>>0;Math.random=()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}};true;"
MEDIR_JS = """(()=>{const cr=X.clearRect.bind(X);window.__testigo=null;
X.clearRect=function(x,y,w,h){cr(x,y,w,h);if(window.__testigo){const f=this.fillStyle;this.fillStyle=window.__testigo;this.fillRect(x,y,w,h);this.fillStyle=f}};
const pb=pintarBase;window.__nb=0;pintarBase=function(){window.__nb++;return pb.apply(this,arguments)};
const zd=zonaDeco;window.__Z=[];zonaDeco=function(z,t,q){if(z&&z.set&&q>0){const inv=X.getTransform().inverse();const a=inv.transformPoint(new DOMPoint(0,0)),b=inv.transformPoint(new DOMPoint(W,H));
  if(z.x1>a.x&&z.x0<b.x)window.__Z.push([z.set,z.x0,+q.toFixed(3),Math.round(b.y)])}return zd(z,t,q)};
window.__cuadro=function(t,n){const L=[];let huecos=0,nb=0,Z=null;
  for(const col of ['#ff00ff','#00ff00']){window.__semilla(12345+n);window.__testigo=col;window.__nb=0;window.__Z=[];render(t);
    L.push(X.getImageData(0,0,W,H).data);nb=Math.max(nb,window.__nb);if(!Z)Z=window.__Z.slice()}
  window.__testigo=null;const A=L[0],B=L[1];let ymin=1e9,ymax=-1;
  for(let y=0;y<H;y+=2)for(let x=0;x<W;x+=2){const i=(y*W+x)*4;if(A[i]!==B[i]||A[i+1]!==B[i+1]||A[i+2]!==B[i+2]){huecos++;if(y<ymin)ymin=y;if(y>ymax)ymax=y}}
  return {n,h:huecos,pct:+(100*huecos*4/(W*H)).toFixed(3),y:huecos?[ymin,ymax]:null,base:nb,Z}};
return true})()"""


def item():
    return next(it for it in R.items_del_corpus([SLOT]))


def con_perfil(d):
    d = copy.deepcopy(d); d["fondos"] = dict(PERFIL)
    e = next(s for s in d["escenas"] if s["tipo"] == "pelicula")
    for i, z in enumerate(e["zonas"]):            # campos por plano (los escribirá el constructor en el bloque 3)
        z.setdefault("entorno", "vitrina" if z["set"] == "vitrinaV" else z["set"])
        z.setdefault("transicion", "inicio" if i == 0 else "corte")
    return d


def variante_c(d):
    """Caso C: todas las opciones en un mismo video (sobre el piloto)."""
    d = copy.deepcopy(d); e = next(s for s in d["escenas"] if s["tipo"] == "pelicula")
    zs = [z for z in e["zonas"] if z["set"] != "vitrinaV"]          # escenarios, en orden: café de gatos, parque, montaña, sala, cocina, dormitorio, sala
    assert [z["set"] for z in zs] == ["cafeGatosV", "parqueV", "montanaV", "salaV", "cocinaV", "dormitorioV", "salaV"], [z["set"] for z in zs]
    def pan_de(z):
        return [p for p in e["pan"] if p.get("x") == z["x0"] and p.get("corte")]
    mon, sala, coc, dor, sala2 = zs[2], zs[3], zs[4], zs[5], zs[6]
    for p in pan_de(mon): p.pop("corte", None); p["dur"] = 1.0       # montaña: paneo desde el parque (la cámara viaja, sin corte)
    mon["transicion"] = "paneo"
    sala.update(transicion="fundido", previa=mon["x0"], dur_fundido=0.5)   # sala: fundido desde la montaña
    coc["transicion"] = "negro"                                        # cocina: pasa por negro, sin líneas de velocidad
    for p in pan_de(coc): p["efecto"] = "ninguno"
    dor.update(set="baseCanal", entorno="base")                        # dormitorio: el plano pide el fondo base del canal
    sala2.update(camara="fija", acabado="ninguno")                     # segunda sala: cámara fija y sin acabado
    return d


def paso_datos():
    INF.mkdir(parents=True, exist_ok=True); TMP.mkdir(parents=True, exist_ok=True)
    d = json.loads(DATOS_27G.read_text())
    (INF / "wk2_datos_27g_origen.json").write_text(json.dumps(d, ensure_ascii=False))
    p = con_perfil(d); c = variante_c(p)
    (INF / "wk2_piloto_datos.json").write_text(json.dumps(p, ensure_ascii=False))
    (INF / "wk2_variante_c_datos.json").write_text(json.dumps(c, ensure_ascii=False))
    e = next(s for s in p["escenas"] if s["tipo"] == "pelicula")
    print("planos del piloto:", [(z["set"], z["x0"], z.get("k"), z["transicion"]) for z in e["zonas"]])


def abrir(p, motor, datos):
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920}); pg.add_init_script(R.SEMILLA_JS)
    pg.add_init_script(f"window.DATOS={pathlib.Path(datos).read_text()};")
    pg.goto(pathlib.Path(motor).resolve().as_uri()); pg.wait_for_function("window.LISTO===true", timeout=30000)
    pg.evaluate(SEMILLA)
    return b, pg


def dibujar(motor, datos, ns, carpeta, fmt="jpg"):
    from playwright.sync_api import sync_playwright
    r = item()["render"]; carpeta = pathlib.Path(carpeta); carpeta.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b, pg = abrir(p, motor, datos)
        tipo = '"image/jpeg",0.92' if fmt == "jpg" else '"image/png"'
        for n in ns:
            t = round(r["t0"] + n / r["fps"], 6)
            url = pg.evaluate(f"(()=>{{window.__semilla({12345 + n});render({t});return document.getElementById('c').toDataURL({tipo})}})()")
            (carpeta / f"{n:05d}.{fmt}").write_bytes(base64.b64decode(url.split(",", 1)[1]))
        b.close()


def paso_render():
    it = item(); r = it["render"]
    C = TMP / "cuadros"; dibujar(MOTOR["despues"], INF / "wk2_piloto_datos.json", range(r["cuadros"]), C)
    ref = VIVO / "pruebas" / it["video"]["archivo"]
    out = TMP / "wk2_piloto_27i.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(r["fps"]), "-i", str(C / "%05d.jpg"), "-i", str(ref),
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "copy", str(out)], check=True)
    print("video del piloto:", out)


def medir(datos, ns, salida):
    from playwright.sync_api import sync_playwright
    r = item()["render"]; res = []
    with sync_playwright() as p:
        b, pg = abrir(p, MOTOR["despues"], datos); pg.evaluate(MEDIR_JS)
        for n in ns:
            res.append(pg.evaluate(f"window.__cuadro({round(r['t0'] + n / r['fps'], 6)},{n})"))
        b.close()
    d = json.loads(pathlib.Path(datos).read_text()); s_fin = d["T"]["s_fin"]
    n_cierre = int((s_fin - 0.25) * r["fps"])
    resumen = {"cuadros": len(res), "con_huecos": [x["n"] for x in res if x["h"] > 0],
               "fondo_base_antes_del_cierre": [x["n"] for x in res if x["base"] and x["n"] < n_cierre],
               "fondo_base_en_el_cierre": sum(1 for x in res if x["base"] and x["n"] >= n_cierre),
               "primer_cuadro": next((x for x in res if x["n"] == 0), None), "n_cierre": n_cierre}
    json.dump({"resumen": resumen, "cuadros": res}, open(salida, "w"), ensure_ascii=False)
    return resumen


def paso_medir():
    r = item()["render"]
    res = medir(INF / "wk2_piloto_datos.json", range(r["cuadros"]), INF / "wk2_piloto_medicion.json")
    print(json.dumps({k: (v if not isinstance(v, list) or len(v) < 40 else f"{len(v)} cuadros") for k, v in res.items()}, ensure_ascii=False))


MOMENTOS = [("Inicio · cuadro 0", 0), ("Inicio · 0,10 s", 3), ("Inicio · 0,33 s", 10), ("Corte al parque · 8,10 s", 243), ("Corte al parque · +2", 245),
            ("Encuadre en el parque · 10,0 s", 300), ("Corte a la montaña · 12,83 s", 385), ("Encuadre en la montaña · 13,4 s", 402),
            ("Corte a la cocina · 24,17 s", 725), ("Entrada al cierre", None)]


def paso_hoja():
    from PIL import Image, ImageDraw, ImageFont
    it = item(); r = it["render"]; fps = r["fps"]
    s_fin = json.loads((INF / "wk2_piloto_datos.json").read_text())["T"]["s_fin"]
    mom = [(t, n if n is not None else int((s_fin + .2) * fps)) for t, n in MOMENTOS]
    A, B = TMP / "hoja_antes", TMP / "hoja_despues"
    dibujar(MOTOR["antes"], it["datos"], [n for _, n in mom], A, "png")
    dibujar(MOTOR["despues"], INF / "wk2_piloto_datos.json", [n for _, n in mom], B, "png")
    try:
        F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24); f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        F = f2 = ImageFont.load_default()
    w, h = 270, 480; cols = len(mom)
    hoja = Image.new("RGB", (70 + cols * (w + 8), 2 * (h + 40) + 50), (16, 16, 20)); d = ImageDraw.Draw(hoja)
    d.text((10, 10), "wk2 · The Cats Decoder · arriba: producción (25-nov) · abajo: piloto 27i (perfil de fondos)", fill=(235, 235, 235), font=F)
    for fila, (lado, carp) in enumerate((("ANTES", A), ("PILOTO", B))):
        y = 50 + fila * (h + 40)
        d.text((8, y + h // 2), lado[0], fill=(235, 235, 235), font=F)
        for j, (txt, n) in enumerate(mom):
            x = 70 + j * (w + 8)
            hoja.paste(Image.open(carp / f"{n:05d}.png").convert("RGB").resize((w, h)), (x, y))
            d.text((x, y + h + 6), txt.replace("·", "·")[:26], fill=(210, 210, 210), font=f2)
    out = INF / "wk2_piloto_antes_despues.png"; hoja.save(out); print("hoja:", out)


def paso_sintetico():
    d = json.loads((INF / "wk2_variante_c_datos.json").read_text()); r = item()["render"]; fps = r["fps"]
    e = next(s for s in d["escenas"] if s["tipo"] == "pelicula"); T = d["T"]
    import re
    def tk(k):
        if isinstance(k, (int, float)): return k
        m = re.match(r"^(\w+?)([+-][\d.]+)?$", k); return T[m.group(1)] + (float(m.group(2)) if m.group(2) else 0)
    ks = sorted({round(tk(z["k"]) * fps) for z in e["zonas"] if z.get("k") is not None}) + [int(T["s_fin"] * fps)]
    ns = sorted({n for k in ks for n in range(k - 9, k + 16) if 0 <= n < r["cuadros"]} | set(range(0, 4)))
    res = medir(INF / "wk2_variante_c_datos.json", ns, INF / "wk2_variante_c_medicion.json")
    print(json.dumps({k: (v if not isinstance(v, list) or len(v) < 40 else f"{len(v)} cuadros") for k, v in res.items()}, ensure_ascii=False))
    dibujar(MOTOR["despues"], INF / "wk2_variante_c_datos.json", ns, TMP / "variante_c", "png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("paso", choices=["datos", "render", "medir", "hoja", "sintetico"])
    a = ap.parse_args()
    {"datos": paso_datos, "render": paso_render, "medir": paso_medir, "hoja": paso_hoja, "sintetico": paso_sintetico}[a.paso]()
