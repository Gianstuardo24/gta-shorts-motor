<script>
// ===== DC · RABBIT22 · INICIO ===== (Rabbit 22h · Don't TRUST the Flying Saucer Story · paquete 9 del lote del 27-nov)
// Regla del paquete: antes del dibujo final no aparece ningún platillo volador físico. Lo de Arnold son destellos y trayectorias; el "platillo" es papel impreso.
(function(){
const {LIN,K,cap,trazo,manoLado,manoArriba,origen,cam,cierreCanal,SET}=window.DC;
const golpe=(t,k,d)=>{const u=(t-k)/d;return u<0||u>1?0:Math.sin(u*Math.PI)};
function ruta(t,kf){if(t<=kf[0][0])return kf[0].slice(1);for(let i=1;i<kf.length;i++)if(t<=kf[i][0]){const u=eio(seg(t,kf[i-1][0],kf[i][0]));return kf[i].slice(1).map((v,j)=>lerp(kf[i-1][j+1],v,u))}return kf[kf.length-1].slice(1)}
const PAPEL='#efe6d0',TINTA='#2a2019',PLATO='#3f7fe0',MANO={manga:'#6b4a2e',puno:'#55391f',piel:'#e8b28c'};
function cielo(L,c0,c1,y1){const g=X.createLinearGradient(0,-200,0,y1||1400);g.addColorStop(0,c0);g.addColorStop(1,c1);X.fillStyle=g;X.fillRect(L-1600,-1700,5400,6600)}
function destello(x,y,r,a){if(a<=0)return;X.save();X.globalAlpha=Math.min(1,a);X.fillStyle='rgba(255,246,201,.25)';X.beginPath();X.arc(x,y,r*1.5,0,7);X.fill();X.fillStyle='#fff6c9';X.beginPath();X.moveTo(x-r*2.2,y);X.quadraticCurveTo(x,y-r*.22,x+r*2.2,y);X.quadraticCurveTo(x,y+r*.22,x-r*2.2,y);X.moveTo(x,y-r*1.6);X.quadraticCurveTo(x-r*.2,y,x,y+r*1.6);X.quadraticCurveTo(x+r*.2,y,x,y-r*1.6);X.fill();X.fillStyle='#fff';X.beginPath();X.arc(x,y,r*.34,0,7);X.fill();X.restore()}
// la trayectoria "a saltos": cuatro arcos que tocan una misma línea
const Y0=1150,W=300,X0=-60,salto=x=>Y0-250*Math.abs(Math.sin((x-X0)/W*Math.PI));
function punteada(L,x1,a){X.fillStyle=`rgba(255,246,201,${a})`;for(let x=X0+10;x<x1;x+=26){X.beginPath();X.arc(L+x,salto(x),7,0,7);X.fill()}}
function montes(L,dx){X.fillStyle='#22324f';X.beginPath();X.moveTo(L-400+dx,1260);[[-200,1040],[-40,1120],[150,820],[330,1090],[520,1010],[640,1100],[860,640],[1080,1060],[1260,980],[1500,1260]].forEach(p=>X.lineTo(L+p[0]+dx,p[1]));X.closePath();X.fill();
 X.fillStyle='#e3ecf5';[[150,820,70,150],[860,640,130,240]].forEach(q=>{X.beginPath();X.moveTo(L+q[0]+dx,q[1]);X.lineTo(L+q[0]+dx-q[2],q[1]+q[3]);X.lineTo(L+q[0]+dx-q[2]*.4,q[1]+q[3]*.72);X.lineTo(L+q[0]+dx,q[1]+q[3]*.95);X.lineTo(L+q[0]+dx+q[2]*.45,q[1]+q[3]*.7);X.lineTo(L+q[0]+dx+q[2],q[1]+q[3]);X.closePath();X.fill()});
 X.fillStyle='#1a2740';X.fillRect(L-1600,1250,5400,3000)}
function nubes(L,t,y,a){X.fillStyle=`rgba(255,255,255,${a})`;for(let i=0;i<6;i++){const x=L+((i*420+rnd(i)*200-t*(30+i*6))%2400+2400)%2400-600,yy=y+rnd(i+9)*260;X.beginPath();X.ellipse(x,yy,150+rnd(i+3)*90,26,0,0,7);X.ellipse(x+80,yy-18,90,22,0,0,7);X.fill()}}
// ---------- P01 · desde la cabina: nueve destellos cruzan de pico a pico ----------
function reloj(x,y,r,u){X.fillStyle='#0d1015';X.beginPath();X.arc(x,y,r*1.14,0,7);X.fill();X.fillStyle='#e9e2d2';X.beginPath();X.arc(x,y,r,0,7);X.fill();X.strokeStyle=TINTA;X.lineCap='round';for(let i=0;i<12;i++){const q=i*Math.PI/6;X.lineWidth=i%3?3:6;X.beginPath();X.moveTo(x+Math.cos(q)*r*.78,y+Math.sin(q)*r*.78);X.lineTo(x+Math.cos(q)*r*.9,y+Math.sin(q)*r*.9);X.stroke()}
 const a=-Math.PI/2+u*Math.PI*2;X.strokeStyle='#c0392b';X.lineWidth=r*.07;X.beginPath();X.moveTo(x,y);X.lineTo(x+Math.cos(a)*r*.72,y+Math.sin(a)*r*.72);X.stroke();X.fillStyle=TINTA;X.beginPath();X.arc(x,y,r*.09,0,7);X.fill();X.fillStyle='#8e98a4';rr(x-r*.14,y-r*1.36,r*.28,r*.26,r*.06);X.fill()}
function cabina(L,t,u,o){const g='#11151b';X.fillStyle=g;X.fillRect(L-300,-400,1700,830);X.beginPath();X.moveTo(L-300,430);X.quadraticCurveTo(L+540,330,L+1380,430);X.lineTo(L+1380,300);X.lineTo(L-300,300);X.closePath();X.fill();
 X.fillRect(L-300,300,150,1100);X.fillRect(L+1010,300,400,1100);X.beginPath();X.moveTo(L+500,360);X.lineTo(L+560,360);X.lineTo(L+548,1300);X.lineTo(L+520,1300);X.closePath();X.fill();
 X.fillStyle='#1a2029';X.beginPath();X.moveTo(L-300,1290);X.quadraticCurveTo(L+540,1200,L+1380,1290);X.lineTo(L+1380,2400);X.lineTo(L-300,2400);X.closePath();X.fill();X.strokeStyle='rgba(255,255,255,.08)';X.lineWidth=6;X.beginPath();X.moveTo(L-300,1290);X.quadraticCurveTo(L+540,1200,L+1380,1290);X.stroke();
 [[190,1530,96],[850,1560,84],[540,1760,70]].forEach((q,i)=>{X.fillStyle='#0d1015';X.beginPath();X.arc(L+q[0],q[1],q[2]*1.12,0,7);X.fill();X.fillStyle='#2a323d';X.beginPath();X.arc(L+q[0],q[1],q[2],0,7);X.fill();X.strokeStyle='#e9e2d2';X.lineWidth=5;X.lineCap='round';const a=-2+Math.sin(t*(.8+i*.3)+i)*.25+i;X.beginPath();X.moveTo(L+q[0],q[1]);X.lineTo(L+q[0]+Math.cos(a)*q[2]*.7,q[1]+Math.sin(a)*q[2]*.7);X.stroke()});
 reloj(L+520,1480,120,u);
 // libreta con lápiz y, en la línea 2, la fecha
 X.save();X.translate(L+850,1335);X.rotate(-.08);X.fillStyle=PAPEL;X.fillRect(-120,-40,240,150);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-120,-40,240,150);if(o.fecha>0){txt('JUNE',0,2,40,TINTA,{w:220,a:o.fecha});txt('1947',0,58,60,TINTA,{w:220,a:o.fecha})}X.restore();
 X.save();X.translate(L+250+Math.sin(t*1.3)*14,1318);X.rotate(.05+Math.sin(t*1.3)*.03);X.fillStyle='#e9b949';X.fillRect(-110,-9,200,18);X.strokeStyle=LIN;X.lineWidth=2;X.strokeRect(-110,-9,200,18);X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(90,-9);X.lineTo(122,0);X.lineTo(90,9);X.closePath();X.fill();X.stroke();X.restore()}
function p01(L,t){const x2=T.c01b,xn=T.x_nine,fin=T.c02a,xf=T.x_few;
 const tr=Math.sin(t*37)*1.6,base=lerp(.02,1.06,seg(t,.2,fin)),u=seg(t,xf+.15,fin);
 const z=lerp(1,1.1,eio(seg(t,0,fin)));
 cam(L,540,880,z,540+tr,880,()=>{cielo(L,'#1c2b4a','#6c86ad',1250);nubes(L,t,520,.10);montes(L,0);nubes(L,t+40,900,.08);
  for(let i=0;i<9;i++){const q=base-i*.05;if(q>0&&q<1.04){const x=L+lerp(130,1010,q),y=760-70*Math.sin(q*Math.PI)+24*Math.sin(q*16+i),br=.55+.45*Math.sin(t*9+i*1.9)+1.2*golpe(t,xn+i*.07,.3);destello(x,y,(14+7*q)*(1+.4*golpe(t,xn+i*.07,.3)),Math.min(1,br+.2)*seg(q,0,.04))}}});
 cabina(L,t,u,{fecha:eio(seg(t,x2+.15,x2+.6))});
 const p=eio(seg(t,xf-.4,xf+.1))*(1-eio(seg(t,xf+.3,xf+.9)));if(p>0){const hx=L+520+40,hy=1480-130-20+(1-p)*500,o=origen(hx+(1-p)*300,hy,-1.25,1.2,-1,150,20);manoLado(o[0],o[1],-1.25,1.2,-1,Object.assign({},MANO,{curl:[.2,.5,.55,.6],pulgar:.5}))}}
// ---------- P02a · rápidos: las estelas; la trayectoria queda como línea punteada ----------
function avion(x,y,s){X.save();X.translate(x,y);X.scale(s,s);X.fillStyle='#0f1622';X.beginPath();X.ellipse(0,0,90,16,0,0,7);X.fill();X.beginPath();X.moveTo(-20,0);X.lineTo(10,-70);X.lineTo(34,-70);X.lineTo(30,0);X.closePath();X.fill();X.beginPath();X.moveTo(-84,-4);X.lineTo(-96,-40);X.lineTo(-78,-40);X.lineTo(-62,-4);X.closePath();X.fill();X.fillRect(88,-22,6,44);X.restore()}
function p02a(L,t){const c=T.c02a,xf=T.x_faster,fin=T.c02b,congela=eio(seg(t,fin-.75,fin-.3));
 cielo(L,'#1c2b4a','#6c86ad',1500);nubes(L,t,700,.10);X.fillStyle='#1a2740';X.fillRect(L-400,1500,1900,900);
 avion(L+lerp(-150,330,seg(t,c,fin)),1320,.9);
 [0,1].forEach(p=>{const k=c+.1+p*1.25,q=seg(t,k,k+1.0);if(q>0&&q<1)for(let i=0;i<9;i++){const x=lerp(-300,1500,q)-i*46,y=salto(x);X.strokeStyle='rgba(255,246,201,.35)';X.lineWidth=7;X.lineCap='round';X.beginPath();for(let j=0;j<=8;j++){const xx=x-j*22;j?X.lineTo(L+xx,salto(xx)):X.moveTo(L+xx,salto(xx))}X.stroke();destello(L+x,y,11,1)}});
 punteada(L,X0+10+congela*1300,congela)}
// ---------- P02b · como un platillo de cocina que rebota en el agua ----------
function platillo(x,y,s,rot){X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(0,10,112,22,0,0,7);X.fill();X.fillStyle=PLATO;X.beginPath();X.ellipse(0,0,110,22,0,0,7);X.fill();trazo(LIN,3);X.fillStyle='#f4f1e8';X.beginPath();X.ellipse(0,-5,92,14,0,0,7);X.fill();X.fillStyle=PLATO;X.beginPath();X.ellipse(0,-4,54,8,0,0,7);X.fill();
 X.fillStyle='#16304d';X.beginPath();X.moveTo(78,-16);X.lineTo(96,-9);X.lineTo(86,-2);X.closePath();X.fill();X.restore()}
function lago(L,t){cielo(L,'#33507a','#9db7d4',1150);X.fillStyle='#22324f';X.beginPath();X.moveTo(L-400,1150);[[-100,1040],[200,1090],[480,1010],[800,1080],[1100,1030],[1500,1150]].forEach(p=>X.lineTo(L+p[0],p[1]));X.closePath();X.fill();
 const g=X.createLinearGradient(0,1150,0,1920);g.addColorStop(0,'#2c6a8c');g.addColorStop(1,'#16405a');X.fillStyle=g;X.fillRect(L-400,1150,1900,1400);X.strokeStyle='rgba(255,255,255,.10)';X.lineWidth=4;for(let i=0;i<9;i++){const y=1190+i*i*8+i*30;X.beginPath();for(let x=-400;x<1500;x+=40)X.lineTo(L+x,y+Math.sin(x*.02+t*1.5+i)*4);X.stroke()}}
function p02b(L,t){const c=T.c02b,xs=T.x_saucer,fin=T.c03,q=seg(t,xs-.25,fin-.1),x=lerp(X0+10,X0+10+1260,q),a=1-seg(t,fin-.5,fin);
 lago(L,t);punteada(L,1300,.9);
 for(let i=1;i<=4;i++){const xc=X0+i*W,tc=xs-.25+(fin-.1-(xs-.25))*((xc-X0-10)/1260),u=seg(t,tc,tc+.9);if(u>0&&u<1){X.strokeStyle=`rgba(255,255,255,${(1-u)*.7})`;X.lineWidth=5;[1,.6].forEach(m=>{X.beginPath();X.ellipse(L+xc,Y0+6,(30+150*u)*m,(8+34*u)*m,0,0,7);X.stroke()});for(let j=0;j<5;j++){X.fillStyle=`rgba(255,255,255,${(1-u)*.8})`;X.beginPath();X.arc(L+xc+(j-2)*26*u*2,Y0-60*Math.sin(u*3.14)*(1+.3*(j%2)),7,0,7);X.fill()}}}
 if(q>0)platillo(L+x,salto(x)-18,1.25,Math.sin(q*40)*.12)}
// ---------- P03 · desde arriba: el platillo se hunde y quedan las ondas ----------
function p03(L,t){const c=T.c03,xn=T.x_not,fin=T.c04a;
 const g=X.createRadialGradient(L+540,1000,100,L+540,1000,1300);g.addColorStop(0,'#2c6a8c');g.addColorStop(1,'#123347');X.fillStyle=g;X.fillRect(L-400,-500,1900,2900);
 X.strokeStyle='rgba(255,255,255,.05)';X.lineWidth=4;for(let i=0;i<16;i++){X.beginPath();for(let x=-400;x<1500;x+=40)X.lineTo(L+x,300+i*110+Math.sin(x*.02+t*1.2+i)*6);X.stroke()}
 const P=[[190,1420],[400,1180],[620,950],[840,720]],ap=1-eio(seg(t,xn+.5,fin));
 P.forEach((p,i)=>{for(let k=0;k<3;k++){const u=((t*.45+k/3+i*.13)%1);X.strokeStyle=`rgba(255,255,255,${(1-u)*.55*ap*(i===3?1:.8)})`;X.lineWidth=6-3*u;X.beginPath();X.arc(L+p[0],p[1],30+170*u,0,7);X.stroke()}});
 const h=eio(seg(t,xn-.1,xn+.7));if(h<1){X.save();X.globalAlpha=1-h*.95;X.translate(L+840,720);X.scale(1-.45*h,1-.45*h);X.rotate(.4+h);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.arc(8,12,150,0,7);X.fill();X.fillStyle=PLATO;X.beginPath();X.arc(0,0,150,0,7);X.fill();trazo(LIN,3);X.fillStyle='#f4f1e8';X.beginPath();X.arc(0,0,122,0,7);X.fill();X.fillStyle=PLATO;X.beginPath();X.arc(0,0,74,0,7);X.fill();X.fillStyle='#1d5d7d';X.beginPath();X.moveTo(150,-16);X.lineTo(122,0);X.lineTo(150,22);X.closePath();X.fill();
  X.fillStyle=`rgba(18,51,71,${h*.8})`;X.beginPath();X.arc(0,0,154,0,7);X.fill();X.restore()}}
// ---------- P04 · el teletipo escribe SAUCER; la prensa lo vuelve titular ----------
function lineasGrises(x,y,w,n,alto,sem){X.fillStyle='rgba(42,32,25,.28)';for(let i=0;i<n;i++)rr(x,y+i*alto*1.9,w*(.72+rnd(i+sem)*.28),alto,alto/2),X.fill()}
function p04a(L,t){const c=T.c04a,fin=T.c04b,sub=lerp(0,160,seg(t,c,fin));
 X.fillStyle='#15202c';X.fillRect(L-400,-500,1900,2900);X.fillStyle='#232f3d';X.fillRect(L-400,-500,1900,960);X.fillStyle='#0d141c';rr(L+150,400,780,70,20);X.fill();
 X.fillStyle='rgba(0,0,0,.3)';X.fillRect(L+252,440,600,1700);X.fillStyle=PAPEL;X.fillRect(L+240,440,600,1700);X.save();X.beginPath();X.rect(L+240,470,600,1700);X.clip();X.translate(0,sub);
 lineasGrises(L+290,520,500,5,22,3);lineasGrises(L+290,1100,500,7,22,11);
 const n=Math.floor(seg(t,c+.25,c+1.05)*6.99),lev=eio(seg(t,fin-.55,fin-.05));
 X.save();X.translate(L+540,900);X.translate(0,-lev*60);X.rotate(lev*.06);X.scale(1+lev*.08,1+lev*.08);if(lev>0){X.fillStyle='rgba(0,0,0,.25)';X.fillRect(-222,-62+lev*40,460,150);X.fillStyle='#f7f0dc';X.fillRect(-230,-76,460,150);X.setLineDash([14,10]);X.strokeStyle=TINTA;X.lineWidth=3;X.strokeRect(-230,-76,460,150);X.setLineDash([])}
 'SAUCER'.split('').forEach((ch,i)=>{if(i<n)txt(ch,-175+i*70,4,104,TINTA,{w:80})});if(n<6&&((t*6)%1<.5)){X.fillStyle=TINTA;X.fillRect(-175+n*70-26,40,52,8)}X.restore();X.restore();
 X.fillStyle='#0d141c';X.fillRect(L+150,400,780,56)}
function diario(x,y,s,rot,o){o=o||{};X.save();X.translate(x,y);X.rotate(rot||0);X.scale(s,s);X.fillStyle='rgba(0,0,0,.28)';X.fillRect(-382,-512,780,1050);X.fillStyle=PAPEL;X.fillRect(-390,-525,780,1050);X.strokeStyle=LIN;X.lineWidth=3;X.strokeRect(-390,-525,780,1050);
 X.fillStyle='rgba(42,32,25,.5)';X.fillRect(-340,-480,680,54);X.fillStyle=TINTA;X.fillRect(-340,-410,680,6);
 if(o.titular>0){X.globalAlpha=o.titular;txt('FLYING',0,-310,150,TINTA,{w:690});txt('SAUCERS',0,-160,150,TINTA,{w:690});X.globalAlpha=1}X.fillStyle=TINTA;X.fillRect(-340,-70,680,5);
 [-340,-106,128].forEach((cx,i)=>lineasGrises(cx,-30,212,12,17,i*7+2));X.fillStyle='rgba(42,32,25,.2)';X.fillRect(-106,330,446,150);X.restore()}
function p04b(L,t){const c=T.c04b,xs=T.x_stuck,baja=eio(seg(t,c+.02,c+.16)),sube=eio(seg(t,c+.3,c+.6)),imp=Math.exp(-Math.max(0,t-c-.16)*9)*(t>c+.16?1:0);
 X.fillStyle='#15202c';X.fillRect(L-400,-500,1900,2900);
 for(let i=3;i>=1;i--){const q=eio(seg(t,xs-.3+i*.12,xs+.1+i*.12));if(q>0)diario(L+540+q*i*46,1080+q*i*40+Math.sin(imp*30)*imp*6,1,q*i*.05,{titular:1})}
 diario(L+540,1080+Math.sin(imp*30)*imp*8,1,0,{titular:t>c+.16?1:0});
 const py=lerp(-900,1080,baja)-sube*1500;if(py>-800){X.fillStyle='rgba(0,0,0,.3)';X.fillRect(L+110,py-560,880,1130);X.fillStyle='#3a4552';X.fillRect(L+100,py-580,880,1130);X.fillStyle='#566473';X.fillRect(L+100,py-580,880,60);X.fillStyle='#232c36';X.fillRect(L+440,py-1900,200,1340)}}
// ---------- P05 · un titular en cada porche: sobre los techos suben círculos de papel ----------
function discoPapel(x,y,r,o){o=o||{};X.save();X.translate(x,y);X.rotate(o.rot||0);X.scale(o.sx===undefined?1:o.sx,1);X.beginPath();const n=o.simple?16:44;for(let i=0;i<n;i++){const a=i/n*Math.PI*2,rr_=r*(1+(o.simple?0:(rnd(i+(o.sem||0))-.5)*.07));i?X.lineTo(Math.cos(a)*rr_,Math.sin(a)*rr_):X.moveTo(Math.cos(a)*rr_,Math.sin(a)*rr_)}X.closePath();
 X.fillStyle=PAPEL;X.fill();if(!o.simple){X.strokeStyle='rgba(42,32,25,.5)';X.lineWidth=3;X.stroke()}X.save();X.clip();
 if(o.simple){X.fillStyle='rgba(42,32,25,.3)';X.fillRect(-r*.6,-r*.2,r*1.2,r*.16);X.fillRect(-r*.5,r*.12,r*1.0,r*.12)}
 else{txt('SAUCERS',0,-r*.08,r*.42,TINTA,{w:r*2.4});X.fillStyle=TINTA;X.fillRect(-r,r*.16,r*2,r*.02);[-1,0,1].forEach((c,i)=>lineasGrises(c*r*.62-r*.28,r*.26,r*.56,7,r*.045,i*5+1));lineasGrises(-r*.7,-r*.86,r*1.4,4,r*.05,9);X.fillStyle='rgba(0,0,0,.08)';X.fillRect(r*.3,-r,r,2*r)}
 X.restore();X.restore()}
function casa(x,yb,s,luz){X.save();X.translate(x,yb);X.scale(s,s);X.fillStyle='#1b2338';X.fillRect(-150,-230,300,230);X.beginPath();X.moveTo(-178,-226);X.lineTo(0,-360);X.lineTo(178,-226);X.closePath();X.fillStyle='#121a2b';X.fill();
 X.fillStyle=luz?'#f6c66a':'#2a3550';X.fillRect(-112,-180,62,70);X.fillRect(50,-180,62,70);X.fillStyle='#0f1626';X.fillRect(-30,-120,60,120);X.fillStyle='#232d47';X.fillRect(-90,-8,180,16);X.fillRect(-70,8,140,14);X.fillStyle='#121a2b';X.fillRect(-96,-150,192,14);X.fillRect(-88,-140,8,134);X.fillRect(80,-140,8,134);X.restore()}
const CASAS=[[230,1700,1.5,0],[820,1740,1.6,.55],[120,1330,.92,1.1],[520,1310,.9,1.5],[900,1340,.95,1.9],[60,1090,.55,2.4],[290,1080,.54,2.7],[520,1075,.52,3.0],[750,1082,.54,3.3],[980,1090,.55,3.6]];
function p05(L,t){const c=T.c05,xo=T.x_one,xw=T.x_within,fin=T.c06;
 const cm=ruta(t,[[c,540,1240,1.22],[xw-.2,540,1200,1.12],[fin,540,1000,1]]);
 cam(L,cm[0],cm[1],cm[2],540,1000,()=>{cielo(L,'#1a1f3d','#b5654a',1120);X.fillStyle='#fbe0a0';X.globalAlpha=.25;X.beginPath();X.arc(L+540,1130,300,Math.PI,0);X.fill();X.globalAlpha=1;
  X.fillStyle='#141b2e';X.fillRect(L-900,1090,2900,2000);X.fillStyle='#1b2540';X.fillRect(L-900,1345,2900,2000);X.fillStyle='#222e4d';X.fillRect(L-900,1745,2900,2000);
  // discos lejanos, que se van sumando
  const lej=seg(t,xw+.6,fin);for(let i=0;i<34;i++){const k=i/34;if(k<lej){const q=back(seg(lej,k,k+.08));X.save();X.globalAlpha=.9;discoPapel(L+60+rnd(i)*980,640+rnd(i+40)*330-30*seg(lej,k,1),(14+rnd(i+80)*22)*q,{simple:true});X.restore()}}
  CASAS.slice().reverse().forEach((h,j)=>{const i=CASAS.length-1-j,k=i<2?xo-.2+i*.7:xw-.3+h[3]*.75-.6,llega=seg(t,k,k+.45),sube=eio(seg(t,k+.4,k+1.5));
   if(sube>0)discoPapel(L+h[0],h[1]-360*h[2]-(40+140*sube)*h[2],90*h[2]*Math.min(1,sube*2.5),{sem:i*13,rot:Math.sin(t*1.2+i)*.06,simple:h[2]<.7});
   casa(L+h[0],h[1],h[2],llega>=1);
   if(llega>0){const u=Math.min(1,llega),px=L+h[0]+lerp(400,40,u)*h[2],py=h[1]-8*h[2]-Math.sin(u*Math.PI)*260*h[2];X.save();X.translate(px,py);X.rotate((1-u)*5);X.fillStyle=PAPEL;X.fillRect(-34*h[2],-10*h[2],68*h[2],20*h[2]);X.fillStyle='rgba(42,32,25,.5)';X.fillRect(-26*h[2],-4*h[2],52*h[2],4*h[2]);X.restore()}})})}
// ---------- P06 · de cerca: el "platillo" es papel impreso, con el borde rasgado ----------
function p06(L,t){const c=T.c06,xs=T.x_shape,xn=T.x_notone,fin=T.c07;
 const g=ruta(t,[[xs-.25,1],[xs+.25,.06],[xs+.75,1],[xn,1],[xn+.3,.5],[xn+.7,1]])[0];
 cielo(L,'#1a1f3d','#b5654a',2200);for(let i=0;i<10;i++)discoPapel(L+80+rnd(i)*940,480+rnd(i+30)*1200,16+rnd(i+60)*20,{simple:true});
 X.fillStyle='rgba(0,0,0,.2)';X.beginPath();X.ellipse(L+560,1090,340*g,340,0,0,7);X.fill();
 discoPapel(L+540,1060+Math.sin(t*1.4)*14,lerp(300,345,seg(t,c,fin)),{sx:g,rot:Math.sin(t*.9)*.05,sem:5})}
// ---------- P07 · el dibujo de Arnold: plano, curvo adelante y en punta atrás; el círculo sobra ----------
function medialuna(){X.beginPath();X.moveTo(-240,70);X.quadraticCurveTo(0,-270,240,70);X.quadraticCurveTo(130,-50,0,44);X.quadraticCurveTo(-130,-50,-240,70);X.closePath()}
const PTS=(()=>{const P=[],q=(a,b,c,n)=>{for(let i=0;i<=n;i++){const u=i/n;P.push([(1-u)*(1-u)*a[0]+2*u*(1-u)*b[0]+u*u*c[0],(1-u)*(1-u)*a[1]+2*u*(1-u)*b[1]+u*u*c[1]])}};q([-240,70],[0,-270],[240,70],40);q([240,70],[130,-50],[0,44],22);q([0,44],[-130,-50],[-240,70],22);return P})();
function p07(L,t){const c=T.c07,xa=T.x_something,xb=T.x_boom,xn=T.x_notround,xs=T.x_so11,xh=T.x_headline11,xq=T.x_not11,k=T.x_tell;
 const u=seg(t,xa-.1,xb+.2),cae=eio(seg(t,xn-.05,xn+.8)),n=Math.floor(u*(PTS.length-1));
 const cm=ruta(t,[[c,540,1000,1.08,540,1000],[xn,540,1000,1.12,540,1000],[xs+.9,700,880,.82,540,1000],[xq,560,1000,1.05,540,1000],[k+.5,540,1000,.9,430,1290]]);
 cam(L,cm[0],cm[1],cm[2],cm[3],cm[4],()=>{X.fillStyle='#2b2030';X.fillRect(L-1200,-1500,4200,5200);X.fillStyle='rgba(255,255,255,.03)';for(let i=0;i<14;i++)X.fillRect(L-1200,-600+i*230,4200,70);
  diario(L+1180,560,.62,.12,{titular:1});
  // el círculo de papel: al final se desprende y se va
  X.save();X.translate(L+540-cae*820,1000+cae*520);X.rotate(-cae*.9);X.fillStyle='rgba(0,0,0,.25)';X.beginPath();X.arc(10,14,344,0,7);X.fill();discoPapel(0,0,340,{sem:5});X.fillStyle='#2b2030';X.globalAlpha=cae>0?1:0;medialuna();X.fill();X.globalAlpha=1;X.restore();
  // la forma que dibujó: queda sobre la mesa
  X.save();X.translate(L+540,1000);if(cae>0){X.fillStyle='rgba(0,0,0,.25)';X.save();X.translate(8,12);medialuna();X.fill();X.restore();X.fillStyle='#f7f0dc';medialuna();X.fill()}
  X.strokeStyle='#3a3a40';X.lineWidth=9;X.lineCap='round';X.lineJoin='round';X.beginPath();for(let i=0;i<=n;i++){i?X.lineTo(PTS[i][0],PTS[i][1]):X.moveTo(PTS[i][0],PTS[i][1])}if(u>=1)X.closePath();X.stroke();X.restore();
  const en=eio(seg(t,c+.1,xa-.1)),va=eio(seg(t,xb+.25,xb+.55)),toca=golpe(t,xq+.5,.35)+golpe(t,xq+1.0,.35);
  if(va<1){const p=PTS[n];manoArriba(L+540+p[0]+(1-en)*700+va*800,1000+p[1]+(1-en)*600+va*700,1.25,{manga:MANO.manga,puno:MANO.puno,graf:true})}
  else if(t>xq-.2){const e2=eio(seg(t,xq-.2,xq+.4))*(1-eio(seg(t,xq+1.5,xq+2.1)));manoArriba(L+560+(1-e2)*900,1040-toca*26+(1-e2)*700,1.25,{manga:MANO.manga,puno:MANO.puno,graf:true})}});
 cierreCanal(L,t,k)}

NUEVOS.dc_rabbit22_p01=SET(p01);NUEVOS.dc_rabbit22_p02a=SET(p02a);NUEVOS.dc_rabbit22_p02b=SET(p02b);NUEVOS.dc_rabbit22_p03=SET(p03);NUEVOS.dc_rabbit22_p04a=SET(p04a);NUEVOS.dc_rabbit22_p04b=SET(p04b);
NUEVOS.dc_rabbit22_p05=SET(p05);NUEVOS.dc_rabbit22_p06=SET(p06);NUEVOS.dc_rabbit22_p07=SET(p07);
})();
// ===== DC · RABBIT22 · FIN =====
</script>
