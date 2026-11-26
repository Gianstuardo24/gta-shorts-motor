"""PRODUCIR UN SHORT: guion (.json) → voz → tiempos → video animado + portada + .txt + ficha, en la carpeta del Estudio.

Uso (desde la carpeta del kit):
  ./venv/bin/python3 motor/producir.py guiones/2026-11-23/perros-18h.json --canal ejemplo --dia 2026-11-23 --hora 18
Opciones:
  --portada-seg 6.5     segundo del video para la portada (por defecto ~30 % del video)
  --muestras 1 4 9      solo hace cuadros sueltos en esos segundos (para revisar sin renderizar todo)
  --forzar              renderiza aunque la revisión encuentre problemas
Sale en: <carpeta_salida>/<carpeta del canal>/<AAAA-MM-DD Día>/HHh - Título.mp4  (+ .txt y .portada.jpg)
         datos/fichas/<carpeta>/<AAAA-MM-DD>_<HH>h.json   (lo que tiene el video, para el reporte semanal)
No corras dos a la vez: el motor usa una sola carpeta de trabajo.
"""
import re, sys, json, shutil, fcntl, subprocess, datetime as dt
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT))
import kit  # noqa: E402

ESC = KIT / "motor" / "escena"
PY = sys.executable
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
LANG = {"en": "en-us", "es": "es", "pt": "pt-br", "fr": "fr-fr", "it": "it"}


def revisar(g, c):
    """Reglas del PLAYBOOK que se pueden revisar solas. Devuelve (errores, avisos)."""
    err, av = [], []
    fr, fv = g.get("frases", []), g.get("frases_voz") or g.get("frases", [])
    if len(fr) != len(fv):
        err.append("frases y frases_voz tienen distinto número de elementos")
    for i, f in enumerate(fv):
        if "?" in f:
            err.append(f"frase_voz {i + 1} tiene '?': la voz IA dice mal las preguntas (escríbela como afirmación)")
        p = f.split()[0] if f.split() else ""
        if len(re.sub(r"\W", "", p)) == 1 and p.lower() not in ("a", "i"):
            av.append(f"frase_voz {i + 1} empieza con '{p}': la voz se la come")
    t = g.get("titulo", "")
    if not t:
        err.append("falta 'titulo'")
    elif len(re.sub(r"[^\w\s$%]", "", t).strip()) > 42:
        av.append(f"título de {len(t)} caracteres: sobre ~40 se corta en el celular")
    d = g.get("descripcion", "")
    if not d:
        av.append("falta 'descripcion' (1–2 frases que insinúan, sin contar el remate)")
    elif len(d.split()) > 25:
        av.append("descripción de más de ~20 palabras")
    if len(g.get("fuentes", [])) < 2:
        av.append("menos de 2 fuentes: cada dato tiene que estar verificado en 2 o más")
    if c.get("cta_voz") and c["cta_voz"].lower() not in " ".join(fv).lower():
        av.append(f"no está el CTA del canal en la voz: \"{c['cta_voz']}\"")
    return err, av


