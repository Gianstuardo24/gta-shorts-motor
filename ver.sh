#!/bin/bash
# uso: ver.sh DIR "0+2 s_lab+2 s_big+1.5 ..."  -> /tmp/ver_DIR.png  (usa los sets ya puestos en datos.json)
D=/home/claude/d23/$1
TS=$(python3 -c "
import json,sys;T=json.load(open('$D/datos.json'))['T'];T['0']=0
out=[]
for x in '''$2'''.split():
    k,_,o=x.partition('+');out.append(str(round(T.get(k,0)+float(o or 0),2)))
print(','.join(out))")
TIEMPOS=$TS python3 /home/claude/probar_sets.py $D/datos.json /tmp/ver_$1.png 2>&1 | tail -2
