<script>
// ===== DC · COFFEE17 · INICIO ===== (Coffee 17h · Why Coffee Makes You RUN to the Bathroom · paquete 5 del lote del 27-nov)
// Reglas del paquete: anatomía abstracta (un tubo), nunca explícita; se distinguen café, descafeinado y agua; no le pasa a todos.
(function(){
const {LIN,K,cap,trazo,manoLado,origen,cam,cierreCanal,SET}=window.DC;
const {cocina,vapor,taza,persona,tazaArriba,mez,golpe,ruta,MANO,PIEL,PIEL2,CREMA,ACERO2,NEGRO,C_OK}=window.DC_CAFE;
const TUBO='#f39c80',TUBO2='#c96a52',FONDO='#1b2f3a',AGUA='#9fd3e6';
// ---------- piezas ----------
function tablero(L){X.fillStyle=FONDO;X.fillRect(L-2500,-1600,8000,6400);X.fillStyle='rgba(255,255,255,.03)';for(let x=-2400;x<5400;x+=120)X.fillRect(L+x,-1600,3,6400);for(let y=-1500;y<4700;y+=120)X.fillRect(L-2500,y,8000,3)}
function curva(P){const n=P.length;return q=>{const f=Math.max(0,Math.min(.9999,q))*(n-1),i=Math.floor(f),w=f-i,p0=P[Math.max(0,i-1)],p1=P[i],p2=P[i+1],p3=P[Math.min(n-1,i+2)],h=(a,b,c,d)=>.5*((2*b)+(-a+c)*w+(2*a-5*b+4*c-d)*w*w+(-a+3*b-3*c+d)*w*w*w);return [h(p0[0],p1[0],p2[0],p3[0]),h(p0[1],p1[1],p2[1],p3[1])]}}
// tubo abstracto con ondas que avanzan. act = cuánto se mueve (0 quieto … 1 fuerte)
function tubo(P,t,act,w,o){o=o||{};const cr=curva(P),N=90;X.lineCap='round';X.lineJoin='round';
 const traza=(ancho,col)=>{X.strokeStyle=col;X.lineWidth=ancho;X.beginPath();for(let i=0;i<=N;i++){const p=cr(i/N);i?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1])}X.stroke()};
 traza(w+16,'rgba(0,0,0,.25)');traza(w,TUBO2);traza(w-16,o.col||TUBO);
 if(act>0){const n=o.n||7;for(let j=0;j<n;j++){const q=((t*(o.vel||.22)+j/n)%1),p=cr(q),e=Math.sin(q*Math.PI);X.fillStyle=TUBO2;X.beginPath();X.arc(p[0],p[1],(w*.5+w*.26*act)*e+w*.1,0,7);X.fill();X.fillStyle=o.col||TUBO;X.beginPath();X.arc(p[0],p[1],Math.max(0,(w*.5+w*.26*act)*e+w*.1-8),0,7);X.fill()}}
 X.strokeStyle='rgba(255,255,255,.22)';X.lineWidth=6;X.beginPath();for(let i=0;i<=N;i++){const p=cr(i/N);i?X.lineTo(p[0]-w*.16,p[1]-w*.2):X.moveTo(p[0]-w*.16,p[1]-w*.2)}X.stroke()}
function crono(x,y,r,o){o=o||{};X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.arc(x+r*.06,y+r*.1,r,0,7);X.fill();X.fillStyle=NEGRO;rr(x-r*.16,y-r*1.24,r*.32,r*.3,r*.08);X.fill();X.save();X.translate(x+r*.74,y-r*.74);X.rotate(.78);rr(-r*.1,-r*.22,r*.2,r*.26,r*.05);X.fill();X.restore();
 X.fillStyle='#e4572e';X.beginPath();X.arc(x,y,r,0,7);X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.beginPath();X.arc(x,y,r*.82,0,7);X.fill();
 if(o.u>0){X.fillStyle='rgba(228,87,46,.38)';X.beginPath();X.moveTo(x,y);X.arc(x,y,r*.78,-Math.PI/2,-Math.PI/2+o.u*Math.PI*2);X.closePath();X.fill()}
 X.strokeStyle='#2a2019';X.lineCap='round';for(let i=0;i<12;i++){const q=i*Math.PI/6;X.lineWidth=i%3?3:6;X.beginPath();X.moveTo(x+Math.cos(q)*r*.7,y+Math.sin(q)*r*.7);X.lineTo(x+Math.cos(q)*r*.78,y+Math.sin(q)*r*.78);X.stroke()}
 if(o.txt){txt(o.txt,x,y-r*.02,r*.74,'#2a2019',{w:r*1.2,a:o.ta===undefined?1:o.ta});txt('min',x,y+r*.44,r*.24,'#7a6f66',{w:r,a:o.ta===undefined?1:o.ta})}
 else{const a=-Math.PI/2+(o.u||0)*Math.PI*2;X.strokeStyle=NEGRO;X.lineWidth=r*.05;X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(a)*r*.66,y+Math.sin(a)*r*.66);X.stroke();X.fillStyle=NEGRO;X.beginPath();X.arc(x,y,r*.08,0,7);X.fill()}}
