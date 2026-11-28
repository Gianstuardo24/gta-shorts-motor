<script>
// ===== DC · SMDM18 · INICIO ===== (MDM 18h · How ONE Joke DESTROYED a Company · lote del 28-nov · una escena por línea del guion)
// Sin retrato: el orador es una figura genérica de traje, sin rasgos. Sin marca ni nombre de tienda en la fachada. Los diarios no llevan titulares legibles (no se inventan).
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,hojaP,renglones,tarj,desenfoca,borroso}=window.B28;
const ORO='#e9c46a',ORO2='#b8892e',OR='233,196,106',PAPEL='#efe6d0',TINTA='#2a2019',FRIO='120,160,230';
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({manga:'#1c2533',puno:'#f1ede4'},o))};

function gema(x,y,r,col){X.save();X.translate(x,y);X.fillStyle=col||'#9fe3ff';X.beginPath();X.moveTo(0,-r);X.lineTo(r*.9,-r*.2);X.lineTo(0,r);X.lineTo(-r*.9,-r*.2);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.6)';X.beginPath();X.moveTo(0,-r);X.lineTo(r*.4,-r*.2);X.lineTo(0,r*.1);X.lineTo(-r*.4,-r*.2);X.closePath();X.fill();X.restore()}
function anillo(x,y,s,col){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle=col||ORO;X.lineWidth=12;X.beginPath();X.ellipse(0,0,36,42,0,0,7);X.stroke();X.strokeStyle='rgba(255,255,255,.4)';X.lineWidth=3;X.beginPath();X.ellipse(-4,-2,30,36,0,3.4,4.6);X.stroke();gema(0,-54,20);X.restore()}
function arete(x,y,s,o){o=o||{};X.save();X.translate(x,y);X.rotate(o.rot||0);X.scale(s,s);X.strokeStyle=o.col||ORO;X.lineWidth=5;X.lineCap='round';X.beginPath();X.arc(0,-40,16,Math.PI*.9,Math.PI*2.2);X.stroke();X.beginPath();X.moveTo(0,-24);X.lineTo(0,0);X.stroke();X.fillStyle=o.col||ORO;X.beginPath();X.moveTo(0,0);X.quadraticCurveTo(30,44,0,70);X.quadraticCurveTo(-30,44,0,0);X.fill();X.fillStyle='rgba(255,255,255,.45)';X.beginPath();X.ellipse(-7,34,5,12,.3,0,7);X.fill();
 if(o.roto>0){X.strokeStyle=`rgba(40,28,10,${o.roto})`;X.lineWidth=3;X.beginPath();X.moveTo(-10,20);X.lineTo(2,34);X.lineTo(-6,46);X.lineTo(8,58);X.stroke()}X.restore()}
function busto(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='#17131c';X.beginPath();X.moveTo(-70,0);X.lineTo(-52,-150);X.quadraticCurveTo(0,-176,52,-150);X.lineTo(70,0);X.closePath();X.fill();X.strokeStyle=ORO;X.lineWidth=5;X.beginPath();X.moveTo(-40,-150);X.quadraticCurveTo(0,-40,40,-150);X.stroke();gema(0,-84,13,'#ff8fa3');X.restore()}
function caja(x,yb,s,ab,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(0,4,80,10,0,0,7);X.fill();X.fillStyle=o.col||'#5a1f33';rr(-64,-56,128,56,8);X.fill();X.fillStyle='rgba(255,255,255,.08)';rr(-64,-56,128,8,4);X.fill();
 if(ab>0){X.fillStyle='#2a0f1a';rr(-56,-66,112,14,4);X.fill();anillo(0,-84,.5)}X.save();X.translate(-64,-56);X.rotate(-1.9*(ab||0));X.fillStyle=o.col2||'#6d2a40';rr(0,-34,128,34,8);X.fill();X.fillStyle=ORO;rr(54,-6,20,8,3);X.fill();X.restore();X.restore()}
// fachada de joyería (sin nombre). on: 0..1 vitrina encendida
function local(x,yb,s,on,v){v=v||0;const tn=['#2a1a2a','#241c30','#30202a','#1f1a2c','#2c2026'][Math.floor(rnd(v+1)*5)],al=Math.floor(rnd(v+2)*3)*34;X.save();X.translate(x,yb);X.scale(s*(.92+.16*rnd(v+3)),s);X.fillStyle=tn;X.fillRect(-170,-470-al,340,470+al);X.fillStyle='#3a2438';X.fillRect(-170,-470,340,60);if(al){X.fillStyle='rgba(255,214,140,.10)';[-90,0,90].forEach(q=>{X.fillRect(q-22,-470-al+10,44,al-18)})}gema(0,-440,17,on>.3?'#9fe3ff':'#4a5a66');
 X.fillStyle=`rgb(${Math.round(lerp(30,255,on))},${Math.round(lerp(34,214,on))},${Math.round(lerp(48,140,on))})`;rr(-140,-360,200,250,8);X.fill();X.fillStyle='#1a1018';X.fillRect(-140,-150,200,40);
 [[-100,-150],[-40,-150],[20,-150]].forEach((p,i)=>{X.fillStyle='#17131c';X.beginPath();X.moveTo(p[0]-22,p[1]);X.lineTo(p[0]-14,p[1]-70-i*12);X.lineTo(p[0]+14,p[1]-70-i*12);X.lineTo(p[0]+22,p[1]);X.closePath();X.fill();X.fillStyle=on>.3?ORO:'#5a5040';X.beginPath();X.arc(p[0],p[1]-78-i*12,9,0,7);X.fill()});
 X.fillStyle='#1c1220';rr(80,-330,70,330,6);X.fill();X.fillStyle=`rgba(255,214,140,${.35*on})`;rr(90,-316,50,150,4);X.fill();X.fillStyle=ORO2;X.beginPath();X.arc(92,-160,6,0,7);X.fill();
 X.fillStyle='#7a2b45';X.beginPath();X.moveTo(-180,-400);X.lineTo(180,-400);X.lineTo(200,-360);X.lineTo(-200,-360);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.14)';for(let i=0;i<6;i++){X.beginPath();X.moveTo(-180+i*66,-400);X.lineTo(-150+i*66,-400);X.lineTo(-166+i*66+(i-2.5)*4,-360);X.lineTo(-200+i*66+(i-2.5)*4,-360);X.closePath();X.fill()}
 if(on>0)luz(-40,-240,260,OR,.35*on);X.restore()}
