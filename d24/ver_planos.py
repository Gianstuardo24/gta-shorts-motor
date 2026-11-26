#!/usr/bin/env python3
# uso: ver_planos.py SLOT -> /tmp/pl_SLOT.jpg : un cuadro por plano, con su tipo
import subprocess,re,sys
S=sys.argv[1]; log=open(f'/home/claude/d24/{S}/planos.log').read().strip().split('\n'); fs=[]
for i,l in enumerate(log):
    m=re.match(r'\s*([\d.]+)-\s*([\d.]+)\s+(\w+)',l); a,b,tp=float(m[1]),float(m[2]),m[3]; f=f'/tmp/pl_{S}_{i}.jpg'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(a+min(1.0,(b-a)*0.65)),'-i',f'/home/claude/d24/{S}/v1.mp4','-frames:v','1','-vf',f"scale=216:-2,drawtext=text='{tp}':x=6:y=h-26:fontsize=20:fontcolor=yellow:box=1:boxcolor=black@0.7",f]); fs.append(f)
def fila(xs,out): subprocess.run(['ffmpeg','-y','-loglevel','error']+sum([['-i',f] for f in xs],[])+['-filter_complex',f'hstack={len(xs)}',out])
filas=[]
for j in range(0,len(fs),8):
    xs=fs[j:j+8]; xs=xs+[xs[-1]]*(8-len(xs)); o=f'/tmp/pl_{S}_f{j}.jpg'; fila(xs,o); filas.append(o)
if len(filas)==1: subprocess.run(['cp',filas[0],f'/tmp/pl_{S}.jpg'])
else: subprocess.run(['ffmpeg','-y','-loglevel','error']+sum([['-i',f] for f in filas],[])+['-filter_complex',f'vstack={len(filas)}',f'/tmp/pl_{S}.jpg'])
