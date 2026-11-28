<script>
// ===== DC · SGTAES22 · INICIO ===== (GTA ES 22h · La PS5 de GTA 6 que NO puedes comprar · lote del 28-nov · una escena por línea del guion)
// Consola GENÉRICA oscura con palmeras grabadas y franjas del turquesa al magenta (lo que dice el guion): sin la forma de ninguna consola real, mandos genéricos, sin logos (ni de la consola, ni del juego, ni del equipo) y sin retratos: las personas son siluetas. Las placas de serie no llevan números legibles.
(function(){
const {cam,cierreCanal,SET,manoLado,origen}=window.DC;
const {golpe,ruta,plano,par,tex,luz,haz,tinte,arriba,tarj,silueta}=window.B28;
const mano=(px,py,ang,s,dir,o)=>{const q=origen(px,py,ang,s,dir,(o&&o.lx)||150,(o&&o.ly)||10);return manoLado(q[0],q[1],ang,s,dir,Object.assign({manga:'#1c2533',puno:'#2a3646'},o))};
const TQ='47,224,208',MG='255,63,176',BL='235,240,255';
const mez=(a,b,k)=>{const A=a.split(',').map(Number),B=b.split(',').map(Number);return A.map((v,i)=>Math.round(v+(B[i]-v)*k)).join(',')};

function placa(x,y,s,texto,a,o){if(a<=0)return;o=o||{};X.save();X.globalAlpha=a;const w=(o.w||(texto.length*30+70))*s;tarj(x,y,w,90*s,14*s,o.col||'#121420',{sa:.3,borde:o.borde||`rgba(${TQ},.7)`,lw:3});txt(texto,x,y+4*s,(o.ts||46)*s,o.tc||'#fff',{w:800});X.restore()}
function estudioO(L,o){o=o||{};const yp=o.yp||1500;X.fillStyle=gl(0,0,0,yp,[[0,'#08090d'],[1,'#171a24']]);X.fillRect(L-1400,-900,3900,yp+960);luz(L-100,yp-500,700,TQ,.07);luz(L+1180,yp-500,700,MG,.07);X.fillStyle=gl(0,yp,0,1920,[[0,'#101218'],[1,'#06070a']]);X.fillRect(L-1400,yp,3900,1500);X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-1400,yp,3900,4)}
function palma(x,y,s,a,inv){X.save();X.translate(x,y);X.scale(s*(inv?-1:1),s);X.strokeStyle=`rgba(255,255,255,${a})`;X.lineWidth=5;X.lineCap='round';X.beginPath();X.moveTo(0,0);X.quadraticCurveTo(16,-120,-6,-230);X.stroke();for(let i=0;i<6;i++){const an=-2.9+i*.56;X.beginPath();X.moveTo(-6,-230);X.quadraticCurveTo(-6+Math.cos(an)*60,-254+Math.sin(an)*60,-6+Math.cos(an)*110,-220+Math.sin(an)*70);X.stroke()}X.restore()}
// cara de la consola genérica (340×760, centrada): palmas, franjas y grad van de 0 a 1 · raso: luz rasante que la recorre · placa: placa de serie
function cara(o){o=o||{};const w=340,h=760,pa=o.palmas===undefined?1:o.palmas,fr=o.franjas===undefined?1:o.franjas,gr=o.grad===undefined?1:o.grad;X.fillStyle=gl(-w/2,0,w/2,0,[[0,'#1d2028'],[.5,'#13151b'],[1,'#0b0c10']]);rr(-w/2,-h/2,w,h,44);X.fill();X.save();rr(-w/2,-h/2,w,h,44);X.clip();tex('cuero',-w/2,-h/2,w,h,{a:.16,s:1});
 if(fr>0){const fin=mez(TQ,MG,gr);for(let i=0;i<5;i++){const b=110+i*58;X.fillStyle=gl(-170,0,-170+340*fr,0,[[0,`rgb(${TQ})`],[1,`rgb(${fin})`]]);X.beginPath();X.moveTo(-170,b);X.lineTo(-170+340*fr,b-150*fr);X.lineTo(-170+340*fr,b-150*fr+30);X.lineTo(-170,b+30);X.closePath();X.fill()}}
 palma(-60,-40,1,.07+.5*pa);palma(70,10,.7,.06+.42*pa,1);
 if(o.raso>0&&o.raso<1){const rx=lerp(-260,260,o.raso);X.fillStyle='rgba(255,255,255,.13)';X.beginPath();X.moveTo(rx,-h/2);X.lineTo(rx+90,-h/2);X.lineTo(rx-40,h/2);X.lineTo(rx-130,h/2);X.closePath();X.fill()}
 X.fillStyle='rgba(190,235,255,.85)';rr(-4,-h/2+44,8,130,4);X.fill();
 if(o.placa){X.fillStyle=gl(-70,0,70,0,[[0,'#8e98a4'],[.5,'#cfd6dc'],[1,'#7c8690']]);rr(-74,292,148,50,6);X.fill();txt('N.º',-44,318,24,'#22282e',{w:800});X.fillStyle='#22282e';for(let i=0;i<4;i++){rr(-12+i*20,308,14,20,3);X.fill()}}
 X.restore();X.strokeStyle='rgba(255,255,255,.1)';X.lineWidth=3;rr(-w/2,-h/2,w,h,44);X.stroke()}
// consola de pie con giro simulado (ang): muestra la cara y el canto
function torre(x,yb,s,ang,o){const c=Math.cos(ang),sn=Math.sin(ang),fw=340*Math.abs(c),sw=100*Math.abs(sn),d=sn>=0?1:-1;X.save();X.translate(x,yb-380*s);X.scale(s,s);X.fillStyle='rgba(0,0,0,.5)';X.beginPath();X.ellipse(0,388,(fw+sw)/2+50,24,0,0,7);X.fill();
 if(sw>2){X.fillStyle=gl(0,-380,0,380,[[0,'#0c0d11'],[1,'#050608']]);rr(d>0?(fw+sw)/2-sw-4:-(fw+sw)/2,-380,sw+4,760,16);X.fill()}X.save();X.translate(d>0?-sw/2:sw/2,0);X.scale(Math.max(.03,Math.abs(c)),1);cara(o);X.restore();X.restore()}
function mando(x,y,s,rot,g){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);if(g>0)luz(0,0,170,TQ,.45*g);X.fillStyle='rgba(0,0,0,.4)';rr(-104,-46,216,110,50);X.fill();X.fillStyle='#191b22';rr(-110,-56,220,104,50);X.fill();[-78,78].forEach(q=>{X.beginPath();X.arc(q,20,44,0,7);X.fill()});
 X.fillStyle=gl(-110,0,110,0,[[0,`rgb(${TQ})`],[1,`rgb(${MG})`]]);rr(-70,-50,140,7,3);X.fill();[-40,40].forEach(q=>{X.fillStyle='#07080b';X.beginPath();X.arc(q,6,17,0,7);X.fill();X.fillStyle='#2a2e38';X.beginPath();X.arc(q,6,10,0,7);X.fill()});
 X.fillStyle='#2a2e38';rr(-90,-28,26,8,3);X.fill();rr(-81,-37,8,26,3);X.fill();[[78,-36],[92,-24],[64,-24],[78,-12]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],5.5,0,7);X.fill()});X.restore()}
