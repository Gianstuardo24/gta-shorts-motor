// ===== cafetal en las tierras altas e iglesia etiope =====
function cafeto(x,y,s,t,sem){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle='#5d4037';X.lineWidth=8;X.beginPath();X.moveTo(0,0);X.lineTo(0,-120);X.stroke();
 for(let i=0;i<7;i++){const yy=-40-i*28,w=110-i*12;X.fillStyle=i%2?'#2e7d32':'#388e3c';X.beginPath();X.ellipse(-w*.45,yy,w*.6,16,-.3,0,7);X.ellipse(w*.45,yy,w*.6,16,.3,0,7);X.fill();
  for(let k=0;k<4;k++){X.fillStyle=rnd(i*7+k+sem)>.35?'#c62828':'#7cb342';X.beginPath();X.arc(-w*.6+k*w*.4,yy+10,7,0,7);X.fill()}}X.restore()}
NUEVOS.cafetalV={osc:.08,
 luces(z){const F=FV(z);return [{x:F.L+800,y:200,fy:HZ+200,r:560,c:'255,236,190',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cielo(L-120,-300,1320,1610,o.hora||'dia',t,121);glow('#fff3c4',60,()=>{X.fillStyle='#fff6d0';X.beginPath();X.arc(L+820,420,70,0,7);X.fill()});
  [[900,'#6b8fa6'],[1020,'#5a8a5a'],[1140,'#4a7a3a']].forEach(([y,c],j)=>{X.fillStyle=c;X.beginPath();X.moveTo(L-120,y+60);for(let i=0;i<=10;i++)X.lineTo(L-120+i*132,y-Math.sin(i*1.3+j)*70-rnd(i+j*9)*40);X.lineTo(L+1200,1310);X.lineTo(L-120,1310);X.fill()});
  for(let r=0;r<3;r++)for(let i=0;i<7;i++)cafeto(L-60+i*180+(r%2)*90,1150+r*60,.6+r*.15,t,r*10+i);
  X.fillStyle='#6d4c2e';X.fillRect(L-120,1300,1320,700);X.fillStyle='#7a5a3a';X.beginPath();X.moveTo(F.cx-100,1300);X.lineTo(F.cx+100,1300);X.lineTo(F.cx+380,1920);X.lineTo(F.cx-380,1920);X.closePath();X.fill();
  for(let i=0;i<6;i++)cafeto(i<3?L+20+i*80:L+780+(i-3)*100,1500+(i%3)*120,1.1+(i%3)*.2,t,40+i);
  {const bx=L+880,by=1720;X.fillStyle='#a1887f';X.beginPath();X.ellipse(bx,by,110,30,0,0,7);X.fill();X.fillStyle='#8d6e63';X.fillRect(bx-110,by-90,220,90);X.fillStyle='#c62828';for(let k=0;k<30;k++){X.beginPath();X.arc(bx-90+rnd(k)*180,by-96+rnd(k*3)*14,9,0,7);X.fill()}}}};
function cruzEtiope(x,y,s,col='#d4af37'){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle=col;X.lineWidth=10;X.beginPath();X.moveTo(0,-140);X.lineTo(0,140);X.moveTo(-110,0);X.lineTo(110,0);X.stroke();
 for(const [dx,dy] of [[0,-140],[0,140],[-110,0],[110,0]]){X.beginPath();X.arc(dx,dy,24,0,7);X.stroke()}X.lineWidth=5;for(let i=0;i<4;i++){X.rotate(Math.PI/2);X.beginPath();X.moveTo(30,30);X.lineTo(70,70);X.stroke();X.beginPath();X.arc(76,76,12,0,7);X.stroke()}X.beginPath();X.arc(0,0,40,0,7);X.stroke();X.restore()}
NUEVOS.iglesiaV={osc:.4,
 luces(z){const F=FV(z);return [{x:F.cx,y:760,fy:HZ+240,r:420,c:'255,200,120',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#7a3e1d',p1:'#4e2410',piso:['#8b5a2b','#7a4e24'],paso:120,t0:'#1a0f08',t1:'#3a2414',cornisa:'#d4af37'});
  for(let i=0;i<3;i++){const ax=L-20+i*380;arcoMorisco(ax,520,300,760,'#3a1c0a');X.save();X.beginPath();X.rect(ax+14,520,272,760);X.clip();
   X.fillStyle=['#1565c0','#c62828','#2e7d32'][i];X.fillRect(ax,640,300,560);X.fillStyle='#fdd835';X.fillRect(ax+30,680,240,30);X.fillRect(ax+30,1120,240,30);cruzEtiope(ax+150,900,1,'#fdd835');X.restore();
   X.strokeStyle='#d4af37';X.lineWidth=8;X.beginPath();X.moveTo(ax,1280);X.lineTo(ax,520+180);X.quadraticCurveTo(ax,520,ax+150,475);X.quadraticCurveTo(ax+300,520,ax+300,700);X.lineTo(ax+300,1280);X.stroke()}
  for(let i=0;i<9;i++){const cx=L+120+i*110,cy=1270;X.fillStyle='#fff8e1';X.fillRect(cx-6,cy-60-(i%3)*20,12,60+(i%3)*20);glow('#ffcc66',18,()=>{X.fillStyle='#ffd27a';X.beginPath();X.ellipse(cx,cy-70-(i%3)*20+Math.sin(t*11+i)*1.5,5,10,0,0,7);X.fill()})}
  {const dx=L+900,dy=1500;X.fillStyle='#6d4c41';X.beginPath();X.ellipse(dx,dy-120,70,20,0,0,7);X.fill();X.fillStyle=gl(dx-70,0,dx+70,0,[[0,'#5d4037'],[.5,'#8d6e63'],[1,'#4e342e']]);X.beginPath();X.moveTo(dx-70,dy-120);X.lineTo(dx+70,dy-120);X.lineTo(dx+50,dy);X.lineTo(dx-50,dy);X.closePath();X.fill();X.strokeStyle='#d7ccc8';X.lineWidth=3;for(let k=0;k<6;k++){X.beginPath();X.moveTo(dx-66+k*26,dy-116);X.lineTo(dx-46+k*20,dy-4);X.stroke()}}
  alfombraPersa(F.cx,1420,800,1820,'#1f3a5f','#c62828')}};
