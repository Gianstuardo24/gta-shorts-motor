<script>
// ===== DC · COFFEE21 · INICIO ===== (Coffee 21h · NEVER Use Boiling Water for Your Coffee · paquete 6 del lote del 27-nov)
// Reglas del paquete: las temperaturas solo aparecen en el termómetro y en la tarjeta; la espera no promete una temperatura exacta; no hace falta equipo caro.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const mez=(a,b,u)=>{const p=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)),A=p(a),B=p(b);return 'rgb('+A.map((v,i)=>Math.round(lerp(v,B[i],u))).join(',')+')'};
const ACERO='#c6ccd4',ACERO2='#8e98a4',NEGRO='#22262b',CREMA='#f1e9d8',C_OSC='#1a0e09',C_OK='#5a3420',C_PAL='#b48c5e',MOLIDO='#3a2318',AGUA='#d7efff';
const MANO={manga:'#d9a441',puno:'#c28f33'},PIEL='#e8b28c',PIEL2='#cf9670';
// ---------- cocina ----------
function cocina(L){const g=X.createLinearGradient(0,-300,0,1400);g.addColorStop(0,'#1a323c');g.addColorStop(1,'#27485a');X.fillStyle=g;X.fillRect(L-1500,-1600,5200,6400);
 X.strokeStyle='rgba(255,255,255,.035)';X.lineWidth=4;for(let x=-1500;x<3700;x+=180){X.beginPath();X.moveTo(L+x,-400);X.lineTo(L+x,1380);X.stroke()}for(let y=120;y<1380;y+=180){X.beginPath();X.moveTo(L-1500,y);X.lineTo(L+3700,y);X.stroke()}
 X.fillStyle='#33414a';X.fillRect(L-1500,1380,5200,3000);X.fillStyle='#55666f';X.fillRect(L-1500,1380,5200,46);X.fillStyle='rgba(0,0,0,.22)';X.fillRect(L-1500,1426,5200,10)}
function meson(L){X.fillStyle='#35434c';X.fillRect(L-900,-900,2900,4200);X.fillStyle='rgba(255,255,255,.03)';for(let i=0;i<60;i++){X.beginPath();X.arc(L-300+rnd(i)*1700,-200+rnd(i+77)*2400,10+rnd(i+5)*26,0,7);X.fill()}}
function vapor(x,y,t,f,s,n){if(f<=0)return;n=n||7;for(let i=0;i<n;i++){const u=((t*.55+i/n)%1),a=(1-u)*.30*Math.min(1,f)*Math.min(1,u*5);X.fillStyle=`rgba(255,255,255,${a})`;X.beginPath();X.arc(x+Math.sin(u*6+i*2.3)*34*s*(.5+u),y-u*300*s*(.5+f*.6),(16+u*46)*s*(.6+.5*f),0,7);X.fill()}}
function llama(x,y,t,f){if(f<=0)return;for(let i=-2;i<=2;i++){const h=(26+70*f)*(1-.12*Math.abs(i))*(.86+.14*Math.sin(t*23+i*2)),w=24;X.fillStyle='#3d9bf0';X.beginPath();X.moveTo(x+i*44-w,y);X.quadraticCurveTo(x+i*44-w,y-h*.6,x+i*44,y-h);X.quadraticCurveTo(x+i*44+w,y-h*.6,x+i*44+w,y);X.closePath();X.fill();X.fillStyle='#c9e8ff';X.beginPath();X.moveTo(x+i*44-w*.45,y);X.quadraticCurveTo(x+i*44-w*.45,y-h*.3,x+i*44,y-h*.55);X.quadraticCurveTo(x+i*44+w*.45,y-h*.3,x+i*44+w*.45,y);X.closePath();X.fill()}}
// hervidor de lado, pico hacia +x (dir=1). rot gira alrededor del asa
function hervidor(x,yb,s,o){o=o||{};const d=o.dir||1;X.save();X.translate(x,yb);X.scale(d*s,s);X.translate(0,-380);X.rotate((o.rot||0)+(o.tiembla||0));X.translate(0,380);X.lineJoin='round';
 X.fillStyle=ACERO2;X.beginPath();X.moveTo(118,-150);X.quadraticCurveTo(210,-170,236,-262);X.lineTo(262,-256);X.quadraticCurveTo(246,-120,128,-84);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=ACERO;X.beginPath();X.moveTo(-156,0);X.quadraticCurveTo(-176,-120,-112,-236);X.lineTo(112,-236);X.quadraticCurveTo(176,-120,156,0);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='rgba(255,255,255,.4)';X.beginPath();X.ellipse(-96,-120,14,84,.12,0,7);X.fill();X.fillStyle='rgba(0,0,0,.10)';X.beginPath();X.ellipse(96,-110,20,92,-.12,0,7);X.fill();
 X.fillStyle=ACERO2;rr(-118,-262,236,34,14);X.fill();trazo(LIN,3);X.fillStyle=NEGRO;X.beginPath();X.arc(0,-276,22,0,7);X.fill();
 X.strokeStyle=NEGRO;X.lineWidth=26;X.lineCap='round';X.beginPath();X.moveTo(-98,-250);X.quadraticCurveTo(-110,-392,0,-394);X.quadraticCurveTo(110,-392,98,-250);X.stroke();X.restore()}
