"""DIRECTOR ESTRATEGICO: junta DATOS + CONOCIMIENTO y propone DECISIONES para mañana, canal por canal, con justificacion.

Lee (no inventa):
  - nuestros canales: videos de los ultimos 7 dias vs los 7 anteriores (vistas a 24 h, % visto), mejores y peores, palancas
  - calibracion: lo que predijo revisar.py vs lo que paso de verdad (se llena aca)
  - mercado: virales de la semana por tema (puntaje, tipos: tendencia vs reproducible, x100+)
  - conocimiento: cambios del arsenal y de las reglas de la semana, piezas con ✅/❌ propio
  - nichos: ranking del explorador · produccion: guiones pendientes, rechazados, cola de la biblioteca
Claude propone por canal: SUBIR | MANTENER | INVESTIGAR | REVISAR | PAUSAR, con evidencia, confianza y tareas concretas
(cuantos guiones, que piezas del arsenal, que experimento). Son PROPUESTAS: las aprueba Tao.
Separacion: DATOS (lo que paso) · CONOCIMIENTO (lo que creemos) · DECISIONES (esto).

Uso:  python director.py      (≈2-3 min; tambien corre solo al final del 📡 Radar completo)
Salida: Estudio › 🧠 Director (datos/estrategia/0-director.md) + tabla decisiones en datos/cerebro.db
"""
import json, sqlite3, statistics, datetime as dt
from pathlib import Path

import ganchos as G

CEREBRO = Path("datos/cerebro.db")
DOC = Path("datos/estrategia/0-director.md")
NOMBRES = {"viceversogg": "GTA ES (ViceVersoGG)", "theviceversegg": "GTA EN (TheViceVerseGG)", "therabbitloop": "The Rabbit Loop",
           "mdollarmistake": "MDM", "cafe": "Coffee, But Why?", "chichibitstv": "Coffee, But Why?", "numbersigns": "Number Signs"}
TEMA_CANAL = {"viceversogg": "gta", "theviceversegg": "gta", "therabbitloop": "aliens", "mdollarmistake": "negocios", "chichibitstv": "cafe",
              "numbersigns": "suerte"}

PROMPT = """Eres el DIRECTOR ESTRATEGICO de una fabrica de YouTube Shorts (canales: GTA 6 ES y EN — el juego ya salio; Tao NO tiene el juego:
formato GUIAS/TRUCOS (modo historia) explicados con animacion propia + material oficial, datos verificados en 2+ fuentes;
The Rabbit Loop — full aliens, EN; MDM — negocios, EN, sigue con 1 video por semana (no cortarlo sin datos);
Number Signs — canal NUEVO desde 20-nov, numerologia EN: tradicion + psicologia, sin horoscopo ni promesas;
Coffee, But Why? — cafe, EN, canal nuevo (ex-chichibistv)). Los videos de GTA programados hasta el lanzamiento son relleno ya hecho.
Te paso DATOS (rendimiento propio, mercado, produccion) y CONOCIMIENTO (arsenal, reglas, calibracion de predicciones, nichos).
Decide que hacer MAÑANA. Devuelve SOLO un objeto JSON:
{"resumen":"3-4 lineas: estado general y la decision mas importante",
 "canales":[{"canal":"gta_es|gta_en|rabbit|mdm|cafe","accion":"SUBIR|MANTENER|INVESTIGAR|REVISAR|PAUSAR",
   "justificacion":"por que, en 2-3 frases","evidencia":["dato concreto con cifra"],"confianza":"alta|media|baja",
   "tareas":[{"tipo":"guion|grabar|investigar|experimento|revisar|publicar","cantidad":N,"detalle":"..","piezas_arsenal":[ids]}],
   "riesgo":"que podria salir mal"}],
 "prioridades":["1. ..","2. .."],
 "experimentos":[{"hipotesis":"..","canal":"gta_es|gta_en|rabbit|mdm|cafe","variable":"una sola","variante_a":"control: como hacemos hoy",
   "variante_b":"la idea nueva, concreta","pieza_arsenal":id o null,"replicas":N,"metrica":"..","criterio":"cuando se da por comprobada"}],
 "intervencion_humana":["lo que necesita a Tao: grabar, aprobar, decidir, iniciar sesion..."],
 "alertas":["datos raros, caidas, riesgos de politica, cuota"]}
Reglas:
- Basa cada decision en evidencia del input (cifras). Si hay pocos datos, la accion correcta suele ser INVESTIGAR o MANTENER, no SUBIR.
- Separa ruido de señal: con pocas vistas, 1-2 videos no prueban nada. Considera explicaciones alternativas (tema del momento, horario).
- Tendencia (no se replica) ≠ reproducible (si se replica). No mezcles aprendizajes entre canales.
- Usa las piezas del arsenal por id cuando recomiendes guiones; prioriza las ✅ propias.
- Sé concreto: cantidades, temas, piezas, experimentos con replicas (minimo 6 videos por variante para sacar conclusiones).
- Experimentos: maximo 1 activo por canal; no propongas uno nuevo para un canal que ya tiene uno activo (mira el laboratorio).
- '% visto' sobre 100% es NORMAL en Shorts (la gente lo vuelve a ver en loop); no es un error de medicion.
- SEMAFORO: respeta su veredicto por canal. En "EN PRUEBA" no cambies el formato (salvo un aviso de gancho claro);
  en "AJUSTAR" ataca el diagnostico que trae (gancho o cuerpo); en "CAMBIAR FORMATO"/"CORTAR" proponlo explicitamente.
- Nunca: urgencia falsa, promesas, material ajeno, contenido de expectativa de GTA, ni REPUBLICAR el mismo video."""


