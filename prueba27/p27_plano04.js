
// ======================= PLANO 04 · primera persona: explorador de texturas, mano y mouse =======================
// ---------- texturas procedurales (miniaturas) con caché ----------
const TEX27=new Map();
function tex27(i,w,h,tipo){const k=i+'_'+w+'_'+h;if(TEX27.has(k))return TEX27.get(k);const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');const r=j=>rnd(i*7.13+j*1.31);
 const T=tipo||['madera','piedra','ladrillo','tela','metal','pasto','arena','oxido','baldosa','cuero','marmol','cuerda','corteza','concreto'][i%14];
 const fondo=(c1,c2)=>{const gg=g.createLinearGradient(0,0,w,h);gg.addColorStop(0,c1);gg.addColorStop(1,c2);g.fillStyle=gg;g.fillRect(0,0,w,h)};
 const motas=(n,col,a1,a2,s1,s2)=>{for(let j=0;j<n;j++){g.fillStyle=`rgba(${col},${a1+(a2-a1)*r(j+50)})`;const s=s1+(s2-s1)*r(j+90);g.fillRect(r(j)*w,r(j+300)*h,s,s)}};
 if(T==='casco'){ // textura del casco del barco: tablas grises horizontales, desgaste, remaches. Sin nombre.
  fondo('#6f7883','#59626d');const ph=w/6;for(let y=0;y<h+ph;y+=ph){const sh=(Math.floor(y/ph)%2)*.06;g.fillStyle=`rgba(255,255,255,${.05+sh})`;g.fillRect(0,y,w,ph*.45);g.fillStyle='rgba(20,24,30,.55)';g.fillRect(0,y+ph-ph*.06,w,ph*.06);
   for(let x=(Math.floor(y/ph)%2)*ph*1.6;x<w;x+=ph*3.2){g.fillStyle='rgba(20,24,30,.45)';g.fillRect(x,y,ph*.05,ph);for(let k=0;k<2;k++){g.fillStyle='rgba(30,34,40,.6)';g.beginPath();g.arc(x+ph*.22,y+ph*(.3+k*.4),ph*.055,0,7);g.fill()}}}
  motas(Math.round(w*h/900),'215,220,225',.04,.18,1,w/70);motas(Math.round(w*h/1800),'40,44,52',.06,.22,1,w/90);
  g.fillStyle='rgba(120,90,60,.10)';for(let j=0;j<6;j++){g.beginPath();g.ellipse(r(j+700)*w,r(j+710)*h,w*.12,h*.03,0,0,7);g.fill()}}
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
 TEX27.set(k,c);return c}

