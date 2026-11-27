<script>
// ===== DC · MDM21 · INICIO ===== (MDM 21h · Blockbuster LOST Everything in ONE Decision · paquete 7 del lote del 27-nov)
// Reglas del paquete: sin rostros ni diálogos que no se narran; sin logos (no hay archivos): videoclub y pantalla genéricos; una decisión no explica sola toda la quiebra.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const PAPEL='#efe6d0',TINTA='#2a2019',MADERA='#6b4a2e',MADERA2='#553a23',CEO={manga:'#1c2533',puno:'#f1ede4'},FUND={manga:'#2a9d8f',puno:'#23867a'};
const COL=['#c0392b','#2a6f97','#e9c46a','#2a9d8f','#8e5aa8','#e76f51','#3d7ea6','#d9a441'];
function lineasGrises(x,y,w,n,alto,sem){X.fillStyle='rgba(42,32,25,.26)';for(let i=0;i<n;i++){rr(x,y+i*alto*1.9,w*(.72+rnd(i+sem)*.28),alto,alto/2);X.fill()}}
// estantes del videoclub: filas de cajas; lleno 1 = llenos y con luz, 0 = vacíos y apagados
function estantes(L,x0,x1,y0,filas,lleno,alto){for(let f=0;f<filas;f++){const y=y0+f*alto;X.fillStyle=lleno?'#3a2c22':'#222a32';X.fillRect(L+x0,y,x1-x0,alto-10);X.fillStyle=lleno?'#2a1f18':'#4a5560';X.fillRect(L+x0,y+alto-22,x1-x0,22);
  if(lleno>0)for(let x=x0+14,i=0;x<x1-70;x+=74,i++){const c=COL[(i*3+f*5+Math.floor(x/74))%COL.length],h=alto-50;X.fillStyle=c;X.fillRect(L+x,y+16,62,h);X.fillStyle='rgba(255,255,255,.22)';X.fillRect(L+x+8,y+26,46,h*.34);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L+x+8,y+16+h*.7,46,8)}
  else for(let x=x0+14,i=0;x<x1-150;x+=74,i++)if(rnd(i*7+f*13+5)<.05){X.fillStyle='#39434e';X.fillRect(L+x,y+alto-22-44,132,44);X.fillStyle='rgba(255,255,255,.08)';X.fillRect(L+x+10,y+alto-22-34,50,24)}}
 for(let x=x0+5;x<x1;x+=444){X.fillStyle=lleno?'#2a1f18':'#4a5560';X.fillRect(L+x,y0,8,filas*alto)}}
function tienda(L,lleno,t){X.fillStyle=lleno?'#1d3138':'#141b21';X.fillRect(L-2600,-1600,9000,6400);
 for(let i=-3;i<9;i++){X.fillStyle=lleno?'#fff4c9':'#39424b';rr(L+i*520+80,96,360,30,14);X.fill();if(lleno){X.fillStyle='rgba(255,244,201,.05)';X.beginPath();X.moveTo(L+i*520+80,126);X.lineTo(L+i*520+440,126);X.lineTo(L+i*520+640,1500);X.lineTo(L+i*520-120,1500);X.closePath();X.fill()}}
 estantes(L,-2600,6400,470,5,lleno,196);X.fillStyle=lleno?'#7a3b2e':'#1f242a';X.fillRect(L-2600,1450,9000,3000);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L-2600,1450,9000,14)}
// ---------- P01 · el VHS entra, sale, y en el frente brillante se refleja una tienda vacía ----------
function casete(x,y,s,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';rr(-232,-126,480,270,18);X.fill();rr(-240,-135,480,270,18);X.fillStyle='#15171b';X.fill();trazo(LIN,3);
 rr(-200,-110,400,96,10);X.fillStyle='#2f5d6b';X.fill();X.fillStyle='rgba(239,230,208,.5)';rr(-180,-92,300,16,8);X.fill();rr(-180,-62,220,16,8);X.fill();rr(-170,10,340,100,14);X.fillStyle='#2c3138';X.fill();[-90,90].forEach(v=>{X.fillStyle='#8e98a4';X.beginPath();X.arc(v,60,34,0,7);X.fill();X.fillStyle='#15171b';X.beginPath();X.arc(v,60,12,0,7);X.fill()});X.restore()}
