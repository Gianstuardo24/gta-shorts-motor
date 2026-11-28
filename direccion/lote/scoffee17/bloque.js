<script>
// ===== DC · SCOFFEE17 · INICIO ===== (Coffee 17h · STOP Fixing Bitter Coffee With SUGAR · lote del 28-nov · una escena por línea del guion)
// Piezas del canal (taza crema con banda roja, manga mostaza, persona) vienen de DC_CAFE. Sin porcentajes ni puntajes: el guion no los da.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {taza,vapor,persona,MANO,CREMA,C_OK}=window.DC_CAFE;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,vaso,hojaP,renglones,tarj,desenfoca,borroso}=window.B28;
const AMARGO='96,58,140',DULCE='255,206,110',COBRE='255,170,100';

function salero(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.rotate(o.rot||0);X.scale(s,s);X.lineJoin='round';
 if(!o.sinSombra){X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(4,4,72,10,0,0,7);X.fill()}
 X.fillStyle='#fbfbf8';X.beginPath();X.moveTo(-48,-112);X.lineTo(48,-112);X.lineTo(54,-8);X.lineTo(-54,-8);X.closePath();X.fill();
 X.beginPath();X.moveTo(-44,-178);X.lineTo(44,-178);X.lineTo(58,-10);X.quadraticCurveTo(58,0,46,0);X.lineTo(-46,0);X.quadraticCurveTo(-58,0,-58,-10);X.closePath();X.fillStyle='rgba(214,236,238,.34)';X.fill();X.strokeStyle='rgba(235,246,250,.85)';X.lineWidth=5;X.stroke();
 X.fillStyle='rgba(255,255,255,.45)';rr(-40,-160,10,130,5);X.fill();
 X.fillStyle=gl(-50,0,50,0,[[0,'#8e98a4'],[.5,'#e2e7ec'],[1,'#7d8792']]);X.beginPath();X.moveTo(-48,-178);X.quadraticCurveTo(-46,-236,0,-238);X.quadraticCurveTo(46,-236,48,-178);X.closePath();X.fill();
 X.fillStyle='#3a424c';[[-18,-214],[0,-222],[18,-214],[-9,-200],[9,-200]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],4,0,7);X.fill()});X.restore()}
function azucarero(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(4,4,112,13,0,0,7);X.fill();
 if(o.cuchara!==false){X.strokeStyle='#b9bec6';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(20,-150);X.lineTo(86,-262);X.stroke()}
 X.fillStyle=gl(-90,0,90,0,[[0,'#d8cdb4'],[.45,'#f6efdf'],[1,'#c9bea4']]);X.beginPath();X.moveTo(-84,-150);X.lineTo(84,-150);X.quadraticCurveTo(100,-40,60,0);X.lineTo(-60,0);X.quadraticCurveTo(-100,-40,-84,-150);X.closePath();X.fill();
 X.fillStyle='#3f6f8a';X.fillRect(-90,-104,180,16);X.fillStyle='#e9e0cb';X.beginPath();X.ellipse(0,-150,84,16,0,0,7);X.fill();X.fillStyle='#fdfdfb';X.beginPath();X.ellipse(0,-152,68,26,0,Math.PI,0);X.fill();X.beginPath();X.ellipse(0,-152,68,10,0,0,7);X.fill();X.restore()}
