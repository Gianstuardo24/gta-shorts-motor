// ===== ESCENARIOS VERTICALES (Shorts 1080x1920) · tanda 1: hogar, ciencia, refugio, cafe otomano, Estambul, palacio, Etiopia =====
// Marco: F={L (x izq. visible), W:1080, cx}. Techo 0-380, pared 380-1300, piso 1300-1920. HUD arriba (0-560): techo tranquilo.
function FV(z){let L=z.cam;if(L===undefined)L=z.x0<0?0:z.x0;return {L,W:1080,cx:L+540}}
function cuartoV(F,o){const x0=F.L-120,x1=F.L+F.W+120,w=x1-x0,cx=F.cx;
 X.fillStyle=gl(0,-200,0,380,[[0,o.t0||'#14141c'],[1,o.t1||'#2a2a36']]);X.fillRect(x0,-300,w,690);
 if(o.vigas){X.fillStyle=o.vigas;for(let i=-2;i<w/170+2;i++){const bx=x0+i*170;X.beginPath();X.moveTo(bx,380);X.lineTo(bx+26,380);X.lineTo(cx+(bx+26-cx)*2.2,-300);X.lineTo(cx+(bx-cx)*2.2,-300);X.closePath();X.fill()}}
 X.fillStyle=o.cornisa||'#e8e0d0';X.fillRect(x0,366,w,22);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(x0,388,w,10);
 X.fillStyle=gl(0,390,0,1300,[[0,o.p0],[1,o.p1]]);X.fillRect(x0,388,w,912);
 if(o.zocalo){X.fillStyle=o.zocalo;X.fillRect(x0,o.zy||1120,w,1300-(o.zy||1120));X.fillStyle='rgba(255,255,255,.15)';X.fillRect(x0,(o.zy||1120)-6,w,8)}
 X.fillStyle=o.rodapie||'#3a2c20';X.fillRect(x0,1282,w,20);
 X.fillStyle=o.piso?o.piso[0]:'#5a4030';X.fillRect(x0,1300,w,700);pisoPersp(x0,x1,cx,1300,1920,o.paso||130,o.piso||['#6b4a30','#5e3f28'],o.linea||'rgba(0,0,0,.22)');
 X.fillStyle=gl(0,1300,0,1380,[[0,'rgba(0,0,0,.4)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,1300,w,80)}
function ventanaV(x,y,w,h,hora,t,o={}){X.fillStyle=o.marco||'#efe9dc';X.fillRect(x-16,y-16,w+32,h+32);X.save();X.beginPath();X.rect(x,y,w,h);X.clip();cielo(x,y,w,h,hora,t,o.sem||3);
 if(o.ciudad)skyline(x,y+h*.4,w,h*.6,hora,o.sem||5);if(o.arbol){X.fillStyle=hora==='noche'?'#0b1a12':'#3f7a35';for(let i=0;i<8;i++){X.beginPath();X.arc(x+w*(.1+rnd(i+o.sem)*.5),y+h*(.55+rnd(i*3)*.3),40+rnd(i+9)*30,0,7);X.fill()}}
 if(o.persiana){for(let yy=y;yy<y+h*.45;yy+=16){X.fillStyle=gl(0,yy,0,yy+10,[[0,'#f5f0e3'],[1,'#cbc3af']]);X.fillRect(x,yy,w,10)}}X.restore();
 X.strokeStyle=o.marco||'#efe9dc';X.lineWidth=10;X.beginPath();X.moveTo(x+w/2,y);X.lineTo(x+w/2,y+h);X.moveTo(x,y+h/2);X.lineTo(x+w,y+h/2);X.stroke();X.fillStyle=o.marco||'#efe9dc';X.fillRect(x-30,y+h+10,w+60,16);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(x-30,y+h+26,w+60,6);
 X.fillStyle='rgba(255,255,255,.08)';X.beginPath();X.moveTo(x+10,y);X.lineTo(x+w*.35,y);X.lineTo(x+10,y+h*.6);X.closePath();X.fill()}
function cuadroFoto(x,y,w,h,sem,tipo='paisaje'){X.fillStyle='rgba(0,0,0,.25)';X.fillRect(x+6,y+8,w,h);X.fillStyle='#2b2b2b';X.fillRect(x-8,y-8,w+16,h+16);X.fillStyle='#f4f1ea';X.fillRect(x,y,w,h);const m=Math.min(w,h)*.12;X.save();X.beginPath();X.rect(x+m,y+m,w-2*m,h-2*m);X.clip();
 if(tipo==='perro'){X.fillStyle='#bfe0f2';X.fillRect(x,y,w,h);X.fillStyle='#d9a35b';X.beginPath();X.ellipse(x+w/2,y+h*.62,w*.22,h*.2,0,0,7);X.fill();X.beginPath();X.arc(x+w/2,y+h*.4,w*.15,0,7);X.fill();X.fillStyle='#8a5a2a';X.beginPath();X.ellipse(x+w/2-w*.14,y+h*.38,w*.05,h*.1,.3,0,7);X.ellipse(x+w/2+w*.14,y+h*.38,w*.05,h*.1,-.3,0,7);X.fill();X.fillStyle='#222';X.beginPath();X.arc(x+w/2-w*.05,y+h*.38,3,0,7);X.arc(x+w/2+w*.05,y+h*.38,3,0,7);X.fill()}
 else{X.fillStyle=gl(0,y,0,y+h,[[0,'#ffcf8a'],[1,'#7fb3a0']]);X.fillRect(x,y,w,h);X.fillStyle='#4f7a5a';X.beginPath();X.moveTo(x,y+h*.75);X.quadraticCurveTo(x+w*.5,y+h*.45,x+w,y+h*.7);X.lineTo(x+w,y+h);X.lineTo(x,y+h);X.fill()}X.restore()}
function sofaV(x,y,s,col){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,300,22,.45);X.fillStyle='#2a1a10';X.fillRect(-250,-24,16,24);X.fillRect(234,-24,16,24);
 X.fillStyle=gl(0,-260,0,-120,[[0,col[0]],[1,col[1]]]);rr(-280,-260,560,150,40);X.fill();X.fillStyle=col[1];rr(-300,-170,80,150,30);X.fill();rr(220,-170,80,150,30);X.fill();
 X.fillStyle=gl(0,-130,0,-40,[[0,col[0]],[1,col[1]]]);rr(-230,-130,225,70,22);X.fill();rr(5,-130,225,70,22);X.fill();X.fillStyle=col[1];X.fillRect(-250,-70,500,50);
 X.fillStyle='rgba(255,255,255,.12)';X.fillRect(-260,-252,520,5);X.fillStyle='#e8b04a';X.save();X.translate(-150,-160);X.rotate(-.2);rr(-40,-40,80,80,16);X.fill();X.restore();X.fillStyle='#5aa0a8';X.save();X.translate(160,-160);X.rotate(.15);rr(-38,-38,76,76,16);X.fill();X.restore();X.restore()}
function lamparaPie(x,y,s,on=true){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#222';X.beginPath();X.ellipse(0,0,46,10,0,0,7);X.fill();X.fillRect(-4,-460,8,460);X.fillStyle=gl(-60,0,60,0,[[0,'#e8dcc0'],[.5,'#fff6e0'],[1,'#d8c8a0']]);X.beginPath();X.moveTo(-50,-560);X.lineTo(50,-560);X.lineTo(80,-450);X.lineTo(-80,-450);X.closePath();X.fill();
 if(on){X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,-480,10,0,-420,330);g.addColorStop(0,'rgba(255,220,150,.42)');g.addColorStop(1,'rgba(255,220,150,0)');X.fillStyle=g;X.beginPath();X.arc(0,-420,330,0,7);X.fill();X.restore()}X.restore()}
function camaPerro(x,y,s,col){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,150,16,.4);X.fillStyle=col||'#8d6e63';X.beginPath();X.ellipse(0,-30,150,48,0,0,7);X.fill();X.fillStyle='#d7ccc8';X.beginPath();X.ellipse(0,-34,112,30,0,0,7);X.fill();X.fillStyle='#e53935';X.beginPath();X.arc(60,-40,14,0,7);X.fill();X.restore()}
function platoMascota(x,y,s,col,lleno){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(0,4,62,10,0,0,7);X.fill();X.fillStyle=col||'#c62828';X.beginPath();X.moveTo(-60,0);X.lineTo(60,0);X.lineTo(48,-34);X.lineTo(-48,-34);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.25)';X.fillRect(-46,-32,92,5);
 if(lleno){X.fillStyle='#8d5a2b';for(let i=0;i<14;i++){X.beginPath();X.arc(-36+i*5.5,-38-(i%3)*4,6,0,7);X.fill()}}X.restore()}

