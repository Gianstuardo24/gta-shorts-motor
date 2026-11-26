"""ESTUDIO: la app local para manejar todo sin la terminal.

Abrir:  cd ~/gta-shorts && source venv/bin/activate && python estudio.py
        -> http://localhost:8000   (Ctrl+C en la terminal para cerrarlo)
"""
import os, re, sys, json, shutil, hashlib, threading, subprocess, datetime as dt, webbrowser
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

import panel
from utilidades import cfg

PUERTO = 8000
PY = sys.executable
RAIZ = panel.RAIZ                      # ~/Desktop/YouTube
LOGS = Path("logs"); LOGS.mkdir(exist_ok=True)
TRABAJO = {"nombre": None, "proc": None, "log": None, "inicio": None}
ACCIONES = {   # boton -> comando
    "lote": ["lote.py", "--web"], "lote_rapido": ["lote.py", "--web", "--sin-ver"],
    "radar_es": ["radar.py"], "radar_en": ["radar.py"], "formatos": ["formatos.py"],
    "tomas": ["tomas.py", "--kit", "--oficial"],
    "diario": ["diario.py"],
    "metricas": ["metricas.py"],
}
CON_EXTRA = {"rehacer": "rehacer.py", "biblioteca": "biblioteca.py", "patrones": "patrones.py", "inteligencia": "inteligencia.py", "ganchos": "ganchos.py", "analisis": "analisis.py", "explorador": "explorador.py", "director": "director.py", "laboratorio": "laboratorio.py",
             "producir": "producir.py"}
AJUSTES = {   # clave -> (archivo, tipo, descripcion)
    "graficos": ("config.json", "bool", "Gráficos animados (fechas, cifras, sellos)"),
    "estimulos": ("config.json", "bool", "Emojis 3D y fotos oficiales tipo polaroid (retención)"),
    "musica": ("config.json", "bool", "Música de fondo generada"),
    "efectos": ("config.json", "bool", "Efectos de sonido (whoosh, pops, dings...)"),
    "volumen_musica": ("config.json", "float", "Volumen de la música (0.1 a 0.4)"),
    "volumen_efectos": ("config.json", "float", "Volumen de los efectos (0.2 a 0.8)"),
    "efectos_tematicos": ("config.json", "bool", "Efectos temáticos por palabra (sirena, motor, caja...)"),
    "usar_fotos": ("config.json", "bool", "Usar fotos además de video"),
    "ver_videos": ("config.json", "int", "Videos virales que se miran por lote"),
    "por_dia": ("config.json", "int", "Shorts por día por canal"),
    "velocidad": ("config.json", "float", "Velocidad de la voz (ES)"),
    "pausa": ("config.json", "float", "Pausa entre frases en segundos (ES)"),
    "velocidad_en": ("canales/en.json", "float", "Velocidad de la voz (EN)"),
    "pausa_en": ("canales/en.json", "float", "Pausa entre frases en segundos (EN)"),
    "cookies_navegador": ("config.json", "str", "Navegador con tu sesión de YouTube"),
}


# ---------------- trabajos (un proceso a la vez) ----------------
def ocupado():
    p = TRABAJO["proc"]
    return p is not None and p.poll() is None


def lanzar(accion, extra=None):
    if ocupado():
        return False, f"Ya está corriendo: {TRABAJO['nombre']}"
    if accion in CON_EXTRA:
        extra = [str(x) for x in (extra or [])]
        cmd, nombre = [CON_EXTRA[accion]] + extra, accion + " " + " ".join(extra)
    elif accion in ACCIONES:
        cmd, nombre = ACCIONES[accion], accion
    else:
        return False, "Acción desconocida"
    env = dict(os.environ)
    if accion == "radar_en":
        env["CANAL"] = "en"
    log = LOGS / f"{dt.datetime.now():%Y%m%d_%H%M%S}_{accion}.log"
    f = open(log, "w")
    TRABAJO.update(nombre=nombre, log=log, inicio=dt.datetime.now(),
                   proc=subprocess.Popen([PY, "-u"] + cmd, stdout=f, stderr=subprocess.STDOUT, env=env))
    threading.Thread(target=lambda: (TRABAJO["proc"].wait(), f.close(), panel.generar()), daemon=True).start()
    return True, f"Iniciado: {nombre}"


def detener():
    if ocupado():
        TRABAJO["proc"].terminate()
        return True
    return False