function pico(x,yb,s,o){o=o||{};const d=o.dir||1,r=o.rot||0,c=Math.cos(r),n=Math.sin(r),px=250,py=-262+380;return [x+d*s*(px*c-py*n),yb+s*(-380+px*n+py*c)]}
function chorro(x0,y0,x1,y1,w,t,turb){X.lineCap='round';X.strokeStyle='rgba(215,239,255,.9)';X.lineWidth=w;X.beginPath();X.moveTo(x0,y0);const mx=lerp(x0,x1,.72)+Math.sin(t*31)*turb*5,my=y0+(y1-y0)*.18;X.quadraticCurveTo(mx,my,x1+Math.sin(t*27)*turb*6,y1);X.stroke();
 X.strokeStyle='rgba(255,255,255,.7)';X.lineWidth=w*.3;X.beginPath();X.moveTo(x0,y0);X.quadraticCurveTo(mx,my,x1+Math.sin(t*27)*turb*6,y1);X.stroke();
 for(let i=0;i<6;i++){const u=((t*2.6+i/6)%1);X.fillStyle=`rgba(215,239,255,${(1-u)*.8})`;X.beginPath();X.arc(x1+(rnd(i)-.5)*90*u*(1+turb),y1-u*(30+60*turb)*Math.sin(u*3.14),4+3*turb,0,7);X.fill()}}
// gotero (cono con filtro) sobre jarra de vidrio. nivel 0..1 y color del café en la jarra
function gotero(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(0,5,170,16,0,0,7);X.fill();
 // jarra
 const niv=o.nivel||0;X.save();X.beginPath();X.moveTo(-120,-330);X.lineTo(120,-330);X.quadraticCurveTo(150,-170,138,0);X.lineTo(-138,0);X.quadraticCurveTo(-150,-170,-120,-330);X.closePath();X.clip();
 X.fillStyle='rgba(214,236,238,.28)';X.fillRect(-160,-340,320,340);if(niv>0){X.fillStyle=o.cafe||C_OK;X.fillRect(-160,-niv*290,320,niv*290);X.fillStyle='rgba(255,255,255,.12)';X.fillRect(-160,-niv*290,320,8)}X.restore();
 X.strokeStyle='rgba(30,50,55,.85)';X.lineWidth=5;X.beginPath();X.moveTo(-120,-330);X.lineTo(120,-330);X.quadraticCurveTo(150,-170,138,0);X.lineTo(-138,0);X.quadraticCurveTo(-150,-170,-120,-330);X.closePath();X.stroke();
 X.fillStyle='rgba(255,255,255,.4)';rr(-112,-290,14,230,7);X.fill();
 if(o.gotea>0){X.strokeStyle=o.cafe||C_OK;X.lineWidth=7+7*o.gotea;X.lineCap='round';X.beginPath();X.moveTo(0,-352);X.lineTo(0,-niv*290-6);X.stroke()}
 // cono
 X.fillStyle=CREMA;X.beginPath();X.moveTo(-178,-590);X.lineTo(178,-590);X.lineTo(56,-362);X.lineTo(-56,-362);X.closePath();X.fill();trazo(LIN,3);rr(-96,-366,192,30,10);X.fillStyle=CREMA;X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(0,0,0,.10)';X.lineWidth=5;[-90,-40,40,90].forEach(v=>{X.beginPath();X.moveTo(v*1.5,-580);X.lineTo(v*.5,-380);X.stroke()});
 // boca del cono con filtro y café molido
 X.fillStyle='#e8dcc0';X.beginPath();X.ellipse(0,-596,190,40,0,0,7);X.fill();trazo(LIN,3);X.fillStyle=MOLIDO;X.beginPath();X.ellipse(0,-590,160,30,0,0,7);X.fill();
 if(o.moja>0){X.fillStyle='rgba(215,239,255,.35)';X.beginPath();X.ellipse(0,-590,150*Math.min(1,o.moja),27*Math.min(1,o.moja),0,0,7);X.fill();const tt=o.t||0;X.fillStyle='rgba(120,80,50,.9)';for(let i=0;i<8;i++){const u=((tt*(1.5+2*(o.hierve||0))+i/8)%1);X.beginPath();X.arc(-120+i*34+Math.sin(i*3)*10,-590+Math.sin(i*2)*12,(4+9*(o.hierve||0))*Math.sin(u*3.14),0,7);X.fill()}}
 X.restore()}