function vaso(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(6,4,96,12,0,0,7);X.fill();X.fillStyle='rgba(159,211,230,.55)';X.beginPath();X.moveTo(-84,-150);X.lineTo(84,-150);X.lineTo(70,0);X.lineTo(-70,0);X.closePath();X.fill();
 X.fillStyle='rgba(214,236,238,.25)';X.beginPath();X.moveTo(-90,-200);X.lineTo(90,-200);X.lineTo(70,0);X.lineTo(-70,0);X.closePath();X.fill();X.strokeStyle='rgba(220,240,245,.9)';X.lineWidth=5;X.stroke();X.fillStyle='rgba(255,255,255,.5)';rr(-66,-180,12,150,6);X.fill();X.restore()}
function mesaMadera(L,y){X.fillStyle='#b98a5a';X.fillRect(L-1500,y,5200,2400);X.fillStyle='#d2a674';X.fillRect(L-1500,y,5200,16);X.fillStyle='rgba(0,0,0,.08)';for(let i=0;i<6;i++)X.fillRect(L-1500,y+60+i*70,5200,5)}
function silla(L,rot){X.save();X.translate(L+540,1500);X.rotate(rot||0);X.lineJoin='round';rr(-230,-760,460,700,50);X.fillStyle='#8a5f3f';X.fill();trazo(LIN,3);X.fillStyle='#74502f';[-110,0,110].forEach(v=>{rr(v-26,-690,52,560,20);X.fill()});X.restore()}
// ---------- P01 / P09 · la persona toma café y se levanta rápido; la taza queda en primer plano ----------
function mesaCafe(L,t,o){cocina(L);silla(L,o.sillaRot||0);
 if(o.dx<1500){X.save();X.translate(o.dx||0,o.dy||0);persona(L,t,{dx:o.tiembla||0,boca:o.boca||{},ty:o.suelta?undefined:o.ty,trot:o.trot||0,cafe:C_OK});X.restore()}
 mesaMadera(L,1600);if(o.suelta){taza(L+570,1640,1.3,{cafe:C_OK});vapor(L+570,1390,t,.7,1,5)}}
function p01(L,t){const xr=T.x_running,xi=T.x_its,xa=T.x_and1,fin=T.c02;
 const ty=ruta(t,[[0,952],[.75,946],[xr+.05,1640]])[0],suelta=t>=xr+.05,sale=Math.pow(seg(t,xi-.05,xi+.75),2);
 const m=eio(seg(t,xr+.05,xr+.3))*(1-seg(t,xi+.2,xi+.5));
 const cm=ruta(t,[[0,540,1000,1],[xa-.1,540,1000,1.03],[fin,570,1500,1.35]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>mesaCafe(L,t,{ty,trot:-.28*(1-eio(seg(t,.6,1.0))),suelta,boca:{m:m*.8},tiembla:8*Math.sin(t*22)*m,dx:sale*1700,dy:-150*Math.sin(Math.min(1,sale*2.2)*1.57),sillaRot:.07*Math.sin((t-xi)*11)*Math.exp(-Math.max(0,t-xi)*1.6)*(t>xi?1:0)}))}
function p09(L,t){const c=T.c09,xg=T.x_gut12,k=T.x_tell;
 const ty=ruta(t,[[c,1330],[c+.4,952],[c+.9,946],[xg-.15,1640]])[0],suelta=t>=xg-.15,sale=Math.pow(seg(t,xg+.2,xg+1.0),2);
 const cm=ruta(t,[[c,540,1000,1,540,1000],[k-.3,540,1000,1.02,540,1000],[k+.5,570,1640,1.05,450,1420]]);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>mesaCafe(L,t,{ty,trot:-.28*golpe(t,c+.2,.9),suelta,boca:{s:.5*seg(t,c+.9,c+1.2)},dx:sale*1700,dy:-150*Math.sin(Math.min(1,sale*2.2)*1.57),sillaRot:.06*Math.sin((t-xg)*11)*Math.exp(-Math.max(0,t-xg-.2)*1.6)*(t>xg+.2?1:0)}));
 cierreCanal(L,t,k)}
