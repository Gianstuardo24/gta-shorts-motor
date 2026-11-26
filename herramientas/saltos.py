#!/usr/bin/env python3
"""
saltos.py · Detector de cuadros aislados · E1 · SOLO LEE el video (nunca lo modifica).

  python3 saltos.py video.mp4 [--datos datos.json] [--t0 0] [--salida carpeta] [--json informe.json]

Mide TODOS los cuadros (no una muestra) en una copia reducida a 108×192; la diferencia entre dos cuadros es el
promedio de |a − b| en los tres colores (escala 0–255).
  ISLA     1 o 2 cuadros que entran y salen con un cambio brusco (> 8) y no se parecen a lo que hay antes ni
           después. Así se ve un cuadro ajeno: la ciudad de neón del plano 10 v2 o el fondo vacío de otra zona.
           · sin --datos: se marca si lo de antes y lo de después se parecen entre sí más que a la isla (r < 1)
           · con --datos: además se revisan los cuadros intermedios que predice el validador en cada corte de cámara
             y de zona (validar.cuadros_mezclados); si entran y salen con un cambio brusco, se ven: se marcan
           · un destello blanco parejo justo en un inicio de escena es el destello del motor: no se marca
  CORTE    un cambio brusco fuera de una isla. Con --datos se indica si coincide con un cambio previsto; los que
           no coinciden se listan como informativos (los movimientos rápidos de cámara también dan cambios bruscos).
  DESTELLO sin --datos, una isla más clara y pareja se informa aparte: suele ser el destello del cambio de escena.
Calibración (E1): 7 videos entregados + 4 planos aprobados + plano 10 v2; ver pruebas/informes/E1/.
No bloquea nada: deja el video como "revisar" (si hay islas) o "ok". Sale con 0 salvo error al leer el video.
"""
import argparse, json, math, pathlib, subprocess, sys
import numpy as np

W, H = 108, 192
UMBRAL = 8.0         # un cambio entre cuadros mayor que esto es brusco (los movimientos y subtítulos normales quedan debajo)
INTERIOR = 0.5       # dentro de una isla de 2 cuadros, el cambio interno tiene que ser menor que la mitad de los bordes
PROP = 1.0           # sin datos: lo de antes y lo de después tienen que parecerse más entre sí que a la isla
VENTANA = 2          # cuadros de tolerancia alrededor de un corte de los datos
FPS = 30.0


def cuadros(video):
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(video), "-vf", f"scale={W}:{H}:flags=area",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.uint8).reshape(-1, H, W, 3)


def dif(a, b):
    return float(np.abs(a.astype(np.int16) - b.astype(np.int16)).mean())


def medir(fr):
    f = fr.astype(np.int16)
    return np.abs(f[1:] - f[:-1]).mean(axis=(1, 2, 3))          # d[i-1] = cambio entre i-1 e i


def cambios_previstos(datos, t0=0.0):
    """Cuadros de los datos donde la imagen puede cambiar de golpe: inicios de escena, cortes de cámara y de zona."""
    sys.path.insert(0, str(pathlib.Path(__file__).parent)); import claves as C
    T = datos.get("T") or {}; cortes, inicios = [], []
    for e in datos.get("escenas") or []:
        a = 0.0 if e.get("desde") == "0" else T.get(e.get("desde"))
        if a is None:
            continue
        if e.get("desde") != "0":
            inicios.append(a)
        for z in e.get("zoom") or []:
            if (z.get("dur") or 0.6) <= 0.02:
                cortes.append(C.tk(z.get("k"), a, T))
        for p in e.get("pan") or []:
            if p.get("corte"):
                cortes.append(C.tk(p.get("k"), a, T))
    a_cuadro = lambda t: math.ceil((t - t0) * FPS - 1e-9)
    return sorted({a_cuadro(t) for t in cortes if t == t}), sorted({a_cuadro(t) for t in inicios})


def es_destello(fr, i, j):
    """La isla es más clara que sus vecinos de manera pareja (el destello blanco del cambio de escena)."""
    A, B = fr[i - 1].astype(np.float32), fr[j + 1].astype(np.float32)
    X = fr[i:j + 1].astype(np.float32).mean(axis=0); delta = X - (A + B) / 2
    m = float(delta.mean())
    return m > 4 and float(np.abs(delta - m).mean()) / m < 0.6 and X.mean() > max(A.mean(), B.mean())


def islas(fr, d, previstos=None, inicios=None, destellos=None):
    out, n = [], len(fr)
    destellos = [] if destellos is None else destellos
    cerca = lambda i, L: L is not None and any(abs(i - c) <= VENTANA for c in L)
    for L in (1, 2):
        for i in range(1, n - L):
            j = i + L - 1
            entra, sale = float(d[i - 1]), float(d[j])
            if entra <= UMBRAL or sale <= UMBRAL:
                continue
            if L == 2 and (float(d[i]) >= INTERIOR * min(entra, sale) or min(entra, sale) <= 2 * UMBRAL):
                continue                                         # 2 cuadros: bordes más marcados (descarta tirones del movimiento)
            fuera = dif(fr[i - 1], fr[j + 1]); r = fuera / min(entra, sale)
            if r >= PROP:
                continue
            if es_destello(fr, i, j):
                if cerca(i, inicios):
                    continue                                     # el destello del motor en un cambio de escena
                if previstos is None:
                    destellos.append({"desde": i, "hasta": j, "largo": L, "entra": round(entra, 2), "sale": round(sale, 2)})
                    continue                                     # sin datos no se puede confirmar: se informa aparte
            if L == 1 and any(x["desde"] <= i <= x["hasta"] for x in out):
                continue
            out.append({"desde": i, "hasta": j, "largo": L, "entra": round(entra, 2), "sale": round(sale, 2),
                        "r": round(r, 3), "motivo": "aislado"})
    # una isla de 2 cuadros puede contener una de 1 ya marcada: se deja la más larga
    out.sort(key=lambda x: (x["desde"], -x["largo"]))
    final = []
    for x in out:
        if final and x["desde"] <= final[-1]["hasta"]:
            continue
        final.append(x)
    return final


