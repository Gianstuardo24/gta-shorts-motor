"""Prueba 27 · detector de saltos: revisa TODOS los cuadros de un mp4 y marca cuadros aislados que no se parecen ni al anterior ni al siguiente."""
import sys, subprocess, numpy as np
f = sys.argv[1]; W, H = 108, 192
raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(int)
d = [np.abs(fr[i] - fr[i - 1]).mean() for i in range(1, len(fr))]
print(f'{len(fr)} cuadros · diferencia media entre cuadros: {np.mean(d):.2f} · máxima: {max(d):.2f}')
malos = [i for i in range(1, len(fr) - 1) if d[i - 1] > 12 and d[i] > 12 and np.abs(fr[i + 1] - fr[i - 1]).mean() < min(d[i - 1], d[i]) * .8]
print('cuadros aislados (glitch):', [f'{i} ({i/30:.3f}s)' for i in malos] or 'ninguno')
cortes = [f'{i/30:.3f}s' for i in range(1, len(fr)) if d[i - 1] > 12 and (i - 1) not in malos and i not in malos]
print('cambios bruscos (cortes legítimos):', cortes or 'ninguno')
