<script>
// ===== DC · RABBIT18 · INICIO ===== (Rabbit 18h · THE PENTAGON CONFIRMED THIS VIDEO IS REAL · paquete 8 del lote del 27-nov)
// Reglas del paquete: sin alienígenas ni naves; el video es auténtico, la interpretación es otra cosa; el triángulo nace dentro de la óptica, nunca en el cielo.
(function(){
const {LIN,K,cap,trazo,manoLado,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const PAPEL='#efe6d0',TINTA='#2a2019',MANO={manga:'#1f2a44',puno:'#17203a'};
function triLuz(x,y,r,a,rot){if(a<=0||r<=0)return;X.save();X.globalAlpha=Math.min(1,a);X.translate(x,y);X.rotate(rot||0);[[2.2,'rgba(124,252,138,.13)'],[1.55,'rgba(124,252,138,.28)'],[1,'#eaffea']].forEach(q=>{X.fillStyle=q[1];X.beginPath();X.moveTo(0,-r*q[0]);X.lineTo(r*q[0]*.87,r*q[0]*.5);X.lineTo(-r*q[0]*.87,r*q[0]*.5);X.closePath();X.fill()});X.restore()}
function puntoLuz(x,y,r,a,col){if(a<=0)return;X.save();X.globalAlpha=Math.min(1,a);X.fillStyle=col||'rgba(255,246,201,.22)';X.beginPath();X.arc(x,y,r*2.6,0,7);X.fill();X.beginPath();X.arc(x,y,r*1.6,0,7);X.fill();X.fillStyle='#fffbe8';X.beginPath();X.arc(x,y,r,0,7);X.fill();X.restore()}
const TRI=[[-.36,-.2,.105],[.08,-.42,.12],[.4,-.08,.095]];
// imagen de visión nocturna dentro de un círculo. tt = tiempo de la imagen (congelable)
function visor(x,y,R,tt,o){o=o||{};X.save();X.beginPath();X.arc(x,y,R,0,7);X.clip();const g=X.createRadialGradient(x,y,R*.1,x,y,R);g.addColorStop(0,'#1f6b33');g.addColorStop(1,'#061a0c');X.fillStyle=g;X.fillRect(x-R,y-R,2*R,2*R);
 X.fillStyle='rgba(4,20,9,.75)';X.fillRect(x-R,y+R*.42,2*R,R);X.strokeStyle='rgba(124,252,138,.18)';X.lineWidth=R*.008+1;for(let i=0;i<5;i++){X.beginPath();for(let k=-R;k<=R;k+=R*.1)X.lineTo(x+k,y+R*(.5+i*.1)+Math.sin(k*.03+tt*1.5+i)*R*.008);X.stroke()}
 (o.tri||TRI).forEach((q,i)=>triLuz(x+(q[0]+Math.sin(tt*.7+i*2)*.03)*R,y+(q[1]+Math.cos(tt*.6+i)*.025)*R,q[2]*R*(o.esc||1),(o.a===undefined?1:o.a)*(.82+.18*Math.sin(tt*11+i*3)),Math.sin(tt*.5+i)*.08));
 X.fillStyle='rgba(0,0,0,.2)';for(let yy=y-R;yy<y+R;yy+=Math.max(5,R*.014))X.fillRect(x-R,yy,2*R,Math.max(2,R*.005));
 const s=(tt*30|0);X.fillStyle='rgba(190,255,200,.12)';for(let i=0;i<50;i++)X.fillRect(x-R+rnd(i+s)*2*R,y-R+rnd(i*7+s+3)*2*R,R*.006+2,R*.006+2);
 const v=X.createRadialGradient(x,y,R*.55,x,y,R);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(0,0,0,.8)');X.fillStyle=v;X.fillRect(x-R,y-R,2*R,2*R);X.restore();
 X.strokeStyle='#0a0f0c';X.lineWidth=R*.06;X.beginPath();X.arc(x,y,R*1.02,0,7);X.stroke()}
function noche(L,yh,t){const g=X.createLinearGradient(0,-200,0,yh);g.addColorStop(0,'#0c1326');g.addColorStop(1,'#23335a');X.fillStyle=g;X.fillRect(L-1600,-1700,5400,6600);
 X.fillStyle='#fff';for(let i=0;i<40;i++){X.globalAlpha=.25+.3*Math.sin(t*1.5+i);X.beginPath();X.arc(L-300+rnd(i)*1700,rnd(i+50)*(yh-80),2+rnd(i+9)*2.5,0,7);X.fill()}X.globalAlpha=1;
 const m=X.createLinearGradient(0,yh,0,yh+900);m.addColorStop(0,'#132245');m.addColorStop(1,'#080e1e');X.fillStyle=m;X.fillRect(L-1600,yh,5400,3000);X.strokeStyle='rgba(255,255,255,.07)';X.lineWidth=4;for(let i=0;i<8;i++){const y=yh+30+i*i*9+i*34;X.beginPath();for(let x=-400;x<1500;x+=40)X.lineTo(L+x,y+Math.sin(x*.02+t*1.3+i)*4);X.stroke()}}
// cámara con monocular de visión nocturna (de lado, apuntando a la izquierda y arriba)
function equipo(x,y,s,rot,o){o=o||{};X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.lineJoin='round';
 rr(-560,-74,300,148,30);X.fillStyle='#2f3b2a';X.fill();trazo(LIN,3);X.fillStyle='#1b2318';rr(-590,-90,60,180,18);X.fill();trazo(LIN,3);X.fillStyle='#3b4a35';X.fillRect(-500,-74,24,148);X.fillRect(-380,-74,24,148);
 rr(-270,-60,130,120,16);X.fillStyle='#22262b';X.fill();trazo(LIN,3);rr(-150,-110,330,220,28);X.fillStyle='#3a4047';X.fill();trazo(LIN,3);X.fillStyle='#22262b';rr(-60,-140,120,40,12);X.fill();
 if(o.brillo>0){const bx=lerp(-590,-150,o.brillo);X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.ellipse(bx,-50,26,70,.3,0,7);X.fill()}X.restore()}
// ---------- P01a · dentro del visor: tres luces triangulares; en "real" la imagen se congela ----------
function p01a(L,t){const xr=T.x_real,cong=t>=xr-.02,tt=cong?xr-.02:t,f=Math.exp(-Math.max(0,t-xr+.02)*9)*(cong?1:0);
 X.fillStyle='#030705';X.fillRect(L-400,-500,1900,2900);visor(L+540,1020,lerp(640,620,seg(t,0,xr)),tt+6,{});
 if(cong){X.fillStyle=`rgba(234,255,234,${f*.7})`;X.fillRect(L-400,-500,1900,2900);X.strokeStyle='#eaffea';X.lineWidth=9;X.lineCap='square';[[-1,-1],[1,-1],[1,1],[-1,1]].forEach(q=>{const cx=L+540+q[0]*420,cy=1020+q[1]*420;X.beginPath();X.moveTo(cx,cy-q[1]*90);X.lineTo(cx,cy);X.lineTo(cx-q[0]*90,cy);X.stroke()})}}
// ---------- P01b · el aparato visto desde atrás: la cámara en dos manos, con la imagen congelada en su pantalla ----------
// (rehecho el 27-nov a pedido de Tao: el encuadre anterior mostraba la cámara de lado, cortada y saliéndose del cuadro)
function camaraAtras(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.lineJoin='round';
 // el lente, hacia el fondo: se ve por encima del cuerpo
 X.fillStyle='#2f3a26';rr(-124,-340,248,160,28);X.fill();trazo(LIN,4);X.fillStyle='rgba(0,0,0,.22)';[-74,-24,26,76].forEach(v=>X.fillRect(v-6,-334,12,84));X.fillStyle='#3f4d33';rr(-138,-256,276,38,10);X.fill();trazo(LIN,3);
 // visor superior
 X.fillStyle='#22262d';rr(-92,-240,184,74,14);X.fill();trazo(LIN,4);X.fillStyle='#0d1015';rr(-54,-226,108,42,10);X.fill();
 // cuerpo
 X.fillStyle='rgba(0,0,0,.4)';rr(-306,-170,640,420,44);X.fill();rr(-320,-190,640,420,44);X.fillStyle='#3a3f47';X.fill();trazo(LIN,4);
 X.save();rr(-320,-190,640,420,44);X.clip();X.fillStyle='#2c3138';X.fillRect(-320,-190,640,66);X.fillStyle='rgba(255,255,255,.06)';X.fillRect(-320,-124,640,6);X.restore();
 // empuñadura y botones
 X.fillStyle='#2a2e35';rr(200,-108,104,318,30);X.fill();trazo(LIN,3);X.fillStyle='rgba(0,0,0,.25)';for(let i=0;i<7;i++)X.fillRect(214,-40+i*34,76,8);
 X.fillStyle='#1c1f25';X.beginPath();X.arc(252,-150,22,0,7);X.fill();trazo(LIN,3);X.fillStyle='#c0392b';X.beginPath();X.arc(252,-150,10,0,7);X.fill();
 X.fillStyle='#1c1f25';[-250,-196].forEach(v=>{rr(v,-166,40,22,8);X.fill()});
 // marco de la pantalla
 rr(-296,-106,480,326,20);X.fillStyle='#0d1015';X.fill();trazo(LIN,4);X.restore()}
function p01b(L,t){const c=T.c01b,xc=T.x_careful,fin=T.c02,by=Math.sin(t*1.3)*5,S=1.05;
 const cm=ruta(t,[[c,540,1050,1.0],[xc,540,1040,1.1],[fin,540,1020,1.2]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{noche(L,1500,t);X.fillStyle='#0a1020';X.fillRect(L-1600,1600,5400,3000);X.fillStyle='#1c2a4a';X.fillRect(L-1600,1590,5400,22);[0,1,2,3,4,5].forEach(i=>X.fillRect(L-300+i*330,1430,16,170));X.fillRect(L-1600,1424,5400,14);
  const cx=L+540,cy=1070+by,oi=origen(cx-292,cy+86,-1.2,1.25,1,118,44),od=origen(cx+292,cy+86,1.2,1.25,-1,118,44),MI=Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.35}),MD=Object.assign({},MANO,{curl:[.5,.54,.58,.6],pulgar:.35});
  manoLado(oi[0],oi[1],-1.2,1.25,1,Object.assign({},MI,{parte:'atras'}));manoLado(od[0],od[1],1.2,1.25,-1,Object.assign({},MD,{parte:'atras'}));
  camaraAtras(cx,cy,S);
  // la imagen congelada, en la pantalla trasera
  const px=cx-56*S,py=cy+57*S,pw=446*S,ph=292*S;X.save();X.beginPath();X.rect(px-pw/2,py-ph/2,pw,ph);X.clip();X.fillStyle='#061a0c';X.fillRect(px-pw/2,py-ph/2,pw,ph);visor(px,py-10,300*S,T.x_real+6,{});
  const br=seg(t,xc+.35,xc+1.35);if(br>0&&br<1){X.fillStyle='rgba(234,255,234,.14)';X.beginPath();const bx=px-pw+br*pw*2;X.moveTo(bx,py-ph/2);X.lineTo(bx+90,py-ph/2);X.lineTo(bx-40,py+ph/2);X.lineTo(bx-130,py+ph/2);X.closePath();X.fill()}X.restore();
  X.strokeStyle='#eaffea';X.lineWidth=5;X.lineCap='square';[[-1,-1],[1,-1],[1,1],[-1,1]].forEach(q=>{const ex=px+q[0]*(pw/2-26),ey=py+q[1]*(ph/2-24);X.beginPath();X.moveTo(ex,ey-q[1]*34);X.lineTo(ex,ey);X.lineTo(ex-q[0]*34,ey);X.stroke()});
  manoLado(oi[0],oi[1],-1.2,1.25,1,Object.assign({},MI,{parte:'pulgar'}));manoLado(od[0],od[1],1.2,1.25,-1,Object.assign({},MD,{parte:'pulgar'}))})}
// ---------- P02 · la cubierta del buque: siluetas apuntan la cámara a unas luces sobre el mar ----------
function marinero(x,y,s,brazo){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#070b16';X.beginPath();X.arc(0,-250,34,0,7);X.fill();rr(-42,-216,84,150,26);X.fill();X.fillRect(-36,-80,30,80);X.fillRect(6,-80,30,80);X.fillRect(-44,-290,88,14);
 if(brazo){X.strokeStyle='#070b16';X.lineWidth=24;X.lineCap='round';X.beginPath();X.moveTo(-20,-190);X.lineTo(-74,-250);X.lineTo(-104,-300);X.stroke();X.fillRect(-150,-336,70,34)}X.restore()}
function buque(L,y){X.fillStyle='#070b16';X.beginPath();X.moveTo(L-500,y);X.lineTo(L+1500,y);X.lineTo(L+1420,y+190);X.lineTo(L-380,y+190);X.closePath();X.fill();X.fillRect(L+620,y-240,520,240);X.fillRect(L+760,y-420,240,180);X.fillRect(L+860,y-640,20,220);X.fillRect(L+800,y-560,140,10);X.fillRect(L-200,y-36,820,8);for(let i=0;i<10;i++)X.fillRect(L-200+i*90,y-36,8,36);
 X.fillStyle='#f6c66a';[[680,-190],[760,-190],[840,-190],[800,-360],[900,-360]].forEach(q=>X.fillRect(L+q[0],y+q[1],34,22))}
function p02(L,t){const c=T.c02,xs=T.x_sailors,xf=T.x_filmed,fin=T.c03;
 const cm=ruta(t,[[c,600,1000,.9],[fin,440,960,1.12]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{noche(L,1420,t);X.fillStyle='#e9e2c8';X.beginPath();X.arc(L+1010,560,60,0,7);X.fill();X.fillStyle='rgba(233,226,200,.12)';X.beginPath();X.arc(L+1010,560,110,0,7);X.fill();
  [[250,640],[400,560],[500,690]].forEach((q,i)=>puntoLuz(L+q[0]+Math.sin(t*.8+i*2)*26,q[1]+Math.cos(t*.7+i)*18,9,.75+.25*Math.sin(t*9+i*2)));
  buque(L,1330);marinero(L+330,1330,1.15,t>xf-.6);marinero(L+470,1330,1.1,false);
  if(t>xf-.2){X.strokeStyle='rgba(255,246,201,.16)';X.lineWidth=4;X.setLineDash([8,18]);X.beginPath();X.moveTo(L+210,960);X.lineTo(L+330,700);X.stroke();X.setLineDash([])}})}
// ---------- P03 · 2021: el documento confirma quién grabó, no qué eran los objetos ----------
function cuadroVideo(x,y,w,tt){X.fillStyle='#061a0c';X.fillRect(x,y,w,w*.62);X.save();X.beginPath();X.rect(x,y,w,w*.62);X.clip();const g=X.createRadialGradient(x+w/2,y+w*.3,10,x+w/2,y+w*.3,w*.7);g.addColorStop(0,'#1f6b33');g.addColorStop(1,'#061a0c');X.fillStyle=g;X.fillRect(x,y,w,w*.62);
 TRI.forEach((q,i)=>triLuz(x+w/2+q[0]*w*.6,y+w*.34+q[1]*w*.5,q[2]*w*.5,.9+.1*Math.sin(tt*11+i),0));X.fillStyle='rgba(0,0,0,.2)';for(let yy=y;yy<y+w*.62;yy+=7)X.fillRect(x,yy,w,2);X.restore();X.strokeStyle='#0a0f0c';X.lineWidth=5;X.strokeRect(x,y,w,w*.62)}
function lineasGrises(x,y,w,n,alto,sem){X.fillStyle='rgba(42,32,25,.26)';for(let i=0;i<n;i++){rr(x,y+i*alto*1.9,w*(.72+rnd(i+sem)*.28),alto,alto/2);X.fill()}}
function p03(L,t){const c=T.c03,x1=T.x_2021,xc=T.x_conf3,xs=T.x_shot;
 cam(L,540,1000,lerp(1,1.07,seg(t,c,T.c04a)),540,1000,()=>{X.fillStyle='#1a2233';X.fillRect(L-400,-500,1900,2900);X.fillStyle='rgba(255,255,255,.025)';for(let i=0;i<12;i++)X.fillRect(L-400,i*200-100,1900,60);
  X.save();X.translate(L+540,1050);X.rotate(-.03);X.fillStyle='rgba(0,0,0,.3)';rr(-402,-560,830,1160,20);X.fill();X.fillStyle='#b98a4e';rr(-415,-580,830,1160,20);X.fill();trazo(LIN,3);
  const tb=back(seg(t,x1-.2,x1+.15));X.save();X.translate(190,-580);X.scale(1,Math.max(.01,tb));X.fillStyle='#b98a4e';rr(0,-78,220,90,16);X.fill();trazo(LIN,3);txt('2021',110,-34,60,TINTA,{w:200});X.restore();
  X.fillStyle=PAPEL;X.fillRect(-370,-530,740,1070);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-370,-530,740,1070);
  cuadroVideo(-320,-480,640,t);X.fillStyle='#8e98a4';rr(-30,-560,60,110,14);X.fill();trazo(LIN,3);
  lineasGrises(-320,-40,640,3,18,2);
  // fila 1: quién grabó → sello; fila 2: qué eran → queda vacío
  X.fillStyle=TINTA;rr(-320,110,120,84,14);X.fill();X.fillStyle=PAPEL;X.beginPath();X.arc(-260,152,24,0,7);X.fill();X.fillStyle=TINTA;X.beginPath();X.arc(-140,128,22,0,7);X.fill();rr(-168,152,56,60,16);X.fill();lineasGrises(-80,128,190,2,16,5);
  X.strokeStyle=TINTA;X.lineWidth=7;X.lineJoin='round';X.beginPath();X.moveTo(-262,296);X.lineTo(-210,386);X.lineTo(-314,386);X.closePath();X.stroke();lineasGrises(-160,318,180,2,16,8);
  X.setLineDash([14,12]);X.strokeStyle=`rgba(42,32,25,${.5+.4*golpe(t,xs,.8)})`;X.lineWidth=5;rr(90,286,240,116,14);X.stroke();X.setLineDash([]);
  const s=seg(t,xc-.12,xc+.06);if(s>0){X.save();X.translate(210,158);X.rotate(-.1);X.scale(1+(1-s)*1.4,1+(1-s)*1.4);X.globalAlpha=s;X.strokeStyle='#2e8b57';X.lineWidth=8;rr(-150,-52,300,104,14);X.stroke();txt('CONFIRMED',0,2,44,'#2e8b57',{w:280});X.restore()}
  X.restore()})}
// ---------- P04a · en línea: muchos ven otra cosa; esa lectura se aparta ----------
function globo(x,y,s,a){if(s<=0)return;X.save();X.globalAlpha=a;X.translate(x,y);X.scale(s,s);X.fillStyle='#e9e2d2';rr(-70,-56,140,96,28);X.fill();X.beginPath();X.moveTo(-30,36);X.lineTo(-46,70);X.lineTo(-4,38);X.closePath();X.fill();X.strokeStyle='#1f6b33';X.lineWidth=7;X.lineJoin='round';X.beginPath();X.moveTo(-26,-34);X.lineTo(0,10);X.lineTo(-52,10);X.closePath();X.stroke();txt('!!',34,-8,54,'#c0392b',{w:60});X.restore()}
function p04a(L,t){const c=T.c04a,xs=T.x_sure,xa=T.x_alien,fin=T.c04b,va=eio(seg(t,xa+.3,fin));
 X.fillStyle='#141a2b';X.fillRect(L-400,-500,1900,2900);
 [[200,1180],[540,1100],[880,1180]].forEach((q,i)=>{rr(L+q[0]-150,q[1]-120,300,214,18);X.fillStyle='#0a0f0c';X.fill();cuadroVideo(L+q[0]-136,q[1]-108,272,t+i);X.fillStyle='#0a0f0c';X.fillRect(L+q[0]-20,q[1]+94,40,50);rr(L+q[0]-90,q[1]+140,180,16,8);X.fill();
  X.fillStyle='#070b16';X.beginPath();X.arc(L+q[0],q[1]+430,84,0,7);X.fill();X.beginPath();X.ellipse(L+q[0],q[1]+700,190,200,0,0,7);X.fill()});
 for(let i=0;i<16;i++){const k=c+.25+i*.11,q=back(seg(t,k,k+.25));globo(L+90+rnd(i)*900+va*1500,520+rnd(i+20)*420+Math.sin(t*2+i)*8,q*(.8+rnd(i+40)*.6),1-va*.6)}}
// ---------- P04b · 2022: una pantalla genérica muestra el video ----------
function p04b(L,t){const c=T.c04b,x2=T.x_2022,xp=T.x_played;
 cam(L,540,1000,lerp(1,1.06,seg(t,c,T.c05)),540,1000,()=>{X.fillStyle='#101627';X.fillRect(L-400,-500,1900,2900);X.fillStyle='#19223a';X.fillRect(L-400,1500,1900,1500);
  rr(L+130,520,820,560,16);X.fillStyle='#05080d';X.fill();const en=eio(seg(t,xp-.3,xp+.2));if(en>0){X.save();X.globalAlpha=en;cuadroVideo(L+150,540,780,t);X.restore()}X.strokeStyle='#2a3550';X.lineWidth=8;rr(L+130,520,820,560,16);X.stroke();
  // quien presenta, con puntero; atril con el año
  X.fillStyle='#070b16';X.beginPath();X.arc(L+200,1180,52,0,7);X.fill();rr(L+140,1230,120,330,36);X.fill();X.strokeStyle='#070b16';X.lineWidth=20;X.lineCap='round';X.beginPath();X.moveTo(L+230,1290);X.lineTo(L+330,1200+10*Math.sin(t*2));X.stroke();X.strokeStyle='#e9e2d2';X.lineWidth=6;X.beginPath();X.moveTo(L+330,1200+10*Math.sin(t*2));X.lineTo(L+470,1040+16*Math.sin(t*2));X.stroke();
  X.fillStyle='#2a3550';rr(L+60,1400,300,200,12);X.fill();const q=back(seg(t,x2-.15,x2+.15));X.save();X.translate(L+210,1480);X.scale(q,q);X.fillStyle=PAPEL;rr(-96,-44,192,88,10);X.fill();txt('2022',0,2,58,TINTA,{w:180});X.restore();
  for(let i=0;i<7;i++){X.fillStyle='#04070e';X.beginPath();X.arc(L+60+i*160,1750+(i%2)*40,70,0,7);X.fill();X.beginPath();X.ellipse(L+60+i*160,1990+(i%2)*40,150,170,0,0,7);X.fill()}})}
// ---------- P05 · la cámara se aparta del ojo: los triángulos quedan dentro del visor, no en el cielo ----------
const CIELO=[[610,600],[800,500],[930,660]];
function p05(L,t){const c=T.c05,xt=T.x_they,xn=T.x_never,u=eio(seg(t,xt-.1,xt+1.7));
 const vx=lerp(540,330,u),vy=lerp(1020,1290,u),R=lerp(640,170,u);
 noche(L,1560,t);CIELO.forEach((q,i)=>puntoLuz(L+q[0]+Math.sin(t*.8+i*2)*10,q[1]+Math.cos(t*.7+i)*8,13*(1+.5*golpe(t,xn-.1,.9)),u*(.8+.2*Math.sin(t*9+i*2))));
 if(u<1){X.fillStyle=`rgba(3,7,5,${1-u})`;X.fillRect(L-400,-500,1900,2900)}
 // silueta de espaldas con el aparato; el visor es el ocular
 if(u>0){X.save();X.globalAlpha=Math.min(1,u*1.5);X.fillStyle='#04070e';X.beginPath();X.arc(L+250,1640,150,0,7);X.fill();X.beginPath();X.ellipse(L+250,2100,360,330,0,0,7);X.fill();rr(L+140,1150,420,300,40);X.fill();X.save();X.translate(L+480,1180);X.rotate(-.5);rr(0,-70,360,140,30);X.fill();X.restore();X.restore();
  if(u>.6){X.strokeStyle=`rgba(255,246,201,${.2*seg(u,.6,1)})`;X.lineWidth=4;X.setLineDash([8,18]);CIELO.forEach(q=>{X.beginPath();X.moveTo(L+740,1010);X.lineTo(L+q[0],q[1]+30);X.stroke()});X.setLineDash([])}}
 visor(L+vx,vy,R,t+6,{esc:1+.25*golpe(t,xn-.1,.9)})}
// ---------- P06 · macro óptico: un punto de luz entra y, dentro del visor, sale como triángulo ----------
function iris(x,y,R,ap){X.fillStyle='#0d1015';X.beginPath();X.arc(x,y,R*1.12,0,7);X.fill();X.fillStyle='#3a4047';X.beginPath();X.arc(x,y,R,0,7);X.fill();trazo(LIN,3);X.fillStyle='#22262b';X.beginPath();X.arc(x,y,R*.86,0,7);X.fill();
 X.strokeStyle='rgba(255,255,255,.08)';X.lineWidth=3;for(let i=0;i<3;i++){const a=-Math.PI/2+i*2.094;X.beginPath();X.moveTo(x+Math.cos(a)*R*.42,y+Math.sin(a)*R*.42);X.lineTo(x+Math.cos(a+1.3)*R*.86,y+Math.sin(a+1.3)*R*.86);X.stroke()}
 X.fillStyle='#061a0c';X.beginPath();X.moveTo(x,y-R*.42*ap);X.lineTo(x+R*.364*ap,y+R*.21*ap);X.lineTo(x-R*.364*ap,y+R*.21*ap);X.closePath();X.fill();X.strokeStyle='#8e98a4';X.lineWidth=4;X.stroke();X.fillStyle='rgba(255,255,255,.10)';X.beginPath();X.ellipse(x-R*.4,y-R*.5,R*.22,R*.1,-.7,0,7);X.fill()}
function haz(x0,y0,x1,y1,w0,w1,a,tri){if(a<=0)return;const g=X.createLinearGradient(0,y0,0,y1);g.addColorStop(0,`rgba(255,246,201,${.5*a})`);g.addColorStop(1,`rgba(${tri?'124,252,138':'255,246,201'},${.32*a})`);X.fillStyle=g;X.beginPath();X.moveTo(x0-w0,y0);X.lineTo(x0+w0,y0);X.lineTo(x1+w1,y1);X.lineTo(x1-w1,y1);X.closePath();X.fill()}
function p06(L,t){const c=T.c06,xl=T.x_light,xh=T.x_through,xt=T.x_turned,xa=T.x_any,xs=T.x_seen,x8=T.x_tri8,fin=T.c07;
 X.fillStyle='#0b1120';X.fillRect(L-400,-500,1900,2900);X.fillStyle='rgba(255,255,255,.03)';for(let x=-400;x<1500;x+=90)X.fillRect(L+x,-500,2,2900);for(let y=-500;y<2400;y+=90)X.fillRect(L-400,y,1900,2);
 const F=[[540,xl-.05,xh-.1,xt-.1],[320,xa,xs-.25,xs+.35],[760,xa+.5,xs+.2,x8-.35]];
 F.forEach((f,i)=>{const p=back(seg(t,f[1],f[1]+.3)),b=eio(seg(t,f[2],f[2]+.6)),d=eio(seg(t,f[3],f[3]+.45));
  haz(L+f[0],560,L+540+(f[0]-540)*.25,960,10,70,b,false);haz(L+540+(f[0]-540)*.25,1040,L+540+(f[0]-540)*.55,1440,40,56,d,true);
  if(p>0)puntoLuz(L+f[0],540,17*p,.85+.15*Math.sin(t*9+i),i===1?'rgba(170,210,255,.22)':i===2?'rgba(255,190,150,.22)':undefined)});
 iris(L+540,1000,200,1);
 const tr=F.map((f,i)=>[(f[0]-540)/540*.9,(i===0?-.05:.12),.19*eio(seg(t,f[3]+.1,f[3]+.5))]);
 visor(L+540,1560,230,t+6,{tri:tr});
 const fl=golpe(t,fin-.22,.3);if(fl>0){X.fillStyle=`rgba(234,255,234,${fl*.85})`;X.fillRect(L-400,-500,1900,2900)}}
// ---------- P07 · lo más probable: un dron pequeño y lejano; el visor se apaga ----------
function dron(x,y,s,t,a){X.save();X.translate(x,y+Math.sin(t*2)*8);X.scale(s,s);X.globalAlpha=a*.6;X.fillStyle='#070b16';rr(-34,-14,68,28,10);X.fill();X.strokeStyle='#070b16';X.lineWidth=7;X.lineCap='round';[[-1,-1],[1,-1],[-1,1],[1,1]].forEach(q=>{X.beginPath();X.moveTo(q[0]*20,q[1]*6);X.lineTo(q[0]*76,q[1]*26-8);X.stroke();X.beginPath();X.ellipse(q[0]*76,q[1]*26-12,34*Math.abs(Math.cos(t*30+q[0])),5,0,0,7);X.stroke()});
 X.globalAlpha=a*.8;X.setLineDash([7,9]);X.strokeStyle='rgba(255,255,255,.55)';X.lineWidth=3;X.beginPath();X.ellipse(0,0,130,64,0,0,7);X.stroke();X.setLineDash([]);X.restore();puntoLuz(x,y+Math.sin(t*2)*8+4*s,6*s,a*(.6+.4*Math.sin(t*9)))}
function p07(L,t){const c=T.c07,xo=T.x_objects,xm=T.x_most,k=T.x_tell;
 const abre=eio(seg(t,xo-.1,xo+.9)),apaga=eio(seg(t,xm+.6,k-.1));
 noche(L,1560,t);dron(L+430,1290,lerp(.6,1.5,eio(seg(t,xo,k))),t,abre);
 if(apaga<1&&abre<.995){X.save();X.translate(L+430,1290);X.scale(1,Math.max(.004,1-apaga));X.translate(-(L+430),-1290);
  // el visor se abre desde el centro (anillo) y deja ver lo que hay detrás, en el cielo real
  X.save();X.beginPath();X.arc(L+430,1290,470,0,Math.PI*2,false);X.arc(L+430,1290,Math.max(.1,420*abre),0,Math.PI*2,true);X.clip('evenodd');visor(L+430,1290,lerp(430,400,seg(t,c,xo)),t+6,{tri:[[0,0,.2]],a:1-abre});X.restore();
  if(abre>0){X.strokeStyle=`rgba(124,252,138,${.7*(1-abre)})`;X.lineWidth=6;X.beginPath();X.arc(L+430,1290,420*abre,0,7);X.stroke()}X.restore()}
 cierreCanal(L,t,k)}

NUEVOS.dc_rabbit18_p01a=SET(p01a);NUEVOS.dc_rabbit18_p01b=SET(p01b);NUEVOS.dc_rabbit18_p02=SET(p02);NUEVOS.dc_rabbit18_p03=SET(p03);NUEVOS.dc_rabbit18_p04a=SET(p04a);NUEVOS.dc_rabbit18_p04b=SET(p04b);
NUEVOS.dc_rabbit18_p05=SET(p05);NUEVOS.dc_rabbit18_p06=SET(p06);NUEVOS.dc_rabbit18_p07=SET(p07);
})();
// ===== DC · RABBIT18 · FIN =====
</script>