function estuche(x,y,s,rot,g){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);if(g>0)luz(0,0,190,MG,.45*g);X.fillStyle='rgba(0,0,0,.4)';rr(-74,-98,160,210,10);X.fill();X.fillStyle='#1c2a4a';rr(-80,-105,160,210,10);X.fill();X.fillStyle='#10182c';rr(-66,-80,132,172,6);X.fill();X.fillStyle=gl(-66,0,66,0,[[0,`rgb(${TQ})`],[1,`rgb(${MG})`]]);X.fillRect(-66,34,132,14);X.fillStyle='rgba(255,255,255,.12)';X.fillRect(-80,-105,160,22);X.restore()}
// maleta rígida de frente, cerrada. lazo: moño de regalo · brillo: luz turquesa-magenta
function maletaF(x,yb,s,o){o=o||{};X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(0,0,290,22,0,0,7);X.fill();if(o.brillo>0){luz(-60,-170,380,TQ,.18*o.brillo);luz(80,-170,340,MG,.15*o.brillo)}
 X.strokeStyle='#0c0d11';X.lineWidth=22;X.lineJoin='round';X.beginPath();X.moveTo(-80,-336);X.lineTo(-80,-386);X.lineTo(80,-386);X.lineTo(80,-336);X.stroke();X.fillStyle=gl(0,-340,0,0,[[0,'#1e2028'],[1,'#0d0e12']]);rr(-270,-340,540,340,30);X.fill();tex('cuero',-270,-340,540,340,{a:.14});
 X.fillStyle='rgba(255,255,255,.05)';for(let i=0;i<5;i++){rr(-236,-296+i*58,472,20,10);X.fill()}X.fillStyle='rgba(0,0,0,.5)';X.fillRect(-270,-176,540,6);
 [-150,150].forEach(q=>{X.fillStyle=gl(0,-206,0,-142,[[0,'#cfd6dc'],[1,'#7c8690']]);rr(q-34,-206,68,64,8);X.fill();X.fillStyle='#22282e';rr(q-20,-190,40,14,4);X.fill()});X.fillStyle='#2a2e38';[[-262,-332],[232,-332],[-262,-38],[232,-38]].forEach(p=>{rr(p[0],p[1],30,30,8);X.fill()});
 if(o.lazo){X.fillStyle=`rgb(${MG})`;X.fillRect(-18,-340,36,340);X.fillRect(-270,-190,540,34);X.beginPath();X.ellipse(-48,-372,50,26,-.4,0,7);X.fill();X.beginPath();X.ellipse(48,-372,50,26,.4,0,7);X.fill();X.fillStyle='#c22a86';X.beginPath();X.arc(0,-360,18,0,7);X.fill()}X.restore()}
// maleta de frente que se abre (ab 0…1): la tapa sube y sale luz de adentro
function maletaAb(x,yb,s,ab){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='rgba(0,0,0,.45)';X.beginPath();X.ellipse(0,0,290,22,0,0,7);X.fill();const yt=lerp(-340,-500,ab),yl=lerp(-176,-200,ab);
 if(ab>0){luz(0,-190,420,TQ,.3*ab);luz(90,-190,360,MG,.24*ab)}X.fillStyle=gl(0,yt,0,yl,[[0,ab>.5?'#22252e':'#1e2028'],[1,ab>.5?'#15171d':'#14151a']]);rr(-270+12*ab,yt,540-24*ab,yl-yt,26);X.fill();if(ab>.5){X.fillStyle='#2a2d37';rr(-236,yt+26,472,yl-yt-52,16);X.fill();tex('tela',-236,yt+26,472,yl-yt-52,{a:.3,s:1.1})}else{X.fillStyle='rgba(255,255,255,.05)';for(let i=0;i<2;i++){rr(-236,yt+40+i*58,472,20,10);X.fill()}}
 if(ab>0){X.fillStyle=gl(-200,0,200,0,[[0,`rgba(${TQ},${.8*ab})`],[1,`rgba(${MG},${.8*ab})`]]);X.fillRect(-250,yl-2,500,-176-yl+6)}
 X.fillStyle=gl(0,-176,0,0,[[0,'#1a1c23'],[1,'#0d0e12']]);rr(-270,-176,540,176,26);X.fill();X.fillStyle='rgba(255,255,255,.05)';for(let i=0;i<2;i++){rr(-236,-126+i*58,472,20,10);X.fill()}[-150,150].forEach(q=>{X.fillStyle='#8e98a4';rr(q-34,-176,68,40,8);X.fill()});X.restore()}
