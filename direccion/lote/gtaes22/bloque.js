<script>
// ===== DC · GTAES22 · INICIO ===== (GTA ES 22h · La prensa se RINDIÓ ante GTA 6 · paquete 13 del lote del 27-nov)
// Reglas del paquete: no se afirma unanimidad ni que más reseñas garanticen la nota; sin medios, críticos ni citas inventadas; sin personajes ni logos.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const ROSA='#ff5fa2',TEAL='#35e0d0',ORO='#ffd23f',NOCHE='#120f1d',CREMA='#f3ecd8',TINTA='#1c1530',LUZ='#fff4f8',GRIS='#3a3650';
const pop=(t,k)=>back(seg(t,k-.1,k+.16));
function ponTxt(s,x,y,size,col,k,o){if(k<=0)return;X.save();X.translate(x,y);X.scale(k,k);txt(s,0,0,size,col,o||{});X.restore()}
function galeria(L,t){X.fillStyle=NOCHE;X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(255,255,255,.02)';for(let i=0;i<10;i++)X.fillRect(L-900,420+i*130,2900,3);X.fillStyle='#0c0a14';X.fillRect(L-900,1640,2900,2600);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L-900,1640,2900,5)}
function mesa(L){X.fillStyle='#17142a';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(255,255,255,.02)';for(let i=0;i<40;i++)X.fillRect(L-900,-900+i*104,2900,3)}
function placa(x,y,s,col,k,o){o=o||{};if(k<=0)return;X.save();X.translate(x,y);X.scale(s*k,s*k);X.fillStyle='rgba(0,0,0,.4)';rr(-150,-112,320,250,28);X.fill();rr(-160,-125,320,250,28);X.fillStyle='#0b0a14';X.fill();X.strokeStyle=col;X.lineWidth=7;X.stroke();
 if(o.giro){[-66,66].forEach((v,i)=>{rr(v-54,-90,108,150,10);X.fillStyle='#1c1830';X.fill();const q=(o.t*8+i*.37)%1;X.fillStyle='rgba(255,244,248,.5)';X.fillRect(v-42,-80+q*118,84,12)})}
 else{txt('99',0,-24,150,LUZ,{g:14+10*(o.late||0),gc:col});if(o.sub>0)txt('DE 100',0,78,36,col,{a:o.sub})}
 if(o.br>0&&o.br<1){X.save();rr(-160,-125,320,250,28);X.clip();X.fillStyle='rgba(255,255,255,.16)';X.beginPath();const bx=-360+o.br*720;X.moveTo(bx,-125);X.lineTo(bx+80,-125);X.lineTo(bx-40,125);X.lineTo(bx-120,125);X.closePath();X.fill();X.restore()}X.restore()}
function chip(x,y,r,col,a){X.globalAlpha=a===undefined?1:a;X.fillStyle='rgba(0,0,0,.35)';X.beginPath();X.arc(x+3,y+4,r,0,7);X.fill();X.fillStyle=col;X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.3)';X.lineWidth=3;X.beginPath();X.arc(x,y,r*.6,0,7);X.stroke();X.globalAlpha=1}
// ---------- P01 · la pared de tarjetas se ordena y forma un 99 ----------
const N9=[".###.","#...#","#...#",".####","....#","#...#",".###."];
function enNueve(c,r){const q=r-4;if(q<0||q>=14)return false;const f=Math.floor(q/2),k=(c>=1&&c<=5)?c-1:(c>=8&&c<=12)?c-8:-1;return k>=0&&N9[f][k]==='#'}
function p01(L,t){const xy=T.x_ylo,xp=T.x_pero,xd=T.x_det,fin=T.c02a,z=eio(seg(t,xp+.1,fin)),late=golpe(t,xy+.1,1.6);
 cam(L,lerp(540,431,z),lerp(1000,941,z),lerp(1,1.03,seg(t,0,xp))+z*1.07,540,1000,()=>{X.fillStyle=NOCHE;X.fillRect(L-900,-900,2900,4200);
  for(let r=0;r<22;r++)for(let c=0;c<14;c++){const i=r*14+c,on=enNueve(c,r),t0=.03+rnd(i+7)*.4,u=eo(seg(t,t0,t0+.5)),v=seg(t,t0+.28,t0+.58),des=(c===5&&r===9)?eio(seg(t,xd,xd+.7)):0;
   X.save();X.translate(L+50+c*70+31+(1-u)*(rnd(i+90)-.5)*300,Math.max(452,470+r*50+21+(1-u)*(rnd(i+190)-.5)*260)-des*10);X.rotate((1-u)*(rnd(i+290)-.5)*1.4-des*.14);
   if(des>0){X.fillStyle='rgba(0,0,0,.45)';X.fillRect(-31+des*8,-21+des*12,62,42)}
   if(v<1){X.globalAlpha=1-v;X.fillStyle=i%3?CREMA:'#e4dcc6';X.fillRect(-31,-21,62,42);X.fillStyle='rgba(28,21,48,.25)';X.fillRect(-23,-11,46,5);X.fillRect(-23,1,34,5)}
   if(v>0){X.globalAlpha=v;X.fillStyle=on?ROSA:'#231f38';X.fillRect(-31,-21,62,42);if(on){X.fillStyle=`rgba(255,255,255,${.12+.3*late})`;X.fillRect(-31,-21,62,14);const w=Math.max(0,1-Math.abs((c+r)*.5-((t*7)%26-4))/1.6);if(w>0){X.fillStyle=`rgba(255,255,255,${.5*w})`;X.fillRect(-31,-21,62,42)}}}
   X.restore()}})}
// ---------- P02a · las reseñas salieron el 18 de noviembre ----------
function tarjeta(x,y,rot,s,i){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-142,-86,300,190);X.fillStyle=i%2?CREMA:'#e4dcc6';X.fillRect(-150,-95,300,190);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-150,-95,300,190);X.fillStyle=[ROSA,TEAL,ORO][i%3];X.fillRect(-150,-95,300,18);X.fillStyle='rgba(28,21,48,.28)';[-40,-10,20,50].forEach((v,k)=>{rr(-124,v,(k%2?200:248),12,6);X.fill()});X.restore()}
function hojaCal(x,y,s,rot,dia){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle='rgba(0,0,0,.35)';rr(-202,-216,420,460,14);X.fill();rr(-210,-230,420,460,14);X.fillStyle=CREMA;X.fill();trazo(LIN,3);X.save();rr(-210,-230,420,460,14);X.clip();X.fillStyle='#c0392b';X.fillRect(-210,-230,420,104);X.restore();txt('NOVIEMBRE',0,-176,50,CREMA);
 X.fillStyle=TINTA;[-120,120].forEach(v=>{X.beginPath();X.arc(v,-230,12,0,7);X.fill()});ponTxt('18',0,62,240,TINTA,dia);X.restore()}
