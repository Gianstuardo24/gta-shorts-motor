<script>
// ===== DC · SCATS21 · INICIO ===== (Cats 21h · Your Cat Will NEVER Taste THIS · lote del 28-nov · una escena por línea del guion)
// El receptor se muestra como dos piezas que encajan (rosa y verde azulado). No se nombran genes. El sabor que "sigue funcionando" es el de la carne, como dice el guion.
(function(){
const {cam,cierreCanal,SET}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,hojaP,renglones,tarj,desenfoca,borroso}=window.B28;
const RA='255,120,170',RB='90,210,200',AMB='255,190,90';

// ---------- porción de pastel en su plato ----------
function pastel(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(0,6,170,20,0,0,7);X.fill();X.fillStyle='#f4f1ea';X.beginPath();X.ellipse(0,-6,160,22,0,0,7);X.fill();X.fillStyle='#dcd7cc';X.beginPath();X.ellipse(0,-2,110,12,0,0,7);X.fill();
 X.fillStyle='#e9c98f';rr(-100,-150,200,140,10);X.fill();X.fillStyle='#fff3e0';X.fillRect(-100,-112,200,16);X.fillRect(-100,-66,200,16);X.fillStyle='rgba(120,70,20,.12)';for(let i=0;i<14;i++){X.beginPath();X.arc(-88+rnd(i)*176,-140+rnd(i+9)*120,3,0,7);X.fill()}
 X.fillStyle=o.gris?'#b9b4b8':'#f48fb1';X.beginPath();X.moveTo(-106,-146);X.quadraticCurveTo(-108,-178,-80,-178);X.lineTo(80,-178);X.quadraticCurveTo(108,-178,106,-146);X.lineTo(106,-128);X.quadraticCurveTo(92,-104,78,-130);X.quadraticCurveTo(60,-150,44,-124);X.quadraticCurveTo(26,-96,8,-128);X.quadraticCurveTo(-12,-152,-30,-126);X.quadraticCurveTo(-52,-98,-70,-130);X.quadraticCurveTo(-90,-150,-106,-128);X.closePath();X.fill();
 X.fillStyle='rgba(255,255,255,.4)';rr(-84,-172,110,9,5);X.fill();
 X.fillStyle='#fffaf0';[[-30,-196,26],[0,-206,30],[30,-196,26]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],p[2],0,7);X.fill()});X.fillStyle='#d8343f';X.beginPath();X.arc(0,-236,20,0,7);X.fill();X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.arc(-6,-242,6,0,7);X.fill();X.restore()}
function lengua(x,y,s,rot,ext){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.fillStyle='#ff7fa3';rr(0,-11,34*ext+6,22,11);X.fill();X.strokeStyle='#d94f72';X.lineWidth=2.5;X.beginPath();X.moveTo(6,0);X.lineTo(34*ext,0);X.stroke();X.restore()}
// ---------- cuenco de lado con agua ----------
function cuenco(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(0,4,150,16,0,0,7);X.fill();
 X.fillStyle=gl(-140,0,140,0,[[0,o.c0||'#cfd6dc'],[.5,o.c1||'#f3f6f8'],[1,o.c0||'#b9c2c9']]);X.beginPath();X.moveTo(-140,-110);X.lineTo(140,-110);X.quadraticCurveTo(130,-10,80,0);X.lineTo(-80,0);X.quadraticCurveTo(-130,-10,-140,-110);X.closePath();X.fill();
 X.fillStyle='#e8eef2';X.beginPath();X.ellipse(0,-110,140,26,0,0,7);X.fill();X.fillStyle=o.agua||'#9fd0e8';X.beginPath();X.ellipse(0,-108,124,19,0,0,7);X.fill();X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.ellipse(-40,-112,40,5,0,0,7);X.fill();
 if(o.franja){X.fillStyle=o.franja;rr(-112,-74,224,16,8);X.fill()}X.restore()}
function cubos(x,yb,s,a){if(a<=0)return;X.save();X.translate(x,yb);X.scale(s*(.6+.4*back(a)),s*(.6+.4*back(a)));X.globalAlpha=Math.min(1,a*1.5);[[0,0,0],[52,0,.1],[24,-44,-.08]].forEach(p=>{X.save();X.translate(p[0],p[1]);X.rotate(p[2]);X.fillStyle='rgba(0,0,0,.15)';rr(-20,-36,48,44,6);X.fill();X.fillStyle='#fdfdfb';rr(-24,-44,48,44,6);X.fill();X.fillStyle='rgba(0,0,0,.08)';rr(-24,-12,48,12,6);X.fill();X.restore()});X.restore()}
// ---------- hélice de ADN vertical, de cuentas. luz:[u0,u1] tramo iluminado · falta:[u0,u1] tramo ausente ----------
function helice(x,y0,y1,w,t,o){o=o||{};const n=Math.round((y1-y0)/26),ph=t*(o.vel===undefined?1.2:o.vel),al=o.a===undefined?1:o.a;X.save();X.lineCap='round';X.globalAlpha=al;
 for(let pass=0;pass<2;pass++)for(let i=0;i<=n;i++){const u=i/n,y=lerp(y0,y1,u),a=u*(o.vueltas||3)*Math.PI*2+ph,xa=x+Math.sin(a)*w,xb=x-Math.sin(a)*w,z=Math.cos(a),en=o.luz&&u>=o.luz[0]&&u<=o.luz[1],fal=o.falta&&u>=o.falta[0]&&u<=o.falta[1];if(fal)continue;
  if(pass===0){if(i%2===0){X.strokeStyle=en?'rgba(255,120,170,.9)':'rgba(150,200,230,.4)';X.lineWidth=en?7:5;X.beginPath();X.moveTo(xa,y);X.lineTo(xb,y);X.stroke()}}
  else[[xa,z,'120,200,255'],[xb,-z,'90,150,230']].forEach(([xx,zz,c])=>{X.fillStyle=en?`rgba(255,150,190,${.75+.25*zz})`:`rgba(${c},${.6+.35*zz})`;X.beginPath();X.arc(xx,y,(9+5*zz)*(en?1.3:1),0,7);X.fill()})}
 if(o.falta){const ya=lerp(y0,y1,o.falta[0]),yb=lerp(y0,y1,o.falta[1]);X.setLineDash([12,12]);X.strokeStyle='rgba(255,255,255,.7)';X.lineWidth=5;rr(x-w-22,ya,2*w+44,yb-ya,18);X.stroke();X.setLineDash([])}X.restore()}