// maleta vista desde arriba. q: 0 cerrada … 1 (la tapa se acorta hacia la bisagra de arriba) · plana: abierta del todo, con la tapa tendida encima
function maletaT(x,y,s,q,o){o=o||{};X.save();X.translate(x,y);X.scale(s,s);const W=800,H=520,yL=lerp(H/2,-H/2+H*.06,q);X.fillStyle='rgba(0,0,0,.45)';rr(-W/2+14,-H/2+22,W,H,34);X.fill();
 if(o.plana){X.fillStyle='#0f1014';rr(-W/2,-H/2-H-16,W,H,34);X.fill();X.fillStyle='#1b1d22';rr(-W/2+26,-H/2-H+10,W-52,H-52,20);X.fill();tex('tela',-W/2+26,-H/2-H+10,W-52,H-52,{a:.3,s:1.2});X.fillStyle='#0c0d11';X.fillRect(-W/2+60,-H/2-22,90,28);X.fillRect(W/2-150,-H/2-22,90,28)}
 X.fillStyle='#0f1014';rr(-W/2,-H/2,W,H,34);X.fill();X.fillStyle='#1b1d22';rr(-W/2+26,-H/2+26,W-52,H-52,20);X.fill();tex('tela',-W/2+26,-H/2+26,W-52,H-52,{a:.3,s:1.2});
 if(q>0||o.plana){X.save();X.beginPath();X.rect(-W/2,o.plana?-H/2:yL,W,o.plana?H:H/2-yL);X.clip();X.fillStyle='#0b0c0f';rr(-372,-42,564,274,24);X.fill();rr(-352,-218,224,136,40);X.fill();rr(-122,-218,224,136,40);X.fill();rr(196,-120,178,228,14);X.fill();
  X.save();X.translate(-90,95);X.rotate(-Math.PI/2);X.scale(.7,.7);cara({palmas:o.palmas,franjas:1,grad:1});X.restore();if(o.luzI>0){luz(-90,95,330,TQ,.2*o.luzI);luz(60,120,300,MG,.18*o.luzI)}
  mando(-240,-150,.95,0,o.g1||0);mando(-10,-150,.95,0,o.g2||0);estuche(285,-6,.95,0,o.g3||0);X.restore()}
 if(!o.plana&&q<1){if(q>0){X.fillStyle='rgba(0,0,0,.5)';X.fillRect(-W/2+10,yL,W-20,26)}const hh=yL+H/2;X.fillStyle=gl(0,-H/2,0,yL,[[0,'#1e2028'],[1,'#101116']]);rr(-W/2,-H/2,W,hh,34);X.fill();X.fillStyle='rgba(255,255,255,.05)';for(let i=0;i<6;i++){rr(-W/2+50,-H/2+hh*(.1+i*.145),W-100,hh*.06,8);X.fill()}
  X.fillStyle='#0c0d11';rr(-90,yL-14,180,36,14);X.fill();[-200,200].forEach(p=>{X.save();X.translate(p,yL);X.scale(1,1-1.7*(o.broche||0));X.fillStyle=gl(-30,0,30,0,[[0,'#7c8690'],[.5,'#cfd6dc'],[1,'#7c8690']]);rr(-30,-30,60,56,8);X.fill();X.fillStyle='#22282e';rr(-18,2,36,12,4);X.fill();X.restore()})}X.restore()}
function etiqueta(x,y,s,rot,tach){X.save();X.translate(x,y);X.rotate(rot);X.scale(s,s);X.strokeStyle='#cfd6dc';X.lineWidth=4;X.beginPath();X.moveTo(-96,0);X.quadraticCurveTo(-150,-40,-190,-10);X.stroke();X.fillStyle='rgba(0,0,0,.35)';rr(-84,-42,200,100,14);X.fill();X.fillStyle='#f4efe6';X.beginPath();X.moveTo(-100,0);X.lineTo(-60,-50);X.lineTo(100,-50);X.lineTo(100,50);X.lineTo(-60,50);X.closePath();X.fill();X.fillStyle='#22282e';X.beginPath();X.arc(-66,0,9,0,7);X.fill();txt('$',-14,4,64,'#22282e',{w:900});X.fillStyle='rgba(34,40,46,.3)';rr(16,-8,60,16,8);X.fill();
 if(tach>0){X.strokeStyle='#e23a3a';X.lineWidth=12;X.lineCap='round';X.beginPath();X.moveTo(-70,44);X.lineTo(-70+170*tach,44-88*tach);X.stroke()}X.restore()}