// taza en tres cuartos: se ve el color del café
function taza(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.rotate(o.rot||0);X.scale(s,s);X.lineJoin='round';
 if(!o.sinSombra){X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(8,4,120,14,0,0,7);X.fill()}
 X.strokeStyle=CREMA;X.lineWidth=24;X.beginPath();X.arc((o.asa||1)*108,-100,52,-1.35*(o.asa||1)+(o.asa<0?Math.PI:0),1.35*(o.asa||1)+(o.asa<0?Math.PI:0),(o.asa||1)<0);X.stroke();X.strokeStyle=LIN;X.lineWidth=3;
 X.fillStyle=CREMA;X.beginPath();X.moveTo(-100,-190);X.lineTo(100,-190);X.lineTo(92,-22);X.quadraticCurveTo(88,0,60,0);X.lineTo(-60,0);X.quadraticCurveTo(-88,0,-92,-22);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='rgba(0,0,0,.06)';X.fillRect(30,-190,70,190);X.fillStyle=o.banda||'#c8553d';X.fillRect(-98,-120,196,26);
 X.fillStyle='#e3d9c2';X.beginPath();X.ellipse(0,-190,100,26,0,0,7);X.fill();trazo(LIN,3);X.fillStyle=o.cafe||C_OK;X.beginPath();X.ellipse(0,-186,86,19,0,0,7);X.fill();X.fillStyle='rgba(255,255,255,.14)';X.beginPath();X.ellipse(-30,-190,30,6,0,0,7);X.fill();X.restore()}
// reloj de cocina: cuña = tiempo que queda (u 1 → 0) y el "30" narrado
function reloj30(x,y,r,u){X.fillStyle='rgba(0,0,0,.24)';X.beginPath();X.arc(x+r*.06,y+r*.1,r,0,7);X.fill();X.fillStyle='#e4572e';X.beginPath();X.arc(x,y,r,0,7);X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.beginPath();X.arc(x,y,r*.8,0,7);X.fill();
 if(u>0){X.fillStyle='rgba(228,87,46,.42)';X.beginPath();X.moveTo(x,y);X.arc(x,y,r*.76,-Math.PI/2,-Math.PI/2+u*Math.PI*2);X.closePath();X.fill()}
 txt('30',x,y+r*.04,r*.78,'#2a2019',{w:r*1.4});X.fillStyle=NEGRO;rr(x-r*.14,y-r*1.16,r*.28,r*.2,r*.06);X.fill()}
// termómetro de dial: banda verde 195–205 y marca del hervor en 212
const AT=T_=>2.618+(T_-170)/50*4.189;
function dial(x,y,r,temp,o){o=o||{};X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.arc(x+r*.05,y+r*.08,r*1.06,0,7);X.fill();X.fillStyle=ACERO2;X.beginPath();X.arc(x,y,r*1.06,0,7);X.fill();trazo(LIN,3);X.fillStyle='#fbf7ec';X.beginPath();X.arc(x,y,r*.94,0,7);X.fill();
 X.lineCap='butt';X.strokeStyle='#d9d2c0';X.lineWidth=r*.12;X.beginPath();X.arc(x,y,r*.74,AT(170),AT(220));X.stroke();X.strokeStyle='#4caf50';X.beginPath();X.arc(x,y,r*.74,AT(195),AT(205));X.stroke();
 X.strokeStyle='#d6402f';X.lineWidth=r*.05;X.beginPath();X.moveTo(x+Math.cos(AT(212))*r*.64,y+Math.sin(AT(212))*r*.64);X.lineTo(x+Math.cos(AT(212))*r*.86,y+Math.sin(AT(212))*r*.86);X.stroke();
 if(!o.sinNum){const q=(T_,dr,s)=>txt(String(T_),x+Math.cos(AT(T_))*r*dr,y+Math.sin(AT(T_))*r*dr,r*s,T_===212?'#d6402f':'#2a2019',{w:r});q(195,.46,.19);q(205,.45,.19);q(212,.40,.21);txt('°F',x,y+r*.52,r*.17,'#7a6f66',{w:r});if(o.c)txt('100 °C',x+r*.34,y+r*.3,r*.13,'#d6402f',{w:r})}
 const a=AT(temp);X.strokeStyle=NEGRO;X.lineCap='round';X.lineWidth=r*.055;X.beginPath();X.moveTo(x-Math.cos(a)*r*.14,y-Math.sin(a)*r*.14);X.lineTo(x+Math.cos(a)*r*.8,y+Math.sin(a)*r*.8);X.stroke();X.fillStyle=NEGRO;X.beginPath();X.arc(x,y,r*.09,0,7);X.fill()}
// ---------- persona parcial: gorra que tapa los ojos, cara de la nariz hacia abajo, taza ----------
function boca(cx,cy,w,e){X.lineCap='round';X.strokeStyle='#8a3d33';X.lineWidth=9;const s=e.s||0,m=e.m||0;X.beginPath();X.moveTo(cx-w/2,cy-12*s+12*m);X.bezierCurveTo(cx-w/4,cy+16*s-20*m,cx+w/4,cy+16*s+18*m,cx+w/2,cy-12*s-8*m);X.stroke();
 if(m>.3){X.lineWidth=5;X.beginPath();X.arc(cx+w/2+12,cy-8*m,11,2.2,4.2);X.stroke();X.beginPath();X.arc(cx-w/2-12,cy+12*m,11,-1,1);X.stroke()}}
