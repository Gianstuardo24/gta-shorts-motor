<script>
// ===== DC · SRABBIT22 · INICIO ===== (Rabbit 22h · Your BRAIN Is LYING About This Mars Photo · lote del 28-nov · una escena por línea del guion)
// La colina es un dibujo propio (no la fotografía real). cara: 0..1 cuánto arman un rostro las sombras · det: 0..1 detalle rocoso de las fotos nítidas.
// En el gancho el rostro aparece, se deshace al cambiar la luz y vuelve con la foto: no se adelanta el final. Sin evidencia "alienígena": solo la superposición que la gente imaginó.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,noche,planeta,hojaP,renglones,tarj,silueta,desenfoca,borroso}=window.B28;
const PAPEL='#efe6d0',TINTA='#2a2019',ROJO='255,150,100';
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({manga:'#e9eef2',puno:'#cfd6dc'},o))};

function colina(x,y,s,o){o=o||{};const ca=o.cara===undefined?1:o.cara,de=o.det||0,gr=o.gris,sh=gr?'rgba(20,18,16,':'rgba(60,24,12,',lu=gr?'rgba(255,255,255,':'rgba(255,230,200,';X.save();X.translate(x,y);X.rotate(o.rot||0);X.scale(s,s);
 X.fillStyle=sh+'.5)';X.beginPath();X.ellipse(26+(o.sx||0),30,250,300,0,0,7);X.fill();X.fillStyle=gl(-240,-290,240,290,[[0,gr?'#b9b4aa':'#c98a5a'],[1,gr?'#6a665e':'#8a4f30']]);X.beginPath();X.ellipse(0,0,240,290,0,0,7);X.fill();
 X.strokeStyle=lu+'.38)';X.lineWidth=14;X.beginPath();X.ellipse(0,0,232,282,0,Math.PI*.9,Math.PI*1.6);X.stroke();
 if(ca>0){X.fillStyle=sh+(.8*ca)+')';X.beginPath();X.ellipse(-92,-70,58,36,.15,0,7);X.fill();X.beginPath();X.ellipse(88,-76,56,34,-.15,0,7);X.fill();X.beginPath();X.moveTo(-14,-40);X.quadraticCurveTo(34,30,-20,72);X.quadraticCurveTo(-4,10,-14,-40);X.fill();X.beginPath();X.ellipse(0,150,110,24,0,0,7);X.fill();X.fillStyle=lu+(.26*ca)+')';X.beginPath();X.ellipse(-32,18,20,58,.2,0,7);X.fill()}
 if(de>0){X.strokeStyle=sh+(.5*de)+')';X.lineWidth=5;X.lineCap='round';[[-180,-150,-90,-40,-150,60],[60,-220,110,-120,40,-40],[-60,90,20,140,-40,230],[120,20,170,110,110,200],[-200,40,-140,120,-170,190]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.quadraticCurveTo(p[2],p[3],p[4],p[5]);X.stroke()});
  for(let i=0;i<26;i++){const a=rnd(i+3)*6.28,r=Math.sqrt(rnd(i+17))*.9,px=Math.cos(a)*r*220,py=Math.sin(a)*r*270;X.fillStyle=sh+(.36*de)+')';X.beginPath();X.ellipse(px,py,8+rnd(i)*16,6+rnd(i+5)*10,rnd(i+9)*3,0,7);X.fill();X.fillStyle=lu+(.22*de)+')';X.beginPath();X.ellipse(px-8,py-8,7+rnd(i)*10,5+rnd(i+5)*6,rnd(i+9)*3,0,7);X.fill()}}X.restore()}
// terreno visto desde arriba, alrededor de (0,0), para un recuadro w×h
function terreno(w,h,gr,sem){X.fillStyle=gl(-w/2,-h/2,w/2,h/2,[[0,gr?'#8f8a80':'#b06a44'],[1,gr?'#5c5850':'#7a3f28']]);X.fillRect(-w/2,-h/2,w,h);const sh=gr?'rgba(20,18,16,':'rgba(60,24,12,',lu=gr?'rgba(255,255,255,':'rgba(255,225,190,';
 for(let i=0;i<16;i++){const x=(rnd(i+(sem||0))-.5)*w,y=(rnd(i+40+(sem||0))-.5)*h,r=14+rnd(i+80)*38;if(Math.hypot(x/1.2,y)<330)continue;X.fillStyle=sh+'.35)';X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle=lu+'.3)';X.lineWidth=4;X.beginPath();X.arc(x,y,r,Math.PI*.9,Math.PI*1.7);X.stroke()}
 for(let i=0;i<10;i++){const x=(rnd(i+7+(sem||0))-.5)*w,y=(rnd(i+57+(sem||0))-.5)*h;if(Math.hypot(x/1.2,y)<360)continue;X.fillStyle=lu+'.16)';X.beginPath();X.ellipse(x,y,40+rnd(i)*50,26+rnd(i+3)*30,rnd(i)*3,0,7);X.fill();X.fillStyle=sh+'.3)';X.beginPath();X.ellipse(x+12,y+14,40+rnd(i)*50,22+rnd(i+3)*26,rnd(i)*3,0,7);X.fill()}}
