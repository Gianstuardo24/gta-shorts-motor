<script>
// ===== DC · GTAEN14 · INICIO ===== (GTA EN 14h · GTA 6 Was HIDING in Another Game · paquete 10 del lote del 27-nov)
// Reglas del paquete: no se afirma que fue una pista confirmada; sin interfaces ni logos; el nombre va pintado en el casco, dentro del mundo del juego.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const CREMA='#e8dcc0',ROJO='#6a2f2c',TINTA='#2a2019',SUNX=760,MANGA={manga:'#3a3044',puno:'#3a3044'};
function caja(x,y,w,h,col){X.fillStyle=col;X.fillRect(x,y,w,h);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(x,y,w,h)}
// ---------- el mundo western: cielo de atardecer, mesetas, río ----------
function mesas(L,dx,col,base,alt,sem){X.fillStyle=col;X.beginPath();X.moveTo(L-4000,base);for(let i=-9;i<14;i++){const x=L+i*460+dx+rnd(i+sem+50)*140,w=170+rnd(i+sem+69)*190,h=alt*(.45+rnd(i+sem+80)*.6);X.lineTo(x,base);X.lineTo(x+26,base-h);X.lineTo(x+w,base-h);X.lineTo(x+w+34,base)}X.lineTo(L+5000,base);X.lineTo(L+5000,base+60);X.lineTo(L-4000,base+60);X.closePath();X.fill()}
function agua(L,t,off){const g=X.createLinearGradient(0,1150,0,2000);g.addColorStop(0,'#6a3d57');g.addColorStop(.2,'#39305a');g.addColorStop(1,'#141a33');X.fillStyle=g;X.fillRect(L-4000,1150,9000,4000);
 for(let i=0;i<10;i++){const y=1166+i*46,w=250-i*17+Math.sin(t*1.6+i*1.3)*26;X.fillStyle=`rgba(246,186,104,${.55-i*.05})`;rr(L+SUNX-w/2,y,w,9,4.5);X.fill()}
 X.lineCap='round';X.lineWidth=4;for(let i=0;i<46;i++){const y=1180+rnd(i+7)*1000,v=.4+(y-1150)/700,x=(((rnd(i+60)*3600-off*v+Math.sin(t+i)*8)%3600)+3600)%3600-1200,w=36+rnd(i+90)*120;X.strokeStyle=`rgba(255,214,170,${.08+rnd(i+33)*.1})`;X.beginPath();X.moveTo(L+x,y);X.lineTo(L+x+w,y);X.stroke()}}
function mundo(L,t,off){const g=X.createLinearGradient(0,-300,0,1160);g.addColorStop(0,'#17142b');g.addColorStop(.45,'#2f2145');g.addColorStop(.72,'#7d3a4f');g.addColorStop(.9,'#d46f3f');g.addColorStop(1,'#f4b25e');X.fillStyle=g;X.fillRect(L-4000,-3000,9000,7000);
 X.fillStyle='rgba(255,214,140,.25)';X.beginPath();X.arc(L+SUNX,1085,210,0,7);X.fill();X.fillStyle='#ffd98a';X.beginPath();X.arc(L+SUNX,1085,120,0,7);X.fill();
 mesas(L,-off*.12,'#5a2f4d',1150,300,3);mesas(L,-off*.3,'#3a2140',1150,170,40);agua(L,t,off)}
