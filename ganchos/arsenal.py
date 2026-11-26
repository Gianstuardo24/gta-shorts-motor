"""ARSENAL: banco ACUMULATIVO de lo que funciona. Nada se borra: cada pieza suma evidencia corrida tras corrida.

Areas (separadas para no mezclar conocimiento):
  hook · titulo · pantalla (texto en pantalla) · estructura · cierre · formato · ritmo_audio · visual · psicologia
  'psicologia' guarda MECANISMOS (que se activa en la cabeza, en que condicion funciona y cuando falla), con evidencia.
Cada pieza: plantilla con [huecos], como usarla, por que funciona, condicion de verdad, ejemplos reales (xN), origen
(externo / propio / experto), evidencia (n casos, ratio medio) y RESULTADO NUESTRO (✅ / ❌ cuando la usamos).

Lo alimenta analisis.py (Radar completo) al final de cada corrida. Tambien a mano:  python arsenal.py
Salidas: tabla `arsenal` en datos/cerebro.db · datos/estrategia/7-arsenal.md (Estudio › 📡 Radar › 🗃️ Arsenal)
         datos/estrategia/arsenal_guionista.md (lo inyecta lote.py: el guionista usa las piezas y anota sus ids).
"""
import re, json, time, sqlite3, statistics, datetime as dt
from pathlib import Path

import ganchos as G
import procedencia as PR

CEREBRO = Path("datos/cerebro.db")
VISTA = Path("datos/estrategia/7-arsenal.md")
GUIONISTA = Path("datos/estrategia/arsenal_guionista.md")
AREAS = {"hook": "🎣 Hooks", "titulo": "🏷️ Títulos", "pantalla": "🖥️ Texto en pantalla", "estructura": "🧱 Estructuras",
         "cierre": "🔚 Cierres", "formato": "🎞️ Formatos", "ritmo_audio": "🥁 Ritmo y audio", "visual": "🎨 Visual",
         "psicologia": "🧠 Psicología (mecanismos)"}
TEMAS = ["general", "gta", "aliens", "negocios", "suerte", "cafe"]


def abrir():
    CEREBRO.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS arsenal (id INTEGER PRIMARY KEY AUTOINCREMENT, area TEXT, tema TEXT, idioma TEXT,
        nombre TEXT, pieza TEXT, como_usar TEXT, por_que TEXT, condicion TEXT, palanca TEXT, origen TEXT, ejemplos TEXT,
        evidencia INTEGER DEFAULT 1, ratio_medio REAL, usos INTEGER DEFAULT 0, nos_funciono INTEGER DEFAULT 0,
        no_funciono INTEGER DEFAULT 0, estado TEXT DEFAULT 'activa', alta TEXT, actualizado TEXT)""")
    cols = {r[1] for r in c.execute("PRAGMA table_info(arsenal)")}
    for col in ("en_contra", "relaciones", "temas_ok", "ultima_validacion", "motivo_archivo"):
        if col not in cols:
            c.execute(f"ALTER TABLE arsenal ADD COLUMN {col} TEXT")
    PR.migrar(c)
    return c


PROMPT = """Eres el bibliotecario del ARSENAL de una fabrica de YouTube Shorts: un banco ACUMULATIVO de piezas que funcionan,
separado por areas (no mezclar): hook, titulo, pantalla, estructura, cierre, formato, ritmo_audio, visual, psicologia.
- 'psicologia' = MECANISMOS: que se activa en la cabeza del espectador (curiosidad por hueco concreto, aversion a perder algo PROPIO,
  FOMO 'otros ya lo tienen', escasez NUEVA y real, identidad/autoevaluacion, seleccion personal, prueba social...), en que condicion
  funciona y cuando falla, segun la evidencia.
- Temas: general, gta, aliens, negocios, suerte, cafe. Idioma: es, en o ambos.
- Fichas marcadas [transversal] son de OTRO nicho (ej. una receta viral): ensenan MECANISMOS generales (gancho, ritmo, psicologia,
  estructura) → pieza con tema "general" y origen "transversal". NUNCA crees ni refuerces una pieza de un tema de canal (gta, aliens,
  cafe, suerte, negocios) con material transversal: ensena el mecanismo, pero NO prueba que funcione en ese nicho.
