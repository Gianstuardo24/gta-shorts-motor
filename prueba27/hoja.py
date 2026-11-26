"""hoja.py CARPETA SALIDA ESCENA_HTML DATOS t1 t2 ... -> cuadros PNG + hoja de 9 cuadros"""
import sys,subprocess,glob
from PIL import Image
d,out,html,datos=sys.argv[1:5];ts=sys.argv[5:]
subprocess.run(['mkdir','-p',d]);subprocess.run(['python3','/home/claude/prueba27/cuadros.py',html,datos,d+'/f']+ts,check=True,stdout=subprocess.DEVNULL)
fs=[f"{d}/f_{float(t):06.2f}.png" for t in ts];ims=[Image.open(f).convert('RGB').resize((270,480)) for f in fs]
W=Image.new('RGB',(274*len(ims)-4,480),'white')
for i,im in enumerate(ims):W.paste(im,(i*274,0))
W.save(out,quality=88);print(out)
