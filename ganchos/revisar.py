"""REVISION OBLIGATORIA DEL GUION: ningun guion pasa a voz/montaje sin aprobar este control.

Claude (con busqueda web) revisa cada frase y el guion completo:
  - DATOS: cada frase etiquetada como hecho | interpretacion | hipotesis | especulacion | desconocido, y cada HECHO verificado
           con fuente. Una hipotesis nunca puede sonar a hecho (debe ir como pregunta o 'segun X').
  - PROMESA: que promete el titulo/hook y en que frase se cumple (si no se cumple, no pasa).
  - NARRATIVA: hook, curiosidad, escalada, payoff, claridad, retencion (frases que sobran).
  - ORIGINALIDAD: que no sea una copia evidente de un video ajeno.  - VISUAL: que cada frase se pueda mostrar.
  - REGLAS: respeta las reglas vigentes y el perfil del canal.
El APROBADO lo decide el CODIGO (no el modelo), con umbrales fijos:
  datos >= 7 y promesa >= 7 · ningun hecho sin verificar · ningun problema grave sin corregir · riesgo de desinformacion != alto
Con --corregir: aplica las correcciones propuestas (frases puntuales) y revisa UNA vez mas.
Cada revision se guarda en el guion ("revision") y en datos/cerebro.db (tabla evaluaciones) con su PREDICCION
(probabilidad de superar la mediana del canal / de ser outlier) para calibrarla despues con el resultado real.

Uso:  python revisar.py G2026111901            (todos los guiones del lote)
      python revisar.py C2026112001 --corregir
      python revisar.py guiones/R2026112401_01.json
Sale con codigo 1 si algun guion queda RECHAZADO (armar_uno.sh y lote.py se detienen para ese guion).
"""
import re, sys, json, sqlite3, subprocess, datetime as dt
from pathlib import Path

from utilidades import extraer_json

CEREBRO = Path("datos/cerebro.db")
REGLAS = Path("datos/estrategia/reglas_vigentes.md")
UMBRAL = {"datos": 7, "promesa": 7}

PROMPT = """Eres el EDITOR JEFE y VERIFICADOR DE DATOS de una fabrica de YouTube Shorts. Tu trabajo es que nada falso, enganoso o
flojo salga publicado. Usa la busqueda web para verificar CADA dato concreto (fechas, cifras, nombres, citas, hechos).
Te paso el guion (JSON: titulo, texto_pantalla, frases, fuentes), el canal, su perfil y las reglas vigentes.
Devuelve SOLO un objeto JSON:
{"frases":[{"n":1,"tipo":"hecho|interpretacion|hipotesis|especulacion|desconocido","verificado":true|false|null,
            "fuente":"url que lo respalda o ''","problema":"'' o que esta mal"}],
 "promesa":"que promete el titulo + primera frase", "entrega":"en que frase se cumple (n) y como, o 'no se cumple'",
 "puntajes":{"datos":0-10,"promesa":0-10,"hook":0-10,"curiosidad":0-10,"escalada":0-10,"payoff":0-10,"claridad":0-10,
             "retencion":0-10,"originalidad":0-10,"visual":0-10,"reglas":0-10},
 "problemas":[{"tipo":"dato|promesa|narrativa|originalidad|visual|regla|tono","n":frase o 0,"detalle":"..","gravedad":"alta|media|baja"}],
 "riesgo_desinformacion":"bajo|medio|alto",
 "correcciones":[{"n":frase (o 0 para el titulo),"texto_nuevo":"frase corregida, mismo largo aprox., mismo idioma"}],
 "prediccion":{"p_supera_mediana":0.0-1.0,"p_outlier":0.0-1.0,"fortalezas":[".."],"debilidades":[".."]},
 "veredicto":"1-2 frases"}
Criterios:
- 'hecho' = afirmacion comprobable. Si no lo pudiste verificar, verificado=false y problema. Una hipotesis o especulacion
  escrita como hecho es problema de gravedad ALTA (debe ir como pregunta, 'segun X' o 'podria').
- Promesa: si el titulo o el hook prometen algo que el guion no entrega, gravedad ALTA.
- Narrativa: la revelacion principal no debe llegar demasiado pronto (comparala con la ANATOMIA TEMPORAL de los top si viene);
  cada frase debe sumar; debe haber al menos una pregunta abierta que se cierre al final; el final debe dejar una pregunta
  o cerrar un loop. Frases que sobran -> problema de retencion.
- Visual: cada frase debe poder mostrarse con imagenes legales (sin caras reales, sin logos, sin material ajeno).
- Correcciones: solo para las frases con problemas; conserva el estilo y la estructura del guion.
- Prediccion: honesta y calibrada (la mayoria de los videos NO supera la mediana); no es una promesa.
No inventes fuentes."""


