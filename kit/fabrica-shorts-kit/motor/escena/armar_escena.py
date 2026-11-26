"""ESCENA: arma un Short con escena animada (escena.html) + voz + musica + efectos, sin stock ni stickers.
Uso: python armar_escena.py <guion.json> <voz.wav> <palabras.json> <salida.mp4> [estilo_musica]
Las marcas de tiempo de cada momento (T) salen de las palabras reales de la voz.
"""
import sys, os, json, re, unicodedata, subprocess, pathlib, random
import numpy as np, soundfile as sf

AQUI = pathlib.Path(__file__).parent.resolve()
SON = AQUI / "sonidos"
SR = 48000
CLAVES = {"pagaste", "pais", "tienda", "moneda", "local", "trescientos", "dolares", "impuestos", "cambia", "tu", "paid", "country", "store", "price", "taxes", "dollars", "cheapest", "korea", "convert", "live", "random", "missing", "pounds", "euros", "purpose", "arecibo", "minutes", "picture", "human", "dna", "solar", "m13", "years", "demonstration", "reply", "address", "aliens"}


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return re.sub(r"[^\w]", "", w)


def alinear(frases, palabras):
    """Asigna a cada palabra del guion su tiempo de inicio (busca hacia adelante; si no aparece, interpola)."""
    tokens = [(fi, w) for fi, f in enumerate(frases) for w in f.split()]
    pal = [(norm(p["w"]), p["i"], p["f"]) for p in palabras]
    tiempos, j = [], 0
    for fi, w in tokens:
        n = norm(w)
        hit = None
        for k in range(j, min(j + 6, len(pal))):
            if pal[k][0] == n or (n and pal[k][0] and (pal[k][0].startswith(n) or n.startswith(pal[k][0]))):
                hit = k
                break
        if hit is not None:
            tiempos.append(pal[hit][1])
            j = hit + 1
        else:
            tiempos.append(None)
    # interpolar huecos
    conocidos = [i for i, x in enumerate(tiempos) if x is not None]
    for i, x in enumerate(tiempos):
        if x is None:
            a = max([c for c in conocidos if c < i], default=None)
            b = min([c for c in conocidos if c > i], default=None)
            ta = tiempos[a] if a is not None else 0.0
            tb = tiempos[b] if b is not None else palabras[-1]["f"]
            ia, ib = (a if a is not None else -1), (b if b is not None else len(tiempos))
            tiempos[i] = ta + (tb - ta) * (i - ia) / max(1, ib - ia)
    return tokens, tiempos


def bloques(frases, tokens, tiempos, fin, max_pal=13):
    """Texto de arriba: una oracion por bloque; si es muy larga, se corta en la coma mas cercana a la mitad."""
    out, idx = [], 0
    for f in frases:
        ws = f.split()
        ts = tiempos[idx: idx + len(ws)]
        idx += len(ws)
        cortes, ini = [], 0
        for k, w in enumerate(ws):
            if w[-1] in ".?!" and k + 1 < len(ws):
                cortes.append((ini, k + 1))
                ini = k + 1
        cortes.append((ini, len(ws)))
        for a, b in cortes:
            if b - a > max_pal:
                comas = [k + 1 for k in range(a, b - 1) if ws[k][-1] in ",;:"]
                m = min(comas, key=lambda c: abs(c - (a + b) / 2)) if comas else (a + b) // 2
                out += [[ws[a:m], ts[a:m]], [ws[m:b], ts[m:b]]]
            else:
                out.append([ws[a:b], ts[a:b]])
    res = []
    for k, (ws, ts) in enumerate(out):
        b = out[k + 1][1][0] if k + 1 < len(out) else fin
        claves = [w for w in ws if re.search(r"\d", w) or norm(w) in CLAVES] or [max(ws, key=len)]
        res.append({"a": ts[0] - 0.05, "b": b - 0.05, "t": " ".join(ws), "k": claves, "w": ts})
    res[0]["a"] = 0
    return res


def momento(tokens, tiempos, frase, patron, desde=0.0):
    for (fi, w), t in zip(tokens, tiempos):
        if fi == frase and t >= desde and re.search(patron, norm(w)):
            return t
    raise ValueError(f"no encontre '{patron}' en la frase {frase}")


def inicio(tokens, tiempos, frase):
    return next(t for (fi, _), t in zip(tokens, tiempos) if fi == frase)