function mosaico(w,h,tam,a,sem){if(a<=0)return;for(let y=-h/2;y<h/2;y+=tam)for(let x=-w/2;x<w/2;x+=tam){const v=rnd((x*7.3+y*3.1+(sem||0))*.37);X.fillStyle=v>.5?`rgba(255,255,255,${a*(v-.5)*.6})`:`rgba(0,0,0,${a*(.5-v)*.7})`;X.fillRect(x,y,tam+1,tam+1)}}
// foto en papel: marco blanco y adentro el terreno gris con la colina
function foto(x,y,w,rot,o){o=o||{};const h=w*1.18;X.save();X.translate(x,y);X.rotate(rot||0);if(o.a!==undefined)X.globalAlpha=o.a;X.fillStyle='rgba(0,0,0,.35)';X.fillRect(-w/2+10,-h/2+14,w,h);X.fillStyle='#f4f1ea';X.fillRect(-w/2,-h/2,w,h);
 const m=w*.06;X.save();X.beginPath();X.rect(-w/2+m,-h/2+m,w-2*m,h-2*m-w*.08);X.clip();X.translate(0,-w*.04);terreno(w,h,true,3);colina(0,0,w/760,{gris:1,cara:o.cara===undefined?1:o.cara,det:o.det||0});mosaico(w,h,w/(o.px||22),o.pix===undefined?.5:o.pix,5);if(o.sobre)o.sobre(w);X.restore();X.restore()}
function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#e9e4d6',{sa:.25});txt(texto,x,y+4*s,(o.ts||50)*s,o.tc||'#2a2f38',{w:800});X.restore()}
function escritorio(L,o){o=o||{};X.fillStyle=o.col||'#3a2a1e';X.fillRect(L-1400,-900,5200,3800);tex('madera',L-600,200,4000,1900,{a:.9,s:1.9,v:o.v||5,tinte:o.tinte||'rgba(20,10,6,.35)'})}
function orbitador(x,y,s,rot,t){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='#2f5fb0';[[-150,-34],[62,-34]].forEach(p=>{X.fillRect(p[0],p[1],88,68);X.strokeStyle='rgba(255,255,255,.35)';X.lineWidth=2;X.strokeRect(p[0],p[1],88,68);X.beginPath();X.moveTo(p[0]+44,p[1]);X.lineTo(p[0]+44,p[1]+68);X.stroke()});
 X.fillStyle=gl(0,-46,0,46,[[0,'#e9eef2'],[1,'#9aa3ad']]);rr(-62,-46,124,92,12);X.fill();X.fillStyle='#f2c94c';rr(-40,-30,80,36,6);X.fill();X.fillStyle='#e9eef2';X.beginPath();X.ellipse(0,-66,46,16,0,0,7);X.fill();X.fillStyle='#22262b';rr(-16,46,32,30,6);X.fill();X.fillStyle='#4a90d0';X.beginPath();X.arc(0,74,10,0,7);X.fill();X.restore()}