Te paso (1) el ARSENAL ACTUAL (id | area | tema | nombre | pieza) y (2) MATERIAL NUEVO: fichas de virales top (xN lo normal de su
canal), nuestros videos con metricas, y consejos de expertos.
Devuelve SOLO un array JSON de operaciones:
 {"op":"nueva","area":..,"tema":..,"idioma":..,"nombre":"2-5 palabras","pieza":"plantilla con [huecos] o descripcion concreta",
  "como_usar":"1 frase","por_que":"mecanismo psicologico en 1 frase","condicion":"cuando funciona / cuando falla / que debe ser verdad",
  "palanca":"curiosidad|perdida|primeros|ventana|identidad|seleccion|prueba_social|ninguna","origen":"externo|propio|experto|transversal",
  "ejemplos":[{"titulo":..,"id":..,"ratio":N}]}
 {"op":"refuerzo","id":N,"ejemplos":[{"titulo":..,"id":..,"ratio":N}]}      -> la pieza ya existe: suma evidencia
 {"op":"matiz","id":N,"condicion":"condicion corregida con lo nuevo"}         -> los datos precisan cuando funciona
 {"op":"contradice","id":N,"motivo":"..","ejemplos":[{"titulo":..,"id":..,"ratio":N}]} -> evidencia en contra (no se borra, se anota)
 {"op":"relacion","id":N,"tipo":"funciona_con|falla_con|relacionada","con":[ids]}   -> conecta piezas entre si
 {"op":"archivar","id":N,"motivo":".."}   -> SOLO si la evidencia en contra ya supera claramente a la de a favor (queda archivada, no se borra)