function cuchara(x,y,rot,s,llena){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.strokeStyle='#b9bec6';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(0,0);X.lineTo(0,150);X.stroke();X.fillStyle='#c6ccd4';X.beginPath();X.ellipse(0,176,26,36,0,0,7);X.fill();if(llena>0){X.fillStyle='#fdfdfb';X.beginPath();X.ellipse(0,170,22*llena,28*llena,0,0,7);X.fill()}X.restore()}
// granos que caen de (x,y0) a y1: devuelve cuántos llegaron
function caen(x,y0,y1,t,k,n,o){o=o||{};let lleg=0;for(let i=0;i<n;i++){const u=(t-k-i*(o.cada||.07))/(o.dur||.55);if(u<0)continue;if(u>=1){lleg++;continue}const xx=x+(rnd(i+(o.sem||0))-.5)*(o.ancho||60)*(.4+u),yy=lerp(y0,y1,u*u);X.fillStyle=o.col||'#fdfdfb';if(o.cubo){X.save();X.translate(xx,yy);X.rotate(u*3+i);const r=o.r||7;X.fillRect(-r,-r,2*r,2*r);X.fillStyle='rgba(120,150,170,.35)';X.fillRect(-r,0,2*r,r);X.restore()}else{X.beginPath();X.arc(xx,yy,o.r||5,0,7);X.fill()}}return lleg}
// taza en perspectiva (boca ancha), para el macro del gancho
function tazaP(x,y,s,t,o){o=o||{};X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(10,356,300,34,0,0,7);X.fill();X.strokeStyle=CREMA;X.lineWidth=54;X.beginPath();X.arc(318,150,110,-1.2,1.3);X.stroke();
 X.fillStyle=gl(-300,0,300,0,[[0,'#d9cfb8'],[.4,CREMA],[1,'#cdbfa2']]);X.beginPath();X.moveTo(-300,0);X.quadraticCurveTo(-290,300,-190,350);X.lineTo(190,350);X.quadraticCurveTo(290,300,300,0);X.closePath();X.fill();
 X.fillStyle='#c8553d';X.beginPath();X.moveTo(-296,120);X.quadraticCurveTo(0,190,296,120);X.lineTo(290,180);X.quadraticCurveTo(0,250,-290,180);X.closePath();X.fill();
 X.fillStyle='#e3d9c2';X.beginPath();X.ellipse(0,0,300,112,0,0,7);X.fill();X.fillStyle='#2a170e';X.beginPath();X.ellipse(0,8,266,90,0,0,7);X.fill();
 X.save();X.beginPath();X.ellipse(0,8,266,90,0,0,7);X.clip();
 if(o.dulce>0){X.fillStyle=`rgba(${DULCE},${.42*o.dulce})`;X.fillRect(-270,-90,540,200)}
 if(o.amargo>0){const e=o.as||1;X.fillStyle=`rgba(6,2,10,${.85*o.amargo})`;X.beginPath();for(let i=0;i<=28;i++){const q=i/28*Math.PI*2,r=1+.16*Math.sin(q*3+t*1.6)+.08*Math.sin(q*5-t*2.1);X.lineTo(20+Math.cos(q)*150*r*e,8+Math.sin(q)*48*r*e)}X.closePath();X.fill();X.strokeStyle=`rgba(${AMARGO},${.7*o.amargo})`;X.lineWidth=5;X.stroke()}
 (o.ondas||[]).forEach(w=>{if(w.u>0&&w.u<1){X.strokeStyle=`rgba(255,240,220,${.6*(1-w.u)})`;X.lineWidth=4;X.beginPath();X.ellipse(w.x,8+w.y,30+w.u*90,(30+w.u*90)*.34,0,0,7);X.stroke()}});
 X.fillStyle='rgba(255,220,180,.16)';X.beginPath();X.ellipse(-110,-24,90,22,-.2,0,7);X.fill();X.restore();X.restore()}
// cocina del canal, con textura. yp: borde del mesón
function cocinaT(L,cm,o){o=o||{};const yp=o.yp||1380;interior(L,{p0:o.p0||'#1a323c',p1:o.p1||'#2c5263',tex:'baldosa',ta:.12,yp:yp+40});meson(L,yp,{tex:o.mt||'madera',col:o.mc||'#7a5636',ta:.92,v:o.mv||0});if(o.cobre!==false)luz(L+(o.lx||850)+par(cm,.4),o.ly||760,700,COBRE,o.la||.26)}
function placa(x,y,s,texto,a){if(a<=0)return;X.save();X.globalAlpha=a;tarj(x,y,230*s,96*s,14*s,'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,62*s,'#2a2f38',{w:800});X.restore()}
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({},MANO,o))};

// ---------- 01 · gancho: cae azúcar y se disuelve, pero la sombra amarga sigue; el foco pasa al salero del fondo ----------
function p01(L,t){const xs=T.x_stop,xa=T.x_another,xk=T.x_kitchen,f=T.c02,foco=eio(seg(t,xa-.6,xa+.1)),br=eio(seg(t,xk-.3,xk+.3));
 const kf=[[0,470,1280,1.75,-.05],[xs,470,1300,1.5,.02],[xa-.5,500,1260,1.12,.04],[xa+.4,640,1180,1.22,0],[xk+.4,760,1090,1.6,0],[f,770,1080,1.66,0]];
 plano(L,t,kf,cm=>{cocinaT(L,cm,{yp:1010,la:.3,lx:820,ly:700});if(br>0)luz(L+850,1010,330,COBRE,.5*br);salero(L+850,1130,1.15,{})});
 desenfoca(9*(1-foco));
 plano(L,t,kf,cm=>{const n=14,ond=[];let lleg=0;for(let i=0;i<n;i++){const u=(t-.5-i*.16)/.6;if(u>=1){lleg++;ond.push({u:(t-.5-i*.16-.6)/.7,x:(rnd(i)-.5)*260,y:(rnd(i+5)-.5)*50})}}
  const dul=Math.min(1,lleg/9)*(1-eio(seg(t,3.2,4.6))),am=eio(seg(t,.8,1.6)),as=1-.3*Math.sin(Math.min(1,lleg/n)*Math.PI)*(1-eio(seg(t,3,4)));
  borroso(7*foco,()=>{tazaP(L+470,1300,1.25,t,{dulce:dul,amargo:am,as,ondas:ond});
   for(let i=0;i<n;i++){const u=(t-.5-i*.16)/.6;if(u<0||u>=1)continue;X.fillStyle='#fdfdfb';const x=L+470+(rnd(i)-.5)*320,y=lerp(560,1306+(rnd(i+5)-.5)*60,u*u);for(let j=0;j<5;j++){X.beginPath();X.arc(x+(rnd(i*7+j)-.5)*46,y-(rnd(i*3+j))*60,6,0,7);X.fill()}}})});
 arriba(L,.62)}

