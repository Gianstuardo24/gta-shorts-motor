"""IMAGENES IA (de tu ChatGPT) como tomas de un video.
Corta una hoja en grilla (por defecto 3x1: tres paneles VERTICALES 9:16 con bordes blancos), hace clips con movimiento suave (Ken Burns),
los suma al catalogo del canal y los deja como 'tomas_elegidas' del guion, en el orden que digas.

Uso:  CANAL=mdm python imagenes_ia.py GUION hojaA.png [hojaB.png ...] --orden=A1,A2,A3,B1,...  [--grilla=3x2]
      ej: CANAL=mdm python imagenes_ia.py M2026111501_01 ~/Downloads/a.png ~/Downloads/b.png --orden=A1,A2,A3,A4,B1,B2,B3,A5,B4,A6,B5,B6
"""
import sys, json, subprocess
from pathlib import Path
from PIL import Image, ImageFilter
from utilidades import cfg
import stock

CFG = cfg()
DIR = Path(CFG.get("tomas_dir", "tomas_stock"))


def cortar(hoja, cols, filas, margen=0.012):
    im = Image.open(hoja).convert("RGB")
    W, H = im.size
    cw, ch = W / cols, H / filas
    out = []
    for f in range(filas):
        for c in range(cols):
            mx, my = cw * margen * 2, ch * margen * 2      # quita el borde blanco entre paneles
            out.append(im.crop((int(c * cw + mx), int(f * ch + my), int((c + 1) * cw - mx), int((f + 1) * ch - my))))
    return out


def encuadre_vertical(panel):
    """El montaje recorta el centro 9:16 (608x1080) de un cuadro 1920x1080. El panel se escala para CUBRIR ese centro completo
    (pantalla completa, sin franjas a los lados): si el panel es mas angosto que 9:16 se recorta un poco arriba y abajo.
    Los lados del cuadro 1920 (que no se ven en el Short) van con el mismo panel desenfocado."""
    W, H = 1920, 1080
    ancho_916 = int(H * 9 / 16) + 8                 # 608 + margen: cubre el recorte 9:16 aunque el zoom este en 1.0
    fondo = panel.resize((W, int(W * panel.height / panel.width)), Image.LANCZOS)
    fondo = fondo.crop((0, (fondo.height - H) // 2, W, (fondo.height - H) // 2 + H)).filter(ImageFilter.GaussianBlur(40))
    alto = max(H, int(ancho_916 * panel.height / panel.width))
    fg = panel.resize((int(alto * panel.width / panel.height), alto), Image.LANCZOS)
    if fg.height > H:                               # recorte vertical centrado (se pierde ~5 % arriba y abajo)
        y0 = (fg.height - H) // 2
        fg = fg.crop((0, y0, fg.width, y0 + H))
    fondo.paste(fg, ((W - fg.width) // 2, 0))
    return fondo


def zoom_lento(img, out, dur=12.0):
    """Zoom-in suave y CENTRADO (sin paneo lateral, para no sacar el panel vertical del encuadre 9:16)."""
    n = int(dur * 30)
    vf = (f"scale=3840:2160,zoompan=z='min(zoom+0.0005,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={n}:s=1920x1080:fps=30,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "fatal", "-loop", "1", "-i", str(img), "-vf", vf, "-frames:v", str(n),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(out)], check=True, timeout=180)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
    if len(args) < 2:
        print(__doc__); return
    stem, hojas = args[0], args[1:]
    cols, filas = map(int, opts.get("grilla", "3x1").split("x"))
    g_path = Path("guiones", f"{stem}.json")
    g = json.loads(g_path.read_text())
    (DIR / "img").mkdir(parents=True, exist_ok=True); (DIR / "clips").mkdir(parents=True, exist_ok=True)
    cat_p = DIR / "catalogo.json"
    cat = json.loads(cat_p.read_text()) if cat_p.exists() else []
    nombres = {}
    for letra, hoja in zip("ABCDEFGH", hojas):
        for k, panel in enumerate(cortar(hoja, cols, filas), 1):
            nombre = f"{letra}{k}"
            img = DIR / "img" / f"ia_{stem}_{nombre}.png"
            (encuadre_vertical(panel) if panel.height > panel.width else
             panel.resize((panel.width * 2, panel.height * 2), Image.LANCZOS)).save(img)
            clip = DIR / "clips" / f"ia_{stem}_{nombre}.mp4"
            zoom_lento(img, clip)
            cat = [t for t in cat if t["archivo"] != str(clip)]
            cat.append({"archivo": str(clip), "inicio": 0.0, "fin": 12.0, "tipo": "foto",
                        "origen": "chatgpt", "fuente": f"ia {stem} {nombre} (generada en ChatGPT del canal)"})
            nombres[nombre] = str(clip)
            print(f"   ✅ {nombre} → {clip}")
    cat_p.write_text(json.dumps(cat, ensure_ascii=False, indent=1))
    orden = [o.strip().upper() for o in opts.get("orden", ",".join(nombres)).split(",") if o.strip().upper() in nombres]
    g["tomas_elegidas"] = [nombres[o] for o in orden]
    g["tomas_descartadas"] = g.get("tomas_descartadas", [])
    g["imagen_por_frase"] = True          # montar.py: cada imagen entra cuando suena su frase
    g_path.write_text(json.dumps(g, ensure_ascii=False, indent=2))
    print(f"✅ {stem}: {len(orden)} imagenes IA como tomas elegidas. Siguiente: montar.py")


if __name__ == "__main__":
    main()
