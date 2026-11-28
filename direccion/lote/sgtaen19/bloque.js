<script>
// ===== DC · SGTAEN19 · INICIO ===== (GTA EN 19h · This PARROT Knows Where the MONEY Is · lote del 28-nov · una escena por línea del guion)
// Sin personajes ni arte del juego: las personas son siluetas genéricas; el loro, el generador y la tienda son dibujos propios. Sin diálogo inventado: los globos llevan íconos, no texto.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,tarj,silueta,desenfoca,borroso}=window.B28;
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({manga:'#1c2533',puno:'#2a3646'},o))};
const SOL='255,214,150',ORO='#f2c94c';

function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#14202a',{sa:.3,borde:o.borde||'rgba(255,214,150,.7)',lw:3});txt(texto,x,y+4*s,(o.ts||46)*s,o.tc||'#fff',{w:800});X.restore()}
function percha(x,y,w){X.fillStyle='#5a3d24';rr(x-w/2,y-4,w,26,12);X.fill();X.fillStyle='rgba(255,255,255,.14)';rr(x-w/2+6,y-2,w-12,6,3);X.fill()}
// loro rojo (dibujo propio). (x,y) = patas sobre la percha · inc: inclinación de la cabeza · dir: 1 mira a la derecha · sx: giro (−1…1) · habla: 0…1 pico abierto · cola: largo de la cola
function loro(x,y,s,t,o){o=o||{};const d=(o.dir||1)*(o.sx===undefined?1:(Math.abs(o.sx)<.14?.14*(o.sx<0?-1:1):o.sx)),co=o.cola===undefined?1:o.cola,pp=(t*.37%1)>.94;X.save();X.translate(x,y);X.scale(s*d,s);
 X.fillStyle='#b3261e';X.beginPath();X.moveTo(-34,-40);X.quadraticCurveTo(-84,120*co,-72,300*co);X.lineTo(-42,300*co);X.quadraticCurveTo(-30,120*co,10,-20);X.fill();
 X.fillStyle='#1f5fbf';X.beginPath();X.moveTo(-12,-30);X.quadraticCurveTo(-42,120*co,-32,262*co);X.lineTo(-10,250*co);X.quadraticCurveTo(-6,100*co,20,-20);X.fill();
 X.fillStyle=gl(-90,-300,90,0,[[0,'#ee4034'],[1,'#b3261e']]);X.beginPath();X.ellipse(0,-150,92,150,.12,0,7);X.fill();
 X.fillStyle='#c92a20';X.beginPath();X.moveTo(-60,-250);X.quadraticCurveTo(-124,-120,-50,10);X.quadraticCurveTo(12,-80,-10,-240);X.fill();
 X.fillStyle='#f2c230';X.beginPath();X.moveTo(-86,-150);X.quadraticCurveTo(-92,-60,-52,0);X.quadraticCurveTo(-28,-70,-40,-150);X.fill();
 X.fillStyle='#1f5fbf';X.beginPath();X.moveTo(-78,-80);X.quadraticCurveTo(-70,-20,-50,14);X.quadraticCurveTo(-34,-30,-42,-80);X.fill();
 X.fillStyle='#3a3a3a';rr(-32,-12,24,22,7);X.fill();rr(14,-12,24,22,7);X.fill();
 X.save();X.translate(20,-290);X.rotate(o.inc||0);X.fillStyle='#ee4034';X.beginPath();X.arc(0,0,74,0,7);X.fill();X.fillStyle='#f4efe6';X.beginPath();X.ellipse(26,4,40,34,0,0,7);X.fill();
 X.save();X.translate(52,18);X.rotate((o.habla||0)*.5);X.fillStyle='#2a2a2a';X.beginPath();X.moveTo(0,-2);X.quadraticCurveTo(32,4,36,30);X.quadraticCurveTo(12,34,-2,16);X.closePath();X.fill();X.restore();
 X.fillStyle='#efe2c0';X.beginPath();X.moveTo(52,-34);X.quadraticCurveTo(122,-30,112,40);X.quadraticCurveTo(108,56,96,60);X.quadraticCurveTo(96,16,50,14);X.closePath();X.fill();
 if(pp){X.strokeStyle='#111';X.lineWidth=5;X.beginPath();X.moveTo(10,-6);X.lineTo(38,-6);X.stroke()}else{X.fillStyle='#fff';X.beginPath();X.arc(24,-6,15,0,7);X.fill();X.fillStyle='#111';X.beginPath();X.arc(27,-6,8,0,7);X.fill();X.fillStyle='#fff';X.beginPath();X.arc(30,-9,3,0,7);X.fill()}
 X.restore();X.restore()}
function generador(x,yb,s,t,o){o=o||{};const v=Math.sin(t*38)*.8;X.save();X.translate(x,yb+v*.5);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';X.beginPath();X.ellipse(0,0,220,20,0,0,7);X.fill();if(o.brillo>0)luz(0,-150,360,'255,210,120',.42*o.brillo);
 X.fillStyle='#14171b';[-150,150].forEach(q=>{X.beginPath();X.arc(q,-30,32,0,7);X.fill()});X.fillStyle='#6b7480';[-150,150].forEach(q=>{X.beginPath();X.arc(q,-30,12,0,7);X.fill()});
 X.fillStyle=gl(0,-250,0,-40,[[0,'#3a424c'],[1,'#20262d']]);rr(-170,-200,340,160,14);X.fill();X.fillStyle=gl(0,-290,0,-200,[[0,'#f0b429'],[1,'#b97a12']]);rr(-150,-284,300,96,26);X.fill();X.fillStyle='#14171b';rr(-24,-300,48,22,6);X.fill();
 if(o.refl!==undefined&&o.refl>0&&o.refl<1){X.save();rr(-150,-284,300,96,26);X.clip();const rx=lerp(-200,200,o.refl);X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.moveTo(rx,-290);X.lineTo(rx+36,-290);X.lineTo(rx+6,-180);X.lineTo(rx-30,-180);X.closePath();X.fill();X.restore()}
 X.fillStyle='#14171b';rr(-150,-180,130,120,8);X.fill();X.fillStyle='#e9eef2';[-120,-80].forEach(q=>{X.beginPath();X.arc(q,-150,14,0,7);X.fill()});X.fillStyle='#22c55e';X.beginPath();X.arc(-50,-90,8,0,7);X.fill();X.fillStyle='#c0392b';rr(-130,-104,44,24,5);X.fill();
 X.fillStyle='#14171b';for(let i=0;i<5;i++){rr(10,-176+i*24,130,10,4);X.fill()}X.strokeStyle='#8e98a4';X.lineWidth=14;X.lineJoin='round';X.beginPath();X.moveTo(-190,-30);X.lineTo(-190,-300);X.lineTo(190,-300);X.lineTo(190,-30);X.stroke();X.fillStyle='#4a5560';rr(170,-150,50,26,8);X.fill();X.restore()}
