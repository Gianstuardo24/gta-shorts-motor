// ===== ESCENARIOS VERTICALES · tanda 2: MDM (1899, fuente de soda, embotelladora, corporativo, 1981), Rabbit (taller, noticias, noche, hangar, investigacion), GTA (casa con palmeras, bar ovni, torre, cuarto gamer, tienda, escenario) + insertos =====
// --- Despacho de 1899: escritorio de persiana, lampara de gas, caja fuerte, calendario, ventana a la calle con farol ---
function calendario(x,y,s,mes,dia,anio,col='#b71c1c'){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-56,-66,120,150);X.fillStyle='#fbf8ef';X.fillRect(-60,-70,120,150);X.fillStyle=col;X.fillRect(-60,-70,120,34);txt(mes,0,-52,20,'#fff',{w:800});txt(String(dia),0,10,58,'#222',{w:800});txt(String(anio),0,58,18,'#555',{w:700});X.fillStyle='#555';X.fillRect(-30,-76,8,14);X.fillRect(22,-76,8,14);X.restore()}
function cajaFuerte(x,y,s){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,110,14,.5);X.fillStyle=gl(-100,0,100,0,[[0,'#1b2a20'],[.5,'#2e4a36'],[1,'#16241a']]);rr(-100,-260,200,260,10);X.fill();X.strokeStyle='#d4af37';X.lineWidth=4;X.strokeRect(-84,-244,168,228);X.fillStyle='#d4af37';X.beginPath();X.arc(0,-140,34,0,7);X.fill();X.fillStyle='#1b2a20';X.beginPath();X.arc(0,-140,24,0,7);X.fill();X.strokeStyle='#d4af37';X.lineWidth=3;for(let i=0;i<12;i++){const a=i*Math.PI/6;X.beginPath();X.moveTo(Math.cos(a)*26,-140+Math.sin(a)*26);X.lineTo(Math.cos(a)*32,-140+Math.sin(a)*32);X.stroke()}
 X.fillRect(50,-150,30,8);txt('1899',0,-210,20,'#d4af37',{w:800});X.restore()}
function lamparaGas(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#8a6a1f';X.fillRect(-4,-40,8,40);X.fillRect(-30,-44,60,8);glow('#ffd27a',30,()=>{X.fillStyle='rgba(255,236,190,.9)';X.beginPath();X.moveTo(-22,-44);X.quadraticCurveTo(-30,-90,0,-110);X.quadraticCurveTo(30,-90,22,-44);X.closePath();X.fill()});X.fillStyle='#ffb300';X.beginPath();X.ellipse(0,-66,5,12+Math.sin(t*12)*1.5,0,0,7);X.fill();X.restore()}
function escritorioPersiana(x,y,s){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,230,18,.5);X.fillStyle=gl(-220,0,220,0,[[0,'#4a2410'],[.5,'#7a3f1c'],[1,'#3e1e0c']]);X.fillRect(-220,-170,440,170);X.fillStyle='#3a1a08';for(let k=0;k<3;k++){X.strokeStyle='rgba(255,210,160,.2)';X.lineWidth=3;X.strokeRect(-200,-150+k*48,120,40);X.strokeRect(80,-150+k*48,120,40);X.fillStyle='#d4af37';X.fillRect(-148,-134+k*48,20,6);X.fillRect(132,-134+k*48,20,6)}
 X.fillStyle='#6b3418';X.fillRect(-236,-186,472,20);X.fillStyle=gl(0,-400,0,-186,[[0,'#5a2c12'],[1,'#7a3f1c']]);X.beginPath();X.moveTo(-220,-186);X.lineTo(-220,-330);X.quadraticCurveTo(0,-420,220,-330);X.lineTo(220,-186);X.closePath();X.fill();
 X.fillStyle='#2a1406';X.fillRect(-190,-320,380,130);for(let i=0;i<8;i++){X.fillStyle='#4a2410';X.fillRect(-180+i*46,-310,40,54);X.fillStyle='#f3ead2';X.fillRect(-172+i*46,-300,24,30)}for(let i=0;i<6;i++){X.fillStyle='#4a2410';X.fillRect(-180+i*61,-250,55,54)}X.restore()}
