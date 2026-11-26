import subprocess,sys,json,numpy as np
def serie(v,fps=5,w=160,h=90):
    p=subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',v,'-vf',f'fps={fps},scale={w}:{h},format=gray','-f','rawvideo','-'],capture_output=True)
    a=np.frombuffer(p.stdout,dtype=np.uint8).reshape(-1,h,w).astype(np.int16)
    d=np.abs(a[1:]-a[:-1]).mean(axis=(1,2))            # cambio medio por píxel entre cuadros (0-255)
    return d,fps
if __name__=='__main__':
    v,ini,fin,out=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
    d,fps=serie(v); d=d[int(ini*fps):int(fin*fps)]
    np.save(out,d)
    q=np.percentile(d,[10,25,50,75,90,99]); print('percentiles 10/25/50/75/90/99:',[round(float(x),2) for x in q])
    for th in (0.15,0.3,0.6): print(f'  cuadros casi quietos (<{th}):',f'{(d<th).mean():.0%}')
    # rachas quietas: segundos seguidos sin movimiento apreciable (<0.3), ignorando cortes
    th=0.3; r=[];c=0
    for x in d:
        if x<th: c+=1
        else:
            if c: r.append(c/fps)
            c=0
    if c: r.append(c/fps)
    r=np.array(r); print('  rachas quietas:',len(r),'· más larga',round(float(r.max()),1),'s · suman en rachas de 3 s o más:',round(float(r[r>=3].sum())),'s de',round(len(d)/fps),'s',f'({r[r>=3].sum()/(len(d)/fps):.0%})')