// --- Sala de estar acogedora (perros y gatos). o.hora, o.sofa:[c0,c1], o.pared:[c0,c1], o.var (cambia la decoracion) ---
NUEVOS.salaV={osc:.2,
 luces(z){const F=FV(z);return [{x:F.L+860,y:1000,fy:HZ+260,r:360,c:'255,214,150',panel:1},{x:F.L+250,y:900,fy:HZ+240,r:360,c:O(z).hora==='noche'?'150,170,230':'255,240,215',panel:1}]},
 fondo(z,t,q){const F=FV(z),o=O(z),L=F.L,v=o.var||0;
  cuartoV(F,{p0:(o.pared||['#c9d6cf','#a9bcb3'])[0],p1:(o.pared||['#c9d6cf','#a9bcb3'])[1],zocalo:v%2?'#8fa59b':null,zy:1100,piso:['#a07a52','#957049','#a9825a'],t0:'#1c1a18',t1:'#3a342c'});
  ventanaV(L+120,560,300,420,o.hora||'dia',t,{arbol:true,sem:3+v});cortina(L+40,520,90,560,['#e6c79a','#b08a5a'],-1,t);cortina(L+410,520,90,560,['#e6c79a','#b08a5a'],1,t);
  cuadroFoto(L+600,600,150,190,v,'perro');cuadroFoto(L+790,640,190,140,v+2);
  librero(L+560,860,420,300,7+v,true);
  alfombraPersa(F.cx,1440,980,1840,v%2?'#3d5a80':'#a0522d','#e8c98a');
  if(!o.sinSofa)sofaV(L+770,1300,.86,o.sofa||['#4a6fa5','#2f4f7a']);lamparaPie(L+1010,1300,.9,true);planta(L+60,1310,1.05);
  {const tx=L+300;X.fillStyle='#5a3a22';X.fillRect(tx-80,1250,160,14);X.fillRect(tx-70,1264,10,40);X.fillRect(tx+60,1264,10,40);taza2(tx-30,1250,'#e8e3d8');X.fillStyle='#1e88e5';X.fillRect(tx+10,1236,50,14);X.fillStyle='#fbc02d';X.fillRect(tx+14,1222,44,14)}}};

