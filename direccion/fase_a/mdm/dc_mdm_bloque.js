<script>
// ===== DC_MDM · INICIO · fase A · MDM 18h, planos 01–04 (dirección V4, autorizada por Tao el 26-nov 23:14) =====
// Todo con prefijo dc_mdm_. Inerte: nada aquí se ejecuta salvo que una escena use estos sets.
// No dibuja ningún logo ni marca. Los planos 05A, 05B y 07–09 no están aquí.
(function(){
const LIN='rgba(40,27,18,.92)';
const K=k=>tk(k,window.__A||0);
const ramp=(t,a,b)=>eio(seg(t,a,b));
function cap(x1,y1,x2,y2,r){const a=Math.atan2(y2-y1,x2-x1);X.beginPath();X.arc(x1,y1,r,a+Math.PI/2,a+Math.PI*1.5);X.arc(x2,y2,r,a-Math.PI/2,a+Math.PI/2);X.closePath()}
function trazo(c,w){X.strokeStyle=c;X.lineWidth=w;X.stroke()}
function vineta(L,f){const v=X.createRadialGradient(L+540,1080,520,L+540,1080,1320);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,`rgba(8,5,3,${f})`);X.fillStyle=v;X.fillRect(L-300,-400,1680,3000)}

// ---------- manos ----------
// dedo de dos falanges desde el nudillo; devuelve la punta [x,y,ángulo]
function dedo(x,y,ang,l1,l2,r,curl,col,una,graf){l1*=1-.5*Math.min(1,curl);l2*=1-.38*Math.min(1,curl);const a1=ang+curl*1.25,a2=a1+curl*1.45,x1=x+Math.cos(a1)*l1,y1=y+Math.sin(a1)*l1,x2=x1+Math.cos(a2)*l2,y2=y1+Math.sin(a2)*l2;
 X.fillStyle=col;cap(x,y,x1,y1,r);X.fill();trazo(LIN,2.4);cap(x1,y1,x2,y2,r*.92);X.fill();trazo(LIN,2.4);X.beginPath();X.arc(x1,y1,r*.8,0,7);X.fill();
 if(graf){X.fillStyle='rgba(70,70,78,.55)';X.beginPath();X.ellipse(x1+Math.cos(a2)*l2*.45,y1+Math.sin(a2)*l2*.45,r*.55,r*.95,a2,0,7);X.fill()}
 if(una){const nx=Math.sin(a2),ny=-Math.cos(a2);X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(x2-Math.cos(a2)*r*.25+nx*r*.42,y2-Math.sin(a2)*r*.25+ny*r*.42,r*.62,r*.34,a2,0,7);X.fill()}
 return [x2,y2,a2]}
// mano de lado (dorso arriba). Muñeca en (0,0), apunta a +x (dir=-1: apunta a -x). parte: 'todo' | 'atras' | 'pulgar'
function manoLado(x,y,ang,s,dir,o){o=o||{};const parte=o.parte||'todo';X.save();X.translate(x,y);X.rotate(ang);X.scale(s*dir,s);X.lineJoin='round';X.lineCap='round';
 const sk=o.piel||'#e8b28c',sk2=o.piel2||'#cf9670',c=o.curl||[0,0,0,0];let p=null;
 if(parte!=='pulgar'){
  X.fillStyle=o.manga||'#27365a';X.beginPath();X.moveTo(-900,-64);X.lineTo(-54,-46);X.lineTo(-54,46);X.lineTo(-900,84);X.closePath();X.fill();trazo(LIN,3);
  X.strokeStyle='rgba(0,0,0,.18)';X.lineWidth=3;X.beginPath();X.moveTo(-860,30);X.lineTo(-90,22);X.stroke();
  X.fillStyle=o.puno||'#f1ede4';rr(-86,-53,64,106,12);X.fill();trazo(LIN,3);
  if(o.boton){X.fillStyle=o.boton;X.beginPath();X.arc(-54,22,7,0,7);X.fill();trazo(LIN,2)}
  X.fillStyle=sk;X.beginPath();X.moveTo(-26,-35);X.lineTo(10,-39);X.lineTo(10,38);X.lineTo(-26,35);X.closePath();X.fill();
  dedo(98,26,.14,44,36,12,c[3],sk2);dedo(104,14,.09,56,44,13.5,c[2],sk2);dedo(108,1,.04,62,50,15,c[1],sk2);
  X.fillStyle=gl(0,-50,0,52,[[0,sk],[.62,sk],[1,sk2]]);X.beginPath();X.moveTo(-24,-37);X.quadraticCurveTo(46,-53,108,-33);X.quadraticCurveTo(129,-4,112,32);X.quadraticCurveTo(56,52,-24,37);X.closePath();X.fill();trazo(LIN,2.4);
  X.strokeStyle='rgba(120,70,45,.35)';X.lineWidth=2;X.beginPath();X.arc(94,-22,10,3.5,5.3);X.stroke();
  if(o.entre)o.entre();
  p=dedo(106,-17,-.03,66,52,15,c[0],sk,true,o.graf)}
 if(parte!=='atras')dedo(34,30,o.pulgar===undefined?.5:o.pulgar,52,40,15,o.pulgarCurl===undefined?.08:o.pulgarCurl,sk,true);
 X.restore();return p}
// origen de la mano para que el punto local (lx,ly) caiga en (px,py)
function origen(px,py,ang,s,dir,lx,ly){const c=Math.cos(ang),n=Math.sin(ang);return [px-s*(dir*lx*c-ly*n),py-s*(dir*lx*n+ly*c)]}

// mano que escribe, vista desde arriba; la punta del lápiz queda en (tx,ty). esp=-1: mano izquierda (espejo)
function manoArriba(tx,ty,s,o){o=o||{};const esp=o.esp||1;X.save();X.translate(tx,ty);X.rotate(o.rot||0);X.scale(s*esp,s);X.lineJoin='round';X.lineCap='round';
 const sk=o.piel||'#e8b28c',sk2='#cf9670';
 // manga y puño (entra desde abajo)
 X.save();X.translate(228,236);X.rotate(1.02);X.fillStyle=o.manga||'#efe6d6';X.beginPath();X.moveTo(40,-92);X.lineTo(1500,-150);X.lineTo(1500,150);X.lineTo(40,92);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=o.puno||'#0e8f8a';rr(-22,-100,90,200,16);X.fill();trazo(LIN,3);if(o.boton){X.fillStyle=o.boton;X.beginPath();X.arc(24,62,10,0,7);X.fill();trazo(LIN,2)}X.restore();
 // dedos de abajo (anular y meñique recogidos)
 X.fillStyle=sk2;cap(168,150,128,166,17);X.fill();trazo(LIN,3);cap(152,124,112,134,18);X.fill();trazo(LIN,3);
 // dedo medio (apoya el lápiz)
 X.fillStyle=sk2;cap(136,96,82,72,18);X.fill();trazo(LIN,3);cap(82,72,36,42,16);X.fill();trazo(LIN,3);X.beginPath();X.arc(82,72,13,0,7);X.fill();
 // dorso
 X.fillStyle=sk;X.beginPath();X.moveTo(112,46);X.quadraticCurveTo(160,44,196,88);X.quadraticCurveTo(232,140,222,206);X.quadraticCurveTo(206,250,160,244);X.quadraticCurveTo(110,236,98,180);X.quadraticCurveTo(86,110,112,46);X.closePath();X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(120,70,45,.3)';X.lineWidth=2;[[132,66],[156,84],[176,108]].forEach(q=>{X.beginPath();X.arc(q[0],q[1],9,3.9,5.6);X.stroke()});
 // lápiz
 if(!o.sinLapiz){const ux=.8,uy=.6;X.save();X.rotate(Math.atan2(uy,ux));X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(0,0);X.lineTo(34,-9);X.lineTo(34,9);X.closePath();X.fill();trazo(LIN,2);X.fillStyle='#3a3a40';X.beginPath();X.moveTo(0,0);X.lineTo(11,-3);X.lineTo(11,3);X.closePath();X.fill();
  X.fillStyle='#b8382c';X.fillRect(34,-9,250,18);X.fillStyle='rgba(255,255,255,.22)';X.fillRect(34,-6,250,4);X.strokeStyle=LIN;X.lineWidth=2;X.strokeRect(34,-9,250,18);X.fillStyle='#c9c4b8';X.fillRect(284,-9,20,18);X.strokeRect(284,-9,20,18);X.fillStyle='#d98a86';rr(304,-9,22,18,5);X.fill();X.stroke();X.restore()}
 // índice y pulgar (encima del lápiz)
 X.fillStyle=sk;cap(128,70,88,36,18);X.fill();trazo(LIN,3);cap(88,36,52,20,16);X.fill();trazo(LIN,3);X.beginPath();X.arc(88,36,13,0,7);X.fill();
 if(o.graf){X.fillStyle='rgba(70,70,78,.5)';X.beginPath();X.ellipse(72,30,16,8,.42,0,7);X.fill()}
 X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(56,19,9,6,.42,0,7);X.fill();
 X.fillStyle=sk;cap(122,166,74,112,19);X.fill();trazo(LIN,3);cap(74,112,42,52,17);X.fill();trazo(LIN,3);X.beginPath();X.arc(74,112,14,0,7);X.fill();
 X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(44,60,7,10,-.5,0,7);X.fill();
 X.restore()}

// ---------- zapato sin marca (lateral vacío). Origen: centro de la suela sobre la mesa; punta a la izquierda ----------
function zapato(cx,by,s){X.save();X.translate(cx,by);X.scale(s,s);X.lineJoin='round';X.lineCap='round';
 // sombra de contacto
 const sh=X.createRadialGradient(0,6,10,0,6,360);sh.addColorStop(0,'rgba(20,12,6,.55)');sh.addColorStop(1,'rgba(20,12,6,0)');X.save();X.scale(1,.07);X.fillStyle=sh;X.beginPath();X.arc(0,90,360,0,7);X.fill();X.restore();
 // lengüeta (detrás)
 X.fillStyle='#e6e0d2';X.beginPath();X.moveTo(-6,-246);X.quadraticCurveTo(18,-306,74,-290);X.lineTo(70,-236);X.closePath();X.fill();trazo(LIN,3);
 // suela
 X.fillStyle='#5b4634';X.beginPath();X.moveTo(-296,0);X.lineTo(294,0);X.quadraticCurveTo(305,0,305,-12);X.lineTo(305,-24);X.lineTo(-300,-24);X.quadraticCurveTo(-326,-26,-331,-48);X.quadraticCurveTo(-338,-20,-296,0);X.closePath();X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(0,0,0,.28)';X.lineWidth=2;for(let i=-280;i<300;i+=22){X.beginPath();X.moveTo(i,-3);X.lineTo(i+8,-20);X.stroke()}
 // entresuela (cuña)
 X.fillStyle=gl(0,-70,0,-22,[[0,'#f3eee2'],[1,'#d8d1c0']]);X.beginPath();X.moveTo(-331,-48);X.quadraticCurveTo(-322,-26,-300,-24);X.lineTo(305,-24);X.lineTo(305,-70);X.quadraticCurveTo(110,-62,-150,-46);X.quadraticCurveTo(-280,-40,-331,-48);X.closePath();X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(120,105,85,.45)';X.lineWidth=2;X.beginPath();X.moveTo(-300,-36);X.lineTo(302,-48);X.stroke();
 // capellada
 const up=()=>{X.beginPath();X.moveTo(-331,-50);X.quadraticCurveTo(-334,-112,-252,-138);X.lineTo(-112,-196);X.lineTo(34,-266);X.quadraticCurveTo(140,-214,216,-252);X.quadraticCurveTo(250,-266,272,-262);X.quadraticCurveTo(314,-230,307,-150);X.quadraticCurveTo(301,-100,305,-68);X.quadraticCurveTo(110,-60,-150,-45);X.quadraticCurveTo(-280,-39,-331,-50);X.closePath()};
 X.fillStyle=gl(0,-270,0,-40,[[0,'#fbf9f3'],[.6,'#f1ede3'],[1,'#d9d2c2']]);up();X.fill();trazo(LIN,3.5);
 // puntera y talón (refuerzos)
 X.fillStyle='rgba(205,198,182,.75)';X.beginPath();X.moveTo(-331,-50);X.quadraticCurveTo(-334,-112,-252,-138);X.quadraticCurveTo(-222,-96,-214,-46);X.closePath();X.fill();trazo(LIN,2.5);
 X.beginPath();X.moveTo(216,-252);X.quadraticCurveTo(250,-266,272,-262);X.quadraticCurveTo(314,-230,307,-150);X.quadraticCurveTo(301,-100,305,-68);X.lineTo(214,-64);X.quadraticCurveTo(186,-150,216,-252);X.closePath();X.fill();trazo(LIN,2.5);
 X.fillStyle='#c9c1ae';X.beginPath();X.moveTo(252,-262);X.lineTo(296,-250);X.lineTo(292,-222);X.lineTo(250,-232);X.closePath();X.fill();trazo(LIN,2);
 // ojetera y cordón
 X.fillStyle='#e9e4d7';X.beginPath();X.moveTo(-150,-180);X.lineTo(30,-266);X.lineTo(66,-240);X.quadraticCurveTo(-22,-190,-118,-146);X.closePath();X.fill();trazo(LIN,2.5);
 for(let i=0;i<6;i++){const u=i/5,ex=lerp(-118,36,u),ey=lerp(-166,-240,u);X.fillStyle='#8f8779';X.beginPath();X.arc(ex,ey,6,0,7);X.fill();
  if(i<5){X.strokeStyle='#fffdf7';X.lineWidth=9;X.beginPath();X.moveTo(ex-2,ey+2);X.lineTo(ex+34,ey-38);X.stroke();X.strokeStyle=LIN;X.lineWidth=1.5;X.beginPath();X.moveTo(ex-6,ey);X.lineTo(ex+30,ey-41);X.moveTo(ex+2,ey+5);X.lineTo(ex+38,ey-35);X.stroke()}}
 X.strokeStyle='#fffdf7';X.lineWidth=8;X.beginPath();X.moveTo(40,-244);X.quadraticCurveTo(96,-300,118,-246);X.quadraticCurveTo(84,-226,44,-240);X.stroke();X.beginPath();X.moveTo(40,-244);X.quadraticCurveTo(2,-312,-34,-268);X.quadraticCurveTo(0,-240,38,-240);X.stroke();
 X.strokeStyle=LIN;X.lineWidth=1.5;X.beginPath();X.moveTo(40,-248);X.quadraticCurveTo(96,-306,122,-246);X.moveTo(40,-248);X.quadraticCurveTo(2,-318,-38,-268);X.stroke();
 // costuras
 X.setLineDash([7,6]);X.strokeStyle='rgba(120,110,95,.7)';X.lineWidth=2;X.beginPath();X.moveTo(-244,-128);X.quadraticCurveTo(-214,-92,-205,-52);X.moveTo(206,-240);X.quadraticCurveTo(180,-150,205,-70);X.moveTo(-140,-58);X.quadraticCurveTo(40,-72,198,-78);X.stroke();X.setLineDash([]);
 // brillo suave en el lateral vacío
 const br=X.createLinearGradient(-90,-200,170,-90);br.addColorStop(0,'rgba(255,255,255,.55)');br.addColorStop(1,'rgba(255,255,255,0)');X.fillStyle=br;X.beginPath();X.ellipse(40,-150,150,42,-.18,0,7);X.fill();
 X.restore()}

// ---------- taller de 1971 (planos 01 y 02): pared, lámpara, repisa y mesa a la altura del ojo ----------
function taller(L,sinRepisa,sinLampara){
 X.fillStyle=gl(0,0,0,1340,[[0,'#3c3a2c'],[.55,'#5a5338'],[1,'#6b6040']]);X.fillRect(L-900,-800,2900,2200);
 X.fillStyle='#3d2a1a';X.fillRect(L-900,1390,2900,1400); // base opaca bajo la mesa: sin costura entre canto y faldón
 if(!sinRepisa){X.fillStyle='#4a3a26';X.fillRect(L-400,838,830,22);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L-400,860,830,14);
  [[-60,150,120,'#8a6f4a'],[110,170,150,'#7d6442'],[300,112,104,'#917650']].forEach(b=>{X.fillStyle=b[3];X.fillRect(L+b[0],838-b[2],b[1],b[2]);X.strokeStyle='rgba(30,20,10,.5)';X.lineWidth=2;X.strokeRect(L+b[0],838-b[2],b[1],b[2]);X.fillStyle='rgba(0,0,0,.14)';X.fillRect(L+b[0],838-b[2],b[1],18)})}
 // lámpara de escritorio (fondo derecho, apunta al zapato)
 if(!sinLampara){X.strokeStyle='#243f37';X.lineWidth=14;X.lineCap='round';X.lineJoin='round';X.beginPath();X.moveTo(L+940,1312);X.lineTo(L+892,1010);X.lineTo(L+772,846);X.stroke();
 X.fillStyle='#2f5d4f';X.beginPath();X.moveTo(L+812,812);X.lineTo(L+722,774);X.lineTo(L+620,932);X.lineTo(L+772,952);X.closePath();X.fill();trazo('rgba(15,25,20,.8)',3);
 X.fillStyle='#fff3c9';X.beginPath();X.ellipse(L+696,944,76,16,.13,0,7);X.fill();
 X.fillStyle='#243f37';X.beginPath();X.ellipse(L+940,1312,74,14,0,0,7);X.fill()}
 const lg=X.createRadialGradient(L+520,1130,40,L+520,1130,900);lg.addColorStop(0,'rgba(255,224,160,.44)');lg.addColorStop(.5,'rgba(255,214,150,.14)');lg.addColorStop(1,'rgba(255,214,150,0)');X.fillStyle=lg;X.fillRect(L-900,-800,2900,2200);
 // mesa: superficie (casi de canto), canto y faldón
 X.fillStyle=gl(0,1308,0,1338,[[0,'#d9ad72'],[1,'#c4955c']]);X.fillRect(L-900,1308,2900,30);
 X.fillStyle=gl(0,1338,0,1408,[[0,'#a9783f'],[1,'#8a5e30']]);X.fillRect(L-900,1338,2900,70);
 X.strokeStyle='rgba(60,35,15,.35)';X.lineWidth=2;for(let i=0;i<9;i++){const y=1346+i*7+rnd(i)*3;X.beginPath();X.moveTo(L-900,y);X.bezierCurveTo(L-200,y+rnd(i+9)*8-4,L+600,y-rnd(i+4)*8+4,L+2000,y);X.stroke()}
 X.fillStyle='rgba(255,235,200,.35)';X.fillRect(L-900,1338,2900,3);
 X.fillStyle=gl(0,1408,0,2500,[[0,'#3d2a1a'],[.4,'#24180f'],[1,'#140d08']]);X.fillRect(L-900,1408,2900,1300);
 X.fillStyle='rgba(0,0,0,.35)';X.fillRect(L-900,1408,2900,10);
 X.fillStyle='#4a3520';X.fillRect(L-900,1712,2900,20);X.fillStyle='rgba(0,0,0,.4)';X.fillRect(L-900,1732,2900,12);
 const caja=(x,y,w,h,c)=>{X.fillStyle=c;X.fillRect(L+x,y-h,w,h);X.fillStyle='rgba(255,220,170,.10)';X.fillRect(L+x,y-h,w,h*.24);X.strokeStyle='rgba(15,9,4,.7)';X.lineWidth=2;X.strokeRect(L+x,y-h,w,h);X.beginPath();X.moveTo(L+x,y-h*.76);X.lineTo(L+x+w,y-h*.76);X.stroke()};
 [[-360,250,118,'#6e5436'],[-98,236,104,'#5f4930'],[150,262,124,'#75593a'],[424,240,110,'#644c32'],[676,250,120,'#6c5337'],[938,236,106,'#5d472f'],[1186,250,118,'#70563a']].forEach(b=>caja(b[0],1712,b[1],b[2],b[3]));
 [[-240,244,112,'#58432c'],[18,250,120,'#6a5136'],[282,238,108,'#5b452d'],[534,256,122,'#6f5538'],[802,240,110,'#5e4830'],[1054,250,116,'#69503a']].forEach(b=>caja(b[0],1712-126,b[1],b[2],b[3]));
 [[-330,250,118,'#5a442d'],[-60,246,112,'#674f35'],[204,256,124,'#59432c'],[474,240,110,'#6b5237'],[730,252,118,'#5c462e'],[996,244,112,'#66503a']].forEach(b=>caja(b[0],1990,b[1],b[2],b[3]));
 X.fillStyle=gl(0,1418,0,2100,[[0,'rgba(12,7,3,.25)'],[1,'rgba(12,7,3,.78)']]);X.fillRect(L-900,1418,2900,1100);
 X.fillStyle=gl(0,1408,0,2500,[[0,'#3a2717'],[1,'#22160c']]);X.fillRect(L+30,1408,44,1100);X.fillRect(L+1006,1408,44,1100)}

