<script>
// ===== DC · CATS16 · INICIO ===== (Cats 16h · If You Have a CAT NEVER Throw THIS Away · paquete 3 del lote del 27-nov)
// Regla del paquete: el cambio se cuenta con postura, distancia y exploración; nada de caras de caricatura ni felicidad instantánea.
(function(){
const {LIN,K,cap,trazo,manoLado,origen,cam,cierreCanal,SET}=window.DC;
const CARTON='#c9a06a',CARTON2='#a47d4c',CARTON3='#ddb985',DENTRO='#5e4527',BW=380,BH=290,BX=190,C1=380,C2=1200,CG=790,ZG=.68;
const CASA={color:'#9e9e9e'},NAR={color:'#e0903e',color2:'#f6dcc0',oscuro:'#b5661f',lejos:'#c47a30'},OSC={color:'#5b5461',color2:'#e8e4ec',oscuro:'#3a343f',lejos:'#4b4551',ojos:'#e9c46a'};
const MANO={manga:'#c8553d',puno:'#b34a34'};
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
// gato del motor con postura: agacha 0 (erguido) … 1 (comprimido contra el piso)
function gatoP(x,y,s,t,o){const a=o.agacha||0;X.save();X.translate(x,y);X.scale(1+.05*a,1-.25*a);if(o.alfa!==undefined)X.globalAlpha=o.alfa;gato(0,0,s,t,o);X.restore()}

// ---------- cajas ----------
function cajaFrente(cx,yb,rot){const w=BW,h=BH;X.save();X.translate(cx,yb-h/2);X.rotate(rot||0);X.lineJoin='round';
 X.fillStyle=CARTON3;X.beginPath();X.moveTo(-w/2,-h/2);X.lineTo(-w/2+30,-h/2-112);X.lineTo(w/2-30,-h/2-112);X.lineTo(w/2,-h/2);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=DENTRO;X.beginPath();X.moveTo(-w/2,-h/2);X.lineTo(-w/2+20,-h/2-44);X.lineTo(w/2-20,-h/2-44);X.lineTo(w/2,-h/2);X.closePath();X.fill();
 [-1,1].forEach(d=>{X.fillStyle=CARTON2;X.beginPath();X.moveTo(d*w/2,-h/2);X.lineTo(d*(w/2+98),-h/2-38);X.lineTo(d*(w/2+106),-h/2-14);X.lineTo(d*w/2,-h/2+28);X.closePath();X.fill();trazo(LIN,3)});
 X.fillStyle=CARTON;X.fillRect(-w/2,-h/2,w,h);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-w/2,-h/2,w,h);
 X.fillStyle='rgba(255,255,255,.2)';X.fillRect(-27,-h/2,54,h);X.fillStyle='rgba(0,0,0,.07)';X.fillRect(-w/2,h/2-60,w,60);
 X.fillStyle=CARTON3;X.beginPath();X.moveTo(-w/2,-h/2);X.lineTo(w/2,-h/2);X.lineTo(w/2-16,-h/2+76);X.lineTo(-w/2+16,-h/2+76);X.closePath();X.fill();trazo(LIN,3);
 X.restore()}
// caja acostada, con la boca a la derecha. capa 'fondo' va detrás del gato; la cara va delante.
function cajaLado(x,yb,capa){const w=BW,h=BH;X.lineJoin='round';
 if(capa==='fondo'){X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(x+w/2+20,yb+5,w*.58,13,0,0,7);X.fill();
  X.fillStyle=DENTRO;X.beginPath();X.moveTo(x+w-6,yb-h);X.lineTo(x+w+44,yb-h+22);X.lineTo(x+w+44,yb);X.lineTo(x+w-6,yb);X.closePath();X.fill();
  X.fillStyle=CARTON2;X.beginPath();X.moveTo(x+w,yb-h);X.lineTo(x+w+124,yb-h-60);X.lineTo(x+w+132,yb-h-42);X.lineTo(x+w+44,yb-h+22);X.closePath();X.fill();trazo(LIN,3);
  X.fillStyle=CARTON3;X.beginPath();X.moveTo(x+w,yb-9);X.lineTo(x+w+156,yb-9);X.lineTo(x+w+166,yb+4);X.lineTo(x+w,yb+4);X.closePath();X.fill();trazo(LIN,3);return}
 X.fillStyle=CARTON;X.fillRect(x,yb-h,w,h);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(x,yb-h,w,h);
 X.fillStyle='rgba(255,255,255,.2)';X.fillRect(x,yb-h*.57,w,28);X.fillStyle='rgba(0,0,0,.07)';X.fillRect(x,yb-56,w,56);
 X.strokeStyle='rgba(40,27,18,.32)';X.lineWidth=4;X.lineCap='round';X.beginPath();X.moveTo(x+62,yb-h+92);X.lineTo(x+62,yb-h+36);X.moveTo(x+44,yb-h+56);X.lineTo(x+62,yb-h+36);X.lineTo(x+80,yb-h+56);X.stroke()}

// ---------- la casa ----------
function casa(L){const g=X.createLinearGradient(0,-600,0,1500);g.addColorStop(0,'#224a4f');g.addColorStop(1,'#31676b');X.fillStyle=g;X.fillRect(L-1500,-1600,5200,6000);   // base opaca completa: el piso se pinta encima, sin costura
 X.fillStyle='#e9e2d2';X.fillRect(L-1500,1462,5200,38);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L-1500,1457,5200,5);
 X.fillStyle='#8a5f3f';X.fillRect(L-1500,1500,5200,2400);X.fillStyle='rgba(0,0,0,.12)';for(let i=0;i<12;i++)X.fillRect(L-1500,1548+i*46+i*i*7,5200,4)}
