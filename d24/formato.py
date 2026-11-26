"""Constructor del formato de Short cerrado con Tao (25-nov). Plantilla de referencia: d24/c17n/b.py.
video(...) arma el _src.json a partir de escenas de alto nivel:
  {"z": set, "o": {...}, "actores": [...], "props": [...], "titulo": ("TEXTO","color", fin)}   -> escena con escenario
  {"i": [fondo3], "luz2": "r,g,b", "pedestal": bool, "props": [...]}                              -> inserto (objeto en primer plano)
Cada escena lleva "k" = marcador donde empieza (por defecto la frase que le toca)."""
import sys, json
sys.path.insert(0, '/home/claude/d24')
from comun import *
from comun import _INS

def video(path, ID, marca, titulo, texto_pantalla, frases, voz=None, escenas=(), marcas=(), numeros=(), emojis=(),
          gancho2=None, prohibidos=(), sacudidas=(), nota="", fuentes=(), cierre="DID YOU KNOW?", cierre2="Yes or no? Comment",
          paises=("YES", "NO"), cta="FOLLOW FOR MORE", like="LIKE", hints=(), burbujas=(), escala=1.24, extra=None):
    n = len(frases)
    nom = lambda i: "s_fin" if i == n - 2 else ("s_cta" if i == n - 1 else f"s_{i}")
    M = [[nom(i), i, None] for i in range(1, n)] + [list(m) for m in marcas]
    zonas, pan, props, actores, titulos, ins = [], [], [], [], [], []
    zx = []                                     # (k, x camara) de cada escena con escenario
    j = 0
    esc = list(escenas)
    for q, s in enumerate(esc):
        s.setdefault("k", 0 if q == 0 else None)
    for q, s in enumerate(esc):
        k = s["k"]; kn = esc[q + 1]["k"] if q + 1 < len(esc) else "s_fin"
        if "z" in s:
            x0 = 1300 * j; z = {"x0": x0 - (300 if j == 0 else 0), "x1": x0 + 1300, "set": s["z"]}
            if s.get("o"): z["o"] = s["o"]
            if j: z["k"] = k; pan.append({"k": k, "x": x0, "dur": 0.04, "corte": 1, "dir": 1})
            zonas.append(z); zx.append((q, x0))
            for a in s.get("actores", []):
                a = dict(a); ks = []
                for kk in a.pop("keys"):
                    kk = dict(kk); kk["x"] = x0 + kk.get("x", 540); kk.setdefault("y", 1700)
                    if "a" in kk: kk["a"] = [x0 + kk["a"][0], kk["a"][1]]
                    ks.append(kk)
                a["keys"] = ks; a["desde"] = k if q else a.get("desde", 0)
                if kn != "s_fin" or q + 1 < len(esc): a.setdefault("hasta", kn)
                if a.get("desde") == 0: a.pop("desde")
                actores.append(a)
            for p in s.get("props", []):
                p = dict(p); p["x"] = x0 + p.get("x", 540); p.setdefault("k", k); p.setdefault("fin", kn)
                if p["k"] == 0 and q == 0: pass
                props.append(p)
            j += 1
        else:
            ins.append((q, k, kn, s))
        if s.get("titulo"):
            t = s["titulo"]; titulos.append({"k": k if k else 0.2, "texto": t[0], "c": t[1], "fin": t[2] if len(t) > 2 else kn})
    E = {"momentos": M, "escenas": [{"tipo": "pelicula", "desde": "0", "escala": escala, "zonas": zonas, "pan": pan,
         "props": props, "actores": actores, "prohibidos": list(prohibidos), "numeros": list(numeros), "zoom": [],
         "planos_hint": list(hints), "sacudidas": list(sacudidas), "titulos": titulos, "emojis": list(emojis),
         "burbujas": list(burbujas), "chips": []}, {"tipo": "cierre", "desde": "s_fin"}],
         "cierre": cierre, "cierre2": cierre2, "paises": list(paises), "sfx": [], "cta": cta, "like": like}
    E["escenas"][0]["zonas"][0]["cam"] = 0
    for z in E["escenas"][0]["zonas"][1:]: z["cam"] = z["x0"]
    for (q, k, kn, s) in ins:
        prev = [x for (qq, x) in zx if qq < q]; nxt = [x for (qq, x) in zx if qq > q]
        vuelta = nxt[0] if (nxt and esc[q + 1].get("z")) else (prev[-1] if prev else 0)
        o = {"fondo": s["i"], "luz2": s.get("luz2", "255,244,228")}
        if s.get("pedestal"): o["pedestal"] = True
        if s.get("aroY"): o["aroY"] = s["aroY"]
        insertar(E, k if k else 0.01, kn, vuelta, "vitrinaV", o, s.get("props", []))
        if s.get("titulo") is None and False: pass
    # prohibidos/burbujas sobre un inserto: "ins": n (n-esimo inserto, desde 1) -> x relativa a ese inserto
    base = _INS[0] - len(ins)
    for pr in E["escenas"][0]["prohibidos"]:
        if pr.get("ins"): pr["x"] = 100000 + (base + pr.pop("ins")) * 2600 + pr.get("x", 540)
    if gancho2 is None: gancho2 = n - 5
    g = {"titulo": titulo, "texto_pantalla": texto_pantalla, "lote": ID, "marca": marca, "cuerpo": "pro",
         "pausa_larga_antes": [1, gancho2, gancho2 + 1, n - 1], "nota_datos": nota,
         "frases": frases, "frases_voz": voz or frases, "fuentes": list(fuentes), "escena": E}
    if extra: g.update(extra)
    guardar(path, g)
    return g
