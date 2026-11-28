<script>
// ===== DC · SCOFFEE21 · INICIO ===== (Coffee 21h · Your Coffee Is LYING to Your Brain · lote del 28-nov · una escena por línea del guion)
// Azul = adenosina (la señal de cansancio). Ámbar = cafeína. Formas abstractas, no la estructura química. Sin cifras: el guion no las da.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {taza,vapor,persona,MANO,CREMA,C_OK}=window.DC_CAFE;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,interior,meson,relojPared,tarj,desenfoca,borroso}=window.B28;
const AZ='90,169,255',AM='255,180,74';
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({},MANO,o))};

// ---------- formas abstractas: 'a' adenosina (azul, con una punta de más) · 'c' cafeína (ámbar): casi el mismo contorno ----------
function mol(x,y,s,rot,tipo,a){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);if(a!==undefined)X.globalAlpha=a;const az=tipo==='a',c=az?'#5aa9ff':'#ffb44a',c2=az?'#2f6fd0':'#d9801a';
 X.fillStyle=c2;X.beginPath();X.arc(-14,3,28,0,7);X.fill();X.beginPath();X.arc(20,3,22,0,7);X.fill();X.fillStyle=c;X.beginPath();X.arc(-14,-2,26,0,7);X.fill();X.beginPath();X.arc(20,-2,20,0,7);X.fill();
 if(az){X.beginPath();X.arc(45,-13,10,0,7);X.fill()}X.fillStyle='rgba(255,255,255,.42)';X.beginPath();X.arc(-22,-12,8,0,7);X.fill();X.restore()}
// encaje (receptor) sobre la superficie de la neurona: abre hacia arriba
function encaje(x,y,s,col){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle=col||'#6a4a9a';X.beginPath();X.moveTo(-74,10);X.lineTo(-74,-56);X.quadraticCurveTo(-74,-74,-56,-74);X.lineTo(-46,-74);X.quadraticCurveTo(-42,-18,0,-18);X.quadraticCurveTo(42,-18,46,-74);X.lineTo(56,-74);X.quadraticCurveTo(74,-74,74,-56);X.lineTo(74,10);X.closePath();X.fill();X.fillStyle='rgba(255,255,255,.12)';rr(-70,-70,16,60,8);X.fill();X.restore()}
function superficie(L,y,x0,x1,col){X.fillStyle=gl(0,y,0,y+700,[[0,col||'#4a3376'],[1,'#22183c']]);X.fillRect(L+x0,y,x1-x0,1400);X.fillStyle='rgba(255,255,255,.08)';X.fillRect(L+x0,y,x1-x0,8);for(let i=0;i<24;i++){X.fillStyle='rgba(255,255,255,.035)';X.beginPath();X.arc(L+x0+rnd(i+3)*(x1-x0),y+60+rnd(i+31)*500,20+rnd(i+7)*50,0,7);X.fill()}}
function cerebro(x,y,s,o){o=o||{};X.save();X.translate(x,y);X.scale(s,s);X.lineCap='round';X.lineJoin='round';const c=o.c||'#c98ab8',d=o.d||'#8a4f84';
 X.fillStyle=d;rr(40,90,70,160,30);X.fill();X.beginPath();X.ellipse(176,128,84,56,0,0,7);X.fill();
 X.fillStyle=c;[[-150,-10,120],[-40,-70,150],[90,-40,140],[160,30,100],[-60,50,130],[70,70,110]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],p[2],0,7);X.fill()});
 {const g=X.createRadialGradient(-70,-120,30,0,0,300);g.addColorStop(0,'rgba(255,255,255,.16)');g.addColorStop(1,'rgba(0,0,0,.14)');X.fillStyle=g;[[-150,-10,120],[-40,-70,150],[90,-40,140],[160,30,100],[-60,50,130],[70,70,110]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],p[2],0,7);X.fill()})}
 X.strokeStyle='rgba(120,50,110,.5)';X.lineWidth=9;[[-210,0,-150,-70,-90,-10],[-60,-160,-10,-100,-70,-40],[40,-150,100,-110,60,-50],[150,-60,200,-10,150,40],[-150,90,-90,60,-40,120],[10,20,60,60,20,120]].forEach(p=>{X.beginPath();X.moveTo(p[0],p[1]);X.quadraticCurveTo(p[2],p[3],p[4],p[5]);X.stroke()});X.restore()}
