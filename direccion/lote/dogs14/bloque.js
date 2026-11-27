<script>
// ===== DC · DOGS14 · INICIO ===== (Dogs 14h · YOUR DOG KNOWS WHAT YOU'RE HIDING · paquete 1 del lote del 27-nov)
// Regla del paquete: la persona se ve igual tranquila y estresada; la señal (rastro) solo aparece cuando se explica el olor.
(function(){
const {LIN,K,cap,trazo,manoArriba,cam,cierreCanal,SET}=window.DC;
const PIEL='#e8b28c',PIEL2='#cf9670',PELO='#3a2a22',CAMISA='#2f6b5a',CAMISA2='#27594b',ROS='#ff4f9a';
const PERRO={pose:'sentado',color:'#d9a35b',collar:'rosa',cola:6};
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}

// ---------- rastro abstracto del olor (único elemento "invisible" del video) ----------
function rastro(P,t,u,o){o=o||{};if(u<=0)return;const N=70,n=P.length,pts=[];
 function cr(q){const f=Math.max(0,Math.min(.9999,q))*(n-1),i=Math.floor(f),w=f-i,p0=P[Math.max(0,i-1)],p1=P[i],p2=P[i+1],p3=P[Math.min(n-1,i+2)];
  const h=(a,b,c,d)=>.5*((2*b)+(-a+c)*w+(2*a-5*b+4*c-d)*w*w+(-a+3*b-3*c+d)*w*w*w);return [h(p0[0],p1[0],p2[0],p3[0]),h(p0[1],p1[1],p2[1],p3[1])]}
 for(let i=0;i<=N;i++){const q=i/N*u,p=cr(q),p2=cr(q+.012),dx=p2[0]-p[0],dy=p2[1]-p[1],d=Math.hypot(dx,dy)||1,amp=(o.amp||15)*Math.sin(Math.min(1,q*5)*1.57)*Math.sin(Math.min(1,(1.02-q)*7)*1.57),of=Math.sin(q*10-t*3.4)*amp;pts.push([p[0]-dy/d*of,p[1]+dx/d*of])}
 X.save();X.lineCap='round';X.lineJoin='round';const s=o.s||1,a=o.a===undefined?1:o.a;
 [[56,.17,ROS],[32,.36,ROS],[13,.92,'#ffd3e6']].forEach(([w,al,c])=>{X.strokeStyle=c;X.globalAlpha=al*a;X.lineWidth=w*s;X.beginPath();X.moveTo(pts[0][0],pts[0][1]);for(let i=1;i<pts.length;i++)X.lineTo(pts[i][0],pts[i][1]);X.stroke()});
 X.globalAlpha=.9*a;X.fillStyle='#ffe6f1';for(let j=0;j<7;j++){const q=((t*.24+j/7)%1);if(q<u-.02){const p=cr(q),r=(5+3*Math.sin(j*2.1))*s;X.beginPath();X.arc(p[0]+Math.sin(t*2+j)*12*s,p[1]+Math.cos(t*1.7+j*1.3)*12*s,r,0,7);X.fill()}}
 X.restore()}

// ---------- frascos ----------
function gasaDentro(w,s){X.fillStyle='#f6f3ea';X.strokeStyle='rgba(40,27,18,.4)';X.lineWidth=2;X.beginPath();X.moveTo(-w*.30,-10*s);X.lineTo(-w*.34,-54*s);X.lineTo(-w*.04,-74*s);X.lineTo(w*.29,-58*s);X.lineTo(w*.32,-12*s);X.closePath();X.fill();X.stroke();X.beginPath();X.moveTo(-w*.04,-74*s);X.lineTo(w*.02,-32*s);X.lineTo(w*.32,-12*s);X.moveTo(w*.02,-32*s);X.lineTo(-w*.30,-10*s);X.stroke()}
function frasco(x,yb,o){o=o||{};const s=o.s||1,w=150*s,h=190*s;X.save();X.translate(x,yb);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.18)';X.beginPath();X.ellipse(0,3,w*.56,9*s,0,0,7);X.fill();
 if(o.gasa!==false)gasaDentro(w,s);
 rr(-w/2,-h,w,h,22*s);X.fillStyle='rgba(214,236,238,.40)';X.fill();X.strokeStyle='rgba(30,50,55,.8)';X.lineWidth=4*s;X.stroke();
 X.fillStyle='rgba(255,255,255,.5)';rr(-w/2+14*s,-h+28*s,11*s,h-64*s,5*s);X.fill();
 rr(-w/2+10*s,-h-14*s,w-20*s,22*s,8*s);X.fillStyle='rgba(214,236,238,.65)';X.fill();X.stroke();
 if(o.letra!==undefined){rr(-38*s,-h+58*s,76*s,68*s,8*s);X.fillStyle='#f6f0df';X.fill();X.strokeStyle='rgba(40,27,18,.5)';X.lineWidth=2;X.stroke();if(o.letra)txt(o.letra,0,-h+95*s,50*s,'#2a2019',{w:70*s})}
 if(o.tapa){rr(-w/2-4*s,-h-30*s,w+8*s,36*s,10*s);X.fillStyle='#ece7d9';X.fill();X.strokeStyle='rgba(30,50,55,.8)';X.lineWidth=4*s;X.stroke();X.fillStyle='rgba(0,0,0,.08)';X.fillRect(-w/2,-h-8*s,w,8*s)}
 X.restore()}

// ---------- la entrada de la casa: muro, espejo, persona parcial, perro del canal ----------
function muro(L){const g=X.createLinearGradient(0,-200,0,1500);g.addColorStop(0,'#3a5674');g.addColorStop(1,'#4c6e8f');X.fillStyle=g;X.fillRect(L-900,-700,2900,2500);
 X.fillStyle='#3a5571';X.fillRect(L-900,1440,2900,270);X.fillStyle='#31485f';X.fillRect(L-900,1440,2900,10);
 X.fillStyle='#e6dfce';X.fillRect(L-900,1700,2900,36);X.fillStyle='#7b5236';X.fillRect(L-900,1736,2900,1200);
 X.fillStyle='rgba(0,0,0,.13)';for(let i=0;i<10;i++)X.fillRect(L-900,1790+i*58,2900,3)}
