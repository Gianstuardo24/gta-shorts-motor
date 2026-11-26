// ===== P27 · INICIO · prueba técnica del doc 27 (plano 10) =====
// Todo con prefijo p27_. Inerte: nada aquí se ejecuta salvo que una escena use estos sets o esta utilería.
(function(){
const mezcla=(a,b,q)=>a.map((v,i)=>Math.round(lerp(v,b[i],q)));
const rgb=c=>`rgb(${c[0]},${c[1]},${c[2]})`;
const intens=(t,o)=>{const a=window.__A||0;let I=o.int!==undefined?o.int:1;if(o.dim){I=lerp(I,o.dim[2],eio(seg(t,tk(o.dim[0],a),tk(o.dim[1],a))))}return I};
const negro=(t,o)=>{const a=window.__A||0;return o.negro?eio(seg(t,tk(o.negro[0],a),tk(o.negro[1],a)))*(o.negro[2]!==undefined?o.negro[2]:.95):0};

// ---------- set: repisa de madera de frente, a la altura de la repisa ----------
NUEVOS.p27_repisaV={osc:.1,luces(){return []},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),B=o.estado==='B',Y=o.repisa||1250;
  // pared de madera
  let g=X.createLinearGradient(0,0,0,1920);g.addColorStop(0,B?'#1c1916':'#2a1c14');g.addColorStop(.6,B?'#2b2622':'#3e2b1f');g.addColorStop(1,'#0c0806');
  X.fillStyle=g;X.fillRect(L-300,-300,1680,2500);
  for(let i=0;i<9;i++){const x=L-130+i*172;X.fillStyle=`rgba(0,0,0,${.20+.07*rnd(i+3)})`;X.fillRect(x,-300,5,Y+300);X.fillStyle='rgba(255,222,184,.05)';X.fillRect(x+6,-300,3,Y+300);
   X.strokeStyle='rgba(0,0,0,.08)';X.lineWidth=2;for(let j=0;j<5;j++){const vx=x+22+rnd(i*9+j)*130;X.beginPath();X.moveTo(vx,-300);X.bezierCurveTo(vx+12,300,vx-14,760,vx+6,Y);X.stroke()}}
  // repisa de arriba, fuera de foco (da profundidad y enmarca)
  X.save();X.filter='blur(9px)';
  if(B){[[60,250,150,'#6b5a45'],[230,300,110,'#57493a'],[700,330,170,'#5e4f3f'],[880,160,120,'#4d4034']].forEach(([x,w,h,c])=>{X.fillStyle=c;X.fillRect(L+x,560-h,w,h);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(L+x,560-h,w,14)})}
  else{[[90,46,190,'#7b2e2a'],[140,40,170,'#2f4a5e'],[184,52,200,'#8a6a3a'],[240,38,160,'#3d5a3a']].forEach(([x,w,h,c])=>{X.fillStyle=c;X.fillRect(L+x,560-h,w,h)});
   X.fillStyle='rgba(0,0,0,.35)';X.fillRect(L+80,360,220,200);[[820,150,60,'#5c4a3a'],[880,110,44,'#6e5a44']].forEach(([x,w,h,c])=>{X.fillStyle=c;X.fillRect(L+x,560-h,w,h)})}
  X.fillStyle='#24170f';X.fillRect(L-200,560,1480,64);X.fillStyle='#5a3b26';X.fillRect(L-200,556,1480,10);X.fillStyle='rgba(0,0,0,.5)';X.fillRect(L-200,624,1480,46);
  X.restore();
  // B: mancha de humedad y pintura gastada en la pared
  if(B){X.save();X.filter='blur(6px)';[[L+760,300,260,'rgba(70,58,40,.30)'],[L+690,420,170,'rgba(60,50,36,.22)'],[L+180,900,200,'rgba(55,48,40,.18)']].forEach(([mx,my,mr,mc])=>{X.fillStyle=mc;X.beginPath();for(let i=0;i<=20;i++){const an=i/20*7,rr3=mr*(.75+.35*rnd(i+mx*.01));i?X.lineTo(mx+Math.cos(an)*rr3,my+Math.sin(an)*rr3*.8):X.moveTo(mx+Math.cos(an)*rr3,my+Math.sin(an)*rr3*.8)}X.fill()});X.filter='none';X.strokeStyle='rgba(20,14,10,.35)';X.lineWidth=2;X.beginPath();X.moveTo(L+720,200);X.lineTo(L+700,330);X.lineTo(L+735,420);X.lineTo(L+716,520);X.stroke();X.restore()}
  // telaraña y polvo (solo B)
  if(B){X.save();X.strokeStyle='rgba(225,225,230,.16)';X.lineWidth=1.6;const cx=L+40,cy=672;for(let i=0;i<7;i++){const an=i/6*Math.PI/2;X.beginPath();X.moveTo(cx,cy);X.lineTo(cx+Math.cos(an)*230,cy+Math.sin(an)*170);X.stroke()}
   for(let r=1;r<5;r++){X.beginPath();for(let i=0;i<7;i++){const an=i/6*Math.PI/2,rr2=r*52;const px=cx+Math.cos(an)*rr2,py=cy+Math.sin(an)*rr2*.74;i?X.quadraticCurveTo(cx+Math.cos(an-.13)*rr2*.9,cy+Math.sin(an-.13)*rr2*.66,px,py):X.moveTo(px,py)}X.stroke()}X.restore()}
  // tabla principal: un filo de la superficie y el canto
  X.fillStyle=gl(0,Y-24,0,Y,[[0,B?'#6f5844':'#80583a'],[1,B?'#5a4636':'#5e3e26']]);X.fillRect(L-200,Y-24,1480,24);
  if(B){X.fillStyle='rgba(205,200,190,.34)';X.fillRect(L-200,Y-24,1480,12);X.fillStyle='rgba(205,200,190,.10)';X.fillRect(L-200,Y,1480,80);for(let i=0;i<160;i++){X.fillStyle=`rgba(220,214,200,${.12+.2*rnd(i+40)})`;X.fillRect(L-180+rnd(i)*1440,Y-22+rnd(i+7)*18,2+rnd(i+3)*3,2)}}
  X.fillStyle=gl(0,Y,0,Y+80,[[0,'#6e4729'],[.18,'#5b3a21'],[1,'#3a2413']]);X.fillRect(L-200,Y,1480,80);
  X.fillStyle='rgba(255,226,180,.30)';X.fillRect(L-200,Y,1480,3);
  X.strokeStyle='rgba(0,0,0,.16)';X.lineWidth=2;for(let j=0;j<7;j++){const yy=Y+12+j*9+rnd(j)*5;X.beginPath();X.moveTo(L-200,yy);for(let k=0;k<=12;k++)X.lineTo(L-200+k*124,yy+Math.sin(k*1.7+j)*3);X.stroke()}
  X.fillStyle='rgba(0,0,0,.6)';X.fillRect(L-200,Y+80,1480,34);
  // parte de abajo: repisa baja con contenido (A ordenada; B desorden, sus cajas son utilería)
  const Y2=Y+300;g=gl(0,Y+114,0,Y2,[[0,'#1d130c'],[1,'#140d08']]);X.fillStyle=g;X.fillRect(L-200,Y+114,1480,Y2-Y-114);
  if(!B){let bx=L+40;const C=['#6b2f2a','#2f4a5e','#7a6236','#3d5a3a','#5a3a52','#7a4a2a','#2e3d52','#6b5a3a','#4a2f2a','#355246'];for(let i=0;i<10;i++){const w=34+rnd(i+20)*20,h=150+rnd(i+30)*60;X.fillStyle=C[i];X.fillRect(bx,Y2-18-h,w,h);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(bx+w-6,Y2-18-h,6,h);X.fillStyle='rgba(230,200,120,.55)';X.fillRect(bx+4,Y2-18-h+22,w-8,4);X.fillRect(bx+4,Y2-18-28,w-8,4);bx+=w+3}
   X.fillStyle=gl(0,Y2-190,0,Y2,[[0,'#9a7a54'],[1,'#7f6243']]);X.fillRect(L+640,Y2-18-170,260,170);X.fillStyle='rgba(240,232,212,.9)';X.fillRect(L+700,Y2-130,140,46);X.strokeStyle='rgba(60,50,40,.6)';X.lineWidth=3;[0,1].forEach(i=>{X.beginPath();X.moveTo(L+712,Y2-116+i*16);X.lineTo(L+790+i*20,Y2-116+i*16);X.stroke()});X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L+640,Y2-188,260,14)}
  else{[[L+120,Y2-30],[L+700,Y2-26],[L+430,Y2-24]].forEach(([px,py],i)=>{X.fillStyle=`rgba(205,198,182,${.55-.1*i})`;X.beginPath();for(let k=0;k<=12;k++){const an=k/12*7,r4=26*(0.7+.5*rnd(k+i*13));k?X.lineTo(px+Math.cos(an)*r4,py+Math.sin(an)*r4*.75):X.moveTo(px+Math.cos(an)*r4,py+Math.sin(an)*r4*.75)}X.fill()})}
  X.fillStyle=gl(0,Y2-18,0,Y2,[[0,B?'#5e4c3b':'#6e4c30'],[1,'#4a3220']]);X.fillRect(L-200,Y2-18,1480,18);X.fillStyle=gl(0,Y2,0,Y2+64,[[0,'#56391f'],[1,'#2a1a0e']]);X.fillRect(L-200,Y2,1480,64);X.fillStyle='rgba(255,226,180,.18)';X.fillRect(L-200,Y2,1480,2);
  if(B){X.fillStyle='rgba(205,200,190,.28)';X.fillRect(L-200,Y2-18,1480,8)}
  X.fillStyle='rgba(0,0,0,.6)';X.fillRect(L-200,Y2+64,1480,40);X.fillStyle='#0b0705';X.fillRect(L-200,Y2+104,1480,700);
 }};