// ---------- set: escritorio en primera persona (monitor que llena el ancho, habitación oscura detrás) ----------
NUEVOS.p27_escritorioV={osc:.1,luces(){return []},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),M=o.monitor||{y0:470,y1:1290};
  let g=X.createLinearGradient(0,0,0,M.y0);g.addColorStop(0,'#07080c');g.addColorStop(1,'#12141c');X.fillStyle=g;X.fillRect(L-300,-300,1680,M.y0+300);
  X.save();X.filter='blur(14px)';X.fillStyle='rgba(70,90,130,.22)';X.fillRect(L+760,40,260,300);X.fillStyle='rgba(20,22,30,.9)';X.fillRect(L+884,40,12,300);X.fillRect(L+760,186,260,10);X.restore();
  // escritorio (madera oscura en perspectiva hacia el monitor)
  g=X.createLinearGradient(0,M.y1-40,0,1980);g.addColorStop(0,'#2a1d14');g.addColorStop(1,'#120c08');X.fillStyle=g;X.fillRect(L-300,M.y1-40,1680,1000);
  X.strokeStyle='rgba(0,0,0,.25)';X.lineWidth=2;for(let i=-6;i<=6;i++){X.beginPath();X.moveTo(L+540+i*60,M.y1-30);X.lineTo(L+540+i*260,1980);X.stroke()}
  // pie del monitor
  X.fillStyle=gl(L+470,0,L+610,0,[[0,'#1a1b20'],[.5,'#2c2e35'],[1,'#17181c']]);X.beginPath();X.moveTo(L+490,M.y1);X.lineTo(L+590,M.y1);X.lineTo(L+600,M.y1+70);X.lineTo(L+480,M.y1+70);X.closePath();X.fill();
  X.fillStyle='#1c1d22';X.beginPath();X.ellipse(L+540,M.y1+78,170,22,0,0,7);X.fill();X.fillStyle='rgba(255,255,255,.08)';X.beginPath();X.ellipse(L+540,M.y1+72,160,12,0,Math.PI,0);X.fill();
  // marco del monitor (más ancho que el cuadro: estamos cerca)
  X.fillStyle='#0e0f13';rr(L-80,M.y0,1240,M.y1-M.y0,18);X.fill();X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-80,M.y0+2,1240,3);
  X.fillStyle='#050608';X.fillRect(L-56,M.y0+26,1192,M.y1-M.y0-66);
  X.fillStyle='rgba(120,200,255,.8)';X.beginPath();X.arc(L+980,M.y1-20,4,0,7);X.fill();
  // teclado en perspectiva
  const K=o.teclado||{x0:30,x1:560,y0:1395,y1:1545};X.fillStyle='#16171c';X.beginPath();X.moveTo(L+K.x0+40,K.y0);X.lineTo(L+K.x1-10,K.y0);X.lineTo(L+K.x1+20,K.y1);X.lineTo(L+K.x0,K.y1);X.closePath();X.fill();
  for(let rI=0;rI<5;rI++){const f=rI/5,y=lerp(K.y0+8,K.y1-8,f),h=(K.y1-K.y0)/5-8,xa=lerp(K.x0+46,K.x0+8,f),xb=lerp(K.x1-16,K.x1+12,f),n=12;for(let c=0;c<n;c++){const x=lerp(xa,xb,c/n),w=(xb-xa)/n-5;X.fillStyle='#24262d';rr(L+x,y,w,h,4);X.fill();X.fillStyle='rgba(255,255,255,.06)';X.fillRect(L+x+2,y+1,w-4,2)}}
  // alfombrilla del mouse
  X.fillStyle='#101116';X.beginPath();X.moveTo(L+600,1440);X.lineTo(L+930,1440);X.lineTo(L+1010,1800);X.lineTo(L+540,1800);X.closePath();X.fill();X.strokeStyle='rgba(255,255,255,.05)';X.lineWidth=2;X.stroke();
 }};