function pata(x1,y1,ang){X.save();X.translate(x1,y1);X.rotate(ang);X.lineJoin='round';
 X.fillStyle='#9e9e9e';X.beginPath();X.moveTo(-900,-34);X.lineTo(-30,-40);X.lineTo(-30,40);X.lineTo(-900,46);X.closePath();X.fill();trazo(LIN,3);
 X.strokeStyle='#5d606b';X.lineWidth=7;X.lineCap='round';[-250,-190,-130].forEach(v=>{X.beginPath();X.moveTo(v,-30);X.quadraticCurveTo(v+12,0,v,32);X.stroke()});
 X.fillStyle='#e2e4ea';X.beginPath();X.ellipse(4,2,56,48,0,0,7);X.fill();trazo(LIN,3);
 X.fillStyle='#e2e4ea';[[44,-24,17],[58,2,18],[46,28,17]].forEach(q=>{X.beginPath();X.arc(q[0],q[1],q[2],0,7);X.fill();trazo(LIN,2.5)});X.fillStyle='#e2e4ea';X.beginPath();X.ellipse(8,2,50,43,0,0,7);X.fill();X.restore()}
function basurero(x,yb){X.lineJoin='round';
 X.fillStyle=CARTON2;X.save();X.translate(x+80,yb-330);X.rotate(-.16);X.fillRect(-10,-150,150,190);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-10,-150,150,190);X.restore();
 X.fillStyle=CARTON3;X.save();X.translate(x+170,yb-320);X.rotate(.1);X.fillRect(0,-110,130,150);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(0,-110,130,150);X.restore();
 X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(x+160,yb+5,190,14,0,0,7);X.fill();
 X.fillStyle='#2b6f9e';X.beginPath();X.moveTo(x,yb-330);X.lineTo(x+330,yb-330);X.lineTo(x+300,yb);X.lineTo(x+30,yb);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='#245d85';rr(x-16,yb-352,362,44,12);X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(255,255,255,.75)';X.lineWidth=9;X.lineCap='round';const cx=x+165,cy=yb-160;for(let i=0;i<3;i++){const a=i*2.094-1.57;X.beginPath();X.arc(cx,cy,52,a+.25,a+1.7);X.stroke();const e=a+1.7,ex=cx+Math.cos(e)*52,ey=cy+Math.sin(e)*52;X.beginPath();X.moveTo(ex,ey);X.lineTo(ex+Math.cos(e-.9)*24,ey+Math.sin(e-.9)*24);X.moveTo(ex,ey);X.lineTo(ex+Math.cos(e+2.2)*24,ey+Math.sin(e+2.2)*24);X.stroke()}}