function fajo(x,y,s,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';rr(-96,-40,200,96,8);X.fill();X.fillStyle='#2f7d4f';rr(-100,-50,200,96,8);X.fill();X.fillStyle='#3f9c63';rr(-100,-50,200,82,8);X.fill();X.strokeStyle='rgba(255,255,255,.35)';X.lineWidth=4;rr(-86,-38,172,58,6);X.stroke();X.fillStyle='rgba(255,255,255,.4)';X.beginPath();X.arc(0,-9,20,0,7);X.fill();X.fillStyle='#e9e2c8';X.fillRect(-26,-50,52,82);X.fillStyle='rgba(0,0,0,.12)';X.fillRect(-26,-50,52,8);X.restore()}
// rejilla de pared: ab 0…1 la tapa se retira hacia la derecha · dinero 0…1 se ve adentro
function rejilla(x,y,w,h,o){o=o||{};const ab=o.ab||0,n=o.n||6;X.fillStyle='#07090c';rr(x-w/2,y-h/2,w,h,10);X.fill();
 if(o.dinero>0){X.save();rr(x-w/2,y-h/2,w,h,10);X.clip();luz(x,y+h*.2,w*.6,'120,255,160',.3*o.dinero);X.globalAlpha=o.dinero;[[-.2,.2,-.1],[.17,.24,.08],[-.02,.04,0]].forEach(p=>fajo(x+p[0]*w,y+p[1]*h,w/400,p[2]));X.restore()}
 if(o.aviso>0){X.strokeStyle=`rgba(255,214,150,${o.aviso})`;X.lineWidth=8;rr(x-w/2-26,y-h/2-26,w+52,h+52,18);X.stroke()}
 X.save();X.translate(x+ab*w*(o.dx===undefined?1.15:o.dx),y+ab*h*(o.dy===undefined?.3:o.dy));X.rotate(ab*(o.giro===undefined?.5:o.giro));X.fillStyle='rgba(0,0,0,.35)';rr(-w/2+8,-h/2+10,w,h,10);X.fill();X.fillStyle=gl(0,-h/2,0,h/2,[[0,'#aab3bc'],[1,'#7c8690']]);rr(-w/2-12,-h/2-12,w+24,h+24,12);X.fill();X.fillStyle='#1c2228';for(let i=0;i<n;i++){rr(-w/2+14,-h/2+12+i*(h-24)/n,w-28,(h-24)/n*.5,5);X.fill()}X.fillStyle='#4a5560';[[-1,-1],[1,-1],[-1,1],[1,1]].forEach(q=>{X.beginPath();X.arc(q[0]*(w/2-2),q[1]*(h/2-2),6,0,7);X.fill()});X.restore()}
function monedaP(x,y,r,rot){X.save();X.translate(x,y);X.scale(Math.max(.25,Math.abs(Math.cos(rot||0))),1);X.fillStyle='#b9860f';X.beginPath();X.arc(0,4,r,0,7);X.fill();X.fillStyle=ORO;X.beginPath();X.arc(0,0,r,0,7);X.fill();X.strokeStyle='#b9860f';X.lineWidth=r*.14;X.beginPath();X.arc(0,0,r*.68,0,7);X.stroke();X.restore()}
function botella(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.rotate(o.rot||0);X.scale(s,s);const c=o.col||'#7a3e12';X.fillStyle=gl(-50,0,50,0,[[0,c],[.5,o.col2||'#b8651c'],[1,c]]);X.beginPath();X.moveTo(-50,0);X.lineTo(-50,-190);X.quadraticCurveTo(-50,-240,-18,-262);X.lineTo(-18,-330);X.lineTo(18,-330);X.lineTo(18,-262);X.quadraticCurveTo(50,-240,50,-190);X.lineTo(50,0);X.closePath();X.fill();X.fillStyle='#1c1410';rr(-22,-352,44,30,6);X.fill();
 if(!o.lisa){X.fillStyle='#efe6cf';rr(-50,-170,100,100,4);X.fill();X.fillStyle='#8a5a2a';rr(-34,-150,68,10,4);X.fill();rr(-26,-128,52,8,4);X.fill();X.beginPath();X.arc(0,-96,12,0,7);X.fill()}X.fillStyle='rgba(255,255,255,.25)';rr(-40,-250,10,230,5);X.fill();X.restore()}
// jaula: fondo en sombra, barrotes traseros, contenido (fn) y barrotes delanteros con separación irregular
function jaula(x,yb,w,h,fn,o){o=o||{};const n=o.n||7,bx=i=>x-w/2+(i+(rnd(i+(o.sem||0))-.5)*.36)*w/n;X.fillStyle='rgba(0,0,0,.35)';X.beginPath();X.ellipse(x,yb+6,w*.6,16,0,0,7);X.fill();X.fillStyle='rgba(10,14,18,.5)';rr(x-w/2,yb-h,w,h,o.r||18);X.fill();
 X.strokeStyle='rgba(70,80,92,.5)';X.lineWidth=5;for(let i=0;i<n;i++){const q=bx(i)+w/n*.5;X.beginPath();X.moveTo(q,yb-h+8);X.lineTo(q,yb-8);X.stroke()}if(fn)fn();
 X.strokeStyle=o.col||'#7c8690';X.lineWidth=o.lw||9;X.lineCap='round';for(let i=1;i<n;i++){X.beginPath();X.moveTo(bx(i),yb-h+6);X.lineTo(bx(i),yb-6);X.stroke()}X.fillStyle='#4a5560';rr(x-w/2-10,yb-h-14,w+20,26,10);X.fill();rr(x-w/2-10,yb-16,w+20,26,10);X.fill()}
function ave(x,y,s,d){X.save();X.translate(x,y);X.scale(s*(d||1),s);X.fillStyle='#1c2430';X.beginPath();X.ellipse(0,-70,44,66,.15,0,7);X.fill();X.beginPath();X.moveTo(-20,-30);X.lineTo(-50,60);X.lineTo(-10,40);X.closePath();X.fill();X.fillStyle='#f4e9c8';X.beginPath();X.ellipse(16,-96,26,30,0,0,7);X.fill();X.fillStyle='#1c2430';X.beginPath();X.arc(8,-128,30,0,7);X.fill();X.fillStyle='#f0a030';X.beginPath();X.moveTo(30,-144);X.quadraticCurveTo(110,-140,104,-104);X.quadraticCurveTo(70,-108,32,-114);X.closePath();X.fill();X.fillStyle='#fff';X.beginPath();X.arc(18,-134,7,0,7);X.fill();X.fillStyle='#111';X.beginPath();X.arc(19,-134,3.5,0,7);X.fill();X.restore()}
function mono(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle='#6b4a2e';X.lineWidth=14;X.lineCap='round';X.beginPath();X.moveTo(40,-20);X.quadraticCurveTo(110,-30,96,-90+Math.sin(t*2)*8);X.stroke();X.fillStyle='#7a5636';X.beginPath();X.ellipse(0,-56,48,58,0,0,7);X.fill();X.beginPath();X.arc(0,-136,38,0,7);X.fill();[-1,1].forEach(q=>{X.beginPath();X.arc(q*38,-146,15,0,7);X.fill()});X.fillStyle='#e4c9a0';X.beginPath();X.ellipse(0,-128,24,22,0,0,7);X.fill();X.fillStyle='#111';[-9,9].forEach(q=>{X.beginPath();X.arc(q,-134,4,0,7);X.fill()});X.restore()}
function iguana(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#4f9a4a';X.beginPath();X.moveTo(-120,-10);X.quadraticCurveTo(-60,-22,-10,-40);X.quadraticCurveTo(50,-62,90,-46);X.quadraticCurveTo(124,-40,120,-22);X.quadraticCurveTo(80,-4,20,-6);X.quadraticCurveTo(-60,0,-120,-10);X.fill();for(let i=0;i<6;i++){X.beginPath();X.moveTo(-20+i*18,-42-i*2);X.lineTo(-12+i*18,-62-i*2);X.lineTo(-4+i*18,-44-i*2);X.fill()}X.fillRect(-10,-12,12,16);X.fillRect(50,-12,12,16);X.fillStyle='#111';X.beginPath();X.arc(100,-40,4,0,7);X.fill();X.restore()}
// muro del patio (donde están el generador y la rejilla): hormigón pintado, sombras de hojas y sol rasante
function muro(L,cm,t,o){o=o||{};const yp=o.yp||1450;X.fillStyle=gl(0,300,0,yp,[[0,'#2f6f73'],[1,'#3f8a86']]);X.fillRect(L-1400,-900,3900,yp+960);tex('concreto',L-1400,-200,3900,yp+200,{a:.4,s:1.4});X.fillStyle='rgba(0,0,0,.16)';X.fillRect(L-1400,yp-120,3900,120);
 X.save();X.globalAlpha=.2;X.fillStyle='#0a1c22';for(let k=0;k<2;k++){const ox=L+(k?930:180)+par(cm,.2),oy=600+k*90,sw=Math.sin(t*.9+k*2)*.06;for(let i=0;i<7;i++){X.save();X.translate(ox,oy);X.rotate(-1.1+i*.36+sw);X.beginPath();X.moveTo(0,0);X.quadraticCurveTo(190,-46,400,10);X.quadraticCurveTo(190,30,0,0);X.fill();X.restore()}}X.restore();
 haz(L-200,200,L+700,1500,80,460,SOL,.16);X.fillStyle=gl(0,yp,0,1920,[[0,'#b08a58'],[1,'#8a6a40']]);X.fillRect(L-1400,yp,3900,1500);tex('arena',L-1400,yp,3900,900,{a:.45,s:1.5});X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L-1400,yp-6,3900,14)}
// patio abierto: cielo de tarde, palmeras lejanas, cerca de tablones, suelo de arena y sombra profunda
function patio(L,cm,t,o){o=o||{};const yf=o.yf||1180;X.fillStyle=gl(0,200,0,yf,[[0,'#1d5f8f'],[.6,'#58a9c9'],[1,'#f0c890']]);X.fillRect(L-1400,-900,3900,yf+960);luz(L+(o.sx||900)+par(cm,.8),yf-560,520,SOL,.5);
 [[120,.62,0],[430,.5,2],[990,.58,4]].forEach(p=>palmeraV(L+p[0]+par(cm,.55),yf-150,p[1],t+p[2]));X.fillStyle='#7a5a3c';X.fillRect(L-1400,yf-330,3900,340);tex('madera',L-1400,yf-330,3900,340,{a:.6,s:1.3,tinte:'120,84,52'});
 X.fillStyle='rgba(0,0,0,.18)';for(let i=0;i<34;i++)X.fillRect(L-1400+i*116+rnd(i+5)*40,yf-330,5,340);X.fillStyle=gl(0,yf,0,1920,[[0,'#c9a26a'],[1,'#9a7646']]);X.fillRect(L-1400,yf,3900,1500);tex('arena',L-1400,yf,3900,1100,{a:.5,s:1.5});X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L-1400,yf-6,3900,16);
 X.fillStyle='rgba(20,24,40,.4)';X.beginPath();X.moveTo(L-1400,yf);X.lineTo(L+(o.sombra||260),yf);X.lineTo(L+(o.sombra||260)+420,2400);X.lineTo(L-1400,2400);X.closePath();X.fill();haz(L+1100,300,L+500,1700,60,420,SOL,.14)}
