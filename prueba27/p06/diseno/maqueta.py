"""Prueba 27 · plano 06 · MAQUETA de diseño (no es el plano): renderiza encuadres fijos con datos del 05
cambiando solo la cámara y el desplazamiento de la imagen, y superpone el nombre con PIL para ver la composición."""
import json, sys, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont
AQ = pathlib.Path(__file__).parent
base = json.loads(pathlib.Path("/home/claude/prueba27/p05/datos.json").read_text())
K = 900 / 1120; TOP0 = 420 - 50 / K          # 357.8: borde superior visible de la hoja en el 04/05
FONT = ImageFont.truetype("/home/claude/escena/Poppins-Bold.ttf", 113)
def cuadro(nombre, s, X, Yc, D, letras=True):
    d = json.loads(json.dumps(base)); e = d["escenas"][0]
    e["zoom"] = [{"k": -1, "s": s, "dur": .01, "x": 100000 + X, "y": Yc}]
    v = next(p for p in e["props"] if p["tipo"] == "p27_visor")
    gr = next(p for p in e["props"] if p["tipo"] == "p27_grilla")
    # la mano del 04, quieta, con el mouse corrido según el recorrido del cursor del 05 (misma razón ≈0,093 del 04): solo datos
    e["props"].insert(2, {"tipo": "p27_manoPOV", "x": 100000 + 640, "y": 1570, "s": 1.0, "k": -1, "capa": True, "grilla": gr, "mueve": [10, -25]})
    if D: v["despl"] = [-2, -1.5, D]
    f = AQ / f"_d_{nombre}.json"; f.write_text(json.dumps(d))
    subprocess.run(["python3", "/home/claude/prueba27/cuadros.py", "/home/claude/escena/escena.html", str(f), str(AQ / nombre), "3.0"], check=True, stdout=subprocess.DEVNULL)
    im = Image.open(AQ / f"{nombre}_003.00.png").convert("RGB")
    sc = s * 1.03; top = TOP0 - D
    W = lambda sx, sy: (540 + (110 + sx * K - X) * sc, 960 + (240 + (575 + (sy - top) * K - Yc) * s) * 1.03)
    if letras:
        # nombre en la hoja: mayúsculas de 250 a 330, centrado en la franja (x ≈ 578)
        lay = Image.new("RGBA", (1120, 1240), (0, 0, 0, 0)); g = ImageDraw.Draw(lay)
        g.text((578, 331), "THE LEONIDA", font=FONT, fill=(29, 43, 71, 255), anchor="ms")
        x0, y0 = W(0, 0); x1, y1 = W(1120, 1240)
        L = lay.resize((round(x1 - x0), round(y1 - y0)))
        clip = W(0, top)[1]                                  # borde superior de la imagen dentro del visor
        m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rectangle([0, clip, 1080, 1920], fill=255)
        capa = Image.new("RGBA", im.size, (0, 0, 0, 0)); capa.paste(L, (round(x0), round(y0)), L)
        im = Image.composite(Image.alpha_composite(im.convert("RGBA"), capa).convert("RGB"), im, m)
        a, b = W(578 - 364, 250), W(578 + 364, 330)
        print(nombre, f"nombre en pantalla: x {a[0]:.0f}–{b[0]:.0f}, y {a[1]:.0f}–{b[1]:.0f} · borde de la imagen y {clip:.0f}")
    im.save(AQ / f"{nombre}.png"); return im
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        n, s, X, Yc, D = spec.split(","); cuadro(n, float(s), float(X), float(Yc), float(D))
