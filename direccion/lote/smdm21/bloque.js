<script>
// ===== DC · SMDM21 · INICIO ===== (MDM 21h · NASA LOST a Spacecraft Over ONE Detail · lote del 28-nov · una escena por línea del guion)
// Sin logos. La sonda es genérica. En el G2 (línea 7) las dos columnas NO llevan rótulo: las unidades recién se nombran en la línea 9. Azul = lo previsto · naranja = lo que pasó.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,noche,planeta,hojaP,renglones,tarj,desenfoca,borroso}=window.B28;
const AZ='110,180,255',NA='255,150,70',PAPEL='#efe6d0',TINTA='#2a2019';
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({manga:'#1c2533',puno:'#f1ede4'},o))};

function espacio(L,t,o){o=o||{};noche(L,t,{c0:o.c0||'#05070f',c1:o.c1||'#101832',y1:1920,n:70,ys:420,yh:1500,sem:o.sem||0})}
function marte(x,y,r,t,o){o=o||{};luz(x,y,r*1.22,'255,150,100',.22);planeta(x,y,r,{c0:'#e0875a',c1:'#8a3f2a',banda:'110,45,28',atm:'255,180,140',giro:Math.sin(t*.3)*r*.2})}
// sonda genérica: cuerpo dorado, antena, un panel solar, tobera. rot en radianes; llama 0..1 (sale hacia atrás)
function sonda(x,y,s,rot,o){o=o||{};X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);if(o.a!==undefined)X.globalAlpha=o.a;X.lineJoin='round';
 if(o.llama>0){const f=o.llama*(.85+.15*Math.sin(o.t*40));X.fillStyle='rgba(255,150,60,.9)';X.beginPath();X.moveTo(-70,-18);X.lineTo(-70-150*f,0);X.lineTo(-70,18);X.closePath();X.fill();X.fillStyle='rgba(255,240,200,.95)';X.beginPath();X.moveTo(-70,-9);X.lineTo(-70-70*f,0);X.lineTo(-70,9);X.closePath();X.fill();luz(-110,0,120,NA,.5*o.llama)}
 X.fillStyle='#5a6470';X.beginPath();X.moveTo(-50,-16);X.lineTo(-74,-24);X.lineTo(-74,24);X.lineTo(-50,16);X.closePath();X.fill();
 const pl=o.panel===undefined?1:o.panel;X.fillStyle='#3a424c';X.fillRect(-6,-40-140*pl,12,140*pl);X.fillStyle='#2f5fb0';X.fillRect(-46,-50-150*pl,92,120*pl);X.strokeStyle='rgba(255,255,255,.35)';X.lineWidth=2;for(let i=1;i<4;i++){X.beginPath();X.moveTo(-46+i*23,-50-150*pl);X.lineTo(-46+i*23,-50-150*pl+120*pl);X.stroke()}
 X.fillStyle=gl(0,-44,0,44,[[0,'#f2c94c'],[1,'#b8892e']]);rr(-52,-44,104,88,10);X.fill();X.fillStyle='rgba(0,0,0,.14)';X.fillRect(-52,8,104,36);X.fillStyle='#e9eef2';X.beginPath();X.ellipse(66,0,22,54,0,0,7);X.fill();X.fillStyle='#b9c2c9';X.beginPath();X.ellipse(72,0,12,40,0,0,7);X.fill();X.strokeStyle='#8e98a4';X.lineWidth=4;X.beginPath();X.moveTo(72,0);X.lineTo(104,0);X.stroke();X.restore()}
function cohete(x,yb,s,t,fl){X.save();X.translate(x,yb);X.scale(s,s);if(fl>0){const f=fl*(.85+.15*Math.sin(t*38));X.fillStyle='rgba(255,150,60,.92)';X.beginPath();X.moveTo(-70,0);X.quadraticCurveTo(0,420*f,70,0);X.closePath();X.fill();X.fillStyle='rgba(255,244,210,.95)';X.beginPath();X.moveTo(-34,0);X.quadraticCurveTo(0,220*f,34,0);X.closePath();X.fill();luz(0,80,300,NA,.6*fl)}
 X.fillStyle='#c9ced6';[-1,1].forEach(q=>{rr(q*64-22,-330,44,330,14);X.fill();X.beginPath();X.moveTo(q*64-22,-320);X.lineTo(q*64,-380);X.lineTo(q*64+22,-320);X.closePath();X.fill()});
 X.fillStyle=gl(-44,0,44,0,[[0,'#dfe5ea'],[.5,'#ffffff'],[1,'#b9c2c9']]);rr(-44,-640,88,640,10);X.fill();X.beginPath();X.moveTo(-44,-630);X.quadraticCurveTo(-40,-760,0,-800);X.quadraticCurveTo(40,-760,44,-630);X.closePath();X.fill();X.fillStyle='#2f5fb0';X.fillRect(-44,-470,88,26);X.fillStyle='#3a424c';X.fillRect(-44,-240,88,14);X.restore()}