def experimento_txt(g):
    ex = g.get("exp_ab") or {}
    if not ex.get("id"):
        return ""
    try:
        f = sqlite3.connect(CEREBRO).execute("SELECT variable, variante_a, variante_b FROM experimentos WHERE id=?", (ex["id"],)).fetchone()
    except Exception:
        f = None
    if not f:
        return ""
    v = f[1] if ex.get("variante") == "A" else f[2]
    return (f"EXPERIMENTO #{ex['id']}: este guion es la variante {ex.get('variante')} ({v}) de la variable '{f[0]}'. "
            "Comprueba que la aplique de verdad (si no, problema tipo 'regla', gravedad media) y que todo lo demas este igual de bien hecho.\n\n")


def revisar_uno(g, canal, perfil, reglas):
    entrada = experimento_txt(g) + (f"CANAL: {canal}\nPERFIL DEL CANAL: {json.dumps(perfil, ensure_ascii=False)[:4000]}\n\nREGLAS VIGENTES:\n{reglas[:6000]}\n\n"
               f"GUION:\n" + json.dumps({k: g.get(k) for k in ("titulo", "texto_pantalla", "frases", "fuentes", "tema")}, ensure_ascii=False, indent=1))
    r = subprocess.run(["claude", "-p", PROMPT, "--allowedTools", "WebSearch", "WebFetch"], input=entrada,
                       capture_output=True, text=True, timeout=1200)
    txt = r.stdout
    i = txt.find("{")
    dec = json.JSONDecoder()
    while i != -1:
        try:
            obj, _ = dec.raw_decode(txt, i)
            if isinstance(obj, dict) and "puntajes" in obj:
                return obj
        except json.JSONDecodeError:
            pass
        i = txt.find("{", i + 1)
    raise ValueError("Claude no devolvio una revision valida")


def decidir(rv):
    """El codigo decide, no el modelo."""
    motivos = []
    p = rv.get("puntajes") or {}
    for k, u in UMBRAL.items():
        if (p.get(k) or 0) < u:
            motivos.append(f"{k} {p.get(k)}/10 (< {u})")
    for f in rv.get("frases") or []:
        if f.get("tipo") == "hecho" and f.get("verificado") is False:
            motivos.append(f"frase {f.get('n')}: hecho sin verificar")
    for pr in rv.get("problemas") or []:
        if pr.get("gravedad") == "alta":
            motivos.append(f"grave ({pr.get('tipo')}, frase {pr.get('n')}): {pr.get('detalle', '')[:90]}")
    if rv.get("riesgo_desinformacion") == "alto":
        motivos.append("riesgo de desinformacion alto")
    return not motivos, motivos


def corregir(g, rv):
    frases = list(g.get("frases") or [])
    cambios = 0
    for c in rv.get("correcciones") or []:
        n, nuevo = c.get("n"), (c.get("texto_nuevo") or "").strip()
        if not nuevo or not isinstance(n, int):
            continue
        if n == 0:
            g.setdefault("titulo_original", g.get("titulo"))
            g["titulo"] = nuevo
            cambios += 1
        elif 1 <= n <= len(frases) and frases[n - 1] != nuevo:
            frases[n - 1] = nuevo
            cambios += 1
    if cambios:
        g.setdefault("frases_originales", g.get("frases"))
        g["frases"] = frases
        g.pop("frases_voz", None)          # la voz se vuelve a preparar con el texto corregido
    return cambios


