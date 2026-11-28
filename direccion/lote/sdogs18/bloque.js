<script>
// ===== DC · SDOGS18 · INICIO ===== (Dogs 18h · NEVER Pet Another Dog in Front of YOURS · lote del 28-nov · una escena por línea del guion)
// Elementos que se repiten: el dueño (camisa verde), el peluche (azul grisáceo, lazo rojo, costura) y el perro del canal (dorado, collar rosa).
(function(){
const {cam,cierreCanal,SET}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,hojaP,tripode,tarj,desenfoca,borroso}=window.B28;
const PIEL='#e8b28c',CAM='#2f6b5a',CAM2='#27594b',PANT='#34435a',PELO='#3a2a22',ROS='#ff4f9a';
const PERRO={collar:'rosa'};

// ---------- dueño sentado, de lado, mirando a la izquierda. Origen: el piso bajo la cadera. o.h = mano [x,y] en coordenadas propias ----------
function dueno(x,yb,s,t,o){o=o||{};const h=o.h||[-190,-150];X.save();X.translate(x,yb);X.scale(s,s);X.lineCap='round';X.lineJoin='round';
 if(o.puf!==false){X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(30,4,160,16,0,0,7);X.fill();X.fillStyle=o.pufc||'#8a5a44';rr(-70,-150,210,150,34);X.fill();X.fillStyle='rgba(255,255,255,.09)';rr(-58,-142,186,20,10);X.fill();X.fillStyle='rgba(0,0,0,.12)';rr(-70,-40,210,40,20);X.fill()}
 if(o.libro){const b=o.libro;X.strokeStyle=CAM2;X.lineWidth=36;X.beginPath();X.moveTo(2,-372);X.lineTo(-70,-286);X.lineTo(b[0]+26,b[1]+30);X.stroke()}
 X.strokeStyle=PANT;X.lineWidth=60;X.beginPath();X.moveTo(40,-172);X.lineTo(-112,-174);X.stroke();X.lineWidth=50;X.beginPath();X.moveTo(-112,-174);X.lineTo(-126,-34);X.stroke();
 X.fillStyle='#2a2019';X.beginPath();X.ellipse(-148,-14,54,21,0,0,7);X.fill();
 X.save();X.translate(30,-172);X.rotate(-.07+(o.incl||0));X.fillStyle=CAM;rr(-66,-232,132,252,46);X.fill();X.fillStyle='rgba(0,0,0,.10)';rr(22,-222,40,232,20);X.fill();
 X.translate(-22,-296);X.rotate(o.cab||0);X.fillStyle=PIEL;rr(-12,34,34,42,10);X.fill();X.beginPath();X.arc(0,0,62,0,7);X.fill();X.beginPath();X.arc(-60,8,10,0,7);X.fill();
 X.fillStyle=PELO;X.beginPath();X.arc(5,-8,66,Math.PI*1.06,Math.PI*2.25);X.quadraticCurveTo(24,-26,-50,-36);X.closePath();X.fill();
 X.fillStyle='#2a2019';X.beginPath();X.ellipse(-34,-6,6,o.ojo===undefined?7:o.ojo,0,0,7);X.fill();
 X.strokeStyle='#8a3d33';X.lineWidth=5.5;X.beginPath();if(o.habla){X.ellipse(-40,22,9,7+5*Math.abs(Math.sin(t*11)),0,0,7)}else X.arc(-38,12,17,.55,2.2);X.stroke();X.restore();
 const sx=10,sy=-384,dx=h[0]-sx,dy=h[1]-sy,d=Math.max(1,Math.hypot(dx,dy)),k=Math.sqrt(Math.max(0,165*165-d*d/4))*.85,ex=sx+dx*.5+dy/d*k,ey=sy+dy*.5-dx/d*k;
 X.strokeStyle=CAM2;X.lineWidth=42;X.beginPath();X.moveTo(sx,sy);X.lineTo(ex,ey);X.stroke();X.strokeStyle=CAM;X.lineWidth=37;X.beginPath();X.moveTo(ex,ey);X.lineTo(h[0],h[1]);X.stroke();
 X.fillStyle=PIEL;X.beginPath();X.ellipse(h[0],h[1],28,19,o.mrot===undefined?-.2:o.mrot,0,0,7);X.fill();
 if(o.libro){const b=o.libro;libro(b[0],b[1],1,-.12)}
 X.restore()}
// mano que acaricia: va y viene sobre un punto
const caricia=(t,x,y,a)=>[x+Math.sin(t*5)*(a||26),y+Math.abs(Math.cos(t*5))*-10];
// ---------- peluche (mira a la derecha). mec: 0..1 cuánto se mueve el mecanismo de cola y cabeza ----------
function peluche(x,yb,s,t,o){o=o||{};const c='#9db4c8',c2='#eef3f6',osc='#6f879d',mv=o.mec===undefined?1:o.mec,w=Math.sin(t*9)*.5*mv,nb=Math.sin(t*4.5)*.07*mv;
 X.save();X.translate(x,yb);X.rotate(o.rot||0);X.scale(s*(o.dir||1),s);X.lineCap='round';
 X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,4,112,14,0,0,7);X.fill();
 X.save();X.translate(-66,-44);X.rotate(-.9+w);X.fillStyle=osc;rr(-12,-72,24,78,12);X.fill();X.restore();
 X.fillStyle=c;X.beginPath();X.ellipse(0,-78,84,82,0,0,7);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(24,-66,44,56,0,0,7);X.fill();
 X.strokeStyle='rgba(60,80,100,.6)';X.lineWidth=3;X.setLineDash([9,8]);X.beginPath();X.moveTo(24,-118);X.lineTo(24,-14);X.stroke();X.setLineDash([]);
 X.fillStyle=c;[[-50,-14],[58,-14]].forEach(p=>{X.beginPath();X.ellipse(p[0],p[1],34,20,0,0,7);X.fill()});X.fillStyle=c2;X.beginPath();X.ellipse(76,-12,14,10,0,0,7);X.fill();
 X.fillStyle=c;rr(30,-112,30,86,15);X.fill();
 X.fillStyle='#d8433f';[[-1],[1]].forEach(([q])=>{X.beginPath();X.moveTo(22,-150);X.lineTo(22+q*36,-172);X.lineTo(22+q*36,-130);X.closePath();X.fill()});X.beginPath();X.arc(22,-150,11,0,7);X.fill();
 X.save();X.translate(26,-214);X.rotate(nb);X.fillStyle=osc;X.beginPath();X.ellipse(-54,8,22,46,.25,0,7);X.fill();
 X.fillStyle=c;X.beginPath();X.arc(0,0,66,0,7);X.fill();{const g=X.createRadialGradient(-16,-24,8,0,0,70);g.addColorStop(0,'rgba(255,255,255,.16)');g.addColorStop(1,'rgba(0,0,0,.10)');X.fillStyle=g;X.beginPath();X.arc(0,0,66,0,7);X.fill()}
 X.fillStyle=c2;X.beginPath();X.ellipse(42,16,34,26,0,0,7);X.fill();X.fillStyle='#22262c';X.beginPath();X.arc(72,6,10,0,7);X.fill();
 X.beginPath();X.arc(16,-14,10,0,7);X.fill();X.strokeStyle='#fff';X.lineWidth=2.6;X.beginPath();X.moveTo(11,-19);X.lineTo(21,-9);X.moveTo(21,-19);X.lineTo(11,-9);X.stroke();
 X.strokeStyle='#22262c';X.lineWidth=3.5;X.beginPath();X.moveTo(70,16);X.quadraticCurveTo(56,34,40,30);X.stroke();
 X.fillStyle=osc;X.beginPath();X.ellipse(-12,-40,24,44,-.5,0,7);X.fill();X.restore();X.restore()}