// ---------- receptor de dos piezas. sep: 0 unido .. 1 separado · roto: 0..1 a la pieza B le falta un trozo · on: brillo de señal · apag: apagado ----------
function sensor(x,y,s,o){o=o||{};const sep=(o.sep||0)*150,ca=o.ca||RA,cb=o.cb||RB,on=o.on||0,ro=o.roto||0,ap=o.apag?.4:1;X.save();X.translate(x,y);X.scale(s,s);X.lineCap='round';X.lineJoin='round';
 [[-1,ca],[1,cb]].forEach(([q,c])=>{X.strokeStyle=`rgba(${c},${.75*ap})`;X.lineWidth=22;X.beginPath();X.moveTo(q*(70+sep),70);X.bezierCurveTo(q*(40+sep),150,q*(100+sep),210,q*(64+sep),320);X.stroke()});
 X.fillStyle=`rgba(${ca},${.6*ap})`;X.strokeStyle=`rgba(${ca},${ap})`;X.lineWidth=7;X.beginPath();X.ellipse(-62-sep,0,118,98,-.25,0,7);X.fill();X.stroke();X.fillStyle=`rgba(255,255,255,${.22*ap})`;X.beginPath();X.ellipse(-92-sep,-36,40,22,-.5,0,7);X.fill();
 X.save();X.translate(62+sep,0);X.fillStyle=`rgba(${cb},${.6*ap})`;X.strokeStyle=`rgba(${cb},${ap})`;X.beginPath();const a0=-1.15,a1=a0+1.5*ro;
 if(ro>.02){X.moveTo(0,0);X.ellipse(0,0,118,98,.25,a1,a0+Math.PI*2);X.closePath()}else X.ellipse(0,0,118,98,.25,0,7);X.fill();X.stroke();
 if(ro>.02){X.setLineDash([12,12]);X.strokeStyle=`rgba(255,255,255,${.75*ro})`;X.lineWidth=5;X.beginPath();X.moveTo(0,0);X.ellipse(0,0,118,98,.25,a0,a1);X.closePath();X.stroke();X.setLineDash([])}X.restore();
 if(on>0){luz(0,0,240,'255,240,200',.55*on);X.fillStyle=`rgba(255,250,230,${.85*on})`;X.beginPath();X.ellipse(0,0,34,62,0,0,7);X.fill()}X.restore()}
function membrana(L,y,t,a){X.save();X.globalAlpha=a===undefined?1:a;for(let i=-6;i<66;i++){const x=L-200+i*46+Math.sin(t*1.2+i)*3;X.strokeStyle='rgba(190,170,230,.35)';X.lineWidth=5;X.beginPath();X.moveTo(x,y+18);X.lineTo(x,y+70);X.stroke();X.fillStyle='rgba(200,180,240,.75)';X.beginPath();X.arc(x,y,19,0,7);X.fill();X.beginPath();X.arc(x,y+88,19,0,7);X.fill()}X.restore()}
function pulso(x,y0,y1,t,k,rgb,a){if(t<k||a<=0)return;for(let j=0;j<3;j++){const u=((t-k)*.9+j/3)%1;X.fillStyle=`rgba(${rgb},${a*(1-u*.5)})`;X.beginPath();X.arc(x,lerp(y0,y1,u),11,0,7);X.fill()}}
function carne(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(0,64,120,16,0,0,7);X.fill();X.fillStyle='#f3ecdc';rr(86,-18,90,26,13);X.fill();X.beginPath();X.arc(178,-18,17,0,7);X.fill();X.beginPath();X.arc(178,8,17,0,7);X.fill();
 X.fillStyle='#b5523a';X.beginPath();X.ellipse(0,0,118,70,-.12,0,7);X.fill();X.fillStyle='#d9735a';X.beginPath();X.ellipse(-12,-10,84,44,-.12,0,7);X.fill();X.fillStyle='rgba(255,236,220,.6)';X.beginPath();X.ellipse(-30,-18,30,10,-.3,0,7);X.fill();X.restore()}
