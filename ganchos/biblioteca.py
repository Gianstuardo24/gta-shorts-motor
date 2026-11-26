"""BIBLIOTECA DE VIRALES (Etapa 1): analisis PROFUNDO de los videos con mejor rendimiento real, en modo hiperobservador.

Cada video: se baja temporalmente -> se MIDE por codigo (cortes, voz, audio, loop, lo mas repetido) ->
Claude lo OBSERVA fotograma a fotograma (cada 0,5 s) + transcripcion -> ficha completa + bitacora libre -> se BORRA.
Nada de esos videos se usa en nuestros Shorts: es investigacion. Un video NUNCA se analiza dos veces.

De donde salen los videos:
  - los virales reales de inteligencia.py (datos/inteligencia.db), los mejores primero
  - hasta 5 de canales oficiales/grandes por tema (fuente de informacion)
  - links que pongas a mano en biblioteca/entrada.txt  (una linea:  URL | tema)
Uso:
  python biblioteca.py --tema gta6                 analiza hasta 30 virales + 5 grandes del tema
  python biblioteca.py --tema gta6 --n 10          menos videos
  python biblioteca.py --tema gta6 --recolectar    corre antes inteligencia.py (sin Claude) para traer virales frescos
  python biblioteca.py --manual                    solo los links de biblioteca/entrada.txt
  --continuo   si YouTube frena o se acaba el uso de Claude, PAUSA y retoma solo (para la corrida diaria)
Funciona con una COLA: pendiente -> preparado (bajado, medido, video borrado) -> analizado. Nada se pierde ni se repite.
Resultado: fichas en datos/inteligencia.db (tabla analisis) + biblioteca/informe_<tema>_FECHA.md + fotos clave en biblioteca/fotos/
"""
import re, sys, json, math, time, random, shutil, sqlite3, threading, subprocess, datetime as dt
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from utilidades import cfg

CFG = cfg()
NAV = CFG.get("cookies_navegador")
VERSION = 2                       # v2 (19-nov): + linea temporal de la experiencia del espectador. Los v1 no se repiten.
BD = Path("datos/inteligencia.db")
RAIZ = Path("biblioteca")
TEMP = RAIZ / "_temporal"
PREP = RAIZ / "_preparado"          # material listo para que Claude lo observe (se borra al terminar)
FOTOS = RAIZ / "fotos"
N_VIRALES, N_GRANDES = 30, 5
SUBS_GRANDE = 500_000
PASO = 0.5                        # un fotograma cada 0,5 s (Shorts de hasta 60 s); mas largos: cada 1 s
LOCK_WHISPER = threading.Lock()
_WHISPER = {}


class Silencio:
    """Calla a yt-dlp pero guarda el ultimo error (para detectar bloqueos de YouTube)."""
    def __init__(self):
        self.ultimo = ""
    def debug(self, m): pass
    def info(self, m): pass
    def warning(self, m): pass
    def error(self, m):
        self.ultimo = str(m)


class Bloqueo(Exception):
    """YouTube esta frenando las descargas: hay que pausar y reintentar mas tarde."""


BLOQUEO = re.compile(r"not a bot|confirm you|429|too many requests|rate.?limit|http error 403|sign in to confirm", re.I)


