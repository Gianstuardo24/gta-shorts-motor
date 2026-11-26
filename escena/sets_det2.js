// ===== ESCENARIOS DETALLADOS · tanda 2 (despacho 80s, casona, estudio de animacion, sala de directorio, mesa cenital) =====
function O(z){return z.o||{}}
function cielo(x,y,w,h,hora,t,sem=1){let c;if(hora==='noche')c=[[0,'#0b1330'],[1,'#27325a']];else if(hora==='tarde')c=[[0,'#3b3f8f'],[.55,'#e0727a'],[1,'#ffc98a']];else c=[[0,'#7fb3e3'],[1,'#d8ecfb']];
 X.fillStyle=gl(0,y,0,y+h,c);X.fillRect(x,y,w,h);
 if(hora==='noche'){for(let i=0;i<40;i++){X.fillStyle=`rgba(255,255,255,${.3+.6*rnd(i+sem)})`;X.fillRect(x+rnd(i*3+sem)*w,y+rnd(i*7+sem)*h*.6,2,2)}X.fillStyle='#f2f4ff';glow('#dfe6ff',30,()=>{X.beginPath();X.arc(x+w*.78,y+h*.22,22,0,7);X.fill()})}}
function skyline(x,y,w,h,hora,sem=3){for(let i=0;i*58<w+40;i++){const bh=h*(.35+rnd(i+sem)*.6),bw=44+rnd(i*5+sem)*30,bx=x+i*58-10;const noche=hora==='noche';X.fillStyle=noche?`rgb(${22+i%3*6},${28+i%4*5},${52+i%3*8})`:hora==='tarde'?`rgb(${90+i%3*12},${70+i%4*8},${110})`:`rgb(${140+i%3*10},${158+i%4*8},${182})`;X.fillRect(bx,y+h-bh,bw,bh);
 for(let r=0;r<bh/20-1;r++)for(let c=0;c<3;c++){const on=rnd(i*31+r*7+c+sem)>(noche?.55:.2);X.fillStyle=noche?(on?'rgba(255,214,130,.85)':'rgba(0,0,0,0)'):'rgba(255,255,255,.35)';X.fillRect(bx+5+c*(bw-10)/3,y+h-bh+7+r*20,(bw-10)/3-5,8)}}}
function cortina(x,y,w,h,col,lado,t){X.save();const n=6;for(let i=0;i<n;i++){const xx=x+i*w/n,g=gl(xx,0,xx+w/n,0,[[0,col[1]],[.5,col[0]],[1,col[1]]]);X.fillStyle=g;X.beginPath();X.moveTo(xx,y);X.lineTo(xx+w/n+1,y);const tie=lado<0?(1-i/n):(i/n);X.quadraticCurveTo(xx+w/n-tie*30*lado,y+h*.55,xx+w/n+1-tie*40*lado,y+h);X.lineTo(xx-tie*40*lado,y+h);X.quadraticCurveTo(xx-tie*30*lado,y+h*.55,xx,y);X.closePath();X.fill()}
 X.fillStyle='#d4af37';X.fillRect(x-10,y-14,w+20,12);X.restore()}
function librero(x,y,w,h,sem=1,deco=true){X.fillStyle='#3b2416';X.fillRect(x-10,y-10,w+20,h+20);X.fillStyle='#2a180e';X.fillRect(x,y,w,h);const fil=Math.floor(h/120);
 for(let r=0;r<fil;r++){const sy=y+r*(h/fil),sh=h/fil;X.fillStyle='#4a2e1b';X.fillRect(x,sy+sh-12,w,12);let bx=x+6;let k=0;while(bx<x+w-14){const bw=10+rnd(k+r*17+sem)*14,bh=sh*(.55+rnd(k*3+r+sem)*.33);
   if(deco&&rnd(k*11+r+sem)>.93&&bx<x+w-70){X.fillStyle='#c9a227';X.beginPath();X.arc(bx+22,sy+sh-36,20,0,7);X.fill();X.fillStyle='#6d4c2e';X.fillRect(bx+19,sy+sh-16,6,6);bx+=52;k++;continue}
   const cols=['#7b1f1f','#1f3a5f','#2e5e3a','#6b4f2a','#3d2b56','#8a6d3b','#5c1a2b','#1e4d4d'];X.fillStyle=cols[Math.floor(rnd(k*7+r+sem)*cols.length)];const tilt=rnd(k*13+r)>.9?.12:0;X.save();X.translate(bx,sy+sh-12);X.rotate(tilt);X.fillRect(0,-bh,bw,bh);X.fillStyle='rgba(255,215,120,.6)';X.fillRect(2,-bh+10,bw-4,3);X.fillRect(2,-14,bw-4,2);X.fillStyle='rgba(0,0,0,.25)';X.fillRect(bw-3,-bh,3,bh);X.restore();bx+=bw+1+(tilt?8:0);k++}}}
function cuadroPaisaje(x,y,w,h,sem=1){X.fillStyle='rgba(0,0,0,.3)';X.fillRect(x-14,y-10,w+34,h+30);X.fillStyle=gl(x,0,x+w,0,[[0,'#8a6a1f'],[.5,'#e2c26a'],[1,'#8a6a1f']]);X.fillRect(x-18,y-18,w+36,h+36);X.fillStyle='#6b4f16';X.fillRect(x-6,y-6,w+12,h+12);
 X.save();X.beginPath();X.rect(x,y,w,h);X.clip();X.fillStyle=gl(0,y,0,y+h,[[0,'#f3b46b'],[.5,'#f7dca0'],[1,'#7a9a6a']]);X.fillRect(x,y,w,h);X.fillStyle='rgba(255,240,200,.9)';X.beginPath();X.arc(x+w*.7,y+h*.42,h*.12,0,7);X.fill();
 X.fillStyle='#5f7d55';X.beginPath();X.moveTo(x,y+h*.7);X.quadraticCurveTo(x+w*.3,y+h*.45,x+w*.55,y+h*.66);X.quadraticCurveTo(x+w*.8,y+h*.5,x+w,y+h*.62);X.lineTo(x+w,y+h);X.lineTo(x,y+h);X.fill();X.fillStyle='#3e5a3c';X.beginPath();X.moveTo(x,y+h*.85);X.quadraticCurveTo(x+w*.5,y+h*.7,x+w,y+h*.86);X.lineTo(x+w,y+h);X.lineTo(x,y+h);X.fill();
 X.fillStyle='#2f3f2a';X.fillRect(x+w*.2,y+h*.52,4,h*.2);X.beginPath();X.arc(x+w*.2+2,y+h*.5,h*.09,0,7);X.fill();X.restore()}
