"""Prueba 27 · plano 10 · arma datos.json (escena aislada, sin planificador ni formato.py).
Línea del guion (GTA EN 14h, línea 9): "Some fans call it a planned tease. Others say it's a leftover. Rockstar hasn't said a word."
"""
import json, sys, pathlib
sys.path.insert(0, "/home/claude/escena")
from armar_escena import alinear, bloques

AQUI = pathlib.Path(__file__).parent
LEAD = 0.15                       # silencio inicial (se recorta al final; evita los 3 cuadros negros de entrada del set)
frase = "Some fans call it a planned tease. Others say it's a leftover. Rockstar hasn't said a word."
pal = json.loads((AQUI / "vz_palabras.json").read_text())
pal = [dict(p, i=p["i"] + LEAD, f=p["f"] + LEAD) for p in pal]
voz_fin = pal[-1]["f"]
FIN = round(voz_fin + 0.40, 2)                # v2: cierre más corto (antes +0.75)
tok, tie = alinear([frase], pal)
fr = bloques([frase], tok, tie, FIN)
cuando = lambda w: next(p["i"] for p in pal if p["w"].lower().startswith(w.lower()))
T = {"fin": FIN, "p27_b": cuando("Others"), "p27_dim": cuando("Rockstar"), "p27_fin": FIN}

LA, LB, Y = 100000, 103000, 1250      # zonas separadas: la luz de una no alcanza a la otra
ZS, ZY = 1.12, 1259                      # encuadre fijo (no es zoom lento): repisa hacia el centro
S = 1.2                                            # escala del barco: idéntica en A y B
BARCO = {"tipo": "p27_barco", "s": S, "k": -1}     # misma definición en ambos estados; solo cambia posición, luz y entorno
def barco(**kw): return dict(BARCO, **kw)

# --- estado A: "planned tease" (repisa limpia, una mano lo deja de frente bajo la lamparita) ---
bx, by = LA + 470, Y - 4                      # v2: más al centro (≈460 px en pantalla)
g = lambda x, y: (x - 232 * S, y - 62 * S)        # v2: agarre por la popa (no tapa cabina, chimenea, mástil ni nombre)
mov_b = [{"k": -1, "x": LA + 480, "y": Y - 300}, {"k": LEAD, "x": LA + 480, "y": Y - 300},
         {"k": LEAD + .72, "x": bx, "y": by - 30, "arco": 30}, {"k": LEAD + .98, "x": bx, "y": by}]
mov_m = [dict(m, x=g(m["x"], m["y"])[0], y=g(m["x"], m["y"])[1]) for m in mov_b] + \
        [{"k": LEAD + 1.16, "x": g(bx, by)[0], "y": g(bx, by)[1]}, {"k": LEAD + 1.75, "x": LA - 260, "y": Y - 760}]