// curva cuadrática muestreada: dibuja de 0 a u; devuelve el punto en u
function curva(P,u,col,lw,dash){const f=q=>[(1-q)*(1-q)*P[0][0]+2*q*(1-q)*P[1][0]+q*q*P[2][0],(1-q)*(1-q)*P[0][1]+2*q*(1-q)*P[1][1]+q*q*P[2][1]];if(u>0&&col){X.save();X.strokeStyle=col;X.lineWidth=lw||8;X.lineCap='round';if(dash)X.setLineDash(dash);X.beginPath();const n=40;for(let i=0;i<=n;i++){const p=f(u*i/n);i?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1])}X.stroke();X.restore()}return f(u)}
function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,(o.ts||50)*s,o.tc||'#2a2f38',{w:800});X.restore()}
function monitor(x,y,w,h,t,plano0,rgb){X.fillStyle='#0b1420';rr(x,y,w,h,14);X.fill();X.strokeStyle='rgba(255,255,255,.2)';X.lineWidth=4;rr(x,y,w,h,14);X.stroke();X.strokeStyle=`rgb(${rgb||'110,230,150'})`;X.lineWidth=5;X.lineCap='round';X.beginPath();for(let i=0;i<=40;i++){const q=i/40,xx=x+16+q*(w-32),am=(1-plano0)*h*.28;const yy=y+h/2+Math.sin(q*18-t*6)*am*Math.sin(q*3.14);i?X.lineTo(xx,yy):X.moveTo(xx,yy)}X.stroke()}
function salaTec(L,cm,o){o=o||{};X.fillStyle=gl(0,0,0,1920,[[0,o.c0||'#0c1a2c'],[1,o.c1||'#16304a']]);X.fillRect(L-1400,-900,5200,3800);tex('metal',L-400,300,3400,1700,{a:.08,v:1});X.strokeStyle='rgba(120,180,255,.06)';X.lineWidth=3;for(let i=-6;i<50;i++){X.beginPath();X.moveTo(L-400+i*80,300);X.lineTo(L-400+i*80,1900);X.stroke()}}
function barrasNum(x,y,n,w,col,sem){for(let i=0;i<n;i++){X.fillStyle=col;rr(x,y+i*46,w*(.55+.45*rnd(i+(sem||0))),22,8);X.fill()}}

// ---------- 01 · gancho: la sonda pasa demasiado cerca de Marte y se pierde detrás del planeta ----------
function p01(L,t){const xl=T.x_lost,xd=T.x_detail,xs=T.x_school,f=T.c02,u=seg(t,0,xd+1.3),P=[[-260,640],[380,720],[640,1130]],p=curva(P.map(q=>[L+q[0],q[1]]),u),tras=u>.8,mar=()=>marte(L+820,1560,640,t);
 plano(L,t,[[0,380,1010,1.16],[xl,470,1040,1.12],[xd,600,1090,1.2],[f,640,1110,1.26]],cm=>{espacio(L,t);
  if(tras){sonda(p[0],p[1],1.1,.9,{t,a:1-eio(seg(u,.8,.97))});mar()}else{mar();sonda(p[0],p[1],1.1,lerp(.1,.9,u),{t})}
  const q=eio(seg(t,xs-.5,xs+.2));if(q>0){curva([[L-260,560],[L+330,560],[L+560,900]],q,`rgba(${AZ},.9)`,7,[18,16]);curva(P.map(z=>[L+z[0],z[1]]),q,`rgba(${NA},.9)`,7)}});
 arriba(L,.6)}

