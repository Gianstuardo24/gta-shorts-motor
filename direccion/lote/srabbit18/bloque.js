<script>
// ===== DC · SRABBIT18 · INICIO ===== (Rabbit 18h · Scientists CHASED This Signal for 17 YEARS · lote del 28-nov · una escena por línea del guion)
// Sin retrato: la investigadora se ve de espaldas. Sin duraciones, frecuencias ni horas en números: el guion no las da. Sin mapa inventado de los otros telescopios.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,noche,relojPared,tarj,desenfoca,borroso}=window.B28;
const VERDE='120,255,170',CAL='255,190,120';
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({manga:'#3a6a7a',puno:'#2f5866'},o))};

// ---------- radiotelescopio: torre + plato inclinado. inc: inclinación del plato (rad) ----------
function antena(x,yb,s,inc,o){o=o||{};const n=o.noche?1:0,c1=n?'#59626e':'#e6e2d6',c2=n?'#3d4550':'#bfb9a8',me=n?'#8e98a4':'#f4f6f8';X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';X.lineCap='round';
 X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(0,4,190,20,0,0,7);X.fill();X.fillStyle=gl(-110,0,110,0,[[0,c2],[.45,c1],[1,c2]]);rr(-110,-300,220,300,10);X.fill();X.fillStyle=n?'rgba(255,214,140,.8)':'rgba(40,60,80,.55)';for(let i=0;i<3;i++)for(let j=0;j<3;j++){rr(-74+j*56,-268+i*86,36,48,5);X.fill()}
 X.fillStyle=c2;rr(-130,-322,260,26,8);X.fill();X.fillStyle=n?'#4a535e':'#8e98a4';X.beginPath();X.moveTo(-60,-322);X.lineTo(-34,-400);X.lineTo(34,-400);X.lineTo(60,-322);X.closePath();X.fill();
 X.translate(0,-410);X.rotate(inc||0);X.strokeStyle=n?'#6b7682':'#9aa3ad';X.lineWidth=7;[[-250,-8],[250,-8],[0,-30]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(0,-300);X.stroke()});X.fillStyle=n?'#3d4550':'#5a6470';rr(-26,-330,52,46,8);X.fill();
 X.fillStyle=gl(-330,0,330,0,[[0,n?'#5a6470':'#c6ccd4'],[.5,me],[1,n?'#4a535e':'#aab3bd']]);X.beginPath();X.moveTo(-330,-20);X.quadraticCurveTo(0,200,330,-20);X.quadraticCurveTo(0,60,-330,-20);X.closePath();X.fill();
 X.fillStyle=n?'#7d8792':'#e9eef2';X.beginPath();X.ellipse(0,-20,330,50,0,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.14)';X.lineWidth=3;[-220,-110,0,110,220].forEach(q=>{X.beginPath();X.moveTo(q,-20-Math.sqrt(Math.max(0,1-q*q/108900))*50);X.lineTo(q*.62,90-Math.abs(q)*.22);X.stroke()});X.beginPath();X.ellipse(0,-20,200,30,0,0,7);X.stroke();X.restore()}
const foco=(x,yb,s,inc)=>[x+Math.sin(inc)*300*s,yb-(410+Math.cos(inc)*300)*s];
function antenaChica(x,yb,s,inc,o){antena(x,yb,s,inc,o)}
// ---------- pantalla con la traza. picos: [[posición 0..1, altura 0..1]] ----------
function traza(x,y,w,h,t,o){o=o||{};X.fillStyle='#07120e';rr(x,y,w,h,18);X.fill();X.strokeStyle='rgba(120,255,170,.12)';X.lineWidth=2;for(let i=1;i<8;i++){X.beginPath();X.moveTo(x+i*w/8,y+8);X.lineTo(x+i*w/8,y+h-8);X.stroke()}for(let i=1;i<4;i++){X.beginPath();X.moveTo(x+8,y+i*h/4);X.lineTo(x+w-8,y+i*h/4);X.stroke()}
 X.save();X.beginPath();X.rect(x+6,y+6,w-12,h-12);X.clip();const rgb=o.rgb||VERDE,yb=y+h*.72;[[14,.18],[5,1]].forEach(([lw,a])=>{X.strokeStyle=`rgba(${rgb},${a})`;X.lineWidth=lw;X.lineJoin='round';X.beginPath();for(let i=0;i<=120;i++){const q=i/120;let v=(o.ruido===0?0:(Math.sin(q*70+t*9)*.5+Math.sin(q*31-t*5)*.5)*.035);(o.picos||[]).forEach(p=>{const d=(q-p[0])/.012;v+=p[1]*Math.exp(-d*d)});const xx=x+q*w,yy=yb-v*h*.62;i?X.lineTo(xx,yy):X.moveTo(xx,yy)}X.stroke()});X.restore();
 X.strokeStyle=o.marco||'#2a3a44';X.lineWidth=8;rr(x,y,w,h,18);X.stroke()}