// ---------- 01 · gancho: el rostro en la colina; cambia la luz y se deshace; con la foto vuelve. Después, la nota ----------
function p01(L,t){const xl=T.x_lying,x7=T.x_1976,xe=T.x_everywhere,xf=T.x_few,xn=T.x_nasa,f=T.c02,des=eio(seg(t,xl+.3,xl+1.5)),fo=eio(seg(t,x7-.35,x7+.05)),fl=golpe(t,x7-.1,.55),mu=eio(seg(t,xe-.2,xe+.6)),no=eio(seg(t,xf-.2,xf+.6)),br=eio(seg(t,xn-.3,xn+.3));
 const o=ruta(t,[[0,540,1080,1.3,-.05],[xl+1.5,560,1070,1.16,.04],[x7,540,1080,1.1,0],[xe+.6,540,1100,.96,0],[xf+.6,620,1110,.98,0],[f,650,1110,1.04,0]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{
  if(fo<1){X.save();X.translate(L+540,1080);terreno(2600,3000,false,1);colina(0,0,1.25,{cara:1-.85*des,sx:-70*des});X.restore();haz(L+lerp(-200,1300,des),300,L+540,1080,60,700,'255,220,170',.14)}
  if(fo>0){X.save();X.globalAlpha=fo;escritorio(L);X.restore();if(mu>0){foto(L+540-250*mu,1090+40*mu,620,-.13*mu,{a:fo});foto(L+540+250*mu,1100+30*mu,620,.12*mu,{a:fo})}foto(L+540,1080,lerp(1500,700,fo),-.02,{a:fo,pix:.5*fo});
   if(no>0){hojaP(L+lerp(1700,1010,no),1250,400,500,.07,()=>{X.fillStyle=TINTA;X.fillRect(-160,-210,200,18);renglones(-160,-160,320,9,10,4);X.fillStyle=`rgba(255,214,90,${.75*br})`;X.fillRect(-166,-52,332,34)});X.fillStyle='#8e98a4';rr(L+lerp(1700,1010,no)-150,990,26,70,10);X.fill()}}
  if(fl>0){X.fillStyle=`rgba(255,255,255,${.5*fl})`;X.fillRect(L-900,-900,2900,3800)}},o[3]);
 arriba(L,.6)}

// ---------- 02 · julio de 1976: Viking 1 da vueltas a Marte buscando dónde aterrizar ----------
function p02(L,t){const c=T.c02,xv=T.x_viking,xl=T.x_landing,f=T.c03,u=seg(t,c,f),baja=eio(seg(t,xl-.6,xl+.5)),ox=L+lerp(200,760,u),oy=lerp(820,760,u);
 plano(L,t,[[c,440,1040,1.08],[xl-.6,600,1040,1.1],[xl+.5,640,1560,1.5],[f,680,1580,1.56]],cm=>{noche(L,t,{c0:'#05070f',c1:'#101832',y1:1920,n:70,ys:420,yh:900,sem:3});
  luz(L+540,2500,1500,ROJO,.25);planeta(L+540,2700,1400,{c0:'#d98456',c1:'#8a3f2a',atm:'255,180,140',giro:-u*160});
  X.save();X.beginPath();X.arc(L+540,2700,1400,0,7);X.clip();[[420,1500,60],[700,1620,90],[900,1480,40],[300,1700,50]].forEach(p=>{X.fillStyle='rgba(60,24,12,.3)';X.beginPath();X.ellipse(L+p[0]-u*160,p[1],p[2],p[2]*.5,0,0,7);X.fill()});X.save();X.translate(L+660,1590);X.scale(1,.55);colina(0,0,.34,{cara:.9});X.restore();X.restore();
  haz(ox,oy+60,ox+lerp(-40,-90,u),1560,14,150,'255,236,200',.2+.1*Math.sin(t*5));orbitador(ox,oy,1.25,.12,t);
  if(baja>0){const rx=L+660+Math.sin(t*2.2)*60*(1-baja),ry=1590+Math.cos(t*1.7)*30*(1-baja);X.strokeStyle=`rgba(255,255,255,${.85*baja})`;X.lineWidth=4;X.beginPath();X.arc(rx,ry,70,0,7);X.stroke();[0,1.57,3.14,4.71].forEach(a=>{X.beginPath();X.moveTo(rx+Math.cos(a)*80,ry+Math.sin(a)*80);X.lineTo(rx+Math.cos(a)*112,ry+Math.sin(a)*112);X.stroke()})}});
 placa(L+250,560,1,'JULY 1976',eio(seg(t,c+.05,c+.4))*(1-eio(seg(t,xv-.5,xv-.2))),{ts:50});placa(L+230,560,1,'VIKING 1',eio(seg(t,xv-.15,xv+.2))*(1-eio(seg(t,xl+.2,xl+.6))),{ts:54});arriba(L,.6)}

// ---------- 03 · una foto mostraba una colina de más de una milla, con dos ojos, una nariz y una boca ----------
function p03(L,t){const c=T.c03,xm=T.x_mile,xe=T.x_eyes,xn=T.x_nose,xb=T.x_mouth,f=T.c04,ras=seg(t,c,f),W=820,k=W/760;
 plano(L,t,[[c,540,1100,1.04],[xe,540,1080,1.26],[f,540,1070,1.36]],cm=>{escritorio(L,{v:6});luz(L+lerp(100,900,ras),700,700,'255,236,200',.22);
  foto(L+540,1090,W,-.03,{pix:.45,sobre:(w)=>{const R=(x,y,rx,ry,a)=>{if(a<=0)return;X.strokeStyle=`rgba(255,255,255,${a})`;X.lineWidth=5;X.beginPath();X.ellipse(x*k,y*k,rx*k,ry*k,0,0,7);X.stroke()};
    R(-92,-70,74,50,eio(seg(t,xe-.1,xe+.2)));R(88,-76,72,48,eio(seg(t,xe+.05,xe+.35)));R(-6,16,44,74,eio(seg(t,xn-.1,xn+.2)));R(0,150,128,40,eio(seg(t,xb-.1,xb+.2)));
    const q=eio(seg(t,xm-.3,xm+.1))*(1-eio(seg(t,xe-.3,xe)));if(q>0){X.strokeStyle=`rgba(255,255,255,${q})`;X.lineWidth=5;X.beginPath();X.moveTo(-250*k,330*k);X.lineTo(250*k,330*k);X.moveTo(-250*k,312*k);X.lineTo(-250*k,348*k);X.moveTo(250*k,312*k);X.lineTo(250*k,348*k);X.stroke()}}});
  placa(L+540,1640,1,'MORE THAN 1 MILE',eio(seg(t,xm-.3,xm+.1))*(1-eio(seg(t,xe-.3,xe))),{ts:44,w:520})});
 arriba(L,.6)}

// ---------- 04 · mucha gente vio una cara gigante que miraba desde Marte: diario, pared, pantalla ----------
function p04(L,t){const c=T.c04,f=T.c05;
 plano(L,t,[[c,420,1120,1.1],[f,1560,1110,1.1]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#2a2430'],[1,'#4a3a44']]);X.fillRect(L-1400,-900,5600,3800);tex('ladrillo',L-500,300,3600,1300,{a:.12,v:2});X.fillStyle='#1c161c';X.fillRect(L-1400,1560,5600,900);
  hojaP(L+330,1130,560,760,-.04,()=>{X.fillStyle=TINTA;X.fillRect(-240,-340,480,46);X.fillRect(-240,-276,360,22);foto(0,10,360,0,{});renglones(-240,250,480,5,10,2)},PAPEL);
  X.fillStyle='#17131c';X.fillRect(L+830,640,460,620);foto(L+1060,950,400,0,{});X.fillStyle='#c0392b';[[850,660],[1270,660]].forEach(p=>{X.beginPath();X.arc(L+p[0],p[1],10,0,7);X.fill()});
  X.fillStyle='#3a3028';rr(L+1560,760,520,470,36);X.fill();X.fillStyle='#0c0c10';rr(L+1596,796,360,398,40);X.fill();X.save();X.beginPath();rr(L+1604,804,344,382,34);X.clip();X.translate(L+1776,995);terreno(400,440,true,3);colina(0,0,.45,{gris:1});X.fillStyle='rgba(120,200,255,.08)';for(let i=0;i<24;i++)X.fillRect(-200,-220+i*18+((t*40)%18),400,6);X.restore();[[2000,860],[2000,960]].forEach(p=>{X.fillStyle='#1c161c';X.beginPath();X.arc(L+p[0],p[1],26,0,7);X.fill()});X.fillStyle='#2a221c';X.fillRect(L+1700,1230,240,330);
  [[120,1.5],[640,1.75],[1330,1.6],[1500,1.85],[2100,1.6]].forEach(([x,s],i)=>silueta(L+x,1960+i%2*30,s,i%2?'#0c0a0e':'#120e14',{}))});
 arriba(L,.6)}

// ---------- 05 · algunos se convencieron de que alguien la había construido (superposición momentánea, después se separan) ----------
function mascara(x,y,s,a){if(a<=0)return;X.save();X.translate(x,y);X.scale(s,s);X.globalAlpha=a;X.strokeStyle='#f2c94c';X.lineWidth=7;X.lineJoin='round';X.lineCap='round';X.beginPath();X.ellipse(0,0,236,286,0,0,7);X.stroke();[-1,1].forEach(q=>{X.beginPath();X.moveTo(q*36,-72);X.quadraticCurveTo(q*92,-112,q*150,-72);X.quadraticCurveTo(q*92,-40,q*36,-72);X.stroke()});X.beginPath();X.moveTo(-14,-50);X.lineTo(-34,70);X.lineTo(26,70);X.closePath();X.stroke();X.beginPath();X.moveTo(-110,150);X.quadraticCurveTo(0,120,110,150);X.quadraticCurveTo(0,186,-110,150);X.stroke();
 X.setLineDash([10,12]);X.lineWidth=4;[[-236,0,-300,0],[236,0,300,0],[0,-286,0,-340]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(p[2],p[3]);X.stroke()});X.setLineDash([]);X.restore()}