// ---------- 02 · diciembre de 1998: despega el cohete; corte a la sonda ya suelta ----------
function p02(L,t){const c=T.c02,xn=T.x_launched,xc=T.x_called,f=T.c03,k=xc-.25,sub=eio(seg(t,xn-.5,k));
 if(t<k)plano(L,t,[[c,540,1260,1.1],[xn-.4,540,1200,1.1],[k,540,520,1.1]],cm=>{X.fillStyle=gl(0,-900,0,1700,[[0,'#081026'],[.7,'#2a3a6a'],[1,'#e08a5a']]);X.fillRect(L-900,-1900,2900,4800);
   X.fillStyle='#141a24';X.fillRect(L-900,1640,2900,900);X.fillStyle='#22262e';X.fillRect(L+250,1000,40,640);X.fillRect(L+250,1000,180,26);X.fillRect(L+250,1240,180,26);
   const yy=1640-sub*sub*1500;for(let i=0;i<14;i++){const u=((t*.6+i/14)%1),r=80+u*200;X.fillStyle=`rgba(230,230,235,${.5*(1-u)*Math.min(1,sub*4+.2)})`;X.beginPath();X.arc(L+540+(rnd(i)-.5)*700*u,1660-u*120,r,0,7);X.fill()}
   cohete(L+540,yy,1,t,Math.min(1,sub*3+.15));placa(L+300,720,1,'DECEMBER 1998',eio(seg(t,c+.05,c+.4))*(1-eio(seg(t,xn-.2,xn+.3))),{ts:44,w:440})});
 else plano(L,t,[[k,540,1040,1.2],[f,580,1020,1.08]],cm=>{espacio(L,t,{sem:5});X.save();X.beginPath();X.arc(L+200,2500,1100,0,7);X.fillStyle=gl(0,1400,0,2000,[[0,'#3f7fd0'],[1,'#1c3a70']]);X.fill();X.restore();luz(L+200,1500,700,'110,170,255',.2);
   const d=eio(seg(t,k,k+1.6));X.save();X.translate(L+360-d*220,1240+d*160);X.rotate(-.5);X.fillStyle='#c9ced6';rr(-150,-40,240,80,10);X.fill();X.fillStyle='#3a424c';X.fillRect(70,-40,20,80);X.restore();
   sonda(L+600+d*40,960-d*40,1.35,-.5,{t,panel:eio(seg(t,k+.5,k+1.4))});placa(L+560,1330,1,'MARS CLIMATE ORBITER',eio(seg(t,xc+.15,xc+.5)),{ts:40,w:620})});
 arriba(L,.6)}

// ---------- 03 · su trabajo: dar vueltas a Marte y estudiar su clima ----------
function p03(L,t){const c=T.c03,xw=T.x_weather,f=T.c04,a=(t-c)*1.5+2.4,o=ruta(t,[[c,520,1090,1.08,-.05],[f,570,1070,1.2,.05]]),px=L+540+Math.cos(a)*470,py=1090+Math.sin(a)*150,fr=Math.sin(a)>0;
 cam(L,o[0],o[1],o[2],540,1000,()=>{espacio(L,t,{sem:9});X.save();X.strokeStyle=`rgba(${AZ},.6)`;X.lineWidth=6;X.setLineDash([16,16]);X.beginPath();X.ellipse(L+540,1090,470,150,0,Math.PI,0);X.stroke();X.restore();
  if(!fr)sonda(px,py,.75,a+1.57,{t});marte(L+540,1090,330,t);
  const q=eio(seg(t,xw-.4,xw+.2));if(q>0){X.save();X.beginPath();X.arc(L+540,1090,330,0,7);X.clip();X.strokeStyle=`rgba(255,236,214,${.7*q})`;X.lineWidth=9;X.lineCap='round';[[440,1010,70],[650,1180,90]].forEach((p,i)=>{X.beginPath();for(let j=0;j<=30;j++){const g=j/30*4.4+t*(i?-1:1),r=p[2]*j/30;j?X.lineTo(L+p[0]+Math.cos(g)*r,p[1]+Math.sin(g)*r*.6):X.moveTo(L+p[0],p[1])}X.stroke()});X.restore()}
  X.save();X.strokeStyle=`rgba(${AZ},.6)`;X.lineWidth=6;X.setLineDash([16,16]);X.beginPath();X.ellipse(L+540,1090,470,150,0,0,Math.PI);X.stroke();X.restore();if(fr)sonda(px,py,.9,a+1.57,{t})},o[3]);
 arriba(L,.6)}