// ---------- utilería: barco de juguete "THE LEONIDA" (geometría única: A y B usan esta misma función y escala) ----------
UTILERIA.p27_barco=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);
 if(o.sombra){const sg=X.createRadialGradient(0,0,10,0,0,260);sg.addColorStop(0,`rgba(0,0,0,${o.sombra})`);sg.addColorStop(1,'rgba(0,0,0,0)');X.save();X.scale(1,.13);X.fillStyle=sg;X.beginPath();X.arc(0,0,260,0,7);X.fill();X.restore()}
 const ang=Math.atan2(-18,464);
 // mástil y banderín (detrás de la cabina)
 X.fillStyle='#8a6640';X.fillRect(127,-318,10,208);X.fillStyle='rgba(255,235,200,.45)';X.fillRect(127,-318,3,208);X.fillRect(104,-282,56,6);X.fillStyle='#e8c24a';X.beginPath();X.moveTo(136,-316);X.lineTo(192,-302);X.lineTo(136,-288);X.closePath();X.fill();
 // chimenea
 X.fillStyle=gl(-44,0,10,0,[[0,'#8e1f1a'],[.45,'#c9372c'],[1,'#7a1a16']]);rr(-44,-300,54,92,6);X.fill();X.fillStyle='#1b1b1f';rr(-46,-306,58,22,6);X.fill();X.fillStyle='rgba(255,255,255,.18)';X.fillRect(-36,-282,6,70);
 // cabina
 X.fillStyle=gl(0,-208,0,-110,[[0,'#f4ecdc'],[1,'#d9cdb6']]);rr(-100,-208,180,100,10);X.fill();X.strokeStyle='#2b3a55';X.lineWidth=4;rr(-100,-208,180,100,10);X.stroke();
 [-78,-28,22].forEach(wx=>{X.fillStyle=gl(0,-190,0,-150,[[0,'#9fd0e8'],[1,'#4f86a6']]);rr(wx,-190,38,40,7);X.fill();X.strokeStyle='#2b3a55';X.lineWidth=3;rr(wx,-190,38,40,7);X.stroke();X.fillStyle='rgba(255,255,255,.55)';X.fillRect(wx+6,-186,8,16)});
 X.strokeStyle='#e0e0e0';X.lineWidth=9;X.beginPath();X.arc(62,-158,15,0,7);X.stroke();X.strokeStyle='#c62f2a';X.lineWidth=9;X.setLineDash([8,8]);X.beginPath();X.arc(62,-158,15,0,7);X.stroke();X.setLineDash([]);
 X.fillStyle='#b8322a';rr(-114,-222,206,18,6);X.fill();X.fillStyle='rgba(255,255,255,.22)';X.fillRect(-108,-220,194,4);
 // casco
 const casco=()=>{X.beginPath();X.moveTo(-230,-108);X.lineTo(236,-126);X.quadraticCurveTo(224,-38,172,-12);X.quadraticCurveTo(20,4,-150,-2);X.quadraticCurveTo(-216,-12,-230,-62);X.closePath()};
 X.save();casco();X.clip();X.save();X.rotate(ang);
 X.fillStyle='#22345a';X.fillRect(-300,-160,620,64);
 X.fillStyle=gl(0,-100,0,-40,[[0,'#f6efdf'],[1,'#e3d6bc']]);X.fillRect(-300,-100,620,62);
 X.fillStyle='#b5302a';X.fillRect(-300,-38,620,60);X.fillStyle='rgba(0,0,0,.18)';X.fillRect(-300,-40,620,4);
 X.restore();
 X.fillStyle=gl(0,-130,0,0,[[0,'rgba(255,255,255,.18)'],[.3,'rgba(255,255,255,0)'],[.8,'rgba(0,0,0,.10)'],[1,'rgba(0,0,0,.35)']]);X.fillRect(-240,-140,490,150);
 X.restore();
 casco();X.strokeStyle='#2a1c12';X.lineWidth=4;X.stroke();
 X.save();X.rotate(ang);X.fillStyle='#6b4528';X.fillRect(-232,-118,470,12);X.fillStyle='rgba(255,230,190,.35)';X.fillRect(-232,-118,470,3);
 X.font='800 50px P';X.textAlign='center';X.textBaseline='middle';X.fillStyle='#1d2b47';X.fillText('THE LEONIDA',4,-68);X.restore();
 [-150,170].forEach(bx=>{X.fillStyle='#2a2a2e';rr(bx-8,-136+(bx>0?-6:0),16,18,4);X.fill()});
 X.restore()};