// ---------- el barco de río ----------
function barco(x,y,s,t,o){o=o||{};X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 {const g=X.createLinearGradient(0,0,0,230);g.addColorStop(0,'rgba(40,18,34,.6)');g.addColorStop(1,'rgba(40,18,34,0)');X.fillStyle=g;X.fillRect(-450,0,920,230);for(let i=0;i<8;i++){X.fillStyle=`rgba(255,210,122,${.2+.08*Math.sin(t*3+i)})`;rr(-366+i*82+Math.sin(t*2+i)*5,46+(i%3)*30,40,8,4);X.fill()}}
 for(let i=0;i<7;i++){const u=(t*.3+i/7)%1,sx=250-u*520,sy=-650-u*170-Math.sin(u*6+i)*16;X.fillStyle=`rgba(30,24,44,${.5*(1-u)})`;X.beginPath();X.arc(sx,sy,22+u*64,0,7);X.fill()}
 X.save();X.translate(-470,-96);X.strokeStyle='#8a4636';X.lineWidth=14;X.beginPath();X.arc(0,0,128,0,7);X.stroke();X.lineWidth=9;for(let k=0;k<8;k++){const a=t*1.8+k*Math.PI/4;X.beginPath();X.moveTo(0,0);X.lineTo(Math.cos(a)*128,Math.sin(a)*128);X.stroke();X.save();X.translate(Math.cos(a)*128,Math.sin(a)*128);X.rotate(a);X.fillStyle='#a85a40';X.fillRect(-8,-26,16,52);X.restore()}X.fillStyle='#3a2028';X.beginPath();X.arc(0,0,20,0,7);X.fill();X.restore();
 X.fillStyle='#1c1626';[215,272].forEach(v=>{X.fillRect(v,-650,30,210);X.fillRect(v-6,-660,42,16)});
 X.fillRect(56,-620,6,80);X.fillStyle='#c8553d';X.beginPath();X.moveTo(56,-620);X.lineTo(-4+Math.sin(t*4)*6,-604);X.lineTo(56,-588);X.closePath();X.fill();
 caja(40,-540,160,92,'#6c4a52');X.fillStyle='#ffd27a';X.fillRect(62,-518,46,40);X.fillRect(126,-518,46,40);X.fillStyle='#3a2530';X.fillRect(24,-552,192,14);
 caja(-330,-450,560,116,'#74505a');for(let i=0;i<7;i++){X.fillStyle=(i*5+2)%3?'#ffd27a':'#3a2836';X.fillRect(-304+i*76,-426,40,54)}
 X.fillStyle='#3a2530';X.fillRect(-392,-336,716,14);
 caja(-400,-322,690,152,'#80585c');for(let i=0;i<8;i++){X.fillStyle=(i*3+1)%4?'#ffd27a':'#3a2836';X.fillRect(-372+i*82,-244,44,58)}
 X.strokeStyle='#c9b48a';X.lineWidth=5;X.beginPath();X.moveTo(-440,-200);X.lineTo(440,-200);X.stroke();for(let i=0;i<23;i++){X.beginPath();X.moveTo(-440+i*40,-200);X.lineTo(-440+i*40,-170);X.stroke()}
 X.beginPath();X.moveTo(-460,-170);X.lineTo(440,-170);X.lineTo(500,-186);X.lineTo(462,0);X.lineTo(-444,0);X.closePath();X.fillStyle=ROJO;X.fill();trazo(LIN,3);
 X.save();X.clip();X.fillStyle='#c9b48a';X.fillRect(-470,-190,990,36);X.fillStyle='#231722';X.fillRect(-470,-26,990,30);X.strokeStyle='rgba(0,0,0,.28)';X.lineWidth=3;[-118,-76].forEach(v=>{X.beginPath();X.moveTo(-470,v);X.lineTo(520,v);X.stroke()});
 if(o.det)for(let i=0;i<60;i++){X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(-450+i*16.3,-140+(i%3)*42,2.2,0,7);X.fill()}
 if(o.mugre){for(let i=0;i<22;i++){const gx=150+rnd(i+21)*270,gy=-132+rnd(i+41)*84;X.fillStyle=i%2?'rgba(40,28,32,.82)':'rgba(58,38,36,.8)';X.beginPath();X.ellipse(gx,gy,34+rnd(i+2)*52,7+rnd(i+6)*9,(rnd(i)-.5)*.25,0,7);X.fill()}
  X.strokeStyle='rgba(40,28,32,.6)';X.lineWidth=6;X.lineCap='round';for(let i=0;i<6;i++){const gx=170+i*46;X.beginPath();X.moveTo(gx,-60);X.lineTo(gx+4,-42+rnd(i+90)*30);X.stroke()}}
 X.restore();
 if(o.mugre){X.strokeStyle='#b89a6a';X.lineWidth=6;X.beginPath();X.moveTo(300,-176);X.lineTo(300,-120);X.stroke();X.fillStyle='#b89a6a';X.beginPath();X.ellipse(300,-92,22,34,0,0,7);X.fill();trazo(LIN,2)}
 X.restore()}
