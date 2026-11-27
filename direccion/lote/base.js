<script>
// ===== DC · BASE DEL LOTE (27-nov) · ayudantes compartidos por los videos del lote. Inerte: solo define window.DC. =====
// Copiados sin cambios del bloque de MDM (aprobado), que no se toca. No dibuja logos ni marcas.
(function(){
const LIN='rgba(40,27,18,.92)';
const K=k=>tk(k,window.__A||0);
function cap(x1,y1,x2,y2,r){const a=Math.atan2(y2-y1,x2-x1);X.beginPath();X.arc(x1,y1,r,a+Math.PI/2,a+Math.PI*1.5);X.arc(x2,y2,r,a-Math.PI/2,a+Math.PI/2);X.closePath()}
function trazo(c,w){X.strokeStyle=c;X.lineWidth=w;X.stroke()}
function vineta(L,f){const v=X.createRadialGradient(L+540,1080,520,L+540,1080,1320);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,`rgba(8,5,3,${f})`);X.fillStyle=v;X.fillRect(L-300,-400,1680,3000)}
function dedo(x,y,ang,l1,l2,r,curl,col,una,graf){l1*=1-.5*Math.min(1,curl);l2*=1-.38*Math.min(1,curl);const a1=ang+curl*1.25,a2=a1+curl*1.45,x1=x+Math.cos(a1)*l1,y1=y+Math.sin(a1)*l1,x2=x1+Math.cos(a2)*l2,y2=y1+Math.sin(a2)*l2;
 X.fillStyle=col;cap(x,y,x1,y1,r);X.fill();trazo(LIN,2.4);cap(x1,y1,x2,y2,r*.92);X.fill();trazo(LIN,2.4);X.beginPath();X.arc(x1,y1,r*.8,0,7);X.fill();
 if(graf){X.fillStyle='rgba(70,70,78,.55)';X.beginPath();X.ellipse(x1+Math.cos(a2)*l2*.45,y1+Math.sin(a2)*l2*.45,r*.55,r*.95,a2,0,7);X.fill()}
 if(una){const nx=Math.sin(a2),ny=-Math.cos(a2);X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(x2-Math.cos(a2)*r*.25+nx*r*.42,y2-Math.sin(a2)*r*.25+ny*r*.42,r*.62,r*.34,a2,0,7);X.fill()}
 return [x2,y2,a2]}
function manoLado(x,y,ang,s,dir,o){o=o||{};const parte=o.parte||'todo';X.save();X.translate(x,y);X.rotate(ang);X.scale(s*dir,s);X.lineJoin='round';X.lineCap='round';
 const sk=o.piel||'#e8b28c',sk2=o.piel2||'#cf9670',c=o.curl||[0,0,0,0];let p=null;
 if(parte!=='pulgar'){
  X.fillStyle=o.manga||'#27365a';X.beginPath();X.moveTo(-900,-64);X.lineTo(-54,-46);X.lineTo(-54,46);X.lineTo(-900,84);X.closePath();X.fill();trazo(LIN,3);
  X.strokeStyle='rgba(0,0,0,.18)';X.lineWidth=3;X.beginPath();X.moveTo(-860,30);X.lineTo(-90,22);X.stroke();
  X.fillStyle=o.puno||'#f1ede4';rr(-86,-53,64,106,12);X.fill();trazo(LIN,3);
  if(o.boton){X.fillStyle=o.boton;X.beginPath();X.arc(-54,22,7,0,7);X.fill();trazo(LIN,2)}
  X.fillStyle=sk;X.beginPath();X.moveTo(-26,-35);X.lineTo(10,-39);X.lineTo(10,38);X.lineTo(-26,35);X.closePath();X.fill();
  dedo(98,26,.14,44,36,12,c[3],sk2);dedo(104,14,.09,56,44,13.5,c[2],sk2);dedo(108,1,.04,62,50,15,c[1],sk2);
  X.fillStyle=gl(0,-50,0,52,[[0,sk],[.62,sk],[1,sk2]]);X.beginPath();X.moveTo(-24,-37);X.quadraticCurveTo(46,-53,108,-33);X.quadraticCurveTo(129,-4,112,32);X.quadraticCurveTo(56,52,-24,37);X.closePath();X.fill();trazo(LIN,2.4);
  X.strokeStyle='rgba(120,70,45,.35)';X.lineWidth=2;X.beginPath();X.arc(94,-22,10,3.5,5.3);X.stroke();
  if(o.entre)o.entre();
  p=dedo(106,-17,-.03,66,52,15,c[0],sk,true,o.graf)}
 if(parte!=='atras')dedo(34,30,o.pulgar===undefined?.5:o.pulgar,52,40,15,o.pulgarCurl===undefined?.08:o.pulgarCurl,sk,true);
 X.restore();return p}
function origen(px,py,ang,s,dir,lx,ly){const c=Math.cos(ang),n=Math.sin(ang);return [px-s*(dir*lx*c-ly*n),py-s*(dir*lx*n+ly*c)]}
function manoArriba(tx,ty,s,o){o=o||{};const esp=o.esp||1;X.save();X.translate(tx,ty);X.rotate(o.rot||0);X.scale(s*esp,s);X.lineJoin='round';X.lineCap='round';
 const sk=o.piel||'#e8b28c',sk2='#cf9670';
 // manga y puño (entra desde abajo)
 X.save();X.translate(228,236);X.rotate(1.02);X.fillStyle=o.manga||'#efe6d6';X.beginPath();X.moveTo(40,-92);X.lineTo(1500,-150);X.lineTo(1500,150);X.lineTo(40,92);X.closePath();X.fill();trazo(LIN,3);
 X.fillStyle=o.puno||'#0e8f8a';rr(-22,-100,90,200,16);X.fill();trazo(LIN,3);if(o.boton){X.fillStyle=o.boton;X.beginPath();X.arc(24,62,10,0,7);X.fill();trazo(LIN,2)}X.restore();
 // dedos de abajo (anular y meñique recogidos)
 X.fillStyle=sk2;cap(168,150,128,166,17);X.fill();trazo(LIN,3);cap(152,124,112,134,18);X.fill();trazo(LIN,3);
 // dedo medio (apoya el lápiz)
 X.fillStyle=sk2;cap(136,96,82,72,18);X.fill();trazo(LIN,3);cap(82,72,36,42,16);X.fill();trazo(LIN,3);X.beginPath();X.arc(82,72,13,0,7);X.fill();
 // dorso
 X.fillStyle=sk;X.beginPath();X.moveTo(112,46);X.quadraticCurveTo(160,44,196,88);X.quadraticCurveTo(232,140,222,206);X.quadraticCurveTo(206,250,160,244);X.quadraticCurveTo(110,236,98,180);X.quadraticCurveTo(86,110,112,46);X.closePath();X.fill();trazo(LIN,3);
 X.strokeStyle='rgba(120,70,45,.3)';X.lineWidth=2;[[132,66],[156,84],[176,108]].forEach(q=>{X.beginPath();X.arc(q[0],q[1],9,3.9,5.6);X.stroke()});
 // lápiz
 if(!o.sinLapiz){const ux=.8,uy=.6;X.save();X.rotate(Math.atan2(uy,ux));X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(0,0);X.lineTo(34,-9);X.lineTo(34,9);X.closePath();X.fill();trazo(LIN,2);X.fillStyle='#3a3a40';X.beginPath();X.moveTo(0,0);X.lineTo(11,-3);X.lineTo(11,3);X.closePath();X.fill();
  X.fillStyle='#b8382c';X.fillRect(34,-9,250,18);X.fillStyle='rgba(255,255,255,.22)';X.fillRect(34,-6,250,4);X.strokeStyle=LIN;X.lineWidth=2;X.strokeRect(34,-9,250,18);X.fillStyle='#c9c4b8';X.fillRect(284,-9,20,18);X.strokeRect(284,-9,20,18);X.fillStyle='#d98a86';rr(304,-9,22,18,5);X.fill();X.stroke();X.restore()}
 // índice y pulgar (encima del lápiz)
 X.fillStyle=sk;cap(128,70,88,36,18);X.fill();trazo(LIN,3);cap(88,36,52,20,16);X.fill();trazo(LIN,3);X.beginPath();X.arc(88,36,13,0,7);X.fill();
 if(o.graf){X.fillStyle='rgba(70,70,78,.5)';X.beginPath();X.ellipse(72,30,16,8,.42,0,7);X.fill()}
 X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(56,19,9,6,.42,0,7);X.fill();
 X.fillStyle=sk;cap(122,166,74,112,19);X.fill();trazo(LIN,3);cap(74,112,42,52,17);X.fill();trazo(LIN,3);X.beginPath();X.arc(74,112,14,0,7);X.fill();
 X.fillStyle='rgba(255,236,222,.8)';X.beginPath();X.ellipse(44,60,7,10,-.5,0,7);X.fill();
 X.restore()}
function mezcla(A,B,u){return {o:[lerp(A.o[0],B.o[0],u),lerp(A.o[1],B.o[1],u)],a:lerp(A.a,B.a,u),c:A.c.map((v,i)=>lerp(v,B.c[i],u)),p:lerp(A.p,B.p,u),pc:lerp(A.pc,B.pc,u)}}
function cam(L,cx,cy,s,ax,ay,fn,rot){X.save();X.translate(L+ax,ay);if(rot)X.rotate(rot);X.scale(s,s);X.translate(-(L+cx),-cy);fn();X.restore()}
function penumbra(L,y1,y0){y0=y0||330;X.fillStyle='rgba(14,8,4,.985)';X.fillRect(L-300,-400,1680,y0+402);const g=X.createLinearGradient(0,y0,0,y1);g.addColorStop(0,'rgba(14,8,4,.985)');g.addColorStop(.42,'rgba(14,8,4,.6)');g.addColorStop(1,'rgba(14,8,4,0)');X.fillStyle=g;X.fillRect(L-300,y0,1680,y1-y0)}
function lapizSuelto(tx,ty,s,rot){X.save();X.translate(tx,ty);X.rotate(rot||0);X.scale(s,s);X.lineJoin='round';X.rotate(Math.atan2(.6,.8));
 X.fillStyle='rgba(40,24,10,.22)';X.fillRect(30,6,290,12);
 X.fillStyle='#e9d2a8';X.beginPath();X.moveTo(0,0);X.lineTo(34,-9);X.lineTo(34,9);X.closePath();X.fill();trazo(LIN,2);X.fillStyle='#3a3a40';X.beginPath();X.moveTo(0,0);X.lineTo(11,-3);X.lineTo(11,3);X.closePath();X.fill();
 X.fillStyle='#b8382c';X.fillRect(34,-9,250,18);X.fillStyle='rgba(255,255,255,.22)';X.fillRect(34,-6,250,4);X.strokeStyle=LIN;X.lineWidth=2;X.strokeRect(34,-9,250,18);X.fillStyle='#c9c4b8';X.fillRect(284,-9,20,18);X.strokeRect(284,-9,20,18);X.fillStyle='#d98a86';rr(304,-9,22,18,5);X.fill();X.stroke();X.restore()}
// Cierre del canal (como en MDM, aprobado por Tao el 27-nov): pregunta, comentar, opciones, LIKE y FOLLOW del motor, sin sus haces de luz.
// k: momento en que empieza la línea del CTA. La mitad de arriba se oscurece para que se lean.
function cierreCanal(L,t,k){const co=eio(seg(t,k-.25,k+.35));
 if(co>0){const g=X.createLinearGradient(0,-400,0,1010);g.addColorStop(0,'rgba(14,8,4,'+(.7*co)+')');g.addColorStop(.9,'rgba(14,8,4,'+(.7*co)+')');g.addColorStop(1,'rgba(14,8,4,0)');X.fillStyle=g;X.fillRect(L-300,-400,1680,1410)}
 if(t>k-.6&&typeof cierre==='function'){const sf=T.s_fin,hz=window.haz;T.s_fin=k-.75;window.haz=function(){};X.save();X.translate(L,0);try{cierre(t)}finally{X.restore();T.s_fin=sf;window.haz=hz}}}
const SET=f=>({osc:.1,luces(){return []},fondo(z,t,q){f(FV(z).L,t)}});
window.DC={LIN,K,cap,trazo,vineta,dedo,manoLado,origen,manoArriba,mezcla,cam,penumbra,lapizSuelto,cierreCanal,SET};
})();
</script>