// tienda de tablones (fachada genérica). letrero 0…1: se enciende el nombre que dice el guion · puerta 0…1 abierta
function tienda(x,yb,s,t,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.fillRect(-270,-6,540,22);X.fillStyle='#c8a26a';X.fillRect(-260,-420,520,420);tex('madera',-260,-420,520,420,{a:.5,s:1.2});X.fillStyle='rgba(0,0,0,.12)';for(let i=1;i<9;i++)X.fillRect(-260,-420+i*47,520,4);
 X.fillStyle='#4a2f22';X.beginPath();X.moveTo(-292,-420);X.lineTo(-240,-486);X.lineTo(240,-486);X.lineTo(292,-420);X.closePath();X.fill();
 X.fillStyle='#12303a';rr(-214,-404,428,78,8);X.fill();X.strokeStyle='#e9d9b0';X.lineWidth=4;rr(-214,-404,428,78,8);X.stroke();if(o.letrero>0){X.save();X.globalAlpha=o.letrero;luz(0,-365,300,'255,214,150',.3,70);txt('THREE SHEETS LIQUOR',0,-361,28,'#ffe9b8',{w:800});X.restore()}
 for(let i=0;i<8;i++){X.fillStyle=i%2?'#e9e2c8':'#1f7a78';X.beginPath();X.moveTo(-250+i*62.5,-318);X.lineTo(-187.5+i*62.5,-318);X.lineTo(-183+i*62.5+ (i-3.5)*3,-268);X.lineTo(-254+i*62.5+(i-3.5)*3,-268);X.closePath();X.fill()}
 X.fillStyle='#0f2028';rr(-220,-240,200,150,6);X.fill();[[-190,.5,'#7a3e12'],[-150,.42,'#1f4a3a'],[-112,.52,'#5a1c1c'],[-74,.44,'#7a3e12'],[-44,.38,'#3a2a5a']].forEach(b=>botella(b[0],-96,b[1]*.6,{col:b[2],col2:b[2],lisa:1}));X.fillStyle='rgba(255,255,255,.1)';X.beginPath();X.moveTo(-220,-240);X.lineTo(-150,-240);X.lineTo(-220,-150);X.closePath();X.fill();X.strokeStyle='#4a2f22';X.lineWidth=10;rr(-220,-240,200,150,6);X.stroke();
 const pa=o.puerta||0;X.fillStyle=pa>0?'#ffd9a0':'#0f2028';X.fillRect(40,-250,140,250);if(pa>0)luz(110,-120,220,'255,214,150',.5*pa);X.save();X.translate(40,0);X.scale(1-pa*.8,1);X.fillStyle='#7a4f30';X.fillRect(0,-250,140,250);X.fillStyle='#12303a';X.fillRect(16,-232,108,110);X.fillStyle='rgba(255,255,255,.14)';X.beginPath();X.moveTo(16,-232);X.lineTo(70,-232);X.lineTo(16,-160);X.closePath();X.fill();X.fillStyle=ORO;X.beginPath();X.arc(118,-110,8,0,7);X.fill();X.restore();
 X.strokeStyle='#4a2f22';X.lineWidth=10;X.strokeRect(40,-250,140,250);X.fillStyle='#8a8f96';X.fillRect(20,-8,180,14);X.restore()}
