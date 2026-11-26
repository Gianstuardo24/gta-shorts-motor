"""Efectos de sonido sinteticos (hechos con codigo, sin material de terceros) para los planos de afuera.
Uso: python3 sintet_sfx.py   -> escribe sonidos/sintet/*.wav (48 kHz mono)"""
import numpy as np, soundfile as sf, pathlib
SR = 48000
OUT = pathlib.Path(__file__).parent / "sonidos" / "sintet"; OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(7)


def t_(d): return np.arange(int(d * SR)) / SR
def env(n, a=0.002, r=0.05):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / max(r, 1e-4))
def bp(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR); X[(f < lo) | (f > hi)] = 0; return np.fft.irfft(X, len(x)).astype(np.float32)
def ruido(d): return rng.standard_normal(int(d * SR)).astype(np.float32)
def pon(p, x, t, g=1.0):
    i = int(t * SR); n = min(len(x), len(p) - i)
    if n > 0: p[i:i + n] += x[:n] * g
def clic(d=0.03, lo=1500, hi=7000, r=0.006):
    x = bp(ruido(d), lo, hi); return x * env(len(x), 0.0005, r)
def tono(f, d, r=0.2, h=(1,)):
    t = t_(d); return sum(np.sin(2 * np.pi * f * k * t) / (i + 1) for i, k in enumerate(h)).astype(np.float32) * env(len(t), 0.003, r)
def S(*xs):
    n = max(len(x) for x in xs); o = np.zeros(n, np.float32)
    for x in xs: o[:len(x)] += x
    return o
def guardar(nom, x, pico=0.85):
    x = x / (np.abs(x).max() + 1e-9) * pico; sf.write(str(OUT / f"{nom}.wav"), x.astype(np.float32), SR)


# teclas: teclado mecanico de los 80
p = np.zeros(int(2.8 * SR), np.float32); t = 0.05
while t < 2.7:
    pon(p, S(clic(0.035, 900, 6000, 0.008), 0.4 * clic(0.02, 200, 900, 0.01)), t, 0.6 + 0.4 * rng.random()); t += rng.uniform(0.07, 0.16)
    if rng.random() < 0.06: t += 0.25
guardar("teclas", p, 0.7)
# telefono de disco sonando (campanilla doble) y descolgar
p = np.zeros(int(1.0 * SR), np.float32); tt = t_(0.75)
camp = (np.sin(2 * np.pi * 1080 * tt) + 0.6 * np.sin(2 * np.pi * 1320 * tt)) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 22 * tt)))
pon(p, (camp * np.minimum(1, tt / 0.01) * np.minimum(1, (0.75 - tt) / 0.05)).astype(np.float32), 0, 0.5)
guardar("timbre", p, 0.6)
x = S(clic(0.05, 300, 3000, 0.02), 0.6 * bp(ruido(0.25), 800, 5000) * env(int(0.25 * SR), 0.01, 0.06)); guardar("descuelga", x, 0.6)
# claqueta: golpe seco de madera
x = S(clic(0.12, 400, 9000, 0.02), 0.8 * bp(ruido(0.12), 120, 600) * env(int(0.12 * SR), 0.0005, 0.03)); guardar("claqueta", x, 0.9)
# proyector de cine (traqueteo)
p = np.zeros(int(2.6 * SR), np.float32)
for i in range(int(2.6 * 24)): pon(p, clic(0.02, 600, 4000, 0.004), i / 24, 0.5 + 0.2 * (i % 2))
p += 0.15 * bp(ruido(2.6), 60, 300); guardar("proyector", p * np.minimum(1, t_(2.6) / 0.2) * np.minimum(1, (2.6 - t_(2.6)) / 0.3), 0.5)
# dados rodando sobre el pano
p = np.zeros(int(1.4 * SR), np.float32)
for i, tt0 in enumerate([0.0, 0.14, 0.25, 0.34, 0.42, 0.5, 0.57, 0.66, 0.8, 0.95]):
    pon(p, S(clic(0.04, 1200, 8000, 0.01), 0.5 * clic(0.04, 300, 1200, 0.015)), tt0 + rng.uniform(-.01, .01), 1 - i * 0.07)
