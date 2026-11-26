"""Prueba 27 · continuidad del barco: silueta constante y cuánto lo tapa la mano en cada instante (estado A)."""
import json, subprocess, pathlib, numpy as np
from PIL import Image
d = json.loads(pathlib.Path('datos.json').read_text()); e = d['escenas'][0]
def variante(nombre, quitar):
    v = json.loads(json.dumps(d)); v['escenas'][0]['props'] = [p for p in e['props'] if p['tipo'] not in quitar]
    pathlib.Path(f'cont/{nombre}.json').write_text(json.dumps(v)); return f'cont/{nombre}.json'
pathlib.Path('cont').mkdir(exist_ok=True)
ts = [0.16, 0.35, 0.55, 0.75, 0.95, 1.10, 1.25, 1.45, 1.80]
V = {'full': variante('full', []), 'sinmano': variante('sinmano', ['p27_mano']), 'vacio': variante('vacio', ['p27_mano', 'p27_barco'])}
for n, f in V.items():
    subprocess.run(['python3', '../cuadros.py', '/home/claude/escena/escena.html', f, f'cont/{n}'] + [str(t) for t in ts], check=True, stdout=subprocess.DEVNULL)
L = lambda n, t: np.asarray(Image.open(f'cont/{n}_{t:06.2f}.png').convert('RGB')).astype(int)
print(f"{'t (s)':>6} | {'área silueta barco (px)':>23} | {'barco tapado por la mano':>24}")
for t in ts:
    barco = np.abs(L('sinmano', t) - L('vacio', t)).sum(2) > 24
    mano = np.abs(L('full', t) - L('sinmano', t)).sum(2) > 24
    print(f"{t:6.2f} | {barco.sum():23d} | {100 * (barco & mano).sum() / max(1, barco.sum()):23.1f}%")