function p02a(L,t){const c=T.c02a,x18=T.x_18,fin=T.c02b;
 cam(L,540,1040,lerp(1.05,1,eo(seg(t,c,c+.9)))+.03*seg(t,x18,fin),540,1000,()=>{mesa(L);
  for(let i=0;i<7;i++){const e=eo(seg(t,c+.1+i*.14,c+.6+i*.14));if(e>0)tarjeta(L+540+(i-3)*150*e,1480+Math.abs(i-3)*34*e+(1-e)*500,(i-3)*.16*e,.9,i)}
  const en=eo(seg(t,x18-.5,x18-.1));hojaCal(L+540,lerp(-360,880,en),1.1,(1-en)*.3-.03,pop(t,x18))})}
// ---------- P02b · el promedio de los críticos: 99 de 100 ----------
function p02b(L,t){const c=T.c02b,xp=T.x_prom,x9=T.x_99,x1=T.x_100,fin=T.c03;
 cam(L,540,1000,lerp(1,1.06,seg(t,c,fin)),540,1000,()=>{galeria(L,t);X.fillStyle='rgba(255,244,214,.07)';X.beginPath();X.moveTo(L+500,-200);X.lineTo(L+580,-200);X.lineTo(L+1000,1640);X.lineTo(L+80,1640);X.closePath();X.fill();X.fillStyle='rgba(255,95,162,.10)';X.beginPath();X.arc(L+540,930,430,0,7);X.fill();
  for(let i=0;i<24;i++){const k=c+.1+i*.14,u=seg(t,k,k+.6);if(u>0&&u<1&&k<x9-.55){const d=i%2?1:-1;chip(L+540+d*lerp(560,150,u),lerp(640+rnd(i+3)*620,930,u),lerp(40,24,u),[ROSA,TEAL,ORO][i%3],1)}}
  ponTxt('PROMEDIO DE LOS CRÍTICOS',L+540,600,44,TEAL,pop(t,xp));
  placa(L+540,930,1.9,ROSA,1,{giro:t<x9,t:t,sub:t<x9?0:seg(t,x1-.2,x1-.02),late:golpe(t,x9,.5),br:seg(t,x1+.15,x1+.95)})})}