// ---------- P01 · el barco cruza el río; la cámara pasa junto al casco sin revelar el nombre ----------
function p01(L,t){const xa=T.x_and,xb=T.x_but,fin=T.c02,off=t*150;
 const cm=ruta(t,[[0,500,1010,.92],[xa-.45,500,1010,.96],[xa+.5,330,1300,2.5],[xb+.3,620,1268,3],[fin,880,1268,3]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{mundo(L,t,off);barco(L+540,1320+Math.sin(t*1.7)*4,1,t,{det:1,mugre:1})})}
// ---------- P02 · la misma escena, fechada: 2018 ----------
function calen(x,y,s,anio,pop){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';rr(-182,-132,380,290,16);X.fill();rr(-190,-140,380,290,16);X.fillStyle='#efe6d0';X.fill();trazo(LIN,3);X.save();rr(-190,-140,380,290,16);X.clip();X.fillStyle='#b8402e';X.fillRect(-190,-140,380,70);X.restore();X.fillStyle=TINTA;[-90,90].forEach(v=>{X.beginPath();X.arc(v,-140,12,0,7);X.fill()});
 if(pop>0){X.save();X.translate(0,44);X.scale(pop,pop);txt(String(anio),0,0,118,TINTA);X.restore()}X.restore()}
function mando(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#d9a783';[-1,1].forEach(d=>{cap(d*250,40,d*330,360,74);X.fill();trazo(LIN,3)});
 X.fillStyle='#22202e';X.beginPath();X.moveTo(-250,-60);X.quadraticCurveTo(0,-100,250,-60);X.quadraticCurveTo(320,-40,330,90);X.quadraticCurveTo(330,190,260,180);X.quadraticCurveTo(200,170,170,90);X.lineTo(-170,90);X.quadraticCurveTo(-200,170,-260,180);X.quadraticCurveTo(-330,190,-330,90);X.quadraticCurveTo(-320,-40,-250,-60);X.closePath();X.fill();trazo(LIN,3);
 [-110,110].forEach((v,i)=>{X.fillStyle='#14121c';X.beginPath();X.arc(v,40,46,0,7);X.fill();X.fillStyle='#3a3750';X.beginPath();X.arc(v+Math.sin(t*2+i)*8,40+Math.cos(t*1.7+i)*6,30,0,7);X.fill()});
 X.fillStyle='#4a4760';[[-230,0],[-196,-30],[-196,30],[-162,0],[230,0],[196,-30],[196,30],[162,0]].forEach(q=>{X.beginPath();X.arc(q[0],q[1]-10,13,0,7);X.fill()});
 X.fillStyle='#d9a783';[-1,1].forEach((d,i)=>{cap(d*250,130,d*118+Math.sin(t*2+(d>0?1:0))*8,46+Math.cos(t*1.7+(d>0?1:0))*6,30);X.fill();trazo(LIN,3)});X.restore()}
function p02(L,t){const c=T.c02,x8=T.x_2018,fin=T.c03,u=seg(t,c,fin),off=t*150;
 cam(L,540,1000,lerp(1.12,1,eo(seg(t,c,c+1.1))),540,1000,()=>{X.fillStyle='#1d1a2b';X.fillRect(L-900,-900,2900,4200);
  X.fillStyle='rgba(244,178,94,.05)';X.beginPath();X.ellipse(L+540,960,760,560,0,0,7);X.fill();X.fillStyle='#13111d';X.fillRect(L-900,1500,2900,2600);
  X.fillStyle='#3a2a2e';rr(L+40,1300,1000,170,12);X.fill();trazo(LIN,3);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L+40,1380,1000,6);
  X.fillStyle='#0b0a11';X.fillRect(L+470,1256,140,48);rr(L+62,676,956,586,20);X.fill();trazo(LIN,3);
  X.save();X.beginPath();X.rect(L+86,700,908,512);X.clip();X.translate(L+540,956);X.scale(.72,.72);X.translate(-(L+540),-1110);mundo(L,t,off);barco(L+lerp(300,760,u),1320+Math.sin(t*1.7)*4,.82,t,{mugre:1});X.restore();
  X.fillStyle='rgba(255,255,255,.04)';X.beginPath();X.moveTo(L+86,700);X.lineTo(L+420,700);X.lineTo(L+250,1212);X.lineTo(L+86,1212);X.closePath();X.fill();
  calen(L+250,560,.62,2018,back(seg(t,x8-.12,x8+.15)));mando(L+540,1650,1,t)})}
