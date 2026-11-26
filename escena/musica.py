"""Generador de pistas de fondo: house / electronica distinta para cada Short.

Bateria = tus samples (sonidos/musica/), bajo y acordes = sintetizados aqui.
Cada video tiene su "semilla": cambia tempo, tonalidad, progresion, patron y samples.
Uso de prueba:  python musica.py 30 semilla [house|synth]   -> musica_prueba.wav
"""
import sys, wave, random, hashlib
from pathlib import Path
import numpy as np

SR = 48000
CARPETA = Path("sonidos/musica")
NOTAS = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
# progresiones en grados de escala menor natural (0=i): estilo house/synthwave
PROGRESIONES = [[0, 5, 2, 6], [0, 6, 5, 6], [0, 3, 5, 4], [0, 5, 3, 4], [0, 2, 5, 6]]
MENOR = [0, 2, 3, 5, 7, 8, 10]
PROG_HOUSE = [[0, 0, 3, 4], [0, 4, 3, 4]]   # i, iv, v menores: "maleante" y "energica" (las que gustaron)


def leer(p):
    with wave.open(str(p)) as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
        x = np.frombuffer(w.readframes(n), dtype=np.int16 if sw == 2 else np.int32).astype(np.float32)
        x /= 32768.0 if sw == 2 else 2147483648.0
        return x.reshape(-1, ch).mean(axis=1) if ch > 1 else x


def samples(tipo):
    return sorted(CARPETA.glob(f"{tipo}_*.wav"))


def poner(pista, s, t, ganancia=1.0):
    i = int(t * SR)
    if i >= len(pista):
        return
    f = min(len(pista), i + len(s))
    pista[i:f] += s[:f - i] * ganancia


def lowpass(x, corte):
    """Filtro pasa-bajos de un polo (suave, barato)."""
    a = np.exp(-2 * np.pi * corte / SR)
    y = np.empty_like(x)
    acc = 0.0
    for k in range(0, len(x), 4096):          # por bloques para no ser lento
        bloque = x[k:k + 4096]
        out = np.empty_like(bloque)
        for j, v in enumerate(bloque):
            acc = (1 - a) * v + a * acc
            out[j] = acc
        y[k:k + 4096] = out
    return y


def lowpass_rapido(x, corte):
    # aproximacion vectorizada: media movil (suficiente para pads/bajo de fondo)
    n = max(1, int(SR / corte / 2))
    k = np.ones(n, dtype=np.float32) / n
    return np.convolve(x, k, mode="same")


def saw(f, dur, detune=0.0):
    t = np.arange(int(dur * SR)) / SR
    ff = f * (1 + detune)
    return 2 * (t * ff - np.floor(0.5 + t * ff))


def tono(f, dur, armonicos=((1, 1.0),)):
    """Tono limpio por suma de armonicos (sin aliasing): suena 'caro', no a juguete."""
    t = np.arange(int(dur * SR)) / SR
    x = sum(a * np.sin(2 * np.pi * f * k * t) for k, a in armonicos)
    return (x / sum(a for _, a in armonicos)).astype(np.float32)


def env(n, a=0.005, r=0.08, sustain=1.0):
    e = np.ones(n, dtype=np.float32) * sustain
    na, nr = int(a * SR), int(r * SR)
    if na:
        e[:na] = np.linspace(0, sustain, na)
    if nr and nr < n:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


def hz(nota_midi):
    return 440.0 * 2 ** ((nota_midi - 69) / 12)


ESTILOS_NUEVOS = ("deep", "tech", "piano", "dark")
PROG_PIANO = [[0, 5, 2, 6], [5, 6, 0, 0], [0, 3, 6, 5], [5, 3, 0, 4]]
PROG_DARK = [[0, 0, 5, 4], [0, 1, 0, 6], [0, 5, 6, 4]]


def piano(f, dur):
    """Piano sintetico: armonicos levemente inarmonicos que decaen (los agudos se apagan antes)."""
    t = np.arange(int(dur * SR)) / SR
    x = np.zeros(len(t), dtype=np.float64)
    for k in range(1, 9):
        fk = f * k * np.sqrt(1 + 0.0004 * k * k)
        if fk > SR / 2.4:
            break
        x += (1 / k ** 1.4) * np.sin(2 * np.pi * fk * t) * np.exp(-t * (2.2 + 1.3 * k))
    x *= env(len(x), 0.003, 0.05)
    return (x / max(1e-6, np.abs(x).max())).astype(np.float32)


def pluck(f, dur, brillo=6):
    t = np.arange(int(dur * SR)) / SR
    x = sum((1 / k) * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (9 + 5 * k)) for k in range(1, brillo + 1))
    x = x * env(len(x), 0.002, 0.03)
    return (x / max(1e-6, np.abs(x).max())).astype(np.float32)