function calabaza(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,4,104,13,0,0,7);X.fill();
 X.strokeStyle='#1d1d1f';X.lineWidth=9;X.beginPath();X.arc(0,-150,86,Math.PI*1.1,Math.PI*1.9);X.stroke();
 X.fillStyle=gl(-98,0,98,0,[[0,'#d9661c'],[.45,'#ff9130'],[1,'#c95512']]);X.beginPath();X.ellipse(0,-86,98,86,0,0,7);X.fill();
 X.strokeStyle='rgba(150,60,10,.4)';X.lineWidth=4;[26,56].forEach(q=>{[-1,1].forEach(d=>{X.beginPath();X.ellipse(d*q*.5,-86,q*.75+14,84,0,d<0?Math.PI*.5:-Math.PI*.5,d<0?Math.PI*1.5:Math.PI*.5);X.stroke()})});
 X.fillStyle='#2a1608';[-36,36].forEach(q=>{X.beginPath();X.moveTo(q-19,-92);X.lineTo(q,-124);X.lineTo(q+19,-92);X.closePath();X.fill()});
 X.beginPath();X.moveTo(-48,-64);X.lineTo(-24,-48);X.lineTo(-8,-60);X.lineTo(8,-48);X.lineTo(24,-60);X.lineTo(48,-64);X.quadraticCurveTo(0,-14,-48,-64);X.fill();
 X.fillStyle='rgba(255,255,255,.4)';X.beginPath();X.ellipse(-52,-128,13,27,.5,0,7);X.fill();X.fillStyle='#b54d10';rr(-72,-176,144,14,7);X.fill();X.restore()}
