#!/usr/bin/env python3
"""
Registro de las CONDICIONES EXACTAS de cada render de referencia (pedido de Tao, 26-nov 11:15).

No copia datos.json al corpus: anota, para cada slot, la versión exacta usada (ruta en git, commit,
id del objeto git y sha256), junto con todo lo demás que define el render: carpeta de render
(cada archivo con su sha256 y su ruta en git), entradas congeladas en el corpus, voz, música,
parámetros de render, motor, modelo de voz y entorno.

  registrar      → escribe pruebas/condiciones_render.json (una sola vez; después queda en solo lectura)
  verificar      → comprueba cada sha256 del registro contra git y el corpus (no escribe nada)
  reconstruir SLOT DESTINO → arma en una carpeta NUEVA las entradas exactas del render (falla si existe)

Solo lee el repositorio y el corpus. Nunca modifica escenas, configuraciones, renders ni el motor.
"""
import argparse, hashlib, json, pathlib, subprocess, sys

RAIZ = pathlib.Path("/home/claude")
AQUI = pathlib.Path(__file__).parent
CORPUS = AQUI / "corpus"
REGISTRO = AQUI / "condiciones_render.json"
ETIQUETA = "estado-inicial-2026-11-26"   # estado exacto del 26-nov antes de cualquier cambio
CARPETAS_RENDER = {"wd2": "rw.7dTU", "wk2": "rw.1xtx", "wc1": "rw.AonJ", "wm2": "rw.wCc0",
                   "wr1": "rw.CSa7", "wge2": "rw.COgH", "wgs1": "rw.7vRY"}
SCRIPTS = ["d24/uno2.sh", "d24/q2.sh", "hacer.sh", "datos_de.sh", "resolver.py", "d24/post.py",
           "planos_shorts.py", "render_par.sh", "d24/formato.py"]
MODELO = pathlib.Path("/mnt/user-data/uploads/gta-shorts/models")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*a, binario=False):
    r = subprocess.run(["git", "-C", str(RAIZ), *a], capture_output=True, check=True)
    return r.stdout if binario else r.stdout.decode().strip()


def en_git(ruta, commit):
    """sha256 e id de objeto de un archivo tal como está en ese commit (None si no existe)."""
    try:
        return {"ruta_git": ruta, "blob": git("rev-parse", f"{commit}:{ruta}"),
                "sha256": sha(git("show", f"{commit}:{ruta}", binario=True))}
    except subprocess.CalledProcessError:
        return None


def ruta_git_de(nombre):
    if nombre == "escena.html":
        return "escena/escena.html.bak_p27_paso0"   # el motor de entrega del 25-nov
    return f"escena/{nombre}"


def inventario_render(carpeta, commit):
    """Cada archivo que usó el render (sin _tmp ni __pycache__), con su sha256 y su ruta en git."""
    inv, faltan = {}, []
    for p in sorted(carpeta.rglob("*")):
        rel = p.relative_to(carpeta).as_posix()
        if not p.is_file() or rel.startswith(("_tmp/", "__pycache__/")) or "/__pycache__/" in rel:
            continue
        s = sha(p.read_bytes()); g = en_git(ruta_git_de(rel), commit)
        inv[rel] = {"sha256": s, "ruta_git": g["ruta_git"] if g else None, "igual_a_git": bool(g and g["sha256"] == s)}
        if not inv[rel]["igual_a_git"]:
            faltan.append(rel)
    return inv, faltan