// ---------- P01 · gancho: la mano se lleva la caja y una pata la detiene ----------
function p01(L,t){const xt=T.x_this,xm=T.x_most,xa=T.x_and,xh=T.x_hurt;
 const llega=eio(seg(t,.05,.7)),ag=eio(seg(t,.62,.85)),prueba=golpe(t,xt-.22,.5),lleva=eio(seg(t,xm,xm+1.5)),para=seg(t,xa+.22,xa+.34),vuelve=1-back(seg(t,xa+.3,xa+.78));
 const m=lleva*Math.max(0,vuelve),dx=175*m,dy=-(46*prueba+165*m),rot=.15*m+.03*prueba,cx=L+470+dx,yb=1500+dy;
 const suelta=eio(seg(t,xa+.3,xa+.6));
 // esquina superior derecha de la caja, de donde toma la mano
 const c=Math.cos(rot),s=Math.sin(rot),gx0=BW/2-34,gy0=-BH/2+8,gx=cx+gx0*c-gy0*s,gy=yb-BH/2+gx0*s+gy0*c;
 const hx=lerp(L+1250,gx,llega)+suelta*70,hy=lerp(560,gy,llega)-suelta*120,an=-.86+.1*m,HS=1.32,o=origen(hx,hy,an,HS,-1,118,44);
 const curl=lerp(.05,.5,ag)*(1-suelta*.8),mo=p=>manoLado(o[0],o[1],an,HS,-1,Object.assign({},MANO,{curl:[curl,curl+.03,curl+.06,curl+.08],pulgar:lerp(.75,.42,ag)+suelta*.3,parte:p}));
 const z=ruta(t,[[0,540,1210,1.12],[xm,540,1200,1.16],[xa,560,1150,1.16],[xa+.5,520,1200,1.26],[T.c02,520,1205,1.3]]);
 cam(L,z[0],z[1],z[2],540,1000,()=>{casa(L);basurero(L+890,1500);
  mo('atras');cajaFrente(cx,yb,rot);mo('pulgar');
  const en=eio(seg(t,xa+.02,xa+.3));if(en>0){const px=cx-BW/2+44*c-(-BH/2-6)*s*0-20,py=yb-BH+(-10)+ (1-Math.max(0,vuelve))*0;
   const tx=lerp(L-260,cx-BW/2+70,en),ty=lerp(1330,yb-BH-14,en)+14*golpe(t,xh+.1,.22)+14*golpe(t,xh+.42,.22);pata(tx,ty,.1-.12*en)}})}
// ---------- P02 · el primer movimiento es esconderse ----------
function transportin(x,yb,dir,ap,sc){sc=sc||1;X.save();X.translate(x,yb);X.scale(dir*sc,sc);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(0,5,225,15,0,0,7);X.fill();
 X.strokeStyle='#5d7382';X.lineWidth=18;X.lineCap='round';X.beginPath();X.arc(0,-264,72,Math.PI,0);X.stroke();
 rr(-190,-264,380,264,42);X.fillStyle='#8fa7b6';X.fill();trazo(LIN,3);X.fillStyle='#74909f';X.fillRect(-188,-124,376,16);
 X.fillStyle='rgba(0,0,0,.25)';[-130,-80,-30].forEach(v=>{rr(v,-226,30,74,12);X.fill()});
 rr(92,-230,98,204,14);X.fillStyle='#2e3d47';X.fill();
 X.save();X.translate(190,-128);X.scale(1-ap*.86,1);X.strokeStyle='#e3eaee';X.lineWidth=6;rr(-98,-102,98,204,12);X.stroke();for(let i=1;i<4;i++){X.beginPath();X.moveTo(-98+i*24.5,-102);X.lineTo(-98+i*24.5,102);X.stroke()}for(let i=1;i<4;i++){X.beginPath();X.moveTo(-98,-102+i*51);X.lineTo(0,-102+i*51);X.stroke()}X.restore();X.restore()}
function sillon(x,yb){X.lineJoin='round';X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(x+330,yb+6,380,16,0,0,7);X.fill();
 X.fillStyle='#4a3524';[40,600].forEach(v=>X.fillRect(x+v,yb-52,26,52));
 rr(x,yb-560,150,512,44);X.fillStyle='#c9952f';X.fill();trazo(LIN,3);
 rr(x+90,yb-640,590,420,60);X.fillStyle='#d9a441';X.fill();trazo(LIN,3);
 rr(x+60,yb-300,640,250,40);X.fillStyle='#e3b352';X.fill();trazo(LIN,3);
 rr(x-20,yb-420,170,372,50);X.fillStyle='#d9a441';X.fill();trazo(LIN,3)}
