"""Comparación con semilla fija (E0, 26-nov-2026).

Renderiza cuadros EXACTOS del corpus congelado con el motor indicado y calcula la huella SHA-256 de los píxeles de cada
cuadro (no del archivo de imagen). Con una línea base, informa qué cuadros cambiaron.

  Nivel rápido:   un cuadro por segundo (producción) o cada 5 cuadros (planos), más los cuadros alrededor de cada cambio de escena
                  y el primero y el último.
  Nivel completo: TODOS los cuadros, exactamente los mismos instantes que usa render.py.

La semilla fija reemplaza Math.random solo dentro de esta herramienta (el motor usa Math.random una vez: el grano del
acabado "pro"). El motor y render.py NO se modifican.

Uso:
  python3 regresion.py --nivel rapido|completo [--motor RUTA/escena.html] [--items wd2,plano05]
                       [--salida informe.json] [--base lineas_base/X.json] [--diferencias CARPETA]
  --base sin --salida compara; --salida sin --base solo calcula. Una línea base nueva SOLO se guarda con autorización de Tao.
"""
import argparse, json, pathlib, sys, time, hashlib, base64, subprocess
from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).parent
CORPUS = AQUI / "corpus"
SEMILLA_JS = "(()=>{let s=12345;Math.random=()=>{s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}})();"
HUELLA_JS = """async()=>{const c=document.getElementById('c');const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;
 const h=await crypto.subtle.digest('SHA-256',d);return Array.from(new Uint8Array(h)).map(b=>b.toString(16).padStart(2,'0')).join('')}"""


def items_del_corpus(filtro=None):
    man = json.loads((CORPUS / "manifiesto.json").read_text())
    out = []
    for it in man["items"]:
        if filtro and it["id"] not in filtro:
            continue
        base = CORPUS / ("produccion" if it["tipo"] == "produccion" else "planos") / it["id"].replace("plano", "")
        datos = base / ("datos_render.json" if it["tipo"] == "produccion" else "datos.json")
        out.append(dict(it, datos=datos))
    return out


def tiempos(it, nivel):
    r = it["render"]; t0, fps, n = r["t0"], r["fps"], r["cuadros"]
    if nivel == "completo":
        idx = range(n)
    else:
        paso = 30 if it["tipo"] == "produccion" else 5          # 1 s en producción; 1/6 s en los planos (son cortos)
        idx = set(range(0, n, paso)) | {n - 1}
        d = json.loads(it["datos"].read_text()); T = d.get("T", {})
        for e in d.get("escenas", []):                     # alrededor de cada cambio de escena (destello y salida)
            k = e.get("desde")
            if k in (None, "0") or k not in T:
                continue
            c = round((T[k] - t0) * fps)
            idx |= {i for i in (c - 4, c - 1, c, c + 1, c + 4, c + 12) if 0 <= i < n}
        idx = sorted(idx)
    return [round(t0 + i / fps, 6) for i in idx]


def medir(motor, items, nivel, dif_dir=None, base=None, avance=True):
    motor = pathlib.Path(motor).resolve()
    res = {"meta": {"nivel": nivel, "motor": str(motor), "motor_sha256": hashlib.sha256(motor.read_bytes()).hexdigest(),
                    "semilla": 12345, "fecha": time.strftime("%Y-%m-%d %H:%M:%S")}, "items": {}}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
        res["meta"]["navegador"] = b.version
        for it in items:
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            pg.add_init_script(SEMILLA_JS)
            pg.add_init_script(f"window.DATOS={it['datos'].read_text()};")
            pg.goto(motor.as_uri())
            pg.wait_for_function("window.LISTO===true", timeout=30000)
            ts = tiempos(it, nivel); h = {}; t_ini = time.time(); malos = 0
            for j, t in enumerate(ts):
                pg.evaluate(f"render({t})")
                hx = pg.evaluate(HUELLA_JS)
                k = f"{t:.6f}"; h[k] = hx
                if dif_dir and base and base.get(it["id"], {}).get(k) not in (None, hx) and malos < 5:
                    malos += 1; dd = pathlib.Path(dif_dir); dd.mkdir(parents=True, exist_ok=True)
                    png = pg.evaluate("document.getElementById('c').toDataURL('image/png')")
                    (dd / f"{it['id']}_{t:08.3f}.png").write_bytes(base64.b64decode(png.split(",", 1)[1]))
            res["items"][it["id"]] = h
            if avance:
                print(f"  {it['id']:9} {len(ts):5} cuadros en {time.time() - t_ini:6.1f} s", flush=True)
            pg.close()
        b.close()
    return res


def comparar(actual, base):
    informe = {}; total = dist = 0
    for iid, h in actual["items"].items():
        hb = base["items"].get(iid)
        if hb is None:
            informe[iid] = {"estado": "sin línea base"}; continue
        comunes = [k for k in h if k in hb]
        malos = [k for k in comunes if h[k] != hb[k]]
        faltan = [k for k in hb if k not in h]
        total += len(comunes); dist += len(malos)
        informe[iid] = {"cuadros": len(comunes), "distintos": len(malos), "primeros": malos[:10], "sin_comparar": len(faltan)}
    return {"cuadros_comparados": total, "cuadros_distintos": dist, "identicos": dist == 0, "por_item": informe}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--nivel", choices=["rapido", "completo"], required=True)
    ap.add_argument("--motor", default="/home/claude/escena/escena.html")
    ap.add_argument("--items")
    ap.add_argument("--salida")
    ap.add_argument("--base")
    ap.add_argument("--diferencias")
    ap.add_argument("--reemplazar-datos", help="solo para pruebas de mutación: ITEM=RUTA")
    a = ap.parse_args()
    its = items_del_corpus(a.items.split(",") if a.items else None)
    if a.reemplazar_datos:
        iid, ruta = a.reemplazar_datos.split("=", 1)
        for it in its:
            if it["id"] == iid: it["datos"] = pathlib.Path(ruta)
    base = json.loads(pathlib.Path(a.base).read_text()) if a.base else None
    t0 = time.time()
    act = medir(a.motor, its, a.nivel, a.diferencias, base["items"] if base else None)
    act["meta"]["segundos"] = round(time.time() - t0, 1)
    if a.salida:
        pathlib.Path(a.salida).write_text(json.dumps(act, indent=0))
    print(f"motor {act['meta']['motor_sha256'][:16]} · {sum(len(v) for v in act['items'].values())} cuadros · {act['meta']['segundos']} s")
    if base:
        c = comparar(act, base)
        print(json.dumps({k: v for k, v in c.items() if k != "por_item"}, ensure_ascii=False))
        for iid, r in c["por_item"].items():
            print(f"  {iid:9} {r}")
        sys.exit(0 if c["identicos"] else 1)