function calend(x,y,s,o){X.save();X.translate(x,y);X.rotate(-.03);X.scale(s,s);X.fillStyle='rgba(0,0,0,.4)';rr(-188,-236,400,500,20);X.fill();X.fillStyle='#e9e6dc';rr(-200,-250,400,500,20);X.fill();X.fillStyle='#22282e';rr(-200,-250,400,120,20);X.fill();X.fillRect(-200,-160,400,30);X.fillStyle='#8e98a4';[-110,110].forEach(q=>{rr(q-10,-280,20,60,8);X.fill()});
 if(o.mes>0){X.save();X.globalAlpha=o.mes;txt('NOVIEMBRE',0,-206,44,'#fff',{w:800});X.restore()}if(o.anio>0){X.save();X.globalAlpha=o.anio;txt('2026',0,-156,34,`rgb(${TQ})`,{w:800});X.restore()}
 if(o.dias>0){X.fillStyle=`rgba(34,40,46,${.28*o.dias})`;for(let r=0;r<5;r++)for(let c=0;c<7;c++){X.beginPath();X.arc(-150+c*50,-80+r*62,9,0,7);X.fill()}}
 if(o.marca>0){X.save();X.globalAlpha=o.marca;X.strokeStyle=`rgb(${MG})`;X.lineWidth=8;X.beginPath();X.arc(-50,44,26,0,7);X.stroke();X.fillStyle='#22282e';X.beginPath();X.arc(-50,44,9,0,7);X.fill();X.fillRect(-3,10,6,50);X.fillStyle=`rgb(${TQ})`;X.beginPath();X.moveTo(3,10);X.lineTo(44,24);X.lineTo(3,38);X.closePath();X.fill();X.restore()}X.restore()}
function jugadorB(x,yb,h,o){o=o||{};const s=h/600,col=o.col||'#11141b';X.save();X.translate(x,yb);X.scale(s*(o.dir||1),s);X.fillStyle='rgba(0,0,0,.35)';X.beginPath();X.ellipse(0,0,90,14,0,0,7);X.fill();X.fillStyle=col;rr(-46,-250,36,250,14);X.fill();rr(10,-250,36,250,14);X.fill();rr(-58,-22,52,22,10);X.fill();rr(8,-22,58,22,10);X.fill();
 X.beginPath();X.moveTo(-58,-250);X.lineTo(58,-250);X.lineTo(52,-330);X.lineTo(-52,-330);X.closePath();X.fill();X.beginPath();X.moveTo(-54,-320);X.lineTo(54,-320);X.lineTo(66,-500);X.quadraticCurveTo(0,-520,-66,-500);X.closePath();X.fill();X.fillRect(-12,-530,24,34);X.beginPath();X.arc(0,-556,34,0,7);X.fill();
 X.strokeStyle=col;X.lineWidth=26;X.lineCap='round';X.lineJoin='round';if(o.recibe){X.beginPath();X.moveTo(-60,-486);X.lineTo(-84,-390);X.lineTo(-150,-330);X.stroke();X.beginPath();X.moveTo(60,-486);X.lineTo(40,-390);X.lineTo(-90,-318);X.stroke()}else{X.beginPath();X.moveTo(-62,-486);X.lineTo(-80,-380);X.lineTo(-74,-280);X.stroke();X.beginPath();X.moveTo(62,-486);X.lineTo(82,-380);X.lineTo(70,-290);X.stroke()}
 if(o.balon){X.fillStyle='#d9742a';X.beginPath();X.arc(100,-290,44,0,7);X.fill();X.strokeStyle='#5a2a0c';X.lineWidth=4;X.beginPath();X.arc(100,-290,44,0,7);X.moveTo(56,-290);X.lineTo(144,-290);X.moveTo(100,-334);X.lineTo(100,-246);X.stroke()}
 X.strokeStyle='rgba(255,220,170,.25)';X.lineWidth=4;X.beginPath();X.moveTo(64,-498);X.lineTo(54,-324);X.stroke();X.restore()}
function cancha(L,cm,t){const yp=1380;X.fillStyle=gl(0,0,0,yp,[[0,'#07080c'],[1,'#151823']]);X.fillRect(L-1400,-900,3900,yp+960);for(let i=0;i<26;i++)luz(L-200+rnd(i)*1500+par(cm,.7),620+rnd(i+9)*520,26+rnd(i+5)*40,i%3?'255,236,200':'255,140,120',(.05+.1*rnd(i+3))*(.6+.4*Math.sin(t*2+i)));
 X.fillStyle='#b8793e';X.fillRect(L-1400,yp,3900,1500);tex('madera',L-1400,yp,3900,900,{a:.55,s:1.8,tinte:'190,128,70'});X.fillStyle='rgba(255,255,255,.16)';X.fillRect(L-1400,yp,3900,6);
 X.strokeStyle='rgba(255,255,255,.75)';X.lineWidth=9;X.beginPath();X.moveTo(L+640,yp+44);X.lineTo(L+1700,yp+44);X.moveTo(L+640,yp+44);X.lineTo(L+500,1960);X.stroke();X.beginPath();X.ellipse(L+575,yp+300,260,90,0,Math.PI*.5,Math.PI*1.5,false);X.stroke();haz(L+300,-100,L+500,yp+200,80,420,'255,244,220',.12);
 const px=par(cm,.3);X.fillStyle='#8e98a4';X.fillRect(L+1010+px,790,14,600);X.fillStyle='rgba(235,240,255,.75)';rr(L+900+px,720,170,116,8);X.fill();X.strokeStyle='#22282e';X.lineWidth=5;X.strokeRect(L+950+px,772,70,50);X.strokeStyle='#e0662a';X.lineWidth=8;X.beginPath();X.ellipse(L+900+px,846,52,12,0,0,7);X.stroke()}