function p02(L,t){const c=T.c02,xh=T.x_hide;
 const gx=ruta(t,[[c,300],[xh+.1,985],[T.c03,1060]])[0],cx=lerp(520,800,eio(seg(t,c,T.c03)));
 cam(L,cx,1090,1.05,540,1000,()=>{casa(L);transportin(L+70,1500,1,1);
  gatoP(L+gx,1500,1.9,t,Object.assign({},CASA,{pose:'parado',camina:t<xh+.1,agacha:.85,inclina:.16,cola:.6}));
  sillon(L+1000,1500)})}

// ---------- el refugio: dos espacios equivalentes (760 de ancho cada uno; el derecho es el espejo del izquierdo) ----------
function refugioFondo(L){X.fillStyle='#2c4051';X.fillRect(L-1900,-1900,6600,6400);X.fillStyle='#22323f';X.fillRect(L-1900,1500,6600,2900)}
function modulo(L,mx,esp){X.save();X.translate(L+mx+380,0);X.scale(esp,1);X.lineJoin='round';
 X.fillStyle='#3a5062';X.fillRect(-380,400,760,170);X.fillStyle='rgba(0,0,0,.16)';[-150,150].forEach(v=>{rr(v-70,474,140,22,11);X.fill()});
 X.fillStyle='#93a7b5';X.fillRect(-380,570,760,930);X.fillStyle='rgba(0,0,0,.10)';X.fillRect(-380,570,760,14);
 X.fillStyle='#7b8e9b';X.fillRect(-380,1500,760,260);X.fillStyle='rgba(0,0,0,.10)';X.fillRect(-380,1500,760,8);
 rr(-364,1448,172,54,16);X.fillStyle='#c98d8d';X.fill();trazo(LIN,3);X.strokeStyle='rgba(0,0,0,.16)';X.lineWidth=3;X.beginPath();X.moveTo(-352,1475);X.lineTo(-204,1475);X.stroke();
 X.fillStyle='#f4f1e8';X.beginPath();X.moveTo(246,1470);X.lineTo(354,1470);X.lineTo(338,1504);X.lineTo(262,1504);X.closePath();X.fill();trazo(LIN,3);X.fillStyle='#8a5a3a';X.beginPath();X.ellipse(300,1470,46,8,0,0,7);X.fill();
 X.restore()}
function marcos(L,mx){X.fillStyle='#5f717c';X.fillRect(L+mx-12,400,24,1372);X.fillRect(L+mx+748,400,24,1372);X.fillRect(L+mx-12,386,784,28);X.fillStyle='#51626c';X.fillRect(L+mx-12,1760,784,24)}
// hoja de calendario. rot = rótulo de la cabecera; num = cifra de la hoja; gris = hoja sin cifra
function hojaCal(cx,yTop,w,rot,num,gris){const hH=w*.24,hS=w*.9;X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.22)';rr(cx-w/2+w*.03,yTop+w*.04,w,hH+hS,w*.05);X.fill();
 rr(cx-w/2,yTop,w,hH+hS,w*.05);X.fillStyle='#fbf7ec';X.fill();trazo(LIN,3);
 X.save();rr(cx-w/2,yTop,w,hH+hS,w*.05);X.clip();X.fillStyle='#c0392b';X.fillRect(cx-w/2,yTop,w,hH);X.restore();
 X.fillStyle='#f2efe6';[-.24,.24].forEach(d=>{X.beginPath();X.arc(cx+d*w,yTop+hH*.5,w*.045,0,7);X.fill()});
 if(gris){X.fillStyle='rgba(42,32,25,.22)';rr(cx-w*.2,yTop+hH+hS*.34,w*.4,hS*.4,w*.04);X.fill()}
 else{txt(rot,cx,yTop+hH*.54,hH*.56,'#fff',{w:w*.9});txt(num,cx,yTop+hH+hS*.54,hS*.7,'#2a2019',{w:w*.8})}}