// ---------- 02 · la mayoría estira la mano hacia el azúcar ----------
function p02(L,t){const c=T.c02,xr=T.x_reach,f=T.c03,g=eio(seg(t,xr-.1,xr+.25)),m=ruta(t,[[c,1320,980],[xr+.1,932,1108],[xr+.5,880,1010],[f-.3,470,1000],[f,440,1010]]),tom=t>xr+.1;
 plano(L,t,[[c,520,1240,1.24],[xr,640,1230,1.3],[f,500,1220,1.34]],cm=>{cocinaT(L,cm,{yp:1300,lx:200});
  taza(L+330,1520,1.5,{cafe:C_OK,asa:-1,rot:-.16*(1-eio(seg(t,c,c+.45)))});vapor(L+330,1230,t,.6,1.2);azucarero(L+800,1520,1.5,{cuchara:!tom});
  if(tom){const inc=-.5-1.3*eio(seg(t,f-.45,f-.1));cuchara(L+m[0],m[1],inc+Math.PI*.82,1.5,1-eio(seg(t,f-.3,f)));caen(L+m[0]-150,m[1]+190,1250,t,f-.4,16,{ancho:80,dur:.35,cada:.02})}
  mano(L+m[0],m[1],-.25,1.5,-1,{curl:[.5+.2*g,.54+.2*g,.58+.2*g,.6+.2*g],pulgar:.35,lx:150,ly:10})});
 arriba(L,.6)}

// ---------- 03 · el azúcar suma dulzor arriba; lo amargo sigue en la taza (corte a ras de la taza) ----------
function p03(L,t){const c=T.c03,xt=T.x_top,xb=T.x_but,xs=T.x_still,f=T.c04,d=eio(seg(t,c+.5,xt+.3)),al=eio(seg(t,xs-.3,xs+.2));
 plano(L,t,[[c,540,930,1.2],[xb-.2,540,960,1.24],[xb+.9,540,1250,1.26],[f,540,1280,1.3]],cm=>{
  X.fillStyle=gl(0,300,0,900,[[0,'#23404c'],[1,'#3d6a78']]);X.fillRect(L-900,-900,2900,1900);luz(L+800,620,620,COBRE,.3);
  X.fillStyle=gl(0,900,0,1900,[[0,'#3a2114'],[1,'#160b07']]);X.fillRect(L-900,900,2900,2900);
  X.fillStyle='#3a2114';X.beginPath();X.moveTo(L-100,930);for(let x=-100;x<=1180;x+=40)X.lineTo(L+x,900+Math.sin(x*.02+t*2.4)*9);X.lineTo(L+1180,960);X.lineTo(L-100,960);X.closePath();X.fill();
  X.fillStyle=gl(0,890,0,1130,[[0,`rgba(${DULCE},${.62*d})`],[1,`rgba(${DULCE},0)`]]);X.fillRect(L-100,890,1300,240);
  caen(L+540,360,900,t,c+.25,26,{ancho:420,dur:.6,cada:.07,r:7});for(let i=0;i<26;i++){const u=(t-c-.25-i*.07-.6)/.9;if(u>0&&u<1){X.fillStyle=`rgba(255,250,235,${.8*(1-u)})`;X.beginPath();X.arc(L+540+(rnd(i)-.5)*420*1.4,900+u*130,7*(1-u),0,7);X.fill()}}
  X.beginPath();X.moveTo(L-200,1470);for(let x=-200;x<=1280;x+=16)X.lineTo(L+x,1470+Math.sin(x*.008+t*1.5)*56+Math.sin(x*.019-t*2.2)*18);X.lineTo(L+1280,2300);X.lineTo(L-200,2300);X.closePath();X.fillStyle=gl(0,1400,0,1900,[[0,'rgba(34,14,46,.92)'],[1,'rgba(10,4,14,.96)']]);X.fill();X.strokeStyle=`rgba(${AMARGO},${.45+.5*al})`;X.lineWidth=6+6*al;X.stroke();
  X.fillStyle=CREMA;X.fillRect(L-140,300,150,1700);X.fillRect(L+1070,300,150,1700);X.fillStyle='rgba(0,0,0,.12)';X.fillRect(L+1070,300,30,1700)});
 arriba(L,.58)}

