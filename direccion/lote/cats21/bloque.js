<script>
// ===== DC · CATS21 · INICIO ===== (Cats 21h · YOUR CAT SECRETLY SPEAKS TO YOU · paquete 4 del lote del 27-nov)
// Regla del paquete: ninguna palabra flotante ("food", "door"…). El sentido de cada maullido se entiende por el contexto y por la respuesta de la persona.
(function(){
const {LIN,K,cap,trazo,manoLado,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const CASA={color:'#9e9e9e'},NAR={color:'#e0903e',color2:'#f6dcc0',oscuro:'#b5661f',lejos:'#c47a30'},OSC={color:'#5b5461',color2:'#e8e4ec',oscuro:'#3a343f',lejos:'#4b4551',ojos:'#e9c46a'},MAMA={color:'#c9a87c',color2:'#f4e6cf',oscuro:'#9a7a52',lejos:'#b39468',ojos:'#7fb7d9'};
const MANO={manga:'#c8553d',puno:'#b34a34'},PIEL='#e8b28c';
function gatoP(x,y,s,t,o){const a=o.agacha||0;X.save();X.translate(x,y);X.scale(1+.05*a,1-.25*a);if(o.alfa!==undefined)X.globalAlpha=o.alfa;gato(0,0,s,t,o);X.restore()}
// ---------- el maullido: boca abierta y ondas (sin palabras). n y el ritmo son la "firma" de cada maullido ----------
function bocaDe(x,y,s,o){const d=o.dir<0?-1:1,sen=o.pose!=='parado',hs=sen?1:1.12,hx=sen?28:88,hy=sen?-170:-142,i=o.inclina||0,c=Math.cos(i),n=Math.sin(i),mx=40*hs,my=21*hs;return [x+d*s*(hx+mx*c-my*n),y+s*(hy+mx*n+my*c),d]}
function fuerza(t,k,n,op){op=op||{};let f=0;for(let j=0;j<n;j++)f=Math.max(f,golpe(t,k+j*(op.gap||.2),op.dur||.34));return f}
function maullar(x,y,s,o,t,k,n,op){op=op||{};const gap=op.gap||.2,[mx,my,d]=bocaDe(x,y,s,o),f=fuerza(t,k,n,op);
 if(f>0){X.fillStyle='#6d2433';X.beginPath();X.ellipse(mx,my+3*s*f,5.5*s,(2+7.5*f)*s,0,0,7);X.fill();X.fillStyle='#f48fb1';X.beginPath();X.ellipse(mx,my+(4+7*f)*s*.72,3.6*s,2.6*s*f,0,0,7);X.fill()}
 const ang=op.ang===undefined?(d>0?-.3:Math.PI+.3):op.ang;ondas(mx+Math.cos(ang)*10*s,my+Math.sin(ang)*10*s,ang,s*(op.tam||1),t,k,n,gap,op.vida||.5,op.col||'#fff1c9')}
function ondas(x,y,ang,s,t,k,n,gap,vida,col){X.lineCap='round';for(let j=0;j<n;j++){const u=seg(t,k+j*gap,k+j*gap+vida);if(u>0&&u<1){const r=(18+72*u)*s;X.strokeStyle=col;X.globalAlpha=(1-u)*.95;X.lineWidth=(6-3*u)*s*.55+2;X.beginPath();X.arc(x,y,r,ang-.55,ang+.55);X.stroke();X.beginPath();X.arc(x,y,r*.62,ang-.5,ang+.5);X.stroke();X.globalAlpha=1}}}

// ---------- la casa y la persona parcial ----------
function casa(L,yf){yf=yf||1500;const g=X.createLinearGradient(0,-600,0,yf);g.addColorStop(0,'#224a4f');g.addColorStop(1,'#31676b');X.fillStyle=g;X.fillRect(L-1500,-1600,5200,6200);
 X.fillStyle='#8a5f3f';X.fillRect(L-1500,yf,5200,2600);X.fillStyle='#e9e2d2';X.fillRect(L-1500,yf-38,5200,38);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L-1500,yf-43,5200,5);
 X.fillStyle='rgba(0,0,0,.12)';for(let i=0;i<12;i++)X.fillRect(L-1500,yf+48+i*46+i*i*7,5200,4)}
function piernas(x,yf,o){o=o||{};const sep=o.sep||130,ph=o.fase||0,an=o.anda||0,dd=o.dir||-1;X.lineJoin='round';
 [0,1].forEach(i=>{const d=i?1:-1,sw=Math.sin(ph+(i?Math.PI:0)),lx=x+d*sep/2+sw*52*an,ly=yf-Math.max(0,-sw)*34*an-(i?0:10);
  X.fillStyle=i?'#34466e':'#2b3a5c';X.beginPath();X.moveTo(lx-66,ly-2000);X.lineTo(lx+66,ly-2000);X.lineTo(lx+52,ly-64);X.lineTo(lx-52,ly-64);X.closePath();X.fill();trazo(LIN,3);
  X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(lx+dd*30,ly+4,110,12,0,0,7);X.fill();
  rr(lx+(dd<0?-132:-54),ly-58,186,58,24);X.fillStyle=i?'#e9e2d2':'#d2cbba';X.fill();trazo(LIN,3);X.fillStyle='#8f8776';X.fillRect(lx+(dd<0?-124:-46),ly-13,170,13)})}
function sillon(x,yb){X.lineJoin='round';X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(x+330,yb+6,380,16,0,0,7);X.fill();
 X.fillStyle='#4a3524';[40,600].forEach(v=>X.fillRect(x+v,yb-52,26,52));rr(x+90,yb-640,590,420,60);X.fillStyle='#d9a441';X.fill();trazo(LIN,3);
 rr(x+60,yb-300,640,250,40);X.fillStyle='#e3b352';X.fill();trazo(LIN,3);rr(x-20,yb-420,170,372,50);X.fillStyle='#d9a441';X.fill();trazo(LIN,3)}
function plato(x,yb,lleno){X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(x,yb+5,130,13,0,0,7);X.fill();
 if(lleno>0){X.fillStyle='#8a5a3a';X.beginPath();X.ellipse(x,yb-58,96,26+34*lleno,0,Math.PI,0);X.fill();X.fillStyle='rgba(0,0,0,.18)';for(let i=0;i<9;i++){X.beginPath();X.arc(x-70+i*17,yb-62-rnd(i)*24*lleno,7,0,7);X.fill()}}
 X.fillStyle='#f4f1e8';X.beginPath();X.moveTo(x-116,yb-60);X.lineTo(x+116,yb-60);X.lineTo(x+88,yb);X.lineTo(x-88,yb);X.closePath();X.fill();trazo(LIN,3);X.fillStyle='#7fb7d9';X.fillRect(x-98,yb-40,196,12)}
// mano con cuchara de comida que entra desde arriba a la derecha y vuelca
function sirve(L,px,py,en,vuelca,t){if(en<=0)return;const hx=L+px+(1-en)*520,hy=py-(1-en)*620,an=-.75-.5*vuelca,o=origen(hx,hy,an,1.25,-1,118,44);
 manoLado(o[0],o[1],an,1.25,-1,Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.4,parte:'atras'}));
 X.save();X.translate(hx,hy);X.rotate(-.2-1.1*vuelca);X.fillStyle='#d9d4c7';X.beginPath();X.moveTo(-150,-34);X.lineTo(-20,-40);X.lineTo(-20,44);X.lineTo(-150,50);X.quadraticCurveTo(-178,8,-150,-34);X.closePath();X.fill();trazo(LIN,3);X.fillStyle='#8a5a3a';X.beginPath();X.ellipse(-150,8,14,40,0,0,7);X.fill();X.fillRect(-20,-12,90,26);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-20,-12,90,26);X.restore();
 manoLado(o[0],o[1],an,1.25,-1,Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.4,parte:'pulgar'}))}