function boca(cx,cy,w,u){const up=-11*u,op=Math.max(0,(u-.4)/.6),yt=cy+up,c1=cy+up+10*u,c2=c1+38*op;X.lineCap='round';X.lineJoin='round';
 X.beginPath();X.moveTo(cx-w/2,yt);X.quadraticCurveTo(cx,c1+(1-u)*3,cx+w/2,yt);X.quadraticCurveTo(cx,c2+(1-u)*3,cx-w/2,yt);X.closePath();
 if(op>0){X.fillStyle='#fff';X.fill()}X.strokeStyle='#8a3d33';X.lineWidth=6.5;X.stroke();
 if(u>.5){const a=(u-.5)*2;X.strokeStyle=`rgba(138,61,51,${.7*Math.min(1,a)})`;X.lineWidth=4;[-1,1].forEach(d=>{X.beginPath();X.arc(cx+d*(w/2+9),yt-2,9,d>0?-.9:Math.PI-.5,d>0?.5:Math.PI+.9);X.stroke()})}}
function pulgarArriba(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 X.fillStyle=CAMISA;rr(-52,64,104,220,14);X.fill();trazo(LIN,3);X.fillStyle=CAMISA2;X.fillRect(-52,64,104,18);
 X.fillStyle=PIEL;cap(-34,-10,-30,-86,22);X.fill();trazo(LIN,3);
 rr(-56,-22,112,96,26);X.fillStyle=PIEL;X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(120,70,45,.4)';X.lineWidth=3;[2,24,46].forEach(v=>{X.beginPath();X.moveTo(-2,-2+v);X.lineTo(50,-2+v);X.stroke()});
 X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(-31,-92,10,12,0,0,7);X.fill();X.restore()}
function reflejo(cx,o){const sh=o.sh||0,dy=-4*(o.u||0);
 // camisa y hombros
 X.fillStyle=CAMISA;X.beginPath();X.moveTo(cx-290,1100);X.lineTo(cx-262,870-sh);X.quadraticCurveTo(cx-240,800-sh,cx-150,776-sh);X.lineTo(cx-66,748-sh*.6);X.lineTo(cx+66,748-sh*.6);X.lineTo(cx+150,776-sh);X.quadraticCurveTo(cx+240,800-sh,cx+262,870-sh);X.lineTo(cx+290,1100);X.closePath();X.fill();trazo(LIN,3);
 // cuello
 X.fillStyle=PIEL2;X.beginPath();X.moveTo(cx-58,600+dy);X.lineTo(cx+58,600+dy);X.lineTo(cx+62,770-sh*.6);X.quadraticCurveTo(cx,812-sh*.6,cx-62,770-sh*.6);X.closePath();X.fill();trazo(LIN,3);
 // solapas del cuello de la camisa
 X.fillStyle=CAMISA;[-1,1].forEach(d=>{X.beginPath();X.moveTo(cx+d*70,738-sh*.6);X.lineTo(cx+d*8,822-sh*.6);X.lineTo(cx+d*96,846-sh*.8);X.lineTo(cx+d*118,772-sh);X.closePath();X.fill();trazo(LIN,3)});
 // cara de la nariz hacia abajo (los ojos quedan fuera del espejo)
 X.fillStyle=PIEL;X.beginPath();X.ellipse(cx,468+dy,134,176,0,0,7);X.fill();trazo(LIN,3);
 X.fillStyle=PIEL;[-1,1].forEach(d=>{X.beginPath();X.ellipse(cx+d*136,476+dy,18,30,0,0,7);X.fill();trazo(LIN,3)});
 const u=o.u||0;X.fillStyle=`rgba(226,120,110,${.22*Math.min(1,u)})`;[-1,1].forEach(d=>{X.beginPath();X.ellipse(cx+d*84,548+dy-6*u,30,20,0,0,7);X.fill()});
 X.strokeStyle='rgba(120,70,45,.55)';X.lineWidth=4;X.lineCap='round';X.beginPath();X.moveTo(cx-17,512+dy);X.quadraticCurveTo(cx,524+dy,cx+17,512+dy);X.stroke();
 boca(cx,578+dy,104,u);
 if(o.pulgar>0)pulgarArriba(cx+178,1150-eio(o.pulgar)*330,1.05)}
function espejo(L,o){const x=L+130,y=430,w=520,h=640;
 X.fillStyle='rgba(0,0,0,.24)';rr(x+14,y+20,w,h,40);X.fill();
 rr(x,y,w,h,40);X.fillStyle='#b98a4e';X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(255,255,255,.18)';X.lineWidth=4;rr(x+9,y+9,w-18,h-18,32);X.stroke();
 const ix=x+26,iy=y+26,iw=w-52,ih=h-52;X.save();rr(ix,iy,iw,ih,20);X.clip();
 const g=X.createLinearGradient(ix,iy,ix+iw,iy+ih);g.addColorStop(0,'#bfd0da');g.addColorStop(1,'#8ea8b8');X.fillStyle=g;X.fillRect(ix,iy,iw,ih);
 reflejo(L+390,o);
 X.fillStyle='rgba(255,255,255,.10)';X.beginPath();X.moveTo(ix+70,iy);X.lineTo(ix+170,iy);X.lineTo(ix+30,iy+ih);X.lineTo(ix-70,iy+ih);X.closePath();X.fill();
 X.restore();rr(ix,iy,iw,ih,20);trazo('rgba(40,27,18,.55)',3)}
