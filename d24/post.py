#!/usr/bin/env python3
# uso: post.py DIR ID  -> arregla en DIR/ID.json las entradas caminando (el motor solo camina con "a":[x,y] + "dur")
import json,sys,re
D,ID=sys.argv[1],sys.argv[2]
g=json.load(open(f"{D}/{ID}.json")); T=json.load(open(f"{D}/datos.json"))["T"]
def res(k):
    if isinstance(k,(int,float)): return float(k)
    if k in T: return T[k]
    m=re.match(r'^([A-Za-z_0-9]+)([+-][0-9.]+)$',str(k))
    if m and m.group(1) in T: return T[m.group(1)]+float(m.group(2))
    try: return float(k)
    except: return None
n=0
for e in g["escena"]["escenas"]:
    if e.get("tipo")!="pelicula": continue
    LEN=e.get("lento") or 1.6
    pans=sorted([(res(p["k"]),p["x"]) for p in e.get("pan",[])])
    def cam(t):
        c=0
        for a,x in pans:
            if a<=t+0.5: c=x
        return c
    for ac in e.get("actores",[]):
        ks=ac["keys"]
        for i,k in enumerate(ks[:-1]):
            nx=ks[i+1]
            if k.get("pose")=="camina" and "a" not in k and abs(nx["x"]-k["x"])>=60:
                t0,t1=res(k["k"]),res(nx["k"]); c=cam(t0)
                x0=k["x"]
                if c<99000:
                    if nx["x"]>x0 and x0<c+260: x0=c-160        # entra desde fuera, por la izquierda
                    elif nx["x"]<x0 and x0>c+820: x0=c+1240     # o por la derecha
                dist=abs(nx["x"]-x0); dur=max(0.9,min(2.2,dist/330.0))
                k.update({"x":x0,"a":[nx["x"],nx.get("y",k["y"])],"dur":round(dur,2),"ease":"eio","pose":nx.get("pose","parado"),"dir":1 if nx["x"]>x0 else -1})
                for c_ in ("cara",): k[c_]=nx.get(c_,k.get(c_,"feliz"))
                if "objeto" in nx: k["objeto"]=nx["objeto"]
                # la llegada conserva la pose final: la key siguiente no debe adelantarse a la caminata
                if t1 is not None and t0 is not None and t1<t0+dur: nx["k"]=round(t0+dur,2)
                n+=1
# cortes suaves (fundido corto) y objetos vivos
FLOTAN={"documento","cartel","cronometro","lupa","telefono","calendarioP","grafico","orbe","trianguloP","ovni","globos","senal","pinGPS","candado","papel"}
for e in g["escena"]["escenas"]:
    if e.get("tipo")!="pelicula": continue
    for p_ in e.get("pan",[]):
        if p_.get("corte"): p_["suave"]=1
    for pr in e.get("props",[]):
        if pr.get("tipo") in FLOTAN and "mov" not in pr:
            pr.setdefault("flota",7); pr.setdefault("mece",0.025)
        if pr.get("tipo") in ("taza","bolsaCafe","bolsa_dinero","trofeo","cajita") and pr.get("x",0)>=99000: pr.setdefault("late",0.03)
for sf in g["escena"].get("sfx",[]):
    if "hoosh" in sf.get("f",""): sf["g"]=min(sf.get("g",0.1),0.05)
json.dump(g,open(f"{D}/{ID}.json","w"),ensure_ascii=False)
print("caminatas corregidas:",n)