function casa(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);const h=o.pil?70:0;if(o.pil){X.fillStyle='#5a3d24';[-110,-40,40,110].forEach(q=>X.fillRect(q-7,-h,14,h))}X.fillStyle=o.col;X.fillRect(-140,-h-200,280,200);X.fillStyle='rgba(0,0,0,.1)';for(let i=1;i<5;i++)X.fillRect(-140,-h-200+i*40,280,3);X.fillStyle=o.techo;X.beginPath();X.moveTo(-164,-h-200);X.lineTo(0,-h-290);X.lineTo(164,-h-200);X.closePath();X.fill();X.fillStyle='#12303a';X.fillRect(-100,-h-150,70,70);X.fillStyle='#4a2f22';X.fillRect(30,-h-130,60,130);X.restore()}
function globo(x,y,w,h,q,tx,fn){if(q<=0)return;const k=back(Math.min(1,q));X.save();X.translate(x,y);X.scale(k,k);X.fillStyle='rgba(0,0,0,.3)';rr(-w/2+6,-h/2+10,w,h,26);X.fill();X.fillStyle='#fff';rr(-w/2,-h/2,w,h,26);X.fill();X.beginPath();X.moveTo(tx-22,h/2-4);X.lineTo(tx+(tx<0?-34:34),h/2+40);X.lineTo(tx+22,h/2-4);X.closePath();X.fill();if(fn)fn();X.restore()}
function caja(x,yb,s,g){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';X.beginPath();X.ellipse(0,0,150,16,0,0,7);X.fill();X.fillStyle='#22282e';rr(-116,-14,40,18,4);X.fill();rr(76,-14,40,18,4);X.fill();X.fillStyle=gl(-130,0,130,0,[[0,'#3a444e'],[.5,'#5a6672'],[1,'#2f3840']]);rr(-130,-340,260,330,14);X.fill();tex('metal',-130,-340,260,330,{a:.3,v:3});
 X.strokeStyle='rgba(255,255,255,.18)';X.lineWidth=2;[[-90,-300,-30,-250],[40,-120,100,-80],[-100,-90,-60,-70],[20,-290,90,-270]].forEach(r=>{X.beginPath();X.moveTo(r[0],r[1]);X.lineTo(r[2],r[3]);X.stroke()});
 X.strokeStyle='#20262d';X.lineWidth=6;rr(-108,-318,216,286,10);X.stroke();X.fillStyle='#20262d';rr(-128,-290,14,50,5);X.fill();rr(-128,-110,14,50,5);X.fill();
 X.save();X.translate(-24,-176);X.rotate((g||0)*2.4);X.fillStyle='#cfd6dc';X.beginPath();X.arc(0,0,46,0,7);X.fill();X.fillStyle='#22282e';X.beginPath();X.arc(0,0,30,0,7);X.fill();X.strokeStyle='#cfd6dc';X.lineWidth=4;for(let i=0;i<10;i++){const a=i*.628;X.beginPath();X.moveTo(Math.cos(a)*20,Math.sin(a)*20);X.lineTo(Math.cos(a)*28,Math.sin(a)*28);X.stroke()}X.fillStyle='#e23a3a';X.fillRect(-2,-30,4,14);X.restore();
 X.save();X.translate(62,-176);X.rotate(-(g||0)*1.2);X.strokeStyle='#cfd6dc';X.lineWidth=10;X.lineCap='round';for(let i=0;i<3;i++){const a=i*2.094;X.beginPath();X.moveTo(0,0);X.lineTo(Math.cos(a)*34,Math.sin(a)*34);X.stroke()}X.fillStyle='#8e98a4';X.beginPath();X.arc(0,0,10,0,7);X.fill();X.restore();X.restore()}