function espalda(L,o){const sh=o.sh||0;X.lineJoin='round';
 // brazo que cuelga (lado del perro)
 X.fillStyle=PIEL2;cap(L+786,1040-sh*.5,L+772,1330,40);X.fill();trazo(LIN,3);
 X.fillStyle=PIEL;X.beginPath();X.ellipse(L+768,1378,46,60,.08,0,7);X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(120,70,45,.4)';X.lineWidth=3;[-14,6,26].forEach(v=>{X.beginPath();X.moveTo(L+748+v,1396);X.lineTo(L+746+v,1430);X.stroke()});
 // espalda
 X.fillStyle=CAMISA;X.beginPath();X.moveTo(L+800,2100);X.lineTo(L+812,1200);X.quadraticCurveTo(L+800,900,L+826,790-sh);X.quadraticCurveTo(L+850,700-sh,L+960,672-sh);X.lineTo(L+1500,640-sh);X.lineTo(L+1500,2100);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=CAMISA;cap(L+812,800-sh,L+788,1030-sh*.5,64);X.fill();trazo(LIN,3);X.fillStyle=CAMISA2;cap(L+776,1062-sh*.5,L+800,1066-sh*.5,12);X.fill();
 X.fillStyle='rgba(0,0,0,.07)';X.beginPath();X.moveTo(L+870,2100);X.lineTo(L+872,1100);X.quadraticCurveTo(L+880,860,L+930,760-sh);X.lineTo(L+850,760-sh);X.lineTo(L+812,1200);X.lineTo(L+800,2100);X.closePath();X.fill();
 // cuello y cabeza de espaldas
 X.fillStyle=PIEL2;X.beginPath();X.moveTo(L+930,540);X.lineTo(L+1100,540);X.lineTo(L+1110,690-sh*.6);X.lineTo(L+920,690-sh*.6);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=CAMISA;X.beginPath();X.moveTo(L+900,668-sh*.7);X.quadraticCurveTo(L+1010,720-sh*.7,L+1130,664-sh*.7);X.lineTo(L+1130,720-sh);X.quadraticCurveTo(L+1010,770-sh,L+896,716-sh);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=PIEL;X.beginPath();X.ellipse(L+868,452,24,40,0,0,7);X.fill();trazo(LIN,3);
 X.fillStyle=PELO;X.beginPath();X.ellipse(L+1020,410,158,196,0,0,7);X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(255,255,255,.08)';X.lineWidth=6;X.beginPath();X.arc(L+1040,400,110,2.6,4.2);X.stroke()}
function entrada(L,t,o){muro(L);espejo(L,o);
 perro(L+330,1790,2.4,t,Object.assign({},PERRO,o.perro||{}));
 espalda(L,o);
 if(o.rastro>0)rastro([[L+905,800],[L+850,985],[L+790,1150],[L+705,1228],[L+622,1232]],t,o.rastro,{amp:13})}

// ---------- P01 · gancho: la sonrisa en el espejo y la nariz ----------
function p01(L,t){const xh=T.x_hiding,xe=T.x_even,xb=T.x_but,xn=T.x_nobody,fin=T.c02;
 const u=.12+.88*Math.min(1.08,back(seg(t,.08,.62)));
 const sh=24*golpe(t,xe+.42,.8);
 const inc=lerp(.24,-.30,eio(seg(t,.12,.6)))-.11*golpe(t,xh,.24)-.11*golpe(t,xh+.34,.24)-.06*golpe(t,xe+.3,.3)-.09*golpe(t,xb+.62,.26)-.09*golpe(t,xb+.98,.26)-.10*golpe(t,xn+.05,.3)-.14*eio(seg(t,xn+.45,fin-.1));
 const ore=.22*eio(seg(t,xh-.08,xh+.18))+.10*golpe(t,xb+.6,.5);
 const c=ruta(t,[[0,540,1000,1],[xe-.07,540,992,1.045],[xb-.03,500,905,1.12],[xb-.02,535,1205,1.95],[fin,540,1180,2.1]]);   // en "But": salto directo al primer plano del perro
 cam(L,c[0],c[1],c[2],540,1000,()=>entrada(L,t,{u,sh,perro:{inclina:inc,orejas:ore,mira:.6,parpadeo:t<xn}}))}
// ---------- P02 · "say you're fine": la sonrisa de cerca ----------
function p02(L,t){const c=T.c02,xf=T.x_fine;
 cam(L,lerp(392,432,seg(t,c,T.c03)),770,1.72,540,1000,()=>entrada(L,t,{u:1+.05*golpe(t,xf,.4),sh:0,pulgar:seg(t,xf-.12,xf+.22),perro:{inclina:-.36-.07*golpe(t,c+.5,.3),orejas:.2,mira:.6}}))}
// ---------- P09 · vuelve el espejo: la misma sonrisa y, ahora, el rastro ----------
function p09(L,t){const c=T.c09,xb=T.x_butnot,k=T.x_tell;
 const ra=eio(seg(t,c+.15,xb+.35)),lleg=seg(t,xb+.1,xb+.5);
 const inc=-.30-.12*eio(lleg)-.08*golpe(t,xb+.5,.28)-.08*golpe(t,xb+.9,.28);
 const z=lerp(1,1.05,eio(seg(t,c,k-.3)));
 cam(L,540,1000,z,540,1000,()=>entrada(L,t,{u:1,sh:0,rastro:ra,perro:{inclina:inc,orejas:.25*eio(lleg),mira:.6}}));
 cierreCanal(L,t,k)}

// ---------- la sala de la prueba ----------
function sala(L){const g=X.createLinearGradient(0,-200,0,1500);g.addColorStop(0,'#4f6b5b');g.addColorStop(1,'#6a8a76');X.fillStyle=g;X.fillRect(L-1700,-700,4700,2400);
 X.fillStyle='#4a6455';X.fillRect(L-1700,1500,4700,150);X.fillStyle='#b7a388';X.fillRect(L-1700,1640,4700,1300);X.fillStyle='rgba(0,0,0,.10)';X.fillRect(L-1700,1640,4700,9)}
function perroAtras(x,y,s,o,t){const c=o.c,osc=o.osc,d=o.cd||1;X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(0,3,128,17,0,0,7);X.fill();
 X.save();X.translate(d*72,-16);X.rotate(d*(.1+Math.sin(t*(o.wag||5)+o.f)*.2));X.fillStyle=c;X.beginPath();X.moveTo(0,-15);X.quadraticCurveTo(d*74,-34,d*112,-6);X.quadraticCurveTo(d*74,10,0,15);X.closePath();X.fill();X.restore();
 const B=[[-94,0],[-106,-52],[-90,-122],[-64,-184],[-50,-226],[50,-226],[64,-184],[90,-122],[106,-52],[94,0]];
 _rel(B,c,()=>{const g=X.createLinearGradient(-106,0,106,0);g.addColorStop(0,'rgba(0,0,0,.16)');g.addColorStop(.42,'rgba(255,255,255,.07)');g.addColorStop(1,'rgba(0,0,0,.12)');X.fillStyle=g;X.fillRect(-120,-240,240,250);if(o.mancha){X.fillStyle=o.mancha;X.beginPath();X.ellipse(30,-110,44,58,.3,0,7);X.fill()}});
 X.fillStyle=osc;X.beginPath();X.ellipse(-80,-36,36,46,.2,0,7);X.fill();X.beginPath();X.ellipse(80,-36,36,46,-.2,0,7);X.fill();
 X.fillStyle=o.collar||'#d94f72';rr(-50,-236,100,22,10);X.fill();
 X.translate(0,-250-(o.sube||0));X.rotate(o.incl||0);const gi=o.gira||0;
 if(Math.abs(gi)>.05){X.fillStyle=o.hocico||c;X.beginPath();X.ellipse(gi*62,-34,34,24,0,0,7);X.fill();X.fillStyle='#2b1b14';X.beginPath();X.ellipse(gi*92,-38,10,9,0,0,7);X.fill()}
 if(o.puntas){X.fillStyle=osc;[-1,1].forEach(q=>{X.beginPath();X.moveTo(q*58,-64);X.lineTo(q*50,-128-(o.or||0)*10);X.lineTo(q*18,-90);X.closePath();X.fill()})}
 X.fillStyle=c;X.beginPath();X.ellipse(0,-46,66,60,0,0,7);X.fill();
 {const g=X.createRadialGradient(-10,-66,10,0,-46,70);g.addColorStop(0,'rgba(255,255,255,.10)');g.addColorStop(1,'rgba(0,0,0,.12)');X.fillStyle=g;X.beginPath();X.ellipse(0,-46,66,60,0,0,7);X.fill()}
 if(!o.puntas){X.fillStyle=osc;[-1,1].forEach(q=>{X.save();X.translate(q*56,-78);X.rotate(q*(.18-(o.or||0)*.3));X.beginPath();X.ellipse(q*8,34,24,46,0,0,7);X.fill();X.restore()})}
 X.restore()}
function trampillaFrente(L,ap,luz){const x=L+330,y=700,w=420,h=340;
 rr(L+496,588,88,58,14);X.fillStyle='#2c3a33';X.fill();X.fillStyle=luz>0?`rgb(${lerp(82,124,luz)|0},${lerp(96,252,luz)|0},${lerp(90,138,luz)|0})`:'#52605a';X.beginPath();X.arc(L+540,617,18,0,7);X.fill();
 X.fillStyle='rgba(0,0,0,.2)';rr(x-14,y-12,w+44,h+44,14);X.fill();rr(x-22,y-22,w+44,h+44,14);X.fillStyle='#d8d2c2';X.fill();trazo(LIN,3);
 X.save();X.beginPath();X.rect(x,y,w,h);X.clip();
 const g=X.createLinearGradient(0,y,0,y+h);g.addColorStop(0,'#f7e9c0');g.addColorStop(1,'#e4c688');X.fillStyle=g;X.fillRect(x,y,w,h);
 X.fillStyle='#b3935c';X.fillRect(x,y+h-50,w,50);[-126,0,126].forEach(d=>frasco(x+w/2+d,y+h-50,{s:.66}));
 const dy=-ap*(h+12);X.fillStyle='#bfb49c';X.fillRect(x,y+dy,w,h);X.strokeStyle='rgba(40,27,18,.45)';X.lineWidth=3;X.strokeRect(x+16,y+dy+16,w-32,h-32);rr(x+w/2-52,y+dy+h-64,104,22,10);X.fillStyle='#7d735f';X.fill();
 X.fillStyle='rgba(0,0,0,.18)';X.fillRect(x,y,w,14);X.restore();X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(x,y,w,h);
 rr(x-44,y+h+22,w+88,26,8);X.fillStyle='#d8d2c2';X.fill();trazo(LIN,3)}
const CUATRO=[{c:'#d9a35b',osc:'#a8723a',collar:'#d94f72',f:0,cd:1},{c:'#6b4a36',osc:'#4a3225',collar:'#e9c46a',f:1.7,cd:-1,puntas:true},{c:'#ece3d2',osc:'#c9b99c',collar:'#3d7ea6',f:3.1,cd:1,mancha:'#b8894f'},{c:'#3b3b44',osc:'#25252c',collar:'#e76f51',f:4.4,cd:-1,puntas:true}];
// ---------- P03 · cuatro perros frente a la trampilla ----------
function p03(L,t){const c=T.c03,x4=T.x_four,xt=T.x_test,ap=eio(seg(t,xt,xt+.5));
 const z=lerp(1,1.07,eio(seg(t,c,T.c04a)));
 cam(L,540,1060,z,540,1060,()=>{sala(L);trampillaFrente(L,ap,seg(t,xt-.05,xt+.2));
  [150,405,675,930].forEach((x,i)=>{const d=i%2?-1:1,q=1-seg(t,x4-.35,x4-.1),mira=(golpe(t,c+.2+i*.36,.85)*d-golpe(t,c+1.75+((i*3)%4)*.28,.75)*d)*q;
   const sube=26*golpe(t,x4-.1+i*.14,.32)+12*eio(seg(t,xt,xt+.3));
   perroAtras(L+x,1800,1.32,Object.assign({},CUATRO[i],{gira:mira*.95,incl:mira*.09+Math.sin(t*1.3+i)*.014,sube,or:eio(seg(t,xt-.05,xt+.2))+golpe(t,x4-.1+i*.14,.32),wag:i===0?6.5:4.5+i*.7}),t)})})}

// ---------- P04 · la muestra tranquila y, tras el reloj, la del examen (vista cenital) ----------
function mesa(L){X.fillStyle='#2c3d35';X.fillRect(L-900,-700,2900,3400);X.fillStyle='#446257';X.fillRect(L-900,-700,2900,2040);X.fillStyle='#5a7a6d';X.fillRect(L-900,1316,2900,24);X.fillStyle='rgba(0,0,0,.22)';X.fillRect(L-900,1340,2900,26);
 X.fillStyle='rgba(255,255,255,.025)';for(let i=0;i<9;i++)X.fillRect(L-900,i*170-140,2900,70)}
function gasa(x,y,s,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.16)';rr(-36,-34,80,80,8);X.fill();rr(-40,-40,80,80,8);X.fillStyle='#f6f3ea';X.fill();X.strokeStyle='rgba(40,27,18,.5)';X.lineWidth=2.5;X.stroke();
 X.strokeStyle='rgba(40,27,18,.13)';X.lineWidth=1.5;for(let i=-24;i<=24;i+=12){X.beginPath();X.moveTo(i,-34);X.lineTo(i,34);X.moveTo(-34,i);X.lineTo(34,i);X.stroke()}X.restore()}
