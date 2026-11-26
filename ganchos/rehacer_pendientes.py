"""REHACER PENDIENTES: los Shorts que aun NO subiste y que salieron de la version vieja de la fabrica
(sin la musica actual, sin titulo en cinta, sin portada) se vuelven a montar con la version de hoy y musica nueva.

Como decide:
  - "Pendiente"  = esta en una carpeta de dia (AAAA-MM-DD ...) o en _reprogramando, NO en Subidos, y su hora no paso.
  - "Vieja"      = el .mp4 se armo antes del corte (por defecto 16-nov 20:00, cuando se aprobo el layout nuevo).
  - El guion se encuentra por el TITULO del .txt (contra salida/*_publicacion.md).
  - Musica: semilla nueva (cada rehecho suena distinto al original) y el estilo actual del canal
    (GTA: deep/tech · Rabbit: dark).  Misma voz y mismo guion: solo cambia montaje, musica, titulo y portada.
  - El video viejo NO se borra: se mueve a <canal>/_reemplazados/_viejo_<nombre>.mp4

Tambien revisa lo que YA SUBISTE (carpetas Subidos) y avisa cuales salieron sin musica (no se pueden resubir).

Uso:  python rehacer_pendientes.py              -> SOLO muestra el plan (no toca nada)
      python rehacer_pendientes.py --aplicar    -> rehace y reemplaza (con pausas para no calentar el Mac)
      --solo=rabbit|es|en   un canal          --corte=2026-11-16T20:00   otra fecha de corte
      --todos               rehace TODOS los pendientes (tambien los ya nuevos), con musica distinta
      --ordenar             mueve a Subidos/ los que ya pasaron su hora (⏰) y siguen en la carpeta del dia
      --atrasados           tambien rehace los que ya pasaron su hora y NO se subieron (ej. el de hoy 13h)
"""
import os, re, sys, json, time, shutil, subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ZONA = ZoneInfo("America/Santiago")
RAIZ = Path(os.environ.get("YT_RAIZ", "~/Desktop/YouTube")).expanduser()
CANALES = {"ViceVersoGG": "es", "TheViceVerseGG": "en", "TheRabbitLoop": "rabbit", "MillionDollarMistake": "mdm", "NumberSigns": "suerte", "ChiChibitsTV": "cafe"}
MUSICA = RAIZ / "Sonidos" / "Musica generada"
PY = sys.executable
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
ARGS = sys.argv[1:]
CORTE = datetime.fromisoformat(next((a.split("=", 1)[1] for a in ARGS if a.startswith("--corte=")), "2026-11-16T20:00")).replace(tzinfo=ZONA)
SOLO = next((a.split("=", 1)[1] for a in ARGS if a.startswith("--solo=")), "")


def norm(t):
    t = (t or "").lower().replace("¿", "").replace("¡", "")
    return re.sub(r"[^\wáéíóúñü ]+", " ", t).split()


def parecido(a, b):
    a, b = set(norm(a)), set(norm(b))
    return len(a & b) / max(len(a | b), 1)


def titulo_txt(txt):
    try:
        t = txt.read_text(encoding="utf-8")
    except Exception:
        return ""
    m = re.search(r"TÍTULO:\s*\n(.+)", t)
    return m.group(1).strip() if m else ""


def titulos_de_lotes():
    """salida/<lote>_publicacion.md -> [(titulo, lote, n)]"""
    out = []
    for md in sorted(Path("salida").glob("*_publicacion.md"), key=lambda p: p.stat().st_mtime):
        lote = md.name[:-len("_publicacion.md")]
        txt = md.read_text(encoding="utf-8")
        for bloque in re.split(r"\n## Short ", "\n" + txt)[1:]:
            n = int(re.match(r"(\d+)", bloque).group(1))
            m = re.search(r"### T[ií]tulo\s*\n```\s*\n(.+?)\n```", bloque)
            if m:
                out.append((m.group(1).strip(), lote, n))
    return out


_M4A = []