function p01(L,t){const xl=T.x_lost,xa=T.x_and1,xb=T.x_but,fin=T.c02;
 const entra=eio(seg(t,.15,.85)),sale=eio(seg(t,xl+.5,xl+.95)),ref=eio(seg(t,xa+.2,xa+1.3)),z=eio(seg(t,xb,fin));
 // el empuje termina con el reflejo a escala 1: el corte al plano 02 es la misma tienda, llena y con luz
 const cm=t<xb?ruta(t,[[0,540,1000,1.06],[xa,540,1010,1.1],[xb,540,1300,1.45]]):[540,lerp(1300,1340,Math.min(1,z*1.6)),1.45*Math.pow(5.65/1.45,z)];
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{X.fillStyle='#12242a';X.fillRect(L-900,-900,2900,4200);X.fillStyle=MADERA;X.fillRect(L-900,1560,2900,2000);X.fillStyle='#8a6240';X.fillRect(L-900,1560,2900,18);
  const cy=lerp(lerp(560,900,entra),800,sale);X.save();X.beginPath();X.rect(L-400,-400,1900,1270);X.clip();casete(L+540,cy,1,0);X.restore();
  X.fillStyle='rgba(0,0,0,.3)';rr(L+52,872,1000,700,26);X.fill();rr(L+40,860,1000,700,26);X.fillStyle='#2a2f36';X.fill();trazo(LIN,3);X.fillStyle='#0c0e11';rr(L+260,890,560,60,12);X.fill();X.fillStyle='#3a4047';X.fillRect(L+40,980,1000,8);
  rr(L+90,1020,300,90,12);X.fillStyle='#0c0e11';X.fill();if((t*1.4)%1<.6){X.fillStyle='#7CFC8A';[130,180,250,300].forEach(v=>X.fillRect(L+v,1058,34,10));X.fillRect(L+226,1048,8,8);X.fillRect(L+226,1074,8,8)}
  [0,1,2,3].forEach(i=>{rr(L+600+i*104,1030,84,64,12);X.fillStyle='#454c55';X.fill();trazo(LIN,2)});X.fillStyle=sale>0&&sale<1?'#7CFC8A':'#3a4047';X.beginPath();X.arc(L+470,1064,14,0,7);X.fill();
  // el frente brillante: reflejo de una tienda vacía
  rr(L+90,1170,900,340,16);X.fillStyle='#0b0d10';X.fill();if(ref>0){X.save();rr(L+90,1170,900,340,16);X.clip();X.globalAlpha=ref*.94;X.translate(L+540,1340);X.scale(.177,.177);X.translate(-(L+540),-1000);tienda(L,0,t);X.restore();X.fillStyle=`rgba(255,255,255,${.04*ref})`;X.beginPath();X.moveTo(L+200,1170);X.lineTo(L+420,1170);X.lineTo(L+300,1510);X.lineTo(L+90,1510);X.closePath();X.fill()}
  X.strokeStyle='#454c55';X.lineWidth=4;rr(L+90,1170,900,340,16);X.stroke();
  const m=1-eio(seg(t,.8,1.3));if(m>0){const o=origen(L+700+(1-m)*500,cy-150-(1-m)*500,-1.1,1.3,-1,118,44);manoLado(o[0],o[1],-1.1,1.3,-1,{manga:'#3d4852',puno:'#3d4852',curl:[.2,.24,.28,.3],pulgar:.6})}})}
// ---------- P02 · el pasillo interminable; el contador llega a 9,000 tiendas ----------
function p02(L,t){const c=T.c02,xk=T.x_king,x9=T.x_9000,fin=T.c03,cx=540+2100*Math.pow(seg(t,c,fin+.3),1.25);
 cam(L,cx,1000,1,540,1000,()=>tienda(L,1,t));
 const en=back(seg(t,xk-.1,xk+.3)),fijo=t>=x9-.02;X.save();X.translate(L+540,760);X.scale(en,en);X.fillStyle='rgba(0,0,0,.35)';rr(-342,-170,700,360,26);X.fill();rr(-350,-180,700,360,26);X.fillStyle='#14181d';X.fill();trazo(LIN,3);
 txt('STORES',0,118,58,'#e9c46a',{w:600});
 if(fijo){const q=back(seg(t,x9-.02,x9+.25));X.save();X.translate(0,-30);X.scale(1,q);txt('9,000',0,0,190,'#fbf7ec',{w:660});X.restore()}
 else{[-225,-75,75,225].forEach((v,i)=>{rr(v-62,-128,124,190,12);X.fillStyle='#22272e';X.fill();X.fillStyle='rgba(251,247,236,.5)';const k=((t*9+i*.37)%1);X.fillRect(v-44,-110+k*150,88,14);X.fillRect(v-44,-110+((k+.5)%1)*150,88,14)})}
 X.restore()}