// set de streaming genérico. v: 0 turquesa (micrófono con brazo) · 1 magenta (aro de luz y cámara)
function setS(L,cm,t,v){const col=v?MG:TQ,px=v?620:110;X.fillStyle=gl(0,0,0,1400,[[0,'#08090d'],[1,v?'#1c1220':'#101c22']]);X.fillRect(L-1400,-900,3900,2360);
 for(let r=0;r<2;r++)for(let c2=0;c2<3;c2++){const x=L+px+c2*124+par(cm,.3),y=640+r*124,h=(r+c2)%2;X.fillStyle=h?'#1a1d27':'#14161e';rr(x,y,112,112,8);X.fill();X.strokeStyle='rgba(255,255,255,.05)';X.lineWidth=3;for(let k=1;k<4;k++){X.beginPath();if(h){X.moveTo(x+k*28,y+6);X.lineTo(x+k*28,y+106)}else{X.moveTo(x+6,y+k*28);X.lineTo(x+106,y+k*28)}X.stroke()}}
 X.fillStyle=`rgba(${col},.9)`;X.fillRect(L-1400,1010,3900,8);luz(L+540,1014,900,col,.16,160);
 if(v){luz(L+230,1040,200,BL,.3);X.strokeStyle='#f4efe6';X.lineWidth=22;X.beginPath();X.arc(L+230,1040,96,0,7);X.stroke();X.strokeStyle='#22262f';X.lineWidth=12;X.beginPath();X.moveTo(L+230,1136);X.lineTo(L+230,1400);X.stroke()}
 silueta(L+(v?850:230),1700,1.3,'#0a0b10',{brazo:v?-1:1,bx:150,by:-240});
 X.fillStyle='#14161e';X.fillRect(L-1400,1400,3900,1200);X.fillStyle='rgba(255,255,255,.07)';X.fillRect(L-1400,1400,3900,5);
 if(!v){X.strokeStyle='#22262f';X.lineWidth=12;X.lineCap='round';X.lineJoin='round';X.beginPath();X.moveTo(L+1100,1400);X.lineTo(L+1000,1090);X.lineTo(L+850,1170);X.stroke();X.fillStyle='#2a2e38';rr(L+800,1140,76,130,30);X.fill();X.fillStyle='rgba(255,255,255,.12)';for(let i=0;i<4;i++)X.fillRect(L+812,1160+i*24,52,5)}
 else{X.strokeStyle='#22262f';X.lineWidth=10;X.lineCap='round';X.beginPath();X.moveTo(L+110,1400);X.lineTo(L+140,1240);X.moveTo(L+170,1400);X.lineTo(L+140,1240);X.stroke();X.fillStyle='#22262f';rr(L+86,1160,110,84,10);X.fill();X.fillStyle='#07080b';X.beginPath();X.arc(L+196,1202,26,0,7);X.fill();X.fillStyle='#e23a3a';X.beginPath();X.arc(L+104,1176,6,0,7);X.fill()}}
function placaS(x,y,s,i,refl){X.save();X.translate(x,y);X.rotate(-.06);X.scale(s,s);X.fillStyle='rgba(0,0,0,.5)';rr(-184,-66,380,150,14);X.fill();X.fillStyle=gl(-190,0,190,0,[[0,'#7c8690'],[.5,'#cfd6dc'],[1,'#7c8690']]);rr(-190,-75,380,150,14);X.fill();tex('metal',-190,-75,380,150,{a:.3,v:1});X.fillStyle='#4a5560';[[-168,-53],[168,-53],[-168,53],[168,53]].forEach(p=>{X.beginPath();X.arc(p[0],p[1],8,0,7);X.fill()});
 txt('N.º',-118,4,54,'#22282e',{w:900});X.fillStyle='#22282e';let xx=-54;for(let k=0;k<5;k++){const w=12+rnd(i*9+k)*22,al=rnd(i*5+k)>.5;rr(xx,al?-24:-10,w,al?48:34,5);X.fill();xx+=w+9}
 if(refl>0&&refl<1){X.save();rr(-190,-75,380,150,14);X.clip();const rx=lerp(-300,300,refl);X.fillStyle='rgba(255,255,255,.5)';X.beginPath();X.moveTo(rx,-80);X.lineTo(rx+50,-80);X.lineTo(rx+10,80);X.lineTo(rx-40,80);X.closePath();X.fill();X.restore()}X.restore()}

// ---------- 01 · gancho: macro del broche; la maleta se abre, deja ver parte de la consola y se cierra antes de mostrar todo ----------
function p01(L,t){const xc=T.x_comprar,xr=T.x_rockstar,xp=T.x_precio,xa=T.x_raro,f=T.c02,br=eio(seg(t,.4,.7)),k=eio(seg(t,.85,xc-.2))*(1-eio(seg(t,xa-.1,xa+.6))),q=.42*k,et=eio(seg(t,xr-.2,xr+.1))*(1-eio(seg(t,xa-.3,xa))),ta=eio(seg(t,xp-.35,xp-.05));
 plano(L,t,[[0,740,1400,2.3],[.85,740,1385,2.1],[xc,540,1180,1.1],[xa,540,1170,1.08],[f,560,1160,1.2]],cm=>{X.fillStyle='#0c0d12';X.fillRect(L-1400,-900,3900,3800);tex('cuero',L-1400,-300,3900,2600,{a:.2,s:2});luz(L+540,1150,820,BL,.1);
  maletaT(L+540,1150,1,q,{broche:br,palmas:.6,luzI:k});if(k>.02){luz(L+440,1330,420,TQ,.16*k);luz(L+700,1330,360,MG,.14*k)}
  if(et>0){X.save();X.globalAlpha=et;etiqueta(L+770,1570,1.15,-.12,ta);X.restore()}});
 arriba(L,.62)}