function libro(x,y,s,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.2)';rr(-104,-62,216,140,8);X.fill();X.fillStyle='#3b5ea8';rr(-110,-72,220,140,8);X.fill();
 X.fillStyle='#f4ecd8';rr(-102,-68,100,128,4);X.fill();rr(2,-68,100,128,4);X.fill();X.fillStyle='rgba(0,0,0,.12)';X.fillRect(-4,-68,8,128);
 X.fillStyle='rgba(60,45,30,.38)';for(let i=0;i<6;i++){rr(-92,-54+i*19,80*(.7+rnd(i)*.3),6,3);X.fill();rr(12,-54+i*19,80*(.7+rnd(i+7)*.3),6,3);X.fill()}X.restore()}
function ondas(x,y,dir,t,k,col){if(t<k)return;X.save();X.lineCap='round';for(let j=0;j<3;j++){const u=((t-k)*1.6+j/3)%1;X.strokeStyle=`rgba(${col||'255,255,255'},${.8*(1-u)})`;X.lineWidth=7;X.beginPath();X.arc(x,y,24+u*70,dir-.6,dir+.6);X.stroke()}X.restore()}
// ---------- perro del canal de espaldas, solo busto (primer plano) ----------
function busto(x,y,s,o){o=o||{};const c='#d9a35b',osc='#a8723a';X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 X.fillStyle=c;X.beginPath();X.moveTo(-94,0);X.lineTo(-106,-52);X.lineTo(-90,-122);X.lineTo(-64,-184);X.lineTo(-50,-226);X.lineTo(50,-226);X.lineTo(64,-184);X.lineTo(90,-122);X.lineTo(106,-52);X.lineTo(94,0);X.closePath();X.fill();
 {const g=X.createLinearGradient(-106,0,106,0);g.addColorStop(0,'rgba(0,0,0,.18)');g.addColorStop(.42,'rgba(255,255,255,.07)');g.addColorStop(1,'rgba(0,0,0,.12)');X.fillStyle=g;X.fillRect(-110,-230,220,232)}
 X.fillStyle='#e0508a';rr(-50,-236,100,22,10);X.fill();X.translate(0,-250);X.rotate(o.incl||0);const gi=o.gira||0;
 if(Math.abs(gi)>.05){X.fillStyle=c;X.beginPath();X.ellipse(gi*62,-34,34,24,0,0,7);X.fill();X.fillStyle='#2b1b14';X.beginPath();X.ellipse(gi*92,-38,10,9,0,0,7);X.fill()}
 X.fillStyle=c;X.beginPath();X.ellipse(0,-46,66,60,0,0,7);X.fill();
 X.fillStyle=osc;[-1,1].forEach(q=>{X.save();X.translate(q*56,-78);X.rotate(q*(.18-(o.or||0)*.5));X.beginPath();X.ellipse(q*8,34,24,46,0,0,7);X.fill();X.restore()});X.restore()}
