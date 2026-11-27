"""Lote posterior a MDM · herramientas comunes a todos los videos (doc 29: paquete cerrado, producción de corrido).
Cada video vive en direccion/lote/<id>/ con video.py (guion oficial, planos, claves, cierre, sonido, paquete) y bloque.js (sus escenas).
No modifica el motor ni el pipeline de producción: arma una COPIA del motor con base.js y el bloque del video.
Uso: python3 kit.py <id> voz | datos | instalar | render | revisar | montar | empacar | todo"""
import sys, json, pathlib, subprocess, importlib.util, os, base64, shutil
AQUI = pathlib.Path(__file__).resolve().parent
RAMA = AQUI.parents[1]
sys.path.insert(0, str(RAMA / "escena")); sys.path.insert(0, str(RAMA / "d24"))

def cargar(vid):
    d = AQUI / vid
    sp = importlib.util.spec_from_file_location("video_" + vid, d / "video.py"); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    m.DIR = d; m.MOTOR = pathlib.Path("/tmp/rr.lote_" + vid); m.TMP = pathlib.Path("/tmp/fv2/lote/" + vid); m.TMP.mkdir(parents=True, exist_ok=True)
    return m

def voz(v):
    (v.DIR / "voz").mkdir(exist_ok=True)
    V = []
    for f in v.F:
        for a, b in v.REEMPLAZOS: f = f.replace(a, b)
        V.append(f)
    g = {"titulo": v.TITULO, "lote": v.LOTE, "marca": v.MARCA, "tema": v.TEMA, "pausa_larga_antes": v.PAUSAS, "frases": v.F, "frases_voz": V}
    (v.DIR / "voz" / "src.json").write_text(json.dumps(g, ensure_ascii=False))
    nombre, vel, lang = v.VOZ
    subprocess.run([sys.executable, str(RAMA / "escena" / "voz_local.py"), str(v.DIR / "voz" / "src.json"), str(v.DIR / "voz" / "vz.wav"), nombre, str(vel), lang, "0.12"],
                   check=True, capture_output=True, cwd=str(RAMA / "escena"))
    pal = json.loads((v.DIR / "voz" / "vz_palabras.json").read_text())
    print("voz:", nombre, vel, lang, "·", round(pal[-1]["f"], 2), "s")

def tiempos(v):
    from armar_escena import alinear, bloques, inicio
    pal = json.loads((v.DIR / "voz" / "vz_palabras.json").read_text())
    D = round(pal[-1]["f"] + 1.6, 2)
    tok, tie = alinear(v.F, pal)
    ini = [inicio(tok, tie, i) for i in range(len(v.F))]
    def w(linea, palabra, n=0):
        a, b = ini[linea - 1], (ini[linea] if linea < len(v.F) else 1e9)
        c = [p for p in pal if a - 1e-6 <= p["i"] < b - 1e-6 and p["w"].lower().startswith(palabra.lower())]
        assert len(c) > n, f"no encuentro '{palabra}' ({n}) en la línea {linea}"
        return c[n]["i"]
    return pal, D, tok, tie, ini, w

def datos(v, mostrar=True):
    from armar_escena import bloques
    from comun import perfil_de
    pal, D, tok, tie, ini, w = tiempos(v)
    fr = bloques(v.F, tok, tie, D)
    T = {"fin": D, "s_fin": D}
    def clave(e):                                   # ("L", n[, desfase]) inicio de la línea n · (n, "palabra"[, k][, desfase])
        if e[0] == "L": return ini[e[1] - 1] + (e[2] if len(e) > 2 else -0.12)
        n = e[2] if len(e) > 2 and isinstance(e[2], int) else 0
        off = e[-1] if isinstance(e[-1], float) else 0.0
        return w(e[0], e[1], n) + off
    for k, e in v.CLAVES.items(): T[k] = clave(e)
    zonas, pan = [], []
    for i, (pl, st, corte, razon) in enumerate(v.PLANOS):
        Lx = 100000 + 2600 * i
        if corte: T["c" + pl] = clave(corte)
        zonas.append({"x0": Lx, "x1": Lx + 1300, "cam": Lx, "set": f"dc_{v.ID}_{st}", "entorno": f"dc_{v.ID}_{st}", "transicion": "inicio" if i == 0 else "corte",
                      "camara": "fija", "acabado": "ninguno", "razon": razon, **({"k": "c" + pl} if i else {})})
        pan.append({"k": -1, "x": Lx, "corte": 1, "dur": 0.04, "efecto": "ninguno"} if i == 0 else {"k": "c" + pl, "x": Lx, "corte": 1, "dur": 0.04, "dir": 1, "efecto": "ninguno"})
    escena = {"tipo": "pelicula", "desde": "0", "luz": False, "p27_fija": True, "escala": 1.24, "zoom": [{"k": -1, "s": 1.0, "dur": .01, "y": 1200}],
              "zonas": zonas, "pan": pan, "props": [], "actores": [], "fondos": perfil_de(v.MARCA)}
    d = {"frases": fr, "T": T, "marca": v.MARCA, "tema": v.TEMA, "escenas": [escena], "p27_fija": True, "fondos": escena["fondos"]}
    d.update(v.CIERRE)
    (v.DIR / "datos.json").write_text(json.dumps(d, ensure_ascii=False))
    if mostrar:
        print("líneas:", " · ".join(f"{i+1}:{ini[i]:.2f}" for i in range(len(v.F))), "· fin", D)
        print("T:", " ".join(f"{k}={x:.2f}" for k, x in sorted(T.items(), key=lambda q: q[1])))
    return d