def tira(fr, i, j, ruta):
    """Lo de antes, la isla y lo de después, uno al lado del otro."""
    from PIL import Image
    sep = np.full((H, 4, 3), 255, np.uint8)
    partes = [fr[max(i - 1, 0)], sep] + sum([[fr[k], sep] for k in range(i, j + 1)], []) + [fr[min(j + 1, len(fr) - 1)]]
    img = np.concatenate(partes, axis=1)
    Image.fromarray(img).resize((img.shape[1] * 2, H * 2), Image.NEAREST).save(ruta)


def analizar(video, datos=None, t0=0.0, salida=None):
    fr = cuadros(video); d = medir(fr)
    previstos, inicios = cambios_previstos(datos, t0) if datos else (None, None)
    destellos = []
    isl = islas(fr, d, previstos, inicios, destellos)
    previstos_no_visibles = []
    if datos:
        import validar as V
        T = datos.get("T") or {}; ya = {k for x in isl for k in range(x["desde"], x["hasta"] + 1)}
        for e in datos.get("escenas") or []:
            a = 0.0 if e.get("desde") == "0" else T.get(e.get("desde"))
            if e.get("tipo") != "pelicula" or a is None:
                continue
            for c in V.cuadros_mezclados(e, a, T, t0):
                i, j = c["cuadros"][0], c["cuadros"][-1]
                if i < 1 or j + 1 >= len(fr):
                    continue
                entra, sale = float(d[i - 1]), float(d[j])
                if entra > UMBRAL and sale > UMBRAL:
                    if not any(k in ya for k in range(i, j + 1)):
                        isl.append({"desde": i, "hasta": j, "largo": j - i + 1, "entra": round(entra, 2), "sale": round(sale, 2),
                                    "r": round(dif(fr[i - 1], fr[j + 1]) / min(entra, sale), 3),
                                    "motivo": "intermedio en un corte (previsto por los datos)"})
                else:
                    previstos_no_visibles.append({"desde": i, "hasta": j, "entra": round(entra, 2), "sale": round(sale, 2)})
        isl.sort(key=lambda x: x["desde"])
    en_isla = {k for x in isl for k in range(x["desde"], x["hasta"] + 2)}
    cortes = []
    for i in range(1, len(fr)):
        if d[i - 1] > UMBRAL and i not in en_isla:
            exp = None
            if datos:
                if any(abs(i - c) <= VENTANA for c in previstos): exp = "corte de los datos"
                elif any(0 <= i - c <= 0.85 * FPS for c in inicios): exp = "cambio de escena"
            cortes.append({"cuadro": i, "tiempo": round(t0 + i / FPS, 3), "cambio": round(float(d[i - 1]), 2), "previsto": exp})
    for x in isl:
        x["tiempo"] = round(t0 + x["desde"] / FPS, 3)
        if salida:
            pathlib.Path(salida).mkdir(parents=True, exist_ok=True)
            x["tira"] = str(pathlib.Path(salida) / f"{pathlib.Path(video).stem}_isla_{x['desde']:05d}.png")
            tira(fr, x["desde"], x["hasta"], x["tira"])
    sin_exp = [c for c in cortes if datos and not c["previsto"]]
    for x in destellos:
        x["tiempo"] = round(t0 + x["desde"] / FPS, 3)
    return {"video": str(video), "cuadros": int(len(fr)), "cambio_medio": round(float(d.mean()), 2),
            "islas": isl, "destellos_sin_confirmar": destellos, "previstos_no_visibles": previstos_no_visibles if datos else None,
            "cortes": cortes,
            "cortes_sin_explicar": sin_exp if datos else None, "estado": "revisar" if isl else "ok"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("videos", nargs="+"); ap.add_argument("--datos"); ap.add_argument("--t0", type=float, default=0.0)
    ap.add_argument("--salida"); ap.add_argument("--json")
    a = ap.parse_args(); todos = []
    datos = json.loads(pathlib.Path(a.datos).read_text()) if a.datos else None
    for v in a.videos:
        r = analizar(v, datos, a.t0, a.salida); todos.append(r)
        print(f"{v}: {r['cuadros']} cuadros · {len(r['islas'])} islas · {len(r['cortes'])} cortes"
              + (f" ({len(r['cortes_sin_explicar'])} sin explicar)" if datos else "") + f" · {r['estado'].upper()}")
        for x in r["islas"]:
            print(f"   ✗ isla de {x['largo']} cuadro(s) en el {x['desde']} ({x['tiempo']:.3f} s) · entra {x['entra']} · sale "
                  f"{x['sale']} · r {x['r']} · {x['motivo']}" + (f" · {x['tira']}" if x.get("tira") else ""))
        for x in r["destellos_sin_confirmar"]:
            print(f"   · destello parejo en el cuadro {x['desde']} ({x['tiempo']:.3f} s): si ahí no cambia la escena, revisar")
        for c in (r["cortes_sin_explicar"] or []):
            print(f"   · cambio brusco sin corte en los datos: cuadro {c['cuadro']} ({c['tiempo']:.3f} s) · cambio {c['cambio']} (informativo)")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(todos, ensure_ascii=False, indent=1))
    sys.exit(0)


if __name__ == "__main__":
    main()
