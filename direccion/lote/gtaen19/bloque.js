<script>
// ===== DC · GTAEN19 · INICIO ===== (GTA EN 19h · GTA 6 Just HUMILIATED Hollywood · paquete 11 del lote del 27-nov)
// Reglas del paquete: se distinguen preventa, estimación del día uno y taquilla; sin logos de juegos, películas ni plataformas; Hollywood no es una persona; las cifras son las aprobadas.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const ORO='#ffd23f',TEAL='#35e0d0',ROSA='#ff5fa2',NOCHE='#14102a',CREMA='#f3ecd8',TINTA='#1c1530',LUZ='#fff4d6';
const pop=(t,k)=>back(seg(t,k-.1,k+.16));
function ponTxt(s,x,y,size,col,k,o){if(k<=0)return;X.save();X.translate(x,y);X.scale(k,k);txt(s,0,0,size,col,o||{});X.restore()}
// ---------- marquesinas con bombillas ----------
function bombillas(x,y,w,h,t,on,paso){paso=paso||48;const P=[],nx=Math.round(w/paso),ny=Math.round(h/paso);for(let i=0;i<=nx;i++){P.push([x+i*w/nx,y]);P.push([x+i*w/nx,y+h])}for(let j=1;j<ny;j++){P.push([x,y+j*h/ny]);P.push([x+w,y+j*h/ny])}
 P.forEach((p,i)=>{const lit=((Math.floor(t*3)+i)%2?1:.5);X.fillStyle=on>0?`rgba(255,226,150,${(.3+.7*lit)*on+.12*(1-on)})`:'#3a3350';X.beginPath();X.arc(p[0],p[1],9,0,7);X.fill()})}
function tablero(x,y,w,h,t,on){X.fillStyle='rgba(0,0,0,.4)';rr(x-w/2+10,y-h/2+14,w,h,22);X.fill();rr(x-w/2,y-h/2,w,h,22);X.fillStyle='#0c0a18';X.fill();X.strokeStyle='#3a3350';X.lineWidth=6;X.stroke();bombillas(x-w/2+22,y-h/2+22,w-44,h-44,t,on)}
function rodillos(x,y,n,an,al,t){for(let i=0;i<n;i++){const v=x+(i-(n-1)/2)*(an+14);rr(v-an/2,y-al/2,an,al,10);X.fillStyle='#1c1830';X.fill();const k=(t*8+i*.37)%1;X.fillStyle='rgba(255,244,214,.5)';X.fillRect(v-an/2+10,y-al/2+8+k*(al-28),an-20,12)}}
function escenario(L,t,cort){X.fillStyle=NOCHE;X.fillRect(L-900,-900,2900,4200);[300,780].forEach(v=>{X.fillStyle='rgba(255,226,150,.045)';X.beginPath();X.moveTo(L+v-30,-200);X.lineTo(L+v+30,-200);X.lineTo(L+v+340,1560);X.lineTo(L+v-340,1560);X.closePath();X.fill()});
 X.fillStyle=TINTA;X.fillRect(L-900,1560,2900,2600);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L-900,1560,2900,6);
 if(cort)[[-900,1010],[970,1000]].forEach(q=>{X.fillStyle='#4a1428';X.fillRect(L+q[0],-900,q[1],2500);X.fillStyle='rgba(0,0,0,.22)';for(let i=0;i<14;i++)X.fillRect(L+q[0]+i*74,-900,26,2500)})}
// ---------- P01 · la claqueta cae; detrás, el récord se quiebra ----------
function claqueta(x,y,s,ang,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';rr(-258,-146,540,380,14);X.fill();
 rr(-270,-160,540,380,14);X.fillStyle='#16141f';X.fill();trazo(LIN,4);X.strokeStyle='rgba(243,236,216,.55)';X.lineWidth=4;[-60,30,120].forEach(v=>{X.beginPath();X.moveTo(-240,v);X.lineTo(240,v);X.stroke()});X.beginPath();X.moveTo(-60,30);X.lineTo(-60,190);X.moveTo(90,30);X.lineTo(90,190);X.stroke();
 const fr=yy=>{X.save();rr(-270,yy,540,62,8);X.clip();X.fillStyle=CREMA;X.fillRect(-270,yy,540,62);X.fillStyle='#16141f';for(let i=-1;i<8;i++){X.beginPath();X.moveTo(-270+i*80,yy+62);X.lineTo(-230+i*80,yy+62);X.lineTo(-190+i*80,yy);X.lineTo(-230+i*80,yy);X.closePath();X.fill()}X.restore();rr(-270,yy,540,62,8);X.strokeStyle=LIN;X.lineWidth=4;X.stroke()};
 fr(-222);X.save();X.translate(-270,-222);X.rotate(-ang);X.translate(270,160);fr(-222);X.restore();X.restore()}
