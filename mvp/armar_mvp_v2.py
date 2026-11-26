"""Video MVP de Repers (Start-Up Chile Ignite): recorrido funcional de 16:9 a partir de la grabacion de pantalla del iPhone.
Uso: python3 armar_mvp.py  -> mvp_repers.mp4
"""
import subprocess, textwrap, os
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

# (inicio, fin, tipo, seccion, titulo, subtitulo, texto)  tipo J = dentro de la partida (sonido real), M = menus (musica pareja)
# v2 (23-nov, pedido de Tao): todo a velocidad real, solo cortes; musica de menus continua y sin acelerar.
S = []
def seg(a, b, tipo, sec, tit, sub, txt): S.append((a, b, tipo, sec, tit, sub, txt))

seg(108.5, 114.6, "J", -1, "Repers · prototipo funcional", "La cámara del celular convierte el movimiento en juego",
    "Grabación real de la app en un iPhone. A continuación, el recorrido completo de un usuario.")
T1 = ("1 · Primer uso", "Cómo entra un usuario nuevo",
      "Tutorial corto, permiso de cámara, datos con el correo de un adulto responsable, recomendaciones de salud y un apodo generado (sin nombre real).")
seg(0.5, 3.5, "M", 0, *T1)
seg(8.5, 11.0, "M", 0, *T1)
seg(20.0, 23.0, "M", 0, *T1)
seg(32.5, 35.0, "M", 0, *T1)
seg(46.0, 49.0, "M", 0, *T1)
seg(56.5, 59.0, "M", 0, *T1)
T2 = ("2 · Elegir partida", "Solo o en línea con amigos",
      "Partida completa, rápida o Misión Escape, y el ejercicio: saltos de tijera, sentadillas, flexiones o elevación de rodillas.")
seg(61.0, 68.5, "M", 1, *T2)
T3a = ("3 · Detección del cuerpo", "Función principal: la cámara reconoce el movimiento",
       "La IA de visión corre en el teléfono: ubica al jugador y comienza la serie.")
seg(83.0, 86.0, "J", 2, *T3a)
T3b = ("3 · Detección del cuerpo", "En tiempo real",
       "El avatar copia el movimiento del jugador y cada elevación de rodilla suma una repetición. Sin control ni accesorios: solo el celular. "
       "El punto verde arriba a la derecha indica que la cámara está encendida.")
seg(86.0, 101.0, "J", 2, *T3b)
T3c = ("3 · Detección del cuerpo", "Rachas y modo turbo",
       "Moverse sin parar activa rachas y el modo turbo. El juego pide moverse; el ejercicio ocurre solo.")
seg(101.0, 106.0, "J", 2, *T3c)
seg(116.0, 118.6, "M", 2, "3 · Detección del cuerpo", "Resultado de la serie",
    "25 repeticiones en 30 segundos, que se convierten en tokens y experiencia.")
T4a = ("4 · Misión Escape", "Función 2: un juego que se controla con el cuerpo",
       "Antes de empezar, la IA revisa que se vea el cuerpo completo; cuando lo ve, el jugador levanta los brazos para partir.")
seg(125.3, 127.0, "M", 3, *T4a)
seg(133.0, 135.6, "J", 3, *T4a)
T4b = ("4 · Misión Escape", "En tiempo real",
       "Trotar en el lugar hace correr al personaje; brazos arriba = saltar; sentadilla = agacharse; un brazo al lado = cambiar de carril. "
       "Arriba a la derecha, un mini avatar copia al jugador en vez de mostrar la cámara.")
seg(139.4, 156.5, "J", 3, *T4b)
seg(157.0, 159.5, "J", 3, "4 · Misión Escape", "Resultado", "151 metros recorridos, con monedas y experiencia.")
T5 = ("5 · Progreso y amigos", "Función 3: lo que hace volver a jugar",
      "Con lo ganado se viste al avatar; hay ruleta y cofre diario, y amigos por código para jugar en línea.")
seg(236.0, 240.0, "M", 4, *T5)
seg(259.5, 263.5, "M", 4, *T5)
seg(273.5, 276.0, "M", 4, *T5)
seg(352.5, 355.5, "M", 4, *T5)
T6 = ("6 · Privacidad", "Pensado para niños y sus familias",
      "La imagen de la cámara se procesa en el teléfono y no se guarda; los demás jugadores solo ven el avatar. La cuenta se elimina desde la app.")