function frascoArriba(x,y,gas){const r=118;X.fillStyle='rgba(0,0,0,.24)';X.beginPath();X.arc(x+10,y+15,r+3,0,7);X.fill();
 X.fillStyle='#cfe3e2';X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle='rgba(30,50,55,.85)';X.lineWidth=5;X.stroke();
 X.fillStyle='#93b3b0';X.beginPath();X.arc(x,y,r-22,0,7);X.fill();if(gas)gasa(x+4,y+6,1.15,.5);
 X.strokeStyle='rgba(255,255,255,.6)';X.lineWidth=7;X.lineCap='round';X.beginPath();X.arc(x,y,r-11,3.5,4.5);X.stroke()}
function tapaArriba(x,y,letra){const r=126;X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.arc(x+9,y+14,r,0,7);X.fill();X.fillStyle='#ece7d9';X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle='rgba(30,50,55,.85)';X.lineWidth=5;X.stroke();
 X.strokeStyle='rgba(0,0,0,.12)';X.lineWidth=4;X.beginPath();X.arc(x,y,r-20,0,7);X.stroke();txt(letra,x,y+6,130,'#2a2019',{w:200})}
function relojArriba(x,y,u){const r=120;X.fillStyle='rgba(0,0,0,.26)';X.beginPath();X.arc(x+10,y+15,r,0,7);X.fill();X.fillStyle='#e4572e';X.beginPath();X.arc(x,y,r,0,7);X.fill();trazo(LIN,4);
 X.fillStyle='#f7f1e1';X.beginPath();X.arc(x,y,r-26,0,7);X.fill();
 const a0=-Math.PI/2,a=a0+u*Math.PI*1.7;X.fillStyle='rgba(228,87,46,.28)';X.beginPath();X.moveTo(x,y);X.arc(x,y,r-30,a0,a);X.closePath();X.fill();
 X.strokeStyle='#2a2019';X.lineCap='round';for(let i=0;i<12;i++){const q=a0+i*Math.PI/6;X.lineWidth=i%3?4:7;X.beginPath();X.moveTo(x+Math.cos(q)*(r-40),y+Math.sin(q)*(r-40));X.lineTo(x+Math.cos(q)*(r-(i%3?54:62)),y+Math.sin(q)*(r-(i%3?54:62)));X.stroke()}
 X.strokeStyle='#2a2019';X.lineWidth=12;X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(a)*(r-58),y+Math.sin(a)*(r-58));X.stroke();X.fillStyle='#e4572e';X.beginPath();X.arc(x,y,22,0,7);X.fill();trazo(LIN,3)}