function galaxia(x,y,r,t,br){luz(x,y,r*1.6,'170,150,255',.25+.5*br);X.save();X.translate(x,y);X.rotate(t*.1);X.scale(1,.55);X.lineCap='round';for(let k=0;k<2;k++){X.strokeStyle=`rgba(210,200,255,${.75})`;X.lineWidth=r*.11;X.beginPath();for(let i=0;i<=30;i++){const a=i/30*4.4+k*Math.PI,rr2=r*(.12+.88*i/30);i?X.lineTo(Math.cos(a)*rr2,Math.sin(a)*rr2):X.moveTo(Math.cos(a)*rr2,Math.sin(a)*rr2)}X.stroke()}X.fillStyle='#fff';X.beginPath();X.arc(0,0,r*.18,0,7);X.fill();X.restore()}
// ---------- paisaje australiano: cielo, polvo rojizo, arbustos. hora: 'dia' | 'tarde' | 'noche' ----------
function campo(L,cm,t,o){o=o||{};const yh=o.yh||1500,h=o.hora||'dia',x0=L-1400,w=o.w||5200;
 if(h==='noche'){noche(L,t,{c0:'#05070f',c1:'#182040',y1:yh,n:70,ys:420,yh:yh-460,sem:o.sem||0});X.fillStyle=gl(0,-900,0,yh,[[0,'#05070f'],[1,'#182040']]);X.fillRect(x0+3900,-1400,w-3900,yh+1400)}
 else{X.fillStyle=gl(0,-300,0,yh,h==='tarde'?[[0,'#2a2a5a'],[.6,'#c8645a'],[1,'#f2b27a']]:[[0,'#3f86c8'],[1,'#cfe6f2']]);X.fillRect(x0,-1400,w,yh+1460)}
 const px=par(cm,.6);X.fillStyle=h==='noche'?'#1a1420':h==='tarde'?'#5a2a2a':'#b8744a';for(let i=0;i<16;i++){X.beginPath();X.ellipse(x0+200+i*340+px,yh+10,300,60+rnd(i+3)*70,0,Math.PI,0);X.fill()}
 X.fillStyle=gl(0,yh,0,1920,h==='noche'?[[0,'#2a1a1c'],[1,'#120a0c']]:h==='tarde'?[[0,'#8a3a26'],[1,'#4a1c14']]:[[0,'#c8643a'],[1,'#8a3a20']]);X.fillRect(x0,yh,w,1400);tex('arena',x0,yh,w,700,{a:h==='noche'?.12:.28,s:1.6});
 for(let i=0;i<22;i++){const x=x0+rnd(i+7)*w,y=yh+40+rnd(i+19)*380,r=24+rnd(i+31)*30;X.fillStyle=h==='noche'?'#0f1612':'#5a6a3a';X.beginPath();X.arc(x,y,r,Math.PI,0);X.arc(x+r*.8,y,r*.7,Math.PI,0);X.fill()}}