// ---------- retratos de frente: gato, tigre, guepardo ----------
function cara(x,y,s,tipo,t){const P={gato:{c:'#8d8f99',c2:'#e2e4ea',d:'#5d606b',ojo:'#9ccc65'},tigre:{c:'#e58a2e',c2:'#fff1dc',d:'#2a1a12',ojo:'#f2c94c'},guepardo:{c:'#e0b866',c2:'#fbf0d6',d:'#3a2a18',ojo:'#d9912e'}}[tipo],G=tipo==='gato',bl=((t*1.1)%3.7)<.12;
 X.save();X.translate(x,y);X.scale(s,s);X.lineCap='round';X.lineJoin='round';
 if(G)[-1,1].forEach(q=>{X.fillStyle=P.c;X.beginPath();X.moveTo(q*176,-70);X.lineTo(q*150,-250);X.lineTo(q*40,-150);X.closePath();X.fill();X.fillStyle='#f5a3b5';X.beginPath();X.moveTo(q*150,-96);X.lineTo(q*140,-204);X.lineTo(q*78,-146);X.closePath();X.fill()});
 else[-1,1].forEach(q=>{X.fillStyle=P.c;X.beginPath();X.arc(q*132,-140,56,0,7);X.fill();X.fillStyle=tipo==='tigre'?P.d:P.c2;X.beginPath();X.arc(q*132,-136,30,0,7);X.fill()});
 X.fillStyle=P.c;X.beginPath();X.ellipse(0,0,196,172,0,0,7);X.fill();{const g=X.createRadialGradient(-40,-70,20,0,0,210);g.addColorStop(0,'rgba(255,255,255,.14)');g.addColorStop(1,'rgba(0,0,0,.14)');X.fillStyle=g;X.beginPath();X.ellipse(0,0,196,172,0,0,7);X.fill()}
 X.fillStyle=P.c2;[-46,46].forEach(q=>{X.beginPath();X.ellipse(q,72,64,50,0,0,7);X.fill()});X.beginPath();X.ellipse(0,108,56,40,0,0,7);X.fill();
 X.strokeStyle=P.d;X.fillStyle=P.d;
 if(tipo==='tigre'){X.lineWidth=13;[[-28,-150,-22,-104],[0,-158,0,-108],[28,-150,22,-104]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(p[2],p[3]);X.stroke()});[-1,1].forEach(q=>[[188,-30,130,-18],[192,22,134,26],[178,74,128,66]].forEach(p=>{X.beginPath();X.moveTo(q*p[0],p[1]);X.lineTo(q*p[2],p[3]);X.stroke()}))}
 else if(tipo==='guepardo'){[[-60,-130],[-20,-142],[24,-140],[62,-128],[-110,-90],[112,-88],[-150,-20],[150,-18],[-140,50],[142,52],[0,-110]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],9,0,7);X.fill()});X.lineWidth=12;[-1,1].forEach(q=>{X.beginPath();X.moveTo(q*48,-8);X.quadraticCurveTo(q*52,50,q*82,112);X.stroke()})}
 else{X.lineWidth=9;[[-34,-150,-22,-112],[0,-156,0,-114],[34,-150,22,-112]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(p[2],p[3]);X.stroke()})}
 [-72,72].forEach(q=>{X.fillStyle=P.ojo;X.beginPath();X.ellipse(q,-34,31,bl?4:33,0,0,7);X.fill();if(!bl){X.fillStyle='#111';X.beginPath();X.ellipse(q,-34,G?9:15,G?28:15,0,0,7);X.fill();X.fillStyle='#fff';X.beginPath();X.arc(q+8,-46,6,0,7);X.fill()}});
 X.fillStyle=G?'#f48fb1':'#3a2a22';X.beginPath();X.moveTo(-22,42);X.lineTo(22,42);X.lineTo(0,66);X.closePath();X.fill();X.strokeStyle='#3a2a22';X.lineWidth=5;X.beginPath();X.moveTo(0,66);X.lineTo(0,86);X.quadraticCurveTo(-20,106,-40,92);X.moveTo(0,86);X.quadraticCurveTo(20,106,40,92);X.stroke();
 X.strokeStyle='rgba(255,255,255,.8)';X.lineWidth=3;[-1,1].forEach(q=>[-8,6,20].forEach(d=>{X.beginPath();X.moveTo(q*70,80+d*.5);X.lineTo(q*220,60+d*2.6);X.stroke()}));X.restore()}
