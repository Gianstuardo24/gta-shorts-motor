<script>
// ===== DC · SGTAEN14 · INICIO ===== (GTA EN 14h · DON'T Stop for This Car in GTA 6 · lote del 28-nov · una escena por línea del guion)
// Sin personajes ni arte del juego: el jugador es una silueta genérica. Sin logos. El trofeo es una placa propia con el nombre que dice el guion. El "código" son símbolos abstractos (no se inventa uno).
(function(){
const {cam,cierreCanal,SET}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,noche,tarj,silueta,desenfoca,borroso}=window.B28;
const CIAN='90,240,255',AMB='255,190,110',VL='90,255,160';

function pinos(L,y,n,h,col,px,sem,t){X.fillStyle=col;for(let i=0;i<n;i++){const x=L-700+i*(2900/n)+(rnd(i+sem)-.5)*120+px,hh=h*(.7+.6*rnd(i+sem+9)),w=hh*.3,s=Math.sin((t||0)*.8+i)*4;X.beginPath();X.moveTo(x-w,y);X.lineTo(x+s,y-hh);X.lineTo(x+w,y);X.closePath();X.fill();X.beginPath();X.moveTo(x-w*.74,y-hh*.36);X.lineTo(x+s,y-hh*1.08);X.lineTo(x+w*.74,y-hh*.36);X.closePath();X.fill();X.fillRect(x-7,y-4,14,40)}}
function pino(x,y,h,col,k){const w=h*(k||.16);X.fillStyle=col;X.beginPath();X.moveTo(x-w,y);X.lineTo(x,y-h);X.lineTo(x+w,y);X.closePath();X.fill();X.beginPath();X.moveTo(x-w*.74,y-h*.36);X.lineTo(x,y-h*1.08);X.lineTo(x+w*.74,y-h*.36);X.closePath();X.fill()}
function bosque(L,cm,t,o){o=o||{};const yh=o.yh||1380;noche(L,t,{c0:'#04060e',c1:'#101a34',y1:yh,n:60,ys:430,yh:yh-520,sem:o.sem||0});if(o.luna!==false){luz(L+(o.lx||860)+par(cm,.8),620,260,'220,230,255',.3);X.fillStyle='#e9eef8';X.beginPath();X.arc(L+(o.lx||860)+par(cm,.8),620,46,0,7);X.fill()}
 pinos(L,yh+6,13,520,'#0c1420',par(cm,.6),3,t);pinos(L,yh+10,10,700,'#070c14',par(cm,.35),11,t);X.fillStyle='#0a0f14';X.fillRect(L-1400,yh,3900,1400)}
function camino(L,y,h,t,o){o=o||{};X.fillStyle='#1c1f26';X.fillRect(L-1400,y,3900,h);tex('concreto',L-1400,y,3900,h,{a:.22,v:6});X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-1400,y,3900,6);X.fillStyle='#d9b24a';for(let i=-8;i<22;i++){X.fillRect(L+i*230+(o.dx||0),y+h*.5-6,120,12)}X.fillStyle='#0c1014';X.fillRect(L-1400,y+h,3900,1400)}
// auto genérico de lado (trompa a la derecha). puerta: 0..1 abierta · refl: -1..2 posición del reflejo que cruza el parabrisas
function auto(x,yb,s,o){o=o||{};const c=o.col||'#6a2f3a',c2=o.col2||'#4a1f28';X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(0,0,330,26,0,0,7);X.fill();
 if(o.faros){haz(300,-96,900,-40,26,200,'255,236,190',.22);luz(304,-96,60,'255,236,190',.8)}
 X.fillStyle=gl(0,-250,0,-40,[[0,c],[1,c2]]);X.beginPath();X.moveTo(-320,-60);X.lineTo(-316,-130);X.quadraticCurveTo(-300,-160,-240,-164);X.lineTo(-170,-240);X.quadraticCurveTo(-150,-258,-110,-258);X.lineTo(70,-258);X.quadraticCurveTo(110,-256,140,-232);X.lineTo(214,-164);X.quadraticCurveTo(300,-150,316,-120);X.lineTo(322,-60);X.closePath();X.fill();
 X.fillStyle='#0c1620';X.beginPath();X.moveTo(-150,-168);X.lineTo(-100,-238);X.lineTo(-10,-238);X.lineTo(-10,-168);X.closePath();X.fill();X.beginPath();X.moveTo(8,-168);X.lineTo(8,-238);X.lineTo(70,-238);X.quadraticCurveTo(100,-236,120,-218);X.lineTo(176,-168);X.closePath();X.fill();
 if(o.refl!==undefined){X.save();X.beginPath();X.moveTo(8,-168);X.lineTo(8,-238);X.lineTo(70,-238);X.quadraticCurveTo(100,-236,120,-218);X.lineTo(176,-168);X.closePath();X.clip();const rx=lerp(-40,220,o.refl);X.fillStyle=`rgba(${CIAN},.75)`;X.beginPath();X.moveTo(rx,-250);X.lineTo(rx+40,-250);X.lineTo(rx+10,-160);X.lineTo(rx-30,-160);X.closePath();X.fill();X.restore()}
 X.fillStyle='rgba(255,255,255,.1)';X.fillRect(-316,-132,632,6);X.fillStyle='#f2c94c';rr(296,-112,24,30,6);X.fill();X.fillStyle='#c0392b';rr(-322,-120,16,34,5);X.fill();
 [-200,206].forEach(q=>{X.fillStyle='#0a0c10';X.beginPath();X.arc(q,-50,62,0,7);X.fill();X.fillStyle='#8e98a4';X.beginPath();X.arc(q,-50,30,0,7);X.fill();X.fillStyle='#22262b';X.beginPath();X.arc(q,-50,12,0,7);X.fill()});
 const pu=o.puerta||0;if(pu>0){X.fillStyle='#07090c';X.beginPath();X.moveTo(-6,-70);X.lineTo(-6,-236);X.lineTo(150,-236);X.lineTo(176,-168);X.lineTo(176,-70);X.closePath();X.fill();if(o.luzInt)luz(86,-160,150,AMB,.5);
  X.save();X.translate(176,-150);X.transform(1-pu*.72,pu*.1,0,1,0,0);X.fillStyle=c;X.beginPath();X.moveTo(-182,80);X.lineTo(-182,-18);X.lineTo(0,-18);X.lineTo(0,80);X.closePath();X.fill();X.fillStyle='#0c1620';X.beginPath();X.moveTo(-176,-22);X.lineTo(-176,-86);X.lineTo(-60,-86);X.lineTo(-6,-22);X.closePath();X.fill();X.strokeStyle=c;X.lineWidth=10;X.stroke();X.restore()}
 X.restore()}
