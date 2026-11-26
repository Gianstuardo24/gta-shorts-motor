"""Funk movido para los Shorts de escena: bateria con groove (tus samples), bajo slap sintetizado,
clavinet a contratiempo y stabs de bronces. Dorico (el modo tipico del funk). Cada semilla cambia
tempo, tonalidad, patron de bajo y vamp.
Uso de prueba:  python musica_funk.py 30 semilla  -> funk_prueba.wav
"""
import sys, random, hashlib
import numpy as np
import musica as M
from musica import SR, poner, env, hz, tono, lowpass_rapido, leer, samples

DORICO = [0, 2, 3, 5, 7, 9, 10]
VAMPS = [[0, 3], [0, 0, 3, 3], [0, 3, 0, 4], [0, 6, 5, 3], [0, 0, 6, 3]]
# patrones de bajo: (posicion en tiempos dentro del compas, grado relativo, octava)
BAJOS = [
    [(0, 0, 0), (0.75, 0, 1), (1.5, 6, 0), (2, 0, 0), (2.75, 4, 0), (3.25, 0, 1), (3.5, 6, 0)],
    [(0, 0, 0), (0.5, 0, 0), (1.25, 0, 1), (2, 4, 0), (2.5, 6, 0), (3, 0, 0), (3.75, 0, 1)],
    [(0, 0, 0), (1, 0, 1), (1.75, 6, 0), (2.5, 0, 0), (3, 2, 0), (3.5, 4, 0)],
]


def nota(g):
    return DORICO[g % 7] + 12 * (g // 7)


def slap(f, dur, brillo):
    """Bajo slap: ataque brillante que se cierra rapido + cuerpo redondo."""
    t = np.arange(int(dur * SR)) / SR
    cuerpo = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t)
    ataque = sum((1 / k) * np.sin(2 * np.pi * f * k * t) for k in range(2, brillo)) * np.exp(-t * 28)
    x = (cuerpo * np.exp(-t * 3.5) + 0.8 * ataque) * env(len(t), 0.002, 0.03)
    return (x / max(1e-6, np.abs(x).max())).astype(np.float32)


def clav(f, dur):
    """Clavinet: muy brillante y seco."""
    t = np.arange(int(dur * SR)) / SR
    x = sum(((-1) ** k / k ** 0.8) * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (14 + 3 * k)) for k in range(1, 9))
    return (x * env(len(t), 0.001, 0.02) / 3).astype(np.float32)


def bronce(f, dur):
    """Stab de bronces: sierra suave con 'swell' corto."""
    t = np.arange(int(dur * SR)) / SR
    x = sum((1 / k) * np.sin(2 * np.pi * f * k * t * (1 + 0.0015 * np.sin(2 * np.pi * 5.5 * t))) for k in range(1, 7))
    e = np.minimum(1, t / 0.03) * np.exp(-np.maximum(0, t - 0.05) * 6)
    return (x * e * env(len(t), 0.0, 0.04) / 2).astype(np.float32)