// ---------- utilería: explorador de archivos con grilla de texturas (pantalla del monitor) ----------
function scroll27(t,o){const a=window.__A||0,t0=tk(o.scroll[0],a),t1=tk(o.scroll[1],a),q=seg(t,t0,t1);return o.dist*(1-Math.pow(1-q,3))}
UTILERIA.p27_grilla=(x,y,s,t,o)=>{o=o||{};const L=x,S=o.pantalla,a=window.__A||0;X.save();X.beginPath();X.rect(L+S.x0,S.y0,S.x1-S.x0,S.y1-S.y0);X.clip();
 X.fillStyle='#15171d';X.fillRect(L+S.x0,S.y0,S.x1-S.x0,S.y1-S.y0);
 // barra superior y ruta genérica
 X.fillStyle='#1f222b';X.fillRect(L+S.x0,S.y0,S.x1-S.x0,70);X.fillStyle='#2a2e39';X.fillRect(L+S.x0,S.y0+70,S.x1-S.x0,2);
 X.font='600 30px P';X.textAlign='left';X.textBaseline='middle';X.fillStyle='#c9cfdb';X.fillText('files  ›  world  ›  textures',L+40,S.y0+36);X.fillStyle='#7d8596';X.font='500 26px P';X.textAlign='right';X.fillText('2,214 items',L+1040,S.y0+36);
 // barra lateral
 X.fillStyle='#1a1c23';X.fillRect(L+S.x0,S.y0+72,190+(-S.x0),S.y1-S.y0);for(let i=0;i<7;i++){X.fillStyle=i===3?'#3b4252':'#262a33';rr(L+24,S.y0+110+i*82,140,52,8);X.fill()}
 // grilla
 const sc=scroll27(t,o),v=(scroll27(t+1/60,o)-scroll27(t-1/60,o))*30,C=o.cols,top=o.y0,RH=o.fila,TW=o.tw,TH=o.th,k=o.clave,hl=seg(t,tk(o.resalta,a),tk(o.resalta,a)+.25),hov=seg(t,tk(o.cursor[0],a),tk(o.cursor[1],a));
 const clicP=(o.clics||[]).reduce((m,c)=>{const d=t-tk(c,a);return d>=0&&d<.12?Math.max(m,Math.sin(d/.12*Math.PI)):m},0);
 X.save();X.beginPath();X.rect(L+200,S.y0+74,S.x1-200,S.y1-S.y0-74);X.clip();
 const pinta=(dy,al)=>{X.globalAlpha=al;for(let r=0;r<40;r++){const cy=top+r*RH-sc+dy;if(cy<S.y0-RH||cy>S.y1+RH)continue;C.forEach((cx,ci)=>{const i=r*C.length+ci,esK=i===k;let sx=1;if(esK){sx=1+.05*back(hl)-.04*clicP}
    X.save();X.translate(L+cx,cy);X.scale(sx,sx);
    if(esK&&hov>0){X.fillStyle=`rgba(255,255,255,${.07*hov})`;rr(-TW/2-14,-TH/2-14,TW+28,TH+70,12);X.fill()}
    X.drawImage(tex27(i,TW,TH,esK?'casco':null),-TW/2,-TH/2);X.strokeStyle='rgba(0,0,0,.5)';X.lineWidth=2;X.strokeRect(-TW/2,-TH/2,TW,TH);
    if(esK&&hl>0){X.save();X.shadowColor='rgba(255,196,60,.9)';X.shadowBlur=26*hl;X.strokeStyle=`rgba(255,200,70,${hl})`;X.lineWidth=6;X.strokeRect(-TW/2-6,-TH/2-6,TW+12,TH+12);X.restore()}
    X.font=(esK&&hl>0?'700 ':'500 ')+'30px "DejaVu Sans Mono",monospace';X.textAlign='center';X.textBaseline='middle';X.fillStyle=esK&&hl>0?`rgb(${lerp(170,255,hl)},${lerp(178,214,hl)},${lerp(194,120,hl)})`:'#aab2c2';X.fillText('tex_0'+(o.num0+i),0,TH/2+30);X.restore()})}};
 if(Math.abs(v)>900){pinta(0,.45);pinta(-v*.012,.3);pinta(-v*.024,.25)}else pinta(0,1);X.globalAlpha=1;X.restore();
 // barra de desplazamiento
 const tot=o.dist+900,pos=sc/tot;X.fillStyle='#22252e';X.fillRect(L+1050,S.y0+80,12,S.y1-S.y0-90);X.fillStyle='#596075';rr(L+1048,S.y0+80+pos*(S.y1-S.y0-260),16,160,8);X.fill();
 // cursor (flecha): quieto durante el scroll; en "found" viaja a la miniatura clave
 const cp=eio(hov),cxp=lerp(o.cur0[0],o.cur1[0],cp),cyp=lerp(o.cur0[1],o.cur1[1],cp)+Math.sin(cp*Math.PI)*-30;
 X.save();X.translate(L+cxp,cyp);X.scale(1.5,1.5);X.fillStyle='#fff';X.strokeStyle='#111';X.lineWidth=2;X.beginPath();X.moveTo(0,0);X.lineTo(0,34);X.lineTo(9,26);X.lineTo(16,41);X.lineTo(22,38);X.lineTo(15,24);X.lineTo(26,24);X.closePath();X.fill();X.stroke();X.restore();
 // brillo de vidrio
 const gv=X.createLinearGradient(L,S.y0,L+700,S.y1);gv.addColorStop(0,'rgba(255,255,255,.05)');gv.addColorStop(.4,'rgba(255,255,255,0)');X.fillStyle=gv;X.fillRect(L+S.x0,S.y0,S.x1-S.x0,S.y1-S.y0);
 X.restore()};