# ---------------- audio ----------------
def leer(p):
    x, sr = sf.read(str(p), always_2d=True)
    x = x.mean(axis=1).astype(np.float32)
    if sr != SR:
        n = int(len(x) * SR / sr)
        x = np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)
    return x


def poner(pista, x, t, g):
    i = int(t * SR)
    if i >= len(pista) or i < 0:
        return
    n = min(len(x), len(pista) - i)
    pista[i:i + n] += x[:n] * g


class Bolsa:
    """Elige sonidos de una lista sin repetir el mismo dos veces seguidas."""
    def __init__(self, archivos, rng):
        self.x = [leer(f) for f in archivos]
        self.rng, self.ult = rng, -1

    def sacar(self):
        op = [i for i in range(len(self.x)) if i != self.ult] or [0]
        self.ult = self.rng.choice(op)
        return self.x[self.ult]


def recorte(x, dur, fade=0.06):
    """Corta un sonido a 'dur' segundos con fundido de salida (para sonidos largos)."""
    n = min(len(x), int(dur * SR))
    x = x[:n].copy()
    f = min(n, int(fade * SR))
    if f:
        x[-f:] *= np.linspace(1, 0, f, dtype=x.dtype)
    return x


def _todos(*patrones):
    out = []
    for p in patrones:
        out += sorted(SON.glob(p))
    return out


# Sonidos del kit: todos sintetizados por motor/crear_sonidos.py (sin samples con licencia de terceros).
# Puedes agregar los tuyos en esas mismas carpetas con el mismo prefijo (ej. sonidos/ui/pop_04.wav).
CAMBIO = _todos("transicion/whoosh_*.wav")                       # whoosh CORTOS (nunca el largo que suena a giro)
APARECE = {"": _todos("ui/pop_*.wav", "ui/ding_*.wav", "tematicos/obturador_*.wav", "tematicos/moneda_*.wav"),
           "espacio": _todos("ui/pop_02.wav", "glitch/*.wav", "tematicos/obturador_*.wav")}
CAMBIO_EXTRA = {"espacio": _todos("glitch/*.wav")}
CAJAS = _todos("tematicos/caja_*.wav")
GOLPES = _todos("impacto/*.wav")


def efectos(D, T, rng, tema="", especiales=()):
    p = np.zeros(int(D * SR) + SR, np.float32)
    cambio = Bolsa(CAMBIO + CAMBIO_EXTRA.get(tema, []), rng)
    aparece = Bolsa(APARECE.get(tema, APARECE[""]), rng)
    caja = Bolsa(CAJAS, rng)
    golpe = Bolsa(GOLPES, rng)
    for k, t in sorted(T.items(), key=lambda kv: kv[1]):
        if k == "fin":
            continue
        if k.startswith("s_"):
            poner(p, cambio.sacar(), t - 0.08, 0.2)                 # cambio de escena = whoosh corto variado
        elif k in ("mx", "cl", "co", "ar", "amazon", "espana") or k.startswith("p_"):
            poner(p, recorte(caja.sacar(), 0.9), t + 0.6, 0.11)     # aparece un precio = caja registradora (rota 5)
        elif k in ("tres", "top", "demo"):
            poner(p, golpe.sacar(), t + 0.35, 0.33)
        else:
            poner(p, aparece.sacar(), t, 0.14)                      # algo aparece = pop variado y bajo
    for i in range(5):                                              # estrellas que se encienden
        poner(p, aparece.sacar(), 0.2 + i * max(0.2, T.get("paises", T.get("adrede", 2)) - 0.4) / 5, 0.06)
    for e in especiales:                                            # sonidos pensados para ESTE guion
        if e["k"] in T or e["k"] == "0":
            t = (0 if e["k"] == "0" else T[e["k"]]) + e.get("off", 0)
            if not (SON / e["f"]).exists():
                print("   (falta el sonido", e["f"], "→ se salta)")
                continue
            x = leer(SON / e["f"])
            if e.get("desde"):
                x = x[int(e["desde"] * SR):]
            if e.get("dur"):
                x = recorte(x, e["dur"], e.get("fade", 0.25))
            if e.get("pico"):                                       # alinear el pico del sonido con el momento
                t -= np.argmax(np.abs(x)) / SR
            poner(p, x, max(0, t), e.get("g", 0.15))
    return p[: int(D * SR)]


