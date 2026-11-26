"""BANCO DE HOOKS HUMANOS + reglas anti-"IA".

Estudia los hooks REALES de los Shorts virales de la biblioteca (lo que dicen en los primeros 3 s, lo que escriben en pantalla,
como suenan) y los de nuestros propios videos con su rendimiento (metricas.db), y destila:
  1) un banco de hooks por tipo, con ejemplos textuales reales (sin copiarlos: se usan como referencia de tono)
  2) reglas de redaccion: que hace que un hook suene humano y que lo delata como "IA"
  3) una lista de palabras/estructuras prohibidas y sus reemplazos
Salida: biblioteca/hooks_<tema>.md  (lote.py y traducir.py lo inyectan al guionista)

Uso:  python hooks.py --tema gta6     ·     python hooks.py --tema rabbit
"""
import sys, json, sqlite3, subprocess, time
from pathlib import Path

BD = Path("datos/inteligencia.db")
MET = Path("datos/metricas.db")

PROMPT = """Eres un guionista senior de Shorts virales y un linguista obsesionado con que los textos suenen HUMANOS.
Te paso (A) hooks reales de Shorts virales analizados (texto hablado en los primeros segundos, texto en pantalla, tipo,
por que detiene, rendimiento) y (B) nuestros propios hooks con sus vistas. Tema: __TEMA__. Idiomas: espanol y ingles.

Escribe un documento en espanol, en markdown, con estas secciones (concreto, con ejemplos; nada de generalidades):
## 1. Como abren los virales (lo observado)
- Patrones reales de los primeros 3 segundos: a quien le hablan (tu / nosotros / nadie), tiempo verbal, longitud en palabras,
  si nombran algo concreto que el espectador tiene o conoce, si hay numero, si hay contraste, como suena la voz.
- Que tienen en comun los de MEJOR rendimiento frente a los demas. Cita 6-10 hooks reales entre comillas como referencia.
## 2. Banco de hooks por tipo
Para cada tipo (amenaza personal, pregunta concreta, contraste/contradiccion, numero+tema, revelacion, promesa, polemica,
"nadie se dio cuenta", instruccion, historia en curso): 1 linea de cuando usarlo + 3 ejemplos NUEVOS en espanol y 3 en ingles
sobre __TEMA__, con el tono de los reales (cortos, directos, con cosas concretas). Marca con ★ los 2 tipos mas potentes segun los datos.
## 3. Reglas para que NO suene a IA
- Lista de 10-15 reglas practicas (ej: "nunca abrir con 'Descubre'", "nada de adjetivos vacios", "una idea por frase",
  "nombrar la cosa concreta antes que el adjetivo", "la pregunta retorica solo si el espectador puede responderla en su cabeza").
- Tabla: PALABRA/ESTRUCTURA DELATORA -> por que suena IA -> reemplazo humano (minimo 15 filas, espanol e ingles).
## 4. Checklist de 6 puntos para aprobar un hook
## 5. Lo que mas nos falta a nosotros (comparando B con A), en 5 lineas accionables.
Responde SOLO el markdown."""


def hooks_virales(c, tema):
    out = []
    q = "SELECT titulo, canal, vistas, veces, ficha, medidas FROM analisis WHERE tipo='Short' AND categoria!='control'"
    filas = c.execute(q + " AND tema=? ORDER BY COALESCE(veces,0) DESC", (tema,)).fetchall()
    if len(filas) < 8:                                   # pocos del tema: se completa con todos los Shorts
        filas += c.execute(q + " AND tema!=? ORDER BY COALESCE(veces,0) DESC LIMIT 40", (tema,)).fetchall()
    for tit, canal, vistas, veces, ficha, medidas in filas:
        try:
            f, m = json.loads(ficha or "{}"), json.loads(medidas or "{}")
        except Exception:
            continue
        h = f.get("hook") or {}
        hablado = h.get("texto_hablado") or h.get("primera_frase") or ""
        if not hablado:
            tr = f.get("transcripcion_inicio") or ""
            hablado = tr[:160]
        out.append(f"- \"{tit}\" ({canal}) · {vistas or 0:,} vistas · {veces or '?'}x lo normal del canal\n"
                   f"  hablado: «{hablado}»\n  en pantalla: «{h.get('texto_escrito', '')}»\n  tipo: {h.get('tipo')} · "
                   f"primera palabra a los {m.get('primera_palabra_s')} s · {m.get('palabras_por_s')} palabras/s\n"
                   f"  por que detiene: {h.get('por_que_detiene', '')}")
    return "\n".join(out)


def hooks_propios():
    """Nuestros hooks (texto_pantalla + primera frase de cada guion) con sus vistas, si hay metricas."""
    vistas = {}
    if MET.exists():
        try:
            m = sqlite3.connect(MET)
            for vid, titulo, v in m.execute("SELECT v.id, v.titulo, (SELECT vistas FROM fotos WHERE id=v.id ORDER BY ts DESC LIMIT 1) FROM videos v"):
                vistas[titulo.lower()[:40]] = v
        except Exception:
            pass
    out = []
    for g in sorted(Path("guiones").glob("*.json"))[-60:]:
        try:
            d = json.loads(g.read_text())
        except Exception:
            continue
        if not d.get("frases"):
            continue
        t = (d.get("titulo") or "").lower()[:40]
        v = next((x for k, x in vistas.items() if k and (k in t or t in k)), None)
        out.append(f"- «{d.get('texto_pantalla', '')}» / hablado: «{d['frases'][0]}»" + (f" · {v:,} vistas" if v else ""))
    return "\n".join(out[-40:])


def main():
    args = sys.argv[1:]
    tema = args[args.index("--tema") + 1] if "--tema" in args else "gta6"
    if not BD.exists():
        print("⚠️ No hay biblioteca todavia (corre biblioteca.py)")
        return
    c = sqlite3.connect(BD)
    a = hooks_virales(c, tema)
    if not a.strip():
        print("⚠️ Todavia no hay Shorts analizados: corre  python biblioteca.py --tema", tema, "--recolectar --n 30")
        return
    entrada = f"(A) HOOKS DE VIRALES:\n{a}\n\n(B) NUESTROS HOOKS:\n{hooks_propios()}"
    print(f"🧠 Destilando banco de hooks de {a.count(chr(10) + '- ') + 1} virales...")
    r = subprocess.run(["claude", "-p", PROMPT.replace("__TEMA__", tema)], input=entrada, capture_output=True, text=True, timeout=900)
    md = (r.stdout or "").strip()
    if len(md) < 400:
        print("⚠️ Claude no devolvio el documento:", md[:200])
        return
    salida = Path("biblioteca") / f"hooks_{tema}.md"
    salida.write_text(f"# Banco de hooks · {tema} · {time.strftime('%Y-%m-%d %H:%M')}\n\n" + md, encoding="utf-8")
    print(f"✅ {salida}")


if __name__ == "__main__":
    main()
