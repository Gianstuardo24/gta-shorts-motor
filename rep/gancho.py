"""Tapa el texto-gancho viejo de un reel de Repers con una tarjeta nueva (gancho Wii/Kinect).
uso: gancho.py entrada.mp4 salida.mp4 "texto" x0 y0 x1 y1 t_fin"""
import sys, subprocess, re
from PIL import Image, ImageDraw, ImageFont
src,dst,texto=sys.argv[1:4]; x0,y0,x1,y1=map(int,sys.argv[4:8]); tfin=float(sys.argv[8]); tini=float(sys.argv[9]) if len(sys.argv)>9 else 0.0
F=ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf",72,layout_engine=ImageFont.Layout.RAQM)
E=ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",109,layout_engine=ImageFont.Layout.RAQM)
# separa emoji final
m=re.search(r"\s*([\U0001F000-\U0001FAFF☀-➿][\U0001F000-\U0001FAFF☀-➿‍️]*)\s*$",texto)
emo=m.group(1) if m else ""; txt=texto[:m.start()] if m else texto
EM=int(72*1.15)
def emoji_img(s):
    im=Image.new("RGBA",(400,200),(0,0,0,0))
    ImageDraw.Draw(im).text((0,0),s,font=E,embedded_color=True); im=im.crop(im.getbbox()); return im.resize((EM,int(EM*im.height/im.width)),Image.LANCZOS)
ei=emoji_img(emo) if emo else None
lines=[]
for parte in txt.split("|"):
    cur=""
    for w in parte.split():
        p=(cur+" "+w).strip()
        if F.getlength(p)>840 and cur: lines.append(cur); cur=w
        else: cur=p
    lines.append(cur)
LH=int(72*1.32); widths=[F.getlength(l) for l in lines]
if ei: widths[-1]+=EM+16
tw=max(widths); th=LH*len(lines)
padx,pady=40,30
cw=max(int(tw)+2*padx, (x1-x0)+24); ch=max(th+2*pady, (y1-y0)+24)
cx=540; cy=(y0+y1)//2
X0=int(cx-cw/2); Y0=int(cy-ch/2)
# no salirse de la pantalla
X0=max(20,min(X0,1080-20-cw)); 
card=Image.new("RGBA",(cw,ch),(0,0,0,0)); d=ImageDraw.Draw(card)
d.rounded_rectangle((0,0,cw-1,ch-1),radius=28,fill=(0,0,0,255))
ty=(ch-th)//2
for i,l in enumerate(lines):
    x=(cw-widths[i])/2; y=ty+i*LH
    d.text((x,y+LH*0.08),l,font=F,fill="white")
    if i==len(lines)-1 and ei: card.alpha_composite(ei,(int(x+F.getlength(l)+16),int(y+(LH-ei.height)/2)))
card.save(dst+".png")
assert X0<=x0 and Y0<=y0 and X0+cw>=x1 and Y0+ch>=y1, ("no cubre",X0,Y0,cw,ch)
subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-i",dst+".png","-filter_complex",f"[0:v][1:v]overlay={X0}:{Y0}:enable='between(t,{tini},{tfin})'[v]","-map","[v]","-map","0:a?","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-c:a","copy","-movflags","+faststart",dst],check=True)
print("ok",dst,(X0,Y0,cw,ch))
