#!/usr/bin/env python3
"""
E1 · Calibración del detector de cuadros aislados (herramientas/saltos.py) sobre las referencias congeladas
y el caso real del plano 10 v2. Solo lee videos. Escribe el informe que se le indique.
Para cada cuadro: s = min(d1, d2) (qué tan distinto es de sus dos vecinos) y r = d0 / s (qué tan parecidos son los
vecinos entre sí, comparado con eso). Un cuadro aislado tiene s alto y r bajo.
Uso: python3 calibrar_saltos.py [--salida informe.json]
"""
import json, pathlib, sys
import numpy as np
sys.path.insert(0, "/home/claude/herramientas")
import saltos as S

R = pathlib.Path(__file__).parent / "referencias_video"
VIDEOS = [(p.stem, p, "referencia") for p in sorted(R.glob("*.mp4"))]
VIDEOS += [("plano10_v2 (caso real)", pathlib.Path("/home/claude/prueba27/p10/plano10_v2.mp4"), "error conocido")]


def perfil(video):
    fr = S.cuadros(video); d, d0 = S.medir(fr)
    s = np.minimum(d[:-1], d[1:]); r = d0 / np.maximum(s, 1e-6)
    orden = np.argsort(r + (s < 4) * 99)[:3]                                  # los 3 cuadros más "aislados" con s ≥ 4
    top = [{"cuadro": int(i + 1), "s": round(float(s[i]), 2), "r": round(float(r[i]), 3)} for i in orden]
    sobre = [{"cuadro": int(i + 1), "s": round(float(s[i]), 2), "r": round(float(r[i]), 3)} for i in np.where(s > S.UMBRAL_SALTO)[0]]
    return fr, {"cuadros": int(len(fr)), "d_media": round(float(d.mean()), 2), "d_max": round(float(d.max()), 2),
                "s_max": round(float(s.max()), 2), "mas_aislados": top, "con_s_sobre_umbral": sobre}


def main():
    filas = {}
    for nombre, v, tipo in VIDEOS:
        fr, p = perfil(v); p["tipo"] = tipo; filas[nombre] = p
        m = p["mas_aislados"][0]
        print(f"{nombre:28} {p['cuadros']:5} cuadros · d media {p['d_media']:5.2f} · d máx {p['d_max']:6.2f} · s máx {p['s_max']:6.2f}"
              f" · más aislado: cuadro {m['cuadro']} (s {m['s']}, r {m['r']}) · con s>{S.UMBRAL_SALTO:g}: "
              + (", ".join(f"{x['cuadro']}(s {x['s']}, r {x['r']})" for x in p["con_s_sobre_umbral"][:6]) or "ninguno"))
    if "--salida" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--salida") + 1]).write_text(json.dumps(filas, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