function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,(o.ts||50)*s,o.tc||'#2a2f38',{w:800});X.restore()}
// ---------- horno de microondas con ventana redonda. abre: 0..1 puerta abierta · on: luz y plato girando · av: avance 0..1 ----------
function microondas(x,yb,s,t,o){o=o||{};const ab=o.abre||0,on=o.on&&ab<.2;X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.ellipse(0,6,330,20,0,0,7);X.fill();
 X.fillStyle=gl(0,-360,0,0,[[0,'#d9dde2'],[1,'#a9b0b8']]);rr(-320,-360,640,360,22);X.fill();X.fillStyle='#22262b';rr(-296,-336,440,312,14);X.fill();
 X.fillStyle=on?'#4a3a22':'#14161a';X.beginPath();X.arc(-76,-180,138,0,7);X.fill();if(on)luz(-76,-180,150,'255,214,140',.5);
 X.fillStyle='#9aa3ad';X.beginPath();X.ellipse(-76,-92,96,16,0,0,7);X.fill();if(o.plato!==false){const g=on?Math.sin(t*2.4)*26:0;X.fillStyle='#f4f1ea';X.beginPath();X.ellipse(-76+g,-112,62,16,0,0,7);X.fill();X.fillStyle='#e07a3a';X.beginPath();X.ellipse(-76+g,-124,44,16,0,Math.PI,0);X.fill();X.fillStyle='#f4f1ea';X.beginPath();X.moveTo(-76+g-56,-124);X.lineTo(-76+g+56,-124);X.lineTo(-76+g+40,-98);X.lineTo(-76+g-40,-98);X.closePath();X.fill()}
 if(ab<.98){X.save();X.translate(-296,0);X.scale(1-ab*.86,1);X.fillStyle=`rgba(30,34,40,${.94})`;rr(0,-336,440,312,14);X.fill();X.fillStyle=on?'rgba(255,214,140,.32)':'rgba(120,150,170,.18)';X.beginPath();X.arc(220,-180,138,0,7);X.fill();X.strokeStyle='#8e98a4';X.lineWidth=12;X.beginPath();X.arc(220,-180,138,0,7);X.stroke();X.fillStyle='rgba(0,0,0,.35)';for(let i=-4;i<=4;i++)for(let j=-4;j<=4;j++){if(i*i+j*j<=18){X.beginPath();X.arc(220+i*30,-180+j*30,4,0,7);X.fill()}}X.fillStyle='#8e98a4';rr(400,-260,16,160,8);X.fill();X.restore()}
 X.fillStyle='#2a2f38';rr(160,-336,136,312,12);X.fill();X.fillStyle='#0c1410';rr(176,-318,104,56,8);X.fill();X.fillStyle=`rgb(${VERDE})`;rr(184,-298,88*(1-(o.av||0)),16,6);X.fill();
 for(let i=0;i<6;i++){X.fillStyle='#4a525c';rr(180+(i%2)*52,-240+Math.floor(i/2)*52,44,40,8);X.fill()}X.fillStyle='#c0392b';rr(180,-76,96,36,10);X.fill();X.restore()}
function cocina(L,cm,t,o){o=o||{};interior(L,{p0:o.p0||'#5a6a5a',p1:o.p1||'#8a9a82',tex:'baldosa',ta:.14,yp:1440});const px=par(cm,.4);X.fillStyle='#4a3a2c';rr(L-200+px,560,700,260,10);X.fill();X.fillStyle='#5a4838';[0,1,2].forEach(i=>{rr(L-184+i*228+px,576,212,228,6);X.fill()});
 luz(L+200+px,900,800,CAL,.2);meson(L,1400,{tex:'marmol',col:'#d9d5cc',ta:.9})}
function receptor(x,yb,w,t,picos,o){X.fillStyle='#2a2f38';rr(x-w/2-16,yb-w*.62-16,w+32,w*.62+32,16);X.fill();X.fillRect(x-30,yb,60,20);rr(x-90,yb+16,180,16,6);X.fill();traza(x-w/2,yb-w*.62,w,w*.62,t,Object.assign({picos},o||{}))}

// ---------- 01 · gancho: el radiotelescopio recibe un pulso de noche; la pantalla lo registra ----------
function p01(L,t){const x17=T.x_17,xb=T.x_bursts,xc=T.x_careful,xr=T.x_closer,f=T.c02,D=1500,inc=-.35,fc=foco(L+500,1560,1.35,inc),p1=golpe(t,.9,.9),p2=golpe(t,xb,.9),pu=Math.max(p1,p2);
 plano(L,t,[[0,520,1380,1.16],[x17,520,1150,1.1],[xb+.5,560,920,1.06],[xc-.35,560,900,1.06],[xc+.05,D+540,1100,1.1],[f,D+540,1090,1.2]],cm=>{campo(L,cm,t,{hora:'noche'});
  if(pu>0){haz(fc[0]+260,fc[1]-900,fc[0],fc[1],10,120,'190,170,255',.5*pu);luz(fc[0],fc[1],200,'190,170,255',.7*pu)}
  antena(L+500,1560,1.35,inc,{noche:1});
  X.fillStyle='#10161e';X.fillRect(L+D-200,-900,1700,3800);tex('metal',L+D-200,300,1700,1700,{a:.08,v:1});X.fillStyle='#1c2530';X.fillRect(L+D-200,1450,1700,900);
  receptor(L+D+540,1380,620,t,[[.5+.0*t,.95*Math.max(.25,golpe(t,xc+.1,1.2))]],{});const br=eio(seg(t,xr-.2,xr+.4));if(br>0){haz(L+D+1250,1000,L+D+700,1100,200,420,CAL,.24*br)}});
 placa(L+270,620,1,'17 YEARS',eio(seg(t,x17-.05,x17+.3))*(1-eio(seg(t,xb-.4,xb))),{ts:56});arriba(L,.6)}