function insignia(x,y,s,a){if(a<=0)return;X.save();X.globalAlpha=a;X.translate(x,y);X.scale(s*(.7+.3*back(a)),s*(.7+.3*back(a)));X.fillStyle='rgba(12,20,36,.88)';X.beginPath();X.arc(0,0,150,0,7);X.fill();X.strokeStyle='rgba(255,255,255,.3)';X.lineWidth=6;X.stroke();X.save();X.beginPath();X.arc(0,0,146,0,7);X.clip();sensor(0,-14,.52,{sep:.22,roto:1});X.restore();X.restore()}
// ---------- cocina cálida ----------
function cocina(L,cm,t,o){o=o||{};interior(L,{p0:'#74462c',p1:'#b67848',tex:'baldosa',ta:.16,yp:1420});const px=par(cm,.4);
 X.fillStyle='#4a2f1e';rr(L+560+px,620,560,300,14);X.fill();X.fillStyle='#5d3b26';[0,1].forEach(i=>{rr(L+580+i*270+px,640,250,260,10);X.fill()});X.fillStyle='#d9b24a';[0,1].forEach(i=>{X.beginPath();X.arc(L+800+i*30+px,770,9,0,7);X.fill()});
 luz(L+200+px,700,640,'255,200,130',.32);meson(L,o.ym||1420,{tex:'madera',col:'#7a5636',ta:.9})}

// ---------- 01 · gancho: macro del glaseado; el foco pasa al gato, que lame sin interés ----------
function p01(L,t){const xe=T.x_eat,xm=T.x_missing1,xc=T.x_careful,f=T.c02,foco=eio(seg(t,xe-1.1,xe-.3)),lam=t<xm?Math.max(0,Math.sin(t*6)):0,frio=eio(seg(t,xm-.2,xm+.6));
 const kf=[[0,390,1150,2.1],[xe-1.2,400,1140,1.9],[xe-.2,560,1130,1.16],[xm,580,1120,1.2],[f,640,1080,1.34]];
 plano(L,t,kf,cm=>{cocina(L,cm,t,{});
  gato(L+740,1420,2.4,t,{pose:'sentado',dir:-1,inclina:lerp(.22,-.06,frio),cola:lerp(2.5,1,frio),lento:frio>.5});if(lam>0)lengua(L+576,1062,2.2,Math.PI-.15,lam)});
 desenfoca(9*(1-foco));
 plano(L,t,kf,cm=>{borroso(5*foco,()=>pastel(L+360,1420,1.9,{}))});
 tinte(L,'50,96,180',.12*frio);arriba(L,.62)}

// ---------- 02 · años 70: lámpara, cuaderno y dos recipientes de vidrio grueso ----------
function vaso70(x,yb,s,niv){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,4,90,12,0,0,7);X.fill();X.fillStyle='rgba(150,200,215,.5)';rr(-64,-200*niv,128,200*niv,10);X.fill();
 rr(-76,-230,152,230,14);X.fillStyle='rgba(220,236,238,.16)';X.fill();X.strokeStyle='rgba(235,245,246,.7)';X.lineWidth=10;X.stroke();X.fillStyle='rgba(255,255,255,.35)';rr(-58,-204,12,160,6);X.fill();X.restore()}
function lampara70(x,yb,s){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='#2a2a26';X.beginPath();X.ellipse(0,-6,90,16,0,0,7);X.fill();X.strokeStyle='#3a3a34';X.lineWidth=14;X.lineCap='round';X.beginPath();X.moveTo(0,-10);X.lineTo(-40,-300);X.lineTo(-190,-420);X.stroke();
 X.fillStyle='#4f7a5a';X.beginPath();X.moveTo(-150,-470);X.lineTo(-270,-330);X.lineTo(-330,-400);X.lineTo(-220,-500);X.closePath();X.fill();X.restore();haz(x-290*s,yb-360*s,x-470*s,yb-20*s,40*s,330*s,'255,214,140',.3)}
function p02(L,t){const c=T.c02,f=T.c03;
 plano(L,t,[[c,430,1180,1.22],[f,610,1165,1.18]],cm=>{
  interior(L,{p0:'#4a4433',p1:'#7a6c48',tex:'tela',ta:.24,yp:1300});const px=par(cm,.35);[0,1,2].forEach(i=>{X.fillStyle='#3a3327';rr(L+80+i*330+px,640,270,360,8);X.fill();X.fillStyle='rgba(255,236,190,.07)';rr(L+96+i*330+px,656,238,328,6);X.fill()});
  meson(L,1300,{tex:'madera',col:'#5d4226',ta:.95,v:7});vaso70(L+600,1330,1.25,.6);vaso70(L+840,1330,1.25,.6);lampara70(L+1180,1320,1.25);
  hojaP(L+450,1560,560,420,-.06,()=>{X.fillStyle='rgba(120,90,40,.10)';X.fillRect(-280,-210,560,420);X.strokeStyle='rgba(120,60,50,.4)';X.lineWidth=3;X.beginPath();X.moveTo(-210,-210);X.lineTo(-210,210);X.stroke();
   const a=eio(seg(t,c+.3,c+.7));X.globalAlpha=a;txt('1970s',-40,-126,96,'#3a2f22',{w:800});X.globalAlpha=1;renglones(-180,-40,420,5,11,3,'rgba(58,47,34,.3)')},'#e6d8b4')});
 tinte(L,'170,120,50',.1);arriba(L,.6)}