Reglas: NO dupliques (si se parece a una existente, usa refuerzo). Concreto y reutilizable, nada generico. Solo lo que el material
respalda; no inventes ejemplos ni cifras. Nunca piezas de urgencia falsa, promesas, 'comparte o mala suerte' ni material ajeno.
GTA: el juego ya salio; piezas sobre lo que REALMENTE hay en el juego.
En 'por_que' y 'condicion' aplica:
PROFUNDIDAD Y PERSPECTIVA (obligatorio en cada afirmacion importante):
- Evidencia: cuantos casos y que tan fuertes (xN, vistas); separa lo observado de lo que interpretas.
- Contraste: compara los TOP con videos NORMALES del mismo canal o tema (si lo normal tambien lo hace, NO es lo que hizo la diferencia).
- Hipotesis alternativas: tema caliente, momento, canal grande, algoritmo, suerte. Di cual explica mejor y por que.
- Mecanismo: que pasa en la cabeza del espectador, segundo a segundo, y por que lo hace quedarse o compartir.
- Condicion y limite: cuando funciona, cuando falla, que lo refutaria.
- Confianza: alta / media / baja segun n y consistencia. Nada de generalidades ni frases de manual."""


def compacto(c):
    out = []
    for i, a, t, n, p, ev, ec in c.execute("SELECT id, area, tema, nombre, pieza, evidencia, en_contra FROM arsenal WHERE estado='activa' ORDER BY id"):
        contra = len(json.loads(ec or "[]"))
        out.append(f"{i} | {a} | {t} | {n} | {p[:140]} | a favor {ev}{f' · en contra {contra}' if contra else ''}")
    return "\n".join(out)


def _fila(c, i):
    f = c.execute("SELECT * FROM arsenal WHERE id=?", (i,)).fetchone()
    if not f:
        return None
    cols = [d[0] for d in c.execute("SELECT * FROM arsenal LIMIT 0").description]
    return dict(zip(cols, f))


def aplicar(c, ops, corrida="manual", prompt_v=""):
    ahora = dt.datetime.now().isoformat(timespec="minutes")
    n = {"nueva": 0, "refuerzo": 0, "matiz": 0, "contradice": 0, "relacion": 0, "archivar": 0}
    ids_de = lambda ej: [e.get("id") for e in ej if e.get("id")]
    for o in ops if isinstance(ops, list) else []:
        if not isinstance(o, dict):
            continue
        op = o.get("op")
        ej = [e for e in (o.get("ejemplos") or []) if isinstance(e, dict)]
        rat = [float(e["ratio"]) for e in ej if isinstance(e.get("ratio"), (int, float))]
        if op == "nueva" and o.get("area") in AREAS and o.get("pieza"):
            tema = o.get("tema") if o.get("tema") in TEMAS else "general"
            if o.get("origen") == "transversal":      # de otro nicho: solo conocimiento general, nunca regla de un canal
                tema = "general"
                if "otro nicho" not in (o.get("condicion") or ""):
                    o["condicion"] = ((o.get("condicion") or "") + " · 🌐 de otro nicho: probar en nuestro canal antes de confiar").strip(" ·")
            cur = c.execute("""INSERT INTO arsenal (area, tema, idioma, nombre, pieza, como_usar, por_que, condicion, palanca, origen,
                      ejemplos, evidencia, ratio_medio, alta, actualizado, en_contra, relaciones, temas_ok, ultima_validacion)
                      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                      (o["area"], tema, o.get("idioma") or "ambos", o.get("nombre"), o["pieza"], o.get("como_usar"), o.get("por_que"),
                       o.get("condicion"), o.get("palanca"), o.get("origen") or "externo", json.dumps(ej, ensure_ascii=False),
                       max(len(ej), 1), round(statistics.mean(rat), 1) if rat else None, ahora, ahora, "[]", "{}",
                       json.dumps([tema]), ahora))
            PR.registrar(c, corrida, "arsenal", cur.lastrowid, "nueva", None, _fila(c, cur.lastrowid), o.get("por_que", ""), ids_de(ej), prompt_v)
            n["nueva"] += 1
            continue
        if not isinstance(o.get("id"), int) or op not in n:
            continue
        antes = _fila(c, o["id"])
        if not antes:
            continue
        if op == "refuerzo":
            viejos = json.loads(antes["ejemplos"] or "[]")
            ya = {e.get("id") for e in viejos}
            nuevos = [e for e in ej if e.get("id") not in ya]
            if not nuevos:
                continue
            todos = viejos + nuevos
            r_all = [float(e["ratio"]) for e in todos if isinstance(e.get("ratio"), (int, float))]
            c.execute("UPDATE arsenal SET ejemplos=?, evidencia=evidencia+?, ratio_medio=?, actualizado=?, ultima_validacion=? WHERE id=?",
                      (json.dumps(todos[-15:], ensure_ascii=False), len(nuevos), round(statistics.mean(r_all), 1) if r_all else None,
                       ahora, ahora, o["id"]))
            motivo, fuentes = f"+{len(nuevos)} casos", ids_de(nuevos)
        elif op == "matiz" and o.get("condicion"):
            c.execute("UPDATE arsenal SET condicion=?, actualizado=? WHERE id=?", (o["condicion"], ahora, o["id"]))
            motivo, fuentes = o.get("motivo", "condicion precisada"), ids_de(ej)
        elif op == "contradice":
            contra = json.loads(antes.get("en_contra") or "[]") + [dict(e, motivo=o.get("motivo", "")) for e in ej] \
                     + ([] if ej else [{"motivo": o.get("motivo", ""), "fecha": ahora}])
            c.execute("UPDATE arsenal SET en_contra=?, actualizado=? WHERE id=?", (json.dumps(contra[-20:], ensure_ascii=False), ahora, o["id"]))
            motivo, fuentes = o.get("motivo", ""), ids_de(ej)
        elif op == "relacion" and o.get("tipo") in ("funciona_con", "falla_con", "relacionada"):
            rel = json.loads(antes.get("relaciones") or "{}")
            rel[o["tipo"]] = sorted(set(rel.get(o["tipo"], [])) | {x for x in o.get("con") or [] if isinstance(x, int)})
            c.execute("UPDATE arsenal SET relaciones=?, actualizado=? WHERE id=?", (json.dumps(rel), ahora, o["id"]))
            motivo, fuentes = o["tipo"], []
        elif op == "archivar":
            c.execute("UPDATE arsenal SET estado='obsoleta', motivo_archivo=?, actualizado=? WHERE id=?", (o.get("motivo", ""), ahora, o["id"]))
            motivo, fuentes = o.get("motivo", ""), []
        else:
            continue
        PR.registrar(c, corrida, "arsenal", o["id"], op, antes, _fila(c, o["id"]), motivo, fuentes, prompt_v)
        n[op] += 1
    c.commit()
    return n


