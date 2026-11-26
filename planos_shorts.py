#!/usr/bin/env python3
# Planificador de planos para Shorts (motor vertical escena.html, escenas "pelicula").
# uso: planos_shorts.py DIR ID [semilla]
# Lee DIR/ID.json + DIR/datos.json + DIR/vz_palabras.json y reescribe el "zoom" de la escena:
# un encuadre por tramo de voz (1,6-2,9 s), sin repetir tipo seguido ni dentro de los ultimos 3 planos.
# No toca guion, textos ni personajes. Los zooms escritos a mano se reemplazan (quedan en ID.pre.json).
#
# Como encuadra el motor: zoom {k,s,x,y,dur,r,mano} lleva el punto (x,y) del mundo al centro (540,1200) con escala s.
#  - sin "x" = centro del cuadro actual (sirve durante paneos e insertos). dur<=0.02 = corte.
#  - cifras, titulos, chips y subtitulos van FUERA del zoom (no se tapan ni se agrandan); las burbujas van DENTRO.
import json, sys, re, random, os, shutil

D, ID = sys.argv[1], sys.argv[2]
SEM = int(sys.argv[3]) if len(sys.argv) > 3 else sum(map(ord, ID))
R = random.Random(SEM)
fj = f"{D}/{ID}.json"
g = json.load(open(fj)); T = json.load(open(f"{D}/datos.json"))["T"]; PAL = json.load(open(f"{D}/vz_palabras.json"))
if not os.path.exists(f"{D}/{ID}.pre.json"): shutil.copy(fj, f"{D}/{ID}.pre.json")
ES = g["escena"]["escenas"]
e = next(x for x in ES if x.get("tipo") == "pelicula")
i_e = ES.index(e)

def res(k):
    if k is None: return None
    if isinstance(k, (int, float)): return float(k)
    if k in T: return T[k]
    m = re.match(r'^([A-Za-z_0-9]+)([+-][0-9.]+)$', str(k))
    if m and m.group(1) in T: return T[m.group(1)] + float(m.group(2))
    try: return float(k)
    except Exception: return None

A0 = res(e.get("desde")) or 0.0
FIN = res(ES[i_e + 1].get("desde")) if i_e + 1 < len(ES) else PAL[-1]["f"] + 0.3
if FIN is None: FIN = PAL[-1]["f"] + 0.3
LEN = e.get("lento") or 1.6
ESC = e.get("escala") or 1.3

# ---------- camara: tramos quietos ----------
pans = sorted([(res(p["k"]), p["x"], (p.get("dur") or 1.0) * LEN, bool(p.get("corte"))) for p in e.get("pan", []) if res(p["k"]) is not None])
segs, x, t, llega, msp = [], 0, A0, "inicio", None
for tk, px, Dp, corte in pans:
    ms, me = tk - 0.3 * Dp, tk + 0.7 * Dp
    if ms > t + 0.05: segs.append({"a": t, "b": ms, "x": x, "llega": llega, "ms": msp, "sale": "corte" if corte else "paneo"})
    x, t, llega, msp = px, me, ("corte" if corte else "paneo"), ms
if FIN > t + 0.05: segs.append({"a": t, "b": FIN, "x": x, "llega": llega, "ms": msp, "sale": "fin"})

# ---------- cosas en pantalla ----------
ACT = [a for a in e.get("actores", []) if a.get("keys")]
for a in ACT:
    a["_d"] = res(a.get("desde")) if a.get("desde") is not None else A0
    a["_h"] = res(a.get("hasta")) if a.get("hasta") is not None else 1e9
    for k in a["keys"]: k["_t"] = res(k["k"])
# perros y gatos (son objetos del motor) tambien pueden ser el sujeto del plano
for p in e.get("props", []):
    if p.get("tipo") in ("perro", "gato") and p.get("x", 0) < 99000 and not p.get("mov"):
        ta = res(p.get("k")) if p.get("k") is not None else A0
        tf = res(p.get("fin")) if p.get("fin") is not None else 1e9
        if ta is None: continue
        ACT.append({"keys": [{"k": ta, "x": p["x"], "y": p["y"], "dir": p.get("dir", 1), "_t": ta}], "_d": ta, "_h": (tf if tf is not None else 1e9) + 0.3,
                    "s": p.get("s", 1), "_animal": p["tipo"], "var": "animal"})
