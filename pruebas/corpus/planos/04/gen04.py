"""Prueba 27 · plano 04 · arma datos.json (escena aislada, sin planificador ni formato.py).
Línea (GTA EN 14h, línea 3): "This January, fans digging through its files found a boat texture nobody had seen."
"""
import json, sys, pathlib
sys.path.insert(0, "/home/claude/escena")
from armar_escena import alinear, bloques

AQUI = pathlib.Path(__file__).parent
LEAD = 0.15
frase = "This January, fans digging through its files found a boat texture nobody had seen."
pal = json.loads((AQUI / "vz_palabras.json").read_text())
pal = [dict(p, i=p["i"] + LEAD, f=p["f"] + LEAD) for p in pal]
FIN = round(pal[-1]["f"] + 0.35, 2)
tok, tie = alinear([frase], pal)
fr = bloques([frase], tok, tie, FIN)
cuando = lambda w: next(p["i"] for p in pal if p["w"].lower().startswith(w.lower()))
T = {"fin": FIN, "p27_ini": cuando("This"), "p27_found": cuando("found"), "p27_boat": cuando("boat"),
     "p27_tex": cuando("texture"), "p27_nob": cuando("nobody")}

L = 100000
PANT = {"x0": -56, "x1": 1136, "y0": 496, "y1": 1250}          # vidrio del monitor (coordenadas de pantalla)
COLS, TOP, FILA, R, CL = [330, 580, 830], 700, 250, 14, 1        # 3 columnas; fila 14, columna del medio = miniatura clave
CLAVE = R * len(COLS) + CL                                        # índice 43 → tex_0412
CY = 960                                                          # centro final de la miniatura clave (storyboard: y≈980)
GRILLA = {"pantalla": PANT, "cols": COLS, "y0": TOP, "fila": FILA, "tw": 220, "th": 170, "clave": CLAVE, "num0": 412 - CLAVE,
          "dist": TOP + R * FILA - CY, "scroll": ["p27_ini", "p27_found+0.10"], "cursor": ["p27_found", "p27_boat"],
          "resalta": "p27_boat", "clics": ["p27_tex", "p27_tex+0.17"], "cur0": [860, 800], "cur1": [600, 985]}
props = [
    dict({"tipo": "p27_grilla", "x": L, "y": 0, "k": -1, "z": 1000}, **GRILLA),
    {"tipo": "p27_manoPOV", "x": L + 640, "y": 1570, "s": 1.0, "k": -1, "capa": True, "grilla": GRILLA, "mueve": [-24, 18]},
    {"tipo": "p27_mesa04", "x": L, "y": 0, "k": -1, "capa": True},
    {"tipo": "p27_luzPantalla", "x": L, "y": 0, "k": -1, "capa": True, "pantalla": PANT},
    # v2 · concepto 2 "la franja que se escapa del cuadro": el visor se abre DENTRO del monitor (va antes de la luz: es pantalla)
    {"tipo": "p27_visor", "x": L, "y": 0, "k": -1, "z": 1001, "pantalla": PANT, "abre": "p27_tex+0.30", "dur": 0.45,
     "desde": [580, CY + 7, 231, 193], "hasta": [560, 875, 900, 720], "barra": 60, "asoma": 50, "cur": GRILLA["cur1"]},
]
escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24,
          "zoom": [{"k": -1, "s": 1.0, "dur": .01, "y": 1200, "mano": 0.7}],     # vaivén de mano por escena (no es zoom)
          "zonas": [{"x0": L, "x1": L + 1300, "set": "p27_escritorioV", "cam": L, "k": -1, "o": {}}],
          "pan": [{"k": -1, "x": L, "corte": 1}], "props": props, "actores": []}
datos = {"frases": fr, "T": T, "marca": "THE VICEVERSE GG", "escenas": [escena], "p27_fija": True, "cierre": "", "cierre2": "", "paises": []}
(AQUI / "datos.json").write_text(json.dumps(datos, ensure_ascii=False))
print("T", {k: round(v, 2) for k, v in T.items()}, "clave", CLAVE, "→ tex_0" + str(412))
