"""MODO TELEFONO del Estudio: una pagina simple para el celular (mismo Wi-Fi) con los videos de hoy y manana,
botones para copiar titulo / descripcion y para abrir o guardar el video. Solo lectura.

Seguridad:
  - Es un servidor APARTE (puerto 8001) que solo responde rutas /m/<clave>/...  Todo lo demas da 404.
  - La clave es secreta y aleatoria (secretos/movil_clave.txt). Sin la clave no se ve nada.
  - El Estudio normal (puerto 8000) sigue escuchando solo en este Mac.
El QR se dibuja con 'segno' si esta instalado (pip install segno); si no, el panel muestra el link para escribirlo.
"""
import json, socket, secrets, threading, datetime as dt
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from http.server import ThreadingHTTPServer

PUERTO_MOVIL = 8001
CLAVE_F = Path("secretos/movil_clave.txt")
NOMBRES = {"ViceVersoGG": ("GTA ES", "#ff3cac"), "TheViceVerseGG": ("GTA EN", "#2be8ff"),
           "TheRabbitLoop": ("Rabbit", "#ff9a3c"), "MillionDollarMistake": ("MDM", "#5effa1"),
           "ChiChibitsTV": ("Café", "#c68642"), "NumberSigns": ("Number Signs", "#c9a0ff")}


def clave():
    if not CLAVE_F.exists():
        CLAVE_F.parent.mkdir(exist_ok=True)
        CLAVE_F.write_text(secrets.token_urlsafe(18))
    return CLAVE_F.read_text().strip()


def ip_local():
    """IP del Mac en el Wi-Fi (no envia nada: solo pregunta que interfaz usaria)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def url():
    return f"http://{ip_local()}:{PUERTO_MOVIL}/m/{clave()}/"


def qr_svg():
    try:
        import segno
    except ImportError:
        return None
    import io
    b = io.BytesIO()
    segno.make(url(), error="m").save(b, kind="svg", scale=6, border=2, dark="#000", light="#fff")
    return b.getvalue().decode()


def info():
    return {"url": url(), "qr": qr_svg()}


def lista(videos_fn, repers_fn):
    """Videos sin subir de hoy y manana (YouTube + Repers), en el formato simple que usa la pagina."""
    hoy = dt.date.today()
    dias = {hoy.isoformat(), (hoy + dt.timedelta(days=1)).isoformat()}
    out = []
    for k in videos_fn():
        nom, col = NOMBRES.get(k["canal"], (k["canal"], "#9d90c9"))
        for d in k["dias"]:
            if d.get("nuevo") or d["dia"][:10] not in dias:
                continue
            for it in d["items"]:
                if it.get("subido"):
                    continue
                out.append({"fecha": d["dia"][:10], "hora": it["hora"], "canal": nom, "color": col,
                            "titulo": it.get("titulo") or it.get("nombre", ""), "desc": it.get("descripcion", ""),
                            "video": it["video"], "src": "yt"})
    try:
        for it in repers_fn():
            if it.get("subido") or it.get("fecha") not in dias:
                continue
            out.append({"fecha": it["fecha"], "hora": it["hora"], "canal": it.get("canal", "Repers"), "color": "#ffd23f",
                        "titulo": it.get("titulo", ""), "desc": it.get("descripcion", ""), "video": it["video"], "src": "r"})
    except Exception:
        pass
    out.sort(key=lambda x: (x["fecha"], str(x["hora"]).zfill(2)))
    return out


def iniciar(H, videos_fn, repers_fn, miniatura_fn, repers_base):
    """Arranca el servidor del telefono en un hilo. H = handler del Estudio (se reusan enviar/media)."""
    k = clave()
    pagina = Path("movil.html")

    class HM(H):
        def do_POST(self):
            self.enviar({"error": "no existe"}, codigo=404)

        def do_GET(self):
            u = urlparse(self.path)
            q = parse_qs(u.query)
            pre = f"/m/{k}/"
            if not u.path.startswith(pre):
                return self.enviar({"error": "no existe"}, codigo=404)
            r = u.path[len(pre):]
            if r == "":
                return self.enviar(pagina.read_text(encoding="utf-8"), "text/html")
            if r == "api":
                return self.enviar(lista(videos_fn, repers_fn))
            p, src = q.get("p", [""])[0], q.get("src", ["yt"])[0]
            base = repers_base if src == "r" else None
            if r == "media":
                return self.media(p, q.get("dl", [""])[0] == "1", base=base)
            if r == "mini":
                m = miniatura_fn(p, base=base)
                return self.enviar(m.read_bytes(), "image/jpeg") if m else self.enviar({"error": "no existe"}, codigo=404)
            return self.enviar({"error": "no existe"}, codigo=404)

        def log_message(self, *a):
            pass

    try:
        srv = ThreadingHTTPServer(("0.0.0.0", PUERTO_MOVIL), HM)
    except OSError as e:
        print(f"📱 Modo teléfono no pudo abrir el puerto {PUERTO_MOVIL}: {e}")
        return None
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    print(f"📱 Modo teléfono: {url()}   (mismo Wi-Fi; el QR está en el panel, botón 📱)")
    return srv
