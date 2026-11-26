#!/usr/bin/env python3
"""Pruebas negativas de la inspección (27i, bloque 2, caso D).

Cada caso planta UN error en una copia de los datos del piloto wk2 (con perfil de fondos) y comprueba que la inspección
lo encuentra con el nombre correcto. Solo se miden los cuadros alrededor del error. Nada se modifica fuera de /tmp.

  flock /tmp/render.lock python3 pruebas/pruebas_inspeccion.py [--salida pruebas/informes/fondos/inspeccion_negativas.json]
"""
import argparse, copy, json, pathlib, subprocess, sys, tempfile
import numpy as np

RAMA = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAMA / "herramientas"))
import inspeccion_fondos as I  # noqa: E402

PILOTO = RAMA / "pruebas" / "informes" / "fondos" / "wk2_piloto_datos.json"
VIDEO = pathlib.Path("/mnt/user-data/outputs/27i_piloto/wk2_piloto_27i.mp4")
TMP = pathlib.Path("/tmp/fv2/insp/negativas")


def peli(d):
    return next(s for s in d["escenas"] if s["tipo"] == "pelicula")


def limpiar(d):
    """Base limpia: los datos del piloto (bloque 1) se armaron con el insertar() anterior y tienen dos cortes de cámara en
    s_6 (sala e inserto). El motor usa el último de la lista; se deja solo ese, como lo hace el constructor v2."""
    e = peli(d); T = d["T"]; vistos = {}
    for i, p in enumerate(e["pan"]):
        if p.get("corte"):
            vistos[round(T.get(p["k"], -1) if isinstance(p["k"], str) else p["k"], 3)] = i
    e["pan"] = [p for i, p in enumerate(e["pan"]) if not p.get("corte") or
                vistos[round(T.get(p["k"], -1) if isinstance(p["k"], str) else p["k"], 3)] == i]
    return d


def zona(d, st, i=0):
    return [z for z in peli(d)["zonas"] if z["set"] == st][i]


def d1(d):   # una zona con transparencia: la montaña "se funde" sin un escenario anterior
    z = zona(d, "montanaV"); z["transicion"] = "fundido"; z.pop("previa", None); return d


def d2(d):   # un set sin cubrir: la cámara se aleja más de lo que cubre el escenario
    zs = peli(d)["zoom"]; i = next(j for j, z in enumerate(zs) if z.get("k") == 13.411)
    zs.insert(i + 1, {"k": 13.6, "s": 0.55, "dur": 0.01, "x": 3250, "y": 1300}); return d


def d3(d):   # un corte con desfase: el zoom de la montaña llega 2 cuadros después del cambio de plano
    z = next(z for z in peli(d)["zoom"] if z.get("k") == "s_3" and z.get("corte")); z["k"] = "s_3+0.067"; return d


def d4(d):   # el plano pide el fondo base y el perfil no lo permite
    d["fondos"]["escenas"] = "nunca"; z = zona(d, "dormitorioV"); z.update(set="baseCanal", entorno="base"); return d


def d5(d):   # se ve el fondo base en un plano que no lo pide
    z = zona(d, "dormitorioV"); z.update(set="baseCanal"); return d


def d6(d):   # el primer cuadro sin su entorno: el primer plano aparece fundiéndose desde nada
    z = peli(d)["zonas"][0]; z.update(transicion="fundido", k=0); return d


def d7(d):   # el escenario dibujado no es el entorno que declara el plano
    zona(d, "dormitorioV")["entorno"] = "cocinaV"; return d


def d8(d):   # clave de tiempo que no existe (el motor la resolvería en silencio como el inicio de la escena)
    p = next(p for p in peli(d)["props"] if isinstance(p.get("k"), str)); p["k"] = "s_99"; return d


