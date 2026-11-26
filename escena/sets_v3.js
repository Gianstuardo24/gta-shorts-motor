// ===== ESCENARIOS VERTICALES · tanda 3: GTA (casa con palmeras, bar ovni, torre, cuarto gamer, tienda, escenario), gatos (cafe de gatos), parque, investigacion + INSERTOS (vitrinaV, mesaCenitalV) y objetos protagonistas =====
function palmeraV(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle='#6b4a2e';X.lineWidth=22;X.lineCap='round';X.beginPath();X.moveTo(0,0);X.quadraticCurveTo(30,-260,10,-520);X.stroke();X.strokeStyle='rgba(0,0,0,.2)';X.lineWidth=3;for(let i=0;i<14;i++){const yy=-i*36;X.beginPath();X.moveTo(-10+i*1.5,yy);X.lineTo(12+i*1.5,yy-6);X.stroke()}
 for(let i=0;i<8;i++){const a=-Math.PI/2+(i-3.5)*.42+Math.sin(t*1.2+i)*.04;X.save();X.translate(10,-520);X.rotate(a);X.fillStyle=i%2?'#2e7d32':'#388e3c';X.beginPath();X.moveTo(0,0);X.quadraticCurveTo(120,-50,230,30);X.quadraticCurveTo(120,-10,0,10);X.closePath();X.fill();X.restore()}X.restore()}