def tiene_musica(mp4, lote=None, n=None):
    """La musica de cada render se archiva como '<lote>[x|r]_NN - <titulo del guion> - estilo.m4a'.
    Un video lleva musica si existe un m4a de SU guion (mismo lote y titulo) creado antes de que se armara ese mp4.
    (Ojo: poner la portada re-escribe el mp4, asi que su fecha puede ser posterior; por eso se compara 'antes', no 'justo antes'.)"""
    if not _M4A:
        _M4A.extend((m.name, m.stat().st_mtime) for m in MUSICA.rglob("*.m4a"))
    t = mp4.stat().st_mtime
    if not lote:
        return any(0 <= t - mt <= 180 for _, mt in _M4A)
    try:
        tit = json.loads((Path("guiones") / f"{lote}_{n:02d}.json").read_text()).get("titulo", "")[:25].lower()
    except Exception:
        tit = ""
    for nombre, mt in _M4A:
        cab = nombre.split(" - ", 1)
        if mt <= t + 60 and re.match(re.escape(lote) + r"[a-z]?_\d\d$", cab[0]) and (
                cab[0] == f"{lote}_{n:02d}" or (tit and len(cab) > 1 and cab[1].lower().startswith(tit[:20]))):
            return True
    return False


def escanear():
    lotes = titulos_de_lotes()
    ahora = datetime.now(ZONA)
    pend, subidos = [], []
    for canal, perfil in CANALES.items():
        if SOLO and SOLO != perfil:
            continue
        base = RAIZ / canal
        if not base.exists():
            continue
        for mp4 in sorted(base.glob("Subidos/*/*.mp4")):
            tit = titulo_txt(mp4.with_suffix(".txt")) or mp4.stem.split(" - ", 1)[-1]
            p, lote, n = max([(parecido(tit, t), l, k) for t, l, k in lotes] or [(0, None, None)])
            subidos.append((canal, mp4.parent.name, mp4.stem, tiene_musica(mp4, lote if p >= 0.5 else None, n)))
        for carpeta in sorted(base.iterdir()):
            dia = re.match(r"(\d{4}-\d{2}-\d{2}) ", carpeta.name)
            if not carpeta.is_dir() or not (dia or carpeta.name == "_reprogramando"):
                continue
            for mp4 in sorted(carpeta.glob("*.mp4")):
                h = re.match(r"(\d{1,2})h - ", mp4.name)
                slot = datetime.fromisoformat(f"{dia.group(1)}T{int(h.group(1)):02d}:00").replace(tzinfo=ZONA) if dia and h else None
                armado = datetime.fromtimestamp(mp4.stat().st_mtime, ZONA)
                tit = titulo_txt(mp4.with_suffix(".txt")) or mp4.stem.split(" - ", 1)[-1]
                cand = [(parecido(tit, t), l, n) for t, l, n in lotes]
                p, lote, n = max(cand) if cand else (0, None, None)
                item = {"canal": canal, "perfil": perfil, "mp4": mp4, "slot": slot, "armado": armado, "titulo": tit,
                        "lote": lote if p >= 0.5 else None, "n": n, "parecido": round(p, 2),
                        "musica": tiene_musica(mp4, lote if p >= 0.5 else None, n)}
                if slot and slot < ahora and "--atrasados" not in ARGS:
                    item["estado"] = "paso"            # su hora ya paso y no esta en Subidos
                elif armado >= CORTE and "--todos" not in ARGS:
                    item["estado"] = "nuevo"
                elif not item["lote"]:
                    item["estado"] = "sin_guion"
                else:
                    item["estado"] = "rehacer"
                pend.append(item)
    return pend, subidos


def plan():
    pend, subidos = escanear()
    sin = [s for s in subidos if not s[3]]
    print(f"\n📤 YA SUBIDOS: {len(subidos)} · sin música: {len(sin)} (esos no se pueden volver a subir)")
    for canal, dia, nombre, _ in sin:
        print(f"   🔇 {canal} · {dia} · {nombre}")
    print("\n🗂️  PENDIENTES (aún no subidos):")
    icono = {"rehacer": "🔁 rehacer", "nuevo": "✅ ya es versión nueva", "paso": "⏰ su hora ya pasó (¿lo subiste sin moverlo a Subidos?)",
             "sin_guion": "❓ no encontré su guion"}
    for it in sorted(pend, key=lambda x: (x["canal"], x["slot"] or datetime.max.replace(tzinfo=ZONA))):
        cuando = f"{DIAS[it['slot'].weekday()]} {it['slot']:%d %Hh}" if it["slot"] else "reprogramando"
        g = f"{it['lote']}_{it['n']:02d}" if it["lote"] else "?"
        print(f"   {icono[it['estado']]:<14} · {it['canal']:<16} · {cuando:<13} · 🎵{'sí' if it['musica'] else 'NO'} · armado {it['armado']:%d/%m %H:%M} · {g} · {it['titulo'][:55]}")
    a_rehacer = [x for x in pend if x["estado"] == "rehacer"]
    print(f"\n👉 A rehacer: {len(a_rehacer)} videos  (~{len(a_rehacer) * 2.5:.0f} min con pausas).")
    if a_rehacer and "--aplicar" not in ARGS:
        print("   Para hacerlo:  python rehacer_pendientes.py --aplicar")
    return a_rehacer