NUEVOS.despacho1899V={osc:.38,
 luces(z){const F=FV(z);return [{x:F.L+700,y:860,fy:HZ+240,r:380,c:'255,210,130',panel:1},{x:F.L+220,y:760,fy:HZ+220,r:300,c:O(z).hora==='noche'?'140,160,230':'255,235,200',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#6b2a2a',p1:'#4a1a1a',zocalo:'#3e2214',zy:1060,piso:['#5a3a22','#4e321c'],t0:'#1a0f08',t1:'#3a2414',cornisa:'#c9a06a'});
  X.fillStyle='rgba(212,175,55,.14)';for(let r=0;r<6;r++)for(let c=0;c<10;c++){X.beginPath();X.arc(L-60+c*130+(r%2)*65,440+r*110,10,0,7);X.fill()}
  ventanaV(L+80,520,280,420,o.hora||'noche',t,{ciudad:false,marco:'#3e2214',sem:31});X.fillStyle='#2a2a30';X.fillRect(L+240,780,10,160);lamparaGas(L+245,780,1.2,t);
  cortina(L+0,480,90,520,['#2e4a36','#16241a'],-1,t);cortina(L+370,480,90,520,['#2e4a36','#16241a'],1,t);
  calendario(L+560,700,1.2,'JULY',o.dia||'1',o.anio||'1899');cuadroPaisaje(L+720,600,240,160,6);
  escritorioPersiana(L+700,1300,1);lamparaGas(L+560,1114,.9,t);papeles(L+780,1114,5);
  {X.fillStyle='#111';X.fillRect(L+880,1086,40,30);X.fillStyle='#d4af37';X.fillRect(L+884,1080,32,8)}
  cajaFuerte(L+140,1330,1);alfombraPersa(F.cx,1440,900,1800,'#2e4a36','#8a1d22');relojPie(L+1010,1320,.9,t)}};

// --- Fuente de soda de 1890: meson de marmol, taburetes, grifos de soda, frascos de vidrio, espejo, piso de baldosa ---
NUEVOS.fuenteSodaV={osc:.2,
 luces(z){const F=FV(z);return [{x:F.L+300,y:420,fy:HZ+260,r:380,c:'255,230,180',panel:1},{x:F.L+780,y:420,fy:HZ+260,r:380,c:'255,230,180',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#efe6d2',p1:'#dccfb2',piso:['#f2f2f2','#222'],paso:90,linea:'rgba(0,0,0,.1)',t0:'#6b4a2a',t1:'#9a7a52',cornisa:'#7a5230'});
  X.fillStyle='#5a3a1f';X.fillRect(L-120,460,1320,560);X.fillStyle=gl(0,500,0,900,[[0,'#cfd8dc'],[1,'#90a4ae']]);X.fillRect(L-40,500,1160,360);X.fillStyle='rgba(255,255,255,.25)';X.beginPath();X.moveTo(L+40,500);X.lineTo(L+200,500);X.lineTo(L+60,860);X.lineTo(L-40,860);X.closePath();X.fill();
  X.fillStyle='#7a5230';X.fillRect(L-120,880,1320,20);for(let i=0;i<12;i++){const jx=L-20+i*96;X.fillStyle='rgba(230,240,250,.45)';rr(jx,800,60,80,10);X.fill();X.fillStyle=['#ef5350','#ffca28','#8d6e63','#66bb6a'][i%4];X.fillRect(jx+6,830,48,46);X.fillStyle='#455a64';X.fillRect(jx+10,792,40,10)}
  txt('SODA',F.cx,560,70,'#7a1d22',{w:800,g:12,gc:'#fff'});
  {const ty=1130;X.fillStyle=gl(0,ty,0,1300,[[0,'#7a5230'],[1,'#4e321c']]);X.fillRect(L-120,ty,1320,170);for(let i=0;i<6;i++){X.strokeStyle='rgba(255,210,160,.2)';X.lineWidth=3;X.strokeRect(L-90+i*210,ty+24,180,120)}
   X.fillStyle=gl(0,ty-30,0,ty,[[0,'#f5f5f5'],[1,'#cfcfcf']]);X.fillRect(L-130,ty-30,1340,34);X.strokeStyle='rgba(120,120,140,.25)';X.lineWidth=2;for(let i=0;i<20;i++){X.beginPath();X.moveTo(L-130+i*70,ty-30);X.quadraticCurveTo(L-100+i*70,ty-14,L-60+i*70,ty);X.stroke()}
   for(let i=0;i<3;i++){const gx=L+300+i*170;X.fillStyle='#b0bec5';X.fillRect(gx-8,ty-160,16,130);X.beginPath();X.arc(gx,ty-170,18,0,7);X.fill();X.fillRect(gx,ty-130,40,10);X.fillRect(gx+34,ty-130,8,26);X.fillStyle='#d4af37';X.beginPath();X.arc(gx,ty-170,8,0,7);X.fill()}
   for(let i=0;i<3;i++){const vx=L+150+i*330;X.fillStyle='rgba(230,240,250,.55)';X.beginPath();X.moveTo(vx-22,ty-30);X.lineTo(vx+22,ty-30);X.lineTo(vx+28,ty-100);X.lineTo(vx-28,ty-100);X.closePath();X.fill();X.fillStyle='rgba(121,85,72,.8)';X.fillRect(vx-22,ty-80,44,48);X.fillStyle='#e53935';X.fillRect(vx+4,ty-130,4,40)}}
  for(let i=0;i<4;i++){const sx=L+120+i*280;somb(sx,1440,70,12,.45);X.fillStyle='#b0bec5';X.fillRect(sx-6,1300,12,140);X.fillStyle='#78909c';X.beginPath();X.ellipse(sx,1440,50,10,0,0,7);X.fill();X.fillStyle='#c62828';X.beginPath();X.ellipse(sx,1300,56,16,0,0,7);X.fill();X.fillStyle='#e57373';X.beginPath();X.ellipse(sx,1294,52,12,0,0,7);X.fill()}}};

// --- Embotelladora: cinta transportadora con botellas que avanzan, maquina llenadora, cajas de madera ---
function botellaV(x,y,s,lleno=1,col='#6d3b1f'){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(200,230,210,.45)';X.beginPath();X.moveTo(-16,0);X.lineTo(16,0);X.lineTo(16,-60);X.quadraticCurveTo(16,-76,8,-84);X.lineTo(8,-104);X.lineTo(-8,-104);X.lineTo(-8,-84);X.quadraticCurveTo(-16,-76,-16,-60);X.closePath();X.fill();if(lleno>0){X.fillStyle=col;X.fillRect(-14,-60*lleno,28,60*lleno-2)}X.fillStyle='rgba(255,255,255,.4)';X.fillRect(-11,-70,4,60);X.fillStyle='#9e9e9e';X.fillRect(-9,-110,18,8);X.restore()}
NUEVOS.embotelladoraV={osc:.24,
 luces(z){const F=FV(z);return [{x:F.L+540,y:380,fy:HZ+260,r:520,c:'255,236,200',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#b8a88c',p1:'#8f8068',piso:['#7a7a7a','#6e6e6e'],paso:160,t0:'#2a2a2a',t1:'#5a5248',cornisa:'#5a5248'});
  for(let i=0;i<4;i++){X.fillStyle='rgba(255,240,200,.25)';X.fillRect(L-40+i*300,460,180,280);X.strokeStyle='#4a4030';X.lineWidth=8;X.strokeRect(L-40+i*300,460,180,280);X.beginPath();X.moveTo(L+50+i*300,460);X.lineTo(L+50+i*300,740);X.moveTo(L-40+i*300,600);X.lineTo(L+140+i*300,600);X.stroke()}
  {const mx=L+300;X.fillStyle=gl(mx-120,0,mx+120,0,[[0,'#546e7a'],[.5,'#78909c'],[1,'#455a64']]);X.fillRect(mx-140,800,280,330);X.fillStyle='#37474f';X.fillRect(mx-160,780,320,30);for(let k=0;k<4;k++){X.fillStyle='#b0bec5';X.fillRect(mx-110+k*70,1110,16,40+Math.max(0,Math.sin(t*4+k))*20)}X.fillStyle='#ffca28';X.beginPath();X.arc(mx+90,860,18,0,7);X.fill();X.fillStyle='#e53935';X.beginPath();X.arc(mx+90,910,12,0,7);X.fill();
   X.fillStyle='#cfd8dc';X.fillRect(mx-60,740,120,40);X.fillStyle='#6d3b1f';X.fillRect(mx-50,700,100,44)}
  {const by=1200;X.fillStyle='#263238';X.fillRect(L-120,by,1320,30);X.fillStyle='#37474f';X.fillRect(L-120,by+30,1320,20);for(let i=0;i<30;i++){X.fillStyle='#111';X.beginPath();X.arc(L-120+i*46+((t*120)%46),by+40,8,0,7);X.fill()}
   for(let i=0;i<16;i++){const bx=L-120+((i*90+t*120)%1400);const ll=bx>L+300?1:0;botellaV(bx,by,1,ll)}
   for(let i=0;i<3;i++){X.fillStyle='#263238';X.fillRect(L+40+i*400,by+50,16,250)}}
  for(let i=0;i<3;i++){const cx=L+760+(i%2)*150,cy=1500-Math.floor(i/2)*130;X.fillStyle='#a1887f';X.fillRect(cx-120,cy-120,240,120);X.strokeStyle='#6d4c41';X.lineWidth=6;X.strokeRect(cx-120,cy-120,240,120);X.beginPath();X.moveTo(cx-120,cy-60);X.lineTo(cx+120,cy-60);X.stroke();txt('BOTTLES',cx,cy-88,22,'#4e342e',{w:800});for(let k=0;k<6;k++){X.fillStyle='rgba(200,230,210,.6)';X.fillRect(cx-100+k*36,cy-150,14,32)}}}};

// --- Oficina corporativa moderna de noche: ventanal con rascacielos, pantalla gigante con grafico, escritorios de vidrio ---
NUEVOS.corporativoV={osc:.3,
 luces(z){const F=FV(z);return [{x:F.L+540,y:700,fy:HZ+260,r:480,c:'170,200,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),h=o.hora||'noche';
  X.save();X.beginPath();X.rect(L-120,-300,1320,1600);X.clip();cielo(L-120,-300,1320,1600,h,t,41);skyline(L-120,400,1320,900,h,43);X.restore();
  for(let i=0;i<5;i++){X.fillStyle='#1d222c';X.fillRect(L-120+i*300,-300,18,1600)}X.fillStyle='#1d222c';X.fillRect(L-120,360,1320,20);
  {const sx=L+140,sy=520,sw=800,sh=460;X.fillStyle='#0b0f18';rr(sx-14,sy-14,sw+28,sh+28,16);X.fill();X.fillStyle='#101a2c';X.fillRect(sx,sy,sw,sh);X.strokeStyle='rgba(79,195,247,.2)';X.lineWidth=2;for(let i=1;i<6;i++){X.beginPath();X.moveTo(sx,sy+i*sh/6);X.lineTo(sx+sw,sy+i*sh/6);X.stroke()}
   X.strokeStyle=o.col||'#69f0ae';X.lineWidth=6;X.shadowColor=o.col||'#69f0ae';X.shadowBlur=14;X.beginPath();for(let i=0;i<=20;i++){const xx=sx+20+i*(sw-40)/20,yy=sy+sh-40-Math.pow(i/20,2.2)*(sh-90)+Math.sin(i*1.7)*12;i?X.lineTo(xx,yy):X.moveTo(xx,yy)}X.stroke();X.shadowBlur=0;
   txt(o.ticker||'TTWO ▲',sx+120,sy+40,30,o.col||'#69f0ae',{w:800});for(let i=0;i<8;i++){X.fillStyle=i%3?'rgba(105,240,174,.5)':'rgba(255,82,82,.5)';X.fillRect(sx+sw-200,sy+80+i*40,140*rnd(i+5),20)}}
  X.fillStyle='#2a2f3a';X.fillRect(L-120,1300,1320,700);pisoPersp(L-120,L+1200,F.cx,1300,1920,200,['#2a2f3a','#262b35'],'rgba(255,255,255,.04)');
  X.fillStyle='rgba(150,190,255,.08)';X.fillRect(L-120,1300,1320,200);
  {const ty=1240;X.fillStyle='rgba(180,220,255,.25)';X.fillRect(L+60,ty,960,16);X.fillStyle='#1d222c';X.fillRect(L+100,ty+16,12,120);X.fillRect(L+968,ty+16,12,120);
   X.fillStyle='#0d1117';rr(L+200,ty-150,220,140,8);X.fill();X.fillStyle='#1565c0';X.fillRect(L+212,ty-138,196,116);X.fillStyle='#69f0ae';for(let i=0;i<5;i++)X.fillRect(L+226,ty-120+i*20,60+rnd(i)*100,8);X.fillStyle='#0d1117';X.fillRect(L+300,ty-10,20,10);
   X.fillStyle='#fafafa';X.fillRect(L+560,ty-14,140,14);taza2(L+760,ty,'#263238');planta(L+1060,1310,.8)}}};

// --- Oficina pequena de 1981 (startup de software): terminales, cajas de disquetes, pizarra con codigo, cafe ---
NUEVOS.oficina81V={osc:.22,
 luces(z){const F=FV(z);return [{x:F.L+540,y:400,fy:HZ+260,r:460,c:'236,244,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#d6cdb8',p1:'#bfb49a',piso:['#58606c','#515965'],paso:150,t0:'#74777f',t1:'#b7bac1',cornisa:'#ddd6c4',zocalo:'#978f7c',zy:1150});
  glow('#eaf4ff',30,()=>{X.fillStyle='#f6faff';rr(L+390,330,300,26,6);X.fill()});
  {X.fillStyle='#f5f5f0';X.fillRect(L+60,520,440,280);X.strokeStyle='#8d877a';X.lineWidth=10;X.strokeRect(L+60,520,440,280);const cod=['MOV AX,0','INT 21H','CALL DISK','JMP START','; QDOS 0.1'];cod.forEach((c,i)=>txt(c,L+90,570+i*44,24,['#1565c0','#2e7d32','#c62828','#1565c0','#6d4c41'][i],{al:'left',w:700}))}
  ventanaV(L+620,520,380,300,o.hora||'dia',t,{ciudad:true,persiana:true,sem:51});
  {const dx=L+60,ty=1188;X.fillStyle='#4e3a28';X.fillRect(dx,ty+20,960,110);X.fillStyle=gl(0,ty-6,0,ty+22,[[0,'#a5825c'],[.4,'#8a6a4a'],[1,'#5e4630']]);rr(dx-10,ty-4,980,24,4);X.fill();
   terminal80(L+250,ty,1.05,t,{sem:3});terminal80(L+720,ty,1.05,t,{sem:7});cajaDisquetes(L+470,ty);taza2(L+560,ty,'#1e88e5');papeles(L+920,ty,6)}
  sillaOficina(L+320,1400,.75,1);sillaOficina(L+800,1404,.75,-1)}};

// --- Sala de reuniones corporativa de 1981 (madera, mesa, computador beige): para IBM/Microsoft ---
function pcBeige(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,170,14,.4);X.fillStyle=gl(0,-90,0,0,[[0,'#ece6d6'],[1,'#c8c0ac']]);X.fillRect(-160,-90,320,90);X.fillStyle='#2b2b2b';X.fillRect(-140,-70,120,14);X.fillRect(-140,-40,120,14);X.fillStyle='#8a8272';X.fillRect(40,-60,90,8);X.fillStyle='#c62828';X.fillRect(120,-24,10,10);
 X.fillStyle=gl(0,-300,0,-100,[[0,'#ece6d6'],[1,'#d0c8b4']]);rr(-120,-310,240,210,14);X.fill();X.fillStyle='#1d1f1a';rr(-100,-292,200,160,14);X.fill();X.fillStyle='#062a10';rr(-90,-284,180,144,12);X.fill();X.fillStyle='#5dff8a';X.shadowColor='#5dff8a';X.shadowBlur=8;txt('A>',-74,-262,18,'#5dff8a',{al:'left',w:700});X.fillRect(-46,-270,10,(Math.floor(t*2)%2)?14:0);X.shadowBlur=0;X.fillStyle='#d0c8b4';X.fillRect(-60,-100,120,12);
 X.fillStyle='#d8d0bc';X.beginPath();X.moveTo(-150,30);X.lineTo(150,30);X.lineTo(140,8);X.lineTo(-140,8);X.closePath();X.fill();X.restore()}
NUEVOS.salaIBMV={osc:.22,
 luces(z){const F=FV(z);return [{x:F.L+540,y:600,fy:HZ+240,r:460,c:'255,236,205',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#5a3820',p1:'#3e2614',piso:['#1f3a5f','#1b3354'],paso:200,linea:'rgba(0,0,0,.15)',t0:'#1f140c',t1:'#3a2414',cornisa:'#6b4528'});
  for(let i=0;i<5;i++){const px=L-80+i*260;X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=4;X.strokeRect(px,440,220,560);X.strokeStyle='rgba(255,210,160,.12)';X.lineWidth=2;X.strokeRect(px+8,448,204,544)}
  if(o.letrero!==false){X.fillStyle='#1d3b6e';X.fillRect(L+330,500,420,170);for(let i=0;i<8;i++){X.fillStyle='#e3f2fd';X.fillRect(L+350,520+i*18,380,8)}X.fillStyle='rgba(29,59,110,.9)';X.fillRect(L+330,500,420,170);txt(o.letrero||'BOARD ROOM',L+540,585,46,'#e3f2fd',{w:800})}
  cuadroPaisaje(L+60,560,200,140,9);cuadroPaisaje(L+820,560,200,140,12);
  {const ty=1210;somb(F.cx,1380,520,26,.5);X.fillStyle=gl(0,ty-40,0,ty,[[0,'#6b3a1f'],[1,'#4a250f']]);X.beginPath();X.moveTo(L+20,ty);X.lineTo(L+1060,ty);X.lineTo(L+1000,ty-50);X.lineTo(L+80,ty-50);X.closePath();X.fill();X.fillStyle='#3a1c0a';X.fillRect(L+20,ty,1040,24);X.fillStyle='#2a1406';X.fillRect(L+80,ty+24,40,140);X.fillRect(L+960,ty+24,40,140);
   pcBeige(L+540,ty-34,.9,t);papeles(L+220,ty-30,4);papeles(L+850,ty-30,3);X.fillStyle='rgba(220,240,255,.55)';X.fillRect(L+330,ty-80,18,40);X.fillRect(L+730,ty-80,18,40)}}};

// --- Taller / garaje (Rabbit 1990 y GTA): banco de trabajo, panel de herramientas, triangulo de espuma colgando o notas en la pared ---
function trianguloEspuma(x,y,s,t,luces=true){X.save();X.translate(x,y+Math.sin(t*1.3)*4);X.rotate(Math.sin(t*.9)*.03);X.scale(s,s);X.strokeStyle='#bbb';X.lineWidth=2;X.beginPath();X.moveTo(-120,-60);X.lineTo(-40,-260);X.moveTo(120,-60);X.lineTo(40,-260);X.stroke();
 X.fillStyle='#141414';X.beginPath();X.moveTo(0,-110);X.lineTo(170,60);X.lineTo(-170,60);X.closePath();X.fill();X.strokeStyle='#2a2a2a';X.lineWidth=4;X.stroke();if(luces){[[-130,40],[130,40],[0,-70]].forEach(([lx,ly],i)=>{glow('#fff8e1',26,()=>{X.fillStyle='#fffde7';X.beginPath();X.arc(lx,ly,13,0,7);X.fill()})});glow('#ff5252',30,()=>{X.fillStyle='#ff5252';X.beginPath();X.arc(0,20,10+Math.sin(t*6)*2,0,7);X.fill()})}X.restore()}
function panelHerramientas(x,y,w,h){X.fillStyle='#c8a77a';X.fillRect(x,y,w,h);X.fillStyle='rgba(0,0,0,.25)';for(let r=0;r<h/24;r++)for(let c=0;c<w/24;c++){X.beginPath();X.arc(x+12+c*24,y+12+r*24,2.5,0,7);X.fill()}
 X.strokeStyle='#37474f';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(x+60,y+40);X.lineTo(x+60,y+170);X.stroke();X.fillStyle='#c62828';X.fillRect(x+48,y+150,24,60);X.strokeStyle='#546e7a';X.lineWidth=8;X.beginPath();X.moveTo(x+130,y+40);X.lineTo(x+130,y+200);X.stroke();X.beginPath();X.arc(x+130,y+40,18,Math.PI*.2,Math.PI*1.8);X.stroke();
 X.fillStyle='#ffca28';X.fillRect(x+190,y+50,26,130);X.fillStyle='#37474f';X.fillRect(x+194,y+30,18,24);X.strokeStyle='#8d6e63';X.lineWidth=12;X.beginPath();X.moveTo(x+270,y+60);X.lineTo(x+270,y+200);X.stroke();X.fillStyle='#455a64';X.fillRect(x+250,y+40,40,30);
 X.strokeStyle='#e53935';X.lineWidth=6;X.beginPath();X.arc(x+w-80,y+110,50,0,7);X.stroke();X.strokeStyle='#212121';X.lineWidth=4;X.beginPath();X.arc(x+w-80,y+110,36,0,7);X.stroke()}
function notasPared(x,y,t){const N=["I CAN'T LEAVE","WHERE IS THE EXIT?","DAY 412","THIS ISN'T REAL","SAME PALM TREES"];N.forEach((n,i)=>{const nx=x+(i%3)*150+(i>2?70:0),ny=y+Math.floor(i/3)*150;X.save();X.translate(nx,ny);X.rotate((rnd(i+3)-.5)*.25);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-62,-46,130,100);X.fillStyle=i%2?'#fff59d':'#fbf8ef';X.fillRect(-66,-50,130,100);
 const p=n.split(' ');let l1=p.slice(0,Math.ceil(p.length/2)).join(' '),l2=p.slice(Math.ceil(p.length/2)).join(' ');txt(l1,-1,-12,16,'#b71c1c',{w:800});txt(l2,-1,12,16,'#b71c1c',{w:800});X.fillStyle='#d32f2f';X.beginPath();X.arc(0,-44,5,0,7);X.fill();X.restore()});
 X.strokeStyle='rgba(183,28,28,.7)';X.lineWidth=2;X.beginPath();X.moveTo(x,y);X.lineTo(x+300,y+150);X.lineTo(x+150,y);X.stroke()}
NUEVOS.tallerV={osc:.42,
 luces(z){const F=FV(z);return [{x:F.L+540,y:600,fy:HZ+240,r:420,c:'255,226,160',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#6b6e75',p1:'#4c4f56',piso:['#5d5f66','#55575e'],paso:170,t0:'#1d1e22',t1:'#3a3b42',cornisa:'#3a3b42'});
  X.strokeStyle='rgba(0,0,0,.2)';X.lineWidth=4;for(let y=420;y<1280;y+=70){X.beginPath();X.moveTo(L-120,y);X.lineTo(L+1200,y);X.stroke()}
  {X.strokeStyle='#222';X.lineWidth=3;X.beginPath();X.moveTo(F.cx,0);X.lineTo(F.cx,400);X.stroke();X.fillStyle='#333';X.beginPath();X.moveTo(F.cx-70,440);X.lineTo(F.cx-30,400);X.lineTo(F.cx+30,400);X.lineTo(F.cx+70,440);X.closePath();X.fill();glow('#ffe7a8',30,()=>{X.fillStyle='#fff1c8';X.beginPath();X.ellipse(F.cx,440,66,9,0,0,7);X.fill()})}
  if(o.notas){X.fillStyle='#8a7a66';X.fillRect(L+40,520,560,420);notasPared(L+120,620,t);txt('LEONIDA',L+500,560,20,'#3e2723',{w:800})}else panelHerramientas(L+60,520,560,300);
  {const bx=L+60,ty=1160;X.fillStyle='#6d4c2e';X.fillRect(bx,ty,640,28);X.fillStyle='#5a3a22';X.fillRect(bx+20,ty+28,20,130);X.fillRect(bx+600,ty+28,20,130);X.fillRect(bx+20,ty+110,600,14);
   X.fillStyle='#212121';X.fillRect(bx+40,ty-40,90,40);X.fillStyle='#c62828';X.fillRect(bx+40,ty-50,90,12);X.fillStyle='#e0e0e0';X.fillRect(bx+180,ty-12,140,12);X.fillStyle='#1565c0';X.fillRect(bx+360,ty-60,40,60);X.fillStyle='#fdd835';X.beginPath();X.arc(bx+500,ty-20,22,0,7);X.fill();X.fillStyle='#111';X.fillRect(bx+460,ty-6,80,6)}
  if(o.triangulo)trianguloEspuma(L+820,820,1.05,t,true);
  else{X.fillStyle='#455a64';X.fillRect(L+760,520,280,760);X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=3;for(let y=540;y<1280;y+=40){X.beginPath();X.moveTo(L+760,y);X.lineTo(L+1040,y);X.stroke()}X.fillStyle='#263238';X.fillRect(L+760,1240,280,40)}
  {X.fillStyle='#1565c0';rr(L+880,1300,110,150,10);X.fill();X.fillStyle='#0d47a1';X.fillRect(L+880,1300,110,20);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(L+935,1450,60,10,0,0,7);X.fill()}}};

// --- Estudio de noticias de TV (2011): escritorio de presentador, pantallas, camara de estudio, luces ---
NUEVOS.noticiasV={osc:.28,
 luces(z){const F=FV(z);return [{x:F.cx,y:500,fy:HZ+240,r:480,c:'200,225,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  X.fillStyle=gl(0,-300,0,1300,[[0,'#0a1630'],[1,'#13254a']]);X.fillRect(L-120,-300,1320,1600);
  for(let i=0;i<7;i++){X.fillStyle='rgba(79,195,247,.08)';X.fillRect(L-120+i*200,380,8,920)}
  {const sx=L+120,sy=460,sw=840,sh=460;X.fillStyle='#050a18';rr(sx-12,sy-12,sw+24,sh+24,10);X.fill();X.fillStyle=gl(0,sy,0,sy+sh,[[0,'#0d2a55'],[1,'#123a72']]);X.fillRect(sx,sy,sw,sh);X.fillStyle='#000';X.beginPath();X.moveTo(sx+sw/2,sy+80);X.lineTo(sx+sw/2+160,sy+330);X.lineTo(sx+sw/2-160,sy+330);X.closePath();X.fill();[[-120,300],[120,300],[0,140]].forEach(([dx,dy])=>{glow('#fff',14,()=>{X.fillStyle='#fff';X.beginPath();X.arc(sx+sw/2+dx,sy+dy,9,0,7);X.fill()})});
   X.fillStyle='#c62828';X.fillRect(sx,sy+sh-70,sw,70);txt(o.cintillo||'BREAKING: THE UFO PHOTO WAS A HOAX',sx+sw/2,sy+sh-35,28,'#fff',{w:800});X.fillStyle='#fff';X.fillRect(sx+20,sy+20,110,36);txt('LIVE',sx+75,sy+38,22,'#c62828',{w:800})}
  X.fillStyle='#1c2a44';X.fillRect(L-120,1300,1320,700);pisoPersp(L-120,L+1200,F.cx,1300,1920,180,['#1c2a44','#18243b'],'rgba(79,195,247,.12)');
  {const ty=1180;X.fillStyle=gl(0,ty,0,1300,[[0,'#e3f2fd'],[1,'#90caf9']]);X.beginPath();X.moveTo(L+180,ty);X.lineTo(L+900,ty);X.lineTo(L+860,1310);X.lineTo(L+220,1310);X.closePath();X.fill();X.fillStyle='#0d47a1';X.fillRect(L+180,ty-18,720,22);txt('NEWS',F.cx,1250,40,'#0d47a1',{w:800})}
  {const cx=L+1000,cy=1500;X.fillStyle='#212121';X.fillRect(cx-8,cy-260,16,260);X.fillRect(cx-60,cy-20,120,20);X.fillStyle='#37474f';rr(cx-90,cy-360,150,100,10);X.fill();X.fillStyle='#111';X.beginPath();X.arc(cx-100,cy-310,30,0,7);X.fill();X.fillStyle=Math.sin(t*3)>0?'#ff1744':'#5a1a1a';X.beginPath();X.arc(cx+40,cy-350,7,0,7);X.fill()}}};

// --- Noche al aire libre (Rabbit): ciudad o pueblo, montanas opcionales, luces en el cielo (bengalas), triangulo, jets ---
NUEVOS.nocheV={osc:.25,
 luces(z){const F=FV(z),o=O(z);const L=[];if(o.bengalas)for(let i=0;i<5;i++)L.push({x:F.L+180+i*180,y:360,fy:900,r:200,c:'255,200,120',panel:1});else L.push({x:F.L+260,y:1000,fy:HZ+240,r:300,c:'255,196,110',panel:1});return L},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),A=window.__A||0;
  cielo(L-120,-300,1320,1700,'noche',t,o.sem||61);
  if(o.montes){X.fillStyle='#120f1e';X.beginPath();X.moveTo(L-120,1000);for(let i=0;i<=12;i++)X.lineTo(L-120+i*110,860+Math.sin(i*1.7)*70+rnd(i+3)*60);X.lineTo(L+1200,1300);X.lineTo(L-120,1300);X.fill()}
  if(o.bengalas){const k0=o.k?tk(o.k,A):0;for(let i=0;i<5;i++){const fall=Math.max(0,t-k0)*12,by=380+i*0+fall+Math.sin(t+i)*4;if(o.montes&&by>860+Math.sin((i*2)*1.7)*70)continue;glow('#ffd180',40,()=>{X.fillStyle='#fff3e0';X.beginPath();X.arc(L+180+i*180,by,12,0,7);X.fill()});X.strokeStyle='rgba(255,255,255,.15)';X.lineWidth=3;X.beginPath();X.moveTo(L+180+i*180,by-14);X.lineTo(L+180+i*180+Math.sin(t+i)*6,by-120);X.stroke()}}
  if(o.triangulo){X.save();X.translate(F.cx,560);X.scale(.7,.7);X.fillStyle='#050505';X.beginPath();X.moveTo(0,-90);X.lineTo(150,60);X.lineTo(-150,60);X.closePath();X.fill();[[-120,40],[120,40],[0,-60]].forEach(([lx,ly])=>glow('#fff',24,()=>{X.fillStyle='#fff';X.beginPath();X.arc(lx,ly,11,0,7);X.fill()}));glow('#ff1744',24,()=>{X.fillStyle='#ff1744';X.beginPath();X.arc(0,20,9,0,7);X.fill()});X.restore()}
  if(o.jets){for(let i=0;i<2;i++){const jx=L+((t*160+i*500)%1500)-200,jy=420+i*120;X.save();X.translate(jx,jy);X.fillStyle='#2a2f3a';X.beginPath();X.moveTo(-70,0);X.lineTo(60,-6);X.lineTo(80,0);X.lineTo(60,6);X.closePath();X.fill();X.fillRect(-10,-40,26,80);X.fillRect(-64,-18,14,36);X.fillStyle='#444b58';X.beginPath();X.arc(-30,-10,9,0,7);X.arc(-30,10,9,0,7);X.fill();glow('#ff6d00',16,()=>{X.fillStyle='#ffab40';X.beginPath();X.arc(-74,0,4,0,7);X.fill()});X.restore()}}
  if(o.ciudad!==false){for(let i=0;i<12;i++){const bh=120+rnd(i+(o.sem||1))*260,bx=L-120+i*115;X.fillStyle=`rgb(${20+i%3*5},${22+i%4*4},${40+i%3*6})`;X.fillRect(bx,1300-bh,100,bh);for(let r=0;r<bh/26-1;r++)for(let c=0;c<3;c++){if(rnd(i*31+r*7+c)>.5){X.fillStyle='rgba(255,210,130,.85)';X.fillRect(bx+10+c*30,1300-bh+10+r*26,16,12)}}}}
  X.fillStyle='#22232c';X.fillRect(L-120,1300,1320,700);X.fillStyle='#2b2c36';X.fillRect(L-120,1300,1320,90);X.fillStyle='#ffd23f';for(let i=0;i<8;i++)X.fillRect(L-120+i*180,1600,110,12);
  if(o.gente){for(let i=0;i<7;i++){const px=L+60+i*150,py=1420+(i%2)*30;X.fillStyle='#0d0d14';X.beginPath();X.arc(px,py-150,22,0,7);X.fill();rr(px-26,py-126,52,126,18);X.fill();if(i%2){X.save();X.translate(px+20,py-110);X.rotate(-.9);X.fillRect(0,-4,46,9);X.restore()}}}
  {const lx=L+260;X.fillStyle='#0d0f1a';X.fillRect(lx-9,880,18,420);X.fillRect(lx-9,880,70,14);X.fillStyle='#1b1e2e';rr(lx+30,876,60,26,10);X.fill();glow('#ffc46e',40,()=>{X.fillStyle='#ffc46e';X.beginPath();X.ellipse(lx+60,902,24,9,0,0,7);X.fill()})}}};

// --- Hangar militar: aviones de ataque estacionados, banderines, luces altas ---
NUEVOS.hangarV={osc:.3,
 luces(z){const F=FV(z);return [{x:F.L+300,y:420,fy:HZ+260,r:420,c:'235,240,255',panel:1},{x:F.L+800,y:420,fy:HZ+260,r:420,c:'235,240,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  X.fillStyle=gl(0,-300,0,1300,[[0,'#2a2f36'],[1,'#4a525c']]);X.fillRect(L-120,-300,1320,1600);X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=6;for(let i=0;i<14;i++){X.beginPath();X.moveTo(L-120+i*100,-300);X.lineTo(F.cx+(L-120+i*100-F.cx)*1.4,380);X.stroke()}
  [300,800].forEach(s=>{glow('#f5f8ff',30,()=>{X.fillStyle='#fff';X.beginPath();X.ellipse(L+s,400,60,14,0,0,7);X.fill()})});
  X.fillStyle='#d8dee6';X.fillRect(L-20,520,1120,560);X.fillStyle=gl(0,520,0,1080,[[0,'#7fa8d6'],[1,'#d7e6f5']]);X.fillRect(L+20,560,1040,480);X.fillStyle='#c9a96a';X.fillRect(L+20,960,1040,80);X.fillStyle='#8d6e53';X.beginPath();X.moveTo(L+20,960);X.lineTo(L+300,860);X.lineTo(L+520,940);X.lineTo(L+800,880);X.lineTo(L+1060,950);X.lineTo(L+1060,1040);X.lineTo(L+20,1040);X.fill();
  {const ax=F.cx,ay=1280;X.fillStyle='#5f6b5a';X.beginPath();X.moveTo(ax-420,ay-80);X.lineTo(ax+330,ay-96);X.lineTo(ax+420,ay-80);X.lineTo(ax+330,ay-62);X.closePath();X.fill();X.fillStyle='#55604f';X.beginPath();X.moveTo(ax-120,ay-86);X.lineTo(ax+60,ay-86);X.lineTo(ax-20,ay-180);X.lineTo(ax-90,ay-180);X.closePath();X.fill();
   X.fillStyle='#4a5444';[-260,-200].forEach(dx=>{rr(ax+dx-60,ay-150,120,44,20);X.fill()});X.fillRect(ax-380,ay-190,30,110);X.fillRect(ax-400,ay-200,70,20);X.fillStyle='#9fb0c0';X.beginPath();X.ellipse(ax+250,ay-104,50,18,0,0,7);X.fill();X.fillStyle='#2b2b2b';[-80,180].forEach(dx=>{X.fillRect(ax+dx,ay-62,10,40);X.beginPath();X.arc(ax+dx+5,ay-16,18,0,7);X.fill()})}
  X.fillStyle='#4a4f57';X.fillRect(L-120,1300,1320,700);pisoPersp(L-120,L+1200,F.cx,1300,1920,240,['#4a4f57','#454a52'],'rgba(255,214,0,.25)');
  for(let i=0;i<6;i++){X.fillStyle=i%2?'#ffd600':'#212121';X.beginPath();X.moveTo(L-120+i*240,1330);X.lineTo(L-60+i*240,1330);X.lineTo(L-120+i*240+20,1360);X.lineTo(L-180+i*240+20,1360);X.closePath();X.fill()}}};