def estado():
    log = ""
    if TRABAJO["log"] and TRABAJO["log"].exists():
        log = TRABAJO["log"].read_text(errors="ignore")[-6000:]
    pasos = re.findall(r"^(?:=+\n)?(.*(?:\d/5|-----\s*\[\w+\].*-----|🎉.*|⛔.*|✅ Plan.*))$", log, re.M)
    corre = ocupado()
    codigo = None if corre or TRABAJO["proc"] is None else TRABAJO["proc"].returncode
    prog = re.findall(r"^\[(\d+)/(\d+)\]", log, re.M)
    etapa = re.findall(r"^=====\s*(.*?)\s*=====", log, re.M)
    return {"trabajo": TRABAJO["nombre"], "corriendo": corre, "codigo": codigo,
            "progreso": [int(prog[-1][0]), int(prog[-1][1])] if prog else None, "etapa": etapa[-1] if etapa else "",
            "ultima": (log.strip().splitlines() or [""])[-1][:160],
            "desde": TRABAJO["inicio"].strftime("%H:%M") if TRABAJO["inicio"] else None,
            "paso": (pasos[-1].strip(" =-") if pasos else ""), "log": log,
            "plan": plan_pendiente()}


# ---------------- plan del lote ----------------
def plan_pendiente():
    for e in sorted(Path("lotes").glob("*/esperando.json"), reverse=True) if Path("lotes").exists() else []:
        try:
            return {"lote": e.parent.name, "temas": json.loads(e.read_text())}
        except ValueError:
            pass
    return None


def responder_plan(lote, sacar, cancelar):
    c = Path("lotes", lote)
    if not (c / "esperando.json").exists():
        return False
    (c / "respuesta.json").write_text(json.dumps({"sacar": sacar, "cancelar": cancelar}))
    return True


# ---------------- videos ----------------
DIAS_CORTOS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]


def fecha_nuevo(v, pre):
    """Dia y hora de un Short en carpetas 'Nuevos': del nombre ('11-16 21h') o del horario sugerido del .txt."""
    m = re.match(r"(\d{2})-(\d{2}) (\d{2})h", pre)
    if m:
        mes, dia, h = m.groups()
    else:
        t = v.with_suffix(".txt").read_text(encoding="utf-8") if v.with_suffix(".txt").exists() else ""
        m = re.search(r"(?:SUGERIDO|PUBLICAR): \w+ (\d{2})/(\d{2}) (\d{2}):", t)
        if not m:
            return "", pre
        dia, mes, h = m.groups()
    hoy = dt.date.today()
    try:
        f = dt.date(hoy.year + (1 if hoy.month == 12 and mes == "01" else 0), int(mes), int(dia))
    except ValueError:
        return "", pre
    return f"{f.isoformat()} {DIAS_CORTOS[f.weekday()]}", f"{h}:00"


RECIBIR_HTML = """<!doctype html><meta charset=utf-8><title>Recibiendo stickers</title>
<body style="font:16px -apple-system;background:#0d0918;color:#ece8ff;padding:30px"><h2>📥 Recibiendo hojas de stickers…</h2><div id=l></div>
<script>
addEventListener("message", async ev => {
  if (ev.origin !== "https://chatgpt.com" || !ev.data || !ev.data.buf) return;
  const r = await fetch("/api/sticker?n=" + encodeURIComponent(ev.data.nombre), {method: "POST", body: ev.data.buf});
  const ok = r.ok;
  document.getElementById("l").insertAdjacentHTML("beforeend", `<p>${ok ? "✅" : "⛔"} ${ev.data.nombre}</p>`);
  ev.source.postMessage({nombre: ev.data.nombre, ok}, ev.origin);
});
opener && opener.postMessage({listo: true}, "https://chatgpt.com");
</script>"""

REFINAR = Path("datos/por_refinar.json")


def por_refinar():
    try:
        return json.loads(REFINAR.read_text())
    except Exception:
        return {}


def marcar_refinar(canal, fecha, si):
    d = por_refinar()
    s = set(d.get(canal, []))
    (s.add if si else s.discard)(fecha[:10])
    d[canal] = sorted(s)
    REFINAR.parent.mkdir(exist_ok=True)
    REFINAR.write_text(json.dumps(d, indent=1))
    return True