// ---------- P03 · un farol recorre el casco; bajo la mugre aparece una marca ----------
function tablones(L){X.fillStyle=ROJO;X.fillRect(L-900,-900,2900,4200);for(let i=-6;i<22;i++){const y=i*150;X.fillStyle=i%2?'rgba(0,0,0,.07)':'rgba(255,255,255,.03)';X.fillRect(L-900,y,2900,150);X.fillStyle='rgba(0,0,0,.4)';X.fillRect(L-900,y,2900,6);
  X.strokeStyle='rgba(0,0,0,.12)';X.lineWidth=3;for(let k=0;k<5;k++){const x0=L-900+rnd(i*7+k+400)*2700,w=120+rnd(i*5+k+500)*300;X.beginPath();X.moveTo(x0,y+30+k*22);X.quadraticCurveTo(x0+w/2,y+24+k*22+rnd(k+i+600)*14,x0+w,y+30+k*22);X.stroke()}
  for(let x=-880+(((i%2)+2)%2)*190;x<2000;x+=380){X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.arc(L+x,y+24,6,0,7);X.fill();X.beginPath();X.arc(L+x,y+128,6,0,7);X.fill()}}}
function marcaTenue(cx,cy,a){X.save();X.translate(cx,cy);if(a>0){txt('THE',0,-95,60,CREMA,{a:a});txt('LEONIDA',0,30,110,CREMA,{a:a})}
 for(let i=0;i<34;i++){const x=-300+rnd(i+11)*600,y=-140+rnd(i+71)*260;X.fillStyle=i%3?'rgba(100,44,42,.93)':'rgba(72,36,38,.9)';X.beginPath();X.ellipse(x,y,26+rnd(i+5)*46,12+rnd(i+9)*20,rnd(i)*3,0,7);X.fill()}X.restore()}
function farol(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle='#1c1626';X.lineWidth=8;X.beginPath();X.arc(0,-104,54,Math.PI*1.05,Math.PI*1.95);X.stroke();X.fillStyle='#1c1626';rr(-50,-110,100,26,8);X.fill();rr(-58,70,116,30,8);X.fill();
 X.fillStyle='rgba(255,214,140,.92)';rr(-44,-84,88,154,10);X.fill();X.fillStyle='#fff3c4';X.beginPath();X.ellipse(0,10+Math.sin(t*9)*3,16,34+Math.sin(t*13)*4,0,0,7);X.fill();X.strokeStyle='#1c1626';X.lineWidth=6;[-44,0,44].forEach(v=>{X.beginPath();X.moveTo(v,-84);X.lineTo(v,70);X.stroke()});X.restore()}
function p03(L,t){const c=T.c03,xd=T.x_dig,xf=T.x_found,xt=T.x_tex,fin=T.c04;
 const lp=ruta(t,[[c,170,660],[xd,250,780],[xf-.1,320,1020],[fin,350,1050]]),lx=L+lp[0]+Math.sin(t*2.2)*8,ly=lp[1]+Math.sin(t*1.6)*6,ma=eio(seg(t,xf-.15,xf+.6)),sq=seg(t,xt,xt+.4);
 cam(L,540,1040,lerp(1,1.28,eio(seg(t,xf-.2,fin))),540,1000,()=>{tablones(L);marcaTenue(L+610,1050,ma*.42);
  if(sq>0){X.save();X.globalAlpha=sq;X.strokeStyle='rgba(232,220,192,.8)';X.lineWidth=6;X.setLineDash([26,18]);X.strokeRect(L+300,740,620,620);X.restore()}
  const g=X.createRadialGradient(lx,ly,50,lx,ly,780);g.addColorStop(0,'rgba(255,190,110,.12)');g.addColorStop(.4,'rgba(20,12,24,.4)');g.addColorStop(1,'rgba(8,6,16,.92)');X.fillStyle=g;X.fillRect(L-900,-900,2900,4200);
  X.fillStyle='#3a3044';cap(lx-14,ly-210,lx-440,ly-620,46);X.fill();trazo(LIN,3);X.fillStyle='#d9a783';X.beginPath();X.arc(lx,ly-190,40,0,7);X.fill();trazo(LIN,3);farol(lx,ly,1.15,t)})}