// ---------- P03 · una caja postal con un DVD: chico, y perdiendo plata ----------
function moneda(x,y,r){X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.arc(x+5,y+7,r,0,7);X.fill();X.fillStyle='#d4af37';X.beginPath();X.arc(x,y,r,0,7);X.fill();trazo(LIN,3);X.fillStyle='#e8c95a';X.beginPath();X.arc(x,y,r*.74,0,7);X.fill();X.strokeStyle='rgba(42,32,25,.5)';X.lineWidth=5;X.lineCap='round';X.beginPath();X.moveTo(x,y-r*.4);X.lineTo(x,y+r*.4);X.stroke()}
function p03(L,t){const c=T.c03,xs=T.x_small,xm=T.x_mailing,xl=T.x_losing,fin=T.c04;
 cam(L,540,1000,lerp(.86,1,eio(seg(t,c,xm))),540,1000,()=>{X.fillStyle='#12242a';X.fillRect(L-900,-900,2900,4200);X.fillStyle=MADERA;rr(L+140,620,800,820,30);X.fill();trazo(LIN,3);X.fillStyle='rgba(0,0,0,.07)';for(let i=0;i<6;i++)X.fillRect(L+140,700+i*130,800,8);
  // sobre postal (sin colores de marca) y el DVD que entra
  const mete=eio(seg(t,xm-.1,xm+.55));X.save();X.translate(L+470,1000);X.rotate(-.06);
  const dx=lerp(330,60,mete);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.arc(dx+8,10,150,0,7);X.fill();const g=X.createLinearGradient(dx-150,-150,dx+150,150);g.addColorStop(0,'#dfe6ee');g.addColorStop(.45,'#b9d8f0');g.addColorStop(.6,'#f0d9ee');g.addColorStop(1,'#cfd6de');X.fillStyle=g;X.beginPath();X.arc(dx,0,150,0,7);X.fill();trazo(LIN,3);X.fillStyle='#8e98a4';X.beginPath();X.arc(dx,0,44,0,7);X.fill();X.fillStyle=MADERA;X.beginPath();X.arc(dx,0,18,0,7);X.fill();
  X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-242,-172,380,360);X.fillStyle='#f4efe2';X.fillRect(-250,-180,380,360);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-250,-180,380,360);lineasGrises(-210,-20,220,3,18,6);X.fillStyle='#c98d8d';X.fillRect(30,-150,70,84);X.strokeStyle='rgba(42,32,25,.4)';X.strokeRect(30,-150,70,84);X.strokeStyle='rgba(42,32,25,.35)';X.lineWidth=4;[0,1,2].forEach(i=>{X.beginPath();for(let k=0;k<=5;k++)X.lineTo(-90+k*22,-136+i*16+Math.sin(k*2)*5);X.stroke()});X.restore();
  [0,1,2].forEach(i=>{const s=eio(seg(t,xl-.1+i*.28,xl+.45+i*.28));if(s<1)moneda(L+760+i*50+s*700,1290-i*70-s*160,46)})})}
// ---------- P04 · la mesa de la reunión: la carpeta con la oferta se desliza al centro ----------
function carpeta(x,y,s,rot,o){o=o||{};X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';rr(-232,-150,480,320,16);X.fill();rr(-240,-160,480,320,16);X.fillStyle='#c9a06a';X.fill();trazo(LIN,3);X.fillStyle='#b98a4e';rr(60,-190,160,50,12);X.fill();trazo(LIN,3);
 rr(-190,-104,380,208,10);X.fillStyle=PAPEL;X.fill();trazo(LIN,2);const ta=o.a===undefined?1:o.a;if(ta>0){X.globalAlpha=ta;txt('$50',0,-34,104,TINTA,{w:340});txt('MILLION',0,54,62,TINTA,{w:340});X.globalAlpha=1}X.restore()}