// ---------- utilería: lamparita de escritorio articulada ----------
const LAMPARA=o=>({b:o.base,c:o.codo,h:o.cabeza,eje:o.eje});
UTILERIA.p27_lamparita=(x,y,s,t,o)=>{o=o||{};const P=LAMPARA(o),[bx,by]=P.b,[cx,cy]=P.c,[hx,hy]=P.h,e=P.eje;X.save();
 X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(bx,by+4,86,13,0,0,7);X.fill();
 X.fillStyle=gl(bx-70,0,bx+70,0,[[0,'#1d1d22'],[.5,'#3a3a42'],[1,'#141418']]);X.beginPath();X.ellipse(bx,by-8,70,16,0,0,7);X.fill();X.fillRect(bx-70,by-22,140,14);X.beginPath();X.ellipse(bx,by-22,70,16,0,0,7);X.fill();
 X.lineCap='round';[[bx,by-26,cx,cy],[cx,cy,hx,hy]].forEach(([x1,y1,x2,y2])=>{X.strokeStyle='#23232a';X.lineWidth=16;X.beginPath();X.moveTo(x1,y1);X.lineTo(x2,y2);X.stroke();X.strokeStyle='rgba(255,255,255,.16)';X.lineWidth=4;X.beginPath();X.moveTo(x1-4,y1);X.lineTo(x2-4,y2);X.stroke()});
 X.fillStyle='#2e2e36';[[cx,cy],[hx,hy]].forEach(([px,py])=>{X.beginPath();X.arc(px,py,14,0,7);X.fill()});
 X.save();X.translate(hx,hy);X.rotate(e);X.fillStyle=gl(0,-60,0,60,[[0,'#3b3b44'],[.5,'#2a2a31'],[1,'#17171c']]);X.beginPath();X.moveTo(-8,-34);X.lineTo(-8,34);X.lineTo(126,82);X.lineTo(126,-82);X.closePath();X.fill();
 X.strokeStyle='rgba(255,255,255,.12)';X.lineWidth=3;X.beginPath();X.moveTo(-8,-34);X.lineTo(126,-82);X.stroke();X.restore();X.lineCap='butt';X.restore()};

// ---------- utilería: mano que toma el barco por la popa (pulgar sobre la borda, índice en la punta) ----------
// Mismo lenguaje que el barco: contorno marrón oscuro de 4 px, degradado con luz desde la derecha (la lámpara).
UTILERIA.p27_mano=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,ab=o.suelta?eio(seg(t,tk(o.suelta[0],a),tk(o.suelta[1],a))):0;X.save();X.translate(x,y);X.scale(s,s);
 const LIN='rgba(42,28,18,.85)',p0='#f1c29b',p1='#dca37b',p2='#b77c56',dx=-.56,dy=-.83;X.lineJoin='round';X.lineCap='round';
 // sombra de contacto sobre el casco
 X.save();X.globalAlpha*=.30*(1-ab);const sh=X.createRadialGradient(14,-34,2,14,-34,46);sh.addColorStop(0,'rgba(20,10,5,1)');sh.addColorStop(1,'rgba(20,10,5,0)');X.fillStyle=sh;X.beginPath();X.arc(14,-34,46,0,7);X.fill();X.restore();
 // antebrazo y manga (desde la muñeca hacia la izquierda, apenas hacia arriba)
 X.save();X.translate(-70,-40);X.rotate(Math.atan2(dy,dx));
 X.fillStyle=gl(0,-48,0,48,[[0,p2],[.35,p1],[.7,p0],[1,p2]]);X.beginPath();X.moveTo(0,-34);X.bezierCurveTo(90,-44,170,-48,250,-50);X.lineTo(250,50);X.bezierCurveTo(170,48,90,44,0,34);X.closePath();X.fill();X.strokeStyle=LIN;X.lineWidth=4;X.stroke();
 X.fillStyle=gl(0,-70,0,70,[[0,'#1c2c22'],[.3,'#3d5f47'],[.6,'#33503c'],[1,'#162219']]);rr(232,-66,900,132,44);X.fill();X.strokeStyle=LIN;X.lineWidth=4;rr(232,-66,900,132,44);X.stroke();
 X.strokeStyle='rgba(10,20,14,.35)';X.lineWidth=2;for(let i=0;i<40;i++){X.beginPath();X.moveTo(300+i*20,-60);X.lineTo(300+i*20,60);X.stroke()}
 X.fillStyle=gl(0,-72,0,72,[[0,'#22362a'],[.4,'#4a7055'],[1,'#1a281f']]);rr(226,-72,72,144,30);X.fill();X.strokeStyle=LIN;X.lineWidth=4;rr(226,-72,72,144,30);X.stroke();
 X.strokeStyle='rgba(10,20,14,.45)';X.lineWidth=3;for(let i=0;i<6;i++){X.beginPath();X.moveTo(236+i*11,-64);X.lineTo(236+i*11,64);X.stroke()}
 X.restore();
 // dorso de la mano (a la izquierda de la popa)
 X.beginPath();X.moveTo(-96,-30);X.quadraticCurveTo(-78,-62,-30,-60);X.quadraticCurveTo(4,-56,8,-26);X.lineTo(10,18);X.quadraticCurveTo(2,46,-34,48);X.quadraticCurveTo(-82,44,-98,12);X.closePath();
 X.fillStyle=gl(-96,0,10,0,[[0,p2],[.45,p1],[1,p0]]);X.fill();X.strokeStyle=LIN;X.lineWidth=4;X.stroke();
 X.strokeStyle='rgba(120,70,40,.35)';X.lineWidth=3;[[-60,-30,-40,10],[-44,-34,-24,8]].forEach(([a1,b1,a2,b2])=>{X.beginPath();X.moveTo(a1,b1);X.quadraticCurveTo(a1+16,(b1+b2)/2,a2,b2);X.stroke()});
 [[4,22],[0,36]].forEach(([kx,ky])=>{X.fillStyle=p1;X.beginPath();X.ellipse(kx,ky,13,10,0,0,7);X.fill();X.strokeStyle=LIN;X.lineWidth=3;X.stroke()});
 X.fillStyle='rgba(255,236,214,.35)';X.beginPath();X.ellipse(-8,-40,16,8,-.4,0,7);X.fill();
 // índice: rodea la punta de la popa; al soltar se abre hacia la izquierda
 const ix=lerp(26,-14,ab),iy=lerp(-2,14,ab);X.strokeStyle=LIN;X.lineWidth=27;X.beginPath();X.moveTo(2,-34);X.quadraticCurveTo(lerp(28,4,ab),lerp(-36,-20,ab),ix,iy);X.stroke();
 X.strokeStyle=p1;X.lineWidth=20;X.beginPath();X.moveTo(2,-34);X.quadraticCurveTo(lerp(28,4,ab),lerp(-36,-20,ab),ix,iy);X.stroke();X.strokeStyle='rgba(255,236,214,.45)';X.lineWidth=5;X.beginPath();X.moveTo(6,-38);X.quadraticCurveTo(lerp(30,6,ab),lerp(-40,-24,ab),ix+3,iy-6);X.stroke();
 X.fillStyle='rgba(248,220,204,.95)';X.beginPath();X.ellipse(ix+2,iy+3,6,5,0,0,7);X.fill();
 // pulgar: apoyado sobre la borda; al soltar se levanta
 const tx=lerp(52,34,ab),ty=lerp(-60,-104,ab);X.strokeStyle=LIN;X.lineWidth=29;X.beginPath();X.moveTo(-22,-50);X.quadraticCurveTo(lerp(14,4,ab),lerp(-74,-92,ab),tx,ty);X.stroke();
 X.strokeStyle=p0;X.lineWidth=22;X.beginPath();X.moveTo(-22,-50);X.quadraticCurveTo(lerp(14,4,ab),lerp(-74,-92,ab),tx,ty);X.stroke();X.strokeStyle=p1;X.lineWidth=8;X.beginPath();X.moveTo(-18,-44);X.quadraticCurveTo(lerp(16,6,ab),lerp(-66,-86,ab),tx-2,ty+6);X.stroke();
 X.fillStyle='rgba(250,226,210,.95)';X.beginPath();X.ellipse(tx-4,ty-3,9,6,-.2,0,7);X.fill();X.strokeStyle='rgba(120,70,40,.5)';X.lineWidth=2;X.stroke();
 X.lineCap='butt';X.lineJoin='miter';X.restore()};