// ---------- 03 · agua con azúcar y agua sola: la cámara baja de cenital a nivel de los cuencos ----------
function sombraAnimal(x,yb,s,tipo,dir){X.save();X.translate(x,yb);X.scale(s*dir,s);X.fillStyle='rgba(16,24,30,.55)';
 if(tipo===0){X.beginPath();X.ellipse(0,-70,120,60,0,0,7);X.fill();X.beginPath();X.arc(120,-120,52,0,7);X.fill();X.beginPath();X.ellipse(96,-176,20,40,-.3,0,7);X.fill();rr(-90,-40,34,44,12);X.fill();rr(60,-40,34,44,12);X.fill();X.beginPath();X.moveTo(-116,-90);X.quadraticCurveTo(-190,-140,-170,-190);X.lineTo(-150,-186);X.quadraticCurveTo(-160,-130,-104,-70);X.fill()}
 else if(tipo===1){X.beginPath();X.ellipse(0,-56,90,56,0,0,7);X.fill();X.beginPath();X.arc(84,-96,40,0,7);X.fill();[60,92].forEach(q=>{X.beginPath();X.ellipse(q,-176,14,58,q>70?.2:-.1,0,7);X.fill()});X.beginPath();X.arc(-88,-50,22,0,7);X.fill()}
 else{X.beginPath();X.ellipse(0,-34,62,34,0,0,7);X.fill();X.beginPath();X.arc(58,-48,26,0,7);X.fill();X.beginPath();X.arc(50,-80,18,0,7);X.fill();X.strokeStyle='rgba(16,24,30,.55)';X.lineWidth=7;X.lineCap='round';X.beginPath();X.moveTo(-58,-30);X.quadraticCurveTo(-130,-20,-150,-70);X.stroke()}X.restore()}
function p03(L,t){const c=T.c03,xs=T.x_sugar,xp=T.x_plain,xk=T.x_pick,f=T.c04,k=eio(seg(t,c+.5,xp+.5)),yh=lerp(-300,1180,k),by=lerp(1060,1420,k),ry=lerp(1,.2,k);
 plano(L,t,[[c,540,1060,1.12],[xp+.5,540,1130,1.06],[f,500,1140,1.12]],cm=>{
  X.fillStyle='#6a4a30';X.fillRect(L-900,-900,2900,3800);tex('madera',L-500,-300,2100,2500,{a:.95,s:1.8,v:5});
  if(yh>-250){X.fillStyle=gl(0,yh-1400,0,yh,[[0,'#3d5560'],[1,'#6b8794']]);X.fillRect(L-900,yh-2000,2900,2000);X.fillStyle='rgba(0,0,0,.3)';X.fillRect(L-900,yh,2900,14)}
  if(k>.6){const q=eio(seg(t,xk-.5,xk+.5));X.save();X.beginPath();X.rect(L-900,yh-1500,2900,1500);X.clip();sombraAnimal(L+lerp(1300,560,q),yh+6,1.5,0,-1);sombraAnimal(L+lerp(1500,330,eio(seg(t,xk-.3,xk+.7))),yh+6,1.3,1,-1);sombraAnimal(L+lerp(1700,160,eio(seg(t,xk-.1,xk+.9))),yh+6,1.3,2,-1);X.restore()}
  [[290,'#bfe3f2',1],[790,'#9fd0e8',0]].forEach(([x,ag,dul])=>{X.save();X.translate(L+x,by);X.fillStyle='rgba(0,0,0,.22)';X.beginPath();X.ellipse(0,150*k+8,200,200*ry*.5+14,0,0,7);X.fill();
   if(k>.02){X.fillStyle=gl(-190,0,190,0,[[0,'#cfd6dc'],[.5,'#f3f6f8'],[1,'#b9c2c9']]);X.beginPath();X.moveTo(-190,0);X.lineTo(190,0);X.quadraticCurveTo(178,140*k,110,150*k);X.lineTo(-110,150*k);X.quadraticCurveTo(-178,140*k,-190,0);X.closePath();X.fill()}
   X.fillStyle='#e8eef2';X.beginPath();X.ellipse(0,0,190,190*ry,0,0,7);X.fill();X.fillStyle=ag;X.beginPath();X.ellipse(0,0,166,166*ry,0,0,7);X.fill();X.fillStyle='rgba(255,255,255,.45)';X.beginPath();X.ellipse(-50,-40*ry,60,22*ry,0,0,7);X.fill();
   if(dul){const g=golpe(t,xk,.9);if(g>0){X.strokeStyle=`rgba(255,214,110,${g})`;X.lineWidth=10;X.beginPath();X.ellipse(0,0,206,206*ry+6,0,0,7);X.stroke()}}X.restore()});
  cubos(L+60,by+lerp(250,150,k),1.5,eio(seg(t,xs-.15,xs+.25)))});
 arriba(L,.6)}

// ---------- 04 · al gato le da lo mismo: prueba los dos ----------
function p04(L,t){const c=T.c04,xb=T.x_both,f=T.c05,u=eio(seg(t,xb-.75,xb-.05)),gx=lerp(40,590,u),bebe=(u<.02||u>.98)?1:0,l=bebe*Math.max(0,Math.sin(t*9));
 plano(L,t,[[c,380,1250,1.2],[xb,660,1250,1.2],[f,700,1250,1.24]],cm=>{
  interior(L,{p0:'#3d5560',p1:'#6b8794',tex:'baldosa',ta:.14,yp:1330,piso:['#8d969b','#7e878c'],paso:170});luz(L+540,600,900,'235,246,255',.2,640);
  cuenco(L+350,1560,1.15,{agua:'#bfe3f2'});cuenco(L+900,1560,1.15,{});cubos(L+560,1564,1,1);
  gato(L+gx,1560,2.3,t,{pose:'parado',camina:!bebe,inclina:bebe?.42:.1,cola:1.5});if(l>0)lengua(L+gx+133*2.3+26,1560-120*2.3+86,2,1.25,l)});
 arriba(L,.6)}