function sala(L){X.fillStyle='#1b2f36';X.fillRect(L-900,-900,2900,4200);X.fillStyle='#22393f';for(let i=0;i<5;i++)X.fillRect(L-300+i*340,420,300,640);X.fillStyle='#16262c';X.fillRect(L-900,1090,2900,3000)}
function sillon(x,y,w,h,col){rr(x-w/2,y-h,w,h,40);X.fillStyle=col;X.fill();trazo(LIN,3);X.fillStyle='rgba(255,255,255,.06)';rr(x-w/2+26,y-h+26,w-52,h*.5,24);X.fill()}
function p04(L,t){const xo=T.x_offer,x5=T.x_50,d=eio(seg(t,xo-.2,x5+.1));
 // plano frontal fijo (sin movimiento de cámara): dos sillas enfrentadas, una mesa y la carpeta que avanza al centro
 sala(L);X.fillStyle='rgba(255,244,201,.05)';X.beginPath();X.ellipse(L+540,1080,560,380,0,0,7);X.fill();
 const inc=eio(seg(t,x5+.35,x5+1.2));sillon(L+540,1180+inc*30,330+inc*16,560+inc*8,'#4a3526');
 X.fillStyle='rgba(0,0,0,.3)';X.fillRect(L-900,1196,2900,30);X.fillStyle=MADERA;X.beginPath();X.moveTo(L+40,1120);X.lineTo(L+1040,1120);X.lineTo(L+1300,1560);X.lineTo(L-220,1560);X.closePath();X.fill();trazo(LIN,3);X.fillStyle=MADERA2;X.fillRect(L-220,1560,1520,60);
 // la carpeta entra con «Their offer» y la cifra aparece cuando se dice
 const ap=seg(t,xo-.22,xo-.08);if(ap>0){X.save();X.globalAlpha=ap;X.translate(L+540,lerp(1470,1320,d));X.scale(1,.5);carpeta(0,0,lerp(1.08,1,d),lerp(.1,0,d),{a:seg(t,x5-.14,x5+.04)});X.restore()}
 sillon(L+540,2010,350,430,'#55666f')}
// ---------- P05 · la mano parece tomarla, se detiene y la empuja de vuelta ----------
function mesaArriba(L){X.fillStyle=MADERA;X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(0,0,0,.07)';for(let i=0;i<14;i++)X.fillRect(L-900,-300+i*190,2900,10);X.fillStyle='rgba(255,255,255,.04)';for(let i=0;i<14;i++)X.fillRect(L-900,-210+i*190,2900,50)}
function p05(L,t){const c=T.c05,xl=T.x_listened,xr=T.x_laughed,xf=T.x_followed,xn=T.x_no;
 const llega=eio(seg(t,c+.05,xl+.3)),tira=eio(seg(t,xl+.3,xl+.9)),emp=eio(seg(t,xf-.05,xn+.08)),rie=golpe(t,xr-.05,.22)+golpe(t,xr+.2,.22),sale=eio(seg(t,xn+.12,xn+.42));
 const fx=540+tira*46-emp*400;
 cam(L,540,1000,lerp(1.02,1.1,seg(t,c,T.c06a)),540,1000,()=>{mesaArriba(L);carpeta(L+fx,1000,1.2,.03-emp*.08);
  manoArriba(L+fx+150+(1-llega)*760+sale*620,1012-rie*30,1.35,{rot:-1.02,sinLapiz:true,manga:CEO.manga,puno:CEO.puno})})}
// ---------- P06a · menos de 12 horas: el reloj y la invitación que llega tarde ----------
function relojMesa(x,y,r,u,tt){X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(x+8,y+12,r*1.08,0,7);X.fill();X.fillStyle='#1c2128';X.beginPath();X.arc(x,y,r*1.08,0,7);X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.beginPath();X.arc(x,y,r*.92,0,7);X.fill();
 if(u>0){X.fillStyle='rgba(192,57,43,.35)';X.beginPath();X.moveTo(x,y);X.arc(x,y,r*.86,-Math.PI/2,-Math.PI/2+u*Math.PI*1.9);X.closePath();X.fill()}
 X.strokeStyle=TINTA;X.lineCap='round';for(let i=0;i<12;i++){const q=i*Math.PI/6;X.lineWidth=i%3?4:8;X.beginPath();X.moveTo(x+Math.cos(q)*r*.74,y+Math.sin(q)*r*.74);X.lineTo(x+Math.cos(q)*r*.86,y+Math.sin(q)*r*.86);X.stroke()}
 const a=-Math.PI/2+u*Math.PI*1.9;X.lineWidth=r*.05;X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(a)*r*.7,y+Math.sin(a)*r*.7);X.stroke();X.lineWidth=r*.07;X.beginPath();X.moveTo(x,y);X.lineTo(x,y-r*.46);X.stroke();if(tt!==undefined){const b=-Math.PI/2+Math.floor(tt*3)*(Math.PI/30);X.strokeStyle='#c0392b';X.lineWidth=r*.022;X.beginPath();X.moveTo(x-Math.cos(b)*r*.12,y-Math.sin(b)*r*.12);X.lineTo(x+Math.cos(b)*r*.8,y+Math.sin(b)*r*.8);X.stroke()}X.fillStyle=TINTA;X.beginPath();X.arc(x,y,r*.07,0,7);X.fill()}
