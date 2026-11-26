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
})();
// ===== P27 · FIN =====