PROPS = []
for p in e.get("props", []):
    ta = res(p.get("k")) if p.get("k") is not None else A0 + 0.5
    tf = res(p.get("fin")) if p.get("fin") is not None else 1e9
    if ta is None or p.get("x", 0) >= 99000 or p.get("tipo") in ("neblina", "humo", "lamparaPie", "rotulo"): continue   # ambiente: no es un objeto a encuadrar
    PROPS.append({"p": p, "a": ta, "f": tf if tf is not None else 1e9, "x": p["x"], "y": p.get("y", 1700)})
BUR = []
for b in e.get("burbujas", []):
    ti = res(b.get("k")); tf = res(b.get("fin")) if b.get("fin") is not None else (ti or 0) + 2.2
    if ti is not None: BUR.append((ti - 0.15, (tf or ti + 2.2) + 0.3, b))
EMO = [(res(n["k"]), res(n["k"]) + n.get("dur", 1.5)) for n in e.get("emojis", []) if res(n["k"]) is not None]
NUM = [(res(n["k"]), res(n.get("fin")) if n.get("fin") is not None else 1e9) for n in e.get("numeros", []) if res(n["k"]) is not None]
GRA = [(res(c["k"]), res(c.get("fin")) if c.get("fin") is not None else 1e9) for c in e.get("titulos", []) if c.get("grande") and res(c["k"]) is not None]
CHI = [(res(c["k"]), res(c.get("fin")) if c.get("fin") is not None else 1e9) for c in e.get("chips", []) if res(c["k"]) is not None]

def estado(a, t):
    cur = a["keys"][0]
    for k in a["keys"]:
        if k["_t"] is not None and t >= k["_t"]: cur = k
    x, y, mov = cur["x"], cur["y"], False
    if cur.get("a"):
        d = cur.get("dur") or 1.2; q = max(0.0, min(1.0, (t - cur["_t"]) / d))
        x = cur["x"] + (cur["a"][0] - cur["x"]) * q; y = cur["y"] + (cur["a"][1] - cur["y"]) * q; mov = 0 < q < 1
    return cur, x, y, mov

def visibles(t, lo, hi):
    out = []
    for a in ACT:
        if not (a["_d"] <= t < a["_h"] - 0.3): continue
        cur, x, y, mov = estado(a, t)
        if lo + 60 <= x <= hi - 60: out.append(a)
    return out

def cabeza(a, y):      # centro y tope de la cabeza
    if a.get("_animal"):
        sa = a.get("s") or 1; h = 205 if a["_animal"] == "perro" else 165
        return y - h * sa, y - (h + 75) * sa, sa * 0.9
    sc = (a.get("s") or 1) * ESC
    return y - 320 * sc, y - 395 * sc, sc

# ---------- donde se puede cortar ----------
CAND = set()
for i, w in enumerate(PAL):
    fin_frase = re.search(r'[.,;:!?…]$', w["w"])
    gap = (PAL[i + 1]["i"] - w["f"]) if i + 1 < len(PAL) else 1
    if fin_frase or gap >= 0.14: CAND.add(round(w["f"] + min(0.06, max(0.0, gap / 2)), 3))
FUERTES = {"never", "nobody", "fired", "lost", "million", "millions", "billion", "billions", "trillions", "secret", "hidden", "locked", "fake", "hoax", "banned",
           "zero", "nothing", "scared", "surprised", "stressed", "real", "wrong", "dead", "worst", "only", "teleported",
           "nunca", "nadie", "millones", "secreto", "récord", "record", "enorme", "prohibido", "falso", "cero", "nada", "ganó", "gano", "fuerte", "peor"}