// ---------- 04 · 1997: laboratorio de degustación, vasos en fila, hojas de registro, una mano sirve ----------
function p04(L,t){const c=T.c04,f=T.c05,xi=T.x_tested;
 plano(L,t,[[c,330,1130,1.18],[f,820,1120,1.14]],cm=>{
  interior(L,{p0:'#3e5a66',p1:'#7a9aa4',tex:'baldosa',ta:.16,yp:1370});const px=par(cm,.3);placa(L+330+px,800,1.05,'1997',eio(seg(t,c+.05,c+.4)));luz(L+640,520,1000,'235,246,255',.22,620);
  meson(L,1330,{tex:'marmol',col:'#d9d5cc',ta:.9});
  ['#5a3420','#7a4a22','#3a2014','#8a5a2a','#4a2a18','#6a3e1e','#2f1a10'].forEach((cq,i)=>vaso(L+110+i*190,1330,1.35,{nivel:.5+.2*rnd(i),liq:cq}));
  hojaP(L+330,1560,330,250,-.1,()=>renglones(-130,-90,260,6,9,2));hojaP(L+900,1590,330,250,.08,()=>renglones(-130,-90,260,6,9,4));
  const sv=eio(seg(t,xi-.7,xi)),hx=L+870,hy=lerp(700,930,sv);
  X.save();X.translate(hx,hy);X.rotate(-.5-.5*sv);X.fillStyle='rgba(214,236,238,.3)';X.strokeStyle='rgba(235,246,250,.85)';X.lineWidth=5;rr(-60,-90,120,170,14);X.fill();X.stroke();X.fillStyle='#4a2a18';rr(-54,-20,108,94,10);X.fill();X.restore();
  if(sv>.9){X.strokeStyle='#4a2a18';X.lineWidth=11;X.lineCap='round';X.beginPath();X.moveTo(hx-84,hy+50);X.quadraticCurveTo(hx-100,hy+150,L+772,1160);X.stroke()}
  mano(hx+40,hy-10,-.2,1.25,-1,{curl:[.5,.54,.58,.6],pulgar:.35})});
 arriba(L,.58)}

// ---------- 05 · 21 voluntarios, bebidas que mezclaban amargo y dulce, y una nota para cada una ----------
function p05(L,t){const c=T.c05,x21=T.x_21,xm=T.x_mixed,xr=T.x_rate,f=T.c06,D=960;
 plano(L,t,[[c,540,1090,1.02],[xm-1.0,580,1090,1.04],[xm+.7,D+540,1090,1.04],[f,D+600,1090,1.08]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#1d2c38'],[1,'#31485a']]);X.fillRect(L-900,-900,4200,3800);tex('tela',L-400,300,3200,1700,{a:.14,v:4});luz(L+540,900,800,'150,200,240',.16);luz(L+D+560,1000,800,COBRE,.16);
  for(let i=0;i<21;i++){const x=L+180+(i%7)*120,y=760+Math.floor(i/7)*200,a=eio(seg(t,c+.1+i*.045,c+.3+i*.045))*(1-eio(seg(t,xm-1.3,xm-1.0)));if(a<=0)continue;X.globalAlpha=a;X.fillStyle=i%2?'#e9c46a':'#f4a261';X.beginPath();X.arc(x,y,30,0,7);X.fill();rr(x-36,y+38,72,70,26);X.fill();X.globalAlpha=1}
  const q=eio(seg(t,x21-.05,x21+.3));if(q>0){X.globalAlpha=q;txt('21',L+400,1500,200,'#fff',{w:900});txt('VOLUNTEERS',L+680,1512,56,'#cfe0ea',{w:800});X.globalAlpha=1}
  X.fillStyle='rgba(0,0,0,.25)';rr(L+D+80,1330,960,26,10);X.fill();
  [.75,.55,.4,.25].forEach((am,i)=>{const x=L+D+200+i*240,yb=1330,w=120,h=250;X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(x,yb+4,74,11,0,0,7);X.fill();
   X.fillStyle=`rgb(${DULCE})`;rr(x-w/2+8,yb-h*.7,w-16,h*.7,8);X.fill();X.fillStyle='#2a170e';rr(x-w/2+8,yb-h*.7*am,w-16,h*.7*am,8);X.fill();
   X.fillStyle='rgba(220,235,245,.16)';X.strokeStyle='rgba(235,245,255,.7)';X.lineWidth=5;rr(x-w/2,yb-h,w,h,12);X.fill();X.stroke();
   tarj(x,yb+140,200,84,16,'#efe6d0',{sa:.25});for(let j=0;j<5;j++){X.strokeStyle='#5a4a3a';X.lineWidth=4;X.beginPath();X.arc(x-72+j*36,yb+140,12,0,7);X.stroke()}
   if(t>xr){const j=Math.floor(((t-xr)*3.2+i*1.3)%5);X.fillStyle='rgba(224,80,60,.85)';X.beginPath();X.arc(x-72+j*36,yb+140,8,0,7);X.fill()}})});
 arriba(L,.6)}

