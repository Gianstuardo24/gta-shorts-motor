#!/usr/bin/env python3
"""Control positivo de la inspección (27i, bloque 2): los 7 videos entregados el 25-nov, SIN perfil de fondos.

La inspección tiene que encontrar en cada uno lo mismo que midió el diagnóstico 27h (fondo base visible más del 2 % de la
pantalla antes del cierre, y los cuadros intermedios de los cortes). Se compara cuadro por cuadro con la tabla del 27h.
Solo lee el corpus congelado y la tabla; escribe el informe en pruebas/informes/fondos/.

  flock /tmp/render.lock python3 pruebas/inspeccion_originales.py [--slots wk2,wgs1] [--tabla /tmp/fondos/tabla_7.json]
"""
import argparse, json, pathlib, sys, time

RAMA = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAMA / "herramientas")); sys.path.insert(0, str(RAMA / "pruebas"))
import inspeccion_fondos as I  # noqa: E402
import regresion as R  # noqa: E402

SLOTS = ["wd2", "wk2", "wc1", "wm2", "wr1", "wge2", "wgs1"]
INF = RAMA / "pruebas" / "informes" / "fondos"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--slots"); ap.add_argument("--tabla", default="/tmp/fondos/tabla_7.json")
    a = ap.parse_args(); slots = a.slots.split(",") if a.slots else SLOTS
    tabla = {v["slot"]: v for v in json.loads(pathlib.Path(a.tabla).read_text())}
    salida = {"fecha": time.strftime("%Y-%m-%d %H:%M:%S"), "videos": {}}
    for it in R.items_del_corpus(slots):
        s = it["id"]; r = it["render"]
        inf = I.inspeccionar(it["datos"], fps=r["fps"], t0=r["t0"], cuadros=r["cuadros"], avance=False,
                             salida=INF / f"inspeccion_{s}_original.json")
        d = json.loads(pathlib.Path(it["datos"]).read_text()); n_fin = int((d["T"]["s_fin"] - 0.1) * 30)    # el mismo corte del 27h
        nuestros = {c["n"] for c in inf["cuadros"] if c["base"] > 2 and c["n"] < n_fin}
        for k in ("desfase_de_corte",):
            nuestros |= {n for t in inf["errores_tecnicos"].get(k, {}).get("tramos", []) for n in range(t["desde"], t["hasta"] + 1)}
        t27 = tabla[s]["prod"]
        suyos = {n for m in t27["momentos"] for n in range(m["desde"], m["hasta"] + 1)}
        comun = nuestros & suyos
        fila = {"cuadros": len(inf["cuadros"]), "segundos": inf["meta"]["segundos"], "bloquea": inf["bloquea"],
                "errores": {k: v["cuadros"] for k, v in inf["errores_tecnicos"].items()},
                "27h_total": len(suyos), "inspeccion_total": len(nuestros), "coinciden": len(comun),
                "solo_27h": sorted(suyos - nuestros)[:40], "solo_inspeccion": sorted(nuestros - suyos)[:40],
                "acuerdo": round(len(comun) / max(1, len(nuestros | suyos)), 3)}
        salida["videos"][s] = fila
        print(f"{s:5} 27h {len(suyos):4} · inspección {len(nuestros):4} · coinciden {len(comun):4} · acuerdo {fila['acuerdo']:.3f} · "
              f"{fila['segundos']:.0f} s · errores {fila['errores']}", flush=True)
    (INF / "inspeccion_7_originales.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