function hojaSuelta(x,y,w,rot,a){X.save();X.globalAlpha=a;X.translate(x,y);X.rotate(rot);X.fillStyle='#fbf7ec';X.fillRect(-w/2,0,w,w*.9);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-w/2,0,w,w*.9);X.fillStyle='rgba(42,32,25,.2)';rr(-w*.2,w*.3,w*.4,w*.36,w*.04);X.fill();X.restore()}
function general(L,fn,z){cam(L,CG,1000,z||ZG,540,1000,fn)}
// ---------- P03 · dos gatos llegan a dos espacios iguales ----------
function p03(L,t){const c=T.c03,xr=T.x_res,xt=T.x_tested,xc=T.x_cats3;
 const en=eio(seg(t,xr-.15,xr+.7)),ap=eio(seg(t,xt-.05,xt+.45)),sal=seg(t,xc-.05,xc+1.35);
 general(L,()=>{refugioFondo(L);modulo(L,0,1);modulo(L,820,-1);
  const a=.85-.15*seg(t,xc+1.3,T.c04);
  if(sal>0){gatoP(L+lerp(215,500,eio(sal)),1500,1.5,t,Object.assign({},NAR,{pose:'parado',camina:sal<1,agacha:a,inclina:.12-.2*golpe(t,xc+1.5,.5),cola:.6}));
   gatoP(L+lerp(1365,1080,eio(sal)),1500,1.5,t,Object.assign({},OSC,{pose:'parado',dir:-1,camina:sal<1,agacha:a,inclina:.12-.2*golpe(t,xc+1.65,.5),cola:.6}))}
  transportin(L+lerp(-330,165,en),1500,1,ap,.8);transportin(L+lerp(1910,1415,en),1500,-1,ap,.8);
  marcos(L,0);marcos(L,820)},lerp(ZG,.715,eio(seg(t,c,T.c04))))}
// ---------- P04 · vista cenital: a un lado llega una caja; al otro, nada ----------
function gatoArriba(x,y,a,s,C,b,t){X.save();X.translate(x,y);X.rotate(a);X.scale(s,s);X.lineCap='round';X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.16)';X.beginPath();X.ellipse(-4,10,lerp(108,78,b),lerp(54,68,b),0,0,7);X.fill();
 X.strokeStyle=C.color;X.lineWidth=22;X.beginPath();X.moveTo(-84,0);X.quadraticCurveTo(lerp(-150,-96,b),lerp(Math.sin(t*3)*16,74,b),lerp(-204,-10,b),lerp(Math.sin(t*3+1)*30,84,b));X.stroke();
 X.fillStyle=C.color;X.beginPath();X.ellipse(lerp(0,-8,b),0,lerp(100,70,b),lerp(48,62,b),0,0,7);X.fill();
 X.strokeStyle=C.oscuro;X.lineWidth=7;for(let i=-2;i<=1;i++){const q=i*lerp(26,18,b);X.beginPath();X.moveTo(q-8,-28);X.quadraticCurveTo(q+2,0,q-8,28);X.stroke()}
 if(b<.5){X.fillStyle=C.color2;[-1,1].forEach(d=>{X.beginPath();X.ellipse(94,d*30,18,12,0,0,7);X.fill()})}
 const hx=lerp(116,58,b),hy=lerp(0,30,b);X.fillStyle=C.color;[-1,1].forEach(d=>{X.beginPath();X.moveTo(hx-12,hy+d*18);X.lineTo(hx+2,hy+d*54);X.lineTo(hx+30,hy+d*26);X.closePath();X.fill()});
 X.beginPath();X.ellipse(hx+8,hy,40,38,0,0,7);X.fill();X.fillStyle=C.oscuro;X.beginPath();X.ellipse(hx,hy,13,22,0,0,7);X.fill();X.fillStyle='#f48fb1';X.beginPath();X.arc(hx+46,hy,5,0,7);X.fill();X.restore()}
function espacioArriba(x0,esp){X.save();X.translate(x0+240,0);X.scale(esp,1);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-232,572,480,940);X.fillStyle='#93a7b5';X.fillRect(-240,560,480,940);X.strokeStyle='#5f717c';X.lineWidth=18;X.strokeRect(-231,569,462,922);
 rr(-200,1300,170,130,18);X.fillStyle='#c98d8d';X.fill();trazo(LIN,3);X.strokeStyle='rgba(0,0,0,.14)';X.lineWidth=3;X.beginPath();X.moveTo(-200,1365);X.lineTo(-30,1365);X.stroke();
 X.fillStyle='#f4f1e8';X.beginPath();X.arc(150,1380,46,0,7);X.fill();trazo(LIN,3);X.fillStyle='#8a5a3a';X.beginPath();X.arc(150,1380,30,0,7);X.fill();X.restore()}