def instalar(v):
    dst = v.MOTOR; dst.mkdir(parents=True, exist_ok=True)
    s = (RAMA / "escena" / "escena.html").read_text(encoding="utf-8")
    marca = "// ===== P27 · FIN =====\n</script>"
    assert s.count(marca) == 1 and "DC ·" not in s
    b = (AQUI / "base.js").read_text() + "\n" + (v.DIR / "bloque.js").read_text()
    (dst / "escena.html").write_text(s.replace(marca, marca + "\n" + b), encoding="utf-8")
    for f in list((RAMA / "escena").glob("*.ttf")) + [RAMA / "escena" / "render.py"]: shutil.copy(f, dst / f.name)

def render(v, t0=0, t1=None, salida=None):
    T = json.loads((v.DIR / "datos.json").read_text())["T"]
    salida = salida or v.TMP / "mudo.mp4"
    subprocess.run(["flock", "/tmp/render.lock", sys.executable, "render.py", str(t0), str(t1 or T["fin"]), "30", str(salida), str(v.DIR / "datos.json")],
                   check=True, capture_output=True, cwd=str(v.MOTOR))
    return salida

def revisar(v):
    T = json.loads((v.DIR / "datos.json").read_text())["T"]; n = int(T["fin"] * 30)
    r = subprocess.run(["flock", "/tmp/render.lock", sys.executable, str(RAMA / "herramientas" / "inspeccion_fondos.py"), str(v.DIR / "datos.json"), "--motor", str(v.MOTOR / "escena.html"),
                        "--t0", "0", "--cuadros", str(n), "--video", str(v.TMP / "mudo.mp4"), "--salida", str(v.TMP / "insp.json"), "--hoja", str(v.TMP / "insp.png")], capture_output=True, text=True)
    lin = [l for l in r.stdout.split("\n") if l.strip() and "cuadros ·" not in l or "· perfil" in l]
    print("inspección (salida %d):" % r.returncode, " | ".join(x.strip() for x in lin[:4])[:400])
    r2 = subprocess.run([sys.executable, str(RAMA / "herramientas" / "validar.py"), str(v.DIR / "datos.json"), "--salida", str(v.TMP / "val.json")], capture_output=True, text=True)
    print("validador:", r2.stdout.strip().split("\n")[-1][-70:])
    r3 = subprocess.run([sys.executable, str(RAMA / "herramientas" / "saltos.py"), str(v.TMP / "mudo.mp4"), "--datos", str(v.DIR / "datos.json"), "--t0", "0"], capture_output=True, text=True)
    print("aislados:", r3.stdout.strip().split("\n")[0][-60:])
    return r.returncode