function contador(x,yt,s,t){X.save();X.translate(x,yt);X.scale(s,s);X.fillStyle='#2f7d4f';X.save();X.translate(0,-150);X.rotate(-.12);rr(-80,-64,160,84,6);X.fill();X.fillStyle='#3f9c63';rr(-80,-64,160,10,4);X.fill();X.restore();X.fillStyle='#d9dde2';rr(-120,-150,240,150,16);X.fill();X.fillStyle='#aab3bc';rr(-120,-40,240,40,10);X.fill();
 X.fillStyle='#0c1410';rr(-96,-134,112,46,6);X.fill();X.fillStyle='#22c55e';for(let i=0;i<4;i++){const h=8+20*Math.abs(Math.sin(t*6+i*1.3));X.fillRect(-84+i*24,-94-h,14,h)}X.fillStyle='#c0392b';X.beginPath();X.arc(52,-112,10,0,7);X.fill();X.fillStyle='#22c55e';X.beginPath();X.arc(86,-112,10,0,7);X.fill();
 X.fillStyle='#14171b';rr(-90,-74,180,30,6);X.fill();for(let i=0;i<3;i++){const q=((t*5+i/3)%1);X.fillStyle=`rgba(63,156,99,${1-q})`;rr(-72,-70+q*20,144,6,3);X.fill()}X.restore()}

// ---------- 01 · gancho: el loro en primer plano inclina la cabeza hacia el generador; cae una moneda de la rejilla ----------
function p01(L,t){const xm=T.x_money,xw=T.x_walk,xc=T.x_cash1,xo=T.x_more,f=T.c02,foco=eio(seg(t,xw-.1,xw+.5)),inc=.3*eio(seg(t,xm-.5,xm))-.14*eio(seg(t,xo-.2,xo+.2)),q=seg(t,xc-.25,xc+.55),av=golpe(t,xo,.9),kf=[[0,400,1090,1.5],[xm,440,1100,1.36],[xc,620,1130,1.2],[f,680,1140,1.26]];
 plano(L,t,kf,cm=>{muro(L,cm,t,{});rejilla(L+850,1020,190,120,{aviso:.9*av});generador(L+850,1450,.9,t,{refl:seg(t,xw,xw+1.2)});
  if(q>0){const u=Math.min(1,q/.6),v=Math.max(0,(q-.6)/.4),my=u<1?lerp(1085,1425,u*u):1425-Math.abs(Math.sin(v*Math.PI))*50*(1-v);monedaP(L+800-q*90,my,22,q*14)}});
 desenfoca(9*(1-foco));
 plano(L,t,kf,cm=>{borroso(7*foco,()=>{percha(L+300,1500,520);loro(L+300,1500,1.5,t,{inc})})});
 arriba(L,.6)}

// ---------- 02 · al comienzo del juego, en Key Lento: barrio costero y la tienda ----------
function p02(L,t){const c=T.c02,xk=T.x_key,f=T.c03;
 plano(L,t,[[c,520,1090,1.04],[f,690,1200,1.5]],cm=>{X.fillStyle=gl(0,200,0,1130,[[0,'#1d5f8f'],[.6,'#58a9c9'],[1,'#f3cf9a']]);X.fillRect(L-1400,-900,3900,2060);luz(L+250+par(cm,.85),900,460,SOL,.55);
  X.fillStyle=gl(0,1100,0,1250,[[0,'#2a8fa8'],[1,'#1f6f8f']]);X.fillRect(L-1400,1100,3900,160);for(let i=0;i<14;i++){X.fillStyle=`rgba(255,255,255,${.25+.2*Math.sin(t*2+i)})`;X.fillRect(L-300+i*140+rnd(i)*80+Math.sin(t+i)*14+par(cm,.7),1120+rnd(i+3)*90,60+rnd(i+5)*60,4)}
  X.fillStyle='#d9bd8a';X.fillRect(L-1400,1230,3900,300);tex('arena',L-1400,1230,3900,300,{a:.5,s:1.4});[[40,.5,0],[350,.4,2],[1060,.56,4]].forEach(p=>palmeraV(L+p[0]+par(cm,.45),1262,p[1],t+p[2]));
  casa(L+190+par(cm,.25),1440,1,{col:'#e9a0a8',techo:'#7a3b3b',pil:1});casa(L+470+par(cm,.25),1440,.66,{col:'#9ad0c2',techo:'#35605a'});
  X.fillStyle='#2b2f36';X.fillRect(L-1400,1470,3900,1100);tex('concreto',L-1400,1470,3900,600,{a:.22,v:5});X.fillStyle='#e9eef2';X.fillRect(L-1400,1470,3900,9);X.fillStyle='#d9b24a';for(let i=-6;i<20;i++)X.fillRect(L+i*250,1640,130,12);
  tienda(L+800,1474,.84,t,{})});
 arriba(L,.6);placa(L+540,650,1.15,'KEY LENTO',eio(seg(t,xk-.1,xk+.2)),{w:330})}

