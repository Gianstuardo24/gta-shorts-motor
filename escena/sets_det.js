// ===== ESCENARIOS DETALLADOS (videos largos): cada uno pinta techo, pared, piso y muebles con referencias reales =====
const NUEVOS={};
function gl(x0,y0,x1,y1,st){const g=X.createLinearGradient(x0,y0,x1,y1);st.forEach(s=>g.addColorStop(s[0],s[1]));return g}
function somb(x,y,rx,ry,a=.35){X.save();X.translate(x,y);X.scale(1,ry/rx);const g=X.createRadialGradient(0,0,0,0,0,rx);g.addColorStop(0,`rgba(0,0,0,${a})`);g.addColorStop(1,'rgba(0,0,0,0)');X.fillStyle=g;X.beginPath();X.arc(0,0,rx,0,7);X.fill();X.restore()}
function pisoPersp(x0,x1,cx,y0,y1,paso,cols,lin){const vy=y0-420,P=(x,yy)=>cx+(x-cx)*((yy-vy)/(y0-vy));
 const xs=[];for(let x=x0-paso*6;x<=x1+paso*6;x+=paso)xs.push(x);const ys=[];let y=y0,h=34;while(y<y1+120){ys.push(y);y+=h;h*=1.32}
 for(let j=0;j<ys.length-1;j++)for(let i=0;i<xs.length-1;i++){X.fillStyle=cols[(i+j)%cols.length];X.beginPath();X.moveTo(P(xs[i],ys[j]),ys[j]);X.lineTo(P(xs[i+1],ys[j]),ys[j]);X.lineTo(P(xs[i+1],ys[j+1]),ys[j+1]);X.lineTo(P(xs[i],ys[j+1]),ys[j+1]);X.closePath();X.fill()}
 if(lin){X.strokeStyle=lin;X.lineWidth=2;xs.forEach(x=>{X.beginPath();X.moveTo(P(x,y0),y0);X.lineTo(P(x,y1+120),y1+120);X.stroke()});ys.forEach(yy=>{X.beginPath();X.moveTo(x0-800,yy);X.lineTo(x1+800,yy);X.stroke()})}}

// ---- objetos de escritorio (anos 80) ----
function terminal80(mx,by,s,t,o={}){X.save();X.translate(mx,by);X.scale(s,s);somb(0,0,130,12,.35);
 X.fillStyle=gl(0,-18,0,-2,[[0,'#e2dccd'],[1,'#c7c0af']]);X.beginPath();X.moveTo(-112,-2);X.lineTo(112,-2);X.lineTo(98,-18);X.lineTo(-98,-18);X.closePath();X.fill();
 X.fillStyle='#b5ae9c';for(let r=0;r<3;r++)for(let c=0;c<15;c++)X.fillRect(-92+c*12.3+r*2,-15+r*4.2,8.5,2.6);
 X.fillStyle='#c4bdab';X.beginPath();X.moveTo(-70,-22);X.lineTo(70,-22);X.lineTo(80,-38);X.lineTo(-80,-38);X.closePath();X.fill();
 X.fillStyle='#a9a291';X.beginPath();X.moveTo(98,-186);X.lineTo(122,-172);X.lineTo(122,-50);X.lineTo(98,-40);X.closePath();X.fill();
 X.fillStyle=gl(-100,0,100,0,[[0,'#d3ccba'],[.6,'#ebe5d6'],[1,'#bcb5a3']]);rr(-100,-192,200,156,14);X.fill();
 X.fillStyle='rgba(255,255,255,.35)';X.fillRect(-92,-190,184,3);
 X.fillStyle='#232520';rr(-85,-178,170,122,16);X.fill();
 X.save();rr(-77,-170,154,106,14);X.clip();const verde=o.color!==true;X.fillStyle=verde?'#061a0b':'#050b18';X.fillRect(-80,-172,160,112);
 if(o.dibujo)o.dibujo(0,-117,t);else{const c=verde?'#5dff8a':'#7fd7ff';X.fillStyle=c;X.shadowColor=c;X.shadowBlur=8;const per=Math.floor(t*2.5/8),n=Math.floor(t*2.5)%8;for(let l=0;l<7;l++){if(l>n)break;const len=26+rnd(l*7+per*13+(o.sem||0))*96;X.fillRect(-68,-160+l*13,l===n?len*(t*2.5%1):len,5)}X.shadowBlur=0}
 X.fillStyle='rgba(0,0,0,.28)';for(let y=-170;y<-62;y+=4)X.fillRect(-80,y,160,1.5);
 const rg=X.createRadialGradient(-34,-146,4,0,-117,110);rg.addColorStop(0,'rgba(255,255,255,.18)');rg.addColorStop(1,'rgba(255,255,255,0)');X.fillStyle=rg;X.fillRect(-80,-172,160,112);X.restore();
 X.fillStyle=Math.sin(t*2+mx)>0?'#69f0ae':'#3b5a46';X.beginPath();X.arc(82,-46,3.2,0,7);X.fill();X.restore()}
function esferaAlambre(cx,cy,r,t,col){X.save();X.strokeStyle=col;X.lineWidth=1.6;X.shadowColor=col;X.shadowBlur=7;
 for(let k=0;k<6;k++){const a=t*.8+k*Math.PI/6;X.beginPath();X.ellipse(cx,cy,Math.abs(Math.cos(a))*r+.1,r,0,0,7);X.stroke()}
 for(let k=1;k<6;k++){const yy=cy-r+k*r/3,r2=Math.sqrt(Math.max(0,r*r-(yy-cy)**2));X.beginPath();X.ellipse(cx,yy,r2,r2*.22+.1,0,0,7);X.stroke()}X.restore()}