def guardar_evaluacion(archivo, g, rv, aprobado, motivos, ronda):
    CEREBRO.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(CEREBRO)
    c.execute("""CREATE TABLE IF NOT EXISTS evaluaciones (guion TEXT, fecha TEXT, ronda INTEGER, canal TEXT, titulo TEXT, aprobado INTEGER,
                 puntajes TEXT, p_supera_mediana REAL, p_outlier REAL, riesgo TEXT, motivos TEXT, prompt TEXT,
                 video_id TEXT, vistas_24h INTEGER, resultado TEXT, PRIMARY KEY (guion, fecha, ronda))""")
    try:
        import procedencia as PR
        pv = PR.version_prompt(c, "revisar", PROMPT)
    except Exception:
        pv = ""
    pr = rv.get("prediccion") or {}
    c.execute("INSERT OR REPLACE INTO evaluaciones (guion, fecha, ronda, canal, titulo, aprobado, puntajes, p_supera_mediana, p_outlier, "
              "riesgo, motivos, prompt) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
              (archivo.stem, dt.datetime.now().isoformat(timespec="seconds"), ronda, g.get("canal"), g.get("titulo"), int(aprobado),
               json.dumps(rv.get("puntajes"), ensure_ascii=False), pr.get("p_supera_mediana"), pr.get("p_outlier"),
               rv.get("riesgo_desinformacion"), json.dumps(motivos, ensure_ascii=False), pv))
    c.commit()
    c.close()


def perfil_de(canal):
    pf = Path("datos/perfiles") / f"{canal}.json"          # perfil estrategico del canal (perfiles por canal, no mezclar)
    if pf.exists():
        try:
            return json.loads(pf.read_text())
        except Exception:
            pass
    p = Path("canales") / f"{canal}.json"
    try:
        d = json.loads(p.read_text()) if p.exists() else {}
    except Exception:
        d = {}
    return d.get("perfil") or {k: d.get(k) for k in ("nicho", "canal", "idioma") if d.get(k)}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    arreglar = "--corregir" in sys.argv
    if not args:
        sys.exit("Uso: python revisar.py <LOTE | guiones/archivo.json> [--corregir]")
    obj = args[0]
    archivos = [Path(obj)] if obj.endswith(".json") else sorted(Path("guiones").glob(f"{obj}_[0-9][0-9].json"))
    if not archivos:
        sys.exit(f"⚠️ No encontre guiones para {obj}")
    reglas = REGLAS.read_text(encoding="utf-8") if REGLAS.exists() else ""
    ana = Path("datos/estrategia/anatomia.md")
    if ana.exists():      # la narrativa se compara con como se mueven los top (revelacion %, preguntas, tension)
        reglas += "\n\n" + ana.read_text(encoding="utf-8")[:3000]
    rechazados = 0
    for a in archivos:
        g = json.loads(a.read_text())
        canal = g.get("canal") or ("en" if a.stem.endswith("en_01") else "gta")
        print(f"🔎 Revisando {a.name}: {g.get('titulo')}", flush=True)
        ok, motivos, rv = False, ["sin revision"], {}
        for ronda in (1, 2):
            try:
                rv = revisar_uno(g, canal, perfil_de(canal), reglas)
            except Exception as e:
                motivos = [f"no se pudo revisar: {e}"]
                break
            ok, motivos = decidir(rv)
            guardar_evaluacion(a, g, rv, ok, motivos, ronda)
            p = rv.get("puntajes") or {}
            print(f"   ronda {ronda}: {'✅ APROBADO' if ok else '❌ NO PASA'} · datos {p.get('datos')} · promesa {p.get('promesa')} · "
                  f"hook {p.get('hook')} · escalada {p.get('escalada')} · payoff {p.get('payoff')} · riesgo {rv.get('riesgo_desinformacion')}", flush=True)
            for m in motivos:
                print(f"     - {m}", flush=True)
            if ok or not arreglar or ronda == 2:
                break
            n = corregir(g, rv)
            print(f"   ✏️ {n} correcciones aplicadas; reviso de nuevo...", flush=True)
            if not n:
                break
        g["revision"] = {"fecha": dt.datetime.now().isoformat(timespec="minutes"), "aprobado": ok, "motivos": motivos,
                         "puntajes": rv.get("puntajes"), "frases": rv.get("frases"), "promesa": rv.get("promesa"),
                         "entrega": rv.get("entrega"), "prediccion": rv.get("prediccion"), "veredicto": rv.get("veredicto"),
                         "riesgo": rv.get("riesgo_desinformacion")}
        a.write_text(json.dumps(g, ensure_ascii=False, indent=2))
        if not ok:
            rechazados += 1
            print(f"   ⛔ {a.name} NO pasa la revision. Corrige el guion (o pide a Claude que lo haga) y vuelve a correr revisar.py.", flush=True)
        else:
            print(f"   🗒️ {rv.get('veredicto', '')}", flush=True)
    print(f"\n{'✅ Todos aprobados' if not rechazados else f'⛔ {rechazados} de {len(archivos)} no pasan'}", flush=True)
    sys.exit(1 if rechazados else 0)


if __name__ == "__main__":
    main()
