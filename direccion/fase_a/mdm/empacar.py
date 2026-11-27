"""MDM 18h · paquete para publicar: video final + portada + texto + ficha, con los nombres y el formato del canal.
Uso: python3 empacar.py CARPETA_FINAL   (el video ya montado debe estar ahí)"""
import sys, json, pathlib, subprocess
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); import guion
F = pathlib.Path(sys.argv[1])
HORA, PUB = "18", "Vie 27/11 18:00"
TITULO = "Nike's DIRTIEST Deal? 👟😳"                      # aprobado por Tao el 25-nov
NOMBRE = f"{HORA}h - " + TITULO.rsplit(" ", 1)[0].replace(":", "")
video = F / f"{NOMBRE}.mp4"; assert video.exists(), video
# portada: el "$35" del gancho con las palabras fuertes del título (mismo patrón que PAID PEANUTS o LOST EVERYTHING)
subprocess.run([sys.executable, "/home/claude/escena/portada.py", str(video), "3.6", "DIRTIEST DEAL?", str(F / f"{NOMBRE}.portada.jpg")], check=True, capture_output=True)
# texto: misma descripción, firma y etiquetas que el video de Nike del 25-nov
subprocess.run([sys.executable, "/home/claude/txt.py", str(F / f"{NOMBRE}.txt"), PUB, TITULO, "And that's only half the story. 👟",
                "💸 Million Dollar Mistake · Big ideas. Bigger mistakes.", "#Shorts #MillionDollarMistake #business #money #Nike"], check=True, capture_output=True)
d = json.loads((AQUI / "datos.json").read_text())
ficha = {"gancho": guion.F[0], "texto_pantalla": "DIRTIEST DEAL?", "tema": TITULO, "micronicho": "Lo vendió por $X", "formato": "pelicula",
         "voz": "bm_george 1.25", "musica": "deep", "duracion_s": round(d["T"]["fin"], 1), "pregunta_cierre": d["cierre"], "idioma": "en",
         "lote": "MDM18_FASEA", "metodo": "paquete de producción (doc 29), dirección V4"}
(F / "MillionDollarMistake_MDM18_FASEA_18h.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=1))
print(NOMBRE); print((F / f"{NOMBRE}.txt").read_text())