def fuerte(s, f):
    for w in PAL:
        if s + 0.5 <= w["i"] <= f - 0.7 and re.sub(r'[^\wáéíóúñ]', '', w["w"].lower()) in FUERTES: return w["i"]
    return None

# ---------- planificar ----------
NZ, hist, LOG, cuenta = [], [], [], {}
FORMAS_INS = ["empuje", "sube", "abre", "deriva", "baja", "inclina"]; usadas_ins = []
SAC = e.setdefault("sacudidas", [])
HINTS = [dict(h, _t=res(h["k"])) for h in e.get("planos_hint", []) if res(h["k"]) is not None]

def K(t, s, x=None, y=None, dur=0.01, **extra):
    z = {"k": round(t - A0, 3), "s": round(s, 3), "dur": round(max(0.01, dur), 2)}
    if x is not None: z["x"] = round(x)
    if y is not None: z["y"] = round(y)
    z.update({k: v for k, v in extra.items() if v})
    NZ.append(z)

def entrada_zoom(n0, punch=1.16, G=0.5):
    """Tras un corte: el plano arranca un poco mas cerca y se asienta (el corte se siente como un zoom que sigue)."""
    if len(NZ) <= n0: return
    z0 = dict(NZ[n0]); k0 = NZ[n0]["k"]
    ini = dict(z0); ini["s"] = round(z0["s"] * punch, 3); ini["dur"] = 0.01
    NZ[n0]["k"] = round(k0 + 0.02, 3); NZ[n0]["dur"] = G
    for z_ in NZ[n0 + 1:]:
        fin_ = z_["k"] + z_["dur"]; z_["k"] = round(max(z_["k"], k0 + G + 0.04), 3); z_["dur"] = round(max(0.25, fin_ - z_["k"]), 2)
    NZ.insert(n0, ini)

def salida_zoom(tc, punch=1.16, G=0.34):
    """Antes de un corte: acelera hacia adentro."""
    if not NZ: return
    u = NZ[-1]; z = {"k": round(tc - G - 0.03 - A0, 3), "s": round(u["s"] * punch, 3), "dur": G}
    for c_ in ("x", "y", "r"):
        if c_ in u: z[c_] = u[c_]
    if z["k"] > u["k"] + 0.25: NZ.append(z)

def sin_medios(i0, t, actores):
    """Si un personaje queda partido por el borde del cuadro, corre el encuadre para dejarlo entero adentro (o entero afuera)."""
    for z in NZ[i0:]:
        if "x" not in z: continue
        zz, cx = z["s"], z["x"]
        for _ in range(2):
            for ac in actores:
                cur, ax, ay, mv = estado(ac, t)
                if mv: continue
                hw = 140 * (ac.get("s") or 1) * ESC
                Lp, Rp = 540 + (ax - hw - cx) * zz, 540 + (ax + hw - cx) * zz
                if Lp < 0 < Rp:
                    adentro, afuera = -Lp / zz + 14, Rp / zz + 14
                    cx += -adentro if adentro <= 1.6 * afuera and adentro <= 190 else (afuera if afuera <= 190 else 0)
                elif Lp < 1080 < Rp:
                    adentro, afuera = (Rp - 1080) / zz + 14, (1080 - Lp) / zz + 14
                    cx += adentro if adentro <= 1.6 * afuera and adentro <= 190 else (-afuera if afuera <= 190 else 0)
        z["x"] = round(cx)

