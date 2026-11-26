import sys,json,re,numpy as np
sys.path.insert(0,'/home/claude/calib'); from cambios import bloques
def perfil(mp4,vtt,cortes_json,ini,fin,huecos=()):
    g,loc,fps=bloques(mp4)
    m=np.ones(len(g),bool); m[:int(ini*fps)]=False; m[int(fin*fps):]=False
    for a,b in huecos: m[int(a*fps):int(b*fps)]=False
    dur=m.sum()/fps
    t=open(vtt,encoding='utf-8').read(); n=0
    for blk in re.split(r'\n\n+',t):
        mm=re.search(r'(\d\d):(\d\d):(\d\d\.\d+) --> ',blk)
        if not mm: continue
        t0=int(mm[1])*3600+int(mm[2])*60+float(mm[3])
        for line in blk.split('\n')[1:]:
            if '<c>' not in line: continue
            ts=[t0]+[int(x[0])*3600+int(x[1])*60+float(x[2]) for x in re.findall(r'<(\d\d):(\d\d):(\d\d\.\d+)><c>',line)]
            n+=sum(1 for x in ts if x<len(m)/fps and m[min(int(x*fps),len(m)-1)])
    c=[x for x in json.load(open(cortes_json))['tiempos'] if x<len(m)/fps and m[min(int(x*fps),len(m)-1)]]
    ev=0;ult=-99
    x=(loc>12)&(g<8)&m
    for i,v in enumerate(x):
        if v and i-ult>=fps: ev+=1
        if v: ult=i
    # rachas sin ningún cambio en pantalla
    q=(loc<3)&m; r=[];k=0
    for v,mk in zip(q,m):
        if v and mk: k+=1
        else:
            if k: r.append(k/fps)
            k=0
    r=np.array(r+[0])
    return dict(seg=round(dur),ppm=round(n*60/dur),cortes_min=round(len(c)*60/dur,1),cambios_locales_min=round(ev*60/dur,1),
                sin_ningun_cambio=round(float(q.sum()/m.sum()),2),racha_quieta_max=round(float(r.max()),1),en_rachas_de_5s_o_mas=round(float(r[r>=5].sum()/dur),2))
if __name__=='__main__':
    V='/mnt/user-data/uploads/gta-shorts/estudio_faceless/'
    P={'1 Company Man':('P2V-vFct8FY',24,675,()),'2 toldinstone':('qJIDOq0ezTs',10,666,((343,415),)),'3 Kurzgesagt':('zozEm4f_dlw',0,9999,())}
    out={}
    for k,(vid,a,b,h) in P.items():
        out[k]=perfil(V+f'videos/{vid}.mp4',V+f'videos/{vid}.en-orig.vtt',V+f'analisis/{vid}/cortes.json',a,b,h); print(k,out[k])
    json.dump(out,open('/home/claude/calib/perfiles.json','w'),ensure_ascii=False,indent=1)