def montar(v, mudo=None, salida=None):
    import numpy as np, soundfile as sf, armar_escena as A, musica
    from scipy.ndimage import maximum_filter1d, uniform_filter1d
    SR, SON = A.SR, A.SON
    mudo = mudo or v.TMP / "mudo.mp4"; salida = salida or v.TMP / "montado.mp4"
    T = json.loads((v.DIR / "datos.json").read_text())["T"]; D = T["fin"]
    fx = np.zeros(int(D * SR) + SR, np.float32)
    for k, off, f, dur, g in v.SFX:
        x = A.leer(SON / f)
        if dur: x = A.recorte(x, dur, .12)
        A.poner(fx, x, max(0, (0 if k == "0" else T[k]) + off), g)
    fx = fx[: int(D * SR)]
    vz = A.leer(v.DIR / "voz" / "vz.wav")
    musica.CARPETA = SON / "musica"
    mus, info = musica.generar(D, v.LOTE + "_escena", "deep")
    n = int(D * SR); vv = np.zeros(n, np.float32); vv[: min(n, len(vz))] = vz[:n]; m = np.zeros(n, np.float32); m[: min(n, len(mus))] = mus[:n]
    env = np.abs(vv); kk = int(0.25 * SR); env = np.convolve(env, np.ones(kk) / kk, mode="same")
    adel = int(0.22 * SR); env = np.maximum(env, np.concatenate([env[adel:], np.zeros(adel, env.dtype)]))
    duck = 1 - 0.55 * np.clip(env / (env.max() * 0.25 + 1e-6), 0, 1)
    ev = uniform_filter1d(maximum_filter1d(np.abs(vv), int(0.012 * SR)), int(0.06 * SR)); hab = ev[ev > ev.max() * 0.05]
    if len(hab):
        thr = float(np.percentile(hab, 70)); g_ = np.where(ev > thr, (thr / np.maximum(ev, 1e-9)) ** (1 - 1 / 3.0), 1.0)
        vv = vv * uniform_filter1d(g_, int(0.03 * SR)).astype(np.float32)
    mez = vv + m * 0.22 * duck + fx
    tmp = pathlib.Path(str(salida) + ".wav"); sf.write(tmp, mez / max(1.0, np.abs(mez).max() / 0.95), SR)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(tmp), "-af", "loudnorm=I=-14:TP=-2:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    med = json.loads(r[r.rindex("{"): r.rindex("}") + 1])
    ln = f"volume={-14.0 - float(med['input_i']):.2f}dB,alimiter=limit=0.84:level=false:attack=5:release=150"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mudo), "-i", str(tmp), "-af", ln, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", "-movflags", "+faststart", str(salida)], check=True)
    tmp.unlink()
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(salida), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    i = r.rindex("Integrated loudness"); print("volumen:", " ".join(r[i:i + 60].split()))
    return salida

def empacar(v, carpeta=None):
    F = pathlib.Path(carpeta or f"/mnt/user-data/outputs/lote/{v.CANAL}"); F.mkdir(parents=True, exist_ok=True)
    nombre = f"{v.HORA}h - " + v.TITULO.rsplit(" ", 1)[0].replace(":", "")
    video = F / f"{nombre}.mp4"; shutil.copy(v.TMP / "montado.mp4", video)
    subprocess.run([sys.executable, "/home/claude/escena/portada.py", str(video), str(v.PORTADA[1]), v.PORTADA[0], str(F / f"{nombre}.portada.jpg")], check=True, capture_output=True)
    subprocess.run([sys.executable, "/home/claude/txt.py", str(F / f"{nombre}.txt"), v.PUBLICAR, v.TITULO, v.DESC, v.FIRMA, v.TAGS], check=True, capture_output=True)
    d = json.loads((v.DIR / "datos.json").read_text())
    ficha = {"gancho": v.F[0], "texto_pantalla": v.PORTADA[0], "tema": v.TITULO, "formato": "pelicula", "voz": f"{v.VOZ[0]} {v.VOZ[1]}", "musica": "deep",
             "duracion_s": round(d["T"]["fin"], 1), "pregunta_cierre": d.get("cierre"), "idioma": "es" if v.VOZ[2] == "es" else "en", "lote": v.LOTE,
             "metodo": "paquete de producción (doc 29)"}
    (F / f"{v.CANAL}_{v.LOTE}_{v.HORA}h.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=1))
    print("paquete:", F / nombre); return F, nombre

if __name__ == "__main__":
    v = cargar(sys.argv[1]); paso = sys.argv[2]
    if paso in ("voz", "todo"): voz(v)
    if paso in ("datos", "voz", "todo"): datos(v)
    if paso in ("instalar", "todo"): instalar(v)
    if paso in ("render", "todo"): datos(v, False); instalar(v); print("render:", render(v))
    if paso in ("revisar", "todo"): revisar(v)
    if paso in ("montar", "todo"): montar(v)
    if paso in ("empacar",): empacar(v)