function p05(L,t){const c=T.c05,xb=T.x_built,f=T.c06,en=eio(seg(t,c+.2,c+1.2)),sep=eio(seg(t,xb+.1,f));
 plano(L,t,[[c,540,1090,1.08],[xb,540,1085,1.3],[f,570,1085,1.22]],cm=>{X.save();X.translate(L+540,1090);terreno(2600,3000,true,1);colina(0,0,1.25,{gris:1});mosaico(1300,1500,34,.4,5);X.restore();
  mascara(L+540+sep*330,1090-sep*40,1.25,en*(1-.75*sep))});
 arriba(L,.6)}

// ---------- 06 · G2: la parte que pocos conocen. La foto y la nota de archivo sobre la mesa ----------
function nota(x,y,w,rot,o){o=o||{};hojaP(x,y,w,w*1.25,rot,()=>{const k=w/400;X.fillStyle=TINTA;X.fillRect(-160*k,-210*k,200*k,18*k);X.fillStyle='rgba(42,32,25,.5)';X.fillRect(-160*k,-180*k,120*k,8*k);renglones(-160*k,-140*k,320*k,4,10*k,4);
  if(o.texto>0){X.fillStyle=`rgba(255,214,90,${.85*o.texto})`;X.fillRect(-170*k,-62*k,340*k,104*k);X.globalAlpha=o.texto;txt('resembled a',0,-34*k,34*k,TINTA,{w:800});txt('human head',0,14*k,34*k,TINTA,{w:800});X.globalAlpha=1}
  else{if(o.marca>0){X.fillStyle=`rgba(255,214,90,${.8*o.marca})`;X.fillRect(-168*k,-56*k,336*k,44*k)}renglones(-160*k,-44*k,320*k,4,10*k,7)}
  renglones(-160*k,60*k,320*k,6,10*k,9)},PAPEL)}
