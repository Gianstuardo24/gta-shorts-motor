<script>
// ===== DC · SGTAES19 · INICIO ===== (GTA ES 19h · Los jugadores CASTIGARON a GTA 6 · lote del 28-nov · una escena por línea del guion)
// Sin logos ni arte de terceros: los nombres van en texto llano, las notas en anillos propios y las personas como avatares anónimos. Solo aparecen cifras que dice el guion. Sin citas ni medios inventados.
(function(){
const {cam,cierreCanal,SET}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,tarj}=window.B28;
const BL='235,240,255',RJ='255,80,70',AM='255,200,90',CI='90,220,255',MG='255,90,200',VD='120,230,150';

function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#121a28',{sa:.3,borde:o.borde||'rgba(235,240,255,.6)',lw:3});txt(texto,x,y+4*s,(o.ts||46)*s,o.tc||'#fff',{w:800});X.restore()}
function fondo(L,c0,c1,tx){X.fillStyle=gl(0,0,0,1920,[[0,c0||'#0b0f18'],[1,c1||'#141c2c']]);X.fillRect(L-1400,-900,3900,3800);if(tx)tex(tx,L-1400,-300,3900,2600,{a:.14,s:1.6})}
function estudio(L,o){o=o||{};const yp=o.yp||1500;X.fillStyle=gl(0,0,0,yp,[[0,o.c0||'#0b0f18'],[1,o.c1||'#1a2233']]);X.fillRect(L-1400,-900,3900,yp+960);X.fillStyle=gl(0,yp,0,1920,[[0,'#10151f'],[1,'#070a10']]);X.fillRect(L-1400,yp,3900,1500);X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-1400,yp,3900,4)}
// anillo de nota: p (0…1) rellena el arco · n: cifra · sub: texto chico
function anillo(x,y,r,p,rgb,o){o=o||{};X.save();X.lineCap='round';X.strokeStyle='rgba(255,255,255,.12)';X.lineWidth=r*.16;X.beginPath();X.arc(x,y,r,0,7);X.stroke();if(p>0){X.strokeStyle=`rgb(${rgb})`;X.beginPath();X.arc(x,y,r,-Math.PI/2,-Math.PI/2+Math.PI*2*Math.min(1,p));X.stroke()}X.restore();
 if(o.n)txt(o.n,x,y+(o.sub?-r*.08:r*.04),r*(o.ts||.8),o.tc||'#fff',{w:900});if(o.sub)txt(o.sub,x,y+r*.5,r*.25,'rgba(255,255,255,.75)',{w:700})}
