"""Prueba 27 · plano 05 · arma datos.json. Reutiliza la escena del plano 04 (mismo escritorio, explorador y visor) con otra cámara:
macro del visor, cámara quieta; el cursor sube hacia cerrar y se detiene; al final la imagen empieza a bajar (la vista sube) sin tocar las letras.
Línea (GTA EN 14h, línea 4): "At first, it looked like just another unused file."
"""
import json, sys, pathlib
sys.path.insert(0, "/home/claude/escena")
from armar_escena import alinear, bloques
AQUI = pathlib.Path(__file__).parent
TESTIGO = "--testigo" in sys.argv          # verificación: la zona reservada a las letras se pinta magenta
CONTROL = "--control" in sys.argv          # control positivo: se fuerza a mostrar la zona para comprobar que el detector la ve
LEAD = 0.15
frase = "At first, it looked like just another unused file."
pal = json.loads((AQUI / "vz_palabras.json").read_text())
pal = [dict(p, i=p["i"] + LEAD, f=p["f"] + LEAD) for p in pal]
FIN = round(pal[-1]["f"] + 0.80, 2)                       # v2 · final quieto en la duda (opción B): nada se mueve
tok, tie = alinear([frase], pal); fr = bloques([frase], tok, tie, FIN)
cuando = lambda w: next(p["i"] for p in pal if p["w"].lower().startswith(w.lower()))
T = {"fin": FIN, "p27_at": cuando("At"), "p27_unused": cuando("unused"), "p27_file": cuando("file"),
     "p27_file_fin": next(p["f"] for p in pal if p["w"].lower().startswith("file"))}

L = 100000
PANT = {"x0": -56, "x1": 1136, "y0": 496, "y1": 1250}
COLS, TOP, FILA, R, CL = [330, 580, 830], 700, 250, 14, 1
CLAVE = R * len(COLS) + CL; CY = 960
# la grilla queda como terminó el plano 04 (todo en el pasado: scroll hecho, miniatura resaltada, doble clic dado)
GRILLA = {"pantalla": PANT, "cols": COLS, "y0": TOP, "fila": FILA, "tw": 220, "th": 170, "clave": CLAVE, "num0": 412 - CLAVE,
          "dist": TOP + R * FILA - CY, "scroll": [-3, -2], "cursor": [-2, -1.6], "resalta": -1.6, "clics": [-1.3, -1.1],
          "cur0": [860, 800], "cur1": [600, 985]}
X_CERRAR = (110 + 900 - 60 * .62 * 1.0, 515 + 30)          # centro del botón ✕ del visor (mismo cálculo que p27_visor)
VISOR = {"tipo": "p27_visor", "x": L, "y": 0, "k": -1, "z": 1001, "pantalla": PANT, "abre": -1, "dur": .01,
         "desde": [580, CY + 7, 231, 193], "hasta": [560, 875, 900, 720], "barra": 60, "asoma": 50, "res": 2.2,
         # cursor: parte donde quedó en el 04, sube lento hacia cerrar y se detiene antes de llegar (no hace clic)
         # v2 · UN solo movimiento: parte donde quedó en el 04, acelera suave y desacelera de forma continua hasta detenerse
         # junto al ✕ (sin tocarlo) al terminar "file"; arco lateral leve, como una mano real
         "curMov": [["p27_at", 600, 985], ["p27_file_fin", 964, 540, "aproxima", -22]],   # v3: la punta queda sobre el ✕ (hover, sin clic); cabe en el cuadro
         }                                                    # v2 · sin desplazamiento: el ascenso es solo del plano 06
if TESTIGO: VISOR["testigo"] = True
if CONTROL: VISOR["testigo"] = True; VISOR["asoma"] = 200
props = [dict({"tipo": "p27_grilla", "x": L, "y": 0, "k": -1, "z": 1000}, **GRILLA), VISOR,
         {"tipo": "p27_luzPantalla", "x": L, "y": 0, "k": -1, "capa": True, "pantalla": PANT, "granoPantalla": True}]
escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24,
          "zoom": [{"k": -1, "s": 2.6, "dur": .01, "x": L + 800, "y": 807}],      # macro del visor, cámara quieta; borde derecho = borde del visor
          "zonas": [{"x0": L, "x1": L + 1300, "set": "p27_escritorioV", "cam": L, "k": -1, "o": {}}],
          "pan": [{"k": -1, "x": L, "corte": 1}], "props": props, "actores": []}
datos = {"frases": fr, "T": T, "marca": "THE VICEVERSE GG", "escenas": [escena], "p27_fija": True, "cierre": "", "cierre2": "", "paises": []}
nombre = "datos_control.json" if CONTROL else ("datos_testigo.json" if TESTIGO else "datos.json")
(AQUI / nombre).write_text(json.dumps(datos, ensure_ascii=False))
print(nombre, "T", {k: round(v, 2) for k, v in T.items()}, "· botón cerrar en", [round(v, 1) for v in X_CERRAR])
