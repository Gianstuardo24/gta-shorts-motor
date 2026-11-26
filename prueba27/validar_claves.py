"""Prueba 27 · valida que TODA clave de tiempo usada en los datos exista en T (el motor resuelve en silencio una clave
desconocida como el inicio de la escena: así se produjo el error del plano 05 v1).
Uso: python3 validar_claves.py datos.json [más.json]   → sale con código 1 si hay claves sin resolver."""
import json, re, sys
CAMPOS = {"k", "fin", "abre", "desde", "hasta_k", "resalta", "centro"}          # campos que el motor pasa por tk()
LISTAS = {"scroll", "cursor", "clics", "suelta", "cae", "dim", "negro", "despl"}  # listas cuyos extremos de tiempo pasan por tk()
def claves(obj, ruta=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            r = f"{ruta}.{k}"
            if k in CAMPOS and isinstance(v, str): yield r, v
            elif k in LISTAS and isinstance(v, list):
                for i, x in enumerate(v[:2] if k in {"dim", "negro", "despl"} else v):
                    if isinstance(x, str): yield f"{r}[{i}]", x
            elif k == "curMov" and isinstance(v, list):
                for i, x in enumerate(v):
                    if isinstance(x, list) and x and isinstance(x[0], str): yield f"{r}[{i}][0]", x[0]
            else: yield from claves(v, r)
    elif isinstance(obj, list):
        for i, x in enumerate(obj): yield from claves(x, f"{ruta}[{i}]")
mal = 0
for f in sys.argv[1:]:
    d = json.load(open(f)); T = d.get("T", {}); n = 0; errores = []
    for ruta, v in claves(d.get("escenas", [])):
        if ruta.endswith(".desde") and v == "0": continue           # "desde":"0" es el inicio de la escena por diseño
        n += 1; m = re.match(r"^(.+?)([+-][0-9.]+)$", v); base = m.group(1) if m else v
        if v not in T and base not in T: errores.append(f"   ✗ {ruta} = '{v}' (no existe '{base}' en T; el motor usaría el inicio de la escena)")
    print(f"{f}: {n} claves de tiempo revisadas · {'OK' if not errores else str(len(errores)) + ' SIN RESOLVER'}"); print("\n".join(errores)) if errores else None
    mal += len(errores)
sys.exit(1 if mal else 0)