// ---------- 02 · 1998: el radiotelescopio de Parkes, Australia, empieza a captar señales extrañas ----------
function p02(L,t){const c=T.c02,xp=T.x_parkes,xs=T.x_strange,f=T.c03,inc=lerp(.45,-.3,eio(seg(t,c+.3,xs))),fc=foco(L+540,1600,1.4,inc);
 plano(L,t,[[c,560,1420,1.26],[xp,540,1180,1.08],[f,540,1060,1.12]],cm=>{campo(L,cm,t,{hora:'dia',yh:1540});luz(L+900,600,700,'255,244,210',.2);
  antena(L+540,1600,1.4,inc,{});
  if(t>xs-.2)for(let j=0;j<3;j++){const u=((t-xs)*.7+j/3)%1,x0=fc[0]+300-60*j,y0=fc[1]-700;X.strokeStyle=`rgba(200,120,255,${.85*(1-u*.4)})`;X.lineWidth=7;X.lineCap='round';X.beginPath();for(let i=0;i<=14;i++){const q=Math.max(0,u-.25)+i/14*.25,xx=lerp(x0,fc[0],q),yy=lerp(y0,fc[1],q)+Math.sin(i*1.6+t*8)*16;i?X.lineTo(xx,yy):X.moveTo(xx,yy)}X.stroke()}});
 placa(L+240,560,1,'1998',eio(seg(t,c+.05,c+.4))*(1-eio(seg(t,xp-.5,xp-.2))),{ts:60});placa(L+330,560,1,'PARKES, AUSTRALIA',eio(seg(t,xp-.15,xp+.2)),{ts:42,w:540});arriba(L,.55)}

// ---------- 03 · cada una duraba apenas unas milésimas de segundo ----------
function p03(L,t){const c=T.c03,f=T.c04,a=golpe(t,c+.75,.32),b=golpe(t,c+1.85,.32);
 plano(L,t,[[c,540,1080,1.04],[f,560,1060,1.2]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#0a1014'],[1,'#141e24']]);X.fillRect(L-900,-900,2900,3800);tex('metal',L-300,300,1700,1700,{a:.1,v:1});
  X.fillStyle='#2a3038';rr(L+40,640,1000,860,40);X.fill();X.fillStyle='rgba(255,255,255,.06)';rr(L+40,640,1000,14,7);X.fill();
  traza(L+90,700,900,620,t,{picos:[[.34,a],[.68,b]]});luz(L+90+900*(a>b?.34:.68),1000,260,VERDE,.4*Math.max(a,b));
  [[160,'#e4572e'],[260,'#f2c94c'],[360,'#6fcf97']].forEach(([x,cq])=>{X.fillStyle='#14181c';X.beginPath();X.arc(L+x,1410,34,0,7);X.fill();X.fillStyle=cq;X.beginPath();X.arc(L+x,1410,14,0,7);X.fill()});X.fillStyle='#14181c';rr(L+620,1380,340,60,14);X.fill()});
 arriba(L,.6)}

// ---------- 04 · se parecían mucho a las ráfagas rápidas de radio, destellos reales de fuera de la galaxia ----------
function forma(x,y,w,h,rgb,a,lw){if(a<=0)return;X.save();X.strokeStyle=`rgba(${rgb},${a})`;X.lineWidth=lw||9;X.lineJoin='round';X.lineCap='round';X.beginPath();for(let i=0;i<=60;i++){const q=i/60,d=(q-.5)/.05,v=Math.exp(-d*d);i?X.lineTo(x+q*w,y-v*h):X.moveTo(x+q*w,y-v*h)}X.stroke();X.restore()}
function p04(L,t){const c=T.c04,xf=T.x_frb,xr=T.x_real,xo=T.x_outside,f=T.c05,br=golpe(t,xr,1.1),j=eio(seg(t,xo-.2,xo+.7));
 plano(L,t,[[c,540,1330,1.2],[xf+.2,540,1300,1.16],[xr,540,860,1.14],[xo,540,1060,.98],[f,540,1070,1.02]],cm=>{noche(L,t,{c0:'#05060f',c1:'#161a3a',y1:1920,n:80,ys:420,yh:1000,sem:6});
  galaxia(L+680,760,170,t,br);forma(L+150,880,360,220,'200,180,255',eio(seg(t,xr-.1,xr+.5)));
  placa(L+360,560,1,'FAST RADIO BURST',eio(seg(t,xf-.05,xf+.3))*(1-eio(seg(t,xo-.4,xo))),{ts:40,w:540,col:'#1a1a3a',tc:'#fff'});
  X.fillStyle='#10161e';X.fillRect(L-900,1180,2900,1400);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L-900,1180,2900,8);receptor(L+540,1700,640,t,[[.5,.9]],{});
  if(j>0){forma(lerp(L+150,L+220,j)+0,lerp(880,1600,j),lerp(360,640,j),lerp(220,246,j),'200,180,255',.9*j,7)}});
 arriba(L,.6)}

