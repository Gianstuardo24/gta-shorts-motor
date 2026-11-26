"""LOTE: investiga -> te propone el plan -> genera los Shorts en ESPANOL e INGLES.

Uso:
  python lote.py                  todo: biblioteca + radares + plan + produccion (6 Shorts por canal)
  python lote.py --videos 4       cuantos Shorts por canal
  python lote.py --sin-radar      usa los ultimos radares (si los corriste hace poco)
  python lote.py --si             aprueba el plan sin preguntar
  python lote.py --sin-ver        no mira los videos (solo lee lo que dicen): mas rapido
  python lote.py --web            el plan se aprueba desde el Estudio (python estudio.py), no en la terminal
Formato vertical opcional al final: blur | centro
"""
import os, re, sys, json, math, time, subprocess, datetime as dt
from pathlib import Path
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from utilidades import extraer_json, cfg

PY = sys.executable
CANALES = ["es", "en"]
LEER = 8              # videos virales que se leen por idioma
IDEAS_POR_TEMA = 2
CFG = cfg()
NAV = CFG.get("cookies_navegador")
N_VER = CFG.get("ver_videos", 4)   # cuantos de los mas virales se MIRAN (imagen + audio)


class Silencio:
    def debug(self, m): pass
    def info(self, m): pass
    def warning(self, m): pass
    def error(self, m): pass


def titulo(t):
    print(f"\n{'=' * 60}\n{t}\n{'=' * 60}")


# ---------------- 1. biblioteca y radares ----------------
def biblioteca():
    titulo("🎬 1/5  Biblioteca de tomas (kit oficial de Rockstar)")
    subprocess.run([PY, "tomas.py", "--kit"])
    if not Path("tomas/catalogo.json").exists():
        print("⛔ La biblioteca esta vacia y no se pudo bajar el kit. Revisa tu conexion y vuelve a correr.")
        sys.exit(1)


def radares():
    titulo("📡 2/5  Radares ES + EN en paralelo (3 a 5 min)")
    procs = []
    for c in CANALES:
        Path("radar", c).mkdir(parents=True, exist_ok=True)
        log = open(Path("radar", c, "_log.txt"), "w")
        procs.append((c, subprocess.Popen([PY, "radar.py"], env=dict(os.environ, CANAL=c),
                                          stdout=log, stderr=subprocess.STDOUT), log))
    for c, p, log in procs:
        p.wait()
        log.close()
        cola = Path("radar", c, "_log.txt").read_text().strip().splitlines()[-1:] or [""]
        print(f"   {'✅' if p.returncode == 0 else '⚠️'} radar {c.upper()}: {cola[0][:90]}")


# ---------------- 2. embudo: los mas virales que no usamos ----------------
def id_de(v):
    return v.get("id") or v["url"].split("v=")[-1][:11]


def usados(c):
    p = Path(f"usados_{c}.txt")
    return set(p.read_text().split()) if p.exists() else set()


def embudo():
    elegidos, vistos = [], set()
    for c in CANALES:
        p = Path("radar", c, "ultimo.json")
        if not p.exists():
            continue
        ya = usados(c)
        vids = [v for v in json.loads(p.read_text()) if id_de(v) not in ya]
        puntaje = lambda v: (v.get("velocidad") or v.get("vph", 0)) * (1 + math.log10(1 + max(v.get("multi", 0), 0)))
        for v in sorted(vids, key=puntaje, reverse=True)[:LEER]:
            if id_de(v) not in vistos:
                vistos.add(id_de(v))
                elegidos.append({**v, "id": id_de(v), "mercado": c})
    return elegidos


