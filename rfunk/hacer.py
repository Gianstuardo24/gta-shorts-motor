import sys, subprocess, numpy as np, json, pathlib, hashlib
sys.path.insert(0,'/home/claude/escena')
import musica; musica.CARPETA=pathlib.Path('/home/claude/escena/sonidos/musica')
import musica_funk as F
from scipy.signal import butter, sosfilt
import soundfile as sf
SR=musica.SR
BASE=pathlib.Path("/mnt/user-data/uploads/Desktop/Repers Shorts")
OUT=pathlib.Path("/home/claude/rfunk/out")
PEND=json.load(open('pend.json'))
def aud(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-ac','1','-ar','8000','-f','f32le','-'],capture_output=True);return np.frombuffer(r.stdout,np.float32)
def drop(x):
    h=400;e=np.sqrt(np.convolve(x**2,np.ones(h)/h,'same'))[::h];d=np.diff(np.convolve(e,np.ones(5)/5,'same'))
    return int(np.argmax(d[:int(10*8000/h)]))*h/8000
for rel in PEND:
    p=BASE/rel; x=aud(p); dur=len(x)/8000; d=drop(x)
    # variante por video: misma idea, distinta semilla (tono/patron/vamp)
    y,info=F.generar(dur+12, "repers-"+pathlib.Path(rel).stem[:3], bpm=112)
    compas=4*60/112
    if d<0.5:
        ini=compas; m=y[int(ini*SR):int((ini+dur)*SR)].copy()
    else:
        k=int(np.ceil(d/compas)); ini=k*compas-d
        m=y[int(ini*SR):int((ini+dur)*SR)].copy()
        nd=int(d*SR); sos=butter(4,700,'lowpass',fs=SR,output='sos'); filt=sosfilt(sos,m[:nd+SR])*0.7
        w=np.clip((np.arange(nd+SR)-(nd-int(.04*SR)))/(.04*SR),0,1)
        m[:nd+SR]=filt*(1-w)+m[:nd+SR]*w
    nf=int(min(1.0,dur/6)*SR); m[-nf:]*=np.linspace(1,0,nf)
    sf.write(OUT/'tmp.wav',m,SR)
    dest=OUT/rel; dest.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run(['ffmpeg','-y','-v','error','-i',str(p),'-i',str(OUT/'tmp.wav'),'-map','0:v','-map','1:a','-c:v','copy','-af','loudnorm=I=-14:TP=-1.5:LRA=11','-ar','48000','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',str(dest)],check=True)
    print(f"{rel[:45]:46s} dur={dur:.1f} drop={d:.2f} {info['tono']}")