const CAROL={manga:'#efe6d6',puno:'#0e8f8a',boton:'#f2c230',piel:'#eab590',piel2:'#d39a76'};
const KNIGHT={manga:'#232f4d',puno:'#f4f1ea',piel:'#e3a985',piel2:'#c98f6b'};
const MY=1322; // línea de apoyo sobre la mesa

function p01(L,t){
 X.save();X.translate(0,-70);taller(L);
 const k0=K('x_asked')+.02,k1=K('c2')-.04,emp=eio(seg(t,k0,k1)),cx=620-180*emp-30*seg(t,k1,k1+.25),ES=.85;
 const rec=eio(seg(t,k1-.30,k1+.02));
 zapato(L+cx,MY,ES);
 // dedo de Knight toca el lateral vacío con "logo"
 const tA=K('x_needed')-.75,tT=K('x_logo'),tS=K('x_logo_fin')+.55;
 // entra con "Phil Knight" (queda a la vista y en suspenso) y toca con "logo"
 if(t>tA&&t<tS+.6){const en=.8*eio(seg(t,tA,tA+.6))+.2*eio(seg(t,tT-.24,tT)),sa=eio(seg(t,tS,tS+.55)),pr=Math.sin(seg(t,tT,tT+.22)*Math.PI)*7;
  const px=L+662+(1-en)*520+sa*560-pr,py=MY-128-(1-en)*40-sa*30,o=origen(px,py,-.2,1.45,-1,224,-20);
  if(en>=1&&sa<=0){X.fillStyle='rgba(60,40,20,.20)';X.beginPath();X.ellipse(px-6,py+10,24,11,0,0,7);X.fill()}
  manoLado(o[0],o[1],-.2,1.45,-1,Object.assign({},KNIGHT,{curl:[0,1.02,1.06,1.1],pulgar:.22,pulgarCurl:.25}))}
 // mano abierta de Knight empuja el talón con "He asked"
 const tE=K('x_asked')-.55;
 if(t>tE){const en=eio(seg(t,tE,k0)),hx=L+cx+272+(1-en)*420,hy=MY-100,o=origen(hx,hy,-.05,1.45,-1,224,-6);
  manoLado(o[0],o[1],-.05,1.45,-1,Object.assign({},KNIGHT,{curl:[.06,.08,.1,.12],pulgar:.35}))}
 // mano de Carolyn (puño de color) espera a la izquierda y recibe la punta
 manoLado(L+92-14*rec,MY-62-86*rec,-.02+.20*rec,1.15,1,Object.assign({},CAROL,{curl:[.10+.30*rec,.13+.30*rec,.16+.30*rec,.19+.28*rec],pulgar:.42+.1*rec,pulgarCurl:.02,graf:true}));
 X.restore();vineta(L,.5)}

