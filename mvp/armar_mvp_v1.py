"""Video MVP de Repers (Start-Up Chile Ignite): recorrido funcional de 16:9 a partir de la grabacion de pantalla del iPhone.
Uso: python3 armar_mvp.py  -> mvp_repers.mp4
"""
import subprocess, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FUENTE = "fuente.mp4"
W, H = 1920, 1080
PW, PH, PX, PY = 462, 1000, 190, 40           # telefono en pantalla
FB = "/home/claude/escena/Poppins-Bold.ttf"
FR = "/home/claude/escena/Poppins-Regular.ttf"
LOGO = "/mnt/user-data/uploads/gta-shorts/assets/logo_repers.png"
AZUL = (30, 95, 224)
SECC = ["Primer uso", "Elegir partida", "Detección del cuerpo", "Misión Escape", "Progreso", "Privacidad y estado"]

# (inicio, fin, velocidad, seccion, titulo, subtitulo, texto)
S = []
def seg(a, b, v, sec, tit, sub, txt): S.append((a, b, v, sec, tit, sub, txt))

T0 = ("Repers · prototipo funcional", "Grabación real de la app en un iPhone",
      "Grabación de pantalla de la app funcionando. Solo se quitaron esperas; las partes aceleradas están marcadas.")
seg(0.5, 5.0, 1.0, -1, *T0)
T1 = ("1 · Primer uso", "Cómo entra un usuario nuevo",
      "Tutorial corto, permiso de cámara, datos con el correo de un adulto responsable, recomendaciones de salud y un apodo generado (sin nombre real).")
seg(7.0, 19.0, 3.0, 0, *T1)
seg(19.5, 23.5, 1.5, 0, *T1)
seg(31.0, 36.0, 2.0, 0, *T1)
seg(43.0, 55.0, 4.0, 0, *T1)
seg(56.0, 59.5, 1.5, 0, *T1)
T2 = ("2 · Elegir partida", "Solo o en línea con amigos",
      "Partida completa, rápida o Misión Escape, y el ejercicio: saltos de tijera, sentadillas, flexiones o elevación de rodillas.")
seg(60.0, 67.5, 1.5, 1, *T2)
T3a = ("3 · Detección del cuerpo", "Función principal: la cámara reconoce el movimiento",
       "La IA de visión corre en el teléfono: ubica al jugador, cuenta regresiva y comienza la serie.")
seg(74.0, 81.0, 2.0, 2, *T3a)
seg(81.0, 86.0, 2.0, 2, *T3a)
T3b = ("3 · Detección del cuerpo", "En tiempo real",
       "El avatar copia el movimiento del jugador y cada elevación de rodilla suma una repetición. Sin control ni accesorios: solo el celular. "
       "El punto verde arriba a la derecha indica que la cámara está encendida.")
seg(86.0, 101.0, 1.0, 2, *T3b)
T3c = ("3 · Detección del cuerpo", "Rachas y modo turbo",
       "Moverse sin parar activa rachas y el modo turbo. El juego pide moverse; el ejercicio ocurre solo.")
seg(108.5, 115.5, 1.0, 2, *T3c)
T3d = ("3 · Detección del cuerpo", "Resultado de la serie",
       "25 repeticiones en 30 segundos, que se convierten en tokens y experiencia.")
seg(116.0, 119.0, 1.0, 2, *T3d)
T4a = ("4 · Misión Escape", "Función 2: un juego que se controla con el cuerpo",
       "Antes de empezar, la IA revisa que se vea el cuerpo completo y que el jugador esté quieto.")
seg(120.0, 127.0, 3.0, 3, *T4a)
seg(127.0, 129.0, 2.0, 3, *T4a)
seg(129.0, 135.0, 1.0, 3, *T4a)
seg(135.0, 140.0, 2.5, 3, *T4a)
T4b = ("4 · Misión Escape", "En tiempo real",
       "Trotar en el lugar hace correr al personaje; brazos arriba = saltar; sentadilla = agacharse; un brazo al lado = cambiar de carril. "
       "Arriba a la derecha, un mini avatar copia al jugador en vez de mostrar la cámara.")
seg(140.0, 156.5, 1.0, 3, *T4b)
seg(157.0, 159.5, 1.0, 3, "4 · Misión Escape", "Resultado", "151 metros recorridos, con monedas y experiencia.")
T5 = ("5 · Progreso y amigos", "Función 3: lo que hace volver a jugar",
      "Con lo ganado se viste al avatar; hay ruleta y cofre diario, y amigos por código para jugar en línea.")
seg(228.0, 248.0, 4.0, 4, *T5)
seg(259.0, 269.0, 2.5, 4, *T5)
seg(272.0, 277.0, 2.0, 4, *T5)
seg(318.0, 322.0, 2.0, 4, *T5)
seg(352.5, 356.0, 1.5, 4, *T5)
T6 = ("6 · Privacidad", "Pensado para niños y sus familias",
      "La imagen de la cámara se procesa en el teléfono y no se guarda; los demás jugadores solo ven el avatar. La cuenta se elimina desde la app.")
seg(384.0, 394.5, 3.0, 5, *T6)
T7 = ("Estado actual", "Prototipo funcional (beta)",
      "Funciona en iPhone y Android y está en proceso de publicación en App Store y Google Play. El multijugador en línea está en pruebas.")
seg(300.0, 305.0, 1.0, 5, *T7)


def fuente(f, n): return ImageFont.truetype(f, n)