// ---------- 05 · por décadas nadie supo explicarlo: pasan hojas de investigación; una se vuelve hélice ----------
function p05(L,t){const c=T.c05,f=T.c06,m=eio(seg(t,f-1.0,f-.25));
 plano(L,t,[[c,540,1100,1],[f,540,1080,1.16]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#151c2a'],[1,'#27364a']]);X.fillRect(L-900,-900,2900,3800);luz(L+540,900,800,'120,160,220',.18);
  for(let i=0;i<7;i++){const u=((t-c)*.42+i/7)%1,s=lerp(.25,1.5,u*u),x=L+540+(rnd(i+2)-.5)*900*(.4+u),y=lerp(820,1250,u)+(rnd(i+11)-.5)*300;X.save();X.globalAlpha=Math.sin(u*Math.PI)*.9;hojaP(x,y,300*s,390*s,(rnd(i)-.5)*.5+u*.3,()=>{renglones(-110*s,-150*s,220*s,8,9*s,i)},'#e9e2cf');X.restore()}
  X.fillStyle='#1a2330';X.fillRect(L-900,1640,2900,900);cuenco(L+330,1700,1,{agua:'#bfe3f2'});cuenco(L+750,1700,1,{});
  if(m<1){X.save();X.globalAlpha=1-m;hojaP(L+540,1080,330*(1-.5*m),430,m*1.2,()=>renglones(-120,-160,240,9,10,5),'#f1ead8');X.restore()}
  helice(L+540,860,1300,70,t,{a:m,vueltas:2})});
 arriba(L,.58)}

// ---------- 06 · G2: nace sin algo. Silueta del gato; en la boca, un sensor al que le falta una parte ----------
function perfil(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';X.fillStyle='#0d1830';X.strokeStyle='rgba(120,170,255,.55)';X.lineWidth=7;
 X.beginPath();X.moveTo(-300,420);X.lineTo(-270,-40);X.lineTo(-214,-250);X.lineTo(-160,-340);X.lineTo(-74,-204);X.quadraticCurveTo(40,-200,130,-150);X.lineTo(254,-44);X.lineTo(278,-8);X.lineTo(236,34);X.lineTo(110,58);X.lineTo(214,128);X.lineTo(190,178);X.quadraticCurveTo(110,236,30,236);X.lineTo(-10,420);X.closePath();X.fill();X.stroke();
 X.fillStyle='#7a2b45';X.beginPath();X.moveTo(232,38);X.lineTo(112,60);X.lineTo(212,126);X.closePath();X.fill();X.fillStyle='#ff7fa3';X.beginPath();X.ellipse(170,104,56,16,.55,0,7);X.fill();
 X.fillStyle='rgba(160,220,140,.9)';X.beginPath();X.ellipse(112,-72,30,20,-.2,0,7);X.fill();X.fillStyle='#0a0f1c';X.beginPath();X.ellipse(118,-72,8,18,0,0,7);X.fill();X.restore()}
function p06(L,t){const c=T.c06,xb=T.x_born6,xn=T.x_nobody,f=T.c07,ap=eio(seg(t,xb-.5,xb)),g=golpe(t,xb,.6),mac=eio(seg(t,xn-.25,xn+.15));
 plano(L,t,[[c,470,1120,1],[xb,600,1130,1.3],[xn-.25,640,1140,1.44],[xn+.15,725,1196,2.6],[f,725,1196,2.8]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#081026'],[1,'#14285a']]);X.fillRect(L-900,-900,2900,3800);luz(L+760,1160,700,RA,.1+.2*ap+.15*g);
  perfil(L+470,1090,1.25);
  if(ap>0){X.save();X.globalAlpha=ap;sensor(L+725,1196,.2+.02*g,{sep:.22,roto:1,on:0});X.restore();luz(L+725,1196,90+60*g,RA,.5*ap)}});
 arriba(L,.6)}

// ---------- 07 · 2005: dentro del ADN del gato; un tramo se ilumina ----------
function p07(L,t){const c=T.c07,xi=T.x_inside,xd=T.x_dna,f=T.c08,o=ruta(t,[[c,470,1080,1.04,-.05],[f,610,1060,1.2,.05]]),lu=eio(seg(t,xi-.2,xi+.5));
 cam(L,o[0],o[1],o[2],540,1000,()=>{X.fillStyle=gl(0,0,0,1920,[[0,'#0c2a33'],[1,'#134652']]);X.fillRect(L-900,-900,2900,3800);
  const px=(o[0]-540)*.5;[[90,1500,1.3],[900,1560,1.5],[1010,1420,1]].forEach(p=>{X.fillStyle='rgba(180,230,235,.10)';rr(L+p[0]-60*p[2]+px,p[1]-320*p[2],120*p[2],320*p[2],16);X.fill()});X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L-900,1560,2900,900);
  luz(L+540,1050,760,'90,210,220',.22);placa2(L+215+px,820,'2005',eio(seg(t,c+.05,c+.4)));
  helice(L+560,560,1560,110,t,{vueltas:3.2,vel:1.5,luz:lu>0?[.4,.4+.2*lu]:null});if(lu>0)luz(L+560,1060,300,RA,.3*lu)},o[3]);
 arriba(L,.6)}