function planta(x,y,s){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,70,12,.4);X.fillStyle=gl(-40,0,40,0,[[0,'#7a3b22'],[.5,'#b5603a'],[1,'#6b321d']]);X.beginPath();X.moveTo(-42,-80);X.lineTo(42,-80);X.lineTo(32,0);X.lineTo(-32,0);X.closePath();X.fill();X.fillStyle='#5a2a17';X.fillRect(-46,-90,92,14);
 for(let i=0;i<16;i++){const a=-Math.PI/2+(rnd(i)-.5)*2.2,l=110+rnd(i+5)*120;X.strokeStyle='#2f5a2a';X.lineWidth=4;X.beginPath();X.moveTo(0,-88);X.quadraticCurveTo(Math.cos(a)*l*.4,-88+Math.sin(a)*l*.6,Math.cos(a)*l*.7,-88+Math.sin(a)*l);X.stroke();X.fillStyle=i%3?'#3f7a35':'#5a9a46';X.save();X.translate(Math.cos(a)*l*.7,-88+Math.sin(a)*l);X.rotate(a+Math.PI/2);X.beginPath();X.ellipse(0,0,16,34,0,0,7);X.fill();X.restore()}X.restore()}
function lamparaBanquero(x,y,s,on=true){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#b08d3a';X.beginPath();X.ellipse(0,0,40,9,0,0,7);X.fill();X.fillRect(-4,-70,8,70);X.fillStyle=gl(0,-100,0,-70,[[0,'#2f8a55'],[1,'#145c34']]);X.beginPath();X.moveTo(-70,-74);X.quadraticCurveTo(0,-112,70,-74);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.3)';X.fillRect(-50,-92,60,3);
 if(on){X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,-40,4,0,-20,190);g.addColorStop(0,'rgba(255,225,160,.45)');g.addColorStop(1,'rgba(255,225,160,0)');X.fillStyle=g;X.beginPath();X.arc(0,-20,190,0,7);X.fill();X.restore()}X.restore()}
function alfombraPersa(cx,y0,w,y1,c1,c2){const P=(x,yy)=>cx+(x-cx)*(1+(yy-y0)/900);X.save();X.beginPath();X.moveTo(P(cx-w/2,y0),y0);X.lineTo(P(cx+w/2,y0),y0);X.lineTo(P(cx+w/2,y1),y1);X.lineTo(P(cx-w/2,y1),y1);X.closePath();X.fillStyle=c1;X.fill();X.clip();
 X.strokeStyle=c2;X.lineWidth=10;X.beginPath();X.moveTo(P(cx-w/2+30,y0+14),y0+14);X.lineTo(P(cx+w/2-30,y0+14),y0+14);X.lineTo(P(cx+w/2-30,y1-24),y1-24);X.lineTo(P(cx-w/2+30,y1-24),y1-24);X.closePath();X.stroke();
 X.lineWidth=3;X.strokeStyle='#e8c98a';X.beginPath();X.moveTo(P(cx-w/2+50,y0+30),y0+30);X.lineTo(P(cx+w/2-50,y0+30),y0+30);X.lineTo(P(cx+w/2-50,y1-44),y1-44);X.lineTo(P(cx-w/2+50,y1-44),y1-44);X.closePath();X.stroke();
 const my=(y0+y1)/2;X.fillStyle=c2;X.beginPath();X.ellipse(cx,my,w*.18,(y1-y0)*.25,0,0,7);X.fill();X.fillStyle='#e8c98a';X.beginPath();X.ellipse(cx,my,w*.08,(y1-y0)*.11,0,0,7);X.fill();
 for(let i=0;i<10;i++){const xx=cx-w/2+80+i*(w-160)/9;X.fillStyle=i%2?'#e8c98a':c2;X.beginPath();X.arc(P(xx,y0+60),y0+60,7,0,7);X.fill();X.beginPath();X.arc(P(xx,y1-70),y1-70,9,0,7);X.fill()}X.restore()}
function pisoMadera(x0,x1,cx,y0,y1,c){pisoPersp(x0,x1,cx,y0,y1,110,c||['#6b4a30','#5e3f28','#73512f'],'rgba(0,0,0,.25)')}
function sillonOrejero(x,y,s,col,dir=1){X.save();X.translate(x,y);X.scale(s*dir,s);somb(0,0,120,16,.5);X.fillStyle='#2a170c';X.fillRect(-90,-30,14,30);X.fillRect(76,-30,14,30);
 X.fillStyle=gl(-90,0,90,0,[[0,col[1]],[.5,col[0]],[1,col[1]]]);rr(-80,-300,160,200,40);X.fill();X.beginPath();X.moveTo(-80,-280);X.quadraticCurveTo(-130,-270,-118,-200);X.lineTo(-104,-120);X.lineTo(-80,-120);X.closePath();X.fill();X.beginPath();X.moveTo(80,-280);X.quadraticCurveTo(130,-270,118,-200);X.lineTo(104,-120);X.lineTo(80,-120);X.closePath();X.fill();
 X.fillStyle=col[1];rr(-112,-150,48,120,20);X.fill();rr(64,-150,48,120,20);X.fill();X.fillStyle=col[0];rr(-74,-130,148,60,18);X.fill();X.fillStyle=col[1];X.fillRect(-90,-74,180,46);
 X.fillStyle='rgba(0,0,0,.35)';for(let r=0;r<3;r++)for(let c=0;c<4;c++){X.beginPath();X.arc(-48+c*32+(r%2)*16,-270+r*42,4,0,7);X.fill()}X.fillStyle='rgba(255,255,255,.15)';X.fillRect(-70,-296,140,4);X.restore()}
function lamparaTiffany(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#3a2a1a';X.beginPath();X.ellipse(0,0,30,8,0,0,7);X.fill();X.fillRect(-4,-110,8,110);
 const cols=['#d84315','#f9a825','#2e7d32','#1565c0','#f9a825','#d84315'];for(let i=0;i<6;i++){X.fillStyle=cols[i];X.beginPath();X.moveTo(-80+i*26.6,-110);X.lineTo(-80+(i+1)*26.6,-110);X.lineTo(-40+(i+1)*13.3,-170);X.lineTo(-40+i*13.3,-170);X.closePath();X.fill()}
 X.strokeStyle='#3a2a1a';X.lineWidth=2;for(let i=0;i<=6;i++){X.beginPath();X.moveTo(-80+i*26.6,-110);X.lineTo(-40+i*13.3,-170);X.stroke()}X.beginPath();X.moveTo(-80,-130);X.lineTo(80,-130);X.stroke();
 X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,-120,4,0,-100,200);g.addColorStop(0,'rgba(255,190,110,.5)');g.addColorStop(1,'rgba(255,190,110,0)');X.fillStyle=g;X.beginPath();X.arc(0,-100,200,0,7);X.fill();X.restore();X.restore()}
