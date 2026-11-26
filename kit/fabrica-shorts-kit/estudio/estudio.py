"""ESTUDIO: la página donde ves, copias y descargas tus Shorts listos para subir.

Abrir (desde la carpeta del kit):   ./venv/bin/python3 estudio/estudio.py      → http://localhost:8765
Lee la carpeta de salida en vivo (config.json → carpeta_salida): si reemplazas un archivo, recarga la página (Cmd+R).
Pestañas: Para subir · Subidos · Reporte (el último de analisis/) · Canales (canales/*.json y planes/*.md).
Solo escucha en tu propio computador (127.0.0.1).
"""
import re, sys, json, shutil, mimetypes, datetime as dt
from pathlib import Path
from urllib.parse import urlparse, parse_qs, quote
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT))
import kit  # noqa: E402

AQUI = Path(__file__).resolve().parent
SUBIDAS = KIT / "datos" / "subidas.json"


def raiz():
    return kit.salida()


def seguro(rel):
    """Ruta dentro de la carpeta de salida (nunca fuera)."""
    p = (raiz() / rel).resolve()
    if raiz().resolve() not in p.parents:
        raise ValueError("ruta fuera de la carpeta de salida")
    return p


def leer_txt(p):
    s = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    t = re.search(r"T[IÍ]TULO:\s*\n(.+)", s)
    d = s.split("DESCRIPCIÓN:", 1)[1].strip() if "DESCRIPCIÓN:" in s else ""
    return (t.group(1).strip() if t else ""), d


def videos():
    """Por canal: días con sus videos (pendientes y los subidos de los últimos 14 días)."""
    hoy = dt.date.today()
    out = []
    for c in kit.canales().values():
        base = raiz() / c.get("carpeta", c["id"])
        dias = {}
        for mp4 in sorted(base.glob("**/*.mp4")) if base.exists() else []:
            partes = mp4.relative_to(base).parts
            if any(x.startswith("_") for x in partes[:-1]):
                continue
            m = re.match(r"(\d{4}-\d{2}-\d{2})", mp4.parent.name)
            if not m:
                continue
            subido = "Subidos" in partes[:-1]
            if subido and (hoy - dt.date.fromisoformat(m.group(1))).days > 14:
                continue
            titulo, desc = leer_txt(mp4.with_suffix(".txt"))
            por = mp4.with_name(mp4.stem + ".portada.jpg")
            dias.setdefault((mp4.parent.name, subido), []).append({
                "rel": str(mp4.relative_to(raiz())), "hora": mp4.name[:2] + ":00",
                "titulo": titulo or mp4.stem[6:], "desc": desc, "subido": subido,
                "portada": str(por.relative_to(raiz())) if por.exists() else None})
        out.append({"id": c["id"], "nombre": c.get("nombre", c["id"]), "carpeta": c.get("carpeta"),
                    "acento": c.get("acento"), "horas": c.get("horas", []),
                    "dias": [{"dia": d, "subido": s, "items": sorted(v, key=lambda x: x["hora"])}
                             for (d, s), v in sorted(dias.items())]})
    return out


def marcar_subido(rel):
    """Mueve el video (con su .txt y portada) a <canal>/Subidos/<día>/ y anota cuándo."""
    v = seguro(rel)
    if not v.is_file() or "Subidos" in v.relative_to(raiz()).parts:
        return False
    canal = raiz() / v.relative_to(raiz()).parts[0]
    destino = canal / "Subidos" / v.parent.name
    destino.mkdir(parents=True, exist_ok=True)
    for f in (v, v.with_suffix(".txt"), v.with_name(v.stem + ".portada.jpg")):
        if f.exists():
            shutil.move(str(f), destino / f.name)
    if v.parent.is_dir() and not any(v.parent.iterdir()):
        v.parent.rmdir()
    d = json.loads(SUBIDAS.read_text()) if SUBIDAS.exists() else {}
    d[rel] = dt.datetime.now().isoformat(timespec="seconds")
    SUBIDAS.parent.mkdir(exist_ok=True)
    SUBIDAS.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    return True


