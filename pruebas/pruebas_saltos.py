#!/usr/bin/env python3
"""
E1 · Pruebas negativas del detector de cuadros aislados: se alteran EN MEMORIA los cuadros de videos aprobados
(nunca el archivo) y se comprueba qué marca el detector. Uso: python3 pruebas_saltos.py [--salida informe.json]
"""
import json, pathlib, sys
import numpy as np
sys.path.insert(0, "/home/claude/herramientas")
import saltos as S

R = pathlib.Path(__file__).parent / "referencias_video"
p05 = S.cuadros(R / "plano05_aprobado.mp4"); p10 = S.cuadros(R / "plano10_aprobado.mp4"); p06 = S.cuadros(R / "plano06_aprobado.mp4")
ajeno = S.cuadros(R / "wge2_entregado.mp4")[[30, 900]]                # dos cuadros de otro video


def caso(fr, cambios):
    f = fr.copy()
    for i, img in cambios.items():
        f[i] = img
    d = S.medir(f); dest = []
    return S.islas(f, d, None, None, dest), dest


def blanco(img, a):
    return np.clip(img.astype(np.float32) * (1 - a) + 255 * a, 0, 255).astype(np.uint8)


CASOS = [
    ("1 cuadro ajeno en el plano 05", p05, {50: ajeno[0]}, "isla", 50),
    ("1 cuadro ajeno en el plano 10", p10, {80: ajeno[1]}, "isla", 80),
    ("2 cuadros ajenos seguidos (plano 10)", p10, {80: ajeno[1], 81: ajeno[1]}, "isla", 80),
    ("cuadro ajeno a medias (mezcla 50 %)", p10, {80: (p10[80] * .5 + ajeno[1] * .5).astype(np.uint8)}, "isla", 80),
    ("cuadro ajeno muy suave (mezcla 15 %)", p10, {80: (p10[80] * .85 + ajeno[1] * .15).astype(np.uint8)}, "nada", None),
    ("cuadro repetido (tirón)", p06, {50: p06[49]}, "nada", None),
    ("destello blanco parejo de 1 cuadro (sin datos)", p10, {80: blanco(p10[80], .35)}, "destello", 80),
    ("cuadro ajeno durante un movimiento rápido (plano 06)", p06, {30: ajeno[0]}, "isla", 30),
]


def main():
    filas, fallas = [], 0
    for nombre, fr, cambios, esperado, donde in CASOS:
        isl, dest = caso(fr, cambios)
        if esperado == "isla":
            ok = any(x["desde"] <= donde <= x["hasta"] for x in isl)
        elif esperado == "destello":
            ok = any(x["desde"] == donde for x in dest) and not isl
        else:
            ok = not isl
        fallas += not ok
        filas.append({"caso": nombre, "esperado": esperado, "ok": ok, "islas": isl, "destellos": dest})
        print(f"{'✔' if ok else '✗'} {nombre:52} esperado: {esperado:8} · islas {[(x['desde'], x['largo'], x['r']) for x in isl]} · destellos {[x['desde'] for x in dest]}")
    print(f"{len(CASOS) - fallas}/{len(CASOS)} casos como se esperaba")
    if "--salida" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--salida") + 1]).write_text(json.dumps(filas, ensure_ascii=False, indent=1, default=str))
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
