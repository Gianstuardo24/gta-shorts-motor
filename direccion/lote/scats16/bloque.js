<script>
// ===== DC · SCATS16 · INICIO ===== (Cats 16h · Don't TRUST Your Cat's Favorite Plant · lote del 28-nov · una escena por línea del guion)
// No se nombra el compuesto químico. Los mosquitos se muestran de a pocos, nunca un enjambre. La línea 11 es una posibilidad, no una garantía.
(function(){
const {cam,cierreCanal,SET}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,noche,tarj,desenfoca,borroso}=window.B28;
const VERDE='170,235,120';

// ---------- hoja dentada con nervaduras; origen en la base, crece hacia arriba ----------
function hoja(x,y,len,rot,o){o=o||{};const W=len*(o.an||.34),n=14,hw=i=>W*Math.sin(Math.PI*Math.pow(i/n,.72))*(i%2?1.07:.95);X.save();X.translate(x,y);X.rotate(rot||0);X.beginPath();X.moveTo(0,0);
 for(let i=1;i<=n;i++)X.lineTo(hw(i),-i/n*len);for(let i=n-1;i>=0;i--)X.lineTo(-hw(i),-i/n*len);X.closePath();
 X.fillStyle=o.col||gl(-W,0,W,0,[[0,o.c0||'#3f8a4a'],[.5,o.c1||'#63b86c'],[1,o.c0||'#3a7d44']]);X.fill();
 if(o.punta){X.save();X.clip();X.fillStyle=o.punta;X.fillRect(-W*1.2,-len*1.05,W*2.4,len*.42);X.restore()}
 X.strokeStyle=o.nerv||'rgba(225,246,205,.6)';X.lineWidth=Math.max(1.5,len*.016);X.lineCap='round';X.beginPath();X.moveTo(0,0);X.lineTo(0,-len*.96);
 for(let i=2;i<n-1;i+=2){const u=i/n,h=hw(i)*.82;X.moveTo(0,-u*len+len*.06);X.lineTo(h,-u*len-len*.03);X.moveTo(0,-u*len+len*.06);X.lineTo(-h,-u*len-len*.03)}X.stroke();X.restore()}
// ---------- mata de hierba gatera en maceta. dobla: -1..1 cuánto se inclinan los tallos ----------
function mata(x,yb,s,t,o){o=o||{};const d=o.dobla||0;X.save();X.translate(x,yb);X.scale(s,s);
 if(o.maceta!==false){X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.ellipse(0,4,124,14,0,0,7);X.fill();X.fillStyle=gl(-92,0,92,0,[[0,'#8a4526'],[.5,'#c2693f'],[1,'#7a3b20']]);X.beginPath();X.moveTo(-92,-150);X.lineTo(92,-150);X.lineTo(70,0);X.lineTo(-70,0);X.closePath();X.fill();
  X.fillStyle='#a5532f';rr(-104,-178,208,36,10);X.fill();X.fillStyle='#3a2a1c';X.beginPath();X.ellipse(0,-174,92,11,0,0,7);X.fill()}
 const base=o.maceta===false?0:-172;
 for(let i=0;i<7;i++){const a=(i-3)*.17+d*.24*(1-Math.abs(i-3)/6)+Math.sin(t*1.5+i)*.02,h=240+rnd(i+(o.sem||0))*120;X.save();X.translate((i-3)*17,base);X.rotate(a);X.strokeStyle='#3d7a45';X.lineWidth=7;X.lineCap='round';X.beginPath();X.moveTo(0,0);X.lineTo(0,-h);X.stroke();
  for(let j=1;j<=3;j++){const y=-h*j/3.3;hoja(0,y,92-j*8,-1.05-d*.2);hoja(0,y,92-j*8,1.05-d*.2)}hoja(0,-h,86,-d*.3);X.restore()}X.restore()}
// ---------- gato panza arriba, rodando ----------
function rueda(x,yb,s,t,o){o=o||{};const c='#8d8f99',c2='#e2e4ea',osc='#5d606b',q=o.quieto?.25:1;X.save();X.translate(x,yb);X.scale(s,s);X.rotate(Math.sin(t*3)*.07*q);X.lineCap='round';
 X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.ellipse(0,4,170,14,0,0,7);X.fill();
 X.strokeStyle=c;X.lineWidth=18;X.beginPath();X.moveTo(-112,-36);X.quadraticCurveTo(-190,-44+Math.sin(t*5)*12*q,-206,-104+Math.sin(t*5)*16*q);X.stroke();
 X.fillStyle=c;X.beginPath();X.ellipse(0,-52,132,54,0,0,7);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(6,-74,92,30,0,0,7);X.fill();
 X.strokeStyle=osc;X.lineWidth=6;[-70,-40,-10].forEach(xx=>{X.beginPath();X.moveTo(xx,-14);X.quadraticCurveTo(xx-8,-30,xx,-44);X.stroke()});
 [[-84,-.35],[-34,.2],[40,-.2],[88,.35]].forEach(([px,a],i)=>{X.save();X.translate(px,-92);X.rotate(a+Math.sin(t*7+i*1.7)*.38*q);X.fillStyle=c;rr(-13,-64,26,70,13);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(0,-62,14,11,0,0,7);X.fill();X.restore()});
 X.translate(132,-62);X.rotate(1.0+Math.sin(t*3.2)*.16*q);X.fillStyle=c;[[-30,-34],[26,-36]].forEach(p=>{X.beginPath();X.moveTo(p[0]-16,p[1]+14);X.lineTo(p[0],p[1]-26);X.lineTo(p[0]+16,p[1]+12);X.closePath();X.fill()});
 X.beginPath();X.ellipse(0,0,50,42,0,0,7);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(8,18,24,15,0,0,7);X.fill();
 X.strokeStyle='#2c2e36';X.lineWidth=4;[[-16,-6],[20,-8]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],9,Math.PI*1.1,Math.PI*1.9);X.stroke()});X.fillStyle='#f48fb1';X.beginPath();X.moveTo(3,10);X.lineTo(13,10);X.lineTo(8,16);X.closePath();X.fill();
 X.strokeStyle='rgba(255,255,255,.75)';X.lineWidth=2;[-5,2,9].forEach(dy=>{X.beginPath();X.moveTo(26,16+dy*.4);X.lineTo(60,10+dy*1.7);X.stroke()});X.restore()}