// ---------- 05 · un problema: ningún otro telescopio del mundo las veía ----------
function p05(L,t){const c=T.c05,xn=T.x_noother,f=T.c06,XS=[430,1230,1880,2640],ES=[1.05,.82,.7,.9];
 plano(L,t,[[c,460,1150,1.14],[xn,560,1150,1.12],[f,2300,1150,1.12]],cm=>{campo(L,cm,t,{hora:'tarde',w:7000});luz(L+2000,1200,1200,'255,170,110',.2);
  XS.forEach((x,i)=>{antena(L+x,1560,ES[i],i?(-.3+.25*i):-.35,{noche:0});const w=i?200:260;receptor(L+x+(i?180:240),1560,w,t,i?[]:[[.5,.9*(.4+.6*Math.abs(Math.sin(t*1.4)))]],i?{rgb:'150,160,170',ruido:0}:{})})});
 arriba(L,.6)}

// ---------- 06 · G2: la respuesta estaba más cerca de lo que nadie imaginó; una pista era la hora del día ----------
function sala(L,cm,t,o){o=o||{};interior(L,{p0:'#16242c',p1:'#2a4250',tex:'concreto',ta:.16,yp:1500,piso:['#3a444c','#2f383f'],paso:170});const px=par(cm,.4);
 X.fillStyle='#3a2c20';rr(L+820+px,640,300,870,6);X.fill();X.fillStyle=`rgba(${CAL},${.9*(o.cal===undefined?1:o.cal)})`;X.beginPath();X.moveTo(L+850+px,670);X.lineTo(L+990+px,690);X.lineTo(L+990+px,1490);X.lineTo(L+850+px,1500);X.closePath();X.fill();haz(L+900+px,1100,L+300+px,1560,260,620,CAL,.2*(o.cal===undefined?1:o.cal))}
function p06(L,t){const c=T.c06,xk=T.x_closer6,xl=T.x_clue,xt=T.x_time,f=T.c07,g=golpe(t,xl+.2,.6),fo=eio(seg(t,xt+.1,xt+.7)),cal=eio(seg(t,xk-.4,xk+.4));
 const kf=[[c,560,1100,1],[xl-.5,520,1060,1.08],[xl+.25,430,900,1.5],[xt+.1,430,900,1.5],[f,455,1000,1.24]];
 plano(L,t,kf,cm=>{sala(L,cm,t,{cal});borroso(5*(1-fo),()=>receptor(L+420,1420,420,t,[[.5,.9]],{}))});
 desenfoca(5*fo);
 plano(L,t,kf,cm=>{const m=11.6+.5*seg(t,c,f);luz(L+420,860,300+60*g,CAL,.2+.3*g);relojPared(L+420,860,150,Math.floor(m),(m%1)*60,{aro:'#22262b'})});
 arriba(L,.6)}