lamp_A = {"base": [LA + 1000, Y - 6], "codo": [LA + 1050, Y - 250], "cabeza": [LA + 840, Y - 440], "eje": 2.444}
props = [
    {"tipo": "p27_lamparita", "x": LA, "y": 0, "k": -1, "z": 1150, **lamp_A},
    barco(x=bx, y=by, mov=mov_b, z=1200, sombra=.55),
    {"tipo": "p27_frente", "x": LA, "y": 0, "k": -1, "fin": "p27_b", "capa": True, "estado": "A", "y0": 1700},
    {"tipo": "p27_mano", "x": 0, "y": 0, "s": S, "k": -1, "fin": "p27_b", "capa": True, "mov": mov_m, "suelta": [LEAD + .98, LEAD + 1.18]},
    {"tipo": "p27_luz", "x": LA, "y": 0, "k": -1, "fin": "p27_b", "capa": True, "foco": [LA + 490, Y - 120], "r": 470,
     "cabeza": lamp_A["cabeza"], "eje": lamp_A["eje"], "amb": [118, 92, 80], "centro": [255, 242, 222], "frio": .05, "haz": .30, "charco": .24, "corteY": Y - 20},
]
# --- estado B: "leftover" (repisa con cajas y polvo; el barco atrás, medio tapado; la luz se apaga con "Rockstar...") ---
lamp_B = dict(lamp_A, base=[LB + 1000, Y - 6], codo=[LB + 1050, Y - 250], cabeza=[LB + 840, Y - 440], eje=2.11)
props += [
    {"tipo": "p27_lamparita", "x": LB, "y": 0, "k": -1, "z": 1150, **lamp_B},
    {"tipo": "p27_caja", "x": LB + 280, "y": Y - 16, "k": -1, "z": 1100, "w": 330, "h": 230, "color": "#7d6346", "polvo": 1, "sem": 1},
    {"tipo": "p27_caja", "x": LB + 262, "y": Y - 246, "k": -1, "z": 1101, "w": 270, "h": 160, "color": "#8a6d4c", "polvo": 1, "sem": 2, "etiqueta": False},
    {"tipo": "p27_tela", "x": LB + 262, "y": Y - 406, "k": -1, "z": 1102, "w": 280},
    barco(x=LB + 660, y=Y - 18, z=1200, sombra=.5),
    {"tipo": "p27_telarana", "x": LB, "y": 0, "k": -1, "z": 1250, "desde": [LB + 818, Y - 400],
     "hasta": [[LB + 700, 672], [LB + 790, 676], [LB + 900, 674], [LB + 990, 680], [LB + 1060, 760]]},
    {"tipo": "p27_caja", "x": LB + 470, "y": Y + 6, "k": -1, "z": 1300, "w": 250, "h": 205, "color": "#76593c", "polvo": .8, "sem": 3},
    {"tipo": "p27_caja", "x": LB + 250, "y": Y + 282, "k": -1, "z": 1000, "w": 300, "h": 200, "color": "#5f4a34", "polvo": .6, "sem": 4},
    {"tipo": "p27_caja", "x": LB + 560, "y": Y + 282, "k": -1, "z": 1000, "w": 240, "h": 170, "color": "#6a5238", "polvo": .6, "sem": 5, "etiqueta": False},
    {"tipo": "p27_caja", "x": LB + 830, "y": Y + 282, "k": -1, "z": 1000, "w": 260, "h": 210, "color": "#594431", "polvo": .6, "sem": 6},
    {"tipo": "p27_frente", "x": LB, "y": 0, "k": -1, "capa": True, "estado": "B", "y0": 1700},
    {"tipo": "p27_pelusa", "x": LB + 470, "y": 700, "s": 2.0, "k": -1, "capa": True, "cae": ["p27_b+0.35", "p27_dim"], "y1": Y - 204, "dx": -45},
    {"tipo": "p27_luz", "x": LB, "y": 0, "k": -1, "capa": True, "foco": [LB + 640, Y - 130], "r": 430,
     "cabeza": lamp_B["cabeza"], "eje": lamp_B["eje"], "amb": [58, 60, 70], "frio": .16, "int": .72, "corteY": Y - 20,
     "dim": ["p27_dim", "p27_dim+0.85", .10], "negro": ["p27_fin-0.38", "p27_fin", .96], "bruma": .05},
    {"tipo": "p27_negro", "x": LB, "y": 0, "k": -1, "capa": True, "centro": "p27_b", "baja": .20, "negro": .08, "sube": .20},   # v3: dip to black
]
escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24,
          "zoom": [{"k": -1, "s": ZS, "dur": .01, "y": ZY}],   # v2b: un solo encuadre que sigue a la cámara (sin "x" por zona: evita el cuadro vacío en el corte)
          "zonas": [{"x0": LA, "x1": LA + 1300, "set": "p27_repisaV", "cam": LA, "k": -1, "o": {"estado": "A", "repisa": Y}},
                    {"x0": LB, "x1": LB + 1300, "set": "p27_repisaV", "cam": LB, "k": -1, "o": {"estado": "B", "repisa": Y}}],
          "pan": [{"k": -1, "x": LA, "corte": 1}, {"k": "p27_b", "x": LB, "corte": 1, "suave": 1}],
          "props": props, "actores": []}
datos = {"frases": fr, "T": T, "marca": "THE VICEVERSE GG", "escenas": [escena], "p27_fija": True,
         "cierre": "", "cierre2": "", "paises": []}
(AQUI / "datos.json").write_text(json.dumps(datos, ensure_ascii=False))
print("T", {k: round(v, 2) for k, v in T.items()}, "LEAD", LEAD)