def generar(duracion, semilla, bpm=None):
    rnd = random.Random(int(hashlib.md5(("funk" + str(semilla)).encode()).hexdigest(), 16))
    bpm = bpm or rnd.choice([108, 110, 112, 114, 116])
    beat = 60 / bpm
    compas = 4 * beat
    swing = rnd.choice([0.04, 0.06, 0.08])
    tonica = rnd.choice(["E", "F", "G", "A", "D"])
    raiz = 24 + M.NOTAS[tonica]                       # MIDI de la tonica grave
    vamp = rnd.choice(VAMPS)
    patron = rnd.choice(BAJOS)

    kick = leer(rnd.choice(samples("kick")))
    clap = leer(rnd.choice(samples("clap")))
    hat = leer(rnd.choice(samples("hat_cerrado")))
    hat_a = leer(samples("hat_abierto")[0])
    perc = leer(samples("perc")[0])

    n = int((duracion + compas) * SR)
    bat, bajo, arm, top = (np.zeros(n, dtype=np.float32) for _ in range(4))

    def t16(t0, pos):                                 # swing en las semicorcheas pares
        frac = (pos * 4) % 2
        return t0 + pos * beat + (swing * beat if abs(frac - 1) < 1e-6 else 0)

    for c in range(int(duracion / compas) + 1):
        t0 = c * compas
        intro = c == 0
        grado = vamp[c % len(vamp)]
        relleno = c % 4 == 3
        # BATERIA: kick sincopado, clap en 2 y 4 con ghost notes, hats en semicorcheas
        for p in ((0, 1.75, 2.5) if not relleno else (0, 1.75, 2.5, 3.25)):
            poner(bat, kick, t16(t0, p), 0.95)
        if not intro:
            for p in (1, 3):
                poner(bat, clap, t16(t0, p), 0.55)
            for p in (1.75, 3.5):
                poner(bat, clap, t16(t0, p), 0.12)    # ghost
        for k in range(16):
            p = k / 4
            acento = 0.3 if k % 2 == 0 else 0.14
            if p == 3.5 and not intro:
                poner(bat, hat_a, t16(t0, p), 0.28)
            else:
                poner(bat, hat, t16(t0, p), acento * (0.6 if intro else 1))
        if relleno:
            poner(bat, perc, t16(t0, 3.75), 0.3)
        # BAJO slap
        for pos, gr, octv in patron:
            f = hz(raiz + nota(grado + gr) + 12 * octv)
            largo = beat * (0.45 if octv else 0.6)
            poner(bajo, slap(f, largo, 9 if octv else 6), t16(t0, pos), 0.8 if octv else 0.95)
        if intro:
            continue
        # CLAVINET: acorde m7 a contratiempo (16avos)
        acorde = [nota(grado), nota(grado + 2), nota(grado + 4), nota(grado + 6)]
        for pos in rnd.choice([(0.5, 1.25, 2.5, 3.75), (0.75, 1.5, 2.75, 3.5), (0.5, 1.5, 2.25, 3.25)]):
            st = sum(clav(hz(raiz + 36 + i), beat * 0.3) for i in acorde[1:]) / 3
            poner(arm, st, t16(t0, pos), 0.42)
        # BRONCES: stab cada 2 compases (y respuesta en el relleno)
        if c % 2 == 1:
            st = sum(bronce(hz(raiz + 36 + i), beat * 0.6) for i in acorde[:3]) / 3
            poner(top, st, t16(t0, 0), 0.35)
            poner(top, st, t16(t0, 0.75), 0.28)
        if relleno:
            arriba = sum(bronce(hz(raiz + 36 + i), beat * 0.9) for i in [nota(grado + 1), nota(grado + 3), nota(grado + 5)]) / 3
            poner(top, arriba, t16(t0, 3), 0.3)
        # colchon suave para que no quede seco
        pad = sum(tono(hz(raiz + 24 + i) * (1 + d), compas, ((1, 1.0), (2, 0.2))) for i in acorde[:3] for d in (-0.003, 0.003)) / 6
        poner(arm, (pad * env(len(pad), 0.3, 0.4, 0.7)).astype(np.float32), t0, 0.12)

    top = lowpass_rapido(top, 4500)
    mezcla = bat * 0.85 + bajo * 0.9 + arm * 0.55 + top * 0.5
    mezcla = mezcla[:int(duracion * SR)]
    nf = int(min(1.5, duracion / 4) * SR)
    mezcla[-nf:] *= np.linspace(1, 0, nf)
    mezcla /= max(1e-6, np.abs(mezcla).max()) / 0.7
    info = {"estilo": "funk", "bpm": bpm, "tono": f"{tonica} dorico", "vamp": vamp}
    return mezcla.astype(np.float32), info


if __name__ == "__main__":
    dur = float(sys.argv[1]) if len(sys.argv) > 1 else 30
    sem = sys.argv[2] if len(sys.argv) > 2 else "prueba"
    x, info = generar(dur, sem)
    print(info, "->", M.guardar(x, "funk_prueba.wav"))