// ---------- perro sentado de frente (para el cierre) ----------
function frente(x,yb,s,t){const c='#d9a35b',c2='#f3d9b0',osc='#a8723a';X.save();X.translate(x,yb);X.scale(s,s);X.lineCap='round';
 X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.ellipse(0,4,130,16,0,0,7);X.fill();
 X.save();X.translate(78,-40);X.rotate(.9+Math.sin(t*9)*.35);X.strokeStyle=c;X.lineWidth=24;X.beginPath();X.moveTo(0,0);X.lineTo(0,-86);X.stroke();X.restore();
 X.fillStyle=c;[-1,1].forEach(q=>{X.beginPath();X.ellipse(q*70,-42,50,42,0,0,7);X.fill()});X.fillStyle=c2;[-1,1].forEach(q=>{X.beginPath();X.ellipse(q*80,-9,30,14,0,0,7);X.fill()});
 X.fillStyle=c;X.beginPath();X.ellipse(0,-116,80,108,0,0,7);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(0,-124,44,72,0,0,7);X.fill();
 X.fillStyle=c;rr(-48,-116,36,114,15);X.fill();rr(12,-116,36,114,15);X.fill();X.fillStyle=c2;[-30,30].forEach(q=>{X.beginPath();X.ellipse(q,-7,23,12,0,0,7);X.fill()});
 X.fillStyle='#e0508a';rr(-48,-222,96,20,10);X.fill();X.fillStyle='#f0c23c';X.beginPath();X.arc(0,-196,9,0,7);X.fill();
 X.translate(0,-272);X.rotate(Math.sin(t*1.4)*.04);X.fillStyle=osc;[-1,1].forEach(q=>{X.save();X.translate(q*66,-18);X.rotate(q*.22);X.beginPath();X.ellipse(q*8,34,25,52,0,0,7);X.fill();X.restore()});
 X.fillStyle=c;X.beginPath();X.ellipse(0,0,76,66,0,0,7);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(0,24,40,32,0,0,7);X.fill();
 X.fillStyle='#2b1b14';X.beginPath();X.ellipse(0,8,15,11,0,0,7);X.fill();X.strokeStyle='#3a2416';X.lineWidth=3.5;X.beginPath();X.moveTo(0,19);X.lineTo(0,30);X.moveTo(-16,34);X.quadraticCurveTo(-6,42,0,30);X.quadraticCurveTo(6,42,16,34);X.stroke();
 X.fillStyle='#ff6f91';X.beginPath();X.ellipse(0,46+Math.sin(t*8)*1.5,10,12,0,0,7);X.fill();
 const bl=((t*1.3)%3.4)<.12?.15:1;X.fillStyle='#1b1b24';[-1,1].forEach(q=>{X.beginPath();X.ellipse(q*29,-16,8,10*bl,0,0,7);X.fill()});if(bl>.5){X.fillStyle='#fff';[-1,1].forEach(q=>{X.beginPath();X.arc(q*29+3,-20,3,0,7);X.fill()})}
 X.restore()}

// ---------- salones ----------
function salon(L,cm,t,o){o=o||{};const yp=o.yp||1400;interior(L,{p0:o.p0||'#6b4030',p1:o.p1||'#a2674a',tex:'tela',ta:.26,yp,pisoTex:o.piso||'madera',pa:o.pa});const px=par(cm,.4);
 if(o.ventana!==false)ventanaV(L+(o.vx||40)+px,yp-800,300,380,o.hora||'tarde',t,{arbol:1});
 if(o.sofa!==false)sofaV(L+(o.sx||300)+px*.7,yp+30,1.3,o.sofac||['#3f6f6a','#2c504c']);
 if(o.lamp!==false)lamparaPie(L+(o.lx||1040)+px,yp+20,1.5,true)}
function alfombra(L,y,col){X.fillStyle=col||'#7a3f4a';X.beginPath();X.ellipse(L+520,y,760,150,0,0,7);X.fill();X.save();X.beginPath();X.ellipse(L+520,y,760,150,0,0,7);X.clip();tex('tela',L-300,y-160,1700,320,{a:.3,v:3});X.restore();X.strokeStyle='rgba(255,255,255,.14)';X.lineWidth=8;X.beginPath();X.ellipse(L+520,y,700,126,0,0,7);X.stroke()}

// ---------- 01 · gancho: la mano acaricia el peluche; el perro real mira desde el primer plano. Cambio de foco de la mano al perro ----------
function p01(L,t){const xh=T.x_harmless,xp=T.x_personally,xc=T.x_careful,f=T.c02,foco=eio(seg(t,xp-.75,xp-.05)),m=caricia(t,-276,-322,24);
 const kf=[[0,600,1080,1.06],[xp-.6,540,1100,1.16],[xp+.3,470,1180,1.12],[f,440,1210,1.2]];
 plano(L,t,kf,cm=>{salon(L,cm,t,{sx:1500,vx:60,lx:1080});luz(L+1080,800,700,'255,196,120',.3);
  X.fillStyle='#5a3b2c';rr(L+290,1300,330,100,22);X.fill();X.fillStyle='#6d4836';rr(L+270,1284,370,40,18);X.fill();
  peluche(L+440,1286,1.05,t,{mec:.35});dueno(L+820,1400,1.25,t,{h:m,cab:.16})});
 desenfoca(7*foco);
 plano(L,t,kf,cm=>{X.fillStyle=gl(0,1350,0,1920,[[0,'rgba(20,10,6,0)'],[1,'rgba(20,10,6,.55)']]);X.fillRect(L-600,1350,2300,900);
  const gi=.75*eio(seg(t,xp-.5,xp)),or=eio(seg(t,xp-.3,xp+.1)),inc=-.09*eio(seg(t,xc-.1,xc+.3));
  borroso(8*(1-foco),()=>busto(L+250,2150,2.5,{gira:gi,or,incl:inc+Math.sin(t*1.3)*.012}))});
 arriba(L,.6)}