// ---------- mosquito ----------
function mosq(x,y,s,t,i,o){o=o||{};X.save();X.translate(x,y);X.scale(s*(o.dir||1),s);X.rotate(o.rot===undefined?-.2:o.rot);const f=Math.sin(t*23+i*2);
 X.fillStyle='rgba(225,238,255,.5)';X.beginPath();X.ellipse(-6,-14,22,7,-.5+f*.3,0,7);X.fill();X.beginPath();X.ellipse(4,-14,22,7,.3-f*.3,0,7);X.fill();
 X.strokeStyle='#1d2128';X.lineWidth=2.2;X.lineCap='round';[[-10,4,-22,22],[-2,5,-6,26],[6,4,12,24],[10,2,24,16]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(p[2],p[3]);X.stroke()});
 X.fillStyle='#2a2f38';X.beginPath();X.ellipse(-14,2,16,5,-.15,0,7);X.fill();X.beginPath();X.arc(6,0,7,0,7);X.fill();X.beginPath();X.arc(15,-1,5,0,7);X.fill();X.beginPath();X.moveTo(19,0);X.lineTo(37,5);X.stroke();X.restore()}
const flota=(t,i,a)=>[Math.sin(t*3+i*1.9)*(a||14),Math.cos(t*4.1+i*2.3)*(a||14)*.7];
// ---------- frasco de vidrio con hojas y etiqueta ----------
function frasco(x,yb,s,o){o=o||{};const w=190*s,h=270*s;X.save();X.translate(x,yb);X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(0,4,w*.56,11*s,0,0,7);X.fill();
 if(o.hojas)for(let i=0;i<5;i++)hoja((i-2)*26*s,-12*s,(120+rnd(i+o.hojas)*60)*s,(i-2)*.22,o.h||{});
 rr(-w/2,-h,w,h,24*s);X.fillStyle='rgba(214,236,238,.26)';X.fill();X.strokeStyle='rgba(235,246,250,.75)';X.lineWidth=4*s;X.stroke();X.fillStyle='rgba(255,255,255,.4)';rr(-w/2+14*s,-h+30*s,12*s,h-70*s,6*s);X.fill();
 X.fillStyle='#c9ccd2';rr(-w/2+8*s,-h-22*s,w-16*s,28*s,8*s);X.fill();
 if(o.et!==undefined){const a=o.ea===undefined?1:o.ea;X.fillStyle='#f6f0df';rr(-w/2+16*s,-h*.5,w-32*s,64*s,8*s);X.fill();if(o.et&&a>0){X.globalAlpha=a;txt(o.et,0,-h*.5+34*s,(o.ts||30)*s,'#2a2f38',{w:800});X.globalAlpha=1}}X.restore()}
function guante(x,y,s,rot,conHoja){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.lineCap='round';X.strokeStyle='#b9bec6';X.lineWidth=7;X.beginPath();X.moveTo(-10,90);X.lineTo(-4,210);X.moveTo(18,90);X.lineTo(6,210);X.stroke();
 if(conHoja)hoja(1,214,110,Math.PI,{});
 X.fillStyle='#e9eef2';rr(-74,-330,148,210,30);X.fill();X.fillStyle='#5aa9d6';rr(-70,-140,140,60,22);X.fill();X.beginPath();X.ellipse(0,-20,78,94,0,0,7);X.fill();
 X.fillStyle='#4b97c4';[[-44,60],[-12,86],[24,84]].forEach(p=>{rr(p[0]-17,p[1]-60,34,84,17);X.fill()});X.fillStyle='#5aa9d6';rr(40,-10,36,96,18);X.fill();X.restore()}
