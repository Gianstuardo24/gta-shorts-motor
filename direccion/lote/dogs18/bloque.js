<script>
// ===== DC · DOGS18 · INICIO ===== (Dogs 18h · STOP Buying RED TOYS For Your Dog · paquete 2 del lote del 27-nov)
// Regla del paquete: al comparar se mantienen objeto, luz y posición; solo cambia la paleta. Nunca blanco y negro total, nunca rojo invisible.
(function(){
const {LIN,K,cap,trazo,manoLado,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
// ---------- la paleta: V = cuánto se ve "como el perro" (dos tipos de conos); G = casi gris (la creencia antigua) ----------
let V=0,G=0;const _c={};
function vis(hex){const k=hex+(V*50|0)+'_'+(G*50|0);if(_c[k])return _c[k];
 let r=parseInt(hex.slice(1,3),16)/255,g=parseInt(hex.slice(3,5),16)/255,b=parseInt(hex.slice(5,7),16)/255;
 if(V>0){const lin=c=>c<=.04045?c/12.92:Math.pow((c+.055)/1.055,2.4),ung=c=>{c=Math.max(0,Math.min(1,c));return c<=.0031308?c*12.92:1.055*Math.pow(c,1/2.4)-.055};
  const R=lin(r),Gn=lin(g),B=lin(b);let r2=ung(.367322*R+.860646*Gn-.227968*B),g2=ung(.280085*R+.672501*Gn+.047413*B),b2=ung(-.01182*R+.04294*Gn+.968881*B);
  const dr=Math.max(0,r-Math.max(g,b))*(1-g/Math.max(r,.01)),dg=Math.max(0,g-Math.max(r,b)),sat=.95-.7*dr-.35*dg,osc=1-.55*dr,   // el rojo queda oscuro y turbio; el amarillo y el azul se mantienen
  y=.299*r2+.587*g2+.114*b2;
  r2=(y+(r2-y)*sat)*osc;g2=(y+(g2-y)*sat)*osc;b2=(y+(b2-y)*sat)*osc;r=lerp(r,r2,V);g=lerp(g,g2,V);b=lerp(b,b2,V)}
 if(G>0){const y=.299*r+.587*g+.114*b;r=lerp(r,y,G);g=lerp(g,y,G);b=lerp(b,y,G)}
 return _c[k]=`rgb(${Math.round(r*255)},${Math.round(g*255)},${Math.round(b*255)})`}
const ROJO='#e53935',AZUL='#2f6fdb',AMA='#f2c21a',PASTO='#3f9a46',PASTO2='#33873b',PASTO3='#55ad5b',SETO='#235a2f',SETO2='#1b4a26',SETO3='#2c6b39';
const perroV=o=>Object.assign({pose:'parado',color:vis('#d9a35b'),color2:vis('#f3d9b0'),oscuro:vis('#a8723a'),lejos:vis('#b07f45'),collar:'rosa',cola:6},o||{});

function pelota(x,y,r,hex,giro,sinSombra){if(!sinSombra){X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.ellipse(x+r*.08,y+r*.97,r*.92,r*.16,0,0,7);X.fill()}
 X.fillStyle=vis(hex);X.beginPath();X.arc(x,y,r,0,7);X.fill();
 X.save();X.beginPath();X.arc(x,y,r,0,7);X.clip();
 X.translate(x,y);X.rotate(giro||0);X.strokeStyle='rgba(255,255,255,.5)';X.lineWidth=r*.07;X.beginPath();X.arc(-r*1.15,0,r*.92,-1,1);X.stroke();X.beginPath();X.arc(r*1.15,0,r*.92,Math.PI-1,Math.PI+1);X.stroke();X.rotate(-(giro||0));
 const g=X.createRadialGradient(-r*.35,-r*.4,r*.08,0,0,r);g.addColorStop(0,'rgba(255,255,255,.30)');g.addColorStop(.5,'rgba(255,255,255,0)');g.addColorStop(.62,'rgba(0,0,0,0)');g.addColorStop(1,'rgba(0,0,0,.30)');X.fillStyle=g;X.fillRect(-r,-r,2*r,2*r);X.restore();
 X.strokeStyle=LIN;X.lineWidth=3;X.beginPath();X.arc(x,y,r,0,7);X.stroke()}
function briznas(L,y,n,h,x0,dx,t,sem,col){X.fillStyle=vis(col);for(let i=0;i<n;i++){const x=L+x0+i*dx+rnd(i+sem)*dx,hh=h*(.55+rnd(i*3+sem)*.9),s=Math.sin(t*1.6+i*.7+sem)*hh*.13,w=dx*.42+9;X.beginPath();X.moveTo(x-w/2,y+2);X.quadraticCurveTo(x+s*.4-w*.1,y-hh*.6,x+s,y-hh);X.quadraticCurveTo(x+s*.4+w*.3,y-hh*.5,x+w/2,y+2);X.closePath();X.fill()}}
function jardin(L,yh,t){X.fillStyle=vis(SETO);X.fillRect(L-1700,-1700,5600,7000);
 for(let i=0;i<46;i++){const x=L-1650+i*118+rnd(i)*70,y=yh-40-rnd(i+50)*380;X.fillStyle=vis(i%3===0?SETO3:i%3===1?SETO2:SETO);X.beginPath();X.arc(x,y,96+rnd(i+9)*64,0,7);X.fill()}
 X.fillStyle=vis(PASTO);X.fillRect(L-1700,yh,5600,5000);
 for(let i=0;i<11;i++){X.fillStyle=vis(i%2?PASTO2:PASTO3);X.globalAlpha=.32;X.fillRect(L-1700,yh+30+i*i*13+i*64,5600,36+i*9);X.globalAlpha=1}
 briznas(L,yh+2,150,34,-1700,37,t,7,PASTO3);briznas(L,yh+2,150,24,-1690,37,t,31,PASTO)}
// perro del canal de espaldas, en primer plano: marca que la imagen es "lo que él ve"
function perroAtras(x,y,s,o,t){o=o||{};const c=vis('#d9a35b'),osc=vis('#a8723a');X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 const B=[[-94,0],[-106,-52],[-90,-122],[-64,-184],[-50,-226],[50,-226],[64,-184],[90,-122],[106,-52],[94,0]];
 _rel(B,c,()=>{const g=X.createLinearGradient(-106,0,106,0);g.addColorStop(0,'rgba(0,0,0,.16)');g.addColorStop(.42,'rgba(255,255,255,.07)');g.addColorStop(1,'rgba(0,0,0,.12)');X.fillStyle=g;X.fillRect(-120,-240,240,250)});
 X.fillStyle=vis('#d94f72');rr(-50,-236,100,22,10);X.fill();
 X.translate(0,-250);X.rotate(o.incl||0);const gi=o.gira||0;
 if(Math.abs(gi)>.05){X.fillStyle=c;X.beginPath();X.ellipse(gi*62,-34,34,24,0,0,7);X.fill();X.fillStyle='#2b1b14';X.beginPath();X.ellipse(gi*92,-38,10,9,0,0,7);X.fill()}
 X.fillStyle=c;X.beginPath();X.ellipse(0,-46,66,60,0,0,7);X.fill();
 {const g=X.createRadialGradient(-10,-66,10,0,-46,70);g.addColorStop(0,'rgba(255,255,255,.10)');g.addColorStop(1,'rgba(0,0,0,.12)');X.fillStyle=g;X.beginPath();X.ellipse(0,-46,66,60,0,0,7);X.fill()}
 X.fillStyle=osc;[-1,1].forEach(q=>{X.save();X.translate(q*56,-78);X.rotate(q*(.18-(o.or||0)*.3));X.beginPath();X.ellipse(q*8,34,24,46,0,0,7);X.fill();X.restore()});
 X.restore()}
// el perro asoma desde abajo (coordenadas de pantalla): a = cuánto asoma
function asoma(L,a,t,o){if(a<=0)return;o=o||{};perroAtras(L+(o.x||250),2330-eio(a)*330,2.3,{gira:o.gira||0,incl:(o.gira||0)*.07+Math.sin(t*1.2)*.012,or:o.or||0},t)}

// ---------- P01a · la mano elige la pelota roja ----------
const MANO={manga:'#3d7ea6',puno:'#356e92'};
function tienda(L){X.fillStyle='#2a2740';X.fillRect(L-900,-900,2900,3900);X.fillStyle='rgba(255,255,255,.05)';for(let y=430;y<1120;y+=74)for(let x=-200;x<1300;x+=74){X.beginPath();X.arc(L+x,y,7,0,7);X.fill()}
 X.fillStyle='#8a6240';X.fillRect(L-900,1300,2900,58);X.fillStyle='rgba(255,255,255,.12)';X.fillRect(L-900,1300,2900,8);X.fillStyle='#6f4d31';X.fillRect(L-900,1358,2900,28);X.fillStyle='#1f1c30';X.fillRect(L-900,1386,2900,1600)}
function p01a(L,t){const fin=T.c01b,ag=eio(seg(t,.3,.52)),sube=eio(seg(t,.55,fin-.05));
 const bx=L+540,by=lerp(1150,1040,sube),r=150;
 const llega=eio(seg(t,.02,.46)),an=-.95,HS=1.5,gx=bx+r*.50,gy=by-r*.62,hx=lerp(L+1300,gx,llega),hy=lerp(380,gy,llega),o=origen(hx,hy,an,HS,-1,118,44);
 const cu=lerp(.1,.62,ag),mo=p=>manoLado(o[0],o[1],an,HS,-1,Object.assign({},MANO,{curl:[cu,cu+.04,cu+.08,cu+.1],pulgar:lerp(.8,.36,ag),pulgarCurl:.1+.25*ag,parte:p}));
 const z=lerp(1,1.4,sube);
 cam(L,540,lerp(1100,1040,sube),z,540,lerp(1000,1050,sube),()=>{tienda(L);pelota(L+215,1150,150,AZUL);pelota(L+865,1150,150,AMA);
  mo('atras');pelota(bx,by,r,ROJO,0,sube>.05);mo('pulgar')})}
// ---------- P01b · la misma pelota, ahora en el pasto: cambia la paleta ----------
function p01b(L,t){const c=T.c01b,xs=T.x_see,xw=T.x_wrong;
 V=eio(seg(t,xs-.05,xs+.5))*(1-eio(seg(t,xw-.66,xw-.3))*(1-eio(seg(t,xw+.04,xw+.4))));G=0;   // en "wrong colors" vuelve un instante a nuestra paleta para comparar
 const cm=ruta(t,[[c,540,1200,1.4,540,1050],[xs,540,1200,1.16,540,1040],[T.c02,540,1200,1.05,540,1060]]);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>{jardin(L,700,t);pelota(L+540,1200,150,ROJO);briznas(L,1362,16,46,330,27,t,3,PASTO3)});
 asoma(L,seg(t,xs+.1,xs+.6),t,{or:.5})}
// ---------- P02 · la creencia antigua: casi gris ----------
function p02(L,t){const c=T.c02,xb=T.x_black;V=0;G=.86*eio(seg(t,xb-.12,xb+.3));
 const gi=ruta(t,[[c,-.9],[c+.7,-.9],[c+1.2,0],[c+1.6,0],[c+2.1,.9]])[0];
 cam(L,540,1050,lerp(1,1.06,seg(t,c,T.c03)),540,1000,()=>{jardin(L,700,t);pelota(L+270,1090,92,ROJO);pelota(L+545,1010,84,AZUL);pelota(L+815,1100,92,AMA);briznas(L,1188,40,30,60,26,t,5,PASTO3)});
 asoma(L,1,t,{x:520,gira:gi,or:.4})}
// ---------- P03 · 1989: dos discos de color en la placa de prueba (cenital) ----------
function disco(x,y,r,hex,a,giro){X.fillStyle='#14181d';X.beginPath();X.arc(x,y,r+12,0,7);X.fill();X.fillStyle='#262c33';X.beginPath();X.arc(x,y,r,0,7);X.fill();
 if(a>0){X.save();X.globalAlpha=a;X.translate(x,y);X.rotate(giro||0);X.fillStyle=vis(hex);X.beginPath();X.arc(0,0,r,0,7);X.fill();X.fillStyle='rgba(255,255,255,.22)';X.beginPath();X.moveTo(0,0);X.arc(0,0,r,-.5,.5);X.closePath();X.fill();X.fillStyle='rgba(0,0,0,.14)';X.beginPath();X.moveTo(0,0);X.arc(0,0,r,Math.PI-.5,Math.PI+.5);X.closePath();X.fill();X.restore()}
 X.strokeStyle='rgba(255,255,255,.18)';X.lineWidth=4;X.beginPath();X.arc(x,y,r+12,0,7);X.stroke()}
function p03(L,t){const c=T.c03,xs=T.x_sci,xd=T.x_dogs3,xc=T.x_color3,fin=T.c04;V=0;G=0;
 X.fillStyle='#3a2a22';X.fillRect(L-400,-500,1900,2900);X.fillStyle='rgba(0,0,0,.10)';for(let i=0;i<12;i++)X.fillRect(L-400,i*190-60,1900,54);
 // calendario de escritorio: la hoja cae en 1989
 const cae=back(seg(t,c+.08,c+.5));X.save();X.translate(L+540,620);X.rotate(-.05);X.fillStyle='rgba(0,0,0,.28)';rr(-196,-150,410,330,18);X.fill();rr(-205,-165,410,330,18);X.fillStyle='#fbf7ec';X.fill();trazo(LIN,3);
 X.save();rr(-205,-165,410,330,18);X.clip();X.fillStyle='#c0392b';X.fillRect(-205,-165,410,74);X.restore();X.fillStyle='#f2efe6';[-100,100].forEach(v=>{X.beginPath();X.arc(v,-128,15,0,7);X.fill()});
 X.save();X.translate(0,48);X.scale(1,Math.max(.02,cae));txt('1989',0,0,150,'#2a2019',{w:380});X.restore();X.restore();
 // placa de prueba: entra desde la derecha
 const en=eio(seg(t,xs-.1,xs+.55)),px=L+150+(1-en)*1100,gir=Math.pow(seg(t,fin-.55,fin),2)*7;
 X.fillStyle='rgba(0,0,0,.3)';rr(px+12,1016,780,400,40);X.fill();rr(px,1000,780,400,40);X.fillStyle='#4a5560';X.fill();trazo(LIN,3);X.fillStyle='rgba(255,255,255,.08)';rr(px+16,1014,748,22,11);X.fill();
 disco(px+150,1200,108,AZUL,eio(seg(t,xd-.05,xd+.3)),gir);disco(px+390,1200,108,'#000000',0);disco(px+630,1200,108,AMA,eio(seg(t,xc-.2,xc+.15)),gir)}
// ---------- P04 · tres tipos de conos contra dos ----------
function cono(x,y,s,hex,rot){if(s<=0)return;X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.lineJoin='round';
 X.fillStyle=vis(hex);X.beginPath();X.moveTo(0,-176);X.quadraticCurveTo(28,-124,60,-12);X.quadraticCurveTo(72,72,0,94);X.quadraticCurveTo(-72,72,-60,-12);X.quadraticCurveTo(-28,-124,0,-176);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle='rgba(255,255,255,.26)';X.beginPath();X.ellipse(-22,-14,12,62,.12,0,7);X.fill();X.fillStyle='rgba(0,0,0,.16)';X.beginPath();X.ellipse(0,60,46,22,0,0,7);X.fill();X.restore()}
function busto(x,y){X.fillStyle='#e9e2d2';X.beginPath();X.arc(x,y-64,58,0,7);X.fill();X.beginPath();X.moveTo(x-112,y+92);X.quadraticCurveTo(x-104,y+4,x,y+4);X.quadraticCurveTo(x+104,y+4,x+112,y+92);X.closePath();X.fill()}
function cabezaPerro(x,y){X.fillStyle='#e9e2d2';[-1,1].forEach(d=>{X.save();X.translate(x+d*62,y-70);X.rotate(d*.3);X.beginPath();X.ellipse(d*10,34,28,60,0,0,7);X.fill();X.restore()});X.beginPath();X.ellipse(x,y-40,70,64,0,0,7);X.fill();X.beginPath();X.ellipse(x,y+10,42,36,0,0,7);X.fill();X.fillStyle='#22324a';X.beginPath();X.ellipse(x,y-4,15,11,0,0,7);X.fill()}
function p04(L,t){const c=T.c04,x3=T.x_three,xd=T.x_dogs4,x2=T.x_two;V=0;G=0;
 X.fillStyle='#22324a';X.fillRect(L-400,-500,1900,2900);X.fillStyle='#1c3b40';X.fillRect(L+540,-500,1400,2900);X.fillStyle='rgba(255,255,255,.14)';X.fillRect(L+536,430,8,1160);
 busto(L+270,620);cabezaPerro(L+810,628);
 const gir=k=>(1-eio(seg(t,k,k+.45)))*-5,es=k=>back(seg(t,k,k+.38));
 [[112,'#3f7fe0'],[270,'#49b35a'],[428,'#e5483a']].forEach((q,i)=>{const k=i===0?c+.02:x3-.08+(i-1)*.22+.1;cono(L+q[0],1130+Math.sin(t*2+i)*8,es(k)*1.06,q[1],gir(k))});
 [[722,'#3f7fe0'],[898,AMA]].forEach((q,i)=>{const k=i===0?xd-.05:x2-.1;cono(L+q[0],1130+Math.sin(t*2+i+2)*8,es(k)*1.06,q[1],gir(k))});
 // base común (mismo eje)
 X.fillStyle='rgba(255,255,255,.14)';rr(L+40,1290,460,10,5);X.fill();rr(L+580,1290,460,10,5);X.fill()}
// ---------- P05 · azules y amarillos; el rojo se vuelve oscuro y turbio ----------
function p05(L,t){const c=T.c05,xm=T.x_muddy;V=eio(seg(t,xm-.1,xm+.45));G=0;
 X.fillStyle='#262d38';X.fillRect(L-400,-500,1900,2900);X.fillStyle='#343d4b';X.fillRect(L-400,1290,1900,1700);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L-400,1290,1900,8);
 const salto=k=>-70*golpe(t,k-.05,.42);
 pelota(L+215,1150+salto(T.x_blues),140,AZUL);pelota(L+540,1150+salto(T.x_yellows),140,AMA);pelota(L+865,1150+salto(T.x_reds),140,ROJO);
 asoma(L,seg(t,xm,xm+.5),t,{x:540,or:.5,gira:.5*eio(seg(t,xm+.6,xm+1.1))})}
// ---------- P06 · a ras de pasto: el pasto se apaga y la pelota roja casi se pierde ----------
function p06(L,t){const c=T.c06,xd=T.x_dull,xr=T.x_red7,xb=T.x_blends;G=0;
 const vp=eio(seg(t,xd-.3,xd+.3)),vb=eio(seg(t,xb-.45,xb+.1)),z=lerp(1,1.14,eio(seg(t,c,T.c07)));
 cam(L,540,1080,z,540,1020,()=>{V=vp;jardin(L,1020,t);
  V=vb;pelota(L+540,960+4*golpe(t,xr-.1,.4),128,ROJO);
  V=vp;briznas(L,1100,60,58,-60,21,t,11,PASTO3);briznas(L,1100,50,84,-70,25,t,23,PASTO);
  X.fillStyle=vis(PASTO2);X.fillRect(L-400,1096,1900,1400);briznas(L,1500,34,330,-120,38,t,41,PASTO2);briznas(L,1560,26,430,-140,50,t,57,PASTO)});
 V=Math.max(vp,vb);asoma(L,seg(t,xd-.5,xd),t,{x:230,or:.4,gira:.6})}
// ---------- P07 · pasa de largo: la pelota sigue ahí, con poco contraste ----------
function p07(L,t){const c=T.c07,xh=T.x_hard,xr=T.x_run,xp=T.x_past;V=1;G=0;
 const dx=ruta(t,[[c,60],[xh+.2,150],[xr-.15,560],[xp+.25,1380],[T.c08,1470]])[0],cx=lerp(520,1140,eio(seg(t,xh+.5,xp+.5)));
 const corre=t>xh+.2&&t<xp+.25,huele=eio(seg(t,xp+.2,xp+.5));
 cam(L,cx,1000,1,540,1000,()=>{jardin(L,1180,t);pelota(L+960,1452,60,ROJO);briznas(L,1512,30,44,760,14,t,13,PASTO3);
  perro(L+dx,1500,2.0,t,perroV({camina:corre,inclina:.06+.3*huele-.14*golpe(t,c+.5,.7),orejas:.1,mira:.4}));
  briznas(L,1530,150,60,-900,19,t,71,PASTO2)})}
// ---------- P08 · azul y amarillo resaltan; el perro elige ----------
function p08(L,t){const c=T.c08,xb=T.x_blue,xy=T.x_yellow,xt=T.x_those,k=T.x_tell;V=1;G=0;
 const cae=(k0,y1)=>{const u=seg(t,k0-.3,k0+.25);return lerp(-200,y1,u*u)-(u>=1?46*Math.abs(Math.sin((t-k0-.25)*7))*Math.exp(-(t-k0-.25)*4):0)};
 const dx=ruta(t,[[xt-.1,-360],[xt+1.2,250]])[0],sienta=seg(t,xt+1.2,xt+1.36),z=lerp(1,1.08,eio(seg(t,c,k)));
 cam(L,540,1300,z,540,1300,()=>{jardin(L,900,t);pelota(L+880,1120,54,ROJO);briznas(L,1170,10,34,820,14,t,3,PASTO3);
  pelota(L+545,cae(xb,1548),90,AZUL,t>xb+.2?0:t*6);pelota(L+800,cae(xy,1480),84,AMA,t>xy+.2?0:t*6);
  if(sienta<1){X.save();X.globalAlpha=1-sienta;perro(L+dx,1640,1.5,t,perroV({camina:t<xt+1.2,inclina:.2*eio(seg(t,xt+.9,xt+1.2)),mira:.4}));X.restore()}
  if(sienta>0){X.save();X.globalAlpha=sienta;perro(L+300,1640,1.5,t,perroV({pose:'sentado',inclina:.12-.1*golpe(t,k+.6,.5),orejas:.2,mira:.5}));X.restore()}
  briznas(L,1668,70,40,-200,21,t,81,PASTO2)});
 cierreCanal(L,t,k)}

NUEVOS.dc_dogs18_p01a=SET(p01a);NUEVOS.dc_dogs18_p01b=SET(p01b);NUEVOS.dc_dogs18_p02=SET(p02);NUEVOS.dc_dogs18_p03=SET(p03);NUEVOS.dc_dogs18_p04=SET(p04);
NUEVOS.dc_dogs18_p05=SET(p05);NUEVOS.dc_dogs18_p06=SET(p06);NUEVOS.dc_dogs18_p07=SET(p07);NUEVOS.dc_dogs18_p08=SET(p08);
})();
// ===== DC · DOGS18 · FIN =====
</script>