// ---------- 02 · 2014: visita a una casa. De la puerta al área de prueba; cuaderno en primer plano ----------
function p02(L,t){const c=T.c02,x36=T.x_36,f=T.c03;
 plano(L,t,[[c,330,1080,1.14],[c+1.2,380,1080,1.12],[x36+.4,700,1085,1.14],[f,730,1085,1.18]],cm=>{
  interior(L,{p0:'#6c7c66',p1:'#9aa686',tex:'tela',ta:.22,yp:1400,pisoTex:'madera'});const px=par(cm,.4);
  X.fillStyle='#e9e2d0';X.fillRect(L+30+px,560,340,850);cielo(L+56+px,586,288,820,'dia',t,3);haz(L+200+px,1000,L+560+px,1560,170,420,'255,246,220',.22);
  X.fillStyle='#7a5a40';X.fillRect(L+344+px,586,26,820);
  tripode(L+1010,1420,1.15);if(Math.sin(t*6)>-.2)luz(L+937,907,44,'255,60,50',.85);
  alfombra(L,1560,'#4f6a78');perro(L+770,1520,1.9,t,{pose:'echado',collar:'rosa',cola:3})});
 const a=eio(seg(t,c,c+.35)),n=eio(seg(t,x36-.1,x36+.3));
 X.save();X.translate(L+215,1612+(1-a)*500+Math.sin(t*1.8)*5);X.rotate(-.07);X.scale(.9,.9);X.fillStyle='rgba(0,0,0,.3)';rr(-190,-226,400,480,18);X.fill();X.fillStyle='#6b4a32';rr(-200,-240,400,480,18);X.fill();X.fillStyle='#b9bcc2';rr(-60,-262,120,50,10);X.fill();
 X.fillStyle='#f3ecd8';rr(-176,-206,352,426,6);X.fill();txt('2014',0,-140,84,'#2a2f38',{w:800});X.fillStyle='rgba(42,32,25,.25)';[0,1,2].forEach(i=>{rr(-140,-80+i*28,280*(.8-i*.15),9,4);X.fill()});
 if(n>0){X.globalAlpha=n;txt('36',-66,92,132,'#c0392b',{w:900});txt('DOGS',92,104,46,'#2a2f38',{w:800});X.globalAlpha=1}X.restore();
 arriba(L,.58)}

// ---------- 03 · el dueño ignora a su perro y acaricia el peluche, que ladra y mueve la cola ----------
function p03(L,t){const c=T.c03,xs=T.x_stuffed,xb=T.x_barked,xw=T.x_wagged,f=T.c04,mec=.25+.75*eio(seg(t,xb-.2,xb+.2)),m=caricia(t,-268,-300,24);
 plano(L,t,[[c,700,1090,1.22,-.02],[xs,690,1090,1.2,-.02],[xb+.2,520,1090,1.08,.012],[f,470,1090,1.1,.022]],cm=>{
  salon(L,cm,t,{p0:'#5f7a72',p1:'#8fa894',hora:'dia',sx:1600,vx:640,lx:1150});alfombra(L,1440,'#8a4a52');
  perro(L+150,1410,2,t,{pose:'sentado',collar:'rosa',cola:0,orejas:.3*eio(seg(t,xb,xb+.3)),mira:1});
  peluche(L+500,1410,1.1,t,{mec});ondas(L+590,1190,-.3,t,xb-.05,'255,255,255');
  dueno(L+850,1400,1.25,t,{h:m,cab:.14})});
 arriba(L,.6)}

// ---------- 04 · lo mismo con una calabaza de plástico y con un libro leído en voz alta (cortes por coincidencia) ----------
function p04(L,t){const c=T.c04,xp=T.x_pumpkin,xb=T.x_book,f=T.c05,e=t<xp-.3?0:t<xb-.3?1:2,k=[c,xp-.3,xb-.3][e],pop=.86+.14*eio(seg(t,k,k+.22));
 plano(L,t,[[c,640,1130,1.36],[f,610,1120,1.42]],cm=>{
  interior(L,{p0:'#4d4a6a',p1:'#77709a',tex:'tela',ta:.24,yp:1400,pisoTex:'madera'});lamparaPie(L+1130+par(cm,.4),1420,1.5,true);alfombra(L,1450,'#2f6f73');
  if(e===0){peluche(L+470,1410,1.1*pop,t,{mec:1});dueno(L+850,1400,1.25,t,{h:caricia(t,-268,-300,24),cab:.14})}
  else if(e===1){calabaza(L+480,1410,1.15*pop);dueno(L+850,1400,1.25,t,{h:caricia(t,-290,-250,20),cab:.16})}
  else{dueno(L+850,1400,1.25,t,{h:[-150,-300],libro:[-190,-322],cab:.2,habla:1,mrot:.9});ondas(L+720,880,Math.PI,t,k+.1,'255,236,200')}});
 arriba(L,.62)}