CASOS = [  # (id, qué se planta, función, cuadros a medir, error que se espera)
    ("D1", "zona con transparencia", d1, (380, 400), "hueco"),
    ("D2", "set sin cubrir (la cámara se aleja de más)", d2, (403, 415), "hueco"),
    ("D3", "corte con desfase de 2 cuadros", d3, (380, 392), "desfase_de_corte"),
    ("D4", "fondo base pedido donde el perfil no lo deja", d4, (800, 812), "base_no_permitida"),
    ("D5", "fondo base visible en un plano que no lo pide", d5, (800, 812), "base_fuera_de_lugar"),
    ("D6", "primer cuadro sin su entorno", d6, (0, 6), "primer_cuadro"),
    ("D7", "escenario distinto del entorno declarado", d7, (800, 806), "fuera_de_plano"),
    ("D8", "clave de tiempo inexistente", d8, (0, 2), "validador"),
]


def video_con_isla(n_isla=500, n_ajeno=1000):
    """Copia reducida del video del piloto con UN cuadro ajeno en n_isla (el cuadro n_ajeno)."""
    W, H = 108, 192
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(VIDEO), "-vf", f"scale={W}:{H}:flags=area", "-f", "rawvideo",
                        "-pix_fmt", "rgb24", "-"], capture_output=True, check=True)
    fr = np.frombuffer(r.stdout, np.uint8).reshape(-1, H, W, 3).copy()
    fr[n_isla] = fr[n_ajeno]
    out = TMP / "piloto_con_isla.mkv"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30",
                    "-i", "-", "-c:v", "ffv1", str(out)], input=fr.tobytes(), check=True)
    limpio = TMP / "piloto_reducido.mkv"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30",
                    "-i", "-", "-c:v", "ffv1", str(limpio)], input=np.frombuffer(r.stdout, np.uint8).tobytes(), check=True)
    return out, limpio


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--salida"); a = ap.parse_args()
    TMP.mkdir(parents=True, exist_ok=True)
    base = limpiar(json.loads(PILOTO.read_text())); res = []
    (TMP / "D0.json").write_text(json.dumps(base, ensure_ascii=False))
    for cid, que, f, (n0, n1), esperado in [("D0", "nada (base limpia: control)", lambda d: d, (380, 392), None)] + CASOS:
        d = f(copy.deepcopy(base)); ruta = TMP / f"{cid}.json"; ruta.write_text(json.dumps(d, ensure_ascii=False))
        inf = I.inspeccionar(ruta, desde=n0, hasta=n1, avance=False)
        enc = sorted(inf["errores_tecnicos"])
        ok = (esperado in enc) if esperado else not enc
        res.append({"caso": cid, "planta": que, "cuadros": [n0, n1], "esperado": esperado, "encontrado": enc, "detectado": ok,
                    "tramos": inf["errores_tecnicos"].get(esperado, {}).get("tramos")})
        print(f"{cid} {'✓' if ok else '✗'} {que}: espera {esperado} · encuentra {enc}", flush=True)
    # D9: cuadro aislado en el video (detector de la E1, conectado con --video)
    con_isla, limpio = video_con_isla()
    for cid, vid, esperado in (("D9", con_isla, True), ("D9-control", limpio, False)):
        inf = I.inspeccionar(TMP / "D0.json", desde=498, hasta=502, video=vid, avance=False)
        hay = "cuadro_aislado" in inf["errores_tecnicos"]
        ok = hay == esperado
        res.append({"caso": cid, "planta": "un cuadro ajeno en el video (cuadro 500)" if esperado else "el mismo video sin el cuadro ajeno",
                    "esperado": "cuadro_aislado" if esperado else "sin cuadros aislados", "encontrado": sorted(inf["errores_tecnicos"]),
                    "detectado": ok, "islas": inf["errores_tecnicos"].get("cuadro_aislado", {}).get("islas")})
        print(f"{cid} {'✓' if ok else '✗'} cuadro aislado: espera {esperado} · encuentra {hay}", flush=True)
    total = sum(1 for r in res if r["detectado"])
    print(f"\n{total} de {len(res)} casos correctos")
    if a.salida:
        pathlib.Path(a.salida).write_text(json.dumps({"casos": res, "correctos": total, "total": len(res)}, ensure_ascii=False, indent=1))
    sys.exit(0 if total == len(res) else 1)


if __name__ == "__main__":
    main()