function p06a(L,t){const c=T.c06a,xi=T.x_inv,x12=T.x_12,fin=T.c06b;
 mesaArriba(L);relojMesa(L+420,900,lerp(280,300,seg(t,c,fin)),seg(t,c+.3,fin-.2),t);
 const s=eio(seg(t,xi-.25,xi+.3));if(s>0){X.save();X.translate(L+700+(1-s)*900,1420-(1-s)*200);X.rotate(.1-.3*(1-s));X.fillStyle='rgba(0,0,0,.28)';X.fillRect(-212,-132,440,290);X.fillStyle=PAPEL;X.fillRect(-220,-140,440,290);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-220,-140,440,290);X.strokeStyle='rgba(42,32,25,.4)';X.beginPath();X.moveTo(-220,-140);X.lineTo(0,20);X.lineTo(220,-140);X.stroke();lineasGrises(-150,60,300,2,16,3);X.restore()}
 const n=back(seg(t,x12-.2,x12+.1));if(n>0){X.save();X.translate(L+760,620);X.rotate(.08);X.scale(n,n);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-172,-102,360,220);X.fillStyle='#f6e58d';X.fillRect(-180,-110,360,220);txt('LESS THAN',0,-52,50,TINTA,{w:330});txt('12 HOURS',0,34,72,TINTA,{w:340});X.restore()}}
// ---------- P06b · casi sin plata, gastan lo que no tienen en un avión ----------
function avionArriba(x,y,s,rot,a){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle=`rgba(0,0,0,${a})`;X.beginPath();X.ellipse(0,0,34,210,0,0,7);X.fill();X.beginPath();X.moveTo(-10,-40);X.lineTo(-250,90);X.lineTo(-250,130);X.lineTo(0,70);X.lineTo(250,130);X.lineTo(250,90);X.lineTo(10,-40);X.closePath();X.fill();X.beginPath();X.moveTo(0,150);X.lineTo(-90,220);X.lineTo(-90,240);X.lineTo(0,214);X.lineTo(90,240);X.lineTo(90,220);X.closePath();X.fill();X.restore()}
function p06b(L,t){const c=T.c06b,xb=T.x_broke,xs=T.x_spent,xj=T.x_jet,xh=T.x_hear,fin=T.c07;
 mesaArriba(L);
 // boleto: su sello redondo ocupa el lugar del reloj
 X.save();X.translate(L+540,900);X.rotate(-.04);X.fillStyle='rgba(0,0,0,.28)';rr(-452,-322,930,660,24);X.fill();rr(-460,-330,930,660,24);X.fillStyle=PAPEL;X.fill();trazo(LIN,3);X.setLineDash([14,14]);X.strokeStyle='rgba(42,32,25,.4)';X.lineWidth=4;X.beginPath();X.moveTo(190,-330);X.lineTo(190,330);X.stroke();X.setLineDash([]);
 X.fillStyle='#1c2128';X.beginPath();X.arc(-120,0,290,0,7);X.fill();X.fillStyle='#fbf7ec';X.beginPath();X.arc(-120,0,262,0,7);X.fill();avionArriba(-120,-6,.9,.5,.85);lineasGrises(230,-250,200,5,18,8);X.fillStyle='rgba(42,32,25,.26)';for(let i=0;i<12;i++)X.fillRect(230+i*17,120,i%3?6:11,130);X.restore();
 // billetera casi vacía: sale el último billete
 const ab=eio(seg(t,xb-.5,xb-.05)),paga=eio(seg(t,xs,xs+.7));X.save();X.translate(L+760,1500);X.rotate(.06);X.fillStyle='rgba(0,0,0,.3)';rr(-232,-152,480,330,30);X.fill();rr(-240,-160,480,330,30);X.fillStyle='#4a2f1d';X.fill();trazo(LIN,3);X.fillStyle='#2e1c10';rr(-210,-130,420,150,16);X.fill();
 X.save();X.translate(-paga*520,-paga*460);X.rotate(-paga*.5);X.fillStyle='#7fb77a';X.fillRect(-150,-150+ (1-ab)*40,300,120);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-150,-150+(1-ab)*40,300,120);X.fillStyle='rgba(0,0,0,.18)';X.beginPath();X.arc(0,-90+(1-ab)*40,36,0,7);X.fill();X.restore();
 X.fillStyle='#5a3a24';rr(-240,-40,480,210,30);X.fill();trazo(LIN,3);X.restore();
 const j=seg(t,xj-.25,xh+.3);if(j>0&&j<1)avionArriba(L+lerp(-400,1500,j),lerp(1900,300,j),1.5,.72,.3)}
