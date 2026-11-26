"""E0 · congela el corpus de referencia (26-nov-2026). Se corre una sola vez; después el corpus queda en solo lectura.
Copia, sin modificar, las entradas exactas de los 7 videos entregados el 25-nov (desde la carpeta temporal del render que los
produjo) y de los planos aprobados 04, 05, 06 y 10, y escribe un manifiesto con la suma sha256 de cada archivo."""
import json, hashlib, shutil, subprocess, pathlib, datetime
H = pathlib.Path("/home/claude"); C = H / "pruebas/corpus"; REF = H / "pruebas/referencias_video"   # los videos no van a git
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def md5v(p):   # huella del flujo de video decodificado (independiente del contenedor mp4)
    return subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-map", "0:v", "-f", "md5", "-"], capture_output=True, text=True).stdout.strip().split("=")[-1]
def cuadros(p): return int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets", "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip())
PROD = [  # slot, carpeta del render que produjo el video entregado, id, canal, video entregado
 ("wd2", "7dTU", "D2026112502", "DogDecoded", "21h - STOP Buying RED TOYS For Your Dog"),
 ("wk2", "1xtx", "K2026112502", "CatDecoded", "21h - YOUR CAT SECRETLY SPEAKS TO YOU"),
 ("wc1", "AonJ", "C2026112501", "ChiChibitsTV", "21h - Why Coffee Makes You RUN to the Bathroom"),
 ("wm2", "wCc0", "M2026112502", "MillionDollarMistake", "21h - Blockbuster LOST Everything in ONE Decision"),
 ("wr1", "CSa7", "R2026112501", "TheRabbitLoop", "22h - THE PENTAGON CONFIRMED THIS VIDEO IS REAL"),
 ("wge2", "COgH", "G2026112502en", "TheViceVerseGG", "21h - GTA 6 Just HUMILIATED Hollywood"),
 ("wgs1", "7vRY", "G2026112501", "ViceVersoGG", "22h - GTA 5 HUMILLÓ a GTA 6")]
PLANOS = [  # plano, carpeta, versión aprobada, generador, extras
 ("04", "p04", "plano04_v2", "gen04.py", []), ("05", "p05", "plano05_v3", "gen05.py", ["datos_testigo.json", "datos_control.json"]),
 ("06", "p06", "plano06_v2", "gen06.py", ["datos_testigo.json"]), ("10", "p10", "plano10_v4", "gen10.py", [])]
man = {"creado": datetime.datetime.now().isoformat(timespec="seconds"), "nota": "Corpus de referencia de la E0. Solo lectura. Cambiarlo requiere autorización de Tao.",
       "motor_entrega_25nov": None, "items": []}
# motor con que se renderizaron los 7 videos entregados (idéntico en las 7 carpetas de render)
me = C / "motor_entrega_25nov"; me.mkdir(parents=True, exist_ok=True)
for f in ["escena.html", "Poppins-Bold.ttf", "Poppins-Regular.ttf"]: shutil.copy2(f"/tmp/rw.7dTU/{f}", me / f)
man["motor_entrega_25nov"] = {"carpeta": "motor_entrega_25nov", "escena.html": sha(me / "escena.html"), "igual_a": "escena/escena.html.bak_p27_paso0"}
REF.mkdir(parents=True, exist_ok=True)
for slot, rw, id_, canal, nombre in PROD:
    d = C / "produccion" / slot; d.mkdir(parents=True, exist_ok=True); s = H / "d24" / slot
    shutil.copy2(f"/tmp/rw.{rw}/_tmp/datos.json", d / "datos_render.json")          # datos EXACTOS con que se renderizó
    for f in [f"{id_}.json", f"{id_}_src.json", "b.py", "vz.wav", "vz_palabras.json", "planos.log", "ficha.json", f"{slot}.txt"]:
        if (s / f).exists(): shutil.copy2(s / f, d / f)
    ent = pathlib.Path(f"/mnt/user-data/outputs/d25/{canal}/{nombre}.mp4"); dst = REF / f"{slot}_entregado.mp4"; shutil.copy2(ent, dst)
    man["items"].append({"id": slot, "tipo": "produccion", "lote": id_, "canal": canal, "titulo_archivo": nombre,
        "origen": {"datos_render": f"/tmp/rw.{rw}/_tmp/datos.json", "slot": str(s), "video_entregado": str(ent)},
        "render": {"t0": 0.0, "fps": 30, "cuadros": cuadros(dst)}, "motor_de_origen": man["motor_entrega_25nov"]["escena.html"],
        "video": {"archivo": f"referencias_video/{dst.name}", "sha256": sha(dst), "md5_video": md5v(dst)},
        "archivos": {f.name: {"sha256": sha(f), "bytes": f.stat().st_size} for f in sorted(d.iterdir())}})
for pl, car, ver, gen, extras in PLANOS:
    d = C / "planos" / pl; d.mkdir(parents=True, exist_ok=True); s = H / "prueba27" / car
    for f in ["datos.json", "src.json", "vz.wav", "vz_palabras.json", gen] + extras:
        if (s / f).exists(): shutil.copy2(s / f, d / f)
    dst = REF / f"plano{pl}_aprobado.mp4"; shutil.copy2(s / f"{ver}.mp4", dst)
    man["items"].append({"id": f"plano{pl}", "tipo": "plano", "version_aprobada": ver, "origen": {"carpeta": str(s)},
        "render": {"t0": 0.15, "fps": 30, "cuadros": cuadros(dst)},
        "video": {"archivo": f"referencias_video/{dst.name}", "sha256": sha(dst), "md5_video": md5v(dst)},
        "archivos": {f.name: {"sha256": sha(f), "bytes": f.stat().st_size} for f in sorted(d.iterdir())}})
(C / "manifiesto.json").write_text(json.dumps(man, ensure_ascii=False, indent=1))
for it in man["items"]: print(f'{it["id"]:9} {it["tipo"]:10} cuadros {it["render"]["cuadros"]:5}  archivos {len(it["archivos"])}')
