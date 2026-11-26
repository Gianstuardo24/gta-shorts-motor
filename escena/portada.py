"""Portada vertical 1080x1920 para un Short: un fotograma del video + título grande.
Uso: python3 portada.py video.mp4 segundo "TÍTULO" salida.jpg [color_hex]
El título se escribe en 2-3 líneas grandes, con la palabra clave en el color de acento.
"""
import subprocess, sys, tempfile, os, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))


def portada(video, seg, titulo, salida, acento="#ffd23f", clave_forzada=None):
    tmp = tempfile.mktemp(suffix=".png")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(seg), "-i", video, "-frames:v", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB").resize((1080, 1920))
    os.remove(tmp)
    # degradado oscuro arriba para que el título se lea
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    for y in range(0, 1000):
        a = 255 if y < 640 else int(255 * (1 - (y - 640) / 360) ** 1.4)
        d.line([(0, y), (1080, y)], fill=(8, 6, 20, a))
    im = Image.alpha_composite(im.convert("RGBA"), capa)
    d = ImageDraw.Draw(im)
    limpio = "".join(ch for ch in titulo if ord(ch) < 0x2000).strip()
    palabras = limpio.split()
    tam = 118
    while tam > 70:
        f = ImageFont.truetype(os.path.join(AQUI, "Poppins-Bold.ttf"), tam)
        lineas = textwrap.wrap(limpio.upper(), width=max(8, int(1500 / tam)))
        if len(lineas) <= 3 and all(d.textlength(l, font=f) < 980 for l in lineas):
            break
        tam -= 6
    # palabra clave = la que tenga numero o la mas larga
    num = [p for p in palabras if any(c.isdigit() for c in p) and len(p.strip("$?.!,'")) > 1]
    clave = (clave_forzada or (num[0] if num else max([p for p in palabras if p.upper() != 'GTA'], key=len))).upper().strip("?.!,'")
    y = int(330 - len(lineas) * tam * 0.56)
    for l in lineas:
        x = (1080 - d.textlength(l, font=f)) / 2
        for w in l.split(" "):
            col = acento if clave and clave in w.strip("?.!,'") else "#ffffff"
            # sombra
            for dx, dy in ((6, 6), (0, 6), (6, 0)):
                d.text((x + dx, y + dy), w, font=f, fill=(0, 0, 0, 200))
            d.text((x, y), w, font=f, fill=col)
            x += d.textlength(w + " ", font=f)
        y += int(tam * 1.12)
    im.convert("RGB").save(salida, quality=90)
    return salida


if __name__ == "__main__":
    a = sys.argv
    portada(a[1], float(a[2]), a[3], a[4], a[5] if len(a) > 5 else "#ffd23f", a[6] if len(a) > 6 else None)
    print("✅", a[4])