// ---------- 04 · voló más de nueve meses; todo se veía normal ----------
function p04(L,t){const c=T.c04,x9=T.x_nine,xn=T.x_normal,f=T.c05,u=eio(seg(t,c,f-.2)),P=[[L+170,1500],[L+250,700],[L+900,760]];
 plano(L,t,[[c,360,1260,1.2],[f,700,950,1.12]],cm=>{espacio(L,t,{sem:3});tierra(L+170,1500,110,t);marte(L+900,760,130,t);
  for(let i=0;i<9;i++){const a=eio(seg(u,i/9-.02,i/9+.08));if(a<=0)continue;const p=curva(P,(i+.5)/9),s=.55+.05*i;X.save();X.globalAlpha=a*.9;X.translate(p[0]+110,p[1]+60+(1-a)*60);X.rotate(-.1+i*.03);X.fillStyle=PAPEL;rr(-34*s,-40*s,68*s,80*s,6);X.fill();X.fillStyle='#c0392b';rr(-34*s,-40*s,68*s,22*s,6);X.fill();X.fillStyle='rgba(42,32,25,.3)';for(let j=0;j<3;j++)X.fillRect(-22*s,-6*s+j*14*s,44*s,5*s);X.restore()}
  const p=curva(P,u,`rgba(${AZ},.95)`,8);sonda(p[0],p[1],.5,-1.2+u*1.1,{t});
  placa(L+560,1270,1,'9 MONTHS',eio(seg(t,x9-.05,x9+.3)),{ts:54});const q=eio(seg(t,xn-.5,xn));if(q>0){X.globalAlpha=q;monitor(L+380,1400,360,130,t,0);X.globalAlpha=1}});
 arriba(L,.6)}

// ---------- 05 · septiembre de 1999: enciende el motor para entrar en órbita y pasa por detrás del planeta ----------
function p05(L,t){const c=T.c05,xf=T.x_fired,xb=T.x_behind,f=T.c06,u=seg(t,c,xb+.5),x=lerp(-160,720,u),y=lerp(880,1050,u*u),tras=x>560,fl=t>xf&&!tras?1:0;
 plano(L,t,[[c,400,1040,1.14],[xb,600,1060,1.2],[f,640,1070,1.24]],cm=>{espacio(L,t,{sem:12});
  if(tras)sonda(L+x,y,1.15,.2,{t,a:1-eio(seg(x,560,700))});marte(L+900,1260,560,t);if(!tras)sonda(L+x,y,1.15,.2,{t,llama:fl});
  X.save();X.strokeStyle=`rgba(${AZ},.45)`;X.lineWidth=6;X.setLineDash([16,16]);X.beginPath();X.moveTo(L+x+90,y+12);X.quadraticCurveTo(L+470,1010,L+580,1090);X.stroke();X.restore()});
 placa(L+290,560,1,'SEPTEMBER 1999',eio(seg(t,c+.05,c+.4))*(1-eio(seg(t,xf-.2,xf+.3))),{ts:44,w:470});arriba(L,.6)}

// ---------- 06 · nunca volvió a salir ----------
function p06(L,t){const c=T.c06,f=T.c07,b=.5+.5*Math.sin((t-c)*7);
 plano(L,t,[[c,560,1080,1.24],[f,540,1080,1.12]],cm=>{espacio(L,t,{sem:12});marte(L+330,1260,560,t);
  X.save();X.strokeStyle=`rgba(${AZ},.45)`;X.lineWidth=6;X.setLineDash([16,16]);X.beginPath();X.arc(L+330,1260,640,-1.1,-.15);X.stroke();X.restore();
  const ex=L+330+Math.cos(-.62)*640,ey=1260+Math.sin(-.62)*640;X.strokeStyle=`rgba(255,255,255,${.35+.5*b})`;X.lineWidth=5;X.beginPath();X.arc(ex,ey,46,0,7);X.stroke();[0,1.57,3.14,4.71].forEach(a=>{X.beginPath();X.moveTo(ex+Math.cos(a)*56,ey+Math.sin(a)*56);X.lineTo(ex+Math.cos(a)*78,ey+Math.sin(a)*78);X.stroke()});
  monitor(L+600,1420,380,130,t,eio(seg(t,c,c+.7)),'255,120,100')});
 arriba(L,.6)}

// ---------- 07 · G2: el detalle que aprendiste en el colegio. Dos columnas de números sin rótulo y una línea entre ellas ----------
function tablero(x,y,w,h,col,o){o=o||{};X.fillStyle='rgba(0,0,0,.3)';rr(x+10,y+14,w,h,22);X.fill();X.fillStyle='#0f2036';rr(x,y,w,h,22);X.fill();X.strokeStyle=col;X.lineWidth=6;rr(x,y,w,h,22);X.stroke();
 X.fillStyle='rgba(255,255,255,.1)';rr(x+30,y+30,w-60,70,14);X.fill();if(o.rot){X.fillStyle=col;txt(o.rot,x+w/2,y+68,o.ts||40,'#fff',{w:800})}else{X.fillStyle='rgba(255,255,255,.28)';rr(x+w/2-70,y+54,140,22,10);X.fill()}
 barrasNum(x+50,y+150,o.n||7,w-190,o.cb||'rgba(200,225,255,.75)',o.sem);if(o.u)for(let i=0;i<(o.n||7);i++){X.fillStyle=col;txt(o.u,x+w-74,y+162+i*46,30,col,{w:800})}}