function placa2(x,y,texto,a){if(a<=0)return;X.save();X.globalAlpha=a;tarj(x,y,240,100,14,'#e9e4d6',{sa:.25});txt(texto,x,y+4,64,'#2a2f38',{w:800});X.restore()}

// ---------- fondo de macro (dentro de la lengua) ----------
function macro(L,t,o){o=o||{};X.fillStyle=gl(0,0,0,1920,[[0,o.c0||'#1b1440'],[1,o.c1||'#3a2260']]);X.fillRect(L-1400,-900,3900,3800);for(let i=0;i<9;i++){const x=L-200+rnd(i+4)*1900,y=520+rnd(i+13)*900,r=40+rnd(i+22)*70;luz(x+Math.sin(t*.5+i)*20,y,r,o.bok||'200,160,255',.10)}membrana(L,o.ym||1420,t,o.ma);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L-1400,(o.ym||1420)+110,3900,1200)}
// ---------- 08 · el sensor de lo dulce tiene dos piezas que encajan ----------
function p08(L,t){const c=T.c08,x2=T.x_two,f=T.c09,u=eio(seg(t,c+.3,x2)),on=eio(seg(t,x2,x2+.35)),o=ruta(t,[[c,500,1080,1.08,-.035],[f,580,1070,1.2,.035]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{macro(L,t,{});sensor(L+540,1100,1.25,{sep:1.6*(1-u),on});
  cubos(L+516,lerp(560,880,eio(seg(t,x2-.2,x2+.5))),1,eio(seg(t,x2-.3,x2)));pulso(L+540-80,1200,1500,t,x2+.2,RA,on);pulso(L+540+80,1200,1500,t,x2+.35,RB,on)},o[3]);
 arriba(L,.6)}
// ---------- 09 · en los gatos una pieza está rota: falta un trozo del gen que la construye ----------
function gen(L,x0,y,w,t,q){const n=14,a=5,b=8;for(let i=0;i<n;i++){const x=L+x0+i*w/n,fal=i>=a&&i<b;if(fal)continue;X.fillStyle=i%2?'rgba(120,200,255,.85)':'rgba(90,150,230,.85)';rr(x+3,y,w/n-6,54,12);X.fill()}
 const xa=L+x0+a*w/n,xb=L+x0+b*w/n;X.setLineDash([12,12]);X.strokeStyle=`rgba(255,255,255,${.8*q})`;X.lineWidth=5;rr(xa+3,y-4,xb-xa-6,62,12);X.stroke();X.setLineDash([]);return [(xa+xb)/2,y]}
function p09(L,t){const c=T.c09,xb=T.x_broken,xk=T.x_chunk,xm=T.x_gone,f=T.c10,ro=eio(seg(t,xb-.5,xb)),tr=.5+.5*Math.sin(t*3.2),q=eio(seg(t,xk-.3,xk+.3)),bar=(t-xk)*.5%1;
 plano(L,t,[[c,560,1080,1.2],[xb+.3,590,1090,1.3],[xk-.2,590,1090,1.3],[xk+.7,540,1330,1.1],[f,540,1340,1.14]],cm=>{
  macro(L,t,{c0:'#10203c',c1:'#1c3a5c',bok:'150,200,255'});sensor(L+540,1100,1.25,{sep:.16+.5*tr*ro,roto:ro});
  if(q>0){X.globalAlpha=q;X.fillStyle='rgba(8,16,30,.6)';rr(L+70,1620,940,210,30);X.fill();const p=gen(L,110,1700,860,t,q);X.strokeStyle='rgba(255,255,255,.6)';X.lineWidth=4;X.setLineDash([8,10]);X.beginPath();X.moveTo(p[0],p[1]-6);X.quadraticCurveTo(p[0]+120,1380,L+540+1.25*(62+150*(.16+.5*tr))+70,1040);X.stroke();X.setLineDash([]);X.globalAlpha=1;
   if(t>xk){X.save();X.beginPath();X.rect(L+70,1620,940,210);X.clip();haz(L+70+940*bar,1600,L+70+940*bar,1850,60,60,'200,230,255',.3);X.restore()}}});
 tinte(L,'40,90,170',.08);arriba(L,.6)}
// ---------- 10 · no detectan lo dulce; el resto, como el de la carne, sigue funcionando ----------
function p10(L,t){const c=T.c10,xs=T.x_sweet,xm=T.x_meat,f=T.c11,D=1150,reb=eio(seg(t,xs-.3,xs+.3)),on=eio(seg(t,xm-.1,xm+.3));
 plano(L,t,[[c,540,1080,1.12],[xm-.75,560,1080,1.14],[xm-.1,D+540,1080,1.12],[f,D+570,1070,1.18]],cm=>{
  macro(L,t,{c0:'#1b1440',c1:'#3a2260'});
  sensor(L+540,1100,1.25,{sep:.3,roto:1,apag:1});X.save();X.translate(L+500+reb*150,lerp(520,800,Math.min(1,reb*2))-Math.sin(Math.max(0,reb-.5)*2*Math.PI)*90);X.rotate(reb*1.4);cubos(0,0,1,1);X.restore();
  if(reb>.5){X.strokeStyle=`rgba(255,255,255,${.7*(1-eio(seg(t,xs+.3,xs+1)))})`;X.lineWidth=12;X.lineCap='round';X.beginPath();X.moveTo(L+470,930);X.lineTo(L+610,930);X.stroke()}
  sensor(L+D+540,1100,1.25,{sep:0,ca:AMB,cb:'255,150,90',on:on*.9});carne(L+D+520,lerp(560,800,eio(seg(t,xm-.5,xm))),1.1);pulso(L+D+460,1200,1500,t,xm+.1,AMB,on);pulso(L+D+620,1200,1500,t,xm+.25,'255,150,90',on)});
 arriba(L,.6)}

// ---------- 11 · no solo los gatos de casa: tigres y guepardos tienen el mismo gen roto ----------
function p11(L,t){const c=T.c11,xt=T.x_tigers,xc=T.x_cheetahs,f=T.c12,e=t<xt-.1?0:t<xc+.35?1:2,k=[c,xt-.1,xc+.35][e],z=1.04+.07*seg(t,k,k+2.2);
 cam(L,540,1060,z,540,1000,()=>{
  if(e===0){X.fillStyle=gl(0,0,0,1920,[[0,'#3a2f52'],[1,'#6a5a86']]);X.fillRect(L-900,-900,2900,3800);tex('tela',L-300,300,1700,1700,{a:.16,v:2});luz(L+540,1000,760,'220,200,255',.2)}
  else if(e===1){X.fillStyle=gl(0,0,0,1920,[[0,'#0f2a22'],[1,'#27563c']]);X.fillRect(L-900,-900,2900,3800);for(let i=0;i<8;i++){X.fillStyle='rgba(20,60,40,.8)';X.beginPath();X.ellipse(L-100+i*190,1800+rnd(i)*80,150,420+rnd(i+4)*200,(rnd(i+8)-.5)*.5,0,7);X.fill()}luz(L+540,1000,760,'200,255,200',.16)}
  else{X.fillStyle=gl(0,0,0,1920,[[0,'#e6a04c'],[1,'#f3d28e']]);X.fillRect(L-900,-900,2900,3800);X.fillStyle='#b98a3a';X.fillRect(L-900,1560,2900,900);X.fillStyle='#6b4a2a';X.fillRect(L+150,1040,18,520);X.beginPath();X.ellipse(L+160,1030,210,50,0,0,7);X.fill();luz(L+540,1000,760,'255,240,200',.2)}
  cara(L+540,1040,e===0?1.45:1.6,['gato','tigre','guepardo'][e],t);insignia(L+830,1500,.8,eio(seg(t,k+.25,k+.6)))});
 arriba(L,e===2?.72:.6)}

// ---------- 12 · si lame tu postre, no está probando lo dulce ----------
function p12(L,t){const c=T.c12,xd=T.x_dessert,xs=T.x_sweetpart,f=T.c13,foco=eio(seg(t,xd-.1,xd+.6)),lam=Math.max(0,Math.sin(t*6.5)),ap=eio(seg(t,xs-.35,xs+.25));
 const kf=[[c,570,1100,1.36],[xd,545,1110,1.3],[f,525,1120,1.36]];
 plano(L,t,kf,cm=>{cocina(L,cm,t,{})});desenfoca(6);
 plano(L,t,kf,cm=>{gato(L+760,1420,2.4,t,{pose:'sentado',dir:-1,inclina:.22,cola:2});lengua(L+596,1062,2.2,Math.PI-.15,lam)});
 desenfoca(5*foco);
 plano(L,t,kf,cm=>{borroso(5*(1-foco),()=>pastel(L+380,1420,1.9,{}));
  for(let i=0;i<5;i++){const u=((t-c)*.5+i/5)%1,x=lerp(L+470,L+590,u),y=1090-Math.sin(u*Math.PI)*70+i*8,gr=Math.max(ap,u>.7?1:0);X.fillStyle=gr>.5?`rgba(170,170,180,${.8*(1-u)})`:`rgba(255,220,120,${.95*(1-u*.6)})`;X.beginPath();for(let j=0;j<8;j++){const a=j*Math.PI/4,r=j%2?5:13;X.lineTo(x+Math.cos(a)*r,y+Math.sin(a)*r)}X.closePath();X.fill()}});
 arriba(L,.62)}

// ---------- 13 · CTA: el gato mira el plato y se acerca al postre ----------
function p13(L,t){const c=T.c13,ac=eio(seg(t,c+1.3,c+2.3));
 plano(L,t,[[c,470,1160,1.14],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{cocina(L,cm,t,{ym:1480});
  pastel(L+250,1480,.95,{});gato(L+lerp(620,520,ac),1480,1.55,t,{pose:'sentado',dir:-1,inclina:.1+.14*ac,cola:2.5,lento:ac<.3})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_scats21_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SCATS21 · FIN =====
</script>
