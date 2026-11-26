import subprocess,sys,json,numpy as np
def bloques(v,fps=5,w=160,h=90,b=10):
    p=subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',v,'-vf',f'fps={fps},scale={w}:{h},format=gray','-f','rawvideo','-'],capture_output=True)
    a=np.frombuffer(p.stdout,dtype=np.uint8).reshape(-1,h,w).astype(np.int16)
    d=np.abs(a[1:]-a[:-1])                                   # cambio por píxel
    g=d.mean(axis=(1,2))                                      # global
    bl=d.reshape(d.shape[0],h//b,b,w//b,b).mean(axis=(2,4))   # por bloque de 10x10
    loc=bl.max(axis=(1,2))                                    # el bloque que más cambia
    return g,loc,fps
def eventos(g,loc,fps,A,B):
    # cambio LOCAL: algo aparece o se mueve en una zona (bloque > 12) sin ser un corte (global < 8)
    x=(loc[int(A*fps):int(B*fps)]>12)&(g[int(A*fps):int(B*fps)]<8); n=0;ult=-99
    for i,v in enumerate(x):
        if v and i-ult>=fps: n+=1          # separa eventos por 1 s o más
        if v: ult=i
    return n
if __name__=='__main__':
    v,tr=sys.argv[1],json.load(open(sys.argv[2])); s=lambda x:int(x.split(':')[0])*60+int(x.split(':')[1])
    g,loc,fps=bloques(v); tot=0;dur=0
    for t in tr:
        A,B=s(t['ini']),s(t['fin']); t['cambios_locales']=eventos(g,loc,fps,A,B); t['cambios_min']=round(t['cambios_locales']*60/(B-A),1)
        t['seg_sin_nada']=round(float(((loc[A*fps:B*fps]<3)).mean()),2)   # fracción del tiempo sin NINGÚN cambio en ninguna zona
        tot+=t['cambios_locales']; dur+=B-A
    json.dump(tr,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
    sn=np.concatenate([loc[s(t['ini'])*fps:s(t['fin'])*fps] for t in tr])
    print(f'cambios locales: {tot} en {dur} s = {tot*60/dur:.1f} por minuto · tiempo sin ningún cambio en pantalla: {(sn<3).mean():.0%}')
    for t in tr: print(f"  {t['n']:>2} {t['ini']}-{t['fin']}  cambios {t['cambios_locales']:>2} ({t['cambios_min']:>4}/min) · sin nada {t['seg_sin_nada']:.0%}")