function p07(L,t){const c=T.c07,xs=T.x_school7,xm=T.x_months,f=T.c08,g=golpe(t,xs,.7),al=eio(seg(t,xs-.2,xs+.3));
 plano(L,t,[[c,540,1100,1],[xs,540,1090,1.14],[f,540,1080,1.26]],cm=>{salaTec(L,cm);luz(L+540,1090,700,'255,90,70',.16*al+.2*g);
  tablero(L+60,820,400,520,`rgb(${NA})`,{sem:1});tablero(L+620,820,400,520,`rgb(${AZ})`,{sem:1});
  X.strokeStyle='rgba(255,255,255,.35)';X.lineWidth=8;X.setLineDash([10,14]);X.beginPath();X.moveTo(L+460,1080);X.lineTo(L+620,1080);X.stroke();X.setLineDash([]);
  for(let j=0;j<3;j++){const u=((t-c)*.8+j/3)%1;X.fillStyle='#fff';X.beginPath();X.arc(L+460+u*160,1080,9,0,7);X.fill()}
  if(al>0){X.save();X.globalAlpha=al;X.translate(L+540,1080-110);X.rotate(-.12+.1*g);X.scale(1+.15*g,1+.15*g);X.fillStyle='#f2c94c';rr(-120,-24,240,48,6);X.fill();X.strokeStyle='#5a4a1c';X.lineWidth=3;for(let i=0;i<=12;i++){X.beginPath();X.moveTo(-108+i*18,-24);X.lineTo(-108+i*18,i%2?-8:2);X.stroke()}X.restore()}});
 arriba(L,.6)}

// ---------- 08 · no fue el motor, ni la computadora de a bordo ----------
function p08(L,t){const c=T.c08,xe=T.x_engine,xk=T.x_computer,f=T.c09,d1=eio(seg(t,xe-.1,xe+.4)),d2=eio(seg(t,xk+.1,xk+.5));
 plano(L,t,[[c,520,1060,1.02],[xk+.2,560,1060,1.04],[xk+.9,550,1330,1.12],[f,540,1360,1.16]],cm=>{salaTec(L,cm,{c0:'#101624',c1:'#1c2c44'});
  [[250,d1,0],[830,d2,1]].forEach(([x,d,i])=>{X.fillStyle='#0f2036';rr(L+x-230,760,460,480,26);X.fill();X.strokeStyle=`rgba(${AZ},${.8-.6*d})`;X.lineWidth=6;rr(L+x-230,760,460,480,26);X.stroke();X.save();X.globalAlpha=1-.72*d;
   if(i===0){X.translate(L+x,1000);X.fillStyle='#8e98a4';rr(-70,-170,140,110,14);X.fill();X.fillStyle=gl(-110,0,110,0,[[0,'#5a6470'],[.5,'#c9ced6'],[1,'#4a5460']]);X.beginPath();X.moveTo(-60,-60);X.lineTo(60,-60);X.lineTo(120,150);X.lineTo(-120,150);X.closePath();X.fill();X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,150,120,22,0,0,7);X.fill()}
   else{X.translate(L+x,1000);X.fillStyle='#1f6a4a';rr(-150,-150,300,300,16);X.fill();X.fillStyle='#22262b';rr(-70,-70,140,140,10);X.fill();X.strokeStyle='#d9b24a';X.lineWidth=6;for(let k=-2;k<=2;k++){X.beginPath();X.moveTo(-70,k*26);X.lineTo(-130,k*26);X.moveTo(70,k*26);X.lineTo(130,k*26);X.moveTo(k*26,-70);X.lineTo(k*26,-130);X.moveTo(k*26,70);X.lineTo(k*26,130);X.stroke()}}
   X.restore();if(d>0){X.strokeStyle=`rgba(120,220,150,${d})`;X.lineWidth=16;X.lineCap='round';X.beginPath();X.moveTo(L+x-50,1290);X.lineTo(L+x-14,1326);X.lineTo(L+x+56,1250);X.stroke()}});
  const q=eio(seg(t,xk+.3,xk+.9));hojaP(L+540,1620+(1-q)*500,620,400,-.03,()=>{X.strokeStyle='rgba(42,32,25,.25)';X.lineWidth=3;for(let i=1;i<6;i++){X.beginPath();X.moveTo(-290,-200+i*66);X.lineTo(290,-200+i*66);X.stroke()}for(let i=1;i<4;i++){X.beginPath();X.moveTo(-310+i*155,-180);X.lineTo(-310+i*155,180);X.stroke()}for(let i=0;i<20;i++){X.fillStyle='rgba(42,32,25,.45)';rr(-286+(i%4)*155,-176+Math.floor(i/4)*66,90*(.5+.5*rnd(i)),18,6);X.fill()}});luz(L+540,1600,520,'255,236,200',.2*q)});
 arriba(L,.6)}