// ---------- 06 · G2: la otra forma ya está en tu cocina. Una mano abre el cajón y encuentra un salero común ----------
function p06(L,t){const c=T.c06,xn=T.x_nobody,xa=T.x_already,f=T.c07,ab=eio(seg(t,c+.25,c+1.05)),sube=eio(seg(t,c+1.3,c+2.3)),br=eio(seg(t,xa-.4,xa+.2)),g=golpe(t,c+1.3,.6);
 const sy=lerp(1190,860,sube),d=ab*250;
 plano(L,t,[[c,540,1130,1.02],[c+1.1,540,1170,1.08],[c+2.3,545,1010,1.3],[f,548,980,1.46]],cm=>{
  X.fillStyle='#4a3020';X.fillRect(L-900,-900,2900,3800);tex('madera',L-400,300,1900,1900,{a:.9,s:1.7,v:8,tinte:'rgba(40,20,10,.35)'});luz(L+540,900,760,COBRE,.18+.3*br+.15*g);
  X.fillStyle='rgba(0,0,0,.35)';rr(L+120,560,840,330,18);X.fill();X.fillStyle='rgba(0,0,0,.35)';rr(L+120,1420+d*.2,840,330,18);X.fill();
  X.fillStyle='#17100b';X.beginPath();X.moveTo(L+150,980);X.lineTo(L+930,980);X.lineTo(L+960,980+d);X.lineTo(L+120,980+d);X.closePath();X.fill();
  if(d>20){X.save();X.beginPath();X.moveTo(L+150,700);X.lineTo(L+930,700);X.lineTo(L+960,980+d);X.lineTo(L+120,980+d);X.closePath();X.clip();
   X.strokeStyle='#b9bec6';X.lineWidth=12;X.lineCap='round';[[250,1010,300,1010+d*.8],[330,1004,360,1000+d*.8]].forEach(p=>{X.beginPath();X.moveTo(L+p[0],p[1]);X.lineTo(L+p[2],p[3]);X.stroke()});
   if(sube<.02)salero(L+560,lerp(1010,1190,ab),1.3,{sinSombra:1});X.restore()}
  X.fillStyle='#6b452c';rr(L+110,980+d,860,300,16);X.fill();tex('madera',L+110,980+d,860,300,{a:.55,s:1.2,v:9});X.fillStyle='rgba(255,255,255,.1)';rr(L+110,980+d,860,10,5);X.fill();X.fillStyle='#c9a45a';rr(L+430,1100+d,220,30,15);X.fill();
  if(sube>=.02){if(br>0)luz(L+560,sy-150,300,COBRE,.55*br);mano(L+640,sy-110,-.15,1.35,-1,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'atras',lx:118,ly:44});salero(L+560,sy,1.3+.1*br,{sinSombra:1});mano(L+640,sy-110,-.15,1.35,-1,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'pulgar',lx:118,ly:44})}
  else if(ab<1||t<c+1.3){const mx=lerp(1300,650,eio(seg(t,c,c+.25))),my=1115+d;mano(L+mx,my,-.1,1.3,-1,{curl:[.7,.74,.78,.8],pulgar:.3})}});
 arriba(L,.6)}

// ---------- 07 · no hace falta máquina nueva ni café más caro: de lo caro (al fondo, fuera de foco) a lo simple ----------
function maquina(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,4,200,18,0,0,7);X.fill();X.fillStyle=gl(-180,0,180,0,[[0,'#8e98a4'],[.5,'#dfe5ea'],[1,'#7d8792']]);rr(-180,-470,360,470,26);X.fill();X.fillStyle='#22262b';rr(-150,-300,300,200,14);X.fill();
 X.fillStyle='#22262b';rr(-180,-470,360,90,26);X.fill();[[-90,'#e4572e'],[0,'#f2c94c'],[90,'#6fcf97']].forEach(p=>{X.fillStyle=p[1];X.beginPath();X.arc(p[0],-425,16,0,7);X.fill()});X.fillStyle='#8e98a4';rr(-60,-300,120,40,10);X.fill();rr(-20,-262,40,40,6);X.fill();X.fillStyle='#55606a';rr(-160,-90,320,30,8);X.fill();X.restore()}