function relojPie(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,70,10,.5);X.fillStyle=gl(-50,0,50,0,[[0,'#3a1f10'],[.5,'#6b3a1f'],[1,'#2e170b']]);X.fillRect(-46,-560,92,560);X.fillRect(-56,-600,112,60);X.beginPath();X.moveTo(-56,-600);X.quadraticCurveTo(0,-650,56,-600);X.fill();
 X.fillStyle='#f3ead2';X.beginPath();X.arc(0,-530,38,0,7);X.fill();X.strokeStyle='#c9a227';X.lineWidth=5;X.stroke();X.strokeStyle='#222';X.lineWidth=3;X.beginPath();X.moveTo(0,-530);X.lineTo(0,-556);X.moveTo(0,-530);X.lineTo(18,-522);X.stroke();
 X.fillStyle='rgba(20,10,4,.85)';rr(-30,-470,60,300,10);X.fill();const a=Math.sin(t*3.1)*.28;X.save();X.translate(0,-466);X.rotate(a);X.strokeStyle='#c9a227';X.lineWidth=3;X.beginPath();X.moveTo(0,0);X.lineTo(0,220);X.stroke();X.fillStyle='#e8c35a';X.beginPath();X.arc(0,230,18,0,7);X.fill();X.restore();
 X.fillStyle='rgba(255,255,255,.12)';X.fillRect(-26,-468,8,296);X.restore()}
function chimenea(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);
 X.fillStyle=gl(-220,0,220,0,[[0,'#cfc6b8'],[.5,'#efe8dc'],[1,'#bfb5a6']]);X.fillRect(-210,-430,420,430);X.fillStyle='#e9e2d6';X.fillRect(-240,-450,480,30);X.fillStyle='#d8d0c2';X.fillRect(-230,-424,460,10);
 X.fillStyle='rgba(0,0,0,.12)';for(let i=0;i<6;i++)X.fillRect(-200+i*80,-410,3,410);
 X.fillStyle='#1a0f0a';X.beginPath();X.moveTo(-130,0);X.lineTo(-130,-230);X.quadraticCurveTo(0,-300,130,-230);X.lineTo(130,0);X.closePath();X.fill();
 X.fillStyle='#3a2a20';X.fillRect(-100,-30,200,14);for(let i=0;i<3;i++){X.fillStyle='#5d3a22';X.save();X.translate(-50+i*50,-44);X.rotate((i-1)*.15);rr(-55,-12,110,24,10);X.fill();X.restore()}
 X.save();X.globalCompositeOperation='lighter';for(let i=0;i<9;i++){const fx=-80+i*20,fh=90+Math.sin(t*9+i*2.1)*30+rnd(i)*40,fw=26;const g=X.createLinearGradient(0,-50,0,-50-fh);g.addColorStop(0,'rgba(255,170,40,.95)');g.addColorStop(.6,'rgba(255,90,20,.6)');g.addColorStop(1,'rgba(255,60,10,0)');X.fillStyle=g;X.beginPath();X.moveTo(fx-fw,-46);X.quadraticCurveTo(fx-fw*.4+Math.sin(t*7+i)*8,-50-fh*.6,fx+Math.sin(t*5+i)*10,-50-fh);X.quadraticCurveTo(fx+fw*.4,-50-fh*.5,fx+fw,-46);X.closePath();X.fill()}
 const gg=X.createRadialGradient(0,-60,10,0,-60,260);gg.addColorStop(0,`rgba(255,150,60,${.35+.08*Math.sin(t*11)})`);gg.addColorStop(1,'rgba(255,150,60,0)');X.fillStyle=gg;X.beginPath();X.arc(0,-60,260,0,7);X.fill();X.restore();
 X.fillStyle='#222';X.fillRect(150,-130,8,130);X.fillRect(170,-120,8,120);X.fillStyle='#c9a227';X.beginPath();X.arc(154,-134,7,0,7);X.arc(174,-124,7,0,7);X.fill();
 [[-190,1],[190,1]].forEach(([cx])=>{X.fillStyle='#c9a227';X.fillRect(cx-6,-500,12,50);X.fillRect(cx-16,-454,32,6);X.fillStyle='#fff8e1';X.fillRect(cx-5,-540,10,40);glow('#ffcc66',20,()=>{X.fillStyle='#ffcc66';X.beginPath();X.ellipse(cx,-548+Math.sin(t*13+cx)*1.5,5,10,0,0,7);X.fill()})});
 X.fillStyle='#3a2615';rr(-36,-520,72,70,10);X.fill();X.fillStyle='#f3ead2';X.beginPath();X.arc(0,-492,22,0,7);X.fill();X.strokeStyle='#222';X.lineWidth=2;X.beginPath();X.moveTo(0,-492);X.lineTo(0,-506);X.moveTo(0,-492);X.lineTo(10,-488);X.stroke();X.restore()}