// ---------- 03 · la vecina te manda a comprar ron a una tienda llamada Three Sheets Liquor ----------
function p03(L,t){const c=T.c03,xr=T.x_rum,xt=T.x_three,f=T.c04,ca=eio(seg(t,xr-.2,f-.25)),en=eio(seg(t,f-.7,f-.1)),gb=eio(seg(t,c+.5,c+.75))*(1-eio(seg(t,xt-.5,xt-.2)));
 plano(L,t,[[c,430,1180,1.22],[xr,450,1170,1.24],[xt,600,1130,1.2],[f,650,1150,1.25]],cm=>{X.fillStyle='#58a9c9';X.fillRect(L-1400,-900,3900,2500);X.fillStyle='#8a8f96';X.fillRect(L-1400,1500,3900,1200);tex('concreto',L-1400,1500,3900,700,{a:.3,v:4});
  tienda(L+560,1500,2,t,{letrero:eio(seg(t,xt-.15,xt+.15)),puerta:en});
  silueta(L+170,1570,.95,'#3a2a3a',{brazo:1,bx:120,by:-190});X.save();X.globalAlpha=1-.9*en;silueta(L+lerp(390,790,ca),1570-30*en,.95*(1-.14*en),'#10141a',{});X.restore();
  globo(L+280,1090,190,170,gb,-40,()=>botella(0,64,.36,{}))});
 arriba(L,.6)}

// ---------- 04 · muchos jugadores toman la botella y se van ----------
function p04(L,t){const c=T.c04,xg=T.x_grab,xl=T.x_leave,f=T.c05,g=eio(seg(t,xg-.4,xg)),m=eio(seg(t,xg+.12,xl+.3)),kf=[[c,500,1090,1.2],[f,600,1090,1.3]],COL=[['#7a3e12','#b8651c'],['#1f4a3a','#3f8a6a'],['#3a2a5a','#6a4a9a'],['#5a1c1c','#a03a3a'],['#8a8468','#cfc8a8']];
 plano(L,t,kf,cm=>{X.fillStyle='#2a1c14';X.fillRect(L-1400,-900,3900,3800);tex('madera',L-1400,300,3900,1700,{a:.5,s:1.6,tinte:'70,44,26'});
  [900,1180,1470].forEach((y,j)=>{let x=L-260+rnd(j+3)*60;for(let i=0;i<16;i++){const k=Math.floor(rnd(i*7+j*13)*5),s=.6+rnd(i+j*5)*.26;if(!(j===1&&x>L+330&&x<L+540))botella(x,y,s,{col:COL[k][0],col2:COL[k][1],lisa:rnd(i+j)>.5});x+=96+rnd(i+j*9)*70}X.fillStyle='#4a321e';X.fillRect(L-1400,y,3900,30);X.fillStyle='rgba(0,0,0,.3)';X.fillRect(L-1400,y+30,3900,16)});
  luz(L+1300,1080,560,SOL,.4)});
 desenfoca(5);
 plano(L,t,kf,cm=>{const bx=L+lerp(430,1560,m*m),by=1180-70*Math.sin(Math.min(1,m*1.6)*1.57),rot=.22*m,hx=bx+70+(1-g)*620,hy=by-150;
  mano(hx,hy,-.12,1.4,-1,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'atras',lx:118,ly:44});botella(bx,by,1.25,{rot});mano(hx,hy,-.12,1.4,-1,{curl:[.5,.54,.58,.6],pulgar:.35,parte:'pulgar',lx:118,ly:44})});
 arriba(L,.6)}

// ---------- 05 · pero escucha: se oyen animales en algún lugar del fondo ----------
function p05(L,t){const c=T.c05,xh=T.x_hear,xb=T.x_back,f=T.c06,dx=L+430,dw=290,dy=760,dh=720;
 plano(L,t,[[c,430,1150,1.1],[xh,520,1140,1.3],[f,575,1100,1.5]],cm=>{interior(L,{p0:'#2a1c14',p1:'#3a2618',tex:'madera',ta:.5,yp:1480,piso:['#3a2a1c','#2a1e14'],pisoTex:'madera',pa:.5});
  [[60,1480,210,150,'#6b4a2e'],[90,1330,170,130,'#7a5636'],[900,1480,200,170,'#6b4a2e'],[930,1310,150,120,'#5a3d24'],[1090,1480,160,220,'#7a5636']].forEach(b=>{X.fillStyle=b[4];X.fillRect(L+b[0],b[1]-b[3],b[2],b[3]);X.strokeStyle='rgba(0,0,0,.3)';X.lineWidth=5;X.strokeRect(L+b[0],b[1]-b[3],b[2],b[3]);X.beginPath();X.moveTo(L+b[0],b[1]-b[3]);X.lineTo(L+b[0]+b[2],b[1]);X.stroke()});
  X.fillStyle='#fff2c8';X.fillRect(dx,dy,dw,dh);X.fillStyle='#1c120c';X.fillRect(dx-18,dy-18,dw+36,18);X.fillRect(dx-18,dy-18,18,dh+18);X.fillRect(dx+dw,dy-18,18,dh+18);
  X.fillStyle=gl(dx,0,dx+dw,0,[[0,'#5a3d24'],[1,'#6b4a2e']]);X.fillRect(dx,dy,dw-26,dh-14);X.strokeStyle='rgba(0,0,0,.25)';X.lineWidth=5;X.strokeRect(dx+30,dy+40,dw-86,260);X.strokeRect(dx+30,dy+340,dw-86,300);X.fillStyle=ORO;X.beginPath();X.arc(dx+dw-62,dy+350,10,0,7);X.fill();
  // luz que entra por debajo y por la rendija, con sombras de plumas que la cruzan
  X.save();X.beginPath();X.moveTo(dx,1478);X.lineTo(dx+dw,1478);X.lineTo(dx+dw+200,1900);X.lineTo(dx-200,1900);X.closePath();X.clip();X.fillStyle='rgba(255,236,190,.42)';X.fillRect(dx-300,1470,dw+600,460);
  for(let i=0;i<4;i++){const u=((t*.55+i*.27)%1),px=dx-200+u*(dw+400),py=1560+rnd(i+4)*220;X.save();X.translate(px,py);X.rotate(-.5+Math.sin(t*3+i)*.5);X.fillStyle='rgba(20,12,8,.55)';X.beginPath();X.moveTo(-70,0);X.quadraticCurveTo(0,-34,80,0);X.quadraticCurveTo(0,30,-70,0);X.fill();X.fillRect(-96,-3,30,6);X.restore()}X.restore();
  for(let i=0;i<3;i++){const u=((t*.9+i*.33)%1),py=dy+60+u*(dh-120);X.fillStyle='rgba(20,12,8,.6)';X.fillRect(dx+dw-26,py,26,34)}
  const so=seg(t,xh-.2,f);if(so>0)for(let i=0;i<3;i++){const u=((t*1.1+i/3)%1);X.strokeStyle=`rgba(255,255,255,${.6*(1-u)})`;X.lineWidth=7;X.beginPath();X.arc(dx+dw-10,dy+dh*.45,60+u*220,-.7,.7);X.stroke();X.beginPath();X.arc(dx+dw-10,dy+dh*.45,60+u*220,Math.PI-.7,Math.PI+.7);X.stroke()}
  borroso(4,()=>silueta(L+lerp(-40,130,eio(seg(t,c,xh-.3))),1700,1.5,'#0a0c10',{}))});
 arriba(L,.62)}

