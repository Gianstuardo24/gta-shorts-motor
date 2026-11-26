#!/usr/bin/env python3
"""Prueba aislada · corte de cámara sincronizado con el corte de zona (pedido de Tao, 26-nov 14:02).

Vive en la rama de prueba `prueba-corte-sincronizado`. No toca producción, la referencia E0 ni los 7 videos:
lee el corpus congelado y escribe solo en /tmp/prueba_corte.

  datos            Corre resolver → post → planificador dos veces por slot: con el planificador de producción (ANTES)
                   y con el de la rama (DESPUÉS). Arma los datos del motor y compara: qué zooms cambiaron, que nada
                   más cambie y cuántos cuadros intermedios predice el validador en cada lado.
  render SLOT      Dibuja TODOS los cuadros del DESPUÉS (motor de la rama, semilla de prueba), guarda JPEG y huellas,
                   y los compara con la línea base completa (motor de producción + datos originales, misma semilla).
  antes SLOT       Dibuja con el motor de producción los cuadros del ANTES alrededor de cada corte (para la comparación).
  comparar SLOT    Hoja antes/después de cada corte, clip lento lado a lado y video DESPUÉS con el audio entregado.
"""
import argparse, base64, hashlib, json, pathlib, shutil, subprocess, sys

RAMA = pathlib.Path(__file__).resolve().parent.parent
VIVO = pathlib.Path("/home/claude")
sys.path.insert(0, str(RAMA / "herramientas"))
sys.path.insert(0, str(RAMA / "pruebas"))
import validar as V          # validador de la rama (entiende el zoom con "corte")
import regresion as R        # corpus, instantes de render, semilla y huella de píxeles

RESOLVER, POST = VIVO / "resolver.py", VIVO / "d24" / "post.py"
PLAN = {"antes": VIVO / "planos_shorts.py", "despues": RAMA / "planos_shorts.py"}
MOTOR = {"antes": VIVO / "escena" / "escena.html", "despues": RAMA / "escena" / "escena.html"}
OUT = pathlib.Path("/tmp/prueba_corte")
ETIQUETA = "estado-inicial-2026-11-26"
BASE_COMPLETA = RAMA / "pruebas" / "lineas_base" / "completo_motor_725e0dba.json"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def correr(cmd, cwd=None):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=cwd)
    if r.returncode != 0:
        raise RuntimeError(f"falló {cmd[1]}: {r.stderr[-400:]}")
    return r.stdout


def item(slot):
    return next(it for it in R.items_del_corpus([slot]))


def mezclados(d, t0, fps):
    out = []
    for e in d.get("escenas") or []:
        if e.get("tipo") != "pelicula":
            continue
        a, _ = V.inicio_escena(e, d["T"])
        if a is not None:
            out += V.cuadros_mezclados(e, a, d["T"], t0, fps)
    return out


