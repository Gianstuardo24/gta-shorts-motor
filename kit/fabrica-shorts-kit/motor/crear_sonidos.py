"""Crea TODOS los sonidos del motor por síntesis (sin samples de terceros): efectos y batería para la música.

Uso (lo corre instalar.sh):   ./venv/bin/python3 motor/crear_sonidos.py
Sale en motor/escena/sonidos/<carpeta>/<nombre>.wav (48 kHz, mono). Si quieres usar sonidos tuyos con licencia,
ponlos en la misma carpeta con el mismo prefijo (ej. ui/pop_04.wav) y el motor los usa también.
"""
from pathlib import Path
import numpy as np
import soundfile as sf

SR = 48000
DEST = Path(__file__).resolve().parent / "escena" / "sonidos"
rng = np.random.default_rng(7)


def t(d):
    return np.arange(int(d * SR)) / SR


def env(d, a=0.004, dec=6.0):
    x = t(d)
    e = np.exp(-dec * x)
    na = max(1, int(a * SR))
    e[:na] *= np.linspace(0, 1, na)
    return e


def lp(x, corte):
    """Paso bajo de un polo (barato y suficiente)."""
    a = np.exp(-2 * np.pi * corte / SR)
    y = np.zeros_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def hp(x, corte):
    return x - lp(x, corte)


def barrido(f0, f1, d):
    f = np.geomspace(f0, f1, int(d * SR))
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def ruido(d):
    return rng.standard_normal(int(d * SR))


def norm(x, pico=0.8):
    m = np.abs(x).max() or 1
    return (x / m * pico).astype(np.float32)


def guardar(carpeta, nombre, x):
    p = DEST / carpeta
    p.mkdir(parents=True, exist_ok=True)
    sf.write(p / f"{nombre}.wav", norm(x), SR)


def whoosh(d, f0, f1, brillo):
    n = ruido(d)
    x = t(d)
    e = np.sin(np.pi * np.clip(x / d, 0, 1)) ** 1.6                  # sube y baja
    capas = []
    for c in np.geomspace(f0, f1, 6):                                # barrido de banda por tramos
        capas.append(lp(hp(n, c * 0.6), c * brillo))
    seg = np.array_split(np.arange(len(n)), 6)
    y = np.zeros_like(n)
    for capa, idx in zip(capas, seg):
        y[idx] = capa[idx]
    return lp(y, 9000) * e


def pop(f0, d=0.09):
    return barrido(f0, f0 * 0.45, d) * env(d, 0.001, 38)


def campana(f, d=0.9, parciales=(1, 2.76, 5.4, 8.9)):
    x = t(d)
    return sum(np.sin(2 * np.pi * f * k * x) * np.exp(-x * (3 + 2.5 * i)) / (1 + i) for i, k in enumerate(parciales))


def kick(f0=130, f1=42, d=0.45, click=0.3):
    k = barrido(f0, f1, d) * env(d, 0.001, 7)
    c = hp(ruido(0.012), 2000) * click
    k[: len(c)] += c
    return k


def hat(d, dec):
    return hp(ruido(d), 7000) * env(d, 0.0005, dec)


def clap(d=0.25):
    n = hp(lp(ruido(d), 5000), 900)
    e = np.zeros(len(n))
    for off in (0, 0.011, 0.022):                                    # 3 golpes muy juntos
        i = int(off * SR)
        e[i:] += np.exp(-np.arange(len(n) - i) / SR * 60)
    e += 0.4 * np.exp(-t(d) * 14)
    return n * e