function taza2(x,y,col){X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(x+3,y,17,4,0,0,7);X.fill();X.strokeStyle=col;X.lineWidth=5;X.beginPath();X.arc(x+14,y-17,8,-1.3,1.3);X.stroke();
 X.fillStyle=gl(x-13,0,x+13,0,[[0,col],[.4,'#fff'],[.5,col],[1,col]]);rr(x-13,y-32,26,32,5);X.fill();X.fillStyle='#3e2417';X.beginPath();X.ellipse(x,y-31,11,3.4,0,0,7);X.fill()}
function papeles(x,y,n){for(let k=0;k<n;k++){X.fillStyle=k%2?'#f7f4ec':'#e6e2d6';X.beginPath();X.moveTo(x-52+k*1.5,y-k*3.2);X.lineTo(x+46+k,y-k*3.2);X.lineTo(x+40+k,y-k*3.2-11);X.lineTo(x-45+k*1.5,y-k*3.2-11);X.closePath();X.fill()}}
function telefono80(x,y){X.fillStyle='#d8cfbd';X.beginPath();X.moveTo(x-40,y);X.lineTo(x+40,y);X.lineTo(x+30,y-30);X.lineTo(x-30,y-30);X.closePath();X.fill();X.fillStyle=gl(0,y-48,0,y-26,[[0,'#e2d9c6'],[1,'#b9af9a']]);rr(x-46,y-48,92,22,11);X.fill();
 X.fillStyle='#8f877a';for(let r=0;r<3;r++)for(let c=0;c<3;c++)X.fillRect(x-14+c*10,y-24+r*7,6,4);X.strokeStyle='#c4baa6';X.lineWidth=3;X.beginPath();X.moveTo(x+40,y-6);for(let k=0;k<14;k++)X.lineTo(x+44+k*4,y-2+(k%2?6:-2));X.stroke()}
function cajaDisquetes(x,y){X.fillStyle='#37474f';X.fillRect(x-40,y-34,80,34);X.fillStyle='#263238';X.fillRect(x-40,y-38,80,6);for(let k=0;k<7;k++){X.fillStyle=['#e53935','#1e88e5','#fdd835','#43a047','#fb8c00','#8e24aa','#eceff1'][k];X.fillRect(x-34+k*10,y-58,7,22)}}
function lamparaArq(x,y,s,on){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#2b2d33';X.beginPath();X.ellipse(0,0,34,8,0,0,7);X.fill();X.strokeStyle='#3a3d45';X.lineWidth=6;X.lineCap='round';X.beginPath();X.moveTo(0,-4);X.lineTo(-30,-110);X.lineTo(46,-150);X.stroke();
 X.fillStyle='#c62828';X.save();X.translate(46,-150);X.rotate(.55);X.beginPath();X.moveTo(-16,-10);X.lineTo(16,-10);X.lineTo(34,28);X.lineTo(-34,28);X.closePath();X.fill();X.fillStyle='#ffe9a8';X.beginPath();X.ellipse(0,28,32,7,0,0,7);X.fill();X.restore();
 if(on){X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(70,-10,4,70,-10,120);g.addColorStop(0,'rgba(255,220,150,.35)');g.addColorStop(1,'rgba(255,220,150,0)');X.fillStyle=g;X.beginPath();X.arc(70,-10,120,0,7);X.fill();X.restore()}X.restore()}
function sillaOficina(x,y,s,dir=1){X.save();X.translate(x,y);X.scale(s*dir,s);somb(0,0,95,15,.45);
 X.strokeStyle='#1b1c20';X.lineWidth=9;X.lineCap='round';const P=[[-72,-4],[72,-4],[-24,10],[30,12]];P.forEach(([lx,ly])=>{X.beginPath();X.moveTo(0,-26);X.lineTo(lx,ly);X.stroke()});P.forEach(([lx,ly])=>{X.fillStyle='#0e0f12';X.beginPath();X.arc(lx,ly+5,8,0,7);X.fill()});
 X.fillStyle=gl(-6,0,6,0,[[0,'#7b7f88'],[1,'#3e4148']]);X.fillRect(-6,-104,12,80);
 X.fillStyle='#2a2b30';X.fillRect(-8,-220,12,110);
 X.fillStyle=gl(-58,0,58,0,[[0,'#22325a'],[.45,'#3e5a94'],[1,'#1d2a4c']]);rr(-58,-318,116,128,30);X.fill();X.strokeStyle='rgba(255,255,255,.12)';X.lineWidth=3;rr(-50,-310,100,112,26);X.stroke();
 X.fillStyle=gl(0,-126,0,-96,[[0,'#46619e'],[1,'#22325a']]);rr(-76,-126,152,32,15);X.fill();X.fillStyle='rgba(255,255,255,.14)';X.fillRect(-66,-124,132,4);X.restore()}

