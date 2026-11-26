"""
claves.py · Réplica exacta de cómo el motor (escena/escena.html) resuelve las claves de tiempo, y mapa de los
campos de los datos que pasan por esa resolución. Solo lee: no modifica nada.

Cómo resuelve el motor (función tk, línea ≈1421):
  · texto que existe en T          → T[clave]
  · texto "marcador±n"             → T[marcador] + parseFloat("±n")        (por ejemplo "s_3+0.25")
  · texto que no existe            → el INICIO DE LA ESCENA, en silencio   ← lo que este módulo vuelve visible
  · número                         → inicio de la escena + número          (relativo)
  · vacío (null, 0, falta)         → inicio de la escena
El inicio de cada escena (escenas[].desde) se resuelve aparte: "0" o T[desde], sin desplazamientos (secuencia()).
"""
import difflib, math, re

PATRON = re.compile(r"^(.+?)([+-][0-9.]+)$")           # el mismo patrón que usa el motor
DESPLAZ_OK = re.compile(r"^[+-](\d+(\.\d*)?|\.\d+)$")   # un número bien escrito después del signo
NUMERO = re.compile(r"^\s*[+-]?(\d+(\.\d*)?|\.\d+)\s*$")


def parse_float_js(s):
    """parseFloat de JavaScript para '±dígitos[.dígitos]': toma el prefijo numérico válido más largo."""
    m = re.match(r"^\s*([+-]?)(\d*)(\.?)(\d*)", s)
    sig, ent, punto, dec = m.groups()
    if not ent and not dec:
        return float("nan")
    return float(f"{sig}{ent or '0'}.{dec or '0'}")


def tk(k, a, T):
    """Réplica de tk(k, a) del motor. Devuelve el tiempo absoluto (o nan si el motor obtendría NaN)."""
    if isinstance(k, str):
        if k in T:
            return T[k]
        m = PATRON.match(k)
        if m and m.group(1) in T:
            return T[m.group(1)] + parse_float_js(m.group(2))
        return a
    if k is None or k is False or k == 0:
        return a
    if k is True:
        return a + 1
    if isinstance(k, (int, float)):
        return a + k
    return float("nan")                                   # lista u objeto: en JS da texto o NaN


def sugerir(base, T):
    """Marcadores parecidos: primero los que son el final o el comienzo del texto (p27_fin → fin), luego los parecidos."""
    afijo = [c for c in T if len(c) >= 3 and c != base and (base.endswith(c) or base.startswith(c))]
    afijo.sort(key=len, reverse=True)
    pare = [c for c in difflib.get_close_matches(base, list(T), n=2, cutoff=0.6) if c not in afijo]
    s = (afijo + pare)[:2]
    return (" ¿Quisiste decir " + " o ".join(f'"{c}"' for c in s) + "?") if s else ""


def clasificar(k, T):
    """Qué es la clave y si el motor la resuelve bien. → (tipo, nivel, motivo).
    nivel: None (bien) · 'info' · 'error'."""
    if k is None:
        return "vacía", None, ""
    if isinstance(k, bool):
        return "booleana", "error", f"valor booleano ({k}): el motor lo trata como {1 if k else 0} s"
    if isinstance(k, (int, float)):
        return "relativa", None, ""
    if isinstance(k, str):
        if k in T:
            return "marcador", None, ""
        if NUMERO.match(k):
            v = float(k)
            if v == 0:
                return "número como texto", "info", f'"{k}" está escrito como texto; el motor usa el inicio de la escena (igual a 0)'
            return "número como texto", "error", f'"{k}" está escrito como texto: el motor usa el inicio de la escena, no {v} s'
        m = PATRON.match(k)
        if m and m.group(1) in T:
            if DESPLAZ_OK.match(m.group(2)):
                return "marcador±n", None, ""
            return "desplazamiento mal escrito", "error", (f'"{m.group(2)}" no es un número válido: el motor suma '
                                                          f'{parse_float_js(m.group(2))} s')
        base = m.group(1) if m else k
        pista = sugerir(base, T)
        return "inexistente", "error", f'"{base}" no existe en T: el motor usa el inicio de la escena, en silencio.{pista}'
    return type(k).__name__, "error", f"tipo {type(k).__name__}: el motor no lo puede resolver como tiempo"