function personaArriba(L,t){const cx=L+470,b=1+.006*Math.sin(t*1.8);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(cx+12,1668,352*b,176,0,0,7);X.fill();
 X.fillStyle='#8fa3b5';X.beginPath();X.ellipse(cx,1652,342*b,170,0,0,7);X.fill();trazo(LIN,3);
 X.fillStyle='#7d92a5';X.beginPath();X.ellipse(cx,1604,124,86,0,0,7);X.fill();trazo(LIN,3);
 X.fillStyle=PIEL2;X.beginPath();X.ellipse(cx,1600,96,72,0,0,7);X.fill();trazo(LIN,3);
 X.fillStyle=PIEL;[-1,1].forEach(d=>{X.beginPath();X.ellipse(cx+d*138,1452,22,36,0,0,7);X.fill();trazo(LIN,3)});
 X.fillStyle=PELO;X.beginPath();X.ellipse(cx,1452,136,152,0,0,7);X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(255,255,255,.09)';X.lineWidth=6;X.lineCap='round';X.beginPath();X.arc(cx+8,1432,58,3.3,5.7);X.stroke();X.beginPath();X.arc(cx+8,1432,98,3.6,5.3);X.stroke()}
const GUANTE={piel:'#9fd0d6',manga:'#f1efe8',puno:'#dcd7c9',sinLapiz:true};
function manoGasa(hx,hy,conGasa){if(conGasa)gasa(hx+40,hy+34,1,.35);manoArriba(hx,hy,1.25,GUANTE)}
function hojaExamen(x,y){X.save();X.translate(x,y);X.rotate(-.07);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(-150,-100,316,224);X.fillStyle='#f7f2e3';X.fillRect(-158,-110,316,224);X.strokeStyle='rgba(40,27,18,.5)';X.lineWidth=2.5;X.strokeRect(-158,-110,316,224);
 X.strokeStyle='rgba(42,32,25,.75)';X.lineWidth=5;X.lineCap='round';[[-128,-70,60],[-128,-28,150],[-128,14,100],[-128,56,170]].forEach((q,i)=>{X.beginPath();X.moveTo(q[0],q[1]);for(let k=0;k<=q[2];k+=10)X.lineTo(q[0]+k,q[1]+Math.sin(k*.7+i*2)*5);X.stroke()});
 X.strokeStyle='#c0392b';X.lineWidth=6;X.beginPath();X.arc(96,-52,26,0,7);X.stroke();X.restore();
 X.save();X.translate(x+120,y+92);X.rotate(-.5);X.fillStyle='#e9b949';X.fillRect(-110,-9,200,18);X.strokeStyle=LIN;X.lineWidth=2;X.strokeRect(-110,-9,200,18);X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(90,-9);X.lineTo(122,0);X.lineTo(90,9);X.closePath();X.fill();X.stroke();X.fillStyle='#d98a86';X.fillRect(-128,-9,18,18);X.strokeRect(-128,-9,18,18);X.restore()}
const NUCA=[436,1596],JA=[290,930],JB=[790,930];
function cenital(L,t,o){mesa(L);relojArriba(L+540,640,o.reloj);
 frascoArriba(L+JA[0],JA[1],o.gA);frascoArriba(L+JB[0],JB[1],o.gB);
 if(o.tA>0)tapaArriba(L+JA[0]-(1-eio(o.tA))*640,JA[1],'A');if(o.tB>0)tapaArriba(L+JB[0]+(1-eio(o.tB))*640,JB[1],'B');
 if(o.hoja)hojaExamen(L+585,1105);
 personaArriba(L,t);manoGasa(L+o.h[0],o.h[1],o.conGasa)}
function gesto(t,k0,kw,kj,J){ // la mano: llega a la nuca, pasa la gasa, la lleva al frasco J y se retira
 const en=eio(seg(t,k0,k0+.5)),ir=eio(seg(t,kw+0,kj)),sal=eio(seg(t,kj+.12,kj+.62));
 let x=lerp(940,NUCA[0],en),y=lerp(2150,NUCA[1],en);
 x+=52*Math.sin((t-k0-.5)*8.5)*seg(t,k0+.45,k0+.6)*(1-seg(t,kw-.15,kw));
 x=lerp(x,J[0]-40,ir);y=lerp(y,J[1]-34,ir)-150*Math.sin(ir*Math.PI);
 x=lerp(x,1240,sal);y=lerp(y,1500,sal);return {h:[x,y],conGasa:t<kj+.06,dentro:t>=kj+.06}}
function p04a(L,t){const c=T.c04a,kj=T.x_calm-.12,g=gesto(t,c-.2,T.x_twice-.35,kj,JA);
 cenital(L,t,{reloj:eio(seg(t,T.x_min-.22,T.c04b-.04))*.94,gA:g.dentro,gB:false,tA:seg(t,kj+.25,kj+.7),tB:0,h:g.h,conGasa:g.conGasa})}
function p04b(L,t){const c=T.c04b,kj=T.x_math+.12,g=gesto(t,c-.62,T.x_math-.55,kj,JB);
 cenital(L,t,{reloj:.94,gA:true,gB:g.dentro,tA:1,tB:seg(t,kj+.14,kj+.5),hoja:true,h:g.h,conGasa:g.conGasa})}

// ---------- P05 · las muestras en pares sobre la tira de medición ----------
const PX=[200,760,1320,1880];
function p05(L,t){const c=T.c05,xs=T.x_so,xu=T.x_up;
 const cx=lerp(480,1320,eio(seg(t,c,c+2.0))),z=lerp(1,1.3,eio(seg(t,xs-.05,T.c06+.2)));
 const pen=[lerp(-300,1400,seg(t,c+.05,T.x_heart+.42))+Math.max(0,t-(T.x_heart+.42))*900,lerp(-300,1400,seg(t,c+.5,T.x_blood+.45))+Math.max(0,t-(T.x_blood+.45))*900];
 const sube=x=>{const a=seg(x,1296,1356),b=seg(x,1566,1600);return 58*eio(a)*(1-eio(b))};
 cam(L,cx,1000,z,540,1000,()=>{sala(L);
  // tira de medición: papel continuo con dos trazos (uno con latidos, uno liso)
  X.fillStyle='rgba(0,0,0,.18)';X.fillRect(L-900,592,4000,300);X.fillStyle='#f3ecd9';X.fillRect(L-900,576,4000,300);
  X.strokeStyle='rgba(60,90,100,.15)';X.lineWidth=2;for(let gx=-900;gx<3100;gx+=70){X.beginPath();X.moveTo(L+gx,576);X.lineTo(L+gx,876);X.stroke()}for(let gy=576;gy<=876;gy+=75){X.beginPath();X.moveTo(L-900,gy);X.lineTo(L+3100,gy);X.stroke()}
  X.fillStyle='rgba(60,90,100,.28)';PX.forEach(x=>{X.fillRect(L+x-281,576,3,300);X.fillRect(L+x+278,576,3,300)});
  const dest=golpe(t,xu-.05,.7);
  [[690,'#c0392b',1],[810,'#2a6f97',0]].forEach(([y0,col,lat],k)=>{const fin=pen[k];if(fin<-300)return;X.strokeStyle=col;X.lineWidth=7+3*dest;X.lineCap='round';X.lineJoin='round';X.beginPath();
   for(let x=-300;x<=fin;x+=6){let y=y0-sube(x);if(lat){const ph=((x+300)%(sube(x)>30?62:96));if(ph<8)y-=34;else if(ph<16)y+=16}if(x===-300)X.moveTo(L+x,y);else X.lineTo(L+x,y)}X.stroke();
   X.fillStyle=col;X.beginPath();X.arc(L+fin,y0-sube(fin),11,0,7);X.fill()});
  // pares de frascos; los que no cumplen bajan dentro del mesón
  PX.forEach((x,i)=>{const k=i===0?T.x_kept+.05:xu+.12+(i===3?.12:0),dy=i===2?0:560*Math.pow(seg(t,k,k+.55),2);
   X.fillStyle='#3f3a30';rr(L+x-236,1290,472,30,10);X.fill();
   if(dy<540){frasco(L+x-112,1300+dy,{letra:'A',tapa:true});frasco(L+x+112,1300+dy,{letra:'B',tapa:true})}});
  // mesón
  X.fillStyle='#a8977c';X.fillRect(L-900,1300,4000,1500);X.fillStyle='#c4b396';X.fillRect(L-900,1300,4000,26);X.fillStyle='rgba(0,0,0,.14)';X.fillRect(L-900,1326,4000,10);
  PX.forEach((x,i)=>{X.fillStyle='rgba(0,0,0,.16)';rr(L+x-236,1352,472,14,7);X.fill()})})}

// ---------- P06 · solo los frascos cruzan la trampilla ----------
function silla(x,yf){X.fillStyle='rgba(0,0,0,.18)';X.beginPath();X.ellipse(x+14,yf+5,180,15,0,0,7);X.fill();X.lineCap='round';
 X.strokeStyle='#5b4634';X.lineWidth=18;X.beginPath();X.moveTo(x-102,yf-8);X.lineTo(x-114,yf-580);X.stroke();X.beginPath();X.moveTo(x+132,yf-8);X.lineTo(x+122,yf-300);X.stroke();
 rr(x-140,yf-610,50,250,20);X.fillStyle='#7c9aa8';X.fill();trazo(LIN,3);rr(x-132,yf-330,290,48,20);X.fillStyle='#7c9aa8';X.fill();trazo(LIN,3)}
function p06(L,t){const c=T.c06,xn=T.x_never,xo=T.x_only7,xs=T.x_samples;
 const cx=lerp(150,210,seg(t,c,xn-.1))+lerp(0,720,eio(seg(t,xn-.1,xs+.2))),ap=eio(seg(t,c+.55,c+1.25)),bx=lerp(318,728,eio(seg(t,xo-.12,xo+.8))),lleg=eio(seg(t,xo+.45,xo+.95));
 cam(L,cx,1000,1,540,1000,()=>{sala(L);silla(L-70,1640);
  perro(L+1175,1640,2.0,t,Object.assign({},PERRO,{dir:-1,inclina:-.08-.12*lleg-.08*golpe(t,xs+.05,.26)-.08*golpe(t,xs+.4,.26),orejas:.22*lleg,mira:.5}));
  X.fillStyle='#34463c';X.fillRect(L+470,930,140,320);                                   // hueco de la trampilla (se ve a través)
  X.fillStyle='#d8d2c2';rr(L+236,1240,640,26,8);X.fill();trazo(LIN,3);                    // repisa que cruza el muro
  X.fillStyle='#8a7f6c';[[262,1],[826,-1]].forEach(q=>{X.beginPath();X.moveTo(L+q[0],1266);X.lineTo(L+q[0]+q[1]*150,1266);X.lineTo(L+q[0]+q[1]*150,1284);X.closePath();X.fill()});
  rr(L+bx-158,1226,316,16,6);X.fillStyle='#6f7f86';X.fill();trazo(LIN,2.5);frasco(L+bx-74,1226,{s:.9,letra:'A',tapa:true});frasco(L+bx+74,1226,{s:.9,letra:'B',tapa:true});
  X.fillStyle='#2b3a32';X.fillRect(L+470,-700,140,1630);X.fillRect(L+470,1266,140,374);X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L+470,-700,8,1630);X.fillRect(L+470,1266,8,374);
  X.fillStyle='#22302a';X.fillRect(L+470,918,140,12);
  const dy=-ap*322;X.fillStyle='#bfb49c';rr(L+446,926+dy,24,318,6);X.fill();trazo(LIN,2.5);X.fillStyle='#7d735f';rr(L+434,1180+dy,14,44,5);X.fill()})}