function croquetas(L,x0,y0,x1,y1,t,k,dur){for(let i=0;i<14;i++){const u=seg(t,k+i*dur/14,k+i*dur/14+.34);if(u>0&&u<1){X.fillStyle='#8a5a3a';X.beginPath();X.arc(L+lerp(x0,x1,u)+rnd(i)*26-13,lerp(y0,y1,u*u),8,0,7);X.fill()}}}
// mano que baja a acariciar la cabeza del gato
function acaricia(L,px,py,en,t){if(en<=0)return;const hx=L+px+(1-en)*330+Math.sin(t*7)*16*(en>.95?1:0),hy=py-(1-en)*640,an=-1.25,o=origen(hx,hy,an,1.3,-1,150,30);
 manoLado(o[0],o[1],an,1.3,-1,Object.assign({},MANO,{curl:[.22,.25,.28,.3],pulgar:.7}))}

// ---------- P01 · gancho: el gato mira y maúlla; la persona se detiene ----------
const G1=[430,1560,3.0];
function inicio(L,t,o){casa(L,1500);
 piernas(L+o.px,1508,{fase:t*7,anda:o.anda,dir:-1});
 if(o.mano>0)acaricia(L,o.mx||700,o.my||1150,o.mano,o.quieta?0:t);
 const g=Object.assign({},CASA,{pose:'sentado',inclina:o.inc,cola:1.3,lento:o.lento});
 gatoP(L+o.gx,G1[1],o.gs,t,g);(o.m||[]).forEach(q=>maullar(L+o.gx,G1[1],o.gs,g,t,q[0],q[1],q[2]))}