function p06(L,t){const c=T.c06,xi=T.x_itself,xs=T.x_story,f=T.c07,fo=eio(seg(t,xi-.5,xi+.1)),g=golpe(t,xi,.6);
 const kf=[[c,500,1100,1],[xi-.4,560,1100,1.1],[xi+.3,800,1140,1.6],[f,820,1150,1.72]];
 plano(L,t,kf,cm=>{escritorio(L,{v:7,tinte:'rgba(10,8,20,.45)'});luz(L+820,1000,620,'255,236,200',.16+.2*g);borroso(6*fo,()=>foto(L+300,1080,520,-.08,{}))});
 plano(L,t,kf,cm=>{borroso(5*(1-fo),()=>nota(L+800,1120,460,.05,{marca:fo}))});
 arriba(L,.6)}

// ---------- 07 · los científicos creían que era solo una colina con sombras raras: cambian la luz sobre una maqueta ----------
function p07(L,t){const c=T.c07,xh=T.x_hill,xs=T.x_shadows,f=T.c08,u=eio(seg(t,c+.4,xs)),o=ruta(t,[[c,500,1100,1.08,-.05],[f,580,1080,1.2,.05]]),lx=L+lerp(120,760,u),ly=lerp(930,720,u);
 cam(L,o[0],o[1],o[2],540,1000,()=>{interior(L,{p0:'#22303a',p1:'#3d5560',tex:'concreto',ta:.16,yp:1560});meson(L,1500,{tex:'metal',col:'#8e98a4',ta:.5});
  X.fillStyle='#3a424c';X.beginPath();X.ellipse(L+540,1500,380,60,0,0,7);X.fill();X.fillStyle='#55606a';X.beginPath();X.ellipse(L+540,1484,360,52,0,0,7);X.fill();
  X.save();X.translate(L+540,1210);X.scale(1,.9);X.beginPath();X.ellipse(0,0,330,330,0,0,7);X.clip();terreno(700,700,false,8);colina(0,0,.86,{cara:1-u,det:.5*u,sx:-60*u});X.restore();X.strokeStyle='#2a2f38';X.lineWidth=12;X.beginPath();X.ellipse(L+540,1210,330,297,0,0,7);X.stroke();
  haz(lx,ly,L+540,1210,30,330,'255,236,190',.22);X.strokeStyle='#2a2f38';X.lineWidth=16;X.lineCap='round';X.beginPath();X.moveTo(lx,ly);X.lineTo(lx+300,ly+30);X.stroke();X.fillStyle='#e9c46a';X.beginPath();X.arc(lx,ly,44,0,7);X.fill();luz(lx,ly,150,'255,236,190',.6);
  mano(lx+300,ly+34,-.1,1.2,-1,{curl:[.6,.64,.68,.7],pulgar:.3})},o[3]);
 arriba(L,.6)}

