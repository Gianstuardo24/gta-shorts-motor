"""Reajusta los tiempos numericos de una escena 'pelicula' (desde '0') cuando cambia la voz.
Cada tiempo se mueve junto con la frase en que cae. Uso: python ajustar_tiempos.py guion_viejo pal_viejas guion_nuevo pal_nuevas"""
import sys, json
gv, pv, gn, pn = sys.argv[1:5]
def inicios(g, pal):
    out, idx = [], 0
    for f in g["frases"]:
        out.append(pal[idx]["i"]); idx += len(f.split())
    return out
G0, G1 = json.load(open(gv)), json.load(open(gn))
a0, a1 = inicios(G0, json.load(open(pv))), inicios(G1, json.load(open(pn)))
def mover(v):
    i = max([j for j in range(len(a0)) if a0[j] <= v] or [0])
    if i >= len(a1): i = len(a1) - 1
    return round(v - a0[i] + a1[i], 3)
def fix(o):
    if isinstance(o, dict):
        for kk in ("k", "fin", "desde", "hasta"):
            v = o.get(kk)
            if isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0.05: o[kk] = mover(v)
        for v in o.values(): fix(v)
    elif isinstance(o, list):
        for v in o: fix(v)
for e in G1["escena"]["escenas"]:
    if e.get("tipo") == "pelicula" and e.get("desde") == "0": fix(e)
json.dump(G1, open(gn, "w"), ensure_ascii=False, indent=1)
print("ok", [round(x - y, 2) for x, y in zip(a1, a0)])
