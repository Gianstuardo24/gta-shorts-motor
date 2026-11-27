"""MDM 18h · montaje: video ya renderizado + voz + música del canal + efectos pertinentes + exportación.
Misma mezcla que escena/armar_escena.py (25-nov): la música baja antes de cada frase, compresor suave en la voz,
ganancia fija a -14 LUFS con limitador. No toca el pipeline de producción: solo importa sus funciones.
Uso: python3 montar.py VIDEO_MUDO.mp4 SALIDA.mp4"""
import sys, json, pathlib, subprocess, numpy as np, soundfile as sf
AQUI = pathlib.Path(__file__).resolve().parent
RAMA = AQUI.parents[2]
sys.path.insert(0, str(RAMA / "escena"))
import armar_escena as A, musica
SR, SON = A.SR, A.SON
video, salida = sys.argv[1:3]
T = json.loads((AQUI / "datos.json").read_text())["T"]
D = T["fin"]
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("0", 0.05, "sintet/hoja.wav", None, .12),                       # gancho: la mano planta la factura
       ("x_price", -0.20, "transicion/whoosh_04.wav", .28, .06),         # gancho: la cámara salta al "$35"
       ("x_joke", 0, "impacto/kick_01.wav", .16, .06),                   # gancho: el papel se sacude
       ("c1", -0.30, "transicion/whoosh_02.wav", .30, .08),              # del gancho a la historia (termina antes de la voz)
       ("c1", 1.44, "impacto/kick_01.wav", .18, .07),                    # 01: la zapatilla se apoya
       ("x_rasga", .12, "sintet/hoja.wav", None, .14),                   # 03: arranca la hoja
       ("x_on", .06, "sintet/chinche.wav", None, .16),                   # 04: clava la carpeta
       ("x_swoosh", -.20, "sintet/hoja.wav", None, .12),                 # 05A: abre la tapa
       ("c5b", .14, "impacto/kick_01.wav", .16, .08), ("x_most", .30, "impacto/kick_01.wav", .16, .06),   # 05B: primeros dos pasos
       ("c6", -0.30, "transicion/whoosh_03.wav", .30, .08),              # salto a 1983 (termina antes de la voz)
       ("x_one", .25, "sintet/hoja.wav", None, .10),                     # 06: llega el sobre
       ("x_gold", -.26, "sintet/descuelga.wav", None, .12),              # 07: abre el estuche
       ("x_gold", .62, "ui/ding_01.wav", .9, .05),                       # 07: el anillo
       ("x_500", 0, "sintet/hoja.wav", None, .12),                       # 08: saca el documento
       ("x_tell", .50, "sintet/chinche.wav", None, .10)]                 # cierre: deja el lápiz
# Sin sonidos de escritura: Tao los encontró molestos (27-nov 00:57).
fx = np.zeros(int(D * SR) + SR, np.float32)
for k, off, f, dur, g in SFX:
    x = A.leer(SON / f)
    if dur: x = A.recorte(x, dur, .12)
    A.poner(fx, x, max(0, (0 if k == "0" else T[k]) + off), g)
fx = fx[: int(D * SR)]
voz = A.leer(AQUI / "voz" / "vz.wav")
musica.CARPETA = SON / "musica"
mus, info = musica.generar(D, "MDM18_FASEA_escena", "deep")
print("música:", info)
n = int(D * SR)
v = np.zeros(n, np.float32); v[: min(n, len(voz))] = voz[:n]
m = np.zeros(n, np.float32); m[: min(n, len(mus))] = mus[:n]
env = np.abs(v); k = int(0.25 * SR); env = np.convolve(env, np.ones(k) / k, mode="same")
adel = int(0.22 * SR); env = np.maximum(env, np.concatenate([env[adel:], np.zeros(adel, env.dtype)]))
duck = 1 - 0.55 * np.clip(env / (env.max() * 0.25 + 1e-6), 0, 1)
from scipy.ndimage import maximum_filter1d, uniform_filter1d
ev = uniform_filter1d(maximum_filter1d(np.abs(v), int(0.012 * SR)), int(0.06 * SR))
hab = ev[ev > ev.max() * 0.05]
if len(hab):
    thr = float(np.percentile(hab, 70))
    g_ = np.where(ev > thr, (thr / np.maximum(ev, 1e-9)) ** (1 - 1 / 3.0), 1.0)
    v = v * uniform_filter1d(g_, int(0.03 * SR)).astype(np.float32)
mezcla = v * 1.0 + m * 0.22 * duck + fx
tmp = pathlib.Path(salida).with_suffix(".mezcla.wav")
sf.write(tmp, mezcla / max(1.0, np.abs(mezcla).max() / 0.95), SR)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(tmp), "-af", "loudnorm=I=-14:TP=-2:LRA=11:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True).stderr
med = json.loads(r[r.rindex("{"): r.rindex("}") + 1])
ln = f"volume={-14.0 - float(med['input_i']):.2f}dB,alimiter=limit=0.84:level=false:attack=5:release=150"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", str(tmp), "-af", ln, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-ar", "48000", "-shortest", "-movflags", "+faststart", salida], check=True)
tmp.unlink()
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", salida, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
i = r.rindex("Integrated loudness"); print("volumen:", " ".join(r[i:i + 260].split()))
