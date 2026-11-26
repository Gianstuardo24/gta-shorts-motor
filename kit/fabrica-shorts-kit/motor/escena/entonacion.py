"""Sube la entonacion al final de las preguntas (Kokoro las dice planas).
Usa WORLD (pyworld): cambia solo el tono (F0) y conserva el timbre, asi no suena a voz de helio.
Si pyworld no esta instalado, deja la frase tal cual."""
import numpy as np


def subir_final(a, sr, semitonos=4.0, cola=0.45, *_):
    try:
        import pyworld as pw
    except ImportError:
        return a
    x = a.astype(np.float64)
    f0, t = pw.harvest(x, sr, frame_period=5.0)
    sp = pw.cheaptrick(x, f0, t, sr)
    ap = pw.d4c(x, f0, t, sr)
    voz = np.nonzero(f0 > 0)[0]
    if len(voz) < 10:
        return a
    fin = t[voz[-1]]
    ini = fin - cola
    # rampa suave (curva) desde 'ini' hasta el final: sube 'semitonos'
    r = np.clip((t - ini) / cola, 0, 1) ** 1.6
    f0n = f0 * (2 ** (semitonos * r / 12))
    y = pw.synthesize(f0n, sp, ap, sr, frame_period=5.0)[:len(x)]
    if len(y) < len(x):
        y = np.pad(y, (0, len(x) - len(y)))
    # solo se reemplaza la parte final (lo demas queda con la voz original, sin pasar por el vocoder)
    i0 = max(0, int((ini - 0.08) * sr))
    w = np.clip((np.arange(len(x)) - i0) / (0.06 * sr), 0, 1)
    out = x * (1 - w) + y * w
    return out.astype(np.float32)
