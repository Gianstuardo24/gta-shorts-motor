// ===== tanda 5: ojo de gato en corte (tapetum lucidum) y ojos que brillan =====
UTILERIA.ojoGato=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);
 const R=300;X.fillStyle=gl(-R,0,R,0,[[0,'#f3e6d6'],[.5,'#fff8ee'],[1,'#e8d6c0']]);X.beginPath();X.arc(0,0,R,0,7);X.fill();X.strokeStyle='#d8bfa0';X.lineWidth=6;X.stroke();
 X.save();X.beginPath();X.arc(0,0,R-18,0,7);X.clip();X.fillStyle='#1a0f14';X.fillRect(-R,-R,2*R,2*R);
 // retina y tapetum (capa espejo iridiscente al fondo)
 const tg=X.createLinearGradient(R*.4,-R*.8,R,R*.8);tg.addColorStop(0,'#2ee6a6');tg.addColorStop(.35,'#3ad0ff');tg.addColorStop(.7,'#b4ff4a');tg.addColorStop(1,'#2ee6a6');X.strokeStyle=tg;X.lineWidth=40;X.beginPath();X.arc(0,0,R-40,-1.1,1.1);X.stroke();
 X.strokeStyle='rgba(255,150,170,.7)';X.lineWidth=12;X.beginPath();X.arc(0,0,R-70,-1.15,1.15);X.stroke();X.restore();
 X.fillStyle='rgba(180,230,255,.35)';X.beginPath();X.ellipse(-R+10,0,60,R*.62,0,0,7);X.fill();
 X.fillStyle=gl(0,-130,0,130,[[0,'#c9a23a'],[1,'#7a8a2a']]);X.beginPath();X.ellipse(-R+70,0,22,R*.55,0,0,7);X.fill();
 X.fillStyle='rgba(230,240,255,.8)';X.beginPath();X.ellipse(-R+120,0,46,95,0,0,7);X.fill();
 // rayo de luz: entra, rebota en el tapetum y sale
 const p=(t*.45)%1,p1=Math.min(1,p*2),p2=Math.max(0,p*2-1);X.save();X.globalCompositeOperation='lighter';X.lineCap='round';
 X.strokeStyle='rgba(255,240,150,.9)';X.lineWidth=14;X.shadowColor='#fff59d';X.shadowBlur=24;X.beginPath();X.moveTo(-R-260,-40);X.lineTo(-R-260+(R*2+260-40)*p1,-40+60*p1);X.stroke();
 if(p2>0){X.strokeStyle='rgba(120,255,200,.95)';X.shadowColor='#69f0ae';X.beginPath();X.moveTo(R-40,20);X.lineTo(R-40-(R*2+260-40)*p2,20+50*p2);X.stroke()}X.restore();
 txt(o.etq||'TAPETUM LUCIDUM',40,R+70,34,'#69f0ae',{w:800,g:14,gc:'#69f0ae'});X.strokeStyle='#69f0ae';X.lineWidth=3;X.beginPath();X.moveTo(120,R+40);X.lineTo(R*.62,R*.62);X.stroke();X.restore()};
UTILERIA.ojosBrillan=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);const parp=Math.abs(Math.sin(t*.7))>.97?.15:1;
 [-150,150].forEach(dx=>{X.save();X.translate(dx,0);X.scale(1,parp);X.save();X.globalCompositeOperation='lighter';const g=X.createRadialGradient(0,0,10,0,0,260);g.addColorStop(0,`rgba(${o.c||'120,255,170'},.55)`);g.addColorStop(1,`rgba(${o.c||'120,255,170'},0)`);X.fillStyle=g;X.beginPath();X.arc(0,0,260,0,7);X.fill();X.restore();
  const eg=X.createRadialGradient(-20,-20,10,0,0,110);eg.addColorStop(0,'#f4ffb0');eg.addColorStop(.5,`rgb(${o.c||'120,255,170'})`);eg.addColorStop(1,'#1d6b3a');X.fillStyle=eg;X.beginPath();X.ellipse(0,0,110,80,0,0,7);X.fill();X.fillStyle='#050505';X.beginPath();X.ellipse(0,0,18,70,0,0,7);X.fill();X.fillStyle='rgba(255,255,255,.85)';X.beginPath();X.arc(-36,-30,14,0,7);X.fill();X.restore()});X.restore()};
