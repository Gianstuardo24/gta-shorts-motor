// ===== tanda 4: dormitorio + cama (insertos de mascotas) =====
function camaV(x,y,s,t,o={}){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,360,24,.5);
 X.fillStyle=gl(-340,0,340,0,[[0,'#5a3a22'],[.5,'#7a5230'],[1,'#4a2e1a']]);rr(-360,-430,60,430,14);X.fill();rr(300,-250,50,250,12);X.fill();
 X.fillStyle='#f3efe6';rr(-300,-200,600,80,20);X.fill();X.fillStyle=gl(0,-260,0,-120,[[0,o.manta||'#4a6fa5'],[1,'#2f4f7a']]);X.beginPath();X.moveTo(-180,-150);X.quadraticCurveTo(-170,-240,0,-232);X.quadraticCurveTo(200,-240,300,-170);X.lineTo(310,-110);X.lineTo(-190,-110);X.closePath();X.fill();
 X.strokeStyle='rgba(255,255,255,.18)';X.lineWidth=4;for(let i=0;i<5;i++){X.beginPath();X.moveTo(-150+i*90,-226+Math.abs(i-2)*4);X.quadraticCurveTo(-120+i*90,-180,-150+i*90,-120);X.stroke()}
 X.fillStyle='#fafafa';rr(-300,-250,140,70,30);X.fill();if(o.persona!==false){X.fillStyle='#e0ac69';X.beginPath();X.arc(-230,-262,40,0,7);X.fill();X.fillStyle='#3e2723';X.beginPath();X.arc(-232,-282,42,Math.PI,0);X.fill();X.strokeStyle='#5d4037';X.lineWidth=3;X.beginPath();X.arc(-214,-262,8,.2,Math.PI-.2);X.stroke()}
 X.fillStyle='#4e342e';X.fillRect(-300,-120,610,30);X.fillStyle='#3e2a1a';X.fillRect(-300,-90,20,90);X.fillRect(290,-90,20,90);
 if(o.zzz){for(let k=0;k<3;k++){const ph=(t*.6+k/3)%1;X.save();X.globalAlpha*=1-ph;txt('z',-180+ph*60+k*10,-320-ph*120,30+k*8,'#fff',{w:800});X.restore()}}X.restore()}
NUEVOS.dormitorioV={osc:.48,
 luces(z){const F=FV(z);return [{x:F.L+130,y:1080,fy:HZ+230,r:300,c:'255,200,130',panel:1},{x:F.L+870,y:620,fy:HZ+200,r:300,c:'150,170,240',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:o.pared?o.pared[0]:'#3d4a6b',p1:o.pared?o.pared[1]:'#2a3350',piso:['#5a4030','#4e3628'],paso:120,t0:'#0d0f18',t1:'#1d2236',cornisa:'#c9b896',zocalo:'#232a40',zy:1140});
  ventanaV(L+720,520,300,380,'noche',t,{arbol:true,sem:19,marco:'#d8d0bc'});cortina(L+640,480,90,520,['#8a6a9a','#5a3a6a'],-1,t);cortina(L+1010,480,90,520,['#8a6a9a','#5a3a6a'],1,t);
  cuadroFoto(L+250,560,220,160,4);cuadroFoto(L+500,600,120,150,3,'perro');
  {const nx=L+120;X.fillStyle='#5a3a22';X.fillRect(nx-70,1120,140,180);X.fillStyle='#4a2e1a';X.fillRect(nx-78,1110,156,16);X.fillStyle='#d4af37';X.beginPath();X.arc(nx,1200,6,0,7);X.fill();lamparaPie(nx,1110,.45,true);taza2(nx+40,1110,'#e8e3d8')}
  camaV(L+560,1330,1,t,{zzz:o.zzz,persona:o.persona,manta:o.manta});
  alfombraPersa(F.cx,1460,900,1760,'#5a3a6a','#c9a06a');
  {X.fillStyle='#e57373';X.beginPath();X.ellipse(L+180,1560,46,16,0,0,7);X.ellipse(L+260,1580,46,16,0,0,7);X.fill()}}};
UTILERIA.camaDormida=(x,y,s,t,o)=>{o=o||{};camaV(x,y,s,t,{zzz:true,manta:o.manta});perro(x+90*s,y-232*s,.85*s,t,{pose:'echado',dir:-1,color:o.color||'#d9a35b',collar:'rosa'})};