function persona(L,t,o){const cx=L+540+(o.dx||0);X.lineJoin='round';
 X.fillStyle='#d9a441';X.beginPath();X.moveTo(cx-560,2100);X.lineTo(cx-500,1180);X.quadraticCurveTo(cx-440,1040,cx-250,1000);X.lineTo(cx+250,1000);X.quadraticCurveTo(cx+440,1040,cx+500,1180);X.lineTo(cx+560,2100);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='#2b3a44';X.beginPath();X.moveTo(cx-250,2100);X.lineTo(cx-230,1190);X.lineTo(cx+230,1190);X.lineTo(cx+250,2100);X.closePath();X.fill();trazo(LIN,3);X.strokeStyle='#2b3a44';X.lineWidth=18;X.beginPath();X.moveTo(cx-225,1195);X.lineTo(cx-120,1010);X.moveTo(cx+225,1195);X.lineTo(cx+120,1010);X.stroke();
 X.fillStyle=PIEL2;X.beginPath();X.moveTo(cx-96,800);X.lineTo(cx+96,800);X.lineTo(cx+110,1010);X.quadraticCurveTo(cx,1070,cx-110,1010);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=PIEL;X.beginPath();X.ellipse(cx,590,212,272,0,0,7);X.fill();trazo(LIN,3);[-1,1].forEach(d=>{X.beginPath();X.ellipse(cx+d*214,600,26,46,0,0,7);X.fill();trazo(LIN,3)});
 X.strokeStyle='rgba(120,70,45,.55)';X.lineWidth=5;X.lineCap='round';X.beginPath();X.moveTo(cx-26,640);X.quadraticCurveTo(cx,660,cx+26,640);X.stroke();
 boca(cx,736,150,o.boca||{});
 // gorra: tapa los ojos y deja oscuro el lugar de los subtítulos
 X.fillStyle='#16222b';X.beginPath();X.moveTo(cx-236,470);X.quadraticCurveTo(cx-250,150,cx,140);X.quadraticCurveTo(cx+250,150,cx+236,470);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='#0f1920';X.beginPath();X.moveTo(cx-300,452);X.quadraticCurveTo(cx,400,cx+300,452);X.quadraticCurveTo(cx+310,500,cx+280,510);X.quadraticCurveTo(cx,468,cx-280,510);X.quadraticCurveTo(cx-310,500,cx-300,452);X.closePath();X.fill();trazo(LIN,3);
 const g=X.createLinearGradient(0,480,0,580);g.addColorStop(0,'rgba(0,0,0,.28)');g.addColorStop(1,'rgba(0,0,0,0)');X.fillStyle=g;X.beginPath();X.ellipse(cx,590,212,272,0,0,7);X.save();X.clip();X.fillRect(cx-240,470,480,120);X.restore();
 // taza con la mano
 if(o.ty!==undefined){const tx=cx+30,ty=o.ty;X.fillStyle='#d9a441';cap(cx+520,ty+420,tx+150,ty-70,70);X.fill();trazo(LIN,3);taza(tx,ty,1.3,{rot:o.trot||0,cafe:o.cafe,sinSombra:true});
  X.fillStyle=PIEL;X.beginPath();X.ellipse(tx+150,ty-130,62,84,.2,0,7);X.fill();trazo(LIN,3);X.strokeStyle='rgba(120,70,45,.4)';X.lineWidth=4;[-40,-8,24].forEach(v=>{X.beginPath();X.moveTo(tx+108,ty-130+v);X.lineTo(tx+150,ty-126+v);X.stroke()})}}

// ---------- P01a · macro: agua hirviendo sobre el café ----------
function p01a(L,t){const fin=T.c01b,rot=.62;
 cam(L,560,860,lerp(1.5,1.62,seg(t,0,fin)),540,1000,()=>{cocina(L);const p=pico(L+60,1010,1.25,{rot});
  gotero(L+620,1380,1.25,{nivel:.12+.3*seg(t,.3,fin),cafe:C_OSC,gotea:seg(t,.5,.8),moja:seg(t,.1,.5),hierve:1,t});
  chorro(p[0],p[1],L+610,646,26,t,1);hervidor(L+60,1010,1.25,{rot,tiembla:Math.sin(t*41)*.012});
  vapor(L+610,640,t,1.3,1.5,9);vapor(p[0],p[1]-10,t+.4,1,1,6)})}