def correr(args, perfil):
    env = dict(os.environ, CANAL=perfil)
    subprocess.run(["nice", "-n", "15", "caffeinate", "-i", PY] + args, check=True, env=env)


def aplicar(a_rehacer):
    grupos = {}
    for it in a_rehacer:
        grupos.setdefault((it["perfil"], it["lote"]), []).append(it)
    for (perfil, lote), items in grupos.items():
        items.sort(key=lambda x: x["n"])
        tb = lote + "r"                                 # lote temporal "rehecho": semilla de musica nueva
        for f in list(Path("guiones").glob(f"{tb}_[0-9][0-9].json")) + list(Path("audio").glob(f"{tb}_[0-9][0-9].wav")):
            f.unlink()
        falta_voz = False
        for k, it in enumerate(items, 1):
            shutil.copy2(Path("guiones") / f"{lote}_{it['n']:02d}.json", Path("guiones") / f"{tb}_{k:02d}.json")
            wav = Path("audio") / f"{lote}_{it['n']:02d}.wav"
            if wav.exists():
                shutil.copy2(wav, Path("audio") / f"{tb}_{k:02d}.wav")
            else:
                falta_voz = True
        print(f"\n===== [{perfil}] {lote}: rehaciendo {len(items)} ({', '.join(str(i['n']) for i in items)}) =====", flush=True)
        if falta_voz:
            correr(["voz.py", tb], perfil)
            time.sleep(15)
        correr(["montar.py", tb, "centro"], perfil)
        time.sleep(15)
        correr(["subtitular.py", f"clips/{tb}_narrado_momentos.json"], perfil)
        for k, it in enumerate(items, 1):
            nuevo = Path("salida") / f"{tb}_narrado_{k:02d}.mp4"
            if not nuevo.exists():
                print(f"   ⚠️ no salió {nuevo}; el original queda igual")
                continue
            viejo = it["mp4"]
            guardado = RAIZ / it["canal"] / "_reemplazados" / f"_viejo_{viejo.name}"
            guardado.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(viejo), guardado)
            shutil.copy2(nuevo, viejo)
            portada = nuevo.with_name(nuevo.stem + ".portada.jpg")
            if portada.exists():
                shutil.copy2(portada, viejo.with_name(viejo.stem + ".portada.jpg"))
            print(f"   🔁 {viejo.parent.name}/{viejo.name}", flush=True)
            if Path("control_final.py").exists():
                subprocess.run([PY, "control_final.py", str(viejo)])
        print("   ❄️  pausa 15 s para enfriar…", flush=True)
        time.sleep(15)
    try:
        import panel
        panel.generar()
    except Exception:
        pass
    print("\n✅ Listo: los pendientes quedaron con la versión nueva (los viejos están en _reemplazados/_viejo_…).")


def ordenar():
    """Los que ya pasaron su hora (⏰) se mueven a Subidos/<dia>/ con su .txt y portada: asi dejan de verse como pendientes."""
    pend, _ = escanear()
    n = 0
    for it in pend:
        if it["estado"] != "paso":
            continue
        mp4 = it["mp4"]
        destino = RAIZ / it["canal"] / "Subidos" / mp4.parent.name
        destino.mkdir(parents=True, exist_ok=True)
        for f in [mp4, mp4.with_suffix(".txt"), mp4.with_name(mp4.stem + ".portada.jpg")]:
            if f.exists():
                shutil.move(str(f), destino / f.name)
        print(f"   📤 {it['canal']} · {mp4.parent.name}/{mp4.name} → Subidos")
        n += 1
    print(f"   {n} movidos a Subidos.")


if __name__ == "__main__":
    if "--ordenar" in ARGS:
        ordenar()
    lista = plan()
    if "--aplicar" in ARGS and lista:
        aplicar(lista)