function p01(L,t){const xs=T.x_speaks,xe=T.x_explain,xc=T.x_careful,xy=T.x_youre,fin=T.c02;
 const M=[[xs-.1,1,{dur:.55,vida:.7}],[xe-.05,2,{}],[fin-.42,3,{gap:.13,dur:.26}]];
 const f=Math.max(...M.map(q=>fuerza(t,q[0],q[1],q[2])));
 const px=lerp(1300,830,eio(seg(t,0,xs+.05))),anda=1-seg(t,xs-.25,xs+.1);
 const inc=-.06-.16*f+.12*golpe(t,xc+.2,.9)-.1*golpe(t,xc+1.2,.8);
 const cm=ruta(t,[[0,540,1060,1],[xc,540,1050,1.06],[fin,520,1080,1.42]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>inicio(L,t,{px,anda,gx:G1[0],gs:G1[2],inc,m:M,mano:eio(seg(t,xe+.35,xe+.9))*(1-eio(seg(t,xc+.1,xc+.6))),mx:760,my:1000,quieta:true}))}
// ---------- P02 · el gatito llama a su madre ----------
function nido(L){X.fillStyle='#3a2b3f';X.fillRect(L-900,-900,2900,4200);X.fillStyle='#4a3a4f';X.fillRect(L-900,1500,2900,2600);
 X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(L+560,1530,620,60,0,0,7);X.fill();X.fillStyle='#b5654a';X.beginPath();X.ellipse(L+560,1512,600,62,0,0,7);X.fill();X.fillStyle='#d9a441';X.beginPath();X.ellipse(L+560,1500,520,44,0,0,7);X.fill()}
function p02(L,t){const c=T.c02,xm=T.x_meow2,xo=T.x_mother;
 const M=[[c+.06,2,{gap:.16,dur:.26,tam:.9}],[xm+.05,2,{gap:.16,dur:.26,tam:.9}]],f=Math.max(...M.map(q=>fuerza(t,q[0],q[1],q[2])));
 const baja=eio(seg(t,xo-.35,xo+.2)),kx=lerp(300,372,eio(seg(t,xo-.1,T.c03)));
 cam(L,560,1180,1.18,540,1000,()=>{nido(L);
  gatoP(L+800,1500,2.5,t,Object.assign({},MAMA,{pose:'sentado',dir:-1,inclina:-.05-.34*baja,cola:1,lento:true}));
  const g=Object.assign({},MAMA,{pose:'sentado',inclina:-.22-.12*f,cola:3});gatoP(L+kx,1500,1.15,t,g);M.forEach(q=>maullar(L+kx,1500,1.15,g,t,q[0],q[1],Object.assign({ang:-.75},q[2])))})}
// ---------- P03 · dos adultos se cruzan: postura, olfato y distancia; ningún maullido ----------
function atardecer(L,ym){const g=X.createLinearGradient(0,-200,0,ym);g.addColorStop(0,'#2b2445');g.addColorStop(.6,'#5a3a5c');g.addColorStop(1,'#b5654a');X.fillStyle=g;X.fillRect(L-1500,-1600,5200,6200);
 X.fillStyle='#231d38';for(let i=0;i<9;i++){const x=L-900+i*330+rnd(i)*80,h=260+rnd(i+4)*300;X.fillRect(x,ym-h,250,h);X.beginPath();X.moveTo(x-10,ym-h);X.lineTo(x+125,ym-h-90);X.lineTo(x+260,ym-h);X.closePath();X.fill()}
 X.fillStyle='#6b4a3d';X.fillRect(L-1500,ym,5200,4000);X.fillStyle='#8a6452';X.fillRect(L-1500,ym,5200,44);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L-1500,ym+44,5200,10);
 X.strokeStyle='rgba(0,0,0,.2)';X.lineWidth=4;for(let r=0;r<9;r++){const y=ym+110+r*86;X.beginPath();X.moveTo(L-1500,y);X.lineTo(L+3700,y);X.stroke();for(let i=0;i<34;i++){const x=L-1500+i*160+(r%2)*80;X.beginPath();X.moveTo(x,y-86);X.lineTo(x,y);X.stroke()}}}