function micro(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='#14151a';X.beginPath();X.ellipse(0,0,110,22,0,0,7);X.fill();X.fillStyle='#2a2d34';X.fillRect(-9,-520,18,520);X.translate(0,-520);X.rotate(o.rot===undefined?-.25:o.rot);X.fillStyle='#3a3e47';rr(-24,-150,48,170,16);X.fill();
 X.fillStyle=gl(-50,0,50,0,[[0,'#7d8792'],[.5,'#e2e7ec'],[1,'#6a737d']]);X.beginPath();X.arc(0,-190,56,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=3;for(let i=-2;i<=2;i++){X.beginPath();X.moveTo(-52,-190+i*18);X.lineTo(52,-190+i*18);X.stroke();X.beginPath();X.moveTo(i*18,-242);X.lineTo(i*18,-138);X.stroke()}
 X.fillStyle='#22252b';rr(-58,-146,116,16,8);X.fill();X.fillStyle=o.on?'#e4572e':'#4a4e57';X.beginPath();X.arc(0,-60,7,0,7);X.fill();X.restore()}
const cabMic=(x,yb,s)=>[x-47*s,yb-704*s];
function ondas(x,y,t,k,o){o=o||{};for(let j=0;j<(o.n||4);j++){const u=o.fijo!==undefined?(j+1)/(o.n||4)*o.fijo:((t-k)*(o.vel||.7)+j/(o.n||4))%1;if(t<k)continue;X.strokeStyle=`rgba(${o.rgb||OR},${(o.a===undefined?.8:o.a)*(o.fijo!==undefined?1-.5*u:1-u)})`;X.lineWidth=o.lw||8;X.beginPath();X.arc(x,y,40+u*(o.r||420),-1.1,1.1);X.stroke();X.beginPath();X.arc(x,y,40+u*(o.r||420),Math.PI-1.1,Math.PI+1.1);X.stroke()}}
function diario(x,y,w,rot,a){X.save();X.translate(x,y);X.rotate(rot||0);if(a!==undefined)X.globalAlpha=a;const h=w*1.32;X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-w/2+6,-h/2+8,w,h);X.fillStyle=PAPEL;X.fillRect(-w/2,-h/2,w,h);
 X.fillStyle=TINTA;X.fillRect(-w*.42,-h*.44,w*.84,h*.08);X.fillRect(-w*.42,-h*.31,w*.7,h*.045);X.fillRect(-w*.42,-h*.25,w*.5,h*.045);X.fillStyle='#bdb39b';X.fillRect(-w*.42,-h*.16,w*.4,h*.26);
 X.fillStyle=TINTA;X.save();X.translate(-w*.22,-h*.03);X.scale(w/700,w/700);rr(-10,-40,20,80,8);X.fill();X.beginPath();X.arc(0,-56,26,0,7);X.fill();X.restore();
 X.fillStyle='rgba(42,32,25,.35)';for(let i=0;i<7;i++){X.fillRect(w*.04,-h*.16+i*h*.04,w*.38,h*.014)}for(let i=0;i<8;i++){X.fillRect(-w*.42,h*.14+i*h*.04,w*.84*(.7+.3*rnd(i)),h*.014)}X.restore()}
// figura de traje, sin rasgos. de frente (o.espalda: de espaldas). o.brazo: [x,y] mano levantada
function traje(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.lineCap='round';X.lineJoin='round';const T1=o.col||'#1c2533';
 X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.ellipse(0,4,110,14,0,0,7);X.fill();X.fillStyle='#141a24';rr(-52,-230,46,230,14);X.fill();rr(6,-230,46,230,14);X.fill();X.fillStyle='#0c0f14';[-30,30].forEach(q=>{X.beginPath();X.ellipse(q,-6,36,13,0,0,7);X.fill()});
 X.fillStyle=T1;X.beginPath();X.moveTo(-84,-220);X.lineTo(-92,-430);X.quadraticCurveTo(-88,-476,-40,-480);X.lineTo(40,-480);X.quadraticCurveTo(88,-476,92,-430);X.lineTo(84,-220);X.closePath();X.fill();
 if(!o.espalda){X.fillStyle='#f1ede4';X.beginPath();X.moveTo(-24,-480);X.lineTo(24,-480);X.lineTo(0,-390);X.closePath();X.fill();X.fillStyle=ORO2;X.beginPath();X.moveTo(-8,-470);X.lineTo(8,-470);X.lineTo(5,-400);X.lineTo(0,-388);X.lineTo(-5,-400);X.closePath();X.fill()}
 X.strokeStyle=T1;X.lineWidth=40;if(o.brazo){X.beginPath();X.moveTo(78,-450);X.quadraticCurveTo(150,-420,o.brazo[0],o.brazo[1]);X.stroke();X.fillStyle='#e0ac80';X.beginPath();X.arc(o.brazo[0],o.brazo[1],24,0,7);X.fill()}else{X.beginPath();X.moveTo(84,-450);X.lineTo(96,-250);X.stroke()}X.beginPath();X.moveTo(-84,-450);X.lineTo(-96,-250);X.stroke();
 X.fillStyle='#e0ac80';rr(-18,-520,36,50,10);X.fill();X.beginPath();X.arc(0,-568,62,0,7);X.fill();X.fillStyle='#4a3a30';X.beginPath();if(o.espalda)X.arc(0,-572,64,0,7);else{X.arc(0,-580,64,Math.PI*1.02,Math.PI*1.98);X.quadraticCurveTo(20,-610,-62,-584)}X.fill();X.restore()}