def abrir():
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS decisiones (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha TEXT, canal TEXT, accion TEXT,
                 justificacion TEXT, evidencia TEXT, confianza TEXT, tareas TEXT, riesgo TEXT, estado TEXT DEFAULT 'propuesta')""")
    return c


def nuestros():
    pro = G.propios()
    try:      # palanca etiquetada por el Radar (ganchos) cuando el guion no la declaro
        et = dict(sqlite3.connect(G.DB).execute("SELECT id, palanca FROM ganchos WHERE origen='propio' ORDER BY fecha"))
        for p in pro:
            p["palanca_declarada"] = p.get("palanca_declarada") or et.get(p["id"])
    except Exception:
        pass
    ahora = dt.datetime.now(dt.timezone.utc)
    out, med_canal = [], {}
    por = {}
    for p in pro:
        por.setdefault(p["canal"], []).append(p)
    for canal, vs in por.items():
        con24 = [v for v in vs if v.get("vistas_24h") is not None]
        med_canal[canal] = statistics.median([v["vistas_24h"] for v in con24]) if con24 else None
        rec = [v for v in con24 if v["horas"] <= 7 * 24 + 24]
        ant = [v for v in con24 if 8 * 24 < v["horas"] <= 15 * 24]
        m = lambda xs, k: round(statistics.median([x[k] for x in xs if x.get(k) is not None]), 1) if [x for x in xs if x.get(k) is not None] else None
        orden = sorted(con24, key=lambda v: -v["vistas_24h"])
        out.append(f"- {NOMBRES.get(canal, canal)}: {len(vs)} videos en total · ultimos 7 dias: {len(rec)} videos, mediana 24h {m(rec, 'vistas_24h')}, "
                   f"% visto {m(rec, 'pct_visto')} · 7 dias anteriores: {len(ant)} videos, mediana 24h {m(ant, 'vistas_24h')} · "
                   f"mediana historica 24h {med_canal[canal]}\n"
                   + "".join(f"    ↑ \"{v['titulo']}\" {v['vistas_24h']} (24h) · {v.get('pct_visto')}% · palanca {v.get('palanca_declarada') or '?'}\n" for v in orden[:3])
                   + "".join(f"    ↓ \"{v['titulo']}\" {v['vistas_24h']} (24h) · {v.get('pct_visto')}%\n" for v in orden[-2:] if len(orden) > 3))
    return "\n".join(out), pro, med_canal


def calibrar(c, pro, med_canal):
    """Llena las evaluaciones de revisar.py con el resultado real (supera o no la mediana del canal a 24 h)."""
    try:
        filas = c.execute("SELECT guion, fecha, titulo, p_supera_mediana FROM evaluaciones WHERE aprobado=1 AND resultado IS NULL").fetchall()
    except sqlite3.OperationalError:
        return "(todavia no hay evaluaciones)"
    por_titulo = {p["titulo"]: p for p in pro}
    for g, f, t, p in filas:
        v = por_titulo.get(t)
        if v and v.get("vistas_24h") is not None and med_canal.get(v["canal"]):
            c.execute("UPDATE evaluaciones SET video_id=?, vistas_24h=?, resultado=? WHERE guion=? AND fecha=?",
                      (v["id"], v["vistas_24h"], "supera" if v["vistas_24h"] > med_canal[v["canal"]] else "no_supera", g, f))
    c.commit()
    r = c.execute("SELECT COUNT(*), AVG(p_supera_mediana), AVG(resultado='supera') FROM evaluaciones WHERE resultado IS NOT NULL").fetchone()
    if not r[0]:
        return "(aun no hay guiones revisados con resultado a 24 h)"
    return (f"{r[0]} guiones revisados con resultado: predijo en promedio {round((r[1] or 0) * 100)}% de probabilidad de superar la mediana; "
            f"superaron {round((r[2] or 0) * 100)}% → {'la revision es optimista' if (r[1] or 0) > (r[2] or 0) + 0.15 else 'la revision es pesimista' if (r[2] or 0) > (r[1] or 0) + 0.15 else 'calibrada'}")


def mercado(c):
    L = []
    try:
        hace7 = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=7)).isoformat()
        for tema, n, x100, tend, rep in c.execute("""SELECT tema, COUNT(*), SUM(ratio >= 100), SUM(tipos LIKE '%tendencia%'), SUM(tipos LIKE '%reproducible%')
                FROM virales WHERE publicado >= ? AND puntaje IS NOT NULL AND substr(tema,1,2) != 'x_' GROUP BY tema""", (hace7,)):
            top = c.execute("""SELECT titulo, ratio, vistas, tipos FROM virales WHERE tema=? AND publicado >= ? ORDER BY puntaje DESC LIMIT 4""",
                            (tema, hace7)).fetchall()
            L.append(f"- {tema}: {n} Shorts de la semana medidos · x100+ {x100 or 0} · tendencias {tend or 0} · reproducibles {rep or 0}\n"
                     + "".join(f"    \"{t[:70]}\" x{r} · {v:,} · {tp}\n" for t, r, v, tp in top))
    except sqlite3.OperationalError:
        pass
    return "\n".join(L) or "(sin datos de mercado: corre el 📡 Radar)"


def conocimiento(c):
    L = []
    try:
        hace7 = (dt.datetime.now() - dt.timedelta(days=7)).isoformat()
        for obj, acc, n in c.execute("SELECT objeto, accion, COUNT(*) FROM conocimiento_log WHERE fecha >= ? GROUP BY objeto, accion", (hace7,)):
            L.append(f"- {obj} · {acc}: {n} (ultimos 7 dias)")
        for i, a, t, n, p, ev, si, no in c.execute("""SELECT id, area, tema, nombre, pieza, evidencia, nos_funciono, no_funciono FROM arsenal
                WHERE estado='activa' ORDER BY (nos_funciono - no_funciono) DESC, evidencia DESC LIMIT 25"""):
            L.append(f"  arsenal #{i} [{a}/{t}] {n}: {p[:90]} · {ev} casos · nos ✅{si} ❌{no}")
        for sec, n in c.execute("SELECT seccion, COUNT(*) FROM reglas WHERE estado='activa' GROUP BY seccion"):
            L.append(f"- reglas activas {sec}: {n}")
    except sqlite3.OperationalError:
        pass
    return "\n".join(L) or "(sin conocimiento acumulado todavia)"


def nichos(c):
    try:
        import explorador as X
        filas = c.execute("""SELECT nicho, idioma, COUNT(*), AVG(pct_x3), AVG(puerta), AVG(sanos), AVG(techo), AVG(saturacion)
                             FROM nichos_scan GROUP BY nicho, idioma""").fetchall()
    except Exception:
        return "(sin explorador de nichos todavia)"
    t = sorted(((X.puntaje({"puerta": pu, "pct_x3": x3 or 0, "sanos": sa or 0, "techo": te or 0, "saturacion": sat or 0},
                          X.NICHOS.get(n, ("", "", True))[2]), n, l, k) for n, l, k, x3, pu, sa, te, sat in filas), reverse=True)
    return "\n".join(f"- {n} [{l}] puntaje {p} ({k} corridas)" for p, n, l, k in t[:10]) or "(sin datos)"


def produccion():
    pro_tit = set()
    try:
        pro_tit = {r[0] for r in sqlite3.connect(G.DB).execute("SELECT titulo FROM videos")}
    except Exception:
        pass
    pend, aprob, rech = [], 0, len(list(Path("guiones/_rechazados").glob("*.json"))) if Path("guiones/_rechazados").exists() else 0
    for g in sorted(Path("guiones").glob("*.json")):
        try:
            d = json.loads(g.read_text())
        except Exception:
            continue
        import re as _re
        m = _re.match(r"^[A-Z](\d{8})\d{2}(en)?_\d{2}$", g.stem)       # solo lotes con fecha (G/R/M/C/N + AAAAMMDD..)
        if not m or m.group(1) < (dt.date.today() - dt.timedelta(days=3)).strftime("%Y%m%d"):
            continue
        if d.get("titulo") not in pro_tit:
            ok = (d.get("revision") or {}).get("aprobado")
            aprob += bool(ok)
            pend.append(f"{g.stem} [{d.get('canal', 'gta')}] {d.get('titulo')} · revision: {'✅' if ok else '⏳' if ok is None else '❌'}")
    cola = ""
    try:
        cola = str(dict(sqlite3.connect("datos/inteligencia.db").execute("SELECT estado, COUNT(*) FROM cola GROUP BY estado").fetchall()))
    except Exception:
        pass
    return (f"guiones sin publicar (recientes): {len(pend)} · aprobados {aprob} · rechazados historicos {rech} · cola biblioteca {cola}\n"
            + "\n".join("  " + p for p in pend[:20]))


def tiempos():
    """Costo en tiempo por video (armar_uno.sh registra cada paso en datos/produccion.csv)."""
    f = Path("datos/produccion.csv")
    if not f.exists():
        return "(sin registro de tiempos todavia)"
    por = {}
    for linea in f.read_text().splitlines()[-600:]:
        x = linea.split(",")
        if len(x) >= 6:
            fecha, lote, canal, paso, seg, st = x[:6]
            d = por.setdefault(canal, {"lotes": set(), "seg": 0, "fallos": 0})
            d["lotes"].add(lote)
            d["seg"] += int(seg or 0)
            d["fallos"] += st != "0"
    return "\n".join(f"- {k}: {len(v['lotes'])} videos armados · {v['seg'] / 60 / max(len(v['lotes']), 1):.1f} min de maquina por video · "
                     f"{v['fallos']} pasos con error" for k, v in por.items())


def main():
    c = abrir()
    print("🧠 Director: juntando datos y conocimiento...", flush=True)
    a, pro, med = nuestros()
    cal = calibrar(c, pro, med)
    import laboratorio as LAB
    try:
        LAB.evaluar()
        lab = LAB.resumen()
    except Exception as e:
        lab = f"(laboratorio: {e})"
    try:
        import semaforo as SEM
        sem = SEM.texto()
    except Exception as e:
        sem = f"(semáforo: {e})"
    cal_clas = Path("datos/estrategia/13-clasificacion.md")
    clas = cal_clas.read_text(encoding="utf-8")[:1500] if cal_clas.exists() else "(sin auditoría todavía)"
    entrada = (f"## DATOS · semáforo de canales (regla fija)\n{sem}\n\n## DATOS · calidad de la clasificación del Radar\n{clas}\n\n## DATOS · nuestros canales\n{a}\n\n## DATOS · mercado (7 dias)\n{mercado(c)}\n\n## DATOS · produccion\n{produccion()}\n{tiempos()}\n\n"
               f"## CONOCIMIENTO · arsenal y reglas\n{conocimiento(c)}\n\n## CONOCIMIENTO · calibracion de predicciones\n{cal}\n\n"
               f"## CONOCIMIENTO · nichos\n{nichos(c)}\n\n## CONOCIMIENTO · laboratorio (experimentos)\n{lab}\n\n## PERFILES\n"
               + "\n".join(f"- {f.stem}: " + f.read_text(encoding="utf-8")[:900].replace("\n", " ") for f in sorted(Path("datos/perfiles").glob("*.json"))))
    try:
        import procedencia as PR
        pv = PR.version_prompt(c, "director", PROMPT)
    except Exception:
        pv = ""
    try:
        r = G.claude(PROMPT, entrada, timeout=1200)
        i = r.find("{")
        d = json.JSONDecoder().raw_decode(r, i)[0] if i >= 0 else {}
    except Exception as e:
        d = {"resumen": f"⚠️ No se pudo generar: {e}", "canales": []}
    hoy = dt.datetime.now().isoformat(timespec="minutes")
    for k in d.get("canales") or []:
        c.execute("INSERT INTO decisiones (fecha, canal, accion, justificacion, evidencia, confianza, tareas, riesgo) VALUES (?,?,?,?,?,?,?,?)",
                  (hoy, k.get("canal"), k.get("accion"), k.get("justificacion"), json.dumps(k.get("evidencia"), ensure_ascii=False),
                   k.get("confianza"), json.dumps(k.get("tareas"), ensure_ascii=False), k.get("riesgo")))
    c.commit()
    try:
        n = LAB.importar(d.get("experimentos"))
        LAB.exportar(LAB.abrir())
        if n:
            print(f"   🧪 {n} experimentos propuestos al laboratorio (los activas tú)", flush=True)
    except Exception as e:
        print(f"   ⚠️ laboratorio: {e}", flush=True)
    ic = {"SUBIR": "🚀", "MANTENER": "➡️", "INVESTIGAR": "🔍", "REVISAR": "🛠️", "PAUSAR": "⏸️"}
    L = [f"# 🧠 Director — decisiones para mañana ({dt.datetime.now():%d/%m %H:%M})", "",
         "_Propuestas basadas en DATOS + CONOCIMIENTO. Las apruebas tú. Prompt " + pv + "_", "", d.get("resumen", ""), "",
         "## 🚦 Semáforo de canales", "", sem, ""]
    for k in d.get("canales") or []:
        L += [f"## {ic.get(k.get('accion'), '•')} {k.get('canal')} — **{k.get('accion')}** _(confianza {k.get('confianza')})_", "",
              k.get("justificacion", ""), ""]
        L += [f"- 📊 {e}" for e in k.get("evidencia") or []]
        L += [f"- ☐ **{t.get('tipo')}** ×{t.get('cantidad')}: {t.get('detalle')}" + (f" · piezas {t.get('piezas_arsenal')}" if t.get("piezas_arsenal") else "")
              for t in k.get("tareas") or []]
        if k.get("riesgo"):
            L.append(f"- ⚠️ {k['riesgo']}")
        L.append("")
    if d.get("prioridades"):
        L += ["## 🎯 Prioridades", ""] + [f"- {p}" for p in d["prioridades"]] + [""]
    if d.get("experimentos"):
        L += ["## 🧪 Experimentos sugeridos", "", "| Hipótesis | Canal | Variable | Réplicas | Métrica | Criterio |", "|---|---|---|---|---|---|"]
        L += [f"| {x.get('hipotesis')} | {x.get('canal')} | {x.get('variable')} | {x.get('replicas')} | {x.get('metrica')} | {x.get('criterio')} |"
              for x in d["experimentos"]] + [""]
    if d.get("intervencion_humana"):
        L += ["## 🙋 Necesita a Tao", ""] + [f"- {x}" for x in d["intervencion_humana"]] + [""]
    if d.get("alertas"):
        L += ["## 🚨 Alertas", ""] + [f"- {x}" for x in d["alertas"]] + [""]
    L += ["## 📏 Calibración de la revisión de guiones", "", cal, ""]
    DOC.parent.mkdir(parents=True, exist_ok=True)
    DOC.write_text("\n".join(L), encoding="utf-8")
    print("✅ Director listo: Estudio › 🧠 Director", flush=True)


if __name__ == "__main__":
    main()
