"""🚦 SEMAFORO por canal: ¿el canal (o su nueva etapa) esta funcionando? Avisa y aconseja con una regla fija.

Regla (decidida ANTES de ver los datos, para no juzgar por un video ni por intuicion):
  - Se juzga a los 10 videos Y 14 dias de la etapa (antes: "🧪 en prueba", con avisos tempranos).
  - 4 señales:  1) se quedo a ver (viewed vs swiped, de Studio: se anota a mano)   ≥70% 🟢 · <50% 🔴
                2) % visto promedio (Analytics)                                     ≥70% 🟢 · <50% 🔴
                3) mediana de vistas a 24 h: ¿sube?  (2a mitad vs 1a mitad de la etapa) ≥×1.2 🟢 · ≤×0.8 🔴
                4) mejor video vs la mediana del canal                              ≥×3 🟢 · <×2 🔴
  - 2+ verdes → 🟢 SIGUE (escalar) · 3+ rojas → 🔴 (ronda 1: cambiar formato · ronda 2 = 20 videos: cortar el nicho)
    · lo demas → 🟡 AJUSTAR, con el diagnostico: se van al inicio = gancho · se quedan pero no terminan = cuerpo.
Los umbrales 1-2 son referencias externas (YouTube no publica un benchmark oficial); 3-4 son nuestros.

Etapas: datos/semaforo.json  ({"canal_token": {"desde": "AAAA-MM-DD", "nombre": "...", "etapa": "..."}}) — se crea solo.
Uso:  python semaforo.py                         (muestra el semaforo)
      python semaforo.py quedarse mdollarmistake 63   (anota el 'se quedo a ver' de Studio, ultimos 28 dias)
El 🧠 Director lo lee solo y lo pone arriba de sus decisiones.
"""
import sys, json, statistics, datetime as dt
from pathlib import Path

CONF = Path("datos/semaforo.json")
SALIDA = Path("datos/estrategia/12-semaforo.md")
INICIO = {
    "mdollarmistake": {"desde": "2026-11-15", "nombre": "MDM", "etapa": "negocios EN, 1 por semana"},
    "numbersigns": {"desde": "2026-11-20", "nombre": "Number Signs", "etapa": "numerología EN (canal nuevo)"},
    "therabbitloop": {"desde": "2026-11-20", "nombre": "The Rabbit Loop", "etapa": "full aliens"},
    "chichibitstv": {"desde": "2026-11-20", "nombre": "Coffee, But Why?", "etapa": "café EN (canal nuevo)"},
    "theviceversegg": {"desde": "2026-11-13", "nombre": "GTA EN (TheViceVerseGG)", "etapa": "relleno hasta el lanzamiento"},
    "viceversogg": {"desde": "2026-11-13", "nombre": "GTA ES (ViceVersoGG)", "etapa": "relleno hasta el lanzamiento"},
}
MIN_VIDEOS, MIN_DIAS = 10, 14


def conf():
    if not CONF.exists():
        CONF.parent.mkdir(parents=True, exist_ok=True)
        CONF.write_text(json.dumps(INICIO, ensure_ascii=False, indent=1), encoding="utf-8")
    d = json.loads(CONF.read_text(encoding="utf-8"))
    for k, v in INICIO.items():
        d.setdefault(k, v)
    return d


def color(valor, verde, rojo, mayor_es_mejor=True):
    if valor is None:
        return "⚪"
    if mayor_es_mejor:
        return "🟢" if valor >= verde else "🔴" if valor < rojo else "🟡"
    return "🟢" if valor <= verde else "🔴" if valor > rojo else "🟡"