// ---- Laboratorio de computacion, ~1985: racks con cintas, terminales CRT, impresora de matriz, persianas ----
NUEVOS.lab80={osc:.12,
 luces(z){const b=z.x0+100;return [330,975,1620].map(s=>({x:b+s,y:748,fy:HZ+300,r:470,c:'236,244,255',panel:1}))},
 fondo(z,t,q){const b=z.x0+100,x0=z.x0,x1=z.x1,w=x1-x0,cx=b+975;
  // techo de placas con tubos fluorescentes
  X.fillStyle=gl(0,520,0,770,[[0,'#74777f'],[1,'#b7bac1']]);X.fillRect(x0,480,w,290);
  X.strokeStyle='rgba(50,52,60,.30)';X.lineWidth=3;[600,655,705,742].forEach(y=>{X.beginPath();X.moveTo(x0,y);X.lineTo(x1,y);X.stroke()});
  for(let i=-4;i<w/150+4;i++){const bx=x0+i*150;X.beginPath();X.moveTo(bx,770);X.lineTo(cx+(bx-cx)*1.9,480);X.stroke()}
  [330,975,1620].forEach(s=>{const px=b+s,pth=()=>{X.beginPath();X.moveTo(px-150,752);X.lineTo(px+150,752);X.lineTo(px+134,724);X.lineTo(px-134,724);X.closePath()};
   glow('#eaf4ff',40,()=>{X.fillStyle='#f6faff';pth();X.fill()});X.strokeStyle='rgba(140,150,165,.9)';X.lineWidth=3;pth();X.stroke();for(let k=-2;k<=2;k++){X.beginPath();X.moveTo(px+k*58,752);X.lineTo(px+k*52,724);X.stroke()}});
  // pared beige con zocalo
  X.fillStyle=gl(0,770,0,1300,[[0,'#cfc8b6'],[1,'#b6ae9a']]);X.fillRect(x0,770,w,530);
  X.fillStyle=gl(0,770,0,830,[[0,'rgba(0,0,0,.30)'],[1,'rgba(0,0,0,0)']]);X.fillRect(x0,770,w,60);
  X.fillStyle='#978f7c';X.fillRect(x0,1150,w,150);X.fillStyle='#ddd6c4';X.fillRect(x0,1143,w,9);X.fillStyle='#4a453b';X.fillRect(x0,1284,w,18);
  // ventana con persianas y ciudad
  {const wx=b+1330,wy=828,ww=470,wh=292;X.fillStyle='rgba(0,0,0,.18)';X.fillRect(wx-10,wy-8,ww+36,wh+44);X.fillStyle='#ebe7dc';rr(wx-16,wy-16,ww+32,wh+34,6);X.fill();
   X.save();X.beginPath();X.rect(wx,wy,ww,wh);X.clip();X.fillStyle=gl(0,wy,0,wy+wh,[[0,'#86b9e6'],[1,'#dcefff']]);X.fillRect(wx,wy,ww,wh);
   for(let i=0;i<8;i++){const bh=70+rnd(i+3)*150,bw=48+rnd(i+9)*40,bx=wx+i*64-14;X.fillStyle=`rgb(${128+i*5},${146+i*4},${170+i*3})`;X.fillRect(bx,wy+wh-bh,bw,bh);X.fillStyle='rgba(255,255,255,.4)';for(let r=0;r<bh/22-1;r++)for(let c=0;c<2;c++)X.fillRect(bx+7+c*(bw/2),wy+wh-bh+8+r*22,bw/4,8)}
   for(let y=wy;y<wy+wh*.6;y+=17){X.fillStyle=gl(0,y,0,y+11,[[0,'#f5f0e3'],[1,'#cbc3af']]);X.fillRect(wx,y,ww,11)}X.fillStyle='#b8b09b';X.fillRect(wx,wy+wh*.6,ww,11);X.restore();
   X.strokeStyle='#d6d1c4';X.lineWidth=10;X.strokeRect(wx,wy,ww,wh);X.beginPath();X.moveTo(wx+ww/2,wy);X.lineTo(wx+ww/2,wy+wh);X.stroke();
   X.fillStyle='#f3efe5';X.fillRect(wx-28,wy+wh+6,ww+56,14);X.fillStyle='rgba(0,0,0,.2)';X.fillRect(wx-28,wy+wh+20,ww+56,6);
   X.strokeStyle='#8c8577';X.lineWidth=2;X.beginPath();X.moveTo(wx+ww-34,wy);X.lineTo(wx+ww-34,wy+wh*.6+70);X.stroke();X.fillStyle='#8c8577';X.beginPath();X.arc(wx+ww-34,wy+wh*.6+74,5,0,7);X.fill()}
  // diario mural de corcho
  {const kx=b+640,ky=848,kw=360,kh=200;X.fillStyle='rgba(0,0,0,.2)';X.fillRect(kx-6,ky-4,kw+24,kh+26);X.fillStyle='#7b5233';rr(kx-12,ky-12,kw+24,kh+24,6);X.fill();
   X.fillStyle=gl(kx,ky,kx+kw,ky+kh,[[0,'#cc9f63'],[1,'#b3864d']]);X.fillRect(kx,ky,kw,kh);for(let i=0;i<140;i++){X.fillStyle=`rgba(90,60,30,${.15+.2*rnd(i)})`;X.fillRect(kx+rnd(i*3)*kw,ky+rnd(i*7)*kh,3,3)}
   [[40,26,92,112,-.08,'#fbfaf5'],[150,18,82,66,.05,'#fff59d'],[248,28,92,122,.06,'#fbfaf5'],[152,98,88,84,-.04,'#e3f2fd'],[28,146,64,46,.1,'#f8bbd0']].forEach(([hx,hy,hw,hh,r,c],i)=>{X.save();X.translate(kx+hx+hw/2,ky+hy+hh/2);X.rotate(r);
    X.fillStyle='rgba(0,0,0,.2)';X.fillRect(-hw/2+4,-hh/2+5,hw,hh);X.fillStyle=c;X.fillRect(-hw/2,-hh/2,hw,hh);X.strokeStyle='rgba(50,60,110,.5)';X.lineWidth=2;
    if(i===0){X.beginPath();X.arc(0,-8,30,0,7);X.stroke();X.beginPath();X.ellipse(0,-8,30,10,0,0,7);X.stroke();X.beginPath();X.ellipse(0,-8,12,30,0,0,7);X.stroke();for(let l=0;l<3;l++){X.beginPath();X.moveTo(-34,32+l*8);X.lineTo(22-l*10,32+l*8);X.stroke()}}
    else if(i===2){for(let f=0;f<2;f++){X.strokeRect(-36,-50+f*46,72,38);X.beginPath();X.moveTo(-30,-20+f*46);X.lineTo(-10,-38+f*46);X.lineTo(8,-26+f*46);X.lineTo(30,-44+f*46);X.stroke()}}
    else{for(let l=0;l<Math.floor(hh/12)-1;l++){X.beginPath();X.moveTo(-hw/2+8,-hh/2+13+l*11);X.lineTo(hw/2-8-(l%3)*10,-hh/2+13+l*11);X.stroke()}}
    X.fillStyle=['#e53935','#1e88e5','#43a047','#fdd835','#8e24aa'][i];X.beginPath();X.arc(0,-hh/2+6,5,0,7);X.fill();X.fillStyle='rgba(255,255,255,.6)';X.beginPath();X.arc(-1.5,-hh/2+4.5,1.6,0,7);X.fill();X.restore()})}
  // reloj de pared
  {const ox=b+1165,oy=905,r=44;X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.arc(ox+5,oy+6,r+6,0,7);X.fill();X.fillStyle='#2b2b30';X.beginPath();X.arc(ox,oy,r+6,0,7);X.fill();X.fillStyle='#f7f5ef';X.beginPath();X.arc(ox,oy,r,0,7);X.fill();
   X.strokeStyle='#333';for(let i=0;i<12;i++){const a=i*Math.PI/6,l=i%3?9:14;X.lineWidth=i%3?2:4;X.beginPath();X.moveTo(ox+Math.cos(a)*(r-4),oy+Math.sin(a)*(r-4));X.lineTo(ox+Math.cos(a)*(r-4-l),oy+Math.sin(a)*(r-4-l));X.stroke()}
   const mins=12+t/60,hand=(ang,len,lw,col)=>{X.strokeStyle=col;X.lineWidth=lw;X.lineCap='round';X.beginPath();X.moveTo(ox,oy);X.lineTo(ox+Math.cos(ang)*len,oy+Math.sin(ang)*len);X.stroke()};
   hand(-Math.PI/2+(10+mins/60)/12*Math.PI*2,24,5,'#222');hand(-Math.PI/2+mins/60*Math.PI*2,34,3.5,'#222');hand(-Math.PI/2+Math.floor(t)/60*Math.PI*2,36,1.5,'#d32f2f');X.fillStyle='#222';X.beginPath();X.arc(ox,oy,4,0,7);X.fill()}
  // piso (alfombra de oficina en baldosas)
  X.fillStyle='#4a515c';X.fillRect(x0,1300,w,700);pisoPersp(x0,x1,cx,1300,1950,150,['#58606c','#515965'],'rgba(25,28,34,.32)');
  X.fillStyle=gl(0,1300,0,1950,[[0,'rgba(0,0,0,.35)'],[.12,'rgba(0,0,0,0)'],[1,'rgba(0,0,0,.3)']]);X.fillRect(x0,1300,w,650);
  {const wx=b+1330;X.save();X.globalCompositeOperation='lighter';X.beginPath();X.moveTo(wx+60,1330);X.lineTo(wx+440,1330);X.lineTo(wx+330,1580);X.lineTo(wx-170,1580);X.closePath();X.fillStyle=gl(0,1330,0,1580,[[0,'rgba(255,236,200,.18)'],[1,'rgba(255,236,200,0)']]);X.fill();X.restore()}
  // gabinetes: dos unidades de cinta y un procesador
  const cab=(sx,ww,kind)=>{const c0=b+sx,top=835,bot=1335;somb(c0+ww/2,bot,ww*.8,26,.5);
   X.fillStyle='#8f8a7e';X.beginPath();X.moveTo(c0+ww,top);X.lineTo(c0+ww+22,top-14);X.lineTo(c0+ww+22,bot-14);X.lineTo(c0+ww,bot);X.closePath();X.fill();
   X.fillStyle='#e9e4d8';X.beginPath();X.moveTo(c0,top);X.lineTo(c0+22,top-14);X.lineTo(c0+ww+22,top-14);X.lineTo(c0+ww,top);X.closePath();X.fill();
   X.fillStyle=gl(c0,0,c0+ww,0,[[0,'#d6d0c2'],[.5,'#e5e0d3'],[1,'#c0baab']]);X.fillRect(c0,top,ww,bot-top);
   X.fillStyle='#2f5f93';X.fillRect(c0,top+14,ww,22);X.fillStyle='#e08a2c';X.fillRect(c0,top+36,ww,6);
   if(kind==='cinta'){X.fillStyle='#1a1e28';rr(c0+12,top+58,ww-24,282,8);X.fill();
    [[top+128,1],[top+268,-1]].forEach(([ry,dr],j)=>{const rx=c0+ww/2,gira=Math.sin(t*.5+sx*.01)>-.3?1:.08,ang=t*(2.4+j*.8)*dr*gira;
     X.fillStyle='#9aa0ab';X.beginPath();X.arc(rx,ry,54,0,7);X.fill();X.fillStyle='#3a2a20';X.beginPath();X.arc(rx,ry,j?36:48,0,7);X.fill();
     X.save();X.translate(rx,ry);X.rotate(ang);X.fillStyle='#c9ced6';X.beginPath();X.arc(0,0,18,0,7);X.fill();X.fillStyle='#1a1e28';for(let k=0;k<3;k++){X.rotate(2.094);X.beginPath();X.arc(0,-9,4,0,7);X.fill()}
     X.strokeStyle='rgba(220,225,235,.55)';X.lineWidth=4;for(let k=0;k<3;k++){X.rotate(2.094);X.beginPath();X.moveTo(0,-22);X.lineTo(0,-52);X.stroke()}X.restore()});
    X.strokeStyle='#3a2a20';X.lineWidth=2;X.beginPath();X.moveTo(c0+ww/2+50,top+140);X.lineTo(c0+ww-22,top+198);X.lineTo(c0+ww/2+50,top+256);X.stroke();X.fillStyle='#cfd4dc';X.beginPath();X.arc(c0+ww-22,top+198,7,0,7);X.fill();
    X.fillStyle='rgba(255,255,255,.10)';X.beginPath();X.moveTo(c0+14,top+60);X.lineTo(c0+64,top+60);X.lineTo(c0+14,top+210);X.closePath();X.fill();
    for(let k=0;k<5;k++){X.fillStyle=['#e8e8e8','#e8e8e8','#ff5252','#ffd54f','#69f0ae'][k];rr(c0+14+k*25,top+354,18,12,3);X.fill()}
    X.fillStyle=Math.sin(t*5+sx)>0?'#69f0ae':'#2e4a3a';X.beginPath();X.arc(c0+ww-20,top+384,5,0,7);X.fill()}
   else{X.fillStyle='#16181f';rr(c0+14,top+66,ww-28,190,6);X.fill();
    for(let r=0;r<10;r++)for(let c=0;c<8;c++){const lit=rnd(r*13+c*7+Math.floor(t*6+r*.7))>.55;X.fillStyle=lit?(r<3?'#ff6e40':'#ffca28'):'#3a2f22';X.beginPath();X.arc(c0+28+c*((ww-56)/7),top+82+r*17,3.4,0,7);X.fill()}
    for(let k=0;k<12;k++){X.fillStyle=k%4===0?'#c62828':'#eceff1';rr(c0+16+k*((ww-32)/12),top+272,8,22,2);X.fill()}
    X.fillStyle='#f5f1e6';X.fillRect(c0+20,top+322,ww-40,26);X.fillStyle='#666';X.fillRect(c0+28,top+332,ww-70,4);X.fillRect(c0+28,top+340,ww-100,3)}
   X.fillStyle='rgba(0,0,0,.4)';for(let y=bot-96;y<bot-16;y+=10)X.fillRect(c0+14,y,ww-28,4);X.fillStyle='rgba(255,255,255,.25)';X.fillRect(c0,top,3,bot-top)};
  cab(40,150,'cinta');cab(205,150,'cinta');cab(372,160,'cpu');
  X.strokeStyle='#121317';X.lineWidth=6;X.beginPath();X.moveTo(b+480,1336);X.bezierCurveTo(b+540,1420,b+640,1400,b+700,1348);X.stroke();
  // escritorios
  const desk=(sx,ww)=>{const dx=b+sx,ty=1188;somb(dx+ww/2,1345,ww*.62,26,.45);X.fillStyle='#4e3a28';X.fillRect(dx+10,ty+20,ww-20,1340-ty-20);
   X.fillStyle=gl(0,ty+20,0,1340,[[0,'#6b5139'],[1,'#4b3826']]);X.fillRect(dx+ww-170,ty+20,160,1340-ty-20);
   for(let k=0;k<3;k++){X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=2;X.strokeRect(dx+ww-162,ty+28+k*42,144,36);X.fillStyle='#c8b28a';rr(dx+ww-108,ty+42+k*42,36,7,3);X.fill()}
   X.fillStyle='#3a2a1c';X.fillRect(dx+14,ty+20,14,1340-ty-20);
   X.fillStyle=gl(0,ty-6,0,ty+22,[[0,'#a5825c'],[.4,'#8a6a4a'],[1,'#5e4630']]);rr(dx,ty-4,ww,24,4);X.fill();X.fillStyle='rgba(255,255,255,.2)';X.fillRect(dx+4,ty-4,ww-8,3)};
  desk(600,460);desk(1300,520);
  terminal80(b+760,1186,1.0,t,{sem:1});papeles(b+905,1186,6);taza2(b+975,1186,'#c62828');cajaDisquetes(b+655,1186);
  terminal80(b+1520,1186,1.12,t,{color:true,dibujo:(x,y,tt)=>esferaAlambre(x,y,40,tt,'#4fc3f7')});telefono80(b+1380,1186);lamparaArq(b+1700,1186,1,true);papeles(b+1745,1186,3);
  // impresora de matriz con papel continuo
  {const px=b+1175,py=1232;somb(px,1345,110,18,.4);X.fillStyle='#3d4148';X.fillRect(px-88,py,176,10);X.fillRect(px-84,py+10,8,1335-py-10);X.fillRect(px+76,py+10,8,1335-py-10);X.fillRect(px-84,1300,168,8);
   for(let k=0;k<7;k++){X.fillStyle=k%2?'#f4f1e8':'#e7e3d7';X.fillRect(px-70,1298-k*6,140,6)}X.fillStyle='rgba(120,200,140,.5)';for(let k=0;k<7;k++)X.fillRect(px-70,1299-k*6,140,1.5);
   const off=(t*14)%22;X.fillStyle='#f6f3ea';X.beginPath();X.moveTo(px-62,py-50);X.lineTo(px+62,py-50);X.lineTo(px+66,py-150);X.quadraticCurveTo(px+70,py-182,px+40,py-178);X.lineTo(px-40,py-178);X.quadraticCurveTo(px-70,py-182,px-66,py-150);X.closePath();X.fill();
   X.save();X.beginPath();X.rect(px-66,py-178,132,128);X.clip();X.fillStyle='#9aa3ad';for(let y=py-50+off;y>py-182;y-=11)X.fillRect(px-44,y,50+rnd(Math.floor((y-off)/11)+40)*40,2.5);X.fillStyle='#c3c7cc';for(let y=py-50+off*.5;y>py-182;y-=11){X.beginPath();X.arc(px-56,y,2.5,0,7);X.arc(px+56,y,2.5,0,7);X.fill()}X.restore();
   X.fillStyle=gl(0,py-62,0,py,[[0,'#e4dfd2'],[1,'#b7b1a2']]);rr(px-92,py-64,184,64,8);X.fill();X.fillStyle='#8d877a';X.fillRect(px-72,py-54,144,8);X.fillStyle='#4a4e57';X.fillRect(px+Math.sin(t*6)*52-10,py-62,20,10);
   X.fillStyle=Math.sin(t*9)>0?'#ff7043':'#5a3a30';X.beginPath();X.arc(px+72,py-16,3.5,0,7);X.fill()}
  sillaOficina(b+860,1352,.95,1);sillaOficina(b+1600,1356,1.0,-1)}};