function p03(L,t){const c=T.c03,xs=T.x_scent,xb=T.x_body,xh=T.x_hisses,fin=T.c04a;
 const ax=ruta(t,[[c,10],[c+1.5,285],[xs-.2,285],[xs+.25,345],[xh,345],[xh+.4,300],[fin-.5,300],[fin,350]])[0],bx=ruta(t,[[c,1150],[c+1.5,965],[xs-.2,965],[xs+.25,860],[xb,860],[xb+.4,915],[fin,915]])[0];
 const andaA=(t<c+1.5)||(t>xs-.2&&t<xs+.25)||(t>xh&&t<xh+.4)||t>fin-.5,andaB=(t<c+1.5)||(t>xs-.2&&t<xs+.25)||(t>xb&&t<xb+.4);
 cam(L,lerp(500,590,seg(t,c,fin)),1000,1,540,1000,()=>{atardecer(L,1300);
  gatoP(L+bx,1300,1.9,t,Object.assign({},OSC,{pose:'parado',dir:-1,camina:andaB,agacha:.75*eio(seg(t,xb-.05,xb+.35))+.2*eio(seg(t,xh,xh+.3)),inclina:.05+.16*golpe(t,xs+.2,.6)+.2*eio(seg(t,xb,xb+.3)),cola:.5}));
  gatoP(L+ax,1300,1.9,t,Object.assign({},NAR,{pose:'parado',camina:andaA,agacha:0,inclina:.02+.14*golpe(t,xs+.2,.6)-.14*eio(seg(t,xb,xb+.3)),cola:2.2}))})}
// ---------- P04 · el doméstico maúlla; afuera, sin personas, silencio; de vuelta, el maullido es para nosotros ----------
const G4=[380,1500,2.6];
function domestico(L,t,M,sube){casa(L,1500);sillon(L+1180,1500);piernas(L+850,1508,{dir:-1,anda:0});
 const f=Math.max(0,...M.map(q=>fuerza(t,q[0],q[1],q[2]))),g=Object.assign({},CASA,{pose:'sentado',inclina:-.3-.1*f,cola:1.3});
 if(sube>0)acaricia(L,560,960,sube,0);
 gatoP(L+G4[0],G4[1],G4[2],t,g);M.forEach(q=>maullar(L+G4[0],G4[1],G4[2],g,t,q[0],q[1],Object.assign({ang:-.95},q[2])))}