def main():
    g_path, wav, pal_path, salida = sys.argv[1:5]
    estilo = sys.argv[5] if len(sys.argv) > 5 else "deep"
    g = json.loads(pathlib.Path(g_path).read_text())
    palabras = json.loads(pathlib.Path(pal_path).read_text())
    voz = leer(wav)
    Dv = len(voz) / SR
    D = round(Dv + 1.6, 2)                    # aire al final para el cierre
    frases = g["frases"]
    tokens, tiempos = alinear(frases, palabras)
    fr = bloques(frases, tokens, tiempos, D)
    I = lambda f: inicio(tokens, tiempos, f)
    M = lambda f, pat: momento(tokens, tiempos, f, pat)
    T = {}
    for clave, fr_i, patron in g["escena"]["momentos"]:
        T[clave] = I(fr_i) if patron is None else M(fr_i, patron)
    T["fin"] = D
    e = g["escena"]
    datos = {"frases": fr, "T": T, "marca": g.get("marca", ""),
             "cierre": e.get("cierre", "¿Y TÚ?"), "cierre2": e.get("cierre2", "Comenta tu país"),
             "paises": e.get("paises", ["MX", "AR", "CL", "CO", "PE", "ES", "UY", "US"])}
    if e.get("cta"):
        datos["cta"] = e["cta"]
    if e.get("like"):
        datos["like"] = e["like"]
    if e.get("escenas"):
        datos["escenas"] = e["escenas"]
    for k in ("tema", "acento"):
        if g.get(k):
            datos[k] = g[k]
    tmp = AQUI / "_tmp"
    tmp.mkdir(exist_ok=True)
    (tmp / "datos.json").write_text(json.dumps(datos, ensure_ascii=False))
    print("T =", {k: round(v, 2) for k, v in T.items()})
    if os.environ.get("SOLO_DATOS"):                         # solo calcular tiempos (lo usa producir.py)
        return
    # video
    video_previo = os.environ.get("VIDEO_PREVIO")           # solo rehacer el audio sobre un video ya renderizado
    if video_previo:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video_previo, "-an", "-c:v", "copy", str(tmp / "video.mp4")], check=True)
    else:
        subprocess.run([sys.executable, str(AQUI / "render.py"), "0", str(D), "30", str(tmp / "video.mp4"), str(tmp / "datos.json")], check=True)
    # musica (generador del Estudio) + efectos
    sys.path.insert(0, str(AQUI))
    import musica
    musica.CARPETA = SON / "musica"
    mus, info = musica.generar(D, g.get("lote", "x") + "_escena", estilo)
    print("musica:", info)
    rng = random.Random(g.get("lote", "x"))
    fx = efectos(D, T, rng, g.get("tema", ""), g.get("escena", {}).get("sfx", []))
    n = int(D * SR)
    v = np.zeros(n, np.float32)
    v[: len(voz)] = voz[:n]
    m = np.zeros(n, np.float32)
    m[: min(n, len(mus))] = mus[:n]
    # la musica se agacha cuando habla la voz
    env = np.abs(v)
    k = int(0.25 * SR)
    env = np.convolve(env, np.ones(k) / k, mode="same")
    duck = 1 - 0.55 * np.clip(env / (env.max() * 0.25 + 1e-6), 0, 1)
    mezcla = v * 1.0 + m * 0.22 * duck + fx
    sf.write(tmp / "mezcla.wav", mezcla / max(1.0, np.abs(mezcla).max() / 0.95), SR)
    # volumen: 2 pasadas de loudnorm (objetivo -14 LUFS, pico -1.5)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(tmp / "mezcla.wav"), "-af", "loudnorm=I=-14:TP=-2:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(r[r.rindex("{"): r.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-2:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,volume=2dB,alimiter=limit=0.8:level=false:attack=3:release=60")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp / "video.mp4"), "-i", str(tmp / "mezcla.wav"),
                    "-af", ln, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", "-movflags", "+faststart", salida], check=True)
    # si quedo bajo -14.6 LUFS, sube la ganancia sin pasar el pico
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", salida, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    li = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1])
    if li < -14.6:
        tmp2 = str(tmp / "subir.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", salida, "-af", f"volume={-14.1 - li:.1f}dB,alimiter=limit=0.84:level=false",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", tmp2], check=True)
        pathlib.Path(tmp2).replace(salida)
        print(f"   volumen {li} -> ~-14 LUFS")
    print("✅", salida)


if __name__ == "__main__":
    main()