function autoAtras(x,yb,s,t,o){o=o||{};const c='#6a2f3a',sw=Math.sin(t*1.6)*.12;X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(0,0,250,22,0,0,7);X.fill();
 X.save();X.translate(-196,-150);X.transform(.5+sw,.0,-.06,1,0,0);X.fillStyle='#4a1f28';rr(-150,-80,150,190,10);X.fill();X.fillStyle='#0c1620';rr(-136,-70,120,76,8);X.fill();X.restore();
 X.fillStyle='#0a0c10';[-150,150].forEach(q=>{rr(q-34,-70,68,76,14);X.fill()});X.fillStyle=gl(0,-300,0,-40,[[0,c],[1,'#4a1f28']]);X.beginPath();X.moveTo(-200,-50);X.lineTo(-204,-170);X.quadraticCurveTo(-190,-200,-150,-206);X.lineTo(-116,-290);X.quadraticCurveTo(0,-312,116,-290);X.lineTo(150,-206);X.quadraticCurveTo(190,-200,204,-170);X.lineTo(200,-50);X.closePath();X.fill();
 X.fillStyle='#0c1620';X.beginPath();X.moveTo(-126,-212);X.lineTo(-100,-278);X.quadraticCurveTo(0,-296,100,-278);X.lineTo(126,-212);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.1)';X.fillRect(-200,-172,400,6);
 [-1,1].forEach(q=>{X.fillStyle='#e23a3a';rr(q*150-40,-166,80,34,10);X.fill();luz(q*150,-150,110,'255,60,50',.5)});X.fillStyle='#e9eef2';rr(-60,-110,120,36,6);X.fill();X.fillStyle='#22262b';rr(-210,-74,420,30,10);X.fill();
 for(let i=0;i<16;i++){X.fillStyle='rgba(200,230,255,.5)';X.beginPath();X.arc(-180+rnd(i+2)*360,-190+rnd(i+20)*120,3+rnd(i)*3,0,7);X.fill()}X.restore()}