// ---------- banda de diez perros: n de ellos van hacia el dueño ----------
const ORD=[2,8,0,5,9,3,6,1,4,7];
function banda(L,t,k,n,o){const yp=1500;X.fillStyle=gl(0,0,0,1920,[[0,o.f0],[1,o.f1]]);X.fillRect(L-900,-900,2900,3800);tex('tela',L-400,300,1900,1700,{a:.16,v:4});
 X.fillStyle='rgba(0,0,0,.22)';rr(L+30,1180,1020,620,40);X.fill();X.fillStyle='rgba(255,255,255,.06)';rr(L+30,1180,1020,10,5);X.fill();
 luz(L+700,820,520,o.luz,.26);
 if(o.con==='libro')dueno(L+790,1060,.95,t,{h:[-150,-300],libro:[-190,-322],cab:.2,habla:1,mrot:.9});else{peluche(L+520,1066,.84,t,{mec:1});dueno(L+790,1060,.95,t,{h:caricia(t,-262,-300,22),cab:.14})}
 const DST=[[440,1085],[600,1100],[290,1105],[150,1135],[930,1150],[720,1165],[370,1172],[530,1176]];
 for(let i=0;i<10;i++){const sx=L+150+(i%5)*195,sy=1420+Math.floor(i/5)*300,r=ORD.indexOf(i),va=r<n,u=va?eio(seg(t,k+r*.09,k+.75+r*.09)):0;
  const x=va?lerp(sx,L+DST[r][0],u):sx,y=va?lerp(sy,DST[r][1],u):sy,dir=va&&L+DST[r][0]<sx-10?-1:1;
  if(va&&u>0)perro(x,y,.8,t,{pose:u<1?'parado':'sentado',camina:u<1,collar:'rosa',cola:7,dir:u<1?dir:(x<L+700?1:-1)});
  else perro(x,y,.8,t,{pose:'sentado',cola:0,color:'#5d6b78',color2:'#7c8a96',oscuro:'#48545f',lejos:'#525f6b',parpadeo:false})}}
function cifra(L,x,y,s,a,q){if(q<=0)return;X.save();X.globalAlpha=q;X.translate(L+x,y);X.scale(.8+.2*back(q),.8+.2*back(q));txt(s,0,0,150,'#fff',{w:900,g:18,gc:a});X.restore()}
// ---------- 05 · con el libro: 2 de cada 10 ----------
function p05(L,t){const c=T.c05,x2=T.x_2,f=T.c06;
 plano(L,t,[[c,440,1300,1.16],[x2-.1,640,1240,1.12],[f,560,1130,1.06]],cm=>{banda(L,t,x2-.25,2,{f0:'#1d2f40',f1:'#2f4a60',luz:'150,200,240',con:'libro'})});
 arriba(L,.6);cifra(L,250,620,'2 / 10','rgba(120,200,255,.9)',eio(seg(t,x2-.05,x2+.3)))}
// ---------- 06 · con el perro de mentira: casi 8 de cada 10 ----------
function p06(L,t){const c=T.c06,x8=T.x_8,f=T.c07;
 plano(L,t,[[c,560,1300,1.14],[x8-.1,540,1220,1.1],[f,540,1100,1.06]],cm=>{banda(L,t,x8-.45,8,{f0:'#3a1f33',f1:'#5c3250',luz:'255,150,190',con:'peluche'})});
 arriba(L,.6);cifra(L,250,620,'8 / 10','rgba(255,120,170,.95)',eio(seg(t,x8-.05,x8+.3)))}

// ---------- 07 · G2: el perro real se mete entre el dueño y el peluche; su cuerpo tapa parte del cuadro ----------
function p07(L,t){const c=T.c07,xw=T.x_worry,xf=T.x_further,f=T.c08,en=eio(seg(t,xw-.2,xf+.15)),g=golpe(t,xf,.5);
 plano(L,t,[[c,560,1150,1.06],[xw,540,1170,1.12],[xf,500,1200,1.3],[xf+.25,500,1204,1.34],[f,495,1200,1.3]],cm=>{
  salon(L,cm,t,{p0:'#3c2f4a',p1:'#62496a',hora:'noche',sx:1500,vx:80,lx:1120});luz(L+1120,800,640,'255,190,120',.3);alfombra(L,1450,'#6a3340');
  peluche(L+430,1410,1.1,t,{mec:1,rot:-.1*en});dueno(L+860,1400,1.25,t,{h:caricia(t,-300,-300,20),cab:.14+.1*en,ojo:7+3*en});
  perro(L+lerp(-620,330,en),1760,3.5,t,{pose:'parado',camina:en<.97,collar:'rosa',cola:9,orejas:.2});
  if(g>0)luz(L+560,1300,700,'255,220,170',.2*g)});
 arriba(L,.64)}