function cajaArriba(cx,cy){const w=210,h=250;X.lineJoin='round';X.fillStyle='rgba(0,0,0,.22)';X.fillRect(cx-w/2+10,cy-h/2+12,w,h+30);
 [-1,1].forEach(d=>{X.fillStyle=CARTON2;X.beginPath();X.moveTo(cx+d*w/2,cy+h/2);X.lineTo(cx+d*(w/2+46),cy+h/2+64);X.lineTo(cx+d*(w/2+20),cy+h/2+76);X.lineTo(cx+d*(w/2-34),cy+h/2);X.closePath();X.fill();trazo(LIN,3)});
 X.fillStyle=CARTON;X.fillRect(cx-w/2,cy-h/2,w,h);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(cx-w/2,cy-h/2,w,h);X.fillStyle='rgba(255,255,255,.2)';X.fillRect(cx-16,cy-h/2,32,h);
 X.fillStyle=DENTRO;X.fillRect(cx-w/2+6,cy+h/2-4,w-12,10)}
function andar(P,t){const p=P(t),q=P(t+.04),d=Math.hypot(q[0]-p[0],q[1]-p[1]);return [p[0],p[1],d>.6?Math.atan2(q[1]-p[1],q[0]-p[0]):null]}
let _aL=-1.57,_aR=-1.57;
function p04(L,t){const c=T.c04,xc=T.x_card,xo=T.x_other,BXc=250,BYc=880;
 const vuelta=(cx,cy,s)=>tt=>{const f=(tt-c)*1.25*s+1.2;return [cx+Math.cos(f)*70,cy+Math.sin(f)*120]};
 const izq=tt=>{const p=vuelta(280,1130,1)(Math.min(tt,xc+.42)),u=eio(seg(tt,xc+.42,xc+.85)),v=eio(seg(tt,xc+.85,xc+1.3));return [lerp(lerp(p[0],BXc,u),BXc,v),lerp(lerp(p[1],1085,u),BYc+30,v)]};
 const der=tt=>{const p=vuelta(800,1130,-1)(Math.min(tt,xo)),u=eio(seg(tt,xo,xo+.75));return [lerp(p[0],958,u),lerp(p[1],650,u)]};
 const a=andar(izq,t),b=andar(der,t);if(a[2]!==null)_aL=a[2];if(b[2]!==null)_aR=b[2];
 const cae=eio(seg(t,xc-.12,xc+.3)),bola=eio(seg(t,xo+.7,xo+1.05));
 X.fillStyle='#2c4051';X.fillRect(L-400,-500,1900,2900);espacioArriba(L+40,1);espacioArriba(L+560,-1);
 gatoArriba(L+a[0],a[1],t>xc+1.3?-1.57:_aL,1,NAR,0,t);
 if(cae>0){const y=lerp(300,BYc,cae);X.save();X.beginPath();X.rect(L+40,560,480,940);X.clip();cajaArriba(L+BXc,y);X.restore()}
 gatoArriba(L+b[0],b[1],bola>0?lerp(_aR,2.5,bola):_aR,1,OSC,bola,t);
 X.fillStyle='#5f717c';X.fillRect(L+522,548,36,964)}
// ---------- P05 · día tres: el gato con caja sale a explorar ----------
function p05a(L,t){const c=T.c05a,q=seg(t,c+.08,c+.5);
 refugioFondo(L);X.fillStyle='#3a5062';X.fillRect(L-300,-400,1700,860);X.fillStyle='#93a7b5';X.fillRect(L-300,460,1700,1800);X.fillStyle='rgba(0,0,0,.10)';X.fillRect(L-300,460,1700,14);
 hojaCal(L+540,636,500,'DAY','3');
 if(q<1){X.save();X.translate(L+290,760);X.rotate(q*q*1.1);X.globalAlpha=1-Math.pow(q,3);X.translate(-(L+290),-760+q*q*520);
  X.fillStyle='#fbf7ec';X.fillRect(L+290,756,500,450);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+290,756,500,450);txt('2',L+540,999,315,'#2a2019',{w:400});X.restore()}}