// tarjeta: sx giro 3D (−1…1) · rot · sk inclinación · s escala
function carta(x,y,w,h,o,fn){o=o||{};const sx=o.sx===undefined?1:o.sx,r=o.r||34;X.save();X.translate(x,y);X.rotate(o.rot||0);if(o.sk)X.transform(1,o.sk,0,1,0,0);X.scale(Math.max(.04,Math.abs(sx))*(o.s||1),(o.s||1));X.fillStyle='rgba(0,0,0,.4)';rr(-w/2+10,-h/2+18,w,h,r);X.fill();X.fillStyle=gl(0,-h/2,0,h/2,[[0,o.c0||'#1c2536'],[1,o.c1||'#111827']]);rr(-w/2,-h/2,w,h,r);X.fill();if(o.borde){X.strokeStyle=o.borde;X.lineWidth=o.lw||6;rr(-w/2,-h/2,w,h,r);X.stroke()}if(fn)fn();X.restore()}
function avatar(x,y,r,col,q){X.save();X.translate(x,y);X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(3,5,r,0,7);X.fill();X.fillStyle=col||'#26324c';X.beginPath();X.arc(0,0,r,0,7);X.fill();X.save();X.beginPath();X.arc(0,0,r,0,7);X.clip();X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.arc(0,-r*.22,r*.34,0,7);X.fill();X.beginPath();X.ellipse(0,r*.74,r*.62,r*.5,0,0,7);X.fill();X.restore();if(q>0){X.globalAlpha=q;X.fillStyle='rgba(8,12,20,.7)';X.beginPath();X.arc(0,0,r,0,7);X.fill();txt('?',0,r*.06,r*1.3,`rgb(${AM})`,{w:900})}X.restore()}
function pulgar(x,y,s,col,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle=col;rr(-44,-50,74,70,16);X.fill();rr(-78,-50,26,70,8);X.fill();X.save();X.translate(8,10);X.rotate(.12);rr(-17,0,34,66,17);X.fill();X.restore();X.fillStyle='rgba(0,0,0,.18)';for(let i=0;i<3;i++)X.fillRect(-40,-34+i*18,60,4);X.restore()}
function lupa(x,y,r){X.save();X.translate(x,y);X.strokeStyle='#cfd6dc';X.lineWidth=r*.3;X.lineCap='round';X.beginPath();X.moveTo(r*.78,r*.78);X.lineTo(r*1.7,r*1.7);X.stroke();X.fillStyle='rgba(160,220,255,.14)';X.beginPath();X.arc(0,0,r,0,7);X.fill();X.strokeStyle='#e9eef2';X.lineWidth=r*.14;X.beginPath();X.arc(0,0,r,0,7);X.stroke();X.strokeStyle='rgba(255,255,255,.5)';X.lineWidth=r*.07;X.beginPath();X.arc(0,0,r*.7,3.6,4.6);X.stroke();X.restore()}
// tarjetita de voto: anillo vacío, o un cero cuando lo dice el guion
function voto(x,y,s,rot,o){o=o||{};X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.globalAlpha*=(o.a===undefined?1:o.a);X.fillStyle='rgba(0,0,0,.3)';rr(-52,-62,112,138,16);X.fill();X.fillStyle=o.col||'#e9eef2';rr(-56,-70,112,138,16);X.fill();X.strokeStyle=o.cero?`rgb(${RJ})`:'rgba(30,40,60,.35)';X.lineWidth=10;X.beginPath();X.arc(0,-14,30,0,7);X.stroke();if(o.cero)txt('0',0,-12,46,'#d42a20',{w:900});X.fillStyle='rgba(30,40,60,.25)';rr(-36,34,72,10,5);X.fill();X.restore()}
function resena(x,y,s,rot,i){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';rr(-70,-86,150,190,14);X.fill();X.fillStyle='#e9eef2';rr(-75,-95,150,190,14);X.fill();X.strokeStyle='#2a3550';X.lineWidth=8;X.beginPath();X.arc(-36,-52,20,0,7);X.stroke();X.fillStyle='rgba(30,40,60,.3)';rr(-4,-62,60,10,5);X.fill();for(let k=0;k<4;k++){rr(-56,-10+k*24,112*(.6+rnd(i*5+k)*.4),10,5);X.fill()}X.restore()}
function urna(x,yb,s,t){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';X.beginPath();X.ellipse(0,0,230,24,0,0,7);X.fill();X.fillStyle=gl(-170,0,170,0,[[0,'#1c2a3a'],[.5,'#2f4860'],[1,'#16222e']]);rr(-170,-120,340,120,12);X.fill();X.fillStyle='rgba(120,220,255,.1)';rr(-200,-460,400,340,22);X.fill();
 X.save();rr(-200,-460,400,340,22);X.clip();for(let i=0;i<10;i++)voto(-140+rnd(i+2)*280,-176+rnd(i+8)*46-(i%3)*20,.52,(rnd(i)-.5)*1.3,{});X.restore();X.strokeStyle=`rgba(${CI},.8)`;X.lineWidth=6;rr(-200,-460,400,340,22);X.stroke();X.fillStyle='#07090c';rr(-90,-474,180,22,10);X.fill();X.restore()}
// pantalla con una partida genérica (dibujo propio): tq avanza a saltos (menos fluido) · fa: fallos visuales discretos
function juego(x,y,w,h,tq,t,fa){X.fillStyle=gl(0,y,0,y+h*.6,[[0,'#3a2a6a'],[.6,'#e8748a'],[1,'#f8c078']]);X.fillRect(x,y,w,h);X.fillStyle='#ffe9b8';X.beginPath();X.arc(x+w*.68,y+h*.44,54,0,7);X.fill();
 X.fillStyle='#2a2550';for(let i=0;i<12;i++){const bx=x+((i*150-tq*60)%1500+1500)%1500-200,bh=70+rnd(i+3)*150;X.fillRect(bx,y+h*.6-bh,90+rnd(i)*50,bh)}
 X.fillStyle='#20203a';X.fillRect(x,y+h*.6,w,h*.4);X.fillStyle='#34344e';X.beginPath();X.moveTo(x+w*.42,y+h*.6);X.lineTo(x+w*.58,y+h*.6);X.lineTo(x+w*1.05,y+h);X.lineTo(x-w*.05,y+h);X.closePath();X.fill();
 for(let i=0;i<5;i++){const q=((tq*1.3+i/5)%1),yy=y+h*.6+q*q*h*.4,ww=4+q*q*22;X.fillStyle='#e9d9a0';X.fillRect(x+w/2-ww/2,yy,ww,10+q*q*60)}
 for(let i=0;i<4;i++){const q=((tq*.5+i/4)%1),px=x+(i%2?w*.5+q*q*w*.6+40:w*.5-q*q*w*.6-40),py=y+h*.6+q*q*h*.36,s=.25+q*q*1.1;X.strokeStyle='#1a1630';X.lineWidth=10*s;X.beginPath();X.moveTo(px,py);X.lineTo(px+6*s,py-150*s);X.stroke();X.fillStyle='#1a1630';for(let k=0;k<5;k++){X.save();X.translate(px+6*s,py-150*s);X.rotate(-2.4+k*.6);X.beginPath();X.ellipse(44*s,0,48*s,12*s,0,0,7);X.fill();X.restore()}}
 const cx=x+w/2+Math.sin(tq*2)*26,cy=y+h*.9;X.fillStyle='rgba(0,0,0,.4)';X.beginPath();X.ellipse(cx,cy+6,120,14,0,0,7);X.fill();X.fillStyle='#c0392b';rr(cx-104,cy-90,208,84,16);X.fill();X.fillStyle='#8a2a22';X.beginPath();X.moveTo(cx-78,cy-90);X.lineTo(cx-56,cy-140);X.lineTo(cx+56,cy-140);X.lineTo(cx+78,cy-90);X.closePath();X.fill();X.fillStyle='#16203a';X.beginPath();X.moveTo(cx-62,cy-94);X.lineTo(cx-46,cy-130);X.lineTo(cx+46,cy-130);X.lineTo(cx+62,cy-94);X.closePath();X.fill();X.fillStyle='#ffd24a';rr(cx-98,cy-70,40,18,6);X.fill();rr(cx+58,cy-70,40,18,6);X.fill();X.fillStyle='#0a0c10';rr(cx-96,cy-14,36,22,6);X.fill();rr(cx+60,cy-14,36,22,6);X.fill();
 if(fa>0&&fa<1){for(let i=0;i<5;i++){if(rnd(Math.floor(t*14)+i*7)>.45){X.fillStyle=i%2?'rgba(255,60,200,.5)':'rgba(60,240,255,.5)';X.fillRect(x+rnd(Math.floor(t*14)+i)*w*.8,y+h*.2+rnd(Math.floor(t*14)+i*3)*h*.7,60+rnd(i)*160,8+rnd(i+2)*14)}}X.save();X.globalAlpha=.35;X.fillStyle='#c0392b';rr(cx-104+34,cy-90-8,208,84,16);X.fill();X.restore()}}

// ---------- 01 · gancho: 99 de 100 contra menos de 6; la cámara pasa entre las dos y asoma lo que esconde la segunda ----------
function p01(L,t){const xc=T.x_castig,xp=T.x_prensa,x9=T.x_99,xu=T.x_publico,xm=T.x_menos,xe=T.x_esconde,xn=T.x_nadie,f=T.c02,g=golpe(t,xc,.6),sp=eio(seg(t,xp-.35,xp+.1)),pu=eio(seg(t,xu-.25,xu+.1)),en=eio(seg(t,xe-.1,xe+.5)),lev=eio(seg(t,xn-.6,xn));
 plano(L,t,[[0,540,1040,1.2],[xp,540,1060,1],[xe,560,1070,1.02],[f,790,1120,1.6]],cm=>{estudio(L,{yp:1500});haz(L-100,420,L+300,1300,60,360,BL,.14*sp);haz(L+1180,420,L+780,1300,60,360,RJ,.16*pu);
  const gy=lerp(1060,720,sp),gs=lerp(1,.6,sp);if(en<1){X.save();X.globalAlpha=1-en;carta(L+540+(g>0?Math.sin(t*60)*8*g:0),gy,560,300,{s:gs,borde:'rgba(255,255,255,.3)'},()=>txt('GTA 6',0,6,150,'#fff',{w:900}));X.restore()}
  const st=seg(t,xc-.18,xc+.05);if(st>0&&sp<1){X.save();X.globalAlpha=1-sp;pulgar(L+790,gy+90,1.5*lerp(2.2,1,eio(st))*gs,`rgb(${RJ})`,-.2);X.restore();luz(L+790,gy+90,280,RJ,.4*g)}
  if(sp>0){X.save();X.globalAlpha=sp;carta(L+lerp(-200,285,sp),1160,430,560,{rot:-.03,sk:.05,borde:`rgba(${BL},.8)`},()=>{const a9=eio(seg(t,x9-.15,x9+.15));txt('PRENSA',0,-205,48,`rgb(${BL})`,{w:800});anillo(0,36,150,.99*a9,BL,a9>.5?{n:'99',sub:'de 100'}:{})});X.restore()}
  if(en>0){X.save();X.globalAlpha=en;carta(L+795,1170,400,520,{c0:'#0c1220',c1:'#080c16',borde:'rgba(255,255,255,.18)'},()=>{for(let i=0;i<6;i++)avatar(-104+(i%3)*104,-110+Math.floor(i/3)*130,42,'#26324c',0);X.globalAlpha=en*lev;txt('?',0,170,120,`rgb(${AM})`,{w:900})});X.restore()}
  if(pu>0){X.save();X.globalAlpha=pu;carta(L+lerp(1300,795,pu)+lev*440,1160-lev*40,430,560,{rot:.03+lev*.16,sk:-.05,borde:`rgba(${RJ},.85)`,c0:'#2a1616',c1:'#160c10'},()=>{const am=eio(seg(t,xm-.1,xm+.2));txt('PÚBLICO',0,-205,48,`rgb(${RJ})`,{w:800});anillo(0,36,150,.56*am,RJ,am>.5?{n:'<6'}:{})});X.restore()}});
 arriba(L,.6)}

// ---------- 02 · en Metacritic, más de 150 críticos lo dejaron en 99 de 100: un muro de reseñas que se agrupa ----------
function p02(L,t){const c=T.c02,xm=T.x_meta,x1=T.x_150,xd=T.x_dejaron,x9=T.x_99b,f=T.c03,jun=eio(seg(t,xd-.2,x9-.05)),a9=eio(seg(t,x9-.25,x9+.1));
 plano(L,t,[[c,490,1050,1.26],[xd,540,1080,1.02],[f,540,1090,1.16]],cm=>{fondo(L,'#0b0f18','#141c2c','tela');luz(L+540,1090,720,BL,.08+.14*a9);
  for(let i=0;i<34;i++){const en=eio(seg(t,c+i*.04,c+.35+i*.04)),x0=L+60+rnd(i+1)*960,y0=600+rnd(i+31)*1040,x=lerp(lerp(x0+(rnd(i+7)-.5)*2400,x0,en),L+540,jun),y=lerp(lerp(y0+(rnd(i+11)-.5)*900+500,y0,en),1090,jun);if(en<=0||jun>=1)continue;X.save();X.globalAlpha=en*(1-jun);resena(x,y,lerp(.85+rnd(i+3)*.5,.3,jun),(rnd(i+5)-.5)*.34*(1-jun),i);X.restore()}
  if(a9>0){X.save();X.globalAlpha=a9;carta(L+540,1090,600,680,{borde:`rgba(${BL},.8)`,s:.9+.1*a9},()=>{txt('CRÍTICOS',0,-250,54,`rgb(${BL})`,{w:800});anillo(0,40,190,.99*a9,BL,{n:'99',sub:'de 100'})});X.restore()}});
 arriba(L,.6);placa(L+540,545,1.05,'METACRITIC',eio(seg(t,xm-.1,xm+.2))*(1-a9),{w:380});placa(L+540,1570,1.1,'+150 CRÍTICOS',eio(seg(t,x1-.1,x1+.2)),{w:440})}

// ---------- 03 · pero ese sitio tiene otra nota, la de los usuarios: la tarjeta gira ----------
function p03(L,t){const c=T.c03,xo=T.x_otra,xu=T.x_usuarios,f=T.c04,gi=eio(seg(t,xo-.3,xo+.45)),sx=Math.cos(gi*Math.PI),cal=eio(seg(t,xo,xo+.5)),au=eio(seg(t,xu-.15,xu+.15));
 plano(L,t,[[c,540,1090,1.16],[xo,540,1090,1.24],[f,560,1095,1.32]],cm=>{fondo(L,'#0b0f18','#141c2c','tela');luz(L+540,1090,720,BL,.22*(1-cal));luz(L+540,1090,720,AM,.2*cal);haz(L+540,150,L+540,1300,60,430,cal>.5?AM:BL,.1);
  carta(L+540,1090,600,680,{sx,borde:sx>0?`rgba(${BL},.8)`:`rgba(${AM},.85)`,c0:sx>0?'#1c2536':'#2a1c16',c1:sx>0?'#111827':'#1a0f10'},()=>{if(sx>0){txt('CRÍTICOS',0,-250,54,`rgb(${BL})`,{w:800});anillo(0,40,190,.99,BL,{n:'99',sub:'de 100'})}else{if(au>0){X.save();X.globalAlpha=au;txt('USUARIOS',0,-250,54,`rgb(${AM})`,{w:800});X.restore()}anillo(0,40,190,0,AM,{n:'?',tc:`rgb(${AM})`})}})});
 tinte(L,'255,120,60',.06*cal);arriba(L,.6)}

// ---------- 04 · se abrió el 20 de noviembre, un día y medio después del lanzamiento ----------
function p04(L,t){const c=T.c04,x2=T.x_20,xn=T.x_nov,xd=T.x_dia,xl=T.x_lanz,f=T.c05,pg=eio(seg(t,x2-.3,x2)),an=eio(seg(t,xn-.15,xn+.15)),av=eio(seg(t,xd-.2,xl-.1)),g=golpe(t,x2,.6);
 plano(L,t,[[c,480,1010,1],[xd,540,1150,1.12],[f,540,1180,1.16]],cm=>{X.fillStyle='#2a1e16';X.fillRect(L-1400,-900,3900,3800);tex('madera',L-1400,-300,3900,2600,{a:.6,s:1.8,tinte:'60,40,26'});X.fillStyle='rgba(0,0,0,.35)';rr(L+52,578,1000,1180,40);X.fill();X.fillStyle='#16202e';rr(L+40,560,1000,1180,40);X.fill();tex('tela',L+40,560,1000,1180,{a:.25,s:1.4});luz(L+300,760,760,'255,236,200',.16);
  X.save();X.translate(L+300,960);X.rotate(-.04);X.fillStyle='rgba(0,0,0,.35)';rr(-178,-200,380,440,20);X.fill();X.fillStyle='#d9d4c6';rr(-190,-196,380,440,20);X.fill();X.fillStyle='#f4efe6';rr(-190,-220,380,440,20);X.fill();X.fillStyle='#c0392b';rr(-190,-220,380,104,20);X.fill();X.fillRect(-190,-150,380,34);X.fillStyle='#8e98a4';[-110,110].forEach(q=>{rr(q-10,-250,20,60,8);X.fill()});
  if(an>0){X.save();X.globalAlpha=an;txt('NOVIEMBRE',0,-166,44,'#fff',{w:800});X.restore()}if(pg>0){X.save();X.globalAlpha=pg;txt('20',0,60,230,'#1c2536',{w:900});X.restore()}else{X.fillStyle='rgba(30,40,60,.16)';for(let k=0;k<4;k++){rr(-130,-60+k*60,260*(.6+rnd(k+2)*.4),18,9);X.fill()}}X.restore();
  if(g>0)luz(L+790,960,360,AM,.4*g);carta(L+790,960,330,420,{rot:.05,borde:`rgba(${AM},.8)`,c0:'#2a1c16',c1:'#1a0f10'},()=>{txt('USUARIOS',0,-150,36,`rgb(${AM})`,{w:800});anillo(0,20,104,0,AM,{});candado(0,34,.8,`rgb(${AM})`,pg>.5)});
  // línea de tiempo: del lanzamiento (bandera) a un día y medio
  const x0=L+180,x1=L+900,yb=1420,xf=lerp(x0,x1,av);X.fillStyle='rgba(255,255,255,.14)';rr(x0,yb-9,x1-x0,18,9);X.fill();if(av>0){X.fillStyle=`rgb(${AM})`;rr(x0,yb-9,xf-x0,18,9);X.fill();luz(xf,yb,90,AM,.6);X.beginPath();X.arc(xf,yb,18,0,7);X.fill()}
  X.fillStyle='#fff';[0,1/1.5,1].forEach(q=>X.fillRect(lerp(x0,x1,q)-3,yb-30,6,60));X.fillStyle='#e9eef2';X.fillRect(x0-4,yb-150,8,150);X.fillStyle=`rgb(${MG})`;X.beginPath();X.moveTo(x0+4,yb-150);X.lineTo(x0+96,yb-122);X.lineTo(x0+4,yb-94);X.closePath();X.fill();
  if(av>.98){X.strokeStyle=`rgba(${AM},.7)`;X.lineWidth=5;X.setLineDash([12,10]);X.beginPath();X.moveTo(x1,yb-30);X.lineTo(L+830,1190);X.stroke();X.setLineDash([])}
  placa(L+560,1300,1,'1 DÍA Y MEDIO',eio(seg(t,xd-.1,xd+.2)),{ts:40,w:380,borde:`rgba(${AM},.7)`});placa(L+300,1540,1,'LANZAMIENTO',eio(seg(t,xl-.3,xl)),{ts:38,w:340})});
 arriba(L,.6)}

// ---------- 05 · y en pocas horas cayó hasta 4,9 de 10 ----------
function p05(L,t){const c=T.c05,xh=T.x_horas,xc=T.x_cayo,x4=T.x_49,f=T.c06,q=eio(seg(t,xh-.1,x4-.1)),a4=eio(seg(t,x4-.12,x4+.15)),g=golpe(t,x4,.6),P=[[200,640],[330,640],[330,830],[430,830],[430,960],[520,960],[520,1130],[600,1130],[600,1250],[700,1250],[700,1330]];
 let tot=0;const S=[];for(let i=1;i<P.length;i++){const d=Math.hypot(P[i][0]-P[i-1][0],P[i][1]-P[i-1][1]);S.push(d);tot+=d}
 plano(L,t,[[c,400,800,1.3],[xc,440,880,1.3],[x4,600,1270,1.3],[f,620,1300,1.4]],cm=>{fondo(L,'#10141c','#1c1014');tex('concreto',L-1400,-300,3900,2600,{a:.2,s:1.6});X.fillStyle='rgba(255,255,255,.035)';for(let i=0;i<11;i++)X.fillRect(L+120,580+i*78+rnd(i)*14,760,3);X.fillStyle='rgba(255,255,255,.22)';X.fillRect(L+120,560,5,840);
  luz(L+700,1330,520,RJ,.1+.22*a4);let rest=q*tot,hx=P[0][0],hy=P[0][1];X.lineCap='round';X.lineJoin='round';X.strokeStyle=gl(0,640,0,1330,[[0,'#e9eef2'],[1,'#ff5046']]);X.lineWidth=16;X.beginPath();X.moveTo(L+P[0][0],P[0][1]);
  for(let i=1;i<P.length&&rest>0;i++){const k=Math.min(1,rest/S[i-1]);hx=lerp(P[i-1][0],P[i][0],k);hy=lerp(P[i-1][1],P[i][1],k);X.lineTo(L+hx,hy);rest-=S[i-1]}X.stroke();luz(L+hx,hy,110,RJ,.6);X.fillStyle='#fff';X.beginPath();X.arc(L+hx,hy,16,0,7);X.fill();
  if(a4>0){X.save();X.globalAlpha=a4;const k=1+.12*g;txt('4,9',L+450,1520,200*k,'#ff5046',{w:900});txt('de 10',L+735,1560,70,'#fff',{w:800});X.restore()}});
 arriba(L,.9,600)}

// ---------- 06 · G2: lo que casi nadie revisa, quiénes pusieron esas notas ----------
function p06(L,t){const c=T.c06,xa=T.x_ahora,xr=T.x_revisa,xq=T.x_quienes,f=T.c07,g=golpe(t,xa,.6),A=[[215,830],[200,1010],[225,1190],[205,1370],[880,840],[895,1020],[870,1200],[890,1380],[340,1500],[550,1530],[750,1500]],u=eio(seg(t,xq+.1,f-.1)),lx=L+lerp(1000,300,u*u*(3-2*u)),ly=lerp(820,1500,u)+Math.sin(u*9)*60,ver=t>xq;
 plano(L,t,[[c,540,1060,1],[xq,540,1080,1.18],[f,560,1100,1.32]],cm=>{X.fillStyle='#070a10';X.fillRect(L-1400,-900,3900,3800);haz(L+540,-100,L+540,1500,50,440,BL,.2);X.fillStyle='rgba(255,255,255,.05)';X.beginPath();X.ellipse(L+540,1470,440,70,0,0,7);X.fill();
  carta(L+540,1080,430,540,{borde:`rgba(${RJ},.85)`,c0:'#2a1616',c1:'#160c10',s:1+.04*g},()=>{txt('USUARIOS',0,-200,44,`rgb(${RJ})`,{w:800});anillo(0,30,140,.49,RJ,{n:'4,9',sub:'de 10'})});
  A.forEach((p,i)=>{const en=seg(t,xq-.25+i*.05,xq+.05+i*.05);if(en<=0)return;const d=Math.hypot(L+p[0]-lx,p[1]-ly),ce=ver?Math.max(0,1-d/150):0,k=back(Math.min(1,en))*(1+.25*ce);X.save();X.translate(L+p[0],p[1]);X.scale(k,k);avatar(0,0,50,'#26324c',ce);X.restore()});
  if(ver){X.save();X.globalAlpha=eio(seg(t,xq,xq+.25));lupa(lx,ly,96);X.restore()}});
 arriba(L,.6)}

// ---------- 07 · cualquiera puede votar; no hace falta demostrar que tienes el juego ----------
function p07(L,t){const c=T.c07,xc=T.x_cualq,xv=T.x_votar,xh=T.x_nohace,xj=T.x_juego,f=T.c08,nh=eio(seg(t,xh-.2,xh+.2)),A=[[130,990],[90,1210],[220,1400],[340,1130],[300,870]];
 plano(L,t,[[c,420,1130,1.1],[xv,560,1130,1.2],[f,670,1110,1.38]],cm=>{interior(L,{p0:'#0c1622',p1:'#12283a',tex:'metal',ta:.1,yp:1500,piso:['#0e2030','#0a1826'],paso:170});luz(L+720,1000,620,CI,.16);urna(L+720,1500,1,t);
  A.forEach((p,i)=>{const en=eio(seg(t,c+.1+i*.1,c+.4+i*.1));X.save();X.globalAlpha=en;avatar(L+p[0],p[1],56,'#26324c',0);X.restore();if(t>xc-.3){const u=((t-(xc-.3))/1.3+i*.21)%1,x0=L+p[0]+50,y0=p[1],x1=L+720,y1=1030,mx=(x0+x1)/2,my=Math.min(y0,y1)-260,a=1-u,x=a*a*x0+2*a*u*mx+u*u*x1,y=a*a*y0+2*a*u*my+u*u*y1;voto(x,y,.5*(1-.3*u),u*2.4+i,{a:Math.min(1,u*6)*(u>.93?(1-u)/.07:1)})}});
  if(nh>0){X.save();X.globalAlpha=nh;X.translate(L+720,790);X.strokeStyle='rgba(255,255,255,.7)';X.lineWidth=6;X.setLineDash([16,13]);X.lineDashOffset=-t*30;X.beginPath();X.arc(0,0,92,0,7);X.stroke();X.setLineDash([]);X.fillStyle='rgba(255,255,255,.22)';rr(-40,-52,80,104,8);X.fill();X.fillStyle='rgba(255,255,255,.35)';X.fillRect(-40,-52,12,104);X.beginPath();X.arc(8,6,24,0,7);X.fill();X.restore()}
  placa(L+720,930,1,'NO HACE FALTA',nh,{ts:36,w:360,borde:`rgba(${CI},.7)`})});
 arriba(L,.62)}

// ---------- 08 · miles de esas notas fueron un cero ----------
function p08(L,t){const c=T.c08,xz=T.x_cero,f=T.c09,z=t>=xz-.15,g=golpe(t,xz-.15,.5);
 plano(L,t,[[c,540,1080,1],[f,540,1100,1.3]],cm=>{fondo(L,'#0b0f18','#1c1014');X.save();X.globalAlpha=.55;carta(L+540,1100,430,540,{borde:`rgba(${RJ},.85)`,c0:'#2a1616',c1:'#160c10'},()=>{txt('USUARIOS',0,-200,44,`rgb(${RJ})`,{w:800});anillo(0,30,140,.49,RJ,{n:'4,9',sub:'de 10'})});X.restore();luz(L+540,1100,720,RJ,.1+.16*g);
  for(let k=0;k<3;k++){const n=[10,8,5][k],s=[.6,1,1.7][k],vel=[330,480,700][k],al=[.5,.85,1][k];for(let i=0;i<n;i++){const y=700+((t-c)*vel+rnd(i+k*20)*1250)%1250,x=L+50+rnd(i*3+k*11)*980;voto(x,y,s*(z?1+.1*g:1),(rnd(i+k)-.5)*.7+Math.sin(t*2+i)*.1,{a:al*seg(y,700,860),cero:z})}}});
 arriba(L,.6)}

// ---------- 09 · hubo respuesta: fans de GTA fueron a bajarle la nota a Zelda Ocarina of Time, el juego que comparte el 99 ----------
function p09(L,t){const c=T.c09,xf=T.x_fans,xb=T.x_bajarle,xz=T.x_zelda,xc=T.x_comparte,x9=T.x_99c,f=T.c10,ad=eio(seg(t,xb-.3,xb)),az=eio(seg(t,xz-.2,xz+.15)),dr=eio(seg(t,xz,xc)),a9=eio(seg(t,x9-.3,x9+.05)),ola=t>xb-.2&&t<xc+.3;
 plano(L,t,[[c,330,1100,1.3],[xb,400,1100,1.26],[xz,740,1100,1.3],[xc,540,1090,1.02],[f,540,1090,1.06]],cm=>{estudio(L,{yp:1500,c1:'#161c2c'});haz(L+290,150,L+290,1500,50,340,MG,.12);haz(L+790,150,L+790,1500,50,340,VD,.12*az);
  [290,790].forEach(q=>{X.fillStyle='#1a2233';rr(L+q-150,1400,300,110,12);X.fill();X.fillStyle='rgba(255,255,255,.08)';X.fillRect(L+q-150,1400,300,5)});
  carta(L+290,1110,400,520,{borde:`rgba(${MG},.8)`},()=>{txt('GTA 6',0,-160,84,'#fff',{w:900});anillo(0,-10,80,.49,RJ,{n:'4,9'});if(a9>0){X.save();X.globalAlpha=a9;anillo(0,170,54,.99,BL,{n:'99'});X.restore()}});
  if(ad>0){X.save();X.globalAlpha=ad;carta(L+790,1110,400,520,{borde:az>0?`rgba(${VD},.8)`:'rgba(255,255,255,.2)'},()=>{if(az>0){X.save();X.globalAlpha=ad*az;txt('ZELDA:',0,-190,60,'#fff',{w:900});txt('OCARINA OF TIME',0,-128,37,'#fff',{w:800});X.restore()}anillo(0,-10,80,lerp(.92,.55,dr),VD,{});if(dr>0&&dr<1){X.fillStyle=`rgb(${RJ})`;X.beginPath();X.moveTo(-22,-28);X.lineTo(22,-28);X.lineTo(0,14);X.closePath();X.fill()}if(a9>0){X.save();X.globalAlpha=a9;anillo(0,170,54,.99,BL,{n:'99'});X.restore()}});X.restore()}
  for(let i=0;i<6;i++){const en=seg(t,xf-.2+i*.06,xf+.1+i*.06);if(en>0){X.save();X.translate(L+110+i*72,1560+(i%2)*46);X.scale(back(Math.min(1,en)),back(Math.min(1,en)));avatar(0,0,34,'#3a2648',0);X.restore()}}
  if(ola)for(let i=0;i<9;i++){const u=((t-(xb-.2))/1.1+i/9)%1,a=1-u,x=L+a*a*290+2*a*u*540+u*u*790,y=a*a*850+2*a*u*600+u*u*850;X.save();X.globalAlpha=Math.min(1,u*6,(1-u)*6);X.translate(x,y);X.rotate(u*1.2-.6);X.fillStyle=`rgb(${RJ})`;X.beginPath();X.arc(0,0,26,0,7);X.fill();X.fillStyle='#fff';X.beginPath();X.moveTo(-12,-8);X.lineTo(12,-8);X.lineTo(0,12);X.closePath();X.fill();X.restore()}
  if(a9>0){X.strokeStyle=`rgba(${BL},${.8*a9})`;X.lineWidth=6;X.setLineDash([14,12]);X.beginPath();X.moveTo(L+350,1280);X.lineTo(L+730,1280);X.stroke();X.setLineDash([])}});
 arriba(L,.6)}

// ---------- 10 · también hay quejas reales: corre a 30 cuadros por segundo y algunos errores ----------
function p10(L,t){const c=T.c10,xq=T.x_quejas,x3=T.x_30,xe=T.x_errores,f=T.c11,tq=Math.floor(t*7)/7,fa=seg(t,xe-.3,xe+.6),a3=eio(seg(t,x3-.1,x3+.15)),sx=L+140,sy=740,sw=800,sh=540;
 plano(L,t,[[c,500,1090,1.1],[x3,540,1070,1.16],[f,560,1090,1.22]],cm=>{interior(L,{p0:'#1a2030',p1:'#232c40',tex:'tela',ta:.12,yp:1520,piso:['#2a2018','#1e1610'],pisoTex:'madera',pa:.5});
  luz(sx+sw/2,sy+sh/2,820,'255,140,150',.14);X.fillStyle='#14100c';rr(L+100,1410,880,130,10);X.fill();X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L+100,1410,880,5);X.fillStyle='#0a0c10';X.fillRect(sx+sw/2-70,sy+sh+20,140,80);rr(sx+sw/2-170,sy+sh+90,340,22,8);X.fill();
  X.fillStyle='#07090c';rr(sx-22,sy-22,sw+44,sh+44,18);X.fill();X.save();X.beginPath();X.rect(sx,sy,sw,sh);X.clip();juego(sx,sy,sw,sh,tq,t,fa);
  if(a3>0){X.globalAlpha=a3;X.fillStyle='rgba(0,0,0,.6)';rr(sx+18,sy+18,210,70,10);X.fill();txt('30 FPS',sx+123,sy+56,44,'#ffe14a',{w:900})}X.restore();
  X.fillStyle='rgba(255,255,255,.05)';X.beginPath();X.moveTo(sx,sy);X.lineTo(sx+260,sy);X.lineTo(sx,sy+300);X.closePath();X.fill();
  placa(L+540,1640,1.1,'QUEJAS REALES',eio(seg(t,xq-.1,xq+.2)),{ts:42,w:420,borde:`rgba(${CI},.8)`})});
 arriba(L,.6)}