// ---- Estudio de producto: fondo infinito, dos softbox, foco central (para objetos protagonistas sin personajes) ----
NUEVOS.vitrina={osc:.3,
 luces(z){const b=z.x0+100;return [{x:b+975,y:740,fy:1620,r:600,c:'255,244,228',panel:1}]},
 fondo(z,t,q){const b=z.x0+100,cx=b+975,x0=z.x0,w=z.x1-z.x0;
  const g=X.createRadialGradient(cx,1260,40,cx,1260,1250);g.addColorStop(0,'#46577a');g.addColorStop(.45,'#1f2940');g.addColorStop(1,'#06080f');X.fillStyle=g;X.fillRect(x0,480,w,1500);
  const f=X.createRadialGradient(cx,1640,10,cx,1640,700);f.addColorStop(0,'rgba(190,210,255,.28)');f.addColorStop(1,'rgba(190,210,255,0)');X.fillStyle=f;X.save();X.translate(cx,1640);X.scale(1,.26);X.translate(-cx,-1640);X.beginPath();X.arc(cx,1640,700,0,7);X.fill();X.restore();
  [[b+150,1],[b+1800,-1]].forEach(([sx,d])=>{X.strokeStyle='#15171c';X.lineWidth=8;X.lineCap='round';[[-80,1690],[80,1690],[14,1660]].forEach(([lx,ly])=>{X.beginPath();X.moveTo(sx,1300);X.lineTo(sx+lx,ly);X.stroke()});
   X.lineWidth=10;X.beginPath();X.moveTo(sx,1300);X.lineTo(sx,960);X.stroke();X.fillStyle='#2a2d34';X.fillRect(sx-14,1290,28,24);
   X.save();X.translate(sx,930);X.rotate(d*.32);X.fillStyle='#0f1014';X.beginPath();X.moveTo(-60,-40);X.lineTo(60,-40);X.lineTo(150*1.0,-190);X.lineTo(150,190);X.lineTo(60,40);X.lineTo(-60,40);X.closePath();X.fill();
   glow('#fff6e6',60,()=>{X.fillStyle=gl(0,-190,0,190,[[0,'#fffdf7'],[.5,'#fff1d8'],[1,'#f4e2c4']]);rr(140,-188,24,376,6);X.fill()});X.restore()});
  for(let i=0;i<26;i++){const px=cx+(rnd(i)-.5)*1300,py=820+((rnd(i*5)*760+t*14*(rnd(i+2)+.3))%760);X.fillStyle=`rgba(255,250,235,${.18+.25*rnd(i+9)})`;X.beginPath();X.arc(px,py,1.6+rnd(i+4)*1.8,0,7);X.fill()}}};