def videos():
    out = []
    if not RAIZ.exists():
        return out
    for canal in sorted(p for p in RAIZ.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
        dias, pasados = panel.shorts_de(canal, todos=True)
        hoy = dt.date.today().isoformat()
        nuevos = []   # carpetas "Nuevos ..." (para revisar y elegir): van primero
        for d in sorted((p for p in canal.iterdir() if p.is_dir() and p.name.startswith("Nuevos")), reverse=True):
            grupos = {}
            for v in sorted(d.glob("*.mp4")):
                pre, _, nom = v.stem.partition(" - ")
                fecha, hora = fecha_nuevo(v, pre)
                grupos.setdefault(fecha, []).append({"hora": hora, "nombre": nom or v.stem, "subido": False,
                                                     **panel.leer_txt(v.with_suffix(".txt")),
                                                     "video": v.relative_to(RAIZ).as_posix()})
            for fecha in sorted(grupos):
                nuevos.append({"dia": fecha or d.name, "grupo": d.name, "nuevo": True,
                               "items": sorted(grupos[fecha], key=lambda x: x["hora"])})
        if not nuevos and not dias:
            continue          # carpetas sin Shorts (ej: Sonidos)
        ref = set(por_refinar().get(canal.name, []))
        for d in nuevos:
            d["refinar"] = d["dia"][:10] in ref
        nts = notas()
        sbs = subidas()
        for d in nuevos:
            for it in d["items"]:
                it["nota"] = nts.get(clave_nota(it["video"], d["dia"], it["hora"]), "")
        out.append({"canal": canal.name, "pasados": pasados, "dias": nuevos + [
            {"dia": d, "pasado": d[:10] < hoy, "refinar": d[:10] in ref, "items": [{**{k: s[k] for k in ("hora", "nombre", "subido", "titulo", "descripcion", "comentario")},
                                  "video": s["video"].relative_to(RAIZ).as_posix()} for s in items]}
            for d, items in dias]})
        lista = out[-1]["dias"]                 # SIEMPRE por fecha (pasados, subidos y nuevos incluidos)
        for d in lista:
            for it in d["items"]:
                pv = RAIZ / it["video"]
                pt = pv.with_name(pv.stem + ".portada.jpg")
                it["portada"] = pt.relative_to(RAIZ).as_posix() if pt.exists() else ""
                it.setdefault("nota", nts.get(clave_nota(it["video"], d["dia"], it["hora"]), ""))
                it["subido_en"] = sbs.get(clave_nota(it["video"], d["dia"], it["hora"]), "")
        lista.sort(key=lambda d: (d["dia"][:10] if re.match(r"\d{4}-", d["dia"]) else "9999", 1 if d.get("nuevo") else 0))
    return out


SUBIDAS = Path("datos/subidas.json")   # canal|dia|hora -> fecha y hora real en que marcaste Subido


def subidas():
    try:
        return json.loads(SUBIDAS.read_text())
    except Exception:
        return {}


def registrar_subida(rel, dia, hora):
    d = subidas()
    d[clave_nota(rel, dia, hora)] = dt.datetime.now().isoformat(timespec="seconds")
    SUBIDAS.parent.mkdir(exist_ok=True)
    SUBIDAS.write_text(json.dumps(d, ensure_ascii=False, indent=1))


NOTAS = Path("datos/notas.json")


def notas():
    try:
        return json.loads(NOTAS.read_text())
    except Exception:
        return {}


def clave_nota(rel, dia, hora):
    canal = Path(rel).parts[0]
    return f"{canal}|{dia[:10]}|{hora}" if re.match(r"\d{4}-", dia or "") else rel


def guardar_nota(rel, dia, hora, texto):
    d = notas()
    k = clave_nota(rel, dia, hora)
    if texto.strip():
        d[k] = texto.strip()
    else:
        d.pop(k, None)
    NOTAS.parent.mkdir(exist_ok=True)
    NOTAS.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    return True


MINIS = Path("subtitulos/_minis")


def miniatura(rel, base=None):
    base = base or RAIZ
    v = (base / unquote(rel)).resolve()
    if base.resolve() not in v.parents or not v.is_file():
        return None
    MINIS.mkdir(parents=True, exist_ok=True)
    out = MINIS / (hashlib.md5(f"{v}{v.stat().st_mtime}".encode()).hexdigest() + ".jpg")
    if not out.exists():
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", "1.5", "-i", str(v), "-frames:v", "1",
                        "-vf", "scale=180:-2", "-q:v", "5", str(out)])
    return out if out.exists() else None


def usar_nuevo(rel, dia, hora):
    """La version nueva pasa a la carpeta del dia (pendiente) y la vieja de esa hora se aparta a _reemplazados/."""
    return video_subido(rel, dia, hora, a_subidos=False)


def descartar(rel):
    v = (RAIZ / rel).resolve()
    if RAIZ.resolve() not in v.parents or not v.is_file():
        return False
    dest = RAIZ / Path(rel).parts[0] / "_descartados"
    dest.mkdir(parents=True, exist_ok=True)
    for f in (v, v.with_suffix(".txt")):
        if f.exists():
            shutil.move(str(f), dest / f.name)
    if v.parent.is_dir() and not any(v.parent.iterdir()):
        v.parent.rmdir()
    return True