// ---------- 08 · pero al publicar la foto, la propia nota de la NASA decía que la colina parecía una cabeza humana ----------
function p08(L,t){const c=T.c08,xr=T.x_released,xn=T.x_note,xh=T.x_head,f=T.c09,en=eio(seg(t,xr-.4,xr+.3)),tx=eio(seg(t,xh-.9,xh-.4));
 plano(L,t,[[c,460,1100,1.06],[xn,620,1110,1.2],[xh,700,1130,1.5],[f,710,1135,1.56]],cm=>{escritorio(L,{v:9,tinte:'rgba(30,14,6,.3)'});luz(L+700,1000,700,'255,236,200',.18);
  foto(L+lerp(-300,300,en),1090,520,-.07,{});nota(L+760,1120,500,.04,{texto:tx,marca:0});X.fillStyle='#8e98a4';rr(L+610,820,26,74,10);X.fill()});
 arriba(L,.6)}

// ---------- 09 · con eso bastó: la cara de Marte se hizo famosa ----------
function icono(x,y,s,a){X.save();X.translate(x,y);X.scale(s,s);X.globalAlpha=a===undefined?1:a;X.fillStyle='#c98a5a';X.beginPath();X.ellipse(0,0,60,72,0,0,7);X.fill();X.fillStyle='#4a2414';X.beginPath();X.ellipse(-22,-18,14,9,0,0,7);X.fill();X.beginPath();X.ellipse(22,-18,14,9,0,0,7);X.fill();X.beginPath();X.ellipse(0,34,26,7,0,0,7);X.fill();X.fillRect(-4,-8,8,26);X.restore()}
function p09(L,t){const c=T.c09,xf=T.x_famous,f=T.c10,br=eio(seg(t,xf-.3,xf+.2));
 plano(L,t,[[c,540,1090,1.9],[xf,540,1100,1.02],[f,540,1100,.96]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#241a2c'],[1,'#3a2a3a']]);X.fillRect(L-1400,-900,3900,3800);tex('tela',L-500,200,2100,1900,{a:.14,v:3});
  X.fillStyle='#c0392b';rr(L+380,870,320,430,10);X.fill();X.fillStyle='#fff';X.fillRect(L+400,890,280,40);icono(L+540,1110,1.5);
  [[150,760,'#2a6f97',.9,-.08],[930,740,'#e9c46a',.9,.07],[130,1320,'#f4f1ea',.95,.06],[950,1300,'#2a9d8f',.9,-.06],[540,690,'#efe6d0',.72,.02],[540,1600,'#8e5aa8',.85,-.03],[150,1760,'#e76f51',.7,.1],[940,1780,'#f4f1ea',.7,-.1]].forEach(([x,y,col,s,r],i)=>{const a=eio(seg(t,c+.5+i*.14,c+.9+i*.14));if(a<=0)return;X.save();X.translate(L+x,y);X.rotate(r);X.scale(s*back(a),s*back(a));X.fillStyle='rgba(0,0,0,.3)';rr(-112,-140,240,300,12);X.fill();X.fillStyle=col;rr(-120,-150,240,300,12);X.fill();icono(0,-10,1.15);X.fillStyle='rgba(0,0,0,.25)';rr(-90,106,180,14,7);X.fill();X.restore()});
  if(br>0)luz(L+540,1110,420,'255,214,140',.3*br)});
 arriba(L,.62)}

