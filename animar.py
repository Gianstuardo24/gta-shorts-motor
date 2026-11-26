"""MOTOR DE GRAFICOS ANIMADOS (Python puro, sin Node ni Chrome): secuencias PNG con transparencia a 30 fps
que ffmpeg encima sobre el video. Estilo editorial, sobrio: tipografia grande, pocos colores, movimiento con easing.

Graficos:  contador · lista · timeline · vs · cita · barras
Uso de prueba:  python animar.py prueba   -> _prueba_logo/animar_*.jpg (hoja de cuadros de cada grafico)
Desde subtitular.py: animar.render(tipo, datos, duracion, carpeta, paleta) -> carpeta con 000001.png... (1080x1920 RGBA)
"""
import math, json, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
FPS = 30
FUENTES = ["/System/Library/Fonts/Supplemental/Impact.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
FUENTES_TXT = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
PALETA = {"acento": (255, 60, 172), "acento2": (43, 232, 255), "amarillo": (255, 210, 63), "blanco": (255, 255, 255),
          "negro": (10, 8, 16), "verde": (94, 255, 161), "rojo": (255, 84, 112)}
CY = 720            # centro de la zona de graficos (misma que graficos.py)


def fuente(tam, texto=False):
    for f in (FUENTES_TXT if texto else FUENTES):
        if Path(f).exists():
            return ImageFont.truetype(f, tam)
    return ImageFont.load_default()


# ---------- easing ----------
def out_back(t, s=1.7):
    t -= 1
    return t * t * ((s + 1) * t + s) + 1


def out_cubic(t):
    return 1 - (1 - t) ** 3


def in_out(t):
    return 0.5 - 0.5 * math.cos(math.pi * t)


def clamp(t):
    return max(0.0, min(1.0, t))


def ventana(t, ini, dur):
    """0..1 dentro de [ini, ini+dur]; 0 antes, 1 despues."""
    return clamp((t - ini) / max(dur, 1e-6))


def fade_salida(t, D, dur=0.3):
    return clamp((D - t) / dur)


# ---------- primitivas ----------
def lienzo():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def sombra(img, radio=18, dy=10, alpha=0.5):
    a = img.split()[3].point(lambda x: int(x * alpha))
    s = Image.new("RGBA", img.size, (0, 0, 0, 255))
    s.putalpha(a)
    s = s.filter(ImageFilter.GaussianBlur(radio))
    out = lienzo()
    out.alpha_composite(s, (0, dy))
    out.alpha_composite(img)
    return out


def texto(d, xy, s, f, color, ancla="mm", trazo=0, color_trazo=(0, 0, 0)):
    d.text(xy, s, font=f, fill=color, anchor=ancla, stroke_width=trazo, stroke_fill=color_trazo)


def panel(d, box, radio=36, relleno=(10, 8, 16, 215), borde=None, grosor=4):
    d.rounded_rectangle(box, radio, fill=relleno, outline=borde, width=grosor if borde else 0)


def escalar_centro(img, s, cx, cy):
    """Escala el lienzo completo dejando FIJO el punto (cx, cy): lo que estaba ahi sigue ahi."""
    if s <= 0:
        return None, None
    w, h = max(2, int(img.width * s)), max(2, int(img.height * s))
    return img.resize((w, h), Image.LANCZOS), (int(cx - cx * s), int(cy - cy * s))


# ---------- graficos ----------
def g_contador(t, D, d, P):
    """{"valor": 212, "unidad": "GB", "etiqueta": "ESPACIO NECESARIO", "prefijo": ""}"""
    img = lienzo()
    dr = ImageDraw.Draw(img)
    e = out_back(ventana(t, 0, 0.45))
    a = int(255 * min(ventana(t, 0, 0.2), fade_salida(t, D)))
    capa = lienzo()
    c = ImageDraw.Draw(capa)
    panel(c, (120, CY - 250, 960, CY + 250), 44, (10, 8, 16, 225), P["acento2"] + (255,), 5)
    valor = float(d.get("valor", 0))
    p = out_cubic(ventana(t, 0.1, 1.1))
    v = valor * p
    s_val = (f"{v:,.0f}" if valor >= 10 or float(valor).is_integer() else f"{v:.1f}").replace(",", ".")
    texto(c, (540, CY - 40), f"{d.get('prefijo', '')}{s_val}", fuente(230), P["blanco"], "mm", 6, (0, 0, 0))
    if d.get("unidad"):
        texto(c, (540, CY + 120), str(d["unidad"]).upper(), fuente(80), P["acento2"], "mm")
    if d.get("etiqueta"):
        et = str(d["etiqueta"]).upper()[:24]
        f2 = fuente(40, True)
        wt = f2.getlength(et) + 50
        c.rounded_rectangle((540 - wt / 2, CY + 185, 540 + wt / 2, CY + 240), 28, fill=P["acento"] + (255,))
        texto(c, (540, CY + 212), et, f2, P["blanco"], "mm")
    sc, pos = escalar_centro(capa, 0.6 + 0.4 * e, 540, CY)
    if sc is not None:
        sc.putalpha(sc.split()[3].point(lambda x: x * a // 255))
        img.alpha_composite(sombra(sc), pos)
    return img


def g_barras(t, D, d, P):
    """{"items": [{"etiqueta": "GTA 5", "valor": 110}, ...], "unidad": "GB", "titulo": "..."}"""
    img = lienzo()
    items = (d.get("items") or [])[:5]
    if not items:
        return img
    capa = lienzo()
    c = ImageDraw.Draw(capa)
    panel(c, (90, CY - 330, 990, CY + 330), 44, (10, 8, 16, 225), P["acento"] + (255,), 5)
    if d.get("titulo"):
        texto(c, (540, CY - 270), str(d["titulo"]).upper()[:26], fuente(46, True), P["blanco"], "mm")
    mx = max(float(i.get("valor") or 0) for i in items) or 1
    n = len(items)
    ancho = min(190, 760 // n - 30)
    x0 = 540 - (n * (ancho + 30) - 30) / 2
    base, alto = CY + 220, 380
    for k, it in enumerate(items):
        p = out_cubic(ventana(t, 0.15 + k * 0.18, 0.9))
        h = alto * float(it.get("valor") or 0) / mx * p
        x = x0 + k * (ancho + 30)
        col = P["acento2"] if k != n - 1 else P["acento"]
        c.rounded_rectangle((x, base - h, x + ancho, base), 18, fill=col + (255,))
        val = float(it.get("valor") or 0) * p
        texto(c, (x + ancho / 2, base - h - 34), f"{val:,.0f}".replace(",", "."), fuente(44), P["blanco"], "mm", 3)
        texto(c, (x + ancho / 2, base + 36), str(it.get("etiqueta", ""))[:10].upper(), fuente(30, True), (200, 195, 225), "mm")
    if d.get("unidad"):
        texto(c, (540, CY + 290), str(d["unidad"]).upper(), fuente(30, True), P["acento2"], "mm")
    a = int(255 * min(ventana(t, 0, 0.25), fade_salida(t, D)))
    capa.putalpha(capa.split()[3].point(lambda x: x * a // 255))
    img.alpha_composite(sombra(capa))
    return img


def g_lista(t, D, d, P):
    """{"items": ["212 GB libres", "Precarga desde el 10", ...], "titulo": "..."}  (cada item entra 1 s despues del anterior,
       o en los tiempos de d["tiempos"] si vienen)"""
    img = lienzo()
    items = (d.get("items") or [])[:6]
    if not items:
        return img
    tiempos = d.get("tiempos") or [0.2 + k * max(0.8, (D - 1.5) / max(len(items), 1)) for k in range(len(items))]
    alto_f = 118
    y0 = CY - (len(items) * alto_f) / 2 + 20
    capa = lienzo()
    c = ImageDraw.Draw(capa)
    if d.get("titulo"):
        texto(c, (540, y0 - 70), str(d["titulo"]).upper()[:28], fuente(50), P["blanco"], "mm", 4)
    for k, it in enumerate(items):
        ti = tiempos[k] if k < len(tiempos) else tiempos[-1]
        p = out_back(ventana(t, ti, 0.45), 1.2)
        if p <= 0:
            continue
        hecho = k < len(items) - 1 and t >= (tiempos[k + 1] if k + 1 < len(tiempos) else 1e9)
        y = y0 + k * alto_f
        x = 110 + (1 - p) * 320
        fila = lienzo()
        fd = ImageDraw.Draw(fila)
        col = P["verde"] if hecho else P["acento2"]
        fd.rounded_rectangle((x, y, x + 860, y + 96), 22, fill=(10, 8, 16, 225))
        fd.rounded_rectangle((x, y, x + 14, y + 96), 7, fill=col + (255,))
        texto(fd, (x + 62, y + 48), f"{k + 1}", fuente(64), col, "mm")
        texto(fd, (x + 118, y + 48), str(it)[:30], fuente(42, True), P["blanco"], "lm")
        if hecho:
            texto(fd, (x + 820, y + 48), "✓", fuente(54, True), P["verde"], "mm")
        al = int(255 * min(1, p))
        fila.putalpha(fila.split()[3].point(lambda v: v * al // 255))
        capa.alpha_composite(fila)
    a = int(255 * fade_salida(t, D))
    capa.putalpha(capa.split()[3].point(lambda x: x * a // 255))
    img.alpha_composite(sombra(capa, 12, 8, 0.45))
    return img


def g_timeline(t, D, d, P):
    """{"eventos": [{"fecha": "AUG 6", "texto": "Minneapolis center goes dark"}, ...]}"""
    img = lienzo()
    ev = (d.get("eventos") or [])[:4]
    if not ev:
        return img
    capa = lienzo()
    c = ImageDraw.Draw(capa)
    x_l = 150
    y0, y1 = CY - 300, CY + 300
    c.rounded_rectangle((x_l - 5, y0, x_l + 5, y1), 5, fill=(255, 255, 255, 50))
    prog = out_cubic(ventana(t, 0.2, D - 0.8))
    c.rounded_rectangle((x_l - 5, y0, x_l + 5, y0 + (y1 - y0) * prog), 5, fill=P["amarillo"] + (255,))
    n = len(ev)
    for k, e in enumerate(ev):
        ye = y0 + (y1 - y0) * (k + 0.5) / n
        ti = 0.2 + (D - 0.8) * ((k + 0.3) / n)
        p = out_back(ventana(t, ti, 0.4), 1.4)
        if p <= 0:
            continue
        fila = lienzo()
        fd = ImageDraw.Draw(fila)
        r = 16 * p
        fd.ellipse((x_l - r, ye - r, x_l + r, ye + r), fill=P["amarillo"] + (255,), outline=(0, 0, 0, 255), width=4)
        x = x_l + 50 + (1 - p) * 60
        fd.rounded_rectangle((x, ye - 60, 980, ye + 60), 22, fill=(10, 8, 16, 225))
        texto(fd, (x + 26, ye - 24), str(e.get("fecha", "")).upper(), fuente(50), P["amarillo"], "lm")
        texto(fd, (x + 26, ye + 30), str(e.get("texto", ""))[:34], fuente(32, True), P["blanco"], "lm")
        al = int(255 * min(1, p))
        fila.putalpha(fila.split()[3].point(lambda v: v * al // 255))
        capa.alpha_composite(fila)
    a = int(255 * min(ventana(t, 0, 0.2), fade_salida(t, D)))
    capa.putalpha(capa.split()[3].point(lambda x: x * a // 255))
    img.alpha_composite(sombra(capa, 12, 8, 0.45))
    return img


def g_vs(t, D, d, P):
    """{"a": "PS5", "va": 30, "b": "PS5 PRO", "vb": 30, "unidad": "FPS", "nota": "MISMA CPU"}"""
    img = lienzo()
    capa = lienzo()
    c = ImageDraw.Draw(capa)
    top, bot = CY - 300, CY + 300
    e = out_cubic(ventana(t, 0, 0.35))
    mitad = 540
    c.rounded_rectangle((100, top, mitad - 6, bot), 40, fill=(43, 134, 197, 230))
    c.rounded_rectangle((mitad + 6, top, 980, bot), 40, fill=(255, 84, 112, 230))
    for k, (nom, val, cx) in enumerate(((d.get("a"), d.get("va"), 320), (d.get("b"), d.get("vb"), 760))):
        texto(c, (cx, top + 80), str(nom or "").upper()[:12], fuente(54), P["blanco"], "mm", 3)
        p = out_cubic(ventana(t, 0.4 + k * 0.3, 1.0))
        try:
            v = float(val)
            s_v = f"{v * p:,.0f}".replace(",", ".")
        except (TypeError, ValueError):
            s_v = str(val or "")
        texto(c, (cx, CY + 10), s_v, fuente(150), P["blanco"], "mm", 5)
        if d.get("unidad"):
            texto(c, (cx, CY + 130), str(d["unidad"]).upper(), fuente(40, True), (255, 255, 255, 220), "mm")
    s = out_back(ventana(t, 0.25, 0.4))
    r = 62 * s
    if r > 0:
        c.ellipse((mitad - r, CY - r, mitad + r, CY + r), fill=P["amarillo"] + (255,), outline=(0, 0, 0, 255), width=6)
        texto(c, (mitad, CY + 2), "VS", fuente(int(52 * s) + 1), (0, 0, 0), "mm")
    if d.get("nota"):
        texto(c, (540, bot - 50), str(d["nota"]).upper()[:28], fuente(34, True), P["blanco"], "mm", 2)
    a = int(255 * min(e, fade_salida(t, D)))
    sc, pos = escalar_centro(capa, 0.92 + 0.08 * e, 540, CY)
    sc.putalpha(sc.split()[3].point(lambda x: x * a // 255))
    img.alpha_composite(sombra(sc), pos)
    return img


def g_cita(t, D, d, P):
    """{"texto": "...", "autor": "...", "destacar": "palabras", "badge": "OFICIAL"}"""
    img = lienzo()
    capa = lienzo()
    c = ImageDraw.Draw(capa)
    f = fuente(46, True)
    palabras = str(d.get("texto", "")).split()
    lineas, act = [], ""
    for p_ in palabras:
        if f.getlength((act + " " + p_).strip()) <= 760:
            act = (act + " " + p_).strip()
        else:
            lineas.append(act)
            act = p_
    lineas = (lineas + [act])[:4]
    alto = 90 + len(lineas) * 58 + (60 if d.get("autor") else 0)
    box = (110, CY - alto / 2, 970, CY + alto / 2)
    c.rounded_rectangle(box, 30, fill=(250, 248, 255, 255))
    texto(c, (150, box[1] + 10), "“", fuente(150), P["acento"], "lt")
    dest = {w.lower().strip(".,") for w in str(d.get("destacar", "")).split()}
    y = box[1] + 60
    for l in lineas:
        x = 150
        for w in l.split(" "):
            ww = f.getlength(w + " ")
            if w.lower().strip(".,") in dest:
                c.rounded_rectangle((x - 4, y - 4, x + ww - 8, y + 50), 8, fill=P["amarillo"] + (255,))
            texto(c, (x, y), w, f, (20, 16, 30), "la")
            x += ww
        y += 58
    if d.get("autor"):
        texto(c, (150, y + 14), f"— {d['autor']}"[:50].upper(), fuente(26, True), (110, 100, 140), "la")
    if d.get("badge"):
        b = str(d["badge"]).upper()[:12]
        fb = fuente(26, True)
        wb = fb.getlength(b) + 40
        c.rounded_rectangle((box[2] - wb - 10, box[1] - 22, box[2] + 10, box[1] + 22), 22, fill=P["verde"] + (255,))
        texto(c, (box[2] - wb / 2, box[1]), b, fb, (0, 0, 0), "mm")
    e = out_back(ventana(t, 0, 0.5), 1.3)
    a = int(255 * min(ventana(t, 0, 0.25), fade_salida(t, D)))
    rot = capa.rotate(-2 + 6 * (1 - e), resample=Image.BICUBIC, center=(540, CY))
    rot.putalpha(rot.split()[3].point(lambda x: x * a // 255))
    dy = int((1 - e) * 60)
    img.alpha_composite(sombra(rot, 22, 14, 0.55), (0, dy))
    return img


GRAFICOS = {"contador": g_contador, "barras": g_barras, "lista": g_lista, "timeline": g_timeline, "vs": g_vs, "cita": g_cita}


def render(tipo, datos, duracion, carpeta, paleta=None):
    """Secuencia PNG RGBA (1080x1920, 30 fps) en `carpeta`. Devuelve la carpeta o None."""
    fn = GRAFICOS.get(tipo)
    if not fn:
        return None
    P = {**PALETA, **(paleta or {})}
    carpeta = Path(carpeta)
    shutil.rmtree(carpeta, ignore_errors=True)
    carpeta.mkdir(parents=True, exist_ok=True)
    n = max(2, int(round(duracion * FPS)))
    for k in range(n):
        fn(k / FPS, duracion, datos, P).save(carpeta / f"{k + 1:06d}.png", compress_level=1)
    return carpeta


def hoja(tipo, datos, D=3.0, salida=None, cols=6):
    """Hoja de cuadros para ver la animacion de un vistazo (prueba)."""
    ts = [D * k / (cols - 1) * 0.98 for k in range(cols)]
    fondo = Image.new("RGB", (cols * 270, 480), (40, 36, 60))
    for k, t in enumerate(ts):
        fr = GRAFICOS[tipo](t, D, datos, PALETA)
        base = Image.new("RGBA", (W, H), (60, 50, 90, 255))
        base.alpha_composite(fr)
        fondo.paste(base.convert("RGB").resize((270, 480)), (k * 270, 0))
    if salida:
        fondo.save(salida, quality=88)
    return fondo


if __name__ == "__main__":
    import sys
    if "prueba" in sys.argv:
        Path("_prueba_logo").mkdir(exist_ok=True)
        hoja("contador", {"valor": 212, "unidad": "GB", "etiqueta": "espacio necesario"}, 3, "_prueba_logo/animar_contador.jpg")
        hoja("barras", {"items": [{"etiqueta": "GTA 5", "valor": 110}, {"etiqueta": "RDR2", "valor": 160}, {"etiqueta": "GTA 6", "valor": 212}], "unidad": "GB", "titulo": "cuánto pesa"}, 3, "_prueba_logo/animar_barras.jpg")
        hoja("lista", {"titulo": "antes del 19", "items": ["212 GB libres", "Precarga desde el 10", "Sale el 19 de noviembre", "Solo consolas"]}, 4, "_prueba_logo/animar_lista.jpg")
        hoja("timeline", {"eventos": [{"fecha": "AUG 6", "texto": "Minneapolis center goes dark"}, {"fecha": "SEP 21", "texto": "Newark: 8 h without arrivals"}, {"fecha": "NOV 13", "texto": "The whole country stops"}]}, 4, "_prueba_logo/animar_timeline.jpg")
        hoja("vs", {"a": "PS5", "va": 30, "b": "PS5 PRO", "vb": 30, "unidad": "fps", "nota": "misma cpu"}, 3, "_prueba_logo/animar_vs.jpg")
        hoja("cita", {"texto": "Leonida is the biggest world we've ever built", "autor": "Aaron Garbut, Rockstar North", "destacar": "biggest world", "badge": "oficial"}, 3, "_prueba_logo/animar_cita.jpg")
        print("ok")