// ---------- utilería: caja de cartón de archivo ----------
UTILERIA.p27_caja=(x,y,s,t,o)=>{o=o||{};const w=o.w||300,h=o.h||200,c=o.color||'#8a6a46';X.save();X.translate(x,y);X.scale(s,s);
 X.fillStyle=gl(-w/2,0,w/2,0,[[0,_osc(c,.78)],[.12,c],[.85,c],[1,_osc(c,.7)]]);X.fillRect(-w/2,-h,w,h);
 X.fillStyle='rgba(0,0,0,.16)';X.fillRect(-w/2,-h,w,h*.16);X.fillStyle='rgba(255,240,210,.10)';X.fillRect(-w/2,-h+h*.16,w,3);
 X.fillStyle='rgba(230,215,180,.35)';X.fillRect(-14,-h,28,h*.4);
 if(o.etiqueta!==false){X.fillStyle='rgba(236,228,206,.85)';X.fillRect(-w*.28,-h*.62,w*.44,h*.26);X.strokeStyle='rgba(60,50,40,.55)';X.lineWidth=3;for(let i=0;i<3;i++){X.beginPath();X.moveTo(-w*.25,-h*.56+i*h*.07);X.lineTo(-w*.25+w*(.22+.14*rnd(i+(o.sem||0))),-h*.56+i*h*.07);X.stroke()}}
 X.strokeStyle='rgba(0,0,0,.22)';X.lineWidth=2;X.beginPath();X.moveTo(-w*.4,-h*.2);X.lineTo(-w*.3,-h*.05);X.moveTo(w*.3,-h*.8);X.lineTo(w*.38,-h*.7);X.stroke();
 if(o.polvo){X.fillStyle=`rgba(210,205,195,${.35*o.polvo})`;X.fillRect(-w/2,-h,w,7);X.fillStyle=`rgba(200,195,185,${.10*o.polvo})`;X.fillRect(-w/2,-h,w,h)}
 X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-w/2,-3,w,3);X.restore()};

// ---------- utilería: primer plano desenfocado (borde de mesa con objetos) ----------
UTILERIA.p27_frente=(x,y,s,t,o)=>{o=o||{};const L=x,B=o.estado==='B',Y0=o.y0||1690;X.save();X.filter='blur(16px)';
 X.fillStyle=gl(0,Y0,0,Y0+260,[[0,B?'#3a3026':'#3b2414'],[.12,B?'#2a221b':'#2a170c'],[1,'#0c0704']]);X.fillRect(L-300,Y0,1680,500);X.fillStyle=B?'rgba(210,205,195,.25)':'rgba(255,214,160,.30)';X.fillRect(L-300,Y0,1680,8);
 if(!B){X.fillStyle='#5a2622';X.fillRect(L+70,Y0-80,320,44);X.fillStyle='#2c3f52';X.fillRect(L+90,Y0-124,290,44);X.fillStyle='rgba(255,220,170,.25)';X.fillRect(L+90,Y0-124,290,6);
  X.fillStyle='#3a2a1c';X.fillRect(L+840,Y0-150,110,150);X.fillStyle='#7a6a4a';[0,1,2].forEach(i=>X.fillRect(L+860+i*28,Y0-230+i*14,10,90))}
 else{X.fillStyle='#6d5a44';X.fillRect(L+720,Y0-170,420,170);X.fillStyle='rgba(215,210,200,.3)';X.fillRect(L+720,Y0-170,420,12);
  X.fillStyle='#8d8676';X.beginPath();X.moveTo(L-100,Y0-40);X.quadraticCurveTo(L+150,Y0-130,L+380,Y0-20);X.lineTo(L+380,Y0+40);X.lineTo(L-100,Y0+40);X.closePath();X.fill();
  X.fillStyle='rgba(225,220,210,.7)';[[L+500,Y0-26],[L+600,Y0-18]].forEach(([px,py])=>{X.beginPath();X.arc(px,py,30,0,7);X.fill()})}
 X.filter='none';X.restore()};

// ---------- utilería: tela con polvo sobre las cajas (B) ----------
UTILERIA.p27_tela=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);const w=o.w||300;
 X.fillStyle=gl(0,-20,0,200,[[0,'#a59d8c'],[1,'#7f7868']]);X.beginPath();X.moveTo(-w/2-10,0);X.quadraticCurveTo(-w/4,-24,0,-6);X.quadraticCurveTo(w/4,-26,w/2+8,-4);X.lineTo(w/2+4,30);X.quadraticCurveTo(w/2-20,70,w/2-60,60);X.quadraticCurveTo(w/2-110,40,w/2-150,70);X.lineTo(-w/2+30,62);X.quadraticCurveTo(-w/2-10,150,-w/2-30,210);X.quadraticCurveTo(-w/2-40,120,-w/2-10,0);X.closePath();X.fill();
 X.strokeStyle='rgba(42,28,18,.55)';X.lineWidth=3;X.stroke();X.strokeStyle='rgba(60,55,45,.35)';X.lineWidth=4;[[-w/2+10,10,-w/2-10,170],[-40,0,-60,50],[60,2,40,56]].forEach(([a1,b1,a2,b2])=>{X.beginPath();X.moveTo(a1,b1);X.quadraticCurveTo((a1+a2)/2+12,(b1+b2)/2,a2,b2);X.stroke()});
 X.fillStyle='rgba(235,232,222,.25)';X.fillRect(-w/2,-14,w,8);X.restore()};

// ---------- utilería: telaraña desde la punta del mástil a la repisa de arriba (B) ----------
UTILERIA.p27_telarana=(x,y,s,t,o)=>{o=o||{};const P=o.desde,Q=o.hasta||[];X.save();X.lineCap='round';
 X.strokeStyle='rgba(232,232,236,.42)';X.lineWidth=1.8;Q.forEach(([qx,qy],i)=>{X.beginPath();X.moveTo(P[0],P[1]);X.quadraticCurveTo((P[0]+qx)/2+8*Math.sin(i),(P[1]+qy)/2+26,qx,qy);X.stroke()});
 X.strokeStyle='rgba(232,232,236,.30)';X.lineWidth=1.3;for(let k=1;k<6;k++){const f=k/6;X.beginPath();Q.forEach(([qx,qy],i)=>{const mx=(P[0]+qx)/2+8*Math.sin(i),my=(P[1]+qy)/2+26,u=1-f,px=u*u*P[0]+2*u*f*mx+f*f*qx,py=u*u*P[1]+2*u*f*my+f*f*qy;i?X.lineTo(px,py+4*Math.sin(k+i)):X.moveTo(px,py)});X.stroke()}
 X.restore()};