// ---------- P03 · dos juegos con el mismo 99; uno es de 1998 ----------
function pedestal(x,yb,lit,l1,l2,tam){X.fillStyle=lit?'#2e2748':'#1a1630';X.fillRect(x-120,yb-330,240,330);X.fillStyle=lit?'#3a3258':'#1f1a36';X.fillRect(x-140,yb-360,280,34);X.fillRect(x-140,yb-16,280,20);X.strokeStyle='rgba(0,0,0,.4)';X.lineWidth=3;X.strokeRect(x-120,yb-326,240,310);
 if(lit){rr(x-104,yb-250,208,120,10);X.fillStyle='#0b0a14';X.fill();if(l2){txt(l1,x,yb-214,30,CREMA);txt(l2,x,yb-170,30,CREMA)}else txt(l1,x,yb-190,tam||46,CREMA)}}
function cartucho(x,y,s,k){if(k<=0)return;X.save();X.translate(x,y);X.scale(s*k,s*k);X.fillStyle='rgba(0,0,0,.35)';rr(-84,-176,180,186,16);X.fill();rr(-90,-186,180,186,16);X.fillStyle='#7d8590';X.fill();trazo(LIN,4);X.fillStyle='#5d646e';for(let i=0;i<5;i++)X.fillRect(-70+i*30,-178,14,22);rr(-66,-140,132,96,8);X.fillStyle='#cdbf96';X.fill();trazo(LIN,3);X.fillStyle='rgba(28,21,48,.3)';[-120,-100,-80].forEach(v=>X.fillRect(-52,v,104,8));X.fillStyle='#4a5058';X.fillRect(-60,-22,120,22);X.restore()}
function estuche(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.35)';rr(-80,-212,172,222,10);X.fill();const g=X.createLinearGradient(0,-222,0,0);g.addColorStop(0,'#3a1c5a');g.addColorStop(.55,'#d6457f');g.addColorStop(1,'#f39a4a');rr(-86,-222,172,222,10);X.fillStyle=g;X.fill();trazo(LIN,4);X.fillStyle='#ffd98a';X.beginPath();X.arc(0,-96,40,Math.PI,0);X.fill();X.fillStyle='#1b1230';X.fillRect(-84,-96,168,26);X.fillStyle='rgba(255,255,255,.18)';X.fillRect(-86,-222,14,222);X.restore()}
function laurel(x,y,s,a){if(a<=0)return;X.save();X.translate(x,y);X.scale(s,s);X.globalAlpha=a;X.fillStyle=ORO;[-1,1].forEach(d=>{for(let k=0;k<7;k++){const an=Math.PI*.5+d*(.38+k*.33);X.save();X.translate(Math.cos(an)*158,Math.sin(an)*158-20);X.rotate(an+d*1.95);X.beginPath();X.ellipse(0,0,34,13,0,0,7);X.fill();X.restore()}});X.restore()}
function p03(L,t){const c=T.c03,xz=T.x_zelda,x98=T.x_1998,xm=T.x_mejor,fin=T.c04,luz=eo(seg(t,xz-.15,xz+.35)),la=eo(seg(t,xm-.3,xm+.4));
 cam(L,540,1190,lerp(1.0,1.15,eio(seg(t,c,xz+.2)))+.07*seg(t,xz+.2,fin),540,1000,()=>{galeria(L,t);
  const bus=eio(seg(t,c+.2,xz-.1));[[lerp(-260,300,bus),.5+.5*luz],[780,1]].forEach(q=>{X.fillStyle=`rgba(255,244,214,${.055*q[1]})`;X.beginPath();X.moveTo(L+q[0]-30,-200);X.lineTo(L+q[0]+30,-200);X.lineTo(L+q[0]+300,1640);X.lineTo(L+q[0]-300,1640);X.closePath();X.fill()});
  pedestal(L+780,1640,1,'GTA 6');estuche(L+780,1280,1);placa(L+780,880,.62,ROSA,1,{sub:1,br:seg(t,c+.3,c+1.2)});
  pedestal(L+300,1640,luz>.5,'OCARINA','OF TIME');laurel(L+300,1170,1.02,la*(.75+.25*Math.sin(t*4)));cartucho(L+300,1280,1.05,back(seg(t,xz-.1,xz+.2)));placa(L+300,880,.62,ORO,back(seg(t,xz+.35,xz+.62)),{sub:1,late:la});
  const k=eo(seg(t,x98-.2,x98+.15));if(k>0){X.save();X.translate(L+392,1150);X.rotate(.5*(1-k)+.12+Math.sin((t-x98)*7)*.22*Math.exp(-Math.max(0,t-x98)*1.6)+Math.sin(t*3)*.03);X.strokeStyle=CREMA;X.lineWidth=3;X.beginPath();X.moveTo(0,0);X.lineTo(26,60);X.stroke();X.translate(26,60);rr(-10,0,150,70,10);X.fillStyle=CREMA;X.fill();trazo(LIN,3);X.fillStyle=TINTA;X.beginPath();X.arc(6,14,6,0,7);X.fill();txt('1998',70,38,44,TINTA);X.restore()}})}