// ---------- 07 · las señales seguían apareciendo cerca de la hora de almuerzo ----------
function p07(L,t){const c=T.c07,xl=T.x_lunch,f=T.c08,u=seg(t,c,f);
 plano(L,t,[[c,470,1010,1.2],[f,560,1150,1.06]],cm=>{sala(L,cm,t,{});const m=11.2+1.4*u;relojPared(L+330,820,130,Math.floor(m),(m%1)*60,{aro:'#22262b'});
  X.fillStyle='rgba(8,14,18,.75)';rr(L+60,1160,880,320,26);X.fill();X.fillStyle=`rgba(${CAL},.22)`;rr(L+400,1180,200,280,14);X.fill();
  X.strokeStyle='rgba(255,255,255,.35)';X.lineWidth=5;X.beginPath();X.moveTo(L+100,1400);X.lineTo(L+900,1400);X.stroke();
  X.fillStyle='#ffd166';X.beginPath();X.arc(L+140,1250,22,0,7);X.fill();X.fillStyle='#8fa6d0';X.beginPath();X.arc(L+860,1250,20,0,7);X.fill();X.fillStyle='rgba(8,14,18,1)';X.beginPath();X.arc(L+870,1244,17,0,7);X.fill();
  [[.46,0],[.52,.3],[.49,.6],[.55,.9],[.44,1.2],[.5,1.5]].forEach(([q,d])=>{const a=eio(seg(t,c+.2+d*.9,c+.45+d*.9));if(a>0){X.strokeStyle=`rgba(${VERDE},${a})`;X.lineWidth=8;X.lineCap='round';X.beginPath();X.moveTo(L+100+q*800,1400);X.lineTo(L+100+q*800,1400-150*a);X.stroke()}});
  const q=eio(seg(t,xl-.2,xl+.2));if(q>0){X.save();X.globalAlpha=q;X.translate(L+500,1220);X.strokeStyle='#fff';X.lineWidth=7;X.lineCap='round';X.beginPath();X.moveTo(-18,-30);X.lineTo(-18,30);X.moveTo(-28,-30);X.lineTo(-28,-8);X.lineTo(-8,-8);X.lineTo(-8,-30);X.moveTo(20,30);X.lineTo(20,-30);X.quadraticCurveTo(36,-20,20,4);X.stroke();X.restore()}});
 arriba(L,.6)}

// ---------- 08 · 2015: Emily Petroff y su equipo agregan un sensor; capta las señales en la frecuencia de un microondas ----------
function investigadora(x,yb,s,t){X.save();X.translate(x,yb);X.scale(s,s);X.lineCap='round';X.lineJoin='round';X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.ellipse(0,4,110,14,0,0,7);X.fill();X.fillStyle='#2a3440';rr(-50,-230,44,230,14);X.fill();rr(6,-230,44,230,14);X.fill();X.fillStyle='#3a2a20';[-28,28].forEach(q=>{X.beginPath();X.ellipse(q,-6,34,13,0,0,7);X.fill()});
 X.fillStyle='#2f7a8a';X.beginPath();X.moveTo(-80,-220);X.lineTo(-86,-430);X.quadraticCurveTo(-82,-474,-40,-478);X.lineTo(40,-478);X.quadraticCurveTo(82,-474,86,-430);X.lineTo(80,-220);X.closePath();X.fill();X.fillStyle='rgba(0,0,0,.12)';X.fillRect(-4,-470,8,250);
 X.strokeStyle='#2f7a8a';X.lineWidth=38;X.beginPath();X.moveTo(76,-446);X.quadraticCurveTo(150,-520,170,-600+Math.sin(t*5)*8);X.stroke();X.beginPath();X.moveTo(-76,-446);X.lineTo(-100,-270);X.stroke();X.fillStyle='#e0ac80';X.beginPath();X.arc(172,-612+Math.sin(t*5)*8,22,0,7);X.fill();
 rr(-16,-518,32,48,10);X.fill();X.fillStyle='#4a3020';X.beginPath();X.arc(0,-566,62,0,7);X.fill();X.beginPath();X.moveTo(-20,-520);X.quadraticCurveTo(40,-470,10,-400);X.quadraticCurveTo(-20,-450,-30,-520);X.fill();X.fillStyle='#e9c46a';rr(-14,-520,28,14,6);X.fill();X.restore()}
