import json,sys,collections
a=json.load(open(sys.argv[1]))['codigos']; b=json.load(open(sys.argv[2]))['codigos']
DIMS=['funcion','enigma','saber','apunta','img_rel','img_tipo']
ns=sorted(a,key=int); res={}
for d in DIMS:
    x=[a[n][d] for n in ns]; y=[b[n][d] for n in ns]; N=len(ns)
    po=sum(1 for i in range(N) if x[i]==y[i])/N
    cats=set(x)|set(y); pe=sum((x.count(c)/N)*(y.count(c)/N) for c in cats)
    kappa=(po-pe)/(1-pe) if pe<1 else float('nan')
    por={}
    for c in sorted(cats):
        usa=[i for i in range(N) if x[i]==c or y[i]==c]; amb=[i for i in usa if x[i]==c and y[i]==c]
        por[c]=(len(amb),len(usa),x.count(c),y.count(c))
    conf=collections.Counter((x[i],y[i]) for i in range(N) if x[i]!=y[i])
    res[d]=dict(acuerdo=round(po,2),azar=round(pe,2),kappa=round(kappa,2),por_codigo=por,confusiones=conf.most_common(6),desacuerdos=[ns[i] for i in range(N) if x[i]!=y[i]])
    print(f"\n== {d}: acuerdo {po:.0%} · esperado por azar {pe:.0%} · kappa {kappa:.2f}")
    for c,(am,us,ca,cb) in por.items(): print(f"   {c:20s} ambos {am} de {us} tramos donde alguno lo usó (pasada1 {ca}, pasada2 {cb})")
    print("   confusiones:",[(f"{p}→{q}",k) for (p,q),k in conf.most_common(6)]); print("   tramos en desacuerdo:",res[d]['desacuerdos'])
json.dump({d:{k:(v if k!='confusiones' else [[list(p),k2] for p,k2 in v]) for k,v in r.items()} for d,r in res.items()},open(sys.argv[3],'w'),ensure_ascii=False,indent=1,default=list)