// ---------- felino grande de lado (leopardo / jaguar): pelaje con rosetas ----------
function felino(x,yb,s,t,o){const c=o.c,c2=o.c2,d='#3a2a18',J=o.man==='jaguar',rb=o.rub||0;X.save();X.translate(x,yb);X.scale(s*(o.ancho||1),s);X.lineCap='round';X.lineJoin='round';
 X.fillStyle='rgba(0,0,0,.28)';X.beginPath();X.ellipse(0,4,200,16,0,0,7);X.fill();
 X.strokeStyle=c;X.lineWidth=24;X.beginPath();X.moveTo(-150,-160);X.bezierCurveTo(-240,-160,-262,-70,-212,-36+Math.sin(t*2)*8);X.stroke();
 X.fillStyle=o.lej;rr(-126,-112,42,112,17);X.fill();rr(72,-112,42,112,17);X.fill();
 X.fillStyle=c;rr(-172,-206,336,126,60);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(0,-94,122,22,0,0,7);X.fill();
 X.fillStyle=c;rr(-160,-124,46,124,19);X.fill();rr(104,-124,46,124,19);X.fill();X.fillStyle=c2;[-137,127].forEach(q=>{X.beginPath();X.ellipse(q+6,-8,29,12,0,0,7);X.fill()});
 [[-134,-176],[-94,-154],[-60,-182],[-24,-156],[12,-180],[48,-154],[86,-178],[122,-154],[-112,-122],[-42,-126],[30,-124],[94,-120],[-140,-70],[126,-66],[-134,-34],[130,-32]].forEach((p,i)=>{X.strokeStyle=d;X.lineWidth=J?6:5;X.beginPath();X.arc(p[0],p[1],J?13:9,i*1.3,i*1.3+4.7);X.stroke();if(J){X.fillStyle=d;X.beginPath();X.arc(p[0],p[1],3.5,0,7);X.fill()}});
 X.translate(178+rb*16,-214+rb*26);X.rotate(rb*.3+Math.sin(t*5)*.07*rb);
 [-30,28].forEach(q=>{X.fillStyle=c;X.beginPath();X.arc(q,-44,21,0,7);X.fill();X.fillStyle=d;X.beginPath();X.arc(q,-44,10,0,7);X.fill()});
 X.fillStyle=c;X.beginPath();X.ellipse(0,0,64,56,0,0,7);X.fill();X.fillStyle=c2;X.beginPath();X.ellipse(26,24,36,25,0,0,7);X.fill();
 X.fillStyle=d;[[-34,-26],[-12,-36],[-40,6],[-22,30]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],4.5,0,7);X.fill()});
 X.fillStyle='#2a1a12';X.beginPath();X.moveTo(42,8);X.lineTo(60,8);X.lineTo(51,19);X.closePath();X.fill();X.strokeStyle='#2a1a12';X.lineWidth=3.2;X.beginPath();X.moveTo(51,19);X.lineTo(51,27);X.quadraticCurveTo(42,36,31,30);X.stroke();
 if(rb>.4){X.lineWidth=4.5;[[-6,-8],[30,-10]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],9,Math.PI*.1,Math.PI*.9);X.stroke()})}else{[[-6,-8],[30,-10]].forEach(p=>{X.fillStyle='#e9c046';X.beginPath();X.ellipse(p[0],p[1],9,10,0,0,7);X.fill();X.fillStyle='#111';X.beginPath();X.arc(p[0]+1,p[1],4.5,0,7);X.fill()})}
 X.strokeStyle='rgba(255,255,255,.7)';X.lineWidth=1.8;[-5,2,9].forEach(dy=>{X.beginPath();X.moveTo(54,22+dy*.4);X.lineTo(92,16+dy*1.7);X.stroke()});X.restore()}
function casa(L,cm,t,o){o=o||{};const yp=o.yp||1450;interior(L,{p0:o.p0||'#4f7062',p1:o.p1||'#86a78f',tex:'tela',ta:.24,yp,pisoTex:'madera'});const px=par(cm,.4);
 ventanaV(L+(o.vx||60)+px,yp-800,320,380,o.hora||'dia',t,{arbol:1});if(o.rayo!==false)haz(L+(o.vx||60)+160+px,yp-620,L+(o.vx||60)+560+px,yp+140,170,460,'255,244,210',.2)}
function tapete(L,y,col,rx){X.fillStyle=col;X.beginPath();X.ellipse(L+540,y,rx||780,150,0,0,7);X.fill();X.save();X.beginPath();X.ellipse(L+540,y,rx||780,150,0,0,7);X.clip();tex('tela',L-300,y-160,1700,320,{a:.32,v:3});X.restore();X.strokeStyle='rgba(255,255,255,.14)';X.lineWidth=8;X.beginPath();X.ellipse(L+540,y,(rx||780)-60,126,0,0,7);X.stroke()}
function jardin(L,cm,t,o){o=o||{};const yp=o.yp||1400;X.fillStyle='#2f4a2c';X.fillRect(L-900,yp-400,3900,3000);cielo(L-900,-900,3900,yp+900,o.hora||'tarde',t,2);if(o.osc){X.fillStyle=`rgba(8,14,34,${o.osc})`;X.fillRect(L-900,-900,3900,yp+900)}
 const px=par(cm,.55);X.fillStyle=o.seto||'#263d2c';for(let i=0;i<14;i++){const x=L-500+i*190+px,r=110+rnd(i+5)*80;X.beginPath();X.arc(x,yp+10,r,0,7);X.fill()}
 X.fillStyle=gl(0,yp,0,1920,[[0,o.g0||'#4f6f35'],[1,o.g1||'#2c4520']]);X.fillRect(L-900,yp,3900,1500);
 for(let i=0;i<60;i++){const x=L-300+rnd(i+3)*1700,yy=yp+30+rnd(i+40)*480,h=22+rnd(i+80)*30,s=Math.sin(t*1.6+i)*5;X.strokeStyle=`rgba(${rnd(i+9)>.5?'140,185,90':'34,62,24'},.5)`;X.lineWidth=5;X.lineCap='round';X.beginPath();X.moveTo(x,yy);X.quadraticCurveTo(x+s,yy-h*.6,x+s*2,yy-h);X.stroke()}}