// ---------- P02 · la primera taza de la mañana; la mirada se va al pasillo ----------
function p02(L,t){const c=T.c02,xr=T.x_right2,xf=T.x_first,fin=T.c03a;
 const toma=eio(seg(t,xr-.3,xr+.1)),sube=eio(seg(t,xr+.15,xf+.2)),cx=lerp(430,900,eio(seg(t,xf-.2,fin)));
 cam(L,cx,1050,1.08,540,1000,()=>{cocina(L);
  // ventana con la mañana
  X.fillStyle='#14262e';X.fillRect(L+40,450,500,640);const a=X.createLinearGradient(0,470,0,1070);a.addColorStop(0,'#7fb7d9');a.addColorStop(.6,'#f6c98a');a.addColorStop(1,'#f9e2a8');X.fillStyle=a;X.fillRect(L+62,472,456,596);X.fillStyle='#fff3c4';X.beginPath();X.arc(L+380,900,74,0,7);X.fill();X.fillStyle='#14262e';X.fillRect(L+280,472,18,596);X.fillRect(L+62,760,456,16);
  X.fillStyle='rgba(255,236,170,.10)';X.beginPath();X.moveTo(L+62,1068);X.lineTo(L+518,1068);X.lineTo(L+760,1380);X.lineTo(L+120,1380);X.closePath();X.fill();
  // pasillo con la puerta del fondo entreabierta
  X.fillStyle='#101d24';X.fillRect(L+980,430,520,950);X.fillStyle='#0b151a';X.beginPath();X.moveTo(L+980,430);X.lineTo(L+1500,430);X.lineTo(L+1380,560);X.lineTo(L+1100,560);X.closePath();X.fill();
  X.fillStyle='#ffe9b0';X.fillRect(L+1170,640,150,620);X.fillStyle='#d9c9a8';X.beginPath();X.moveTo(L+1170,640);X.lineTo(L+1250,668);X.lineTo(L+1250,1290);X.lineTo(L+1170,1260);X.closePath();X.fill();trazo(LIN,3);X.fillStyle='#e9c46a';X.beginPath();X.arc(L+1236,960,10,0,7);X.fill();
  X.fillStyle='rgba(255,233,176,.16)';X.beginPath();X.moveTo(L+1250,1280);X.lineTo(L+1320,1260);X.lineTo(L+1500,1380);X.lineTo(L+1100,1380);X.closePath();X.fill();
  const my=1380-sube*1100,hx=L+430+150,hy=lerp(700,my-150,toma),o=origen(hx,hy,-1.15,1.3,-1,118,44),m=p=>manoLado(o[0],o[1],-1.15,1.3,-1,Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.35,parte:p}));
  if(toma>0)m('atras');taza(L+430,my,1.3,{cafe:C_OK,sinSombra:sube>.05});if(toma>0)m('pulgar');vapor(L+430,my-250,t,.8,1,6)})}
