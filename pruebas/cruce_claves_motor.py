#!/usr/bin/env python3
"""
E1 · Cruce del validador con el MOTOR REAL (la verdad de referencia).

Abre el motor de referencia en Chrome con unos datos, envuelve su función tk() SOLO EN LA MEMORIA DE LA PÁGINA
(el archivo del motor no se toca) y dibuja cuadros cada 0,2 s (cada cuadro en los planos). Anota cada clave de texto
que el motor no pudo resolver y que reemplazó por el inicio de la escena. Después compara esa lista con la del
validador estático (herramientas/validar.py):
  · lo que el motor no resolvió y el validador no vio  → FALSO NEGATIVO del validador
  · lo que el validador marca y el motor nunca evaluó  → se informa (campo que en ese momento no se dibuja)
Uso: python3 cruce_claves_motor.py [--salida informe.json]      (con flock /tmp/render.lock: abre el navegador)
"""
import copy, json, pathlib, re, sys, time
sys.path.insert(0, "/home/claude/herramientas"); sys.path.insert(0, str(pathlib.Path(__file__).parent))
from playwright.sync_api import sync_playwright
import validar as V
import mutaciones_claves as M

MOTOR = pathlib.Path("/home/claude/escena/escena.html")
C = pathlib.Path(__file__).parent / "corpus"
ENVOLVER = """(()=>{const orig=tk;window.__NR={};window.__N=0;
 tk=function(k,a){window.__N++;if(typeof k==='string'&&T[k]===undefined){const m=/^(.+?)([+-][0-9.]+)$/.exec(k);
   if(!(m&&T[m[1]]!==undefined))window.__NR[k]=(window.__NR[k]||0)+1}return orig(k,a)};return typeof tk})()"""


def casos():
    out = [(f"corpus {p.parent.name}/{p.name}", json.loads(p.read_text())) for p in sorted(C.glob("produccion/*/datos_render.json"))]
    out += [(f"corpus plano{p.parent.name}/{p.name}", json.loads(p.read_text())) for p in sorted(C.glob("planos/*/datos*.json"))]
    v1 = pathlib.Path("/tmp/caso05v1/datos.json")
    if v1.exists():
        out.append(("caso real · plano 05 v1", json.loads(v1.read_text())))
    for nombre, cual, mut, nivel, ruta in M.CASOS:
        if nivel == "error":
            d = copy.deepcopy(M.base[cual]); mut(d); out.append((f"mutación · {nombre}", d))
    return out


def tiempos(d):
    T = d["T"]; fin = T.get("fin", max(T.values()))
    paso = 1 / 30 if fin < 8 else 0.2
    n = int(fin / paso) + 1
    return [round(0.15 + i * paso, 4) if fin < 8 else round(i * paso, 4) for i in range(n)]


def main():
    filas, fn = [], 0
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
        solo = sys.argv[sys.argv.index("--solo") + 1] if "--solo" in sys.argv else ""
        for nombre, d in [c for c in casos() if solo in c[0]]:
            t0 = time.time()
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            pg.add_init_script(f"window.DATOS={json.dumps(d, ensure_ascii=False)};")
            pg.goto(MOTOR.as_uri()); pg.wait_for_function("window.LISTO===true", timeout=30000)
            assert pg.evaluate(ENVOLVER) == "function"
            ts = tiempos(d)
            for t in ts:
                pg.evaluate(f"render({t})")
            motor_nr = set(pg.evaluate("Object.keys(window.__NR)")); llamadas = pg.evaluate("window.__N"); pg.close()
            r = V.validar_datos(d, nombre)
            est = {x["valor"] for x in r["hallazgos"] if x["nivel"] == "error" and isinstance(x["valor"], str)
                   and ("no existe en T" in x["motivo"] or "escrito como texto" in x["motivo"] or "queda sin resolver" in x["motivo"]) and not re.match(r"^escenas\[\d+\]\.desde$", x["ruta"])}
            falsos_neg = sorted(motor_nr - est)
            solo_est = sorted(est - motor_nr)
            fn += len(falsos_neg)
            filas.append({"caso": nombre, "cuadros": len(ts), "llamadas_tk": llamadas, "motor_no_resolvio": sorted(motor_nr),
                          "validador_marco": sorted(est), "falsos_negativos": falsos_neg, "marcados_no_evaluados": solo_est})
            print(f"{'✔' if not falsos_neg else '✗'} {nombre:58} {len(ts):4} cuadros · {llamadas:7} llamadas · motor sin resolver "
                  f"{len(motor_nr)} · validador {len(est)}" + (f" · FALSOS NEGATIVOS {falsos_neg}" if falsos_neg else "")
                  + (f" · marcados y no evaluados {solo_est}" if solo_est else "") + f" · {time.time() - t0:.0f} s", flush=True)
        b.close()
    print(f"falsos negativos del validador frente al motor: {fn}")
    if "--salida" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--salida") + 1]).write_text(json.dumps(filas, ensure_ascii=False, indent=1))
    sys.exit(1 if fn else 0)


if __name__ == "__main__":
    main()
