"""Miniatura 16:9 (1280x720) para videos LARGOS de MDM: fondo de ChatGPT + texto grande + logo del canal.

Uso:
  python3 miniatura_largo.py fondo.png salida.jpg "LINEA 1|LINEA 2" [opciones]
    --destacar N      linea que va en amarillo (0, 1...; por defecto la ultima)
    --lado izq|der    lado del texto (por defecto izq)
    --cx 0.5          centro horizontal del recorte (0 = izquierda, 1 = derecha)
    --cy 0.5          centro vertical del recorte
    --logo ruta       logo del canal (por defecto assets/logo_mdm.png)
"""
import sys, argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H = 1280, 720
FUENTE = next((f for f in ["/home/claude/fuentes/Anton-Regular.ttf", "assets/fuentes/Anton-Regular.ttf",
                            "/System/Library/Fonts/Supplemental/Impact.ttf"] if Path(f).exists()), None)
ANCHO = 600
AMARILLO = (255, 199, 51)
BLANCO = (255, 255, 255)
VERDE = (46, 125, 50)


def recorte(im, cx, cy, zoom=1.0):
    r = max(W / im.width, H / im.height) * zoom
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x0 = int((im.width - W) * cx)
    y0 = int((im.height - H) * cy)
    return im.crop((x0, y0, x0 + W, y0 + H))


def realzar(im):
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(1.15)
    return ImageEnhance.Sharpness(im).enhance(1.25)


def degradado(lado):
    """Oscurece el lado del texto para que se lea siempre."""
    g = Image.new("L", (W, 1))
    for x in range(W):
        u = x / W if lado == "izq" else 1 - x / W
        g.putpixel((x, 0), int(205 * max(0.0, 1 - u / 0.62) ** 1.4))
    return g.resize((W, H))


def texto(img, lineas, destacar, lado):
    d = ImageDraw.Draw(img)
    ancho_max = ANCHO
    tams = []
    for i, l in enumerate(lineas):                       # cada linea al maximo que entra (la destacada mas grande)
        tope = 230 if i == destacar else 150
        t = tope
        while t > 40 and ImageFont.truetype(FUENTE, t).getlength(l) > ancho_max:
            t -= 4
        tams.append(t)
    alto = sum(int(t * 1.02) for t in tams)
    y = (H - alto) // 2 + 30
    x0 = 70 if lado == "izq" else W - 70
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))       # sombra blanda debajo del texto
    dc = ImageDraw.Draw(capa)
    yy = y
    for l, t in zip(lineas, tams):
        f = ImageFont.truetype(FUENTE, t)
        x = x0 if lado == "izq" else x0 - f.getlength(l)
        dc.text((x + 8, yy + 10), l, font=f, fill=(0, 0, 0, 200))
        yy += int(t * 1.02)
    img.alpha_composite(capa.filter(ImageFilter.GaussianBlur(10)))
    for i, (l, t) in enumerate(zip(lineas, tams)):
        f = ImageFont.truetype(FUENTE, t)
        x = x0 if lado == "izq" else x0 - f.getlength(l)
        col = AMARILLO if i == destacar else BLANCO
        d.text((x, y), l, font=f, fill=col, stroke_width=max(6, t // 22), stroke_fill=(0, 0, 0))
        y += int(t * 1.02)


def rotulo(img, txt, x, y, tam, color="amar"):
    f = ImageFont.truetype(FUENTE, int(tam))
    x = float(x) - f.getlength(txt) / 2
    y = float(y)
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(capa).text((x + 6, y + 8), txt, font=f, fill=(0, 0, 0, 210))
    img.alpha_composite(capa.filter(ImageFilter.GaussianBlur(8)))
    col = AMARILLO if color.startswith("amar") else BLANCO
    ImageDraw.Draw(img).text((x, y), txt, font=f, fill=col, stroke_width=max(5, int(tam) // 20), stroke_fill=(0, 0, 0))


def logo(img, ruta, lado):
    l = Image.open(ruta).convert("RGBA")
    l.thumbnail((112, 112), Image.LANCZOS)
    x = 34 if lado == "izq" else W - l.width - 34
    sombra = Image.new("RGBA", img.size, (0, 0, 0, 0))
    m = l.split()[3].point(lambda a: int(a * 0.7))
    sombra.paste((0, 0, 0, 255), (x + 4, 30 + 6), m)
    img.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(6)))
    img.alpha_composite(l, (x, 30))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("fondo"); a.add_argument("salida"); a.add_argument("texto")
    a.add_argument("--destacar", type=int, default=-1)
    a.add_argument("--lado", default="izq")
    a.add_argument("--cx", type=float, default=0.5)
    a.add_argument("--cy", type=float, default=0.5)
    a.add_argument("--zoom", type=float, default=1.0)
    a.add_argument("--ancho", type=int, default=600)
    a.add_argument("--sin-degradado", action="store_true")
    a.add_argument("--logo", default=next((f for f in ["assets/logo_mdm.png", "/mnt/user-data/uploads/gta-shorts/assets/logo_mdm.png"] if Path(f).exists()), ""))
    a.add_argument("--rotulo", action="append", default=[],
                   help='etiqueta sobre un objeto: "TEXTO;x_centro;y_arriba;tam;amar|blanco"')
    o = a.parse_args()
    global ANCHO
    ANCHO = o.ancho
    lineas = [s.strip().upper() for s in o.texto.split("|") if s.strip()]
    dest = o.destacar if o.destacar >= 0 else len(lineas) - 1
    img = realzar(recorte(Image.open(o.fondo).convert("RGB"), o.cx, o.cy, o.zoom)).convert("RGBA")
    negro = Image.new("RGBA", (W, H), (4, 10, 6, 255))
    if not o.sin_degradado:
        img = Image.composite(negro, img, degradado(o.lado))
    if lineas:
        texto(img, lineas, dest, o.lado)
    for r in o.rotulo:
        rotulo(img, *r.split(";"))
    if Path(o.logo).exists():
        logo(img, o.logo, o.lado)
    img.convert("RGB").save(o.salida, quality=93)
    print("ok", o.salida)


if __name__ == "__main__":
    main()