NUEVOS.casaPalmasV={osc:.18,
 luces(z){const F=FV(z),h=O(z).hora||'tarde';return [{x:F.L+540,y:200,fy:HZ+200,r:520,c:h==='noche'?'150,170,255':'255,210,160',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),h=o.hora||'tarde';
  cielo(L-120,-300,1320,1610,h,t,71);if(o.sinCasa){X.fillStyle=h==='noche'?'#1a1a2e':'#7a8fa6';X.beginPath();X.moveTo(L-120,1150);for(let i=0;i<=8;i++)X.lineTo(L-120+i*165,1080-Math.sin(i*1.9)*50);X.lineTo(L+1200,1300);X.lineTo(L-120,1300);X.fill();for(let i=0;i<6;i++){const hx=L-100+i*230;X.fillStyle=['#e8d5b5','#d9c4a0','#f0e0c8'][i%3];X.fillRect(hx,1180,170,120);X.fillStyle='#c0623a';X.beginPath();X.moveTo(hx-10,1180);X.lineTo(hx+85,1130);X.lineTo(hx+180,1180);X.fill()}X.fillStyle='#43a047';for(let i=0;i<14;i++){X.beginPath();X.arc(L-120+i*100,1290,40,Math.PI,0);X.fill()}}X.fillStyle=h==='noche'?'#111':'rgba(255,180,120,.25)';X.beginPath();X.arc(L+800,560,90,0,7);X.fill();
  if(!o.sinCasa){const hx=L+120,hy=1300;X.fillStyle='#e8d5b5';X.fillRect(hx,hy-480,820,480);X.fillStyle='#c0623a';X.beginPath();X.moveTo(hx-40,hy-480);X.lineTo(hx+410,hy-640);X.lineTo(hx+860,hy-480);X.closePath();X.fill();X.strokeStyle='rgba(0,0,0,.2)';X.lineWidth=3;for(let i=0;i<10;i++){X.beginPath();X.moveTo(hx-20+i*90,hy-480);X.lineTo(hx+410,hy-630);X.stroke()}
   X.fillStyle='#bfc3c8';X.fillRect(hx+60,hy-300,360,300);X.strokeStyle='rgba(0,0,0,.25)';X.lineWidth=4;for(let i=1;i<6;i++){X.beginPath();X.moveTo(hx+60,hy-300+i*50);X.lineTo(hx+420,hy-300+i*50);X.stroke()}
   X.fillStyle='#5d4037';X.fillRect(hx+520,hy-260,110,260);X.fillStyle='#d4af37';X.beginPath();X.arc(hx+610,hy-130,6,0,7);X.fill();
   for(const wx of [hx+90,hx+680]){X.fillStyle=h==='noche'?'rgba(255,210,120,.9)':'#8fc3e8';X.fillRect(wx,hy-430,110,90);X.strokeStyle='#fff';X.lineWidth=6;X.strokeRect(wx,hy-430,110,90)}
   X.fillStyle='#455a64';X.fillRect(hx+680,hy-90,100,90);txt('BELVILLE',hx+410,hy-360,26,'#7a4a2a',{w:800})}
  palmeraV(L+40,1310,1.2,t);palmeraV(L+1020,1320,1.1,t);
  X.fillStyle='#8a8f98';X.fillRect(L-120,1300,1320,120);X.fillStyle='#3a3d45';X.fillRect(L-120,1420,1320,600);X.fillStyle='#fdd835';for(let i=0;i<8;i++)X.fillRect(L-120+i*180,1680,110,12);
  X.fillStyle='#43a047';X.fillRect(L-120,1290,1320,16)}};
NUEVOS.barOvniV={osc:.45,
 luces(z){const F=FV(z);return [{x:F.L+300,y:700,fy:HZ+240,r:340,c:'0,229,255',panel:1},{x:F.L+800,y:700,fy:HZ+240,r:340,c:'255,45,149',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#1a1030',p1:'#0d0820',piso:['#1d1430','#18102a'],paso:120,t0:'#06030c',t1:'#120a22',cornisa:'#2a1a44'});
  glow('#00e5ff',40,()=>{X.strokeStyle='#00e5ff';X.lineWidth=10;X.beginPath();X.ellipse(F.cx,560,220,50,0,0,7);X.stroke();X.beginPath();X.arc(F.cx,530,90,Math.PI,0);X.stroke()});txt('UFO BAR',F.cx,660,60,'#ff2d95',{w:800,g:30,gc:'#ff2d95'});
  {const fx=L+380,fy=760,fw=320,fh=230;X.fillStyle='#3e2723';X.fillRect(fx-16,fy-16,fw+32,fh+32);X.fillStyle='#f5ecd8';X.fillRect(fx,fy,fw,fh);X.save();X.beginPath();X.rect(fx+14,fy+14,fw-28,fh-28);X.clip();X.fillStyle=gl(0,fy,0,fy+fh,[[0,'#ffb37a'],[1,'#ffe0b2']]);X.fillRect(fx,fy,fw,fh);
   X.fillStyle='#e8d5b5';X.fillRect(fx+60,fy+110,200,110);X.fillStyle='#c0623a';X.beginPath();X.moveTo(fx+50,fy+110);X.lineTo(fx+160,fy+70);X.lineTo(fx+270,fy+110);X.closePath();X.fill();X.fillStyle='#bfc3c8';X.fillRect(fx+80,fy+150,90,70);palmeraV(fx+40,fy+220,.3,t);palmeraV(fx+290,fy+220,.28,t);X.restore()}
  if(o.foco){const p=.5+.5*Math.sin(t*5);X.strokeStyle=`rgba(255,235,59,${p})`;X.lineWidth=6;X.strokeRect(L+350,730,380,290)}
  for(let i=0;i<10;i++){X.fillStyle=['#7b1fa2','#1565c0','#00838f','#ad1457'][i%4];X.fillRect(L+60+i*100,1060,60,26)}X.fillStyle='#4a148c';X.fillRect(L-120,1080,1320,20);
  {const ty=1180;X.fillStyle=gl(0,ty,0,1300,[[0,'#2a1a44'],[1,'#120a22']]);X.fillRect(L-120,ty,1320,120);X.fillStyle='#00e5ff';X.fillRect(L-120,ty-8,1320,8);for(let i=0;i<5;i++){const gx=L+80+i*220;X.fillStyle='rgba(200,230,255,.5)';X.fillRect(gx,ty-60,30,52);X.fillStyle=['#76ff03','#ff4081','#ffd740','#18ffff','#ea80fc'][i];X.fillRect(gx+2,ty-36,26,28)}}
  for(let i=0;i<4;i++){const sx=L+120+i*280;X.fillStyle='#b0bec5';X.fillRect(sx-6,1310,12,140);X.fillStyle='#ff2d95';X.beginPath();X.ellipse(sx,1310,54,15,0,0,7);X.fill()}}};
NUEVOS.torreV={osc:.15,
 luces(z){const F=FV(z);return [{x:F.L+540,y:200,fy:HZ+200,r:540,c:'255,220,170',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),cima=o.cima;
  cielo(L-120,-300,1320,2300,o.hora||'tarde',t,81);
  if(cima){for(let i=0;i<7;i++){X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.ellipse(L+((i*230+t*12)%1400)-120,1500+i*40,140,30,0,0,7);X.fill()}
   X.fillStyle='#3a3d45';X.fillRect(L-120,1600,1320,40);for(let i=0;i<10;i++){X.strokeStyle='#c62828';X.lineWidth=12;X.beginPath();X.moveTo(L-120+i*140,1640);X.lineTo(L-50+i*140,1920);X.stroke();X.strokeStyle='#eceff1';X.beginPath();X.moveTo(L-50+i*140,1640);X.lineTo(L-120+i*140,1920);X.stroke()}
   X.fillStyle='#c62828';X.fillRect(F.cx-20,300,40,1300);for(let k=0;k<6;k++){X.fillStyle=k%2?'#eceff1':'#c62828';X.fillRect(F.cx-20,300+k*216,40,216)}glow('#ff1744',30,()=>{X.fillStyle=Math.sin(t*4)>0?'#ff1744':'#5a1010';X.beginPath();X.arc(F.cx,290,18,0,7);X.fill()})}
  else{X.fillStyle='#6b8a5a';X.beginPath();X.moveTo(L-120,1100);for(let i=0;i<=10;i++)X.lineTo(L-120+i*132,1060-Math.sin(i*1.3)*60);X.lineTo(L+1200,1300);X.lineTo(L-120,1300);X.fill();
   const tx=o.sinTorre?L+99999:L+700;X.strokeStyle='#c62828';X.lineWidth=8;X.beginPath();X.moveTo(tx-150,1300);X.lineTo(tx-10,140);X.lineTo(tx+10,140);X.lineTo(tx+150,1300);X.stroke();for(let i=0;i<18;i++){const yy=1300-i*64,w=150-i*8;X.strokeStyle=i%2?'#eceff1':'#c62828';X.lineWidth=5;X.beginPath();X.moveTo(tx-w,yy);X.lineTo(tx+w-8,yy-64);X.moveTo(tx+w,yy);X.lineTo(tx-w+8,yy-64);X.stroke()}
   glow('#ff1744',30,()=>{X.fillStyle=Math.sin(t*4)>0?'#ff1744':'#5a1010';X.beginPath();X.arc(tx,130,16,0,7);X.fill()});palmeraV(L+120,1320,1,t);
   X.fillStyle='#3a3d45';X.fillRect(L-120,1300,1320,700);X.fillStyle='#fdd835';for(let i=0;i<8;i++)X.fillRect(L-120+i*180,1640,110,12)}}};
NUEVOS.cuartoGamerV={osc:.4,
 luces(z){const F=FV(z);return [{x:F.L+540,y:900,fy:HZ+240,r:420,c:'120,160,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),viejo=o.era==='2013';
  cuartoV(F,{p0:viejo?'#3a3550':'#1c1a2e',p1:viejo?'#2a2540':'#120f20',piso:['#2a2438','#241f31'],paso:130,t0:'#0b0912',t1:'#1a1626',cornisa:'#2a2540'});
  if(!viejo){X.strokeStyle='#ff2d95';X.lineWidth=6;X.shadowColor='#ff2d95';X.shadowBlur=20;X.beginPath();X.moveTo(L-120,420);X.lineTo(L+1200,420);X.stroke();X.strokeStyle='#00e5ff';X.shadowColor='#00e5ff';X.beginPath();X.moveTo(L-120,1270);X.lineTo(L+1200,1270);X.stroke();X.shadowBlur=0}
  for(let i=0;i<3;i++){const px=L+80+i*330;X.fillStyle='#111';X.fillRect(px,500,240,330);X.fillStyle=['#7b1fa2','#00838f','#c62828'][i];X.fillRect(px+14,514,212,302);txt(['LEVEL UP','PLAY','GAME OVER'][i],px+120,665,30,'#fff',{w:800})}
  {const tx=F.cx,ty=1170;X.fillStyle='#111';X.fillRect(tx-420,ty,840,24);X.fillStyle='#1d1d1d';X.fillRect(tx-400,ty+24,30,110);X.fillRect(tx+370,ty+24,30,110);
   if(viejo){X.fillStyle='#d0c8b4';rr(tx-260,ty-260,520,250,20);X.fill();X.fillStyle='#111';rr(tx-230,ty-240,460,210,30);X.fill();X.fillStyle='#16324a';rr(tx-214,ty-226,428,182,26);X.fill();txt('2013',tx,ty-136,60,'#4fc3f7',{w:800})}
   else{X.fillStyle='#0d0d0d';X.fillRect(tx-330,ty-300,660,280);X.fillStyle=gl(tx-310,0,tx+310,0,[[0,'#ff6f00'],[.5,'#ff2d95'],[1,'#7c4dff']]);X.fillRect(tx-316,ty-288,632,256);X.fillStyle='#111';X.fillRect(tx-12,ty-20,24,20)}
   X.fillStyle='#212121';rr(tx+180,ty-24,120,24,8);X.fill();X.fillStyle='#e0e0e0';X.fillRect(tx-300,ty-8,90,8)}
  {const sx=F.cx,sy=1470;X.fillStyle='#c62828';rr(sx-120,sy-260,240,240,40);X.fill();X.fillStyle='#212121';rr(sx-140,sy-40,280,40,16);X.fill();X.fillRect(sx-8,sy,16,60);X.fillRect(sx-80,sy+60,160,12)}}};
NUEVOS.tiendaJuegosV={osc:.38,
 luces(z){const F=FV(z);return [{x:F.L+540,y:620,fy:HZ+240,r:460,c:'255,45,149',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cielo(L-120,-300,1320,900,'noche',t,91);skyline(L-120,0,1320,500,'noche',93);
  X.fillStyle='#1a1426';X.fillRect(L-120,380,1320,920);glow('#ff2d95',40,()=>{X.strokeStyle='#ff2d95';X.lineWidth=10;rr(L+140,420,800,120,20);X.stroke()});txt('GAME STORE',F.cx,482,64,'#fff',{w:800,g:24,gc:'#ff2d95'});
  {X.fillStyle='rgba(120,200,255,.18)';X.fillRect(L+40,600,1000,620);for(let r=0;r<4;r++){X.fillStyle='#2a2438';X.fillRect(L+60,700+r*140,960,12);for(let c=0;c<14;c++){X.fillStyle=['#e53935','#1e88e5','#43a047','#fb8c00','#8e24aa','#00acc1'][(c+r)%6];X.fillRect(L+70+c*68,620+r*140,54,80);X.fillStyle='rgba(255,255,255,.3)';X.fillRect(L+70+c*68,620+r*140,54,8)}}
   X.strokeStyle='#3a3050';X.lineWidth=14;X.strokeRect(L+40,600,1000,620);X.beginPath();X.moveTo(F.cx,600);X.lineTo(F.cx,1220);X.stroke();X.fillStyle='rgba(255,255,255,.07)';X.beginPath();X.moveTo(L+60,600);X.lineTo(L+300,600);X.lineTo(L+60,1000);X.closePath();X.fill()}
  X.fillStyle='#fdd835';X.fillRect(L+700,1080,260,90);txt('SOLD OUT',L+830,1125,34,'#c62828',{w:800});
  X.fillStyle='#2b2c36';X.fillRect(L-120,1300,1320,700);X.fillStyle='#34353f';X.fillRect(L-120,1300,1320,110)}};
NUEVOS.escenarioV={osc:.4,
 luces(z){const F=FV(z);return [{x:F.cx,y:380,fy:HZ+240,r:500,c:'255,220,140',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  X.fillStyle='#0b0612';X.fillRect(L-120,-300,1320,1700);
  for(let i=0;i<8;i++){const cx=L-60+i*170;X.fillStyle=gl(cx,0,cx+170,0,[[0,'#5a0f1e'],[.5,'#9a1b2f'],[1,'#5a0f1e']]);X.fillRect(cx,380,170,920)}
  X.fillStyle='#d4af37';X.fillRect(L-120,370,1320,20);X.fillStyle='#7a1d22';X.beginPath();X.moveTo(L-120,390);for(let i=0;i<=11;i++)X.quadraticCurveTo(L-60+i*120,500,L+i*120,390);X.lineTo(L+1200,390);X.fill();
  X.save();X.globalCompositeOperation='lighter';for(let i=0;i<5;i++){const lx=L+60+i*240,g=X.createLinearGradient(lx,380,lx+(F.cx-lx)*.3,1300);g.addColorStop(0,'rgba(255,230,160,.25)');g.addColorStop(1,'rgba(255,230,160,0)');X.fillStyle=g;X.beginPath();X.moveTo(lx-20,380);X.lineTo(lx+20,380);X.lineTo(lx+(F.cx-lx)*.3+160,1300);X.lineTo(lx+(F.cx-lx)*.3-160,1300);X.closePath();X.fill()}X.restore();
  for(let i=0;i<40;i++){const cx=L+rnd(i)*1080,cy=((rnd(i*3)*1300+t*90*(rnd(i+5)+.4))%1300);X.fillStyle=['#ffd740','#ff4081','#18ffff','#69f0ae'][i%4];X.save();X.translate(cx,cy);X.rotate(t*3+i);X.fillRect(-6,-3,12,6);X.restore()}
  X.fillStyle='#2a1a30';X.fillRect(L-120,1300,1320,700);X.fillStyle=gl(0,1300,0,1360,[[0,'#d4af37'],[1,'#8a6d1f']]);X.fillRect(L-120,1300,1320,24);
  for(let r=0;r<3;r++)for(let i=0;i<14;i++){X.fillStyle=`rgba(10,6,20,${.9-r*.1})`;X.beginPath();X.arc(L-80+i*90+(r%2)*45,1760+r*80,34,0,7);X.fill();rr(L-120+i*90+(r%2)*45,1780+r*80,80,140,30);X.fill()}}};
NUEVOS.cafeGatosV={osc:.18,
 luces(z){const F=FV(z);return [{x:F.L+540,y:420,fy:HZ+260,r:480,c:'255,226,190',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#f6e3d0',p1:'#e8c9aa',piso:['#c49a6c','#b88e62'],paso:120,t0:'#7a5a40',t1:'#b08a66',cornisa:'#fff'});
  X.fillStyle='#e57373';X.fillRect(L+180,440,720,100);txt('CAT CAFE',F.cx,492,56,'#fff',{w:800});
  for(let i=0;i<3;i++){const sx=L+60+i*360;X.fillStyle='#8d6e63';X.fillRect(sx,640,260,14);X.fillStyle='#a1887f';X.fillRect(sx+20,600,40,40);X.fillStyle='#4fc3f7';X.beginPath();X.arc(sx+190,624,20,0,7);X.fill()}
  {const tx=L+120;X.fillStyle='#d7ccc8';X.fillRect(tx-10,760,40,540);X.fillStyle='#bcaaa4';for(let k=0;k<3;k++){rr(tx-80,780+k*170,180,40,16);X.fill()}X.fillStyle='#a1887f';rr(tx-60,1220,180,80,20);X.fill();X.fillStyle='#ef5350';X.beginPath();X.arc(tx+90,1140,14,0,7);X.fill();X.strokeStyle='#ef5350';X.lineWidth=2;X.beginPath();X.moveTo(tx+90,1126);X.lineTo(tx+90,960);X.stroke()}
  ventanaV(L+380,700,320,300,'dia',t,{arbol:true,sem:13});
  {const ty=1200;X.fillStyle='#fafafa';X.beginPath();X.ellipse(L+840,ty,160,26,0,0,7);X.fill();X.fillStyle='#8d6e63';X.fillRect(L+830,ty,20,100);taza2(L+790,ty-4,'#ef9a9a');taza2(L+880,ty-4,'#90caf9');X.fillStyle='#ffe082';X.beginPath();X.ellipse(L+840,ty-14,40,10,0,0,7);X.fill()}
  for(let i=0;i<5;i++){X.fillStyle=['#ffb74d','#81c784','#64b5f6','#f06292','#ba68c8'][i];X.beginPath();X.ellipse(L+180+i*190,1420+(i%2)*60,60,22,0,0,7);X.fill()}}};
NUEVOS.parqueV={osc:.1,
 luces(z){const F=FV(z);return [{x:F.L+700,y:200,fy:HZ+200,r:560,c:'255,244,214',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cielo(L-120,-300,1320,1400,o.hora||'dia',t,101);for(let i=0;i<4;i++){X.fillStyle='rgba(255,255,255,.8)';const cx=L+((i*330+t*10)%1400)-120;X.beginPath();X.arc(cx,320+i*60,50,0,7);X.arc(cx+50,300+i*60,60,0,7);X.arc(cx+110,320+i*60,46,0,7);X.fill()}
  X.fillStyle='#7cb342';X.beginPath();X.moveTo(L-120,1050);X.quadraticCurveTo(F.cx,950,L+1200,1060);X.lineTo(L+1200,1300);X.lineTo(L-120,1300);X.fill();
  for(let i=0;i<5;i++){const tx=L-40+i*270,th=320+rnd(i)*120;X.fillStyle='#5d4037';X.fillRect(tx-14,1180-th*.4,28,th*.4+40);X.fillStyle=i%2?'#388e3c':'#43a047';X.beginPath();X.arc(tx,1180-th*.55,110,0,7);X.arc(tx-70,1180-th*.4,80,0,7);X.arc(tx+70,1180-th*.42,84,0,7);X.fill()}
  X.fillStyle='#8bc34a';X.fillRect(L-120,1300,1320,700);for(let i=0;i<260;i++){X.fillStyle=i%2?'#7cb342':'#9ccc65';const gx=L-120+rnd(i)*1320,gy=1300+rnd(i*7)*620;X.fillRect(gx,gy,4,12+rnd(i+1)*10)}
  X.fillStyle='#d7b98a';X.beginPath();X.moveTo(F.cx-120,1300);X.lineTo(F.cx+120,1300);X.lineTo(F.cx+400,1920);X.lineTo(F.cx-400,1920);X.closePath();X.fill();
  {const bx=L+880,by=1300;X.fillStyle='#6d4c41';X.fillRect(bx-120,by-80,240,18);X.fillRect(bx-120,by-130,240,14);X.fillStyle='#37474f';X.fillRect(bx-110,by-62,12,62);X.fillRect(bx+98,by-62,12,62)}
  X.strokeStyle='#eceff1';X.lineWidth=6;for(let i=0;i<10;i++){X.beginPath();X.moveTo(L-100+i*60,1240);X.lineTo(L-100+i*60,1310);X.stroke()}X.beginPath();X.moveTo(L-120,1260);X.lineTo(L+460,1260);X.stroke()}};
NUEVOS.investigaV={osc:.38,
 luces(z){const F=FV(z);return [{x:F.L+540,y:1050,fy:HZ+220,r:420,c:'255,240,210',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#3a4250',p1:'#262c36',piso:['#3b3f47','#363a42'],paso:160,t0:'#0f1216',t1:'#20252d',cornisa:'#2a2f38'});
  {X.fillStyle='#ece4d0';X.fillRect(L+60,480,960,520);X.strokeStyle='#5d4037';X.lineWidth=12;X.strokeRect(L+60,480,960,520);
   for(let i=0;i<6;i++){const px=L+110+(i%3)*300,py=520+Math.floor(i/3)*240;X.save();X.translate(px+110,py+90);X.rotate((rnd(i+1)-.5)*.12);X.fillStyle='#fff';X.fillRect(-110,-90,220,180);X.fillStyle='#0c1428';X.fillRect(-98,-78,196,136);if(i%2===0){X.fillStyle='#000';X.beginPath();X.moveTo(0,-50);X.lineTo(60,30);X.lineTo(-60,30);X.closePath();X.fill();[[-46,20],[46,20],[0,-34]].forEach(([a,b])=>{X.fillStyle='#fff';X.beginPath();X.arc(a,b,5,0,7);X.fill()})}else{X.fillStyle='#fff';X.beginPath();X.arc(-20,-10,4,0,7);X.arc(20,-14,4,0,7);X.arc(0,10,4,0,7);X.fill()}
    txt(['APR 1990','?','FAKE?','REAL?','APR 1990','?'][i],0,76,18,'#b71c1c',{w:800});X.fillStyle='#d32f2f';X.beginPath();X.arc(0,-90,6,0,7);X.fill();X.restore()}
   X.strokeStyle='#d32f2f';X.lineWidth=2;X.beginPath();X.moveTo(L+220,520);X.lineTo(L+520,760);X.lineTo(L+820,520);X.stroke()}
  {const ty=1180;X.fillStyle='#4e342e';X.fillRect(L-120,ty,1320,24);X.fillStyle='#3e2723';X.fillRect(L-110,ty+24,1300,120);glow('#fffbe6',30,()=>{X.fillStyle='#fffdf2';rr(L+330,ty-30,420,30,6);X.fill()});
   X.save();X.translate(L+540,ty-90);X.fillStyle='#000';X.beginPath();X.moveTo(0,-40);X.lineTo(70,30);X.lineTo(-70,30);X.closePath();X.fill();X.restore();
   X.strokeStyle='#333';X.lineWidth=10;X.beginPath();X.arc(L+680,ty-110,50,0,7);X.stroke();X.fillStyle='rgba(180,220,255,.3)';X.beginPath();X.arc(L+680,ty-110,46,0,7);X.fill();X.strokeStyle='#5d4037';X.lineWidth=14;X.beginPath();X.moveTo(L+716,ty-74);X.lineTo(L+780,ty-10);X.stroke();
   lamparaArq(L+180,ty,1,true);papeles(L+900,ty,6)}}};

// ===== INSERTOS: fondos de primer plano sin personajes =====
NUEVOS.vitrinaV={osc:.3,
 luces(z){const F=FV(z);return [{x:F.cx,y:500,fy:1500,r:520,c:O(z).luz2||'255,244,228',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);const c=o.fondo||['#46577a','#1f2940','#06080f'];
  const g=X.createRadialGradient(F.cx,1150,40,F.cx,1150,1300);g.addColorStop(0,c[0]);g.addColorStop(.45,c[1]);g.addColorStop(1,c[2]);X.fillStyle=g;X.fillRect(L-120,-300,1320,2400);
  const f=X.createRadialGradient(F.cx,1560,10,F.cx,1560,600);f.addColorStop(0,'rgba(255,255,255,.22)');f.addColorStop(1,'rgba(255,255,255,0)');X.fillStyle=f;X.save();X.translate(F.cx,1560);X.scale(1,.28);X.translate(-F.cx,-1560);X.beginPath();X.arc(F.cx,1560,600,0,7);X.fill();X.restore();
  if(o.pedestal){X.fillStyle=gl(F.cx-200,0,F.cx+200,0,[[0,'#2a2d34'],[.5,'#4a4f5a'],[1,'#23262c']]);X.fillRect(F.cx-200,1300,400,360);X.fillStyle='#5a606c';X.beginPath();X.ellipse(F.cx,1300,200,36,0,0,7);X.fill()}
  for(let i=0;i<26;i++){const px=F.cx+(rnd(i)-.5)*1000,py=200+((rnd(i*5)*1500+t*14*(rnd(i+2)+.3))%1500);X.fillStyle=`rgba(255,250,235,${.15+.25*rnd(i+9)})`;X.beginPath();X.arc(px,py,1.6+rnd(i+4)*1.8,0,7);X.fill()}}};
NUEVOS.mesaCenitalV={osc:.25,
 luces(z){const F=FV(z);return [{x:F.cx,y:900,fy:1000,r:800,c:'255,225,170',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),A=window.__A||0;
  X.fillStyle='#4a2c18';X.fillRect(L-120,-300,1320,2400);for(let i=0;i<22;i++){const py=-200+i*100;X.fillStyle=i%2?'#55331d':'#4d2e1a';X.fillRect(L-120,py,1320,98);X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=3;X.beginPath();X.moveTo(L-120,py);X.lineTo(L+1200,py);X.stroke();X.strokeStyle='rgba(255,220,180,.06)';X.lineWidth=2;for(let k=0;k<5;k++){X.beginPath();X.moveTo(L-120,py+14+k*16);for(let xx=0;xx<1320;xx+=120)X.quadraticCurveTo(L-120+xx+60,py+14+k*16+Math.sin(xx*.01+i+k)*6,L-120+xx+120,py+14+k*16);X.stroke()}}
  const fi=o.firma?seg(t,tk(o.firma,A),tk(o.firma,A)+1.6):0;
  contratoCenital(F.cx-40,900,1.15,t,o,fi);
  if(o.billetes){for(let k=0;k<4;k++)fajoCenital(L+780+(k%2)*60,1380+Math.floor(k/2)*110,1,o.billete)}
  if(o.cafe!==false)cafeCenital(L+200,1420,t);lentesCenital(L+260,420,.3);plumaCenital(F.cx+220-fi*80,1240-fi*40,-.6);
  if(o.extra==='disquete')UTILERIA.disquete(L+840,520,1,t,{});
  X.save();const vg=X.createRadialGradient(F.cx,960,300,F.cx,960,1200);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,.6)');X.fillStyle=vg;X.fillRect(L-120,-300,1320,2400);X.restore()}};

// ===== OBJETOS PROTAGONISTAS (para insertos o escenas) =====
UTILERIA.botella1899=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);somb(0,0,110,16,.5);X.fillStyle=gl(-70,0,70,0,[[0,'rgba(120,170,140,.55)'],[.4,'rgba(200,240,215,.6)'],[1,'rgba(90,140,110,.55)']]);X.beginPath();X.moveTo(-70,0);X.lineTo(70,0);X.lineTo(70,-300);X.quadraticCurveTo(70,-360,30,-380);X.lineTo(30,-460);X.lineTo(-30,-460);X.lineTo(-30,-380);X.quadraticCurveTo(-70,-360,-70,-300);X.closePath();X.fill();
 X.fillStyle='rgba(80,40,20,.85)';X.fillRect(-64,-250,128,244);X.fillStyle='rgba(255,255,255,.45)';X.fillRect(-50,-360,12,320);X.fillStyle='#bdbdbd';X.fillRect(-36,-480,72,26);X.strokeStyle='#888';X.lineWidth=4;X.beginPath();X.moveTo(-24,-480);X.quadraticCurveTo(0,-520,24,-480);X.stroke();
 X.fillStyle='#f5ecd8';X.fillRect(-60,-200,120,90);X.strokeStyle='#7a1d22';X.lineWidth=3;X.strokeRect(-54,-194,108,78);txt(o.etiqueta||'SODA',0,-170,22,'#7a1d22',{w:800});txt('1899',0,-136,16,'#7a1d22',{w:700});X.restore()};
UTILERIA.disquete=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);X.rotate(o.rot||-.12);X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-150,-144,310,310);X.fillStyle='#1b1b1f';X.fillRect(-160,-160,320,320);X.fillStyle='#2b2b30';X.beginPath();X.arc(0,0,60,0,7);X.fill();X.fillStyle='#8d6e63';X.beginPath();X.arc(0,0,40,0,7);X.fill();X.fillStyle='#1b1b1f';X.beginPath();X.arc(0,0,20,0,7);X.fill();X.fillStyle='#8d6e63';rr(-16,64,32,80,10);X.fill();
 X.fillStyle='#fbf8ef';X.fillRect(-140,-150,280,90);X.fillStyle='#1565c0';X.fillRect(-140,-150,280,14);txt(o.etiqueta||'QDOS 1.0',0,-100,34,'#222',{w:800});X.fillStyle='#424242';X.fillRect(-160,120,30,30);X.restore()};
UTILERIA.consolaGen=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);somb(0,0,160,16,.5);if(o.forma==='torre'){X.fillStyle=gl(-60,0,60,0,[[0,'#f5f5f5'],[.5,'#ffffff'],[1,'#dcdcdc']]);X.beginPath();X.moveTo(-70,0);X.quadraticCurveTo(-110,-240,-60,-430);X.lineTo(60,-430);X.quadraticCurveTo(110,-240,70,0);X.closePath();X.fill();X.fillStyle='#111';X.fillRect(-26,-430,52,430);X.fillStyle='#4fc3f7';X.fillRect(-4,-400,8,40)}
 else{X.fillStyle='#111';rr(-110,-300,220,300,20);X.fill();X.fillStyle='#1d1d1d';X.fillRect(-90,-280,180,260);X.fillStyle='#76ff03';X.beginPath();X.arc(0,-40,8,0,7);X.fill();X.fillStyle='#000';X.beginPath();X.ellipse(0,-300,90,14,0,0,7);X.fill();for(let k=0;k<6;k++){X.fillStyle='#2a2a2a';X.beginPath();X.arc(-50+k*20,-300,5,0,7);X.fill()}}
 X.fillStyle='rgba(255,255,255,.18)';X.fillRect(-60,-420,6,380);X.restore()};
UTILERIA.trofeo=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);somb(0,0,120,16,.5);X.fillStyle='#3e2723';X.fillRect(-90,-70,180,70);X.fillStyle='#d4af37';X.fillRect(-80,-60,160,20);txt(o.texto||'RECORD',0,-24,22,'#d4af37',{w:800});
 X.fillStyle=gl(-80,0,80,0,[[0,'#9a7a1f'],[.4,'#ffe082'],[.6,'#f5c542'],[1,'#8a6a14']]);X.fillRect(-20,-170,40,100);X.beginPath();X.moveTo(-100,-380);X.lineTo(100,-380);X.quadraticCurveTo(100,-200,0,-170);X.quadraticCurveTo(-100,-200,-100,-380);X.fill();X.strokeStyle='#d4af37';X.lineWidth=14;X.beginPath();X.arc(-100,-310,44,Math.PI*.5,Math.PI*1.5);X.stroke();X.beginPath();X.arc(100,-310,44,-Math.PI*.5,Math.PI*.5);X.stroke();
 X.fillStyle='rgba(255,255,255,.55)';X.fillRect(-60,-370,14,150);X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,-280,10,0,-280,260);g.addColorStop(0,`rgba(255,220,120,${.25+.1*Math.sin(t*3)})`);g.addColorStop(1,'rgba(255,220,120,0)');X.fillStyle=g;X.beginPath();X.arc(0,-280,260,0,7);X.fill();X.restore();X.restore()};
UTILERIA.fotoCasa=(x,y,s,t,o)=>{X.save();X.translate(x,y);X.scale(s,s);X.rotate(-.04);X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-250,-210,520,440);X.fillStyle='#3e2723';X.fillRect(-270,-230,540,460);X.fillStyle='#f5ecd8';X.fillRect(-240,-200,480,400);X.save();X.beginPath();X.rect(-220,-180,440,360);X.clip();X.fillStyle=gl(0,-180,0,180,[[0,'#ffb37a'],[1,'#ffe0b2']]);X.fillRect(-220,-180,440,360);
 X.fillStyle='#e8d5b5';X.fillRect(-150,0,300,170);X.fillStyle='#c0623a';X.beginPath();X.moveTo(-170,0);X.lineTo(0,-80);X.lineTo(170,0);X.closePath();X.fill();X.fillStyle='#bfc3c8';X.fillRect(-120,60,130,110);X.fillStyle='#5d4037';X.fillRect(50,70,60,100);palmeraV(-200,180,.45,t);palmeraV(200,180,.42,t);X.restore();X.fillStyle='rgba(255,255,255,.08)';X.fillRect(-240,-200,480,400);X.restore()};
UTILERIA.tazaTurca=(x,y,s,t,o)=>{X.save();X.translate(x,y);X.scale(s,s);somb(0,0,170,20,.5);X.fillStyle='#d4af37';X.beginPath();X.ellipse(0,-10,170,30,0,0,7);X.fill();X.fillStyle='#b8901f';X.beginPath();X.ellipse(0,-14,150,22,0,0,7);X.fill();
 X.fillStyle=gl(-70,0,70,0,[[0,'#e0d8c8'],[.4,'#ffffff'],[1,'#cfc6b4']]);X.beginPath();X.moveTo(-70,-20);X.lineTo(70,-20);X.lineTo(80,-170);X.lineTo(-80,-170);X.closePath();X.fill();X.fillStyle='#1565c0';X.fillRect(-78,-150,156,16);X.fillStyle='#c62828';for(let k=0;k<5;k++){X.beginPath();X.arc(-56+k*28,-100,9,0,7);X.fill()}X.fillStyle='#3e2412';X.beginPath();X.ellipse(0,-170,80,14,0,0,7);X.fill();X.fillStyle='rgba(210,170,120,.6)';X.beginPath();X.ellipse(0,-170,60,9,0,0,7);X.fill();
 X.save();X.globalAlpha*=.35;for(let k=0;k<3;k++){X.strokeStyle='#fff';X.lineWidth=7;X.beginPath();const ox=Math.sin(t*1.4+k)*18;X.moveTo(-30+k*30,-186);X.bezierCurveTo(-40+k*30+ox,-260,-10+k*30+ox,-320,-30+k*30,-420);X.stroke()}X.restore();cezve(190,-14,1.6);X.restore()};
UTILERIA.edicto=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.fillRect(-196,-286,410,590);X.fillStyle=gl(-200,0,200,0,[[0,'#e8d3a8'],[.5,'#f5e6c4'],[1,'#dcc496']]);X.fillRect(-200,-290,400,580);X.fillStyle='#8a6a3a';X.beginPath();X.ellipse(0,-290,214,26,0,0,7);X.ellipse(0,290,214,26,0,0,7);X.fill();
 txt(o.titulo||'BY ORDER OF THE SULTAN',0,-220,22,'#5a1a10',{w:800});X.fillStyle='#7a5a3a';for(let l=0;l<11;l++)X.fillRect(-150,-170+l*30,300-(l%3)*40,5);txt(o.texto||'COFFEEHOUSES CLOSED',0,190,26,'#b71c1c',{w:800});X.fillStyle='#b71c1c';X.beginPath();X.arc(110,240,30,0,7);X.fill();X.fillStyle='#e57373';X.beginPath();X.arc(110,240,18,0,7);X.fill();X.restore()};
UTILERIA.monitorOnda=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);somb(0,0,260,20,.5);X.fillStyle='#212121';X.fillRect(-14,-120,28,120);X.fillRect(-100,-12,200,12);X.fillStyle='#111';rr(-300,-560,600,440,22);X.fill();pantallaDatos(-280,-540,560,400,o.pant||'onda',t);X.restore()};
UTILERIA.cronometro=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);somb(0,0,150,18,.5);X.fillStyle='#b0bec5';X.fillRect(-20,-400,40,40);X.fillRect(-36,-420,72,22);X.fillStyle=gl(-150,0,150,0,[[0,'#9a7a1f'],[.5,'#ffe082'],[1,'#8a6a14']]);X.beginPath();X.arc(0,-210,170,0,7);X.fill();X.fillStyle='#fffdf5';X.beginPath();X.arc(0,-210,140,0,7);X.fill();
 X.strokeStyle='#333';for(let i=0;i<60;i++){const a=i*Math.PI/30,l=i%5?8:18;X.lineWidth=i%5?2:4;X.beginPath();X.moveTo(Math.cos(a)*130,-210+Math.sin(a)*130);X.lineTo(Math.cos(a)*(130-l),-210+Math.sin(a)*(130-l));X.stroke()}
 const a=-Math.PI/2+(t%6)/6*Math.PI*2;X.strokeStyle='#c62828';X.lineWidth=5;X.beginPath();X.moveTo(0,-210);X.lineTo(Math.cos(a)*120,-210+Math.sin(a)*120);X.stroke();X.fillStyle='#222';X.beginPath();X.arc(0,-210,10,0,7);X.fill();txt(o.texto||'2:00',0,-140,34,'#222',{w:800});X.restore()};
UTILERIA.trianguloP=(x,y,s,t,o)=>trianguloEspuma(x,y,s,t,true);
UTILERIA.pcBeigeP=(x,y,s,t,o)=>pcBeige(x,y,s,t);
UTILERIA.jebenaP=(x,y,s,t,o)=>{jebena(x,y,s);X.save();X.globalAlpha*=.3;for(let k=0;k<3;k++){X.strokeStyle='#fff';X.lineWidth=6*s;X.beginPath();const ox=Math.sin(t*1.3+k)*20*s;X.moveTo(x+(-10+k*10)*s,y-160*s);X.bezierCurveTo(x+(-30+k*10)*s+ox,y-260*s,x+ox,y-330*s,x+(-20+k*12)*s,y-440*s);X.stroke()}X.restore()};
UTILERIA.notasP=(x,y,s,t,o)=>{X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#8a7a66';X.fillRect(-340,-600,680,560);X.strokeStyle='#5d4e3c';X.lineWidth=14;X.strokeRect(-340,-600,680,560);notasPared(-250,-500,t);X.restore()};
UTILERIA.huevoRoto=(x,y,s,t,o)=>{X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(180,220,255,.35)';X.fillRect(-300,-300,600,300);X.strokeStyle='rgba(255,255,255,.9)';X.lineWidth=3;for(let i=0;i<12;i++){const a=i*Math.PI/6;X.beginPath();X.moveTo(0,-150);X.lineTo(Math.cos(a)*(120+rnd(i)*160),-150+Math.sin(a)*(80+rnd(i+3)*90));X.stroke()}
 X.fillStyle='#ffca28';X.beginPath();X.ellipse(0,-150,70,46,0,0,7);X.fill();X.fillStyle='rgba(255,255,255,.9)';X.beginPath();X.ellipse(-10,-140,140,70,.2,0,7);X.fill();X.fillStyle='#ffb300';X.beginPath();X.arc(10,-150,40,0,7);X.fill();X.fillStyle='#4fc3f7';for(let i=0;i<5;i++){X.beginPath();X.moveTo(-200+i*80,-220);X.lineTo(-180+i*80,-180);X.lineTo(-220+i*80,-190);X.closePath();X.fill()}X.restore()};