// ---------- 11 · esa nota mezcla quejas reales con una guerra entre fans: dos capas alrededor del 4,9 ----------
function p11(L,t){const c=T.c11,xm=T.x_mezcla,xr=T.x_reales,xg=T.x_guerra,f=T.c12,en=eio(seg(t,c,xm)),ar=eio(seg(t,xr-.3,xr+.1)),ag=eio(seg(t,xg-.3,xg+.1)),F=[];
 for(let i=0;i<7;i++){const a=t*.8+i*Math.PI*2/7;F.push({x:540+Math.cos(a)*340,y:1060+Math.sin(a)*120,z:Math.sin(a),k:0})}for(let i=0;i<8;i++){const a=-t*.6+i*Math.PI*2/8;F.push({x:540+Math.cos(a)*440,y:1130+Math.sin(a)*200,z:Math.sin(a),k:1})}
 const ficha=p=>{const s=(.8+.3*p.z)*en,col=p.k?(ag>0?`rgba(${RJ},${.5+.5*ag})`:'#3a4458'):(ar>0?`rgba(${CI},${.5+.5*ar})`:'#3a4458');X.save();X.translate(L+p.x,p.y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(3,5,46,0,7);X.fill();X.fillStyle=col;X.beginPath();X.arc(0,0,46,0,7);X.fill();if(p.k)pulgar(4,2,.5,'#fff',0);else{X.fillStyle='#0b1320';rr(-6,-26,12,32,6);X.fill();X.beginPath();X.arc(0,20,7,0,7);X.fill()}X.restore()};
 plano(L,t,[[c,520,1080,1.06,-.03],[f,560,1090,1.18,.03]],cm=>{fondo(L,'#0b0f18','#181420');luz(L+540,1090,700,RJ,.1);luz(L+540,1090,500,CI,.08*ar);F.filter(p=>p.z<0).forEach(ficha);
  carta(L+540,1090,380,470,{borde:`rgba(${RJ},.85)`,c0:'#2a1616',c1:'#160c10'},()=>anillo(0,10,140,.49,RJ,{n:'4,9',sub:'de 10'}));F.filter(p=>p.z>=0).forEach(ficha)});
 arriba(L,.6);placa(L+290,1600,1.15,'QUEJAS REALES',ar,{ts:38,w:400,borde:`rgba(${CI},.8)`});placa(L+740,1710,1.15,'GUERRA ENTRE FANS',ag,{ts:38,w:500,borde:`rgba(${RJ},.8)`})}

// ---------- 12 · CTA: una tarjeta sobre la mesa con el espacio vacío para tu nota ----------
function p12(L,t){const c=T.c12,bl=((t-c)*2%1)<.55;
 plano(L,t,[[c,470,1190,1.14],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{X.fillStyle=gl(0,0,0,1200,[[0,'#10141c'],[1,'#1c2433']]);X.fillRect(L-1400,-900,3900,2200);meson(L,1200,{tex:'madera',col:'#4a3424',ta:.7});luz(L+430,1320,540,'255,244,220',.14);
  carta(L+430,1320,320,390,{rot:-.05,borde:'rgba(255,255,255,.6)'},()=>{anillo(0,-30,100,0,BL,{});if(bl){X.fillStyle='#fff';rr(-30,-8,60,10,5);X.fill()}txt('de 10',0,128,36,'rgba(255,255,255,.8)',{w:800})})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12].forEach((f,i)=>{NUEVOS['dc_sgtaes19_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SGTAES19 · FIN =====
</script>