for sg in segs:
    a, b, camx = sg["a"], sg["b"], sg["x"]
    if b - a < 0.25: continue
    if camx >= 99000:                      # inserto de detalle: cada uno con una forma de camara distinta
        L = b - a; cxi = camx + 540; d = max(0.3, L - 0.08); n_ins = len(NZ)
        pap = next((p for p in e.get("props", []) if p.get("tipo") == "papel" and camx - 150 <= p.get("x", 0) <= camx + 1230), None)
        libres_i = [f_ for f_ in FORMAS_INS if f_ not in usadas_ins] or FORMAS_INS
        forma = "papel" if pap else R.choice(libres_i)
        usadas_ins.append(forma)
        if forma == "papel":               # recorre el papel de arriba abajo y se detiene en el dato
            ps = pap.get("s", 1); fd = (pap.get("o") or pap).get("filaDato", 7)
            y0 = pap["y"] - 640 * ps; y1 = pap["y"] + (-630 + fd * 50) * ps
            K(a - 0.02, 1.45, pap["x"], y0 + 120); K(a + 0.05, 1.7, pap["x"], y1, dur=max(0.5, d * 0.7))
        elif forma == "empuje": K(a - 0.02, 1.0); K(a + 0.02, 1.13, dur=d)
        elif forma == "abre": K(a - 0.02, 1.26, cxi, 1260); K(a + 0.02, 1.0, cxi, 1200, dur=d)
        elif forma == "sube": K(a - 0.02, 1.24, cxi, 1430); K(a + 0.02, 1.24, cxi, 1170, dur=d)
        elif forma == "baja": K(a - 0.02, 1.24, cxi, 1120); K(a + 0.02, 1.24, cxi, 1400, dur=d)
        elif forma == "deriva": K(a - 0.02, 1.16, cxi - 75, 1230); K(a + 0.02, 1.16, cxi + 75, 1230, dur=d)
        else: K(a - 0.02, 1.13, cxi, 1220, r=-0.04); K(a + 0.02, 1.13, cxi, 1220, dur=d, r=0.04)
        entrada_zoom(n_ins); salida_zoom(b)
        hist.append("detalle"); cuenta["detalle:" + forma] = cuenta.get("detalle:" + forma, 0) + 1
        LOG.append(f"{a:6.2f}-{b:6.2f} detalle   ({forma})")
        continue
    lo, hi = camx, camx + 1080
    zona = next((z for z in e.get("zonas", []) if z["x0"] <= camx + 540 <= z["x1"]), {"x0": camx - 150, "x1": camx + 1230})
    cl = lambda xx, s: max(zona["x0"] + 540 / s, min(zona["x1"] - 540 / s, xx))
    if sg["llega"] == "paneo" and sg["ms"] is not None:
        K(sg["ms"], 1.0, dur=0.3); hist.append("general")                              # el paneo ya muestra el lugar completo: cuenta como general
    # eventos: algo aparece o alguien cambia de accion
    ev = sorted({p["a"] - 0.05 for p in PROPS if a + 0.9 < p["a"] < b - 0.8 and lo <= p["x"] <= hi} |
                {k["_t"] - 0.05 for ac in ACT for k in ac["keys"] if k["_t"] and a + 0.9 < k["_t"] < b - 0.8 and ac["_d"] <= k["_t"] < ac["_h"]})
    fij = sorted(h["_t"] - 0.05 for h in HINTS if a + 0.6 < h["_t"] < b - 0.8)
    cand = sorted(c for c in CAND if a + 0.9 < c < b - 0.8)
    cortes, t = [a], a
    while True:
        nx = [f for f in fij if f > t + 0.6]
        if nx and nx[0] < t + 6.2: t = nx[0]
        else:
            obj = t + R.uniform(4.0, 5.4)         # Tao 24-nov 22:56: planos de 4 a 6 s
            op = [c for c in ev if t + 3.2 <= c <= t + 6.2] or [c for c in cand if t + 3.2 <= c <= t + 6.2]
            t = min(op, key=lambda c: abs(c - obj)) if op else obj
        if t >= b - 2.6: break
        cortes.append(t)
    for i, s in enumerate(cortes):
        f = cortes[i + 1] if i + 1 < len(cortes) else b; L = f - s
        vis = visibles(s + 0.15, lo, hi)
        quietos = [ac for ac in vis if not estado(ac, s + 0.15)[3] and not any(k.get("a") and k["_t"] and s - 0.2 < k["_t"] < f for k in ac["keys"])]
        andan = [(ac, k) for ac in ACT for k in ac["keys"] if k.get("a") and k["_t"] is not None and s - 0.3 <= k["_t"] < f - 0.6 and ac["_d"] <= k["_t"] < ac["_h"]]
        bur = [bb for (b0, b1, bb) in BUR if b0 < f and b1 > s]
        num = any(n0 - 0.2 < f and min(n1, n0 + 3.2) > s for n0, n1 in NUM) or any(n0 - 0.2 < f and n1 > s for n0, n1 in EMO)   # el emoji que salta ocupa el centro alto
        gra = any(g0 - 0.2 < f and min(g1, g0 + 2.2) > s for g0, g1 in GRA)
        chi = any(c0 - 0.2 < f and c1 > s for c0, c1 in CHI)
        techo = 1010 if num else (860 if (gra or chi) else 680)      # bajo esta linea de pantalla debe quedar la cabeza
        aparece = [p for p in PROPS if s - 0.3 <= p["a"] < s + 0.9 and lo + 40 <= p["x"] <= hi - 40]
        pv = [p for p in PROPS if p["a"] <= s + 0.2 < p["f"] - 0.5 and lo + 40 <= p["x"] <= hi - 40]
        prev = hist[-1] if hist else None
        def activo():
            best, bt = None, -1e9
            for ac in quietos:
                for k in ac["keys"]:
                    if k["_t"] is not None and s - 3 <= k["_t"] <= s + 1.2 and k["_t"] > bt: best, bt = ac, k["_t"]
            return best or (quietos[len(hist) % len(quietos)] if quietos else None)
        foco = activo()
        hint = next((h for h in HINTS if abs(h["_t"] - s) < 0.22), None)
        tw = None
        if hint: tipo = hint["tipo"]; foco = next((ac for ac in quietos if ac.get("var") == hint.get("var")), foco)
        elif bur:                                                    # la burbuja va dentro del zoom: se encuadra entera, o cuadro abierto
            ops = [x_ for x_ in ("globo", "general", "balanceo") if x_ not in cuenta] or [x_ for x_ in ("globo", "general", "balanceo") if x_ != prev]
            tipo = ops[0]
        elif andan: tipo = "camina" if "camina" not in cuenta else next((x_ for x_ in ("general", "recorre", "balanceo") if x_ not in cuenta), "general")
        else:
            c = {"medio": 3.0, "primer": 2.2, "dos": 2.2, "holandes": 1.3, "objeto": 1.8, "general": 0.7, "aleja": 1.6, "acerca": 1.6,
                 "vertical": 1.3, "ojos": 0.8, "mano": 1.5, "rapido": 2.6, "recorre": 1.1, "manos": 2.0, "tercio": 1.6, "balanceo": 1.2, "alto": 1.2}
            if not foco: [c.pop(k_, None) for k_ in ("medio", "primer", "holandes", "aleja", "acerca", "vertical", "ojos", "mano", "rapido", "manos", "tercio", "alto")]
            if foco:
                cur_f = estado(foco, s + 0.15)[0]
                if not (cur_f.get("objeto") or foco.get("objeto") or cur_f.get("pose") in ("sostiene", "ofrece", "juega", "telefono")): c.pop("manos", None)
            par = None
            if len(quietos) >= 2:
                xs = sorted(estado(ac, s + 0.15)[1] for ac in quietos)
                if 180 <= xs[-1] - xs[0] <= 760: par = (xs[0], xs[-1])
            if not par: c.pop("dos", None)
            if not pv: c.pop("objeto", None); c.pop("vertical", None)
            tw = fuerte(s, f) if foco else None
            if tw is None: c.pop("rapido", None)
            if num or techo >= 1000: [c.pop(k_, None) for k_ in ("primer", "ojos", "rapido", "aleja", "manos", "alto")]
            if L < 1.5: [c.pop(k_, None) for k_ in ("aleja", "acerca", "vertical", "recorre")]
            if L > 2.6: c.pop("ojos", None)
            if aparece and "objeto" in c and "objeto" not in cuenta: c = {"objeto": 3}
            rec = set(hist[-3:])
            c2 = ({k_: v for k_, v in c.items() if k_ not in cuenta}                 # Tao: que no se repita la forma dentro del video
                  or {k_: v for k_, v in c.items() if k_ not in rec} or {k_: v for k_, v in c.items() if k_ != prev} or {"general": 1})
            if prev in ("medio", "holandes", "mano", "tercio"): [c2.pop(k_, None) for k_ in ("medio", "holandes", "mano", "tercio") if len(c2) > 1]
            for k_ in c2: c2[k_] = c2[k_] / (1 + 2.0 * cuenta.get(k_, 0))
            tipo = R.choices(*zip(*c2.items()))[0]
        if tipo not in ("general", "recorre", "objeto", "dos", "camina", "globo", "balanceo") and not foco: tipo = "general"
        hist.append(tipo); cuenta[tipo] = cuenta.get(tipo, 0) + 1
        LOG.append(f"{s:6.2f}-{f:6.2f} {tipo:9s} L={L:.1f} foco={foco.get('var') if foco else '-'} n_vis={len(vis)}{' burbuja' if bur else ''}{' cifra' if num else ''}")
        fx = fy = None
        if foco:
            cur, ax, ay, _ = estado(foco, s + 0.15); yc, ytop, sc = cabeza(foco, ay); dr = cur.get("dir", 1)
            def cy_para(z, mitad=75):       # y del mundo que va al centro, dejando la cabeza bajo el techo
                obj = max(1090, techo + mitad * sc * z + 25)        # donde queda el centro de la cabeza en pantalla
                return yc - (obj - 1200) / z
        mov = R.random() < 0.55
        n0 = len(NZ)
        if tipo == "globo":
            bb = bur[0]; ab = e["actores"][bb["de"]] if bb.get("de") is not None and bb["de"] < len(e["actores"]) else None
            if ab is not None and ab in ACT:
                _, bx0, by0, _m = estado(ab, max(s + 0.15, res(bb["k"]) + 0.05)); scb = (ab.get("s") or 1) * ESC
                bx = bx0 + (bb.get("dx") or 0); by = by0 - 330 * scb - 130 + (bb.get("dy") or 0)
                w = max(160, 27 * len(bb["texto"]) + 70) * 1.3
                x0, x1 = min(bx - w / 2, bx0 - 150) - 60, max(bx + w / 2, bx0 + 150) + 60
                for o in quietos:                      # el que escucha tambien entra al cuadro si esta cerca
                    ox = estado(o, s + 0.15)[1]
                    if o is not ab and abs(ox - bx0) <= 560: x0, x1 = min(x0, ox - 150), max(x1, ox + 150)
                z = max(1.0, min(1.32, 1080 / (x1 - x0)))
                cyy = min(by - 75 - (techo + 20 - 1200) / z, by0 - 240)        # burbuja bajo el techo y pies casi a la vista
                if z < 1.06: K(s, 1.0); K(s + 0.03, 1.04, dur=L - 0.1)
                else: K(s, z, cl((x0 + x1) / 2, z), cyy); K(s + 0.03, z + 0.03, cl((x0 + x1) / 2, z), cyy, dur=L - 0.1)
            else: K(s, 1.0); K(s + 0.03, 1.04, dur=L - 0.1)
        elif tipo == "general":
            K(s, 1.0); K(s + 0.03, 1.09 if mov else 1.06, dur=L - 0.1)
        elif tipo == "manos":            # primer plano de lo que tiene en las manos
            z = 2.05; my = ay - 170 * sc; cyy = my - (max(1190, techo + 210) - 1200) / z
            K(s, z, cl(ax + dr * 70, z), cyy); K(s + 0.03, z + 0.12, cl(ax + dr * 70, z), cyy, dur=L - 0.1)
        elif tipo == "tercio":           # el personaje a un lado, con aire hacia donde mira
            z = 1.24; K(s, z, cl(ax + dr * 200, z), cy_para(z)); K(s + 0.03, z + 0.04, cl(ax + dr * 170, z), cy_para(z + 0.04), dur=L - 0.1)
        elif tipo == "balanceo":         # la camara se mece de un lado a otro
            z = 1.2 if foco else 1.12; bx_ = ax if foco else camx + 540; by_ = cy_para(z) if foco else 1230; r0 = R.choice([-1, 1]) * 0.04
            if bur: z, bx_, by_ = 1.06, camx + 540, 1215
            K(s, z, cl(bx_, z), by_, r=r0); K(s + 0.03, z, cl(bx_, z), by_, dur=L - 0.05, r=-r0)
        elif tipo == "alto":             # cabeza arriba del cuadro, cuerpo entero abajo: se ve mas grande
            z = 1.5; obj_ = techo + 80 * sc * z + 30; cyy = yc - (obj_ - 1200) / z
            K(s, z, cl(ax, z), cyy); K(s + 0.03, z + 0.08, cl(ax, z), cyy + 20, dur=L - 0.1)
        elif tipo == "recorre":
            z = 1.14; d = R.choice([-1, 1]) * 110
            K(s, z, cl(camx + 540 - d, z), 1230); K(s + 0.03, z, cl(camx + 540 + d, z), 1230, dur=L - 0.05)
        elif tipo == "medio":
            z = 1.3; K(s, z, cl(ax + dr * 35, z), cy_para(z)); K(s + 0.03, z + (0.14 if mov else 0.09), cl(ax + dr * 35, z), cy_para(z + 0.12), dur=L - 0.1)
        elif tipo == "mano":
            z = 1.34; K(s, z, cl(ax + dr * 30, z), cy_para(z), mano=1.4)
        elif tipo == "holandes":
            z = 1.4; rr = R.choice([-1, 1]) * 0.055
            K(s, z, cl(ax, z), cy_para(z), r=rr); K(s + 0.03, z + 0.05, cl(ax, z), cy_para(z + 0.05), dur=L - 0.1, r=rr)
        elif tipo == "primer":
            z = 1.72; K(s, z, cl(ax + dr * 25, z), cy_para(z, 80)); K(s + 0.03, z + (0.1 if mov else 0.04), cl(ax + dr * 25, z), cy_para(z + 0.1, 80), dur=L - 0.1)
        elif tipo == "ojos":
            z = 2.25; K(s, z, cl(ax, z), cy_para(z, 80)); K(s + 0.03, z + 0.08, cl(ax, z), cy_para(z + 0.08, 80), dur=L - 0.1)
        elif tipo == "rapido":
            K(s, 1.0); K(s + 0.03, 1.05, dur=max(0.3, tw - s - 0.1))
            z = 1.7; K(tw - 0.06, z, cl(ax, z), cy_para(z, 80), dur=0.16); SAC.append({"k": round(tw - A0, 3), "f": 9, "dur": 0.35})
        elif tipo == "aleja":
            z = 1.65; K(s, z, cl(ax, z), cy_para(z, 80)); K(s + 0.25, 1.0, dur=max(0.8, L - 0.5))
        elif tipo == "acerca":
            z = 1.38; K(s, 1.0); K(s + 0.2, z, cl(ax + dr * 30, z), cy_para(z), dur=max(0.8, L - 0.4))
        elif tipo == "dos":
            x0, x1 = par; z = max(1.08, min(1.34, 1080 / (x1 - x0 + 430)))
            ymed = min(cabeza(ac, estado(ac, s + 0.15)[2])[0] for ac in quietos)
            cyy = ymed - (max(1100, techo + 75 * ESC * z + 25) - 1200) / z
            K(s, z, cl((x0 + x1) / 2, z), cyy); K(s + 0.03, z + 0.04, cl((x0 + x1) / 2, z), cyy, dur=L - 0.1)
        elif tipo in ("objeto", "vertical"):
            p = (aparece or pv)[0] if (aparece or pv) else None
            p = min(aparece or pv, key=lambda q: abs(q["a"] - s))
            py = p["y"] if p["y"] < 1500 else p["y"] - 110          # los que flotan se centran en si mismos; los del piso, un poco mas arriba
            z = 1.42
            cyo = py - (max(1180, techo + 190) - 1200) / z
            if tipo == "objeto" or not foco:
                K(s, z, cl(p["x"], z), cyo); K(s + 0.03, z + (0.09 if mov else 0.04), cl(p["x"], z), cyo, dur=L - 0.1)
            else:                                    # paneo vertical: del objeto a la cara
                z = 1.5; K(s, z, cl(p["x"], z), cyo); K(s + 0.25, z, cl(ax, z), cy_para(z), dur=max(0.8, L - 0.5))
        elif tipo == "camina":
            ac, k = andan[0]; z = 1.18; d = k.get("dur") or 1.2
            xa = max(lo + 150, min(hi - 150, k["x"])); xb = k["a"][0]; yc2 = cabeza(ac, k["a"][1])[0]
            cyy = yc2 - (max(1100, techo + 75 * ESC * z + 25) - 1200) / z
            K(s, z, cl(xa, z), cyy); K(max(s + 0.03, k["_t"]), z, cl(xb, z), cyy, dur=d)
        else:
            K(s, 1.0)
        if tipo not in ("camina",): sin_medios(n0, s + 0.15, vis)
        ult_del_tramo = (i == len(cortes) - 1)
        viaja = (i > 0 or sg["llega"] == "paneo") and tipo not in ("rapido",) and len(NZ) > n0
        if i == 0 and sg["llega"] == "corte" and tipo != "rapido": entrada_zoom(n0)
        if viaja:                        # la camara viaja al encuadre nuevo y despues sigue su movimiento
            G = 0.8 if L >= 2.4 else 0.5
            NZ[n0]["dur"] = G
            for z_ in NZ[n0 + 1:]:
                fin_ = z_["k"] + z_["dur"]; z_["k"] = round(max(z_["k"], NZ[n0]["k"] + G + 0.02), 3); z_["dur"] = round(max(0.25, fin_ - z_["k"]), 2)
        if ult_del_tramo and sg["sale"] == "corte": salida_zoom(b)