# ---------------- base de datos ----------------
def abrir_bd():
    BD.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(BD, check_same_thread=False)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS cola (id TEXT PRIMARY KEY, tema TEXT, categoria TEXT, tipo TEXT, titulo TEXT,
        url TEXT, vistas INTEGER, veces REAL, estado TEXT, intentos INTEGER DEFAULT 0, error TEXT, actualizado REAL);
    CREATE TABLE IF NOT EXISTS analisis (id TEXT PRIMARY KEY, tema TEXT, categoria TEXT, tipo TEXT, version INTEGER,
        fecha REAL, titulo TEXT, canal TEXT, url TEXT, vistas INTEGER, veces REAL, medidas TEXT, ficha TEXT,
        formula TEXT, fotos TEXT);
    """)
    return c


def ya_analizados(bd):
    """Analizados + los que ya estan en la cola (no se vuelven a encolar)."""
    return ({r[0] for r in bd.execute("SELECT id FROM analisis")}
            | {r[0] for r in bd.execute("SELECT id FROM cola")})


# ---------------- 1. elegir videos ----------------
def candidatos(bd, tema, n_virales, n_grandes):
    try:
        return _candidatos(bd, tema, n_virales, n_grandes)
    except sqlite3.OperationalError:
        return []                      # todavia no corre inteligencia.py: no hay tablas de virales


def ultima_medicion(bd, tema):
    """Solo cuenta la recoleccion MAS RECIENTE del tema (las anteriores pueden estar desactualizadas)."""
    f = bd.execute("SELECT MAX(x.medido) FROM virales x JOIN videos v ON v.id = x.id WHERE v.tema = ?", (tema,)).fetchone()
    return (f[0] or 0) if f else 0


def _candidatos(bd, tema, n_virales, n_grandes):
    hechos = ya_analizados(bd)
    filas = bd.execute("""
        SELECT v.id, v.tipo, v.titulo, v.canal, v.subs, v.duracion, m.vistas, x.veces, v.canal_id
        FROM virales x JOIN videos v ON v.id = x.id
        JOIN mediciones m ON m.id = x.id AND m.medido = x.medido
        WHERE v.tema = ? AND x.medido >= ? ORDER BY x.medido DESC""",
        (tema, ultima_medicion(bd, tema) - 3600)).fetchall()
    vistos, virales = set(), []
    for f in filas:
        if f[0] in vistos or f[0] in hechos:
            continue
        vistos.add(f[0])
        virales.append({"id": f[0], "tipo": f[1], "titulo": f[2], "canal": f[3], "subs": f[4], "duracion": f[5],
                        "vistas": f[6], "veces": f[7], "categoria": "viral", "canal_id": f[8]})
    # OUTLIERS: pesa mas un video que supera MUCHO lo normal de su canal y, sobre todo, en canales CHICOS
    # (si un canal de 5.000 subs saca 400.000 vistas, el merito es del video, no del canal: eso es lo replicable).
    def puntaje(v):
        subs = max(v.get("subs") or 1000, 1000)
        chico = 2.0 if subs < 50_000 else 1.4 if subs < 200_000 else 1.0
        return (v["veces"] or 0) * math.log10(max(v["vistas"] or 10, 10)) * chico * math.log10(max((v["vistas"] or 0) / subs, 1) + 1.5)
    virales.sort(key=puntaje, reverse=True)
    for v in virales:
        v["categoria"] = "outlier_chico" if (v.get("subs") or 0) and v["subs"] < 50_000 else "viral"
    # prioridad: Shorts (ensenan el formato); los largos aportan datos e ideas (hasta un tercio)
    shorts = [v for v in virales if v["tipo"] == "Short"][:n_virales]
    largos = [v for v in virales if v["tipo"] != "Short"][:max(3, n_virales // 3)]
    virales = shorts + largos
    # GRUPO DE CONTROL: 2 Shorts normales del mismo canal por cada Short viral (solo se MIDEN, sin Claude).
    # Asi se puede comparar con numeros: "los virales cortan cada 1,4 s y los normales del mismo canal cada 2,3 s".
    control = []
    for v in shorts:
        f = bd.execute("SELECT mediana, normales FROM normal_canal WHERE canal_id=? AND tipo='Short'",
                       (v.get("canal_id"),)).fetchone()
        if not f:
            continue
        for n in [x for x in json.loads(f[1] or "[]") if x["id"] not in hechos and x["id"] != v["id"]][:2]:
            control.append({"id": n["id"], "tipo": "Short", "titulo": n.get("titulo") or "", "canal": v["canal"],
                            "vistas": n.get("vistas"), "veces": round((n.get("vistas") or 0) / max(f[0] or 1, 1), 1),
                            "categoria": "control"})
            hechos.add(n["id"])
    virales = virales + control
    # canales oficiales/grandes: los mas vistos por hora de la semana (fuente de informacion)
    ya = {v["id"] for v in virales} | hechos
    grandes = []
    for f in bd.execute("""
        SELECT v.id, v.tipo, v.titulo, v.canal, v.subs, v.duracion, MAX(m.vistas), v.subido
        FROM videos v JOIN mediciones m ON m.id = v.id
        WHERE v.tema = ? AND v.subs >= ? AND v.subido > ? GROUP BY v.id""",
            (tema, SUBS_GRANDE, dt.datetime.now().timestamp() - 8 * 86400)).fetchall():
        if f[0] in ya:
            continue
        horas = max(1.0, (dt.datetime.now().timestamp() - f[7]) / 3600)
        grandes.append({"id": f[0], "tipo": f[1], "titulo": f[2], "canal": f[3], "subs": f[4], "duracion": f[5],
                        "vistas": f[6], "veces": None, "vph": f[6] / horas, "categoria": "grande"})
    grandes.sort(key=lambda v: v["vph"], reverse=True)
    return virales + grandes[:n_grandes]


def manuales(bd):
    p = RAIZ / "entrada.txt"
    if not p.exists():
        p.parent.mkdir(exist_ok=True)
        p.write_text("# Un link por linea. Opcional: URL | tema   (ej: https://youtube.com/shorts/xxxx | gta6)\n")
        return []
    hechos, out = ya_analizados(bd), []
    for linea in p.read_text().splitlines():
        if not linea.strip() or linea.startswith("#"):
            continue
        partes = [x.strip() for x in linea.split("|")]
        url, tema = partes[0], (partes[1] if len(partes) > 1 else "manual")
        if not re.search(r"youtube\.com|youtu\.be", url):
            print(f"   (solo YouTube por ahora: se salta {url[:60]})")
            continue
        m = re.search(r"(?:v=|shorts/|youtu\.be/)([\w-]{11})", url)
        vid = m.group(1) if m else re.sub(r"\W+", "_", url)[-40:]
        if vid not in hechos:
            out.append({"id": vid, "url": url, "tema": tema, "tipo": None, "titulo": "", "canal": "", "subs": 0,
                        "vistas": 0, "veces": None, "categoria": "manual"})
    return out


# ---------------- 2. medir por codigo ----------------
_SHORT_CACHE = {}


def prueba_shorts(vid):
    """youtube.com/shorts/ID: si es Short responde 200; si no, YouTube REDIRIGE a /watch. None = no se pudo saber."""
    import urllib.request, urllib.error
    if vid in _SHORT_CACHE:
        return _SHORT_CACHE[vid]

    class SinRedireccion(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    abrir = urllib.request.build_opener(SinRedireccion)
    res = None
    for _ in range(2):
        try:
            r = abrir.open(urllib.request.Request(f"https://www.youtube.com/shorts/{vid}",
                           headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                                                  "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                                    "Accept-Language": "es-CL,es;q=0.9"}), timeout=10)
            res = r.status == 200
            r.close()                                    # no se lee la pagina: solo importa si redirige
            break
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                res = False
                break
        except Exception:
            pass
    _SHORT_CACHE[vid] = res
    return res


def es_short(info, dur, pista_url=""):
    """Short = link /shorts/ o formatos de video verticales (el ancho/alto general que da YouTube no es confiable)."""
    if dur and dur > 180:
        return False
    if "/shorts/" in (pista_url or "") or "/shorts/" in (info.get("webpage_url") or "") \
            or "/shorts/" in (info.get("original_url") or ""):
        return True
    fs = [f for f in (info.get("formats") or [])
          if f.get("vcodec") not in (None, "none") and f.get("width") and f.get("height")]
    if fs:
        return sum(f["height"] > f["width"] for f in fs) > len(fs) / 2
    w, h = info.get("width") or 0, info.get("height") or 0
    return (h > w) if (w and h) else bool(dur and dur <= 60)


def info_video(url):
    from yt_dlp import YoutubeDL
    errores = []
    for cookies in (False, True):
        log = Silencio()
        o = {"quiet": True, "skip_download": True, "ignoreerrors": True, "logger": log, "noplaylist": True}
        if cookies and NAV:
            o["cookiesfrombrowser"] = (NAV,)
        with YoutubeDL(o) as y:
            i = y.extract_info(url, download=False)
        if i:
            return i
        errores.append(log.ultimo)
    if all(BLOQUEO.search(e or "") for e in errores):
        raise Bloqueo(errores[-1][:150])
    return None


def bajar(url, carpeta):
    """Copia temporal en calidad baja (480p): pesa poco y basta para observar."""
    from yt_dlp import YoutubeDL
    errores = []
    for cookies in (True, False):                     # con la sesion de Safari primero: parece una visita normal
        o = {"quiet": True, "logger": Silencio(), "noplaylist": True, "retries": 3,
             "format": "bv*[height<=854][height>=360]+ba/b[height<=854]/bv*+ba/b", "merge_output_format": "mp4",
             "outtmpl": str(carpeta / "temporal.%(ext)s")}
        if cookies and NAV:
            o["cookiesfrombrowser"] = (NAV,)
        try:
            with YoutubeDL(o) as y:
                y.download([url])
        except Exception as e:
            errores.append(str(e))
            continue
        v = next((p for p in carpeta.glob("temporal.*") if p.suffix in (".mp4", ".mkv", ".webm")), None)
        if v:
            return v
    if errores and all(BLOQUEO.search(e) for e in errores):
        raise Bloqueo(errores[-1][:150])
    return None


def duracion(ruta):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(ruta)],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def cortes(video):
    """Tiempos de cambio de toma (deteccion de escena de ffmpeg)."""
    r = subprocess.run(["ffmpeg", "-nostdin", "-i", str(video), "-filter:v", "select='gt(scene,0.28)',showinfo",
                        "-f", "null", "-"], capture_output=True, text=True)
    return [round(float(x), 2) for x in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def audio_mono(video, sr=16000):
    raw = subprocess.run(["ffmpeg", "-nostdin", "-i", str(video), "-f", "s16le", "-ac", "1", "-ar", str(sr),
                          "-loglevel", "error", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def transcribir(audio):
    """Palabras con tiempo (Whisper). Un solo modelo compartido, de a un video a la vez."""
    from faster_whisper import WhisperModel
    with LOCK_WHISPER:
        if "m" not in _WHISPER:
            _WHISPER["m"] = WhisperModel("small", device="cpu", compute_type="int8")
        segs, info = _WHISPER["m"].transcribe(audio, word_timestamps=True, vad_filter=True)
        palabras = [{"w": w.word.strip(), "i": round(w.start, 2), "f": round(w.end, 2)}
                    for s in segs for w in (s.words or [])]
    return palabras, info.language


def medir_audio(a, palabras, sr=16000):
    """Voz vs fondo, y golpes (transientes) por segundo: aproximaciones, no exactas."""
    if len(a) < sr:
        return {}
    hop = int(0.05 * sr)
    n = len(a) // hop
    rms = np.sqrt((a[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-6
    db = 20 * np.log10(rms)
    voz = np.zeros(n, bool)
    for w in palabras:
        voz[int(w["i"] / 0.05):int(w["f"] / 0.05) + 1] = True
    fondo = db[~voz] if (~voz).any() else np.array([-90.0])
    habla = db[voz] if voz.any() else np.array([-90.0])
    salto = (db[1:] - db[:-1]) > 9
    golpes = int((salto & ~voz[1:]).sum())          # solo fuera de la voz: efectos/golpes, no silabas
    D = len(a) / sr
    return {"volumen_voz_db": round(float(np.median(habla)), 1), "volumen_fondo_db": round(float(np.median(fondo)), 1),
            "fondo_vs_voz_db": round(float(np.median(fondo) - np.median(habla)), 1),
            "hay_fondo_sonoro": bool(np.median(fondo) > -45),
            "golpes_fuera_de_voz_por_s": round(golpes / D, 2), "silencio_pct": round(100 * float((db < -50).mean()), 1)}


def similitud_loop(video, D):
    """Que tan parecido es el ultimo fotograma al primero (1 = igual): pista de loop visual."""
    def foto(t):
        raw = subprocess.run(["ffmpeg", "-nostdin", "-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1",
                              "-vf", "scale=32:56,format=gray", "-f", "rawvideo", "-loglevel", "error", "-"],
                             capture_output=True).stdout
        return np.frombuffer(raw, np.uint8).astype(np.float32) if len(raw) == 32 * 56 else None
    a, b = foto(0.1), foto(max(0.0, D - 0.15))
    if a is None or b is None:
        return None
    return round(1 - float(np.abs(a - b).mean()) / 255, 2)


def mas_repetido(info):
    h = info.get("heatmap") or []
    if not h:
        return []
    top = sorted(h, key=lambda x: x.get("value", 0), reverse=True)[:3]
    return [{"desde": round(x.get("start_time", 0), 1), "hasta": round(x.get("end_time", 0), 1),
             "intensidad": round(x.get("value", 0), 2)} for x in sorted(top, key=lambda x: x.get("start_time", 0))]


def medir(video, info):
    D = duracion(video)
    cs = [c for c in cortes(video) if 0.2 < c < D - 0.2]
    gaps = np.diff([0.0] + cs + [D]) if D else np.array([])
    a = audio_mono(video)
    palabras, lengua = transcribir(a) if len(a) else ([], None)
    habla = sum(w["f"] - w["i"] for w in palabras)
    pausas = sum(1 for x, y in zip(palabras, palabras[1:]) if y["i"] - x["f"] > 0.5)
    texto = " ".join(w["w"] for w in palabras)
    m = {"duracion_s": round(D, 1), "cortes": len(cs), "cortes_por_s": round(len(cs) / D, 2) if D else 0,
         "seg_entre_cortes_mediana": round(float(np.median(gaps)), 2) if len(gaps) else None,
         "primer_corte_s": cs[0] if cs else None, "tiempos_cortes": cs[:80],
         "primera_palabra_s": palabras[0]["i"] if palabras else None, "palabras": len(palabras),
         "palabras_por_s": round(len(palabras) / habla, 2) if habla else 0,
         "voz_pct": round(100 * habla / D, 1) if D else 0, "pausas_largas": pausas,
         "preguntas": texto.count("?"), "idioma_voz": lengua,
         "loop_similitud": similitud_loop(video, D), "mas_repetido": mas_repetido(info)}
    m.update(medir_audio(a, palabras))
    return m, palabras


def transcripcion_con_tiempos(palabras, cada=2.0):
    bloques = {}
    for w in palabras:
        bloques.setdefault(int(w["i"] // cada), []).append(w["w"])
    return "\n".join(f"[{k * cada:5.1f}s] {' '.join(v)}" for k, v in sorted(bloques.items()))


def hojas(video, carpeta, D, paso=None):
    paso = paso or (PASO if D <= 60 else 1.0)
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", str(video),
                    "-vf", f"fps=1/{paso},scale=240:-2,tile=4x4:padding=3:margin=3", "-q:v", "4",
                    str(carpeta / "hoja_%02d.jpg")], check=True)
    return sorted(carpeta.glob("hoja_*.jpg")), paso


def fotos_clave(video, vid, D):
    FOTOS.mkdir(parents=True, exist_ok=True)
    out = []
    for k, t in enumerate((0.3, D * 0.5, max(0.0, D - 0.3))):
        p = FOTOS / f"{vid}_{k}.jpg"
        subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", str(video),
                        "-frames:v", "1", "-vf", "scale=180:-2", "-q:v", "5", str(p)])
        if p.exists():
            out.append(p.name)
    return out


# ---------------- 3. observar (Claude) ----------------
PROMPT_SHORT = """Eres un analista HIPEROBSERVADOR de videos cortos virales. Tu trabajo es entender en profundidad por que
este video rindio mucho mejor de lo normal, segundo a segundo, para descubrir patrones que podamos replicar
(sin copiar el video). Nuestros canales: Shorts narrados con voz IA (GTA 6 en espanol e ingles; aliens y misterios en The Rabbit Loop;
cafe en Coffee, But Why?; numerologia en Number Signs; negocios en MDM). Si el video es de OTRO nicho, igual analizalo a fondo:
lo que ensena (gancho, ritmo, psicologia, estructura) sirve como conocimiento general.
Fijate ESPECIALMENTE en: la portada (primer fotograma), el hook visual + hablado, el CTA (que, cuando, como), y los
"reenganches" (cada vez que algo recupera la atencion cuando podria caer). Si el canal es chico y el video enorme,
explica que hizo distinto ese video.