// ---------- 08 · cerca de un tercio se metió entre su dueño y el perro de mentira ----------
function p08(L,t){const c=T.c08,xs=T.x_squeezed,f=T.c09,en=eio(seg(t,c+.1,xs+.5));
 plano(L,t,[[c,440,1100,1.1],[xs+.5,560,1090,1.16],[f,575,1085,1.18]],cm=>{
  salon(L,cm,t,{p0:'#6f8794',p1:'#a3b9bd',hora:'dia',sx:1500,vx:420,lx:1160});alfombra(L,1440,'#b07a3c');
  peluche(L+lerp(330,230,en),1410,1.1,t,{mec:.6,rot:-.22*eio(seg(t,xs,xs+.5))});
  dueno(L+880,1400,1.25,t,{h:[-270+Math.sin(t*5)*18*en,-286],cab:.12});
  perro(L+lerp(-380,500,en),1410,2.35,t,{pose:'parado',camina:en<.98,collar:'rosa',cola:8,inclina:-.12*en})});
 arriba(L,.6)}

// ---------- 09 · algunos hasta le tiraron un mordisco: amago y corte antes del contacto ----------
function p09(L,t){const c=T.c09,xn=T.x_snapped,f=T.c10,u=eo(seg(t,xn-.16,xn+.04)),hold=seg(t,xn+.04,f);
 plano(L,t,[[c,250,1190,1.2],[xn-.16,262,1190,1.22],[xn+.06,640,1180,1.3],[f,646,1180,1.32]],cm=>{
  interior(L,{p0:'#3d5a52',p1:'#5f8474',tex:'tela',ta:.24,yp:1470,pisoTex:'madera'});alfombra(L,1560,'#8a4a52');
  peluche(L+850,1500,1.9,t,{mec:0,dir:-1,rot:.13*u});
  perro(L+lerp(-230,40,u),1530,2.6,t,{pose:'parado',collar:'rosa',cola:0,orejas:-.25*u,inclina:.14*u,parpadeo:false});
  if(u>.9){X.strokeStyle=`rgba(255,255,255,${.9*(1-hold*.6)})`;X.lineWidth=9;X.lineCap='round';[-.6,0,.6].forEach(a=>{const ox=L+622,oy=1066,r0=22,r1=58;X.beginPath();X.moveTo(ox+Math.sin(a)*r0,oy-Math.cos(a)*r0-10);X.lineTo(ox+Math.sin(a)*r1,oy-Math.cos(a)*r1-10);X.stroke()})}});
 arriba(L,.62)}

// ---------- 10 · la prueba salió de una que se usa con bebés de seis meses: dos esquemas en paralelo ----------
function icono(x,yb,s,col,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle=col;if(o.raya){X.setLineDash([10,8]);X.strokeStyle=col;X.lineWidth=6;X.beginPath();X.arc(0,-150,34,0,7);X.stroke();rr(-44,-108,88,108,30);X.stroke();X.setLineDash([])}else{X.beginPath();X.arc(0,-150,36,0,7);X.fill();rr(-46,-108,92,108,32);X.fill()}X.restore()}
function ficha(x,y,t,tipo,a6){hojaP(x,y,720,820,tipo?.02:-.025,()=>{X.fillStyle='rgba(42,32,25,.16)';rr(-300,-360,600,12,6);X.fill();
  X.strokeStyle='rgba(42,32,25,.35)';X.lineWidth=6;X.beginPath();X.moveTo(-300,300);X.lineTo(300,300);X.stroke();
  X.save();X.translate(0,100);icono(220,200,2.5,'#34435a');
  if(tipo){icono(-10,200,1.3,'#8a6f5a',{raya:1});icono(-220,200,1.55,'#e0508a');X.fillStyle='#fff';[-16,16].forEach(q=>{X.beginPath();X.arc(-220+q,200-236,7,0,7);X.fill()});
   if(a6>0){X.globalAlpha=a6;tarj(0,-370,420,110,18,'#2a2f38',{sa:.2});txt('6 MONTHS',0,-366,64,'#fff',{w:800});X.globalAlpha=1}}
  else{peluche(-10,200,.95,t,{mec:.5});perro(-230,200,1.5,t,{pose:'sentado',collar:'rosa',cola:5})}
  X.restore();X.strokeStyle='rgba(224,80,138,.85)';X.lineWidth=7;X.setLineDash([14,12]);X.beginPath();X.moveTo(-170,-70);X.quadraticCurveTo(20,-250,200,-190);X.stroke();X.setLineDash([])},'#f1e9d6')}
