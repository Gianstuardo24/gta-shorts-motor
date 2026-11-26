#!/usr/bin/env python3
"""
E0 · comparación de DATOS (no de píxeles): vuelve a correr la parte determinista del pipeline de producción
sobre entradas congeladas y comprueba que sale lo mismo, byte a byte.

  guion _src.json + datos.json (marcadores T)
      → resolver.py → post.py → planos_shorts.py  →  {ID}.json final + planos.log

Entradas:
  - {ID}_src.json y vz_palabras.json: del corpus congelado (pruebas/corpus/produccion/<slot>/).
  - datos.json del slot: de la etiqueta git del estado inicial (no está copiado en el corpus).
Se compara contra el {ID}.json y el planos.log congelados (los que alimentaron el render entregado).
Todo corre en /tmp/datos_pipeline/<slot>/; no se escribe nada en producción ni en el corpus.

Uso: python3 datos_pipeline.py [--items wd2,wk2] [--etiqueta estado-inicial-2026-11-26] [--salida informe.json]
Sale con código 1 si algo difiere.
"""
import argparse, hashlib, json, pathlib, shutil, subprocess, sys

AQUI = pathlib.Path(__file__).parent
CORPUS = AQUI / "corpus"
RAIZ = pathlib.Path("/home/claude")
RESOLVER = RAIZ / "resolver.py"
POST = RAIZ / "d24" / "post.py"
PLANOS = RAIZ / "planos_shorts.py"


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def correr(cmd, salida=None):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if salida:
        pathlib.Path(salida).write_text(r.stdout + r.stderr)
    if r.returncode != 0:
        raise RuntimeError(f"falló {cmd[1] if len(cmd) > 1 else cmd}: {r.stderr[-400:]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items")
    ap.add_argument("--etiqueta", default="estado-inicial-2026-11-26")
    ap.add_argument("--salida")
    a = ap.parse_args()
    man = json.loads((CORPUS / "manifiesto.json").read_text())
    its = [it for it in man["items"] if it["tipo"] == "produccion"]
    if a.items:
        its = [it for it in its if it["id"] in a.items.split(",")]
    res, todo_ok = {}, True
    for it in its:
        slot, lote = it["id"], it["lote"]
        C = CORPUS / "produccion" / slot
        D = pathlib.Path("/tmp/datos_pipeline") / slot
        shutil.rmtree(D, ignore_errors=True); D.mkdir(parents=True)
        shutil.copyfile(C / f"{lote}_src.json", D / f"{lote}_src.json")
        shutil.copyfile(C / "vz_palabras.json", D / "vz_palabras.json")
        datos = subprocess.run(["git", "-C", str(RAIZ), "show", f"{a.etiqueta}:d24/{slot}/datos.json"],
                               capture_output=True, check=True).stdout
        (D / "datos.json").write_bytes(datos); (D / "datos0.json").write_bytes(datos)
        r = {"datos_slot_sha256": hashlib.sha256(datos).hexdigest()}
        try:
            correr(["python3", str(RESOLVER), str(D / f"{lote}_src.json"), str(D / "datos0.json"), str(D / f"{lote}.json")])
            correr(["python3", str(POST), str(D), lote])
            correr(["python3", str(PLANOS), str(D), lote], salida=D / "planos.txt")
            r["guion_final"] = sha(D / f"{lote}.json") == it["archivos"][f"{lote}.json"]["sha256"]
            r["planos_log"] = sha(D / "planos.log") == it["archivos"]["planos.log"]["sha256"]
        except Exception as e:
            r["error"] = str(e); r["guion_final"] = r["planos_log"] = False
        r["identico"] = r["guion_final"] and r["planos_log"]
        todo_ok &= r["identico"]
        res[slot] = r
        print(f"  {slot:5} {lote:14} guion final {'IDÉNTICO' if r['guion_final'] else 'DISTINTO'} · "
              f"planos.log {'IDÉNTICO' if r['planos_log'] else 'DISTINTO'}" + (f" · {r['error']}" if "error" in r else ""))
    out = {"scripts": {"resolver.py": sha(RESOLVER), "post.py": sha(POST), "planos_shorts.py": sha(PLANOS)},
           "etiqueta_datos": a.etiqueta, "items": res, "identicos": todo_ok}
    if a.salida:
        pathlib.Path(a.salida).write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(json.dumps({"items": len(res), "identicos": todo_ok}))
    sys.exit(0 if todo_ok else 1)


if __name__ == "__main__":
    main()