function bolsa(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,4,120,14,0,0,7);X.fill();X.fillStyle='#1c1c20';X.beginPath();X.moveTo(-100,0);X.lineTo(-90,-300);X.lineTo(-70,-340);X.lineTo(70,-340);X.lineTo(90,-300);X.lineTo(100,0);X.closePath();X.fill();
 X.fillStyle='#d9b24a';rr(-64,-230,128,130,10);X.fill();X.fillStyle='#1c1c20';X.beginPath();X.ellipse(0,-165,26,36,.4,0,7);X.fill();X.fillStyle='#d9b24a';[-36,0,36].forEach(q=>{X.beginPath();X.arc(q,-60,9,0,7);X.fill()});X.restore()}
function p07(L,t){const c=T.c07,xm=T.x_machine,xe=T.x_expensive,f=T.c08,a1=eio(seg(t,xm-.3,xm+.2)),a2=eio(seg(t,xe-.2,xe+.4));
 const kf=[[c,330,1130,1.16],[xm+.2,420,1130,1.16],[xe+.5,760,1150,1.24],[f,790,1150,1.3]];
 plano(L,t,kf,cm=>{cocinaT(L,cm,{yp:1380,lx:900});maquina(L+230,1380,1.15);if(a1>0){X.fillStyle=`rgba(10,18,24,${.6*a1})`;X.fillRect(L+10,820,440,570)}bolsa(L+540,1380,1.1);if(a2>0){X.fillStyle=`rgba(10,18,24,${.6*a2})`;X.fillRect(L+420,990,240,400)}});
 desenfoca(6);
 plano(L,t,kf,cm=>{luz(L+860,1250,420,COBRE,.2+.2*a2);taza(L+700,1560,1.5,{cafe:C_OK,asa:-1});vapor(L+700,1270,t,.6,1.2);salero(L+940,1560,1.3,{})});
 arriba(L,.6)}

// ---------- 08 · le agregaron un tipo de sal a esas bebidas amargas (macro del cristal hasta que se disuelve) ----------
function p08(L,t){const c=T.c08,xs=T.x_salt,f=T.c09,k=xs-.55,u=seg(t,k,k+1.9),cy=lerp(520,1420,u*u*(3-2*u)),en=cy>900,dis=eio(seg(cy,950,1420));
 plano(L,t,[[c,540,800,1.1],[k,540,780,1.2],[k+1.9,540,1300,1.5],[f,540,1320,1.54]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#2f4a56'],[1,'#57808c']]);X.fillRect(L-900,-900,2900,3800);[[200,500,120],[860,640,160],[520,380,90]].forEach(p=>luz(L+p[0],p[1],p[2],'235,246,255',.2));
  X.fillStyle=gl(0,900,0,1900,[[0,'#6a3e1e'],[1,'#2a170e']]);rr(L+170,900,740,1100,30);X.fill();X.fillStyle='rgba(255,230,190,.25)';X.fillRect(L+170,900,740,10);
  for(let i=1;i<5;i++){const yy=lerp(540,1300,Math.min(1,u*1.05))-i*110+rnd(i)*40,xx=L+540+(rnd(i+3)-.5)*260;if(yy<900){X.save();X.translate(xx,yy);X.rotate(t*2+i);X.fillStyle='rgba(250,252,255,.9)';X.fillRect(-11,-11,22,22);X.restore()}}
  if(dis<1){const r=30*(1-dis*.9);X.save();X.translate(L+540,cy);X.rotate(u*4);X.fillStyle=`rgba(250,252,255,${.95-.4*dis})`;X.fillRect(-r,-r,2*r,2*r);X.fillStyle='rgba(150,180,200,.35)';X.fillRect(-r,0,2*r,r);X.strokeStyle='rgba(255,255,255,.8)';X.lineWidth=3;X.strokeRect(-r,-r,2*r,2*r);X.restore()}
  if(en)for(let i=0;i<7;i++){const v=(dis*1.2+i/7)%1;X.strokeStyle=`rgba(255,255,255,${.5*(1-v)*Math.min(1,dis*3)})`;X.lineWidth=3;X.beginPath();X.moveTo(L+540+Math.sin(i*2)*20,cy-10);X.quadraticCurveTo(L+540+Math.sin(i*2.3)*90*v,cy-80*v,L+540+Math.sin(i*1.7)*140*v,cy-170*v);X.stroke()}
  const g=golpe(t,k+.72,.5);if(g>0){X.strokeStyle=`rgba(255,240,220,${g})`;X.lineWidth=6;X.beginPath();X.ellipse(L+540,904,60+120*(1-g),10+16*(1-g),0,0,7);X.stroke()}
  X.fillStyle='rgba(220,236,240,.14)';X.strokeStyle='rgba(235,246,250,.7)';X.lineWidth=12;rr(L+150,300,780,1750,40);X.fill();X.stroke();X.fillStyle='rgba(255,255,255,.22)';rr(L+190,360,26,1500,13);X.fill()});
 arriba(L,.6)}

