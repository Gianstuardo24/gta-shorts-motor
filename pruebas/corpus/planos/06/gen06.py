"""Prueba 27 · plano 06 · arma datos.json.
Línea (GTA EN 14h, línea 5): "Then they read the ship's name painted on it: The Leonida."
Un solo plano continuo desde el último cuadro del 05 (misma escena, mismo visor, cursor en hover sobre el ✕):
  1 · alejarse  (con "Then"):  ×2,6 → ×1,3 alrededor del cursor (el cursor y el ✕ quedan fijos en pantalla)
  2 · subir     (antes de "The" → después de "Leonida"): la cámara sube y la imagen baja dentro del visor;
                 primer píxel de letras con "The", nombre completo con "Leonida", frenado natural
  3 · acercarse (+4 %, sin rebote) anclado al borde derecho y a la línea del nombre, para asimilarlo
Toda la cámara y el desplazamiento se escriben como claves densas (una por cuadro): no se toca el motor.
"""
import json, sys, math, pathlib
import numpy as np

sys.path.insert(0, "/home/claude/escena")
from armar_escena import alinear, bloques
AQUI = pathlib.Path(__file__).parent
TESTIGO = "--testigo" in sys.argv          # verificación: la zona de las letras se pinta magenta
LEAD, FPS = 0.15, 30
frase = "Then they read the ship's name painted on it: The Leonida."
pal = json.loads((AQUI / "vz_palabras.json").read_text())
pal = [dict(p, i=p["i"] + LEAD, f=p["f"] + LEAD) for p in pal]
limpia = lambda w: w.lower().strip(".,:;!?")
cuando = lambda w: [p["i"] for p in pal if limpia(p["w"]) == w.lower()][-1]   # palabra exacta; si se repite, la última ("The" de "The Leonida")
T_THEN, T_THE, T_LEO = cuando("Then"), cuando("The"), cuando("Leonida")
T_LEO_FIN = [p["f"] for p in pal if limpia(p["w"]) == "leonida"][-1]
FIN = round(T_LEO_FIN + 0.70, 2)                         # tiempo para reconocer y asimilar el nombre
tok, tie = alinear([frase], pal); fr = bloques([frase], tok, tie, FIN)
T = {"fin": FIN, "p27_then": T_THEN, "p27_the": T_THE, "p27_leonida": T_LEO, "p27_leonida_fin": T_LEO_FIN}

# ---------- geometría (la misma del 05) ----------
L = 100000
K = 900 / 1120                       # unidades del mundo por unidad de la hoja dentro del visor
TOP0 = 420 - 50 / K                  # 357,8: borde superior visible de la hoja al final del 05
IMG_Y = 575                          # borde superior de la imagen en el mundo (debajo de la barra)
S0, X0, Y0 = 2.6, 800, 807           # cámara al final del 05
R = X0 + 540 / (1.03 * S0)           # borde derecho del cuadro en el mundo (= borde del visor): fijo todo el plano
BAR = 515                            # borde superior de la barra en el mundo
Y_BAR_PANT = 960 + (240 + (BAR - Y0) * S0) * 1.03     # 425,2: altura de la barra en pantalla al final del 05
S1 = 1.3                             # escala después de alejarse
D_FIN = 157.8                        # desplazamiento final de la imagen: borde visible en y 200 de la hoja (la borda azul entra justo)
LETRAS = (250, 330)
NOMBRE_Y_MUNDO = IMG_Y + ((LETRAS[0] + LETRAS[1]) / 2 - (TOP0 - D_FIN)) * K
Y_NOMBRE_PANT = 720
camX = lambda s: R - 540 / (1.03 * s)                                       # borde derecho anclado
camY_ancla = lambda s, wy, sy: wy - ((sy - 960) / 1.03 - 240) / s            # cámara que deja el punto wy en la altura sy

# ---------- curvas ----------
def suave(u):                        # smootherstep: arranca y frena sin saltos de velocidad ni de aceleración
    u = min(1, max(0, u)); return u * u * u * (u * (6 * u - 15) + 10)
P1 = (T_THEN, 2.02)                  # alejarse
P3 = (2.62, FIN)                     # acercamiento leve
# subir: la imagen baja con aceleración y frenado naturales; los puntos fijan la sincronía con la voz
D_ENTRA = TOP0 - LETRAS[1]           # 27,8: aquí el borde inferior de las letras toca el borde de la imagen
D_COMPLETO = TOP0 - LETRAS[0] + 4    # 111,8: letras enteras más 4 unidades de aire arriba
# velocidad en forma de campana (CDF de una Beta): nace en 0, acelera hasta el nombre y frena suave, sin quiebres.
# Los parámetros se ajustan para que el borde de las letras toque la imagen justo antes de "The" y el nombre quede completo con "Leonida".
from scipy.special import betainc
from scipy.optimize import fsolve
TS, TE = 1.70, 2.85
_u1, _u2 = (T_THE - 0.012 - TS) / (TE - TS), (T_LEO - 0.002 - TS) / (TE - TS)
_p = fsolve(lambda p: [betainc(math.exp(p[0]), math.exp(p[1]), _u1) - D_ENTRA / D_FIN,
                       betainc(math.exp(p[0]), math.exp(p[1]), _u2) - D_COMPLETO / D_FIN], [math.log(4), math.log(4)])