function p02(L,t){
 // mismo taller y mismo eje (Carolyn a la izquierda, Knight a la derecha), más cerca y a ras de mesa.
 // Una sola mano y una sola acción: la mano que recibió el zapato lo suelta junto al papel, toma el lápiz y empieza a dibujar.
 const Z=1.5,CXW=372,CYW=1225,ES=.85,P=400;X.save();X.translate(L+540,1060);X.scale(Z,Z);X.translate(-(L+CXW),-CYW);
 taller(L,true,true);
 zapato(L+P+496,MY,ES);
 // papel en primer plano (casi de canto) y su sombra
 X.fillStyle='rgba(40,24,10,.28)';X.beginPath();X.moveTo(L+211,1318);X.lineTo(L+566,1318);X.lineTo(L+598,1340);X.lineTo(L+183,1340);X.closePath();X.fill();
 X.fillStyle='#fbf8ee';X.beginPath();X.moveTo(L+215,1314);X.lineTo(L+560,1314);X.lineTo(L+590,1334);X.lineTo(L+185,1334);X.closePath();X.fill();trazo('rgba(60,45,30,.6)',1.5);
 const lap=(x1,y1,x2,y2)=>{const an=Math.atan2(y2-y1,x2-x1),ln=Math.hypot(x2-x1,y2-y1);X.save();X.translate(x1,y1);X.rotate(an);X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(0,0);X.lineTo(20,-6);X.lineTo(20,6);X.closePath();X.fill();trazo(LIN,1.5);X.fillStyle='#3a3a40';X.beginPath();X.moveTo(0,0);X.lineTo(7,-2);X.lineTo(7,2);X.closePath();X.fill();
  X.fillStyle='#b8382c';X.fillRect(20,-6,ln-40,12);X.strokeStyle=LIN;X.lineWidth=1.5;X.strokeRect(20,-6,ln-40,12);X.fillStyle='#c9c4b8';X.fillRect(ln-20,-6,10,12);X.fillStyle='#d98a86';X.fillRect(ln-10,-6,10,12);X.strokeRect(ln-20,-6,20,12);X.restore()};
 // la mano entra por la izquierda (su lado): suelta la punta del zapato, toma el lápiz con "Carolyn" y dibuja (el papel queda de canto: el trazo no se ve)
 const a=K('c2'),tt=K('x_carolyn')-.10,tom=eio(seg(t,a+.22,tt)),esc=seg(t,tt+.30,tt+.48);
 // el lápiz se levanta pivotando sobre su punta hasta la inclinación con que queda en la mano (sin salto)
 if(tom<1){const lev=eio(seg(t,tt-.16,tt)),A=lerp(Math.atan2(-6,-236),-2.005,lev),ty=1326-5*lev;lap(L+P+20,ty,L+P+20+236*Math.cos(A),ty+236*Math.sin(A))}
 const w=Math.sin((t-tt)*12)*esc,px=L+lerp(P+20,P+4,eio(seg(t,tt+.05,tt+.4)))+9*w,py=1321-Math.sin(seg(t,tt,tt+.38)*Math.PI)*30,an=.04-.05*w;
 const o1=origen(px,py,an,1.25,1,190,150),ox=lerp(L+P-14,o1[0],tom),oy=lerp(1196,o1[1],tom)-Math.sin(tom*Math.PI)*26,ang=lerp(.12,an,tom);
 manoLado(ox,oy,ang,1.25,1,Object.assign({},CAROL,{curl:[lerp(.28,.55,tom),lerp(.32,.62,tom),lerp(.36,.7,tom),lerp(.40,.76,tom)],pulgar:.35,pulgarCurl:.02,graf:true,
  entre:tom>=1?()=>{X.save();X.translate(190,150);X.rotate(Math.atan2(-.89,-.456));X.scale(1/1.25,1/1.25);lapLocal();X.restore()}:null}));
 function lapLocal(){X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(0,0);X.lineTo(20,-6);X.lineTo(20,6);X.closePath();X.fill();trazo(LIN,1.5);X.fillStyle='#3a3a40';X.beginPath();X.moveTo(0,0);X.lineTo(7,-2);X.lineTo(7,2);X.closePath();X.fill();X.fillStyle='#b8382c';X.fillRect(20,-6,196,12);X.strokeStyle=LIN;X.lineWidth=1.5;X.strokeRect(20,-6,196,12);X.fillStyle='#c9c4b8';X.fillRect(216,-6,10,12);X.fillStyle='#d98a86';X.fillRect(226,-6,10,12);X.strokeRect(216,-6,20,12)}
 X.restore();vineta(L,.5)}