// ---------- P07 · el perro elige; la planilla de aciertos ----------
function repisa(L,x0,x1,xs,enc){X.fillStyle='#8a7f6c';X.fillRect(L+x0+40,1300,26,340);X.fillRect(L+x1-66,1300,26,340);
 rr(L+x0,1240,x1-x0,30,8);X.fillStyle='#d8d2c2';X.fill();trazo(LIN,3);X.fillStyle='#c4bca8';X.fillRect(L+x0+12,1270,x1-x0-24,56);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(L+x0+12,1270,x1-x0-24,56);
 xs.forEach((x,i)=>{const e=enc?enc[i]||0:0;if(enc){X.fillStyle='#2c3a33';X.beginPath();X.arc(L+x,1298,19,0,7);X.fill();X.fillStyle=e>0?`rgb(${lerp(82,124,e)|0},${lerp(96,252,e)|0},${lerp(90,138,e)|0})`:'#52605a';X.beginPath();X.arc(L+x,1298,13,0,7);X.fill()}})}
const NAR=[606,-594];   // punta de la nariz del perro parado a escala 3, medida desde su origen
function p07a(L,t){const c=T.c07a,xp=T.x_picked,J=[520,760,1000];
 const nx=lerp(lerp(J[0]-24,J[1]-24,eio(seg(t,c+.12,c+.4))),J[2]-24,eio(seg(t,xp-.02,xp+.3))),enc=seg(t,xp+.46,xp+.62);
 const inc=.05+.07*golpe(t,c+.42,.2)+.07*golpe(t,xp+.32,.2)+.05*eio(enc);
 cam(L,760,1090,1.45,540,1000,()=>{sala(L);repisa(L,380,1150,J,[0,0,enc]);J.forEach(x=>frasco(L+x,1240,{}));
  perro(L+nx-NAR[0],1640,3,t,Object.assign({},PERRO,{pose:'parado',camina:t<xp+.3,inclina:inc,orejas:.2*enc,mira:.4}))})}