function publico(L,y,n,t,s,col){for(let i=0;i<n;i++){const x=L-200+i*(1500/n)+(rnd(i+3)-.5)*40,yy=y+(rnd(i+11)-.5)*30+Math.sin(t*1.2+i)*3;X.fillStyle=col||'#0c0c12';X.beginPath();X.arc(x,yy-70*s,44*s,0,7);X.fill();X.beginPath();X.moveTo(x-90*s,yy+90*s);X.quadraticCurveTo(x-80*s,yy-20*s,x,yy-24*s);X.quadraticCurveTo(x+80*s,yy-20*s,x+90*s,yy+90*s);X.closePath();X.fill()}}
function escenario(L,cm,o){o=o||{};X.fillStyle=gl(0,0,0,1920,[[0,o.c0||'#120a14'],[1,o.c1||'#2a1422']]);X.fillRect(L-1400,-900,3900,3800);const px=par(cm,.5);
 if(o.telon!==false){X.fillStyle='rgba(122,43,69,.55)';for(let i=0;i<11;i++){X.fillRect(L-260+i*150+px,200,96,1160)}X.fillStyle='rgba(233,196,106,.25)';X.fillRect(L-400+px,1340,2000,14)}
 X.fillStyle='#1a0f18';X.fillRect(L-1400,o.yp||1500,3900,900);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L-1400,o.yp||1500,3900,8)}
function atril(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='#3a2416';X.beginPath();X.moveTo(-90,0);X.lineTo(-70,-300);X.lineTo(70,-300);X.lineTo(90,0);X.closePath();X.fill();X.fillStyle='#553a23';X.beginPath();X.moveTo(-104,-300);X.lineTo(104,-300);X.lineTo(92,-340);X.lineTo(-92,-340);X.closePath();X.fill();X.fillStyle=ORO2;X.beginPath();X.arc(0,-150,22,0,7);X.fill();X.restore()}
function vasoCorte(x,yb,s,rot,br){X.save();X.translate(x,yb);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(220,236,240,.28)';X.strokeStyle='rgba(240,248,252,.85)';X.lineWidth=4;X.beginPath();X.moveTo(-34,-96);X.lineTo(34,-96);X.lineTo(26,0);X.lineTo(-26,0);X.closePath();X.fill();X.stroke();X.lineWidth=2;X.strokeStyle='rgba(240,248,252,.6)';for(let i=-1;i<=1;i++){X.beginPath();X.moveTo(i*18-9,-70);X.lineTo(i*18,-10);X.lineTo(i*18+9,-70);X.stroke()}
 if(br>0){X.strokeStyle=`rgba(255,255,255,${br})`;X.lineWidth=4;[[0,-110,22],[30,-80,14]].forEach(p=>{X.beginPath();X.moveTo(p[0]-p[2],p[1]);X.lineTo(p[0]+p[2],p[1]);X.moveTo(p[0],p[1]-p[2]);X.lineTo(p[0],p[1]+p[2]);X.stroke()})}X.restore()}
function sandwich(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(0,8,190,22,0,0,7);X.fill();X.fillStyle='#f4f1ea';X.beginPath();X.ellipse(0,0,180,24,0,0,7);X.fill();
 const capa=(y,h,c)=>{X.fillStyle=c;X.beginPath();X.moveTo(-130,y);X.lineTo(130,y);X.lineTo(118,y-h);X.lineTo(-118,y-h);X.closePath();X.fill()};capa(-8,34,'#e8c98a');X.fillStyle='#6fbf5a';X.beginPath();for(let i=0;i<=13;i++)X.lineTo(-126+i*19.4,-42-(i%2)*12);X.lineTo(126,-36);X.lineTo(-126,-36);X.closePath();X.fill();capa(-52,14,'#f3a0a0');capa(-66,10,'#f2c94c');capa(-76,34,'#e8c98a');X.fillStyle='#c99a5a';X.fillRect(-118,-112,236,6);X.restore()}