function p05b(L,t){const c=T.c05b,xa=T.x_already;
 const cm=ruta(t,[[c+.1,380,1355,1.316,540,965],[c+1.2,452,1185,1.3,540,1000]]);
 const gx=ruta(t,[[c+.05,358],[c+.5,462],[c+.75,462],[xa+.45,505],[T.c06,520]])[0],anda=(t>c+.05&&t<c+.5)||(t>c+.75&&t<xa+.45);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>{refugioFondo(L);modulo(L,0,1);modulo(L,820,-1);hojaCal(L+650,770,190,'DAY','3');
  cajaLado(L+BX,1500,'fondo');
  gatoP(L+gx+lerp(0,95,eio(seg(t,c+.75,xa+.45))),1500,1.5,t,Object.assign({},NAR,{pose:'parado',camina:anda,agacha:lerp(.7,.22,eio(seg(t,c+.75,xa+.45))),inclina:.1+.16*eio(seg(t,xa+.4,xa+.8)),cola:1.2}));
  cajaLado(L+BX,1500);marcos(L,0);marcos(L,820)})}
// ---------- P06 · el otro lado: el calendario corre y el gato sin caja sale mucho después ----------
function p06(L,t){const c=T.c06,xw=T.x_without,x2=T.x_two,xr=T.x_reach,N=8,d=(x2-.05-(xw-.2))/N;
 const n=Math.max(0,Math.min(N,Math.floor((t-(xw-.2))/d))),sale=seg(t,xr-.15,xr+1.25),cambia=seg(t,xr-.2,xr+.02);
 const cm=ruta(t,[[c,1200,1185,1.3],[xw-.3,1235,1200,1.42],[x2+.2,1190,1185,1.32],[T.c07,1170,1185,1.3]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{refugioFondo(L);modulo(L,0,1);modulo(L,820,-1);
  const fin=t>=x2-.05;hojaCal(L+1000,740,230,fin?'WEEKS':'DAY',fin?'2':'3',n>0&&!fin);
  for(let i=0;i<N;i++){const q=seg(t,xw-.2+i*d,xw-.2+i*d+.55);if(q>0&&q<1)hojaSuelta(L+1000-q*240-i%3*22,800+q*q*580,230,-q*(1.2+i%2*.6),1-q*q)}
  if(cambia<1)gatoP(L+1440,1500,1.5,t,Object.assign({},OSC,{pose:'sentado',agacha:.55,inclina:.3,cola:.4,alfa:1-cambia}));
  if(cambia>0)gatoP(L+lerp(1430,1215,eio(sale)),1500,1.5,t,Object.assign({},OSC,{pose:'parado',dir:-1,camina:sale>0&&sale<1,agacha:lerp(.75,.3,eio(sale)),inclina:.14-.1*eio(sale),cola:.8,alfa:cambia}));
  marcos(L,0);marcos(L,820)})}
// ---------- P07 · la misma comparación, otra vez: llega la caja, el gato entra, sale antes; al otro lado pasa una semana más ----------
function p07(L,t){const c=T.c07,xs=T.x_second,xc=T.x_cats8,xw=T.x_week;
 const llega=eio(seg(t,xs-.2,xs+.35)),bx=L+BX-(1-llega)*640;
 const entra=seg(t,xs+.42,xs+1.1),dentro=t>=xs+1.1&&t<xc-.05,sienta=seg(t,xc+.8,xc+.95);
 const gx=ruta(t,[[xc-.05,358],[xc+.28,462],[xc+.34,462],[xc+.8,600]])[0];
 general(L,()=>{refugioFondo(L);modulo(L,0,1);modulo(L,820,-1);
  cajaLado(bx,1500,'fondo');
  if(t<xs+1.1)gatoP(L+lerp(640,425,eio(entra))+6*Math.sin(t*2.1)*(1-seg(t,xs+.3,xs+.42)),1500,1.5,t,Object.assign({},NAR,{pose:'parado',dir:-1,camina:entra>0&&entra<1,agacha:.8,inclina:.14-.16*golpe(t,c+.35,.6)-.2*golpe(t,xs+.05,.4),cola:.6}));
  else if(!dentro){if(sienta<1)gatoP(L+gx,1500,1.5,t,Object.assign({},NAR,{pose:'parado',camina:t<xc+.8,agacha:lerp(.6,.2,seg(t,xc,xc+.8)),cola:1.2,alfa:1-sienta}));
   if(sienta>0)gatoP(L+640,1500,1.5,t,Object.assign({},NAR,{pose:'sentado',cola:1.4,lento:true,alfa:sienta}))}
  cajaLado(bx,1500);
  gatoP(L+1440,1500,1.5,t,Object.assign({},OSC,{pose:'sentado',agacha:.55,inclina:.3-.1*golpe(t,c+.9,.7)-.18*eio(seg(t,xw+.5,xw+.75)),cola:.4}));
  for(let i=0;i<7;i++){const q=back(seg(t,xw-.12+i*.085,xw+.1+i*.085));if(q>0){X.save();X.translate(L+888+i*104,830);X.scale(q,q);hojaCal(0,-66,94,'','',true);X.restore()}}
  marcos(L,0);marcos(L,820)})}
// ---------- P08 · en casa: se deja una caja y el gato se acomoda ----------
function casaAncha(L){casa(L);X.lineJoin='round';
 [[900,420,280,360],[1250,520,220,270]].forEach(q=>{X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L+q[0]+10,q[1]+12,q[2],q[3]);X.fillStyle='#e9e2d2';X.fillRect(L+q[0],q[1],q[2],q[3]);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+q[0],q[1],q[2],q[3]);X.fillStyle='#3d7f84';X.fillRect(L+q[0]+26,q[1]+26,q[2]-52,q[3]-52)});
 X.fillStyle='#b5533c';X.beginPath();X.ellipse(L+470,1590,560,70,0,0,7);X.fill();X.strokeStyle='rgba(255,255,255,.25)';X.lineWidth=6;X.beginPath();X.ellipse(L+470,1590,515,56,0,0,7);X.stroke();
 sillon(L+960,1500)}