// ---------- 09 · dos equipos compartían números: uno escribió en libras-fuerza, el otro leyó newtons ----------
function p09(L,t){const c=T.c09,xc=T.x_contractor,xp=T.x_pounds,xn=T.x_nasa9,xw=T.x_newtons,f=T.c10,D=660,ap=eio(seg(t,xp-.2,xp+.2)),an=eio(seg(t,xw-.2,xw+.2));
 plano(L,t,[[c,740,1100,.7],[xc-.3,760,1100,.72],[xc+.4,420,1100,1.14],[xn-.8,480,1100,1.14],[xn,D+560,1100,1.14],[f,D+600,1090,1.2]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#2a1c12'],[1,'#4a3220']]);X.fillRect(L-1400,-900,2250,3800);tex('ladrillo',L-500,300,1350,1100,{a:.12,v:2});X.fillStyle=gl(0,0,0,1920,[[0,'#0c1a2c'],[1,'#16304a']]);X.fillRect(L+850,-900,3200,3800);tex('metal',L+850,300,1800,1700,{a:.08,v:1});
  X.fillStyle='#17131c';X.fillRect(L+810,-900,80,3800);luz(L+380,900,700,'255,190,120',.2);luz(L+D+540,900,700,AZ,.18);
  meson(L,1480,{tex:'madera',col:'#553a23',ta:.9});X.fillStyle='#16283c';X.fillRect(L+890,1480,3200,900);X.fillStyle='rgba(255,255,255,.08)';X.fillRect(L+890,1480,3200,8);
  hojaP(L+400,1130,470,520,-.04,()=>{barrasNum(-170,-150,6,230,'rgba(42,32,25,.6)',2);if(ap>0)for(let i=0;i<6;i++){X.globalAlpha=ap;txt('lbf',120,-138+i*46,34,'#c0392b',{w:800});X.globalAlpha=1}});
  placa(L+400,790,1,'POUNDS OF FORCE',ap,{ts:42,w:520,col:'#f2c94c',tc:'#2a1a0c'});mano(L+620,1300+Math.sin(t*9)*8,-.5,1.3,-1,{curl:[.5,.8,.9,.9],pulgar:.1,pulgarCurl:.5,lx:196,ly:-6,graf:1});
  X.strokeStyle='rgba(255,255,255,.3)';X.lineWidth=10;X.beginPath();X.moveTo(L+640,1130);X.lineTo(L+D+280,1130);X.stroke();
  for(let j=0;j<5;j++){const u=((t-c)*.3+j/5)%1,x=L+640+u*(D-360),pas=x>L+850;X.fillStyle='#fff';rr(x-44,1116,88,28,10);X.fill();if(!pas&&ap>0){X.globalAlpha=ap;txt('lbf',x+74,1132,26,'#f2c94c',{w:800});X.globalAlpha=1}else if(pas&&x<L+1010&&ap>0){const v=(x-L-850)/160;X.globalAlpha=ap*(1-v);txt('lbf',L+860,1132+v*170,26,'#f2c94c',{w:800});X.globalAlpha=1}}
  tablero(L+D+300,860,520,520,`rgb(${AZ})`,{sem:2,n:6,rot:an>0?'NEWTONS':'',u:an>0?'N':''})});
 arriba(L,.6)}

