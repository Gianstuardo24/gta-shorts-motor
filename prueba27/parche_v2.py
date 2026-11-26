p='p27_bloque.js';s=open(p).read()
def R(a,b):
    global s; assert s.count(a)==1,('NO',a[:70]); s=s.replace(a,b)
def entre(ini,fin,nuevo):
    global s; i=s.index(ini); j=s.index(fin,i); s=s[:i]+nuevo+s[j:]

# (a) B: mancha de humedad en la pared y polvo espeso en la tabla
R("  // telaraña y polvo (solo B)\n  if(B){",
  "  // B: mancha de humedad y pintura gastada en la pared\n  if(B){X.save();X.filter='blur(6px)';[[L+760,300,260,'rgba(70,58,40,.30)'],[L+690,420,170,'rgba(60,50,36,.22)'],[L+180,900,200,'rgba(55,48,40,.18)']].forEach(([mx,my,mr,mc])=>{X.fillStyle=mc;X.beginPath();for(let i=0;i<=20;i++){const an=i/20*7,rr3=mr*(.75+.35*rnd(i+mx*.01));i?X.lineTo(mx+Math.cos(an)*rr3,my+Math.sin(an)*rr3*.8):X.moveTo(mx+Math.cos(an)*rr3,my+Math.sin(an)*rr3*.8)}X.fill()});X.filter='none';X.strokeStyle='rgba(20,14,10,.35)';X.lineWidth=2;X.beginPath();X.moveTo(L+720,200);X.lineTo(L+700,330);X.lineTo(L+735,420);X.lineTo(L+716,520);X.stroke();X.restore()}\n  // telaraña y polvo (solo B)\n  if(B){")
R("if(B){X.fillStyle='rgba(205,200,190,.22)';X.fillRect(L-200,Y-24,1480,9);for(let i=0;i<90;i++)",
  "if(B){X.fillStyle='rgba(205,200,190,.34)';X.fillRect(L-200,Y-24,1480,12);X.fillStyle='rgba(205,200,190,.10)';X.fillRect(L-200,Y,1480,80);for(let i=0;i<160;i++)")

# (b) zona inferior: repisa baja con contenido (A ordenada, B desorden)
entre("  // parte de abajo: puertas (A)"," }};\n",
"""  // parte de abajo: repisa baja con contenido (A ordenada; B desorden, sus cajas son utilería)
  const Y2=Y+300;g=gl(0,Y+114,0,Y2,[[0,'#1d130c'],[1,'#140d08']]);X.fillStyle=g;X.fillRect(L-200,Y+114,1480,Y2-Y-114);
  if(!B){let bx=L+40;const C=['#6b2f2a','#2f4a5e','#7a6236','#3d5a3a','#5a3a52','#7a4a2a','#2e3d52','#6b5a3a','#4a2f2a','#355246'];for(let i=0;i<10;i++){const w=34+rnd(i+20)*20,h=150+rnd(i+30)*60;X.fillStyle=C[i];X.fillRect(bx,Y2-18-h,w,h);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(bx+w-6,Y2-18-h,6,h);X.fillStyle='rgba(230,200,120,.55)';X.fillRect(bx+4,Y2-18-h+22,w-8,4);X.fillRect(bx+4,Y2-18-28,w-8,4);bx+=w+3}
   X.fillStyle=gl(0,Y2-190,0,Y2,[[0,'#9a7a54'],[1,'#7f6243']]);X.fillRect(L+640,Y2-18-170,260,170);X.fillStyle='rgba(240,232,212,.9)';X.fillRect(L+700,Y2-130,140,46);X.strokeStyle='rgba(60,50,40,.6)';X.lineWidth=3;[0,1].forEach(i=>{X.beginPath();X.moveTo(L+712,Y2-116+i*16);X.lineTo(L+790+i*20,Y2-116+i*16);X.stroke()});X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L+640,Y2-188,260,14)}
  else{[[L+120,Y2-30],[L+700,Y2-26],[L+430,Y2-24]].forEach(([px,py],i)=>{X.fillStyle=`rgba(205,198,182,${.55-.1*i})`;X.beginPath();for(let k=0;k<=12;k++){const an=k/12*7,r4=26*(0.7+.5*rnd(k+i*13));k?X.lineTo(px+Math.cos(an)*r4,py+Math.sin(an)*r4*.75):X.moveTo(px+Math.cos(an)*r4,py+Math.sin(an)*r4*.75)}X.fill()})}
  X.fillStyle=gl(0,Y2-18,0,Y2,[[0,B?'#5e4c3b':'#6e4c30'],[1,'#4a3220']]);X.fillRect(L-200,Y2-18,1480,18);X.fillStyle=gl(0,Y2,0,Y2+64,[[0,'#56391f'],[1,'#2a1a0e']]);X.fillRect(L-200,Y2,1480,64);X.fillStyle='rgba(255,226,180,.18)';X.fillRect(L-200,Y2,1480,2);
  if(B){X.fillStyle='rgba(205,200,190,.28)';X.fillRect(L-200,Y2-18,1480,8)}
  X.fillStyle='rgba(0,0,0,.6)';X.fillRect(L-200,Y2+64,1480,40);X.fillStyle='#0b0705';X.fillRect(L-200,Y2+104,1480,700);
""")