function prenda(x,y,s,tipo,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.35)';X.beginPath();X.ellipse(4,10,70,14,0,0,7);X.fill();
 if(tipo===0){X.fillStyle='#d9d4c6';X.beginPath();X.moveTo(-40,-40);X.lineTo(-76,-22);X.lineTo(-62,6);X.lineTo(-40,-4);X.lineTo(-40,44);X.lineTo(40,44);X.lineTo(40,-4);X.lineTo(62,6);X.lineTo(76,-22);X.lineTo(40,-40);X.quadraticCurveTo(0,-22,-40,-40);X.fill()}
 else if(tipo===1){X.fillStyle='#3a5a8a';X.beginPath();X.moveTo(-40,-50);X.lineTo(40,-50);X.lineTo(52,54);X.lineTo(14,54);X.lineTo(0,-10);X.lineTo(-14,54);X.lineTo(-52,54);X.closePath();X.fill()}
 else if(tipo===2){X.fillStyle='#e9eef2';X.beginPath();X.moveTo(-50,10);X.quadraticCurveTo(-52,-26,-20,-26);X.lineTo(8,-26);X.quadraticCurveTo(30,0,56,6);X.quadraticCurveTo(64,22,50,24);X.lineTo(-50,24);X.closePath();X.fill();X.fillStyle='#c0392b';X.fillRect(-50,16,104,8)}
 else{X.fillStyle='#c0392b';X.beginPath();X.arc(0,0,40,Math.PI,0);X.fill();rr(-40,-4,104,14,7);X.fill()}X.restore()}
function platillo(x,y,s,t,o){o=o||{};X.save();X.translate(x,y);X.scale(s,s);luz(0,10,420,CIAN,.3);X.fillStyle='rgba(160,240,255,.5)';X.beginPath();X.ellipse(0,-34,96,74,0,Math.PI,0);X.fill();X.fillStyle=gl(-300,0,300,0,[[0,'#3a4450'],[.5,'#aab6c2'],[1,'#2f3842']]);X.beginPath();X.ellipse(0,0,300,56,0,0,7);X.fill();X.fillStyle='#1c232b';X.beginPath();X.ellipse(0,22,190,26,0,0,7);X.fill();
 for(let i=0;i<7;i++){const a=((i/7)+t*.18)%1,xx=Math.cos(a*6.28)*250,z=Math.sin(a*6.28);if(z>-.2){X.fillStyle=`rgba(${CIAN},${.5+.5*z})`;X.beginPath();X.arc(xx,6+z*20,10+4*z,0,7);X.fill()}}X.restore()}
function placaLogro(x,y,s,o){o=o||{};X.save();X.translate(x,y);X.scale(s*(o.sx===undefined?1:o.sx),s);X.fillStyle='rgba(0,0,0,.4)';rr(-410,-96,840,220,40);X.fill();X.fillStyle=gl(0,-110,0,110,[[0,'#1c2a38'],[1,'#0f1822']]);rr(-420,-110,840,220,40);X.fill();X.strokeStyle=`rgba(${CIAN},.8)`;X.lineWidth=6;rr(-420,-110,840,220,40);X.stroke();
 X.fillStyle='#f2c94c';X.beginPath();X.moveTo(-350,-56);X.lineTo(-270,-56);X.quadraticCurveTo(-270,14,-310,24);X.quadraticCurveTo(-350,14,-350,-56);X.fill();X.fillRect(-318,22,16,26);rr(-340,46,60,14,5);X.fill();X.strokeStyle='#f2c94c';X.lineWidth=8;X.beginPath();X.arc(-350,-30,20,1.57,4.71);X.stroke();X.beginPath();X.arc(-270,-30,20,-1.57,1.57);X.stroke();
 if(o.sub>0){X.globalAlpha=o.sub;txt('HIDDEN TROPHY',70,-46,40,`rgb(${CIAN})`,{w:800})}if(o.tit>0){X.globalAlpha=o.tit;txt('The Truth Is Out There',70,24,54,'#fff',{w:800})}else if(o.oculto){X.globalAlpha=1;X.fillStyle='rgba(255,255,255,.2)';rr(-190,-6,520,30,14);X.fill()}X.restore()}
function glifo(x,y,s,i,a,rgb){if(a<=0)return;X.save();X.translate(x,y);X.scale(s,s);X.globalAlpha=a;X.fillStyle='rgba(8,20,24,.9)';rr(-50,-60,100,120,14);X.fill();X.strokeStyle=`rgb(${rgb||CIAN})`;X.lineWidth=7;X.lineCap='round';X.lineJoin='round';rr(-50,-60,100,120,14);X.stroke();X.beginPath();
 const k=i%5;if(k===0){X.arc(0,0,26,0,7);X.moveTo(4,0);X.arc(0,0,4,0,7)}else if(k===1){X.moveTo(0,-32);X.lineTo(28,26);X.lineTo(-28,26);X.closePath()}else if(k===2){X.moveTo(-26,-24);X.lineTo(26,-24);X.moveTo(-26,0);X.lineTo(26,0);X.moveTo(-26,24);X.lineTo(26,24)}else if(k===3){X.moveTo(-28,-26);X.lineTo(0,0);X.lineTo(-28,26);X.moveTo(4,-26);X.lineTo(30,0);X.lineTo(4,26)}else{X.moveTo(0,-32);X.lineTo(0,32);X.moveTo(-28,0);X.arc(0,0,28,Math.PI,0)}X.stroke();X.restore()}