def registrar(a):
    if REGISTRO.exists():
        sys.exit(f"{REGISTRO.name} ya existe: es una referencia y no se reescribe sin autorización de Tao")
    commit = git("rev-list", "-n1", ETIQUETA)
    man = json.loads((CORPUS / "manifiesto.json").read_text())
    entorno = (AQUI / "entorno.txt").read_text()
    reg = {"creado": subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True).stdout.strip(),
           "nota": "Condiciones exactas de cada render de referencia. Solo lectura: cambiarlo requiere autorización de Tao.",
           "etiqueta": ETIQUETA, "commit": commit,
           "scripts_pipeline": {s: en_git(s, commit) for s in SCRIPTS},
           "modelo_voz": {f.name: {"bytes": f.stat().st_size, "sha256": sha(f.read_bytes())} for f in sorted(MODELO.glob("*"))},
           "entorno": entorno, "slots": {}, "planos": {}}
    for it in man["items"]:
        if it["tipo"] != "produccion":
            continue
        slot, lote = it["id"], it["lote"]
        ficha = json.loads((CORPUS / "produccion" / slot / "ficha.json").read_text())
        voz, vel = ficha["voz"].split()
        rw = pathlib.Path("/tmp") / CARPETAS_RENDER[slot]
        inv, faltan = inventario_render(rw, commit) if rw.exists() else ({}, ["(carpeta de render no disponible)"])
        salidas = {}
        for nom in ("datos.json", "video.mp4", "mezcla.wav"):
            p = rw / "_tmp" / nom
            if p.exists():
                salidas[f"_tmp/{nom}"] = sha(p.read_bytes())
        reg["slots"][slot] = {
            "lote": lote, "canal": it["canal"], "titulo_archivo": it["titulo_archivo"],
            "datos_slot": {"datos.json": en_git(f"d24/{slot}/datos.json", commit),
                           "datos0.json": en_git(f"d24/{slot}/datos0.json", commit),
                           "nota": "marcadores T de la voz; post.py y planos_shorts.py los leen. Igual a datos0.json"},
            "entradas_corpus": {n: d["sha256"] for n, d in it["archivos"].items()},
            "entradas_en_git": {n: en_git(f"d24/{slot}/{n}", commit) for n in
                                (f"{lote}_src.json", f"{lote}.json", "b.py", "vz_palabras.json", "planos.log", "ficha.json")},
            "comando": {"encolar": f"d24/q2.sh {slot} {lote} {voz} {vel} {ficha.get('idioma', 'en')}",
                        "pipeline": "uno2.sh: b.py → hacer.sh (voz, datos_de.sh, resolver.py) → post.py → planos_shorts.py → render_par.sh",
                        "render": f"render_par.sh {lote}.json vz.wav vz_palabras.json v1.mp4 {ficha.get('musica', 'deep')}"},
            "voz": {"voz": voz, "velocidad": float(vel), "idioma": ficha.get("idioma"), "pausa": 0.12, "joven": False,
                    "modelo": "kokoro-v1.0 (ver modelo_voz)"},
            "musica": {"estilo": ficha.get("musica", "deep"), "azar": "con semilla fija (musica.py: md5 de la semilla; armar_escena.py: el lote; sintet_sfx.py: 7)"},
            "render": {"t0": it["render"]["t0"], "fps": it["render"]["fps"], "cuadros": it["render"]["cuadros"],
                       "cuadro": "JPEG calidad 0.92 → ffmpeg libx264 -preset veryfast -crf 20 yuv420p (render.py)",
                       "azar_del_motor": "Math.random sin semilla en el grano del acabado pro (no reproducible bit a bit)"},
            "motor": {"sha256": it["motor_de_origen"], "ruta_git": "escena/escena.html.bak_p27_paso0",
                      "copia_corpus": "corpus/motor_entrega_25nov/escena.html"},
            "carpeta_render": {"origen": str(rw), "archivos": inv, "distintos_de_git": faltan},
            "salidas_render": salidas,
            "video_entregado": it["video"]}
    for it in man["items"]:
        if it["tipo"] == "produccion":
            continue
        n = it["id"].replace("plano", "")
        reg["planos"][it["id"]] = {
            "entradas_corpus": {k: d["sha256"] for k, d in it["archivos"].items()},
            "bloque_p27": en_git("prueba27/p27_bloque.js", commit),
            "motor": {"sha256": sha((RAIZ / "escena/escena.html").read_bytes()), "ruta_git": "escena/escena.html",
                      "nota": "el motor actual reproduce el video aprobado cuadro a cuadro (camino real, E0)"},
            "render": {"t0": it["render"]["t0"], "fps": it["render"]["fps"], "cuadros": it["render"]["cuadros"],
                       "comando": f"render.py 0.15 <fin> 30 con prueba27/p{n}/datos.json"},
            "video_aprobado": it["video"]}
    REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=1))
    REGISTRO.chmod(0o444)
    malos = {s: v["carpeta_render"]["distintos_de_git"] for s, v in reg["slots"].items() if v["carpeta_render"]["distintos_de_git"]}
    print(f"registro escrito: {REGISTRO} · {len(reg['slots'])} slots · {len(reg['planos'])} planos · commit {commit[:7]}")
    print("archivos de render distintos de git:", malos or "ninguno")


