"""Acorta insertos largos: si un plano de detalle dura mas que su maximo, vuelve antes al escenario.
Uso: python3 recortar_insertos.py guion_final.json datos0.json   (modifica guion_final.json)"""
import json, sys, os
fj, fd = sys.argv[1:3]
fw = os.path.join(os.path.dirname(os.path.abspath(fj)), "vz_palabras.json")
PAL = json.load(open(fw)) if os.path.exists(fw) else []
def calzar(obj, t_in, t_out):
    """Vuelta al escenario en una pausa de la voz (fin de frase > coma > entre palabras), cerca del objetivo."""
    mejor, pm = obj, -1e9
    for a, b in zip(PAL, PAL[1:]):
        g = (a["f"] + b["i"]) / 2
        if not (obj - 0.7 <= g <= obj + 0.9) or g > t_out - 0.35 or g < t_in + 1.0: continue
        w = 3 if a["w"].rstrip('"\'')[-1:] in ".!?:" else 2 if a["w"][-1:] in ",;" else 1
        sc = w - abs(g - obj) * 1.2
        if sc > pm: mejor, pm = g, sc
    return mejor
g = json.load(open(fj)); T = json.load(open(fd))["T"]
e = g["escena"]["escenas"][0]
MAX = {"capituloH": 1.9, "chequeH": 4.9, "cuatroH": 7.0, "manosTeclado": 2.4, "telefonoH": 2.4, "papelesH": 2.4, "billetesH": 2.4, "tableroH": 6.5, "balanzaH": 4.4, "pilaH": 3.0, "diarioH": 2.8, "numeroH": 2.4,
       "mesaCenital": 3.2, "vitrina": 2.8}
VAR = [1.0, 0.85, 1.1, 0.9, 1.05]
tt = lambda k: k if isinstance(k, (int, float)) else T.get(k)
zona = {z["x0"] + 537: z.get("set") for z in e["zonas"]}
pans = sorted(enumerate(e["pan"]), key=lambda ip: (tt(ip[1]["k"]) if tt(ip[1]["k"]) is not None else 1e9, ip[0]))
quitar, nuevos, n = set(), [], 0
for j, (i, p) in enumerate(pans):
    if not (p.get("corte") and p["x"] >= 99000): continue
    t_in = tt(p["k"]);
    if t_in is None or j + 1 >= len(pans): continue
    io, po = pans[j + 1]; t_out = tt(po["k"])
    if t_out is None: continue
    home = 0
    for i2, p2 in pans[:j]:
        if p2["x"] < 99000: home = p2["x"]
    lim = MAX.get(zona.get(p["x"]), 3.0) * VAR[n % len(VAR)]; n += 1
    if t_out - t_in <= lim + 0.3: continue
    tn = round(calzar(t_in + lim, t_in, t_out), 2)
    sig = [tt(p3["k"]) for i3, p3 in pans if p3.get("corte") and p3["x"] >= 99000 and i3 != i and tt(p3["k"]) is not None and tn - 0.05 < tt(p3["k"]) < tn + 1.2]
    if (po["x"] != home and t_out - tn < 1.2) or sig: continue      # no dejar un pedacito de escena (<1.2 s) entre dos insertos
    nuevos.append({"k": tn, "x": home, "dur": 0.04, "corte": 1, "dir": 1, "tr": po.get("tr", "lineas")})
    e["zoom"].append({"k": tn, "s": 1.0, "dur": 0.01})
    if po["x"] == home and po.get("corte"):
        quitar.add(io)
        for s in g["escena"].get("sfx", []):
            if s.get("k") == po["k"]: s["k"], s["off"] = "0", round(tn - 0.05, 2)
    print(f"{zona.get(p['x'])}: {t_out - t_in:.1f}s -> {lim:.1f}s")
e["pan"] = [p for i, p in enumerate(e["pan"]) if i not in quitar] + nuevos
json.dump(g, open(fj, "w"), ensure_ascii=False)
print("recortados", len(nuevos))
