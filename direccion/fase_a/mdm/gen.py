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
     # gancho · línea 1
     "x_price": w(1, "price"), "x_joke": w(1, "joke"), "x_but": w(1, "But"),
     # plano 01 · líneas 2–3 (c1: primer cuadro del plano, 0,12 s antes de la línea 2)
     "c1": ini[1] - 0.12, "x_needed": w(2, "needed"), "x_logo": w(2, "logo"), "x_logo_fin": w(2, "for"), "x_asked": w(3, "He"),
     "c2": w(3, "design") - 0.02, "x_carolyn": w(3, "Carolyn"),
     # plano 03 · línea 4
     "c3": ini[3] - 0.03, "x_2": w(4, "2"), "x_hour_fin": w(4, "After") - 0.08, "x_17": w(4, "17"), "x_work_fin": w(4, "the") - 0.05,
     "x_35": w(4, "35"), "x_35_fin": w(4, "dollars", 1) + 0.30, "x_rasga": w(4, "dollars", 1) + 0.38,
     # plano 04 · línea 5
     "c4": ini[4] - 0.02, "x_love0": w(5, "didn't"), "x_love1": w(5, "it,") + 0.15, "x_grow": w(5, "would"), "x_on": w(5, "on"),
     "c5": ini[5],
     # planos 05A y 05B · línea 6 (esperan el archivo del logo)
     "x_swoosh": w(6, "swoosh"), "c5b": w(6, "of") - 0.03, "x_most": w(6, "most"), "x_logos": w(6, "logos"),
     # plano 06 · línea 7 y "In 1983"
     "c6": ini[6] - 0.12, "x_one": w(7, "the", 2), "x_misses": w(7, "misses"),
     # plano 07 · línea 8
     "c7": w(8, "Nike") - 0.04, "x_surprised": w(8, "surprised"), "x_gold": w(8, "gold"), "x_ring": w(8, "ring"),
     # plano 08 · línea 9
     "c8": ini[8] - 0.12, "x_500": w(9, "500"), "x_shares": w(9, "shares"),
     # plano 09 · línea 10 (09b: recuerdo de 1971 con "She set her price")
     "c9": ini[9] - 0.12, "c9b": w(10, "She") - 0.04, "c9c": w(10, "and") - 0.04,
     # cierre · líneas 11 y 12
     "c10": ini[10] - 0.12, "x_small": w(11, "A"), "x_tell": ini[11], "x_follow": w(12, "Follow"),
     "s_cta": w(12, "Follow")}                       # el botón de seguir entra con "Follow"
# (plano, set, clave del corte de entrada, casilla de su zona, razón). La casilla fija la posición de la zona.
PLANOS = [("00", "p00", None, -1, "gancho: la factura de $35"),
          ("01", "p01", "c1", 0, "zapato sin marca: el encargo"), ("02", "p02", "c2", 1, "empieza el trabajo"),
          ("03", "p03", "c3", 2, "ella fija el precio"), ("04", "p04", "c4", 3, "la duda de Knight"),
          ("05a", "p05a", "c5", 4, "la carpeta se abre: el dibujo"), ("05b", "p05b", "c5b", 10, "uno, dos, multitud"),
          ("06", "p06", "c6", 5, "el regalo llega y ella no lo nota"), ("07", "p07", "c7", 6, "el anillo"),
          ("08", "p08", "c8", 7, "las 500 acciones"), ("09a", "p09", "c9", 8, "no fue un mal trato"),
          ("09b", "p09b", "c9b", 9, "recuerdo: ella puso el precio"), ("09c", "p09", "c9c", 11, "retoma la línea"),
          ("10", "p10", "c10", 12, "cierre: el precio y lo que vino después")]
L = [100000 + 2600 * c for _, _, _, c, _ in PLANOS]
CORTES = [k for _, _, k, _, _ in PLANOS]
zonas = [{"x0": L[i], "x1": L[i] + 1300, "cam": L[i], "set": f"dc_mdm_{st}", "entorno": f"dc_mdm_{st}",
          "transicion": "inicio" if i == 0 else "corte", "camara": "fija", "acabado": "ninguno",
          "razon": r, **({"k": k} if i else {})} for i, (_, st, k, _, r) in enumerate(PLANOS)]
pan = [{"k": -1, "x": L[0], "corte": 1, "dur": 0.04, "efecto": "ninguno"}] + \
      [{"k": CORTES[i], "x": L[i], "corte": 1, "dur": 0.04, "dir": 1, "efecto": "ninguno"} for i in range(1, len(PLANOS))]
escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24,
          "zoom": [{"k": -1, "s": 1.0, "dur": .01, "y": 1200}], "zonas": zonas, "pan": pan, "props": [], "actores": [],
          "fondos": perfil_de("MILLION DOLLAR MISTAKE")}
datos = {"frases": fr, "T": T, "marca": "MILLION DOLLAR MISTAKE", "tema": "mdm", "escenas": [escena], "p27_fija": True,
         "fondos": escena["fondos"],
         # cierre del canal (como en los demás videos de MDM): pregunta de la línea 12, comentar, like y seguir
         "cierre": "WHAT WOULD YOU CHARGE?", "cierre2": "Tell me. Comment", "paises": [], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
(AQUI / "datos.json").write_text(json.dumps(datos, ensure_ascii=False))
print("T", {k: round(v, 2) for k, v in sorted(T.items(), key=lambda x: x[1])})