# ---------- guardar ----------
for a in ACT:
    for k in a["keys"]: k.pop("_t", None)
    a.pop("_d", None); a.pop("_h", None)
NZ.sort(key=lambda z: z["k"])
# 26-nov (prueba, pedido de Tao 14:02): el zoom que fija el encuadre nuevo usa la MISMA clave que el corte de zona y lleva
# "corte": el motor lo aplica de golpe en el mismo cuadro que la zona. Antes quedaba 25-45 ms despues y en ese hueco se
# veian 1-2 cuadros con la zona nueva y el encuadre viejo (fondo ajeno).
for p in e.get("pan", []):
    tp = res(p.get("k")) if p.get("corte") else None
    if tp is None: continue
    sig = [z for z in NZ if -1e-9 <= A0 + z["k"] - tp <= 0.1]
    if not sig: continue
    z = min(sig, key=lambda z_: z_["k"])
    if z["dur"] <= 0.02 and z.get("_kc", p["k"]) == p["k"]: z["_kc"] = p["k"]
for z in NZ:
    if "_kc" in z: z["k"] = z.pop("_kc"); z["corte"] = 1
e["zoom"] = NZ
json.dump(g, open(fj, "w"), ensure_ascii=False)
np = len(LOG); dur = FIN - A0
dist = sorted(cuenta.items(), key=lambda kv: -kv[1])
print(f"planos: {np} en {dur:.1f} s (uno cada {dur / max(1, np):.1f} s) · tipos distintos: {len(cuenta)} · " + ", ".join(f"{k}×{v}" for k, v in dist))
rep = [i for i in range(1, len(hist)) if hist[i] == hist[i - 1]]
print("repetidos seguidos:", len(rep))
open(f"{D}/planos.log", "w").write("\n".join(LOG) + "\n")