def guion_de(canal, dia, hora):
    """Stem del guion (ej. L202611131407_01) que corresponde a un video programado."""
    try:
        reg = json.loads(Path("horarios.json").read_text())
    except Exception:
        return None
    clave = f"{dia[:10]}T{(hora or '00')[:2]}"
    return next((k for k, v in reg.items() if v.get("canal", "").lstrip("@") == canal and v.get("slot", "").startswith(clave)), None)


def kit_info(canal, dia, hora):
    stem = guion_de(canal, dia, hora)
    if not stem:
        return {"ok": False, "msg": "No encontré el guion de ese video"}
    g = Path("guiones") / f"{stem}.json"
    d = json.loads(g.read_text()) if g.exists() else {}
    kit = d.get("kit") or {}
    try:
        listo = f"kit_{stem}" in json.loads(Path("assets/stickers/stickers.json").read_text())
    except Exception:
        listo = False
    return {"ok": True, "guion": stem, "prompt": kit.get("prompt", ""), "elementos": kit.get("elementos", []),
            "estado": "listo" if listo else ("sin imagen" if kit else "sin kit")}


def kit_guardar(stem, datos):
    if not re.fullmatch(r"[A-Za-z0-9_]+", stem or "") or datos[:8] != b"\x89PNG\r\n\x1a\n":
        return False, "Solo PNG"
    dest = Path("assets/stickers/entrada")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / f"kit_{stem}.png").write_bytes(datos)
    r = subprocess.run([PY, "stickers.py"], capture_output=True, text=True)
    ok = f"kit_{stem}" in (r.stdout or "")
    return ok, (r.stdout or r.stderr)[-300:]


def rehacer_video(canal, dia, hora):
    """Busca que guion es ese video (horarios.json) y lanza rehacer.py solo para el, con voz nueva, a 'Nuevos'."""
    try:
        reg = json.loads(Path("horarios.json").read_text())
    except Exception:
        return False, "No hay registro de horarios"
    clave = f"{dia[:10]}T{(hora or '00')[:2]}"
    stem = next((k for k, v in reg.items() if v.get("canal", "").lstrip("@") == canal and v.get("slot", "").startswith(clave)), None)
    if not stem:
        return False, f"No encontré qué guion es ({canal} {dia[:10]} {hora})"
    base, num = stem[:-3], str(int(stem[-2:]))
    perfiles = {}
    for f in Path("canales").glob("*.json"):
        try:
            perfiles[json.loads(f.read_text()).get("canal", "").lstrip("@")] = f.stem
        except ValueError:
            pass
    perfil = perfiles.get(canal, "es")
    if perfil == "en" and base.endswith("en"):
        extra = [base[:-2], f"--num-en={num}"]
    elif perfil in ("es", "en"):
        extra = [base, f"--num={num}"]
    else:
        extra = [base, f"--num={num}", f"--perfil={perfil}"]
    return lanzar("rehacer", extra + ["--voz", "--nuevos"])


def video_subido(rel, dia, hora, a_subidos=True):
    """Marca UN video como subido: lo mueve (con su .txt) a Subidos/<dia>/<HHh - titulo>.
    Si venia de una carpeta 'Nuevos', la version vieja de ese mismo dia y hora se aparta a _reemplazados/."""
    v = (RAIZ / rel).resolve()
    if RAIZ.resolve() not in v.parents or not v.is_file() or not re.match(r"\d{4}-\d{2}-\d{2} ", dia or ""):
        return False
    canal = RAIZ / Path(rel).parts[0]
    hh = (hora or "00")[:2]
    nombre = v.stem.split(" - ", 1)[-1]
    dias_cortos = {"Sáb": "Sab"}
    destino = canal / "Subidos" / dia if a_subidos else canal / dia
    destino.mkdir(parents=True, exist_ok=True)
    if v.parent.name.startswith("Nuevos"):
        for viejo_dir in (canal / dia, canal / dia.replace("Sáb", "Sab")):
            for viejo in viejo_dir.glob(f"{hh}h - *.mp4") if viejo_dir.is_dir() else []:
                apartado = canal / "_reemplazados" / dia
                apartado.mkdir(parents=True, exist_ok=True)
                for f in (viejo, viejo.with_suffix(".txt")):
                    if f.exists():
                        shutil.move(str(f), apartado / f.name)
            if viejo_dir.is_dir() and not any(viejo_dir.iterdir()):
                viejo_dir.rmdir()
    for f in (v, v.with_suffix(".txt")):
        if f.exists():
            shutil.move(str(f), destino / f"{hh}h - {nombre}{f.suffix}")
    if v.parent.is_dir() and not any(v.parent.iterdir()):
        v.parent.rmdir()
    return True


