<script>
// ===== DC · GTAES19 · INICIO ===== (GTA ES 19h · GTA 5 HUMILLÓ a GTA 6 · paquete 12 del lote del 27-nov)
// Reglas del paquete: no se sugiere que GTA 6 lleva trece años compitiendo; 32,5 millones son ventas antes de salir; sin pronósticos; sin personajes ni logos.
// La pista es la escala: 4,6 px por millón desde la línea de partida. Todo lo que se mide en ella es proporcional.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const TEAL='#35e0d0',ROSA='#ff5fa2',AMA='#ffd23f',ASF='#15131f',TINTA='#2a2019',Y0=1640,U=4.6,X5=330,X6=750,TRAMO=32.5*4.6;
const yM=m=>Y0-m*U,C5=yM(215)+72,C6=yM(32.5)+72,YT=yM(215)-160;
// ---------- la pista vista desde arriba ----------
function pista(L,t,o){o=o||{};X.fillStyle='#0e0c16';X.fillRect(L-3000,-9000,7000,14000);X.fillStyle=ASF;X.fillRect(L+150,-9000,780,14000);
 for(let y=-9000;y<5000;y+=80){X.fillStyle=(Math.floor(y/80)&1)?'#2a2740':'#1c1a2b';X.fillRect(L+116,y,34,80);X.fillRect(L+930,y,34,80)}
 X.globalAlpha=.85;X.fillStyle=TEAL;X.fillRect(L+144,-9000,8,14000);X.fillStyle=ROSA;X.fillRect(L+928,-9000,8,14000);X.globalAlpha=1;
 X.fillStyle='rgba(255,255,255,.14)';X.fillRect(L+538,-9000,4,14000);X.fillStyle='rgba(255,255,255,.4)';for(let i=0;i<110;i++)X.fillRect(L+536,-9000+i*128+rnd(i+3)*90,8,26);
 // lo recorrido por cada uno
 const y5=yM(215),y6=yM(32.5),g=X.createLinearGradient(0,y5,0,Y0);g.addColorStop(0,`rgba(53,224,208,${.45+.3*(o.p5||0)})`);g.addColorStop(1,`rgba(53,224,208,${.14+.3*(o.p5||0)})`);X.fillStyle=g;X.fillRect(L+X5-70,y5,140,Y0-y5);
 X.fillStyle=`rgba(255,95,162,${.4+.4*(o.p6||0)})`;X.fillRect(L+X6-70,y6,140,Y0-y6);
 for(let i=0;i<7;i++){const y=Y0-((t*240+i*141+rnd(i+17)*110)%(Y0-y5));X.fillStyle='rgba(200,255,250,.3)';X.fillRect(L+X5-4,y,8,26+rnd(i+5)*26)}
 // línea de partida, cajones y nombres pintados
 for(let i=0;i<20;i++)for(let j=0;j<2;j++){X.fillStyle=(i+j)%2?'#e9e6f2':'#15131f';X.fillRect(L+150+i*39,Y0+j*20,39,20)}
 X.strokeStyle='rgba(255,255,255,.3)';X.lineWidth=5;[X5,X6].forEach(v=>{X.beginPath();X.moveTo(L+v-110,Y0+170);X.lineTo(L+v-110,Y0+56);X.lineTo(L+v+110,Y0+56);X.lineTo(L+v+110,Y0+170);X.stroke()});
 txt('GTA 5',L+X5,Y0+236,62,TEAL);txt('GTA 6',L+X6,Y0+236,62,ROSA);
 // los años, pintados al borde del carril de GTA 5
 if(o.a13>0)txt('2013',L+X5,Y0+112,58,'#e9e6f2',{a:o.a13});if(o.anios>0){for(let k=1;k<13;k++){const y=Y0-k*(Y0-y5)/13;if(o.z0!==undefined&&y>o.z0-24&&y<o.z1+24)continue;X.fillStyle=`rgba(233,230,242,${.4*o.anios})`;X.fillRect(L+104,y-2,46,4);txt(String(2013+k),L+58,y,30,'#e9e6f2',{a:.6*o.anios})}}}
