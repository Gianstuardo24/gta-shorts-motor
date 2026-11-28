<script>
// ===== DC · SDOGS14 · INICIO ===== (Dogs 14h · Don't TRUST Your Dog's Tail Wag · lote del 28-nov · una escena por línea del guion)
// Regla del video: el perro se ve de espaldas, así su derecha es la derecha de la pantalla. Verde azulado = lado derecho (acercarse); coral = lado izquierdo (alejarse). Los colores recién se explican en la línea 11.
(function(){
const {cam,cierreCanal,SET}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,pantalla,tripode,tarj}=window.B28;
const PERRO={c:'#d9a35b',c2:'#f6e2bd',osc:'#a8723a',collar:'#e0508a'},DOM={c:'#4d3d36',c2:'#8f7a6a',osc:'#2e2420',collar:'#3d6fb0'};
const VID={c:'#e6d9c2',c2:'#fff6e4',osc:'#b7a688'};
const ORO='255,214,110',VERDE='96,224,190',CORAL='255,120,96';
const wag=(t,b,a,w)=>b+a*Math.sin(t*(w||12));

// ---------- cola: gruesa en la base, pluma clara hacia la punta ----------
function cola(len,a,c,c2){const n=10,P=[[0,0]];for(let i=1;i<=n;i++){const u=i/n,q=a*(.3+.7*u);P.push([Math.sin(q)*len*u,-Math.cos(q)*len*u])}
 X.lineCap='round';X.lineJoin='round';
 X.strokeStyle='rgba(60,34,14,.5)';for(let i=1;i<=n;i++){X.lineWidth=48-24*(i/n);X.beginPath();X.moveTo(P[i-1][0],P[i-1][1]);X.lineTo(P[i][0],P[i][1]);X.stroke()}
 X.strokeStyle=c;for(let i=1;i<=n;i++){X.lineWidth=40-24*(i/n);X.beginPath();X.moveTo(P[i-1][0],P[i-1][1]);X.lineTo(P[i][0],P[i][1]);X.stroke()}
 X.strokeStyle=c2;for(let i=4;i<=n;i++){X.lineWidth=(40-24*(i/n))*.5;X.beginPath();X.moveTo(P[i-1][0],P[i-1][1]);X.lineTo(P[i][0],P[i][1]);X.stroke()}}
// ---------- perro de pie visto de espaldas. Origen: el suelo entre las patas. Base de la cola en (0,-262); largo 200. ----------
function dorso(x,yb,s,o){o=o||{};const c=o.c||PERRO.c,c2=o.c2||PERRO.c2,osc=o.osc||PERRO.osc,al=o.alerta||0,mi=o.mira||0;X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';
 if(!o.sinSombra){X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.ellipse(0,4,150,18,0,0,7);X.fill()}
 X.fillStyle=osc;rr(-24,-128,20,122,9);X.fill();rr(4,-128,20,122,9);X.fill();
 [-1,1].forEach(q=>{X.fillStyle=c;rr(q*58-28,-158,56,158,24);X.fill();X.fillStyle='rgba(0,0,0,.10)';rr(q*58-28+(q>0?36:0),-150,20,146,10);X.fill();X.fillStyle=osc;X.beginPath();X.ellipse(q*60,-7,35,16,0,0,7);X.fill()});
 X.fillStyle=osc;X.beginPath();X.ellipse(0,-290-al*8,90,84,0,0,7);X.fill();
 X.fillStyle=c;X.beginPath();X.ellipse(0,-192,114,98,0,0,7);X.fill();
 {const g=X.createRadialGradient(-34,-236,20,0,-192,128);g.addColorStop(0,'rgba(255,255,255,.13)');g.addColorStop(1,'rgba(0,0,0,.17)');X.fillStyle=g;X.beginPath();X.ellipse(0,-192,114,98,0,0,7);X.fill()}
 const hx=mi*22,hy=-412-al*14;
 if(o.collar){X.fillStyle=o.collar;rr(-46+hx*.5,-374-al*10,92,20,10);X.fill()}
 if(Math.abs(mi)>.12){X.fillStyle=c;X.beginPath();X.ellipse(hx+mi*56,hy+8,36,25,0,0,7);X.fill();X.fillStyle='#2b1b14';X.beginPath();X.ellipse(hx+mi*88,hy+4,11,10,0,0,7);X.fill()}
 X.fillStyle=c;X.beginPath();X.ellipse(hx,hy,63,57,0,0,7);X.fill();
 {const g=X.createRadialGradient(hx-12,hy-22,8,hx,hy,68);g.addColorStop(0,'rgba(255,255,255,.10)');g.addColorStop(1,'rgba(0,0,0,.12)');X.fillStyle=g;X.beginPath();X.ellipse(hx,hy,63,57,0,0,7);X.fill()}
 X.fillStyle=osc;[-1,1].forEach(q=>{X.save();X.translate(hx+q*53,hy-30);X.rotate(q*(.2-al*.6));X.beginPath();X.ellipse(q*8,30,22,45,0,0,7);X.fill();X.restore()});
 X.translate(0,-262);cola(o.largo||190,o.ang||0,c,c2);X.restore()}
// ---------- estela luminosa del recorrido de la punta ----------
function arco(bx,by,R,a0,a1,o){o=o||{};const al=o.a===undefined?1:o.a;if(al<=0||a1-a0<.005)return;X.save();X.lineCap='round';const rgb=o.rgb||ORO;
 [[58,.13],[30,.3],[11,.95]].forEach(([w,q],i)=>{X.strokeStyle=i<2?`rgba(${rgb},${q*al})`:`rgba(255,250,232,${q*al})`;X.lineWidth=w*(o.s||1);X.beginPath();X.arc(bx,by,R,-Math.PI/2+a0,-Math.PI/2+a1);X.stroke()});X.restore()}
function eje(bx,by,R,al){if(al<=0)return;X.save();X.strokeStyle=`rgba(255,255,255,${.75*al})`;X.lineWidth=6;X.lineCap='round';X.setLineDash([18,20]);X.beginPath();X.moveTo(bx,by-R*.3);X.lineTo(bx,by-R*1.2);X.stroke();X.setLineDash([]);X.restore()}
// extremos del recorrido entre k y t para una cola que se mueve como f(t)
function extremos(f,k,t){let a=f(k),b=a;const n=28;for(let i=1;i<=n;i++){const v=f(k+(t-k)*i/n);if(v<a)a=v;if(v>b)b=v}return [a,b]}

// ---------- sala de casa (cálida) ----------
function sala(L,cm,t,o){o=o||{};interior(L,{p0:'#6b4030',p1:'#a2674a',tex:'tela',ta:.26,yp:o.yp||1560,pisoTex:'madera'});const px=par(cm,.45),yp=o.yp||1560;
 ventanaV(L+70+px,yp-880,300,380,'tarde',t,{arbol:1});
 sofaV(L+790+px*.8,yp+40,1.25,['#3f6f6a','#2c504c']);lamparaPie(L+1010+px,yp+30,1.5,true)}
// ---------- sala de observación (verde grisácea, metal cepillado, luz blanca) ----------
function obs(L,cm,o){o=o||{};const yp=o.yp||1360;interior(L,{p0:o.p0||'#4f6058',p1:o.p1||'#76897e',tex:'concreto',ta:.2,yp,piso:o.piso||['#8d969b','#7e878c'],paso:170});
 const px=par(cm,.3);tex('metal',L-260+px,yp-760,520,560,{a:.85,v:1});X.strokeStyle='rgba(0,0,0,.25)';X.lineWidth=6;X.strokeRect(L-260+px,yp-760,520,560);
 tex('metal',L+900+px,yp-900,520,700,{a:.7,v:1});X.strokeRect(L+900+px,yp-900,520,700)}
function marcas(L,x,y,s){X.strokeStyle='rgba(255,255,255,.75)';X.lineWidth=9*s;X.lineCap='butt';[[-1,-1],[1,-1],[-1,1],[1,1]].forEach(([a,b])=>{const cx=L+x+a*210*s,cy=y+b*52*s;X.beginPath();X.moveTo(cx-a*46*s,cy);X.lineTo(cx,cy);X.lineTo(cx-a*14*s,cy-b*26*s);X.stroke()})}
function placa(x,y,s,texto,a){if(a<=0)return;X.save();X.globalAlpha=a;tarj(x,y,230*s,96*s,14*s,'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,62*s,'#2a2f38',{w:800});X.restore()}

// ---------- 01 · gancho: primerísimo plano de la cola; se congela y la estela muestra hacia dónde se carga ----------
function p01(L,t){const xh=T.x_happy,xw=T.x_wrong,xd=T.x_detail,f=T.c02,S=2.7,yb=2010,bx=L+540,by=yb-262*S,R=190*S;
 const fr=eio(seg(t,xw-.3,xw+.05)),a=lerp(wag(t,.28,.52,13),.8,fr),tr=eio(seg(t,xw+.05,xw+.75)),frio=eio(seg(t,xw-.25,xw+.7)),det=eio(seg(t,xd-.1,xd+.35));
 plano(L,t,[[0,440,1010,1.5],[xh,570,1000,1.44],[xw-.25,640,1000,1.4],[xw+.8,540,1030,1.14],[xd,540,1030,1.14],[f,580,990,1.26]],cm=>{
  sala(L,cm,t);luz(L+1010+par(cm,.45),980,700,'255,196,120',.34*(1-.55*frio));
  dorso(bx,yb,S,Object.assign({},PERRO,{ang:a}));
  eje(bx,by,R,tr);arco(bx,by,R,lerp(.8,-.24,tr),.8,{});
  if(det>0)arco(bx,by,R,.24,.8,{rgb:'255,96,170',a:det*(.75+.25*Math.sin(t*7))})});
 tinte(L,'40,92,176',.11*frio);arriba(L,.62)}

// ---------- 02 · 2007: sala de observación, cámara en trípode, marcas en el piso ----------
function p02(L,t){const c=T.c02,f=T.c03,xf=T.x_filmed;
 plano(L,t,[[c,300,1090,1.3],[c+1,330,1090,1.28],[xf+1,690,1080,1.16],[f,720,1075,1.2]],cm=>{
  obs(L,cm);placa(L+560+par(cm,.3),850,1.05,'2007',eio(seg(t,c+.05,c+.4)));
  luz(L+640,520,900,'235,246,255',.22,700);marcas(L,690,1600,1.25);
  tripode(L+170,1640,1.75);if(t>xf&&Math.sin((t-xf)*7)>-.2)luz(L+58,860,60,'255,60,50',.9);
  perro(L+700,1610,2.2,t,{pose:'parado',collar:'rosa',cola:5})});
 arriba(L,.55)}

// ---------- 03 · los cuatro estímulos entran por lados distintos; el perro (de espaldas) es la referencia ----------
function p03(L,t){const c=T.c03,xs=T.x_stranger,xc=T.x_cat,xd=T.x_dom,f=T.c04,K=[c,xs,xc,xd,f];
 const e=i=>eio(seg(t,K[i]-.02,K[i]+.3))*(1-eio(seg(t,K[i+1]-.22,K[i+1]+.02))),mi=ruta(t,[[c,-.7],[xs-.1,-.7],[xs+.25,.7],[xc-.1,.7],[xc+.25,0],[xd-.1,0],[xd+.25,-.8]])[0];
 plano(L,t,[[c,480,1100,1.1],[xs-.1,470,1100,1.12],[xs+.3,600,1100,1.12],[xc-.1,610,1100,1.12],[xc+.3,540,1070,1.14],[xd-.1,540,1070,1.14],[xd+.35,470,1100,1.16],[f,455,1100,1.18]],cm=>{
  obs(L,cm,{p0:'#3f5059',p1:'#5f7480',yp:1250,piso:['#7b858d','#6c767e']});
  X.fillStyle='#2f3b42';X.fillRect(L-400,1150,1900,110);X.fillStyle='rgba(255,255,255,.12)';X.fillRect(L-400,1150,1900,8);
  haz(L+540,300,L+540,1180,120,460,'235,246,255',.16);
  const q0=e(0),q1=e(1),q2=e(2),q3=e(3);
  if(q0>0)figura(L+lerp(-260,330,q0),1150,1.25,{look:'cliente',camisa:'#2f6b5a',pant:'#34435a'},t,'parado','feliz',1);
  if(q1>0)window.B28.silueta(L+lerp(1340,760,q1),1150,1.28,'#1d2630',{});
  if(q2>0){X.save();X.beginPath();X.rect(L-400,300,1900,850);X.clip();gato(L+540,lerp(1500,1150,q2),1.9,t,{pose:'sentado'});X.restore()}
  if(q3>0)perro(L+lerp(-420,300,q3),1150,2.25,t,Object.assign({pose:'parado',cola:0},{color:DOM.c,color2:DOM.c2,oscuro:DOM.osc,lejos:'#3a2e29',collar:'azul'}));
  dorso(L+540,1960,1.75,Object.assign({},PERRO,{ang:wag(t,0,.42,11),mira:mi}))});
 arriba(L,.6)}

// ---------- 04 · fondo limpio: una línea de luz traza el recorrido y deja ver que no es parejo ----------
function p04(L,t){const c=T.c04,xb=T.x_but4,f=T.c05,S=2.25,yb=1900,bx=L+540,by=yb-262*S,R=190*S;
 const lento=eio(seg(t,xb-.15,xb+.25)),fn=q=>.26+.52*Math.sin(q<xb?q*12:xb*12+(q-xb)*lerp(12,5.2,eio(seg(q,xb-.15,xb+.25)))),a=fn(t);
 const o=ruta(t,[[c,470,-.085],[f,610,.085]]);
 cam(L,o[0],1080,1.06,540,1000,()=>{X.fillStyle=gl(0,0,0,1920,[[0,'#0b1a22'],[1,'#173340']]);X.fillRect(L-900,-900,2900,3800);
  luz(L+540,1180,820,'90,170,190',.22);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(L+540,1905,520,60,0,0,7);X.fill();
  dorso(bx,yb,S,Object.assign({},PERRO,{ang:a}));
  if(t>xb){const ex=extremos(fn,xb,t),q=eio(seg(t,xb,xb+.3));eje(bx,by,R,q);arco(bx,by,R,ex[0],ex[1],{a:q})}},o[1]);
 arriba(L,.5)}

// ---------- dueño agachado, de frente ----------
function agachado(x,yb,s,t){X.save();X.translate(x,yb);X.scale(s,s);X.lineCap='round';X.lineJoin='round';const PIEL='#e8b28c',CAM='#2f6b5a',PANT='#34435a';
 X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.ellipse(0,4,150,18,0,0,7);X.fill();
 X.fillStyle='#2a2019';[-1,1].forEach(q=>{X.beginPath();X.ellipse(q*66,-10,44,18,0,0,7);X.fill()});
 X.fillStyle=CAM;rr(-74,-330,148,230,44);X.fill();
 X.fillStyle=PANT;[-1,1].forEach(q=>{rr(q*66-40,-170,80,160,34);X.fill()});X.fillStyle='rgba(255,255,255,.07)';[-1,1].forEach(q=>{rr(q*66-30,-162,22,120,10);X.fill()});
 const b=Math.sin(t*3)*6;X.strokeStyle=CAM;X.lineWidth=36;[-1,1].forEach(q=>{X.beginPath();X.moveTo(q*70,-300);X.quadraticCurveTo(q*118,-200,q*46,-96+b);X.stroke()});
 X.fillStyle=PIEL;[-1,1].forEach(q=>{X.beginPath();X.arc(q*46,-90+b,22,0,7);X.fill()});
 X.fillStyle=PIEL;rr(-16,-352,32,34,10);X.fill();X.beginPath();X.arc(0,-402,62,0,7);X.fill();
 X.fillStyle='#3a2a22';X.beginPath();X.arc(0,-414,64,Math.PI*1.02,Math.PI*1.98);X.quadraticCurveTo(30,-440,-64,-406);X.fill();
 X.fillStyle='#2a2019';[-1,1].forEach(q=>{X.beginPath();X.arc(q*22,-398,6.5,0,7);X.fill()});X.strokeStyle='#8a3d33';X.lineWidth=6;X.beginPath();X.arc(0,-384,24,.25,Math.PI-.25);X.stroke();X.restore()}

// ---------- 05 · con su dueño: el recorrido se carga a la derecha del perro ----------
function p05(L,t){const c=T.c05,xr=T.x_right5,f=T.c06,S=1.95,yb=1930,bx=L+430,by=yb-262*S,R=190*S,fn=q=>.3+.5*Math.sin(q*12),q=eio(seg(t,xr-.25,xr+.25));
 plano(L,t,[[c,440,1090,1.12],[f,600,1080,1.22]],cm=>{
  obs(L,cm,{p0:'#5f6652',p1:'#8f9170',yp:1300,piso:['#a39a86','#948b78']});luz(L+760,760,820,'255,196,120',.3);marcas(L,430,1700,1.2);
  agachado(L+790,1430,1.12,t);
  dorso(bx,yb,S,Object.assign({},PERRO,{ang:fn(t),mira:.5}));
  eje(bx,by,R,q);arco(bx,by,R,-.2,.8,{a:q*.55});arco(bx,by,R,.2,.8,{rgb:VERDE,a:q})});
 tinte(L,'255,170,90',.08);arriba(L,.58)}

// ---------- 06 · con el perro dominante: se carga a la izquierda ----------
function p06(L,t){const c=T.c06,xl=T.x_left6,f=T.c07,S=1.95,yb=1930,bx=L+720,by=yb-262*S,R=190*S,fn=q=>-.3+.5*Math.sin(q*10.5),q=eio(seg(t,xl-.25,xl+.25)),en=eio(seg(t,c-.1,c+.8));
 plano(L,t,[[c,700,1090,1.2],[f,500,1080,1.14]],cm=>{
  obs(L,cm,{p0:'#465763',p1:'#6b8090',yp:1300,piso:['#868f98','#777f88']});luz(L+300,700,820,'170,205,255',.26);marcas(L,720,1700,1.2);
  perro(L+lerp(-420,190,en),1440,2.5,t,{pose:'parado',camina:en<.98,cola:0,color:DOM.c,color2:DOM.c2,oscuro:DOM.osc,lejos:'#3a2e29',collar:'azul',inclina:-.08});
  dorso(bx,yb,S,Object.assign({},PERRO,{ang:fn(t),mira:-.6,alerta:.5*en}));
  eje(bx,by,R,q);arco(bx,by,R,-.8,.2,{a:q*.55});arco(bx,by,R,-.8,-.2,{rgb:CORAL,a:q})});
 tinte(L,'50,96,180',.14);arriba(L,.58)}

// ---------- pantalla con la cola (el "video" que ven los otros perros) ----------
function videoCola(x,y,w,h,t,o){o=o||{};pantalla(x,y,w,h,()=>{X.fillStyle=gl(0,y,0,y+h,[[0,o.f0||'#22313b'],[1,o.f1||'#3d5360']]);X.fillRect(x,y,w,h);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(x,y+h*.86,w,h*.14);
  const s=h/470,bx=x+w/2,yb=y+h*1.06,by=yb-262*s,R=190*s;dorso(bx,yb,s,Object.assign({},o.perro||VID,{ang:o.ang||0,sinSombra:1,collar:false}));
  if(o.arco)arco(bx,by,R,o.arco[0],o.arco[1],{rgb:o.rgb||ORO,a:o.aa===undefined?1:o.aa,s:s*1.6});if(o.eje)eje(bx,by,R,o.eje)},{marco:o.marco||'#101318'})}

// ---------- 07 · G2: dos perros miran un video de una cola; la estela se congela en el golpe ----------
function p07(L,t){const c=T.c07,xo=T.x_other,xs=T.x_second,f=T.c08,fn=q=>-.28+.5*Math.sin(q*9),fr=eio(seg(t,xo-.2,xo+.1)),a=lerp(fn(t),-.78,fr),g=golpe(t,xo+.05,.6);
 plano(L,t,[[c,540,1120,1],[xo-.2,540,1010,1.2],[xs,540,930,1.4],[f,540,910,1.5]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#0d1016'],[1,'#1b1f2a']]);X.fillRect(L-900,-900,2900,3800);tex('tela',L-300,300,1680,1300,{a:.12,v:2});
  luz(L+540,900,900,'120,170,210',.2+.12*g);
  videoCola(L+170,520,740,760,t,{ang:a,arco:fr>0?[-.78,lerp(-.78,.22,eio(seg(t,xo-.2,xo+.25)))]:null,aa:1,eje:fr});
  if(g>0)luz(L+540,900,620,ORO,.22*g);
  X.fillStyle='rgba(0,0,0,.45)';X.fillRect(L-900,1640,2900,900);
  dorso(L+250,2240,1.75,{c:'#141922',c2:'#1b222d',osc:'#0d1118',ang:.35+.12*Math.sin(t*3),mira:.25,sinSombra:1});
  dorso(L+850,2260,1.6,{c:'#171c26',c2:'#1f2732',osc:'#0d1118',ang:-.3+.1*Math.sin(t*2.6+1),mira:-.25,sinSombra:1});
  X.strokeStyle='rgba(150,200,235,.28)';X.lineWidth=5;[[250,2240,1.75,.25],[850,2260,1.6,-.25]].forEach(([x,y,s,m])=>{X.beginPath();X.ellipse(L+x+m*22*s,y-412*s,63*s,57*s,0,Math.PI*1.1,Math.PI*1.9);X.stroke()})});
 arriba(L,.72)}

// ---------- sala de proyección (vista lateral): pared de tela, piso de baldosa ----------
function cine(L,cm,o){o=o||{};interior(L,{p0:o.p0||'#27323f',p1:o.p1||'#3c4b5c',tex:'tela',ta:.22,yp:1380,pisoTex:'baldosa',pa:.5,piso:['#59636e','#4c5560']});
 X.fillStyle='#1a2029';X.fillRect(L+770,1140,36,240);X.fillRect(L+690,1368,200,16)}
function pecho(x,y,t,k,rap){const f=lerp(1.6,3.1,rap),u=((t-k)*f)%1;if(t<k)return;[0,.5].forEach(d=>{const v=(u+d)%1;X.strokeStyle=`rgba(255,110,96,${.75*(1-v)})`;X.lineWidth=7;X.beginPath();X.arc(x,y,16+v*52,0,7);X.stroke()});X.fillStyle='rgba(255,110,96,.95)';X.beginPath();X.arc(x,y,13+5*Math.max(0,Math.sin(u*Math.PI*2)),0,7);X.fill()}

// ---------- 08 · 2013: un perro frente a una pantalla donde otro perro mueve la cola ----------
function p08(L,t){const c=T.c08,xv=T.x_videos,f=T.c09,on=eio(seg(t,xv-.35,xv+.1));
 plano(L,t,[[c,360,1120,1.22],[xv,520,1100,1.18],[f,680,1060,1.3]],cm=>{
  cine(L,cm);placa(L+400+par(cm,.3),800,1,'2013',eio(seg(t,c+.05,c+.4)));
  videoCola(L+570,700,430,440,t,{ang:wag(t,0,.5,9),f0:on>0?'#22313b':'#0c1117',f1:on>0?'#3d5360':'#0c1117'});if(on<1){X.fillStyle=`rgba(8,11,15,${1-on})`;X.fillRect(L+570,700,430,440)}
  luz(L+785,920,620,'150,200,230',.2*on);
  perro(L+330,1620,2.25,t,{pose:'sentado',collar:'rosa',cola:3})});
 arriba(L,.6)}

// ---------- 09 · se carga a la derecha: el que mira sigue suelto ----------
function p09(L,t){const c=T.c09,f=T.c10,q=eio(seg(t,c+.1,c+.5));
 plano(L,t,[[c,560,1130,1.3],[f,575,1125,1.34]],cm=>{
  cine(L,cm,{p0:'#1f3a3c',p1:'#33595a'});
  videoCola(L+540,770,450,450,t,{ang:wag(t,.3,.5,9),arco:[.2,.8],rgb:VERDE,aa:q,eje:q});luz(L+765,990,680,VERDE,.2);
  perro(L+330,1630,2.3,t,{pose:'echado',collar:'rosa',cola:2.2})});
 tinte(L,'60,200,180',.07);arriba(L,.6)}

// ---------- 10 · se carga a la izquierda: sube el pulso y se pone alerta ----------
function p10(L,t){const c=T.c10,xh=T.x_heart,xa=T.x_anx,f=T.c11,q=eio(seg(t,c+.1,c+.5)),al=eio(seg(t,xh-.3,xh+.3)),rap=eio(seg(t,xh,xa));
 plano(L,t,[[c,560,1130,1.3],[xh,520,1110,1.36],[f,480,1100,1.42]],cm=>{
  cine(L,cm,{p0:'#3a2630',p1:'#573945'});
  videoCola(L+540,770,450,450,t,{ang:wag(t,-.3,.5,9),arco:[-.8,-.2],rgb:CORAL,aa:q,eje:q});luz(L+765,990,680,CORAL,.18);
  perro(L+330,1630,2.3,t,{pose:'sentado',collar:'rosa',cola:0,orejas:.3*al,inclina:-.1*al});
  pecho(L+450,1264,t,xh-.1,rap)});
 tinte(L,'220,60,50',.05+.05*al);arriba(L,.6)}

// ---------- 11 · cada mitad del cerebro mueve el lado contrario de la cola ----------
function mitad(x,y,s,lado,rgb,br){X.save();X.translate(x,y);X.scale(s*lado,s);X.beginPath();X.moveTo(-8,-150);X.bezierCurveTo(-120,-176,-190,-70,-176,30);X.bezierCurveTo(-170,120,-90,170,-8,150);X.closePath();
 X.fillStyle=`rgba(${rgb},${.55+.4*br})`;X.fill();X.strokeStyle=`rgba(${rgb},1)`;X.lineWidth=7;X.stroke();
 X.strokeStyle=`rgba(255,255,255,${.35+.3*br})`;X.lineWidth=6;X.lineCap='round';[[-40,-110,-110,-70,-60,-30],[-150,-10,-80,-20,-40,30],[-130,70,-90,60,-50,100],[-30,-60,-70,-40,-30,-10]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.quadraticCurveTo(p[2],p[3],p[4],p[5]);X.stroke()});X.restore()}
function via(x0,y0,x1,y1,rgb,u,t,br){if(u<=0)return;const n=40;X.save();X.lineCap='round';X.strokeStyle=`rgba(${rgb},${.6+.4*br})`;X.lineWidth=11+7*br;X.beginPath();
 for(let i=0;i<=n*u;i++){const q=i/n,e=q*q*(3-2*q),x=lerp(x0,x1,e),y=lerp(y0,y1,q);i?X.lineTo(x,y):X.moveTo(x,y)}X.stroke();
 for(let j=0;j<4;j++){const q=((t*.55+j/4)%1);if(q<u){const e=q*q*(3-2*q);X.fillStyle=`rgba(255,255,255,${.5+.5*br})`;X.beginPath();X.arc(lerp(x0,x1,e),lerp(y0,y1,q),7+5*br,0,7);X.fill()}}X.restore()}
function flecha(x,y,dy,rgb,a){if(a<=0)return;X.save();X.globalAlpha=a;X.strokeStyle=`rgb(${rgb})`;X.fillStyle=`rgb(${rgb})`;X.lineWidth=18;X.lineCap='round';X.beginPath();X.moveTo(x,y);X.lineTo(x,y+dy*.6);X.stroke();const d=Math.sign(dy);X.beginPath();X.moveTo(x,y+dy);X.lineTo(x-38,y+dy-d*52);X.lineTo(x+38,y+dy-d*52);X.closePath();X.fill();X.restore()}
function p11(L,t){const c=T.c11,xo=T.x_opp,xa=T.x_approach,xw=T.x_otra,f=T.c12,S=1.5,yb=1900,bx=L+540,by=yb-262*S,R=190*S;
 const sep=eio(seg(t,c+.2,c+1.1)),u=eio(seg(t,xo-.5,xo+.7)),A=eio(seg(t,xa-.3,xa+.2))*(1-eio(seg(t,xw-.3,xw))),W=eio(seg(t,xw-.05,xw+.35));
 const ang=ruta(t,[[c,0],[xa-.3,0],[xa+.3,.62],[xw-.2,.62],[xw+.4,-.62],[f,-.62]])[0]+.2*Math.sin(t*10)*(.4+.6*Math.max(A,W));
 const o=ruta(t,[[c,560,1090,1.08,-.045],[f,520,1070,1.14,.045]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{X.fillStyle=gl(0,0,0,1920,[[0,'#141233'],[1,'#2a2452']]);X.fillRect(L-900,-900,2900,3800);luz(L+540,720,700,'120,110,220',.22);
  const cy=790,d=14+22*sep;mitad(L+540-d,cy,1.55,1,VERDE,A);mitad(L+540+d,cy,1.55,-1,CORAL,W);
  via(L+540-d-130,cy+240,bx+R*.62,by-R*.78,VERDE,u,t,A);via(L+540+d+130,cy+240,bx-R*.62,by-R*.78,CORAL,u,t,W);
  X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(L+540,yb+4,330,40,0,0,7);X.fill();
  dorso(bx,yb,S,Object.assign({},PERRO,{ang}));
  arco(bx,by,R,.12,.95,{rgb:VERDE,a:u*(.35+.65*A)});arco(bx,by,R,-.95,-.12,{rgb:CORAL,a:u*(.35+.65*W)});
  flecha(bx+R*1.15,by-R*.2,-150,VERDE,A);flecha(bx-R*1.15,by-R*.55,150,CORAL,W)},o[3]);
 arriba(L,.5)}

// ---------- 12 · parque al atardecer: los dos arcos aparecen un momento y se van ----------
function pasto(L,y,t){X.fillStyle=gl(0,y,0,1920,[[0,'#5f7d3a'],[1,'#33501f']]);X.fillRect(L-900,y,2900,1400);
 for(let i=0;i<70;i++){const x=L-300+rnd(i+3)*1700,yy=y+30+rnd(i+40)*760,h=22+rnd(i+80)*34+(yy-y)*.05,s=Math.sin(t*1.6+i)*5;X.strokeStyle=`rgba(${rnd(i+9)>.5?'150,190,90':'40,70,24'},.55)`;X.lineWidth=5;X.lineCap='round';X.beginPath();X.moveTo(x,yy);X.quadraticCurveTo(x+s,yy-h*.6,x+s*2,yy-h);X.stroke()}}
function p12(L,t){const c=T.c12,xa=T.x_always,xw=T.x_watch,f=T.c13,S=2.2,yb=1960,bx=L+540,by=yb-262*S,R=190*S;
 const A=golpe(t,c+.5,1.5),W=golpe(t,xa+.15,1.5),ang=ruta(t,[[c,0],[c+.5,.55],[xa+.1,.55],[xa+.7,-.55],[xw,-.55],[xw+.5,0]])[0]+.22*Math.sin(t*11);
 plano(L,t,[[c,500,1160,1.2],[xw,560,1130,1.26],[f,585,1120,1.3]],cm=>{
  X.fillStyle='#5f7d3a';X.fillRect(L-900,1000,2900,1700);cielo(L-900,-900,2900,2050,'tarde',t,2);const px=par(cm,.6);
  X.fillStyle='#3d4a3a';for(let i=0;i<9;i++){const x=L-200+i*190+px,r=120+rnd(i+5)*90;X.beginPath();X.arc(x,1120,r,0,7);X.fill()}
  luz(L+250+px,1010,520,'255,200,130',.4);pasto(L,1150,t);
  dorso(bx,yb,S,Object.assign({},PERRO,{ang}));
  arco(bx,by,R,.12,.9,{rgb:VERDE,a:A});arco(bx,by,R,-.9,-.12,{rgb:CORAL,a:W});eje(bx,by,R,Math.max(A,W)*.8)});
 tinte(L,'255,160,80',.06);arriba(L,.55)}

// ---------- 13 · CTA: llega su persona; la cola en primer plano ----------
function p13(L,t){const c=T.c13,ab=eio(seg(t,c-.1,c+.7));
 plano(L,t,[[c,610,1010,1.08],[c+2.2,548,1000,1.02],[T.fin,540,1000,1]],cm=>{
  interior(L,{p0:'#6e4632',p1:'#a36a4a',tex:'tela',ta:.24,yp:1480,pisoTex:'madera'});
  X.fillStyle='#e9dfcb';X.fillRect(L+476,1066,300,420);cielo(L+496,1086,260,394,'tarde',t,4);X.fillStyle='#5a3a26';X.save();X.translate(L+496,1086);X.transform(1-ab*.72,0,0,1,0,0);X.fillRect(0,0,260,394);X.fillStyle='#d9b24a';X.beginPath();X.arc(222,210,13,0,7);X.fill();X.restore();
  luz(L+626,1300,560,'255,200,130',.38*ab);
  if(ab>.3)figura(L+640,1478,.72,{look:'cliente',camisa:'#2f6b5a',pant:'#34435a'},t,'parado','feliz',-1);
  lamparaPie(L+120,1500,1.05,true);
  dorso(L+300,1905,1.6,Object.assign({},PERRO,{ang:wag(t,.3,.5,13),mira:.55}))},1000);
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_sdogs14_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SDOGS14 · FIN =====
</script>