// ---------- P07 · entran de shorts, chalas y camisa hawaiana (de espaldas: sin rostros) ----------
function camisaP(){X.beginPath();X.moveTo(-120,-1040);X.quadraticCurveTo(0,-1072,120,-1040);X.lineTo(184,-992);X.lineTo(200,-850);X.lineTo(134,-838);X.lineTo(126,-660);X.lineTo(-126,-660);X.lineTo(-134,-838);X.lineTo(-200,-850);X.lineTo(-184,-992);X.closePath()}
function fundador(x,yf,s,t,fase,anda,o){X.save();X.translate(x,yf);X.scale(s,s);const sw=Math.sin(t*6.5+fase)*anda;
 X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,0,170,26,0,0,7);X.fill();
 [-1,1].forEach(d=>{const lift=Math.max(0,d*sw)*38,lx=d*54;X.fillStyle=o.piel;X.beginPath();X.moveTo(lx-38,-430);X.lineTo(lx+38,-430);X.lineTo(lx+26,-36-lift);X.lineTo(lx-26,-36-lift);X.closePath();X.fill();trazo(LIN,3);
  X.fillStyle='#e9c46a';rr(lx-42,-22-lift*.6,84,24,11);X.fill();trazo(LIN,3);X.fillStyle=o.piel;rr(lx-30,-50-lift,60,32,12);X.fill();trazo(LIN,2)});
 X.fillStyle=o.short;X.beginPath();X.moveTo(-120,-684);X.lineTo(120,-684);X.lineTo(128,-400);X.lineTo(10,-400);X.lineTo(0,-520);X.lineTo(-10,-400);X.lineTo(-128,-400);X.closePath();X.fill();trazo(LIN,3);
 [-1,1].forEach(d=>{X.fillStyle=o.piel;cap(d*166,-850,d*172-d*sw*12,-640,25);X.fill();trazo(LIN,3)});
 camisaP();X.fillStyle=o.camisa;X.fill();trazo(LIN,3);
 if(o.flores){X.save();camisaP();X.clip();for(let i=0;i<24;i++){const fx=-190+rnd(i+3)*380,fy=-1040+rnd(i+40)*380;X.fillStyle=i%2?'#f6e58d':'#f4a6b0';for(let k=0;k<5;k++){X.beginPath();X.ellipse(fx+Math.cos(k*1.256)*17,fy+Math.sin(k*1.256)*17,12,8,k*1.256,0,7);X.fill()}X.fillStyle='#e76f51';X.beginPath();X.arc(fx,fy,6,0,7);X.fill()}X.restore()}
 X.fillStyle=o.piel;X.fillRect(-32,-1100,64,66);[-1,1].forEach(d=>{X.beginPath();X.ellipse(d*80,-1150,12,22,0,0,7);X.fill();trazo(LIN,2)});X.fillStyle=o.pelo;X.beginPath();X.arc(0,-1160,80,0,7);X.fill();trazo(LIN,3);X.fillStyle=o.piel;X.beginPath();X.ellipse(0,-1094,34,15,0,0,Math.PI);X.fill();
 X.restore()}
function p07(L,t){const c=T.c07,fin=T.c08a,an=1-eio(seg(t,fin-.7,fin-.2)),av=seg(t,c,fin),en=1-eo(seg(t,c,c+.7));
 cam(L,540,1100,lerp(1,1.06,av),540,1100,()=>{X.fillStyle='#1b2f36';X.fillRect(L-900,-900,2900,4200);X.fillStyle='#22393f';for(let i=0;i<5;i++)X.fillRect(L-320+i*350,120,310,560);
  // la sala formal al fondo: sillones altos, trajes (siluetas, sin rostro) y la mesa larga
  [200,370,540,710,880].forEach(x=>{X.fillStyle='#3a2c22';rr(L+x-56,452,112,220,26);X.fill();trazo(LIN,2);X.fillStyle='#0f171b';X.beginPath();X.arc(L+x,520,26,0,7);X.fill();rr(L+x-50,550,100,120,26);X.fill();X.fillStyle='#d8dde0';X.beginPath();X.moveTo(L+x-12,552);X.lineTo(L+x+12,552);X.lineTo(L+x,582);X.closePath();X.fill();X.fillStyle='#8a2f2a';X.fillRect(L+x-3,566,6,40)});
  X.fillStyle=MADERA2;X.fillRect(L+90,640,900,70);X.fillStyle='#8a6240';X.fillRect(L+90,640,900,10);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+90,640,900,70);
  X.fillStyle='#16262c';X.fillRect(L-900,710,2900,3000);X.fillStyle='rgba(255,255,255,.035)';X.beginPath();X.moveTo(L+330,710);X.lineTo(L+750,710);X.lineTo(L+1120,2100);X.lineTo(L-40,2100);X.closePath();X.fill();
  fundador(L+322,1800-av*44+en*520,.95-av*.045,t,0,an,{piel:'#d9a783',pelo:'#4a3626',short:'#3d7ea6',camisa:'#9aa7ad'});
  fundador(L+758,1812-av*44+en*560,.95-av*.045,t,1.6,an,{piel:'#e2b592',pelo:'#2a2019',short:'#c8553d',camisa:'#2a9d8f',flores:true})})}