// ---------- 02 · apareció en noviembre de 2026, justo antes del lanzamiento ----------
function p02(L,t){const c=T.c02,xn=T.x_nov,x2=T.x_2026,xa=T.x_antes,f=T.c03,dias=eio(seg(t,c+.15,c+.5))*(1-eio(seg(t,xa-.4,xa-.15)));
 plano(L,t,[[c,330,1090,1.3],[xa-.1,345,1095,1.36],[xa+.8,720,1160,1.3],[f,740,1160,1.36]],cm=>{estudioO(L,{yp:1400});luz(L+330,1050,560,BL,.14);calend(L+330,1090,1,{mes:eio(seg(t,xn-.15,xn+.15)),anio:eio(seg(t,x2-.15,x2+.15)),dias,marca:eio(seg(t,xa-.1,xa+.15))});
  haz(L+800,200,L+800,1400,50,360,BL,.14);maletaF(L+800,1400,.8,{brillo:.7+.3*Math.sin(t*3)})});
 arriba(L,.6)}

// ---------- 03 · una consola oscura, con palmeras grabadas y franjas que van del turquesa al magenta ----------
function p03(L,t){const c=T.c03,xp=T.x_palmeras,xf=T.x_franjas,xt=T.x_turquesa,xm=T.x_magenta,f=T.c04,ang=t<xp+.5?lerp(-1.1,0,eio(seg(t,c,xp-.2))):Math.PI*eio(seg(t,xp+.5,xf+.15)),fre=Math.cos(ang)>=0,pal=eio(seg(t,xp-.3,xp+.3)),fr=eio(seg(t,xf+.1,xt+.25)),gr=eio(seg(t,xt+.25,xm+.15));
 plano(L,t,[[c,500,1090,1.1],[xp,540,1080,1.24],[xf,560,1120,1.2],[f,540,1150,1.36]],cm=>{estudioO(L,{yp:1500});X.fillStyle='#1a1d27';X.beginPath();X.ellipse(L+540,1500,330,54,0,0,7);X.fill();X.strokeStyle='rgba(255,255,255,.12)';X.lineWidth=4;X.beginPath();X.ellipse(L+540,1500,330,54,0,0,7);X.stroke();
  haz(L+540,150,L+540,1500,60,400,BL,.12);if(fr>0){luz(L+340,1300,420,TQ,.18*fr);luz(L+740,1250,420,mez(TQ,MG,gr),.18*fr)}
  torre(L+540,1500,1,ang,fre?{palmas:pal,franjas:0,raso:seg(t,xp-.4,xp+.8)}:{palmas:.7,franjas:fr,grad:gr,raso:seg(t,xf-.1,xf+1)})});
 arriba(L,.6)}

// ---------- 04 · viene en una maleta rígida, con dos controles a juego y una copia del juego (cenital que baja) ----------
function p04(L,t){const c=T.c04,xd=T.x_dos,xc=T.x_copia,f=T.c05,g1=golpe(t,xd,.7),g2=golpe(t,xd+.3,.7),g3=golpe(t,xc,.8);
 plano(L,t,[[c,540,1010,.9,0],[xd,480,1120,1.18,-.03],[xc,640,1250,1.26,.02],[f,570,1200,1.18,0]],cm=>{X.fillStyle='#0c0d12';X.fillRect(L-1400,-900,3900,3800);tex('cuero',L-1400,-300,3900,2600,{a:.2,s:2});luz(L+540,1100,900,BL,.1);maletaT(L+540,1300,.95,1,{plana:1,palmas:.7,luzI:1,g1,g2,g3})});
 arriba(L,.6)}

// ---------- 05 · muchos fans pidieron que saliera a la venta: la vitrina no se abre ----------
function p05(L,t){const c=T.c05,xf=T.x_fans,xv=T.x_venta,f=T.c06,al=eio(seg(t,xf-.1,xv));
 plano(L,t,[[c,480,1120,1.08],[f,600,1120,1.14]],cm=>{estudioO(L,{yp:1420});X.fillStyle='#1a1d27';rr(L+270,1330,540,110,10);X.fill();haz(L+540,300,L+540,1330,40,300,BL,.16);X.fillStyle='#22262f';rr(L+440,1230,200,100,8);X.fill();torre(L+540,1230,.62,.35,{palmas:.7,franjas:1,grad:1});
  X.fillStyle='rgba(160,220,255,.07)';X.fillRect(L+290,640,500,690);X.strokeStyle='rgba(200,230,255,.5)';X.lineWidth=6;X.strokeRect(L+290,640,500,690);X.fillStyle='rgba(255,255,255,.08)';X.beginPath();X.moveTo(L+330,640);X.lineTo(L+450,640);X.lineTo(L+330,1000);X.closePath();X.fill();candado(L+540,1290,.5,'#cfd6dc',false);
  [[150,1900,1.5,1],[400,1960,1.6,1],[720,1950,1.55,-1],[960,1890,1.45,-1]].forEach((p,i)=>silueta(L+p[0],p[1],p[2],i%2?'#1a1d28':'#141722',{brazo:p[3],bx:lerp(150,105,al),by:lerp(-190,-330-i%2*20,al)}))});
 arriba(L,.6)}