def envolver(d, txt, f, ancho):
    lineas, cur = [], ""
    for p in txt.split():
        t = (cur + " " + p).strip()
        if d.textlength(t, font=f) <= ancho: cur = t
        else: lineas.append(cur); cur = p
    if cur: lineas.append(cur)
    return lineas


def fondo(i, sec, tit, sub, txt, v):
    im = Image.new("RGB", (W, H), (11, 16, 32))
    g = Image.new("L", (W, H))
    gd = ImageDraw.Draw(g)
    for y in range(H): gd.line([(0, y), (W, y)], fill=int(40 * y / H))
    im = Image.composite(Image.new("RGB", (W, H), (22, 30, 60)), im, g)
    # resplandor detras del telefono
    gl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(gl).rounded_rectangle([PX - 30, PY - 20, PX + PW + 30, PY + PH + 20], 70, fill=(30, 95, 224, 70))
    im.paste(gl.filter(ImageFilter.GaussianBlur(40)), (0, 0), gl.filter(ImageFilter.GaussianBlur(40)))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([PX - 10, PY - 10, PX + PW + 10, PY + PH + 10], 52, fill=(4, 6, 12), outline=(70, 80, 110), width=3)
    x0 = 760
    # marca arriba
    try:
        lg = Image.open(LOGO).convert("RGBA").resize((72, 72))
        m = Image.new("L", (72, 72), 0); ImageDraw.Draw(m).ellipse([0, 0, 71, 71], fill=255)
        im.paste(lg, (x0, 50), m)
    except Exception:
        pass
    d.text((x0 + 92, 58), "Repers", font=fuente(FB, 34), fill=(255, 255, 255))
    d.text((x0 + 92, 100), "Juego móvil que convierte el movimiento del cuerpo en juego", font=fuente(FR, 22), fill=(160, 170, 200))
    # etiqueta de velocidad
    rt = v == 1.0
    et = "TIEMPO REAL" if rt else f"ACELERADO ×{v:g}"
    fe = fuente(FB, 24); we = d.textlength(et, font=fe)
    col = (34, 197, 94) if rt else (245, 158, 11)
    d.rounded_rectangle([x0, 190, x0 + we + 66, 236], 23, fill=(col[0] // 5, col[1] // 5, col[2] // 5), outline=col, width=2)
    if rt: d.ellipse([x0 + 20, 205, x0 + 36, 221], fill=col)
    else:
        for dx in (0, 13): d.polygon([(x0 + 18 + dx, 204), (x0 + 30 + dx, 213), (x0 + 18 + dx, 222)], fill=col)
    d.text((x0 + 50, 196), et, font=fe, fill=col)
    # titulo, subtitulo y texto
    d.text((x0, 270), tit, font=fuente(FB, 66), fill=(255, 255, 255))
    d.text((x0, 362), sub, font=fuente(FB, 34), fill=(110, 160, 255))
    ft = fuente(FR, 36)
    y = 450
    for ln in envolver(d, txt, ft, 1060):
        d.text((x0, y), ln, font=ft, fill=(225, 230, 245)); y += 50
    # barra de secciones
    fs = fuente(FB, 19); x = x0; y = 990
    for k, nom in enumerate(SECC):
        wn = d.textlength(nom, font=fs) + 30
        act = k == sec
        d.rounded_rectangle([x, y, x + wn, y + 42], 21, fill=AZUL if act else (28, 36, 64), outline=(70, 90, 150) if not act else AZUL, width=2)
        d.text((x + 15, y + 9), nom, font=fs, fill=(255, 255, 255) if act else (150, 160, 190))
        x += wn + 8
    p = f"fondos/f{i:02d}.png"; im.save(p); return p


def mascara():
    m = Image.new("L", (PW, PH), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, PW - 1, PH - 1], 44, fill=255)
    m.save("fondos/mascara.png")


def atempo(v):
    out, r = [], v
    while r > 2.0: out.append("atempo=2.0"); r /= 2.0
    out.append(f"atempo={r:.4f}")
    return ",".join(out)


def main():
    Path("fondos").mkdir(exist_ok=True); Path("partes").mkdir(exist_ok=True)
    mascara()
    total = 0; lista = []
    for i, (a, b, v, sec, tit, sub, txt) in enumerate(S):
        f = fondo(i, sec, tit, sub, txt, v)
        dur = (b - a) / v; total += dur
        o = f"partes/p{i:02d}.mp4"
        vol = 1.0 if v == 1.0 else 0.45
        fil = (f"[1:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{v},fps=30,scale={PW}:{PH}[ph];"
               f"[2:v]format=gray[mk];[ph][mk]alphamerge[phm];"
               f"[0:v][phm]overlay={PX}:{PY}:shortest=1,format=yuv420p[v];"
               f"[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS,{atempo(v)},volume={vol},"
               f"afade=t=in:d=0.08,afade=t=out:st={max(0, dur - 0.1):.3f}:d=0.1[a]")
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{dur:.3f}", "-i", f, "-i", FUENTE,
               "-loop", "1", "-t", f"{dur:.3f}", "-i", "fondos/mascara.png",
               "-filter_complex", fil, "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", o]
        subprocess.run(cmd, check=True)
        lista.append(o)
        print(f"{i:02d} {a:6.1f}-{b:6.1f} x{v:g} -> {dur:5.2f}s  (acum {total:6.2f})  {tit}")
    Path("lista.txt").write_text("".join(f"file '{p}'\n" for p in lista))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "lista.txt",
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "mvp_repers.mp4"], check=True)
    print("TOTAL", round(total, 2), "s")


if __name__ == "__main__":
    main()
