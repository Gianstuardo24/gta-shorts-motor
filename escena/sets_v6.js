UTILERIA.fotoOvni=(x,y,s,t,o)=>{o=o||{};X.save();X.translate(x,y);X.scale(s,s);X.rotate(.03);X.fillStyle='rgba(0,0,0,.4)';X.fillRect(-250,-290,520,600);X.fillStyle='#f6f2e8';X.fillRect(-270,-310,540,620);X.fillStyle='#05070d';X.fillRect(-240,-280,480,480);
 X.fillStyle='rgba(255,255,255,.05)';for(let i=0;i<300;i++)X.fillRect(-240+rnd(i)*480,-280+rnd(i*3)*480,2,2);X.fillStyle='#000';X.beginPath();X.moveTo(0,-140);X.lineTo(170,90);X.lineTo(-170,90);X.closePath();X.fill();
 [[-140,70],[140,70],[0,-110]].forEach(([a,b])=>glow('#fff',30,()=>{X.fillStyle='#fff';X.beginPath();X.arc(a,b,16,0,7);X.fill()}));glow('#ff1744',30,()=>{X.fillStyle='#ff5252';X.beginPath();X.arc(0,30,13,0,7);X.fill()});
 txt(o.texto||'APRIL 1990',0,255,34,'#333',{w:700});X.restore()};