function placa(x,y,s,texto,a){if(a<=0)return;X.save();X.globalAlpha=a;tarj(x,y,230*s,96*s,14*s,'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,62*s,'#2a2f38',{w:800});X.restore()}

// ---------- 01 · gancho: una hoja tapa el lente; al retirarse, el gato se frota contra la planta ----------
function p01(L,t){const xc=T.x_crazy,xh=T.x_half,f=T.c02,ab=eio(seg(t,.55,1.7)),rz=Math.sin(t*4.4),q=1-eio(seg(t,xh-.2,xh+.3));
 plano(L,t,[[0,560,1150,1.06],[xc,590,1140,1.14],[f,610,1130,1.24]],cm=>{casa(L,cm,t,{});tapete(L,1520,'#7a4a5a');
  mata(L+760,1500,1.3,t,{dobla:.5+.35*rz*q,sem:2});gato(L+430+14*rz*q,1500,2.35,t,{pose:'parado',inclina:(.16+.12*rz)*q,cola:3})});
 desenfoca(10*(1-ab));
 if(ab<1){const u=ab;X.save();X.translate(L+540-u*900,1500+u*260);X.rotate(-.25-u*.7);hoja(-120,560,2300,.12,{an:.38});X.restore()}
 arriba(L,.62)}

// ---------- 02 · ya lo viste: olfatea, se frota la cara y rueda por el piso ----------
function p02(L,t){const c=T.c02,xr=T.x_rubs,xo=T.x_rolls,f=T.c03,rz=Math.sin(t*5),e=t<xr-.1?0:t<xo-.2?1:2;
 plano(L,t,[[c,460,1250,1.2],[xr,560,1240,1.28],[xo-.2,560,1240,1.28],[xo+.4,440,1280,1.22],[f,410,1290,1.28]],cm=>{
  casa(L,cm,t,{yp:1330,p0:'#5d5a78',p1:'#8f88a8',vx:1600,rayo:false});lamparaPie(L+60+par(cm,.4),1350,1.5,true);tapete(L,1560,'#2f6f73',900);
  [[180,1500,.5],[300,1640,-1],[940,1620,.9],[80,1600,2]].forEach(p=>hoja(L+p[0],p[1],70,p[2],{}));
  mata(L+860,1520,1.25,t,{dobla:e===1?.5+.35*rz:.1,sem:4});
  if(e===0)gato(L+470,1540,2.3,t,{pose:'parado',inclina:.34+.05*Math.sin(t*9),cola:2});
  else if(e===1)gato(L+530+14*rz,1540,2.3,t,{pose:'parado',inclina:.18+.14*rz,cola:3});
  else rueda(L+420,1560,2.3,t,{})});
 arriba(L,.6)}

// ---------- 03 · 2021: mesa botánica, frascos de vidrio, manos con guantes ----------
function p03(L,t){const c=T.c03,xw=T.x_why,f=T.c04,b=eio(seg(t,c+.3,xw));
 plano(L,t,[[c,450,1100,1.1],[f,600,1090,1.08]],cm=>{
  interior(L,{p0:'#34505c',p1:'#5f8290',tex:'baldosa',ta:.14,yp:1330});const px=par(cm,.3);placa(L+250+px,800,1.05,'2021',eio(seg(t,c+.05,c+.4)));
  luz(L+560,520,900,'235,246,255',.24,640);meson(L,1330,{tex:'marmol',col:'#d9d5cc',ta:.9});
  frasco(L+250,1330,1.15,{hojas:3,et:'CATNIP',ts:34});frasco(L+540,1330,1.15,{hojas:9,et:'',h:{c0:'#4a8f6a',c1:'#7cc49a',punta:'rgba(236,244,240,.85)'}});frasco(L+830,1330,1.15,{et:''});
  guante(L+939+lerp(150,0,b),lerp(560,800,b),1.1,.5,true)});
 arriba(L,.58)}

// ---------- 04 · las dos plantas y la sustancia: de la hoja al cerebro del gato ----------
function cabezaGato(x,y,s,br,t){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#16242e';X.strokeStyle='rgba(140,200,220,.7)';X.lineWidth=6;X.lineJoin='round';
 X.beginPath();X.moveTo(-150,-60);X.lineTo(-136,-226);X.lineTo(-52,-150);X.quadraticCurveTo(0,-164,52,-150);X.lineTo(136,-226);X.lineTo(150,-60);X.quadraticCurveTo(170,80,60,150);X.quadraticCurveTo(0,176,-60,150);X.quadraticCurveTo(-170,80,-150,-60);X.closePath();X.fill();X.stroke();
 X.fillStyle='#f48fb1';X.beginPath();X.moveTo(-14,96);X.lineTo(14,96);X.lineTo(0,112);X.closePath();X.fill();
 [-1,1].forEach(q=>{X.fillStyle=`rgba(${q<0?'226,170,196':'214,160,190'},${.75+.2*br})`;X.beginPath();X.moveTo(q*6,-104);X.bezierCurveTo(q*96,-128,q*128,-40,q*104,14);X.bezierCurveTo(q*70,48,q*24,40,q*6,22);X.closePath();X.fill();
  X.strokeStyle='rgba(120,60,90,.55)';X.lineWidth=5;X.lineCap='round';[[20,-80,70,-70,60,-36],[30,-30,80,-30,96,0],[18,-4,50,10,64,26]].forEach(p=>{X.beginPath();X.moveTo(q*p[0],p[1]);X.quadraticCurveTo(q*p[2],p[3],q*p[4],p[5]);X.stroke()})});
 if(br>0){luz(0,6,150,'255,196,90',.75*br);for(let j=0;j<2;j++){const u=(t*.9+j/2)%1;X.strokeStyle=`rgba(255,206,110,${.8*(1-u)*br})`;X.lineWidth=7;X.beginPath();X.arc(0,6,24+u*90,0,7);X.stroke()}X.fillStyle=`rgba(255,226,150,${br})`;X.beginPath();X.arc(0,6,20,0,7);X.fill()}X.restore()}
function p04(L,t){const c=T.c04,xs=T.x_silver,xq=T.x_chemical,xp=T.x_pleasure,f=T.c05,br=eio(seg(t,xp-.2,xp+.4)),sale=eio(seg(t,xq-.2,xq+.4));
 plano(L,t,[[c,470,1400,1.34],[xs,610,1400,1.34],[xq-.2,540,1400,1.3],[xq+1,540,1100,1],[xp-.2,540,1060,1.04],[xp+.9,540,860,1.32],[f,540,850,1.36]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#1d1a3a'],[.55,'#14303a'],[1,'#0f2229']]);X.fillRect(L-900,-900,2900,3800);
  luz(L+540,1420,700,'200,240,255',.26,360);X.fillStyle='#22343c';rr(L+110,1220,860,440,40);X.fill();X.fillStyle='rgba(255,255,255,.06)';rr(L+110,1220,860,12,6);X.fill();
  hoja(L+360,1600,330,-.12,{});hoja(L+720,1600,330,.12,{c0:'#4a8f6a',c1:'#7cc49a',punta:'rgba(236,244,240,.9)',an:.3});
  const a1=eio(seg(t,c+.5,c+.9)),a2=eio(seg(t,xs-.05,xs+.3));if(a1>0){X.globalAlpha=a1;tarj(L+360,1700,260,74,14,'#f6f0df',{sa:.2});txt('CATNIP',L+360,1703,40,'#2a2f38',{w:800});X.globalAlpha=1}
  if(a2>0){X.globalAlpha=a2;tarj(L+720,1700,330,74,14,'#f6f0df',{sa:.2});txt('SILVER VINE',L+720,1703,40,'#2a2f38',{w:800});X.globalAlpha=1}
  {const ac=eio(seg(t,xq-.3,xq+.3));if(ac>0){X.globalAlpha=ac;cabezaGato(L+540,800,1.35,br,t);X.globalAlpha=1}}
  if(sale>0)for(let i=0;i<16;i++){const u=((t-xq)*.42-i*.055),x0=L+(i%2?720:360)+(rnd(i)-.5)*90,y0=1420-rnd(i+4)*120;if(u<0||u>1.25)continue;const q=Math.min(1,u),e=q*q*(3-2*q),x=lerp(x0,L+540,e)+Math.sin(q*6+i)*30*(1-q),y=q<.75?lerp(y0,930,q/.75):lerp(930,808,(q-.75)/.25);
   X.fillStyle=`rgba(${VERDE},${u>1?Math.max(0,1-(u-1)*4):.95})`;X.beginPath();X.arc(x,y,9-3*q,0,7);X.fill();X.fillStyle=`rgba(${VERDE},.22)`;X.beginPath();X.arc(x,y,20-6*q,0,7);X.fill()}});
 arriba(L,.6)}

// ---------- 05 · se siente bien: de cinco a quince minutos ----------
function p05(L,t){const c=T.c05,x5=T.x_five,x15=T.x_fifteen,f=T.c06,rel=eio(seg(t,x5+.1,x5+.5)),o=ruta(t,[[c,500,1150,1.14,-.04],[f,590,1140,1.2,.04]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{interior(L,{p0:'#8a5a3a',p1:'#c08a5a',tex:'tela',ta:.22,yp:1380,pisoTex:'madera'});
  X.fillStyle='rgba(255,226,150,.26)';X.beginPath();X.moveTo(L+120,1420);X.lineTo(L+760,1420);X.lineTo(L+1040,1800);X.lineTo(L+240,1800);X.closePath();X.fill();haz(L+260,560,L+620,1500,150,420,'255,226,150',.2);
  hoja(L+760,1640,90,1.2,{});hoja(L+820,1570,70,-.6,{});
  if(rel<.5)rueda(L+500,1600,2.3,t,{});else gato(L+500,1620,2.5,t,{pose:'sentado',lento:true,cola:1})},o[3]);
 arriba(L,.58);
 const a=eio(seg(t,x5-.35,x5)),p=ruta(t,[[c,0],[x5-.3,0],[x5+.15,1/3],[x15-.3,1/3],[x15+.3,1]])[0],x0=L+150,w=780,y=1705;if(a>0){X.save();X.globalAlpha=a;
  X.fillStyle='rgba(20,12,8,.6)';rr(x0-40,y-96,w+80,170,30);X.fill();X.fillStyle='rgba(255,255,255,.22)';rr(x0,y,w,22,11);X.fill();X.fillStyle='#ffd166';rr(x0,y,Math.max(22,w*p),22,11);X.fill();X.beginPath();X.arc(x0+w*p,y+11,22,0,7);X.fill();
  txt('5 MIN',x0+w/3,y-44,48,p>=1/3-.01?'#fff':'rgba(255,255,255,.0)',{w:800});const b=eio(seg(t,x15-.05,x15+.25));if(b>0){X.globalAlpha=a*b;txt('15 MIN',x0+w-70,y-44,48,'#fff',{w:800})}X.restore()}}

// ---------- 06 · G2: la hoja llena el cuadro y su sombra tiene forma de escudo ----------
function escudo(x,y,s){X.beginPath();X.moveTo(x-200*s,y-260*s);X.quadraticCurveTo(x,y-310*s,x+200*s,y-260*s);X.lineTo(x+200*s,y+10*s);X.quadraticCurveTo(x+190*s,y+210*s,x,y+320*s);X.quadraticCurveTo(x-190*s,y+210*s,x-200*s,y+10*s);X.closePath()}
function p06(L,t){const c=T.c06,xo=T.x_other,xm=T.x_misses,f=T.c07,d=eio(seg(t,c+.3,xm)),sh=eio(seg(t,xo-.3,xo+.2)),g=golpe(t,xo,.6);
 plano(L,t,[[c,520,1120,1.06],[xo,560,1100,1.2],[f,585,1090,1.3]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,`rgb(${Math.round(lerp(150,54,d))},${Math.round(lerp(112,50,d))},${Math.round(lerp(72,96,d))})`],[1,`rgb(${Math.round(lerp(206,112,d))},${Math.round(lerp(168,88,d))},${Math.round(lerp(112,128,d))})`]]);X.fillRect(L-900,-900,2900,3800);tex('concreto',L-400,300,1900,1700,{a:.16,v:6});
  if(d>.05){X.globalAlpha=d;X.fillStyle='#2a2f45';for(let i=0;i<9;i++){X.beginPath();X.arc(L-200+i*190+par(cm,.5),1840,130+rnd(i+5)*90,0,7);X.fill()}X.globalAlpha=1}
  luz(L+220,1500,900,'255,190,110',.3*(1-.4*d));
  X.save();X.globalAlpha=.34*(1-sh);X.translate(L+760,1530);X.rotate(.2);X.scale(1.25,1.05);hoja(0,0,640,0,{col:'#0c0a12',nerv:'rgba(0,0,0,0)'});X.restore();
  if(sh>0){X.fillStyle=`rgba(12,10,20,${.42*sh})`;escudo(L+770,1150,(.9+.14*sh+.05*g));X.fill();X.strokeStyle=`rgba(255,236,190,${.35*sh+.4*g})`;X.lineWidth=7;escudo(L+770,1150,(.9+.14*sh+.05*g));X.stroke()}
  X.strokeStyle='#3d7a45';X.lineWidth=16;X.lineCap='round';X.beginPath();X.moveTo(L+330,1960);X.quadraticCurveTo(L+350,1700,L+400,1560);X.stroke();hoja(L+400,1570,760,.1+Math.sin(t*1.3)*.02,{})});
 arriba(L,.58)}