// ---------- P03 · 1990: la mesa del experimento (cenital) y el voluntario parcial con el sensor (lateral) ----------
function p03a(L,t){const c=T.c03a,xr=T.x_res,xt=T.x_tested;
 X.fillStyle='#3d4a52';X.fillRect(L-400,-500,1900,2900);X.fillStyle='rgba(255,255,255,.03)';for(let i=0;i<50;i++){X.beginPath();X.arc(L-300+rnd(i)*1700,-200+rnd(i+77)*2400,10+rnd(i+5)*26,0,7);X.fill()}
 const cae=back(seg(t,c+.08,c+.5));X.save();X.translate(L+300,640);X.rotate(-.06);X.fillStyle='rgba(0,0,0,.28)';rr(-176,-136,370,300,18);X.fill();rr(-185,-150,370,300,18);X.fillStyle='#fbf7ec';X.fill();trazo(LIN,3);X.save();rr(-185,-150,370,300,18);X.clip();X.fillStyle='#c0392b';X.fillRect(-185,-150,370,66);X.restore();X.fillStyle='#f2efe6';[-90,90].forEach(v=>{X.beginPath();X.arc(v,-117,13,0,7);X.fill()});X.save();X.translate(0,44);X.scale(1,Math.max(.02,cae));txt('1990',0,0,132,'#2a2019',{w:340});X.restore();X.restore();
 // registrador con su tira de papel
 const en=eio(seg(t,xr-.15,xr+.5)),px=L+560+(1-en)*800;X.fillStyle='rgba(0,0,0,.3)';rr(px+12,1016,430,330,30);X.fill();rr(px,1000,430,330,30);X.fillStyle='#55666f';X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.fillRect(px+40,1050,350,150);X.strokeStyle='#c0392b';X.lineWidth=5;X.beginPath();for(let i=0;i<=34;i++){const y=1125+Math.sin(i*.9+t*3)*5;i?X.lineTo(px+46+i*10,y):X.moveTo(px+46+i*10,y)}X.stroke();X.fillStyle='#7CFC8A';X.beginPath();X.arc(px+70,1270,14,0,7);X.fill();X.fillStyle='#2c3a33';[130,190,250].forEach(v=>{X.beginPath();X.arc(px+v,1270,14,0,7);X.fill()});
 // cable con el sensor
 X.strokeStyle='#22262b';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(px+40,1300);X.bezierCurveTo(px-200,1380,px-120,1560,px-300,1520);X.stroke();X.fillStyle='#e9e2d2';X.beginPath();X.arc(px-300,1520,40,0,7);X.fill();trazo(LIN,3);X.fillStyle='#e4572e';X.beginPath();X.arc(px-300,1520,12,0,7);X.fill();
 const ta=eio(seg(t,xt-.25,xt+.15));if(ta>0){X.save();X.translate(0,(1-ta)*-900);tazaArriba(L+770,640);X.restore();X.fillStyle=C_OK;X.beginPath();X.arc(L+770,640-(1-ta)*900,96,0,7);X.fill()}}
function p03b(L,t){const c=T.c03b,xs=T.x_sensors,xg=T.x_gave;
 cam(L,540,1060,lerp(1,1.06,seg(t,c,T.c04)),540,1000,()=>{cocina(L);X.lineJoin='round';
  // silla y voluntario parcial (del pecho a las rodillas), de lado
  X.fillStyle='#5b4634';X.fillRect(L+70,700,44,700);rr(L+70,1290,480,54,20);X.fillStyle='#7c9aa8';X.fill();trazo(LIN,3);X.fillStyle='#5b4634';X.fillRect(L+500,1340,36,300);X.fillRect(L+90,1340,36,300);
  X.fillStyle='#3f4f6b';X.beginPath();X.moveTo(L+150,1180);X.lineTo(L+600,1150);X.quadraticCurveTo(L+680,1160,L+676,1240);X.lineTo(L+660,1700);X.lineTo(L+540,1700);X.lineTo(L+540,1300);X.lineTo(L+150,1300);X.closePath();X.fill();trazo(LIN,3);
  X.fillStyle='#6f8496';X.beginPath();X.moveTo(L+120,-400);X.quadraticCurveTo(L+104,700,L+140,1200);X.lineTo(L+470,1196);X.quadraticCurveTo(L+520,1000,L+470,760);X.quadraticCurveTo(L+430,420,L+480,-400);X.closePath();X.fill();trazo(LIN,3);
  X.fillStyle='#6f8496';cap(L+300,420,L+420,960,62);X.fill();trazo(LIN,3);X.fillStyle=PIEL2;cap(L+420,960,L+590,1090,44);X.fill();trazo(LIN,3);X.fillStyle=PIEL;X.beginPath();X.ellipse(L+626,1104,50,40,.3,0,7);X.fill();trazo(LIN,3);
  // sensor simplificado en el abdomen bajo, con su cable al registrador
  const s=back(seg(t,xs-.2,xs+.2));if(s>0){X.strokeStyle='#22262b';X.lineWidth=9;X.lineCap='round';X.beginPath();X.moveTo(L+476,1118);X.bezierCurveTo(L+620,1260,L+760,1420,L+880,1300);X.stroke();X.save();X.translate(L+470,1112);X.scale(s,s);X.fillStyle='#e9e2d2';X.beginPath();X.arc(0,0,40,0,7);X.fill();trazo(LIN,3);X.fillStyle=((t*2)%1<.5)?'#e4572e':'#8a3d33';X.beginPath();X.arc(0,0,13,0,7);X.fill();X.restore()}
  // mesa con el registrador y la taza que le dan
  rr(L+720,1200,560,40,14);X.fillStyle='#b98a5a';X.fill();trazo(LIN,3);X.fillStyle='#8f6b45';X.fillRect(L+770,1240,36,400);
  rr(L+850,1030,230,170,22);X.fillStyle='#55666f';X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.fillRect(L+872,1056,186,84);X.strokeStyle='#c0392b';X.lineWidth=4;X.beginPath();for(let i=0;i<=18;i++){const y=1098+Math.sin(i*.9+t*3)*3;i?X.lineTo(L+876+i*10,y):X.moveTo(L+876+i*10,y)}X.stroke();
  const d=eio(seg(t,xg-.3,xg+.2));if(d>0){const tx=L+790,ty=1200-(1-d)*300,hx=tx+110,hy=ty-160,o=origen(hx,hy,-1.2,1.1,-1,118,44),sv=eio(seg(t,xg+.3,xg+.9));
   if(sv<1){manoLado(o[0]+sv*400,o[1]-sv*700,-1.2,1.1,-1,Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'atras'}))}taza(tx,ty,.95,{cafe:C_OK,asa:-1});if(sv<1)manoLado(o[0]+sv*400,o[1]-sv*700,-1.2,1.1,-1,Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'pulgar'}));vapor(tx,ty-190,t,.6*d,.8,5)}})}