function tablero(L,y,val,sub,s,giro,t){X.save();X.translate(L+X5,y);X.scale(s||1,s||1);rr(-150,-70,300,140,16);X.fillStyle='#0b0a12';X.fill();X.strokeStyle=TEAL;X.lineWidth=5;X.stroke();
 if(giro)[-80,0,80].forEach((v,i)=>{rr(v-34,-54,68,84,8);X.fillStyle='#1a1826';X.fill();const k=(t*8+i*.37)%1;X.fillStyle='rgba(234,255,251,.5)';X.fillRect(v-24,-48+k*62,48,10)});
 if(val)txt(val,0,-12,84,'#eafffb',{g:16,gc:TEAL});if(sub)txt(sub,0,44,28,TEAL);X.restore()}
function auto(x,y,s,col,t){X.save();X.translate(x,y+Math.sin(t*31)*1.2);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';rr(-52,-108,124,240,30);X.fill();
 X.fillStyle='#0a0910';[[-68,-80],[52,-80],[-68,52],[52,52]].forEach(q=>{rr(q[0],q[1],16,46,6);X.fill()});
 rr(-58,-116,116,232,34);X.fillStyle=col;X.fill();trazo(LIN,3);X.fillStyle='rgba(255,255,255,.14)';rr(-44,-104,88,58,18);X.fill();X.fillStyle='#12101c';rr(-42,-40,84,96,18);X.fill();X.fillStyle='rgba(255,255,255,.14)';rr(-34,-34,68,24,10);X.fill();
 X.fillStyle='#fff3c4';rr(-48,-114,26,10,5);X.fill();rr(22,-114,26,10,5);X.fill();X.fillStyle='#ff3b3b';rr(-48,104,30,10,5);X.fill();rr(18,104,30,10,5);X.fill();X.fillStyle='rgba(255,255,255,.25)';X.fillRect(-6,-116,12,76);X.fillRect(-6,56,12,60);X.restore();
 for(let i=0;i<3;i++){const u=(t*1.6+i/3)%1;X.fillStyle=`rgba(200,200,220,${.22*(1-u)})`;X.beginPath();X.arc(x+18*s,y+(120+u*70)*s,(8+u*16)*s,0,7);X.fill()}}