// n partículas azules dentro del cerebro (centro x,y; escala s). caen: 0..1 cuánto se van al fondo
function nube(x,y,s,n,t,caen){for(let i=0;i<n;i++){const a=rnd(i+2)*6.28,r=Math.sqrt(rnd(i+19)),px=Math.cos(a)*r*210,py=lerp(Math.sin(a)*r*140-20,60+rnd(i+41)*110,caen||0);mol(x+(px+Math.sin(t*1.3+i)*8)*s,y+(py+Math.cos(t*1.1+i*2)*6)*s,.36*s,rnd(i+7)*6+t*.3,'a')}}
function etiqueta(x,y,texto,a,col){if(a<=0)return;X.save();X.globalAlpha=a;const w=texto.length*31+60;tarj(x,y,w,84,18,col||'#101a2c',{sa:.25,borde:'rgba(255,255,255,.25)',lw:3});txt(texto,x,y+4,48,'#fff',{w:800});X.restore()}
function sombraCansada(x,y,s,a){if(a<=0)return;X.save();X.translate(x,y);X.scale(s,s);X.rotate(.1);X.fillStyle=`rgba(4,8,18,${.55*a})`;X.beginPath();X.ellipse(50,-330,205,255,.28,0,7);X.fill();X.beginPath();X.moveTo(-540,1300);X.lineTo(-480,190);X.quadraticCurveTo(-400,20,-200,0);X.lineTo(260,34);X.quadraticCurveTo(450,80,510,250);X.lineTo(580,1300);X.closePath();X.fill();X.restore()}
function cuarto(L,cm,t,o){o=o||{};interior(L,{p0:o.p0||'#1a323c',p1:o.p1||'#2c5263',tex:'baldosa',ta:.12,yp:2300});const px=par(cm,.4);if(o.ventana!==false){ventanaV(L+30+px,620,260,420,o.hora||'tarde',t,{});haz(L+160+px,820,L+700+px,1500,160,520,'255,200,130',.16*(o.luz===undefined?1:o.luz))}}

// ---------- 01 · gancho: toma café al amanecer; todo se ilumina, pero la sombra del cansancio sigue ahí ----------
function p01(L,t){const xe=T.x_energy,xi=T.x_isnt,xc=T.x_careful,xh=T.x_hours,f=T.c02,baja=eio(seg(t,xe-.5,xe+.2)),som=eio(seg(t,xi-.2,xi+.6)),cre=eio(seg(t,xh-.3,f)),par2=eio(seg(t,xc-.2,xc+.4)),ty=lerp(1050,1420,baja);
 plano(L,t,[[0,610,1010,1.5],[xe-.5,600,1010,1.44],[xi,560,1000,1.06],[f,620,960,1.14]],cm=>{cuarto(L,cm,t,{luz:.5+.5*baja});luz(L+300,800,900,AM,.1+.16*baja);
  sombraCansada(L+800,1010,1.12+.1*cre,som);
  persona(L,t,{dx:0,ty,trot:-.36*(1-baja),cafe:C_OK,boca:{s:baja*(1-som)}});vapor(L+570,ty-250,t,.5*(1-par2),1.2);
  if(par2>0)for(let i=0;i<7;i++){const u=((t-xc)*.35+i/7)%1;mol(L+570+Math.sin(u*5+i*2)*60,ty-260-u*520,.5+.3*u,t+i,'a',par2*(1-u))}});
 tinte(L,'255,170,90',.07*baja*(1-som));arriba(L,.5)}