def desmarcar_subido(canal, dia):
    """Deshace 'Ya subi este dia': devuelve la carpeta desde Subidos/ a pendientes."""
    origen = RAIZ / canal / "Subidos" / dia
    if not origen.is_dir():
        return False
    destino = RAIZ / canal / dia
    destino.mkdir(parents=True, exist_ok=True)
    for f in origen.iterdir():
        shutil.move(str(f), destino / f.name)
    origen.rmdir()
    return True


def marcar_subido(canal, dia):
    origen = RAIZ / canal / dia
    if not origen.is_dir():
        return False
    destino = RAIZ / canal / "Subidos" / dia
    destino.mkdir(parents=True, exist_ok=True)
    for f in origen.iterdir():
        shutil.move(str(f), destino / f.name)
    origen.rmdir()
    return True


# ---------------- radar y formatos ----------------
def radares():
    out = []
    for rd in sorted(p for p in Path("radar").iterdir() if p.is_dir()) if Path("radar").exists() else []:
        lista, analisis, fecha = panel.radar_datos(rd)
        if lista:
            out.append({"canal": rd.name, "fecha": fecha, "videos": lista[:30], "analisis": panel.md_a_html(analisis)})
    return out


def formatos():
    inf = sorted(Path("formatos").glob("formatos_*.md")) if Path("formatos").exists() else []
    return {"html": panel.md_a_html(inf[-1].read_text(encoding="utf-8")) if inf else ""}


# ---------------- biblioteca de virales ----------------
BD = Path("datos/inteligencia.db")
CAMPOS_FICHA = ("resumen", "hook", "idea_central", "tema", "angulo", "estructura", "emocion", "edicion", "texto_pantalla",
                "elementos_graficos", "audio", "payoff", "loop", "interaccion", "novedad", "formula", "puntajes",
                "hipotesis_viral", "para_nosotros", "confianza", "bitacora", "observaciones_libres", "linea_temporal", "curva", "contraste_con_lo_normal",
                "por_que_interesa", "momentos_mas_repetidos", "datos_clave", "ideas_shorts")


def biblioteca_api(q):
    import sqlite3
    temas = list(json.loads(Path("inteligencia_temas.json").read_text())) if Path("inteligencia_temas.json").exists() else []
    if not BD.exists():
        return {"temas": temas, "stats": {}, "fichas": []}
    c = sqlite3.connect(BD)
    try:
        filas = c.execute("SELECT id, tema, categoria, tipo, fecha, titulo, canal, url, vistas, veces, medidas, ficha, formula, fotos "
                          "FROM analisis ORDER BY fecha DESC").fetchall()
    except sqlite3.OperationalError:
        return {"temas": temas, "stats": {}, "fichas": []}
    tema = (q.get("tema") or [""])[0]
    stats = {"total": 0, "Short": 0, "Largo": 0, "control": 0}
    fichas = []
    for (id_, tem, cat, tipo, fecha, tit, canal, url, vistas, veces, med, ficha, formula, fotos) in filas:
        if tema and tem != tema:
            continue
        if cat == "control":
            stats["control"] += 1
            continue
        stats["total"] += 1
        stats[tipo] = stats.get(tipo, 0) + 1
        try:
            f, m = json.loads(ficha or "{}"), json.loads(med or "{}")
        except Exception:
            f, m = {}, {}
        fichas.append({"id": id_, "tema": tem, "categoria": cat, "tipo": tipo, "fecha": dt.datetime.fromtimestamp(fecha).strftime("%d/%m %H:%M"),
                       "titulo": tit, "canal": canal, "url": url, "vistas": vistas, "veces": veces, "formula": formula,
                       "fotos": json.loads(fotos or "[]"), "medidas": {k: v for k, v in m.items() if k != "tiempos_cortes"},
                       "ficha": {k: f.get(k) for k in CAMPOS_FICHA if f.get(k) is not None}})
    try:
        stats["cola"] = dict(c.execute("SELECT estado, COUNT(*) FROM cola GROUP BY estado").fetchall())
    except sqlite3.OperationalError:
        stats["cola"] = {}
    return {"temas": temas, "stats": stats, "fichas": fichas}


def formulas_api(q):
    tema = (q.get("tema") or ["gta6"])[0] or "gta6"
    p = Path("biblioteca") / f"formulas_{tema.replace(' ', '_')}.md"
    return {"html": panel.md_a_html(p.read_text(encoding="utf-8")) if p.exists() else ""}