BA, BB = math.exp(_p[0]), math.exp(_p[1])
def D(t):
    return D_FIN * float(betainc(BA, BB, min(1, max(0, (t - TS) / (TE - TS)))))
def camara(t):
    u1 = suave((t - P1[0]) / (P1[1] - P1[0]))
    s = math.exp(math.log(S0) + (math.log(S1) - math.log(S0)) * u1)
    s *= 1 + 0.04 * suave((t - P3[0]) / (P3[1] - P3[0]))
    n = D(t) / D_FIN                                   # avance del ascenso (0 → 1)
    ya = camY_ancla(s, BAR, Y_BAR_PANT)                # alejarse alrededor del cursor: la barra no se mueve
    yb = camY_ancla(s, NOMBRE_Y_MUNDO, Y_NOMBRE_PANT)  # encuadre final: nombre en y 720
    return s, camX(s), ya + (yb - ya) * n

cuadros_t = [round(LEAD + i / FPS, 4) for i in range(int(round((FIN - LEAD) * FPS)) + 1)]
zoom = [{"k": -1, "s": S0, "dur": .01, "x": L + X0, "y": Y0}]
for t in cuadros_t:
    s, x, y = camara(t)
    zoom.append({"k": round(t - 0.02, 4), "s": round(s, 5), "dur": .01, "x": round(L + x, 3), "y": round(y, 3)})
despK = [[round(t, 4), round(D(t), 4)] for t in cuadros_t]

PANT = {"x0": -56, "x1": 1136, "y0": 496, "y1": 1250}
COLS, TOP, FILA, R_, CL = [330, 580, 830], 700, 250, 14, 1
CLAVE = R_ * len(COLS) + CL; CY = 960
GRILLA = {"pantalla": PANT, "cols": COLS, "y0": TOP, "fila": FILA, "tw": 220, "th": 170, "clave": CLAVE, "num0": 412 - CLAVE,
          "dist": TOP + R_ * FILA - CY, "scroll": [-3, -2], "cursor": [-2, -1.6], "resalta": -1.6, "clics": [-1.3, -1.1],
          "cur0": [860, 800], "cur1": [600, 985]}
VISOR = {"tipo": "p27_visor", "x": L, "y": 0, "k": -1, "z": 1001, "pantalla": PANT, "abre": -1, "dur": .01,
         "desde": [580, CY + 7, 231, 193], "hasta": [560, 875, 900, 720], "barra": 60, "asoma": 50, "res": 2.2,
         "cur": [964, 540],          # el cursor sigue en hover sobre el ✕ todo el plano: no hace clic
         "despK": despK,
         # v2 · el título del archivo alineado con el borde izquierdo de "THE LEONIDA" (x 286,8 del mundo):
         # entero y con aire en el encuadre final; fuera de cuadro en el primer cuadro (continuidad exacta con el 05)
         "tituloDx": round(220 * K, 1)}
if TESTIGO: VISOR["testigo"] = True
# la mano del 04, quieta sobre el mouse; el mouse quedó corrido por el recorrido del cursor del 05 (misma razón ≈0,093 del 04)
MANO = {"tipo": "p27_manoPOV", "x": L + 640, "y": 1570, "s": 1.0, "k": -1, "capa": True, "grilla": GRILLA, "mueve": [10, -25]}
props = [dict({"tipo": "p27_grilla", "x": L, "y": 0, "k": -1, "z": 1000}, **GRILLA), VISOR, MANO,
         {"tipo": "p27_luzPantalla", "x": L, "y": 0, "k": -1, "capa": True, "pantalla": PANT, "granoPantalla": True}]
escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24, "zoom": zoom,
          "zonas": [{"x0": L, "x1": L + 1300, "set": "p27_escritorioV", "cam": L, "k": -1, "o": {}}],
          "pan": [{"k": -1, "x": L, "corte": 1}], "props": props, "actores": []}
datos = {"frases": fr, "T": T, "marca": "THE VICEVERSE GG", "escenas": [escena], "p27_fija": True, "cierre": "", "cierre2": "", "paises": []}
nombre = "datos_testigo.json" if TESTIGO else "datos.json"
(AQUI / nombre).write_text(json.dumps(datos, ensure_ascii=False))
# tabla de control para las mediciones (no la usa el motor)
(AQUI / "curvas.json").write_text(json.dumps({"t": cuadros_t, "D": [D(t) for t in cuadros_t], "cam": [camara(t) for t in cuadros_t],
                                              "K": K, "TOP0": TOP0, "IMG_Y": IMG_Y, "LETRAS": LETRAS, "T": T, "D_ENTRA": D_ENTRA, "D_COMPLETO": D_COMPLETO}))
print("campana Beta", round(BA, 2), round(BB, 2), "·", nombre, "T", {k: round(v, 3) for k, v in T.items()}, "· cuadros", len(cuadros_t))