// ---------- 02 · desde que despiertas, el cerebro acumula adenosina ----------
function p02(L,t){const c=T.c02,xa=T.x_adenosine,f=T.c03,n=Math.floor(lerp(2,26,seg(t,c+.3,f))),o=ruta(t,[[c,500,1060,1.1,-.04],[f,590,1040,1.2,.04]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{X.fillStyle=gl(0,0,0,1920,[[0,'#101a3a'],[.7,'#2a2a5a'],[1,'#7a4a5a']]);X.fillRect(L-900,-900,2900,3800);
  const sy=lerp(1900,1560,eio(seg(t,c,f)));luz(L+200,sy,620,'255,190,110',.5);X.fillStyle='#ffd9a0';X.beginPath();X.arc(L+200,sy,90,0,7);X.fill();X.fillStyle='#1a1f3a';X.fillRect(L-900,1640,2900,900);
  luz(L+540,1000,640,'200,150,255',.18);cerebro(L+540,1020,1.5,{});nube(L+540,1010,1.5,n,t,0);
  const q=eio(seg(t,xa-.1,xa+.25));if(q>0){X.strokeStyle=`rgba(255,255,255,${.7*q})`;X.lineWidth=4;X.beginPath();X.moveTo(L+620,700);X.lineTo(L+600,860);X.stroke()}etiqueta(L+640,650,'ADENOSINE',q)},o[3]);
 arriba(L,.56)}

// ---------- 03 · mientras más se acumula, más sueño: baja de los hombros y bostezo ----------
function p03(L,t){const c=T.c03,xs=T.x_sleepier,xg=T.x_signal,f=T.c04,bj=eio(seg(t,xs-.4,xs+.6)),bo=golpe(t,xs+.1,2.2);
 plano(L,t,[[c,540,-330,1.2],[xs-.5,540,-300,1.2],[xs+.5,540,880,1.02],[f,540,960,1.08]],cm=>{
  X.fillStyle=gl(0,-900,0,1920,[[0,'#0c1430'],[1,'#22365a']]);X.fillRect(L-900,-1900,2900,5800);tex('tela',L-400,300,1900,1700,{a:.1,v:2});
  if(cm[1]<560){luz(L+540,-330,620,AZ,.2);cerebro(L+540,-320,1.4,{c:'#a98ac0',d:'#6f4f8a'});nube(L+540,-330,1.4,40,t,eio(seg(t,c,xs)))}
  X.save();X.translate(0,60*bj);persona(L,t,{dx:0,boca:{s:-.2*bj}});if(bo>0){X.fillStyle='#5a2a22';X.beginPath();X.ellipse(L+540,744,44,16+50*bo,0,0,7);X.fill()}X.restore()});
 tinte(L,'40,90,190',.1);arriba(L,.56)}

// ---------- 04 · la cafeína tiene casi la misma forma ----------
function p04(L,t){const c=T.c04,xm=T.x_same,f=T.c05,j=eio(seg(t,xm-.3,xm+.5)),o=ruta(t,[[c,520,1080,1.06,-.05],[f,560,1060,1.18,.05]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{X.fillStyle=gl(0,0,0,1920,[[0,'#10122c'],[1,'#2a2452']]);X.fillRect(L-900,-900,2900,3800);for(let i=0;i<8;i++)luz(L+rnd(i+4)*1080,500+rnd(i+13)*1000,70+rnd(i+22)*90,i%2?AZ:AM,.08);
  const xa=lerp(300,470,j),xc=lerp(790,610,j),r=Math.sin(t*.8)*.12;luz(L+xa,1080,300,AZ,.3);luz(L+xc,1080,300,AM,.3);
  mol(L+xa,1080,5,r,'a');X.save();X.globalAlpha=1-.35*j;mol(L+xc,1080,5,r,'c');X.restore();
  if(j>.5){X.save();X.translate(L+540,1080);X.rotate(r);X.strokeStyle=`rgba(255,255,255,${(j-.5)*1.6})`;X.lineWidth=6;X.setLineDash([16,14]);X.beginPath();X.arc(-70,-10,140,2.0,4.9);X.arc(100,-10,112,-1.75,1.75);X.arc(-70,-10,140,1.2,2.0);X.stroke();X.setLineDash([]);X.restore()}
  etiqueta(L+xa-20,760,'ADENOSINE',1-j);etiqueta(L+xc+20,1400,'CAFFEINE',eio(seg(t,c+.05,c+.4)),'#3a2408')},o[3]);
 arriba(L,.58)}

// ---------- 05 · se mete en los mismos lugares del cerebro y los bloquea ----------
const ENC=[220,600,980,1360,1740];
function fila(L,t,k,o){o=o||{};superficie(L,1300,-700,3200,o.sup);ENC.forEach((x,i)=>{encaje(L+x,1300,1.5);const u=o.sinCafe?0:eio(seg(t,k+i*(o.cada===undefined?.28:o.cada),k+.45+i*(o.cada===undefined?.28:o.cada)));
  if(u>0){const sal=o.sale?eio(seg(t,o.sale+i*.07,o.sale+.6+i*.07)):0;mol(L+x+sal*120*(i%2?1:-1),lerp(700,1300-66,u)-sal*700,1.45,(1-u)*2+sal*2,'c',1-sal)}})}
function p05(L,t){const c=T.c05,xs=T.x_slips,xb=T.x_blocks,f=T.c06,k=xs-.45;
 plano(L,t,[[c,380,1090,1.3],[f,1480,1090,1.3]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#10122c'],[1,'#2a2452']]);X.fillRect(L-1400,-900,5200,3800);luz(L+cm[0],900,800,AM,.12);
  fila(L,t,k,{});
  ENC.forEach((x,i)=>{const u=((t-c)*.5+i*.31)%1,reb=t>k+.45+i*.28,yy=reb?lerp(760,1100,Math.abs(Math.sin(u*Math.PI))):lerp(700,1000,u);mol(L+x-60+Math.sin(u*6+i)*50,yy,1.1,t*1.5+i,'a')})});
 arriba(L,.58)}

// ---------- 06 · la señal no pasa y te sientes despierto: corte que sube del cerebro a la persona ----------
function p06(L,t){const c=T.c06,xa=T.x_awake,f=T.c07,k=xa-1.0,per=t>k;
 if(!per)plano(L,t,[[c,640,1090,1.34],[k,760,1070,1.42]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#10122c'],[1,'#2a2452']]);X.fillRect(L-1400,-900,5200,3800);luz(L+cm[0],900,800,AM,.14);fila(L,t,c-9,{});
   ENC.forEach((x,i)=>{const u=((t-c)*.6+i*.31)%1;mol(L+x-50+Math.sin(u*6+i)*40,lerp(820,1130,Math.abs(Math.sin(u*Math.PI))),1.1,t*1.5+i,'a')});
   ENC.forEach((x,i)=>{const g=Math.abs(Math.sin(((t-c)*.6+i*.31)%1*Math.PI));if(g>.93){X.strokeStyle='rgba(255,255,255,.7)';X.lineWidth=5;X.lineCap='round';[-.7,0,.7].forEach(a=>{X.beginPath();X.moveTo(L+x-50+Math.sin(a)*46,1150-Math.cos(a)*10);X.lineTo(L+x-50+Math.sin(a)*74,1136-Math.cos(a)*34);X.stroke()})}})});
 else{plano(L,t,[[k,560,1330,1.2],[k+.6,560,1020,1.06],[f,585,995,1.1]],cm=>{cuarto(L,cm,t,{p0:'#3a2e22',p1:'#6a5236',hora:'dia'});luz(L+300,800,900,AM,.28);persona(L,t,{dx:0,ty:1500,cafe:C_OK,boca:{s:eio(seg(t,k+.3,k+.8))}});vapor(L+570,1250,t,.4,1.2);
   X.fillStyle='#2a2f38';X.beginPath();X.moveTo(L+110,1920);X.lineTo(L+180,1640);X.lineTo(L+470,1640);X.lineTo(L+540,1920);X.closePath();X.fill();luz(L+330,1600,300,'200,230,255',.2)});tinte(L,'255,170,80',.06)}
 arriba(L,.56)}

// ---------- 07 · G2: horas después. Taza vacía frente al reloj; la sombra avanza y el ámbar se vuelve azul ----------
function p07(L,t){const c=T.c07,xh=T.x_hours7,xk=T.x_crash,f=T.c08,av=eio(seg(t,c+.5,xh+.6)),fr=eio(seg(t,xh-.4,xk)),g=golpe(t,xk,.6),o=ruta(t,[[c,490,1100,1.08,-.045],[f,590,1080,1.2,.045]]);
 cam(L,o[0],o[1],o[2],540,1000,()=>{interior(L,{p0:'#3a2e22',p1:'#6a5236',tex:'tela',ta:.2,yp:1420});meson(L,1380,{tex:'madera',col:'#6a4a2e',ta:.92});
  luz(L+lerp(200,900,av),700,900,AM,.3*(1-fr));luz(L+820,760,900,AZ,.22*fr+.15*g);
  relojPared(L+540,900,250,8+av*6.5,(av*6.5*60)%60,{aro:'#22262b'});
  X.fillStyle='rgba(0,0,0,.3)';X.beginPath();X.moveTo(L+470,1640);X.lineTo(L+610,1640);const sx=lerp(-460,520,av);X.lineTo(L+610+sx+130,1900);X.lineTo(L+470+sx-130,1900);X.closePath();X.fill();
  taza(L+540,1650,1.7,{cafe:'#e9dfc8',asa:-1})},o[3]);
 tinte(L,'40,80,180',.12*fr);arriba(L,.58)}

// ---------- 08 · no quitó el cansancio, solo lo tapó: una capa de cafeína sobre la señal ----------
function ola(L,y,t,amp,a){X.beginPath();X.moveTo(L-400,y);for(let x=-400;x<=1500;x+=16)X.lineTo(L+x,y+Math.sin(x*.012+t*2.2)*amp+Math.sin(x*.027-t*1.6)*amp*.4);X.lineTo(L+1500,y+500);X.lineTo(L-400,y+500);X.closePath();X.fillStyle=gl(0,y-amp,0,y+500,[[0,`rgba(${AZ},${.95*a})`],[1,`rgba(30,70,160,${.9*a})`]]);X.fill()}
function p08(L,t){const c=T.c08,xr=T.x_remove,xv=T.x_covered,f=T.c09,cu=eio(seg(t,xr-.6,xv));
 plano(L,t,[[c,420,1150,1.14],[xv,600,1130,1.2],[f,660,1120,1.26]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#0e1a34'],[1,'#1c2c50']]);X.fillRect(L-900,-900,2900,3800);for(let i=0;i<7;i++)luz(L+rnd(i+4)*1080,520+rnd(i+13)*400,60+rnd(i+22)*70,AZ,.08);
  ola(L,1230,t,44,1);for(let i=0;i<9;i++){const x=-200+((t*150+i*190)%1700),y=1230+Math.sin(x*.012+t*2.2)*44+Math.sin(x*.027-t*1.6)*18;X.fillStyle='rgba(235,246,255,.9)';X.beginPath();X.arc(L+x,y-4,9,0,7);X.fill();luz(L+x,y-4,46,AZ,.5)}
  const w=lerp(0,1560,cu);X.save();X.beginPath();X.rect(L-300,860,w,700);X.clip();X.fillStyle=`rgba(${AM},.26)`;rr(L-300,1010,1760,330,70);X.fill();X.strokeStyle=`rgba(${AM},.95)`;X.lineWidth=7;rr(L-300,1010,1760,330,70);X.stroke();
  X.fillStyle='rgba(255,240,205,.5)';rr(L-270,1026,1700,20,10);X.fill();X.fillStyle='rgba(255,236,190,.12)';for(let i=0;i<8;i++){X.beginPath();X.moveTo(L-200+i*230,1340);X.lineTo(L-120+i*230,1340);X.lineTo(L+20+i*230,1010);X.lineTo(L-60+i*230,1010);X.closePath();X.fill()}X.restore();
  if(cu>0&&cu<1)luz(L-300+w,1175,170,'255,236,190',.55)});
 arriba(L,.58)}

// ---------- 09 · mientras la cafeína está ahí, el cerebro sigue fabricando adenosina, que no tiene adónde ir ----------
function espera(L,t,c,n,cae){for(let i=0;i<n;i++){const x=L-60+rnd(i+3)*1200,y0=560+rnd(i+17)*480+Math.sin(t*2+i)*14,dst=ENC[i%5],u=cae?eio(seg(t,cae+rnd(i+9)*.35,cae+.5+rnd(i+9)*.35)):0;mol(lerp(x+Math.sin(t*1.4+i*2)*18,L+dst+(rnd(i+5)-.5)*90,u),lerp(y0,1250+rnd(i+23)*260,u),.8,t+i,'a',1-.5*u*(i%5?1:0))}}
function p09(L,t){const c=T.c09,xk=T.x_keeps,xn=T.x_nowhere,f=T.c10,n=Math.floor(lerp(4,34,seg(t,c+.2,xn)));
 plano(L,t,[[c,560,1330,1.2],[xk,560,1200,1.1],[f,560,960,1.04]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#081028'],[1,'#141c44']]);X.fillRect(L-1400,-900,5200,3800);luz(L+540,800,800,AZ,.14);
  fila(L,t,c-9,{sup:'#3a2a6a'});espera(L,t,c,n,0)});
 tinte(L,'30,60,170',.08);arriba(L,.58)}

// ---------- 10 · la cafeína se va y todo entra de golpe; corte a la persona agotada ----------
function p10(L,t){const c=T.c10,xw=T.x_wears,xr=T.x_rushes,xo=T.x_once,f=T.c11,per=t>xr+.42,g=golpe(t,xr+.2,.5);
 if(!per){plano(L,t,[[c,560,960,1.04],[xr,560,1100,1.16],[xr+.42,560,1280,1.4]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#081028'],[1,'#141c44']]);X.fillRect(L-1400,-900,5200,3800);luz(L+540,1200,900,AZ,.14+.3*g);
   fila(L,t,c-9,{sup:'#3a2a6a',sale:xw-.2});espera(L,t,c,34,xr-.15)})}
 else{plano(L,t,[[xr+.42,540,900,1.22],[f,540,940,1.12]],cm=>{cuarto(L,cm,t,{p0:'#0e1830',p1:'#1c3050',ventana:false});luz(L+540,700,800,AZ,.18);
   X.save();X.translate(0,90);X.translate(L+540,1000);X.rotate(.05);X.translate(-(L+540),-1000);persona(L,t,{dx:0,boca:{s:-.5,m:.5}});X.restore();
   for(let i=0;i<8;i++){const a=i/8*6.28+t*.6;mol(L+540+Math.cos(a)*330,640+Math.sin(a)*150,.6,t+i,'a',.8)}});tinte(L,'30,70,190',.14)}
 arriba(L,.58)}

// ---------- 11 · si tomas todos los días, el cerebro arma más de esos lugares: la misma taza ya no alcanza ----------
function banda(L,y,n,ocu,t,nu,libres){const w=650,x0=L+300,e=n>5?.5:.96,dy=n>5?23:44;X.fillStyle=gl(0,y,0,y+120,[[0,'#4a3376'],[1,'#2a1e4a']]);rr(x0-30,y,w+60,120,26);X.fill();
 for(let i=0;i<n;i++){const x=x0+w*(i+.5)/n,nuevo=i>=n-nu.n,a=nuevo?nu.a:1;if(a<=0)continue;X.save();X.globalAlpha=a;encaje(x,y,(nuevo?(.6+.4*back(a)):1)*e,nuevo?'#8a6ad0':'#6a4a9a');X.restore();
  if(i<ocu)mol(x,y-dy,e,0,'c');else if(libres>0&&a>=1)mol(x,lerp(y-260,y-dy,libres),e*.95,(1-libres)*3,'a',libres)}}
function p11(L,t){const c=T.c11,xa=T.x_adapts,xm=T.x_more,xe=T.x_enough,f=T.c12,cre=eio(seg(t,xm-.5,xm+.5)),ll=eio(seg(t,xm+.6,xm+1.6)),du=golpe(t,xe-.3,1.2);
 plano(L,t,[[c,540,1000,1.2],[xa-.2,540,1010,1.18],[xm-.3,540,1270,1.04],[f,540,1290,1.08]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#10122c'],[1,'#2a2452']]);X.fillRect(L-900,-900,2900,3800);luz(L+640,1000,640,AM,.12);luz(L+640,1520,640,AZ,.12);
  taza(L+150,1120,.8,{cafe:C_OK,asa:-1});banda(L,1050,4,3,t,{n:0,a:1},eio(seg(t,c+.6,c+1.3)));
  X.strokeStyle='rgba(255,255,255,.2)';X.lineWidth=5;X.setLineDash([10,16]);X.beginPath();X.moveTo(L+80,1290);X.lineTo(L+1000,1290);X.stroke();X.setLineDash([]);
  X.save();X.translate(L+150,1630);X.rotate(Math.sin(t*14)*.05*du);taza(0,0,.8,{cafe:C_OK,asa:-1});X.restore();banda(L,1560,8,3,t,{n:4,a:cre},ll)});
 arriba(L,.58)}

// ---------- 12 · el café no da energía: esconde lo cansado que estás ----------
function p12(L,t){const c=T.c12,xh=T.x_hides,f=T.c13,som=eio(seg(t,xh-.5,xh+.3));
 plano(L,t,[[c,580,1040,1.36],[xh,570,1010,1.14],[f,600,980,1]],cm=>{cuarto(L,cm,t,{p0:'#3a2e22',p1:'#6a5236',hora:'dia'});luz(L+300,800,900,AM,.24);
  sombraCansada(L+830,1010,1.22,som);persona(L,t,{dx:0,ty:1470,cafe:C_OK,boca:{s:.6*(1-som)}});vapor(L+570,1220,t,.5,1.2)});
 arriba(L,.5)}

// ---------- 13 · CTA: varias tazas en el escritorio; la mano se acerca a otra ----------
function p13(L,t){const c=T.c13,m=eio(seg(t,c+.6,c+1.8))*(1-.12*eio(seg(t,c+1.8,c+2.6)));
 plano(L,t,[[c,460,1190,1.16],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{interior(L,{p0:'#1a323c',p1:'#2c5263',tex:'baldosa',ta:.12,yp:1520});meson(L,1480,{tex:'madera',col:'#6a4a2e',ta:.92});luz(L+260,1100,620,AM,.24);
  taza(L+150,1486,.95,{cafe:'#e9dfc8',asa:-1});taza(L+330,1492,1.05,{cafe:'#e9dfc8',asa:-1,rot:.03});taza(L+250,1300,.8,{cafe:'#e9dfc8',asa:1,sinSombra:1});
  taza(L+560,1490,1.1,{cafe:C_OK,asa:-1});vapor(L+560,1280,t,.5,1);mano(L+lerp(1250,700,m),1400,-.12,1.15,-1,{curl:[.3,.34,.38,.4],pulgar:.5})});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_scoffee21_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SCOFFEE21 · FIN =====
</script>