// ---------- P01b · reacción parcial: prueba y hace una mueca leve ----------
function p01b(L,t){const c=T.c01b,xm=T.x_morning,xr=T.x_ruin,xe=T.x_every2,xa=T.x_and1,fin=T.c02;
 const ty=ruta(t,[[c,1420],[xm+.1,958],[xr-.1,946],[xe-.05,1300],[xa+.2,1300],[xa+.9,1330]])[0],trot=-.3*eio(seg(t,xm-.2,xm+.2))*(1-eio(seg(t,xr-.15,xr+.15)));
 const mu=eio(seg(t,xe-.02,xe+.2))*(1-eio(seg(t,xa+.2,xa+.7)));
 const cm=ruta(t,[[c,540,1000,1],[xa,540,1000,1.04],[fin,540,1010,1.1]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{cocina(L);persona(L,t,{dx:9*Math.sin((t-xe)*16)*mu+7*Math.sin((t-xa)*9)*seg(t,xa+.3,xa+.5)*(1-seg(t,xa+1.3,xa+1.6)),boca:{m:mu,s:-.25*(1-mu)},ty,trot,cafe:C_OSC});
  if(t>xe)vapor(L+570,ty-250,t,.8,1,5)})}
// ---------- P02 · "más caliente, más fuerte": la mano sube el fuego ----------
function perilla(x,y,a){X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(x+5,y+7,58,0,7);X.fill();X.fillStyle=NEGRO;X.beginPath();X.arc(x,y,58,0,7);X.fill();trazo(LIN,3);X.fillStyle='#3a4047';X.beginPath();X.arc(x,y,40,0,7);X.fill();
 X.strokeStyle='#f1e9d8';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(a-1.57)*38,y+Math.sin(a-1.57)*38);X.stroke();
 X.strokeStyle='rgba(255,255,255,.3)';X.lineWidth=6;X.beginPath();X.arc(x,y,78,-2.6,.6);X.stroke();X.strokeStyle='#e4572e';X.beginPath();X.arc(x,y,78,-.3,.6);X.stroke()}