# ---------------------------------------------------------------------------------------------------------------
# Mapa de campos con claves de tiempo (sacado del código del motor 725e0dba; ver campos_motor.json).
# Ruta relativa a cada escena:  lista[]  = cada elemento · campo[0] = posición en una lista · fila[*][0] = 1.ª columna
# Rol: 'inicio' (algo empieza o aparece) · 'fin' (termina) · 'punto' (un instante, p. ej. una pose o un clic)
# Pares (inicio, fin) del mismo objeto: se avisa si el fin cae antes del inicio.
# ---------------------------------------------------------------------------------------------------------------
PELICULA = [
    ("zonas[].k", "inicio"), ("zonas[].o.k", "inicio"), ("zonas[].o.firma", "inicio"), ("zonas[].o.separa", "inicio"),
    ("zoom[].k", "punto"), ("pan[].k", "punto"), ("extras[].desde", "inicio"), ("extras[].hasta", "fin"),
    ("actores[].desde", "inicio"), ("actores[].hasta", "fin"), ("actores[].keys[].k", "punto"),
    ("props[].k", "inicio"), ("props[].fin", "fin"), ("props[].mov[].k", "punto"), ("props[].rots[].k", "punto"),
    ("props[].estados[].k", "punto"),
    ("titulos[].k", "inicio"), ("titulos[].fin", "fin"), ("chips[].k", "inicio"), ("chips[].fin", "fin"),
    ("burbujas[].k", "inicio"), ("burbujas[].fin", "fin"), ("numeros[].k", "inicio"), ("numeros[].fin", "fin"),
    ("prohibidos[].k", "punto"), ("vidrios[].k", "punto"), ("trizas[].k", "inicio"), ("trizas[].fin", "fin"),
    ("sacudidas[].k", "punto"), ("emojis[].k", "inicio"), ("kc", "inicio"),
    ("telefono.k", "inicio"), ("telefono.fin", "fin"), ("telefono.items[].k", "punto"),
    ("tablet.k", "inicio"), ("tablet.fin", "fin"), ("tablet.items[].k", "punto"), ("tablet.sello.k", "punto"),
    ("mando.k", "inicio"), ("mando.fin", "fin"), ("mando.items[].k", "punto"),
    ("barra.k", "inicio"), ("barra.fin", "fin"),
]
# Campos propios de algunos tipos de utilería (props[] con ese "tipo").
UTILERIA = {
    "mitad": [("de", "inicio"), ("a", "fin")],
    "bote": [("nk", "punto")],
    "p27_grilla": [("resalta", "punto"), ("cursor[0]", "inicio"), ("cursor[1]", "fin"), ("clics[*]", "punto"),
                   ("scroll[0]", "inicio"), ("scroll[1]", "fin")],
    "p27_manoPOV": [("grilla.cursor[0]", "inicio"), ("grilla.cursor[1]", "fin"), ("grilla.clics[*]", "punto"),
                    ("grilla.scroll[0]", "inicio"), ("grilla.scroll[1]", "fin")],
    "p27_mano": [("suelta[0]", "inicio"), ("suelta[1]", "fin")],
    "p27_negro": [("centro", "punto")],
    "p27_luz": [("dim[0]", "inicio"), ("dim[1]", "fin"), ("negro[0]", "inicio"), ("negro[1]", "fin")],
    "p27_pelusa": [("cae[0]", "inicio"), ("cae[1]", "fin")],
    "p27_ventana": [("abre", "inicio")],
    "p27_visor": [("abre", "inicio"), ("despl[0]", "inicio"), ("despl[1]", "fin"), ("curMov[*][0]", "punto"),
                  ("despK[*][0]", "punto")],
}
# Tipos de escena antiguos: leen T[campo] directo (sin "marcador±n" ni números).
DIRECTOS = ["k", "k1", "k2", "k3", "kr", "ke", "ks[*]"]
PARES = [("k", "fin"), ("desde", "hasta"), ("de", "a"), ("[0]", "[1]")]


def _pasos(ruta):
    return re.findall(r"[A-Za-z_][\w]*|\[\]|\[\*\]|\[\d+\]", ruta)


def recorrer(obj, ruta, prefijo=""):
    """Todas las (ruta_concreta, valor) que coinciden con una ruta del mapa. Los campos ausentes no se reportan."""
    pasos = _pasos(ruta)
    def ir(o, ps, r):
        if not ps:
            yield r, o; return
        p, resto = ps[0], ps[1:]
        if p in ("[]", "[*]"):
            if isinstance(o, list):
                for i, x in enumerate(o):
                    yield from ir(x, resto, f"{r}[{i}]")
        elif p.startswith("["):
            i = int(p[1:-1])
            if isinstance(o, list) and len(o) > i:
                yield from ir(o[i], resto, f"{r}[{i}]")
        elif isinstance(o, dict) and p in o:
            yield from ir(o[p], resto, f"{r}.{p}" if r else p)
    yield from ir(obj, pasos, prefijo)


def claves_de_escena(e):
    """(ruta, valor, rol, modo) de cada clave de tiempo de una escena. modo: 'tk' (resolución completa) o 'directo'."""
    out = []
    if e.get("tipo") == "pelicula":
        for ruta, rol in PELICULA:
            out += [(r, v, rol, "tk") for r, v in recorrer(e, ruta)]
        for i, pr in enumerate(e.get("props") or []):
            for ruta, rol in UTILERIA.get(pr.get("tipo"), []):
                out += [(r, v, rol, "tk") for r, v in recorrer(pr, ruta, f"props[{i}]")]
    elif e.get("tipo") != "cierre":
        for ruta in DIRECTOS:
            out += [(r, v, "punto", "directo") for r, v in recorrer(e, ruta)]
    return out


def es_numero(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and not (isinstance(v, float) and math.isnan(v))