// ---------- 07 · se frotaban la planta por la cara y la cabeza (macro) ----------
function p07(L,t){const c=T.c07,xr=T.x_rubbing,xf=T.x_face,xh=T.x_head,f=T.c08,on=.45+.55*eio(seg(t,xr-.6,xr)),rz=Math.sin(t*4.6)*on,alto=eio(seg(t,xh-.3,xh+.1));
 const kf=[[c,560,1190,1.04],[xr,600,1180,1.14],[f,640,1160,1.22]];
 plano(L,t,kf,cm=>{jardin(L,cm,t,{yp:1500});[[200,700,90],[820,620,120],[520,560,70]].forEach((p,i)=>luz(L+p[0]+par(cm,.6),p[1],p[2],'255,214,150',.3))});
 desenfoca(7);
 plano(L,t,kf,cm=>{const d=.3+.5*on+.3*rz;
  X.strokeStyle='#3d7a45';X.lineWidth=14;X.lineCap='round';[[880,.0],[960,.12],[800,-.1]].forEach(([x,a],i)=>{X.save();X.translate(L+x,1960);X.rotate(a+d*.16);X.beginPath();X.moveTo(0,0);X.lineTo(0,-760);X.stroke();
   [300,470,640].forEach((y,j)=>{hoja(0,-y,250-j*20,-1.0-d*.32,{});hoja(0,-y,250-j*20,1.0-d*.2,{})});hoja(0,-760,240,-d*.4,{});X.restore()});
  gato(L+150+26*rz+40*on,lerp(1820,1900,alto),4.1,t,{pose:'parado',inclina:lerp(.2+.12*rz,-.26+.1*rz,alto)*on,cola:2,lento:on>.5})});
 arriba(L,.62)}

