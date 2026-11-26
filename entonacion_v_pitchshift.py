"""Sube la entonacion al final de las preguntas (Kokoro las dice planas).
Corta la cola de la frase en tramos y sube cada tramo un poco mas (glide), unidos con fundidos cortos."""
import numpy as np, librosa


def subir_final(a, sr, semitonos=4.0, cola=0.4, tramos=4, xf=0.012):
    a = a.astype(np.float32)
    voz = np.nonzero(np.abs(a) > 0.02 * np.abs(a).max())[0]
    fin = int(voz[-1]) + 1 if len(voz) else len(a)
    ini = max(0, fin - int(cola * sr))
    out = a.copy()
    lim = np.linspace(ini, fin, tramos + 1).astype(int)
    nx = int(xf * sr)
    for i in range(tramos):
        a0, a1 = max(0, lim[i] - nx), min(len(a), lim[i + 1] + nx)
        st = semitonos * (i + 1) / tramos
        seg = librosa.effects.pitch_shift(a[a0:a1], sr=sr, n_steps=st, n_fft=512, hop_length=128)
        w = np.ones(a1 - a0, np.float32)
        w[:nx] = np.linspace(0, 1, nx)
        if i < tramos - 1:
            w[-nx:] = np.linspace(1, 0, nx)
        out[a0:a1] = out[a0:a1] * (1 - w) + seg * w
    out[fin:] = a[fin:]
    return out