// ---------- P08a · diez años después: baja la persiana ----------
function p08a(L,t){const c=T.c08a,xl=T.x_later,xf=T.x_filed,baja=eio(seg(t,xf-.1,xf+.9));
 X.fillStyle='#12242a';X.fillRect(L-900,-900,2900,4200);X.fillStyle='#1a2f36';X.fillRect(L-900,1660,2900,2000);
 rr(L+110,740,860,930,10);X.fillStyle='#2f4a52';X.fill();trazo(LIN,3);X.fillStyle='#e76f51';X.fillRect(L+110,740,860,130);X.fillStyle='rgba(255,255,255,.25)';rr(L+250,776,580,58,12);X.fill();
 X.fillStyle=baja<.9?'#fff4c9':'#141a1e';X.fillRect(L+170,930,740,700);if(baja<.9){X.save();X.beginPath();X.rect(L+170,930,740,700);X.clip();X.translate(L+540,1280);X.scale(.5,.5);X.translate(-(L+540),-1000);estantes(L,-400,1500,560,4,1,196);X.restore()}
 X.fillStyle='#8e98a4';X.fillRect(L+160,920,760,(710)*baja+16);X.strokeStyle='rgba(0,0,0,.25)';X.lineWidth=5;for(let y=946;y<930+710*baja;y+=34){X.beginPath();X.moveTo(L+160,y);X.lineTo(L+920,y);X.stroke()}X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+160,920,760,720);
 const q=seg(t,c+.05,xl+.1)*1.2,va=1-seg(t,xf+.85,xf+1.1);X.save();X.globalAlpha=va;X.translate(L+540,575);for(let i=0;i<10;i++){const u=seg(q,i/10,i/10+.25);if(u>0&&u<1){X.save();X.globalAlpha=(1-u)*va;X.translate(u*(i%2?420:-420),40+u*u*420);X.rotate((i%2?1:-1)*u*1.4);X.fillStyle='#fbf7ec';X.fillRect(-150,-70,300,170);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-150,-70,300,170);X.restore()}}
 X.fillStyle='rgba(0,0,0,.28)';rr(-172,-122,360,250,16);X.fill();rr(-180,-130,360,250,16);X.fillStyle='#fbf7ec';X.fill();trazo(LIN,3);X.save();rr(-180,-130,360,250,16);X.clip();X.fillStyle='#c0392b';X.fillRect(-180,-130,360,62);X.restore();const f=back(seg(t,xl-.2,xl+.1));if(f>0){X.save();X.translate(0,30);X.scale(f,f);txt('10',0,-14,110,TINTA,{w:320});txt('YEARS',0,62,42,TINTA,{w:320});X.restore()}X.restore()}
// ---------- P08b · una sala iluminada por una pantalla genérica ----------
function p08b(L,t){const c=T.c08b,fin=T.c09a;
 cam(L,540,1000,lerp(1,1.08,seg(t,c,fin)),540,1000,()=>{X.fillStyle='#0c1418';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(120,170,255,.07)';X.beginPath();X.moveTo(L+190,1150);X.lineTo(L+890,1150);X.lineTo(L+1500,2300);X.lineTo(L-420,2300);X.closePath();X.fill();
  rr(L+170,560,740,590,18);X.fillStyle='#05080d';X.fill();X.save();X.beginPath();X.rect(L+194,584,692,542);X.clip();X.fillStyle='#101a2a';X.fillRect(L+194,584,692,542);
  for(let f=0;f<4;f++)for(let i=-1;i<7;i++){const x=L+214+i*148-((t*26*(f%2?1:-1)+f*40)%148+148)%148+ (f%2?0:0),y=612+f*128;rr(x,y,132,104,10);X.fillStyle=COL[(i*2+f*3+8)%COL.length];X.globalAlpha=.9;X.fill();X.globalAlpha=1;X.fillStyle='rgba(255,255,255,.18)';X.fillRect(x+10,y+70,80,10)}X.restore();X.strokeStyle='#2a3550';X.lineWidth=8;rr(L+170,560,740,590,18);X.stroke();X.fillStyle='#05080d';X.fillRect(L+500,1150,80,60);rr(L+400,1206,280,20,10);X.fill();
  X.fillStyle='#070b10';rr(L+60,1560,960,500,60);X.fill();rr(L+0,1480,200,600,60);X.fill();rr(L+880,1480,200,600,60);X.fill();X.beginPath();X.arc(L+420,1500,84,0,7);X.fill();X.beginPath();X.arc(L+650,1510,78,0,7);X.fill()})}