// ---- Despacho ejecutivo de los 80 (madera, librero, ventanal con ciudad, escritorio con lampara de banquero). o.hora: dia | tarde | noche ----
NUEVOS.despacho80={get osc(){return .2},
 luces(z){const b=z.x0+100,h=O(z).hora||'dia';const L=[{x:b+1350,y:900,fy:HZ+260,r:420,c:h==='noche'?'150,170,255':'255,236,205',panel:1}];L.push({x:b+700,y:1060,fy:HZ+200,r:300,c:'255,220,150',panel:1});return L},
 fondo(z,t,q){const b=z.x0+100,x0=z.x0,x1=z.x1,w=x1-x0,cx=b+975,o=O(z),h=o.hora||'dia';
  X.fillStyle='#1f140c';X.fillRect(x0,480,w,290);X.fillStyle='#4a2f1c';X.fillRect(x0,752,w,22);X.fillStyle='#6b4528';X.fillRect(x0,744,w,8);
  X.fillStyle=gl(0,774,0,1300,[[0,'#5a3820'],[1,'#3e2614']]);X.fillRect(x0,774,w,526);
  for(let i=0;i*240<w;i++){const px=x0+i*240+20;X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=4;X.strokeRect(px,800,200,300);X.strokeStyle='rgba(255,210,160,.12)';X.lineWidth=2;X.strokeRect(px+6,806,188,288);X.strokeStyle='rgba(0,0,0,.3)';X.lineWidth=3;X.strokeRect(px,1130,200,140)}
  X.fillStyle='#2e1c0f';X.fillRect(x0,1284,w,18);
  {const wx=b+1080,wy=800,ww=560,wh=360;X.fillStyle='#2a1a0e';X.fillRect(wx-24,wy-24,ww+48,wh+48);X.save();X.beginPath();X.rect(wx,wy,ww,wh);X.clip();cielo(wx,wy,ww,wh,h,t,5);skyline(wx,wy+wh*.35,ww,wh*.65,h,7);X.restore();
   X.strokeStyle='#3b2615';X.lineWidth=12;X.beginPath();X.moveTo(wx+ww/3,wy);X.lineTo(wx+ww/3,wy+wh);X.moveTo(wx+2*ww/3,wy);X.lineTo(wx+2*ww/3,wy+wh);X.stroke();X.strokeRect(wx,wy,ww,wh);
   X.fillStyle='rgba(255,255,255,.07)';X.beginPath();X.moveTo(wx+20,wy);X.lineTo(wx+120,wy);X.lineTo(wx+20,wy+200);X.closePath();X.fill();
   cortina(wx-110,wy-30,110,wh+90,['#7a1f2b','#4a0f18'],-1,t);cortina(wx+ww,wy-30,110,wh+90,['#7a1f2b','#4a0f18'],1,t)}
  librero(b+20,800,420,470,9);
  {const dx=b+560,dy=920;X.fillStyle='rgba(0,0,0,.3)';X.fillRect(dx-10,dy-8,260,190);X.fillStyle=gl(dx,0,dx+240,0,[[0,'#8a6a1f'],[.5,'#e2c26a'],[1,'#8a6a1f']]);X.fillRect(dx-12,dy-12,264,194);X.fillStyle='#f6f0e0';X.fillRect(dx,dy,240,170);txt('CERTIFICATE',dx+120,dy+34,18,'#6b4f16',{w:800});X.fillStyle='#b8a57a';for(let l=0;l<4;l++)X.fillRect(dx+40,dy+64+l*18,160-l*20,3);X.fillStyle='#b71c1c';X.beginPath();X.arc(dx+190,dy+138,14,0,7);X.fill()}
  pisoMadera(x0,x1,cx,1300,1950,['#3a2416','#33200f','#40291a']);alfombraPersa(cx,1330,1500,1640,'#5a1620','#1f2f4a');
  X.fillStyle=gl(0,1300,0,1360,[[0,'rgba(0,0,0,.45)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,1300,w,60);
  // escritorio ejecutivo
  {const dx=b+460,ww=620,ty=1176;somb(dx+ww/2,1350,ww*.6,26,.55);X.fillStyle=gl(0,ty,0,1345,[[0,'#5a2c14'],[1,'#3a1a0a']]);X.fillRect(dx+16,ty+24,ww-32,1345-ty-24);
   for(let k=0;k<2;k++){const px=dx+40+k*(ww-250);X.strokeStyle='rgba(255,200,150,.15)';X.lineWidth=3;X.strokeRect(px,ty+48,170,110);X.strokeStyle='rgba(0,0,0,.4)';X.strokeRect(px+8,ty+56,154,94);X.fillStyle='#c9a227';X.beginPath();X.arc(px+85,ty+103,6,0,7);X.fill()}
   X.fillStyle=gl(0,ty-8,0,ty+26,[[0,'#9a5a2e'],[.35,'#7a3f1c'],[1,'#4a220c']]);rr(dx,ty-6,ww,32,6);X.fill();X.fillStyle='rgba(255,230,200,.25)';X.fillRect(dx+6,ty-6,ww-12,3);
   X.fillStyle='#1d3b2a';X.beginPath();X.moveTo(dx+180,ty);X.lineTo(dx+420,ty);X.lineTo(dx+410,ty-8);X.lineTo(dx+190,ty-8);X.closePath();X.fill();
   lamparaBanquero(dx+90,ty-4,1,true);telefono80(dx+520,ty-2);papeles(dx+300,ty-6,4);
   X.fillStyle='#d4af37';X.fillRect(dx+250,ty-30,120,22);X.fillStyle='#2a1a0e';X.fillRect(dx+256,ty-26,108,14);
   X.fillStyle='#1a1a1a';X.fillRect(dx+440,ty-46,12,40);X.fillRect(dx+456,ty-40,10,34);X.fillStyle='#8d6e63';X.fillRect(dx+436,ty-8,36,8)}
  // sillon de cuero detras
  {const sx=b+770;X.save();X.fillStyle=gl(sx-90,0,sx+90,0,[[0,'#2a0e08'],[.5,'#5a1e10'],[1,'#2a0e08']]);rr(sx-90,890,180,300,50);X.fill();X.fillStyle='rgba(0,0,0,.35)';for(let r=0;r<4;r++)for(let c=0;c<4;c++){X.beginPath();X.arc(sx-54+c*36+(r%2)*18,940+r*50,5,0,7);X.fill()}X.fillStyle='rgba(255,200,170,.18)';X.fillRect(sx-70,896,140,5);X.restore()}
  // carrito con licorera de cristal
  {const cx2=b+1760,cy=1300;X.fillStyle='#c9a227';X.fillRect(cx2-90,cy-150,180,8);X.fillRect(cx2-90,cy-60,180,8);X.fillRect(cx2-86,cy-150,6,150);X.fillRect(cx2+80,cy-150,6,150);
   X.fillStyle='rgba(200,230,255,.35)';X.beginPath();X.moveTo(cx2-40,cy-150);X.quadraticCurveTo(cx2-60,cy-200,cx2-30,cy-230);X.lineTo(cx2-30,cy-260);X.lineTo(cx2-14,cy-260);X.lineTo(cx2-14,cy-230);X.quadraticCurveTo(cx2+16,cy-200,cx2-4,cy-150);X.closePath();X.fill();X.fillStyle='rgba(180,90,20,.7)';X.fillRect(cx2-46,cy-190,40,40);
   X.fillStyle='rgba(220,240,255,.5)';X.fillRect(cx2+20,cy-180,24,30);X.fillRect(cx2+52,cy-180,24,30);X.fillStyle='#111';[cx2-70,cx2+70].forEach(wx=>{X.beginPath();X.arc(wx,cy+4,9,0,7);X.fill()})}
  planta(b+1880,1330,1.1)}};

// ---- Casona antigua (victoriana): papel mural, boiserie, chimenea con fuego, reloj de pie, cortinas de terciopelo, sillon orejero ----
NUEVOS.casona={osc:.42,
 luces(z){const b=z.x0+100;return [{x:b+975,y:1180,fy:HZ+230,r:520,c:'255,170,90',panel:1},{x:b+1480,y:1080,fy:HZ+220,r:300,c:'255,200,130',panel:1}]},
 fondo(z,t,q){const b=z.x0+100,x0=z.x0,x1=z.x1,w=x1-x0,cx=b+975,o=O(z),h=o.hora||'noche';
  X.fillStyle='#2a1a10';X.fillRect(x0,480,w,280);X.fillStyle='#e9dcc0';X.fillRect(x0,744,w,26);X.fillStyle='#c8b896';X.fillRect(x0,766,w,6);
  X.fillStyle=gl(0,772,0,1300,[[0,'#2f4a3a'],[1,'#22372b']]);X.fillRect(x0,772,w,528);
  X.fillStyle='rgba(212,175,55,.16)';for(let r=0;r<8;r++)for(let c=0;c*90<w;c++){const px=x0+c*90+(r%2)*45,py=800+r*62;X.beginPath();X.moveTo(px,py-18);X.quadraticCurveTo(px+14,py,px,py+18);X.quadraticCurveTo(px-14,py,px,py-18);X.fill();X.beginPath();X.arc(px,py,4,0,7);X.fill()}
  X.fillStyle=gl(0,1110,0,1300,[[0,'#4a2c18'],[1,'#33200f']]);X.fillRect(x0,1110,w,190);X.fillStyle='#6b4428';X.fillRect(x0,1104,w,10);for(let i=0;i*200<w;i++){X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=3;X.strokeRect(x0+i*200+20,1134,160,130);X.strokeStyle='rgba(255,210,160,.1)';X.strokeRect(x0+i*200+26,1140,148,118)}
  // ventana con cortinas
  {const wx=b+170,wy=820,ww=260,wh=380;X.fillStyle='#e9dcc0';X.fillRect(wx-14,wy-14,ww+28,wh+28);X.save();X.beginPath();X.rect(wx,wy,ww,wh);X.clip();cielo(wx,wy,ww,wh,h,t,11);
   X.fillStyle='#0d0f14';X.beginPath();X.moveTo(wx+150,wy+wh);X.lineTo(wx+160,wy+wh*.55);X.lineTo(wx+170,wy+wh);X.fill();for(let i=0;i<9;i++){X.beginPath();X.arc(wx+120+rnd(i)*110,wy+wh*.42+rnd(i+3)*80,26+rnd(i+7)*20,0,7);X.fill()}X.restore();
   X.strokeStyle='#e9dcc0';X.lineWidth=8;X.beginPath();X.moveTo(wx+ww/2,wy);X.lineTo(wx+ww/2,wy+wh);X.moveTo(wx,wy+wh/3);X.lineTo(wx+ww,wy+wh/3);X.moveTo(wx,wy+2*wh/3);X.lineTo(wx+ww,wy+2*wh/3);X.stroke();
   cortina(wx-120,wy-40,130,wh+110,['#8e1b2b','#4a0b14'],-1,t);cortina(wx+ww-10,wy-40,130,wh+110,['#8e1b2b','#4a0b14'],1,t);X.fillStyle='#4a0b14';X.fillRect(wx-140,wy-60,ww+280,40);X.fillStyle='#d4af37';X.fillRect(wx-140,wy-24,ww+280,6)}
  pisoMadera(x0,x1,cx,1300,1950,['#4a2c18','#3f2514','#53331d']);
  X.fillStyle=gl(0,1300,0,1360,[[0,'rgba(0,0,0,.5)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,1300,w,60);
  cuadroPaisaje(b+855,840,240,160,4);
  chimenea(cx,1330,1,t);
  alfombraPersa(cx,1350,1300,1660,'#7a1d22','#1f2f5a');
  librero(b+1560,800,300,490,13);
  relojPie(b+520,1330,1,t);
  sillonOrejero(b+1350,1395,.95,['#7a2a1a','#4a1408'],-1);
  {const tx=b+1520;X.fillStyle='#3a2414';X.beginPath();X.ellipse(tx,1236,60,12,0,0,7);X.fill();X.fillRect(tx-6,1236,12,110);X.fillRect(tx-40,1340,80,8);lamparaTiffany(tx,1232,1,t)}
  // arana de cristal
  {const ax=cx+20,ay=720;X.strokeStyle='#c9a227';X.lineWidth=4;X.beginPath();X.moveTo(ax,480);X.lineTo(ax,ay-30);X.stroke();X.fillStyle='#c9a227';X.beginPath();X.ellipse(ax,ay,90,14,0,0,7);X.fill();
   for(let i=0;i<7;i++){const px=ax-84+i*28;X.fillStyle='rgba(220,240,255,.8)';X.beginPath();X.moveTo(px,ay+10);X.lineTo(px-5,ay+30);X.lineTo(px,ay+44);X.lineTo(px+5,ay+30);X.closePath();X.fill();X.fillStyle='#fff8e1';X.fillRect(px-3,ay-26,6,20);glow('#ffcc66',18,()=>{X.fillStyle='#ffd27a';X.beginPath();X.ellipse(px,ay-32,4,8,0,0,7);X.fill()})}}}};

// ---- Estudio de animacion a mano (~1983): mesas de luz con disco, barras de registro, bocetos de la pelota que rebota, camara de animacion vertical ----
function mesaAnimacion(x,y,s,t,sem){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,150,16,.45);
 X.fillStyle='#5a3a22';X.fillRect(-130,-170,14,170);X.fillRect(116,-170,14,170);X.fillRect(-130,-60,260,10);
 X.save();X.translate(0,-180);X.rotate(-.02);X.fillStyle=gl(0,-120,0,10,[[0,'#d9b98c'],[1,'#a8865a']]);X.beginPath();X.moveTo(-150,0);X.lineTo(150,0);X.lineTo(126,-130);X.lineTo(-126,-130);X.closePath();X.fill();
 X.fillStyle='#ffffff';X.beginPath();X.ellipse(0,-62,92,52,0,0,7);X.fill();glow('#fffbe6',30,()=>{X.fillStyle='#fffdf2';X.beginPath();X.ellipse(0,-62,82,46,0,0,7);X.fill()});
 X.fillStyle='rgba(30,30,40,.5)';X.lineWidth=2;X.strokeStyle='rgba(30,30,40,.55)';for(let k=0;k<3;k++){X.beginPath();X.arc(-40+k*36,-58-Math.abs(Math.sin(k*1.1))*26,10,0,7);X.stroke()}
 X.fillStyle='#8d8d8d';X.fillRect(-46,-116,92,8);X.fillStyle='#555';X.fillRect(-36,-122,10,8);X.fillRect(-5,-122,10,8);X.fillRect(26,-122,10,8);
 X.fillStyle='#f4efe2';for(let k=0;k<5;k++)X.fillRect(80+k*1.2,-46-k*3,48,6);X.restore();
 X.fillStyle='#6d4c2e';X.fillRect(-150,-196,40,26);for(let k=0;k<5;k++){X.fillStyle=['#e53935','#1e88e5','#fbc02d','#43a047','#212121'][k];X.save();X.translate(-140+k*6,-196);X.rotate(-.2+k*.1);X.fillRect(-2,-34,4,34);X.restore()}
 X.strokeStyle='#2a2a2a';X.lineWidth=5;X.beginPath();X.moveTo(120,-190);X.lineTo(150,-300);X.lineTo(80,-340);X.stroke();X.fillStyle='#37474f';X.save();X.translate(80,-340);X.rotate(.7);X.beginPath();X.moveTo(-14,-8);X.lineTo(14,-8);X.lineTo(26,20);X.lineTo(-26,20);X.closePath();X.fill();X.restore();X.restore()}
function camaraAnimacion(x,y,s,t){X.save();X.translate(x,y);X.scale(s,s);somb(0,0,170,18,.5);X.fillStyle='#3a3f47';X.fillRect(-150,-140,300,140);X.fillStyle='#2a2e34';X.fillRect(-160,-160,320,24);
 X.fillStyle=gl(-14,0,14,0,[[0,'#9aa3ad'],[1,'#5b636d']]);X.fillRect(-120,-720,24,560);X.fillRect(96,-720,24,560);
 X.fillStyle='#2b2f36';rr(-70,-690,140,110,10);X.fill();X.fillStyle='#111';X.beginPath();X.arc(0,-570,26,0,7);X.fill();X.fillStyle='#455a64';X.beginPath();X.arc(0,-570,14,0,7);X.fill();
 X.fillStyle='#1d2026';rr(-50,-760,100,70,8);X.fill();X.fillStyle='#c62828';X.beginPath();X.arc(36,-740,5,0,7);X.fill();
 X.fillStyle='#f6f2e6';X.fillRect(-110,-176,220,14);[-160,160].forEach(dx=>{X.strokeStyle='#2a2e34';X.lineWidth=6;X.beginPath();X.moveTo(dx,-160);X.lineTo(dx*1.1,-320);X.stroke();X.fillStyle='#2a2e34';X.save();X.translate(dx*1.1,-320);X.rotate(dx>0?-.6:.6);rr(-30,-20,60,40,6);X.fill();X.restore()});
 X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,-180,4,0,-180,180);g.addColorStop(0,'rgba(255,245,220,.35)');g.addColorStop(1,'rgba(255,245,220,0)');X.fillStyle=g;X.beginPath();X.arc(0,-180,180,0,7);X.fill();X.restore();X.restore()}
NUEVOS.animacion={osc:.14,
 luces(z){const b=z.x0+100;return [{x:b+600,y:760,fy:HZ+280,r:480,c:'255,236,200',panel:1},{x:b+1450,y:760,fy:HZ+280,r:480,c:'255,236,200',panel:1}]},
 fondo(z,t,q){const b=z.x0+100,x0=z.x0,x1=z.x1,w=x1-x0,cx=b+975;
  X.fillStyle=gl(0,500,0,770,[[0,'#8a7a66'],[1,'#c9b89c']]);X.fillRect(x0,480,w,290);X.strokeStyle='rgba(60,40,20,.25)';X.lineWidth=10;for(let i=-3;i<w/260+3;i++){const bx=x0+i*260;X.beginPath();X.moveTo(bx,770);X.lineTo(cx+(bx-cx)*1.8,480);X.stroke()}
  [600,1450].forEach(s=>{const px=b+s;glow('#fff3dc',40,()=>{X.fillStyle='#fff6e2';X.beginPath();X.moveTo(px-200,760);X.lineTo(px+200,760);X.lineTo(px+170,700);X.lineTo(px-170,700);X.closePath();X.fill()});X.strokeStyle='#8a7a66';X.lineWidth=6;X.beginPath();X.moveTo(px,760);X.lineTo(px,700);X.stroke()});
  X.fillStyle=gl(0,770,0,1300,[[0,'#efe1c6'],[1,'#dcc8a6']]);X.fillRect(x0,770,w,530);X.fillStyle='#8a6a48';X.fillRect(x0,1284,w,18);
  for(let r=0;r<2;r++){const ry=820+r*150;X.fillStyle='#b98f5a';X.fillRect(b+40,ry,1880,10);for(let i=0;i<17;i++){const px=b+60+i*110;if(px>b+1260&&px<b+1700&&r===1)continue;X.save();X.translate(px+45,ry+64);X.rotate((rnd(i+r*20)-.5)*.08);X.fillStyle='rgba(0,0,0,.15)';X.fillRect(-41,-55,90,118);X.fillStyle='#fbf7ec';X.fillRect(-45,-60,90,118);
    X.strokeStyle='rgba(40,40,60,.6)';X.lineWidth=2;if((i+r)%3===0){for(let k=0;k<5;k++){const bx=-34+k*17,by=30-Math.abs(Math.sin((k+i*.3)*1.2))*70;X.beginPath();X.ellipse(bx,by,7,7*(by>20?.7:1),0,0,7);X.stroke()}X.setLineDash([3,4]);X.beginPath();X.moveTo(-34,30);X.quadraticCurveTo(0,-90,34,30);X.stroke();X.setLineDash([])}
    else if((i+r)%3===1){X.beginPath();X.arc(0,-14,20,0,7);X.stroke();X.beginPath();X.moveTo(0,6);X.lineTo(0,34);X.moveTo(-18,16);X.lineTo(18,16);X.moveTo(0,34);X.lineTo(-12,52);X.moveTo(0,34);X.lineTo(12,52);X.stroke();X.beginPath();X.arc(-7,-17,2,0,7);X.arc(7,-17,2,0,7);X.fill()}
    else{X.beginPath();X.ellipse(0,0,30,22,0,0,7);X.stroke();X.beginPath();X.moveTo(-30,0);X.lineTo(30,0);X.moveTo(0,-22);X.lineTo(0,22);X.stroke();for(let k=0;k<3;k++){X.beginPath();X.moveTo(-36,36+k*7);X.lineTo(24-k*8,36+k*7);X.stroke()}}
    X.fillStyle='#e53935';X.beginPath();X.arc(0,-54,4,0,7);X.fill();X.restore()}}
  {const sx=b+1300;X.fillStyle='#6b4a2e';X.fillRect(sx,1010,380,12);X.fillRect(sx,1120,380,12);for(let k=0;k<6;k++){X.fillStyle=gl(0,0,0,0,[[0,'#9aa3ad'],[1,'#9aa3ad']]);X.fillStyle=k%2?'#9aa3ad':'#b0b8c2';X.beginPath();X.ellipse(sx+40+k*62,1004,28,8,0,0,7);X.fill();X.fillRect(sx+12+k*62,968,56,36);X.fillStyle='#7d8590';X.beginPath();X.ellipse(sx+40+k*62,968,28,8,0,0,7);X.fill()}
   for(let k=0;k<9;k++){X.fillStyle=['#1e3a5f','#7b1f1f','#2e5e3a','#3d2b56'][k%4];X.fillRect(sx+10+k*40,1064,32,56);X.fillStyle='#fff';X.fillRect(sx+16+k*40,1080,20,10)}}
  pisoMadera(x0,x1,cx,1300,1950,['#a07a52','#957049','#a9825a']);X.fillStyle=gl(0,1300,0,1360,[[0,'rgba(0,0,0,.3)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,1300,w,60);
  mesaAnimacion(b+300,1360,1,t,1);mesaAnimacion(b+760,1360,1,t,2);camaraAnimacion(b+1700,1350,1,t);
  {const tx=b+1180;X.fillStyle='#78909c';X.beginPath();X.moveTo(tx-34,1350);X.lineTo(tx+34,1350);X.lineTo(tx+28,1270);X.lineTo(tx-28,1270);X.closePath();X.fill();for(let k=0;k<5;k++){X.fillStyle='#f3efe4';X.beginPath();X.arc(tx-22+k*11+(k%2)*4,1266-(k%3)*8,12,0,7);X.fill()}
   [[tx+70,1380],[tx+120,1410],[tx-90,1400]].forEach(([px,py],i)=>{X.fillStyle='#f3efe4';X.beginPath();X.arc(px,py,12+i*2,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.2)';X.lineWidth=1.5;X.beginPath();X.moveTo(px-6,py-3);X.lineTo(px+5,py+4);X.stroke()})}}};

// ---- Sala de directorio: mesa larga, sillas de respaldo alto, ventanal de piso a techo con ciudad, lamparas colgantes. o.hora ----
NUEVOS.reunion={osc:.16,
 luces(z){const b=z.x0+100;return [520,975,1430].map(s=>({x:b+s,y:820,fy:HZ+120,r:380,c:'255,232,190',panel:1}))},
 fondo(z,t,q){const b=z.x0+100,x0=z.x0,x1=z.x1,w=x1-x0,cx=b+975,o=O(z),h=o.hora||'dia';
  X.fillStyle='#e8e4dc';X.fillRect(x0,480,w,280);X.fillStyle='#cfc9bd';X.fillRect(x0,752,w,18);
  X.save();X.beginPath();X.rect(x0,770,w,520);X.clip();cielo(x0,770,w,520,h,t,21);skyline(x0,900,w,400,h,23);X.restore();
  X.fillStyle='rgba(180,220,255,.08)';X.fillRect(x0,770,w,520);for(let i=0;i*300<w+300;i++){const mx=x0+i*300;X.fillStyle='#2b2f36';X.fillRect(mx-8,770,16,520);X.fillStyle='rgba(255,255,255,.12)';X.beginPath();X.moveTo(mx+30,770);X.lineTo(mx+110,770);X.lineTo(mx+30,1080);X.closePath();X.fill()}
  X.fillStyle='#2b2f36';X.fillRect(x0,1270,w,32);
  [520,975,1430].forEach(s=>{const px=b+s;X.strokeStyle='#1d1f24';X.lineWidth=3;X.beginPath();X.moveTo(px,480);X.lineTo(px,790);X.stroke();X.fillStyle='#1d1f24';X.beginPath();X.moveTo(px-70,830);X.lineTo(px-40,790);X.lineTo(px+40,790);X.lineTo(px+70,830);X.closePath();X.fill();glow('#ffe7b0',30,()=>{X.fillStyle='#fff1c8';X.beginPath();X.ellipse(px,830,66,8,0,0,7);X.fill()})});
  pisoPersp(x0,x1,cx,1300,1950,180,['#3b3f47','#363a42'],'rgba(0,0,0,.25)');X.fillStyle=gl(0,1300,0,1380,[[0,'rgba(0,0,0,.4)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,1300,w,80);
  // sillas detras de la mesa
  for(let i=0;i<6;i++){const sx=b+330+i*260;X.fillStyle=gl(sx-46,0,sx+46,0,[[0,'#111'],[.5,'#2c2c2c'],[1,'#111']]);rr(sx-46,1010,92,200,26);X.fill();X.fillStyle='rgba(255,255,255,.12)';X.fillRect(sx-36,1016,72,4)}
  // mesa larga (vista lateral con tablero visible)
  {const ty=1196;somb(cx,1370,900,30,.5);X.fillStyle=gl(0,ty-40,0,ty,[[0,'#6b3a1f'],[1,'#4a250f']]);X.beginPath();X.moveTo(b+200,ty);X.lineTo(b+1750,ty);X.lineTo(b+1690,ty-46);X.lineTo(b+260,ty-46);X.closePath();X.fill();
   X.fillStyle='rgba(255,220,180,.18)';X.beginPath();X.moveTo(b+300,ty-40);X.lineTo(b+1600,ty-40);X.lineTo(b+1610,ty-34);X.lineTo(b+290,ty-34);X.closePath();X.fill();
   X.fillStyle='#3a1c0a';X.fillRect(b+200,ty,1550,22);X.fillStyle='#2a1406';X.fillRect(b+260,ty+22,40,150);X.fillRect(b+1650,ty+22,40,150);X.fillRect(b+900,ty+22,150,150);
   for(let i=0;i<6;i++){const px=b+330+i*260;X.fillStyle='#f4f1ea';X.beginPath();X.moveTo(px-40,ty-22);X.lineTo(px+30,ty-22);X.lineTo(px+36,ty-30);X.lineTo(px-34,ty-30);X.closePath();X.fill();
    X.fillStyle='rgba(220,240,255,.55)';X.fillRect(px+50,ty-58,16,34);X.fillStyle='rgba(150,200,255,.35)';X.fillRect(px+50,ty-40,16,16);X.fillStyle='#d4af37';X.fillRect(px-30,ty-48,48,14)}
   X.fillStyle='rgba(220,240,255,.45)';X.beginPath();X.moveTo(cx-20,ty-40);X.lineTo(cx+20,ty-40);X.lineTo(cx+16,ty-110);X.quadraticCurveTo(cx,ty-130,cx-16,ty-110);X.closePath();X.fill()}
  planta(b+120,1330,1.05);planta(b+1860,1330,1.05)}};

// ---- Mesa vista desde arriba (inserto sin personajes): contrato, pluma, cafe, lentes, fajos de billetes. o.monto, o.izq/o.der (rotulos), o.separa (momento), o.firma (momento) ----
function fajoCenital(x,y,s,txtF){X.save();X.translate(x,y);X.scale(s,s);for(let k=3;k>=0;k--){X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-92+k*3+6,-44-k*3+8,184,88);X.fillStyle=gl(-90,0,90,0,[[0,'#6b8f5a'],[.5,'#8fb07a'],[1,'#5f8350']]);X.fillRect(-92+k*3,-44-k*3,184,88);X.strokeStyle='rgba(30,60,30,.5)';X.lineWidth=2;X.strokeRect(-84+k*3,-36-k*3,168,72);X.fillStyle='rgba(30,60,30,.45)';X.beginPath();X.ellipse(-50+k*3,-k*3,18,22,0,0,7);X.fill()}
 X.fillStyle='#f5efd6';X.fillRect(-16,-56,32,112);txt(txtF||'$10,000',0,0,13,'#5a4a1a',{w:800});X.restore()}
function cafeCenital(x,y,t){X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.arc(x+10,y+12,82,0,7);X.fill();X.fillStyle='#f4f1ea';X.beginPath();X.arc(x,y,80,0,7);X.fill();X.fillStyle='#dcd6c8';X.beginPath();X.arc(x,y,56,0,7);X.fill();X.fillStyle='#fbf9f4';X.beginPath();X.arc(x,y,50,0,7);X.fill();
 X.fillStyle='#4a2a14';X.beginPath();X.arc(x,y,40,0,7);X.fill();X.strokeStyle='rgba(220,180,130,.6)';X.lineWidth=3;X.beginPath();X.arc(x,y,24,t*.5,t*.5+4);X.stroke();X.fillStyle='#fbf9f4';rr(x+48,y-12,40,24,10);X.fill();
 X.save();X.globalAlpha*=.25;for(let k=0;k<3;k++){X.strokeStyle='#fff';X.lineWidth=6;X.beginPath();const o=Math.sin(t*1.5+k)*14;X.moveTo(x-20+k*20,y-10);X.bezierCurveTo(x-30+k*20+o,y-60,x+o-10+k*20,y-90,x+k*14,y-140);X.stroke()}X.restore()}
function lentesCenital(x,y,r){X.save();X.translate(x,y);X.rotate(r);X.strokeStyle='#1a1a1a';X.lineWidth=7;X.fillStyle='rgba(190,220,255,.25)';[-58,58].forEach(dx=>{X.beginPath();X.ellipse(dx,0,46,36,0,0,7);X.fill();X.stroke()});X.beginPath();X.moveTo(-12,-6);X.quadraticCurveTo(0,-16,12,-6);X.stroke();X.lineWidth=5;X.beginPath();X.moveTo(-104,-6);X.lineTo(-150,60);X.moveTo(104,-6);X.lineTo(150,60);X.stroke();
 X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.ellipse(-70,-12,12,6,-.5,0,7);X.ellipse(46,-12,12,6,-.5,0,7);X.fill();X.restore()}
function plumaCenital(x,y,r){X.save();X.translate(x,y);X.rotate(r);X.fillStyle='rgba(0,0,0,.3)';rr(-150,-6,300,24,12);X.fill();X.fillStyle=gl(0,-12,0,12,[[0,'#3a3a3a'],[.4,'#111'],[1,'#000']]);rr(-150,-12,250,24,12);X.fill();X.fillStyle='#d4af37';X.fillRect(30,-12,10,24);X.fillRect(-120,-14,90,4);X.fillStyle='#d4af37';X.beginPath();X.moveTo(100,-10);X.lineTo(150,0);X.lineTo(100,10);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.3)';X.fillRect(-140,-8,220,3);X.restore()}
function contratoCenital(x,y,s,t,o,firma){X.save();X.translate(x,y);X.scale(s,s);X.rotate(-.04);X.fillStyle='rgba(0,0,0,.28)';X.fillRect(-206,-266,430,560);X.fillStyle='#fbf8ef';X.fillRect(-215,-280,430,560);X.fillStyle='#f1ecdf';X.fillRect(-215,-280,430,24);
 txt(o.titulo||'AGREEMENT',0,-220,30,'#2b2b2b',{w:800});X.fillStyle='#9e9a90';for(let l=0;l<14;l++)X.fillRect(-170,-170+l*22,340-(l%4)*40,5);
 txt(o.monto||'$10,000,000',0,170,34,'#b71c1c',{w:800});X.strokeStyle='#555';X.lineWidth=2;X.beginPath();X.moveTo(-170,236);X.lineTo(-20,236);X.moveTo(40,236);X.lineTo(180,236);X.stroke();
 if(firma>0){X.save();X.beginPath();X.rect(-170,190,150*firma,50);X.clip();X.strokeStyle='#0d2b7a';X.lineWidth=3;X.beginPath();X.moveTo(-160,228);for(let k=0;k<12;k++)X.quadraticCurveTo(-150+k*12,200+(k%2)*30,-140+k*12,226);X.stroke();X.restore()}
 X.fillStyle='rgba(183,28,28,.85)';X.beginPath();X.arc(150,-160,34,0,7);X.fill();X.strokeStyle='#fbf8ef';X.lineWidth=2;X.beginPath();X.arc(150,-160,26,0,7);X.stroke();X.restore()}
NUEVOS.mesaCenital={osc:.25,
 luces(z){const b=z.x0+100;return [{x:b+900,y:1100,fy:1250,r:760,c:'255,225,170',panel:1}]},
 fondo(z,t,q){const b=z.x0+100,x0=z.x0,w=z.x1-z.x0,o=O(z);
  X.fillStyle='#4a2c18';X.fillRect(x0,480,w,1500);for(let i=0;i<14;i++){const py=640+i*96;X.fillStyle=i%2?'#55331d':'#4d2e1a';X.fillRect(x0,py,w,94);X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=3;X.beginPath();X.moveTo(x0,py);X.lineTo(x0+w,py);X.stroke();
   X.strokeStyle='rgba(255,220,180,.06)';X.lineWidth=2;for(let k=0;k<5;k++){X.beginPath();X.moveTo(x0,py+14+k*16);for(let xx=0;xx<w;xx+=120)X.quadraticCurveTo(x0+xx+60,py+14+k*16+Math.sin(xx*.01+i+k)*6,x0+xx+120,py+14+k*16);X.stroke()}}
  X.fillStyle='#1f3b2a';X.fillRect(b+230,800,1400,880);X.strokeStyle='#c9a227';X.lineWidth=3;X.strokeRect(b+246,816,1368,848);
  const sp=o.separa?eio(seg(t,tk(o.separa,window.__A||0),tk(o.separa,window.__A||0)+1.1)):0,fi=o.firma?seg(t,tk(o.firma,window.__A||0),tk(o.firma,window.__A||0)+1.6):0;
  contratoCenital(b+640,1230,1,t,o,fi);
  const n=o.fajos||6;for(let k=0;k<n;k++){const izq=k<n/2,bx=b+1180+(k%3)*40+(izq?-sp*120:sp*260),by=1000+Math.floor(k%3)*90+(izq?0:sp*40)+(k>=n/2?260:0)*(1-sp)+(izq?0:-260*(1-sp));fajoCenital(bx+(izq?0:200*(1-sp)),by,1,o.billete)}
  if(sp>.3){X.save();X.globalAlpha*=seg(sp,.3,1);txt(o.izq||'LUCASFILM',b+1180,1430,30,'#fff',{w:800,g:12,gc:'#000'});txt(o.der||'PIXAR',b+1600,1430,30,'#fff',{w:800,g:12,gc:'#000'});X.restore()}
  cafeCenital(b+320,980,t);lentesCenital(b+330,1500,.3);plumaCenital(b+760+fi*-60,1520-fi*60,-.5);
  X.save();const vg=X.createRadialGradient(b+900,1250,300,b+900,1250,1150);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,.55)');X.fillStyle=vg;X.fillRect(x0,480,w,1500);X.restore()}};