Usa la herramienta Read para mirar estas hojas de contacto, EN ORDEN:
__HOJAS__
Cada hoja es una grilla de 4x4 fotogramas, de izquierda a derecha y de arriba a abajo.
El fotograma k (contando desde 0 en la primera hoja) es el segundo k x __PASO__ del video.
Abajo van: los DATOS del video, las MEDICIONES hechas por codigo (son hechos: usalas) y la TRANSCRIPCION con tiempos.

Reglas:
- Mira TODOS los fotogramas. Describe lo que de verdad se ve; no supongas.
- Distingue siempre: "medido" (viene de las mediciones), "observado" (lo ves o lo escuchas), "hipotesis" (tu interpretacion).
- Ninguna cifra de retencion, compartidos o guardados: no la tenemos (salvo "mas_repetido", que es dato real de YouTube).
- FORMULAS YA CONOCIDAS EN LA BIBLIOTECA (reusa el nombre si calza; si no calza ninguna, crea un nombre corto nuevo):
__FORMULAS__

Puntajes 1-5 con estas reglas fijas: 1 = ausente o debil; 3 = correcto, lo tipico del nicho; 5 = excepcional, se nota a simple vista.

Responde SOLO un objeto JSON en espanol:
{"resumen": "1 frase: de que trata y como lo cuenta",
 "bitacora": [{"t": "0.0-1.0", "se_ve": "...", "texto_en_pantalla": "...", "se_escucha": "voz/musica/efecto", "edicion": "corte, zoom...",
               "funcion": "hook | contexto | desarrollo | prueba | giro | payoff | cta | loop", "por_que_retiene": "..."}],
 "observaciones_libres": ["detalles llamativos que no caben en ninguna categoria: TODO lo que un experto notaria"],
 "hook": {"primeros_3s": "...", "tipo": "visual | pregunta | dato_sorprendente | contradiccion | accion | promesa | polemica | otro",
          "texto_escrito": "texto exacto en pantalla al inicio o \\"\\"", "primera_frase": "...", "por_que_detiene": "..."},
 "idea_central": "se entiende en 5 segundos: ...", "tema": "...", "angulo": "que lo hace distinto dentro del tema",
 "estructura": [{"desde": 0, "hasta": 2, "fase": "hook | contexto | desarrollo | prueba | giro | payoff | cta", "que_pasa": "..."}],
 "emocion": {"dominante": "curiosidad | asombro | humor | miedo | indignacion | nostalgia | satisfaccion | ambicion | ternura | otra",
             "momento_pico_s": 0, "por_que_se_comparte": "..."},
 "edicion": {"ritmo": "...", "zooms": "...", "transiciones": "...", "pausas": "...", "estimulo_nuevo_cada_s": 0},
 "texto_pantalla": {"subtitulos": "estilo, palabras por bloque, colores, resaltado", "altura_subtitulos_pct": 0,
                    "titulo_fijo": "...", "otros_textos": "..."},
 "elementos_graficos": [{"t": 0, "tipo": "flecha | circulo | emoji | sticker | contador | barra | foto_encima | mapa | meme | captura | icono | otro",
                         "descripcion": "...", "para_que": "..."}],
 "audio": {"voz": "humana | ia | sin_voz", "musica": "...", "efectos": ["..."], "sincronia_con_imagen": "..."},
 "payoff": {"que_obtiene": "...", "cumple_el_hook": true, "llega_en_s": 0},
 "loop": {"hay": false, "como": "..."},
 "interaccion": {"que_provoca_comentarios": "...", "cta": "...", "cta_en_s": 0, "cta_tipo": "pregunta | pedir_comentario | seguir | ninguno | otro"},
 "portada": {"primer_fotograma": "que se ve y que texto hay en el cuadro 0 (es la miniatura que ve la gente en el perfil/busqueda)",
             "legible_sin_sonido": true, "tiene_texto_grande": true, "calidad": "1-5"},
 "reenganches": [{"t": 0, "como": "zoom | cambio de toma | sonido | texto nuevo | pregunta | giro | sticker | otro",
                  "por_que_recupera_atencion": "..."}],
 "ocho_pasos": {"1_hook_visual_y_hablado": "...", "2_promesa_o_pregunta": "...", "3_contexto_minimo": "...",
                "4_desarrollo_con_pruebas": "...", "5_reenganche_a_mitad": "...", "6_giro_o_dato_fuerte": "...",
                "7_payoff": "...", "8_cta_o_loop": "...", "pasos_que_faltan": ["..."]},
 "canal": {"tamano": "chico | mediano | grande", "ventaja_del_video_sobre_el_canal": "que hizo este video que el canal no suele hacer"},
 "novedad": {"nivel": "nuevo | variante | conocido", "que_es_novedoso": "...", "por_que": "..."},
 "formula": {"nombre": "...", "estructura": "A -> B -> C", "indispensable": ["..."], "variable": ["..."]},
 "puntajes": {"hook": 0, "claridad": 0, "curiosidad": 0, "retencion_narrativa": 0, "emocion": 0, "payoff": 0,
              "compartible": 0, "loop": 0, "replicable": 0},
 "hipotesis_viral": [{"razon": "...", "evidencia": "medido | observado | hipotesis"}],
 "para_nosotros": {"como_aplicarlo": "...", "elementos_a_crear": ["graficos, sonidos o recursos que deberiamos tener"],
                   "idea_de_short": "titulo + hook escrito"},
 "linea_temporal": [{"desde": 0, "hasta": 2, "fase": "interrupcion | curiosidad | desarrollo | escalada | giro | payoff | loop | cta",
                     "estado_del_espectador": "que se esta preguntando / que espera en este momento",
                     "tension": 0, "info_nueva": "que aprende aca (o nada)", "pregunta_abierta": "la pregunta que lo mantiene mirando",
                     "dice_vs_muestra": "coinciden | se complementan | se contradicen a proposito | no relacionado"}],
 "curva": {"preguntas": [{"abre_s": 0, "cierra_s": 0, "pregunta": "..."}], "revelacion_principal_s": 0, "revelacion_pct": 0,
           "densidad_info": "datos nuevos por cada 10 s (aprox.)", "silencios_o_pausas": "donde y para que",
           "intensidad_musical": "como sube/baja y en que momentos", "cambios_visuales_por_s": 0,
           "brechas_dice_vs_muestra": "momentos donde lo que se ve agrega o contradice lo que se dice"},
 "contraste_con_lo_normal": {"que_haria_un_short_normal_del_tema": "...", "que_hizo_distinto_este": "...",
                             "explicaciones_alternativas": ["tema caliente | canal grande | momento | suerte: cual pesa y por que"]},
 "tema_real": "de que TRATA de verdad el video (no el titulo): gta | aliens | cafe | suerte | negocios | otro: <de que trata en 1-3 palabras>",
 "confianza": "alta | media | baja"}
