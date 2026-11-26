"""Voz mas joven: sube el tono y corre un poco los formantes (WORLD). La duracion no cambia,
asi los tiempos de las palabras siguen sirviendo. Uso: python joven.py entrada.wav salida.wav [semitonos] [formante]"""
import sys
import numpy as np
import soundfile as sf
import pyworld as pw

ent, sal = sys.argv[1], sys.argv[2]
st = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
fm = float(sys.argv[4]) if len(sys.argv) > 4 else 1.06
a, sr = sf.read(ent)
if a.ndim > 1:
    a = a.mean(axis=1)
x = a.astype(np.float64)
f0, t = pw.harvest(x, sr, frame_period=5.0)
sp = pw.cheaptrick(x, f0, t, sr)
ap = pw.d4c(x, f0, t, sr)
n = sp.shape[1]
idx = np.clip(np.arange(n) / fm, 0, n - 1)
lo = np.floor(idx).astype(int); hi = np.minimum(lo + 1, n - 1); w = idx - lo
sp2 = np.ascontiguousarray(sp[:, lo] * (1 - w) + sp[:, hi] * w)
y = pw.synthesize(f0 * 2 ** (st / 12), sp2, ap, sr, frame_period=5.0)[:len(x)]
if len(y) < len(x):
    y = np.pad(y, (0, len(x) - len(y)))
y = y / max(1e-9, np.abs(y).max()) * min(0.98, np.abs(x).max() * 1.0)
sf.write(sal, y.astype(np.float32), sr)
print("ok", sal)