function placa(x,y,s,texto,a,w){if(a<=0)return;X.save();X.globalAlpha=a;tarj(x,y,(w||230)*s,96*s,14*s,'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,(w?46:62)*s,'#2a2f38',{w:800});X.restore()}
function tienda(L,cm,t,o){o=o||{};interior(L,{p0:'#3a1a2a',p1:'#6a3046',tex:'tela',ta:.26,yp:1380,pisoTex:'madera',pa:.6,piso:['#3a2416','#2f1d12']});const px=par(cm,.4);
 [[120,0],[520,1],[920,2]].forEach(([x,i])=>{X.fillStyle='#1c1018';rr(L+x-150+px,620,300,420,10);X.fill();X.fillStyle=`rgba(255,214,140,${.9*(o.on===undefined?1:o.on)})`;rr(L+x-134+px,636,268,388,6);X.fill();[[-70,0],[0,1],[70,2]].forEach(([q,j])=>{busto(L+x+q+px,1010,.62+.1*((i+j)%2))})});luz(L+540,820,900,OR,.24*(o.on===undefined?1:o.on))}
function mostrador(L,y){X.fillStyle='#4a2a18';X.fillRect(L-1400,y,3900,900);tex('madera',L-1400,y,3900,700,{a:.85,s:1.5,v:6});X.fillStyle='#5a1f33';X.fillRect(L-1400,y-70,3900,70);tex('tela',L-1400,y-70,3900,70,{a:.5,v:3});X.fillStyle='rgba(220,240,250,.16)';X.fillRect(L-1400,y-190,3900,120);X.fillStyle='rgba(255,255,255,.4)';X.fillRect(L-1400,y-190,3900,6);X.fillStyle='rgba(255,255,255,.1)';for(let i=0;i<10;i++){X.beginPath();X.moveTo(L-300+i*300,y-70);X.lineTo(L-250+i*300,y-70);X.lineTo(L-170+i*300,y-190);X.lineTo(L-220+i*300,y-190);X.closePath();X.fill()}}

// ---------- 01 · gancho: muchas vitrinas; entra el micrófono y la luz se enfría ----------
function p01(L,t){const xe=T.x_empire,xt=T.x_thousand,xb=T.x_but,xw=T.x_worst,f=T.c02,ent=eio(seg(t,xb-.45,xb+.25)),frio=eio(seg(t,xb-.2,xw));
 const kf=[[0,1575,1250,1.9],[xe,1545,1200,1.3],[xt+.6,1500,1000,.62],[xb,1500,1010,.64],[xw+.3,1500,1120,1.02],[f,1500,1130,1.08]];
 plano(L,t,kf,cm=>{X.fillStyle=gl(0,0,0,1700,[[0,'#0c0a18'],[1,'#241a30']]);X.fillRect(L-1400,-1400,6200,5200);
  for(let r=2;r>=0;r--){const y=1420-r*520,s=1-.0*r;for(let i=-2;i<12;i++){const k=r*20+i,ap=1-frio*(rnd(k+7)<.75?eio(seg(frio,rnd(k+3)*.7,rnd(k+3)*.7+.3)):0);local(L+i*392+(r%2)*190+(rnd(k+11)-.5)*70,y,1,ap,k)}X.fillStyle='#17121c';X.fillRect(L-1400,y,6200,60)}
  [[-60,0],[700,1],[1330,2],[2050,3],[2900,4]].forEach(([x,i])=>{X.fillStyle='#0c0a10';X.fillRect(L+x-7,1040,14,440);X.fillStyle='#ffe2a0';X.beginPath();X.arc(L+x,1030,22,0,7);X.fill();luz(L+x,1030,200,OR,.35)});
  X.fillStyle='#120e16';X.fillRect(L-1400,1480,6200,1500);X.fillStyle='rgba(255,214,140,.07)';X.fillRect(L-1400,1480,6200,300)});
 if(ent>0){X.save();X.translate(0,(1-ent)*900);luz(L+560,1100,700,FRIO,.2*ent);micro(L+640,2380,1.9,{rot:-.2,on:1});X.restore()}
 tinte(L,'40,70,160',.16*frio);arriba(L,.6)}

// ---------- 02 · 1991: la joyería de la familia; una figura de traje mira las vitrinas ----------
function p02(L,t){const c=T.c02,xr=T.x_ratner,xf=T.x_family,f=T.c03;
 plano(L,t,[[c,360,1090,1.26],[xr,420,1090,1.22],[f,760,1080,1.14]],cm=>{tienda(L,cm,t,{});
  mostrador(L,1500);placa(L+590,1266,.82,'1991',eio(seg(t,c+.05,c+.4)));[[150,0],[330,1],[520,2]].forEach(([x,i])=>{X.save();X.translate(L+x,1446);X.rotate(-.1+i*.08);anillo(0,0,.7);X.restore()});
  traje(L+900,1560,1.5,{espalda:1})});
 arriba(L,.6)}

// ---------- 03 · era barata y a la gente le encantaba ----------
function corazon(x,y,s,a){if(a<=0)return;X.save();X.translate(x,y);X.scale(s*back(Math.min(1,a*1.4)),s*back(Math.min(1,a*1.4)));X.globalAlpha=Math.min(1,a*2)*(a>.8?(1-a)*5:1);X.fillStyle='#ff4f7a';X.beginPath();X.moveTo(0,22);X.bezierCurveTo(-46,-10,-22,-44,0,-18);X.bezierCurveTo(22,-44,46,-10,0,22);X.fill();X.restore()}
function p03(L,t){const c=T.c03,xl=T.x_loved,f=T.c04,da=eio(seg(t,c+.5,c+1.3));
 plano(L,t,[[c,380,1120,1.16],[f,720,1110,1.16]],cm=>{tienda(L,cm,t,{});
  [[250,'cliente',0],[560,'jugadora',1],[870,'gamer',2]].forEach(([x,lk,i])=>{figura(L+x,1560,1.25,{look:lk},t,'parado','feliz',1);corazon(L+x+10,1040-((t-xl-i*.18)*120),1.5,seg(t,xl-.1+i*.18,xl+1.2+i*.18))});
  mostrador(L,1620);caja(L+lerp(1200,420,da),1560-golpe(t,c+.5,.8)*60,1.3,eio(seg(t,c+1.2,c+1.6)));
  [[640,0],[820,1],[1000,2]].forEach(([x,i])=>{X.save();X.translate(L+x,1500);X.rotate(Math.sin(t*2+i)*.12);X.fillStyle=PAPEL;X.beginPath();X.moveTo(0,0);X.lineTo(22,16);X.lineTo(22,62);X.lineTo(-22,62);X.lineTo(-22,16);X.closePath();X.fill();X.fillStyle=TINTA;X.beginPath();X.arc(0,18,4,0,7);X.fill();X.fillRect(-12,36,24,5);X.restore()})});
 tinte(L,'255,190,90',.06);arriba(L,.6)}

// ---------- 04 · ese abril: un discurso ante miles de empresarios ----------
function p04(L,t){const c=T.c04,xs=T.x_speech,xt=T.x_thousands,f=T.c05;
 plano(L,t,[[c,540,1560,1.2],[xt,540,1280,1.06],[f,540,1080,1.16]],cm=>{escenario(L,cm,{yp:1330});
  [[0,640],[1,760],[2,880]].forEach(([i,y])=>{X.strokeStyle=`rgba(233,196,106,${.18-.04*i})`;X.lineWidth=16;X.beginPath();X.ellipse(L+540,y-200,900+i*140,260+i*40,0,Math.PI*.08,Math.PI*.92);X.stroke()});
  haz(L+540,200,L+540,1330,60,260,'255,236,190',.3);luz(L+540,1180,300,'255,236,190',.35);
  atril(L+540,1330,.8);traje(L+540,1326,.52,{brazo:[150,-520]});micro(L+470,1330,.42,{rot:.3,on:1});
  publico(L,1560,9,t,1.3,'#0f0b12');publico(L+70,1740,8,t,1.7,'#09070c');publico(L-40,1960,7,t,2.2,'#050407')});
 arriba(L,.62)}

// ---------- 05 · el chiste de los vasos: uno gira bajo el foco y el gesto se vuelve incómodo ----------
function p05(L,t){const c=T.c05,xg=T.x_glasses,xh=T.x_cheap5,xc=T.x_crap,f=T.c06,sub=eio(seg(t,xg-.5,xg+.2)),inc=eio(seg(t,xc-.9,xc-.2)),foco=eio(seg(t,xc-.5,xc+.2));
 const kf=[[c,540,1150,1.1],[xg,560,1100,1.2],[xc,560,1090,1.26],[f,520,1150,1.2]],gy=lerp(1290,1000,sub)+inc*40;
 plano(L,t,kf,cm=>{escenario(L,cm,{yp:1620,c0:'#120a14',c1:inc>0?'#1c1620':'#2a1422'});haz(L+560,120,L+560,1500,50,lerp(330,190,inc),'255,236,190',.3);
  X.fillStyle='#1c2533';X.beginPath();X.moveTo(L+140,1920);X.lineTo(L+190,820);X.quadraticCurveTo(L+230,700,L+380,690);X.lineTo(L+640,690);X.quadraticCurveTo(L+790,700,L+830,820);X.lineTo(L+880,1920);X.closePath();X.fill();
  X.fillStyle='#f1ede4';X.beginPath();X.moveTo(L+440,690);X.lineTo(L+580,690);X.lineTo(L+510,960);X.closePath();X.fill();X.fillStyle=ORO2;X.beginPath();X.moveTo(L+494,700);X.lineTo(L+526,700);X.lineTo(L+520,930);X.lineTo(L+510,960);X.lineTo(L+500,930);X.closePath();X.fill();
  X.fillStyle='#e0ac80';rr(L+466,560,88,140,24);X.fill();
  X.fillStyle=gl(L+300,0,L+860,0,[[0,'#8e98a4'],[.5,'#e2e7ec'],[1,'#7d8792']]);X.beginPath();X.ellipse(L+590,1330,290,40,0,0,7);X.fill();
  [[400,0],[500,1],[690,3],[790,4]].forEach(([x,i])=>vasoCorte(L+x,1322,1.25,0,0));
  const gr=(1-inc)*Math.sin(t*5)*.3;vasoCorte(L+596,gy,1.6,gr,(1-inc)*(.5+.5*Math.sin(t*9)));
  X.strokeStyle='#1c2533';X.lineWidth=70;X.lineCap='round';X.beginPath();X.moveTo(L+800,860);X.quadraticCurveTo(L+900,1100,L+690,gy+30);X.stroke();X.fillStyle='#e0ac80';X.beginPath();X.ellipse(L+660,gy+10,46,36,0,0,7);X.fill()});
 desenfoca(6*foco);
 plano(L,t,kf,cm=>{X.save();X.translate(0,(1-eio(seg(t,xc-1.0,xc-.2)))*700);micro(L+250,2160,1.5,{rot:.25,on:1});X.restore()});
 tinte(L,'60,80,140',.1*inc);arriba(L,.64)}

// ---------- 06 · los aretes costaban menos que un sándwich y no durarían tanto ----------
function monedas(x,yb,n){for(let i=0;i<n;i++){X.fillStyle=ORO2;X.beginPath();X.ellipse(x,yb-i*16+5,38,12,0,0,7);X.fill();X.fillStyle=ORO;X.beginPath();X.ellipse(x,yb-i*16,38,12,0,0,7);X.fill()}}
function p06(L,t){const c=T.c06,xe=T.x_earrings,xs=T.x_sandwich,xl=T.x_last,f=T.c07,ro=eio(seg(t,xl-.25,xl+.3));
 plano(L,t,[[c,340,1060,1.3],[xs-.5,360,1060,1.3],[xs+.2,760,1070,1.3],[xl,760,1070,1.26],[xl+.3,740,1090,1.22],[f,540,1280,1.04]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#0c0810'],[1,'#22121c']]);X.fillRect(L-1400,-900,3900,3800);tex('tela',L-400,300,1900,1700,{a:.16,v:3});
  haz(L+330,160,L+330,1240,60,300,'255,220,150',.34);haz(L+770,160,L+770,1240,60,300,'255,220,150',.34);
  X.fillStyle='#5a1f33';rr(L+150,1200,360,40,12);X.fill();rr(L+590,1200,360,40,12);X.fill();
  X.fillStyle='#f4ead2';rr(L+230,860,200,300,10);X.fill();arete(L+290,1000,1.5,{roto:ro,col:ro>.5?'#a89260':ORO});arete(L+372,1000+ro*120,1.5,{roto:ro,rot:ro*.9,col:ro>.5?'#a89260':ORO});
  sandwich(L+770,1196,1);const q=eio(seg(t,xs+.25,xs+.6));if(q>0){X.globalAlpha=q;monedas(L+330,1330,1);monedas(L+770,1330,3);X.globalAlpha=1}
  micro(L+540,2330,1.5,{rot:-.2,on:1})});
 arriba(L,.6)}

// ---------- 07 · G2: el micrófono solo; la onda de sonido se vuelve diarios ----------
function p07(L,t){const c=T.c07,xw=T.x_worst7,xd=T.x_disaster,f=T.c08,m=cabMic(L+540,1820,1.5),tr=eio(seg(t,xw-.1,xw+.5)),g=golpe(t,xw,.6);
 plano(L,t,[[c,540,1150,1],[xw,540,1100,1.2],[f,540,1080,1.4]],cm=>{escenario(L,cm,{telon:false,yp:1820,c0:'#08060c',c1:'#1c1220'});haz(L+540,100,L+540,1820,60,330,'255,236,190',.3+.2*g);
  if(tr<1)ondas(m[0],m[1],t,c+.2,{r:520,a:.8*(1-tr)});
  if(tr>0)for(let i=0;i<8;i++){const a=lerp(-.25,Math.PI+.25,i/7),u=((t-xw)*.32+i*.11)%1,d=150+u*520;diario(m[0]+Math.cos(a)*d,m[1]+Math.sin(a)*d*.85+40,120+u*90,a+u*2,tr*(1-u*.7))}
  micro(L+540,1820,1.5,{on:1})});
 tinte(L,'50,80,160',.12*eio(seg(t,xd-.3,xd+.2)));arriba(L,.6)}

// ---------- 08 · ya había contado ese chiste y no había pasado nada (corte por coincidencia) ----------
function p08(L,t){const c=T.c08,xn=T.x_nothing,f=T.c09,k=xn+.75,seg2=t>k,m=cabMic(L+540,1700,1.5);
 plano(L,t,[[c,540,1100,1.1],[f,540,1080,1.18]],cm=>{
  if(!seg2){escenario(L,cm,{yp:1700,c0:'#1c1410',c1:'#3a2a1c'});haz(L+540,100,L+540,1700,60,300,'255,220,160',.26);const ap=1-eio(seg(t,xn-.5,xn+.4));ondas(m[0],m[1],t,c,{r:480,a:.8*ap,rgb:'255,220,160'});publico(L,1860,6,t,1.5,'#120c0a')}
  else{escenario(L,cm,{telon:false,yp:1700,c0:'#08060c',c1:'#1c1220'});haz(L+540,100,L+540,1700,60,330,'255,236,190',.3);ondas(m[0],m[1],t,k,{fijo:eio(seg(t,k,k+.4)),r:480,a:.9});publico(L,1860,9,t,1.5,'#060509')}
  micro(L+540,1700,1.5,{on:1})});
 arriba(L,.6)}

// ---------- 09 · esta vez lo tomaron los diarios, y sus clientes lo leyeron ----------
function rodillo(x,y,r,t,dir){X.fillStyle=gl(x-r,0,x+r,0,[[0,'#3a3e47'],[.5,'#8e98a4'],[1,'#2a2d34']]);X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.4)';X.lineWidth=6;for(let i=0;i<4;i++){const a=t*3*dir+i*1.57;X.beginPath();X.moveTo(x+Math.cos(a)*r*.2,y+Math.sin(a)*r*.2);X.lineTo(x+Math.cos(a)*r*.86,y+Math.sin(a)*r*.86);X.stroke()}X.fillStyle='#1b1d22';X.beginPath();X.arc(x,y,r*.16,0,7);X.fill()}
function p09(L,t){const c=T.c09,xn=T.x_newspapers,xk=T.x_customers,xl=T.x_laughing,f=T.c10,D=1500;
 plano(L,t,[[c,460,1100,1.14],[xk-.9,620,1100,1.14],[xk+.2,D+500,1110,1.1],[f,D+580,1110,1.16]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#16181e'],[1,'#2a2e38']]);X.fillRect(L-1400,-900,5600,3800);tex('concreto',L-400,300,2000,1700,{a:.2,v:6});luz(L+500,800,800,'255,236,200',.14);
  X.fillStyle=PAPEL;X.beginPath();X.moveTo(L-400,1010);X.lineTo(L+330,1010);X.lineTo(L+560,1250);X.lineTo(L+1300,1250);X.lineTo(L+1300,1290);X.lineTo(L+540,1290);X.lineTo(L+310,1050);X.lineTo(L-400,1050);X.closePath();X.fill();
  for(let i=0;i<14;i++){const x=L-380+((t*340+i*130)%1700);if(x>L+600){X.fillStyle=TINTA;X.fillRect(x,1256,70,9);X.fillStyle='rgba(42,32,25,.4)';X.fillRect(x,1272,90,5)}}
  rodillo(L+330,890,130,t,1);rodillo(L+330,1170,130,t,-1);rodillo(L+560,1130,130,t,1);rodillo(L+560,1410,130,t,-1);rodillo(L+900,1410,110,t,-1);
  X.fillStyle='#22252b';X.fillRect(L+150,1540,960,60);X.fillRect(L+190,1600,60,400);X.fillRect(L+1010,1600,60,400);
  for(let i=0;i<7;i++){const u=((t-xn)*.42+i/7)%1;if(t<xn-.2)continue;const x=lerp(L+1250,L+D+260+(i%3)*260,u),y=1250-Math.sin(u*Math.PI)*420+(i%3)*30;diario(x,y,150,u*5+i,Math.min(1,u*6)*(1-Math.max(0,u-.85)*6))}
  X.fillStyle=gl(0,0,0,1700,[[0,'#0c0a18'],[1,'#241a30']]);X.fillRect(L+D-200,-900,2400,3800);[0,1,2].forEach(i=>local(L+D+130+i*380,1420,1,1));X.fillStyle='#120e16';X.fillRect(L+D-200,1420,2400,1500);
  const le=eio(seg(t,xl-.5,xl+.1));[[260,'cliente'],[560,'jugadora'],[840,'gamer']].forEach(([x,lk],i)=>{figura(L+D+x,1700,1.2,{look:lk},t,'parado',le>.6?'triste':'feliz',i%2?-1:1);if(le>0)diario(L+D+x,lerp(1320,1470,le),150,(i-1)*.08,le)})});
 arriba(L,.6)}

// ---------- 10 · dejaron de ir: cerca de 500 millones de libras de valor desaparecieron ----------
function p10(L,t){const c=T.c10,xs=T.x_stopped,x5=T.x_500,xd=T.x_disappeared,f=T.c11,van=eio(seg(t,c+.1,xs+.9)),cae=eio(seg(t,x5-.6,x5+.5)),fr=eio(seg(t,xd-.2,xd+.7));
 plano(L,t,[[c,540,1120,1.14],[x5,540,1090,1.04],[f,540,1080,1]],cm=>{tienda(L,cm,t,{on:1-.75*van});mostrador(L,1620);
  [[200,'cliente'],[420,'jugadora'],[650,'gamer'],[860,'cliente']].forEach(([x,lk],i)=>{const u=eio(seg(t,c+.15+i*.16,xs+.5+i*.16));if(u<1){X.save();X.globalAlpha=1-u;figura(L+x+u*(i%2?520:-520),1560,1.2,{look:lk},t,u>0?'camina':'parado','triste',i%2?1:-1);X.restore()}});
  const P=[[90,760],[260,720],[430,740],[560,700],[660,1010],[800,1220],[960,1330]],n=1+cae*(P.length-1);X.strokeStyle=ORO;X.lineWidth=14;X.lineCap='round';X.lineJoin='round';
  if(fr<1){X.globalAlpha=1-fr;X.beginPath();X.moveTo(L+P[0][0],P[0][1]);for(let i=1;i<=Math.min(P.length-1,Math.floor(n));i++)X.lineTo(L+P[i][0],P[i][1]);if(n<P.length){const i=Math.floor(n),q=n-i;if(i+1<P.length)X.lineTo(L+lerp(P[i][0],P[i+1][0],q),lerp(P[i][1],P[i+1][1],q))}X.stroke();X.globalAlpha=1}
  if(fr>0)for(let i=0;i<P.length-1;i++){X.save();X.translate(L+(P[i][0]+P[i+1][0])/2+(rnd(i)-.5)*160*fr,(P[i][1]+P[i+1][1])/2+fr*fr*520+rnd(i+4)*120*fr);X.rotate(Math.atan2(P[i+1][1]-P[i][1],P[i+1][0]-P[i][0])+fr*(rnd(i+9)-.5)*5);X.globalAlpha=1-fr*.8;X.beginPath();X.moveTo(-70,0);X.lineTo(70,0);X.stroke();X.restore()}
  const q=eio(seg(t,x5-.05,x5+.3));if(q>0){X.save();X.globalAlpha=q;X.fillStyle='rgba(12,8,14,.72)';rr(L+130,1120,820,230,30);X.fill();txt('£500 MILLION',L+540,1238,112,ORO,{w:900});X.restore()}});
 tinte(L,'40,60,120',.12*van);arriba(L,.6)}

// ---------- 11 · dieciocho meses después, estaba fuera del negocio ----------
function sillon(x,yb,s,rot){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(0,4,150,18,0,0,7);X.fill();X.strokeStyle='#2a2d34';X.lineWidth=14;X.lineCap='round';[-1,-.4,.4,1].forEach(q=>{X.beginPath();X.moveTo(0,-60);X.lineTo(q*120,-4);X.stroke()});X.fillStyle='#2a2d34';X.fillRect(-9,-190,18,140);
 X.save();X.translate(0,-190);X.transform(Math.cos(rot||0),0,0,1,0,0);X.fillStyle='#3a2416';rr(-130,-40,260,60,22);X.fill();X.fillStyle=gl(-130,0,130,0,[[0,'#4a2e1c'],[.5,'#6b452c'],[1,'#3a2416']]);rr(-120,-420,240,390,50);X.fill();X.fillStyle='rgba(0,0,0,.2)';[-250,-150].forEach(y=>{[-50,50].forEach(q=>{X.beginPath();X.arc(q,y,8,0,7);X.fill()})});X.fillStyle='#3a2416';rr(-160,-150,34,120,14);X.fill();rr(126,-150,34,120,14);X.fill();X.restore();X.restore()}
function p11(L,t){const c=T.c11,xo=T.x_out,f=T.c12;
 plano(L,t,[[c,640,1120,1.08],[f,500,1100,1.26]],cm=>{interior(L,{p0:'#4a4f58',p1:'#7a808a',tex:'concreto',ta:.2,yp:1420,pisoTex:'madera',pa:.5,piso:['#4a3a2e','#3e3026']});const px=par(cm,.4);
  ventanaV(L+60+px,560,300,460,'dia',t,{});X.fillStyle='rgba(40,50,64,.35)';X.fillRect(L+44+px,544,332,492);
  X.fillStyle='#2a2f38';X.fillRect(L+820+px,560,240,860);X.fillStyle='#8a909a';X.fillRect(L+836+px,576,208,844);
  borroso(7,()=>{X.globalAlpha=.8*(1-eio(seg(t,xo+.3,f)));traje(L+lerp(900,1010,seg(t,c,f))+px,1420,.9,{espalda:1,col:'#3a424e'});X.globalAlpha=1});
  sillon(L+430,1600,1.5,Math.sin((t-c)*1.4)*.5*(1-seg(t,c,f)));meson(L,1640,{tex:'madera',col:'#553a23',ta:.9});caja(L+760,1640,1.5,0);
  for(let i=0;i<5;i++){const u=seg(t,c+i*.14,c+.7+i*.14);if(u>0&&u<1){X.save();X.translate(L+250+u*120,1480-Math.sin(u*Math.PI)*260);X.rotate(u*4+i);X.globalAlpha=1-u;X.fillStyle=PAPEL;X.fillRect(-40,-50,80,100);X.fillStyle='#c0392b';X.fillRect(-40,-50,80,22);X.restore()}}
  X.fillStyle='#b9bec6';rr(L+190,1540,130,100,8);X.fill();X.fillStyle=PAPEL;X.fillRect(L+200,1470,110,130);X.fillStyle='#c0392b';X.fillRect(L+200,1470,110,30)});
 tinte(L,'90,100,120',.1);arriba(L,.6)}

// ---------- 12 · lección: nunca bromees con la calidad de lo que vendes; tus clientes pueden estar escuchando ----------
function p12(L,t){const c=T.c12,xq=T.x_quality,xl=T.x_listening,f=T.c13,ap=eio(seg(t,xl-.3,xl+.6));
 plano(L,t,[[c,560,1230,1.6],[xq,555,1230,1.5],[xl,545,1200,1.2],[f,540,1180,1.06]],cm=>{X.fillStyle='#17121c';X.fillRect(L-1400,-900,3900,3800);
  X.fillStyle='#2a1a2a';rr(L+60,800,960,920,20);X.fill();X.fillStyle='#7a2b45';X.beginPath();X.moveTo(L+30,740);X.lineTo(L+1050,740);X.lineTo(L+1090,830);X.lineTo(L-10,830);X.closePath();X.fill();X.fillStyle=`rgb(${Math.round(lerp(255,26,ap))},${Math.round(lerp(214,30,ap))},${Math.round(lerp(140,44,ap))})`;rr(L+110,880,860,790,10);X.fill();
  luz(L+540,1250,700,OR,.3*(1-ap));[[250,0],[540,1],[830,2]].forEach(([x,i])=>{X.globalAlpha=1-.7*ap;busto(L+x,1560,1.1+.15*(i%2));X.globalAlpha=1});
  X.save();X.globalAlpha=.22*(1-ap);X.fillStyle='#2a3a4a';X.beginPath();X.arc(L+770,1030,110,0,7);X.fill();X.beginPath();X.moveTo(L+560,1670);X.quadraticCurveTo(L+580,1200,L+770,1170);X.quadraticCurveTo(L+960,1200,L+960,1670);X.closePath();X.fill();X.restore();
  X.fillStyle='rgba(255,255,255,.07)';X.beginPath();X.moveTo(L+110,880);X.lineTo(L+380,880);X.lineTo(L+220,1670);X.lineTo(L+110,1670);X.closePath();X.fill();
  mano(L+470,1330,-.9,1.7,1,{curl:[.5,.8,.9,.9],pulgar:-.3,pulgarCurl:.4,parte:'atras',lx:196,ly:-6});anillo(L+478,1260,1.5);luz(L+478,1190,120,'200,240,255',.5*(1-.5*ap));mano(L+470,1330,-.9,1.7,1,{curl:[.5,.8,.9,.9],pulgar:-.3,pulgarCurl:.4,parte:'pulgar',lx:196,ly:-6})});
 const q=eio(seg(t,c+.05,c+.35))*(1-eio(seg(t,xq+.8,xq+1.2)));if(q>0){X.save();X.globalAlpha=q;tarj(L+250,560,300,96,16,ORO,{sa:.3});txt('LESSON',L+250,564,58,'#2a1a0c',{w:900});X.restore()}
 tinte(L,'40,60,120',.12*ap);arriba(L,.6)}

// ---------- 13 · CTA: el micrófono apagado junto a una caja cerrada ----------
function p13(L,t){const c=T.c13,o=ruta(t,[[c,470,1160,1.14,-.03],[c+2.4,535,1010,1.02,0],[T.fin,540,1000,1,.012]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{X.fillStyle=gl(0,0,0,1920,[[0,'#0c0810'],[1,'#22121c']]);X.fillRect(L-1400,-900,3900,3800);tex('tela',L-400,300,1900,1700,{a:.14,v:3});
  X.fillStyle='#5a1f33';X.fillRect(L-1400,1480,3900,900);tex('tela',L-1400,1480,3900,500,{a:.4,v:3});X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-1400,1480,3900,8);
  luz(L+470,1380,360,OR,.26);micro(L+250,1490,.5,{rot:-.2,on:0});caja(L+520,1492,1.6,0)},o[3]);
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_smdm18_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SMDM18 · FIN =====
</script>
