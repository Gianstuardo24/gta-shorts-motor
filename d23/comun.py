import json
def perro(**k):
    d={"tipo":"perro","pose":"sentado","cola":6,"color":"#d9a35b","collar":"rosa"}; d.update(k)
    if d.get("collar") is None: d.pop("collar")
    return d
LOBO=dict(color="#8d8d94",color2="#d6d6dc",oscuro="#55555e",lejos="#6e6e76",collar=None,cola=0)
def gato(**k):
    d={"tipo":"gato","pose":"sentado","s":0.85}; d.update(k); return d
def guardar(path,g): json.dump(g,open(path,"w"),ensure_ascii=False)

# ---- 23-nov: escenarios nuevos e insertos (cortes a un objeto en primer plano) ----
def poner_sets(E, specs):
    """specs: lista por zona de (set, opciones) o None para dejar igual. Agrega 'cam' a cada zona."""
    e = E["escenas"][0]; pans = {p["k"]: p["x"] for p in e.get("pan", [])}
    for z, sp in zip(e["zonas"], specs):
        if sp:
            z["set"] = sp[0]; z.pop("luz", None); z.pop("neon", None)
            if len(sp) > 1 and sp[1]: z["o"] = sp[1]
        z["cam"] = pans.get(z.get("k"), 0 if z["x0"] < 0 else z["x0"])

def quitar_props(E, tipos):
    e = E["escenas"][0]; e["props"] = [p for p in e["props"] if p["tipo"] not in tipos]

_INS = [0]
def insertar(E, k_in, k_out, vuelta, set_="vitrinaV", o=None, props=(), whoosh=True):
    """Corte a un primer plano entre k_in y k_out; 'vuelta' = x de camara de la zona a la que vuelve."""
    e = E["escenas"][0]; _INS[0] += 1; XI = 100000 + _INS[0] * 2600
    z = {"x0": XI - 120, "x1": XI + 1200, "set": set_, "cam": XI}
    if o: z["o"] = o
    e["zonas"].append(z)
    e["pan"].append({"k": k_in, "x": XI, "dur": 0.04, "corte": 1})
    ex = [p for p in e["pan"] if p["k"] == k_out and not p.get("corte")]
    if ex: ex[0].update({"dur": 0.04, "corte": 1, "dir": 1})      # sale del inserto directo a la escena siguiente
    else: e["pan"].append({"k": k_out, "x": vuelta, "dur": 0.04, "corte": 1, "dir": 1})
    e.setdefault("zoom", []).extend([{"k": k_in, "s": 1.0, "dur": 0.01}, {"k": k_out, "s": 1.0, "dur": 0.01}])
    for p in props:
        p = dict(p); p["x"] = XI + p.get("x", 540); p.setdefault("y", 1650); p.setdefault("k", k_in); p.setdefault("fin", k_out); p.setdefault("z", 1800)
        e["props"].append(p)
    if whoosh:
        E.setdefault("sfx", [])
        E["sfx"] += [{"f": "extra/Whip_Whoosh_BW.11026.wav", "k": k_in, "off": -0.06, "dur": 0.3, "g": 0.10},
                     {"f": "extra/MODE_BE2_fx_foley_whoosh_04.wav", "k": k_out, "off": -0.05, "dur": 0.3, "g": 0.10}]