// ---------- P04 · a los cuatro minutos el tubo empieza a moverse; sigue media hora ----------
const LARGO=[[-500,1150],[-150,1000],[250,1220],[640,1010],[1040,1230],[1440,1010],[1840,1220],[2240,1030],[2700,1160]];
function p04(L,t){const c=T.c04,xm=T.x_moving,x4=T.x_four,xa=T.x_and5,xh=T.x_half;
 const act=eio(seg(t,xm-.1,xm+.6)),cx=lerp(540,1500,eio(seg(t,xa-.1,T.c05a)));
 cam(L,cx,1000,lerp(1.07,1,eio(seg(t,c,xm+.3))),540,1000,()=>{tablero(L);tubo(LARGO.map(p=>[L+p[0],p[1]]),t,act,120,{n:9,vel:.16})});
 const u=t<xa?seg(t,c+.3,x4)*.133:lerp(.133,.5,eio(seg(t,xa,xh+.4)));
 crono(L+540,600,150,{u,txt:t>x4-.08&&t<xa+.3?'4':null,ta:1})}
// ---------- P05 · lo mismo con agua caliente: el reloj corre y el tubo no se mueve ----------
function p05a(L,t){tablero(L);taza(L+540,1320,2.2,{cafe:C_OK});vapor(L+540,900,t,.9,1.6,7)}
function p05b(L,t){cam(L,540,1000,lerp(1,1.06,eio(seg(t,T.x_nothing,T.c06))),540,1000,()=>p05b_(L,t))}
function p05b_(L,t){const c=T.c05b,xn=T.x_nothing,xs=T.x_so6;
 const cm=ruta(t,[[c,540,1100,1,540,1100],[c+1.3,300,1000,.55,300,820],[T.c06,300,1000,.6,300,820]]);
 tablero(L);tubo([[L-200,1380],[L+200,1300],[L+540,1420],[L+880,1300],[L+1280,1380]],t,0,110,{});
 X.save();X.translate(L+cm[3],cm[4]);X.scale(cm[2],cm[2]);X.translate(-(L+cm[0]),-cm[1]);taza(L+540,1320,2.2,{cafe:AGUA});vapor(L+540,900,t,.9,1.6,7);X.restore();
 const en=back(seg(t,c+1.0,c+1.4));if(en>0){X.save();X.translate(L+760,760);X.scale(en,en);crono(0,0,170,{u:seg(t,c+1.4,xn+.3)});X.restore()}}
