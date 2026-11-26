#!/usr/bin/env python3
# uso: medir.py a.mp4 [b.mp4 ...]  -> movimiento de la ESCENA (se recorta la franja de textos de arriba), mismas medidas del evaluador
import subprocess,sys,numpy as np
def mov(mp4,fps=10,w=90,h=80,b=10):
    # zona de escena: y 1000..1900 de 1920 (bajo cifras y titulos)
    vf=f'fps={fps},crop=1080:900:0:1000,scale={w}:{h},format=gray'
    p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-i',mp4,'-vf',vf,'-f','rawvideo','-'],stdout=subprocess.PIPE)
    g=[];prev=None;n=w*h
    while True:
        buf=p.stdout.read(n)
        if len(buf)<n: break
        f=np.frombuffer(buf,dtype=np.uint8).reshape(h,w).astype(np.int16)
        if prev is not None: g.append(np.abs(f-prev).mean())
        prev=f
    return np.array(g),fps
for m in sys.argv[1:]:
    g,fps=mov(m); T=len(g)/fps
    cortes=int(((g[1:]>12)&(g[:-1]<=12)).sum())
    quieto=(g<0.6).mean()*100
    print(f"{m.split('/')[-2]+'/'+m.split('/')[-1]:28s} dur {T:5.1f}s · cambio medio {g.mean():5.2f} · cuadros casi quietos {quieto:4.1f}% · cambios bruscos de encuadre {cortes} ({cortes/T*60:4.1f}/min)")