# ---------------- ajustes ----------------
def leer_ajustes():
    out = []
    for clave, (archivo, tipo, desc) in AJUSTES.items():
        d = json.loads(Path(archivo).read_text()) if Path(archivo).exists() else {}
        k = clave.replace("_en", "") if archivo != "config.json" else clave
        defecto = {"graficos": True, "usar_fotos": False, "por_dia": 2, "pausa": 0.12, "ver_videos": 4,
                   "musica": True, "efectos": True, "volumen_musica": 0.2, "volumen_efectos": 0.45, "efectos_tematicos": False}.get(clave)
        out.append({"clave": clave, "tipo": tipo, "desc": desc, "valor": d.get(k, defecto)})
    return out


def guardar_ajustes(cambios):
    for clave, valor in cambios.items():
        if clave not in AJUSTES:
            continue
        archivo, tipo, _ = AJUSTES[clave]
        p = Path(archivo)
        d = json.loads(p.read_text()) if p.exists() else {}
        k = clave.replace("_en", "") if archivo != "config.json" else clave
        try:
            d[k] = {"bool": lambda v: v in (True, "true", "1", 1), "int": int, "float": float, "str": str}[tipo](valor)
        except (ValueError, TypeError):
            continue
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def lotes_recientes():
    return sorted({p.stem.rsplit("_", 1)[0] for p in Path("guiones").glob("L*_[0-9][0-9].json")
                   if not p.stem.rsplit("_", 1)[0].endswith("en")}, reverse=True)[:8] if Path("guiones").exists() else []