// ---------- 08 · entonces llevaron mosquitos: jardín de noche, pocos insectos junto a la luz ----------
function farol(x,yb,s){X.fillStyle='#1a1f2a';X.fillRect(x-7*s,yb-520*s,14*s,520*s);rr(x-44*s,yb-640*s,88*s,124*s,14*s);X.fill();X.fillStyle='#ffe2a0';rr(x-32*s,yb-626*s,64*s,96*s,10*s);X.fill();luz(x,yb-580*s,360*s,'255,214,140',.5)}
function p08(L,t){const c=T.c08,f=T.c09,en=eio(seg(t,c,c+.8));
 plano(L,t,[[c,400,1080,1.1],[f,700,1010,1.62]],cm=>{jardin(L,cm,t,{hora:'noche',osc:.3,seto:'#101c22',g0:'#1f3526',g1:'#122018',yp:1420});farol(L+250,1480,1.2);
  [[720,1000,2.2],[470,860,1.3],[900,1180,1.2]].forEach((p,i)=>{const fl=flota(t,i,16);X.globalAlpha=eio(seg(t,c+i*.25,c+.5+i*.25));mosq(L+p[0]+fl[0]+(1-en)*260,p[1]+fl[1],p[2],t,i,{dir:-1});X.globalAlpha=1})});
 arriba(L,.6)}