function p10(L,t){const c=T.c10,xs=T.x_six,f=T.c11;
 plano(L,t,[[c,470,1100,1.12],[xs-.5,520,1100,1.1],[xs+.35,1330,1100,1.12],[f,1370,1100,1.16]],cm=>{
  X.fillStyle='#5b3d2a';X.fillRect(L-900,-900,3800,3800);tex('madera',L-500,200,3000,1900,{a:.95,s:1.8,v:5});luz(L+900,700,1100,'255,220,170',.2);
  ficha(L+470,1130,t,0,0);ficha(L+1370,1130,t,1,eio(seg(t,xs-.05,xs+.3)))});
 arriba(L,.62)}

// ---------- 11 · parecían proteger su vínculo con el dueño: una línea une la mano con el perro; el peluche, fuera de foco ----------
function p11(L,t){const c=T.c11,xb=T.x_bond,f=T.c12,u=eio(seg(t,c+.5,c+1.6)),br=.5+.5*eio(seg(t,xb-.2,xb+.2));
 plano(L,t,[[c,540,1090,1.1],[f,585,1075,1.22]],cm=>{
  salon(L,cm,t,{sx:1500,vx:40,lx:1130});luz(L+760,900,760,'255,190,120',.3);alfombra(L,1440,'#7a3f4a');
  borroso(9,()=>{X.globalAlpha=.8;peluche(L+235,1410,1.05,t,{mec:.3});X.globalAlpha=1});
  perro(L+450,1410,2.1,t,{pose:'sentado',collar:'rosa',cola:6,inclina:-.3,mira:1});dueno(L+880,1400,1.25,t,{h:[-235,-250],cab:.16});
  const x0=L+880-235*1.25,y0=1400-250*1.25,x1=L+520,y1=1090;X.save();X.lineCap='round';
  [[30,.16],[14,.4],[6,1]].forEach(([w,a],i)=>{X.strokeStyle=i<2?`rgba(255,79,154,${a*br})`:`rgba(255,236,244,${a*br})`;X.lineWidth=w;X.beginPath();X.moveTo(x0,y0);const n=30;for(let j=1;j<=n*u;j++){const q=j/n;X.lineTo(lerp(x0,x1,q),lerp(y0,y1,q)+Math.sin(q*Math.PI)*46)}X.stroke()});
  if(u>=1)for(let j=0;j<3;j++){const q=(t*.6+j/3)%1;X.fillStyle=`rgba(255,255,255,${br})`;X.beginPath();X.arc(lerp(x0,x1,q),lerp(y0,y1,q)+Math.sin(q*Math.PI)*46,8,0,7);X.fill()}X.restore()});
 tinte(L,'255,170,90',.06);arriba(L,.6)}

// ---------- 12 · no es solo una caricia: alguien ocupa su lugar. El perro se interpone ----------
function p12(L,t){const c=T.c12,xp=T.x_place,f=T.c13,en=eio(seg(t,xp-1.1,xp-.1)),o=ruta(t,[[c,620,1090,1.16,-.13],[f,470,1090,1.1,.13]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{
  salon(L,{0:o[0]},t,{p0:'#553a5a',p1:'#86607c',hora:'tarde',sx:1500,vx:540,lx:1180});alfombra(L,1440,'#2f6f73');
  peluche(L+lerp(520,240,en),1410,1.1,t,{mec:.5*(1-en),rot:-.5*en});
  dueno(L+870,1400,1.25,t,{h:en<.6?caricia(t,-268,-300,22):caricia(t,-290,-262,22),cab:.14});
  perro(L+lerp(-420,470,en),1410,2.2,t,{pose:en<.98?'parado':'sentado',camina:en<.98,collar:'rosa',cola:9})},o[3]);
 arriba(L,.62)}

// ---------- 13 · CTA: el dueño acaricia a su propio perro, que mira a cámara ----------
function p13(L,t){const c=T.c13;
 plano(L,t,[[c,470,1180,1.14],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{
  salon(L,cm,t,{yp:1490,sx:1500,vx:1400,lx:1000});alfombra(L,1530,'#7a3f4a');
  dueno(L+590,1490,.74,t,{h:caricia(t,-300,-420,16),cab:.12});frente(L+350,1500,1.02,t)});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_sdogs18_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SDOGS18 · FIN =====
</script>
