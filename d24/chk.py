import json,glob,sys,re
def t(k,T):
    if isinstance(k,(int,float)): return float(k)
    m=re.match(r'^([A-Za-z_0-9]+)([+-][0-9.]+)?$',str(k))
    if not m: return None
    b=m.group(1); o=float(m.group(2) or 0)
    if b in T: return T[b]+o
    try: return float(b)+o
    except: return None
for d in sorted(sys.argv[1:] or [x.split('/')[0] for x in glob.glob('*/datos.json')]):
    try:
        src=json.load(open(glob.glob(d+'/*_src.json')[0])); T=json.load(open(d+'/datos.json'))['T']
    except Exception as e: print(d,'sin datos'); continue
    e=src['escena']['escenas'][0]; pans=sorted([(t(p['k'],T),p['x']) for p in e['pan']])
    ins=[]
    for i,(tt,x) in enumerate(pans):
        if x>=100000:
            fin=pans[i+1][0] if i+1<len(pans) else 999
            ins.append((tt,fin))
    out=[]
    for z in e.get('zoom',[]):
        tz=t(z['k'],T)
        if 'x' in z and z['x']<100000:
            for a,b in ins:
                if a-0.05<=tz<b-0.05: out.append(f"zoom {z['k']} dentro de inserto {a:.1f}-{b:.1f}")
    # actores fuera de cuadro
    def cam(tt):
        c=0
        for a,x in pans:
            if a<=tt+0.01: c=x
        return c
    for i,a in enumerate(e['actores']):
        for k in a['keys']:
            tk=t(k['k'],T); c=cam(tk+0.3)
            if c<100000 and not (c+140<=k['x']<=c+940) and k.get('pose')!='camina': out.append(f"actor{i} x={k['x']} fuera (cam {c}) en {k['k']}")
    # escenas repetidas dentro del video (Tao, 24-nov: no repetir escenas) y caminatas mal escritas
    vistos={}
    for z in e['zonas']:
        if z['x0']>=99000 and z.get('set')=='vitrinaV': continue
        kk=(z.get('set'),json.dumps(z.get('o'),sort_keys=True))
        vistos[kk]=vistos.get(kk,0)+1
    for (st,o),n in vistos.items():
        if n>1: out.append(f"escena repetida {st} x{n}")
    for i,a in enumerate(e['actores']):
        for k in a['keys']:
            if k.get('pose')=='camina' and 'a' not in k: out.append(f"actor{i}: 'camina' sin destino (usar a:[x,y]+dur)")
    print(d, 'OK' if not out else ' | '.join(out))
