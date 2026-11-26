"""Prueba 27 · mide en el render la POSICIÓN real del cursor en cada cuadro (todo lo demás está quieto):
fondo sin cursor = primer cuadro donde el cursor está al final y último cuadro donde el cursor está al inicio.
Uso: medir_cursor.py video.mp4 [grafico.jpg palabras.json]"""
import sys, json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
f=sys.argv[1];W,H=1080,1920
p=subprocess.Popen(['ffmpeg','-loglevel','error','-i',f,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
fr=[];b=p.stdout.read(W*H*3)
while b:
    x=np.frombuffer(b,np.uint8).reshape(H,W,3)[::2,::2].astype(np.int16).copy();x[:205]=0   # se ignora la franja del subtítulo (y<410): cambia de color con cada palabra
    fr.append(x);b=p.stdout.read(W*H*3)
a0,a1=fr[0],fr[-1];dd=np.abs(a0-a1).sum(2)>40;ys,xs=np.where(dd)
# separar la región del cursor inicial (abajo a la izquierda) de la final (arriba a la derecha)
fin_m=(xs>270);fondo=a1.copy();yy,xx=ys[fin_m],xs[fin_m];fondo[yy,xx]=a0[yy,xx]
P=[]
for a in fr:
    m=np.abs(a-fondo).sum(2)>40;yy,xx=np.where(m)
    P.append((xx.mean()*2,yy.mean()*2) if len(xx)>30 else (np.nan,np.nan))
P=np.array(P);t=np.arange(len(P))/30;V=np.r_[0,np.hypot(*np.diff(P,axis=0).T)*30]
V=np.nan_to_num(V);ok=~np.isnan(P[:,0])
mov=V>15;idx=np.where(mov)[0];i0,i1=idx[0],idx[-1];pk=int(np.argmax(V))
paradas=[i for i in range(i0,i1+1) if V[i]<=15 and any(V[j]>60 for j in range(i+1,i1+1))]   # parada seguida de un rearranque real (no el ruido del final lento)
# monotonía: después del pico la velocidad no vuelve a subir más de un 12 % (ruido de compresión/centroide)
rebotes=[round(t[i],2) for i in range(pk+1,i1) if V[i+1]>V[i]*1.12+20]
print(f'cursor medido en {int(ok.sum())}/{len(P)} cuadros · se mueve de {t[i0]:.2f} a {t[i1]:.2f} s · detenciones intermedias: {len(paradas)}')
print(f'velocidad pico: {V[pk]:.0f} px/s en {t[pk]:.2f} s · tras el pico, rebotes de velocidad: {rebotes if rebotes else "ninguno"} · quieto después de {t[i1]:.2f} s')
print(f'tiempo por debajo de 200 px/s antes de detenerse: {sum(1 for i in range(pk,i1+1) if V[i]<200)/30:.2f} s · posición final medida: ({P[-1,0]:.0f}, {P[-1,1]:.0f})')
if len(sys.argv)>2:
    Wc,Hc=1200,440;C=Image.new('RGB',(Wc,Hc),(16,17,22));d=ImageDraw.Draw(C);x0,y0,x1,y1=60,44,Wc-20,Hc-80
    fn=ImageFont.truetype('/home/claude/escena/Poppins-Regular.ttf',18);fb=ImageFont.truetype('/home/claude/escena/Poppins-Bold.ttf',20)
    d.line([(x0,y1),(x1,y1)],fill=(120,120,130),width=2);d.line([(x0+(x1-x0)*ti/t[-1],y1-(y1-y0)*v/max(V.max(),1)) for ti,v in zip(t,V)],fill=(255,200,70),width=4)
    pal=json.load(open(sys.argv[3]))
    for q in pal:
        X=x0+(x1-x0)*q['i']/t[-1];d.line([(X,y0),(X,y1)],fill=(60,66,84),width=1);d.text((X+2,y1+10),q['w'].strip('.,'),font=fn,fill=(200,205,215))
    X=x0+(x1-x0)*t[i1]/t[-1];d.text((X-30,y1+42),f'se detiene {t[i1]:.2f} s',font=fb,fill=(0,255,120))
    d.text((x0,10),f'Velocidad REAL del cursor medida en el render (pico {V[pk]:.0f} px/s)',font=fb,fill=(255,255,255));C.save(sys.argv[2],quality=92)