# ---------------- servidor ----------------
class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def enviar(self, cuerpo, tipo="application/json", codigo=200):
        datos = cuerpo if isinstance(cuerpo, bytes) else (json.dumps(cuerpo, ensure_ascii=False).encode() if tipo == "application/json" else cuerpo.encode())
        self.send_response(codigo)
        self.send_header("Content-Type", tipo + ("; charset=utf-8" if "json" in tipo or "html" in tipo else ""))
        self.send_header("Content-Length", str(len(datos)))
        if "json" in tipo or "html" in tipo:
            self.send_header("Cache-Control", "no-store")   # que el navegador no muestre una version vieja del panel
        self.end_headers()
        self.wfile.write(datos)

    def media(self, rel, descargar=False, base=None):
        base = base or RAIZ
        p = (base / unquote(rel)).resolve()
        if base.resolve() not in p.parents or not p.is_file():
            return self.enviar({"error": "no existe"}, codigo=404)
        tam, rango = p.stat().st_size, self.headers.get("Range")
        ini, fin = 0, tam - 1
        if rango:
            m = re.match(r"bytes=(\d*)-(\d*)", rango)
            if m:
                ini = int(m.group(1) or 0)
                fin = int(m.group(2)) if m.group(2) else tam - 1
        self.send_response(206 if rango else 200)
        tipo = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}.get(p.suffix.lower(), "video/mp4")
        self.send_header("Content-Type", tipo)
        self.send_header("Accept-Ranges", "bytes")
        if descargar:
            from urllib.parse import quote
            self.send_header("Content-Disposition", f"attachment; filename*=UTF-8''{quote(p.name)}")
        self.send_header("Content-Length", str(fin - ini + 1))
        if rango:
            self.send_header("Content-Range", f"bytes {ini}-{fin}/{tam}")
        self.end_headers()
        with open(p, "rb") as f:
            f.seek(ini)
            restante = fin - ini + 1
            while restante > 0:
                bloque = f.read(min(1 << 20, restante))
                if not bloque:
                    break
                try:
                    self.wfile.write(bloque)
                except (BrokenPipeError, ConnectionResetError):
                    break
                restante -= len(bloque)

    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        rutas = {"/api/estado": estado, "/api/videos": videos, "/api/radar": radares, "/api/formatos": formatos,
                 "/api/ajustes": leer_ajustes, "/api/lotes": lotes_recientes}
        if u.path == "/recibir":   # ventanita que recibe hojas de stickers desde la pestaña de ChatGPT (postMessage)
            return self.enviar(RECIBIR_HTML, "text/html")
        if u.path in ("/", "/index.html", "/clasico"):
            return self.enviar(Path("estudio.html").read_text(encoding="utf-8"), "text/html")
        if u.path == "/panel":   # panel nuevo de videos (va dentro de la pestaña Videos)
            return self.enviar(Path("inicio.html").read_text(encoding="utf-8"), "text/html")
        if u.path == "/asset":   # logos de los canales para el panel de inicio (solo assets/logo_*.png)
            f = Path("assets") / Path(q.get("f", [""])[0]).name
            if not (f.name.startswith("logo_") and f.suffix == ".png" and f.is_file()):
                return self.enviar({"error": "no existe"}, codigo=404)
            return self.enviar(f.read_bytes(), "image/png")
        if u.path == "/mini":
            m = miniatura(q.get("p", [""])[0])
            if not m:
                return self.enviar({"error": "no existe"}, codigo=404)
            return self.enviar(m.read_bytes(), "image/jpeg")
        if u.path == "/media":
            return self.media(q.get("p", [""])[0], q.get("dl", [""])[0] == "1")
        if u.path == "/api/repers":      # publicaciones de Repers (tandas de ~/Desktop/Repers Shorts)
            import importlib, repers_estudio
            importlib.reload(repers_estudio)
            return self.enviar(repers_estudio.items())
        if u.path == "/api/horarios":   # horas fijas de cada canal (para dibujar los videos que faltan producir)
            out = {}
            for f in [Path("config.json")] + sorted(Path("canales").glob("*.json")):
                if re.search(r"_v\d|_antes|_v_", f.stem):
                    continue
                try:
                    d = json.loads(f.read_text())
                except Exception:
                    continue
                c = d.get("canal", "").lstrip("@")
                if c and d.get("horas_fijas"):
                    out[c] = d["horas_fijas"]
            return self.enviar(out)
        if u.path == "/api/rendimiento":   # rendimiento de las sesiones de grabacion de Repers
            import importlib, repers_estudio, rendimiento
            importlib.reload(repers_estudio); importlib.reload(rendimiento)
            return self.enviar(rendimiento.datos())
        if u.path == "/api/repers_metricas":
            import importlib, repers_estudio
            importlib.reload(repers_estudio)
            return self.enviar(repers_estudio.metricas(q.get("refrescar", [""])[0] == "1"))
        if u.path in ("/rmedia", "/rmini"):
            import repers_estudio
            if u.path == "/rmini":
                m = miniatura(q.get("p", [""])[0], repers_estudio.RPS)
                return self.enviar(m.read_bytes(), "image/jpeg") if m else self.enviar({"error": "no existe"}, codigo=404)
            return self.media(q.get("p", [""])[0], q.get("dl", [""])[0] == "1", repers_estudio.RPS)
        if u.path == "/api/estrategia":   # paginas de Analisis: diario, marketing, ideas de ChatGPT, equipo
            f = Path("datos/estrategia") / (Path(q.get("f", [""])[0]).name + ".md")
            return self.enviar({"html": panel.md_a_html(f.read_text(encoding="utf-8")) if f.is_file() else ""})
        if u.path == "/api/kit":
            return self.enviar(kit_info(q.get("canal", [""])[0], q.get("dia", [""])[0], q.get("hora", [""])[0]))
        if u.path == "/api/aprendizajes":
            out = []
            for f in sorted(Path("biblioteca").glob("*.md")) if Path("biblioteca").exists() else []:
                if f.name.startswith(("hooks_", "formulas_")) or f.name.startswith("informe_manual"):
                    out.append({"archivo": f.name, "html": panel.md_a_html(f.read_text(encoding="utf-8")[:60000]),
                                "fecha": dt.datetime.fromtimestamp(f.stat().st_mtime).strftime("%d/%m %H:%M")})
            return self.enviar(out)
        if u.path == "/api/roadmap":
            try:
                return self.enviar(json.loads(Path("datos/roadmap.json").read_text()))
            except Exception:
                return self.enviar({"bloques": []})
        if u.path == "/api/metricas":
            try:
                import importlib, metricas
                importlib.reload(metricas)
                return self.enviar(metricas.resumen())
            except Exception as err:
                return self.enviar({"canales": [], "estado": {}, "error": str(err)})
        if u.path == "/api/biblioteca":
            return self.enviar(biblioteca_api(q))
        if u.path == "/api/formulas":
            return self.enviar(formulas_api(q))
        if u.path == "/foto":
            f = (Path("biblioteca/fotos") / Path(unquote(q.get("f", [""])[0])).name)
            if f.is_file():
                return self.enviar(f.read_bytes(), "image/jpeg")
            return self.enviar({"error": "no existe"}, codigo=404)
        if u.path in rutas:
            return self.enviar(rutas[u.path]())
        self.enviar({"error": "no existe"}, codigo=404)

    def do_OPTIONS(self):          # permiso del navegador para recibir hojas de stickers desde ChatGPT
        self.send_response(204)
        self.cors()
        self.end_headers()

    def cors(self):
        if self.headers.get("Origin") == "https://chatgpt.com":
            self.send_header("Access-Control-Allow-Origin", "https://chatgpt.com")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Access-Control-Allow-Private-Network", "true")

    def do_POST(self):
        largo = int(self.headers.get("Content-Length") or 0)
        p = urlparse(self.path).path
        if p == "/api/kit_imagen":  # imagen del kit visual arrastrada al Estudio -> se guarda y se recorta
            datos = self.rfile.read(min(largo, 25 << 20))
            stem = parse_qs(urlparse(self.path).query).get("guion", [""])[0]
            ok, msg = kit_guardar(stem, datos)
            return self.enviar({"ok": ok, "msg": msg})
        if p == "/api/kit_disenar":
            largo2 = largo
            d = json.loads(self.rfile.read(largo2) or b"{}")
            stem = guion_de(d.get("canal", ""), d.get("dia", ""), d.get("hora", ""))
            if not stem:
                return self.enviar({"ok": False, "msg": "No encontré el guion"})
            perfiles = {}
            for f in Path("canales").glob("*.json"):
                try:
                    perfiles[json.loads(f.read_text()).get("canal", "").lstrip("@")] = f.stem
                except ValueError:
                    pass
            base, num = stem[:-3], str(int(stem[-2:]))
            env = dict(os.environ, CANAL=perfiles.get(d.get("canal", ""), "es"))
            r = subprocess.run([PY, "kit_visual.py", base, "--num", num, "--rehacer"], capture_output=True, text=True, env=env, timeout=900)
            return self.enviar({"ok": "✅" in (r.stdout or ""), "msg": (r.stdout or r.stderr)[-400:]})
        if p == "/api/sticker":    # hoja PNG generada en ChatGPT -> assets/stickers/entrada/ (solo PNG, max 20 MB)
            datos = self.rfile.read(min(largo, 20 << 20))
            nombre = re.sub(r"[^a-zA-Z0-9_-]", "", parse_qs(urlparse(self.path).query).get("n", ["hoja"])[0])[:60] or "hoja"
            ok = datos[:8] == b"\x89PNG\r\n\x1a\n"
            if ok:
                dest = Path("assets/stickers/entrada")
                dest.mkdir(parents=True, exist_ok=True)
                (dest / f"{nombre}.png").write_bytes(datos)
            self.send_response(200 if ok else 400)
            self.cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": ok}).encode())
            return
        d = json.loads(self.rfile.read(largo) or b"{}")
        if p == "/api/correr":
            ok, msg = lanzar(d.get("accion"), d.get("extra"))
            return self.enviar({"ok": ok, "msg": msg})
        if p == "/api/detener":
            return self.enviar({"ok": detener()})
        if p == "/api/plan":
            return self.enviar({"ok": responder_plan(d.get("lote"), d.get("sacar", []), d.get("cancelar", False))})
        if p == "/api/refinar":
            return self.enviar({"ok": marcar_refinar(d.get("canal"), d.get("dia", ""), bool(d.get("si")))})
        if p == "/api/nota":
            return self.enviar({"ok": guardar_nota(d.get("video", ""), d.get("dia", ""), d.get("hora", ""), d.get("texto", ""))})
        if p == "/api/usar_nuevo":
            return self.enviar({"ok": usar_nuevo(d.get("video", ""), d.get("dia", ""), d.get("hora", ""))})
        if p == "/api/descartar":
            return self.enviar({"ok": descartar(d.get("video", ""))})
        if p == "/api/rehacer_video":
            ok, msg = rehacer_video(d.get("canal", ""), d.get("dia", ""), d.get("hora", ""))
            return self.enviar({"ok": ok, "msg": msg})
        if p == "/api/repers_subido":
            import repers_estudio
            return self.enviar({"ok": repers_estudio.marcar(d.get("clave", ""), d.get("subido", True))})
        if p == "/api/video_subido":
            ok = video_subido(d.get("video", ""), d.get("dia", ""), d.get("hora", ""))
            if ok:
                registrar_subida(d.get("video", ""), d.get("dia", ""), d.get("hora", ""))
            return self.enviar({"ok": ok})
        if p == "/api/desmarcar":
            return self.enviar({"ok": desmarcar_subido(d.get("canal"), d.get("dia"))})
        if p == "/api/subido":
            return self.enviar({"ok": marcar_subido(d.get("canal"), d.get("dia"))})
        if p == "/api/ajustes":
            guardar_ajustes(d)
            return self.enviar({"ok": True})
        self.enviar({"error": "no existe"}, codigo=404)


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", PUERTO), H)
    url = f"http://localhost:{PUERTO}"
    print(f"🎬 Estudio abierto en {url}   (Ctrl+C para cerrar)")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        detener()
        print("\nEstudio cerrado.")


if __name__ == "__main__":
    main()