// ---------- 06 · detrás de la tienda: un patio oculto con animales exóticos de contrabando, y unos tipos que lo vigilan ----------
function p06(L,t){const c=T.c06,xy=T.x_yard,xa=T.x_animals,xg=T.x_guys,f=T.c07,ab=eio(seg(t,c,c+.7)),g=eio(seg(t,xg-.6,xg+.3));
 plano(L,t,[[c,540,1170,1.5],[c+.9,540,1160,1.1],[xa,530,1170,1.15],[f,560,1150,1.24]],cm=>{patio(L,cm,t,{});generador(L+1010,1262,.46,t,{});
  if(g>0){X.save();X.globalAlpha=g;silueta(L+lerp(1180,790,g),1300,.74,'#1a2030',{});silueta(L+lerp(1300,905,g),1310,.8,'#141a26',{brazo:-1,bx:90,by:-170});X.restore()}
  X.fillStyle='#6b4a2e';X.fillRect(L+420,1240,200,96);X.strokeStyle='rgba(0,0,0,.3)';X.lineWidth=5;X.strokeRect(L+420,1240,200,96);jaula(L+520,1240,170,236,()=>{percha(L+520,1150,130);loro(L+520,1150,.36,t,{cola:.7})},{n:4,sem:23,lw:6});
  jaula(L+190,1570,300,380,()=>{percha(L+190,1400,230);ave(L+180,1400,1.1,1)},{n:7,sem:1});
  jaula(L+560,1640,250,290,()=>mono(L+560,1624,1.05,t),{n:5,sem:9});
  jaula(L+900,1610,300,180,()=>iguana(L+900,1596,1),{n:7,sem:17,r:8})});
 if(ab<1){X.fillStyle='#120c08';const w=560*(1-ab);X.fillRect(L,0,w,1920);X.fillRect(L+1080-w,0,w,1920)}
 arriba(L,.6)}

// ---------- 07 · G2: lo que el loro no te dice, y donde está el resto del dinero ----------
function p07(L,t){const c=T.c07,xt=T.x_tell7,xr=T.x_rest,f=T.c08,giro=eio(seg(t,c+.25,c+.9)),foco=eio(seg(t,xr-.4,xr+.2)),kf=[[c,400,1130,1.22],[xr,560,1140,1.2],[f,700,1160,1.36]];
 plano(L,t,kf,cm=>{muro(L,cm,t,{});rejilla(L+860,1020,190,120,{aviso:.8*foco*(.6+.4*Math.sin(t*6))});generador(L+850,1450,.95,t,{refl:seg(t,xr-.2,xr+.9),brillo:foco})});
 desenfoca(8*(1-foco));
 plano(L,t,kf,cm=>{borroso(6*foco,()=>{jaula(L+330,1450,370,700,()=>{percha(L+330,1130,280);loro(L+330,1130,.95,t,{sx:lerp(-1,1,giro),inc:.12*Math.sin(t*1.6)})},{n:6,sem:3});luz(L+330,980,270,'255,60,40',.2)})});
 arriba(L,.6)}

// ---------- 08 · en una jaula hay un loro rojo: pregúntale por el dinero y te dice que revises el generador ----------
function p08(L,t){const c=T.c08,xa=T.x_ask,xt=T.x_tells,xg=T.x_gen,f=T.c09,pr=eio(seg(t,xa-.1,xa+.2))*(1-eio(seg(t,xt-.35,xt-.05))),resp=eio(seg(t,xt,xt+.25)),gb=eio(seg(t,xg-.3,xg+.1)),ha=resp>0&&t<xg+.5?.5+.5*Math.sin(t*16):0;
 plano(L,t,[[c,450,1150,1.1],[xa,450,1140,1.2],[xt,480,1130,1.2],[f,520,1140,1.26]],cm=>{muro(L,cm,t,{});rejilla(L+800,1020,170,110,{});generador(L+790,1450,.7,t,{brillo:gb,refl:seg(t,xg-.2,xg+.7)});
  jaula(L+360,1450,370,700,()=>{percha(L+360,1130,280);loro(L+360,1130,.95,t,{inc:.28*resp,habla:ha})},{n:6,sem:3});luz(L+360,980,250,'255,60,40',.14);
  globo(L+170,930,210,160,pr,-40,()=>{monedaP(-40,0,40,0);txt('$',-40,4,44,'#8a6410',{w:900});txt('?',52,6,84,'#22282e',{w:900})});
  globo(L+650,800,220,170,resp,-60,()=>generador(0,62,.36,t,{}));
  placa(L+790,1160,1,'GENERATOR',gb,{ts:40,w:300})});
 borroso(5,()=>{X.fillStyle='#0a0d12';X.beginPath();X.arc(L+130,1590,150,0,7);X.fill();X.beginPath();X.moveTo(L-220,1920);X.quadraticCurveTo(L-140,1700,L+130,1730);X.quadraticCurveTo(L+400,1740,L+450,1920);X.closePath();X.fill()});
 arriba(L,.6)}