def datos(slots):
    rep = {}
    for it in R.items_del_corpus(slots):
        if it["tipo"] != "produccion":
            continue
        slot, lote = it["id"], it["lote"]
        C = R.CORPUS / "produccion" / slot
        dr = json.loads((C / "datos_render.json").read_text())
        lados = {}
        for lado in ("antes", "despues"):
            D = OUT / slot / lado
            shutil.rmtree(D, ignore_errors=True); D.mkdir(parents=True)
            shutil.copyfile(C / f"{lote}_src.json", D / f"{lote}_src.json")
            shutil.copyfile(C / "vz_palabras.json", D / "vz_palabras.json")
            dj = subprocess.run(["git", "-C", str(VIVO), "show", f"{ETIQUETA}:d24/{slot}/datos.json"], capture_output=True, check=True).stdout
            (D / "datos.json").write_bytes(dj); (D / "datos0.json").write_bytes(dj)
            correr(["python3", RESOLVER, D / f"{lote}_src.json", D / "datos0.json", D / f"{lote}.json"])
            correr(["python3", POST, D, lote])
            correr(["python3", PLAN[lado], D, lote])
            g = json.loads((D / f"{lote}.json").read_text())
            d = dict(dr); d["escenas"] = g["escena"]["escenas"]          # armar_escena.py pasa "escenas" tal cual
            (D / "datos_render.json").write_text(json.dumps(d, ensure_ascii=False))
            lados[lado] = {"g": g, "d": d, "log": (D / "planos.log").read_text(), "sha": sha((D / f"{lote}.json").read_bytes())}
        A, B = lados["antes"], lados["despues"]
        t0, fps = it["render"]["t0"], it["render"]["fps"]
        r = {"antes_igual_a_lo_entregado": A["sha"] == it["archivos"][f"{lote}.json"]["sha256"],
             "antes_igual_a_datos_del_motor": A["d"]["escenas"] == dr["escenas"],
             "planos_log_igual": A["log"] == B["log"]}
        sin_zoom = lambda esc: [{k: v for k, v in e.items() if k != "zoom"} for e in esc]
        r["todo_lo_demas_igual"] = (sin_zoom(A["d"]["escenas"]) == sin_zoom(B["d"]["escenas"])
                                    and {k: v for k, v in A["d"].items() if k != "escenas"} == {k: v for k, v in B["d"].items() if k != "escenas"})
        cambios = []
        for ea, eb in zip(A["d"]["escenas"], B["d"]["escenas"]):
            za, zb = ea.get("zoom") or [], eb.get("zoom") or []
            if len(za) != len(zb):
                r["todo_lo_demas_igual"] = False; continue
            for x, y in zip(za, zb):
                if x != y:
                    resto = {k: v for k, v in x.items() if k != "k"} == {k: v for k, v in y.items() if k not in ("k", "corte")}
                    cambios.append({"antes": x["k"], "despues": y["k"], "corte": y.get("corte"), "solo_clave_y_marca": resto and y.get("corte") == 1})
        r["zooms_cambiados"] = len(cambios)
        r["solo_clave_y_marca"] = all(c["solo_clave_y_marca"] for c in cambios)
        r["cambios"] = cambios
        for lado in ("antes", "despues"):
            m = mezclados(lados[lado]["d"], t0, fps)
            r[f"intermedios_{lado}"] = {"grupos": len(m), "cuadros": sum(len(c["cuadros"]) for c in m), "detalle": m}
        rep[slot] = r
        print(f"  {slot:5} zooms cambiados {r['zooms_cambiados']:2} (solo clave y marca: {r['solo_clave_y_marca']}) · resto igual: "
              f"{r['todo_lo_demas_igual']} · planos.log igual: {r['planos_log_igual']} · antes = entregado: {r['antes_igual_a_lo_entregado']} · "
              f"intermedios previstos {r['intermedios_antes']['cuadros']:2} → {r['intermedios_despues']['cuadros']}", flush=True)
    (OUT / "datos.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1))
    return rep


def dibujar(motor, datos_json, ts, carpeta=None, jpeg=False):
    """Dibuja los instantes ts con la semilla de prueba; devuelve huellas de píxeles y, si hay carpeta, guarda las imágenes."""
    from playwright.sync_api import sync_playwright
    huellas = {}
    if carpeta:
        pathlib.Path(carpeta).mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files", "--disable-web-security"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.add_init_script(R.SEMILLA_JS)
        pg.add_init_script(f"window.DATOS={pathlib.Path(datos_json).read_text()};")
        pg.goto(pathlib.Path(motor).resolve().as_uri())
        pg.wait_for_function("window.LISTO===true", timeout=30000)
        for n, t in ts:
            pg.evaluate(f"render({t})")
            huellas[f"{t:.6f}"] = pg.evaluate(R.HUELLA_JS)
            if carpeta:
                fmt = "image/jpeg',0.92" if jpeg else "image/png'"
                url = pg.evaluate(f"document.getElementById('c').toDataURL('{fmt})")
                (pathlib.Path(carpeta) / f"{n:05d}.{'jpg' if jpeg else 'png'}").write_bytes(base64.b64decode(url.split(",", 1)[1]))
        b.close()
    return huellas


def render(slot):
    it = item(slot); r = it["render"]
    ts = [(i, round(r["t0"] + i / r["fps"], 6)) for i in range(r["cuadros"])]
    D = OUT / slot / "despues"
    h = dibujar(MOTOR["despues"], D / "datos_render.json", ts, D / "cuadros", jpeg=True)
    base = json.loads(BASE_COMPLETA.read_text())["items"][slot]
    distintos = sorted(n for n, t in ts if h[f"{t:.6f}"] != base[f"{t:.6f}"])
    rep = json.loads((OUT / "datos.json").read_text())[slot]
    previstos = sorted({n for c in rep["intermedios_antes"]["detalle"] for n in c["cuadros"]})
    res = {"slot": slot, "cuadros": len(ts), "distintos_de_la_linea_base": distintos, "previstos": previstos,
           "coinciden": distintos == previstos, "motor_despues": sha(MOTOR["despues"].read_bytes()),
           "motor_linea_base": json.loads(BASE_COMPLETA.read_text())["meta"]["motor_sha256"]}
    (D / "render.json").write_text(json.dumps(res, indent=1))
    print(f"{slot}: {len(ts)} cuadros · distintos de la línea base: {len(distintos)} · previstos: {len(previstos)} · "
          f"coinciden: {res['coinciden']} · iguales: {len(ts) - len(distintos)}")
    return res


def grupos(slot):
    rep = json.loads((OUT / "datos.json").read_text())[slot]
    gs = sorted([sorted(c["cuadros"]) for c in rep["intermedios_antes"]["detalle"]])
    return gs


def antes(slot):
    it = item(slot); r = it["render"]
    idx = sorted({i for g in grupos(slot) for i in range(g[0] - 8, g[-1] + 9) if 0 <= i < r["cuadros"]})
    ts = [(i, round(r["t0"] + i / r["fps"], 6)) for i in idx]
    h = dibujar(MOTOR["antes"], R.CORPUS / "produccion" / slot / "datos_render.json", ts, OUT / slot / "antes" / "cuadros", jpeg=True)
    base = json.loads(BASE_COMPLETA.read_text())["items"][slot]
    igual = all(h[f"{t:.6f}"] == base[f"{t:.6f}"] for _, t in ts)
    print(f"{slot}: {len(ts)} cuadros del antes · idénticos a la línea base: {igual}")
    return igual


def comparar(slot):
    from PIL import Image, ImageDraw, ImageFont
    it = item(slot); fps = it["render"]["fps"]
    A, B = OUT / slot / "antes" / "cuadros", OUT / slot / "despues" / "cuadros"
    S = OUT / slot / "comparacion"; shutil.rmtree(S, ignore_errors=True); (S / "clip").mkdir(parents=True)
    try:
        F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
        f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    except Exception:
        F = f2 = ImageFont.load_default()
    gs = grupos(slot)
    # hoja: por corte, ANTES (anterior · intermedio(s) · siguiente) arriba y DESPUÉS en los mismos cuadros abajo
    w, hh = 216, 384
    filas = []
    for g in gs:
        cols = [g[0] - 1] + g + [g[-1] + 1]
        im = Image.new("RGB", (60 + len(cols) * (w + 6), 2 * (hh + 34) + 40), (18, 18, 22)); d = ImageDraw.Draw(im)
        d.text((8, 6), f"{slot} · corte a los {f'{g[0] / fps:.2f}'.replace('.', ',')} s · cuadros {', '.join(map(str, g))}", fill=(235, 235, 235), font=F)
        for fila, (lado, carp) in enumerate((("ANTES", A), ("DESPUÉS", B))):
            y = 40 + fila * (hh + 34)
            d.text((8, y + hh // 2), lado[0], fill=(235, 235, 235), font=F)
            for j, n in enumerate(cols):
                x = 60 + j * (w + 6)
                d.rectangle([x - 3, y - 3, x + w + 2, y + hh + 2], fill=((210, 50, 50) if (lado == "ANTES" and n in g) else (60, 170, 90) if n in g else (18, 18, 22)))
                im.paste(Image.open(carp / f"{n:05d}.jpg").resize((w, hh)), (x, y))
                d.text((x + 4, y + hh + 4), f"{n} · {f'{n / fps:.3f}'.replace('.', ',')}", fill=(200, 200, 200), font=f2)
        filas.append(im)
    W = max(f.width for f in filas); H = sum(f.height for f in filas) + 8 * len(filas)
    hoja = Image.new("RGB", (W, H), (10, 10, 12)); y = 0
    for f in filas:
        hoja.paste(f, (0, y)); y += f.height + 8
    hoja.save(S / f"hoja_cortes_{slot}.png")
    # clip lento: cada corte ±8 cuadros a 1/4 de velocidad, ANTES a la izquierda y DESPUÉS a la derecha
    k = 0
    for gi, g in enumerate(gs):
        for n in range(g[0] - 8, g[-1] + 9):
            if not (A / f"{n:05d}.jpg").exists():
                continue
            im = Image.new("RGB", (1080, 1040), (12, 12, 14)); d = ImageDraw.Draw(im)
            d.text((16, 12), f"Corte {gi + 1}/{len(gs)} · {f'{g[0] / fps:.2f}'.replace('.', ',')} s · cuadro {n} · 1/4 de velocidad", fill=(235, 235, 235), font=F)
            for j, (lado, carp) in enumerate((("ANTES (producción)", A), ("DESPUÉS (rama de prueba)", B))):
                x = j * 540
                if n in g:
                    d.rectangle([x, 60, x + 539, 1039], fill=(210, 50, 50) if j == 0 else (60, 170, 90))
                im.paste(Image.open(carp / f"{n:05d}.jpg").resize((528, 939)), (x + 6, 94))
                d.text((x + 10, 62), lado, fill=(255, 255, 255), font=f2)
            for _ in range(4):
                im.save(S / "clip" / f"{k:06d}.jpg", quality=90); k += 1
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(S / "clip" / "%06d.jpg"),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", str(S / f"transiciones_antes_despues_{slot}.mp4")], check=True)
    # video DESPUÉS completo con el audio del video entregado (mismo códec que producción)
    ref = VIVO / "pruebas" / it["video"]["archivo"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(B / "%05d.jpg"), "-i", str(ref),
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "copy", str(S / f"{slot}_despues_prueba.mp4")], check=True)
    print(f"{slot}: hoja de {len(gs)} cortes, clip lento de {k} cuadros y video DESPUÉS en {S}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("paso", choices=["datos", "render", "antes", "comparar"])
    ap.add_argument("slot", nargs="?")
    a = ap.parse_args()
    if a.paso == "datos":
        datos(a.slot.split(",") if a.slot else None)
    else:
        {"render": render, "antes": antes, "comparar": comparar}[a.paso](a.slot)