// ---------- utilería: pelusa de polvo que cae ----------
UTILERIA.p27_pelusa=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,k0=tk(o.cae[0],a),k1=tk(o.cae[1],a);if(t<k0)return;const q=seg(t,k0,k1);
 const px=x+Math.sin(q*9)*36+q*o.dx,py=lerp(y,o.y1,eo(q));X.save();X.translate(px,py);X.rotate(q*2.2);X.scale(s,s);
 // bola de polvo: motas superpuestas y borde fibroso corto (sin "patas")
 const hg=X.createRadialGradient(0,0,0,0,0,30);hg.addColorStop(0,'rgba(255,248,232,.22)');hg.addColorStop(1,'rgba(255,248,232,0)');X.fillStyle=hg;X.beginPath();X.arc(0,0,30,0,7);X.fill();
 for(let i=0;i<46;i++){const an=rnd(i*1.7+3)*7,rd=Math.sqrt(rnd(i*2.3+5))*15*(.8+.3*Math.sin(an*3)),r=2.6+rnd(i+9)*4.2;X.fillStyle=i<14?`rgba(150,145,135,${.35+.2*rnd(i)})`:`rgba(236,233,225,${.45+.35*rnd(i+4)})`;X.beginPath();X.arc(Math.cos(an)*rd,Math.sin(an)*rd*.85,r,0,7);X.fill()}
 X.lineCap='round';for(let i=0;i<70;i++){const an=rnd(i*3.1+7)*7,r0=12+rnd(i+13)*5,l=3+rnd(i+17)*6,cu=(rnd(i+19)-.5)*1.2;X.strokeStyle=`rgba(235,231,222,${.4+.4*rnd(i+21)})`;X.lineWidth=1;X.beginPath();X.moveTo(Math.cos(an)*r0,Math.sin(an)*r0*.85);X.lineTo(Math.cos(an+cu*.2)*(r0+l),Math.sin(an+cu*.2)*(r0+l)*.85);X.stroke()}
 X.lineCap='butt';X.restore()};

// ---------- utilería: fundido a negro y vuelta (dip to black) centrado en un corte ----------
// Cubre toda la pantalla (no el subtítulo, que el motor dibuja después). El salto de cámara ocurre dentro del negro.
UTILERIA.p27_negro=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,c=tk(o.centro,a),b=o.baja||.20,n=o.negro||.08,u=o.sube||.20;
 const t0=c-n/2-b,t1=c-n/2,t2=c+n/2,t3=c+n/2+u;if(t<t0||t>t3)return;
 const al=t<t1?(t-t0)/b:(t<=t2?1:1-(t-t2)/u);X.save();X.setTransform(1,0,0,1,0,0);X.globalAlpha=1;X.globalCompositeOperation='source-over';X.filter='none';X.fillStyle=`rgba(0,0,0,${Math.max(0,Math.min(1,al))})`;X.fillRect(0,0,X.canvas.width,X.canvas.height);X.restore()};

// ---------- utilería: luz de la escena (va al final, encima de todo lo iluminado) ----------
let GR27=null;
UTILERIA.p27_luz=(x,y,s,t,o)=>{o=o||{};const L=x,I=intens(t,o),[cx,cy]=o.foco,r=o.r||480,amb=o.amb||[70,60,64],cen=o.centro||[255,236,210];
 X.save();X.beginPath();X.rect(L-300,-300,1680,2500);X.clip();   /* la luz solo afecta su propia zona */
 // 1) penumbra del entorno: multiplica (centro casi intacto, bordes oscuros); al apagarse todo se oscurece
 X.globalCompositeOperation='multiply';
 const C=mezcla(mezcla(amb,[0,0,0],.45),cen,I),E=mezcla(mezcla(amb,[0,0,0],.6),amb,I);
 const g=X.createRadialGradient(cx,cy,r*.12,cx,cy,r*1.9);g.addColorStop(0,rgb(C));g.addColorStop(.42,rgb(mezcla(C,E,.55)));g.addColorStop(1,rgb(E));
 X.fillStyle=g;X.save();X.translate(cx,cy);X.scale(1.3,.82);X.translate(-cx,-cy);X.fillRect(L-900,-1400,2900,4800);X.restore();
 // 2) haz y charco de luz cálida
 X.globalCompositeOperation='lighter';const [hx,hy]=o.cabeza,e=o.eje,mx=hx+Math.cos(e)*120,my=hy+Math.sin(e)*120,lc=o.color||'255,214,150';
 if(I>.02){X.save();if(o.corteY){X.beginPath();X.rect(L-300,-300,1680,o.corteY+300);X.clip()}X.filter='blur(22px)';const cg=X.createLinearGradient(mx,my,cx,cy);cg.addColorStop(0,`rgba(${lc},${(o.haz||.26)*I})`);cg.addColorStop(1,`rgba(${lc},0)`);X.fillStyle=cg;
  const nx=-Math.sin(e),ny=Math.cos(e),d=Math.hypot(cx-mx,cy-my),w0=70,w1=r*.85;X.beginPath();X.moveTo(mx+nx*w0,my+ny*w0);X.lineTo(mx-nx*w0,my-ny*w0);
  const px=-(cy-my)/d,py=(cx-mx)/d;X.lineTo(cx-px*w1,cy-py*w1);X.lineTo(cx+px*w1,cy+py*w1);X.closePath();X.fill();X.filter='none';X.restore();
  const pg=X.createRadialGradient(cx,cy,0,cx,cy,r);pg.addColorStop(0,`rgba(${lc},${(o.charco||.20)*I})`);pg.addColorStop(1,`rgba(${lc},0)`);X.fillStyle=pg;X.save();X.translate(cx,cy);X.scale(1.25,.6);X.translate(-cx,-cy);X.beginPath();X.arc(cx,cy,r,0,7);X.fill();X.restore();
  // motas en el haz
  for(let i=0;i<22;i++){const u=rnd(i*3.7+1),v=((rnd(i*1.3+5)+t*.035*(.5+rnd(i)))%1),qx=lerp(mx,cx,v)+(u-.5)*lerp(w0*1.6,w1*1.4,v),qy=lerp(my,cy,v)+(rnd(i+8)-.5)*60;X.fillStyle=`rgba(255,240,215,${(.10+.22*rnd(i+2))*I})`;X.beginPath();X.arc(qx,qy,1.4+rnd(i+4)*2.2,0,7);X.fill()}
  // ampolleta
  const bg=X.createRadialGradient(mx-Math.cos(e)*40,my-Math.sin(e)*40,0,mx,my,150);bg.addColorStop(0,`rgba(255,246,222,${.9*I})`);bg.addColorStop(.3,`rgba(${lc},${.35*I})`);bg.addColorStop(1,`rgba(${lc},0)`);X.fillStyle=bg;X.beginPath();X.arc(mx-Math.cos(e)*30,my-Math.sin(e)*30,150,0,7);X.fill()}
 // 2b) bajo la tabla la lámpara no llega: sombra progresiva
 if(o.corteY){X.globalCompositeOperation='multiply';const sb=X.createLinearGradient(0,o.corteY+90,0,o.corteY+520);sb.addColorStop(0,'rgb(255,255,255)');sb.addColorStop(1,'rgb(105,100,104)');X.fillStyle=sb;X.fillRect(L-300,o.corteY+90,1680,2000)}
 if(o.bruma){X.globalCompositeOperation='screen';X.fillStyle=`rgba(150,148,140,${o.bruma})`;X.fillRect(L-300,-300,1680,2500)}
 // 3) relleno frío del cuarto (B) y grano propio (el acabado "pro" no se usa en esta prueba)
 X.globalCompositeOperation='soft-light';const gg=X.createLinearGradient(0,400,0,1920);gg.addColorStop(0,`rgba(120,160,220,${o.frio||.10})`);gg.addColorStop(1,'rgba(255,170,90,.14)');X.fillStyle=gg;X.fillRect(L-300,-300,1680,2500);
 if(!GR27){const c=document.createElement('canvas');c.width=c.height=256;const gx=c.getContext('2d'),d=gx.createImageData(256,256);for(let i=0;i<d.data.length;i+=4){const v=110+rnd(i*.37+3)*145;d.data[i]=d.data[i+1]=d.data[i+2]=v;d.data[i+3]=255}gx.putImageData(d,0,0);GR27=X.createPattern(c,'repeat')}
 X.globalCompositeOperation='overlay';X.globalAlpha=.10;X.fillStyle=GR27;X.fillRect(L-300,-300,1680,2500);X.globalAlpha=1;
 // 4) viñeta y fundido a negro final
 X.globalCompositeOperation='source-over';const v=X.createRadialGradient(L+540,1060,420,L+540,1060,1250);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(2,1,6,.55)');X.fillStyle=v;X.fillRect(L-300,-300,1680,2500);
 const n=negro(t,o);if(n>0){X.fillStyle=`rgba(2,1,4,${n})`;X.fillRect(L-300,-300,1680,2500)}
 X.restore()};

