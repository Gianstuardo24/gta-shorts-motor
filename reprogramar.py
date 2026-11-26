"""REPROGRAMAR los Shorts pendientes a N por dia (por defecto 3), corriendo la fila hacia adelante.

Toma, en orden, los Shorts pendientes de cada canal (carpetas de dia desde hoy + carpetas "Nuevos <lote>") y los
vuelve a repartir desde HOY en los horarios del canal ("horas_fijas" del perfil). Mueve video + texto, actualiza
la hora en el .txt, el registro horarios.json y renombra su version en "Nuevos rehechos" para que sigan emparejados.

Uso:  python reprogramar.py              -> SOLO muestra el plan (no mueve nada)
      python reprogramar.py --aplicar    -> lo aplica
"""
import os, re, sys, json, shutil
from datetime import datetime, timedelta, time
from pathlib import Path
from zoneinfo import ZoneInfo

ZONA = ZoneInfo("America/Santiago")
DIAS = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
RAIZ = Path(os.environ.get("YT_RAIZ", "~/Desktop/YouTube")).expanduser()
REG = Path("horarios.json")
CANALES = {"ViceVersoGG": "config.json", "TheViceVerseGG": "canales/en.json", "TheRabbitLoop": "canales/rabbit.json"}


def horas_de(perfil):
    d = json.loads(Path(perfil).read_text())
    return d.get("horas_fijas") or [14, 21, 22]


def pendientes(canal):
    hoy = datetime.now(ZONA).date().isoformat()
    out = []
    for d in sorted(canal.iterdir()):
        if d.is_dir() and re.match(r"\d{4}-\d{2}-\d{2} ", d.name) and d.name[:10] >= hoy:
            for v in sorted(d.glob("*.mp4")):
                m = re.match(r"(\d{2})h - (.*)$", v.stem)
                if m:
                    out.append({"orden": (d.name[:10], m.group(1)), "v": v, "titulo": m.group(2),
                                "viejo": (d.name[:10], m.group(1))})
    for d in sorted(canal.glob("Nuevos L*")):
        lote = d.name.split(" ", 1)[1]
        for v in sorted(d.glob("*.mp4")):
            m = re.match(r"(\d{2}) - (.*)$", v.stem)
            if m:
                out.append({"orden": ("9999" + lote, m.group(1)), "v": v, "titulo": m.group(2),
                            "stem": f"{lote}_{m.group(1)}"})
    return sorted(out, key=lambda x: x["orden"])


def slots(horas):
    minimo = datetime.now(ZONA) + timedelta(minutes=20)
    fecha = minimo.date()
    while True:
        for h in sorted(horas):
            s = datetime.combine(fecha, time(h), ZONA)
            if s > minimo:
                yield s
        fecha += timedelta(days=1)


def plan_canal(nombre, perfil):
    canal = RAIZ / nombre
    if not canal.exists():
        return []
    gen = slots(horas_de(perfil))
    return [{**p, "nuevo": next(gen)} for p in pendientes(canal)]


def aplicar(nombre, plan, reg):
    canal = RAIZ / nombre
    tmp = canal / "_reprogramando"
    tmp.mkdir(exist_ok=True)
    rehechos = canal / "Nuevos rehechos"
    for k, p in enumerate(plan):                      # fase 1: todo a una carpeta temporal (sin choques de nombres)
        p["tmp"] = []
        for f in (p["v"], p["v"].with_suffix(".txt")):
            if f.exists():
                t = tmp / f"{k:03d}{f.suffix}"
                shutil.move(str(f), t)
                p["tmp"].append(t)
        if "viejo" in p:
            fecha, hh = p["viejo"]
            for f in rehechos.glob(f"{fecha[5:]} {hh}h - *") if rehechos.exists() else []:
                t = tmp / f"r{k:03d}{f.suffix}"
                shutil.move(str(f), t)
                p["tmp"].append(t)
    for k, p in enumerate(plan):                      # fase 2: a su nuevo dia y hora
        s = p["nuevo"]
        dia = canal / f"{s:%Y-%m-%d} {DIAS[s.weekday()]}"
        dia.mkdir(exist_ok=True)
        nombre_v = f"{s:%H}h - {p['titulo']}"
        for t in p["tmp"]:
            if t.name.startswith("r"):
                rehechos.mkdir(exist_ok=True)
                shutil.move(str(t), rehechos / f"{s:%m-%d} {s:%H}h - {p['titulo']}{t.suffix}")
                continue
            destino = dia / f"{nombre_v}{t.suffix}"
            shutil.move(str(t), destino)
            if t.suffix == ".txt":
                txt = destino.read_text(encoding="utf-8")
                nueva = f"PUBLICAR: {DIAS[s.weekday()]} {s:%d/%m %H}:00 (hora de Chile)"
                txt = re.sub(r"^(PUBLICAR|HORARIO SUGERIDO): .*$", nueva, txt, count=1, flags=re.M)
                destino.write_text(txt, encoding="utf-8")
        stem = p.get("stem") or next((k2 for k2, v in reg.items() if v.get("canal", "").lstrip("@") == nombre
                                     and v.get("slot", "").startswith(f"{p['viejo'][0]}T{p['viejo'][1]}")), None)
        if stem:
            reg[stem] = {"canal": "@" + nombre, "slot": s.isoformat()}
    for d in list(canal.iterdir()):                   # carpetas que quedaron vacias
        if d.is_dir() and (re.match(r"\d{4}-\d{2}-\d{2} ", d.name) or d.name.startswith(("Nuevos L", "_reprogramando"))):
            try:
                if not any(d.iterdir()):
                    d.rmdir()
            except OSError:
                pass


def main():
    reg = json.loads(REG.read_text()) if REG.exists() else {}
    planes = {n: plan_canal(n, p) for n, p in CANALES.items()}
    for n, plan in planes.items():
        print(f"\n===== {n}  ({len(plan)} pendientes, horas {horas_de(CANALES[n])}) =====")
        dia_ant = None
        for p in plan:
            s = p["nuevo"]
            if s.date() != dia_ant:
                print(f"  {DIAS[s.weekday()]} {s:%d/%m}")
                dia_ant = s.date()
            antes = f"{p['viejo'][0][5:]} {p['viejo'][1]}h" if "viejo" in p else p["v"].parent.name
            print(f"     {s:%H}:00  {p['titulo'][:55]:55}  (antes: {antes})")
    if "--aplicar" not in sys.argv:
        print("\n(solo plan: nada se movio)  ->  para aplicarlo:  python reprogramar.py --aplicar")
        return
    for n, plan in planes.items():
        aplicar(n, plan, reg)
    REG.write_text(json.dumps(reg, ensure_ascii=False, indent=1))
    manana = (datetime.now(ZONA) + timedelta(days=1)).date()           # lo que viene despues de hoy: por refinar
    ref = Path("datos/por_refinar.json")
    d = json.loads(ref.read_text()) if ref.exists() else {}
    for n, plan in planes.items():
        fechas = {p["nuevo"].date().isoformat() for p in plan if p["nuevo"].date() >= manana}
        d[n] = sorted(set(d.get(n, [])) | fechas)
    ref.write_text(json.dumps(d, indent=1))
    print("\n✅ Reprogramado. Revisa el Estudio (pestaña Videos o vista Semana).")


if __name__ == "__main__":
    main()
