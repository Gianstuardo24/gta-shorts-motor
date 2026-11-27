#!/usr/bin/env python3
"""Detectores de la etapa de dirección creativa (doc 28 § 6), versión mínima.

Solo leen datos: nunca modifican escenas, renders ni el motor.

Fórmulas base del 25-nov (§ 6.1), plano por plano (un plano = una zona de la película):
  F1  set + figuras de pie + palabra flotante (rótulo o emoji)
  F2  inserto con pedestal y fondo neutro (set vitrinaV)
  F3  persona que explica u ofrece
Señal extra: texto flotante que repite una palabra dicha (umbral 0).

Uso:
  python3 direccion/detectores.py pruebas/corpus/produccion        # informe de los 7
  python3 direccion/detectores.py RUTA/AL/_src.json --json
"""
import glob
import json
import os
import re
import sys

FIGURAS = {"gato", "perro"}          # animales que se colocan de pie o sentados
FLOTANTES = {"rotulo"}               # textos sueltos sobre la escena
POSES_F3 = {"explica", "ofrece"}
SET_F2 = {"vitrinaV"}


def _frase_de(momentos):
    """clave de momento -> índice de frase."""
    return {m[0]: m[1] for m in momentos}


def _palabras_dichas(d):
    frases = d.get("frases_voz") or d.get("frases") or []
    txt = " ".join(f if isinstance(f, str) else str(f) for f in frases)
    return {w for w in re.findall(r"[a-záéíóúñü']+", txt.lower()) if len(w) > 1}


def analizar(d):
    esc = d["escena"]
    peli = next(s for s in esc["escenas"] if s.get("tipo") == "pelicula")
    frase = _frase_de(esc.get("momentos", []))
    zonas = sorted(peli["zonas"], key=lambda z: z["x0"])
    # rango de frases de cada zona: desde su clave hasta la clave de la zona siguiente
    ini = [frase.get(z.get("k"), 0) if z.get("k") is not None else 0 for z in zonas]
    fin = ini[1:] + [10 ** 6]
    dichas = _palabras_dichas(d)

    def zona_de_x(x):
        for i, z in enumerate(zonas):
            if z["x0"] <= x < z["x1"]:
                return i
        return None

    def zona_de_k(k):
        p = frase.get(k, k if isinstance(k, int) else None)
        if p is None:
            return None
        for i in range(len(zonas)):
            if ini[i] <= p < fin[i]:
                return i
        return None

    planos = [dict(n=i + 1, set=z.get("set"), figuras=0, flotantes=[], poses=[]) for i, z in enumerate(zonas)]
    for p in peli.get("props", []):
        i = zona_de_x(p.get("x", -1))
        if i is None:
            continue
        if p.get("tipo") in FIGURAS:
            planos[i]["figuras"] += 1
        elif p.get("tipo") in FLOTANTES:
            planos[i]["flotantes"].append(("rotulo", str(p.get("texto", ""))))
    for a in peli.get("actores", []):
        for kk in a.get("keys", []):
            i = zona_de_x(kk.get("x", -1))
            if i is not None:
                planos[i]["figuras"] += 1
                planos[i]["poses"].append(kk.get("pose"))
    for e in peli.get("emojis", []):
        i = zona_de_k(e.get("k"))
        if i is not None:
            planos[i]["flotantes"].append(("emoji", e.get("e", "")))

    for pl in planos:
        marcas = []
        if pl["set"] in SET_F2:
            marcas.append("F2")
        rotulos = [t for k, t in pl["flotantes"] if k == "rotulo"]
        if pl["set"] not in SET_F2 and pl["figuras"] > 0 and rotulos:
            marcas.append("F1")
        # un emoji suelto no es una palabra: queda como observación, no como F1
        pl["emoji_flotante"] = [t for k, t in pl["flotantes"] if k == "emoji"]
        if any(x in POSES_F3 for x in pl["poses"]):
            marcas.append("F3")
        repite = [t for k, t in pl["flotantes"] if k == "rotulo"
                  and any(w in dichas for w in re.findall(r"[a-záéíóúñü']+", t.lower()))]
        pl["formulas"] = marcas
        pl["texto_que_repite_la_voz"] = repite
    return planos


def informe(ruta):
    archivos = sorted(glob.glob(os.path.join(ruta, "*", "*_src.json"))) if os.path.isdir(ruta) else [ruta]
    total = con = 0
    por_formula = {"F1": 0, "F2": 0, "F3": 0}
    filas = []
    for f in archivos:
        d = json.load(open(f, encoding="utf-8"))
        planos = analizar(d)
        n = sum(1 for p in planos if p["formulas"])
        total += len(planos)
        con += n
        for p in planos:
            for m in p["formulas"]:
                por_formula[m] += 1
        filas.append((os.path.basename(os.path.dirname(f)) or f, len(planos), n, planos))
    return dict(planos=total, con_formula=con, por_formula=por_formula, videos=filas)


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "pruebas/corpus/produccion"
    r = informe(ruta)
    if "--json" in sys.argv:
        print(json.dumps(r, ensure_ascii=False, indent=1))
        sys.exit(0)
    for slot, n, c, planos in r["videos"]:
        marcas = " ".join(f"{p['n']}:{'+'.join(p['formulas']) or '·'}" for p in planos)
        print(f"{slot:5} {c:2}/{n:2}  {marcas}")
    print(f"TOTAL {r['con_formula']}/{r['planos']}  por fórmula {r['por_formula']}")