seg(388.0, 391.0, "M", 5, *T6)
seg(393.0, 395.0, "M", 5, *T6)
seg(300.0, 304.0, "M", 5, "Estado actual", "Prototipo funcional (beta)",
    "Funciona en iPhone y Android y está en proceso de publicación en App Store y Google Play. El multijugador en línea está en pruebas.")
CAMA = [276.0, 316.0, 334.0]     # tramos largos de musica de menu, continua, para poner debajo de cada bloque de menus


def fuente(f, n): return ImageFont.truetype(f, n)


def envolver(d, txt, f, ancho):
    lineas, cur = [], ""
    for p in txt.split():
        t = (cur + " " + p).strip()
        if d.textlength(t, font=f) <= ancho: cur = t
        else: lineas.append(cur); cur = p
    if cur: lineas.append(cur)
    return lineas


def fondo(i, sec, tit, sub, txt, tipo):
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
    rt = tipo == "J"
    et = "EN LA PARTIDA · TIEMPO REAL" if rt else "MENÚS DE LA APP · TIEMPO REAL"
    fe = fuente(FB, 24); we = d.textlength(et, font=fe)
    col = (34, 197, 94) if rt else (120, 160, 255)
    d.rounded_rectangle([x0, 190, x0 + we + 66, 236], 23, fill=(col[0] // 5, col[1] // 5, col[2] // 5), outline=col, width=2)
    d.ellipse([x0 + 20, 205, x0 + 36, 221], fill=col)
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
    total = 0; lista = []; audios = []
    cama_i, cama_t, prev = -1, 0.0, None
    for i, (a, b, tipo, sec, tit, sub, txt) in enumerate(S):
        f = fondo(i, sec, tit, sub, txt, tipo)
        dur = b - a; total += dur
        o = f"partes/p{i:02d}.mp4"
        fil = (f"[1:v]trim={a}:{b},setpts=PTS-STARTPTS,fps=30,scale={PW}:{PH}[ph];"
               f"[2:v]format=gray[mk];[ph][mk]alphamerge[phm];"
               f"[0:v][phm]overlay={PX}:{PY}:shortest=1,format=yuv420p[v]")
        if not (os.environ.get("SOLO_AUDIO") and Path(o).exists()): subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{dur:.3f}", "-i", f, "-i", FUENTE,
                        "-loop", "1", "-t", f"{dur:.3f}", "-i", "fondos/mascara.png", "-filter_complex", fil, "-map", "[v]",
                        "-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-r", "30", "-an", o], check=True)
        lista.append(o)
        # audio: en la partida el sonido real; en menus una musica de menu continua (sin saltos ni aceleracion)
        if tipo == "J":
            ini, vol = a, 1.0
        else:
            if prev != "M":
                cama_i += 1; cama_t = CAMA[min(cama_i, len(CAMA) - 1)]
            ini, vol = cama_t, 0.7
            cama_t += dur
        fin_in = 0.0 if (tipo == "M" and prev == "M") else 0.06
        sig = S[i + 1][2] if i + 1 < len(S) else None
        fin_out = 0.0 if (tipo == "M" and sig == "M") else 0.08
        af = f"atrim={ini}:{ini + dur},asetpts=PTS-STARTPTS,volume={vol}"
        if fin_in: af += f",afade=t=in:d={fin_in}"
        if fin_out: af += f",afade=t=out:st={max(0, dur - fin_out):.3f}:d={fin_out}"
        wa = f"partes/a{i:02d}.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", FUENTE, "-af", af, "-ac", "2", "-ar", "48000", wa], check=True)
        audios.append(wa); prev = tipo
        print(f"{i:02d} {a:6.1f}-{b:6.1f} {tipo} -> {dur:5.2f}s  (acum {total:6.2f})  {tit}")
    Path("lista.txt").write_text("".join(f"file '{p}'\n" for p in lista))
    Path("lista_a.txt").write_text("".join(f"file '{p}'\n" for p in audios))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "lista.txt", "-c", "copy", "partes/video.mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "lista_a.txt", "partes/audio.wav"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "partes/video.mp4", "-i", "partes/audio.wav",
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "mvp_repers.mp4"], check=True)
    print("TOTAL", round(total, 2), "s")


if __name__ == "__main__":
    main()