// ---------- P04 · la textura, una más entre otras; se gira, se limpia y se lee el nombre ----------
function mesaLuz(L){X.fillStyle='#3d2a1e';X.fillRect(L-900,-900,2900,4200);for(let i=0;i<16;i++){X.fillStyle=i%2?'rgba(0,0,0,.08)':'rgba(255,255,255,.025)';X.fillRect(L-900,-400+i*190,2900,190);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L-900,-400+i*190,2900,5)}}
function loseta(x,y,lado,rot,tipo,o){o=o||{};X.save();X.translate(x,y);X.rotate(rot);X.scale(lado/600,lado/600);X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-288,-282,600,600);
 if(tipo==='casco'){X.fillStyle=ROJO;X.fillRect(-300,-300,600,600);for(let i=0;i<4;i++){X.fillStyle=i%2?'rgba(0,0,0,.08)':'rgba(255,255,255,.03)';X.fillRect(-300,-300+i*150,600,150);X.fillStyle='rgba(0,0,0,.4)';X.fillRect(-300,-300+i*150,600,6);[-240,60].forEach(v=>{X.beginPath();X.arc(v+(i%2)*120,-300+i*150+24,6,0,7);X.fill()})}
  const w=o.w||0,wx=-300+600*w;
  if(w>0){X.save();X.beginPath();X.rect(-300,-300,wx+300,600);X.clip();txt('THE',0,-95,60,CREMA);txt('LEONIDA',0,30,110,CREMA);X.restore()}
  if(w<1){X.save();X.beginPath();X.rect(wx,-300,300-wx,600);X.clip();txt('THE',0,-95,60,CREMA,{a:.16});txt('LEONIDA',0,30,110,CREMA,{a:.16});for(let i=0;i<40;i++){const px=-300+rnd(i+13)*600,py=-250+rnd(i+77)*500;X.fillStyle=i%2?'rgba(84,58,54,.8)':'rgba(70,44,44,.85)';X.beginPath();X.ellipse(px,py,40+rnd(i+3)*60,18+rnd(i+8)*26,rnd(i)*3,0,7);X.fill()}X.restore()}}
 else if(tipo==='madera'){X.fillStyle='#7a5a3a';X.fillRect(-300,-300,600,600);for(let i=0;i<5;i++){X.fillStyle='rgba(0,0,0,.3)';X.fillRect(-300+i*120,-300,6,600)}}
 else if(tipo==='metal'){X.fillStyle='#4a5560';X.fillRect(-300,-300,600,600);X.fillStyle='rgba(0,0,0,.35)';for(let i=0;i<4;i++)for(let j=0;j<4;j++){X.beginPath();X.arc(-225+i*150,-225+j*150,14,0,7);X.fill()}}
 else if(tipo==='cuerda'){X.fillStyle='#5a4630';X.fillRect(-300,-300,600,600);X.save();X.beginPath();X.rect(-300,-300,600,600);X.clip();X.strokeStyle='rgba(0,0,0,.3)';X.lineWidth=16;for(let i=-6;i<8;i++){X.beginPath();X.moveTo(-300+i*110,-300);X.lineTo(i*110,300);X.stroke()}X.restore()}
 else{X.fillStyle='#7c7566';X.fillRect(-300,-300,600,600);X.strokeStyle='rgba(0,0,0,.25)';X.lineWidth=4;X.setLineDash([18,14]);X.strokeRect(-262,-262,524,524);X.setLineDash([])}
 X.strokeStyle=LIN;X.lineWidth=5;X.strokeRect(-300,-300,600,600);X.restore()}