// ---------- utilería: mouse y mano en primera persona (mano derecha desde abajo a la derecha, manga de polerón) ----------
UTILERIA.p27_manoPOV=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,LIN='rgba(30,22,16,.85)',p0='#efc09a',p1='#d9a079',p2='#b47952';
 const g0=o.grilla,hov=eio(seg(t,tk(g0.cursor[0],a),tk(g0.cursor[1],a))),mx=x+(o.mueve||[0,0])[0]*hov,my=y+(o.mueve||[0,0])[1]*hov;
 const sc=t<tk(g0.scroll[1],a)?(t-tk(g0.scroll[0],a)):0,rueda=sc>0?Math.sin(sc*26)*5*(1-seg(t,tk(g0.scroll[1],a)-.6,tk(g0.scroll[1],a))):0;
 const clic=(g0.clics||[]).reduce((m,c)=>{const d=t-tk(c,a);return d>=0&&d<.12?Math.max(m,Math.sin(d/.12*Math.PI)):m},0);
 X.save();X.translate(mx,my);X.scale(s,s);X.lineJoin='round';X.lineCap='round';
 // sombra del mouse y la mano sobre la alfombrilla
 X.save();X.filter='blur(14px)';X.fillStyle='rgba(0,0,0,.55)';X.beginPath();X.ellipse(30,70,150,130,-.2,0,7);X.fill();X.restore();
 // mouse (visto desde atrás y arriba)
 X.fillStyle=gl(-90,0,90,0,[[0,'#1d1f25'],[.5,'#3a3d46'],[1,'#1a1c21']]);X.beginPath();X.moveTo(0,-150);X.bezierCurveTo(70,-150,92,-60,90,30);X.bezierCurveTo(88,120,50,150,0,150);X.bezierCurveTo(-50,150,-88,120,-90,30);X.bezierCurveTo(-92,-60,-70,-150,0,-150);X.closePath();X.fill();X.strokeStyle=LIN;X.lineWidth=3;X.stroke();
 X.strokeStyle='rgba(0,0,0,.6)';X.lineWidth=3;X.beginPath();X.moveTo(0,-150);X.lineTo(0,-40);X.stroke();
 X.fillStyle=clic>0?`rgba(0,0,0,${.25*clic})`:'rgba(0,0,0,0)';X.beginPath();X.moveTo(-2,-150);X.bezierCurveTo(-70,-150,-90,-60,-89,-40);X.lineTo(-2,-40);X.closePath();X.fill();
 X.fillStyle='#0c0d10';rr(-9,-128,18,46,8);X.fill();X.strokeStyle='rgba(255,255,255,.25)';X.lineWidth=2;for(let i=0;i<5;i++){const yy=-122+((i*9+rueda*3)%45+45)%45;X.beginPath();X.moveTo(-6,yy);X.lineTo(6,yy);X.stroke()}
 X.fillStyle='rgba(255,255,255,.07)';X.beginPath();X.ellipse(-30,-80,26,60,-.2,0,7);X.fill();
 // manga y antebrazo (entran desde abajo a la derecha)
 X.save();X.translate(70,140);X.rotate(Math.atan2(.85,.53));
 X.fillStyle=gl(0,-60,0,60,[[0,p2],[.4,p1],[.8,p0],[1,p2]]);X.beginPath();X.moveTo(0,-50);X.lineTo(200,-60);X.lineTo(200,60);X.lineTo(0,52);X.closePath();X.fill();X.strokeStyle=LIN;X.lineWidth=4;X.stroke();
 X.fillStyle=gl(0,-90,0,90,[[0,'#1f242e'],[.35,'#3a4352'],[.7,'#2f3744'],[1,'#191d25']]);rr(170,-88,700,176,50);X.fill();X.strokeStyle=LIN;X.lineWidth=4;rr(170,-88,700,176,50);X.stroke();
 X.fillStyle=gl(0,-92,0,92,[[0,'#232935'],[.45,'#465063'],[1,'#1b2029']]);rr(160,-92,80,184,34);X.fill();X.strokeStyle=LIN;X.lineWidth=4;rr(160,-92,80,184,34);X.stroke();
 X.strokeStyle='rgba(10,12,16,.45)';X.lineWidth=3;for(let i=0;i<7;i++){X.beginPath();X.moveTo(170+i*10,-84);X.lineTo(170+i*10,84);X.stroke()}X.restore();
 // dorso de la mano sobre el mouse
 X.beginPath();X.moveTo(-70,-10);X.quadraticCurveTo(-60,-70,10,-78);X.quadraticCurveTo(84,-74,96,-20);X.quadraticCurveTo(108,60,74,120);X.quadraticCurveTo(10,150,-40,110);X.quadraticCurveTo(-82,60,-70,-10);X.closePath();
 X.fillStyle=gl(-80,-80,100,120,[[0,p0],[.5,p1],[1,p2]]);X.fill();X.strokeStyle=LIN;X.lineWidth=4;X.stroke();
 X.strokeStyle='rgba(120,70,40,.30)';X.lineWidth=3;[[-30,-50,-10,60],[0,-56,16,60],[30,-54,40,58]].forEach(([a1,b1,a2,b2])=>{X.beginPath();X.moveTo(a1,b1);X.quadraticCurveTo(a1+8,(b1+b2)/2,a2,b2);X.stroke()});
 // dedos: índice sobre la rueda/botón izquierdo, medio sobre el derecho, anular y meñique al costado, pulgar a la izquierda
 const dedo=(x0,y0,x1,y1,cx,cy,w,uña)=>{X.strokeStyle=LIN;X.lineWidth=w+6;X.beginPath();X.moveTo(x0,y0);X.quadraticCurveTo(cx,cy,x1,y1);X.stroke();X.strokeStyle=p1;X.lineWidth=w;X.beginPath();X.moveTo(x0,y0);X.quadraticCurveTo(cx,cy,x1,y1);X.stroke();X.strokeStyle='rgba(255,236,214,.45)';X.lineWidth=w*.25;X.beginPath();X.moveTo(x0-w*.2,y0);X.quadraticCurveTo(cx-w*.2,cy,x1-w*.2,y1+4);X.stroke();if(uña){X.fillStyle='rgba(248,222,206,.95)';X.beginPath();X.ellipse(x1,y1+4,w*.28,w*.22,0,0,7);X.fill()}};
 const iy=-128+rueda+clic*6;dedo(-22,-66,-8,iy,-20,-100,30,true);
 dedo(22,-70,40,-120+clic*0,36,-100,30,true);
 dedo(60,-58,86,-70,80,-70,26,false);dedo(80,-30,100,-16,98,-30,24,false);
 dedo(-66,0,-96,-40,-96,0,30,true);
 X.fillStyle='rgba(255,236,214,.30)';X.beginPath();X.ellipse(10,-40,40,14,-.3,0,7);X.fill();
 X.lineCap='butt';X.lineJoin='miter';X.restore()};