function p08(L,t){const c=T.c08,xl=T.x_leave,xc=T.x_costs,k=T.x_tell;
 const cm=ruta(t,[[c,CG,1000,ZG,540,1000],[xc+.9,380,1355,1.15,368,1345]]);
 const entra=seg(t,xl+.4,xc+.7),gx=lerp(900,440,eio(entra)),fuera=seg(t,k-.1,k+.1);
 const deja=eio(seg(t,xl-.1,xl+.25)),se_va=eio(seg(t,xl+.2,xl+.9)),hx=L+BX+270+se_va*340,hy=1210+8*golpe(t,xl-.05,.3)-se_va*760,o=origen(hx,hy,-1.0,1.4,-1,118,44);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>{casaAncha(L);
  cajaLado(L+BX,1500,'fondo');
  if(fuera<1)gatoP(L+gx,1500,1.5,t,Object.assign({},CASA,{pose:'parado',dir:-1,camina:entra>0&&entra<1,agacha:lerp(.55,.3,entra),inclina:.1,cola:1,alfa:1-fuera}));
  if(fuera>0)gatoP(L+lerp(540,592,eio(seg(t,k-.1,k+.5))),1500,1.35,t,Object.assign({},CASA,{pose:'sentado',lento:true,cola:1.2,alfa:fuera}));
  cajaLado(L+BX,1500);
  if(se_va<1)manoLado(o[0],o[1],-1.0,1.4,-1,Object.assign({},MANO,{curl:[.3-.2*deja,.33-.2*deja,.36-.2*deja,.38-.2*deja],pulgar:.5+.3*deja}))});
 cierreCanal(L,t,k)}

NUEVOS.dc_cats16_p01=SET(p01);NUEVOS.dc_cats16_p02=SET(p02);NUEVOS.dc_cats16_p03=SET(p03);NUEVOS.dc_cats16_p04=SET(p04);NUEVOS.dc_cats16_p05a=SET(p05a);NUEVOS.dc_cats16_p05b=SET(p05b);
NUEVOS.dc_cats16_p06=SET(p06);NUEVOS.dc_cats16_p07=SET(p07);NUEVOS.dc_cats16_p08=SET(p08);
})();
// ===== DC · CATS16 · FIN =====
</script>