// ---------- 09 · bajó el amargor y hasta supieron más dulces, sin azúcar extra ----------
function barras(x,y,am,du,la,ld){[[am,AMARGO,-62,'BITTER',la],[du,DULCE,62,'SWEET',ld]].forEach(([v,c,dx,tx,a])=>{X.fillStyle='rgba(255,255,255,.12)';rr(x+dx-30,y-300,60,300,16);X.fill();X.fillStyle=`rgb(${c})`;rr(x+dx-30,y-300*v,60,300*v,16);X.fill();if(a>0){X.globalAlpha=a;txt(tx,x+dx,y+36,27,'#e8eef2',{w:800});X.globalAlpha=1}})}
function p09(L,t){const c=T.c09,xd=T.x_dropped,xw=T.x_sweeter,xo=T.x_without,f=T.c10,baja=eio(seg(t,xd-.5,xd+.2)),sube=eio(seg(t,xw-.3,xw+.4)),la=eio(seg(t,c+.1,c+.5)),ld=eio(seg(t,xw-.3,xw));
 plano(L,t,[[c,490,1070,1.1],[xd+.3,540,1065,1.12],[f,580,1060,1.16]],cm=>{
  interior(L,{p0:'#2c3f4c',p1:'#4f6f7c',tex:'baldosa',ta:.14,yp:1420});meson(L,1380,{tex:'marmol',col:'#d9d5cc',ta:.9});luz(L+760,900,700,COBRE,.2*sube);
  vaso(L+300,1380,2,{nivel:.7,liq:'#3a2014'});vaso(L+770,1380,2,{nivel:.7,liq:'#4a2a18'});[300,770].forEach((x,k)=>{for(let i=0;i<5;i++){const u=(t*.45+i/5+k*.13)%1;X.fillStyle=`rgba(255,236,210,${.5*(1-u)})`;X.beginPath();X.arc(L+x+(rnd(i+k*7)-.5)*90,1370-u*190,5+3*rnd(i),0,7);X.fill()}});
  barras(L+300,1010,.85,.3,la,ld);barras(L+770,1010,lerp(.85,.42,baja),lerp(.3,.58,sube),la,ld);
  X.save();X.translate(L+770,640);X.rotate(.3);X.fillStyle='rgba(250,252,255,.95)';X.fillRect(-22,-22,44,44);X.fillStyle='rgba(150,180,200,.4)';X.fillRect(-22,0,44,22);X.restore();
  const q=eio(seg(t,xo-.2,xo+.2));if(q>0){X.globalAlpha=q;X.save();X.translate(L+990,1250);[[0,0],[40,0],[20,-34]].forEach(p=>{X.fillStyle='#fdfdfb';rr(p[0]-18,p[1]-34,36,34,5);X.fill()});X.strokeStyle='#e4572e';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(-34,-76);X.lineTo(76,12);X.stroke();X.restore();X.globalAlpha=1}});
 arriba(L,.6)}

// ---------- 10 · el sodio bloquea parte de la señal amarga en la lengua ----------
function p10(L,t){const c=T.c10,xs=T.x_sodium,xb=T.x_blocks,f=T.c11,baj=eio(seg(t,xs-.2,xb)),blo=eio(seg(t,xb-.1,xb+.25));
 plano(L,t,[[c,540,1020,1.06],[xb,540,1060,1.18],[f,540,1066,1.22]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#2a1830'],[1,'#4a2848']]);X.fillRect(L-900,-900,2900,3800);for(let i=0;i<7;i++)luz(L+rnd(i+4)*1080,500+rnd(i+13)*500,60+rnd(i+22)*70,'255,170,200',.1);
  X.fillStyle=gl(0,1200,0,1920,[[0,'#f08aa4'],[1,'#c95a7c']]);X.beginPath();X.moveTo(L-200,1330);X.quadraticCurveTo(L+540,1150,L+1280,1330);X.lineTo(L+1280,2100);X.lineTo(L-200,2100);X.closePath();X.fill();
  [200,430,650,880].forEach((x,i)=>{const yb=1262-Math.sin((x/1080)*Math.PI)*56,bl=(i%2===1)?blo:0;
   for(let j=0;j<3;j++){const u=((t-c)*.6+j/3+i*.17)%1,yy=lerp(520,yb-90,u);if(bl>.5&&u>.7)continue;X.fillStyle='rgba(150,100,210,.95)';X.beginPath();X.arc(L+x+Math.sin(u*5+i)*22,yy,19,0,7);X.fill()}
   X.fillStyle='#b84a70';X.beginPath();X.ellipse(L+x,yb,96,62,0,Math.PI,0);X.fill();X.fillStyle='#7a2b4c';X.beginPath();X.ellipse(L+x,yb-14,56,30,0,0,7);X.fill();
   for(let j=0;j<2;j++){const u=((t-c)*.9+j/2+i*.2)%1;X.fillStyle=`rgba(190,140,255,${.9*(1-u)*(1-bl)})`;X.beginPath();X.arc(L+x,yb+40+u*300,15,0,7);X.fill()}
   if(i%2===1&&baj>0){const yy=lerp(420,yb-50,baj);X.save();X.translate(L+x,yy);X.rotate((1-baj)*2);X.fillStyle='rgba(235,246,255,.96)';X.fillRect(-36,-36,72,72);X.fillStyle='rgba(120,170,220,.45)';X.fillRect(-36,0,72,36);X.restore()}});
  const q=eio(seg(t,xs-.05,xs+.3))*(1-eio(seg(t,f-.4,f-.1)));if(q>0){X.globalAlpha=q;tarj(L+540,700,300,90,18,'#e9f2fa',{sa:.25});txt('SODIUM',L+540,704,50,'#24384a',{w:800});X.globalAlpha=1}});
 arriba(L,.6)}