La bitacora debe cubrir TODO el video (bloques de 0,5 a 2 s; mas finos en los primeros 3 s).
La linea_temporal cubre TODO el video por fases y describe la EXPERIENCIA del espectador (no solo lo que se ve): tension 0-10,
que pregunta lo sostiene y cuando se cierra. revelacion_pct = segundo de la revelacion principal / duracion x 100."""

PROMPT_LARGO = """Eres un investigador HIPEROBSERVADOR de contenido. Te paso un video LARGO con muy buen rendimiento (o de un canal
oficial/grande): su informacion, sus capitulos, los minutos que MAS SE REPITEN (dato real de YouTube: ahi esta lo que
mas interesa) y la transcripcion con tiempos. Objetivo: sacar la INFORMACION y las IDEAS para hacer Shorts propios
(no copiar el video), y entender por que interesa. No inventes nada: usa solo lo que se dice. Marca rumor/opinion.
FORMULAS YA CONOCIDAS EN LA BIBLIOTECA: __FORMULAS__
Responde SOLO un objeto JSON en espanol:
{"resumen": "1-2 frases", "tema": "...", "angulo": "...",
 "por_que_interesa": [{"razon": "...", "evidencia": "medido | observado | hipotesis"}],
 "momentos_mas_repetidos": [{"minuto": "mm:ss", "que_pasa": "...", "por_que_engancha": "..."}],
 "datos_clave": [{"minuto": "mm:ss", "dato": "...", "tipo": "confirmado | rumor | opinion"}],
 "observaciones_libres": ["..."],
 "novedad": {"nivel": "nuevo | variante | conocido", "que_es_novedoso": "..."},
 "ideas_shorts": [{"titulo": "...", "hook_escrito": "3-6 palabras", "formula": "...", "de_que_dato": "minuto"}],
 "confianza": "alta | media | baja"}