// ---------- letra manuscrita (trazos que se van dibujando) ----------
const G={'$':[[[.62,.24],[.46,.13],[.26,.15],[.15,.29],[.23,.44],[.42,.52],[.6,.63],[.65,.79],[.5,.9],[.3,.9],[.12,.79]],[[.4,.02],[.37,1.02]]],
 '2':[[[.12,.3],[.22,.15],[.42,.1],[.58,.2],[.6,.38],[.46,.58],[.12,.92],[.68,.9]]],
 '/':[[[.56,.04],[.1,1.02]]],
 'h':[[[.14,.04],[.12,.92]],[[.12,.62],[.3,.46],[.46,.52],[.5,.92]]],
 'r':[[[.14,.46],[.12,.92]],[[.13,.62],[.3,.47],[.48,.52]]],
 '3':[[[.14,.2],[.32,.1],[.54,.16],[.58,.34],[.36,.48],[.58,.6],[.62,.8],[.42,.92],[.14,.84]]],
 '5':[[[.6,.1],[.22,.1],[.17,.46],[.4,.42],[.6,.56],[.6,.78],[.4,.92],[.14,.84]]]};
const ANCHO={'$':.74,'2':.76,'/':.58,'h':.62,'r':.56,'3':.74,'5':.72};
function suav(P){const R=[];for(let i=0;i<P.length-1;i++){const p0=P[Math.max(0,i-1)],p1=P[i],p2=P[i+1],p3=P[Math.min(P.length-1,i+2)];for(let j=0;j<8;j++){const u=j/8,u2=u*u,u3=u2*u;
  R.push([.5*(2*p1[0]+(-p0[0]+p2[0])*u+(2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*u2+(-p0[0]+3*p1[0]-3*p2[0]+p3[0])*u3),.5*(2*p1[1]+(-p0[1]+p2[1])*u+(2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*u2+(-p0[1]+3*p1[1]-3*p2[1]+p3[1])*u3)])}}R.push(P[P.length-1]);return R}
function letras(str,x,y,h){const S=[];let cx=x;for(const ch of str){(G[ch]||[]).forEach(st=>{const P=st.length>2?suav(st):st;S.push(P.map(p=>[cx+p[0]*h*.78+(1-p[1])*h*.12,y+p[1]*h]))});cx+=(ANCHO[ch]||.6)*h*.78}return S}
function palitos(x,y,h,n,medio){const S=[];let cx=x;for(let i=0;i<n;i++){if(i%5===4){S.push([[cx-.8*h-10,y+h*.8],[cx-.2*h+16,y+h*.18]]);cx+=h*.3}else{S.push([[cx+(rnd(i*3.1)-.5)*5,y+rnd(i)*.06*h],[cx+(rnd(i*7.7)-.5)*5-3,y+h*(.94+rnd(i*5)*.06)]]);cx+=h*.2}}
 if(medio)S.push([[cx+2,y+h*.03],[cx,y+h*.5]]);return S}
function dibuja(S,q,w,col){let tot=0;S.forEach(P=>{for(let i=1;i<P.length;i++)tot+=Math.hypot(P[i][0]-P[i-1][0],P[i][1]-P[i-1][1])});tot*=cl(q);let pen=S[0][0];
 X.save();X.strokeStyle=col;X.lineWidth=w;X.lineCap='round';X.lineJoin='round';
 for(const P of S){if(tot<=0)break;X.beginPath();X.moveTo(P[0][0],P[0][1]);pen=P[0];for(let i=1;i<P.length;i++){const d=Math.hypot(P[i][0]-P[i-1][0],P[i][1]-P[i-1][1]);if(d<=tot){X.lineTo(P[i][0],P[i][1]);pen=P[i];tot-=d}else{const u=tot/d;pen=[lerp(P[i-1][0],P[i][0],u),lerp(P[i-1][1],P[i][1],u)];X.lineTo(pen[0],pen[1]);tot=0;break}}X.stroke()}
 X.restore();return pen}
// hoja de factura (820×1150 en su propio sistema). q1,q2,q3: avance de "$2/hr", los palitos y "$35". Devuelve los tres lápices (en coordenadas de la hoja)
const TX={a:letras('$2/hr',292,238,124),b:palitos(276,512,108,17,true),c:letras('$35',318,808,172)};
function hojaFactura(q1,q2,q3,dent){
 X.fillStyle=gl(0,0,820,1150,[[0,'#f8d94e'],[1,'#f0c738']]);X.beginPath();
 if(dent){X.moveTo(0,0);for(let i=0;i<41;i++){X.lineTo(i*20+10,i%2?0:7);X.lineTo(i*20+20,0)}X.lineTo(820,1150);X.lineTo(0,1150);X.closePath()}else X.rect(0,0,820,1150);
 X.fill();trazo('rgba(120,90,10,.55)',2);
 X.strokeStyle='rgba(150,115,20,.32)';X.lineWidth=2;for(let y=210;y<1100;y+=64){X.beginPath();X.moveTo(40,y);X.lineTo(780,y);X.stroke()}
 X.fillStyle='#5a3d1e';X.textBaseline='alphabetic';X.textAlign='left';X.font='700 62px P';X.fillText('INVOICE',56,122);X.fillRect(56,146,708,6);
 X.font='700 38px P';X.fillText('RATE',60,342);X.fillText('HOURS',60,602);X.fillText('TOTAL',60,912);
 X.strokeStyle='#5a3d1e';X.lineWidth=3;X.beginPath();X.moveTo(262,372);X.lineTo(764,372);X.moveTo(262,632);X.lineTo(764,632);X.stroke();X.lineWidth=5;X.strokeRect(262,772,502,236);
 const pa=dibuja(TX.a,q1,11,'#2b2a30'),pb=dibuja(TX.b,q2,10,'#2b2a30'),pc=dibuja(TX.c,q3,14,'#2b2a30');return [pa,pb,pc]}

function maderaArriba(L){X.fillStyle=gl(L,0,L+1080,1920,[[0,'#c99a60'],[1,'#a87840']]);X.fillRect(L-300,-400,1680,3000);
 for(let i=0;i<7;i++){const y=-100+i*330;X.fillStyle=`rgba(${i%2?70:255},${i%2?40:230},${i%2?15:190},.06)`;X.fillRect(L-300,y,1680,330);X.fillStyle='rgba(50,28,10,.45)';X.fillRect(L-300,y,1680,4);
  X.strokeStyle='rgba(70,40,15,.20)';X.lineWidth=2;for(let j=0;j<6;j++){const yy=y+30+j*52+rnd(i*7+j)*20;X.beginPath();X.moveTo(L-300,yy);X.bezierCurveTo(L+200,yy+rnd(i+j)*26-13,L+700,yy-rnd(i*3+j)*26+13,L+1380,yy+rnd(j)*10);X.stroke()}}
 const lg=X.createRadialGradient(L+300,700,60,L+300,700,1300);lg.addColorStop(0,'rgba(255,232,180,.34)');lg.addColorStop(1,'rgba(255,232,180,0)');X.fillStyle=lg;X.fillRect(L-300,-400,1680,3000)}

function p03(L,t){
 maderaArriba(L);
 const PX=L+130,PY=470; // esquina de la hoja
 const a1=K('x_2')-.05,a2=K('x_hour_fin'),b1=K('x_17'),b2=K('x_work_fin'),c1=K('x_35'),c2=K('x_35_fin'),r1=K('x_rasga'),r2=K('c4')-.02;
 const q1=seg(t,a1,a2),q2=seg(t,b1,b2),q3=seg(t,c1,c2),u=eio(seg(t,r1,r2));
 // talonario: lomo, hoja siguiente y talón

 X.fillStyle='rgba(30,16,6,.38)';X.fillRect(PX+14,PY-44,836,1220);
 X.fillStyle='#7a5a34';X.fillRect(PX-6,PY-56,832,70);X.strokeStyle=LIN;X.lineWidth=2;X.strokeRect(PX-6,PY-56,832,70);
 X.fillStyle='#f1ca3c';X.fillRect(PX,PY,820,1150);X.strokeStyle='rgba(120,90,10,.5)';X.strokeRect(PX,PY,820,1150);
 X.strokeStyle='rgba(150,115,20,.30)';X.lineWidth=2;for(let y=210;y<1100;y+=64){X.beginPath();X.moveTo(PX+40,PY+y);X.lineTo(PX+780,PY+y);X.stroke()}
 X.fillStyle='#f6d648';X.fillRect(PX,PY-4,820,18);X.setLineDash([6,8]);X.strokeStyle='rgba(90,60,10,.7)';X.lineWidth=2;X.beginPath();X.moveTo(PX,PY+14);X.lineTo(PX+820,PY+14);X.stroke();X.setLineDash([]);
 // hoja escrita (se arranca al final)
 X.save();X.translate(PX+820,PY+14);X.rotate(-.085*u);X.translate(-820-26*u,96*u);
 if(u>0){X.save();X.translate(22*u,30*u);X.fillStyle=`rgba(30,16,6,${.34*u})`;X.fillRect(0,0,820,1136);X.restore()}
 X.translate(0,0);const pens=(()=>{X.save();X.translate(0,-14);const r=hojaFactura(q1,q2,q3,u>0);X.restore();return r})();
 X.restore();
 // posición del lápiz: sigue el trazo activo y viaja entre renglones
 const W=p=>[PX+p[0],PY+p[1]];const A0=W(TX.a[0][0]),A1=W(pens[0]),B0=W(TX.b[0][0]),B1=W(pens[1]),C0=W(TX.c[0][0]),C1=W(pens[2]);
 let pen;if(t<a1)pen=[A0[0]+40*(1-eo(seg(t,a1-.5,a1))),A0[1]-30*(1-eo(seg(t,a1-.5,a1)))];else if(t<a2)pen=A1;else if(t<b1){const m=eio(seg(t,a2,b1));pen=[lerp(A1[0],B0[0],m),lerp(A1[1],B0[1],m)-Math.sin(m*Math.PI)*26]}
 else if(t<b2)pen=B1;else if(t<c1){const m=eio(seg(t,b2,c1));pen=[lerp(B1[0],C0[0],m),lerp(B1[1],C0[1],m)-Math.sin(m*Math.PI)*26]}else if(t<c2)pen=C1;else{const m=eio(seg(t,c2,c2+.3));pen=[C1[0]+m*90+u*240,C1[1]+m*36+u*420]}
 const sub=(t<a1||(t>=a2&&t<b1)||(t>=b2&&t<c1)||t>=c2);
 if(sub){X.fillStyle='rgba(30,16,6,.16)';X.beginPath();X.ellipse(pen[0]+150,pen[1]+190,150,96,.6,0,7);X.fill()}
 manoArriba(pen[0],pen[1],1.55,Object.assign({},CAROL,{graf:true,rot:-.04}));
 // mano izquierda: toma la esquina inferior y arranca la hoja por la perforación
 const en=eio(seg(t,r1-.3,r1));if(en>0){const hx=PX+70+70*u-(1-en)*360,hy=PY+1096+190*u+(1-en)*260;manoArriba(hx,hy,1.5,Object.assign({},CAROL,{esp:-1,sinLapiz:true,rot:.2,piel:'#dca783'}))}
 vineta(L,.42)}

// ---------- oficina de Knight (plano 04): corcho, factura clavada y carpeta rígida cerrada ----------
function chinche(x,y,c){X.fillStyle='rgba(20,10,5,.35)';X.beginPath();X.ellipse(x+5,y+8,13,9,0,0,7);X.fill();X.fillStyle=c;X.beginPath();X.arc(x,y,13,0,7);X.fill();trazo(LIN,2);X.fillStyle='rgba(255,255,255,.55)';X.beginPath();X.arc(x-4,y-4,4,0,7);X.fill()}
function carpeta(cx,cy,rot,pin){X.save();X.translate(cx,cy-246);X.rotate(rot);X.translate(0,246);
 X.fillStyle='rgba(20,10,5,.40)';rr(-158,-206,340,452,10);X.fill();
 // tapa trasera: asoma arriba una pestaña (por ahí se fija; la tapa delantera abre como puerta)
 X.fillStyle='#2c6a50';rr(-170,-250,340,472,8);X.fill();trazo(LIN,3);
 // tapa delantera, lomo de tela y esquinas
 X.fillStyle=gl(-170,-220,170,222,[[0,'#256048'],[1,'#1b4a37']]);rr(-170,-220,340,442,8);X.fill();trazo(LIN,3);
 X.fillStyle='#14251e';X.fillRect(-170,-220,46,442);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-170,-220,46,442);
 X.fillStyle='#14251e';X.beginPath();X.moveTo(170,-220);X.lineTo(120,-220);X.lineTo(170,-170);X.closePath();X.fill();X.beginPath();X.moveTo(170,222);X.lineTo(120,222);X.lineTo(170,172);X.closePath();X.fill();
 X.strokeStyle='rgba(255,255,255,.10)';X.lineWidth=2;X.strokeRect(-112,-208,270,418);
 X.fillStyle='#efe6cf';rr(-70,-150,190,74,6);X.fill();trazo(LIN,2);
 X.fillStyle='#b9b4a6';X.beginPath();X.arc(150,6,9,0,7);X.fill();trazo(LIN,2);
 if(pin)chinche(0,-236,'#c8372d');X.restore()}

function p04(L,t){
 // pared y corcho
 X.fillStyle=gl(0,0,0,1920,[[0,'#465660'],[1,'#2c373e']]);X.fillRect(L-300,-400,1680,3000);
 const lg=X.createRadialGradient(L+260,640,80,L+260,640,1200);lg.addColorStop(0,'rgba(255,236,200,.26)');lg.addColorStop(1,'rgba(255,236,200,0)');X.fillStyle=lg;X.fillRect(L-300,-400,1680,3000);
 X.fillStyle='rgba(10,8,6,.40)';rr(L+92,466,920,990,10);X.fill();
 X.fillStyle=gl(L+70,440,L+1010,1440,[[0,'#8a6238'],[1,'#6b4a28']]);rr(L+70,440,940,1000,10);X.fill();trazo(LIN,3);
 X.fillStyle='#c79d66';X.fillRect(L+104,474,872,932);X.strokeStyle='rgba(40,25,10,.6)';X.lineWidth=2;X.strokeRect(L+104,474,872,932);
 for(let i=0;i<420;i++){const x=L+108+rnd(i)*864,y=478+rnd(i+500)*924;X.fillStyle=i%3?'rgba(90,58,26,.28)':'rgba(255,232,190,.25)';X.fillRect(x,y,3+rnd(i*3)*4,2+rnd(i*5)*3)}
 X.fillStyle='rgba(30,18,8,.18)';X.fillRect(L+104,474,872,18);
 // factura clavada (la misma del plano 03)
 X.save();X.translate(L+150,600);X.rotate(-.03);X.fillStyle='rgba(30,16,6,.34)';X.fillRect(12,16,328,460);X.scale(.4,.4);hojaFactura(1,1,1,true);X.restore();chinche(L+312,618,'#2f6fb5');
 // tiempos de la duda
 const b0=K('x_love0')-.05,b1=K('x_love1'),s0=K('x_grow')-.05,s1=K('x_on')-.12,pinT=K('x_on')+.06,sol=K('x_on')+.30;
 const baja=eio(seg(t,b0,b1)),sube=eio(seg(t,s0,s1)),sue=eio(seg(t,sol,sol+.3)),osc=Math.sin(t*1.7)*3*(1-sube);
 const cx=L+708+18*baja*(1-sube)-6*sube,cy=lerp(lerp(958,1046,baja),912,sube)+osc,rot=lerp((.02+.07*baja)*(1-sube),-.075*(1-Math.exp(-(t-sol)*9)*Math.cos((t-sol)*16)),sue>0?1:0);
 // brazo derecho de Knight: dedos detrás de la carpeta, pulgar por delante
 const ret=eio(seg(t,sol,sol+.34)),hx=cx+196+ret*520,hy=cy+70+ret*460,an=.95;const o=origen(hx,hy,an,1.5,-1,60,10);
 const KN=Object.assign({},KNIGHT,{curl:[.16,.18,.2,.22],pulgar:.5,pulgarCurl:.05});
 manoLado(o[0],o[1],an,1.5,-1,Object.assign({},KN,{parte:'atras'}));
 carpeta(cx,cy,rot,t>=pinT);
 manoLado(o[0],o[1],an,1.5,-1,Object.assign({},KN,{parte:'pulgar'}));
 // mano izquierda: fija la pestaña con una chinche ("grow on him")
 const e0=s1-.42;if(t>e0&&t<sol+.6){const en=eio(seg(t,e0,pinT-.02)),sa=eio(seg(t,sol-.06,sol+.26)),px=cx+4-(1-en)*420-sa*900,py=cy-232+(1-en)*640+sa*1200;const o2=origen(px,py,-1.0,1.3,1,224,-20);
  if(t<pinT&&en>.2)chinche(px+2,py+4,'#c8372d');
  manoLado(o2[0],o2[1],-1.0,1.3,1,Object.assign({},KNIGHT,{curl:[0,1.02,1.06,1.1],pulgar:.22,pulgarCurl:.25}))}
 // hombro y espalda de Knight en primer término (nunca la cara)
 X.fillStyle='#161d30';X.beginPath();X.moveTo(L+470,2400);X.quadraticCurveTo(L+520,1760,L+760,1640);X.quadraticCurveTo(L+960,1560,L+1380,1600);X.lineTo(L+1380,2400);X.closePath();X.fill();
 X.strokeStyle='rgba(255,255,255,.07)';X.lineWidth=5;X.beginPath();X.moveTo(L+500,2100);X.quadraticCurveTo(L+540,1770,L+770,1652);X.quadraticCurveTo(L+960,1574,L+1380,1612);X.stroke();
 vineta(L,.5)}

const SET=f=>({osc:.1,luces(){return []},fondo(z,t,q){f(FV(z).L,t)}});
NUEVOS.dc_mdm_p01=SET(p01);NUEVOS.dc_mdm_p02=SET(p02);NUEVOS.dc_mdm_p03=SET(p03);NUEVOS.dc_mdm_p04=SET(p04);
})();
// ===== DC_MDM · FIN =====
</script>