function pasillo(L,cx,cy,t,rgb){X.fillStyle='#04100c';X.fillRect(L-900,-900,2900,3800);for(let i=7;i>=0;i--){const q=((i+(t*.6%1))/8),s=.08+q*q*1.5,w=900*s,h=1300*s;X.strokeStyle=`rgba(${rgb||VL},${.15+.5*q})`;X.lineWidth=4+10*q;X.strokeRect(L+cx-w/2,cy-h/2,w,h);X.fillStyle=`rgba(${rgb||VL},${.05*q})`;X.fillRect(L+cx-w/2,cy-h/2,w,h*.06)}luz(L+cx,cy,360,rgb||VL,.35)}
function puertaLab(L,cx,cy,w,h,ab,rgb){const d=ab*w*.52;[-1,1].forEach(q=>{const x=q<0?L+cx-w/2-d:L+cx+d;X.fillStyle=gl(x,0,x+w/2,0,[[0,'#2a343a'],[.5,'#55636b'],[1,'#222b30']]);X.fillRect(x,cy-h/2,w/2,h);X.fillStyle='rgba(0,0,0,.3)';for(let i=0;i<5;i++)X.fillRect(x+20,cy-h/2+40+i*h/5,w/2-40,10);X.fillStyle='#d9b24a';for(let i=0;i<8;i++){X.beginPath();X.moveTo(x+(q<0?w/2-30:0)+i*0,cy-h/2+i*h/8);X.lineTo(x+(q<0?w/2:30),cy-h/2+i*h/8+(q<0?0:0));X.lineTo(x+(q<0?w/2:30),cy-h/2+i*h/8+h/16);X.lineTo(x+(q<0?w/2-30:0),cy-h/2+i*h/8+h/16);X.closePath();X.fill()}});
 X.strokeStyle='#1a2226';X.lineWidth=30;X.strokeRect(L+cx-w/2-15,cy-h/2-15,w+30,h+30);X.fillStyle=`rgb(${ab>.1?VL:'255,90,70'})`;X.beginPath();X.arc(L+cx,cy-h/2-56,16,0,7);X.fill()}
function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#101a24',{sa:.3,borde:`rgba(${CIAN},.6)`,lw:3});txt(texto,x,y+4*s,(o.ts||46)*s,o.tc||'#fff',{w:800});X.restore()}

// ---------- 01 · gancho: ruta de noche, auto abandonado con la puerta abierta y ropa hacia el bosque ----------
function p01(L,t){const xa=T.x_abandoned,xb=T.x_bait,xc=T.x_careful,xw=T.x_woods,f=T.c02,rf=seg(t,xb-.5,xb+.5),gl2=eio(seg(t,xw-.4,xw+.4));
 plano(L,t,[[0,860,1500,1.9],[xa,640,1330,1.24],[xb,600,1260,1.14],[xw,500,1200,1.08],[f,460,1180,1.14]],cm=>{bosque(L,cm,t,{luna:false});
  if(gl2>0)luz(L+140+par(cm,.5),1240,360,CIAN,.3*gl2*(.7+.3*Math.sin(t*5)));camino(L,1470,330,t);
  [[270,1545,2,.2],[150,1500,0,-.3],[40,1462,3,.1]].forEach((p,i)=>prenda(L+p[0],p[1],1-.12*i,p[2],p[3]));
  auto(L+640,1560,1.05,{puerta:.9,luzInt:1,faros:1,refl:rf>0&&rf<1?rf:undefined})});
 arriba(L,.6)}