// ---------- P04 · debajo de cada 99: 22 reseñas a un lado, más de 140 al otro ----------
const IZQ=[],DER=[];for(let i=0;i<22;i++)IZQ.push([106+(i%5)*62,836+Math.floor(i/5)*62]);for(let i=0;i<144;i++)DER.push([483+(i%10)*56,836+Math.floor(i/10)*56]);
function tableros(L,t,o){[[50,360,ORO],[440,590,TEAL]].forEach(q=>{rr(L+q[0],440,q[1],q[0]<100?800:1320,22);X.fillStyle='#17142a';X.fill();X.strokeStyle='#2a2646';X.lineWidth=4;X.stroke()});
 txt('OCARINA',L+230,492,36,ORO,{a:o.nom});txt('GTA 6',L+735,492,40,ROSA,{a:o.nom});
 IZQ.forEach((p,i)=>{const k=o.iz(i);if(k>0)chip(L+p[0],p[1],24*Math.min(1,k),ORO,o.at)});
 DER.forEach((p,i)=>{const k=o.de(i);chip(L+p[0],p[1],22,k>0?TEAL:GRIS,(i>=140?.55:1)*o.at)})}
function p04(L,t){const c=T.c04,s7=T.s_7,x9=T.x_99b,x22=T.x_22,xc=T.x_cambio,x140=T.x_140,fin=T.c06;
 const cm=ruta(t,[[c,735,2.6],[c+.2,735,2.6],[s7-.15,540,1],[fin,540,1.03]]);
 cam(L,cm[0],470,cm[1],540,412,()=>{mesa(L);
  tableros(L,t,{nom:1,at:1,iz:i=>back(seg(t,lerp(x9+.1,x22-.1,i/21),lerp(x9+.1,x22-.1,i/21)+.18)),de:i=>t>=lerp(xc+.3,x140-.05,Math.floor(i/10)/14)?1:0});
  placa(L+735,640,.8,ROSA,1,{sub:1,late:golpe(t,x140,.6)});placa(L+230,640,.8,ORO,back(seg(t,x9-.12,x9+.14)),{sub:1});
  ponTxt('22 RESEÑAS',L+230,1180,48,ORO,pop(t,x22));ponTxt('MÁS DE 140',L+735,1700,58,TEAL,pop(t,x140),{g:10})})}
