"""Voz del guion con Kokoro (mismo modelo, voz y velocidad que voz.py del Mac) + tiempo de cada palabra.
Uso: python voz_local.py guion.json salida.wav [voz] [velocidad] [idioma]
Escribe salida.wav y salida_palabras.json (palabras del texto en pantalla con su inicio y fin).
El tiempo de cada frase es exacto (se sintetiza frase por frase); dentro de la frase se reparte por largo hablado.
"""
import sys, json, re, pathlib
import numpy as np
from entonacion import subir_final
import soundfile as sf
from kokoro_onnx import Kokoro

MODELOS = pathlib.Path("/mnt/user-data/uploads/gta-shorts/models")
PAUSA, PAUSA_COMA = 0.12, 0.10
UMBRAL_DB, MARGEN_INI, MARGEN_FIN = -55, 0.07, 0.08   # 25-nov Tao: menos pausa entre escenas (antes 0.15 / 0.10)


def recortar(a, sr):
    marco = max(1, int(0.01 * sr))
    n = len(a) // marco
    vol = np.sqrt((a[:n * marco].reshape(n, marco) ** 2).mean(1))
    voz = np.where(vol > vol.max() * 10 ** (UMBRAL_DB / 20))[0]
    if len(voz) == 0:
        return a
    a = a[max(0, voz[0] * marco - int(MARGEN_INI * sr)):min(len(a), (voz[-1] + 1) * marco + int(MARGEN_FIN * sr))].copy()
    f = min(len(a) // 2, int(0.008 * sr))
    a[:f] *= np.linspace(0, 1, f, dtype=a.dtype)
    a[-f:] *= np.linspace(1, 0, f, dtype=a.dtype)
    return a


def arranque(a, sr, ven=0.40, maxdb=14.0):
    """25-nov (Tao: "To get" se oye "get"): Kokoro dice muy bajo la primera palabra corta (To, But, So).
    Sube el inicio de la frase hasta el nivel del resto, solo donde hay voz, con transiciones suaves."""
    from scipy.ndimage import uniform_filter1d, maximum_filter1d
    e = uniform_filter1d(maximum_filter1d(np.abs(a), int(0.015 * sr)), int(0.03 * sr))
    vozm = e > e.max() * 10 ** (-40 / 20)
    if not vozm.any():
        return a
    i0 = int(np.argmax(vozm)); i1 = min(len(a), i0 + int(ven * sr))
    ref = np.median(e[vozm][int(ven * sr):] if vozm.sum() > ven * sr * 2 else e[vozm])
    g = np.ones(len(a))
    w = slice(i0, i1)
    g[w] = np.clip(ref * 0.8 / np.maximum(e[w], 1e-9), 1.0, 10 ** (maxdb / 20))
    g[w] = np.where(vozm[w], g[w], 1.0)
    rampa = np.clip((np.arange(i1, len(a)) - i1) / (0.06 * sr), 0, 1)
    g[i1:] = 1.0
    g = uniform_filter1d(g, int(0.025 * sr))
    return (a * g).astype(a.dtype)


def peso(w):
    """Largo hablado aproximado de una palabra del texto en pantalla (las cifras se dicen largas)."""
    d = re.sub(r"\D", "", w)
    if d:
        return 3.2 * len(d) + 2
    return len(re.sub(r"[^\wáéíóúñü]", "", w.lower())) + 1.2 + (1.5 if w[-1:] in ",.?!:" else 0)


def main():
    g_path, salida = sys.argv[1], pathlib.Path(sys.argv[2])
    voz = sys.argv[3] if len(sys.argv) > 3 else "em_alex"
    vel = float(sys.argv[4]) if len(sys.argv) > 4 else 1.3
    lang = sys.argv[5] if len(sys.argv) > 5 else "es"
    global PAUSA
    PAUSA = float(sys.argv[6]) if len(sys.argv) > 6 else PAUSA
    g = json.loads(pathlib.Path(g_path).read_text())
    frases, habladas = g["frases"], g.get("frases_voz") or g["frases"]
    assert len(frases) == len(habladas), "frases y frases_voz deben tener el mismo numero"
    k = Kokoro(str(MODELOS / "kokoro-v1.0.onnx"), str(MODELOS / "voices-v1.0.bin"))
    partes, palabras, t, sr = [], [], 0.0, 24000
    # 25-nov Tao: pausa larga (0,37 s) en puntos estrategicos: despues del gancho inicial, antes del segundo gancho
    # y antes del CTA; el resto 0,28 s. "pausa_larga_antes" = indices de frase ANTES de las cuales va la pausa larga.
    largas = set(g.get("pausa_larga_antes", [1, len(frases) - 1]))
    for nf, (f, h) in enumerate(zip(frases, habladas)):
        if nf in largas and partes:
            partes.append(np.zeros(int(sr * 0.09), dtype=partes[-1].dtype)); t += 0.09
        trozos = []                                  # cada oracion aparte: las preguntas suben al final
        for o in [x for x in re.split(r"(?<=[.?!])\s+", h.strip()) if x]:
            ao, sr = k.create(o, voice=voz, speed=vel, lang=lang, trim=False)
            ao = arranque(recortar(ao, sr), sr)
            if o.rstrip().endswith("?"):
                ao = subir_final(ao, sr, 4.0, 0.45)
            trozos += [ao, np.zeros(int(sr * 0.1), dtype=ao.dtype)]
        a = np.concatenate(trozos[:-1])
        d = len(a) / sr
        ws = f.split()
        pes = [peso(w) for w in ws]
        tot, acc = sum(pes), 0.0
        ini_voz, fin_voz = t + MARGEN_INI * 0.8, t + d - MARGEN_FIN
        for w, p in zip(ws, pes):
            i = ini_voz + (fin_voz - ini_voz) * acc / tot
            acc += p
            palabras.append({"w": w, "i": round(i, 3), "f": round(ini_voz + (fin_voz - ini_voz) * acc / tot, 3)})
        partes += [a, np.zeros(int(sr * PAUSA), dtype=a.dtype)]
        t += d + PAUSA
    audio = np.concatenate(partes)
    sf.write(salida, audio, sr)
    salida.with_name(salida.stem + "_palabras.json").write_text(json.dumps(palabras, ensure_ascii=False, indent=0))
    print(f"✅ {salida} ({len(audio) / sr:.1f}s)")


if __name__ == "__main__":
    main()