// ---------- 02 · el mapa: la ruta al este de Port Gellhorn, cerca del Starlet Motel ----------
function p02(L,t){const c=T.c02,xe=T.x_east,xp=T.x_port,xs=T.x_starlet,f=T.c03,u=eio(seg(t,c+.3,xs+.2)),P=q=>[L+lerp(240,900,q),1180+Math.sin(q*3.2)*70-q*90];
 plano(L,t,[[c,420,1120,1.2],[xs,640,1090,1.14],[f-.5,700,1060,1.2],[f,860,1010,2.3]],cm=>{X.fillStyle='#0c1a22';X.fillRect(L-900,-900,2900,3800);X.strokeStyle='rgba(120,200,220,.07)';X.lineWidth=3;for(let i=-4;i<26;i++){X.beginPath();X.moveTo(L-200+i*70,300);X.lineTo(L-200+i*70,1900);X.stroke();X.beginPath();X.moveTo(L-400,300+i*70);X.lineTo(L+1500,300+i*70);X.stroke()}
  X.fillStyle='#16303a';X.beginPath();X.moveTo(L-100,820);X.quadraticCurveTo(L+300,700,L+700,780);X.quadraticCurveTo(L+1050,820,L+1200,760);X.lineTo(L+1200,1560);X.quadraticCurveTo(L+700,1640,L+300,1540);X.quadraticCurveTo(L+40,1500,L-100,1560);X.closePath();X.fill();X.strokeStyle='rgba(120,220,230,.35)';X.lineWidth=5;X.stroke();
  X.strokeStyle='rgba(255,255,255,.08)';X.lineWidth=7;X.lineCap='round';[[300,860,520,1080],[700,820,640,1040],[420,1540,560,1300],[980,1500,860,1240],[120,1000,330,1150]].forEach(r=>{X.beginPath();X.moveTo(L+r[0],r[1]);X.quadraticCurveTo(L+(r[0]+r[2])/2+40,(r[1]+r[3])/2,L+r[2],r[3]);X.stroke()});for(let i=0;i<26;i++){X.fillStyle='rgba(60,150,120,.35)';X.beginPath();X.arc(L+rnd(i+40)*1100,860+rnd(i+70)*640,10+rnd(i)*12,0,7);X.fill()}for(let i=0;i<7;i++){X.strokeStyle='rgba(120,220,230,.14)';X.lineWidth=4;X.beginPath();X.moveTo(L-60+i*190,700-i%2*40);X.quadraticCurveTo(L+20+i*190,680-i%2*40,L+90+i*190,700-i%2*40);X.stroke()}
  X.strokeStyle='rgba(255,255,255,.18)';X.lineWidth=16;X.lineCap='round';X.beginPath();for(let i=0;i<=30;i++){const p=P(i/30);i?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1])}X.stroke();
  X.strokeStyle=`rgb(${AMB})`;X.lineWidth=9;X.setLineDash([22,16]);X.lineDashOffset=-t*60;X.beginPath();for(let i=0;i<=30*u;i++){const p=P(i/30);i?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1])}X.stroke();X.setLineDash([]);
  const a=P(0);X.fillStyle='#e9eef2';[[-30,-20,26,40],[0,-36,30,56],[34,-14,24,34]].forEach(r=>{X.fillRect(a[0]+r[0],a[1]+r[1],r[2],r[3])});placa(a[0]+190,a[1]+120,1,'PORT GELLHORN',eio(seg(t,xp-.1,xp+.2)),{ts:38,w:400});
  const m=P(.78);X.fillStyle='#c0392b';rr(m[0]-44,m[1]-120,88,56,8);X.fill();X.fillStyle='#fff';X.fillRect(m[0]-4,m[1]-64,8,50);rr(m[0]-26,m[1]-104,52,10,4);X.fill();rr(m[0]-26,m[1]-88,34,10,4);X.fill();placa(m[0]-40,m[1]-190,1,'STARLET MOTEL',eio(seg(t,xs-.1,xs+.2)),{ts:38,w:400});
  const p=P(u),pu=.5+.5*Math.sin(t*6);luz(p[0],p[1],90+30*pu,AMB,.6);X.fillStyle=`rgb(${AMB})`;X.beginPath();X.arc(p[0],p[1],20,0,7);X.fill();
  const q=eio(seg(t,xe-.1,xe+.2));if(q>0){X.save();X.globalAlpha=q;X.translate(L+900,1520);X.strokeStyle='#fff';X.fillStyle='#fff';X.lineWidth=7;X.beginPath();X.arc(0,0,60,0,7);X.stroke();X.beginPath();X.moveTo(70,0);X.lineTo(30,-22);X.lineTo(30,22);X.closePath();X.fill();txt('E',96,2,44,'#fff',{w:900});X.restore()}});
 arriba(L,.6)}