// ---------- 10 · una libra-fuerza son unos cuatro newtons y medio: cada corrección quedó mal por ese tanto ----------
function p10(L,t){const c=T.c10,x4=T.x_four,xe=T.x_every,xm=T.x_much,f=T.c11,eq=eio(seg(t,c+.3,x4)),sal=eio(seg(t,xe-.5,xe+.4)),ti=(1-eq)*.16;
 plano(L,t,[[c,540,1010,1.3],[x4+.4,540,1040,1.12],[xe+.3,540,1220,.98],[f,540,1240,1]],cm=>{salaTec(L,cm,{c0:'#101a2e',c1:'#1c3050'});luz(L+540,900,700,'255,236,200',.1);
  X.fillStyle='#c9ced6';X.beginPath();X.moveTo(L+490,1210);X.lineTo(L+590,1210);X.lineTo(L+556,860);X.lineTo(L+524,860);X.closePath();X.fill();X.fillStyle='#8e98a4';rr(L+400,1200,280,28,10);X.fill();
  X.save();X.translate(L+540,860);X.rotate(ti);X.fillStyle='#e9eef2';rr(-330,-12,660,24,12);X.fill();
  [[-270,0],[270,1]].forEach(([x,i])=>{X.save();X.translate(x,0);X.rotate(-ti);X.strokeStyle='#b9c2c9';X.lineWidth=5;X.beginPath();X.moveTo(-100,150);X.lineTo(0,0);X.lineTo(100,150);X.stroke();X.fillStyle='#8e98a4';rr(-130,150,260,22,10);X.fill();
   if(i===0){X.fillStyle=`rgb(${NA})`;rr(-76,34,152,116,12);X.fill();txt('1 lbf',0,94,50,'#2a1a0c',{w:900})}
   else for(let k=0;k<5;k++){const a=eio(seg(t,c+.5+k*.25,c+.8+k*.25));if(a<=0)continue;const w=k===4?24:48,bx=-112+(k%3)*76+(k>=3?38:0),by=k<3?98:44;X.globalAlpha=a;X.fillStyle=`rgb(${AZ})`;rr(bx,by-(1-a)*200,w,52,8);X.fill();if(k<4)txt('N',bx+24,by+28-(1-a)*200,30,'#0c1a2c',{w:900});X.globalAlpha=1}
   X.restore()});X.restore();
  placa(L+540,1330,1,'1 lb force ≈ 4.5 N',eio(seg(t,x4-.05,x4+.3))*(1-.0*sal),{ts:60,w:680});
  if(sal>0){X.globalAlpha=sal;X.fillStyle='rgba(8,16,30,.7)';rr(L+90,1450,900,360,30);X.fill();const u=eio(seg(t,xe-.2,xm+.3)),A=[[L+140,1640],[L+540,1520],[L+940,1560]],B=[[L+140,1640],[L+540,1560],[L+940,1760]];curva(A,1,`rgba(${AZ},.9)`,6,[14,14]);const p=curva(B,u,`rgba(${NA},1)`,8);
   for(let k=1;k<=5;k++){if(u>k/6){const q=curva(B,k/6);X.fillStyle=`rgb(${NA})`;X.beginPath();X.arc(q[0],q[1],11,0,7);X.fill()}}sonda(p[0],p[1],.42,.2+u*.3,{t});X.globalAlpha=1}});
 arriba(L,.6)}

// ---------- 11 · tras nueve meses de pequeños errores llegó demasiado bajo, dentro de la atmósfera. No se supo más ----------
function p11(L,t){const c=T.c11,xl=T.x_low,xd=T.x_deep,xn=T.x_never,f=T.c12,u=eio(seg(t,c+.3,xd+.6)),A=[[L-200,760],[L+500,640],[L+1300,820]],B=[[L-200,760],[L+460,860],[L+1040,1210]],p=curva(B,u),den=eio(seg(t,xd-.4,xd+.5));
 plano(L,t,[[c,380,1000,1.12],[xl,560,1040,1.16],[xd,700,1120,1.3],[f,720,1130,1.34]],cm=>{espacio(L,t,{sem:7});
  luz(L+700,2050,1250,'255,150,100',.3);planeta(L+700,2150,1000,{c0:'#e0875a',c1:'#8a3f2a',atm:'255,180,140',giro:t*4});
  X.save();X.strokeStyle='rgba(255,170,120,.16)';X.lineWidth=120;X.beginPath();X.arc(L+700,2150,1070,Math.PI*1.1,Math.PI*1.9);X.stroke();X.restore();
  curva(A,1,`rgba(${AZ},.75)`,6,[16,16]);curva(B,u,`rgba(${NA},.95)`,7);
  if(den<1)sonda(p[0],p[1],.85,.35+u*.25,{t,a:1-den});if(den>0)luz(p[0],p[1],160+60*den,'255,190,140',.7*den*(1-eio(seg(t,xd+.5,xn))));
  });
 monitor(L+60,1560,330,120,t,eio(seg(t,xn-.5,xn+.2)),den>.5?'255,120,100':'110,230,150');arriba(L,.6)}