// ---------- 09 · mira la rejilla de la pared justo al lado: adentro hay unos 1.300 dólares ----------
function p09(L,t){const c=T.c09,xv=T.x_vent,xi=T.x_inside,xn=T.x_1300,f=T.c10,av=eio(seg(t,xv-.2,xv+.1))*(1-eio(seg(t,xi-.4,xi-.1))),ab=eio(seg(t,xi-.35,xi+.25)),ma=eio(seg(t,xi-.85,xi-.35));
 plano(L,t,[[c,440,1060,1.12],[xi,560,1050,1.36],[f,640,1070,1.36]],cm=>{muro(L,cm,t,{yp:1500});generador(L+60,1500,1.5,t,{});
  rejilla(L+570,1040,380,250,{ab,dinero:ab,n:7,aviso:av*(.7+.3*Math.sin(t*8)),dx:1,dy:.1,giro:.12});   // la tapa sale de costado: las lamas son horizontales y así el patrón no "salta" entre cuadros
  if(ma>0){const hx=L+570+60+ab*380+(1-ma)*700,hy=1050+ab*25;mano(hx,hy,-.1,1.4,-1,{curl:[.6,.64,.68,.7],pulgar:.3})}});
 arriba(L,.6);placa(L+440,1530,1.2,'ABOUT $1,300',eio(seg(t,xn-.1,xn+.2)),{w:420,tc:'#ffe9b8'})}

// ---------- 10 · no te vayas todavía: la trastienda tiene una caja fuerte y un contador de billetes, con más ----------
function p10(L,t){const c=T.c10,xr=T.x_room,xs=T.x_safe,xc=T.x_counter,xe=T.x_even,f=T.c11,gs=golpe(t,xs,.6),mas=eio(seg(t,xe-.2,xe+.5));
 plano(L,t,[[c,300,1140,1.18],[xr,360,1140,1.2],[xs,540,1170,1.42],[xc,810,1130,1.45],[f,860,1110,1.6]],cm=>{interior(L,{p0:'#3a4046',p1:'#4a525a',tex:'concreto',ta:.5,yp:1420,piso:['#2c3238','#22272c'],pisoTex:'concreto',pa:.5});
  X.strokeStyle='#14171b';X.lineWidth=5;X.beginPath();X.moveTo(L+560,300);X.lineTo(L+560,700);X.stroke();haz(L+560,720,L+560,1500,40,520,'255,236,190',.16);luz(L+560,720,70,'255,236,190',.9);X.fillStyle='#fff2c8';X.beginPath();X.arc(L+560,720,18,0,7);X.fill();
  X.fillStyle='#d9bd8a';X.fillRect(L+40,800,240,640);luz(L+160,1120,340,SOL,.3);X.fillStyle='#1c120c';X.fillRect(L+22,782,276,18);X.fillRect(L+22,782,18,658);X.fillRect(L+280,782,18,658);silueta(L+lerp(110,190,eio(seg(t,c,xr))),1450,.9,'#0a0d12',{});
  caja(L+560,1420,1.15,gs);if(gs>0)luz(L+560,1220,300,'255,236,190',.25*gs);
  X.fillStyle='#3a444e';X.fillRect(L+730,1234,18,190);X.fillRect(L+1030,1234,18,190);X.fillStyle='#6b7682';X.fillRect(L+700,1210,380,26);tex('metal',L+700,1210,380,26,{a:.3,v:1});contador(L+850,1210,.95,t);
  for(let i=0;i<1+Math.floor(mas*3.99);i++)fajo(L+1010,1196-i*26,.52,(i%2?.06:-.05));if(mas>0)luz(L+1000,1150,200,'120,255,160',.22*mas)});
 arriba(L,.6)}

// ---------- 11 · un loro que habla te puede dar más de 2.000 dólares antes de que la historia arranque ----------
function p11(L,t){const c=T.c11,xh=T.x_hand,xn=T.x_2000,f=T.c12,j=eio(seg(t,c+.15,xh+.25)),g=golpe(t,xn,.7),kf=[[c,500,1130,1.14,-.025],[xn,540,1140,1.22,0],[f,585,1130,1.28,.025]];
 plano(L,t,kf,cm=>{patio(L,cm,t,{yf:1130,sombra:120});X.fillStyle='#5a3d24';X.fillRect(L+748,1070,24,300);percha(L+760,1070,250);loro(L+760,1070,.6,t,{dir:-1,inc:.14*Math.sin(t*1.5),cola:.8})});
 desenfoca(3.5);
 plano(L,t,kf,cm=>{meson(L,1340,{tex:'madera',col:'#6b4a2e',ta:.7});luz(L+540,1500,420,'255,214,120',.16+.25*g);
  [[-1,0,-.1],[-1,1,.07]].forEach(p=>fajo(L+lerp(-260,430,j)+p[1]*30,1560-p[1]*30,1.05,p[2]*(1-j)+p[1]*.03));
  [[1,0,.12],[1,1,-.08],[1,2,.05],[1,3,-.03]].forEach(p=>fajo(L+lerp(1340,670,j)-p[1]*14,1570-p[1]*30,1.05,p[2]*(1-j)-p[1]*.02));
  placa(L+540,1250,1.25+.1*g,'OVER $2,000',eio(seg(t,xn-.1,xn+.2)),{w:400,tc:'#ffe9b8'})});
 arriba(L,.6)}

// ---------- 12 · CTA: el loro en primer plano y el patio abierto detrás ----------
function p12(L,t){const c=T.c12;
 plano(L,t,[[c,460,1190,1.16],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{patio(L,cm,t,{yf:1260,sombra:60});X.fillStyle='#5a3d24';X.fillRect(L+398,1410,24,520);percha(L+410,1410,300);loro(L+410,1410,.72,t,{inc:.26*Math.sin((t-c)*1.4),cola:.4})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12].forEach((f,i)=>{NUEVOS['dc_sgtaen19_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SGTAEN19 · FIN =====
</script>