// ---------- 03 · de noche, después de las 2: desde adentro, el reloj del tablero ----------
function p03(L,t){const c=T.c03,x2=T.x_2,f=T.c04,h=t<x2-.25?'1:59':t<x2+1.3?'2:00':'2:01',g=golpe(t,x2-.25,.5);
 plano(L,t,[[c,540,1010,1.02],[x2,560,1040,1.14],[f,570,1050,1.2]],cm=>{noche(L,t,{c0:'#04060e',c1:'#101a34',y1:1150,n:50,ys:430,yh:500,sem:4});pinos(L,1156,12,420,'#070c14',0,5,t);
  X.fillStyle='#14171c';X.beginPath();X.moveTo(L-400,1920);X.lineTo(L+500,1150);X.lineTo(L+580,1150);X.lineTo(L+1500,1920);X.closePath();X.fill();
  for(let i=0;i<6;i++){const q=((t*.9+i/6)%1),y=1150+q*q*780,w=6+q*q*40;X.fillStyle=`rgba(217,178,74,${.3+.6*q})`;X.fillRect(L+540-w/2,y,w,30+q*q*150)}haz(L+540,1900,L+540,1200,560,90,'255,236,190',.1);
  X.fillStyle='#0a0c10';X.beginPath();X.moveTo(L-400,1500);X.quadraticCurveTo(L+540,1390,L+1500,1500);X.lineTo(L+1500,2300);X.lineTo(L-400,2300);X.closePath();X.fill();X.strokeStyle='#14181e';X.lineWidth=60;X.beginPath();X.arc(L+250,1900,330,Math.PI*1.12,Math.PI*1.9);X.stroke();
  X.fillStyle='#05080a';rr(L+560,1560,400,170,24);X.fill();X.strokeStyle='rgba(90,240,255,.3)';X.lineWidth=4;rr(L+560,1560,400,170,24);X.stroke();luz(L+760,1645,200+60*g,CIAN,.2+.3*g);txt(h,L+760,1650,120,`rgb(${CIAN})`,{w:900});
  X.fillStyle='#0a0c10';X.fillRect(L-400,300,340,1300);X.fillRect(L+1140,300,400,1300);X.beginPath();X.moveTo(L-60,300);X.lineTo(L+40,300);X.lineTo(L-60,900);X.closePath();X.fill();X.beginPath();X.moveTo(L+1140,300);X.lineTo(L+1040,300);X.lineTo(L+1140,900);X.closePath();X.fill()});
 arriba(L,.62)}

// ---------- 04 · un auto dejado en la ruta, con la puerta abierta de par en par ----------
function p04(L,t){const c=T.c04,xd=T.x_door,f=T.c05;
 plano(L,t,[[c,540,1260,1],[f,500,1230,1.32]],cm=>{bosque(L,cm,t,{sem:6,luna:false});X.fillStyle='#1c1f26';X.beginPath();X.moveTo(L-600,1920);X.lineTo(L+440,1380);X.lineTo(L+640,1380);X.lineTo(L+1700,1920);X.closePath();X.fill();tex('concreto',L-600,1380,2300,540,{a:.12,v:6});
  for(let i=0;i<5;i++){const q=i/5,y=1400+q*q*520,w=8+q*q*30;X.fillStyle='#d9b24a';X.fillRect(L+540-w/2,y,w,24+q*q*90)}
  haz(L+540,1460,L+540,1000,200,420,'255,236,190',.1);autoAtras(L+560,1640,1.5,t,{});luz(L+560,1500,520,'255,60,50',.12)});
 arriba(L,.6)}

// ---------- 05 · al lado, un rastro de ropa que se mete entre los árboles ----------
function p05(L,t){const c=T.c05,xt=T.x_trees,f=T.c06,R=[[760,1700,1.5,0,.2],[640,1560,1.2,1,-.3],[560,1450,.95,2,.2],[500,1370,.76,3,-.1],[462,1310,.6,0,.3],[440,1264,.46,2,-.2]];
 plano(L,t,[[c,640,1500,1.2],[xt,500,1300,1.3],[f,470,1240,1.4]],cm=>{bosque(L,cm,t,{sem:8,yh:1240,lx:820});X.fillStyle=gl(0,1240,0,1920,[[0,'#0a1410'],[1,'#16241a']]);X.fillRect(L-900,1240,2900,900);tex('pasto',L-900,1240,2900,700,{a:.14,s:1.4});
  haz(L+1300,1640,L+420,1300,220,60,'255,236,190',.22);
  R.forEach((p,i)=>{const a=eio(seg(t,c+.15+i*.2,c+.4+i*.2));if(a>0){X.save();X.globalAlpha=a;prenda(L+p[0],p[1],p[2],p[3],p[4]);X.restore()}});
  pinos(L,1250,3,900,'#04070b',par(cm,.1)-300,21,t);luz(L+430,1180,200,CIAN,.12*eio(seg(t,xt-.3,xt+.4)))});
 arriba(L,.6)}