guardar("dados", p, 0.8)
# billetes contados: papel que roza cada 0.19 s
p = np.zeros(int(2.8 * SR), np.float32)
for i in range(14): pon(p, bp(ruido(0.09), 2500, 11000) * env(int(0.09 * SR), 0.01, 0.03), 0.05 + i * 0.19, 0.6 + 0.3 * rng.random())
guardar("billetes", p, 0.6)
# hoja que se da vuelta
x = bp(ruido(0.4), 600, 7000); e = np.sin(np.linspace(0, np.pi, len(x))) ** 2; guardar("hoja", x * e, 0.6)
# lapiz escribiendo (rasgueo modulado)
tt = t_(3.6); x = bp(ruido(3.6), 1800, 9000) * (0.4 + 0.6 * np.abs(np.sin(2 * np.pi * 3.1 * tt)) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.7 * tt)))
guardar("lapiz", x * np.minimum(1, tt / 0.1) * np.minimum(1, (3.6 - tt) / 0.2), 0.45)
# chinche que se clava en el corcho
x = S(0.8 * tono(180, 0.12, 0.03), clic(0.05, 800, 4000, 0.012)); guardar("chinche", x, 0.8)
# computador: pitidos de proceso y aviso de terminado
p = np.zeros(int(2.6 * SR), np.float32)
for i in range(6): pon(p, tono(1200 + 200 * (i % 3), 0.05, 0.02), 0.1 + i * 0.32, 0.4)
pon(p, tono(880, 0.3, 0.12, (1, 2)), 2.2, 0.7); pon(p, tono(1320, 0.35, 0.15, (1, 2)), 2.32, 0.6)
p += 0.04 * np.sin(2 * np.pi * 60 * t_(2.6)).astype(np.float32); guardar("compu", p, 0.6)
# ciudad de noche: trafico suave y un auto que pasa
tt = t_(2.8); x = 0.5 * bp(ruido(2.8), 40, 500) + 0.25 * bp(ruido(2.8), 500, 2500) * (0.3 + 0.7 * np.exp(-((tt - 1.4) / 0.5) ** 2))
guardar("ciudad", x * np.minimum(1, tt / 0.3) * np.minimum(1, (2.8 - tt) / 0.4), 0.5)
# sube / baja: barrido de tono
for nom, f0, f1 in (("sube", 220, 880), ("baja", 700, 160)):
    tt = t_(1.8); f = f0 * (f1 / f0) ** (tt / 1.8); ph = 2 * np.pi * np.cumsum(f) / SR
    x = (np.sin(ph) + 0.3 * np.sin(2 * ph)) * np.minimum(1, tt / 0.1) * np.minimum(1, (1.8 - tt) / 0.25); guardar(nom, x.astype(np.float32), 0.5)
# regla de anos: tics y campanita
p = np.zeros(int(1.8 * SR), np.float32)
for i in range(10): pon(p, clic(0.02, 2000, 9000, 0.004), i * 0.12 * (1 + i * 0.04), 0.6)
pon(p, tono(1568, 0.6, 0.25, (1, 2.01, 3.02)), 1.3, 0.7); guardar("tics", p, 0.6)
# balanza: tintineo metalico + golpe del platillo
x = np.zeros(int(1.0 * SR), np.float32); pon(x, tono(2350, 0.6, 0.18, (1, 1.51, 2.3)), 0, 0.5); pon(x, bp(ruido(0.2), 60, 400) * env(int(0.2 * SR), 0.001, 0.05), 0.05, 1.0)
guardar("balanza", x, 0.75)
# tablero de aeropuerto: aletas girando
p = np.zeros(int(1.8 * SR), np.float32); t = 0
while t < 1.7: pon(p, clic(0.015, 1500, 7000, 0.003), t, 0.5 + 0.5 * rng.random()); t += rng.uniform(0.018, 0.05)
guardar("aletas", p * np.minimum(1, (1.8 - t_(1.8)) / 0.4), 0.55)
print("ok", sorted(f.name for f in OUT.glob("*.wav")))
