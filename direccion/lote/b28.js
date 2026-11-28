<script>
// ===== DC · B28 · ayudantes del lote del 28-nov (dirección visual de Tao: fondos variados, texturas, profundidad, luz y cámara). Inerte: solo define window.B28. No dibuja logos ni marcas. =====
(function(){
const {cam}=window.DC;
// --- generador de texturas (copia del de la prueba técnica del doc 27, que vive dentro de su propio bloque y no es visible desde aquí) ---
const TEX28=new Map();
function tex28(i,w,h,tipo){const k=i+'_'+w+'_'+h;if(TEX28.has(k))return TEX28.get(k);const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');const r=j=>rnd(i*7.13+j*1.31);
 const T=tipo||['madera','piedra','ladrillo','tela','metal','pasto','arena','oxido','baldosa','cuero','marmol','cuerda','corteza','concreto'][i%14];
 const fondo=(c1,c2)=>{const gg=g.createLinearGradient(0,0,w,h);gg.addColorStop(0,c1);gg.addColorStop(1,c2);g.fillStyle=gg;g.fillRect(0,0,w,h)};
 const motas=(n,col,a1,a2,s1,s2)=>{for(let j=0;j<n;j++){g.fillStyle=`rgba(${col},${a1+(a2-a1)*r(j+50)})`;const s=s1+(s2-s1)*r(j+90);g.fillRect(r(j)*w,r(j+300)*h,s,s)}};
 if(T==='casco'){ // casco de barco: tablas largas pintadas de gris, veta, pintura saltada, clavos y línea de flotación. Sin nombre.
  fondo('#7a838d','#636c76');const ph=w/7;let fila=0;for(let y=0;y<h+ph;y+=ph,fila++){
   g.fillStyle=`rgba(255,255,255,${.04+.04*(fila%3)})`;g.fillRect(0,y+ph*.08,w,ph*.3);
   for(let k=0;k<4;k++){g.strokeStyle=`rgba(40,46,54,${.10+.08*r(fila*9+k)})`;g.lineWidth=w/700;g.beginPath();const yy=y+ph*(.2+.18*k);g.moveTo(0,yy);g.bezierCurveTo(w*.3,yy+ph*.05,w*.7,yy-ph*.05,w,yy+ph*.02);g.stroke()}
   g.fillStyle='rgba(18,22,28,.65)';g.fillRect(0,y+ph*.93,w,ph*.07);
   const off=(fila%2)*w*.45+r(fila)*w*.2;for(let x=off;x<w;x+=w*.9){g.fillStyle='rgba(18,22,28,.55)';g.fillRect(x,y,w/300+1,ph);for(let k=0;k<3;k++){g.fillStyle='rgba(40,40,44,.7)';g.beginPath();g.arc(x+w*.012,y+ph*(.22+k*.28),w/260+1,0,7);g.fill()}}
   for(let k=0;k<2;k++){g.fillStyle=`rgba(120,84,52,${.35+.25*r(fila*5+k)})`;g.beginPath();const cx=r(fila*3+k+20)*w,cy=y+ph*(.3+.4*r(fila+k+40));g.ellipse(cx,cy,w*(.02+.04*r(fila+k+60)),ph*(.08+.12*r(fila+k+70)),0,0,7);g.fill()}}
  const wl=h*.82;g.fillStyle='rgba(28,40,44,.45)';g.fillRect(0,wl,w,h-wl);g.fillStyle='rgba(200,205,195,.35)';g.fillRect(0,wl-w/200-1,w,w/200+1);
  motas(Math.round(w*h/1100),'215,220,225',.04,.14,1,w/90);for(let j=0;j<5;j++){const gx=r(j+500)*w,gg2=g.createLinearGradient(0,0,0,h);gg2.addColorStop(0,'rgba(110,70,40,.0)');gg2.addColorStop(.5,'rgba(110,70,40,.16)');gg2.addColorStop(1,'rgba(110,70,40,0)');g.fillStyle=gg2;g.fillRect(gx,0,w*.012,h)}}
 else if(T==='madera'){fondo('#8a5a33','#6b4426');for(let y=0;y<h;y+=h/5){g.fillStyle='rgba(0,0,0,.35)';g.fillRect(0,y,w,2);for(let k=0;k<6;k++){g.strokeStyle=`rgba(60,35,15,${.25+.2*r(k+y)})`;g.lineWidth=1.5;g.beginPath();const yy=y+r(k*3+y)*h/5;g.moveTo(0,yy);g.bezierCurveTo(w*.3,yy+4,w*.6,yy-4,w,yy+2);g.stroke()}}}
 else if(T==='piedra'){fondo('#7d7a73','#5e5b55');for(let j=0;j<14;j++){g.fillStyle=`rgba(${90+40*r(j)},${88+38*r(j)},${82+36*r(j)},1)`;g.beginPath();g.ellipse(r(j+1)*w,r(j+2)*h,w*(.12+.1*r(j+3)),h*(.1+.08*r(j+4)),r(j+5)*3,0,7);g.fill();g.strokeStyle='rgba(30,30,28,.5)';g.lineWidth=2;g.stroke()}}
 else if(T==='ladrillo'){fondo('#8d4a35','#733a28');const bh=h/6;for(let y=0;y<h;y+=bh){const o=(Math.round(y/bh)%2)*w/6;for(let x=-o;x<w;x+=w/3){g.fillStyle=`rgba(${150+30*r(x+y)},${75+15*r(x)},${55},1)`;g.fillRect(x+2,y+2,w/3-4,bh-4)}}}
 else if(T==='tela'){fondo('#5a6a7a','#47566a');g.strokeStyle='rgba(255,255,255,.10)';g.lineWidth=2;for(let x=0;x<w;x+=6){g.beginPath();g.moveTo(x,0);g.lineTo(x,h);g.stroke()}g.strokeStyle='rgba(0,0,0,.15)';for(let y=0;y<h;y+=6){g.beginPath();g.moveTo(0,y);g.lineTo(w,y);g.stroke()}}
 else if(T==='metal'){fondo('#9aa1a8','#6e757c');for(let y=0;y<h;y+=3){g.fillStyle=`rgba(255,255,255,${.03+.05*r(y)})`;g.fillRect(0,y,w,1)}[[.15,.2],[.85,.2],[.15,.8],[.85,.8]].forEach(([a,b])=>{g.fillStyle='#50565c';g.beginPath();g.arc(a*w,b*h,6,0,7);g.fill()})}
 else if(T==='pasto'){fondo('#4f6b2e','#3c5523');for(let j=0;j<220;j++){g.strokeStyle=`rgba(${100+60*r(j)},${150+50*r(j+1)},60,.6)`;g.lineWidth=1.5;const x=r(j+2)*w,y=r(j+3)*h;g.beginPath();g.moveTo(x,y);g.lineTo(x+(r(j+4)-.5)*8,y-8-r(j+5)*10);g.stroke()}}
 else if(T==='arena'){fondo('#c9ad7a','#b0935f');motas(500,'120,95,60',.15,.4,1,2.5)}
 else if(T==='oxido'){fondo('#8b4f2c','#6a3a22');for(let j=0;j<30;j++){g.fillStyle=`rgba(${160+60*r(j)},${90+40*r(j+1)},40,${.2+.3*r(j+2)})`;g.beginPath();g.arc(r(j+3)*w,r(j+4)*h,4+r(j+5)*22,0,7);g.fill()}}
 else if(T==='baldosa'){fondo('#d8d4c8','#bdb8aa');const s=w/4;for(let x=0;x<w;x+=s)for(let y=0;y<h;y+=s){g.strokeStyle='rgba(80,75,65,.6)';g.lineWidth=3;g.strokeRect(x,y,s,s)}}
 else if(T==='cuero'){fondo('#6a3f26','#4f2d1a');motas(300,'30,15,8',.15,.35,1,3);g.strokeStyle='rgba(230,190,140,.4)';g.setLineDash([6,5]);g.lineWidth=2;g.strokeRect(10,10,w-20,h-20);g.setLineDash([])}
 else if(T==='marmol'){fondo('#e6e3dc','#cfcac0');for(let j=0;j<6;j++){g.strokeStyle=`rgba(110,110,120,${.2+.2*r(j)})`;g.lineWidth=1+r(j+1)*2;g.beginPath();g.moveTo(r(j+2)*w,0);g.bezierCurveTo(r(j+3)*w,h*.3,r(j+4)*w,h*.7,r(j+5)*w,h);g.stroke()}}
 else if(T==='cuerda'){fondo('#a88a5c','#8c7048');for(let y=0;y<h;y+=14){for(let x=0;x<w;x+=10){g.strokeStyle='rgba(60,45,25,.5)';g.lineWidth=2;g.beginPath();g.moveTo(x,y);g.lineTo(x+10,y+12);g.stroke()}}}
 else if(T==='corteza'){fondo('#5b4636','#46352a');for(let x=0;x<w;x+=8){g.strokeStyle=`rgba(25,18,12,${.3+.3*r(x)})`;g.lineWidth=2+r(x+1)*3;g.beginPath();g.moveTo(x,0);g.bezierCurveTo(x+6,h*.3,x-6,h*.7,x+3,h);g.stroke()}}
 else{fondo('#8e8e8a','#757571');motas(400,'40,40,40',.1,.3,1,3);motas(120,'230,230,225',.1,.3,1,2)}
 TEX28.set(k,c);return c}

const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
// plano(L,t,kf,fn): cámara por claves [t,cx,cy,escala,(rot)]; el punto (cx,cy) queda en el centro del cuadro. fn recibe [cx,cy,s] para el paralaje.
function plano(L,t,kf,fn,ay){const c=ruta(t,kf);cam(L,c[0],c[1],c[2],540,ay||1000,()=>fn(c),c[3]||0)}
const par=(c,k)=>(c[0]-540)*k;                       // desplazamiento de una capa lejana (k cerca de 1: casi fija al cuadro)
// ---------- texturas del motor (cacheadas) ----------
const TI={madera:0,piedra:1,ladrillo:2,tela:3,metal:4,pasto:5,arena:6,oxido:7,baldosa:8,cuero:9,marmol:10,cuerda:11,corteza:12,concreto:13};
function tex(tipo,x,y,w,h,o){o=o||{};const tw=o.tw||512,th=o.th||512,c=tex28(TI[tipo]+14*(o.v||0),tw,th,tipo),s=o.s||1;X.save();X.beginPath();X.rect(x,y,w,h);X.clip();if(o.a!==undefined)X.globalAlpha=o.a;
 for(let yy=y;yy<y+h;yy+=th*s)for(let xx=x;xx<x+w;xx+=tw*s)X.drawImage(c,xx,yy,tw*s,th*s);X.globalAlpha=1;if(o.tinte){X.fillStyle=o.tinte;X.fillRect(x,y,w,h)}X.restore()}
// ---------- luz ----------
function luz(x,y,r,rgb,a,ry){if(a<=0)return;X.save();X.globalCompositeOperation='lighter';X.translate(x,y);X.scale(1,(ry||r)/r);const g=X.createRadialGradient(0,0,0,0,0,r);g.addColorStop(0,`rgba(${rgb},${a})`);g.addColorStop(1,`rgba(${rgb},0)`);X.fillStyle=g;X.beginPath();X.arc(0,0,r,0,7);X.fill();X.restore()}
function haz(x0,y0,x1,y1,w0,w1,rgb,a){if(a<=0)return;X.save();X.globalCompositeOperation='lighter';const g=X.createLinearGradient(x0,y0,x1,y1);g.addColorStop(0,`rgba(${rgb},${a})`);g.addColorStop(1,`rgba(${rgb},0)`);X.fillStyle=g;const q=Math.atan2(y1-y0,x1-x0)+Math.PI/2,c=Math.cos(q),s=Math.sin(q);X.beginPath();X.moveTo(x0-c*w0,y0-s*w0);X.lineTo(x0+c*w0,y0+s*w0);X.lineTo(x1+c*w1,y1+s*w1);X.lineTo(x1-c*w1,y1-s*w1);X.closePath();X.fill();X.restore()}
function sombra(x,y,rx,ry,a){X.fillStyle=`rgba(0,0,0,${a===undefined?.3:a})`;X.beginPath();X.ellipse(x,y,rx,ry,0,0,7);X.fill()}
function tinte(L,rgb,a){if(a<=0)return;X.fillStyle=`rgba(${rgb},${a})`;X.fillRect(L-1400,-1400,3900,5000)}
// arriba(L,a): degradé oscuro sobre la franja de subtítulos. Se llama al final del plano, fuera de la cámara.
function arriba(L,a,y1){const g=X.createLinearGradient(0,170,0,y1||660);g.addColorStop(0,`rgba(10,8,14,${a===undefined?.6:a})`);g.addColorStop(1,'rgba(10,8,14,0)');X.fillStyle=g;X.fillRect(L-300,-400,1680,(y1||660)+400)}
function vin(L,a){window.DC.vineta(L,a===undefined?.35:a)}
// ---------- fondos ----------
// interior: pared con textura, zócalo y piso en perspectiva. o: p0,p1 (pared) · tex,ta,ts · yp (línea de piso) · piso:[c1,c2] o pisoTex · paso · rod
function interior(L,o){o=o||{};const yp=o.yp||1300,x0=L-1400,w=3900;
 X.fillStyle=gl(0,-300,0,yp,[[0,o.p0||'#39424f'],[1,o.p1||'#566273']]);X.fillRect(x0,-1400,w,yp+1460);   // la pared baja 60 px bajo la línea de piso: sin costura entre pared y piso al escalar la cámara
 if(o.tex)tex(o.tex,x0,-400,w,yp+400,{a:o.ta===undefined?.2:o.ta,s:o.ts||1.5,v:o.v||0});
 X.fillStyle=o.rod||'rgba(20,14,10,.55)';X.fillRect(x0,yp-30,w,30);
 const ps=o.piso||['#6b4a30','#5e3f28'];X.fillStyle=ps[0];X.fillRect(x0,yp,w,2600-yp);
 if(o.pisoTex)tex(o.pisoTex,x0,yp,w,2600-yp,{a:o.pa===undefined?.85:o.pa,s:1.7,v:o.v||0});else pisoPersp(x0,x0+w,L+540,yp,2600,o.paso||150,ps,'rgba(0,0,0,.22)');
 X.fillStyle=gl(0,yp,0,yp+140,[[0,'rgba(0,0,0,.45)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,yp,w,140)}
// mesón o mesa en primer plano: tablero desde y hasta abajo, con canto iluminado
function meson(L,y,o){o=o||{};const x0=L-1400,w=3900;X.fillStyle=o.col||'#7a5636';X.fillRect(x0,y,w,2700-y);if(o.tex)tex(o.tex,x0,y,w,2700-y,{a:o.ta===undefined?.9:o.ta,s:o.ts||1.6,v:o.v||0,tinte:o.tinte});
 X.fillStyle='rgba(255,255,255,.16)';X.fillRect(x0,y,w,8);X.fillStyle=gl(0,y+8,0,y+90,[[0,'rgba(0,0,0,.28)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,y+8,w,82)}
function noche(L,t,o){o=o||{};X.fillStyle=gl(0,-300,0,o.y1||1500,[[0,o.c0||'#0c1230'],[1,o.c1||'#3a3566']]);X.fillRect(L-1400,-1400,3900,5000);
 for(let i=0;i<(o.n===undefined?46:o.n);i++){const x=L-400+rnd(i+(o.sem||0))*1900,y=(o.ys||520)+rnd(i+50)*(o.yh||820),a=.35+.3*Math.sin(t*1.3+i*2.1);X.fillStyle=`rgba(255,246,221,${a})`;X.beginPath();X.arc(x,y,2+rnd(i+90)*2.6,0,7);X.fill()}}
function planeta(x,y,r,o){o=o||{};X.save();X.beginPath();X.arc(x,y,r,0,7);X.clip();X.fillStyle=gl(x-r,y-r,x+r,y+r,[[0,o.c0||'#e0875a'],[1,o.c1||'#8a3f2a']]);X.fillRect(x-r,y-r,2*r,2*r);
 for(let i=0;i<8;i++){X.fillStyle=`rgba(${o.banda||'110,45,28'},${.10+.09*rnd(i+3)})`;X.beginPath();X.ellipse(x+(rnd(i)-.5)*r+(o.giro||0),y-r+(i+.5)*r/4,r*(.7+rnd(i+9)*.6),r*.05+rnd(i+5)*r*.05,0,0,7);X.fill()}
 const g=X.createRadialGradient(x-r*.45,y-r*.45,r*.2,x,y,r*1.15);g.addColorStop(0,'rgba(255,255,255,.14)');g.addColorStop(.55,'rgba(0,0,0,0)');g.addColorStop(1,'rgba(0,0,0,.62)');X.fillStyle=g;X.fillRect(x-r,y-r,2*r,2*r);X.restore();
 if(o.atm){X.strokeStyle=`rgba(${o.atm},.4)`;X.lineWidth=r*.035;X.beginPath();X.arc(x,y,r*1.014,0,7);X.stroke()}}
// ---------- objetos comunes ----------
function pantalla(x,y,w,h,fn,o){o=o||{};X.fillStyle='rgba(0,0,0,.3)';rr(x-10,y-4,w+36,h+40,18);X.fill();X.fillStyle=o.marco||'#15171c';rr(x-18,y-18,w+36,h+36,16);X.fill();X.save();X.beginPath();X.rect(x,y,w,h);X.clip();X.fillStyle=o.fondo||'#0c1622';X.fillRect(x,y,w,h);fn&&fn();
 X.fillStyle='rgba(255,255,255,.05)';X.beginPath();X.moveTo(x,y);X.lineTo(x+w*.45,y);X.lineTo(x+w*.15,y+h);X.lineTo(x,y+h);X.closePath();X.fill();X.restore()}
function hojaP(x,y,w,h,rot,fn,col){X.save();X.translate(x,y);X.rotate(rot||0);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-w/2+8,-h/2+10,w,h);X.fillStyle=col||'#efe6d0';X.fillRect(-w/2,-h/2,w,h);fn&&fn();X.restore()}
function renglones(x,y,w,n,alto,sem,col){X.fillStyle=col||'rgba(42,32,25,.28)';for(let i=0;i<n;i++){rr(x,y+i*alto*1.9,w*(.72+rnd(i+(sem||0))*.28),alto,alto/2);X.fill()}}
function tarj(x,y,w,h,r,col,o){o=o||{};X.fillStyle=`rgba(0,0,0,${o.sa===undefined?.3:o.sa})`;rr(x-w/2+8,y-h/2+12,w,h,r);X.fill();X.fillStyle=col;rr(x-w/2,y-h/2,w,h,r);X.fill();if(o.borde){X.strokeStyle=o.borde;X.lineWidth=o.lw||4;X.stroke()}}
function tripode(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.strokeStyle='#2a2f38';X.lineWidth=12;X.lineCap='round';[[-90,0],[0,-8],[90,0]].forEach(p=>{X.beginPath();X.moveTo(0,-330);X.lineTo(p[0],p[1]);X.stroke()});
 X.fillStyle='#3a414c';rr(-16,-372,32,50,6);X.fill();X.fillStyle='#1c2027';rr(-92,-470,170,104,14);X.fill();X.fillStyle=gl(0,-470,0,-366,[[0,'rgba(255,255,255,.14)'],[1,'rgba(255,255,255,0)']]);rr(-92,-470,170,104,14);X.fill();
 X.fillStyle='#0d0f13';X.beginPath();X.arc(96,-418,44,0,7);X.fill();X.fillStyle='#31506e';X.beginPath();X.arc(100,-418,26,0,7);X.fill();X.fillStyle='rgba(255,255,255,.35)';X.beginPath();X.arc(90,-428,8,0,7);X.fill();X.fillStyle='#c0392b';X.beginPath();X.arc(-64,-446,7,0,7);X.fill();X.restore()}
function relojPared(x,y,r,hh,mm,o){o=o||{};X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(x+8,y+12,r*1.08,0,7);X.fill();X.fillStyle=o.aro||'#2a2f38';X.beginPath();X.arc(x,y,r*1.08,0,7);X.fill();X.fillStyle=o.cara||'#efe9dc';X.beginPath();X.arc(x,y,r,0,7);X.fill();
 X.strokeStyle='#2a2019';X.lineCap='round';for(let i=0;i<12;i++){const q=i*Math.PI/6;X.lineWidth=i%3?r*.025:r*.05;X.beginPath();X.moveTo(x+Math.cos(q)*r*.8,y+Math.sin(q)*r*.8);X.lineTo(x+Math.cos(q)*r*.92,y+Math.sin(q)*r*.92);X.stroke()}
 const ah=-Math.PI/2+(hh%12+mm/60)*Math.PI/6,am=-Math.PI/2+mm*Math.PI/30;X.lineWidth=r*.07;X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(ah)*r*.5,y+Math.sin(ah)*r*.5);X.stroke();X.lineWidth=r*.045;X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(am)*r*.76,y+Math.sin(am)*r*.76);X.stroke();X.fillStyle='#c0392b';X.beginPath();X.arc(x,y,r*.07,0,7);X.fill()}
// vaso de vidrio con líquido: nivel 0..1, color del líquido
function vaso(x,yb,s,o){o=o||{};const w=70*s,h=150*s,n=o.nivel===undefined?.6:o.nivel;X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(x,yb+4*s,w*.62,10*s,0,0,7);X.fill();
 X.fillStyle=o.liq||'#6b3d1e';X.beginPath();X.moveTo(x-w*.42-(w*.08)*n,yb-h*n);X.lineTo(x+w*.42+(w*.08)*n,yb-h*n);X.lineTo(x+w*.42,yb);X.lineTo(x-w*.42,yb);X.closePath();X.fill();
 X.fillStyle='rgba(220,235,245,.16)';X.strokeStyle='rgba(235,245,255,.6)';X.lineWidth=3*s;X.beginPath();X.moveTo(x-w*.5,yb-h);X.lineTo(x+w*.5,yb-h);X.lineTo(x+w*.42,yb);X.lineTo(x-w*.42,yb);X.closePath();X.fill();X.stroke();X.fillStyle='rgba(255,255,255,.3)';X.fillRect(x-w*.36,yb-h*.9,6*s,h*.72)}
// figura genérica de espaldas o silueta (sin rostro): para público, clientes, científicos lejanos
function silueta(x,yb,s,col,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle=col;X.beginPath();X.arc(0,-300,38,0,7);X.fill();X.beginPath();X.moveTo(-70,0);X.quadraticCurveTo(-84,-230,-52,-250);X.quadraticCurveTo(0,-272,52,-250);X.quadraticCurveTo(84,-230,70,0);X.closePath();X.fill();if(o.brazo){X.lineWidth=26;X.strokeStyle=col;X.lineCap='round';X.beginPath();X.moveTo(50*o.brazo,-225);X.quadraticCurveTo(110*o.brazo,-200,(o.bx===undefined?130:o.bx)*o.brazo,(o.by===undefined?-150:o.by));X.stroke()}X.restore()}
// desenfoca(px): desenfoca TODO lo dibujado hasta ahora en el cuadro (para cambio de foco: primero el fondo, se desenfoca, y después lo nítido). Llamar fuera de la cámara.
function desenfoca(px){if(px<.3)return;X.save();X.setTransform(1,0,0,1,0,0);X.filter='blur('+px.toFixed(1)+'px)';X.drawImage(X.canvas,0,0);X.filter='none';X.restore()}
// borroso(px,fn): dibuja fn con cada forma desenfocada (para un objeto fuera de foco, de pocas formas)
function borroso(px,fn){if(px<.3){fn();return}X.save();X.filter='blur('+px.toFixed(1)+'px)';fn();X.filter='none';X.restore()}
window.B28={desenfoca,borroso,golpe,ruta,plano,par,tex,luz,haz,sombra,tinte,arriba,vin,interior,meson,noche,planeta,pantalla,hojaP,renglones,tarj,tripode,relojPared,vaso,silueta};
})();
</script>