// ======================= PLANO 04 · primera persona: explorador de texturas, mano y mouse =======================
// ---------- texturas procedurales (miniaturas) con caché ----------
const TEX27=new Map();
// v2 · la hoja de textura (UV sheet) del barco: UNA imagen; el visor y la miniatura recortan de ella. Sin letras pintadas:
// el nombre, si estuviera, iría en la parte alta de la franja crema (y 255–345), siempre fuera de lo que muestra el plano 04.
const HOJA27={w:1120,h:1240,franja:[230,420],flot:792,quilla:900,letras:[250,330],margen:15,nombreX:578};const HOJA27m=new Map();
function hoja27(res,testigo){res=res||1;const key=res+'_'+(testigo?1:0);if(HOJA27m.has(key))return HOJA27m.get(key);const W=HOJA27.w,H=HOJA27.h,c=document.createElement('canvas');c.width=Math.round(W*res);c.height=Math.round(H*res);const g=c.getContext('2d'),r=j=>rnd(j*3.17+77);g.scale(res,res);
 for(let y=0;y<H;y+=32)for(let x=0;x<W;x+=32){g.fillStyle=((x+y)/32)%2?'#2b2f38':'#323641';g.fillRect(x,y,32,32)}   // fondo "transparente" de visor
 const casco=()=>{g.beginPath();g.moveTo(60,200);g.lineTo(1112,200);g.bezierCurveTo(1080,520,1000,800,870,878);g.quadraticCurveTo(600,900,300,912);g.lineTo(175,906);g.bezierCurveTo(140,860,118,700,60,200);g.closePath()};
 g.save();casco();g.clip();
 g.fillStyle='#22345a';g.fillRect(0,200,W,30);                                   // franja azul de la borda
 g.fillStyle=(()=>{const gg=g.createLinearGradient(0,230,0,420);gg.addColorStop(0,'#efe6d2');gg.addColorStop(1,'#ddd1b8');return gg})();g.fillRect(0,230,W,190);   // franja crema (la del nombre)
 for(let j=0;j<40;j++){g.fillStyle=`rgba(120,105,80,${.06+.08*r(j)})`;g.fillRect(r(j+1)*W,230+r(j+2)*186,6+r(j+3)*30,2+r(j+4)*4)}
 g.fillStyle='rgba(40,34,26,.55)';g.fillRect(0,418,W,4);
 // plano 06 · el nombre pintado, UNA sola vez (regla 1): mayúsculas de y 250 a 330, misma fuente y azul marino que el barco del plano 10 (regla 7)
 g.save();g.font='800 113px P';g.textAlign='center';g.textBaseline='alphabetic';g.fillStyle='#1d2b47';g.fillText('THE LEONIDA',HOJA27.nombreX,HOJA27.letras[1]);g.restore();
 const ph=46;for(let y=422,f=0;y<HOJA27.flot;y+=ph,f++){g.fillStyle=f%2?'#6f7883':'#78818c';g.fillRect(0,y,W,ph);g.fillStyle='rgba(255,255,255,.07)';g.fillRect(0,y+3,W,ph*.35);
  for(let k=0;k<3;k++){g.strokeStyle=`rgba(40,46,54,${.12+.08*r(f*9+k)})`;g.lineWidth=1.5;g.beginPath();const yy=y+ph*(.25+.22*k);g.moveTo(0,yy);g.bezierCurveTo(W*.3,yy+3,W*.7,yy-3,W,yy+1);g.stroke()}
  g.fillStyle='rgba(18,22,28,.7)';g.fillRect(0,y+ph-3,W,3);const off=(f%2)*240+r(f)*120;for(let x=off;x<W;x+=430){g.fillStyle='rgba(18,22,28,.6)';g.fillRect(x,y,3,ph);[.3,.7].forEach(v=>{g.fillStyle='rgba(36,36,40,.8)';g.beginPath();g.arc(x+12,y+ph*v,3.2,0,7);g.fill()})}
  for(let k=0;k<2;k++){g.fillStyle=`rgba(120,84,52,${.30+.25*r(f*5+k)})`;g.beginPath();g.ellipse(r(f*3+k+20)*W,y+ph*(.3+.4*r(f+k+40)),14+30*r(f+k+60),4+6*r(f+k+70),0,0,7);g.fill()}}
 g.fillStyle='#e9e4d6';g.fillRect(0,HOJA27.flot-4,W,8);                         // línea de flotación
 g.fillStyle='#9b3a2f';g.fillRect(0,HOJA27.flot+4,W,H);for(let j=0;j<60;j++){g.fillStyle=`rgba(60,20,15,${.08+.12*r(j+200)})`;g.fillRect(r(j+201)*W,HOJA27.flot+6+r(j+202)*110,10+r(j+203)*40,2)}
 [300,430,560,690,820].forEach(x=>{g.fillStyle='#b89448';g.beginPath();g.arc(x,470,21,0,7);g.fill();g.fillStyle='#22323f';g.beginPath();g.arc(x,470,14,0,7);g.fill();g.fillStyle='rgba(255,255,255,.35)';g.beginPath();g.arc(x-5,465,5,0,7);g.fill()});
 g.restore();casco();g.strokeStyle='rgba(8,10,14,.85)';g.lineWidth=4;g.stroke();
 g.beginPath();g.moveTo(178,905);g.lineTo(232,906);g.lineTo(220,972);g.lineTo(160,966);g.closePath();g.fillStyle='#8e342b';g.fill();g.strokeStyle='rgba(8,10,14,.85)';g.lineWidth=3;g.stroke();g.fillStyle='#3a3a40';g.fillRect(193,880,6,30);
 // piezas secundarias, más chicas y discretas: cubierta, chimenea, pared de la cabina
 const pieza=(x,y,w,h,pintar)=>{g.save();g.beginPath();g.rect(x,y,w,h);g.clip();pintar();g.restore();g.strokeStyle='rgba(8,10,14,.8)';g.lineWidth=3;g.strokeRect(x,y,w,h)};
 pieza(300,990,360,80,()=>{g.fillStyle='#7a5a3c';g.fillRect(300,990,360,80);for(let y=990;y<1070;y+=16){g.fillStyle='rgba(30,20,12,.5)';g.fillRect(300,y,360,2)}for(let k=0;k<5;k++){g.fillStyle='rgba(30,20,12,.4)';g.fillRect(300+r(k+300)*360,990+Math.floor(r(k+301)*5)*16,2,16)}});
 pieza(80,1010,170,90,()=>{g.fillStyle='#a8372d';g.fillRect(80,1010,170,90);g.fillStyle='#1b1b1f';g.fillRect(80,1010,170,24)});
 pieza(720,975,330,185,()=>{g.fillStyle='#e6dfcf';g.fillRect(720,975,330,185);[750,840,930].forEach(x=>{g.fillStyle='#3a4a5c';g.beginPath();g.roundRect(x,1010,62,56,10);g.fill()});g.strokeStyle='rgba(60,50,40,.45)';g.lineWidth=3;g.strokeRect(1008,1020,30,130)});
 if(testigo){g.fillStyle='rgb(255,0,255)';g.fillRect(0,HOJA27.letras[0],W,HOJA27.letras[1]-HOJA27.letras[0])}   // solo verificación: dónde irían las letras
 if(document.fonts&&!document.fonts.check("800 113px P"))return c;   // sin la fuente todavía: no se guarda, para no fijar una letra equivocada
 HOJA27m.set(key,c);return c}