// ---------- 06 · lo sigues y un OVNI luminoso aparece justo encima. Y sí, te lleva ----------
function p06(L,t){const c=T.c06,xu=T.x_ufo,xk=T.x_takes,f=T.c07,ap=eio(seg(t,xu-.5,xu+.2)),sub=eio(seg(t,xk-.2,f)),o=ruta(t,[[c,540,1340,1.16,0],[xu,540,1150,1.02,-.03],[f,560,1040,1.08,.03]]),uy=lerp(300,760,ap);
 cam(L,o[0],o[1],o[2],540,1000,()=>{bosque(L,{0:o[0]},t,{sem:10,yh:1500,luna:false});X.fillStyle=gl(0,1500,0,1920,[[0,'#0a1410'],[1,'#16241a']]);X.fillRect(L-900,1500,2900,900);
  if(ap>0){haz(L+540,uy+40,L+540,1560,110,300,CIAN,.3*ap);luz(L+540,1540,360,CIAN,.3*ap)}
  luz(L+540,1540,420,'150,190,220',.16,150);const sy=1560-sub*520,ss=1.15*(1-.25*sub);X.save();X.globalAlpha=1-.45*sub;silueta(L+540,sy+4,ss*1.05,ap>0?`rgba(${CIAN},${.75*ap})`:'rgba(150,180,210,.5)',{});silueta(L+540,sy,ss,'#06090c',{});X.restore();
  if(ap>0)platillo(L+540,uy,1.2,t,{});pino(L-150,1640,1700,'#030508');pino(L+1230,1640,1560,'#030508')},o[3]);
 arriba(L,.62)}

// ---------- 07 · G2: el encuentro es solo el comienzo. El OVNI se va y aparece una placa de logro ----------
function p07(L,t){const c=T.c07,xs=T.x_secret,xb=T.x_beginning,f=T.c08,va=eio(seg(t,c,xs)),en=eio(seg(t,xs-.25,xs+.2)),g=golpe(t,xs,.6);
 plano(L,t,[[c,540,820,1.02],[xs,540,1080,1.06],[f,540,1100,1.22]],cm=>{noche(L,t,{c0:'#04060e',c1:'#101a34',y1:1920,n:70,ys:300,yh:1500,sem:2});pinos(L,1920,12,420,'#070c14',0,3,t);
  if(va<1){X.save();X.globalAlpha=1-va;platillo(L+lerp(540,1000,va),lerp(700,420,va),lerp(1,.2,va),t,{});X.restore()}
  if(en>0){X.save();X.globalAlpha=en;luz(L+540,1120,500+80*g,CIAN,.2+.25*g);placaLogro(L+540,1120+(1-en)*120,.86+.04*g,{oculto:1});X.restore()}});
 arriba(L,.6)}

// ---------- 08 · un trofeo oculto: se llama The Truth Is Out There ----------
function p08(L,t){const c=T.c08,xt=T.x_trophy,xk=T.x_called,f=T.c09,gi=seg(t,c,c+.7),sx=Math.cos(gi*Math.PI*2);
 plano(L,t,[[c,540,1100,1.22],[xk,540,1090,1.14],[f,540,1085,1.2]],cm=>{noche(L,t,{c0:'#04060e',c1:'#101a34',y1:1920,n:70,ys:300,yh:1500,sem:2});pinos(L,1920,12,420,'#070c14',0,3,t);
  luz(L+540,1100,560,CIAN,.24+.1*Math.sin(t*3));placaLogro(L+540,1100,.88,{sx:gi<1?Math.max(.06,Math.abs(sx)):1,sub:eio(seg(t,xt-.6,xt-.3)),tit:eio(seg(t,xk+.15,xk+.5)),oculto:1});
  for(let i=0;i<8;i++){const u=((t*.4+i/8)%1);X.fillStyle=`rgba(${CIAN},${.7*(1-u)})`;X.beginPath();X.arc(L+140+rnd(i+3)*800,1360-u*520,4+3*rnd(i),0,7);X.fill()}});
 arriba(L,.6)}