def resultados_nuestros(c):
    """Guiones que anotaron 'arsenal': [ids] -> a las 24 h se mira si rindio sobre la mediana de su canal."""
    try:
        m = sqlite3.connect(G.DB)
        pro = G.propios()
    except Exception:
        return
    por_canal = {}
    for p in pro:
        if p.get("vistas_24h") is not None:
            por_canal.setdefault(p["canal"], []).append(p["vistas_24h"])
    med = {k: statistics.median(v) for k, v in por_canal.items() if v}
    titulos = {p["titulo"]: p for p in pro}
    c.execute("CREATE TABLE IF NOT EXISTS arsenal_usos (guion TEXT, pieza INTEGER, video TEXT, resultado TEXT, PRIMARY KEY (guion, pieza))")
    for g in Path("guiones").glob("*.json"):
        try:
            d = json.loads(g.read_text())
        except Exception:
            continue
        ids = [i for i in d.get("arsenal") or [] if isinstance(i, int)]
        p = titulos.get(d.get("titulo", ""))
        if not ids or not p or p.get("vistas_24h") is None or p["canal"] not in med:
            continue
        rel = p["vistas_24h"] / max(med[p["canal"]], 1)
        res = "si" if rel >= 1.5 else "no" if rel <= 0.5 else "neutro"
        for i in ids:
            if c.execute("SELECT 1 FROM arsenal_usos WHERE guion=? AND pieza=?", (g.stem, i)).fetchone():
                continue
            c.execute("INSERT INTO arsenal_usos VALUES (?,?,?,?)", (g.stem, i, p["id"], res))
            c.execute("UPDATE arsenal SET usos=usos+1, nos_funciono=nos_funciono+?, no_funciono=no_funciono+? WHERE id=?",
                      (res == "si", res == "no", i))
            PR.registrar(c, "uso", "arsenal", i, "uso", None, {"guion": g.stem, "video": p["id"], "resultado": res},
                         f"{p['vistas_24h']} vistas 24h vs mediana {int(med[p['canal']])}", [p["id"]])
    c.commit()


def alimentar(material, corrida=None):
    """material: texto con fichas top, nuestros videos y expertos. Devuelve el conteo de operaciones."""
    corrida = corrida or dt.datetime.now().isoformat(timespec="minutes")
    c = abrir()
    pv = PR.version_prompt(c, "arsenal", PROMPT)
    resultados_nuestros(c)
    if not material.strip():
        exportar(c, corrida)
        return {}
    try:
        ops = G.extraer_json(G.claude(PROMPT, f"## (1) ARSENAL ACTUAL\n{compacto(c) or '(vacio)'}\n\n## (2) MATERIAL NUEVO\n{material[:150000]}",
                                      timeout=1800))
    except Exception as e:
        print(f"   ⚠️ arsenal: {e}", flush=True)
        ops = []
    n = aplicar(c, ops, corrida, pv)
    exportar(c, corrida)
    print(f"   🗃️ Arsenal: +{n.get('nueva', 0)} nuevas · {n.get('refuerzo', 0)} reforzadas · {n.get('matiz', 0)} matizadas · "
          f"{n.get('contradice', 0)} con evidencia en contra · {n.get('relacion', 0)} relaciones · {n.get('archivar', 0)} archivadas · activas {c.execute("SELECT COUNT(*) FROM arsenal WHERE estado='activa'").fetchone()[0]}", flush=True)
    return n


def puntaje(evid, ratio, si, no):
    return evid * (1 + min((ratio or 0) / 50, 3)) + 3 * si - 3 * no


