import json,sys,statistics as st,collections
for d in ['mdm1','mdm2','rab1','rab2','dog1','caf1']:
    D=json.load(open(f'{d}/datos.json')); T=D['T']; e=D['escenas'][0]
    tt=lambda k: float(k) if isinstance(k,(int,float)) else T.get(k)
    FIN=min(max(f['b'] for f in D['frases']), T.get('s_end',1e9))
    pans=sorted([p for p in e['pan'] if tt(p['k']) is not None], key=lambda p: tt(p['k']))
    zset={z['x0']+537:z.get('set') for z in e['zonas']}
    def cam(t):
        x=0
        for p in pans:
            if tt(p['k'])<=t: x=p['x']
        return x
    desl={round(tt(p['k']),2) for p in pans if not p.get('corte')}
    cortes=sorted({round(tt(p['k']),2) for p in pans}|{round(tt(z['k']),2) for z in e['zoom'] if z.get('dur',1)<=0.02 and tt(z['k']) is not None})
    cortes=[c for c in cortes if 0<=c<FIN]
    pl=[]
    for a,b in zip(cortes,cortes[1:]+[FIN]):
        if b-a<0.3: continue
        x=cam(a+0.01)
        if pl and x>=99000 and pl[-1][2]==x: pl[-1]=(pl[-1][0],b,x); continue
        pl.append((a,b,x))
    L=[b-a for a,b,x in pl]; Lset=[b-a for a,b,x in pl if x<99000]
    fuera=sum(b-a for a,b,x in pl if x>=99000)
    ins=[zset.get(x) for a,b,x in pl if x>=99000]
    ci=collections.Counter(ins)
    # tramos (sets en escenario) en orden
    seq=[]
    for p in pans:
        if p['x']<99000:
            s=next((z.get('set') for z in e['zonas'] if z['x0']<p['x']<z['x1'] and z['x0']<99000),None)
            if not seq or seq[-1]!=s: seq.append(s)
    cs=collections.Counter(seq)
    p30=sum(1 for a,b,x in pl if a<30)
    print(f"\n== {d}  dur {FIN/60:.1f} min  planos {len(pl)}  por min {len(pl)/FIN*60:.1f}")
    print(f"   plano: media {st.mean(L):.1f}s mediana {st.median(L):.1f}s p90 {sorted(L)[int(len(L)*.9)]:.1f}s max {max(L):.1f}s | en set: media {st.mean(Lset):.1f}s, >4.5s: {sum(1 for l in Lset if l>4.5)} ({sum(l for l in Lset if l>4.5)/FIN*100:.0f}% del tiempo), >8s: {sum(1 for l in Lset if l>8)}")
    print(f"   fuera del set {fuera/FIN*100:.0f}%  insertos {len(ins)} ({len(ci)} distintos) rep: {[(k,v) for k,v in ci.items() if v>1]}")
    print(f"   espacios distintos {len(cs)}  visitas {len(seq)}  regresos {len(seq)-len(cs)}  {dict(cs)}")
    print(f"   planos en primeros 30 s: {p30}; primer plano dura {pl[0][1]-pl[0][0]:.1f}s ({'inserto '+str(zset.get(pl[0][2])) if pl[0][2]>=99000 else 'set'})")
    print(f"   numeros {len(e.get('numeros',[]))} titulos {len(e.get('titulos',[]))} chips {len(e.get('chips',[]))} props {len(e.get('props',[]))} actores {len(e.get('actores',[]))} burbujas {len(e.get('burbujas',[]))} sfx {len(D.get('sfx',[]) or e.get('sfx',[]))}")
    print('   frase keys', list(D['frases'][0].keys()), len(D['frases']))