function espectro(x,y,w,h,t,pico,rgb,a){if(a<=0)return;X.save();X.globalAlpha=a;X.fillStyle='rgba(8,14,18,.9)';rr(x,y,w,h,20);X.fill();for(let i=0;i<24;i++){const q=(i+.5)/24,d=(q-pico)/.05,v=.12+.1*Math.abs(Math.sin(i*1.7+t*3))+.75*Math.exp(-d*d);X.fillStyle=`rgba(${rgb},${.55+.45*Math.exp(-d*d)})`;rr(x+20+i*(w-40)/24,y+h-24-v*(h-60),(w-40)/24-6,v*(h-60),5);X.fill()}X.restore()}
function p08(L,t){const c=T.c08,xe=T.x_emily,xs=T.x_sensor,xc=T.x_caught,xq=T.x_freq,xm=T.x_microwave,f=T.c09,k=xc-.3,fase=t>k;
 if(!fase)plano(L,t,[[c,440,1160,1.1],[xs,620,1080,1.22]],cm=>{campo(L,cm,t,{hora:'dia',yh:1540});antena(L+140,1600,1.2,-.3,{});
   X.fillStyle='#6b7682';X.fillRect(L+770,820,16,740);X.fillStyle='#22262b';rr(L+700,720,156,120,14);X.fill();X.fillStyle=`rgb(${VERDE})`;X.beginPath();X.arc(L+824,750,9+3*Math.sin(t*8),0,7);X.fill();X.strokeStyle='#8e98a4';X.lineWidth=7;X.beginPath();X.moveTo(L+740,720);X.lineTo(L+720,620);X.moveTo(L+780,720);X.lineTo(L+800,600);X.stroke();
   investigadora(L+560,1570,1.25,t);placa(L+250,1680,1,'2015',eio(seg(t,c+.05,c+.4)),{ts:60});placa(L+640,1700,1,'EMILY PETROFF',eio(seg(t,xe-.05,xe+.3)),{ts:42,w:440})});
 else plano(L,t,[[k,560,1000,1.08],[xq,540,1080,1],[f,540,1090,1.03]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#0a1014'],[1,'#16242c']]);X.fillRect(L-900,-900,2900,3800);tex('metal',L-300,300,1700,1700,{a:.08,v:1});
   X.fillStyle='#22262b';rr(L+100,640,140,110,14);X.fill();X.strokeStyle='#8e98a4';X.lineWidth=7;X.beginPath();X.moveTo(L+140,640);X.lineTo(L+124,560);X.moveTo(L+190,640);X.lineTo(L+206,548);X.stroke();espectro(L+270,620,720,360,t,.62,VERDE,1);
   const a2=eio(seg(t,xq-.3,xq+.2)),m=eio(seg(t,xm-.3,xm+.2));espectro(L+270,1140,720,360,t,.62,CAL,a2);if(a2>0){X.save();X.globalAlpha=a2;microondas(L+150,1380,.36,t,{on:1,plato:false});X.restore()}
   if(m>0){X.strokeStyle=`rgba(255,255,255,${.85*m})`;X.lineWidth=6;X.setLineDash([14,12]);const xx=L+270+20+.62*680;X.beginPath();X.moveTo(xx,640);X.lineTo(xx,1480);X.stroke();X.setLineDash([]);luz(xx,1060,200,'255,255,255',.2*m)}});
 arriba(L,.6)}

// ---------- 09 · probaron el microondas de la cocina: calentar comida normalmente no hacía nada ----------
function p09(L,t){const c=T.c09,xt=T.x_tested,xn=T.x_nothing,f=T.c10;
 plano(L,t,[[c,380,1160,1.26],[xn-.9,400,1160,1.26],[xn-.1,820,1150,1.2],[f,850,1150,1.24]],cm=>{cocina(L,cm,t,{});microondas(L+380,1400,1.05,t,{on:1,av:.15+.3*seg(t,c,f)});receptor(L+1020,1390,340,t,[],{})});
 arriba(L,.6)}

// ---------- 10 · después abrieron la puerta antes de que terminara, y la señal apareció ----------
function p10(L,t){const c=T.c10,xo=T.x_opened,xa=T.x_appeared,f=T.c11,ab=eio(seg(t,xo-.1,xo+.3)),g=golpe(t,xo+.15,.7),pk=eio(seg(t,xo+.7,xo+.95))*(.75+.25*Math.max(golpe(t,xo+.7,.5),golpe(t,xa-.1,.6))),m=eio(seg(t,c+.1,xo-.1));
 plano(L,t,[[c,400,1160,1.26],[xo+.3,400,1160,1.3],[xo+.5,430,1160,1.3],[xo+.8,830,1150,1.26],[f,850,1150,1.32]],cm=>{cocina(L,cm,t,{});microondas(L+380,1400,1.05,t,{on:1,abre:ab,av:.55});
  if(g>0)for(let j=0;j<3;j++){X.strokeStyle=`rgba(200,120,255,${g*(1-j*.25)})`;X.lineWidth=8;X.beginPath();X.arc(L+300,1210,160+j*70+(1-g)*120,-.9,.9);X.stroke()}
  if(ab<.9){const hx=L+lerp(1300,800,m)-ab*340,hy=1250;mano(hx,hy,-.05,1.3,-1,{curl:[.6,.64,.68,.7],pulgar:.3})}
  receptor(L+1020,1390,340,t,[[.5,.95*pk]],{});if(pk>0)luz(L+1020,1280,260,VERDE,.4*Math.max(golpe(t,xo+.7,.9),golpe(t,xa-.1,.8)))});
 arriba(L,.6)}