def exportar(c, corrida=None):
    filas = c.execute("""SELECT id, area, tema, idioma, nombre, pieza, como_usar, por_que, condicion, palanca, origen, ejemplos,
                         evidencia, ratio_medio, usos, nos_funciono, no_funciono FROM arsenal WHERE estado='activa'""").fetchall()
    filas = sorted(filas, key=lambda f: -puntaje(f[12], f[13], f[15], f[16]))
    tot = len(filas)
    L = [f"# 🗃️ Arsenal — {dt.datetime.now():%d/%m %H:%M}", "",
         f"_{tot} piezas activas · crece con cada corrida del 📡 Radar completo · ✅/❌ = cómo nos fue cuando la usamos · "
         f"historial de cualquier pieza: `python procedencia.py arsenal <#>`_", ""]
    if corrida:
        L.append(PR.cambios_md(c, corrida, "arsenal"))
    for area, nombre in AREAS.items():
        de = [f for f in filas if f[1] == area]
        if not de:
            continue
        L += [f"## {nombre} ({len(de)})", "", "| # | Tema | Pieza | Por qué funciona | Condición | A favor | En contra | Relaciones | Nosotros |",
              "|---|---|---|---|---|---|---|---|---|"]
        for f in de[:40]:
            ej = json.loads(f[11] or "[]")
            ejs = "; ".join(f"[{(e.get('titulo') or '')[:40]}](https://youtube.com/shorts/{e.get('id')}) x{e.get('ratio')}"
                            for e in ej[:2] if e.get("id"))
            nos = (f"✅{f[15]} " if f[15] else "") + (f"❌{f[16]}" if f[16] else "") or ("usada" if f[14] else "—")
            celda = lambda s: (s or "").replace("|", "/").replace("\n", " ")
            try:
                comp = c.execute("SELECT comprobada FROM arsenal WHERE id=?", (f[0],)).fetchone()[0]
            except sqlite3.OperationalError:
                comp = None
            extra = c.execute("SELECT en_contra, relaciones FROM arsenal WHERE id=?", (f[0],)).fetchone()
            contra = len(json.loads(extra[0] or "[]"))
            rel = json.loads(extra[1] or "{}")
            rels = " ".join(f"{ {'funciona_con': '✚', 'falla_con': '✖', 'relacionada': '↔'}[k]}{','.join(map(str, v))}" for k, v in rel.items() if v)
            L.append(f"| {f[0]} | {f[2]}/{f[3]} | **{celda(f[4])}**: {celda(f[5])} | {celda(f[7])} | {celda(f[8])} | "
                     f"{f[12]} casos{f' · x{f[13]}' if f[13] else ''}{' · ' + ejs if ejs else ''} | {contra or '—'} | {rels or '—'} | "
                     f"{nos}{' · 🧪✅ comprobada' if comp == 'si' else ' · 🧪❌ refutada' if comp == 'no' else ''} |")
        L.append("")
    arch = c.execute("SELECT id, area, tema, nombre, motivo_archivo, actualizado FROM arsenal WHERE estado='obsoleta' ORDER BY actualizado DESC").fetchall()
    if arch:
        L += [f"## 🗄️ Archivadas ({len(arch)}) — no se usan, se guardan con su historial", ""]
        L += [f"- #{i} [{a}/{t}] {n} — _{m}_ ({u[:10]})" for i, a, t, n, m, u in arch[:50]]
    VISTA.parent.mkdir(parents=True, exist_ok=True)
    VISTA.write_text("\n".join(L), encoding="utf-8")
    G_ = ["ARSENAL (piezas probadas; usa las que calcen y ANOTA sus ids en el campo \"arsenal\": [ids] del guion).",
          "Respeta la condicion de cada pieza. Prioriza las que tienen ✅ con nosotros; evita las que tienen ❌.", ""]
    for area in AREAS:
        de = [f for f in filas if f[1] == area][:12]
        if de:
            G_.append(f"[{area}]")
            G_ += [f"- id {f[0]} ({f[2]}/{f[3]}, {f[12]} casos{f', x' + str(f[13]) if f[13] else ''}"
                   f"{', nos ✅' + str(f[15]) if f[15] else ''}{', nos ❌' + str(f[16]) if f[16] else ''}): {f[4]} — {f[5]} · "
                   f"condicion: {f[8]}" for f in de]
    GUIONISTA.write_text("\n".join(G_), encoding="utf-8")


if __name__ == "__main__":
    import analisis as A
    m = A.material_arsenal(0)
    alimentar(m)