Entre 5 y 15 datos_clave y entre 3 y 5 ideas_shorts."""


TEMAS_TUTORIAL = ("estrategia_youtube", "animacion_ia", "tutorial", "herramientas", "referencias")

PROMPT_TUTORIAL = """Eres un analista HIPEROBSERVADOR de videos educativos sobre YouTube (crecer canales, estrategia, herramientas,
animacion y edicion con IA). Te paso la info del video, los minutos MAS REPETIDOS, la transcripcion con tiempos y hojas de
contacto (fotogramas numerados) para que MIRES las pantallas: configuraciones, herramientas, graficos y animaciones que muestra.
Usa la herramienta Read para mirar estas hojas, EN ORDEN:
__HOJAS__
El fotograma k (desde 0 en la primera hoja) es el segundo k x __PASO__ del video.
Objetivo: extraer TODO lo accionable para un equipo que produce Shorts automatizados (GTA 6, misterios) con una herramienta propia
(Python + ffmpeg + voz IA + Claude). Separa hechos de ventas: muchos de estos videos venden cursos o comunidades.
No inventes: lo que no se ve ni se dice, no va. Responde SOLO un objeto JSON en espanol:
{"resumen": "2 frases: que ensena y a quien le vende algo (si vende)",
 "tipo_video": "estrategia | herramienta | animacion | caso | mixto",
 "tecnicas": [{"minuto": "mm:ss", "nombre": "...", "pasos": ["...", "..."], "para_que_sirve": "...",
               "evidencia": "muestra datos | muestra pantalla | solo lo dice", "aplica_a_shorts": "si | parcial | no"}],
 "herramientas": [{"nombre": "...", "para_que": "...", "precio": "gratis | freemium | pago (cuanto si lo dice) | no dice",
                   "alternativa_gratis": "... o vacio", "la_muestra_en_pantalla": true}],
 "ajustes_youtube": [{"minuto": "mm:ss", "ajuste": "...", "recomendacion": "...", "por_que": "..."}],
 "afirmaciones": [{"minuto": "mm:ss", "afirmacion": "...", "respaldo": "dato propio | fuente externa | sin respaldo | venta"}],
 "animaciones_observadas": [{"minuto": "mm:ss", "que_se_ve": "...", "estilo": "tipografia, colores, ritmo, transiciones",
                              "como_replicarlo": "con que (ffmpeg / Remotion / Manim / stickers) y como", "dificultad": "baja | media | alta"}],
 "patron_del_propio_video": {"hook": "...", "estructura": "...", "ritmo_cortes": "...", "subtitulos": "...", "b_roll": "...",
                              "por_que_funciona": "..."},
 "ventas_y_sesgos": ["..."],
 "para_nuestra_herramienta": [{"tarea": "accion concreta", "modulo": "guion | voz | montaje | graficos | portada | publicacion | metricas",
                               "impacto": "alto | medio | bajo", "esfuerzo": "bajo | medio | alto"}],
 "ideas_shorts": [{"titulo": "...", "hook_escrito": "3-6 palabras", "de_que_minuto": "mm:ss"}],
 "confianza": "alta | media | baja"}