// ---------- 11 · en el café basta una pizca mínima ----------
function p11(L,t){const c=T.c11,xp=T.x_pinch,xe=T.x_enough,f=T.c12,k=xp-.15;
 plano(L,t,[[c,540,1200,1.1],[xp,560,1080,1.5],[xp+.9,545,1250,1.5],[f,540,1240,1.3]],cm=>{cocinaT(L,cm,{yp:1500,lx:220,la:.3});
  taza(L+540,1680,1.9,{cafe:C_OK,asa:1});vapor(L+540,1330,t,.5,1.4);
  caen(L+552,990,1322,t,k,6,{ancho:50,dur:.7,cada:.1,cubo:1,r:8});
  for(let i=0;i<6;i++){const u=(t-k-i*.1-.7)/.5;if(u>0&&u<1){X.strokeStyle=`rgba(255,240,220,${.7*(1-u)})`;X.lineWidth=4;X.beginPath();X.ellipse(L+540+(rnd(i)-.5)*60,1322,16+u*50,(16+u*50)*.26,0,0,7);X.stroke()}}
  mano(L+556,960,-.15,1.5,-1,{curl:[.42,.9,.95,.95],pulgar:.1,pulgarCurl:.5,lx:196,ly:-6})});
 arriba(L,.6)}

// ---------- 12 · la próxima vez: una pizca de sal antes que el azúcar ----------
function p12(L,t){const c=T.c12,xt=T.x_try,xb=T.x_before,f=T.c13,sub=eio(seg(t,xb-.2,xb+.5)),ty=lerp(1560,1090,sub);
 plano(L,t,[[c,470,1150,1.02],[xb,560,1090,1.08],[f,585,1060,1.12]],cm=>{cocinaT(L,cm,{yp:1380,lx:140,la:.3});borroso(4,()=>azucarero(L+110,1380,1.1,{}));
  persona(L,t,{dx:40,ty,trot:-.34*sub,cafe:C_OK,boca:{s:eio(seg(t,xb+.5,xb+1))}});vapor(L+610,ty-250,t,.5*(1-sub),1.2);
  if(sub<.05){caen(L+612,1150,ty-250,t,xt-.2,5,{ancho:40,dur:.5,cada:.09,cubo:1,r:7});const sa=eio(seg(t,c,c+.3))*(1-eio(seg(t,xt+.5,xt+.8)));if(sa>0)mano(L+lerp(-260,612,sa),1130,.12,1.35,1,{curl:[.42,.9,.95,.95],pulgar:.1,pulgarCurl:.5,lx:196,ly:-6})}});
 arriba(L,.55)}

// ---------- 13 · CTA: taza y salero; la mano duda antes de agregar ----------
function p13(L,t){const c=T.c13,du=Math.sin((t-c)*2.2);
 plano(L,t,[[c,440,1200,1.2],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{cocinaT(L,cm,{yp:1470,lx:250,la:.3});
  taza(L+300,1478,1.25,{cafe:C_OK,asa:-1});vapor(L+300,1240,t,.45,1);
  const sx=L+500+du*14,sy=1250-Math.abs(du)*12,rot=-.95+du*.2,hx=sx+96,hy=sy-64;mano(hx,hy,-.3,1.1,-1,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'atras',lx:118,ly:44});salero(sx,sy,1,{rot,sinSombra:1});mano(hx,hy,-.3,1.1,-1,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'pulgar',lx:118,ly:44})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_scoffee17_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SCOFFEE17 · FIN =====
</script>