function p04(L,t){const c=T.c04,xr=T.x_read,xth=T.x_the,c6=T.s_6,fin=T.c05;
 const gi=eio(seg(t,xr,xr+.85)),w=seg(t,xr+.9,xth-.05),z=eio(seg(t,c6,fin-.15));
 // al final LEONIDA queda centrado y a 205 px: es el encuadre del que sale el corte al mapa
 cam(L,540,lerp(1000,1030,z),lerp(lerp(1,1.06,seg(t,c,xr)),1.864,z),540,1000,()=>{mesaLuz(L);
  [[210,640,.12,'madera'],[860,700,-.1,'metal'],[220,1420,-.08,'cuerda'],[870,1400,.1,'lona']].forEach(q=>loseta(L+q[0],q[1],360,q[2],q[3]));
  if(gi>0){X.fillStyle=`rgba(10,8,16,${.5*gi})`;X.fillRect(L-900,-900,2900,4200)}
  loseta(L+540,lerp(1040,1000,gi),600*lerp(.62,1,gi),lerp(-Math.PI/2,0,gi),'casco',{w:w});
  if(w>0&&w<1)manoArriba(L+250+w*620,1040,1.25,{sinLapiz:true,manga:MANGA.manga,puno:MANGA.puno});
  const pr=lerp(1000,470,z),g=X.createRadialGradient(L+540,1020,pr*.55,L+540,1020,pr);g.addColorStop(0,'rgba(8,6,16,0)');g.addColorStop(1,`rgba(8,6,16,${.5+.35*z})`);X.fillStyle=g;X.fillRect(L-900,-900,2900,4200)})}
// ---------- P05 · las mismas letras, ahora sobre el mapa estilizado de Leonida ----------
const FLA=[[0,.08],[.42,.06],[.60,.05],[.72,.10],[.80,.22],[.86,.38],[.93,.56],[.97,.72],[.95,.86],[.88,.94],[.80,.90],[.74,.78],[.66,.64],[.60,.50],[.56,.36],[.50,.26],[.40,.22],[.26,.20],[.12,.20],[0,.17]];
function formaLeonida(ox,oy,w,h){X.beginPath();FLA.forEach((p,i)=>i?X.lineTo(ox+p[0]*w,oy+p[1]*h):X.moveTo(ox+p[0]*w,oy+p[1]*h));X.closePath()}
function mapa(L,t,o){X.fillStyle='#0d1b2e';X.fillRect(L-1500,-1500,4100,5000);X.strokeStyle='rgba(64,224,208,.07)';X.lineWidth=2;for(let x=-1500;x<2600;x+=120){X.beginPath();X.moveTo(L+x,-1500);X.lineTo(L+x,3500);X.stroke()}for(let y=-1500;y<3500;y+=120){X.beginPath();X.moveTo(L-1500,y);X.lineTo(L+2600,y);X.stroke()}
 const ox=L+150,oy=500,w=850,h=1000;X.save();X.shadowColor='#ff5fa2';X.shadowBlur=18+26*o.brillo;formaLeonida(ox,oy,w,h);const g=X.createLinearGradient(0,oy,0,oy+h);g.addColorStop(0,'#c2417f');g.addColorStop(1,'#f08a4b');X.fillStyle=g;X.fill();X.restore();X.strokeStyle='#ffd0e2';X.lineWidth=5;X.lineJoin='round';formaLeonida(ox,oy,w,h);X.stroke();
 for(let i=0;i<6;i++){X.fillStyle='#f08a4b';X.beginPath();X.ellipse(ox+(.84-i*.045)*w,oy+(.975+i*.012)*h,16-i*1.5,7,-.3,0,7);X.fill()}
 const ci=o.ciudad;if(ci>0){const cx=ox+.9*w,cy=oy+.78*h;X.fillStyle=`rgba(255,240,170,${.22*Math.min(1,ci)+.06*Math.sin(t*5)})`;X.beginPath();X.arc(cx,cy,74*ci,0,7);X.fill();for(let i=0;i<7;i++){const hh=(20+rnd(i+4)*46)*ci;X.fillStyle='#1a1230';X.fillRect(cx-42+i*12,cy-hh,10,hh);X.fillStyle='#ffe9a0';X.fillRect(cx-39+i*12,cy-hh+5,3,3);X.fillRect(cx-39+i*12,cy-hh+14,3,3)}}
 txt('LEONIDA',L+330,870,110,CREMA)}
