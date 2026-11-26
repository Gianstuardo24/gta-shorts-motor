# Revisa que ningun inserto vuelva a otra escena ni deje un pedazo corto antes del cambio de tramo. Uso: python3 revisar_insertos.py datos.json ...
import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f)); T=d['T']; e=d['escenas'][0]
    tt=lambda k: k if isinstance(k,(int,float)) else T.get(k)
    P=sorted([p for p in e['pan'] if tt(p['k']) is not None],key=lambda p: tt(p['k']))
    home=None; mal=[]
    for i,p in enumerate(P):
        t=tt(p['k'])
        if p['x']>=99000: 
            # insert start: next non-insert pan should return to the same zone as the last scene pan before it
            prev=[q for q in P[:i] if q['x']<99000]
            nxt=[q for q in P[i+1:] if q['x']<99000]
            if prev and nxt and nxt[0]['x']!=prev[-1]['x'] and nxt[0].get('corte'):
                # return goes to a different scene than where we left, check if a later pan within 2s moves again
                later=[q for q in P[i+1:] if q['x']<99000 and tt(q['k'])<tt(nxt[0]['k'])+0.01]
                mal.append((round(t,1),prev[-1]['x'],nxt[0]['x']))
            # also: a scene pan BEFORE the return that is not corte (tramo change) while inside insert
            if prev and nxt:
                if len(nxt)>1 and nxt[0]['x']!=nxt[1]['x'] and tt(nxt[1]['k'])-tt(nxt[0]['k'])<2.5:
                    mal.append(('salta',round(t,1),round(tt(nxt[0]['k']),1),nxt[0]['x'],round(tt(nxt[1]['k']),1),nxt[1]['x']))
    print(f.split('/')[-2], mal)
