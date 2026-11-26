"""Prueba 27 · mide el movimiento REAL de un render: energía de cambio entre cuadros consecutivos (cuánto cambia la imagen),
detección de detenciones intermedias y de quietud. Uso: medir_movimiento.py video.mp4 t_quieto_desde [salida.jpg] [palabras.json LEAD]"""
import sys, json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
f=sys.argv[1];tq=float(sys.argv[2]);out=sys.argv[3] if len(sys.argv)>3 else None
W,H=270,480
raw=subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
fr=np.frombuffer(raw,np.uint8).reshape(-1,H,W,3).astype(np.int16)
E=np.array([0]+[np.abs(fr[i]-fr[i-1]).sum(2).__gt__(18).sum() for i in range(1,len(fr))],float)   # píxeles que cambian
t=np.arange(len(fr))/30;mov=E>2
iq=int(np.ceil(tq*30));quieto=E[iq:]
# detención intermedia: entre el primer y el último cuadro con movimiento, ¿hay cuadros sin cambio?
idx=np.where(mov)[0];paradas=[i for i in range(idx[0],idx[-1]+1) if not mov[i]] if len(idx) else []
print(f'cuadros: {len(fr)} · con movimiento: {int(mov.sum())} ({t[idx[0]]:.2f}–{t[idx[-1]]:.2f} s) · detenciones intermedias: {len(paradas)}')
print(f'quietud desde {tq:.2f} s: máximo de píxeles que cambian = {int(quieto.max()) if len(quieto) else 0} (0 = completamente quieto)')
pk=int(np.argmax(E));sube=all(E[i]<=E[i+1]*1.35+3 for i in range(idx[0],pk));baja=all(E[i+1]<=E[i]*1.35+3 for i in range(pk,idx[-1]))
print(f'perfil: pico en {t[pk]:.2f} s · subida sin tirones: {"sí" if sube else "NO"} · bajada continua: {"sí" if baja else "NO"}')
if out:
    Wc,Hc=1200,420;C=Image.new('RGB',(Wc,Hc),(16,17,22));d=ImageDraw.Draw(C);x0,y0,x1,y1=60,40,Wc-20,Hc-70;fn=ImageFont.truetype('/home/claude/escena/Poppins-Regular.ttf',18)
    d.line([(x0,y1),(x1,y1)],fill=(120,120,130),width=2);pts=[(x0+(x1-x0)*ti/t[-1],y1-(y1-y0)*e/max(E.max(),1)) for ti,e in zip(t,E)];d.line(pts,fill=(90,200,255),width=4)
    X=x0+(x1-x0)*tq/t[-1];d.rectangle([X,y0,x1,y1],outline=(0,255,120),width=2);d.text((X+6,y0+4),'quieto',font=fn,fill=(0,255,120))
    if len(sys.argv)>5:
        pal=json.load(open(sys.argv[4]));LEAD=float(sys.argv[5])
        for p in pal:
            X=x0+(x1-x0)*p['i']/t[-1];d.line([(X,y1),(X,y1+6)],fill=(200,205,215),width=2);d.text((X-10,y1+10),p['w'].strip('.,'),font=fn,fill=(200,205,215))
    d.text((x0,8),'Movimiento real medido en el render (píxeles que cambian entre cuadros consecutivos)',font=ImageFont.truetype('/home/claude/escena/Poppins-Bold.ttf',20),fill=(255,255,255))
    C.save(out,quality=92)