// ---------- 09 · después tu personaje empieza a tener sueños extraños ----------
function p09(L,t){const c=T.c09,f=T.c10,o=ruta(t,[[c,500,1130,1.08,-.04],[f,580,1100,1.18,.04]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{interior(L,{p0:'#101826',p1:'#1c2c44',tex:'tela',ta:.14,yp:1520,piso:['#1a2230','#141a26']});
  X.fillStyle='#0a1018';X.fillRect(L+620,640,330,430);X.save();X.beginPath();X.rect(L+636,656,298,398);X.clip();X.fillStyle='#16284a';X.fillRect(L+636,656,298,398);for(let i=0;i<4;i++){const x=L+500+((t*130+i*150)%620);X.fillStyle=`rgba(${CIAN},.3)`;X.beginPath();X.moveTo(x,656);X.lineTo(x+50,656);X.lineTo(x-30,1054);X.lineTo(x-80,1054);X.closePath();X.fill()}X.restore();haz(L+790,860,L+360,1500,150,420,CIAN,.12);
  X.fillStyle='#2a1c14';rr(L+60,1330,800,230,20);X.fill();X.fillStyle='#e9eef2';rr(L+90,1290,180,90,30);X.fill();X.fillStyle='#3a5a8a';X.beginPath();X.moveTo(L+250,1380);X.quadraticCurveTo(L+420,1250+Math.sin(t*1.6)*6,L+840,1340);X.lineTo(L+850,1480);X.lineTo(L+250,1480);X.closePath();X.fill();X.fillStyle='#06090c';X.beginPath();X.arc(L+200,1310,48,0,7);X.fill();
  for(let i=0;i<5;i++){const a=eio(seg(t,c+.2+i*.3,c+.6+i*.3)),x=L+220+i*150,y=960-i%2*90+Math.sin(t*1.5+i)*14;if(i===2){X.save();X.globalAlpha=a*.9;platillo(x,y,.36,t,{});X.restore()}else glifo(x,y,.8,i,a*.9)}
  for(let i=0;i<3;i++){X.fillStyle=`rgba(255,255,255,${.5})`;X.beginPath();X.arc(L+250+i*36,1240-i*44,10+i*5,0,7);X.fill()}},o[3]);
 arriba(L,.6)}

// ---------- 10 · los sueños llevan a un código y a un laboratorio subterráneo ----------
function p10(L,t){const c=T.c10,xc=T.x_code,xl=T.x_lab,f=T.c11,ord=eio(seg(t,c+.2,xc)),ab=eio(seg(t,xl-.5,xl+.3));
 plano(L,t,[[c,540,1060,1.1],[xl-.5,540,1100,1.06],[f,540,1130,1.34]],cm=>{pasillo(L,540,1150,t);puertaLab(L,540,1150,640,900,ab);
  });
 tinte(L,'40,200,120',.06*ab);arriba(L,.72);
 // el código (símbolos abstractos, no se inventa uno): fragmentos que se ordenan en una fila, en pantalla y bajo la franja de subtítulos
 X.save();X.globalAlpha=ord;X.fillStyle='rgba(4,10,12,.85)';rr(L+130,450,820,180,26);X.fill();X.restore();for(let i=0;i<5;i++){const x0=L+200+rnd(i+3)*700,y0=760+rnd(i+9)*620;glifo(lerp(x0,L+240+i*150,ord),lerp(y0,540,ord),lerp(.9,1,ord),i,1,ord>.98?VL:CIAN)}}

// ---------- 11 · el auto nunca fue el secreto: era la puerta de entrada (corte por coincidencia de puertas) ----------
function p11(L,t){const c=T.c11,xn=T.x_never,xf=T.x_front,f=T.c12,z=eio(seg(t,xn-.2,xf+.3)),s=lerp(1,5.5,z*z),ab=eio(seg(t,xf-.1,xf+.6));
 plano(L,t,[[c,540,1150,1],[f,540,1150,1.1]],cm=>{pasillo(L,540,1150,t);puertaLab(L,540,1150,640,900,ab);
  if(z<1){X.save();X.translate(L+540,1150);X.scale(s,s);X.globalAlpha=1-eio(seg(z,.7,1));X.fillStyle='#07090c';X.beginPath();X.rect(-700,-1100,1400,2200);X.moveTo(-230,330);X.lineTo(230,330);X.lineTo(230,-190);X.lineTo(150,-330);X.lineTo(-230,-330);X.closePath();X.fill('evenodd');X.strokeStyle='#6a2f3a';X.lineWidth=26;X.lineJoin='round';X.beginPath();X.moveTo(-230,330);X.lineTo(230,330);X.lineTo(230,-190);X.lineTo(150,-330);X.lineTo(-230,-330);X.closePath();X.stroke();luz(0,0,420,AMB,.3*(1-z));X.restore()}});
 tinte(L,'255,170,80',.08*(1-z));tinte(L,'40,200,120',.07*z);arriba(L,.72)}

// ---------- 12 · CTA: vuelve el auto abandonado; una lucecita cian en el cielo ----------
function p12(L,t){const c=T.c12;
 plano(L,t,[[c,480,1200,1.18],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{bosque(L,cm,t,{yh:1330,luna:false});camino(L,1400,260,t);auto(L+420,1490,.84,{puerta:.9,luzInt:1});
  const pu=.6+.4*Math.sin(t*4);luz(L+700,1180,70,CIAN,.7*pu);X.fillStyle=`rgba(${CIAN},${pu})`;X.beginPath();X.arc(L+700,1180,7,0,7);X.fill()});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12].forEach((f,i)=>{NUEVOS['dc_sgtaen14_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SGTAEN14 · FIN =====
</script>