def correr(args, **kw):
    r = subprocess.run(args, cwd=str(ESC), capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print(r.stdout[-1500:], r.stderr[-1500:])
        raise SystemExit(f"❌ falló: {' '.join(map(str, args[:3]))}")
    return r.stdout


def datos(guion, wav, pal, destino):
    import os
    correr([PY, "armar_escena.py", str(guion), str(wav), str(pal), "/tmp/_nada.mp4", "deep"],
           env={**os.environ, "SOLO_DATOS": "1"})
    shutil.copy(ESC / "_tmp" / "datos.json", destino)
    return json.loads(Path(destino).read_text())


def nombre_archivo(titulo):
    t = "".join(ch for ch in titulo if ord(ch) < 0x2000)
    t = re.sub(r'[\\/:*?"<>|]', "", t)
    return re.sub(r"\s+", " ", t).strip()[:80] or "video"


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        print(__doc__)
        return
    src = Path(a[0]).resolve()
    op = lambda n, d=None: a[a.index(n) + 1] if n in a else d
    c = kit.canal(op("--canal") or sys.exit("falta --canal"))
    dia = op("--dia") or dt.date.today().isoformat()
    hora = int(op("--hora") or (c.get("horas") or [18])[0])
    g = json.loads(src.read_text(encoding="utf-8"))
    g.setdefault("marca", c.get("marca", ""))
    g.setdefault("acento", c.get("acento"))
    g.setdefault("lote", f"{c['id']}_{dia}_{hora:02d}")
    err, av = revisar(g, c)
    for x in av:
        print("⚠️ ", x)
    for x in err:
        print("⛔ ", x)
    if err and "--forzar" not in a:
        raise SystemExit("Corrige el guion (o usa --forzar).")

    lock = open(ESC / ".produciendo", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("Ya hay otro video produciéndose. Espera a que termine.")

    trab = KIT / "datos" / "trabajo" / g["lote"]
    trab.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, trab / "guion_src.json")
    # 1) voz
    print("🎙️  voz…")
    wav = trab / "vz.wav"
    base = trab / ("vz_base.wav" if c.get("voz_joven") else "vz.wav")
    voz = c["voz"][0] if isinstance(c.get("voz"), list) else c.get("voz", "af_heart")
    correr([PY, "voz_local.py", str(trab / "guion_src.json"), str(base), voz, str(c.get("velocidad", 1.2)),
            LANG.get(c.get("idioma", "en"), "en-us"), str(c.get("pausa", 0.12))])
    pal = trab / "vz_palabras.json"
    if c.get("voz_joven"):
        correr([PY, "joven.py", str(base), str(wav)])
        shutil.copy(trab / "vz_base_palabras.json", pal)
    # 2) tiempos → claves "momento+0.4" → guion final
    print("⏱️  tiempos…")
    datos(trab / "guion_src.json", wav, pal, trab / "datos0.json")
    correr([PY, str(KIT / "motor" / "resolver.py"), str(trab / "guion_src.json"), str(trab / "datos0.json"), str(trab / "guion.json")])
    d = datos(trab / "guion.json", wav, pal, trab / "datos.json")
    T = d["T"]
    print("   T:", " ".join(f"{k}={v:.1f}" for k, v in sorted(T.items(), key=lambda kv: kv[1])))
    if "--muestras" in a:
        ts = [x for x in a[a.index("--muestras") + 1:] if re.fullmatch(r"[\d.]+", x)]
        correr([PY, "muestras.py", str(trab / "datos.json"), str(trab / "muestras.png"), *ts])
        print(f"🖼️  {trab / 'muestras.png'}")
        return
    # 3) video
    print("🎬 render (tarda unos minutos)…")
    destino = kit.salida() / c["carpeta"] / f"{dia} {DIAS[dt.date.fromisoformat(dia).weekday()]}"
    destino.mkdir(parents=True, exist_ok=True)
    base_nombre = f"{hora:02d}h - {nombre_archivo(g['titulo'])}"
    mp4 = destino / f"{base_nombre}.mp4"
    correr([PY, "armar_escena.py", str(trab / "guion.json"), str(wav), str(pal), str(mp4), c.get("musica", "deep")])
    # 4) portada
    seg = float(op("--portada-seg") or g.get("portada_seg") or round(T.get("fin", 30) * 0.3, 1))
    correr([PY, "portada.py", str(mp4), str(seg), g.get("texto_portada") or g["titulo"],
            str(destino / f"{base_nombre}.portada.jpg"), c.get("acento") or "#ffd23f"])
    # 5) .txt (lo que se copia y pega en YouTube)
    tags = " ".join(dict.fromkeys(c.get("hashtags", []) + g.get("hashtags", [])))
    fuente = f"\nFuente: {g['fuente_texto']}\n" if g.get("fuente_texto") else ""
    (destino / f"{base_nombre}.txt").write_text(
        f"PUBLICAR: {DIAS[dt.date.fromisoformat(dia).weekday()]} {dia[8:10]}/{dia[5:7]} {hora:02d}:00 "
        f"({kit.config().get('zona_horaria')})\n\nTÍTULO:\n{g['titulo']}\n\nDESCRIPCIÓN:\n{g.get('descripcion', '')}\n"
        f"{fuente}\n{c.get('firma', '')}\n\n{tags}\n", encoding="utf-8")
    # 6) ficha
    esc = (g.get("escena") or {})
    ficha = {"gancho": g["frases"][0], "texto_pantalla": g.get("texto_pantalla", ""), "tema": g.get("tema") or g["titulo"],
             "micronicho": c.get("micronicho", ""), "formato": ",".join(e.get("tipo", "") for e in esc.get("escenas", [])),
             "voz": voz, "musica": c.get("musica", "deep"), "duracion_s": round(T.get("fin", 0), 1),
             "pregunta_cierre": esc.get("cierre", ""), "idioma": c.get("idioma", ""), "lote": g["lote"]}
    fdir = KIT / "datos" / "fichas" / c["carpeta"]
    fdir.mkdir(parents=True, exist_ok=True)
    (fdir / f"{dia}_{hora:02d}h.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"✅ {mp4}")


if __name__ == "__main__":
    main()