function p04a(L,t){domestico(L,t,[[T.c04a+.05,2,{}]],0)}
function p04b(L,t){const c=T.c04b;X.fillStyle='#141b30';X.fillRect(L-900,-900,2900,4200);const g=X.createLinearGradient(0,0,0,1500);g.addColorStop(0,'#141b30');g.addColorStop(1,'#2a3557');X.fillStyle=g;X.fillRect(L-900,-900,2900,2400);
 X.fillStyle='#f1ecd6';X.beginPath();X.arc(L+850,560,70,0,7);X.fill();X.fillStyle='#141b30';X.beginPath();X.arc(L+822,540,62,0,7);X.fill();
 X.fillStyle='rgba(255,255,255,.7)';[[120,480],[330,610],[560,450],[700,760],[220,820],[960,880]].forEach((q,i)=>{X.globalAlpha=.4+.4*Math.sin(t*2+i);X.beginPath();X.arc(L+q[0],q[1],4,0,7);X.fill()});X.globalAlpha=1;
 X.fillStyle='#10162a';[[-60,1060,330,440],[320,1160,260,340],[640,1000,300,500],[960,1120,300,380]].forEach(q=>X.fillRect(L+q[0],q[1],q[2],q[3]));
 X.fillStyle='#3b3550';X.fillRect(L-900,1500,2900,2600);X.fillStyle='#4a4463';X.fillRect(L-900,1500,2900,40);
 gatoP(L+860,1500,1.5,t,Object.assign({},NAR,{pose:'sentado',dir:-1,cola:.8,lento:true,color:'#8a6a4a',oscuro:'#5e4630',lejos:'#735840'}));
 gatoP(L+G4[0],G4[1],G4[2],t,Object.assign({},OSC,{pose:'sentado',inclina:-.3+.22*eio(seg(t,c+.5,c+1.1)),cola:.7}))}
function p04c(L,t){const c=T.c04c;domestico(L,t,[[T.x_meow5-.05,1,{dur:.6,vida:.75}],[T.x_save-.05,2,{}]],eio(seg(t,T.x_save+.25,T.c05)))}
// ---------- P05 · tres viñetas, mismo encuadre del gato: plato, puerta, sillón ----------
const G5=[300,1500,2.3];
function puerta(L,ab){X.fillStyle='#e9e2d2';X.fillRect(L+590,560,420,948);X.fillStyle='#ffe9b0';X.fillRect(L+616,586,368,914);X.fillStyle='#7fb77a';X.fillRect(L+616,1240,368,260);X.fillStyle='#9ad0f0';X.fillRect(L+616,586,368,400);
 X.save();X.translate(L+616,0);X.scale(1-.78*ab,1);X.fillStyle='#8a5f3f';X.fillRect(0,586,368,914);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(0,586,368,914);X.strokeStyle='rgba(0,0,0,.2)';X.lineWidth=5;X.strokeRect(40,640,288,360);X.strokeRect(40,1050,288,390);X.fillStyle='#e9c46a';X.beginPath();X.arc(318,1040,22,0,7);X.fill();trazo(LIN,3);X.restore()}