function quemador(x){X.fillStyle=NEGRO;rr(x-190,1356,380,28,10);X.fill();X.fillStyle='#3a4047';[-150,-50,50,150].forEach(v=>X.fillRect(x+v-8,1340,16,20))}
function p02(L,t){const c=T.c02,xh=T.x_hotter,xs=T.x_stronger,fin=T.c03;
 const f=lerp(.3,1,eio(seg(t,xh-.15,xh+.5))),a=lerp(-1.6,.4,eio(seg(t,xh-.15,xh+.5))),llega=eio(seg(t,c+.1,xh-.25));
 const cm=ruta(t,[[c,560,1330,1.25],[xh+.1,560,1330,1.25],[xs+.2,540,1010,1.02]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{cocina(L);quemador(L+520);llama(L+520,1344,t,f);hervidor(L+520,1340,1.1,{tiembla:Math.sin(t*43)*.02*f*f});
  const p=pico(L+520,1340,1.1,{});vapor(p[0],p[1]-6,t,f*1.4,1.2,9);vapor(L+520,1030,t+.3,f*f*.9,1,5);
  perilla(L+520,1560,a);const hx=L+lerp(1250,566,llega)+eio(seg(t,xs-.2,xs+.3))*300,hy=lerp(1900,1578,llega)+eio(seg(t,xs-.2,xs+.3))*260,o=origen(hx,hy,.35,1.2,-1,118,44);
  manoLado(o[0],o[1],.35,1.2,-1,Object.assign({},MANO,{curl:[.45,.5,.55,.58],pulgar:.35}))})}
// ---------- P03 · cenital: la tarjeta con el rango y el termómetro en el hervor ----------
function hervidorArriba(x,y,t,f){X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.arc(x+12,y+16,190,0,7);X.fill();X.fillStyle=ACERO2;X.beginPath();X.moveTo(x-150,y-150);X.lineTo(x-268,y-250);X.lineTo(x-236,y-282);X.lineTo(x-116,y-176);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=ACERO;X.beginPath();X.arc(x,y,188,0,7);X.fill();trazo(LIN,3);X.fillStyle=ACERO2;X.beginPath();X.arc(x+Math.sin(t*37)*3*f,y+Math.cos(t*31)*3*f,128,0,7);X.fill();trazo(LIN,3);
 X.strokeStyle=NEGRO;X.lineWidth=40;X.lineCap='round';X.beginPath();X.moveTo(x-128,y+128);X.lineTo(x+128,y-128);X.stroke();X.fillStyle=NEGRO;X.beginPath();X.arc(x,y,30,0,7);X.fill();
 for(let i=0;i<7;i++){const u=((t*.6+i/7)%1);X.fillStyle=`rgba(255,255,255,${(1-u)*.3*f})`;X.beginPath();X.arc(x-256-u*120+Math.sin(i*2+u*5)*26,y-270-u*150,22+u*56,0,7);X.fill()}}
function tarjeta(L,en,q1,q2,q3){const x=L+560+(1-en)*700;X.save();X.translate(x+215,640);X.rotate(.04);X.fillStyle='rgba(0,0,0,.28)';rr(-207,-146,430,310,24);X.fill();rr(-215,-155,430,310,24);X.fillStyle=CREMA;X.fill();trazo(LIN,3);
 X.fillStyle='#5a3420';X.beginPath();X.ellipse(-150,-100,26,18,-.5,0,7);X.fill();X.strokeStyle=CREMA;X.lineWidth=4;X.beginPath();X.moveTo(-168,-92);X.quadraticCurveTo(-150,-104,-132,-108);X.stroke();X.fillStyle='rgba(42,32,25,.18)';rr(-110,-108,290,14,7);X.fill();
 X.save();X.translate(0,-22);X.scale(Math.max(.01,q1),Math.max(.01,q1));txt('195',-128,0,82,'#2a2019',{w:200});X.restore();if(q2>0){X.globalAlpha=Math.min(1,q2);txt('–',-22,-26,76,'#2a2019',{w:60});X.globalAlpha=1;X.save();X.translate(0,-22);X.scale(Math.max(.01,q2),Math.max(.01,q2));txt('205',80,0,82,'#2a2019',{w:200});X.restore();txt('°F',176,-46,36,'#7a6f66',{w:60,a:Math.min(1,q2)})}
 if(q3>0)txt('90–96 °C',0,90,58,'#7a6f66',{w:380,a:q3});X.restore()}
function p03(L,t){const c=T.c03,xr=T.x_rec,x5=T.x_195,x0=T.x_205,xf=T.x_fahr,xw=T.x_water4,x2=T.x_212;
 const temp=lerp(190,212,eio(seg(t,xw-.2,x2+.25)))+Math.sin(t*19)*.5*seg(t,x2,x2+.3),en=eio(seg(t,T.x_nat-.2,T.x_nat+.4));
 cam(L,540,1000,lerp(1,1.05,seg(t,c,T.c04)),540,1000,()=>{meson(L);hervidorArriba(L+300,1010,t,1);
  X.strokeStyle=ACERO2;X.lineWidth=14;X.lineCap='round';const dx=L+780+(1-en)*700;X.beginPath();X.moveTo(dx-190,1330);X.lineTo(L+410+(1-en)*700,1110);X.stroke();
  dial(dx,1420,250,temp,{c:t>x2-.1});tarjeta(L,eio(seg(t,xr-.15,xr+.4)),back(seg(t,x5-.08,x5+.25)),back(seg(t,x0-.08,x0+.25)),eio(seg(t,xf-.05,xf+.35)))})}
// ---------- P04 · macro lateral: el agua demasiado caliente saca de más; la taza queda oscura y se aparta ----------
function p04(L,t){const c=T.c04,xp=T.x_pull,xt=T.x_thats,xb=T.x_bitter5,fin=T.c05;
 const vierte=1-eio(seg(t,xt-.3,xt+.1)),niv=lerp(.1,.78,seg(t,c,xt)),aparta=eio(seg(t,xb+.05,xb+.75)),rot=.6*vierte;
 cam(L,560,1010,1.1,540,1000,()=>{cocina(L);const kx=L+40-(1-vierte)*380,ky=980-(1-vierte)*120,p=pico(kx,ky,1.2,{rot});
  const gx=L+620+aparta*720;gotero(gx,1380,1.15,{nivel:niv,cafe:mez(C_OK,C_OSC,seg(t,c,xp+.6)),gotea:vierte*.9+.3*(1-aparta)*(1-vierte),moja:1,hierve:vierte,t});
  if(vierte>.05)chorro(p[0],p[1],L+612,706,24*vierte,t,1);hervidor(kx,ky,1.2,{rot,tiembla:Math.sin(t*41)*.012*vierte});vapor(L+612,700,t,1.2*vierte+.3,1.4,8);
  if(aparta>0){const hx=gx-236,hy=1180,o=origen(hx,hy,.05,1.25,1,150,0);manoLado(o[0],o[1],.05,1.25,1,Object.assign({},MANO,{curl:[.1,.12,.14,.16],pulgar:.8}))}})}
// ---------- P05 · el hervidor se apaga; el reloj de 30 segundos queda junto a la taza ----------
function mesada(L,t,o){cocina(L);quemador(L+300);llama(L+300,1344,t,o.fuego);perilla(L+300,1560,lerp(-1.6,.4,o.fuego));
 gotero(L+800,1380,.95,{nivel:o.nivel||0,cafe:C_OK,gotea:o.gotea||0,moja:o.moja||0,hierve:0,t});
 if(o.reloj>0){X.save();X.translate(L+560,1380-118*o.reloj);X.scale(o.reloj,o.reloj);reloj30(0,0,112,o.cuna===undefined?1:o.cuna);X.restore()}}
function p05(L,t){const c=T.c05,xf=T.x_fix,x3=T.x_30a,apaga=eio(seg(t,xf+.1,xf+.5)),f=1-apaga,vap=lerp(1.3,.5,eio(seg(t,xf+.4,T.c06)));
 mesada(L,t,{fuego:f,reloj:back(seg(t,x3-.25,x3+.15))});hervidor(L+300,1340,1.05,{tiembla:Math.sin(t*43)*.016*f});const p=pico(L+300,1340,1.05,{});vapor(p[0],p[1]-6,t,vap,1.2,8);
 const llega=eio(seg(t,xf-.5,xf+.05)),va=eio(seg(t,xf+.6,xf+1.2)),hx=L+lerp(1250,346,llega)+va*900,hy=lerp(1950,1578,llega)+va*400,o=origen(hx,hy,.35,1.2,-1,118,44);
 if(va<1)manoLado(o[0],o[1],.35,1.2,-1,Object.assign({},MANO,{curl:[.45,.5,.55,.58],pulgar:.35}))}
// ---------- P06 · cenital: las manos despejan termómetro, hervidor de lujo y café caro ----------
function hervidorLujo(x,y){X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.arc(x+10,y+14,132,0,7);X.fill();X.strokeStyle='#c77b4a';X.lineWidth=26;X.lineCap='round';X.beginPath();X.moveTo(x-110,y-40);X.bezierCurveTo(x-240,y-60,x-180,y-220,x-300,y-230);X.stroke();X.strokeStyle=LIN;X.lineWidth=3;
 X.fillStyle='#c77b4a';X.beginPath();X.arc(x,y,130,0,7);X.fill();trazo(LIN,3);X.fillStyle='#d99468';X.beginPath();X.arc(x,y,88,0,7);X.fill();trazo(LIN,3);X.fillStyle='#6b4226';X.beginPath();X.arc(x,y,22,0,7);X.fill();X.strokeStyle='#6b4226';X.lineWidth=34;X.beginPath();X.moveTo(x+90,y+90);X.lineTo(x+190,y+190);X.stroke()}
function bolsaCara(x,y,r){X.save();X.translate(x,y);X.rotate(r);X.fillStyle='rgba(0,0,0,.28)';rr(-122,-166,260,350,18);X.fill();rr(-130,-175,260,350,18);X.fillStyle='#17181c';X.fill();trazo(LIN,3);X.fillStyle='#d4af37';X.fillRect(-130,-120,260,14);X.fillRect(-130,96,260,14);
 X.beginPath();X.arc(0,-10,62,0,7);X.fill();X.fillStyle='#17181c';X.beginPath();X.ellipse(0,-10,26,36,-.5,0,7);X.fill();X.strokeStyle='#d4af37';X.lineWidth=5;X.beginPath();X.moveTo(-14,18);X.quadraticCurveTo(0,-10,14,-38);X.stroke();
 X.fillStyle='#d4af37';[-1,0,1].forEach(i=>{X.beginPath();for(let k=0;k<10;k++){const a=k*Math.PI/5-Math.PI/2,rr_=k%2?7:16;X.lineTo(i*44+Math.cos(a)*rr_,140+Math.sin(a)*rr_)}X.closePath();X.fill()});X.restore()}
function tazaArriba(x,y){X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.arc(x+10,y+14,150,0,7);X.fill();X.fillStyle=CREMA;rr(x+110,y-30,110,60,26);X.fill();trazo(LIN,3);X.fillStyle=CREMA;X.beginPath();X.arc(x,y,150,0,7);X.fill();trazo(LIN,3);X.fillStyle='#e8dcc0';X.beginPath();X.arc(x,y,126,0,7);X.fill();trazo(LIN,3);X.fillStyle=MOLIDO;X.beginPath();X.arc(x,y,96,0,7);X.fill()}
function p06(L,t){const c=T.c06,xt=T.x_thermo,xf=T.x_fancy,xe=T.x_exp;
 const sale=(k)=>eio(seg(t,k+.1,k+.7)),toca=(k)=>eio(seg(t,k-.4,k+.1));
 meson(L);hervidorArriba(L+300,1330,t,.5);tazaArriba(L+760,1380);reloj30(L+540,1010,118,1);
 const a=sale(xt),b=sale(xf),d=sale(xe);
 // termómetro: sale hacia la derecha
 X.save();X.translate(a*900,-a*200);dial(L+820,720,150,205,{});X.restore();if(toca(xt)>0&&a<1){manoArriba(L+lerp(1300,640,toca(xt))+a*900,lerp(1500,790,toca(xt))-a*200,1.2,{sinLapiz:true,manga:MANO.manga,puno:MANO.puno})}
 // hervidor de lujo: sale hacia la izquierda
 X.save();X.translate(-b*900,-b*160);hervidorLujo(L+330,640);X.restore();if(toca(xf)>0&&b<1){manoArriba(L+lerp(-300,470,toca(xf))-b*900,lerp(1400,690,toca(xf))-b*160,1.2,{sinLapiz:true,esp:-1,manga:MANO.manga,puno:MANO.puno})}
 // café caro: sale hacia abajo a la izquierda
 X.save();X.translate(-d*700,d*700);bolsaCara(L+200,960,-.12);X.restore();if(toca(xe)>0&&d<1){manoArriba(L+lerp(-300,300,toca(xe))-d*700,lerp(1900,1010,toca(xe))+d*700,1.2,{sinLapiz:true,esp:-1,manga:MANO.manga,puno:MANO.puno})}}
// ---------- P07 · hierve, espera unos 30 segundos y vierte ----------
function p07(L,t){const c=T.c07,xb=T.x_boil9,xw=T.x_wait9,xp=T.x_before,fin=T.c08a;
 const f=1-eio(seg(t,xb+.05,xb+.35)),cuna=1-seg(t,xw-.1,xp-.1),vap=lerp(1.4,.45,eio(seg(t,xb+.2,xp-.1))),v=eio(seg(t,xp-.25,xp+.3));
 const cm=ruta(t,[[c,540,1000,1],[xp-.2,540,1000,1.03],[fin,690,960,1.3]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{mesada(L,t,{fuego:f,reloj:1,cuna,moja:seg(t,xp+.25,xp+.6),gotea:seg(t,xp+.5,xp+.8)*.5,nivel:.06+.2*seg(t,xp+.5,fin)});
  const kx=L+lerp(300,470,v),ky=lerp(1340,1010,v),rot=.5*v,p=pico(kx,ky,1.05,{rot});
  if(v>.9)chorro(p[0],p[1],L+800,818,13,t,.15);
  hervidor(kx,ky,1.05,{rot,tiembla:Math.sin(t*43)*.016*f});vapor(p[0],p[1]-6,t,vap*(1-v*.6),1.2,8);if(v>.9)vapor(L+800,810,t,.5,1,5);
  if(v>0){const hx=kx-30,hy=ky-400*1.05-20+60*(1-v),o=origen(lerp(L-500,hx,v),lerp(hy-300,hy,v),1.25,1.2,1,150,30);manoLado(o[0],o[1],1.25,1.2,1,Object.assign({},MANO,{curl:[.6,.64,.68,.7],pulgar:.3}))}})}
// ---------- P08a · la espera corta la deja en el rango ----------
function p08a(L,t){const c=T.c08a,xr=T.x_right,temp=lerp(212,200,eio(seg(t,c+.3,xr+.1)))+Math.sin(t*9)*.35;
 meson(L);hervidorArriba(L+150,560,t,.35);X.strokeStyle=ACERO2;X.lineWidth=22;X.lineCap='round';X.beginPath();X.moveTo(L+420,880);X.lineTo(L+250,640);X.stroke();dial(L+540,1080,lerp(330,350,seg(t,c,T.c08b)),temp,{})}
// ---------- P08b · si se espera de más: taza pálida, que se aparta ----------
function conDial(L,x,temp,cafe,dx){X.strokeStyle=ACERO2;X.lineWidth=14;X.lineCap='round';X.beginPath();X.moveTo(L+x+dx+60,1150);X.lineTo(L+x+dx+60,900);X.stroke();dial(L+x+dx+60,800,150,temp,{});taza(L+x+dx,1380,1.5,{cafe,asa:x>540?1:-1})}
function p08b(L,t){const c=T.c08b,xd=T.x_dont,xb=T.x_below,xw=T.x_weak,baja=eio(seg(t,xd-.1,xb+.3)),ap=eio(seg(t,xw-.05,xw+.6));
 cam(L,540,1000,lerp(1,1.05,seg(t,c,T.c09)),540,1000,()=>{cocina(L);conDial(L,270,200+Math.sin(t*9)*.3,C_OK,0);vapor(L+270,1080,t,.55,1,5);
  conDial(L,790,lerp(200,178,baja),mez(C_OK,C_PAL,eio(seg(t,xb-.2,xb+.5))),ap*560);vapor(L+790+ap*560,1080,t,.55*(1-baja),1,5);
  const lleg=eio(seg(t,xw-.5,xw-.05));if(lleg>0){const hx=L+790+ap*560+250+(1-lleg)*500,hy=1250,o=origen(hx,hy,0,1.25,-1,118,44);manoLado(o[0],o[1],0,1.25,-1,Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.35}))}})}