function huella(x,y,s,col){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle=col;X.beginPath();X.ellipse(0,14,30,25,0,0,7);X.fill();[[-32,-16,13,17,-.35],[-12,-36,13,18,-.1],[12,-36,13,18,.1],[32,-16,13,17,.35]].forEach(q=>{X.beginPath();X.ellipse(q[0],q[1],q[2],q[3],q[4],0,7);X.fill()});X.restore()}
function p07b(L,t){const c=T.c07b,z=lerp(1.0,1.05,seg(t,c,T.c08));
 cam(L,540,960,z,540,1000,()=>{mesa(L);X.fillStyle='#446257';X.fillRect(L-900,1300,2900,1700);
  X.save();X.translate(L+540,960);X.rotate(-.025);X.fillStyle='rgba(0,0,0,.24)';rr(-430,-430,888,888,26);X.fill();rr(-444,-444,888,888,26);X.fillStyle='#f3ecd9';X.fill();trazo(LIN,3);
  rr(-90,-486,180,70,16);X.fillStyle='#8a8f96';X.fill();trazo(LIN,3);
  for(let i=0;i<16;i++){const gx=-303+(i%4)*202,gy=-303+Math.floor(i/4)*202,q=back(seg(t,c+.1+i*.052,c+.3+i*.052));
   rr(gx-88,gy-88,176,176,22);X.fillStyle='#e4dcc6';X.fill();X.strokeStyle='rgba(40,27,18,.3)';X.lineWidth=2.5;X.stroke();
   if(q>0){if(i===9){X.save();X.translate(gx,gy);X.scale(q,q);X.strokeStyle='#c0492f';X.lineWidth=13;X.lineCap='round';X.beginPath();X.moveTo(-44,-44);X.lineTo(44,44);X.moveTo(44,-44);X.lineTo(-44,44);X.stroke();X.restore()}else huella(gx,gy+6,1.25*q,'#1f5d57')}}
  X.restore()})}