function p05(L,t){const c=T.c05,xl=T.x_leo7,xs=T.x_state,xg=T.x_gta7;
 const u=eio(seg(t,xl-.25,xs+.25)),s=lerp(lerp(1.864,1.7,seg(t,c,xl-.25)),1,u)*(1+.07*seg(t,xs+.25,T.c06));
 cam(L,lerp(330,540,u),lerp(870,1000,u),s,540,1000,()=>mapa(L,t,{brillo:.3+golpe(t,xs-.05,.8),ciudad:back(seg(t,xg-.05,xg+.4))}))}
// ---------- P06 · en 2018 el nombre estaba bajo llave; el calendario avanza cinco años ----------
function cofre(x,y,ab,luz,t,o){X.save();X.translate(x,y);
 if(luz>0){const g=X.createRadialGradient(0,-360,20,0,-360,620);g.addColorStop(0,`rgba(255,95,162,${.6*luz})`);g.addColorStop(.5,`rgba(64,224,208,${.2*luz})`);g.addColorStop(1,'rgba(64,224,208,0)');X.fillStyle=g;X.fillRect(-800,-1100,1600,1200)}
 const th=lerp(120,290,ab);X.fillStyle=ab>.5?'#2a1a12':'#6a4426';X.beginPath();X.moveTo(-290,-330);X.lineTo(-290,-330-th+50);X.quadraticCurveTo(0,-330-th-30,290,-330-th+50);X.lineTo(290,-330);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='#1c1418';[-190,190].forEach(v=>X.fillRect(v-22,-330-th+34,44,th-34));
 if(luz>0){const my=lerp(-300,-560,luz);X.save();X.shadowColor='#ff5fa2';X.shadowBlur=30;formaLeonida(-105,my-125,210,250);X.fillStyle='#e0558f';X.fill();X.restore();formaLeonida(-105,my-125,210,250);X.strokeStyle='#ffd0e2';X.lineWidth=4;X.stroke()}
 if(luz<=0&&o.cae<1){X.save();X.beginPath();X.rect(-400,-1500,800,1170);X.clip();X.translate(30,lerp(-700+Math.sin(t*2.4)*10,-150,o.cae));X.rotate(.06);X.fillStyle=ROJO;X.fillRect(-150,-150,300,300);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-150,-150,300,300);txt('LEONIDA',0,6,54,CREMA);X.restore()}
 rr(-290,-330,580,330,14);X.fillStyle='#5a3a22';X.fill();trazo(LIN,3);X.fillStyle='rgba(0,0,0,.18)';for(let i=1;i<4;i++)X.fillRect(-290,-330+i*82,580,5);X.fillStyle='#1c1418';[-190,190].forEach(v=>X.fillRect(v-22,-330,44,330));X.fillStyle='#8a8f98';[-190,190].forEach(v=>[-300,-170,-40].forEach(q=>{X.beginPath();X.arc(v,q,7,0,7);X.fill()}));
 if(ab>0){X.fillStyle='#120c0a';X.fillRect(-270,-338,540,22)}
 if(o.cand>0){X.save();X.translate(0,-300);X.scale(o.cand,o.cand);X.strokeStyle='#8a8f98';X.lineWidth=14;X.beginPath();X.arc(0,-6,30,Math.PI,0);X.stroke();rr(-44,-6,88,74,10);X.fillStyle='#c9a24a';X.fill();trazo(LIN,3);X.fillStyle=TINTA;X.beginPath();X.arc(0,24,9,0,7);X.fill();X.fillRect(-4,24,8,22);X.restore()}
 X.restore()}
function p06(L,t){const c=T.c06,x8=T.x_2018b,xn=T.x_nobody,xk=T.x_knew,xw=T.x_wasnt,xf=T.x_five;
 const cierra=eio(seg(t,xn+.75,xn+1.2)),abre=eio(seg(t,xf+.3,xf+.75)),ab=Math.max(1-cierra,abre),FT=[xw,xw+.3,xw+.6,xw+.9,xf];let n=0;FT.forEach(v=>{if(t>=v)n++});
 X.fillStyle='#241a22';X.fillRect(L-900,-900,2900,4200);X.fillStyle='#2e2029';for(let i=0;i<9;i++)X.fillRect(L-100+i*160,-900,8,2400);
 X.fillStyle='#4a3020';X.fillRect(L-900,1500,2900,2600);X.fillStyle='#5c3c28';X.fillRect(L-900,1500,2900,16);X.fillStyle='rgba(255,190,110,.07)';X.beginPath();X.arc(L+920,1380,420,0,7);X.fill();
 calen(L+270,610,.8,2018+n,n?1:back(seg(t,x8-.12,x8+.15)));
 if(n>0){const u=seg(t,FT[n-1],FT[n-1]+.3);if(u<1){X.save();X.globalAlpha=1-u;X.translate(L+270,610+u*u*420);X.rotate(u*.5);X.scale(.8,.8);X.fillStyle='#efe6d0';X.fillRect(-176,-66,352,206);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-176,-66,352,206);txt(String(2017+n),0,44,118,TINTA);X.restore()}}
 cofre(L+560,1500,ab,abre,t,{cae:eio(seg(t,xn,xn+.7)),cand:back(seg(t,xk-.1,xk+.15))*(1-seg(t,xf+.15,xf+.3))});farol(L+920,1402,1,t)}
