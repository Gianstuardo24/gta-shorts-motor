"""Convierte claves 'momento+seg' (ej. 'duck+0.4', 's_in-0.2') en segundos absolutos usando T de datos.json.
Uso: python3 resolver.py guion_src.json datos.json guion_final.json
Solo toca escenas 'pelicula' con desde "0" (inicio = 0 s)."""
import json, re, sys

src, dat, out = sys.argv[1:4]
g = json.load(open(src))
T = json.load(open(dat))["T"]
PAT = re.compile(r"^([A-Za-z_]\w*)([+-]\d+(?:\.\d+)?)$")
CLAVES = {"k", "fin", "hasta", "desde"}
faltan = []


def res(v):
    if isinstance(v, str):
        m = PAT.match(v)
        if m:
            n, off = m.group(1), float(m.group(2))
            if n not in T:
                faltan.append(n)
                return v
            return round(T[n] + off, 2)
    return v


def walk(o, top=False):
    if isinstance(o, dict):
        for k, v in list(o.items()):
            if k in CLAVES and not top:
                o[k] = res(v)
            else:
                walk(v)
    elif isinstance(o, list):
        for x in o:
            walk(x)


for e in g["escena"]["escenas"]:
    if e.get("tipo") == "pelicula":
        assert str(e.get("desde")) == "0", "pelicula debe empezar en 0"
        walk(e, top=True)
json.dump(g, open(out, "w"), ensure_ascii=False)
if faltan:
    print("FALTAN momentos:", sorted(set(faltan)))
    sys.exit(1)
print("ok", out, "dur", round(T["fin"], 2))
