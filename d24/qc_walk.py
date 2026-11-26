#!/usr/bin/env python3
# uso: qc_walk.py SLOT ID [SLOT ID ...] -> /tmp/qc_walk.jpg con 4 cuadros de cada caminata (fila por video)
import json,sys,subprocess,re,os
filas=[]
for slot,ID in zip(sys.argv[1::2],sys.argv[2::2]):
    g=json.load(open(f"{slot}/{ID}.json")); T=json.load(open(f"{slot}/datos.json"))["T"]
    def res(k):
        if isinstance(k,(int,float)): return float(k)
        if k in T: return T[k]
        m=re.match(r'^([A-Za-z_0-9]+)([+-][0-9.]+)$',str(k)); return T[m.group(1)]+float(m.group(2))
    e=g["escena"]["escenas"][0]; ts=[]
    for a in e["actores"]:
        for k in a["keys"]:
            if k.get("a"): ts.append((res(k["k"]),k.get("dur",1.2)))
    if not ts: continue
    t0,d=ts[0]; fs=[]
    for j,q in enumerate([0.15,0.45,0.75,1.1]):
        f=f"/tmp/w_{slot}_{j}.jpg"; subprocess.run(["ffmpeg","-y","-loglevel","error","-ss",str(t0+q*d),"-i",f"{slot}/v1.mp4","-frames:v","1","-vf","scale=200:-2",f]); fs.append(f)
    out=f"/tmp/w_{slot}.jpg"; cmd=["ffmpeg","-y","-loglevel","error"]+sum([["-i",f] for f in fs],[])+["-filter_complex",f"hstack={len(fs)}",out]; subprocess.run(cmd); filas.append(out)
    print(slot,"caminata en",round(t0,1),"dur",d)
if len(filas)>1:
    cmd=["ffmpeg","-y","-loglevel","error"]+sum([["-i",f] for f in filas],[])+["-filter_complex",f"hstack={len(filas)}","/tmp/qc_walk.jpg"]; subprocess.run(cmd)
elif filas: os.replace(filas[0],"/tmp/qc_walk.jpg")