def acorde7(grado):
    """Notas (semitonos sobre la tonica) del acorde de septima del grado en la escala menor."""
    return [MENOR[g % 7] + 12 * (g // 7) for g in (grado, grado + 2, grado + 4, grado + 6)]


def _house(duracion, rnd, estilo):
    """House moderno en 4 sabores: deep (calido), tech (bajo rodante), piano (acordes de piano), dark (misterio)."""
    bpm = {"deep": rnd.choice([120, 121, 122]), "tech": rnd.choice([125, 126, 127]),
           "piano": rnd.choice([122, 123, 124]), "dark": rnd.choice([96, 100, 104])}[estilo]
    tonica = rnd.choice(list(NOTAS))
    raiz = 26 + NOTAS[tonica] if NOTAS[tonica] < 6 else 14 + NOTAS[tonica]   # bajo entre D1 y C#2
    prog = rnd.choice(PROG_PIANO if estilo == "piano" else PROG_DARK if estilo == "dark" else PROG_HOUSE + [[0, 5, 3, 4]])
    beat = 60 / bpm
    compas = 4 * beat
    n = int((duracion + 1) * SR)
    bat, bajo, arm, top = (np.zeros(n, dtype=np.float32) for _ in range(4))
    kick = leer(rnd.choice(samples("kick")))
    clap = leer(rnd.choice(samples("clap")))
    hat_c = leer(rnd.choice(samples("hat_cerrado")))
    hat_a = leer(rnd.choice(samples("hat_abierto")))
    shaker = leer(rnd.choice(samples("shaker")))
    perc = leer(rnd.choice(samples("perc")))
    swing = rnd.choice([0.0, 0.025, 0.04])
    patron_piano = rnd.choice([[0, 0.75, 1.5, 2.5, 3.0], [0, 1.5, 2.0, 3.5], [0.5, 1.5, 2.25, 3.0, 3.5]])
    arp = rnd.choice([[0, 2, 4, 2], [0, 4, 2, 4], [0, 2, 4, 7]])
    compases = int(np.ceil(duracion / compas)) + 1
    for c in range(compases):
        t0 = c * compas
        intro = c == 0
        grado = prog[c % len(prog)]
        nota = raiz + MENOR[grado % 7]
        relleno = c % 4 == 3                                # cada 4 compases un remate
        for b in range(4):
            tb = t0 + b * beat
            if estilo != "dark" or b in (0, 2) or (b == 3 and relleno):
                poner(bat, kick, tb, 0.95 if estilo != "dark" else 0.85)
            if not intro and (b in (1, 3) if estilo != "dark" else b == 2):
                poner(bat, clap, tb, 0.5 if estilo != "dark" else 0.3)
            off = tb + beat / 2 + swing * beat
            poner(bat, shaker if estilo == "dark" else hat_a, off, (0.33 if not intro else 0.18) * (0.5 if estilo == "dark" else 1))
            pasos = range(4) if estilo == "tech" else () if estilo == "dark" else (0, 1, 3)
            for s16 in pasos:
                poner(bat, hat_c, tb + s16 * beat / 4 + (swing * beat if s16 % 2 else 0), 0.14 + 0.1 * (s16 == 0))
            if not intro and (estilo == "tech" and b == 2 or relleno and b == 3):
                poner(bat, perc, tb + beat * 0.75, 0.32)
            if intro:
                continue
            # bajo
            if estilo == "tech":                             # rodante: 3 semicorcheas por tiempo, sin pisar el kick
                for s16 in (1, 2, 3):
                    d = beat * 0.2
                    s_ = np.tanh(tono(hz(nota), d, ((1, 1.0), (2, 0.5), (3, 0.25))) * 2.0) * env(int(d * SR), 0.003, 0.04)
                    poner(bajo, s_.astype(np.float32), tb + s16 * beat / 4, 0.55 + 0.15 * (s16 == 2))
            elif estilo == "dark":                           # sub largo y saturado, respira con el kick
                d = beat * 0.9
                s_ = np.tanh(tono(hz(nota), d, ((1, 1.0), (2, 0.35), (3, 0.12))) * 1.8) * env(int(d * SR), 0.05, 0.2)
                poner(bajo, s_.astype(np.float32), tb + beat * 0.1, 0.9)
            else:                                            # deep / piano: contratiempo clasico (+ octava a veces)
                oct_ = 12 if (estilo == "piano" and b == 3 and c % 2) else 0
                d = beat * 0.42
                s_ = np.tanh(tono(hz(nota + oct_), d, ((1, 1.0), (2, 0.45), (3, 0.18))) * 1.6) / np.tanh(1.6)
                poner(bajo, (s_ * env(len(s_), 0.006, 0.07)).astype(np.float32), tb + beat / 2, 0.75)
        if intro:
            continue
        notas = acorde7(grado)
        if estilo == "piano":                                # acordes de piano ritmicos (piano house)
            for pos in patron_piano:
                d = beat * 1.1
                st = sum(piano(hz(raiz + 36 + i), d) for i in notas) / 3
                poner(arm, st, t0 + pos * beat, 0.42)
        elif estilo == "deep":                               # stabs calidos + colchon suave
            for pos in ((1.5, 3.5) if c % 2 == 0 else (1.5, 2.75, 3.5)):
                d = beat * 0.34
                st = sum(tono(hz(raiz + 36 + i) * (1 + dd), d, ((1, 1.0), (2, 0.25), (3, 0.08)))
                         for i in notas for dd in (-0.002, 0.002)) / 8
                poner(arm, (st * env(len(st), 0.008, 0.12)).astype(np.float32), t0 + pos * beat, 0.34)
            pad = sum(tono(hz(raiz + 36 + i) * (1 + dd), compas, ((1, 1.0), (2, 0.2))) for i in notas[:3] for dd in (-0.003, 0.003)) / 6
            poner(arm, (pad * env(len(pad), 0.4, 0.5, 0.7)).astype(np.float32), t0, 0.12)
        elif estilo == "tech":                               # un pluck seco por compas (minimal)
            for pos in ((0.5,) if c % 2 else (0.5, 2.75)):
                poner(arm, pluck(hz(raiz + 36 + notas[0]), beat * 0.6, 4), t0 + pos * beat, 0.32)
                poner(arm, pluck(hz(raiz + 36 + notas[2]), beat * 0.6, 4), t0 + pos * beat, 0.22)
        else:                                                # dark: misterio. Dron grave + pulsos graves sueltos, nada brillante
            for pos in ((0, 1.5) if c % 2 == 0 else (0.75, 2.5)):        # notas graves, sueltas, con cola larga
                i = notas[rnd.choice([0, 0, 2, 1])]
                poner(top, pluck(hz(raiz + 24 + i), beat * 1.6, 2), t0 + pos * beat, 0.3)
            if c % 4 == 2:                                                # tension: semitono arriba (frigio)
                poner(top, pluck(hz(raiz + 25), beat * 2.0, 2), t0 + 3 * beat, 0.25)
            pad = sum(tono(hz(raiz + 12 + i) * (1 + dd), compas, ((1, 1.0), (2, 0.15))) for i in notas[:2] for dd in (-0.004, 0.004)) / 4
            poner(arm, (pad * env(len(pad), 0.8, 0.8, 0.9)).astype(np.float32), t0, 0.35)
    if estilo == "dark":
        top = lowpass_rapido(top, 1800)
        arm = lowpass_rapido(arm, 1500)
        bat = bat * 0.8
    mezcla = bat * 0.85 + bajo * 0.95 + arm * 0.6 + top * 0.5
    info = {"estilo": estilo, "bpm": bpm, "tono": f"{tonica} menor", "progresion": prog}
    return mezcla, info


def generar(duracion, semilla, estilo=None):
    rnd = random.Random(int(hashlib.md5(str(semilla).encode()).hexdigest(), 16))
    estilo = estilo or rnd.choice(["deep", "tech"])
    if estilo in ESTILOS_NUEVOS:
        mezcla, info = _house(duracion, rnd, estilo)
        mezcla = mezcla[:int(duracion * SR)]
        nf = int(min(1.5, duracion / 4) * SR)
        mezcla[-nf:] *= np.linspace(1, 0, nf)
        mezcla /= max(1e-6, np.abs(mezcla).max()) / 0.7
        return mezcla.astype(np.float32), info
    bpm = rnd.choice([124, 126]) if estilo == "house" else rnd.choice([100, 104, 108])
    tonica = rnd.choice(list(NOTAS))
    raiz = 24 + NOTAS[tonica]                      # bajo en octava 1 (sub-bajo)
    prog = rnd.choice(PROG_HOUSE if estilo == "house" else PROGRESIONES)
    beat = 60 / bpm
    compas = 4 * beat
    n = int((duracion + 1) * SR)
    bat = np.zeros(n, dtype=np.float32)
    bajo = np.zeros(n, dtype=np.float32)
    pad = np.zeros(n, dtype=np.float32)

    kick = leer(rnd.choice(samples("kick")))
    clap = leer(rnd.choice(samples("clap")))
    hat_c = leer(rnd.choice(samples("hat_cerrado")))
    hat_a = leer(rnd.choice(samples("hat_abierto")))
    shaker = leer(rnd.choice(samples("shaker")))
    perc = leer(rnd.choice(samples("perc")))
    swing = rnd.choice([0.0, 0.02, 0.035])
    usa_perc = rnd.random() < 0.6

    compases = int(np.ceil(duracion / compas)) + 1
    for c in range(compases):
        t0 = c * compas
        intro = c == 0
        grado = prog[c % len(prog)]
        nota = raiz + MENOR[grado]
        for b in range(4):
            tb = t0 + b * beat
            if estilo == "house" or b in (0, 2):
                poner(bat, kick, tb, 0.9)
            if not intro and b in (1, 3) and (estilo == "house" or b == 3 or b == 1):
                poner(bat, clap, tb, 0.55)
            # contratiempo: hat abierto (house) / shaker
            poner(bat, hat_a if estilo == "house" else shaker, tb + beat / 2 + swing * beat, 0.35 if not intro else 0.2)
            for s16 in range(4):   # semicorcheas de hat cerrado con dinamica
                if s16 == 2:
                    continue
                poner(bat, hat_c, tb + s16 * beat / 4 + (swing * beat if s16 % 2 else 0), 0.18 + 0.1 * (s16 == 0))
            if usa_perc and not intro and b == 3 and c % 2:
                poner(bat, perc, tb + beat * 0.75, 0.3)
            # bajo: contratiempo (house) o corcheas (synth)
            if not intro:
                golpes = [beat / 2] if estilo == "house" else [0, beat / 2]
                for g in golpes:
                    d = beat * 0.45
                    # sub limpio + armonicos suaves para que se escuche en el celular
                    s = tono(hz(nota), d, ((1, 1.0), (2, 0.45), (3, 0.18), (4, 0.08)))
                    s = np.tanh(s * 1.6) / np.tanh(1.6)           # saturacion leve: mas cuerpo
                    s = s * env(len(s), 0.006, 0.07)
                    poner(bajo, s.astype(np.float32), tb + g, 0.75)
        # HOUSE: stabs cortos de acorde menor con septima, a contratiempo (deep house)
        if not intro and estilo == "house":
            grados = [grado, grado + 2, grado + 4, grado + 6]
            notas = [MENOR[g % 7] + 12 * (g // 7) for g in grados]
            for tt in (t0 + beat * 1.5, t0 + beat * 3.5) if c % 2 == 0 else (t0 + beat * 1.5, t0 + beat * 2.75, t0 + beat * 3.5):
                d = beat * 0.32
                st = sum(tono(hz(raiz + 24 + i) * (1 + dd), d, ((1, 1.0), (2, 0.25), (3, 0.08)))
                         for i in notas for dd in (-0.002, 0.002)) / 8
                poner(pad, (st * env(len(st), 0.008, 0.12)).astype(np.float32), tt, 0.32)
        # SYNTH: acorde sostenido del compas (pad de ambiente)
        if not intro and estilo != "house":
            acorde = [MENOR[grado % 7], MENOR[(grado + 2) % 7] + 12 * ((grado + 2) // 7), MENOR[(grado + 4) % 7] + 12 * ((grado + 4) // 7)]
            # acordes calidos: pocos armonicos, una octava mas abajo, ataque lento (pad oscuro)
            voz = sum(tono(hz(raiz + 36 + i) * (1 + d), compas, ((1, 1.0), (2, 0.3), (3, 0.12)))
                      for i in acorde for d in (-0.003, 0.003)) / 6
            voz = (voz * env(len(voz), 0.35, 0.5, 0.8)).astype(np.float32)
            poner(pad, voz, t0, 0.3)

    mezcla = bat * 0.85 + bajo * 0.95 + pad * 0.5
    mezcla = mezcla[:int(duracion * SR)]
    # salida suave al final (coincide con el cierre del logo)
    nf = int(min(1.5, duracion / 4) * SR)
    mezcla[-nf:] *= np.linspace(1, 0, nf)
    mezcla /= max(1e-6, np.abs(mezcla).max()) / 0.7
    info = {"estilo": estilo, "bpm": bpm, "tono": f"{tonica} menor", "progresion": prog}
    return mezcla.astype(np.float32), info


def guardar(x, ruta):
    s = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(ruta), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(s.tobytes())
    return ruta


if __name__ == "__main__":
    dur = float(sys.argv[1]) if len(sys.argv) > 1 else 30
    sem = sys.argv[2] if len(sys.argv) > 2 else "prueba"
    est = sys.argv[3] if len(sys.argv) > 3 else None
    x, info = generar(dur, sem, est)
    print(info, "->", guardar(x, "musica_prueba.wav"))