// ---------- 10 · 1998: diez veces más nítida. 2001: más nítida todavía (cortes por coincidencia) ----------
function p10(L,t){const c=T.c10,x98=T.x_1998,xs=T.x_sharper,x01=T.x_2001,xt=T.x_still,f=T.c11,k1=x98+.55,k2=x01+.55,e=t<k1?0:t<k2?1:2,k=[c,k1,k2][e],z=1.02+.06*seg(t,k,k+2.6)+.05*(1-eio(seg(t,k,k+.25)));
 cam(L,540,1090,z,540,1000,()=>{X.save();X.translate(L+540,1090);terreno(2600,3000,true,1);colina(0,0,1.25,{gris:1,cara:[1,.4,0][e],det:[0,.6,1][e]});mosaico(1400,1600,[38,15,0][e]||10,[.5,.3,0][e],5);X.restore();
  if(e===2)haz(L-100,300,L+540,1090,60,800,'255,255,255',.1)});
 placa(L+250,560,1,['1976','1998','2001'][e],eio(seg(t,k+.05,k+.3)),{ts:60});arriba(L,.6)}

// ---------- 11 · la cara ya no estaba: era una colina rocosa, como muchas otras alrededor ----------
function cerro(x,yb,w,h,sem,o){o=o||{};X.fillStyle=gl(x-w/2,yb-h,x+w/2,yb,[[0,'#d79a6a'],[1,'#8a4f30']]);X.beginPath();X.moveTo(x-w/2,yb);X.quadraticCurveTo(x-w*.36,yb-h*.9,x-w*.14,yb-h);X.lineTo(x+w*.18,yb-h*.96);X.quadraticCurveTo(x+w*.4,yb-h*.8,x+w/2,yb);X.closePath();X.fill();
 X.fillStyle='rgba(60,24,12,.28)';X.beginPath();X.moveTo(x+w*.02,yb-h*.98);X.lineTo(x+w*.18,yb-h*.96);X.quadraticCurveTo(x+w*.4,yb-h*.8,x+w/2,yb);X.lineTo(x+w*.1,yb);X.closePath();X.fill();
 X.strokeStyle='rgba(60,24,12,.35)';X.lineWidth=4;X.lineCap='round';for(let i=0;i<7;i++){const xx=x-w*.34+rnd(i+sem)*w*.6,y0=yb-h*(.3+rnd(i+sem+9)*.6);X.beginPath();X.moveTo(xx,y0);X.lineTo(xx+(rnd(i+sem+3)-.5)*40,y0+h*.2);X.stroke()}
 for(let i=0;i<6;i++){X.fillStyle='#7a3f28';X.beginPath();X.ellipse(x-w*.5+rnd(i+sem+20)*w,yb+6,14+rnd(i+sem)*20,8+rnd(i)*8,0,0,7);X.fill()}}
function p11(L,t){const c=T.c11,xg=T.x_gone,xo=T.x_others,f=T.c12;
 plano(L,t,[[c,440,1150,1.2],[xo-.4,520,1150,1.16],[f,1500,1130,1.02]],cm=>{X.fillStyle=gl(0,-300,0,1380,[[0,'#d9a070'],[1,'#f0c8a0']]);X.fillRect(L-1400,-1400,5600,2800);const px=par(cm,.7);
  X.fillStyle='#c98a62';for(let i=0;i<9;i++){X.beginPath();X.ellipse(L-600+i*520+px,1380,360,80+rnd(i+2)*90,0,Math.PI,0);X.fill()}
  X.fillStyle=gl(0,1380,0,1920,[[0,'#b86a40'],[1,'#7a3a22']]);X.fillRect(L-1400,1380,5600,1400);tex('arena',L-1400,1380,5600,700,{a:.25,s:1.6});
  cerro(L+1180+px*.4,1400,420,190,5);cerro(L+2250+px*.4,1410,380,170,9);cerro(L+460,1560,820,430,1);cerro(L+1560,1600,620,300,12);cerro(L+2150,1640,700,360,17);cerro(L+2760,1580,560,330,23)});
 arriba(L,.62)}