function autos(L,t){auto(L+X5,C5,.62,TEAL,t);auto(L+X6,C6,.62,ROSA,t)}
// ---------- P01 · dos carriles: uno ya recorrió muchísimo, el otro recién parte ----------
function p01(L,t){const xh=T.x_hum,xy=T.x_yno,xc=T.x_cui,fin=T.c02;
 const cm=ruta(t,[[0,540,1590,1.6],[xh-.22,540,1590,1.6],[xh+.5,540,640,1.6],[xy+.1,540,640,1.6],[xc-.3,540,1000,1],[xc+.4,540,1000,1.02],[fin,680,1450,1.5]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{pista(L,t);tablero(L,YT);autos(L,t)})}
// ---------- P02 · el contador llega a 215 millones; el carril viene desde 2013 ----------
function p02(L,t){const c=T.c02,x2=T.x_215,xm=T.x_mill,xd=T.x_desde,xa=T.x_2013,s3=T.s_3,fin=T.c03;
 const cm=ruta(t,[[c,330,640,1.6],[xd-.8,330,650,1.64],[xa,330,1680,1.6],[s3+.15,330,1640,1.74],[fin,330,560,1.45]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{pista(L,t,{a13:1,anios:1-seg(t,xd-.85,xd-.7)+seg(t,xa,xa+.35),p5:.5*golpe(t,s3,2.6),z0:cm[1]-760/cm[2],z1:cm[1]-600/cm[2]});
  tablero(L,YT,t>=x2?'215':null,t>=xm?'MILLONES':null,1+.1*golpe(t,x2,.3)+.06*golpe(t,fin-.9,.7),t<x2,t);autos(L,t)})}
// ---------- P03 · plano bajo en la salida: las luces siguen en rojo y ya hay 32,5 millones ----------
function autoLado(x,y,s,col,t){X.save();X.translate(x,y+Math.sin(t*30)*1.5);X.scale(s,s);X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(0,8,310,18,0,0,7);X.fill();
 X.beginPath();X.moveTo(-280,-40);X.lineTo(-272,-96);X.quadraticCurveTo(-200,-118,-120,-122);X.quadraticCurveTo(-60,-176,40,-172);X.quadraticCurveTo(120,-166,170,-112);X.quadraticCurveTo(250,-104,286,-78);X.lineTo(290,-40);X.closePath();X.fillStyle=col;X.fill();trazo(LIN,3);
 X.beginPath();X.moveTo(-104,-120);X.quadraticCurveTo(-56,-160,36,-158);X.quadraticCurveTo(100,-154,140,-114);X.closePath();X.fillStyle='#12101c';X.fill();X.fillStyle='rgba(255,255,255,.18)';X.fillRect(-260,-70,530,8);
 [-170,176].forEach(v=>{X.fillStyle='#0a0910';X.beginPath();X.arc(v,-40,50,0,7);X.fill();X.fillStyle='#3a3650';X.beginPath();X.arc(v,-40,24,0,7);X.fill();X.fillStyle='#0a0910';for(let k=0;k<5;k++){const a=t*14+k*1.2566;X.beginPath();X.arc(v+Math.cos(a)*14,-40+Math.sin(a)*14,4,0,7);X.fill()}});
 X.fillStyle='#fff3c4';rr(262,-92,26,14,6);X.fill();X.fillStyle='#ff3b3b';rr(-284,-98,14,26,6);X.fill();X.restore();
 for(let i=0;i<4;i++){const u=(t*1.8+i/4)%1;X.fillStyle=`rgba(200,200,220,${.25*(1-u)})`;X.beginPath();X.arc(x-(300+u*150)*s,y-(56+u*40)*s,(12+u*30)*s,0,7);X.fill()}}
function p03(L,t){const c=T.c03,xp=T.x_partio,x3=T.x_325,xa=T.x_antes,s5=T.s_5,fin=T.c04,rojo=.75+.25*Math.sin(t*10)*seg(t,xa-.1,xa+.1);
 cam(L,600,1110,lerp(1.1,1.2,eio(seg(t,c,fin))),540,1000,()=>{const g=X.createLinearGradient(0,-200,0,1200);g.addColorStop(0,'#100d1c');g.addColorStop(.6,'#2a1a45');g.addColorStop(1,'#8a2f6a');X.fillStyle=g;X.fillRect(L-900,-900,2900,4200);
  // horizonte: siluetas genéricas
  X.fillStyle='#1a1230';for(let i=0;i<16;i++){const x=L-200+i*96,h=60+rnd(i+5)*170;X.fillRect(x,1200-h,70,h)}
  [80,900,1010].forEach((x,i)=>{X.strokeStyle='#120c22';X.lineWidth=12;X.beginPath();X.moveTo(L+x,1200);X.quadraticCurveTo(L+x+18,1040,L+x+8,900);X.stroke();X.fillStyle='#120c22';for(let k=0;k<6;k++){const a=-2.6+k*.42;X.beginPath();X.ellipse(L+x+8+Math.cos(a)*56,900+Math.sin(a)*40,62,13,a,0,7);X.fill()}});
  X.fillStyle=ASF;X.fillRect(L-900,1200,2900,3000);X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-900,1200,2900,6);
  // línea de partida y pórtico con luces en rojo
  for(let i=0;i<8;i++)for(let j=0;j<2;j++){X.fillStyle=(i+j)%2?'#e9e6f2':'#15131f';X.beginPath();X.moveTo(L+230+j*28-i*10,1216+i*36);X.lineTo(L+258+j*28-i*10,1216+i*36);X.lineTo(L+248+j*28-i*10,1252+i*36);X.lineTo(L+220+j*28-i*10,1252+i*36);X.closePath();X.fill()}
  X.fillStyle='#1c1a2b';X.fillRect(L+236,740,20,480);rr(L+140,660,212,84,14);X.fill();trazo(LIN,3);[0,1,2,3].forEach(i=>{X.fillStyle=`rgba(255,59,59,${rojo})`;X.beginPath();X.arc(L+174+i*48,702,17,0,7);X.fill()});X.fillStyle=`rgba(255,59,59,${.10*rojo})`;X.beginPath();X.arc(L+246,702,170,0,7);X.fill();
  // lo ya recorrido antes de la luz verde
  X.fillStyle='rgba(255,95,162,.55)';X.fillRect(L+212,1440,728,24);X.fillStyle='#fff0f6';X.fillRect(L+934,1428,8,48);
  // letrero
  const a=back(seg(t,x3-.1,x3+.18));X.fillStyle='#1c1a2b';X.fillRect(L+590,960,16,250);X.fillRect(L+850,960,16,250);X.save();X.translate(L+728,850);X.scale(1+.05*golpe(t,s5+.3,.5)+.05*golpe(t,s5+1.1,.5),1+.05*golpe(t,s5+.3,.5)+.05*golpe(t,s5+1.1,.5));rr(-220,-130,440,260,18);X.fillStyle='#0b0a12';X.fill();X.strokeStyle=ROSA;X.lineWidth=6;X.stroke();if(a>0){X.save();X.scale(a,a);txt('32,5',0,-26,128,'#fff0f6',{g:18,gc:ROSA});txt('MILLONES',0,72,40,ROSA);X.restore()}X.restore();
  autoLado(L+650,1392,1,ROSA,t)})}
// ---------- P04 · la cinta de medir: 32,5 es el 15 % de 215 ----------
function cinta(L,e){const y1=lerp(Y0,yM(215),e);X.fillStyle=AMA;X.fillRect(L+526,y1,28,Y0-y1);X.fillStyle='rgba(0,0,0,.5)';for(let m=0;m*U<Y0-y1;m+=5)X.fillRect(L+526,Y0-m*U-2,m%25?12:28,3);
 rr(L+496,Y0+6,88,88,16);X.fillStyle=AMA;X.fill();trazo(LIN,3);X.fillStyle=ASF;X.beginPath();X.arc(L+540,Y0+50,20,0,7);X.fill();X.fillStyle='#e9e6f2';X.fillRect(L+514,y1-8,52,10)}
function p04(L,t){const c=T.c04,s7=T.s_7,xa=T.x_325b,x15=T.x_15,xl=T.x_lleva,fin=T.c05,e=eio(seg(t,c+.25,s7-.15));
 cam(L,540,1000,lerp(1,1.04,seg(t,c,fin)),540,1000,()=>{pista(L,t,{p6:golpe(t,xa-.05,.9),p5:golpe(t,xl-.05,.9)});tablero(L,YT,'215','MILLONES',1+.08*golpe(t,xl,.6));autos(L,t);cinta(L,e);
  const a=back(seg(t,xa-.1,xa+.15));if(a>0){X.save();X.translate(L+X6,yM(32.5)-52);X.scale(a,a);txt('32,5 M',0,0,54,'#fff0f6',{g:10,gc:ROSA});X.restore()}
  const b=back(seg(t,x15-.1,x15+.18));if(b>0){X.strokeStyle=AMA;X.lineWidth=6;X.lineJoin='round';X.beginPath();X.moveTo(L+X6+80,yM(32.5));X.lineTo(L+X6+108,yM(32.5));X.lineTo(L+X6+108,Y0);X.lineTo(L+X6+80,Y0);X.stroke();X.save();X.translate(L+X6,yM(32.5)-190);X.scale(b,b);txt('15 %',0,0,128,AMA,{g:14});X.restore()}})}
// ---------- P05 · casi siete tramos como el que ya tiene ----------
function p05(L,t){const c=T.c05,xs=T.x_siete,fin=T.c06a;
 const cm=ruta(t,[[c,700,1400,1.4],[c+.25,700,1400,1.4],[xs,700,640,1.4],[xs+.4,700,640,1.4],[fin,540,1000,1]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{pista(L,t);tablero(L,YT,'215','MILLONES',1);
  X.strokeStyle=AMA;X.lineWidth=5;X.setLineDash([22,14]);X.beginPath();X.moveTo(L+150,yM(215));X.lineTo(L+930,yM(215));X.stroke();X.setLineDash([]);
  for(let k=2;k<=7;k++){const tk=lerp(c+.3,xs-.15,(k-2)/5),a=eo(seg(t,tk,tk+.25));if(a>0){X.save();X.globalAlpha=a;X.fillStyle='rgba(255,95,162,.12)';X.fillRect(L+X6-70,Y0-k*TRAMO+4,140,TRAMO-8);X.strokeStyle=ROSA;X.lineWidth=5;X.setLineDash([16,12]);X.strokeRect(L+X6-70,Y0-k*TRAMO+4,140,TRAMO-8);X.restore()}}
  autos(L,t);const b=back(seg(t,xs-.08,xs+.2));if(b>0){X.save();X.translate(L+X6,Y0-7*TRAMO-90);X.scale(b,b);txt('CASI',0,-74,44,AMA);txt('7×',0,6,112,AMA,{g:14});X.restore()}})}
// ---------- P06 · a uno le tomó 13 años; el otro recién empieza ----------
function pared(L){X.fillStyle='#120f1d';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(255,255,255,.025)';for(let i=0;i<14;i++)X.fillRect(L-900,300+i*130,2900,3);X.fillStyle='#0c0a14';X.fillRect(L-900,1560,2900,2600)}
function calGTA(x,y,s,col,titulo,o){X.save();X.translate(x,y);X.scale(s,s);for(let i=o.pila||0;i>0;i--){X.fillStyle=i%2?'#cfc6ae':'#efe6d0';X.fillRect(-186+i*2,144+i*5,372-i*4,6)}
 X.fillStyle='rgba(0,0,0,.35)';rr(-182,-132,380,290,16);X.fill();rr(-190,-140,380,290,16);X.fillStyle='#efe6d0';X.fill();trazo(LIN,3);X.save();rr(-190,-140,380,290,16);X.clip();X.fillStyle=col;X.fillRect(-190,-140,380,80);X.restore();txt(titulo,0,-98,48,ASF);
 X.fillStyle=TINTA;[-120,120].forEach(v=>{X.beginPath();X.arc(v,-140,12,0,7);X.fill()});if(o.anio)txt(String(o.anio),0,50,118,TINTA);
 if(o.bandera){const w=o.bandera;X.fillStyle=TINTA;X.fillRect(-84,-36,8,170);for(let i=0;i<5;i++)for(let j=0;j<4;j++){const dy=Math.sin(w*5+i*.9)*6;X.fillStyle=(i+j)%2?TINTA:'#fbf7ec';X.fillRect(-76+i*32,-36+j*26+dy,32,26)}X.strokeStyle=TINTA;X.lineWidth=3;X.strokeRect(-76,-36,160,104)}
 X.restore()}
function p06a(L,t){const c=T.c06a,x13=T.x_13,FT=[];for(let i=1;i<=13;i++)FT.push(c+.15+i*((x13-.05)-(c+.15))/13);let n=0;FT.forEach(v=>{if(t>=v)n++});
 pared(L);for(let i=Math.max(0,n-4);i<n;i++){const u=seg(t,FT[i],FT[i]+.4);if(u<1){X.save();X.globalAlpha=1-u;X.translate(L+540+(i%2?1:-1)*u*520,1040+u*u*380);X.rotate((i%2?1:-1)*u*1.2);X.fillStyle='#efe6d0';X.fillRect(-280,-100,560,320);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-280,-100,560,320);txt(String(2013+i),0,80,180,TINTA);X.restore()}}
 calGTA(L+540,960,1.6,TEAL,'GTA 5',{anio:2013+n,pila:Math.max(0,13-n)});
 const b=back(seg(t,x13-.08,x13+.2));if(b>0){X.save();X.translate(L+540,1400);X.scale(b,b);txt('13 AÑOS',0,0,120,AMA,{g:14});X.restore()}}
function p06b(L,t){const c=T.c06b,xr=T.x_recien;pared(L);calGTA(L+540,960,1.6,ROSA,'GTA 6',{bandera:t});
 const b=back(seg(t,xr-.08,xr+.2));if(b>0){X.save();X.translate(L+540,1400);X.scale(b,b);txt('RECIÉN EMPIEZA',0,0,78,ROSA,{g:12});X.restore()}}
// ---------- P07 · los dos carriles siguen abiertos hacia adelante; cierre ----------
function autoAtras(x,y,s,col,t){X.save();X.translate(x,y+Math.sin(t*28)*1.2*s);X.scale(s,s);X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(0,72,130,16,0,0,7);X.fill();X.fillStyle='#0a0910';rr(-112,20,36,56,8);X.fill();rr(76,20,36,56,8);X.fill();
 X.beginPath();X.moveTo(-110,50);X.lineTo(-104,-20);X.quadraticCurveTo(-70,-70,0,-72);X.quadraticCurveTo(70,-70,104,-20);X.lineTo(110,50);X.closePath();X.fillStyle=col;X.fill();trazo(LIN,3);
 X.fillStyle='#12101c';X.beginPath();X.moveTo(-70,-22);X.quadraticCurveTo(-50,-58,0,-60);X.quadraticCurveTo(50,-58,70,-22);X.closePath();X.fill();X.fillStyle='#ff3b3b';rr(-98,-6,54,16,8);X.fill();rr(44,-6,54,16,8);X.fill();X.fillStyle='#1c1a2b';rr(-30,22,60,18,4);X.fill();X.restore()}
function p07(L,t){const k=T.x_tell,VX=430,VY=1150;X.fillStyle='#0e0c16';X.fillRect(L-900,-900,2900,4200);
 const g=X.createLinearGradient(0,760,0,VY);g.addColorStop(0,'#100d1c');g.addColorStop(1,'#7a2a66');X.fillStyle=g;X.fillRect(L-900,760,2900,VY-760);X.fillStyle='rgba(255,170,120,.35)';X.beginPath();X.arc(L+VX,VY,70,Math.PI,0);X.fill();
 X.fillStyle='#0e0c16';X.fillRect(L-900,VY,2900,3000);X.fillStyle=ASF;X.beginPath();X.moveTo(L+VX-14,VY);X.lineTo(L+VX+14,VY);X.lineTo(L+1560,1920);X.lineTo(L-700,1920);X.closePath();X.fill();
 X.lineWidth=6;X.strokeStyle=TEAL;X.beginPath();X.moveTo(L+VX-14,VY);X.lineTo(L-700,1920);X.stroke();X.strokeStyle=ROSA;X.beginPath();X.moveTo(L+VX+14,VY);X.lineTo(L+1560,1920);X.stroke();
 for(let i=0;i<9;i++){const u=((i/9+t*.5)%1),p=u*u,y=VY+p*770,w=2+p*14;X.fillStyle='rgba(255,255,255,.35)';X.fillRect(L+VX-w/2,y,w,10+p*70)}
 autoAtras(L+VX-(1222-VY)*.76,1222,.34,TEAL,t);autoAtras(L+VX+(1392-VY)*.76,1392,.92,ROSA,t);
 cierreCanal(L,t,k)}

NUEVOS.dc_gtaes19_p01=SET(p01);NUEVOS.dc_gtaes19_p02=SET(p02);NUEVOS.dc_gtaes19_p03=SET(p03);NUEVOS.dc_gtaes19_p04=SET(p04);NUEVOS.dc_gtaes19_p05=SET(p05);NUEVOS.dc_gtaes19_p06a=SET(p06a);NUEVOS.dc_gtaes19_p06b=SET(p06b);NUEVOS.dc_gtaes19_p07=SET(p07);
})();
// ===== DC · GTAES19 · FIN =====
</script>