function p05(L,t){const c=T.c05,xm=T.x_meows7,xf=T.x_food,c2=T.x_one2-.04,xd=T.x_door,c3=T.x_one3-.04,xa=T.x_att;
 let M,vin=t<c2?1:t<c3?2:3;
 if(vin===1)M=[[c+.45,1,{dur:.6,vida:.75}],[xm-.05,2,{}]];else if(vin===2)M=[[c2+.04,3,{gap:.13,dur:.24}]];else M=[[c3+.03,1,{dur:.3,vida:.4}]];
 const f=Math.max(0,...M.map(q=>fuerza(t,q[0],q[1],q[2]))),pet=vin===3?eio(seg(t,xa-.2,xa+.1)):0;
 const g=Object.assign({},CASA,{pose:'sentado',inclina:-.2-.12*f+.14*pet,cola:1.3,lento:pet>.5});
 const z=vin===1?lerp(1,1.05,seg(t,c,c2)):1.05;
 cam(L,540,1100,z,540,1000,()=>{casa(L,1500);
  if(vin===1){piernas(L+960,1508,{dir:-1,anda:0});const en=eio(seg(t,xf-.6,xf-.2)),vu=eio(seg(t,xf-.12,xf+.12));plato(L+650,1500,seg(t,xf,xf+.35));croquetas(L,700,1180,650,1440,t,xf-.05,.25);sirve(L,790,1130,en,vu,t)}
  else if(vin===2){puerta(L,eio(seg(t,xd-.12,xd+.2)))}
  else{sillon(L+660,1500)}
  gatoP(L+G5[0],G5[1],G5[2],t,g);M.forEach(q=>maullar(L+G5[0],G5[1],G5[2],g,t,q[0],q[1],Object.assign({ang:-.6},q[2])));
  if(vin===3)acaricia(L,330,1010,pet,t)})}
// ---------- P06 · mira a la persona y repite el maullido que funcionó ----------
function p06(L,t){const c=T.c06,xl=T.x_learn;const M=[[c+.12,2,{}]],f=fuerza(t,M[0][0],2,{});
 const mira=ruta(t,[[c,-.3],[c+.9,-.3],[c+1.3,.06],[c+1.7,-.3]])[0],g=Object.assign({},CASA,{pose:'sentado',inclina:mira-.1*f,cola:1.5});
 const en=eio(seg(t,xl-.75,xl-.3)),vu=eio(seg(t,xl-.2,xl+.05));
 cam(L,560,1080,lerp(1.08,1.14,seg(t,c,T.c07)),540,1000,()=>{casa(L,1500);piernas(L+900,1508,{dir:-1,anda:0});plato(L+640,1500,seg(t,xl-.05,xl+.3));croquetas(L,690,1180,640,1440,t,xl-.12,.25);sirve(L,780,1130,en,vu,t);
  gatoP(L+330,1500,2.5,t,g);maullar(L+330,1500,2.5,g,t,M[0][0],2,{ang:-.8})})}