// ---------- 12 · nadie construyó una cara: fue tu cerebro, hecho para encontrar caras hasta en rocas y sombras ----------
function p12(L,t){const c=T.c12,xb=T.x_brain,xw=T.x_wired,xr=T.x_rocks,f=T.c13,ca=eio(seg(t,xw-.3,xw+.3))*(1-eio(seg(t,xr-.2,xr+.6))),fo=eio(seg(t,xw-.6,xw)),br=eio(seg(t,xb-.2,xb+.3))*(1-eio(seg(t,xw-.4,xw)));
 const kf=[[c,500,1150,1.06],[xw,600,1080,1.22],[f,620,1070,1.28]];
 plano(L,t,kf,cm=>{X.fillStyle=gl(0,-300,0,1920,[[0,'#3a2a2e'],[1,'#6a4636']]);X.fillRect(L-1400,-1400,3900,4800);
  X.fillStyle=gl(L+200,500,L+1100,1700,[[0,'#b98a66'],[1,'#6a4630']]);X.beginPath();X.moveTo(L+250,1750);X.quadraticCurveTo(L+180,900,L+520,620);X.quadraticCurveTo(L+900,480,L+1120,860);X.quadraticCurveTo(L+1260,1300,L+1100,1750);X.closePath();X.fill();tex('piedra',L+200,500,1000,1260,{a:.22,v:2});
  [[560,960,60,40],[840,940,58,38],[700,1250,120,24],[690,1090,22,60],[420,1300,30,20],[980,1300,26,18],[520,740,24,16]].forEach((p,i)=>{X.fillStyle=`rgba(50,26,14,${i<4?.5+.3*ca:.45})`;X.beginPath();X.ellipse(L+p[0],p[1],p[2],p[3],i===3?.1:0,0,7);X.fill()});
  if(ca>0){X.strokeStyle=`rgba(255,255,255,${.85*ca})`;X.lineWidth=6;[[560,960,76,54],[840,940,74,52]].forEach(p=>{X.beginPath();X.ellipse(L+p[0],p[1],p[2],p[3],0,0,7);X.stroke()});X.beginPath();X.moveTo(L+570,1240);X.quadraticCurveTo(L+700,1310,L+830,1240);X.stroke()}});
 desenfoca(5*(1-fo));
 plano(L,t,kf,cm=>{borroso(6*fo,()=>{silueta(L+250,2150,2.6,'#120c10',{})});if(br>0){luz(L+250,1370,150,'255,150,190',.6*br);X.strokeStyle=`rgba(255,170,200,${br})`;X.lineWidth=6;X.lineCap='round';[[210,1340,250,1310,290,1350],[220,1390,260,1370,300,1400]].forEach(p=>{X.beginPath();X.moveTo(L+p[0],p[1]);X.quadraticCurveTo(L+p[2],p[3],L+p[4],p[5]);X.stroke()})}});
 arriba(L,.6)}

// ---------- 13 · CTA: una roca ambigua; un pequeño movimiento cambia lo que parece ----------
function p13(L,t){const c=T.c13,ca=.5+.5*Math.sin((t-c)*1.5);
 plano(L,t,[[c,460+40*Math.sin((t-c)*1.5),1190,1.16],[c+2.4,535+14*Math.sin((t-c)*1.5),1010,1.02],[T.fin,540,1000,1]],cm=>{X.fillStyle=gl(0,-300,0,1500,[[0,'#3a2228'],[1,'#c8805a']]);X.fillRect(L-1400,-1400,3900,2980);   // el cielo baja 80 px bajo el horizonte: sin costura al escalar la cámara
  X.fillStyle='#a8623e';for(let i=0;i<8;i++){X.beginPath();X.ellipse(L-300+i*330+par(cm,.7),1500,240,60+rnd(i+2)*80,0,Math.PI,0);X.fill()}X.fillStyle=gl(0,1500,0,1920,[[0,'#b86a40'],[1,'#7a3a22']]);X.fillRect(L-1400,1500,3900,900);
  X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.ellipse(L+420,1500,220,26,0,0,7);X.fill();X.fillStyle=gl(L+220,1200,L+620,1500,[[0,'#d79a6a'],[1,'#8a4f30']]);X.beginPath();X.moveTo(L+230,1500);X.quadraticCurveTo(L+210,1260,L+400,1210);X.quadraticCurveTo(L+600,1230,L+620,1500);X.closePath();X.fill();
  [[350,1340,26,16],[480,1336,26,16],[416,1430,50,10]].forEach((p,i)=>{X.fillStyle=`rgba(60,24,12,${.25+.5*ca})`;X.beginPath();X.ellipse(L+p[0]+(1-ca)*(i-1)*14,p[1]+(1-ca)*(i===2?-18:6),p[2],p[3],(1-ca)*(i-1)*.5,0,7);X.fill()})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_srabbit22_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SRABBIT22 · FIN =====
</script>