// ---------- P06 · la balanza: el mismo número, seis veces más críticos ----------
function columna(x,yb,n,col,a,res){for(let i=0;i<n;i++){X.fillStyle='rgba(0,0,0,.3)';rr(x-21,yb-(i+1)*10+2,46,9,4);X.fill();X.fillStyle=col;rr(x-23,yb-(i+1)*10,46,9,4);X.globalAlpha=a;X.fill();X.globalAlpha=1}if(res>0){X.strokeStyle=`rgba(255,255,255,${res})`;X.lineWidth=5;rr(x-28,yb-n*10-6,56,n*10+10,8);X.stroke()}}
function p06(L,t){const c=T.c06,xd=T.x_dificil,s9=T.s_9,xm=T.x_mismo,x6=T.x_seis,fin=T.c07;
 const TC=[];for(let i=0;i<7;i++)TC.push(c+.35+i*.32);const carg=TC.reduce((a,k,i)=>a+eo(seg(t,k,k+.22))*(i<6?1:.4),0)/6.4,ang=lerp(-.07,.075,carg)+Math.sin(t*1.9)*.02+golpe(t,xd,.8)*.012;
 cam(L,540,1080,lerp(1,1.05,seg(t,c,fin)),540,1000,()=>{galeria(L,t);
  // poste y base
  X.fillStyle='#2e2748';X.beginPath();X.moveTo(L+420,1640);X.lineTo(L+660,1640);X.lineTo(L+580,1560);X.lineTo(L+500,1560);X.closePath();X.fill();X.fillRect(L+526,800,28,770);X.strokeStyle='rgba(0,0,0,.4)';X.lineWidth=3;X.strokeRect(L+526,800,28,770);
  // brazo y platos
  X.save();X.translate(L+540,800);X.rotate(ang);X.fillStyle='#4a4270';rr(-320,-13,640,26,13);X.fill();trazo(LIN,3);X.restore();X.fillStyle=ORO;X.beginPath();X.arc(L+540,800,22,0,7);X.fill();trazo(LIN,3);
  [-1,1].forEach(d=>{const ex=L+540+d*300*Math.cos(ang),ey=800+d*300*Math.sin(ang),py=ey+470;X.strokeStyle='#8a82b0';X.lineWidth=4;X.beginPath();X.moveTo(ex,ey);X.lineTo(ex-170,py);X.moveTo(ex,ey);X.lineTo(ex+170,py);X.stroke();
   X.fillStyle='#3a3258';rr(ex-184,py,368,22,10);X.fill();trazo(LIN,3);
   if(d<0)columna(ex,py,22,ORO,1,.0);
   else for(let i=0;i<7;i++){const u=eo(seg(t,TC[i],TC[i]+.22));if(u>0)columna(ex-150+i*50,py-(1-u)*520,i<6?22:9,TEAL,u,i<6?golpe(t,x6+i*.13,.3):0)}});
  // el mismo 99 a los dos lados, a la misma altura
  const lt=golpe(t,xm,.7);placa(L+240,560,.5+.04*lt,ORO,1,{sub:1,late:lt});placa(L+840,560,.5+.04*lt,ROSA,1,{sub:1,late:lt});
  ponTxt('6×',L+840,1500,130,TEAL,pop(t,x6),{g:14})})}
// ---------- P07 · el 99 al centro, con los dos grupos detrás; cierre ----------
function p07(L,t){const c=T.c07,k=T.x_tell,m=eio(seg(t,k-.2,k+.5));
 cam(L,540,1050,1+.03*seg(t,c,k),540,1000,()=>{mesa(L);tableros(L,t,{nom:.5,at:.45,iz:i=>1,de:i=>1});X.fillStyle='rgba(10,8,20,.35)';X.fillRect(L-900,-900,2900,4200)});
 placa(L+lerp(540,430,m),lerp(1010,1300,m)+Math.sin(t*1.6)*5,lerp(1.5,.9,m),ROSA,back(seg(t,c,c+.3)),{sub:1,late:.4+.4*Math.sin(t*3)});
 cierreCanal(L,t,k)}

NUEVOS.dc_gtaes22_p01=SET(p01);NUEVOS.dc_gtaes22_p02a=SET(p02a);NUEVOS.dc_gtaes22_p02b=SET(p02b);NUEVOS.dc_gtaes22_p03=SET(p03);NUEVOS.dc_gtaes22_p04=SET(p04);NUEVOS.dc_gtaes22_p06=SET(p06);NUEVOS.dc_gtaes22_p07=SET(p07);
})();
// ===== DC · GTAES22 · FIN =====
</script>
