"""EVALUADOR v0 (24-nov-2026) — perfil MEDIDO de un video a partir de: mp4 (360p), subtítulos .vtt con tiempo por palabra,
info.json y cortes.json del laboratorio. No interpreta: cuenta y mide. Uso: python3 evaluador.py <id> [<id> ...]"""
import subprocess,sys,json,re,glob,os,numpy as np
BASE='/mnt/user-data/uploads/gta-shorts/estudio_faceless/'
def movimiento(mp4,fps=5,w=160,h=90,b=10):
    p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-i',mp4,'-vf',f'fps={fps},scale={w}:{h},format=gray','-f','rawvideo','-'],stdout=subprocess.PIPE)
    g=[];loc=[];prev=None;n=w*h
    while True:
        buf=p.stdout.read(n)
        if len(buf)<n: break
        f=np.frombuffer(buf,dtype=np.uint8).reshape(h,w).astype(np.int16)
        if prev is not None:
            d=np.abs(f-prev); g.append(d.mean()); loc.append(d.reshape(h//b,b,w//b,b).mean(axis=(1,3)).max())
        prev=f
    return np.array(g),np.array(loc),fps
def palabras(vtt):
    t=open(vtt,encoding='utf-8').read(); ws=[]
    for blk in re.split(r'\n\n+',t):
        m=re.search(r'(\d\d):(\d\d):(\d\d\.\d+) --> ',blk)
        if not m: continue
        t0=int(m[1])*3600+int(m[2])*60+float(m[3])
        for line in blk.split('\n')[1:]:
            if '<c>' not in line: continue
            a=re.match(r'^([^<]+)',line)
            if a and a[1].strip(): ws.append((t0,a[1].strip()))
            for mm in re.finditer(r'<(\d\d):(\d\d):(\d\d\.\d+)><c>([^<]*)</c>',line):
                if mm[4].strip(): ws.append((int(mm[1])*3600+int(mm[2])*60+float(mm[3]),mm[4].strip()))
    return [(t,w.replace('&gt;','').replace('&amp;','&').strip()) for t,w in ws if w.replace('&gt;','').strip()]
def silabas(w):
    w=re.sub(r'[^a-z]','',w.lower())
    if not w: return 0
    n=len(re.findall(r'[aeiouy]+',w))
    if w.endswith('e') and not w.endswith(('le','ee')) and n>1: n-=1
    return max(n,1)
def frases(ws):
    out=[];cur=[]
    for t,w in ws:
        cur.append((t,w))
        if re.search(r'[.?!]["\')]*$',w): out.append(cur);cur=[]
    if cur: out.append(cur)
    return out
CONTR=re.compile(r"\b\w+(?:'|’)(?:s|t|re|ve|ll|d|m)\b",re.I)
def lenguaje(ws):
    toks=[re.sub(r"[^\w'’%$-]","",w) for _,w in ws]; toks=[x for x in toks if x]; low=[x.lower().replace('’',"'") for x in toks]; N=len(toks)
    fr=frases(ws); nf=len(fr); per=lambda c:round(100*c/N,2)
    tu=sum(1 for x in low if x in("you","your","you're","yours","you've","you'll","you'd","yourself"))
    yo=sum(1 for x in low if x in("i","i'm","i've","i'll","i'd","my","me","we","we're","we've","our","us"))
    con=sum(1 for x in low if CONTR.search(x))
    num=sum(1 for x in toks if re.search(r'\d',x))
    alfa=[re.sub(r'[^a-z]','',x) for x in low]; alfa=[x for x in alfa if x]
    largo=sum(len(x) for x in alfa)/len(alfa); largas=sum(1 for x in alfa if len(x)>=8)/len(alfa)
    V=100; mattr=np.mean([len(set(alfa[i:i+V]))/V for i in range(0,max(1,len(alfa)-V),10)])
    sil=sum(silabas(x) for x in alfa); flesch=206.835-1.015*(N/nf)-84.6*(sil/len(alfa))
    reg='informal' if (per(con)>=2.0 and per(tu)>=1.5) else ('formal' if (per(con)<0.6 and largas>=0.16) else 'neutro')
    return dict(palabras=N,frases=nf,frase_media=round(N/nf,1),preguntas_100f=round(100*sum(1 for f in fr if f[-1][1].rstrip('"\')').endswith('?'))/nf,1),
                tu_100=per(tu),yo_100=per(yo),contracciones_100=per(con),numeros_100=per(num),largo_palabra=round(largo,2),palabras_largas=round(100*largas,1),
                variedad=round(float(mattr),3),flesch=round(flesch,1),registro=reg),fr
def evalua(vid):
    mp4=BASE+f'videos/{vid}.mp4'; vtts=sorted(glob.glob(BASE+f'videos/{vid}.*-orig.vtt')); vtt=vtts[0]; idi=os.path.basename(vtt).split('.')[-2].split('-')[0]
    info=json.load(open(BASE+f'analisis/{vid}/info.json')); cortes=json.load(open(BASE+f'analisis/{vid}/cortes.json')).get('tiempos',[])
    ws=palabras(vtt); cache=f'/home/claude/calib/micro/{vid}_mov.npz'
    if os.path.exists(cache): z=np.load(cache); g,loc,fps=z['g'],z['loc'],5
    else: g,loc,fps=movimiento(mp4); np.savez_compressed(cache,g=g,loc=loc)
    dur=len(g)/fps
    r=dict(id=vid,titulo=info.get('titulo'),canal=info.get('canal'),subs=info.get('subs_canal'),vistas=info.get('vistas'),fecha=info.get('fecha'),dur_min=round(dur/60,1),idioma=idi)
    r['xN']=round(r['vistas']/r['subs'],1) if r['subs'] else None
    # voz
    t0,t1=ws[0][0],ws[-1][0]; gaps=[ws[i+1][0]-ws[i][0] for i in range(len(ws)-1)]
    r['voz']=dict(ppm=round(len(ws)*60/(t1-t0)),ppm_primeros_30s=round(sum(1 for t,_ in ws if t<t0+30)*2),pausas_min=round(sum(1 for x in gaps if x>1.2)*60/(t1-t0),1))
    # imagen
    lim=[0]+[c for c in cortes if c<dur]+[dur]; pl=np.diff(lim)
    q=loc<3; rr=[];k=0
    for v in q:
        if v:k+=1
        else:
            if k: rr.append(k/fps)
            k=0
    if k: rr.append(k/fps)
    rr=np.array(rr+[0]); x=(loc>12)&(g<8); ev=0;ult=-99
    for i,v in enumerate(x):
        if v and i-ult>=fps: ev+=1
        if v: ult=i
    r['imagen']=dict(cortes_min=round(len(cortes)*60/dur,1),plano_mediano=round(float(np.median(pl)),1),plano_max=round(float(pl.max()),1),
                     sin_cambio=round(100*float(q.mean())),cambios_locales_min=round(ev*60/dur,1),racha_quieta_max=round(float(rr.max()),1),en_rachas_5s=round(100*float(rr[rr>=5].sum()/dur)))
    r['gancho']=dict(cortes_30s=sum(1 for c in cortes if c<t0+30),seg_primer_corte=round(min([c for c in cortes if c>t0]+[dur])-t0,1),sin_cambio_30s=round(100*float(q[int(t0*fps):int((t0+30)*fps)].mean())))
    if idi=='en':
        L,fr=lenguaje(ws); r['lenguaje']=L
        f0=fr[0]; txt=' '.join(w for _,w in f0).lower()
        r['gancho'].update(primera_frase_palabras=len(f0),primera_pregunta=txt.rstrip('"\')').endswith('?'),primera_con_numero=bool(re.search(r'\d',txt)),primera_con_tu=bool(re.search(r"\byou(r|'re)?\b",txt)))
        # sincronía imagen–frase: ¿cambia algo en pantalla mientras dura cada frase?
        cam=(loc>12); ok=0
        for f in fr:
            a,b=int(f[0][0]*fps),int(min(f[-1][0]+0.6,dur)*fps)+1
            if cam[a:b].any(): ok+=1
        ini=np.array([f[0][0] for f in fr]); cerca=sum(1 for c in cortes if np.abs(ini-c).min()<=1.0)
        r['sincronia']=dict(frases_con_cambio_visual=round(100*ok/len(fr)),cortes_junto_a_inicio_de_frase=round(100*cerca/len(cortes)) if cortes else None)
        json.dump([[round(f[0][0],1),round(f[-1][0],1),' '.join(w for _,w in f)] for f in fr],open(f'/home/claude/calib/micro/{vid}_frases.json','w'))
    return r
if __name__=='__main__':
    for vid in sys.argv[1:]:
        try:
            r=evalua(vid); json.dump(r,open(f'/home/claude/calib/micro/{vid}.json','w'),ensure_ascii=False,indent=1,default=lambda o:o.item() if hasattr(o,'item') else str(o))
            print('OK',vid,r['dur_min'],'min ·',r['canal'],'·',(r['titulo'] or '')[:60],'· xN',r['xN'],flush=True)
        except Exception as e: print('ERROR',vid,repr(e)[:200],flush=True)