// ---------- 12 · lección: nunca supongas que el otro equipo quiere decir lo mismo que tú. Revisa las unidades ----------
function regla(x,y,w,col,u,paso,a){X.save();X.translate(x,y);X.rotate(a||0);X.fillStyle='rgba(0,0,0,.25)';rr(6,10,w,96,8);X.fill();X.fillStyle=col;rr(0,0,w,96,8);X.fill();X.strokeStyle='rgba(20,20,30,.7)';X.lineWidth=3;for(let i=0;i*paso<=w-20;i++){X.beginPath();X.moveTo(14+i*paso,0);X.lineTo(14+i*paso,i%2?22:38);X.stroke()}txt(u,w-50,66,34,'rgba(20,20,30,.85)',{w:900});X.restore()}
function p12(L,t){const c=T.c12,xk=T.x_check,f=T.c13,al=eio(seg(t,xk-.3,xk+.3)),ok=eio(seg(t,xk+.3,xk+.7));
 plano(L,t,[[c,540,1080,1.02],[xk,540,1110,1.2],[f,540,1120,1.3]],cm=>{X.fillStyle='#16304a';X.fillRect(L-900,-900,2900,3800);X.strokeStyle='rgba(160,210,255,.12)';X.lineWidth=3;for(let i=-4;i<30;i++){X.beginPath();X.moveTo(L-200+i*60,300);X.lineTo(L-200+i*60,1900);X.stroke();X.beginPath();X.moveTo(L-400,300+i*60);X.lineTo(L+1500,300+i*60);X.stroke()}luz(L+540,1100,800,'200,230,255',.14);
  regla(L+lerp(60,170,al),lerp(940,1010,al),700,'#f2c94c','in',88,lerp(-.07,0,al));regla(L+lerp(260,170,al),lerp(1230,1116,al),700,'#7fc8f0','cm',35,lerp(.06,0,al));
  mano(L+lerp(210,300,al)+Math.sin(t*2)*6,lerp(1010,1066,al),.1,1.25,1,{curl:[.2,.24,.28,.3],pulgar:.6,lx:190,ly:0});mano(L+lerp(900,800,al)+Math.sin(t*2.3)*6,lerp(1300,1176,al),-.1,1.25,-1,{curl:[.2,.24,.28,.3],pulgar:.6,lx:190,ly:0});
  if(al>0){X.strokeStyle=`rgba(255,255,255,${.8*al})`;X.lineWidth=5;X.setLineDash([12,12]);X.beginPath();X.moveTo(L+184,900);X.lineTo(L+184,1320);X.stroke();X.setLineDash([])}
  if(ok>0){X.save();X.translate(L+540,1420);X.scale(back(ok),back(ok));X.fillStyle='#2ea86a';X.beginPath();X.arc(0,0,74,0,7);X.fill();X.strokeStyle='#fff';X.lineWidth=16;X.lineCap='round';X.lineJoin='round';X.beginPath();X.moveTo(-32,2);X.lineTo(-8,28);X.lineTo(36,-24);X.stroke();X.restore()}});
 const q=eio(seg(t,c+.05,c+.35))*(1-eio(seg(t,c+1.6,c+2)));if(q>0){X.save();X.globalAlpha=q;tarj(L+250,560,300,96,16,'#e9c46a',{sa:.3});txt('LESSON',L+250,564,58,'#2a1a0c',{w:900});X.restore()}
 arriba(L,.6)}

// ---------- 13 · CTA: la línea de la órbita se vuelve dos reglas alineadas ----------
function p13(L,t){const c=T.c13,m=eio(seg(t,c+.3,c+1.5));
 plano(L,t,[[c,470,1180,1.16],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{espacio(L,t,{sem:4,c1:'#16304a'});luz(L+400,1300,600,AZ,.14);luz(L+700,1380,300,NA,.12);
  if(m<1){X.save();X.globalAlpha=1-m;X.strokeStyle=`rgba(${AZ},.9)`;X.lineWidth=8;X.setLineDash([16,16]);X.beginPath();X.ellipse(L+420,1310,330,110,0,0,7);X.stroke();X.restore()}
  if(m>0){X.save();X.globalAlpha=m;regla(L+110,lerp(1310,1200,m),620,'#f2c94c','in',78,0);regla(L+110,lerp(1310,1320,m),620,'#7fc8f0','cm',31,0);X.restore()}});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_smdm21_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SMDM21 · FIN =====
</script>