def desmarcar(rel):
    v = seguro(rel)
    partes = v.relative_to(raiz()).parts
    if not v.is_file() or "Subidos" not in partes:
        return False
    destino = raiz() / partes[0] / v.parent.name
    destino.mkdir(parents=True, exist_ok=True)
    for f in (v, v.with_suffix(".txt"), v.with_name(v.stem + ".portada.jpg")):
        if f.exists():
            shutil.move(str(f), destino / f.name)
    if not any(v.parent.iterdir()):
        v.parent.rmdir()
    return True


def reporte():
    rs = sorted((KIT / "analisis").glob("reporte_*.md"))
    return {"nombre": rs[-1].name, "md": rs[-1].read_text(encoding="utf-8")} if rs else None


def canales_y_planes():
    planes = {p.stem: p.read_text(encoding="utf-8") for p in sorted((KIT / "planes").glob("*.md"))} \
        if (KIT / "planes").exists() else {}
    return {"canales": list(kit.canales().values()), "planes": planes}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def enviar(self, obj, tipo="application/json; charset=utf-8", code=200):
        b = obj if isinstance(obj, bytes) else json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def archivo(self, p, descargar=False):
        tam = p.stat().st_size
        rango = self.headers.get("Range")
        ini, fin = 0, tam - 1
        if rango and rango.startswith("bytes="):            # Safari necesita rangos para reproducir video
            a, _, b = rango[6:].partition("-")
            ini = int(a) if a else max(0, tam - int(b))
            fin = int(b) if (a and b) else tam - 1
        self.send_response(206 if rango else 200)
        self.send_header("Content-Type", mimetypes.guess_type(p.name)[0] or "application/octet-stream")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(fin - ini + 1))
        if rango:
            self.send_header("Content-Range", f"bytes {ini}-{fin}/{tam}")
        if descargar:
            self.send_header("Content-Disposition", f"attachment; filename*=UTF-8''{quote(p.name)}")
        self.end_headers()
        with open(p, "rb") as f:
            f.seek(ini)
            falta = fin - ini + 1
            while falta > 0:
                trozo = f.read(min(1 << 20, falta))
                if not trozo:
                    break
                try:
                    self.wfile.write(trozo)
                except (BrokenPipeError, ConnectionResetError):
                    return
                falta -= len(trozo)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path == "/":
                html = (AQUI / "estudio.html").read_text(encoding="utf-8")
                cfg = kit.config()
                html = html.replace("{{NOMBRE}}", cfg.get("nombre_estudio", "Estudio")) \
                           .replace("{{COLOR}}", cfg.get("color", "#ff2d95")).replace("{{COLOR2}}", cfg.get("color2", "#00e5ff"))
                return self.enviar(html.encode(), "text/html; charset=utf-8")
            if u.path == "/api/videos":
                return self.enviar(videos())
            if u.path == "/api/reporte":
                return self.enviar(reporte())
            if u.path == "/api/canales":
                return self.enviar(canales_y_planes())
            if u.path == "/archivo":
                p = seguro(q.get("rel", ""))
                if p.is_file():
                    return self.archivo(p, q.get("dl") == "1")
            self.enviar({"error": "no encontrado"}, code=404)
        except ValueError:
            self.enviar({"error": "ruta no permitida"}, code=403)

    def do_POST(self):
        u = urlparse(self.path)
        largo = int(self.headers.get("Content-Length", 0))
        d = json.loads(self.rfile.read(largo) or b"{}")
        try:
            if u.path == "/api/subido":
                return self.enviar({"ok": marcar_subido(d.get("rel", ""))})
            if u.path == "/api/desmarcar":
                return self.enviar({"ok": desmarcar(d.get("rel", ""))})
        except ValueError:
            return self.enviar({"error": "ruta no permitida"}, code=403)
        self.enviar({"error": "no encontrado"}, code=404)


if __name__ == "__main__":
    puerto = int(kit.config().get("puerto_estudio", 8765))
    print(f"🎬 Estudio en http://localhost:{puerto}   (carpeta: {raiz()})   Ctrl+C para cerrar")
    ThreadingHTTPServer(("127.0.0.1", puerto), H).serve_forever()