// ---------- P07a · dos fichas, ningún veredicto ----------
function ficha(x,y,rot,f,l1,l2){const sx=Math.max(.02,Math.abs(1-2*f)),cara=f>.5;X.save();X.translate(x,y);X.rotate(rot);X.scale(sx,1);X.fillStyle='rgba(0,0,0,.3)';X.fillRect(-196,-246,410,520);X.fillStyle=cara?CREMA:'#8a5a44';X.fillRect(-205,-260,410,520);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-205,-260,410,520);X.strokeStyle=cara?'rgba(42,32,25,.35)':'rgba(0,0,0,.3)';X.strokeRect(-185,-240,370,480);
 if(cara){if(l2){txt(l1,0,-46,62,TINTA);txt(l2,0,40,62,TINTA)}else txt(l1,0,0,62,TINTA)}X.restore()}
function p07a(L,t){const c=T.c07a,xp=T.x_planned,xo=T.x_others,xl=T.x_left,xr=T.x_rock,fin=T.c07b;
 const a=eo(seg(t,c+.05,c+.5)),b=eo(seg(t,xo-.2,xo+.25));
 cam(L,540,1040,lerp(1,1.05,seg(t,c,fin)),540,1000,()=>{mesaLuz(L);
  if(a>0)ficha(L+290-(1-a)*700,1040,-.05-(1-a)*.3,seg(t,xp-.2,xp+.08),'PLANNED','TEASE');
  if(b>0)ficha(L+790+(1-b)*700,1060,.04+(1-b)*.3,seg(t,xl-.2,xl+.08),'LEFTOVER');
  const sp=ruta(t,[[xr-.1,760,2400],[xr+.3,330,1160],[xr+.62,356,1146],[xr+.9,800,1186],[xr+1.15,820,1172],[xr+1.4,1150,2400]]);
  if(t>xr-.1)manoArriba(L+sp[0],sp[1]+Math.sin(t*9)*5,1.2,{manga:MANGA.manga,puno:MANGA.puno});
  const g=X.createRadialGradient(L+540,1040,520,L+540,1040,1100);g.addColorStop(0,'rgba(8,6,16,0)');g.addColorStop(1,'rgba(8,6,16,.6)');X.fillStyle=g;X.fillRect(L-900,-900,2900,4200)})}
// ---------- P07b · el barco sigue navegando; cierre ----------
function p07b(L,t){const c=T.c07b,k=T.x_tell,off=t*150;
 const cm=ruta(t,[[c,540,1250,.8,540,1100],[k+.7,540,1320,.52,400,1440]]);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>{mundo(L,t,off);barco(L+540+(t-c)*14,1320+Math.sin(t*1.7)*4,1,t,{mugre:1})});
 cierreCanal(L,t,k)}

NUEVOS.dc_gtaen14_p01=SET(p01);NUEVOS.dc_gtaen14_p02=SET(p02);NUEVOS.dc_gtaen14_p03=SET(p03);NUEVOS.dc_gtaen14_p04=SET(p04);NUEVOS.dc_gtaen14_p05=SET(p05);NUEVOS.dc_gtaen14_p06=SET(p06);NUEVOS.dc_gtaen14_p07a=SET(p07a);NUEVOS.dc_gtaen14_p07b=SET(p07b);
})();
// ===== DC · GTAEN14 · FIN =====
</script>