# (c) mano nueva: toma el barco por la popa (pulgar sobre la borda, índice en la punta), sin tapar cabina, chimenea, mástil ni nombre
entre("// ---------- utilería: mano que deja el objeto","// ---------- utilería: caja de cartón",
r"""// ---------- utilería: mano que toma el barco por la popa (pulgar sobre la borda, índice en la punta) ----------
// Mismo lenguaje que el barco: contorno marrón oscuro de 4 px, degradado con luz desde la derecha (la lámpara).
UTILERIA.p27_mano=(x,y,s,t,o)=>{o=o||{};const a=window.__A||0,ab=o.suelta?eio(seg(t,tk(o.suelta[0],a),tk(o.suelta[1],a))):0;X.save();X.translate(x,y);X.scale(s,s);
 const LIN='rgba(42,28,18,.85)',p0='#f1c29b',p1='#dca37b',p2='#b77c56',dx=-.94,dy=-.34;X.lineJoin='round';X.lineCap='round';
 // sombra de contacto sobre el casco
 X.save();X.globalAlpha*=.30*(1-ab);const sh=X.createRadialGradient(14,-34,2,14,-34,46);sh.addColorStop(0,'rgba(20,10,5,1)');sh.addColorStop(1,'rgba(20,10,5,0)');X.fillStyle=sh;X.beginPath();X.arc(14,-34,46,0,7);X.fill();X.restore();
 // antebrazo y manga (desde la muñeca hacia la izquierda, apenas hacia arriba)
 X.save();X.translate(-88,-6);X.rotate(Math.atan2(dy,dx));
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

""")

# (d) primer plano desenfocado, tela con polvo y telaraña del mástil
R("// ---------- utilería: pelusa de polvo que cae ----------",
r"""// ---------- utilería: primer plano desenfocado (borde de mesa con objetos) ----------
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

// ---------- utilería: pelusa de polvo que cae ----------""")

# (e) pelusa más grande y con más contraste (con un leve halo para el teléfono)
R("for(let i=0;i<14;i++){const r=6+rnd(i+2)*14;X.fillStyle=`rgba(225,222,215,${.20+.18*rnd(i)})`;",
  "{const hg=X.createRadialGradient(0,0,0,0,0,46*s);hg.addColorStop(0,'rgba(255,248,232,.28)');hg.addColorStop(1,'rgba(255,248,232,0)');X.fillStyle=hg;X.beginPath();X.arc(0,0,46*s,0,7);X.fill()}\n for(let i=0;i<18;i++){const r=6+rnd(i+2)*14;X.fillStyle=`rgba(240,238,230,${.45+.3*rnd(i)})`;")
R("X.strokeStyle='rgba(235,232,225,.35)';X.lineWidth=1.4;for(let i=0;i<8;i++)","X.strokeStyle='rgba(245,242,235,.7)';X.lineWidth=1.8;for(let i=0;i<12;i++)")

# (f) aire con polvo (velo) opcional en la luz
R(" // 3) relleno frío del cuarto (B)"," if(o.bruma){X.globalCompositeOperation='screen';X.fillStyle=`rgba(150,148,140,${o.bruma})`;X.fillRect(L-300,-300,1680,2500)}\n // 3) relleno frío del cuarto (B)")
open(p,'w').write(s);print('parche aplicado')