// --- Cocina de manana (desayuno de mascotas): muebles altos, refrigerador, cafetera, ventana con sol, plato de comida ---
NUEVOS.cocinaV={osc:.12,
 luces(z){const F=FV(z);return [{x:F.L+700,y:700,fy:HZ+260,r:460,c:'255,244,220',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#f3ead8',p1:'#e6d9c0',piso:['#e8e2d6','#cfc6b6'],paso:110,linea:'rgba(0,0,0,.12)',t0:'#d9d2c4',t1:'#efe8da',cornisa:'#fff'});
  X.fillStyle='#fbf7ef';X.fillRect(L-120,860,1320,280);X.strokeStyle='rgba(120,140,160,.25)';X.lineWidth=2;for(let y=860;y<1140;y+=40){X.beginPath();X.moveTo(L-120,y);X.lineTo(L+1200,y);X.stroke()}for(let x=L-120;x<L+1200;x+=40){X.beginPath();X.moveTo(x,860);X.lineTo(x,1140);X.stroke()}
  for(let i=0;i<4;i++){const cx=L+20+i*190;X.fillStyle=gl(cx,0,cx+170,0,[[0,'#6f8f7a'],[1,'#5c7a66']]);X.fillRect(cx,430,170,380);X.strokeStyle='rgba(255,255,255,.25)';X.lineWidth=3;X.strokeRect(cx+14,444,142,352);X.fillStyle='#d4af37';X.fillRect(cx+130,610,8,40)}
  ventanaV(L+790,470,240,330,'dia',t,{arbol:true,sem:8});
  {const fx=L+800;X.fillStyle=gl(fx,0,fx+240,0,[[0,'#e9ecef'],[.5,'#ffffff'],[1,'#d0d5da']]);rr(fx,880,240,430,18);X.fill();X.fillStyle='rgba(0,0,0,.15)';X.fillRect(fx,1030,240,4);X.fillStyle='#adb5bd';X.fillRect(fx+200,920,10,90);X.fillRect(fx+200,1060,10,150);X.fillStyle='#ffca28';X.fillRect(fx+40,920,40,30);X.fillStyle='#ef5350';X.beginPath();X.arc(fx+120,935,14,0,7);X.fill()}
  {const ty=1160;X.fillStyle=gl(0,ty,0,1300,[[0,'#6f8f7a'],[1,'#4f6a58']]);X.fillRect(L-120,ty,900,140);X.fillStyle='#e9e4da';X.fillRect(L-130,ty-26,920,30);X.fillStyle='rgba(255,255,255,.4)';X.fillRect(L-130,ty-26,920,4);
   for(let i=0;i<4;i++){X.strokeStyle='rgba(255,255,255,.2)';X.lineWidth=3;X.strokeRect(L-100+i*200,ty+16,180,110);X.fillStyle='#d4af37';X.fillRect(L-20+i*200,ty+30,30,6)}
   X.fillStyle='#263238';rr(L+80,ty-200,120,174,14);X.fill();X.fillStyle='#455a64';X.fillRect(L+92,ty-150,96,8);X.fillStyle='rgba(200,230,255,.35)';rr(L+100,ty-100,80,74,10);X.fill();X.fillStyle='#4e2a14';X.fillRect(L+106,ty-60,68,28);X.fillStyle=Math.sin(t*3)>0?'#ff5252':'#5a1f1f';X.beginPath();X.arc(L+176,ty-180,5,0,7);X.fill();
   X.fillStyle='#bcaaa4';rr(L+330,ty-150,70,124,10);X.fill();X.fillStyle='#8d6e63';X.fillRect(L+330,ty-150,70,20);X.fillStyle='#fff';X.fillRect(L+345,ty-110,40,30);txt('FOOD',L+365,ty-95,12,'#5d4037',{w:800});
   X.fillStyle='#f5f5f5';X.beginPath();X.ellipse(L+520,ty-30,60,12,0,0,7);X.fill();for(let i=0;i<3;i++){X.fillStyle=['#ff7043','#fdd835','#66bb6a'][i];X.beginPath();X.arc(L+495+i*24,ty-42,14,0,7);X.fill()}
   taza2(L+640,ty-26,'#1e88e5')}
  platoMascota(L+300,1500,1.1,o.plato||'#e53935',!!o.lleno);platoMascota(L+470,1500,1.1,'#1e88e5',false)}};

// --- Laboratorio de ciencia (estudios con animales): mesones, microscopio, monitores con datos, frascos, pizarra. o.pantalla: caras|onda|nombres|foto ---
function pantallaDatos(x,y,w,h,tipo,t){X.fillStyle='#0d1b2a';X.fillRect(x,y,w,h);X.save();X.beginPath();X.rect(x,y,w,h);X.clip();
 if(tipo==='onda'){X.strokeStyle='#4fc3f7';X.lineWidth=3;X.shadowColor='#4fc3f7';X.shadowBlur=8;X.beginPath();for(let i=0;i<=w;i+=3){const yy=y+h/2+Math.sin(i*.09+t*6)*h*.18*Math.sin(i*.013+t)+Math.sin(i*.4+t*9)*h*.06;i?X.lineTo(x+i,yy):X.moveTo(x+i,yy)}X.stroke();X.shadowBlur=0;X.strokeStyle='#ff4081';X.beginPath();for(let i=0;i<=w;i+=3){const yy=y+h*.78+Math.sin(i*.25+t*12)*h*.06;i?X.lineTo(x+i,yy):X.moveTo(x+i,yy)}X.stroke()}
 else if(tipo==='caras'){[[.3,'#8d8d94'],[.7,'#d9a35b']].forEach(([fx,c])=>{const cx=x+w*fx,cy=y+h*.55;X.fillStyle=c;X.beginPath();X.ellipse(cx,cy,w*.15,h*.3,0,0,7);X.fill();X.fillStyle='#222';X.beginPath();X.arc(cx-w*.05,cy-h*.06,4,0,7);X.arc(cx+w*.05,cy-h*.06,4,0,7);X.fill();X.strokeStyle='#4fc3f7';X.lineWidth=2;X.strokeRect(cx-w*.17,cy-h*.34,w*.34,h*.66);X.strokeStyle='#ffd740';X.beginPath();X.moveTo(cx-w*.09,cy-h*.16);X.quadraticCurveTo(cx-w*.05,cy-h*.24,cx-w*.01,cy-h*.17);X.stroke()})}
 else if(tipo==='nombres'){const pal=['MOCHI','LUNA','TOFU','MOCHI'];pal.forEach((p,i)=>{const on=i===3;X.fillStyle=on?'#69f0ae':'rgba(79,195,247,.5)';X.fillRect(x+16,y+18+i*h*.22,on?w*.8:w*.5,h*.14);txt(p,x+30,y+18+i*h*.22+h*.07,h*.09,'#0d1b2a',{al:'left',w:800})})}
 else{X.fillStyle='#16324a';X.fillRect(x,y,w,h);X.strokeStyle='rgba(79,195,247,.4)';for(let i=0;i<8;i++){X.beginPath();X.moveTo(x,y+i*h/8);X.lineTo(x+w,y+i*h/8);X.stroke()}}
 X.fillStyle='rgba(255,255,255,.06)';X.fillRect(x,y,w,h*.4);X.restore();X.strokeStyle='#263238';X.lineWidth=10;X.strokeRect(x,y,w,h)}
function microscopio(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#eceff1';rr(-50,-14,100,14,4);X.fill();X.fillStyle='#37474f';X.beginPath();X.moveTo(20,-14);X.quadraticCurveTo(50,-80,10,-120);X.lineTo(-6,-110);X.quadraticCurveTo(24,-76,0,-14);X.closePath();X.fill();X.fillStyle='#eceff1';X.save();X.translate(-6,-118);X.rotate(-.45);rr(-12,-70,24,80,6);X.fill();X.fillStyle='#263238';X.fillRect(-14,-84,28,16);X.restore();X.fillStyle='#90a4ae';X.fillRect(-36,-46,70,8);X.fillStyle='#b0bec5';X.fillRect(-14,-60,10,16);X.restore()}
function frascos(x,y,n,sem){for(let i=0;i<n;i++){const h=40+rnd(i+sem)*50,w=26+rnd(i*3+sem)*16,c=['rgba(129,212,250,.6)','rgba(165,214,167,.6)','rgba(255,204,128,.6)','rgba(206,147,216,.6)'][i%4];X.fillStyle='rgba(230,240,250,.5)';rr(x+i*44,y-h,w,h,6);X.fill();X.fillStyle=c;X.fillRect(x+i*44+2,y-h*.55,w-4,h*.55-2);X.fillStyle='#455a64';X.fillRect(x+i*44+4,y-h-8,w-8,8)}}
NUEVOS.labV={osc:.1,
 luces(z){const F=FV(z);return [{x:F.L+300,y:400,fy:HZ+280,r:420,c:'235,245,255',panel:1},{x:F.L+780,y:400,fy:HZ+280,r:420,c:'235,245,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#e3eaef',p1:'#cbd6de',piso:['#b9c4cc','#aeb9c2'],paso:150,linea:'rgba(0,0,0,.12)',t0:'#9aa6b0',t1:'#c9d3db',cornisa:'#f5f8fa',zocalo:'#9fb0bd',zy:1140});
  [300,780].forEach(s=>{glow('#eef6ff',30,()=>{X.fillStyle='#f6fbff';rr(L+s-150,330,300,26,6);X.fill()})});
  {X.fillStyle='#fafafa';X.fillRect(L+40,520,420,260);X.strokeStyle='#90a4ae';X.lineWidth=8;X.strokeRect(L+40,520,420,260);X.strokeStyle='#1565c0';X.lineWidth=3;
   X.beginPath();X.moveTo(L+70,740);for(let i=0;i<8;i++)X.lineTo(L+70+i*45,740-Math.pow(i,1.6)*14);X.stroke();X.strokeStyle='#c62828';X.beginPath();X.moveTo(L+70,740);for(let i=0;i<8;i++)X.lineTo(L+70+i*45,740-i*8);X.stroke();X.fillStyle='#333';X.fillRect(L+70,560,180,8);X.fillRect(L+70,580,120,6);X.fillStyle='#ef6c00';X.fillRect(L+60,790,80,10)}
  {X.fillStyle='#cfd8dc';X.fillRect(L+520,560,500,12);X.fillRect(L+520,700,500,12);frascos(L+540,560,10,o.sem||2);frascos(L+540,700,8,(o.sem||2)+5)}
  {const ty=1180;X.fillStyle='#37474f';X.fillRect(L-120,ty,1320,22);X.fillStyle=gl(0,ty+22,0,1300,[[0,'#eceff1'],[1,'#b0bec5']]);X.fillRect(L-110,ty+22,1300,120);for(let i=0;i<6;i++){X.strokeStyle='rgba(0,0,0,.15)';X.lineWidth=2;X.strokeRect(L-90+i*210,ty+34,190,96);X.fillStyle='#78909c';X.fillRect(L-10+i*210,ty+50,30,5)}
   X.fillStyle='#263238';X.fillRect(L+600,ty-200,8,200);pantallaDatos(L+480,ty-340,300,190,o.pantalla||'onda',t);X.fillStyle='#263238';X.fillRect(L+590,ty-150,30,150);X.fillRect(L+560,ty-10,90,10);
   pantallaDatos(L+800,ty-280,220,150,o.pantalla2||'foto',t);X.fillStyle='#263238';X.fillRect(L+900,ty-130,20,130);
   microscopio(L+160,ty,1.1);frascos(L+300,ty,3,9);X.fillStyle='#eceff1';X.fillRect(L+60,ty-24,60,24);X.fillStyle='#ff7043';X.fillRect(L+66,ty-20,48,6);
   X.fillStyle='#fff';X.beginPath();X.moveTo(L+420,ty);X.lineTo(L+470,ty);X.lineTo(L+462,ty-60);X.lineTo(L+428,ty-60);X.closePath();X.fill();X.fillStyle='rgba(129,212,250,.7)';X.fillRect(L+430,ty-30,32,28)}
  {const px=L+120,py=1330;X.fillStyle='#455a64';rr(px-30,py-40,60,40,8);X.fill();X.fillStyle='#263238';X.fillRect(px-4,py-150,8,110);X.fillStyle='#212121';X.beginPath();X.arc(px,py-170,26,0,7);X.fill();X.fillStyle='#ff5252';X.beginPath();X.arc(px+14,py-180,4,0,7);X.fill()}
  planta(L+1000,1320,.8)}};

// --- Refugio de animales: caniles con rejas, carteles de adopcion, platos, correas ---
NUEVOS.refugioV={osc:.16,
 luces(z){const F=FV(z);return [{x:F.L+540,y:380,fy:HZ+260,r:520,c:'255,240,210',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#f0e6c8',p1:'#d8c9a0',piso:['#9e9e9e','#8f8f8f'],paso:140,linea:'rgba(0,0,0,.18)',t0:'#6d6250',t1:'#a89a7c',cornisa:'#fff3d6'});
  X.fillStyle='#e65100';X.fillRect(L+140,440,800,90);txt('ADOPT ME',L+540,486,54,'#fff',{w:800});X.fillStyle='rgba(0,0,0,.2)';X.fillRect(L+140,530,800,8);
  for(let i=0;i<3;i++){const kx=L+40+i*340,ky=640;X.fillStyle='#bfa98a';X.fillRect(kx,ky,320,640);X.fillStyle=gl(0,ky,0,ky+640,[[0,'#5d4e3c'],[1,'#3e3428']]);X.fillRect(kx+16,ky+16,288,608);
   camaPerro(kx+160,ky+600,1,['#1e88e5','#e53935','#43a047'][i]);platoMascota(kx+70,ky+610,.7,'#fbc02d',true);
   X.strokeStyle='#9e9e9e';X.lineWidth=7;for(let b=0;b<9;b++){X.beginPath();X.moveTo(kx+20+b*35,ky+16);X.lineTo(kx+20+b*35,ky+624);X.stroke()}X.lineWidth=10;X.beginPath();X.moveTo(kx+16,ky+300);X.lineTo(kx+304,ky+300);X.stroke();
   X.fillStyle='#fffde7';X.save();X.translate(kx+160,ky+90);X.rotate((i-1)*.05);X.fillRect(-70,-40,140,80);X.fillStyle='#e53935';X.beginPath();X.moveTo(0,-14);X.bezierCurveTo(-24,-36,-40,-6,0,20);X.bezierCurveTo(40,-6,24,-36,0,-14);X.fill();X.restore()}
  for(let i=0;i<4;i++){X.strokeStyle=['#e53935','#1e88e5','#43a047','#fb8c00'][i];X.lineWidth=6;X.beginPath();X.moveTo(L+1050+i*0,600+i*30);X.quadraticCurveTo(L+1070,700+i*40,L+1050,780+i*40);X.stroke()}}};

// --- Cafe otomano (Estambul, 1600s): arcos, alfombras, cojines bajos, cafeteras de cobre, faroles ---
function farol(x,y,s,t,col='#ffb74d'){X.save();X.translate(x,y);X.scale(s,s);X.strokeStyle='#5d4037';X.lineWidth=3;X.beginPath();X.moveTo(0,-200);X.lineTo(0,-60);X.stroke();X.fillStyle='#8d6e63';X.beginPath();X.moveTo(-26,-60);X.lineTo(26,-60);X.lineTo(14,-74);X.lineTo(-14,-74);X.closePath();X.fill();
 glow(col,30,()=>{X.fillStyle=col;X.beginPath();X.moveTo(-24,-56);X.lineTo(24,-56);X.lineTo(30,10);X.lineTo(0,34);X.lineTo(-30,10);X.closePath();X.fill()});X.strokeStyle='#5d4037';X.lineWidth=3;for(let k=-1;k<=1;k++){X.beginPath();X.moveTo(k*12,-56);X.lineTo(k*16,10);X.stroke()}
 X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,0,4,0,0,220);g.addColorStop(0,`rgba(255,180,90,${.35+.05*Math.sin(t*9+x)})`);g.addColorStop(1,'rgba(255,180,90,0)');X.fillStyle=g;X.beginPath();X.arc(0,0,220,0,7);X.fill();X.restore();X.restore()}
function cezve(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle=gl(-30,0,30,0,[[0,'#8a4b20'],[.5,'#e0915a'],[1,'#7a3f18']]);X.beginPath();X.moveTo(-28,0);X.lineTo(28,0);X.lineTo(22,-50);X.lineTo(30,-60);X.lineTo(-30,-60);X.lineTo(-22,-50);X.closePath();X.fill();X.fillStyle='#5d3a1a';X.fillRect(26,-46,70,8);X.restore()}
function dallah(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle=gl(-40,0,40,0,[[0,'#9a6a1f'],[.5,'#f0c860'],[1,'#8a5a14']]);X.beginPath();X.moveTo(-40,0);X.quadraticCurveTo(-50,-60,-24,-80);X.lineTo(-18,-120);X.quadraticCurveTo(0,-150,18,-120);X.lineTo(24,-80);X.quadraticCurveTo(50,-60,40,0);X.closePath();X.fill();
 X.beginPath();X.moveTo(30,-70);X.quadraticCurveTo(80,-90,90,-130);X.lineTo(80,-130);X.quadraticCurveTo(70,-96,26,-80);X.fill();X.fillStyle='#f0c860';X.beginPath();X.arc(0,-150,8,0,7);X.fill();X.restore()}
function arcoMorisco(x,y,w,h,col){X.save();X.fillStyle=col;X.beginPath();X.moveTo(x,y+h);X.lineTo(x,y+w*.6);X.quadraticCurveTo(x,y,x+w/2,y-w*.15);X.quadraticCurveTo(x+w,y,x+w,y+w*.6);X.lineTo(x+w,y+h);X.closePath();X.fill();X.restore()}
function alfombraPared(x,y,w,h,c1,c2){X.fillStyle=c1;X.fillRect(x,y,w,h);X.strokeStyle=c2;X.lineWidth=8;X.strokeRect(x+14,y+14,w-28,h-28);X.fillStyle=c2;X.beginPath();X.moveTo(x+w/2,y+40);X.lineTo(x+w-40,y+h/2);X.lineTo(x+w/2,y+h-40);X.lineTo(x+40,y+h/2);X.closePath();X.fill();X.fillStyle='#f3d27a';X.beginPath();X.moveTo(x+w/2,y+h*.3);X.lineTo(x+w*.7,y+h/2);X.lineTo(x+w/2,y+h*.7);X.lineTo(x+w*.3,y+h/2);X.closePath();X.fill()}
NUEVOS.cafeOtomanoV={osc:.38,
 luces(z){const F=FV(z);return [{x:F.L+300,y:760,fy:HZ+240,r:320,c:'255,180,100',panel:1},{x:F.L+800,y:760,fy:HZ+240,r:320,c:'255,180,100',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z);
  cuartoV(F,{p0:'#d9b48a',p1:'#b88a5c',piso:['#8a5a3a','#7a4e30'],paso:120,t0:'#3a2416',t1:'#6b4426',vigas:'#2a1a0e',cornisa:'#c9a06a'});
  for(let i=0;i<3;i++){const ax=L-20+i*380;arcoMorisco(ax,560,300,720,'#2a1a10');X.save();X.beginPath();X.rect(ax+12,560,276,720);X.clip();
    if(i===1){cielo(ax,500,300,780,'noche',t,17);X.fillStyle='#1a1426';X.beginPath();X.arc(ax+150,1000,110,Math.PI,0);X.fill();X.fillRect(ax+40,1000,220,300);X.fillRect(ax+20,820,14,260);X.fillRect(ax+266,820,14,260);X.beginPath();X.moveTo(ax+20,820);X.lineTo(ax+27,780);X.lineTo(ax+34,820);X.fill();X.beginPath();X.moveTo(ax+266,820);X.lineTo(ax+273,780);X.lineTo(ax+280,820);X.fill()}
    else alfombraPared(ax+40,680,220,420,i?'#7a1d22':'#1f3a5f','#e8b04a');X.restore();X.strokeStyle='#c9a06a';X.lineWidth=10;X.beginPath();X.moveTo(ax,1280);X.lineTo(ax,560+300*.6);X.quadraticCurveTo(ax,560,ax+150,515);X.quadraticCurveTo(ax+300,560,ax+300,560+300*.6);X.lineTo(ax+300,1280);X.stroke()}
  farol(L+300,780,1,t);farol(L+800,760,1,t,'#ffcc80');
  alfombraPersa(F.cx,1420,1000,1800,'#8e1b2b','#1f3a5f');
  for(let i=0;i<4;i++){const cx=L+120+i*280;X.fillStyle=['#c62828','#1565c0','#2e7d32','#f9a825'][i];rr(cx-90,1330,180,60,24);X.fill();X.fillStyle='rgba(255,255,255,.15)';X.fillRect(cx-80,1334,160,6);X.fillStyle='#e8b04a';X.fillRect(cx-90,1378,180,8)}
  {const tx=F.cx;X.fillStyle='#b07a30';X.beginPath();X.ellipse(tx,1450,120,26,0,0,7);X.fill();X.fillStyle='#e0a84a';X.beginPath();X.ellipse(tx,1444,112,20,0,0,7);X.fill();X.fillStyle='#6b4426';X.fillRect(tx-8,1450,16,60);
   dallah(tx-40,1440,.6);[0,1,2].forEach(k=>{X.fillStyle='#fafafa';X.fillRect(tx+20+k*28,1424,20,18);X.fillStyle='#4e2a14';X.fillRect(tx+22+k*28,1424,16,4)})}
  {const sx=L+840;X.fillStyle='#5d3a1a';X.fillRect(sx,1100,220,180);X.fillStyle='#3e2510';X.fillRect(sx-10,1090,240,16);cezve(sx+60,1090,1);cezve(sx+150,1090,.8);
   X.save();X.globalAlpha*=.3;for(let k=0;k<3;k++){X.strokeStyle='#fff';X.lineWidth=5;X.beginPath();const ox=Math.sin(t*1.5+k)*10;X.moveTo(sx+50+k*10,1030);X.bezierCurveTo(sx+40+ox,980,sx+70+ox,940,sx+50+k*10,890);X.stroke()}X.restore()}}};

// --- Calle de Estambul de noche: cupulas y minaretes, casas de madera con balcones, adoquines, faroles ---
NUEVOS.estambulV={osc:.45,
 luces(z){const F=FV(z);return [{x:F.L+260,y:900,fy:HZ+240,r:300,c:'255,190,110',panel:1},{x:F.L+860,y:960,fy:HZ+240,r:280,c:'255,190,110',panel:1},{x:F.L+700,y:200,fy:HZ+100,r:300,c:'200,215,255',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cielo(L-120,-300,1320,1600,'noche',t,29);
  X.fillStyle='#141a2e';X.beginPath();X.arc(F.cx,820,230,Math.PI,0);X.fill();X.fillRect(F.cx-260,820,520,300);X.beginPath();X.arc(F.cx-200,880,90,Math.PI,0);X.arc(F.cx+200,880,90,Math.PI,0);X.fill();
  [F.cx-330,F.cx+330].forEach(mx=>{X.fillRect(mx-16,420,32,700);X.fillRect(mx-24,640,48,16);X.fillRect(mx-22,520,44,14);X.beginPath();X.moveTo(mx-16,420);X.lineTo(mx,330);X.lineTo(mx+16,420);X.fill()});
  X.fillStyle='rgba(255,210,120,.65)';for(let i=0;i<6;i++){X.fillRect(F.cx-180+i*60,960,22,40)}
  for(let s=0;s<2;s++){const hx=s?L+700:L-80,hw=460;X.fillStyle=s?'#5a3a28':'#6b3f2a';X.fillRect(hx,700,hw,600);X.fillStyle=s?'#4a2e1e':'#55311f';X.fillRect(hx-10,690,hw+20,24);X.fillRect(hx+(s?-30:60),880,hw*.8,180);
   for(let r=0;r<3;r++)for(let c=0;c<3;c++){const on=rnd(r*7+c+s*11)>.4;X.fillStyle=on?'rgba(255,200,110,.9)':'#1e140e';X.fillRect(hx+50+c*140,740+r*170,70,100);X.strokeStyle='#3a2416';X.lineWidth=5;X.strokeRect(hx+50+c*140,740+r*170,70,100)}
   X.fillStyle='#2a1a10';X.fillRect(hx+(s?60:300),1120,100,180)}
  X.fillStyle='#3a3a44';X.fillRect(L-120,1300,1320,700);for(let r=0;r<12;r++)for(let c=0;c<16;c++){const yy=1300+r*r*4.4+r*14,xx=L-120+c*90+(r%2)*45;X.fillStyle=rnd(r*16+c)>.5?'#4a4a56':'#42424d';X.beginPath();X.ellipse(F.cx+(xx-F.cx)*(1+r*.08),yy+10,40+r*2,8+r*1.2,0,0,7);X.fill()}
  if(O(z).var){for(let i=0;i<2;i++){const sx=L+60+i*620,sy=1290;X.fillStyle='#5d3a1a';X.fillRect(sx,sy-200,14,200);X.fillRect(sx+380,sy-200,14,200);for(let k=0;k<6;k++){X.fillStyle=k%2?'#c62828':'#f3e3c0';X.beginPath();X.moveTo(sx-20+k*70,sy-200);X.lineTo(sx+50+k*70,sy-200);X.lineTo(sx+50+k*70,sy-150);X.quadraticCurveTo(sx+15+k*70,sy-130,sx-20+k*70,sy-150);X.closePath();X.fill()}
   X.fillStyle='#7a5230';X.fillRect(sx,sy-60,394,20);for(let k=0;k<4;k++){X.fillStyle=['#8d6e63','#a1887f','#6d4c41','#bcaaa4'][k];X.beginPath();X.ellipse(sx+50+k*95,sy-70,40,30,0,Math.PI,0);X.fill();X.fillStyle='#3e2412';X.beginPath();X.ellipse(sx+50+k*95,sy-90,30,8,0,0,7);X.fill()}}}
  farol(L+260,1050,1.1,t);farol(L+860,1110,1,t)}};

// --- Palacio / sala del trono (o.estilo: 'otomano' | 'etiope'): columnas, dosel, alfombra larga, guardias decorativos, braseros ---
NUEVOS.palacioV={osc:.3,
 luces(z){const F=FV(z);return [{x:F.cx,y:600,fy:HZ+220,r:480,c:'255,200,120',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L,o=O(z),et=o.estilo==='etiope';
  cuartoV(F,{p0:et?'#7a3e1d':'#2c4a6e',p1:et?'#4e2410':'#1b2f4a',piso:et?['#a0522d','#8b4513']:['#d8d0c0','#c8bfae'],paso:120,t0:'#1a1208',t1:'#3a2816',cornisa:'#d4af37'});
  X.fillStyle='rgba(212,175,55,.18)';for(let r=0;r<7;r++)for(let c=0;c<9;c++){const px=L-40+c*140+(r%2)*70,py=440+r*120;X.beginPath();X.moveTo(px,py-24);X.lineTo(px+20,py);X.lineTo(px,py+24);X.lineTo(px-20,py);X.closePath();X.fill()}
  [L+60,L+1020].forEach(cx=>{X.fillStyle=gl(cx-40,0,cx+40,0,[[0,'#b8a880'],[.5,'#f0e6c8'],[1,'#a89870']]);X.fillRect(cx-40,420,80,880);X.fillStyle='#d4af37';X.fillRect(cx-54,400,108,30);X.fillRect(cx-54,1270,108,30)});
  {const cx=F.cx;X.fillStyle=et?'#1b5e20':'#8e1b2b';X.beginPath();X.moveTo(cx-260,440);X.lineTo(cx+260,440);X.lineTo(cx+300,560);X.lineTo(cx-300,560);X.closePath();X.fill();X.fillStyle='#d4af37';X.fillRect(cx-300,556,600,10);
   for(let s of [-1,1]){X.fillStyle=et?'#2e7d32':'#a01d30';X.beginPath();X.moveTo(cx+s*280,560);X.quadraticCurveTo(cx+s*330,900,cx+s*270,1280);X.lineTo(cx+s*230,1280);X.quadraticCurveTo(cx+s*270,900,cx+s*240,560);X.closePath();X.fill()}
   if(et){[['#2e7d32',0],['#fdd835',1],['#c62828',2]].forEach(([c,i])=>{X.fillStyle=c;X.fillRect(cx-160,640+i*40,320,40)})}else{X.fillStyle='#d4af37';X.beginPath();X.arc(cx,720,70,0,7);X.fill();X.fillStyle='#8e1b2b';X.beginPath();X.arc(cx+18,712,60,0,7);X.fill();X.fillStyle='#d4af37';X.beginPath();X.arc(cx+40,712,14,0,7);X.fill()}
   X.fillStyle='#5d3a1a';X.fillRect(cx-170,1240,340,60);X.fillStyle='#d4af37';X.fillRect(cx-180,1232,360,14)}
  {X.fillStyle=et?'#6d1b1b':'#7a1d22';X.beginPath();X.moveTo(F.cx-170,1300);X.lineTo(F.cx+170,1300);X.lineTo(F.cx+330,1920);X.lineTo(F.cx-330,1920);X.closePath();X.fill();X.strokeStyle='#d4af37';X.lineWidth=8;X.stroke()}
  [L+200,L+880].forEach((bx,i)=>{X.fillStyle='#5d4037';X.fillRect(bx-10,1180,20,120);X.fillStyle='#d4af37';X.beginPath();X.ellipse(bx,1180,60,16,0,0,7);X.fill();X.save();X.globalCompositeOperation='lighter';for(let k=0;k<5;k++){const fh=60+Math.sin(t*8+k*2+i)*20;const g=X.createLinearGradient(0,1180,0,1180-fh);g.addColorStop(0,'rgba(255,170,40,.9)');g.addColorStop(1,'rgba(255,80,10,0)');X.fillStyle=g;X.beginPath();X.moveTo(bx-40+k*16,1176);X.quadraticCurveTo(bx-32+k*16,1176-fh*.6,bx-30+k*16+Math.sin(t*6+k)*6,1176-fh);X.quadraticCurveTo(bx-26+k*16,1176-fh*.5,bx-20+k*16,1176);X.fill()}X.restore()})}};

// --- Ceremonia del cafe etiope: jebena de barro, tacitas en bandeja, incienso, pasto fresco en el piso, taburete bajo ---
function jebena(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle=gl(-50,0,50,0,[[0,'#2a1a10'],[.5,'#5a3a24'],[1,'#21140c']]);X.beginPath();X.arc(0,-50,52,0,7);X.fill();X.fillRect(-12,-150,24,70);X.beginPath();X.moveTo(-18,-150);X.lineTo(18,-150);X.lineTo(14,-160);X.lineTo(-14,-160);X.closePath();X.fill();
 X.strokeStyle='#3a2416';X.lineWidth=10;X.beginPath();X.moveTo(40,-80);X.quadraticCurveTo(80,-90,60,-30);X.stroke();X.beginPath();X.moveTo(-40,-70);X.lineTo(-74,-100);X.stroke();X.strokeStyle='#d4af37';X.lineWidth=3;X.beginPath();X.arc(0,-50,40,.3,2.8);X.stroke();X.fillStyle='rgba(255,255,255,.18)';X.beginPath();X.ellipse(-18,-70,10,18,-.4,0,7);X.fill();X.restore()}
NUEVOS.ceremoniaV={osc:.3,
 luces(z){const F=FV(z);return [{x:F.L+640,y:900,fy:HZ+250,r:420,c:'255,190,120',panel:1}]},
 fondo(z,t,q){const F=FV(z),L=F.L;
  cuartoV(F,{p0:'#e8c89a',p1:'#c9a06a',piso:['#7a5a3a','#6b4e30'],paso:120,t0:'#3a2614',t1:'#6b4a2a',cornisa:'#a0522d'});
  for(let i=0;i<3;i++){const y=500+i*16;X.fillStyle=['#2e7d32','#fdd835','#c62828'][i];X.fillRect(L-120,y,1320,14)}
  {const tx=L+120;X.fillStyle='#f5ecd8';X.fillRect(tx,640,320,420);X.strokeStyle='#a0522d';X.lineWidth=10;X.strokeRect(tx,640,320,420);for(let i=0;i<6;i++){X.fillStyle=['#c62828','#2e7d32','#fdd835'][i%3];X.fillRect(tx+20+i*48,670,30,30);X.fillRect(tx+20+i*48,1010,30,30)}X.fillStyle='#6d4c41';X.beginPath();X.arc(tx+160,850,90,0,7);X.fill();X.fillStyle='#8d6e63';X.beginPath();X.arc(tx+160,850,60,0,7);X.fill()}
  {const bx=L+620;X.fillStyle='#8d6e63';X.fillRect(bx,700,360,24);X.fillRect(bx,880,360,24);for(let k=0;k<5;k++){X.fillStyle=['#c62828','#f9a825','#2e7d32','#1565c0','#6d4c41'][k];X.beginPath();X.ellipse(bx+40+k*70,680,26,20,0,0,7);X.fill();X.beginPath();X.ellipse(bx+40+k*70,860,26,20,0,0,7);X.fill()}}
  X.fillStyle='#4caf50';for(let i=0;i<220;i++){const gx=L-60+rnd(i)*1200,gy=1380+rnd(i*3)*480;X.save();X.translate(gx,gy);X.rotate((rnd(i*7)-.5)*.8);X.fillRect(-2,-26-rnd(i+2)*20,4,30);X.restore()}
  {const cx=F.cx+40,cy=1560;X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(cx+10,cy+16,300,40,0,0,7);X.fill();X.fillStyle='#6d4c2e';X.beginPath();X.ellipse(cx,cy,290,36,0,0,7);X.fill();X.fillStyle='#8d6e4a';X.beginPath();X.ellipse(cx,cy-6,280,30,0,0,7);X.fill();
   for(let k=0;k<6;k++){const px=cx-150+k*60;X.fillStyle='#fafafa';X.beginPath();X.moveTo(px-18,cy-14);X.lineTo(px+18,cy-14);X.lineTo(px+12,cy-44);X.lineTo(px-12,cy-44);X.closePath();X.fill();X.fillStyle='#1565c0';X.fillRect(px-14,cy-34,28,4);X.fillStyle='#3e2412';X.beginPath();X.ellipse(px,cy-44,12,3,0,0,7);X.fill()}
   jebena(cx+220,cy-10,1);X.fillStyle='#3e2a1a';X.fillRect(cx-260,cy-40,50,30);
   X.save();X.globalAlpha*=.35;for(let k=0;k<3;k++){X.strokeStyle='#fff';X.lineWidth=4;X.beginPath();const ox=Math.sin(t*1.2+k*2)*16;X.moveTo(cx-236+k*8,cy-44);X.bezierCurveTo(cx-250+ox,cy-140,cx-210+ox,cy-220,cx-240+k*10,cy-330);X.stroke()}X.restore()}
  {const sx=L+160,sy=1500;X.fillStyle='#5d3a1a';X.fillRect(sx-60,sy-60,120,20);X.fillRect(sx-50,sy-40,14,40);X.fillRect(sx+36,sy-40,14,40)}}};