// ---------- utilería: taza y cuaderno en primer plano (cortados abajo a la izquierda, desenfocados) ----------
UTILERIA.p27_mesa04=(x,y,s,t,o)=>{const L=x;X.save();X.filter='blur(5px)';
 X.fillStyle='#d9d2c2';X.beginPath();X.moveTo(L-120,1660);X.lineTo(L+300,1620);X.lineTo(L+360,1990);X.lineTo(L-120,1990);X.closePath();X.fill();X.strokeStyle='rgba(60,70,90,.35)';X.lineWidth=3;for(let i=0;i<7;i++){X.beginPath();X.moveTo(L-110,1700+i*42);X.lineTo(L+320,1660+i*42+i*4);X.stroke()}
 X.fillStyle='#3b3f4a';for(let i=0;i<8;i++){X.beginPath();X.arc(L+300+i*3,1640+i*42,9,0,7);X.fill()}
 X.fillStyle=gl(L-60,0,L+170,0,[[0,'#2a3d52'],[.6,'#3f5a78'],[1,'#253547']]);X.fillRect(L-60,1500,220,230);X.beginPath();X.ellipse(L+50,1730,110,24,0,0,7);X.fill();
 X.fillStyle='#16202c';X.beginPath();X.ellipse(L+50,1500,110,22,0,0,7);X.fill();X.fillStyle='#4a2c1a';X.beginPath();X.ellipse(L+50,1504,96,16,0,0,7);X.fill();
 X.strokeStyle='#33495f';X.lineWidth=22;X.beginPath();X.arc(L+168,1600,52,-1.2,1.2);X.stroke();
 X.fillStyle='rgba(255,255,255,.10)';X.fillRect(L+100,1510,14,200);X.filter='none';X.restore()};