// ---- Computadora grafica de 1985 (gabinete + monitor CRT a color en carro). o.precio: etiqueta colgante; o.render:false = imagen completa ----
function escenaRT(x,y,w,h,t,o){const hy=y+h*.56,vx=x+w/2;X.fillStyle=gl(0,y,0,hy,[[0,'#2f63ad'],[1,'#b5d3f2']]);X.fillRect(x,y,w,hy-y+1);X.fillStyle='#111';X.fillRect(x,hy,w,y+h-hy);
 const H2=y+h-hy,c=w/(2.2*H2);let prev=hy+1.5;for(let j=1;j<=9;j++){const yy=hy+H2*Math.pow(j/9,1.7);for(let i=-14;i<14;i++){X.fillStyle=(i+j)%2?'#c62828':'#fdd835';X.beginPath();X.moveTo(vx+i*c*(prev-hy)*1.6,prev);X.lineTo(vx+(i+1)*c*(prev-hy)*1.6,prev);X.lineTo(vx+(i+1)*c*(yy-hy)*1.6,yy);X.lineTo(vx+i*c*(yy-hy)*1.6,yy);X.closePath();X.fill()}prev=yy}
 const esf=(ex,ey,r,tipo)=>{X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(ex+r*.15,ey+r*.92,r*.95,r*.2,0,0,7);X.fill();
  if(tipo==='cromo'){const g=X.createLinearGradient(0,ey-r,0,ey+r);g.addColorStop(0,'#eaf3ff');g.addColorStop(.42,'#7aa3d8');g.addColorStop(.5,'#1d1d1d');g.addColorStop(.58,'#c62828');g.addColorStop(.7,'#fdd835');g.addColorStop(.84,'#c62828');g.addColorStop(1,'#4a1010');X.fillStyle=g}
  else{const g=X.createRadialGradient(ex-r*.3,ey-r*.35,r*.08,ex,ey,r);g.addColorStop(0,'#ffffff');g.addColorStop(.25,'#80deea');g.addColorStop(1,'#0d3c8c');X.fillStyle=g}
  X.beginPath();X.arc(ex,ey,r,0,7);X.fill();X.strokeStyle='rgba(0,0,0,.35)';X.lineWidth=1.5;X.stroke();X.fillStyle='rgba(255,255,255,.9)';X.beginPath();X.ellipse(ex-r*.36,ey-r*.46,r*.2,r*.1,-.5,0,7);X.fill()};
 esf(x+w*.3,y+h*.6,h*.17,'cromo');esf(x+w*.62,y+h*.69,h*.12,'vidrio');esf(x+w*.82,y+h*.6,h*.085,'cromo');
 const prog=o.render===false?2:((t*.11)%1.3);if(prog<1){const ry=y+h*prog;X.fillStyle='#050608';X.fillRect(x,ry,w,h);X.fillStyle='rgba(255,255,255,.85)';X.fillRect(x,ry-2,w,2);for(let i=0;i<10;i++){X.fillStyle=`rgba(180,220,255,${rnd(i+Math.floor(t*18))*.35})`;X.fillRect(x+i*w/10,ry,w/10-2,5)}}
 X.fillStyle='rgba(0,0,0,.22)';for(let yy=y;yy<y+h;yy+=3)X.fillRect(x,yy,w,1);const rg=X.createRadialGradient(x+w*.28,y+h*.18,10,x+w*.5,y+h*.5,w*.75);rg.addColorStop(0,'rgba(255,255,255,.16)');rg.addColorStop(1,'rgba(255,255,255,0)');X.fillStyle=rg;X.fillRect(x,y,w,h)}
