"""Pasa NUESTROS largos por el mismo evaluador. Primero los baja a 360p (como las referencias) para que las medidas sean comparables."""
import sys,json,re,subprocess,os,numpy as np
sys.path.insert(0,'/home/claude/evaluador'); import evaluador as E
L='/home/claude/largos/'; OUT='/home/claude/calib/propios/'
V={'mdm1':('mdm1/mdm_final_23n_v2.mp4','Million Dollar Mistake','Pixar: The Worst Deal in Hollywood History'),'mdm2':('mdm2/mdm2_final.mp4','Million Dollar Mistake','MDM 2'),
   'rab1':('rab1/rab_final.mp4','The Rabbit Loop','Rabbit 1'),'rab2':('rab2/rab2_final.mp4','The Rabbit Loop','Rabbit 2'),'dog1':('dog1/dog_final.mp4','Dog Decoded','Dog 1'),'caf1':('caf1/caf1_final.mp4','Coffee But Why?','Coffee 1')}
for k,(f,canal,tit) in V.items():
    src=L+f; low=OUT+k+'_360.mp4'
    if not os.path.exists(low): subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',src,'-vf','scale=640:360','-r','30','-c:v','libx264','-preset','veryfast','-crf','26','-an',low])
    r=subprocess.run(['ffmpeg','-hide_banner','-i',low,'-filter:v',"select='gt(scene,0.30)',showinfo",'-an','-f','null','-'],capture_output=True,text=True)
    cortes=[round(float(x),1) for x in re.findall(r'pts_time:([\d.]+)',r.stderr)]
    ws=[(p['i'],p['w']) for p in json.load(open(L+f.split('/')[0]+'/vz_palabras.json'))]
    g,loc,fps=E.movimiento(low); dur=len(g)/fps
    t0,t1=ws[0][0],ws[-1][0]; gaps=[ws[i+1][0]-ws[i][0] for i in range(len(ws)-1)]
    R=dict(id=k,canal=canal,titulo=tit,dur_min=round(dur/60,1))
    R['voz']=dict(ppm=round(len(ws)*60/(t1-t0)),ppm_primeros_30s=round(sum(1 for t,_ in ws if t<t0+30)*2),pausas_min=round(sum(1 for x in gaps if x>1.2)*60/(t1-t0),1))
    lim=[0]+cortes+[dur]; pl=np.diff(lim); q=loc<3; rr=[];c=0
    for v in q:
        if v:c+=1
        else:
            if c: rr.append(c/fps)
            c=0
    if c: rr.append(c/fps)
    rr=np.array(rr+[0]); x=(loc>12)&(g<8); ev=0;ult=-99
    for i,v in enumerate(x):
        if v and i-ult>=fps: ev+=1
        if v: ult=i
    R['imagen']=dict(cortes_min=round(len(cortes)*60/dur,1),plano_mediano=round(float(np.median(pl)),1),plano_max=round(float(pl.max()),1),sin_cambio=round(100*float(q.mean())),
                     cambios_locales_min=round(ev*60/dur,1),racha_quieta_max=round(float(rr.max()),1),en_rachas_5s=round(100*float(rr[rr>=5].sum()/dur)))
    R['gancho']=dict(cortes_30s=sum(1 for c in cortes if c<t0+30),sin_cambio_30s=round(100*float(q[int(t0*fps):int((t0+30)*fps)].mean())))
    Lg,fr=E.lenguaje(ws); R['lenguaje']=Lg
    f0=' '.join(w for _,w in fr[0]).lower(); R['gancho'].update(primera_frase_palabras=len(fr[0]),primera_pregunta=f0.rstrip().endswith('?'),primera_con_numero=bool(re.search(r'\d',f0)),primera_con_tu=bool(re.search(r"\byou(r|'re)?\b",f0)))
    cam=(loc>12); ok=sum(1 for f in fr if cam[int(f[0][0]*fps):int(min(f[-1][0]+0.6,dur)*fps)+1].any())
    R['sincronia']=dict(frases_con_cambio_visual=round(100*ok/len(fr)))
    json.dump(R,open(OUT+k+'.json','w'),ensure_ascii=False,indent=1,default=lambda o:o.item() if hasattr(o,'item') else str(o))
    print('OK',k,R['dur_min'],'min',R['voz'],R['imagen'],flush=True)
