#!/usr/bin/env python3
"""Pruebas del constructor y el planificador v2 (27i, bloque 3). Todo corre en copias dentro de /tmp/fv2/constructor.

  1 originales     cada b.py de d24 (36) con el comun/formato de la rama: el _src.json sale idéntico, byte a byte
  2 planificador   los 7 entregados con el planificador de la rama y con el de 27g: {ID}.json y planos.log idénticos
  3 v2             los 7 entregados con v2=True: perfil del canal, campos de cada plano, primer plano "inicio",
                   insertos con su clave de entrada y sin dos cortes de cámara con la misma clave
  4 opciones       wk2 con v2=True y una opción distinta por plano (paneo, fundido, negro sin efecto, fondo base pedido,
                   cámara fija y sin acabado): el constructor escribe lo que pide cada plano

  python3 pruebas/pruebas_constructor.py [--salida pruebas/informes/fondos/constructor_v2.json]
"""
import argparse, collections, json, pathlib, re, shutil, subprocess, sys

RAMA = pathlib.Path(__file__).resolve().parent.parent
D24 = RAMA / "d24"
PLAN = RAMA / "planos_shorts.py"
PLAN_27G = pathlib.Path("/home/claude/.ramas/prueba-corte-sincronizado/planos_shorts.py")
TMP = pathlib.Path("/tmp/fv2/constructor")
ENTREGADOS = ["wd2", "wk2", "wc1", "wm2", "wr1", "wge2", "wgs1"]
V2 = "\n_video_orig = video\ndef video(*a, **k):\n    k['v2'] = True\n    return _video_orig(*a, **k)\n"


def salidas(src):
    return re.findall(r'(?:video|guardar)\(\s*"([^"/]+\.json)"', src)


def correr_b(slot, extra="", sufijo="rama", reemplazos=()):
    """Corre una copia del b.py del slot con el d24 de la rama, en su propia carpeta temporal."""
    dst = TMP / sufijo / slot
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(D24 / slot, dst)
    src = (D24 / slot / "b.py").read_text().replace("'/home/claude/d24'", repr(str(D24)))
    if extra:
        ln = src.split("\n"); i = next(j for j, l in enumerate(ln) if "import *" in l); ln.insert(i + 1, extra); src = "\n".join(ln)
    for a, b in reemplazos:
        assert src.count(a) == 1, (slot, a[:60]); src = src.replace(a, b)
    (dst / "b_prueba.py").write_text(src)
    r = subprocess.run([sys.executable, "b_prueba.py"], cwd=dst, capture_output=True, text=True)
    return r, dst, salidas(src)


def correr_b_produccion(slot):
    """El mismo b.py con el código de producción (/home/claude/d24, sin cambios): la referencia de la comparación."""
    dst = TMP / "produccion" / slot
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(D24 / slot, dst)
    src = (D24 / slot / "b.py").read_text(); (dst / "b_prueba.py").write_text(src)
    r = subprocess.run([sys.executable, "b_prueba.py"], cwd=dst, capture_output=True, text=True)
    return r, dst


def paso_originales():
    res = {}
    for b in sorted(D24.glob("*/b.py")):
        slot = b.parent.name
        r, dst, outs = correr_b(slot); rp, dp = correr_b_produccion(slot)
        if r.returncode != 0 or rp.returncode != 0:
            res[slot] = {"estado": "falla", "error": (r.stderr or rp.stderr)[-300:]}; continue
        ok = all((dst / o).read_bytes() == (dp / o).read_bytes() for o in outs)
        guardado = all((dp / o).read_bytes() == (D24 / slot / o).read_bytes() for o in outs)
        res[slot] = {"estado": "idéntico" if ok else "DISTINTO", "archivos": outs, "coincide_con_el_guardado": guardado}
    n_ok = sum(1 for v in res.values() if v["estado"] == "idéntico")
    viejos = sum(1 for v in res.values() if not v.get("coincide_con_el_guardado", True))
    print(f"1 originales: {n_ok} de {len(res)} idénticos al código de producción "
          f"({viejos} archivos guardados del 24-nov ya no coinciden con su propio b.py, ni con el código de producción)", flush=True)
    for s, v in res.items():
        if v["estado"] != "idéntico": print("   ", s, v)
    return {"identicos": n_ok, "total": len(res), "por_slot": res}