function copa(x,y,s,col,som){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle=som?'#221a3a':col;X.strokeStyle=som?'#3a3058':LIN;X.lineWidth=4;
 [-1,1].forEach(d=>{X.beginPath();X.arc(d*96,-150,44,0,7);X.lineWidth=14;X.strokeStyle=som?'#221a3a':col;X.stroke()});X.lineWidth=4;X.strokeStyle=som?'#3a3058':LIN;
 X.beginPath();X.moveTo(-100,-230);X.lineTo(100,-230);X.quadraticCurveTo(96,-70,0,-50);X.quadraticCurveTo(-96,-70,-100,-230);X.closePath();X.fill();X.stroke();X.fillRect(-14,-52,28,60);rr(-70,6,140,34,8);X.fill();X.stroke();if(!som){X.fillStyle='rgba(255,255,255,.35)';X.fillRect(-70,-212,22,110)}X.restore()}
function p01(L,t){const xh=T.x_hum,xr=T.x_record,xt=T.x_touched,xa=T.x_and,xo=T.x_only,fin=T.c02;
 const cu=seg(t,.02,.3),cae=cu*cu,sale=eio(seg(t,xh+.12,xh+.75)),ang=.42*(1-eio(seg(t,xh-.09,xh))),parte=eio(seg(t,xr-.1,xt)),sac=golpe(t,xh-.02,.3);
 const ac=eio(seg(t,xa+.3,fin));cam(L,540+ac*70,1000+ac*60+sac*14,lerp(1,1.04,seg(t,0,xa))+ac*.1+sac*.045,540,1000,()=>{escenario(L,t,1);
  // el récord: dos mitades que se separan por la grieta
  if(parte<1)[-1,1].forEach(d=>{X.save();X.translate(L+540+d*parte*240,700+parte*parte*1700);X.rotate(d*parte*.7);X.beginPath();if(d<0){X.moveTo(-400,-260);X.lineTo(20,-260);X.lineTo(-30,-80);X.lineTo(40,40);X.lineTo(-20,260);X.lineTo(-400,260)}else{X.moveTo(400,-260);X.lineTo(20,-260);X.lineTo(-30,-80);X.lineTo(40,40);X.lineTo(-20,260);X.lineTo(400,260)}X.closePath();X.clip();tablero(0,0,680,360,t,t<xh?1:.25);txt('RECORD',0,6,124,t<xh?LUZ:'#8a8298',{g:t<xh?18:0,gc:ORO});X.restore()});
  if(t>=xh&&parte<.02){X.strokeStyle='#05040a';X.lineWidth=8;X.lineJoin='round';X.beginPath();X.moveTo(L+560,520);X.lineTo(L+510,620);X.lineTo(L+580,740);X.lineTo(L+520,880);X.stroke()}
  // lo que queda: una copa ganada y otra todavía a oscuras
  const c1=eo(seg(t,xt-.2,xt+.5)),c2=eo(seg(t,xa-.1,xa+.5));
  if(c1>0){X.fillStyle='#2a2244';X.fillRect(L+210,1560-c1*330,200,c1*330+4);X.fillStyle=`rgba(255,226,150,${.10*c1})`;X.beginPath();X.arc(L+310,1050,220,0,7);X.fill();copa(L+310,1560-c1*330-44,1.1,ORO);const gl=(t*.9)%1;X.save();X.translate(L+250+gl*130,1560-c1*330-290+gl*150);X.rotate(t*2);X.fillStyle=`rgba(255,255,255,${.9*Math.sin(gl*Math.PI)})`;for(let k=0;k<4;k++){X.rotate(Math.PI/2);X.beginPath();X.moveTo(0,-4);X.lineTo(26,0);X.lineTo(0,4);X.closePath();X.fill()}X.restore()}
  if(c2>0){X.fillStyle='#2a2244';X.fillRect(L+670,1560-c2*330,200,c2*330+4);const g2=golpe(t,xo,.9);X.fillStyle=`rgba(53,224,208,${.12*g2})`;X.beginPath();X.arc(L+770,1050,220,0,7);X.fill();copa(L+770,1560-c2*330-44,1.1,ORO,1);if(g2>0){X.strokeStyle=`rgba(53,224,208,${g2})`;X.lineWidth=5;X.beginPath();X.arc(L+770,1050,150+g2*40,0,7);X.stroke()}}
  if(sale<1)claqueta(L+540,lerp(-460,1160,cae)-golpe(t,.3,.22)*26+sale*sale*1900,1.25,ang,sale*.5);
})}
// ---------- P02 · 19 de noviembre, tras dos retrasos; se abre la caja ----------
function fieltro(L){X.fillStyle='#16122b';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(255,255,255,.02)';for(let i=0;i<40;i++)X.fillRect(L-900,-900+i*104,2900,3)}
function hojaCal(x,y,s,rot,mes,dia,equis){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle='rgba(0,0,0,.35)';rr(-182,-196,380,420,14);X.fill();rr(-190,-210,380,420,14);X.fillStyle=CREMA;X.fill();trazo(LIN,3);X.save();rr(-190,-210,380,420,14);X.clip();X.fillStyle='#c0392b';X.fillRect(-190,-210,380,96);X.restore();if(mes)txt(mes,0,-160,50,CREMA);
 X.fillStyle=TINTA;[-110,110].forEach(v=>{X.beginPath();X.arc(v,-210,12,0,7);X.fill()});if(dia>0)ponTxt('19',0,56,220,TINTA,dia);
 if(equis>0){X.strokeStyle='#c0392b';X.lineWidth=26;X.lineCap='round';X.beginPath();X.moveTo(-110,-50);X.lineTo(-110+220*Math.min(1,equis*2),-50+220*Math.min(1,equis*2));X.stroke();if(equis>.5){const e=(equis-.5)*2;X.beginPath();X.moveTo(110,-50);X.lineTo(110-220*e,-50+220*e);X.stroke()}}X.restore()}
function cajaJuego(x,y,s,ab){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';rr(-150,-180,320,400,12);X.fill();
 rr(-160,-195,320,390,12);X.fillStyle='#1b1830';X.fill();trazo(LIN,3);X.fillStyle='#b9c2cc';X.beginPath();X.arc(0,0,124,0,7);X.fill();trazo(LIN,3);X.fillStyle='rgba(255,95,162,.35)';X.beginPath();X.moveTo(0,0);X.arc(0,0,124,-1,-.2);X.closePath();X.fill();X.fillStyle='rgba(53,224,208,.35)';X.beginPath();X.moveTo(0,0);X.arc(0,0,124,2,2.9);X.closePath();X.fill();X.fillStyle='#1b1830';X.beginPath();X.arc(0,0,30,0,7);X.fill();
 const sx=Math.cos(ab*Math.PI);X.save();X.translate(-160,0);X.scale(sx,1);if(sx>=0){const g=X.createLinearGradient(0,-195,0,195);g.addColorStop(0,'#3a1c5a');g.addColorStop(.55,'#d6457f');g.addColorStop(1,'#f39a4a');rr(0,-195,320,390,12);X.fillStyle=g;X.fill();trazo(LIN,3);X.fillStyle='#ffd98a';X.beginPath();X.arc(160,10,74,Math.PI,0);X.fill();X.fillStyle='#1b1230';X.fillRect(0,10,320,60);[70,250].forEach(v=>{X.fillRect(v-5,-70,10,90);for(let k=0;k<5;k++){const a=-2.5+k*.45;X.beginPath();X.ellipse(v+Math.cos(a)*34,-70+Math.sin(a)*24,38,9,a,0,7);X.fill()}});txt('GTA 6',160,128,64,'#fff0f6')}
 else{rr(0,-195,320,390,12);X.fillStyle='#24203a';X.fill();trazo(LIN,3);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(30,-150,260,300)}X.restore();X.restore()}
function p02(L,t){const c=T.c02,xl=T.x_launched,xn=T.x_nov,x19=T.x_19,x2=T.x_two,fin=T.c03;
 cam(L,540,1040,lerp(1.04,1,eo(seg(t,c,c+.8))),540,1000,()=>{fieltro(L);
  [[-1,0],[1,.25]].forEach((q,i)=>{const e=eo(seg(t,x2-.15+q[1],x2+.3+q[1]));if(e>0)hojaCal(L+540+q[0]*e*330,800+e*40-i*30,.86,q[0]*e*.32,null,0,seg(t,x2+.1+q[1]*.6,x2+.42+q[1]*.6))});
  const en=eo(seg(t,xn-.25,xn+.15));hojaCal(L+540,lerp(-300,790,en),1.05,(1-en)*.3-.03,'NOVEMBER',pop(t,x19),0);
  cajaJuego(L+540,1420,.95,eio(seg(t,x19+.05,x19+.6)))})}
// ---------- P03 · antes del día uno: las cajas se apilan y el contador llega a 32.5 millones ----------
function p03(L,t){const c=T.c03,xs=T.x_sold,x3=T.x_325,xm=T.x_mill3,fin=T.c04,n=Math.floor(seg(t,c+.1,x3)*108);
 const cm=ruta(t,[[c,430,1000,1.12],[x3-.05,540,1040,1],[fin,540,1040,1.04]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{escenario(L,t,0);X.fillStyle=TINTA;X.fillRect(L-900,1760,2900,2600);X.fillStyle='#3a2a1e';X.fillRect(L+90,1728,900,34);
  for(let i=0;i<n;i++){const col=i%9,fil=Math.floor(i/9),x=L+540+(col-4)*96-44,y=1728-(fil+1)*52;X.fillStyle=['#ff5fa2','#35e0d0','#8e5aa8','#f39a4a'][(col*3+fil*5)%4];rr(x,y,88,46,6);X.fill();X.fillStyle='rgba(0,0,0,.25)';X.fillRect(x+10,y+30,68,6);X.fillStyle='rgba(255,255,255,.25)';X.fillRect(x+10,y+8,30,8)}
  tablero(L+540,650,700,320,t,1);ponTxt('SOLD BEFORE DAY ONE',L+540,560,36,TEAL,pop(t,xs));
  if(t<x3)rodillos(L+540,668,4,96,110,t);else{ponTxt('32.5',L+540,662,150,LUZ,pop(t,x3),{g:16,gc:ORO});ponTxt('MILLION COPIES',L+540,762,40,ORO,pop(t,xm))}})}
// ---------- P04 · la estimación del día uno: 3.79 mil millones de dólares ----------
function marcadorDia(L,t,o){tablero(L+540,960,900,640,t,o.on);
 if(o.dia>0)ponTxt('DAY ONE',L+540,770,64,TEAL,o.dia,{a:o.on*.9+.1});
 if(o.giro)rodillos(L+540,960,4,150,200,t);else if(o.num>0){ponTxt('$3.79',L+540,950,214,o.on>.5?LUZ:'#57507a',o.num,{g:o.on>.5?20:0,gc:ORO});if(o.bill>0)ponTxt('BILLION',L+540,1110,84,o.on>.5?ORO:'#4a4468',o.bill)}
 if(o.est>0){X.save();X.translate(L+540,1310);X.rotate(-.03);X.scale(o.est,o.est);rr(-260,-40,520,80,10);X.fillStyle=o.on>.5?CREMA:'#57507a';X.fill();trazo(LIN,3);txt('TAKE-TWO ESTIMATE',0,2,38,TINTA);X.restore()}}
function p04(L,t){const c=T.c04,xe=T.x_est,xd=T.x_day,x3=T.x_379,xb=T.x_bill,fin=T.c05;
 cam(L,540,1000,lerp(1,1.06,seg(t,c,fin)),540,1000,()=>{escenario(L,t,1);marcadorDia(L,t,{on:1,dia:pop(t,xd),giro:t<x3,num:t<x3?0:pop(t,x3),bill:pop(t,xb),est:pop(t,xe)})})}
// ---------- P05 · comparación a escala: fin de semana de estreno contra un solo día ----------
const BASE=1640,PXB=250;
function p05(L,t){const c=T.c05,xm=T.x_movie,x12=T.x_12,xw=T.x_wk,s6=T.s_6,x3=T.x_three,xs=T.x_single,xl=T.x_launch,fin=T.c06;
 const h1=1.2*PXB*eo(seg(t,xm-.2,x12-.1)),h2=3.79*PXB*eo(seg(t,s6+.05,x3-.15));
 const cm=ruta(t,[[c,400,1380,1.45],[s6-.25,400,1380,1.5],[s6+.55,540,1050,1],[fin,540,1040,1.04]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{escenario(L,t,0);X.fillStyle=TINTA;X.fillRect(L-900,BASE,2900,2600);X.fillStyle='rgba(255,255,255,.1)';X.fillRect(L-900,BASE,2900,6);
  // la película: una columna de cinta
  if(h1>0){X.fillStyle='#3a3350';X.fillRect(L+180,BASE-h1,220,h1);X.save();X.beginPath();X.rect(L+180,BASE-h1,220,h1);X.clip();for(let y=BASE-20;y>BASE-h1-40;y-=44){X.fillStyle=NOCHE;X.fillRect(L+190,y-22,22,26);X.fillRect(L+368,y-22,22,26)}for(let y=BASE-12;y>BASE-h1-110;y-=100){X.fillStyle='#57507a';X.fillRect(L+226,y-88,128,76)}X.restore();X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+180,BASE-h1,220,h1)}
  ponTxt('BIGGEST MOVIE',L+290,BASE+62,34,CREMA,pop(t,xm));ponTxt('OPENING',L+290,BASE+106,34,CREMA,pop(t,xm+.25));
  ponTxt('$1.2',L+290,BASE-300-152,100,ORO,pop(t,x12),{g:12});ponTxt('BILLION',L+290,BASE-300-84,42,ORO,pop(t,x12+.3));ponTxt('OPENING WEEKEND',L+290,BASE-300-36,26,CREMA,pop(t,xw));
  // GTA 6: la columna del día uno
  if(h2>0){const g=X.createLinearGradient(0,BASE-948,0,BASE);g.addColorStop(0,'#ff5fa2');g.addColorStop(1,'#f39a4a');X.fillStyle=`rgba(255,95,162,${.14+.1*golpe(t,xl,1.2)})`;X.fillRect(L+654,BASE-h2-26,272,h2+26);X.fillStyle=g;X.fillRect(L+680,BASE-h2,220,h2);X.save();X.beginPath();X.rect(L+680,BASE-h2,220,h2);X.clip();const by=BASE-((t*520)%1100);X.fillStyle='rgba(255,255,255,.2)';X.fillRect(L+680,by,220,54);X.restore();X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+680,BASE-h2,220,h2);
   for(let k=1;k<=3;k++){const a=eo(seg(t,x3-.1+(k-1)*.14,x3+.15+(k-1)*.14));if(a>0){X.save();X.globalAlpha=a;X.strokeStyle=CREMA;X.lineWidth=5;X.setLineDash([18,12]);X.strokeRect(L+690,BASE-k*300+6,200,288);X.restore()}}}
  ponTxt('GTA 6',L+790,BASE+72,56,ROSA,pop(t,s6+.2));
  ponTxt('ABOUT',L+540,960,40,TEAL,pop(t,x3));ponTxt('3×',L+540,1050,130,TEAL,pop(t,x3),{g:14});
  ponTxt('$3.79',L+790,BASE-948-158,104,LUZ,pop(t,x3-.3),{g:14,gc:ORO});ponTxt('BILLION',L+790,BASE-948-86,44,ORO,pop(t,x3-.1));ponTxt('ONE DAY',L+790,BASE-948-36,30,CREMA,pop(t,xs))})}
// ---------- P06 · el marcador del dinero se apaga; queda la sala de los críticos ----------
function sala(L,t){X.fillStyle='#0d0a1c';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(190,205,255,.07)';X.beginPath();X.moveTo(L+170,960);X.lineTo(L+910,960);X.lineTo(L+1400,2100);X.lineTo(L-320,2100);X.closePath();X.fill();
 rr(L+150,500,780,470,10);X.fillStyle='#1b1a33';X.fill();X.fillStyle=`rgba(200,212,255,${.16+.03*Math.sin(t*3)})`;X.fillRect(L+170,520,740,430);X.strokeStyle='#2a2748';X.lineWidth=6;rr(L+150,500,780,470,10);X.stroke();
 [[1210,.62,9],[1400,.8,7],[1640,1.05,6]].forEach((f,j)=>{for(let i=0;i<f[2];i++){const w=150*f[1],x=L+540+(i-(f[2]-1)/2)*(w+16)-w/2;rr(x,f[0]-150*f[1],w,210*f[1],26*f[1]);X.fillStyle=['#2a0f1f','#34132a','#421836'][j];X.fill();X.strokeStyle='rgba(0,0,0,.4)';X.lineWidth=3;X.stroke();X.fillStyle='rgba(255,255,255,.04)';rr(x+12*f[1],f[0]-136*f[1],w-24*f[1],60*f[1],16*f[1]);X.fill()}})}
function p06(L,t){const c=T.c06,xm=T.x_money,xs=T.x_sure,fin=T.c07,on=1-eio(seg(t,xm-.35,xm+.05)),neg=seg(t,xm+.05,xm+.3),sale=seg(t,xs-.05,xs+.55);
 if(sale<=0){cam(L,540,1000,1.06,540,1000,()=>{escenario(L,t,1);marcadorDia(L,t,{on:on,dia:1,giro:false,num:1,bill:1,est:1});X.fillStyle=`rgba(6,4,14,${.5*(1-on)+.38*neg})`;X.fillRect(L-900,-900,2900,4200)})}
 else{cam(L,540,1100,lerp(1.1,1,eo(seg(t,xs,fin))),540,1000,()=>{sala(L,t);X.fillStyle=`rgba(6,4,14,${.88*(1-sale)})`;X.fillRect(L-900,-900,2900,4200)})}}
// ---------- P07 · caen las reseñas; 99 de 100; el mismo puntaje de hace 28 años ----------
function tarjeta(x,y,rot,s,a,i){X.save();X.globalAlpha=a;X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-142,-86,300,190);X.fillStyle=i%3?CREMA:'#e4dcc6';X.fillRect(-150,-95,300,190);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-150,-95,300,190);X.fillStyle=['#ff5fa2','#35e0d0','#ffd23f'][i%3];X.fillRect(-150,-95,300,18);X.fillStyle='rgba(28,21,48,.28)';[-40,-10,20,50].forEach((v,k)=>{rr(-124,v,(k%2?200:248),12,6);X.fill()});X.restore()}
const CAR=[];for(let i=0;i<16;i++)CAR.push([540+(rnd(i+1)-.5)*760,1010+(rnd(i+31)-.5)*880,(rnd(i+61)-.5)*1.3]);
function pila(L,t,tiempos){CAR.forEach((q,i)=>{const k=tiempos?tiempos[i]:-9,u=tiempos?eo(seg(t,k,k+.34)):1;if(u>0)tarjeta(L+q[0],q[1],q[2]+(1-u)*.6,1+(1-u)*.9,u,i)})}
function ficha99(x,y,s,col,k,sub,br){if(k<=0)return;X.save();X.translate(x,y);X.scale(s*k,s*k);X.fillStyle='rgba(0,0,0,.4)';rr(-178,-172,380,380,44);X.fill();rr(-190,-190,380,380,44);X.fillStyle=col;X.fill();trazo(LIN,5);txt('99',0,-24,230,TINTA);if(sub>0)txt('OUT OF 100',0,128,42,TINTA,{a:sub});if(br>0&&br<1){X.save();rr(-190,-190,380,380,44);X.clip();X.fillStyle='rgba(255,255,255,.35)';X.beginPath();const bx=-420+br*840;X.moveTo(bx,-190);X.lineTo(bx+90,-190);X.lineTo(bx-50,190);X.lineTo(bx-140,190);X.closePath();X.fill();X.restore()}X.restore()}
function ocarina(x,y,s,k){if(k<=0)return;X.save();X.translate(x,y);X.rotate(-.28);X.scale(s*k,s*k);X.fillStyle='rgba(0,0,0,.35)';X.beginPath();X.ellipse(8,14,150,74,0,0,7);X.fill();X.fillStyle='#b5653a';X.beginPath();X.moveTo(-150,10);X.quadraticCurveTo(-140,-78,-10,-74);X.quadraticCurveTo(130,-70,150,0);X.quadraticCurveTo(140,74,0,72);X.quadraticCurveTo(-130,76,-150,10);X.closePath();X.fill();trazo(LIN,4);
 rr(-40,-128,70,64,14);X.fill();trazo(LIN,4);X.fillStyle='rgba(255,255,255,.2)';X.beginPath();X.ellipse(-50,-36,60,14,-.1,0,7);X.fill();X.fillStyle='#3a1c10';[[-70,10,15],[-20,22,13],[34,20,15],[84,6,12],[10,-22,9],[60,-26,9]].forEach(q=>{X.beginPath();X.arc(q[0],q[1],q[2],0,7);X.fill()});X.restore()}