// ---------- P09a · queda una sola, en Oregon ----------
const ORE=[[.04,.1],[.1,.02],[.22,.07],[.3,.14],[.45,.12],[.62,.1],[.97,.1],[1,.3],[.93,.45],[.93,1],[0,1],[.02,.6]];
function local(x,y,s,luz){X.save();X.translate(x,y);X.scale(s,s);if(luz>0){X.fillStyle=`rgba(255,244,201,${.22*luz})`;X.beginPath();X.arc(0,-30,110,0,7);X.fill()}X.fillStyle=luz>0?'#2f4a52':'#22303a';X.fillRect(-56,-70,112,70);X.fillStyle=luz>0?'#e76f51':'#39444d';X.fillRect(-62,-92,124,26);X.fillStyle=luz>0?'#fff4c9':'#1a242c';X.fillRect(-40,-52,80,52);X.restore()}
function p09a(L,t){const c=T.c09a,x1=T.x_one10,xo=T.x_oregon;
 cam(L,540,1000,lerp(1,1.1,eio(seg(t,c,T.c09b))),540,1000,()=>{X.fillStyle='#12242a';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(255,255,255,.03)';for(let x=-900;x<2000;x+=110)X.fillRect(L+x,-900,2,4200);for(let y=-900;y<3000;y+=110)X.fillRect(L-900,y,2900,2);
  const ox=L+130,oy=640,w=820,h=640;X.beginPath();ORE.forEach((p,i)=>i?X.lineTo(ox+p[0]*w,oy+p[1]*h):X.moveTo(ox+p[0]*w,oy+p[1]*h));X.closePath();X.fillStyle='#1d3d45';X.fill();X.strokeStyle='#8fc7bd';X.lineWidth=6;X.lineJoin='round';X.stroke();
  for(let i=0;i<13;i++){const a=1-eio(seg(t,c+.1+i*.07,c+.5+i*.07)),x=L+60+rnd(i)*960,y=460+rnd(i+20)*1100;if(a>0){X.globalAlpha=a;local(x,y,.55,1);X.globalAlpha=1}else local(x,y,.55,0)}
  local(ox+.42*w,oy+.5*h,1.25,.7+.3*Math.sin(t*4));const q=back(seg(t,xo-.15,xo+.15));if(q>0){X.save();X.translate(ox+.5*w,oy+.84*h);X.scale(q,q);txt('OREGON',0,0,84,'#8fc7bd',{w:700});X.restore()}})}
// ---------- P09b · la carpeta vuelve al centro; cierre ----------
function p09b(L,t){const c=T.c09b,xt=T.x_take,k=T.x_tell,v=eio(seg(t,c+.1,c+1.0));
 const cm=ruta(t,[[c,540,1000,1.05,540,1000],[k-.2,540,1000,1.12,540,1000],[k+.5,540,1000,.85,430,1295]]);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>{mesaArriba(L);carpeta(L+lerp(-420,540,v),1000,1.2,lerp(-.25,.03,v));
  const e=eio(seg(t,xt-.35,xt+.1))*(1-eio(seg(t,k-.55,k-.2)));if(e>0)manoArriba(L+690+(1-e)*820,1012,1.35,{rot:-1.02,sinLapiz:true,manga:'#4a5560',puno:'#f1ede4'})});
 cierreCanal(L,t,k)}

NUEVOS.dc_mdm21_p01=SET(p01);NUEVOS.dc_mdm21_p02=SET(p02);NUEVOS.dc_mdm21_p03=SET(p03);NUEVOS.dc_mdm21_p04=SET(p04);NUEVOS.dc_mdm21_p05=SET(p05);NUEVOS.dc_mdm21_p06a=SET(p06a);NUEVOS.dc_mdm21_p06b=SET(p06b);
NUEVOS.dc_mdm21_p07=SET(p07);NUEVOS.dc_mdm21_p08a=SET(p08a);NUEVOS.dc_mdm21_p08b=SET(p08b);NUEVOS.dc_mdm21_p09a=SET(p09a);NUEVOS.dc_mdm21_p09b=SET(p09b);
})();
// ===== DC · MDM21 · FIN =====
</script>