// ---------- P08 · A y B iguales; el rastro sale solo de B ----------
function p08(L,t){const c=T.c08,xb=T.x_body,xt=T.x_that,xg=T.x_gives,xp=T.x_part,xz=T.x_thats,JA8=620,JB8=900;
 const RA=[[L+900,1036],[L+912,930],[L+858,846],[L+745,842],[L+655,930],[L+596,1020]];
 const sig=eio(seg(t,xz+.1,xz+1.0));
 const nx=ruta(t,[[c,400],[xb-.15,JA8-22],[xb+1.5,JA8-22],[xt-.1,JB8-24],[xg-.25,JB8-24],[xg+.35,566],[xz+.1,566],[xz+1.0,JB8-30]])[0];
 const inc=.04+.07*golpe(t,xb+.1,.22)+.07*golpe(t,xb+.62,.22)+.07*golpe(t,xt+.25,.22)+.07*golpe(t,xt+.95,.22)+.07*golpe(t,xt+1.7,.22)-.16*eio(seg(t,xg-.2,xg+.4))*(1-sig)-.14*Math.sin(sig*Math.PI)+.05*sig;
 const cm=ruta(t,[[c,640,1085,1.12],[xb+1.5,660,1085,1.2],[xt,800,1080,1.3],[xg-.2,800,1080,1.34],[xp,690,1030,1.2],[T.c09,712,1035,1.24]]);
 const u=eio(seg(t,xp-.02,xp+.8));
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{sala(L);repisa(L,470,1060,[JA8,JB8]);frasco(L+JA8,1240,{letra:'A'});frasco(L+JB8,1240,{letra:'B'});
  const mov=(t>c&&t<xb-.15)||(t>xb+1.5&&t<xt-.1)||(t>xg-.25&&t<xg+.35)||(t>xz+.1&&t<xz+1.0);
  perro(L+nx-NAR[0],1640,3,t,Object.assign({},PERRO,{pose:'parado',camina:mov,inclina:inc,orejas:.22*eio(seg(t,xp,xp+.3)),mira:.4}));
  rastro(RA,t,u,{amp:12})})}

NUEVOS.dc_dogs14_p01=SET(p01);NUEVOS.dc_dogs14_p02=SET(p02);NUEVOS.dc_dogs14_p03=SET(p03);NUEVOS.dc_dogs14_p04a=SET(p04a);NUEVOS.dc_dogs14_p04b=SET(p04b);NUEVOS.dc_dogs14_p05=SET(p05);
NUEVOS.dc_dogs14_p06=SET(p06);NUEVOS.dc_dogs14_p07a=SET(p07a);NUEVOS.dc_dogs14_p07b=SET(p07b);NUEVOS.dc_dogs14_p08=SET(p08);NUEVOS.dc_dogs14_p09=SET(p09);
})();
// ===== DC · DOGS14 · FIN =====
</script>