def canal(nombre_token, c, vids):
    desde = c.get("desde", "2000-01-01")
    vs = sorted([v for v in vids if v["publicado"][:10] >= desde and (v.get("duracion") or 0) <= 180],
                key=lambda v: v["publicado"])
    n = len(vs)
    dias = max(0, (dt.date.today() - dt.date.fromisoformat(desde)).days)
    v24 = [v["a"]["24"] for v in vs if v["a"].get("24") is not None]
    ret = [v["retencion"] for v in vs if v.get("retencion") is not None]
    med = statistics.median(v24) if v24 else None
    # señales
    q = (c.get("quedarse") or {}).get("pct")
    pct = round(statistics.mean(ret), 1) if ret else None
    tend = None
    if len(v24) >= 4:
        mitad = len(v24) // 2
        a, b = statistics.median(v24[:mitad]), statistics.median(v24[mitad:])
        tend = round(b / max(a, 1), 2)
    mejor = round(max(v24) / max(med, 1), 1) if v24 and med else None
    s = {"quedarse": (q, color(q, 70, 50)), "pct_visto": (pct, color(pct, 70, 50)),
         "tendencia": (tend, color(tend, 1.2, 0.8)), "mejor": (mejor, color(mejor, 3, 2))}
    verdes = sum(1 for _, col in s.values() if col == "🟢")
    rojas = sum(1 for _, col in s.values() if col == "🔴")
    listo = n >= MIN_VIDEOS and dias >= MIN_DIAS
    ronda = 2 if n >= 2 * MIN_VIDEOS else 1
    if not listo:
        estado = "🧪 EN PRUEBA"
        consejo = f"Faltan {max(0, MIN_VIDEOS - n)} videos y {max(0, MIN_DIAS - dias)} días para juzgar. Mismo formato hasta entonces."
    elif verdes >= 2:
        estado, consejo = "🟢 SIGUE", "Funciona: subir a 2 videos al día y repetir el formato de los mejores."
    elif rojas >= 3:
        estado = "🔴 CORTAR" if ronda == 2 else "🔴 CAMBIAR FORMATO"
        consejo = ("Dos rondas sin señales: el nicho no prende con nosotros. Cerrar y elegir otro en 🧭 Nichos."
                   if ronda == 2 else "Ronda 1 sin señales: cambiar gancho y estilo, y dar 10 videos más.")
    else:
        estado, consejo = "🟡 AJUSTAR", "Hay algo, pero no alcanza."
    # diagnostico (sirve tambien en prueba, como aviso temprano)
    avisos = []
    if q is not None and q < 50:
        avisos.append("se van al inicio → el problema es el GANCHO (primera frase + primera imagen)")
    elif q is not None and q >= 70 and pct is not None and pct < 50:
        avisos.append("se quedan pero no terminan → el problema es el CUERPO (ritmo, largo, promesa que tarda)")
    if pct is not None and pct < 50 and q is None:
        avisos.append("% visto bajo: revisar ritmo y largo; anota el 'se quedó a ver' para saber si es el gancho")
    if tend is not None and tend <= 0.8:
        avisos.append(f"las vistas a 24 h van bajando (×{tend})")
    if mejor is not None and mejor >= 3:
        avisos.append(f"hay un video ×{mejor} sobre la mediana: copiar su gancho/tema")
    if q is None:
        avisos.append(f"falta el 'se quedó a ver': python semaforo.py quedarse {nombre_token} <pct>")
    return {"canal": nombre_token, "nombre": c.get("nombre", nombre_token), "etapa": c.get("etapa", ""), "desde": desde,
            "n": n, "dias": dias, "mediana24": med, "senales": s, "estado": estado, "consejo": consejo, "avisos": avisos}


def calcular():
    import metricas as M
    r = M.resumen()
    cf = conf()
    por = {k["canal"]: k["videos"] for k in r.get("canales", [])}
    return [canal(k, cf[k], por.get(k, [])) for k in cf]


def texto(filas=None):
    filas = filas if filas is not None else calcular()
    f = lambda x: "—" if x is None else x
    L = ["| Canal | Etapa | Videos | Días | Se quedó | % visto | Tendencia 24h | Mejor | Estado |", "|---|---|---|---|---|---|---|---|---|"]
    for k in filas:
        s = k["senales"]
        L.append(f"| {k['nombre']} | {k['etapa']} (desde {k['desde']}) | {k['n']}/{MIN_VIDEOS} | {k['dias']}/{MIN_DIAS} | "
                 f"{s['quedarse'][1]} {f(s['quedarse'][0])}% | {s['pct_visto'][1]} {f(s['pct_visto'][0])}% | "
                 f"{s['tendencia'][1]} ×{f(s['tendencia'][0])} | {s['mejor'][1]} ×{f(s['mejor'][0])} | **{k['estado']}** |")
    L.append("")
    for k in filas:
        L.append(f"- **{k['nombre']}** — {k['estado']}: {k['consejo']}")
        L += [f"   - ⚠️ {a}" for a in k["avisos"]]
    return "\n".join(L)


def main():
    a = sys.argv[1:]
    if a and a[0] == "quedarse" and len(a) >= 3:
        d = conf()
        d.setdefault(a[1], {"desde": dt.date.today().isoformat(), "nombre": a[1]})
        d[a[1]]["quedarse"] = {"pct": float(a[2]), "fecha": dt.date.today().isoformat()}
        CONF.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"✅ {a[1]}: se quedó a ver {a[2]}% (anotado)")
    t = texto()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(f"# 🚦 Semáforo de canales ({dt.datetime.now():%d/%m %H:%M})\n\n"
                      "_Regla fija: se juzga a los 10 videos y 14 días de cada etapa. "
                      "Umbrales de 'se quedó' y '% visto': referencias externas (YouTube no publica uno oficial)._\n\n" + t + "\n",
                      encoding="utf-8")
    print(t)


if __name__ == "__main__":
    main()