// ---------- P07 · amanecer: el maullido junto a la cama ----------
function p07(L,t){const c=T.c07,xm=T.x_meow9,xw=T.x_well,xl=T.x_learned;
 const M=[[c+.25,2,{}],[xm-.06,2,{}]],f=Math.max(...M.map(q=>fuerza(t,q[0],2,{}))),baja=eio(seg(t,xw-.45,xw+.05));
 const g=Object.assign({},CASA,{pose:'sentado',inclina:-.3-.1*f+.16*baja,cola:1.5,lento:baja>.6});
 cam(L,540,1100,lerp(1,1.07,seg(t,c,T.c08)),540,1000,()=>{X.fillStyle='#27324f';X.fillRect(L-900,-900,2900,4200);X.fillStyle='#3c3a52';X.fillRect(L-900,1560,2900,2600);X.fillStyle='rgba(255,255,255,.05)';X.fillRect(L-900,1560,2900,8);
  // ventana con el amanecer
  X.fillStyle='#1b2338';X.fillRect(L+60,470,400,470);const a=X.createLinearGradient(0,490,0,920);a.addColorStop(0,'#3d4a7a');a.addColorStop(.55,'#d98a6a');a.addColorStop(1,'#f6c66a');X.fillStyle=a;X.fillRect(L+80,490,360,430);
  X.fillStyle='#fbe6a2';X.beginPath();X.arc(L+260,920+40-60*seg(t,c,T.c08),70,Math.PI,0);X.fill();X.fillStyle='#1b2338';X.fillRect(L+252,490,16,430);X.fillRect(L+80,700,360,14);X.fillRect(L+60,920,400,24);
  // cama: colchón, frazada y almohada
  X.fillStyle='#4a3524';X.fillRect(L+620,1300,40,260);X.fillStyle='#5b4634';X.fillRect(L+560,1250,900,70);
  rr(L+560,1090,900,180,40);X.fillStyle='#e9e2d2';X.fill();trazo(LIN,3);rr(L+800,980,700,150,60);X.fillStyle='#f4f1e8';X.fill();trazo(LIN,3);
  X.fillStyle='#b5654a';X.beginPath();X.moveTo(L+540,1070);X.lineTo(L+1500,1040);X.lineTo(L+1500,1420);X.quadraticCurveTo(L+1000,1470,L+600,1430);X.quadraticCurveTo(L+520,1300,L+540,1070);X.closePath();X.fill();trazo(LIN,3);
  X.strokeStyle='rgba(0,0,0,.14)';X.lineWidth=5;[0,1,2].forEach(i=>{X.beginPath();X.moveTo(L+640+i*220,1090);X.quadraticCurveTo(L+620+i*220,1260,L+660+i*220,1430);X.stroke()});
  // la mano baja desde la cama
  if(baja>0){const hx=L+lerp(760,470,baja)+Math.sin(t*6.5)*14*(baja>.95?1:0),hy=lerp(1100,1140,baja),an=2.55,o=origen(hx,hy,an,1.25,1,150,30);
   manoLado(o[0],o[1],an,1.25,1,{manga:'#7d92a5',puno:'#6b7f92',curl:[.25,.28,.31,.33],pulgar:.7})}
  gatoP(L+330,1560,2.3,t,g);M.forEach(q=>maullar(L+330,1560,2.3,g,t,q[0],2,{ang:-.7}))})}
// ---------- P08 · vuelve el encuadre del inicio: la persona responde; el gato maúlla otra vez y se acerca ----------
function p08(L,t){const c=T.c08,xm=T.x_meows10,xa=T.x_answer,k=T.x_tell;
 const M=[[xm-.08,2,{}],[xa+.5,2,{}],[k+1.5,1,{dur:.5,vida:.7}]],f=Math.max(...M.map(q=>fuerza(t,q[0],q[1],q[2])));
 const ac=eio(seg(t,xa+.45,k+.3)),baja=eio(seg(t,k-.35,k+.45)),ag=eio(seg(t,T.x_talking-.1,xa-.1));
 const cm=ruta(t,[[c,520,1080,1.42],[xm,540,1060,1.12],[xa,540,1060,1.16]]);
 cam(L,cm[0],cm[1],cm[2],540,1000+120*baja,()=>{inicio(L,t,{px:830,anda:0,gx:G1[0]+50*ac,gs:G1[2]*(1+.07*ac),inc:-.1-.16*f+.06*ag,m:M,mano:ag,mx:790,my:1010,quieta:true,lento:t>k+.5});
  ondas(L+900,700,2.15,2.6,t,xa-.02,2,.2,.55,'#bfe6ff')});
 cierreCanal(L,t,k)}

NUEVOS.dc_cats21_p01=SET(p01);NUEVOS.dc_cats21_p02=SET(p02);NUEVOS.dc_cats21_p03=SET(p03);NUEVOS.dc_cats21_p04a=SET(p04a);NUEVOS.dc_cats21_p04b=SET(p04b);NUEVOS.dc_cats21_p04c=SET(p04c);
NUEVOS.dc_cats21_p05=SET(p05);NUEVOS.dc_cats21_p06=SET(p06);NUEVOS.dc_cats21_p07=SET(p07);NUEVOS.dc_cats21_p08=SET(p08);
})();
// ===== DC · CATS21 · FIN =====
</script>