// ---------- P09 · prueba el café y deja la taza en primer plano; cierre ----------
function p09(L,t){const c=T.c09,k=T.x_tell;
 const ty=ruta(t,[[c,1330],[c+.45,952],[c+.85,946],[c+1.25,1420],[k+.5,1780]])[0],trot=-.3*golpe(t,c+.25,.8),s=eio(seg(t,c+1.05,c+1.5));
 const cm=ruta(t,[[c,540,1000,1],[k-.1,540,1010,1.02],[k+.7,560,1400,1.1]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{cocina(L);persona(L,t,{boca:{s:.75*s},ty,trot,cafe:C_OK});vapor(L+570,ty-250,t,.6,1,5)});
 cierreCanal(L,t,k)}

window.DC_CAFE={cocina,meson,vapor,llama,hervidor,pico,chorro,gotero,taza,reloj30,boca,persona,tazaArriba,perilla,quemador,mez,golpe,ruta,MANO,PIEL,PIEL2,CREMA,ACERO,ACERO2,NEGRO,C_OSC,C_OK,C_PAL,MOLIDO};   // piezas del canal, para Coffee 17h
NUEVOS.dc_coffee21_p01a=SET(p01a);NUEVOS.dc_coffee21_p01b=SET(p01b);NUEVOS.dc_coffee21_p02=SET(p02);NUEVOS.dc_coffee21_p03=SET(p03);NUEVOS.dc_coffee21_p04=SET(p04);NUEVOS.dc_coffee21_p05=SET(p05);
NUEVOS.dc_coffee21_p06=SET(p06);NUEVOS.dc_coffee21_p07=SET(p07);NUEVOS.dc_coffee21_p08a=SET(p08a);NUEVOS.dc_coffee21_p08b=SET(p08b);NUEVOS.dc_coffee21_p09=SET(p09);
})();
// ===== DC · COFFEE21 · FIN =====
</script>