// ---------- 11 · el misterio no estaba en el espacio profundo: era alguien apurado por comer (corte por coincidencia: plato → ventana redonda) ----------
function platoFrente(x,y,r,n){X.fillStyle=gl(x-r,y-r,x+r,y+r,[[0,n?'#7d8792':'#e9eef2'],[1,n?'#4a535e':'#aab3bd']]);X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.18)';X.lineWidth=4;[.33,.66].forEach(q=>{X.beginPath();X.arc(x,y,r*q,0,7);X.stroke()});for(let i=0;i<12;i++){const a=i*Math.PI/6;X.beginPath();X.moveTo(x+Math.cos(a)*r*.12,y+Math.sin(a)*r*.12);X.lineTo(x+Math.cos(a)*r,y+Math.sin(a)*r);X.stroke()}
 X.strokeStyle=n?'#8e98a4':'#6b7682';X.lineWidth=9;[.8,2.35,3.9,5.5].forEach(a=>{X.beginPath();X.moveTo(x+Math.cos(a)*r*.96,y+Math.sin(a)*r*.96);X.lineTo(x,y);X.stroke()});X.fillStyle='#3d4550';rr(x-30,y-30,60,60,10);X.fill()}
function p11(L,t){const c=T.c11,xw=T.x_wasnt,xh=T.x_hurry,f=T.c12,k=xw+.35,coc=t>k,S=1.9,mx=L+540-76*S,my=1640-180*S;
 if(!coc)plano(L,t,[[c,540,my,1.04],[k,540,my,1.12]],cm=>{noche(L,t,{c0:'#05070f',c1:'#182040',y1:1920,n:70,ys:420,yh:1500,sem:2});platoFrente(mx,my,138*S,1)});
 else plano(L,t,[[k,540,my,1.12],[xh,560,my+40,1.02],[f,580,my+50,1.06]],cm=>{cocina(L,cm,t,{p0:'#6a7a6a',p1:'#9aaa92'});const ab=eio(seg(t,k+.5,k+.9)),sa=eio(seg(t,xh-.3,xh+.6));
   X.save();X.translate(0,240);microondas(L+540,1400,S,t,{on:t<k+.5,abre:ab,av:.6,plato:sa<.05});X.restore();
   if(ab>.5){const px=lerp(L+540-76*S,L+1500,sa),py=lerp(1640-112*S,1500,sa);if(sa>=.05){X.fillStyle='#f4f1ea';X.beginPath();X.ellipse(px,py,62*S,16*S,0,0,7);X.fill();X.fillStyle='#e07a3a';X.beginPath();X.ellipse(px,py-12*S,44*S,16*S,0,Math.PI,0);X.fill();X.fillStyle='#f4f1ea';X.beginPath();X.moveTo(px-56*S,py-12*S);X.lineTo(px+56*S,py-12*S);X.lineTo(px+40*S,py+14*S);X.lineTo(px-40*S,py+14*S);X.closePath();X.fill()}
    mano(lerp(L+1500,L+540-76*S+90,eio(seg(t,k+.8,xh-.3)))+sa*(960),py-10,-.05,1.5,-1,{curl:[.5,.54,.58,.6],pulgar:.35,lx:118,ly:44})}});
 arriba(L,.6)}

// ---------- 12 · CTA: el microondas en primer plano; la antena aparece un momento como reflejo en la puerta ----------
function p12(L,t){const c=T.c12,r=golpe(t,c+1.3,1.7);
 plano(L,t,[[c,450,1190,1.18],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{cocina(L,cm,t,{yp:1500});X.save();X.translate(0,90);microondas(L+420,1400,.95,t,{on:0});X.restore();
  if(r>0){X.save();X.globalAlpha=.5*r;X.beginPath();X.arc(L+420-76*.95,1490-180*.95,128*.95,0,7);X.clip();X.fillStyle='#0c1424';X.fillRect(L+100,1100,600,500);antena(L+350,1440,.34,-.3,{noche:1});X.restore()}});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12].forEach((f,i)=>{NUEVOS['dc_srabbit18_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SRABBIT18 · FIN =====
</script>