// ---------- 06 · G2: lo más raro, a quiénes se la dieron y cuántas existen (la cámara se detiene en la placa de serie) ----------
function p06(L,t){const c=T.c06,xa=T.x_ahora,xq=T.x_quienes,xc=T.x_cuantas,f=T.c07,g=golpe(t,xa,.6),ang=lerp(-.95,0,eio(seg(t,c,xq-.1))),gp=golpe(t,xc,.7);
 plano(L,t,[[c,540,1100,1.05],[xq,540,1150,1.22],[xc,540,1385,2.3],[f,540,1400,2.5]],cm=>{X.fillStyle='#050608';X.fillRect(L-1400,-900,3900,3800);haz(L+540,100,L+540,1500,40,330,BL,.2+.1*g);luz(L+830,1150,520,MG,.18);X.fillStyle='rgba(255,255,255,.05)';X.beginPath();X.ellipse(L+540,1500,330,50,0,0,7);X.fill();
  torre(L+540,1500,1,ang,{palmas:.6,franjas:1,grad:1,placa:1});if(gp>0)luz(L+540,1438,130,BL,.5*gp)});
 arriba(L,.94,680)}

// ---------- 07 · las primeras no fueron para gamers: fueron para basquetbolistas del Miami Heat, un día antes del estreno ----------
function p07(L,t){const c=T.c07,xg=T.x_gamers,xb=T.x_basq,xm=T.x_miami,xd=T.x_dia,f=T.c08,k=xb-.25;
 if(t<k){const sl=eio(seg(t,c+.5,xg+.2));plano(L,t,[[c,520,1130,1.12],[k,580,1130,1.2]],cm=>{estudioO(L,{yp:1450});X.fillStyle='#07080b';rr(L+150,1010,360,240,14);X.fill();X.fillStyle='#1c2a4a';rr(L+166,1026,328,208,8);X.fill();luz(L+330,1130,420,'90,140,255',.2);X.fillStyle='#07080b';X.fillRect(L+310,1250,40,130);
   X.fillStyle='#0f1118';rr(L+60,1380,620,80,10);X.fill();silueta(L+330,1760,1.5,'#0a0b10',{brazo:1,bx:lerp(150,190,sl),by:-200});X.strokeStyle='#22262f';X.lineWidth=18;X.lineCap='round';X.beginPath();X.arc(L+330,1310,74,Math.PI*1.08,Math.PI*1.92);X.stroke();X.fillStyle='#22262f';rr(L+244,1290,30,70,12);X.fill();rr(L+386,1290,30,70,12);X.fill();
   maletaF(L+lerp(640,1500,sl*sl),1380,.6,{brillo:1})});tinte(L,'0,0,0',.3*eio(seg(t,xg-.2,xg+.2)))}
 else{const en=eio(seg(t,xb+.1,xm));plano(L,t,[[k,780,1060,1.22],[xm,560,1180,1.2],[f,500,1200,1.3]],cm=>{cancha(L,cm,t);jugadorB(L+880,1650,640,{balon:1});jugadorB(L+700,1600,600,{});jugadorB(L+520,1620,620,{recibe:1});
   silueta(L+150,1640,1.1,'#0c0e14',{brazo:1,bx:120,by:-170});maletaF(L+lerp(250,372,en),1400,.34,{brillo:1})})}
 arriba(L,.6);placa(L+540,1660,1.1,'MIAMI HEAT',eio(seg(t,xm-.1,xm+.2)),{w:340,borde:`rgba(${BL},.7)`});placa(L+540,1780,1,'UN DÍA ANTES',eio(seg(t,xd-.1,xd+.2)),{ts:40,w:380,borde:`rgba(${MG},.7)`})}

// ---------- 08 · después llegaron a streamers y creadores de contenido (corte por coincidencia entre dos sets) ----------
function p08(L,t){const c=T.c08,xs=T.x_streamers,xc=T.x_creadores,f=T.c09,k=xc-.12,v=t<k?0:1,ab=eio(seg(t,xs-.3,xc+.5));
 plano(L,t,v?[[k,600,1140,1.2],[f,540,1140,1.28]]:[[c,470,1140,1.14],[k,540,1140,1.2]],cm=>{setS(L,cm,t,v);maletaAb(L+540,1400,.74,ab)});
 arriba(L,.6)}

// ---------- 09 · cada una trae su propio número de serie (placas distintas, sin números legibles) ----------
function p09(L,t){const c=T.c09,xs=T.x_serie,f=T.c10;
 plano(L,t,[[c,280,930,1.5],[xs,620,1150,1.5],[f,800,1310,1.58]],cm=>{X.fillStyle='#0d0f14';X.fillRect(L-1400,-900,3900,3800);tex('metal',L-1400,-300,3900,2600,{a:.14,v:1});luz(L+540,1100,900,BL,.08);
  [[250,900],[560,1120],[870,1340]].forEach((p,i)=>{luz(L+p[0],p[1],300,i%2?MG:TQ,.1);placaS(L+p[0],p[1],1,i+1,seg(t,c+.15+i*.6,c+.75+i*.6))})});
 arriba(L,.6)}