def verificar(a):
    reg = json.loads(REGISTRO.read_text()); commit = reg["commit"]; malos = []
    def chk(etq, d):
        if d is None:
            malos.append(f"{etq}: no está en git"); return
        g = en_git(d["ruta_git"], commit)
        if not g or g["sha256"] != d["sha256"] or g["blob"] != d.get("blob", g["blob"]):
            malos.append(f"{etq}: distinto de git")
    for s, d in reg["scripts_pipeline"].items():
        chk(f"script {s}", d)
    man = json.loads((CORPUS / "manifiesto.json").read_text()); arch = {it["id"]: it["archivos"] for it in man["items"]}
    n = 0
    for slot, v in reg["slots"].items():
        for k in ("datos.json", "datos0.json"):
            chk(f"{slot} {k}", v["datos_slot"][k]); n += 1
        for nom, d in v["entradas_en_git"].items():
            chk(f"{slot} {nom}", d); n += 1
        for nom, s in v["entradas_corpus"].items():
            p = CORPUS / "produccion" / slot / nom; n += 1
            if not p.exists() or sha(p.read_bytes()) != s or arch[slot][nom]["sha256"] != s:
                malos.append(f"{slot} corpus/{nom}: distinto")
        for rel, d in v["carpeta_render"]["archivos"].items():
            g = en_git(d["ruta_git"], commit); n += 1
            if not g or g["sha256"] != d["sha256"]:
                malos.append(f"{slot} render/{rel}: distinto de git")
        if v["salidas_render"].get("_tmp/datos.json") not in (None, v["entradas_corpus"]["datos_render.json"]):
            malos.append(f"{slot}: datos del render ≠ datos_render.json del corpus")
    for f, d in reg["modelo_voz"].items():
        p = MODELO / f; n += 1
        if not p.exists() or p.stat().st_size != d["bytes"]:
            malos.append(f"modelo {f}: falta o cambió de tamaño")
    print(f"comprobados {n} archivos del registro · " + ("TODO IGUAL" if not malos else f"{len(malos)} DIFERENCIAS"))
    for m in malos[:20]:
        print("  ", m)
    sys.exit(0 if not malos else 1)


def reconstruir(a):
    reg = json.loads(REGISTRO.read_text()); v = reg["slots"][a.slot]; commit = reg["commit"]
    D = pathlib.Path(a.destino)
    if D.exists():
        sys.exit(f"{D} ya existe: la reconstrucción solo escribe en una carpeta nueva")
    (D / "render").mkdir(parents=True); (D / "slot").mkdir()
    for rel, d in v["carpeta_render"]["archivos"].items():          # la carpeta de render, desde git
        p = D / "render" / rel; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(git("show", f"{commit}:{d['ruta_git']}", binario=True))
    for k in ("datos.json", "datos0.json"):                          # marcadores del slot, desde git
        (D / "slot" / k).write_bytes(git("show", f"{commit}:{v['datos_slot'][k]['ruta_git']}", binario=True))
    for nom in v["entradas_corpus"]:                                 # entradas congeladas, desde el corpus
        (D / "slot" / nom).write_bytes((CORPUS / "produccion" / a.slot / nom).read_bytes())
    malos = [rel for rel, d in v["carpeta_render"]["archivos"].items() if sha((D / "render" / rel).read_bytes()) != d["sha256"]]
    malos += [k for k in ("datos.json", "datos0.json") if sha((D / "slot" / k).read_bytes()) != v["datos_slot"][k]["sha256"]]
    malos += [n for n, s in v["entradas_corpus"].items() if sha((D / "slot" / n).read_bytes()) != s]
    total = len(v["carpeta_render"]["archivos"]) + 2 + len(v["entradas_corpus"])
    (D / "LEEME.txt").write_text(
        f"Reconstrucción exacta del render de {a.slot} ({v['lote']}, {v['canal']}).\n"
        f"render/ = la carpeta de render (motor de entrega incluido); slot/ = guion, voz, palabras, marcadores y datos del render.\n"
        f"Volver a renderizar el video tal cual: cd render && cp ../slot/datos_render.json . && python3 render.py "
        f"{v['render']['t0']} <duración> {v['render']['fps']}  (el grano del acabado pro es aleatorio sin semilla).\n"
        f"Comando original: {v['comando']['encolar']}\n")
    print(f"{a.slot}: {total} archivos reconstruidos en {D} · " + ("todos con su sha256" if not malos else f"DISTINTOS: {malos}"))
    sys.exit(0 if not malos else 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("registrar"); sp.add_parser("verificar")
    r = sp.add_parser("reconstruir"); r.add_argument("slot"); r.add_argument("destino")
    a = ap.parse_args(); {"registrar": registrar, "verificar": verificar, "reconstruir": reconstruir}[a.cmd](a)