// ---------- utilería: ventana que se abre con el doble clic y crece hasta llenar el cuadro (puente al plano 05) ----------
UTILERIA.p27_ventana=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,t0=tk(o.abre,a),q=seg(t,t0,t0+o.dur);if(q<=0)return;const e=eio(q),L=x;
 const [ax,ay,aw,ah]=o.desde,[bx,by,bw,bh]=o.hasta,cx=lerp(ax,bx,e),cy=lerp(ay,by,e),w=lerp(aw,bw,e),h=lerp(ah,bh,e),bar=lerp(14,64,Math.min(1,e*2.2));
 X.save();X.globalAlpha=Math.min(1,q*6);X.shadowColor='rgba(0,0,0,.6)';X.shadowBlur=40;X.fillStyle='#1c1f27';X.fillRect(L+cx-w/2,cy-h/2,w,h);X.shadowBlur=0;
 X.fillStyle='#262a35';X.fillRect(L+cx-w/2,cy-h/2,w,bar);X.font=`600 ${Math.round(bar*.46)}px P`;X.textAlign='left';X.textBaseline='middle';X.fillStyle='#c9cfdb';X.fillText('tex_0412.png',L+cx-w/2+bar*.6,cy-h/2+bar/2);
 ['#e0605a','#e8b84a','#5ec46b'].forEach((c,i)=>{X.fillStyle=c;X.beginPath();X.arc(L+cx+w/2-bar*(.6+i*.7),cy-h/2+bar/2,bar*.18,0,7);X.fill()});
 const pad=lerp(4,0,e),iw=w-pad*2,ih=h-bar-pad*2,tw=Math.max(8,Math.round(iw)),th=Math.max(8,Math.round(ih));
 X.drawImage(tex27(999000+Math.round(tw/8),tw,th,'casco'),L+cx-w/2+pad,cy-h/2+bar+pad,iw,ih);
 X.restore()};

// ---------- utilería: luz de la pantalla sobre la habitación, el escritorio y la mano (sin tocar la pantalla) ----------
UTILERIA.p27_luzPantalla=(x,y,s,t,o)=>{o=o||{};const L=x,S=o.pantalla;X.save();X.beginPath();X.rect(L-300,-300,1680,2500);X.rect(L+S.x0,S.y0,S.x1-S.x0,S.y1-S.y0);X.clip('evenodd');
 X.globalCompositeOperation='multiply';const g=X.createRadialGradient(L+560,980,200,L+560,1100,1250);g.addColorStop(0,'rgb(230,234,246)');g.addColorStop(.55,'rgb(150,156,176)');g.addColorStop(1,'rgb(60,62,78)');X.fillStyle=g;X.fillRect(L-300,-300,1680,2500);
 X.globalCompositeOperation='lighter';const d=X.createLinearGradient(0,S.y1,0,S.y1+520);d.addColorStop(0,'rgba(150,175,230,.16)');d.addColorStop(1,'rgba(150,175,230,0)');X.fillStyle=d;X.fillRect(L-300,S.y1,1680,520);
 X.restore();X.save();
 X.globalCompositeOperation='overlay';X.globalAlpha=.08;if(!window.__GR27b){const c=document.createElement('canvas');c.width=c.height=256;const gx=c.getContext('2d'),dd=gx.createImageData(256,256);for(let i=0;i<dd.data.length;i+=4){const v=110+rnd(i*.37+11)*145;dd.data[i]=dd.data[i+1]=dd.data[i+2]=v;dd.data[i+3]=255}gx.putImageData(dd,0,0);window.__GR27b=X.createPattern(c,'repeat')}X.fillStyle=window.__GR27b;X.fillRect(L-300,-300,1680,2500);
 X.globalAlpha=1;X.globalCompositeOperation='source-over';const v=X.createRadialGradient(L+540,1000,500,L+540,1000,1300);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(2,2,8,.5)');X.fillStyle=v;X.fillRect(L-300,-300,1680,2500);X.restore()};
