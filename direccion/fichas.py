#!/usr/bin/env python3
"""Esquema y control de una secuencia de dirección (doc 28 § 5.3). Solo lee.

secuencia.json:
{
  "video": "rabbit22h", "tramo": [2, 10], "origen": "claude" | "chatgpt" | "mezcla",
  "concepto": "...", "regla": "...", "hilo": "...",
  "planos": [
    {"n": 1, "lineas": [2, 3], "idea": "...", "accion": "...", "hilo": "...",
     "prepara": [5], "paga": [], "revela": {"que": "...", "palabra": "..."},
     "oculta": {"que": "...", "hasta": "..."},
     "camara": {"intencion": "revelar", "movimiento": "..."},
     "transicion": "corte", "modo": "objeto que cambia", "produccion": "nuevo", "costo_min": 30,
     "descriptores": {"espacio": "...", "escala": "...", "accion": "...", "modo": "..."},
     "continua": null}
  ]
}

Uso: python3 direccion/fichas.py RUTA/secuencia.json
"""
import json
import sys

CAMPOS = ["n", "lineas", "idea", "accion", "hilo", "prepara", "paga", "revela", "oculta",
          "camara", "transicion", "modo", "produccion", "descriptores"]
INTENCIONES = {"revelar", "seguir", "aislar", "leer", "asimilar", "fija"}
ORIGENES = {"claude", "chatgpt", "mezcla"}


def revisar(sec):
    errores, avisos = [], []
    if sec.get("origen") not in ORIGENES:
        errores.append("origen ausente o inválido (claude, chatgpt o mezcla)")
    for k in ("concepto", "regla", "hilo"):
        if not sec.get(k):
            errores.append(f"falta '{k}' de la secuencia")
    planos = sec.get("planos", [])
    nums = {p.get("n") for p in planos}
    enlaces = 0
    vistos = {}
    for p in planos:
        for c in CAMPOS:
            if c not in p:
                errores.append(f"plano {p.get('n')}: falta '{c}'")
        for r in p.get("prepara", []) + p.get("paga", []):
            if r not in nums:
                errores.append(f"plano {p.get('n')}: enlace a un plano que no existe ({r})")
        enlaces += len(p.get("prepara", []))
        if (p.get("camara") or {}).get("intencion") not in INTENCIONES:
            errores.append(f"plano {p.get('n')}: la cámara necesita una intención ({', '.join(sorted(INTENCIONES))})")
        if p.get("transicion", "corte") != "corte" and not p.get("razon_transicion"):
            errores.append(f"plano {p.get('n')}: transición distinta del corte sin razón narrativa")
        d = p.get("descriptores") or {}
        clave = (d.get("espacio"), d.get("escala"), d.get("accion"), d.get("modo"))
        if clave in vistos and p.get("continua") != vistos[clave]:
            avisos.append(f"plano {p.get('n')}: repite los descriptores del plano {vistos[clave]} sin continuidad declarada")
        vistos.setdefault(clave, p.get("n"))
        if not p.get("prepara") and not p.get("paga") and not p.get("continua"):
            avisos.append(f"plano {p.get('n')}: huérfano (no prepara, no paga y no continúa nada)")
    if enlaces < 2:
        errores.append(f"la secuencia tiene {enlaces} enlaces prepara → paga; el mínimo es 2")
    preparados = {r for p in planos for r in p.get("prepara", [])}
    pagados = {p.get("n") for p in planos if p.get("paga")}
    for r in sorted(preparados - pagados):
        avisos.append(f"promesa sin pago: el plano {r} recibe un enlace pero no declara qué paga")
    return errores, avisos


if __name__ == "__main__":
    sec = json.load(open(sys.argv[1], encoding="utf-8"))
    errores, avisos = revisar(sec)
    for e in errores:
        print("ERROR ", e)
    for a in avisos:
        print("AVISO ", a)
    print(f"{len(errores)} errores · {len(avisos)} avisos")
    sys.exit(1 if errores else 0)