def id_de(slot):
    return next(p.stem for p in (D24 / slot).glob("*.json")
                if not p.stem.endswith(("_src", ".pre")) and p.stem not in ("datos", "datos0", "ficha", "vz_palabras"))


def paso_planificador():
    res = {}
    for slot in ENTREGADOS:
        ID = id_de(slot); out = {}
        for lado, plan in (("27g", PLAN_27G), ("rama", PLAN)):
            dst = TMP / f"plan_{lado}" / slot
            if dst.exists(): shutil.rmtree(dst)
            dst.mkdir(parents=True)
            for f in (f"{ID}.json", f"{ID}.pre.json", "datos.json", "vz_palabras.json"):
                if (D24 / slot / f).exists(): shutil.copy(D24 / slot / f, dst / f)
            r = subprocess.run([sys.executable, str(plan), str(dst), ID], capture_output=True, text=True)
            out[lado] = (r.returncode, (dst / f"{ID}.json").read_bytes(), (dst / "planos.log").read_bytes() if (dst / "planos.log").exists() else b"")
        ok = out["27g"] == out["rama"]
        res[slot] = "idéntico" if ok else "DISTINTO"
    n_ok = sum(1 for v in res.values() if v == "idéntico")
    print(f"2 planificador: {n_ok} de {len(res)} idénticos al de 27g", flush=True)
    return {"identicos": n_ok, "total": len(res), "por_slot": res}


def cortes_repetidos(e):
    por_k = collections.defaultdict(set)
    for p in e.get("pan", []):
        if p.get("corte"): por_k[json.dumps(p["k"])].add(p["x"])
    return {k: sorted(v) for k, v in por_k.items() if len(v) > 1}


def revisar_v2(g, marca):
    e = next(s for s in g["escena"]["escenas"] if s["tipo"] == "pelicula"); prob = []
    perf = json.loads((D24 / "perfiles_canal.json").read_text())["canales"][marca.upper()]
    if {k: v for k, v in (e.get("fondos") or {}).items() if k != "version"} != perf: prob.append("perfil distinto del canal")
    for z in e["zonas"]:
        if "entorno" not in z or "transicion" not in z: prob.append(f"zona {z['x0']} sin campos de plano")
        if z["set"] == "vitrinaV" and (z.get("entorno") != "vitrina" or "k" not in z): prob.append(f"inserto {z['x0']} sin entorno o clave")
    iniciales = [z for z in e["zonas"] if z.get("transicion") == "inicio"]
    if len(iniciales) != 1: prob.append(f"{len(iniciales)} planos con 'inicio'")
    rep = cortes_repetidos(e)
    if rep: prob.append(f"cortes repetidos: {rep}")
    return prob, e


def paso_v2():
    res = {}
    for slot in ENTREGADOS:
        r0, d0, outs = correr_b(slot)
        r, dst, outs = correr_b(slot, V2, "v2")
        if r.returncode != 0:
            res[slot] = {"estado": "falla", "error": r.stderr[-400:]}; continue
        g = json.loads((dst / outs[0]).read_text()); g0 = json.loads((d0 / outs[0]).read_text())
        prob, e = revisar_v2(g, g["marca"])
        e0 = next(s for s in g0["escena"]["escenas"] if s["tipo"] == "pelicula")
        res[slot] = {"estado": "ok" if not prob else "problemas", "problemas": prob,
                     "cortes_repetidos_antes": cortes_repetidos(e0), "cortes_repetidos_v2": cortes_repetidos(e),
                     "planos": [(z["set"], z.get("entorno"), z.get("transicion"), z.get("k")) for z in e["zonas"]]}
    n_ok = sum(1 for v in res.values() if v["estado"] == "ok")
    antes = sum(len(v.get("cortes_repetidos_antes", {})) for v in res.values())
    print(f"3 v2: {n_ok} de {len(res)} con todos los campos · cortes repetidos: {antes} antes → "
          f"{sum(len(v.get('cortes_repetidos_v2', {})) for v in res.values())} con v2", flush=True)
    for s, v in res.items():
        if v["estado"] != "ok": print("   ", s, v.get("problemas") or v.get("error"))
    return {"ok": n_ok, "total": len(res), "por_slot": res}


