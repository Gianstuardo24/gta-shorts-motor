"""MINIATURAS (portadas 1080x1920) para cada Short pendiente: llamativas, de buena calidad y del tema.

- Fondo: la mejor imagen oficial/legal del tema (GTA: kit de prensa de Rockstar; Rabbit: su stock legal), con mas
  contraste, color y vineta.
- Texto grande de 2 a 4 palabras (lo escribe Claude a partir del titulo) con una palabra destacada.
- Un sticker que calce con el tema + el logo del canal. Todo dentro de la zona segura del centro.
Se guarda junto al video:  "<video>.portada.jpg"   (Instagram: portada del Reel · YouTube: cuando el canal pueda subirla)

Uso:  python miniaturas.py                 portadas de todos los Shorts pendientes que no tengan
      python miniaturas.py --todo          rehace todas
      python miniaturas.py --en-video      ademas mete la portada en los 2 primeros cuadros del video
                                           (para elegirla en el selector de cuadros de YouTube)
"""
import os, re, sys, json, math, random, hashlib, subprocess, tempfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

RAIZ = Path(os.environ.get("YT_RAIZ", "~/Desktop/YouTube")).expanduser()
CANALES = {"ViceVersoGG": "es", "TheViceVerseGG": "en", "TheRabbitLoop": "rabbit"}
W, H = 1080, 1920
FUENTES = ["/System/Library/Fonts/Supplemental/Impact.ttf", "/System/Library/Fonts/Supplemental/Arial Black.ttf",
           "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
ACENTO = {"es": (255, 214, 10), "en": (255, 214, 10), "rabbit": (255, 120, 20)}
ACENTO2 = {"es": (255, 60, 172), "en": (43, 232, 255), "rabbit": (245, 234, 213)}

PROMPT = """Eres disenador de miniaturas virales de YouTube Shorts (canal: __NICHO__, idioma: __IDIOMA__).
Para cada video te paso su titulo. Devuelve para cada uno:
- "texto": 2 a 4 palabras EN MAYUSCULAS, en __IDIOMA__, que generen curiosidad y se lean en 1 segundo.
  Debe decir de que trata (nombra la cosa concreta) y NO mentir ni prometer lo que el video no tiene.
- "destacar": UNA palabra de "texto" que va en color (la mas fuerte).
- "foto": el tema de la imagen de fondo, elegido SOLO de esta lista: __FOTOS__
- "sticker": un objeto de esta lista que calce con el tema (o "" si ninguno): __STICKERS__
Responde SOLO un array JSON, un objeto por video y en el mismo orden:
[{"texto": "...", "destacar": "...", "foto": "...", "sticker": "..."}]"""


def perfil_cfg(perfil):
    d = json.loads(Path("config.json").read_text())
    if perfil != "es":
        d.update(json.loads(Path("canales", f"{perfil}.json").read_text()))
    return d


def fuente(tam):
    for f in FUENTES:
        if Path(f).exists():
            return ImageFont.truetype(f, tam)
    return ImageFont.load_default()


def fotos_de(cfg):
    carpeta = Path(cfg.get("fotos_estimulos", "tomas/imagenes"))
    fs = [f for f in carpeta.rglob("*") if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")]
    fs = [f for f in fs if "ULTIMATE" not in f.stem.upper() and "VINTAGE" not in f.stem.upper()]
    capturas = [f for f in fs if "screenshot" in str(f).lower()]
    return capturas or fs


def sujeto(f):
    return re.sub(r"_(\d+|[0-9a-f]{6})$", "", f.stem).replace("_", " ")


def stickers_de(cfg):
    try:
        reg = json.loads(Path("assets/stickers/stickers.json").read_text()).get(cfg.get("stickers", "gta"), {})
    except Exception:
        return {}
    return {n: Path("assets/stickers") / r for n, r in reg.items() if (Path("assets/stickers") / r).exists()}


def titulo_de(v):
    t = v.with_suffix(".txt")
    if t.exists():
        m = re.search(r"T[IÍ]TULO:\n(.*)", t.read_text(encoding="utf-8"))
        if m:
            return m.group(1).strip()
    return v.stem.split(" - ", 1)[-1]


def pendientes(canal, todo):
    hoy = datetime.now(ZoneInfo("America/Santiago")).date().isoformat()
    out = []
    for d in sorted(canal.iterdir()):
        if not d.is_dir():
            continue
        if (re.match(r"\d{4}-\d{2}-\d{2} ", d.name) and d.name[:10] >= hoy) or d.name.startswith("Nuevos"):
            for v in sorted(d.glob("*.mp4")):
                if todo or not v.with_name(v.stem + ".portada.jpg").exists():
                    out.append(v)
    return out


def pedir_textos(videos, cfg, perfil, fotos, stickers):
    idioma = "espanol" if perfil == "es" else "ingles"
    sujetos = sorted({sujeto(f) for f in fotos})
    pr = (PROMPT.replace("__NICHO__", cfg.get("nicho", "GTA 6")).replace("__IDIOMA__", idioma)
          .replace("__FOTOS__", ", ".join(sujetos[:150])).replace("__STICKERS__", ", ".join(stickers) or "(ninguno)"))
    entrada = "\n".join(f"{i}. {titulo_de(v)}" for i, v in enumerate(videos, 1))
    r = subprocess.run(["claude", "-p", pr], input=entrada, capture_output=True, text=True, timeout=600)
    from utilidades import extraer_json
    try:
        return extraer_json(r.stdout)
    except ValueError:
        print("⚠️ Claude no devolvio los textos; uso el titulo")
        return [{} for _ in videos]


def elegir_foto(tema, fotos, semilla):
    pal = {w for w in re.findall(r"[a-z]+", (tema or "").lower()) if len(w) > 2}
    punt = sorted(((len(pal & set(re.findall(r"[a-z]+", sujeto(f).lower()))), f) for f in fotos), key=lambda x: -x[0])
    mejores = [f for n, f in punt if n == punt[0][0]] if punt else []
    return random.Random(semilla).choice(mejores or fotos) if fotos else None


def fondo(foto, rnd):
    im = Image.open(foto).convert("RGB")
    z = rnd.uniform(1.0, 1.12)                                   # leve zoom distinto en cada portada
    r = max(W / im.width, H / im.height) * z
    im = im.resize((math.ceil(im.width * r), math.ceil(im.height * r)), Image.LANCZOS)
    x0 = int((im.width - W) * rnd.uniform(0.3, 0.7))
    y0 = (im.height - H) // 2
    im = im.crop((x0, y0, x0 + W, y0 + H))
    im = ImageEnhance.Contrast(im).enhance(1.18)
    im = ImageEnhance.Color(im).enhance(1.3)
    im = ImageEnhance.Sharpness(im).enhance(1.3)
    vin = Image.new("L", (W, H), 0)                              # vineta: bordes mas oscuros
    ImageDraw.Draw(vin).ellipse([-W * 0.25, -H * 0.1, W * 1.25, H * 1.1], fill=255)
    vin = vin.filter(ImageFilter.GaussianBlur(160))
    oscuro = Image.new("RGB", (W, H), (0, 0, 0))
    return Image.composite(im, Image.blend(im, oscuro, 0.65), vin)


def lineas_de(texto, f, ancho):
    pal, lineas, actual = texto.split(), [], ""
    for p in pal:
        prueba = (actual + " " + p).strip()
        if f.getlength(prueba) <= ancho or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    return lineas + ([actual] if actual else [])


def texto_grande(img, texto, destacar, perfil, y_centro):
    d = ImageDraw.Draw(img)
    texto = re.sub(r"\s+", " ", texto.upper()).strip()
    for tam in range(190, 80, -6):                               # el mas grande que entre en 2-3 lineas
        f = fuente(tam)
        ls = lineas_de(texto, f, 920)
        if len(ls) <= 3 and all(f.getlength(l) <= 920 for l in ls):
            break
    alto = int(tam * 1.05)
    y = y_centro - alto * len(ls) // 2
    banda = Image.new("RGBA", (W, alto * len(ls) + 120), (0, 0, 0, 0))   # sombra suave detras del texto
    ImageDraw.Draw(banda).rounded_rectangle([40, 0, W - 40, banda.height], 60, fill=(0, 0, 0, 120))
    img.paste(banda.filter(ImageFilter.GaussianBlur(30)), (0, y - 60), banda.filter(ImageFilter.GaussianBlur(30)))
    destacar = (destacar or "").upper()
    for l in ls:
        x = (W - f.getlength(l)) / 2
        for p in l.split(" "):
            color = ACENTO[perfil] if destacar and p.strip("¿?¡!.,") == destacar.strip("¿?¡!.,") else (255, 255, 255)
            d.text((x, y), p, font=f, fill=color, stroke_width=max(8, tam // 14), stroke_fill=(0, 0, 0))
            x += f.getlength(p + " ")
        y += alto
    return y


def portada(v, datos, cfg, perfil, fotos, stickers):
    semilla = int(hashlib.md5(v.stem.encode()).hexdigest(), 16)
    rnd = random.Random(semilla)
    foto = elegir_foto(datos.get("foto"), fotos, semilla)
    img = fondo(foto, rnd) if foto else Image.new("RGB", (W, H), (20, 12, 30))
    img = img.convert("RGBA")
    arriba = rnd.random() < 0.5                                   # 2 composiciones que se alternan
    texto = datos.get("texto") or titulo_de(v)[:40]
    st = stickers.get(datos.get("sticker") or "")
    if st:
        s = Image.open(st).convert("RGBA")
        s.thumbnail((460, 460))
        s = s.rotate(rnd.choice([-1, 1]) * rnd.uniform(5, 12), resample=Image.BICUBIC, expand=True)
        sx = 70 if rnd.random() < 0.5 else W - s.width - 70
        sy = 1180 if arriba else 430
        img.alpha_composite(s, (int(sx), int(sy)))
    texto_grande(img, texto, datos.get("destacar"), perfil, 760 if arriba else 1230)
    logo = Path(cfg.get("logo", ""))
    if logo.exists():
        l = Image.open(logo).convert("RGBA")
        l.thumbnail((150, 150))
        img.alpha_composite(l, ((W - l.width) // 2, 230))
    destino = v.with_name(v.stem + ".portada.jpg")
    img.convert("RGB").save(destino, quality=92)
    return destino


def meter_en_video(v, p):
    """Pone la portada en los 2 primeros cuadros (0,07 s): no se nota y se puede elegir en el selector de YouTube."""
    tmp = Path(tempfile.gettempdir()) / f"port_{os.getpid()}.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(v), "-i", str(p), "-filter_complex",
                        "[1:v]scale=1080:1920,format=yuv420p[p];[0:v][p]overlay=enable='lt(t,0.07)'",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "copy", str(tmp)])
    if r.returncode == 0 and tmp.exists():
        tmp.replace(v)


def main():
    todo = "--todo" in sys.argv
    for nombre, perfil in CANALES.items():
        canal = RAIZ / nombre
        if not canal.exists():
            continue
        videos = pendientes(canal, todo)
        if not videos:
            continue
        cfg = perfil_cfg(perfil)
        fotos, stickers = fotos_de(cfg), stickers_de(cfg)
        print(f"\n🖼  {nombre}: {len(videos)} portadas")
        datos = pedir_textos(videos, cfg, perfil, fotos, stickers)
        for v, d in zip(videos, datos + [{}] * (len(videos) - len(datos))):
            p = portada(v, d if isinstance(d, dict) else {}, cfg, perfil, fotos, stickers)
            if "--en-video" in sys.argv:
                meter_en_video(v, p)
            print(f"   ✅ {v.parent.name}/{p.name}   «{d.get('texto', '') if isinstance(d, dict) else ''}»")


if __name__ == "__main__":
    main()