# ---------------- 3. leer lo que dicen (solo subtitulos, nunca el video) ----------------
def con_tiempos(data, cada=30):
    bloques = {}
    for ev in data.get("events", []):
        txt = "".join(s.get("utf8", "") for s in ev.get("segs", [])).replace("\n", " ").strip()
        if txt:
            k = int(ev.get("tStartMs", 0) / 1000 // cada * cada)
            bloques.setdefault(k, []).append(txt)
    return "\n".join(f"[{k // 60}:{k % 60:02d}] {' '.join(v)}" for k, v in sorted(bloques.items()))


def leer(v):
    from yt_dlp import YoutubeDL
    opts = {"quiet": True, "skip_download": True, "noplaylist": True, "logger": Silencio()}
    if NAV:
        opts["cookiesfrombrowser"] = (NAV,)
    try:
        with YoutubeDL(opts) as y:
            info = y.extract_info(v["url"], download=False)
            orig = info.get("language") or ""
            prefs = [f"{orig}-orig", orig, "en-orig", "en", "en-US", "es-orig", "es", "es-419"]
            for fuente in ("subtitles", "automatic_captions"):
                subs = info.get(fuente) or {}
                for lang in [l for l in prefs if l] + list(subs):
                    fmt = next((f for f in subs.get(lang, []) if f.get("ext") == "json3"), None)
                    if fmt:
                        return {**v, "texto": con_tiempos(json.loads(y.urlopen(fmt["url"]).read().decode()))[:9000],
                                "descripcion": (info.get("description") or "")[:800]}
            return {**v, "texto": "", "descripcion": (info.get("description") or "")[:800]}
    except Exception:
        return {**v, "texto": "", "descripcion": ""}


def ficha(k, v):
    return (f"### VIDEO {k} (id {v['id']}, mercado {v['mercado'].upper()}) {'[CANAL OFICIAL]' if v.get('oficial') else ''}\n"
            f"TITULO: {v['titulo']}\nCANAL: {v.get('canal')} · {v.get('subs', 0):,} subs · {v.get('vistas', 0):,} vistas · "
            f"{v.get('vph', 0):,} vistas/hora · multiplicador x{v.get('multi', 0)} · {v.get('tipo')} "
            f"{'· ACELERANDO' if v.get('acelera') else ''}\nDESCRIPCION: {v.get('descripcion', '')}\n"
            f"LO QUE DICE:\n{v.get('texto') or '(sin subtitulos)'}\n{v.get('visual', '')}")


# ---------------- 4. plan (Claude) ----------------
PROMPT_PLAN = """Eres el estratega de dos canales de YouTube Shorts sobre GTA 6: __ES__ (espanol) y __EN__ (ingles).
Mismo contenido para ambos, adaptado a cada idioma. Te paso los videos MAS VIRALES de estos dias (ES y EN)
con sus numeros y LO QUE DICEN (subtitulos con minuto). Haz un embudo:
1. Detecta los TEMAS de los que habla la gente (historia, personajes, features, mapa, filtraciones, fechas, precios...).
   Un tema que aparece en VARIOS videos virales, o en uno con multiplicador alto o ACELERANDO, es mas fuerte.
2. Elige los __T__ mejores temas para hacer Shorts PROPIOS (no copiar a nadie: tomamos la informacion, no el video).
3. Por tema, __I__ ideas de Short distintas (angulos diferentes).
4. A cada idea asignale un "formato": lista_top, explicacion_sistema, comparacion, noticia, oficial_vs_rumor o detalles_ocultos.
   MEZCLA formatos en el lote (no todas noticias). Si te paso "FORMATOS QUE MEJOR RINDEN", prioriza esos.
5. Si te paso "BIBLIOTECA DE VIRALES": es lo mas valioso. Usa sus DATOS CLAVE e IDEAS (de los largos) para los temas
   y sus FORMULAS y HOOKS (de los Shorts) para el angulo. En "por_que" nombra que fichas respaldan la idea.
Responde SOLO un array JSON:
[{"tema": "nombre corto", "por_que": "1-2 frases con la evidencia (que videos, numeros)",
  "videos": [numeros de VIDEO que lo tratan], "riesgo": "confirmado | rumor | mezcla",
  "ideas": [{"titulo": "titulo en espanol", "hook": "primera frase en espanol", "angulo": "que aportamos", "formato": "lista_top"}]}]"""

PROMPT_GUIONES = """Eres guionista de YouTube Shorts virales sobre GTA 6 para el canal en espanol __ES__.
Te paso el PLAN aprobado y la investigacion (lo que dicen los videos virales). Escribe UN guion por cada idea del plan, en orden.
- NO copies frases ni la estructura de ningun video: usa la informacion y cuentala a tu manera.
- Respeta el "formato" de cada idea. lista_top: el hook anuncia el numero ("5 cosas que...") y cada punto empieza con su numero.
  comparacion: dos cosas frente a frente con cifras. oficial_vs_rumor: separa claramente lo confirmado de lo que no.
  explicacion_sistema: UN solo sistema del juego, que es y por que importa. Si te paso RECETAS, siguelas.
- Hook en 2 segundos -> 2 a 4 frases con los datos clave -> cierre con remate o pregunta para comentarios.
- 60 a 95 palabras (25 a 40 s). Frases cortas, tono energico y cercano. Numeros escritos con palabras (los lee una voz).
- Lo lee una voz: si algo es pregunta (aunque sea retorica) va con ¿?. Pocas comas, nunca antes del remate. Una idea por frase.
- HOOK HUMANO: la primera frase y el texto_pantalla nombran algo CONCRETO que el espectador tiene, conoce o espera (consola,
  fecha, precio, personaje, lugar). Prohibido abrir con "Descubre", "Increible", "Esto cambia todo", "Te sorprendera",
  "Nadie te lo cuenta", "Atencion" y similares. Si hay BANCO DE HOOKS, pasa cada hook por su checklist antes de responder.
- NUNCA dos cifras seguidas ("GTA seis dieciséis horas" se oye y se lee como un solo numero): separalas con palabras
  ("GTA seis antes que nadie: dieciséis horas...").
- TITULO: abre curiosidad y NO da la respuesta (el dato clave va en el video). Si el tema es una persona famosa, su NOMBRE
  va al principio del titulo y en la primera frase. La respuesta se entrega en los primeros 3 segundos del video.
- VERIFICA con busqueda web cada cifra, fecha y dato. Si no lo puedes confirmar: no lo uses, o dilo claramente como rumor.
- Usa "LO QUE SE VE" de la investigacion para saber que imagenes enganchan, y eligelas en "claves".
- Si hay "BIBLIOTECA DE VIRALES": aplica la FORMULA de la ficha que respalda cada idea (estructura, tipo de hook,
  elementos indispensables). Sus datos clave tambien se VERIFICAN antes de usarlos. No repitas el mismo tipo de hook
  en dos guiones del lote.
- CLARIDAD (relee todo antes de responder): cada frase se entiende escuchandola UNA vez, sin contexto previo.
  Usa SIEMPRE la misma palabra para la misma cosa (si dices "revisores", no cambies a "censores"); explica quien es quien
  ("los revisores de Corea del Sur", no solo "los censores"). El hook escrito usa las MISMAS palabras que la voz.
  Nada de etiquetas pegadas como ": rumor". Si algo no esta confirmado, dilo natural ("eso viene de una sola fuente, asi que aun no esta confirmado").
- "texto_pantalla" = el HOOK escrito arriba (se lee con el sonido apagado). Reglas:
  3 a 6 palabras, UNA idea, se entiende SOLO sin escuchar nada: nombra el tema concreto (mapa, precio, trailer, Lucia, policia...).
  Abre una duda o promete algo, pero NO cuenta la respuesta. Refuerza la misma promesa que la primera frase hablada.
  Tipos que funcionan: numero + tema ("5 DETALLES OCULTOS DEL TRAILER 2"), dato sorprendente ("EL MAPA ES 2 VECES GTA 5"),
  pregunta concreta ("¿CUANTO COSTARA GTA 6?"), contradiccion ("ROCKSTAR DESMINTIO ESTE RUMOR"), revelacion ("LO QUE NADIE VIO EN LUCIA").
  MAL: "TAN GRANDE QUE PIDIERON MAPAS" (no se entiende de que habla). BIEN: "GTA 6 TRAERA MAPA DE PAPEL".
  Nunca vacio, nunca clickbait que el video no cumple.
- "claves": 2 a 4 palabras EN INGLES, en minusculas, para elegir imagenes de la biblioteca. Usa SOLO palabras de esta lista
  (son los nombres de las tomas disponibles): __VOCAB__
Responde SOLO un array JSON:
[{"titulo": "...", "texto_pantalla": "HOOK de 3 a 6 palabras",
  "frases": ["...", "..."], "fuentes": ["https://..."], "claves": ["..."], "tema": "nombre del tema"}]"""


def vocabulario():
    cat = json.loads(Path("tomas/catalogo.json").read_text())
    palabras = Counter()
    for t in cat:
        nombre = Path(t.get("fuente") or t["archivo"]).stem
        for p in re.split(r"[^a-zA-Z]+", nombre.lower()):
            if len(p) >= 3 and p not in {"gtavi", "gta", "and", "the", "mp4", "jpg", "png", "screenshots"}:
                palabras[p] += 1
    return ", ".join(p for p, _ in palabras.most_common(80)) or "(sin nombres: deja claves vacio)"


def claude(prompt, entrada, web=False):
    try:                      # capa de aprendizaje: lecciones + historial de lo ya publicado van SIEMPRE primero
        import lecciones
        entrada = lecciones.bloque() + entrada
    except Exception as e:
        print("⚠️ No se pudieron cargar las lecciones:", e)
    cmd = ["claude", "-p", prompt] + (["--allowedTools", "WebSearch", "WebFetch"] if web else [])
    r = subprocess.run(cmd, input=entrada, capture_output=True, text=True)
    return extraer_json(r.stdout)


def mostrar_plan(plan):
    for k, t in enumerate(plan, 1):
        print(f"\n🔥 TEMA {k}: {t['tema']}   [{t.get('riesgo', '?')}]")
        print(f"   📊 {t.get('por_que', '')}")
        for i in t.get("ideas", []):
            print(f"   🎬 [{i.get('formato', '?')}] {i['titulo']}\n      🪝 {i.get('hook', '')}")


def plan_md(plan, base):
    lineas = [f"# Plan del lote {base}", ""]
    for k, t in enumerate(plan, 1):
        lineas += [f"## {k}. {t['tema']} ({t.get('riesgo', '')})", t.get("por_que", ""), ""]
        lineas += [f"- **{i['titulo']}**: {i.get('hook', '')} _{i.get('angulo', '')}_" for i in t.get("ideas", [])]
        lineas.append("")
    return "\n".join(lineas)


# ---------------- 5. produccion ----------------
def paso(cmd, canal):
    print(f"\n----- [{canal.upper()}] {' '.join(cmd[1:])} -----")
    subprocess.run(cmd, check=True, env=dict(os.environ, CANAL=canal))


def biblioteca_contexto(tema=None, dias=10, maximo=25):
    """Lo aprendido en la BIBLIOTECA DE VIRALES (biblioteca.py): formulas, hooks y datos clave con minuto."""
    import sqlite3
    bd = Path("datos/inteligencia.db")
    if not bd.exists():
        return ""
    tema = tema or cfg().get("tema_biblioteca", "gta6")
    try:
        c = sqlite3.connect(bd)
        filas = c.execute("SELECT tipo, categoria, titulo, canal, vistas, veces, ficha FROM analisis WHERE tema=? AND fecha>? AND categoria!='control' "
                          "ORDER BY (tipo='Short') DESC, COALESCE(veces,0) DESC LIMIT ?",
                          (tema, time.time() - dias * 86400, maximo)).fetchall()
    except Exception:
        return ""
    out = []
    for tipo, cat, tit, canal, vistas, veces, ficha in filas:
        try:
            f = json.loads(ficha or "{}")
        except Exception:
            continue
        cab = f"- [{tipo} · {cat}{f' · {veces}x lo normal' if veces else ''} · {vistas or 0:,} vistas] \"{tit}\" ({canal})"
        if tipo == "Short":
            h, fo = f.get("hook") or {}, f.get("formula") or {}
            out.append(cab + f"\n  hook: {h.get('tipo')} · \"{h.get('texto_escrito', '')}\" · {h.get('por_que_detiene', '')}"
                       f"\n  formula: {fo.get('nombre')} ({fo.get('estructura')}) · indispensable: {', '.join(fo.get('indispensable') or [])}"
                       f"\n  por que pego: " + " / ".join(x.get("razon", "") for x in f.get("hipotesis_viral") or [])
                       + f"\n  para nosotros: {(f.get('para_nosotros') or {}).get('como_aplicarlo', '')}")
        else:
            datos = " | ".join(f"[{d.get('minuto')}] {d.get('dato')} ({d.get('tipo')})" for d in (f.get("datos_clave") or [])[:8])
            ideas = " | ".join(f"{i.get('hook_escrito')}: {i.get('titulo')}" for i in (f.get("ideas_shorts") or [])[:4])
            out.append(cab + f"\n  datos clave: {datos}\n  ideas: {ideas}")
    formulas = Path("biblioteca") / f"formulas_{tema.replace(' ', '_')}.md"
    hooks = Path("biblioteca") / f"hooks_{tema.replace(' ', '_')}.md"
    cab = ("FORMULAS VIVAS (patrones.py, lo mas destilado de la biblioteca):\n" + formulas.read_text(encoding="utf-8")[:7000]
           + "\n\n") if formulas.exists() else ""
    if hooks.exists():   # banco de hooks humanos + reglas anti-IA (hooks.py): OBLIGATORIO respetarlas
        cab += "BANCO DE HOOKS Y REGLAS ANTI-IA (respetar SIEMPRE; las palabras delatoras estan prohibidas):\n" + hooks.read_text(encoding="utf-8")[:9000] + "\n\n"
    reglas = Path("datos/estrategia/reglas_vigentes.md")   # analisis.py: lo que funciona en los top x20+ y en nuestros videos
    if reglas.exists():
        cab += "REGLAS VIGENTES DEL CEREBRO (respetar; son lo aprendido de los mejores casos y de nuestras metricas):\n" + reglas.read_text(encoding="utf-8")[:6000] + "\n\n"
    for pf in ("gta", "en"):   # perfil estrategico de cada canal de GTA (ES y EN): audiencia, motivaciones, prohibidos, angulo
        f = Path("datos/perfiles") / f"{pf}.json"
        if f.exists():
            cab += f"PERFIL DEL CANAL {pf.upper()} (respetar: angulo distinto ES vs EN, temas prohibidos, duracion):\n" + f.read_text(encoding="utf-8")[:3500] + "\n\n"
    arsenal = Path("datos/estrategia/arsenal_guionista.md")   # arsenal.py: piezas probadas (con ids para medir como nos va)
    if arsenal.exists():
        cab += arsenal.read_text(encoding="utf-8")[:7000] + "\n\n"
    cab += "FICHAS RECIENTES:\n" if (cab or out) else ""
    return cab + "\n".join(out) if (cab or out) else ""


def main():
    args = sys.argv[1:]
    n_videos = int(args[args.index("--videos") + 1]) if "--videos" in args else 6
    modo = args[-1] if args and args[-1] in ("blur", "centro") else "centro"
    n_temas = math.ceil(n_videos / IDEAS_POR_TEMA)
    base = dt.datetime.now().strftime("L%Y%m%d%H%M")
    t0 = time.time()

    biblioteca()
    if "--sin-radar" not in args:
        radares()

    titulo("🔎 3/5  Embudo: leyendo lo que dicen los videos mas virales")
    cand = embudo()
    if not cand:
        print("⛔ No hay videos en los radares. Corre sin --sin-radar.")
        sys.exit(1)
    with ThreadPoolExecutor(4) as pool:
        cand = list(pool.map(leer, cand))
    for k, v in enumerate(cand, 1):
        print(f"   {k:>2}. [{v['mercado'].upper()}] {'📝' if v['texto'] else '⚪'} {v['titulo'][:65]}")
    print(f"   📝 = leido completo · ⚪ = sin subtitulos (uso titulo y descripcion)")

    carpeta = Path("lotes", base)
    carpeta.mkdir(parents=True, exist_ok=True)
    if "--sin-ver" not in args and N_VER > 0:
        import ver
        top = sorted([v for v in cand if not v.get("oficial")],
                     key=lambda v: v.get("velocidad") or v.get("vph", 0), reverse=True)[:N_VER]
        print(f"\n👀 Mirando y escuchando los {len(top)} mas virales (copia temporal 360p que se borra)...")
        vistos = ver.analizar(top, carpeta / "ver")
        for v in cand:
            if v["id"] in vistos:
                v["visual"] = ver.como_texto(vistos[v["id"]])
        print(f"   ✅ {len(vistos)} videos analizados · hojas de contacto en {carpeta}/ver/")
    investigacion = "\n".join(ficha(k, v) for k, v in enumerate(cand, 1))
    if Path("formatos/recetas.md").exists():   # lo que aprendio formatos.py
        investigacion += "\n\nFORMATOS QUE MEJOR RINDEN AHORA (RECETAS):\n" + Path("formatos/recetas.md").read_text(encoding="utf-8")[:6000]
    bib = biblioteca_contexto()
    if bib:
        print(f"📚 Biblioteca de virales: formulas vivas + {bib.count(chr(10) + '- [') + int(bib.startswith('- ['))} fichas entran al plan y a los guiones")
        investigacion += ("\n\nBIBLIOTECA DE VIRALES (analisis profundo, viral vs normal de su canal; los Shorts ensenan el FORMATO, "
                          "los largos aportan DATOS e IDEAS):\n" + bib[:14000])

    es, en = cfg().get("canal", "@ViceVersoGG"), "@TheViceVerseGG"
    try:
        en = json.loads(Path("canales/en.json").read_text()).get("canal", en)
    except Exception:
        pass
    print(f"\n🧠 Claude cruza los {len(cand)} videos y arma el plan ({n_temas} temas x {IDEAS_POR_TEMA} ideas)...")
    prompt = PROMPT_PLAN.replace("__ES__", es).replace("__EN__", en).replace("__T__", str(n_temas)).replace("__I__", str(IDEAS_POR_TEMA))
    try:
        plan = claude(prompt, investigacion)
    except ValueError:
        print("⛔ Claude no devolvio un plan valido. Vuelve a correr:  python lote.py --sin-radar")
        sys.exit(1)

    (carpeta / "investigacion.md").write_text(investigacion, encoding="utf-8")

    try:                      # filtro anti-repeticion: fuera las ideas que se parecen a algo ya publicado o programado
        import lecciones
        hist = lecciones.historial()
        for t in plan:
            quedan = []
            for i in t.get("ideas", []):
                r = lecciones.repetido(i.get("titulo", ""), hist)
                if r:
                    print(f"🔁 Descartada por repetida ({int(r[0]*100)}% parecida a [{r[1]} · {r[2]}] {r[3]}): {i.get('titulo')}")
                else:
                    quedan.append(i)
            t["ideas"] = quedan
        plan = [t for t in plan if t.get("ideas")]
    except Exception as e:
        print("⚠️ Filtro anti-repeticion no disponible:", e)

    titulo("📋 4/5  PLAN DEL LOTE")
    mostrar_plan(plan)
    if "--web" in args:          # aprobacion desde el Estudio
        (carpeta / "esperando.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
        print("\n⏸  ESPERANDO_APROBACION: revisa el plan en el Estudio y aprueba", flush=True)
        resp = carpeta / "respuesta.json"
        while not resp.exists():
            time.sleep(2)
        d = json.loads(resp.read_text())
        (carpeta / "esperando.json").unlink(missing_ok=True)
        if d.get("cancelar"):
            (carpeta / "plan.md").write_text(plan_md(plan, base) + "\n_Cancelado._", encoding="utf-8")
            print("Cancelado desde el Estudio.")
            return
        plan = [t for k, t in enumerate(plan, 1) if k not in set(d.get("sacar", []))]
        print(f"✅ Plan aprobado en el Estudio ({len(plan)} temas)")
    elif "--si" not in args:
        r = input("\n👉 Enter = aprobar todo · numeros de TEMAS a sacar (ej: 2,3) · n = cancelar: ").strip().lower()
        if r == "n":
            (carpeta / "plan.md").write_text(plan_md(plan, base) + "\n_Cancelado._", encoding="utf-8")
            print("Cancelado. La investigacion quedo en", carpeta)
            return
        sacar = {int(x) for x in re.findall(r"\d+", r)}
        plan = [t for k, t in enumerate(plan, 1) if k not in sacar]
    ideas = [i for t in plan for i in t.get("ideas", [])][:n_videos]
    if not ideas:
        print("No quedaron ideas en el plan.")
        return
    (carpeta / "plan.md").write_text(plan_md(plan, base), encoding="utf-8")
    (carpeta / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")

    titulo(f"✍️  5/5  Produccion: {len(ideas)} Shorts en ES + {len(ideas)} en EN")
    print("🧠 Claude escribe los guiones y verifica los datos en la web (5 a 10 min)...")
    try:
        import laboratorio
        exp_txt, exp_orden = laboratorio.instruccion_guionista("gta_es", len(ideas))
    except Exception as e:
        exp_txt, exp_orden = "", None
    entrada = (exp_txt + "PLAN APROBADO:\n" + json.dumps(plan, ensure_ascii=False, indent=1) +
               f"\n\nESCRIBE {len(ideas)} GUIONES (uno por idea, en orden).\n\nINVESTIGACION:\n" + investigacion)
    try:
        guiones = claude(PROMPT_GUIONES.replace("__ES__", es).replace("__VOCAB__", vocabulario()), entrada, web=True)
    except ValueError:
        print(f"⛔ Claude no devolvio guiones. El plan quedo en {carpeta}/plan.md")
        sys.exit(1)
    Path("guiones").mkdir(exist_ok=True)
    for k, g in enumerate(guiones[:len(ideas)], 1):
        g["lote"] = base
        if exp_orden:      # el codigo manda: variante A/B alternada del experimento activo
            g["exp_ab"] = {"id": exp_orden[0], "variante": dict(exp_orden[1]).get(k, "A")}
        Path("guiones", f"{base}_{k:02d}.json").write_text(json.dumps(g, ensure_ascii=False, indent=2))
        print(f"\n✍️  {k}. {g.get('titulo')}  🎯 {', '.join(g.get('claves') or [])}")
        for f in g.get("frases", []):
            print(f"   · {f}")

    # revision obligatoria: datos verificados, promesa cumplida, narrativa. El que no pasa queda fuera del lote.
    print("\n🔎 Revisión obligatoria de los guiones (datos, promesa, narrativa)...", flush=True)
    subprocess.run([PY, "revisar.py", base, "--corregir"])
    rech = Path("guiones/_rechazados")
    for a in sorted(Path("guiones").glob(f"{base}_[0-9][0-9].json")):
        if not (json.loads(a.read_text()).get("revision") or {}).get("aprobado"):
            rech.mkdir(exist_ok=True)
            a.rename(rech / a.name)
            print(f"   ⛔ {a.name} queda fuera del lote (ver guiones/_rechazados/ y su campo 'revision')", flush=True)
    if not list(Path("guiones").glob(f"{base}_[0-9][0-9].json")):
        print("⛔ Ningún guion pasó la revisión. El plan quedó guardado; corrige y vuelve a producir.")
        sys.exit(1)

    # ES y EN en paralelo: el ingles se adapta y se produce mientras se hace el espanol
    log_en = open(carpeta / "ingles.log", "w")
    print("\n🌎 Version en ingles en paralelo (detalle en lotes/%s/ingles.log)" % base, flush=True)
    en_proc = subprocess.Popen([PY, "traducir.py", base, "en", modo, "--sin-publicar"], stdout=log_en, stderr=subprocess.STDOUT)
    paso([PY, "voz.py", base], "es")
    paso([PY, "montar.py", base, modo], "es")
    paso([PY, "subtitular.py", f"clips/{base}_narrado_momentos.json"], "es")
    paso([PY, "publicar.py", base], "es")       # primero ES: el EN se intercala segun estos horarios
    print("\n⏳ Esperando la version en ingles...", flush=True)
    en_proc.wait()
    log_en.close()
    if en_proc.returncode != 0:
        print(f"⛔ Fallo la version en ingles: revisa lotes/{base}/ingles.log")
        sys.exit(1)
    paso([PY, "publicar.py", base + "en"], "en")

    ids = {cand[n - 1]["id"] for t in plan for n in t.get("videos", []) if isinstance(n, int) and 0 < n <= len(cand)}
    for c in CANALES:
        nuevos = ids - usados(c)
        if nuevos:
            with open(f"usados_{c}.txt", "a") as f:
                f.write("".join(i + "\n" for i in sorted(nuevos)))
    try:
        import panel
        panel.generar()
    except Exception:
        pass
    mins = (time.time() - t0) / 60
    titulo(f"🎉 Lote {base} listo en {mins:.0f} min")
    print(f"📁 Escritorio/YouTube/: {len(ideas)} Shorts en cada canal, con horario y textos")
    print(f"📋 Plan e investigacion: lotes/{base}/")
    print("🖥️  Panel: cd ~/Desktop/YouTube && python3 -m http.server 8000  →  http://localhost:8000/panel.html")


if __name__ == "__main__":
    main()