Entre 4 y 12 tecnicas, 3 a 10 para_nuestra_herramienta (ordenadas por impacto), y todas las animaciones que veas distintas."""


def objeto_json(texto):
    dec = json.JSONDecoder()
    i = texto.find("{")
    while i != -1:
        try:
            obj, _ = dec.raw_decode(texto, i)
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            pass
        i = texto.find("{", i + 1)
    return None


def formulas_conocidas(bd, tema):
    filas = bd.execute("SELECT formula, COUNT(*) FROM analisis WHERE formula IS NOT NULL AND formula != '' "
                       "GROUP BY formula ORDER BY COUNT(*) DESC LIMIT 40").fetchall()
    return "\n".join(f"- {f} ({n} videos)" for f, n in filas) or "(todavia ninguna: esta es de las primeras)"


def subtitulos_largo(info):
    from yt_dlp import YoutubeDL
    from lote import con_tiempos
    orig = info.get("language") or ""
    prefs = [f"{orig}-orig", orig, "en-orig", "en", "en-US", "es-orig", "es", "es-419"]
    with YoutubeDL({"quiet": True, "logger": Silencio()}) as y:
        for fuente in ("subtitles", "automatic_captions"):
            subs = info.get(fuente) or {}
            for lang in [l for l in prefs if l] + list(subs):
                fmt = next((f for f in subs.get(lang, []) if f.get("ext") == "json3"), None)
                if fmt:
                    try:
                        return con_tiempos(json.loads(y.urlopen(fmt["url"]).read().decode()))[:16000]
                    except Exception:
                        pass
    return ""


def cabecera(v, info):
    return (f"DATOS: \"{info.get('title')}\" · canal {info.get('channel')} ({info.get('channel_follower_count') or 0:,} subs) · "
            f"{info.get('view_count') or 0:,} vistas · likes {info.get('like_count') or 0:,} · comentarios "
            f"{info.get('comment_count') or 0:,} · categoria: {v['categoria']}"
            + (f" · {v['veces']}x lo normal de su canal" if v.get("veces") else "")
            + f"\nDescripcion: {(info.get('description') or '')[:500]}\nTags: {', '.join((info.get('tags') or [])[:15])}\n")


class LimiteClaude(Exception):
    """Se acabo el uso de Claude por ahora: pausar y retomar mas tarde."""


LIMITE = re.compile(r"usage limit|limit reached|rate limit|hit your limit|try again later|overloaded|5-hour", re.I)
INFO_CAMPOS = ("title", "channel", "channel_follower_count", "view_count", "like_count", "comment_count", "description",
               "tags", "duration", "width", "height")


# ---------------- cola ----------------
def encolar(bd, videos, tema):
    ahora = dt.datetime.now().timestamp()
    for v in videos:
        bd.execute("INSERT OR IGNORE INTO cola (id, tema, categoria, tipo, titulo, url, vistas, veces, estado, intentos, actualizado) "
                   "VALUES (?,?,?,?,?,?,?,?, 'pendiente', 0, ?)",
                   (v["id"], v.get("tema") or tema, v["categoria"], v.get("tipo"), v.get("titulo"),
                    v.get("url") or (f"https://www.youtube.com/shorts/{v['id']}" if v.get("tipo") == "Short"
                                     else f"https://www.youtube.com/watch?v={v['id']}"), v.get("vistas"), v.get("veces"), ahora))
    bd.commit()


def de_la_cola(bd, estado, tema=None):
    q = "SELECT id, tema, categoria, tipo, titulo, url, vistas, veces FROM cola WHERE estado=?"
    filas = bd.execute(q + (" AND (tema=? OR categoria='manual')" if tema else "") + " ORDER BY actualizado",
                       (estado, tema) if tema else (estado,)).fetchall()
    return [dict(zip(("id", "tema", "categoria", "tipo", "titulo", "url", "vistas", "veces"), f)) for f in filas]


def marcar(bd, vid, estado, error=None, intento=False):
    bd.execute("UPDATE cola SET estado=?, error=?, actualizado=?, intentos=intentos+? WHERE id=?",
               (estado, error, dt.datetime.now().timestamp(), 1 if intento else 0, vid))
    bd.commit()


# ---------------- paso 1: PREPARAR (sin Claude) ----------------
def preparar_uno(v):
    """Baja, mide, saca fotogramas/transcripcion y BORRA el video. Deja todo listo en biblioteca/_preparado/<id>/."""
    time.sleep(random.uniform(5, 20))                 # ritmo humano: nada de rafagas
    info = info_video(v["url"])
    if not info:
        return "error", "sin datos de YouTube"
    dur = info.get("duration") or 0
    if v.get("tipo") not in ("Short", "Largo"):        # el tipo ya viene de la recoleccion (pestana Shorts)
        v["tipo"] = "Short" if es_short(info, dur, v.get("url") or "") else "Largo"
    v["titulo"] = v.get("titulo") or info.get("title") or ""
    carpeta = PREP / v["id"]
    carpeta.mkdir(parents=True, exist_ok=True)
    datos = {"v": v, "info": {k: info.get(k) for k in INFO_CAMPOS}}
    datos["info"]["chapters"] = [c.get("title") for c in (info.get("chapters") or [])][:25]
    if v["tipo"] == "Largo":
        texto = subtitulos_largo(info)
        if not texto:
            shutil.rmtree(carpeta, ignore_errors=True)
            return "error", "largo sin subtitulos"
        lista, paso = [], None
        if (v.get("tema") or "") in TEMAS_TUTORIAL and dur <= 3600:   # tutoriales: ademas se MIRAN las pantallas
            tmp = TEMP / v["id"]
            tmp.mkdir(parents=True, exist_ok=True)
            video = None
            try:
                video = bajar(v["url"], tmp)
                if video:
                    paso_t = max(6.0, round(dur / 128, 1))        # hasta ~128 fotogramas (8 hojas de 4x4)
                    lista, paso = hojas(video, carpeta, dur, paso_t)
            except Exception as e:
                print(f"   (sin fotogramas para {v['id']}: {str(e)[:60]})")
            finally:
                if video and video.exists():
                    video.unlink()
                shutil.rmtree(tmp, ignore_errors=True)
        datos.update(medidas={"duracion_s": dur, "mas_repetido": mas_repetido(info), "capitulos": datos["info"]["chapters"]},
                     transcripcion=texto, hojas=[x.name for x in lista], paso=paso, fotos=[])
    else:
        tmp = TEMP / v["id"]
        tmp.mkdir(parents=True, exist_ok=True)
        video = None
        try:
            video = bajar(v["url"], tmp)
            if not video:
                shutil.rmtree(carpeta, ignore_errors=True)
                return "error", "no se pudo bajar"
            medidas, palabras = medir(video, info)
            if v.get("categoria") == "control":       # control: solo mediciones (sin fotogramas ni Claude)
                fotos, lista, paso = [], [], None
            else:
                fotos = fotos_clave(video, v["id"], medidas["duracion_s"])
                lista, paso = hojas(video, carpeta, medidas["duracion_s"])
        finally:
            if video and video.exists():
                video.unlink()                            # la copia del video se borra SIEMPRE, aqui mismo
            shutil.rmtree(tmp, ignore_errors=True)
        datos.update(medidas=medidas, transcripcion=transcripcion_con_tiempos(palabras),
                     hojas=[x.name for x in lista], paso=paso, fotos=fotos)
    (carpeta / "prep.json").write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")
    return "preparado", None


# ---------------- paso 2: OBSERVAR (Claude) ----------------
def observar_uno(v, formulas):
    carpeta = PREP / v["id"]
    datos = json.loads((carpeta / "prep.json").read_text())
    info, medidas = datos["info"], datos["medidas"]
    v = {**datos["v"], **{k: x for k, x in v.items() if x not in (None, "")}}
    if v.get("categoria") == "control":
        return {"v": v, "info": info, "medidas": medidas, "ficha": {"control": True}, "fotos": []}
    if v["tipo"] == "Largo":
        entrada = (cabecera(v, info) + f"Capitulos: {' / '.join(info.get('chapters') or [])}\n"
                   f"MAS REPETIDO (segundos): {json.dumps(medidas.get('mas_repetido'))}\n\nTRANSCRIPCION:\n{datos['transcripcion']}")
        if (v.get("tema") or "") in TEMAS_TUTORIAL and datos.get("hojas"):
            prompt = (PROMPT_TUTORIAL.replace("__HOJAS__", "\n".join(str((carpeta / x).resolve()) for x in datos["hojas"]))
                      .replace("__PASO__", str(datos["paso"])))
            cmd = ["claude", "-p", prompt, "--allowedTools", "Read"]
        else:
            cmd = ["claude", "-p", PROMPT_LARGO.replace("__FORMULAS__", formulas)]
    else:
        sin_listas = {k: x for k, x in medidas.items() if k != "tiempos_cortes"}
        entrada = (cabecera(v, info) + f"\nMEDICIONES (codigo, son hechos): {json.dumps(sin_listas, ensure_ascii=False)}\n"
                   f"Tiempos de cada corte (s): {medidas.get('tiempos_cortes')}\n\nTRANSCRIPCION:\n"
                   + (datos["transcripcion"] or "(sin voz)"))
        prompt = (PROMPT_SHORT.replace("__HOJAS__", "\n".join(str((carpeta / x).resolve()) for x in datos["hojas"]))
                  .replace("__PASO__", str(datos["paso"])).replace("__FORMULAS__", formulas))
        cmd = ["claude", "-p", prompt, "--allowedTools", "Read"]
    r = subprocess.run(cmd, input=entrada, capture_output=True, text=True, timeout=1500)
    ficha = objeto_json(r.stdout)
    if not ficha:
        if LIMITE.search((r.stdout or "") + (r.stderr or "")):
            raise LimiteClaude(((r.stdout or "") + (r.stderr or "")).strip()[:200])
        return None
    return {"v": v, "info": info, "medidas": medidas, "ficha": ficha, "fotos": datos.get("fotos") or []}


def guardar(bd, tema, r):
    v, info, f = r["v"], r["info"], r["ficha"]
    formula = (f.get("formula") or {}).get("nombre") if isinstance(f.get("formula"), dict) else None
    bd.execute("INSERT OR REPLACE INTO analisis VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
               (v["id"], v.get("tema") or tema, v["categoria"], v["tipo"], VERSION, dt.datetime.now().timestamp(),
                v["titulo"], info.get("channel") or "", v.get("url"), info.get("view_count") or 0, v.get("veces"),
                json.dumps(r["medidas"], ensure_ascii=False), json.dumps(f, ensure_ascii=False), formula,
                json.dumps(r["fotos"])))
    bd.commit()


# ---------------- informe ----------------
def md(s):
    return str(s or "").replace("|", "/").replace("\n", " ")


def ficha_md(r):
    v, f, m = r["v"], r["ficha"], r["medidas"]
    cab = (f"### [{md(v['titulo'])}]({v.get('url')})\n`{v['categoria']}` · {v['tipo']}"
           + (f" · **{v['veces']}x** lo normal" if v.get("veces") else "") + f" · {r['info'].get('view_count') or 0:,} vistas\n")
    if v["tipo"] == "Largo" and f.get("tecnicas") is not None:      # ficha de tutorial / estrategia
        def lista(items, fmt):
            return "\n".join(fmt(i) for i in items or []) or "  - (nada)"
        tec = lista(f.get("tecnicas"), lambda t: f"  - `{t.get('minuto')}` **{t.get('nombre')}** → " + " → ".join(t.get("pasos") or [])
                    + f" _({t.get('evidencia')}; Shorts: {t.get('aplica_a_shorts')})_")
        her = lista(f.get("herramientas"), lambda h: f"  - **{h.get('nombre')}** ({h.get('precio')}): {h.get('para_que')}"
                    + (f" · gratis: {h.get('alternativa_gratis')}" if h.get("alternativa_gratis") else ""))
        aju = lista(f.get("ajustes_youtube"), lambda x: f"  - `{x.get('minuto')}` {x.get('ajuste')}: **{x.get('recomendacion')}** _({x.get('por_que')})_")
        afi = lista(f.get("afirmaciones"), lambda x: f"  - `{x.get('minuto')}` {x.get('afirmacion')} _({x.get('respaldo')})_")
        ani = lista(f.get("animaciones_observadas"), lambda x: f"  - `{x.get('minuto')}` {x.get('que_se_ve')} · {x.get('estilo')} → **{x.get('como_replicarlo')}** _({x.get('dificultad')})_")
        tar = lista(f.get("para_nuestra_herramienta"), lambda x: f"  - [{x.get('impacto')}/{x.get('esfuerzo')}] **{x.get('modulo')}**: {x.get('tarea')}")
        pat = f.get("patron_del_propio_video") or {}
        ideas = lista(f.get("ideas_shorts"), lambda i: f"  - **{i.get('hook_escrito')}** · {i.get('titulo')} _({i.get('de_que_minuto')})_")
        return (cab + f"- {f.get('resumen', '')} _(tipo: {f.get('tipo_video')}, confianza {f.get('confianza')})_\n"
                f"- **Técnicas:**\n{tec}\n- **Herramientas:**\n{her}\n- **Ajustes de YouTube:**\n{aju}\n"
                f"- **Afirmaciones y respaldo:**\n{afi}\n- **Animaciones observadas:**\n{ani}\n"
                f"- **Patrón del video:** hook: {pat.get('hook')} · estructura: {pat.get('estructura')} · cortes: {pat.get('ritmo_cortes')} · "
                f"subtítulos: {pat.get('subtitulos')} · b-roll: {pat.get('b_roll')} · por qué funciona: {pat.get('por_que_funciona')}\n"
                f"- **Ventas y sesgos:** " + " / ".join(f.get("ventas_y_sesgos") or []) + "\n"
                f"- **Para nuestra herramienta:**\n{tar}\n- **Ideas de Shorts:**\n{ideas}\n")
    if v["tipo"] == "Largo":
        datos = "\n".join(f"  - `{d.get('minuto')}` {d.get('dato')} _({d.get('tipo')})_" for d in f.get("datos_clave") or [])
        ideas = "\n".join(f"  - **{i.get('hook_escrito')}** · {i.get('titulo')} _({i.get('formula')})_" for i in f.get("ideas_shorts") or [])
        return cab + f"- {f.get('resumen', '')}\n- **Datos clave:**\n{datos}\n- **Ideas:**\n{ideas}\n"
    hook, form, pts = f.get("hook") or {}, f.get("formula") or {}, f.get("puntajes") or {}
    medido = (f"cortes cada {m.get('seg_entre_cortes_mediana')} s · primera palabra a los {m.get('primera_palabra_s')} s · "
              f"{m.get('palabras_por_s')} palabras/s · fondo {m.get('fondo_vs_voz_db')} dB vs voz · loop {m.get('loop_similitud')}")
    return (cab + f"- {f.get('resumen', '')}\n- **Medido:** {medido}\n"
            f"- **Hook:** {hook.get('tipo')} · \"{md(hook.get('texto_escrito'))}\" · {hook.get('por_que_detiene', '')}\n"
            f"- **Fórmula:** {form.get('nombre')} ({form.get('estructura')}) · **Novedad:** {(f.get('novedad') or {}).get('nivel')}\n"
            f"- **Puntajes:** " + " · ".join(f"{k} {x}" for k, x in pts.items()) + "\n"
            f"- **Por qué pegó:** " + " / ".join(f"{h.get('razon')} _({h.get('evidencia')})_" for h in f.get("hipotesis_viral") or []) + "\n"
            f"- **Observaciones libres:** " + " / ".join(f.get("observaciones_libres") or []) + "\n"
            f"- **Portada:** {(f.get('portada') or {}).get('primer_fotograma', '')} · **CTA:** {(f.get('interaccion') or {}).get('cta', '')}"
            f" ({(f.get('interaccion') or {}).get('cta_tipo', '')}, s {(f.get('interaccion') or {}).get('cta_en_s', '')})\n"
            f"- **Reenganches:** " + " / ".join(f"{x.get('t')}s {x.get('como')}" for x in f.get("reenganches") or []) + "\n"
            f"- **8 pasos:** " + " · ".join(f"{k[2:]}: {x}" for k, x in (f.get("ocho_pasos") or {}).items() if k != "pasos_que_faltan" and x) + "\n"
            f"- **Para nosotros:** {(f.get('para_nosotros') or {}).get('como_aplicarlo', '')}\n")


# ---------------- corrida ----------------
def pausa(minutos, motivo):
    hasta = dt.datetime.now() + dt.timedelta(minutes=minutos)
    print(f"⏸️  {motivo}. Pausa de {minutos:.0f} min (retoma a las {hasta:%H:%M}). No se pierde nada.", flush=True)
    time.sleep(minutos * 60)


def fase_preparar(bd, tema, continuo):
    pausas = 0
    while True:
        pend = [v for v in de_la_cola(bd, "pendiente", tema)]
        if not pend:
            return True
        print(f"📥 Preparando {len(pend)} videos (de a 2, con pausas para no saturar YouTube)...", flush=True)
        frenar = threading.Event()

        def uno(v):
            if frenar.is_set():
                return v, "saltado", None
            try:
                estado, err = preparar_uno(v)
                return v, estado, err
            except Bloqueo as e:
                frenar.set()
                return v, "bloqueo", str(e)
            except Exception as e:
                return v, "error", str(e)[:150]
        with ThreadPoolExecutor(2) as pool:
            for v, estado, err in pool.map(uno, pend):
                if estado == "preparado":
                    marcar(bd, v["id"], "preparado")
                    print(f"   📦 listo para observar: {(v.get('titulo') or v['id'])[:55]}", flush=True)
                elif estado == "error":
                    n = bd.execute("SELECT intentos FROM cola WHERE id=?", (v["id"],)).fetchone()[0]
                    marcar(bd, v["id"], "error" if n >= 2 else "pendiente", err, intento=True)
                    print(f"   ⚠️ {v['id']}: {err}{' (se reintenta en la proxima corrida)' if n < 2 else ''}", flush=True)
        if not frenar.is_set():
            return True
        pausas += 1
        if not continuo or pausas > 4:
            print("⏸️  YouTube esta frenando las descargas. Lo pendiente queda en la cola: corre de nuevo mas tarde.")
            return False
        pausa(random.uniform(30, 60), "YouTube esta frenando las descargas")


def fase_observar(bd, tema, continuo, hechos):
    esperado = 0
    while True:
        listos = de_la_cola(bd, "preparado", tema)
        if not listos:
            return True
        print(f"🔬 Claude observando {len(listos)} videos en profundidad (3 a la vez)...", flush=True)
        formulas = formulas_conocidas(bd, tema)
        frenar = threading.Event()

        def uno(v):
            if frenar.is_set():
                return v, None, None
            try:
                return v, observar_uno(v, formulas), None
            except LimiteClaude as e:
                frenar.set()
                return v, None, "limite"
            except Exception as e:
                return v, None, str(e)[:150]
        with ThreadPoolExecutor(3) as pool:
            for v, r, err in pool.map(uno, listos):
                if r:
                    guardar(bd, tema, r)
                    marcar(bd, v["id"], "analizado")
                    shutil.rmtree(PREP / v["id"], ignore_errors=True)      # se borran las hojas: ya no hacen falta
                    hechos.append(r)
                    print(f"   ✅ ficha {len(hechos)}: {r['v']['titulo'][:55]}", flush=True)
                elif err and err != "limite":
                    n = bd.execute("SELECT intentos FROM cola WHERE id=?", (v["id"],)).fetchone()[0]
                    marcar(bd, v["id"], "error" if n >= 2 else "preparado", err, intento=True)
                    print(f"   ⚠️ {v['id']}: {err}", flush=True)
                elif err is None and r is None and not frenar.is_set():
                    n = bd.execute("SELECT intentos FROM cola WHERE id=?", (v["id"],)).fetchone()[0]
                    marcar(bd, v["id"], "error" if n >= 2 else "preparado", "ficha invalida", intento=True)
        if not frenar.is_set():
            return True
        if not continuo or esperado >= 10 * 60:
            print("⏸️  Se acabo el uso de Claude por ahora. Lo preparado queda guardado: corre de nuevo mas tarde.")
            return False
        pausa(30, "Se acabo el uso de Claude por ahora")
        esperado += 30


def main():
    args = sys.argv[1:]
    tema = args[args.index("--tema") + 1] if "--tema" in args else None
    if "--reanalizar" in args:           # vuelve a analizar (con el prompt nuevo) lo ya hecho de un tema: --reanalizar estrategia_youtube
        t = args[args.index("--reanalizar") + 1]
        bd0 = abrir_bd()
        ids = [r[0] for r in bd0.execute("SELECT id FROM analisis WHERE tema=?", (t,))]
        bd0.execute("DELETE FROM analisis WHERE tema=?", (t,))
        bd0.execute("UPDATE cola SET estado='pendiente', error=NULL, intentos=0 WHERE tema=?", (t,))
        bd0.commit()
        for i in ids:
            shutil.rmtree(PREP / i, ignore_errors=True)
        print(f"🔁 {len(ids)} videos de '{t}' vuelven a la cola para reanalizarse")
    n = int(args[args.index("--n") + 1]) if "--n" in args else N_VIRALES
    continuo = "--continuo" in args
    bd = abrir_bd()
    if tema and "--recolectar" in args:
        print("📡 Recolectando virales frescos (inteligencia.py --sin-claude)...", flush=True)
        subprocess.run([sys.executable, "inteligencia.py", "--tema", tema, "--sin-claude"])
    nuevos = manuales(bd)
    if tema and "--manual" not in args:
        nuevos += candidatos(bd, tema, n, N_GRANDES)
    encolar(bd, nuevos, tema)
    estados = dict(bd.execute("SELECT estado, COUNT(*) FROM cola GROUP BY estado").fetchall())
    print(f"🗂️  Cola: {len(nuevos)} nuevos · pendientes {estados.get('pendiente', 0)} · preparados "
          f"{estados.get('preparado', 0)} · analizados {estados.get('analizado', 0)} · con error {estados.get('error', 0)}", flush=True)
    hechos = []
    fase_preparar(bd, tema, continuo)
    fase_observar(bd, tema, continuo, hechos)
    shutil.rmtree(TEMP, ignore_errors=True)
    if not hechos:
        print("ℹ️  No se completo ningun analisis nuevo en esta corrida.")
        return
    fecha = dt.datetime.now()
    salida = RAIZ / f"informe_{(tema or 'manual').replace(' ', '_')}_{fecha:%Y%m%d_%H%M}.md"
    total = bd.execute("SELECT COUNT(*) FROM analisis").fetchone()[0]
    salida.write_text(f"# Biblioteca de virales · {tema or 'manual'} · {fecha:%Y-%m-%d %H:%M}\n\n"
                      f"Analizados en esta corrida: {len(hechos)} · total en la biblioteca: {total}\n\n"
                      + "\n\n".join(ficha_md(r) for r in hechos if r["v"].get("categoria") != "control") + "\n", encoding="utf-8")
    print(f"\n✅ {len(hechos)} fichas nuevas · biblioteca: {total} videos · informe: {salida}")


if __name__ == "__main__":
    main()