// ---------- 09 · comparación sobria: a los que se frotaron se les posaron muchos menos ----------
function p09(L,t){const c=T.c09,xf=T.x_fewer,f=T.c10,en=eio(seg(t,c+.2,xf+.4));
 plano(L,t,[[c,360,1120,1.16],[xf,560,1110,1.08],[f,540,1100,1.04]],cm=>{
  X.fillStyle=gl(0,0,0,1920,[[0,'#0e1a2c'],[1,'#1e3344']]);X.fillRect(L-900,-900,2900,3800);
  X.strokeStyle='rgba(160,200,220,.10)';X.lineWidth=3;for(let i=-8;i<26;i++){X.beginPath();X.moveTo(L+i*60,300);X.lineTo(L+i*60,1500);X.stroke()}for(let j=0;j<21;j++){X.beginPath();X.moveTo(L-400,300+j*60);X.lineTo(L+1500,300+j*60);X.stroke()}
  X.fillStyle='#16242c';X.fillRect(L-900,1480,2900,900);X.fillStyle='rgba(255,255,255,.08)';X.fillRect(L-900,1480,2900,8);
  X.fillStyle='rgba(255,255,255,.18)';X.fillRect(L+536,560,8,1000);
  luz(L+270,1150,460,VERDE,.14);X.save();X.translate(L+270,640);tarj(0,0,130,130,65,'#1f3b2c',{sa:.2});hoja(0,44,88,0,{});X.restore();
  gato(L+270,1480,2.2,t,{pose:'sentado',cola:1.5,lento:true});gato(L+810,1480,2.2,t,{pose:'sentado',cola:4,dir:-1,inclina:.08*Math.sin(t*6)});
  {const fl=flota(t,9,18);mosq(L+lerp(520,440,en)+fl[0],lerp(760,700,en)+fl[1],1.3,t,9,{dir:1,rot:-.5})}
  [[850,1180,0],[740,1260,1],[905,1330,2],[800,1050,3],[690,1160,4],[930,1240,5]].forEach((p,i)=>{const u=eio(seg(t,c+.25+i*.22,c+.9+i*.22)),fl=flota(t,i,u<1?16:2);mosq(lerp(L+1160+i*20,L+p[0],u)+fl[0],lerp(700+i*90,p[1],u)+fl[1],1.25,t,i,{dir:-1,rot:u<1?-.2:.5})})});
 arriba(L,.6)}