// ---------- P06 · tres columnas: café, descafeinado y agua ----------
function columna(L,x,t,act,en,tipo){if(en<=0)return;X.save();X.translate(0,(1-en)*-1300);
 if(tipo===2)vaso(L+x,820,1.05);else{taza(L+x,820,.95,{cafe:tipo?'#6b4a34':C_OK,banda:tipo?'#3f9a46':'#c8553d'});if(tipo===1)txt('DECAF',L+x,820-114,24,'#fff',{w:180})}
 vapor(L+x,640,t,.5,.8,4);X.restore();
 X.globalAlpha=en;tubo([[L+x,900],[L+x-70,1040],[L+x+70,1200],[L+x-70,1360],[L+x,1520]],t,act,70,{n:5,vel:.3});X.globalAlpha=1}
function p06(L,t){const c=T.c06,xd=T.x_decaf,xl=T.x_less,xw=T.x_water8;
 tablero(L);[1,2].forEach(i=>{X.fillStyle='rgba(255,255,255,.08)';X.fillRect(L+i*360-3,470,6,1140)});
 columna(L,180,t,eio(seg(t,xl+.2,xl+.8)),eio(seg(t,c+.1,c+.6)),0);
 columna(L,540,t,.5*eio(seg(t,xd-.05,xd+.5)),eio(seg(t,c+.9,c+1.4)),1);
 columna(L,900,t,0,eio(seg(t,c+1.7,c+2.2)),2);
 const q=golpe(t,xw-.1,.7);if(q>0){X.strokeStyle=`rgba(159,211,230,${.8*q})`;X.lineWidth=8;rr(L+760,560,280,1010,30);X.stroke()}}
// ---------- P07 · la ficha "gastrin" manda una señal que recorre el tubo ----------
function ficha(x,y,r,enc){X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.arc(x+6,y+9,r,0,7);X.fill();if(enc>0){X.fillStyle=`rgba(255,214,120,${.28*enc})`;X.beginPath();X.arc(x,y,r*(1.25+.08*Math.sin(enc*20)),0,7);X.fill()}
 X.fillStyle=mez('#55666f','#f2c21a',enc);X.beginPath();X.arc(x,y,r,0,7);X.fill();trazo(LIN,3);X.fillStyle=mez('#3d4a52','#fbe9a8',enc);X.beginPath();X.arc(x,y,r*.8,0,7);X.fill();txt('gastrin',x,y+2,r*.38,mez('#aab4ba','#2a2019',enc),{w:r*1.5})}