def main():
    # transiciones (whoosh cortos, ~0.35-0.55 s)
    for i, (d, f0, f1, b) in enumerate([(0.38, 400, 3800, 1.6), (0.45, 300, 2500, 1.4), (0.5, 600, 6000, 1.8),
                                        (0.35, 900, 4500, 1.5), (0.55, 250, 2000, 1.3)], start=2):
        guardar("transicion", f"whoosh_0{i}", whoosh(d, f0, f1, b))
    # ui
    guardar("ui", "pop_01", pop(900))
    guardar("ui", "pop_02", pop(1250, 0.07))
    guardar("ui", "pop_03", pop(700, 0.11))
    guardar("ui", "ding_01", campana(1760, 0.8))
    guardar("ui", "clap_03", clap(0.2))
    # impacto
    guardar("impacto", "kick_01", kick())
    guardar("impacto", "kick_02", kick(160, 38, 0.6, 0.5))
    # glitch / electricidad
    d = 0.35
    sq = np.sign(np.sin(2 * np.pi * 180 * t(d))) * (rng.random(int(d * SR)) > 0.3)
    guardar("glitch", "glitch_01", lp(sq * env(d, 0.002, 6), 6000))
    d = 0.4
    zap = hp(ruido(d), 1500) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 37 * t(d)))) * env(d, 0.001, 5)
    guardar("glitch", "electrico_02", zap + 0.3 * np.sin(2 * np.pi * 120 * t(d)) * env(d, 0.001, 5))
    # temáticos
    for i, f in enumerate((2093, 2349, 1976), start=1):              # caja registradora: clic + campanita
        c = np.zeros(int(0.9 * SR))
        clic = hp(ruido(0.03), 1500) * env(0.03, 0.0005, 120)
        c[: len(clic)] += clic * 0.7
        b = campana(f, 0.8) * 0.8
        c[int(0.06 * SR): int(0.06 * SR) + len(b)] += b[: len(c) - int(0.06 * SR)]
        guardar("tematicos", f"caja_0{i}", c)
    for i, (f1, f2) in enumerate(((2637, 3520), (3136, 4186)), start=1):   # moneda
        d = 0.35
        x = t(d)
        m = np.sin(2 * np.pi * f1 * x) * np.exp(-x * 14)
        m[int(0.06 * SR):] += np.sin(2 * np.pi * f2 * x[: len(x) - int(0.06 * SR)]) * np.exp(-x[: len(x) - int(0.06 * SR)] * 10)
        guardar("tematicos", f"moneda_0{i}", m)
    d = 0.18
    ob = np.zeros(int(d * SR))
    for off in (0, 0.07):                                            # obturador: 2 clics
        cl = hp(ruido(0.02), 2500) * env(0.02, 0.0003, 160)
        i = int(off * SR)
        ob[i:i + len(cl)] += cl
    guardar("tematicos", "obturador_01", ob)
    d = 1.4
    x = t(d)
    f = 650 + 350 * np.sin(2 * np.pi * 1.4 * x)
    guardar("tematicos", "sirena_01", lp(np.sin(2 * np.pi * np.cumsum(f) / SR), 3000) * np.minimum(1, x * 8) * np.minimum(1, (d - x) * 6))
    d = 1.6
    x = t(d)
    f = np.geomspace(55, 160, len(x))
    saw = 2 * ((np.cumsum(f) / SR) % 1) - 1
    guardar("tematicos", "motor_acelera_01", lp(saw + 0.2 * ruido(d), 1200) * np.minimum(1, x * 4) * np.minimum(1, (d - x) * 3))
    # batería para la música
    guardar("musica", "kick_01", kick(120, 45, 0.4, 0.25))
    guardar("musica", "kick_02", kick(105, 40, 0.5, 0.15))
    guardar("musica", "hat_cerrado_01", hat(0.06, 70))
    guardar("musica", "hat_cerrado_02", hat(0.05, 90))
    guardar("musica", "hat_abierto_01", hat(0.35, 9))
    guardar("musica", "clap_01", clap(0.22))
    guardar("musica", "clap_02", clap(0.28))
    guardar("musica", "clap_03", clap(0.18))
    d = 0.12
    guardar("musica", "shaker_01", hp(ruido(d), 4500) * np.sin(np.pi * np.clip(t(d) / d, 0, 1)) ** 2)
    d = 0.16
    guardar("musica", "shaker_02", hp(ruido(d), 3800) * np.sin(np.pi * np.clip(t(d) / d, 0, 1)) ** 3)
    guardar("musica", "perc_01", barrido(420, 260, 0.18) * env(0.18, 0.001, 22))
    n = len(list(DEST.rglob("*.wav")))
    print(f"✅ {n} sonidos creados en {DEST}")


if __name__ == "__main__":
    main()