// ---------- 10 · según los reportes, existen solo unas 100 en todo el mundo ----------
function p10(L,t){const c=T.c10,xr=T.x_reportes,x1=T.x_100,xm=T.x_mundo,f=T.c11,g=golpe(t,x1,.7),am=eio(seg(t,xm-.5,xm+.1));
 plano(L,t,[[c,540,1540,2.2],[x1,540,1120,1.05],[f,540,1100,1]],cm=>{X.fillStyle=gl(0,0,0,1920,[[0,'#07080c'],[1,'#11131b']]);X.fillRect(L-1400,-900,3900,3800);if(am>0){X.save();X.globalAlpha=.22*am;tierra(L+540,1090,400,t);X.restore()}
  for(let r=0;r<10;r++)for(let q=0;q<10;q++){const x=L+153+q*86,y=820+r*60;X.fillStyle='#1e2230';rr(x-30,y-20,60,40,8);X.fill();X.fillStyle='#2c3142';rr(x-10,y-28,20,10,4);X.fill()}
  maletaF(L+540,1650,.5,{brillo:1})});
 arriba(L,.9,640);placa(L+540,572,1.45+.12*g,'≈ 100',eio(seg(t,x1-.1,x1+.15)),{w:250,ts:60,borde:`rgba(${MG},.8)`});placa(L+540,1780,1.1,'SEGÚN LOS REPORTES',eio(seg(t,xr-.1,xr+.2)),{ts:38,w:520})}

// ---------- 11 · Rockstar ya dijo que no llegará a las tiendas: baja la persiana y se apagan las luces ----------
function p11(L,t){const c=T.c11,xd=T.x_dijo,xt=T.x_tiendas,f=T.c12,q=eio(seg(t,xd-.1,xt-.1)),wx=L+210,wy=720,ww=660,wh=700;
 plano(L,t,[[c,440,1120,1.05],[f,560,1090,1.28]],cm=>{X.fillStyle='#14110f';X.fillRect(L-1400,-900,3900,3800);tex('ladrillo',L-1400,-300,3900,2000,{a:.5,s:1.6,tinte:'60,40,34'});X.fillStyle='#1c1f26';X.fillRect(L-1400,1500,3900,1200);tex('concreto',L-1400,1500,3900,700,{a:.2});X.fillStyle='#0f1118';X.fillRect(wx-40,wy-110,ww+80,70);
  X.fillStyle='#07080b';X.fillRect(wx-18,wy-18,ww+36,wh+36);X.fillStyle=gl(0,wy,0,wy+wh,[[0,'#2a2418'],[1,'#3a301c']]);X.fillRect(wx,wy,ww,wh);luz(wx+ww/2,wy+wh*.55,520,'255,220,160',.5*(1-q));X.fillStyle='#22262f';rr(wx+ww/2-160,wy+wh-130,320,130,8);X.fill();maletaF(wx+ww/2,wy+wh-130,.72,{brillo:1-q});
  X.fillStyle='rgba(255,255,255,.07)';X.beginPath();X.moveTo(wx,wy);X.lineTo(wx+220,wy);X.lineTo(wx,wy+420);X.closePath();X.fill();
  if(q>0){const yb=wy+wh*q;X.save();X.beginPath();X.rect(wx,wy,ww,wh*q);X.clip();X.fillStyle='#3a404a';X.fillRect(wx,wy,ww,wh);let yy=wy;for(let i=0;yy<wy+wh;i++){const hh=30+rnd(i+3)*18;X.fillStyle='rgba(0,0,0,.28)';X.fillRect(wx,yy+hh-6,ww,6);X.fillStyle='rgba(255,255,255,.05)';X.fillRect(wx,yy,ww,4);yy+=hh}X.restore();X.fillStyle='#22262f';X.fillRect(wx-6,yb-14,ww+12,22)}
  luz(L+990,640,300,'255,220,160',.25)});
 tinte(L,'0,0,10',.25*q);arriba(L,.6)}

// ---------- 12 · es una consola que no se compra: te la tienen que regalar (la maleta pasa de una mano a otra) ----------
function p12(L,t){const c=T.c12,xr=T.x_regalar,f=T.c13,mv=eio(seg(t,c+.2,xr-.1)),tom=eio(seg(t,xr-.3,xr+.05)),sue=eio(seg(t,xr+.1,xr+.6)),mx=L+lerp(230,560,mv),my=1340;
 plano(L,t,[[c,380,1130,1.2],[xr,590,1130,1.2],[f,640,1130,1.28]],cm=>{estudioO(L,{yp:1560});X.save();X.globalAlpha=.5;X.fillStyle='#3a404a';X.fillRect(L+330,640,420,560);for(let i=0;i<12;i++){X.fillStyle='rgba(0,0,0,.3)';X.fillRect(L+330,640+i*47+rnd(i)*8,420,6)}X.restore();luz(L+300,1100,620,TQ,.12);luz(L+860,1100,620,MG,.12);
  maletaF(mx,my,.7,{lazo:1,brillo:1});mano(mx-40-sue*340,my-262,.08,1.15,1,{curl:[.8,.84,.88,.9],pulgar:.3});mano(mx+40+(1-tom)*480,my-262,-.08,1.15,-1,{curl:[lerp(.3,.8,tom),lerp(.34,.84,tom),lerp(.38,.88,tom),lerp(.4,.9,tom)],pulgar:.3})});
 arriba(L,.6)}

// ---------- 13 · CTA: la maleta cerrada sobre la mesa; el broche brilla y no se abre ----------
function p13(L,t){const c=T.c13,b=.5+.5*Math.sin((t-c)*3);
 plano(L,t,[[c,470,1190,1.14],[c+2.4,535,1010,1.02],[T.fin,540,1000,1]],cm=>{estudioO(L,{yp:1470});haz(L+430,300,L+430,1470,40,330,BL,.12);maletaF(L+430,1470,.62,{brillo:.5+.5*b});luz(L+337,1362,44,BL,.5*b)});
 cierreCanal(L,t,T.x_tell)}

[p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13].forEach((f,i)=>{NUEVOS['dc_sgtaes22_p'+String(i+1).padStart(2,'0')]=SET(f)});
})();
// ===== DC · SGTAES22 · FIN =====
</script>