// ---------- 10 · lo mismo que excita al gato aleja a los bichos; leopardos y jaguares también lo hicieron ----------
function p10(L,t){const c=T.c10,xb=T.x_bugs,xl=T.x_leopards,xj=T.x_jaguars,f=T.c11,rz=Math.sin(t*4.5),A=1300,B=2600;
 plano(L,t,[[c,540,1130,1.12],[xl-.5,560,1130,1.14],[xl,A+540,1130,1.1],[xj+.3,A+560,1130,1.12],[xj+.8,B+540,1130,1.1],[f,B+570,1130,1.14]],cm=>{
  jardin(L,{0:540},t,{yp:1450});mata(L+760,1500,1.3,t,{dobla:.5+.3*rz,sem:2,maceta:false});gato(L+440+12*rz,1500,2.3,t,{pose:'parado',inclina:.16+.12*rz,cola:3,lento:true});
  [[300,900],[620,760]].forEach((p,i)=>{const u=eio(seg(t,xb-.9,xb-.2)),v=eio(seg(t,xb-.1,xb+.7)),fl=flota(t,i,12);mosq(L+p[0]+fl[0]-v*760*(i?-1:1)+(1-u)*(i?520:-520),p[1]-v*60+fl[1],1.4,t,i,{dir:(i?-1:1)*(v>.3?-1:1)})});
  // sabana (leopardo)
  X.fillStyle=gl(0,0,0,1450,[[0,'#e8a04a'],[1,'#f6d79a']]);X.fillRect(L+A-110,-900,1300,2400);X.fillStyle='#fff2c8';X.beginPath();X.arc(L+A+820,760,90,0,7);X.fill();
  X.fillStyle='#6b4a2a';X.fillRect(L+A+190,880,22,570);X.beginPath();X.ellipse(L+A+200,870,250,60,0,0,7);X.fill();X.beginPath();X.ellipse(L+A+330,820,150,40,0,0,7);X.fill();
  X.fillStyle=gl(0,1450,0,1920,[[0,'#c9a24a'],[1,'#8a6a2a']]);X.fillRect(L+A-110,1450,1300,900);tex('arena',L+A-110,1450,1300,500,{a:.3});
  X.fillStyle='#7d7468';X.beginPath();X.ellipse(L+A+420,1560,470,120,0,Math.PI,0);X.fill();
  mata(L+A+800,1470,1.35,t,{dobla:.5+.3*rz,sem:6,maceta:false});felino(L+A+420,1470,1.55,t,{c:'#e0b04a',c2:'#f7e6bc',lej:'#b98d34',rub:.6+.4*rz});
  // selva (jaguar)
  X.fillStyle=gl(0,0,0,1450,[[0,'#0f2a22'],[1,'#1f4a36']]);X.fillRect(L+B-110,-900,1400,2400);
  for(let i=0;i<9;i++){X.save();X.translate(L+B-60+i*150,560+rnd(i)*260);X.rotate(2.6+rnd(i+3)*1.2);hoja(0,0,330,0,{c0:'#1d5a3a',c1:'#2f7a4e',nerv:'rgba(180,230,190,.25)',an:.3});X.restore()}
  X.fillStyle='#143024';X.fillRect(L+B-110,1450,1400,900);X.fillStyle='rgba(120,200,190,.18)';X.beginPath();X.ellipse(L+B+300,1700,620,80,0,0,7);X.fill();
  mata(L+B+820,1470,1.4,t,{dobla:.5+.3*rz,sem:8,maceta:false});felino(L+B+420,1470,1.6,t,{c:'#cf9434',c2:'#f1dcae',lej:'#a47426',man:'jaguar',ancho:1.1,rub:.6+.4*rz});
  X.fillStyle='#0c0a10';X.fillRect(L+A-110,-900,14,3800);X.fillRect(L+B-110,-900,14,3800)});
 arriba(L,.62)}

// ---------- 11 · no es solo una fiesta: puede que se esté poniendo repelente ----------
function p11(L,t){const c=T.c11,xs=T.x_spray,f=T.c12,w=seg(t,c,f),gx=lerp(330,720,eio(w)),v=eio(seg(t,xs-.5,xs+.5));
 plano(L,t,[[c,440,1170,1.2],[f,700,1160,1.24]],cm=>{jardin(L,cm,t,{yp:1420});luz(L+900+par(cm,.55),1040,560,'255,190,120',.35);
  mata(L+170,1500,1.3,t,{dobla:-.2,sem:2,maceta:false});gato(L+gx,1520,2.3,t,{pose:'parado',camina:true,cola:3});
  [[1000,980],[1090,1160]].forEach((p,i)=>{const fl=flota(t,i,12);mosq(L+gx+lerp(560,250,eio(seg(t,c+.3,xs-.4)))+v*420+fl[0]+i*70,p[1]-v*200+fl[1],1.4,t,i,{dir:v>.3?1:-1})});
  for(let i=0;i<4;i++){const u=(t*.8+i/4)%1;X.fillStyle=`rgba(${VERDE},${.7*(1-u)*eio(seg(t,c+.4,c+1))})`;X.beginPath();X.arc(L+gx+170+Math.sin(i*2.4)*60,1250-u*90+Math.cos(i*1.7)*40,5+3*(1-u),0,7);X.fill()}});
 tinte(L,'255,170,90',.05);arriba(L,.6)}

// ---------- 12 · CTA: el gato junto a la maceta, olfatea y mira a cámara ----------
function p12(L,t){const c=T.c12,kf=[[c,480,1170,1.12],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],mira=eio(seg(t,c+1.1,c+1.6));
 plano(L,t,kf,cm=>{casa(L,cm,t,{yp:1490,p0:'#6b4a3a',p1:'#a67a56',hora:'tarde',vx:660,rayo:false});sofaV(L+900,1520,1.2,['#3f6f6a','#2c504c'])});
 desenfoca(6);
 plano(L,t,kf,cm=>{tapete(L,1520,'#7a4a5a',700);mata(L+215,1500,.78,t,{dobla:.25*(1-mira),sem:2});gato(L+480,1500,1.55,t,{pose:'sentado',dir:mira>.5?1:-1,inclina:mira>.5?0:.2,cola:2,lento:mira>.5})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12].forEach((f,i)=>{NUEVOS['dc_scats16_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SCATS16 · FIN =====
</script>