# wk2 con una opción distinta por plano (los mismos casos que la variante C del bloque 1, ahora escritos por el constructor)
OPCIONES = [
    ('{"k":"s_3","z":"montanaV",', '{"k":"s_3","z":"montanaV","transicion":"paneo",'),
    ('{"k":"s_4","z":"salaV",', '{"k":"s_4","z":"salaV","transicion":"fundido",'),
    ('{"k":"s_7","z":"cocinaV",', '{"k":"s_7","z":"cocinaV","transicion":"negro","efecto_corte":"ninguno",'),
    ('{"k":"s_8","z":"dormitorioV",', '{"k":"s_8","z":"dormitorioV","entorno":"base",'),
    ('{"k":"s_9","z":"salaV",', '{"k":"s_9","z":"salaV","camara":"fija","acabado":"ninguno",'),
]


def paso_opciones():
    r, dst, outs = correr_b("wk2", V2, "opciones", OPCIONES)
    if r.returncode != 0:
        print("4 opciones: falla", r.stderr[-400:]); return {"estado": "falla", "error": r.stderr[-400:]}
    g = json.loads((dst / outs[0]).read_text()); e = next(s for s in g["escena"]["escenas"] if s["tipo"] == "pelicula")
    Z = {z.get("k"): z for z in e["zonas"] if z["set"] != "vitrinaV"}
    pan = {json.dumps(p["k"]): p for p in e["pan"] if p.get("x", 0) < 99000}
    mon = next(z for z in e["zonas"] if z["set"] == "montanaV")
    chequeos = {
        "paneo: la cámara llega a la montaña sin corte": not pan['"s_3"'].get("corte") and Z["s_3"]["transicion"] == "paneo",
        "fundido: la sala se funde sobre la montaña": Z["s_4"]["transicion"] == "fundido" and Z["s_4"].get("previa") == mon["x0"],
        "negro sin líneas: la cocina pasa por negro": Z["s_7"]["transicion"] == "negro" and pan['"s_7"'].get("efecto") == "ninguno",
        "el dormitorio pide el fondo base": Z["s_8"]["set"] == "baseCanal" and Z["s_8"]["entorno"] == "base",
        "la segunda sala: cámara fija y sin acabado": Z["s_9"].get("camara") == "fija" and Z["s_9"].get("acabado") == "ninguno",
    }
    prob, _ = revisar_v2(g, g["marca"])
    ok = all(chequeos.values()) and not prob
    print(f"4 opciones: {'ok' if ok else 'PROBLEMAS'} · " + " · ".join(f"{'✓' if v else '✗'} {k}" for k, v in chequeos.items()), flush=True)
    return {"estado": "ok" if ok else "problemas", "chequeos": chequeos, "problemas": prob, "src": str(dst / outs[0])}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--salida"); a = ap.parse_args()
    TMP.mkdir(parents=True, exist_ok=True)
    inf = {"originales": paso_originales(), "planificador": paso_planificador(), "v2": paso_v2(), "opciones": paso_opciones()}
    if a.salida:
        pathlib.Path(a.salida).write_text(json.dumps(inf, ensure_ascii=False, indent=1))
    ok = (inf["originales"]["identicos"] == inf["originales"]["total"] and inf["planificador"]["identicos"] == inf["planificador"]["total"]
          and inf["v2"]["ok"] == inf["v2"]["total"] and inf["opciones"]["estado"] == "ok")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