window.__p27={hoja:()=>hoja27(),HOJA:HOJA27};   // solo lectura, para las verificaciones de la prueba
const CASCO27=(dx,dy,dw,dh)=>{const c=hoja27(),sw=HOJA27.w*.62,sh=sw*dh/dw;X.drawImage(c,(HOJA27.w-sw)/2,HOJA27.h/2-sh/2,sw,sh,dx,dy,dw,dh)};   // miniatura = recorte central de la hoja
function tex27(i,w,h,tipo){const k=i+'_'+w+'_'+h;if(TEX27.has(k))return TEX27.get(k);const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');const r=j=>rnd(i*7.13+j*1.31);
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
 X.font='600 30px P';X.textAlign='left';X.textBaseline='middle';X.fillStyle='#c9cfdb';X.fillText('files  ›  world  ›  textures',L+40,S.y0+36);X.fillStyle='#8a92a3';X.font='500 28px P';X.textAlign='right';X.fillText('2,214 items',L+1040,S.y0+36);
 // barra lateral
 X.fillStyle='#1a1c23';X.fillRect(L+S.x0,S.y0+72,190+(-S.x0),S.y1-S.y0);for(let i=0;i<7;i++){X.fillStyle=i===3?'#3b4252':'#262a33';rr(L+24,S.y0+110+i*82,140,52,8);X.fill()}
 // grilla
 const sc=scroll27(t,o),v=(scroll27(t+1/60,o)-scroll27(t-1/60,o))*30,C=o.cols,top=o.y0,RH=o.fila,TW=o.tw,TH=o.th,k=o.clave,hl=seg(t,tk(o.resalta,a),tk(o.resalta,a)+.25),hov=seg(t,tk(o.cursor[0],a),tk(o.cursor[1],a));
 const clicP=(o.clics||[]).reduce((m,c)=>{const d=t-tk(c,a);return d>=0&&d<.12?Math.max(m,Math.sin(d/.12*Math.PI)):m},0);
 X.save();X.beginPath();X.rect(L+200,S.y0+74,S.x1-200,S.y1-S.y0-74);X.clip();
 const pinta=(dy,al)=>{X.globalAlpha=al;for(let r=0;r<40;r++){const cy=top+r*RH-sc+dy;if(cy<S.y0-RH||cy>S.y1+RH)continue;C.forEach((cx,ci)=>{const i=r*C.length+ci,esK=i===k;let sx=1;if(esK){sx=1+.05*back(hl)-.04*clicP}
    X.save();X.translate(L+cx,cy);X.scale(sx,sx);
    if(esK&&hov>0){X.fillStyle=`rgba(255,255,255,${.07*hov})`;rr(-TW/2-14,-TH/2-14,TW+28,TH+70,12);X.fill()}
    if(esK)CASCO27(-TW/2,-TH/2,TW,TH);else X.drawImage(tex27(i,TW,TH),-TW/2,-TH/2);X.strokeStyle='rgba(0,0,0,.5)';X.lineWidth=2;X.strokeRect(-TW/2,-TH/2,TW,TH);
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
 // dedos apoyados: índice sobre el botón izquierdo (junto a la rueda), medio sobre el derecho; anular y meñique recogidos al costado; pulgar a lo largo del mouse
 const capsula=(x0,y0,x1,y1,w0,w1,uña)=>{const an=Math.atan2(y1-y0,x1-x0),L2=Math.hypot(x1-x0,y1-y0);X.save();X.translate(x0,y0);X.rotate(an);
  X.beginPath();X.moveTo(0,-w0/2);X.lineTo(L2-w1/2,-w1/2);X.arc(L2-w1/2,0,w1/2,-Math.PI/2,Math.PI/2);X.lineTo(0,w0/2);X.closePath();
  X.fillStyle=gl(0,-w0/2,0,w0/2,[[0,p0],[.55,p1],[1,p2]]);X.fill();X.strokeStyle=LIN;X.lineWidth=3.5;X.stroke();
  X.strokeStyle='rgba(120,70,40,.35)';X.lineWidth=2;[.45,.75].forEach(f=>{X.beginPath();X.moveTo(L2*f,-w0*.32);X.quadraticCurveTo(L2*f+3,0,L2*f,w0*.32);X.stroke()});
  if(uña){X.fillStyle='rgba(250,226,212,.9)';X.beginPath();X.ellipse(L2-w1*.55,0,w1*.32,w1*.3,0,0,7);X.fill()}X.restore()};
 capsula(-64,-6,-98,52,34,30,true);                       // pulgar
 capsula(76,-26,98,-74,28,24,true);                       // meñique (más corto, al costado)
 capsula(46,-46,60,-116,31,27,true);                      // anular
 capsula(14,-56,18,-138,33,29,true);                      // medio (botón derecho)
 const ip=rueda+clic*7;capsula(-20,-54,-16,-140+ip,34,30,true);   // índice (rueda y clic)
 X.fillStyle='rgba(255,236,214,.22)';X.beginPath();X.ellipse(4,-30,46,14,-.2,0,7);X.fill();
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
 const pad=lerp(4,0,e),iw=w-pad*2,ih=h-bar-pad*2;CASCO27(L+cx-w/2+pad,cy-h/2+bar+pad,iw,ih);
 {const sh=X.createLinearGradient(0,0,0,560);sh.addColorStop(0,`rgba(6,8,12,${.62*e})`);sh.addColorStop(1,'rgba(6,8,12,0)');X.fillStyle=sh;X.fillRect(L+cx-w/2,Math.max(0,cy-h/2),w,560)}   // sombra arriba: el subtítulo se lee sobre la textura
 X.restore()};

// ---------- utilería (v2): visor que se abre dentro del monitor; la tira del casco es más alta que la ventana ----------
// plano 06 · desplazamiento de la imagen por claves densas [[tiempo, unidades de la hoja], …], interpolación lineal (la curva se calcula en gen06.py)
function despK27(K,t,a){if(t<=tk(K[0][0],a))return K[0][1];for(let i=1;i<K.length;i++){const t1=tk(K[i][0],a);if(t<=t1){const t0=tk(K[i-1][0],a);return lerp(K[i-1][1],K[i][1],(t-t0)/Math.max(1e-6,t1-t0))}}return K[K.length-1][1]}
UTILERIA.p27_visor=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,t0=tk(o.abre,a),q=seg(t,t0,t0+o.dur);if(q<=0)return;const e=eio(q),L=x,S=o.pantalla;
 const [ax,ay,aw,ah]=o.desde,[bx,by,bw,bh]=o.hasta,cx=lerp(ax,bx,e),cy=lerp(ay,by,e),w=lerp(aw,bw,e),h=lerp(ah,bh,e),bar=lerp(16,o.barra||60,e),x0=L+cx-w/2,y0=cy-h/2;
 X.save();X.beginPath();X.rect(L+S.x0,S.y0,S.x1-S.x0,S.y1-S.y0);X.clip();
 X.globalAlpha=Math.min(1,q*6);X.shadowColor='rgba(0,0,0,.65)';X.shadowBlur=44;X.fillStyle='#1c1f27';X.fillRect(x0,y0,w,h);X.shadowBlur=0;
 // contenido: recorte fijo de la hoja (mismo encuadre a cualquier tamaño de ventana)
 const cw=w,ch=h-bar,k=cw/HOJA27.w,dsp=o.despK?despK27(o.despK,t,a):(o.despl?Math.pow(seg(t,tk(o.despl[0],a),tk(o.despl[1],a)),2)*o.despl[2]:0),sy=HOJA27.franja[1]-(o.asoma||50)/(bw/HOJA27.w)-dsp,sh=ch/k,RS=o.res||1;window.__p27v={sy,t};
 X.drawImage(hoja27(RS,o.testigo),0,sy*RS,HOJA27.w*RS,Math.min(sh,HOJA27.h-sy)*RS,x0,y0+bar,cw,Math.min(ch,(HOJA27.h-sy)*k));
 // barra superior con nombre de archivo y controles (minimizar, maximizar, cerrar)
 X.fillStyle='#262a35';X.fillRect(x0,y0,w,bar);X.fillStyle='#343a48';X.fillRect(x0,y0+bar-2,w,2);
 const tx=Math.min(1,Math.max(0,(e-.45)/.4));if(tx>0){X.globalAlpha*=tx;X.font='600 30px P';X.textAlign='left';X.textBaseline='middle';X.fillStyle='#c9cfdb';X.fillText('tex_0412.png',x0+(o.tituloDx!==undefined?o.tituloDx:24),y0+bar/2);
  const bs=bar*.62,yc=y0+bar/2;[[w-bs*3.4,'min'],[w-bs*2.2,'max'],[w-bs*1.0,'cerrar']].forEach(([dx,tp])=>{const bx2=x0+dx;X.strokeStyle=tp==='cerrar'?'#e6e9f0':'#9aa2b2';X.lineWidth=3.5;X.beginPath();
   if(tp==='min'){X.moveTo(bx2-bs*.28,yc+bs*.1);X.lineTo(bx2+bs*.28,yc+bs*.1)}else if(tp==='max'){X.rect(bx2-bs*.26,yc-bs*.26,bs*.52,bs*.52)}else{X.moveTo(bx2-bs*.27,yc-bs*.27);X.lineTo(bx2+bs*.27,yc+bs*.27);X.moveTo(bx2+bs*.27,yc-bs*.27);X.lineTo(bx2-bs*.27,yc+bs*.27)}X.stroke()})}
 X.restore();
 // el cursor queda encima de la ventana (mismo dibujo y posición que en la grilla)
 let cu=o.cur;if(o.curMov){const M=o.curMov;cu=[M[0][1],M[0][2]];
  // 'aproxima': velocidad ∝ t·(1−t)³ (nace en 0, pico al 25 %, se apaga suave hasta 0, un solo movimiento); M[i][4] = arco lateral (px del mundo)
  const aprox=u=>1-Math.pow(1-u,4)*(1+4*u);
  for(let i=1;i<M.length;i++){const k0=tk(M[i-1][0],a),k1=tk(M[i][0],a);if(t>=k0){const u=seg(t,k0,k1),qq=M[i][3]==='aproxima'?aprox(u):(M[i][3]==='sale'?eo:eio)(u);
   let px=lerp(M[i-1][1],M[i][1],qq),py=lerp(M[i-1][2],M[i][2],qq);if(M[i][4]){const dx=M[i][1]-M[i-1][1],dy=M[i][2]-M[i-1][2],dl=Math.hypot(dx,dy)||1,b2=Math.sin(Math.PI*qq)*M[i][4];px+=-dy/dl*b2;py+=dx/dl*b2}cu=[px,py]}}}
 if(cu){X.save();X.translate(L+cu[0],cu[1]);X.scale(1.5,1.5);X.fillStyle='#fff';X.strokeStyle='#111';X.lineWidth=2;X.beginPath();X.moveTo(0,0);X.lineTo(0,34);X.lineTo(9,26);X.lineTo(16,41);X.lineTo(22,38);X.lineTo(15,24);X.lineTo(26,24);X.closePath();X.fill();X.stroke();X.restore()}};

// ---------- utilería: luz de la pantalla sobre la habitación, el escritorio y la mano (sin tocar la pantalla) ----------
UTILERIA.p27_luzPantalla=(x,y,s,t,o)=>{o=o||{};const L=x,S=o.pantalla;X.save();X.beginPath();X.rect(L-300,-300,1680,2500);X.rect(L+S.x0,S.y0,S.x1-S.x0,S.y1-S.y0);X.clip('evenodd');
 X.globalCompositeOperation='multiply';const g=X.createRadialGradient(L+560,980,200,L+560,1100,1250);g.addColorStop(0,'rgb(230,234,246)');g.addColorStop(.55,'rgb(150,156,176)');g.addColorStop(1,'rgb(60,62,78)');X.fillStyle=g;X.fillRect(L-300,-300,1680,2500);
 {const b2=X.createLinearGradient(0,S.y1+120,0,1950);b2.addColorStop(0,'rgb(255,255,255)');b2.addColorStop(1,'rgb(120,122,140)');X.fillStyle=b2;X.fillRect(L-300,S.y1+120,1680,900)}
 X.globalCompositeOperation='lighter';const d=X.createLinearGradient(0,S.y1,0,S.y1+520);d.addColorStop(0,'rgba(150,175,230,.16)');d.addColorStop(1,'rgba(150,175,230,0)');X.fillStyle=d;X.fillRect(L-300,S.y1,1680,520);
 X.restore();X.save();
 X.globalCompositeOperation='overlay';X.globalAlpha=.08;if(o.granoPantalla)X.setTransform(1,0,0,1,0,0);if(!window.__GR27b){const c=document.createElement('canvas');c.width=c.height=256;const gx=c.getContext('2d'),dd=gx.createImageData(256,256);for(let i=0;i<dd.data.length;i+=4){const v=110+rnd(i*.37+11)*145;dd.data[i]=dd.data[i+1]=dd.data[i+2]=v;dd.data[i+3]=255}gx.putImageData(dd,0,0);window.__GR27b=X.createPattern(c,'repeat')}X.fillStyle=window.__GR27b;if(o.granoPantalla)X.fillRect(0,0,1080,1920);else X.fillRect(L-300,-300,1680,2500);
 X.globalAlpha=1;X.globalCompositeOperation='source-over';if(o.granoPantalla){X.restore();X.save();X.beginPath();X.rect(L-300,-300,1680,2500)}const v=X.createRadialGradient(L+540,1000,500,L+540,1000,1300);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(2,2,8,.5)');X.fillStyle=v;X.fillRect(L-300,-300,1680,2500);X.restore()};

})();
// ===== P27 · FIN =====