UTILERIA.compu85=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);somb(-40,0,560,40,.6);
 const gx=-460,gw=300,gh=640,dep=80;
 X.fillStyle=gl(gx+gw,0,gx+gw+dep,0,[[0,'#1d2026'],[1,'#101216']]);X.beginPath();X.moveTo(gx+gw,-gh);X.lineTo(gx+gw+dep,-gh-36);X.lineTo(gx+gw+dep,-36);X.lineTo(gx+gw,0);X.closePath();X.fill();
 X.fillStyle=gl(0,-gh-36,0,-gh,[[0,'#626874'],[1,'#3b4048']]);X.beginPath();X.moveTo(gx,-gh);X.lineTo(gx+dep,-gh-36);X.lineTo(gx+gw+dep,-gh-36);X.lineTo(gx+gw,-gh);X.closePath();X.fill();
 X.fillStyle=gl(gx,0,gx+gw,0,[[0,'#2a2e36'],[.45,'#3e434d'],[1,'#282c33']]);X.fillRect(gx,-gh,gw,gh);
 X.fillStyle='#16181d';X.fillRect(gx+20,-gh+22,gw-40,52);txt(o.marca||'IMAGE COMPUTER',gx+gw/2,-gh+49,22,'#d5dce6',{w:700});X.fillStyle=gl(gx+20,0,gx+gw-20,0,[[0,'#00bcd4'],[1,'#ff4081']]);X.fillRect(gx+20,-gh+70,gw-40,4);
 for(let k=0;k<22;k++){const yy=-gh+100+k*12;X.fillStyle='#121419';rr(gx+26,yy,gw-52,6,3);X.fill();X.fillStyle='rgba(255,255,255,.08)';X.fillRect(gx+26,yy+6,gw-52,1.5)}
 const c0=-gh+380;X.fillStyle='#0c0e13';rr(gx+22,c0,gw-44,170,8);X.fill();
 for(let k=0;k<5;k++){const bx=gx+40+k*48;X.fillStyle=gl(bx,0,bx+34,0,[[0,'#1b5e20'],[1,'#2e7d32']]);X.fillRect(bx,c0+12,34,146);for(let c=0;c<6;c++){X.fillStyle='#121212';X.fillRect(bx+6,c0+22+c*21,22,13);X.fillStyle='#b0bec5';X.fillRect(bx+6,c0+22+c*21,22,2)}X.fillStyle=Math.sin(t*4+k*1.7)>0?'#ff5252':'#4a1f1f';X.beginPath();X.arc(bx+17,c0+150,3.5,0,7);X.fill()}
 X.fillStyle='rgba(130,170,230,.12)';X.beginPath();X.moveTo(gx+22,c0);X.lineTo(gx+120,c0);X.lineTo(gx+22,c0+130);X.closePath();X.fill();
 X.fillStyle='#1a1c22';X.fillRect(gx+22,-74,gw-44,54);X.fillStyle='#c62828';rr(gx+36,-64,34,32,4);X.fill();X.fillStyle='#ef5350';rr(gx+36,-64,34,13,4);X.fill();
 for(let k=0;k<4;k++){const on=rnd(k*5+Math.floor(t*4))>.4;X.fillStyle=on?['#69f0ae','#69f0ae','#ffd740','#40c4ff'][k]:'#2a2f36';X.beginPath();X.arc(gx+110+k*26,-47,5,0,7);X.fill()}
 X.fillStyle='#9ea7b3';X.beginPath();X.arc(gx+gw-50,-47,10,0,7);X.fill();X.fillStyle='#333';X.fillRect(gx+gw-52,-54,4,14);
 X.fillStyle='rgba(120,220,255,.6)';X.fillRect(gx+gw-4,-gh,4,gh);X.fillStyle='rgba(255,255,255,.28)';X.fillRect(gx,-gh,gw,3);X.fillStyle='#0d0e11';X.fillRect(gx+10,0,30,8);X.fillRect(gx+gw-40,0,30,8);
 const mx=170;X.fillStyle='#2b2e35';X.fillRect(mx-200,-252,400,22);X.fillStyle='rgba(255,255,255,.15)';X.fillRect(mx-200,-252,400,3);X.fillStyle='#1d2026';X.fillRect(mx-190,-230,14,214);X.fillRect(mx+176,-230,14,214);X.fillRect(mx-190,-92,380,14);
 [mx-183,mx+183].forEach(wx=>{X.fillStyle='#0b0b0d';X.beginPath();X.arc(wx,-9,10,0,7);X.fill()});
 X.fillStyle=gl(0,-286,0,-252,[[0,'#ece8df'],[1,'#c9c3b5']]);X.beginPath();X.moveTo(mx-172,-252);X.lineTo(mx+172,-252);X.lineTo(mx+150,-282);X.lineTo(mx-150,-282);X.closePath();X.fill();
 X.fillStyle='#b2ab9b';for(let r=0;r<4;r++)for(let c=0;c<20;c++)X.fillRect(mx-140+c*14+r*2,-278+r*6.5,10,4);
 const W2=430,H2=340,top=-286-H2-14;X.fillStyle='#bdb7aa';X.beginPath();X.moveTo(mx-90,top+H2-6);X.lineTo(mx+90,top+H2-6);X.lineTo(mx+120,-284);X.lineTo(mx-120,-284);X.closePath();X.fill();
 X.fillStyle='#a49e91';X.beginPath();X.moveTo(mx+W2/2-6,top+18);X.lineTo(mx+W2/2+40,top+60);X.lineTo(mx+W2/2+40,top+H2-40);X.lineTo(mx+W2/2-6,top+H2-6);X.closePath();X.fill();
 X.fillStyle=gl(mx-W2/2,0,mx+W2/2,0,[[0,'#cfcac0'],[.55,'#ece8df'],[1,'#bab4a8']]);rr(mx-W2/2,top,W2,H2,24);X.fill();X.fillStyle='rgba(255,255,255,.5)';X.fillRect(mx-W2/2+20,top+3,W2-40,3);
 const sx0=mx-W2/2+34,sy0=top+28,sw=W2-68,sh=H2-78;X.fillStyle='#19191c';rr(sx0-9,sy0-9,sw+18,sh+18,22);X.fill();X.save();rr(sx0,sy0,sw,sh,18);X.clip();escenaRT(sx0,sy0,sw,sh,t,o);X.restore();
 X.fillStyle='#a8a294';for(let k=0;k<4;k++){rr(mx+W2/2-150+k*30,top+H2-34,20,10,3);X.fill()}X.fillStyle='#43a047';X.beginPath();X.arc(mx-W2/2+40,top+H2-29,5,0,7);X.fill();
 X.strokeStyle='#0b0c0f';X.lineWidth=8;X.lineCap='round';X.beginPath();X.moveTo(gx+gw+30,-110);X.bezierCurveTo(gx+gw+90,-6,mx-230,-20,mx-190,-120);X.stroke();
 if(o.precio){const ax=gx+gw-26,ay=-gh+6,sw2=Math.sin(t*1.6)*.07;X.save();X.translate(ax,ay);X.rotate(-.25+sw2);X.strokeStyle='#e8dcc4';X.lineWidth=3;X.beginPath();X.moveTo(0,0);X.lineTo(0,96);X.stroke();X.translate(0,96);X.rotate(.25);
  X.fillStyle='rgba(0,0,0,.35)';rr(-60,6,150,76,10);X.fill();X.fillStyle='#fff8e1';X.beginPath();X.moveTo(-64,14);X.lineTo(-46,0);X.lineTo(80,0);X.lineTo(80,70);X.lineTo(-64,70);X.closePath();X.fill();X.strokeStyle='#c9b27a';X.lineWidth=2;X.stroke();
  X.fillStyle='#555';X.beginPath();X.arc(-46,14,5,0,7);X.fill();txt(o.precio,10,37,32,'#c62828',{w:800});X.restore()}
 X.restore()};
