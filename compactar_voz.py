"""Quita silencios largos y acelera la voz. Uso: python3 compactar_voz.py orig.wav orig_palabras.json frases.json vel out.wav out_palabras.json
- entre oraciones deja maximo 0.20 s; dentro de una oracion (comas) maximo 0.28 s
- luego acelera con atempo=vel (mismo tono)"""
import json, sys, subprocess, numpy as np, soundfile as sf
wi, pi, fj, vel, wo, po = sys.argv[1:7]; vel = float(vel)
x, sr = sf.read(wi); P = json.load(open(pi)); F = json.load(open(fj))
fin_oracion = set(); n = 0
for f in F:
    n += len(f.split()); fin_oracion.add(n - 1)
assert n == len(P), (n, len(P))
cortes = []                       # (ini, fin) en segundos a quitar
for j in range(len(P) - 1):
    a, b = P[j]["f"], P[j + 1]["i"]; gap = b - a
    keep = 0.20 if j in fin_oracion else 0.28
    if gap > keep + 0.05:
        q = gap - keep                                   # cuanto sacar, centrado en el silencio
        c0 = a + (gap - q) / 2; cortes.append((c0, c0 + q))
fade = int(0.012 * sr); partes = []; pos = 0
for c0, c1 in cortes:
    i0, i1 = int(c0 * sr), int(c1 * sr)
    seg = x[pos:i0].copy()
    if len(seg) > 2 * fade:
        seg[-fade:] *= np.linspace(1, 0, fade)[:, None] if seg.ndim > 1 else np.linspace(1, 0, fade)
        if pos > 0: seg[:fade] *= np.linspace(0, 1, fade)[:, None] if seg.ndim > 1 else np.linspace(0, 1, fade)
    partes.append(seg); pos = i1
partes.append(x[pos:]); y = np.concatenate(partes)
sf.write("/tmp/_voz_comp.wav", y, sr)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/_voz_comp.wav", "-filter:a", f"atempo={vel}", wo], check=True)
def nuevo(t):
    r = sum(min(c1, t) - c0 for c0, c1 in cortes if c0 < t)
    return round((t - r) / vel, 3)
for w in P: w["i"], w["f"] = nuevo(w["i"]), nuevo(w["f"])
json.dump(P, open(po, "w"), ensure_ascii=False)
print(f"cortes {len(cortes)}  quitado {sum(c1-c0 for c0,c1 in cortes):.1f}s  dur final {len(y)/sr/vel:.1f}s")