const LARGO7=[[420,1180],[700,1320],[1000,1140],[1300,1330],[1600,1150],[1900,1330],[2200,1160],[2500,1320],[2900,1200]];
function pulso(P,t,k,dur){const u=seg(t,k,k+dur);if(u<=0||u>=1)return;const p=curva(P)(u);X.fillStyle='rgba(255,214,120,.35)';X.beginPath();X.arc(p[0],p[1],64,0,7);X.fill();X.fillStyle='#ffe9a8';X.beginPath();X.arc(p[0],p[1],30,0,7);X.fill()}
function p07(L,t){const c=T.c07,xg=T.x_gastrin,xe=T.x_even,x2=T.x_gastrin2,xs=T.x_same,xc=T.x_eat,P=LARGO7.map(p=>[L+p[0],p[1]]);
 const enc=eio(seg(t,xg-.08,xg+.25)),enc2=eio(seg(t,xs+.5,xs+.8));
 const cm=ruta(t,[[c,330,1040,1.35],[xg+.4,330,1040,1.35],[x2,460,1080,1.05],[xs,1250,1120,1],[T.c08,1700,1120,1]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{tablero(L);
  tubo(P,t,eio(seg(t,x2+.5,x2+1.4)),110,{n:9,vel:.16});
  taza(L+150,900,1.05,{cafe:C_OK});vapor(L+150,700,t,.6,.9,5);const d=eio(seg(t,xe-.1,xe+.35));if(d>0){X.save();X.translate((1-d)*-700,0);taza(L+150,1180,.9,{cafe:'#6b4a34',banda:'#3f9a46'});txt('DECAF',L+150,1180-108,23,'#fff',{w:180});X.restore()}
  X.strokeStyle='rgba(255,255,255,.25)';X.lineWidth=8;X.setLineDash([4,22]);X.lineCap='round';X.beginPath();X.moveTo(L+250,960);X.lineTo(L+320,1040);X.stroke();X.setLineDash([]);
  ficha(L+420,1100,112,enc);pulso(P,t,x2+.25,2.6);
  // después de comer: la misma ficha, la misma señal
  const pl=eio(seg(t,xs-.2,xs+.3));if(pl>0){X.save();X.translate(0,(1-pl)*-900);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(L+1620,820,190,34,0,0,7);X.fill();X.fillStyle='#f4f1e8';X.beginPath();X.ellipse(L+1610,800,190,40,0,0,7);X.fill();trazo(LIN,3);X.fillStyle='#e9e2d2';X.beginPath();X.ellipse(L+1610,796,140,26,0,0,7);X.fill();
   X.fillStyle='#d9a441';rr(L+1500,720,150,70,16);X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.beginPath();X.ellipse(L+1690,770,60,24,0,0,7);X.fill();trazo(LIN,3);X.fillStyle='#f2c21a';X.beginPath();X.arc(L+1690,766,20,0,7);X.fill();X.restore();
   X.strokeStyle='rgba(255,255,255,.25)';X.lineWidth=8;X.setLineDash([4,22]);X.beginPath();X.moveTo(L+1620,880);X.lineTo(L+1620,980);X.stroke();X.setLineDash([]);
   ficha(L+1620,1100,112,enc2);pulso(P.slice(4),t,xs+.8,2.2)}})}
// ---------- P08 · tres de cada diez; más en mujeres que en hombres (comparación agregada, sin cifras) ----------
function figura(x,y,s,col){X.fillStyle=col;X.beginPath();X.arc(x,y-150*s,46*s,0,7);X.fill();X.beginPath();X.moveTo(x-70*s,y+90*s);X.quadraticCurveTo(x-76*s,y-90*s,x,y-92*s);X.quadraticCurveTo(x+76*s,y-90*s,x+70*s,y+90*s);X.closePath();X.fill()}
function simbolo(x,y,r,f){X.strokeStyle='#e9e2d2';X.lineWidth=r*.26;X.lineCap='round';X.beginPath();X.arc(x,y,r,0,7);X.stroke();X.beginPath();if(f){X.moveTo(x,y+r);X.lineTo(x,y+r*2.3);X.moveTo(x-r*.7,y+r*1.7);X.lineTo(x+r*.7,y+r*1.7)}else{X.moveTo(x+r*.7,y-r*.7);X.lineTo(x+r*1.7,y-r*1.7);X.moveTo(x+r*.8,y-r*1.7);X.lineTo(x+r*1.7,y-r*1.7);X.lineTo(x+r*1.7,y-r*.8)}X.stroke()}
function p08(L,t){const c=T.c08,x3=T.x_three,xw=T.x_women;tablero(L);
 for(let i=0;i<10;i++){const x=L+150+(i%5)*195,y=760+Math.floor(i/5)*330,idx=[1,3,7].indexOf(i),q=idx<0?0:eio(seg(t,x3-.1+idx*.2,x3+.15+idx*.2)),en=back(seg(t,c+.05+i*.05,c+.35+i*.05));
  if(en>0){X.save();X.translate(x,y);X.scale(en,en);if(q>0){X.fillStyle=`rgba(243,156,128,${.25*q})`;X.beginPath();X.arc(0,-40,150,0,7);X.fill()}figura(0,0,1,mez('#56707d','#f39c80',q));X.restore()}}
 const b=eio(seg(t,xw-.15,xw+.5));if(b>0){X.globalAlpha=Math.min(1,b*2);simbolo(L+210,1400,30,true);simbolo(L+204,1560,30,false);X.globalAlpha=1;
  X.fillStyle='rgba(255,255,255,.10)';rr(L+290,1372,640,56,28);X.fill();rr(L+290,1512,640,56,28);X.fill();X.fillStyle='#f39c80';rr(L+290,1372,Math.max(56,560*b),56,28);X.fill();rr(L+290,1512,Math.max(56,200*b),56,28);X.fill()}}

NUEVOS.dc_coffee17_p01=SET(p01);NUEVOS.dc_coffee17_p02=SET(p02);NUEVOS.dc_coffee17_p03a=SET(p03a);NUEVOS.dc_coffee17_p03b=SET(p03b);NUEVOS.dc_coffee17_p04=SET(p04);NUEVOS.dc_coffee17_p05a=SET(p05a);
NUEVOS.dc_coffee17_p05b=SET(p05b);NUEVOS.dc_coffee17_p06=SET(p06);NUEVOS.dc_coffee17_p07=SET(p07);NUEVOS.dc_coffee17_p08=SET(p08);NUEVOS.dc_coffee17_p09=SET(p09);
})();
// ===== DC · COFFEE17 · FIN =====
</script>
