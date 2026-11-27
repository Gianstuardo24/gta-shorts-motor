"""MDM 18h · fase A · planos 01–04 · arma datos.json (escena aislada, sin planificador: la cámara es fija en cada plano).
Dirección: storyboard externo V3 + ajustes V4 (26-nov 23:11), autorizada por Tao a las 23:14 solo para 01–04.
Los planos 05A, 05B y 07–09 quedan reservados: aquí no hay nada de ellos."""
import json, sys, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
RAMA = AQUI.parents[2]
sys.path.insert(0, str(RAMA / "escena")); sys.path.insert(0, str(RAMA / "d24")); sys.path.insert(0, str(AQUI))
from armar_escena import alinear, bloques, inicio
from comun import perfil_de
import guion

pal = json.loads((AQUI / "voz" / "vz_palabras.json").read_text())
F = guion.F
D = round(pal[-1]["f"] + 1.6, 2)
tok, tie = alinear(F, pal)
fr = bloques(F, tok, tie, D)
ini = [inicio(tok, tie, i) for i in range(len(F))]
def w(linea, palabra, n=0):
    """inicio de la n-ésima palabra de la línea (1 = primera línea del guion) que empieza con `palabra`"""
    a, b = ini[linea - 1], (ini[linea] if linea < len(F) else 1e9)
    c = [p for p in pal if a - 1e-6 <= p["i"] < b - 1e-6 and p["w"].lower().startswith(palabra.lower())]
    return c[n]["i"]
T = {"fin": D, "s_fin": D,
     # plano 01 · líneas 2–3 (c1: primer cuadro del plano, 0,12 s antes de la línea 2)
     "c1": ini[1] - 0.12, "x_needed": w(2, "needed"), "x_logo": w(2, "logo"), "x_logo_fin": w(2, "for"), "x_asked": w(3, "He"),
     "c2": w(3, "design") - 0.02, "x_carolyn": w(3, "Carolyn"),
     # plano 03 · línea 4
     "c3": ini[3] - 0.03, "x_2": w(4, "2"), "x_hour_fin": w(4, "After") - 0.08, "x_17": w(4, "17"), "x_work_fin": w(4, "the") - 0.05,
     "x_35": w(4, "35"), "x_35_fin": w(4, "dollars", 1) + 0.30, "x_rasga": w(4, "dollars", 1) + 0.38,
     # plano 04 · línea 5
     "c4": ini[4] - 0.02, "x_love0": w(5, "didn't"), "x_love1": w(5, "it,") + 0.15, "x_grow": w(5, "would"), "x_on": w(5, "on"),
     "c5": ini[5],
     # plano 06 · línea 7 y "In 1983" (los planos 05A y 05B, reservados, van entre c5 y c6)
     "c6": ini[6] - 0.12, "x_one": w(7, "the", 2), "x_misses": w(7, "misses"), "x_surprised": w(8, "surprised"),
     "c7": w(8, "Nike") - 0.04}
# (número de plano, clave del corte de entrada, razón). Cada plano tiene su zona fija según su número.
PLANOS = [(1, None, "zapato sin marca: el encargo"), (2, "c2", "empieza el trabajo"), (3, "c3", "ella fija el precio"),
          (4, "c4", "la duda de Knight"), (6, "c6", "el regalo llega y ella no lo nota")]
L = [100000 + 2600 * (n - 1) for n, _, _ in PLANOS]
CORTES = [k for _, k, _ in PLANOS]
zonas = [{"x0": L[i], "x1": L[i] + 1300, "cam": L[i], "set": f"dc_mdm_p0{n}", "entorno": f"dc_mdm_p0{n}",
          "transicion": "inicio" if i == 0 else "corte", "camara": "fija", "acabado": "ninguno",
          "razon": r, **({"k": k} if i else {})} for i, (n, k, r) in enumerate(PLANOS)]
pan = [{"k": -1, "x": L[0], "corte": 1, "dur": 0.04, "efecto": "ninguno"}] + \
      [{"k": CORTES[i], "x": L[i], "corte": 1, "dur": 0.04, "dir": 1, "efecto": "ninguno"} for i in range(1, len(PLANOS))]
escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24,
          "zoom": [{"k": -1, "s": 1.0, "dur": .01, "y": 1200}], "zonas": zonas, "pan": pan, "props": [], "actores": [],
          "fondos": perfil_de("MILLION DOLLAR MISTAKE")}
datos = {"frases": fr, "T": T, "marca": "MILLION DOLLAR MISTAKE", "tema": "mdm", "escenas": [escena], "p27_fija": True,
         "fondos": escena["fondos"], "cierre": "", "cierre2": "", "paises": []}
(AQUI / "datos.json").write_text(json.dumps(datos, ensure_ascii=False))
print("T", {k: round(v, 2) for k, v in sorted(T.items(), key=lambda x: x[1])})