function p07(L,t){const c=T.c07,xl=T.x_landed,x9=T.x_99,xo=T.x_out,xs=T.x_score,x28=T.x_28,xc=T.x_oca,fin=T.c08;
 const TI=CAR.map((q,i)=>i<4?c+.25+i*.42:i<12?xl-.35+(i-4)*.2:x9-1.6+(i-12)*.35),mv=eio(seg(t,xs-.15,xs+.6)),viejo=eo(seg(t,xs+.3,xs+.9));
 cam(L,540,1000,lerp(1,1.05,seg(t,c,fin))+.03*golpe(t,x9,.25),540,1000,()=>{fieltro(L);pila(L,t,TI);
  if(mv>0){X.fillStyle=`rgba(10,8,22,${.45*mv})`;X.fillRect(L-900,-900,2900,4200)}
  ficha99(L+lerp(540,330,mv),lerp(1010,1040,mv),lerp(1.15,.82,mv),ORO,back(seg(t,x9-.08,x9+.2)),seg(t,xo-.05,xo+.15),seg(t,xo+.2,xo+1.0));
  if(viejo>0){ficha99(L+790+(1-viejo)*600,1040,.68,'#cdbf96',1,1,seg(t,xc+.15,xc+1.0));X.fillStyle='rgba(60,50,40,.12)';for(let i=0;i<5;i++){X.beginPath();X.ellipse(L+790+(1-viejo)*600-70+rnd(i+3)*150,960+rnd(i+9)*170,40,14,rnd(i)*3,0,7);X.fill()}}
  const k28=pop(t,x28);if(k28>0){X.strokeStyle=TEAL;X.lineWidth=6;X.lineJoin='round';X.beginPath();X.moveTo(L+330,1230);X.lineTo(L+330,1280);X.lineTo(L+790,1280);X.lineTo(L+790,1200);X.stroke();ponTxt('28 YEARS',L+560,1370,92,TEAL,k28,{g:12})}
  ocarina(L+790,780+Math.sin(t*3.2)*9,.9,back(seg(t,xc-.25,xc+.1)))})}
// ---------- P08 · el 99 al centro; cierre ----------
function p08(L,t){const k=T.x_tell;fieltro(L);pila(L,t,null);X.fillStyle='rgba(10,8,22,.4)';X.fillRect(L-900,-900,2900,4200);ficha99(L+430,1300+Math.sin(t*1.6)*5,.78,ORO,1,1,(t*.45)%1.6);cierreCanal(L,t,k)}

NUEVOS.dc_gtaen19_p01=SET(p01);NUEVOS.dc_gtaen19_p02=SET(p02);NUEVOS.dc_gtaen19_p03=SET(p03);NUEVOS.dc_gtaen19_p04=SET(p04);NUEVOS.dc_gtaen19_p05=SET(p05);NUEVOS.dc_gtaen19_p06=SET(p06);NUEVOS.dc_gtaen19_p07=SET(p07);NUEVOS.dc_gtaen19_p08=SET(p08);
})();
// ===== DC · GTAEN19 · FIN =====
</script>
