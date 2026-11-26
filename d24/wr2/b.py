import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["A newspaper invented flying saucers. Not a pilot, not a witness.",
"In June 1947, pilot Kenneth Arnold saw nine shiny objects near Mount Rainier.",
"He compared the way they moved to a saucer skipping across water.",
"But the papers ran it as flying saucers, and the name stuck.",
"Now watch what one headline did.",
"Within weeks, hundreds of people across the country reported flying saucers.",
"And Arnold later drew his objects thin and crescent shaped. So the classic saucer started as a headline.",
"Tell me if you knew where the name came from.",
"Follow for the next case."]
V=[f.replace("1947","nineteen forty-seven") for f in F]
P=dict(look="piloto",var=91,s=1.0)
video("R2026112502_src.json","R2026112502","THE RABBIT LOOP","A Newspaper Invented Flying Saucers 🛸📰","A NEWSPAPER INVENTED THEM",F,V,
 marcas=[("witness",0,"^witness"),("nine",1,"^nine"),("skipping",2,"^skipping"),("stuck",3,"^stuck"),("headline",4,"^headline"),("hundreds",5,"^hundreds"),("crescent",6,"^crescent")],
 escenas=[
  {"i":["#1d1a14","#0e0c08","#020201"],"luz2":"255,236,190","props":[{"tipo":"periodico","x":540,"y":1780,"s":1.25,"titular":"FLYING SAUCERS!","sub":"PILOT SEES NINE OBJECTS","fecha":"JUNE 1947"},{"tipo":"humo","x":200,"y":1800,"s":.6,"a":.14}]},
  {"k":"s_1","z":"montanaV","o":{"objetos":1,"avion":1},"titulo":("JUNE 24 1947","cian")},
  {"k":"s_2","i":["#2f6aa8","#173a63","#06121f"],"luz2":"200,230,255","props":[{"tipo":"rebota","x":540,"y":1450,"s":1.0,"texto":"HOW THEY MOVED"}]},
  {"k":"s_3","z":"noticiasV","o":{"cintillo":"FLYING SAUCERS SIGHTED"},"actores":[{"look":"ejecutivo","var":92,"camisa":"#4e342e","corbata":"#b71c1c","s":1.0,"keys":[{"k":"s_3","x":420,"pose":"lee","cara":"sorpresa","objeto":"documento"}]}]},
  {"k":"s_4","i":["#1d1a14","#0e0c08","#020201"],"luz2":"255,236,190","props":[{"tipo":"periodico","x":540,"y":1720,"s":1.1,"titular":"SAUCERS EVERYWHERE","sub":"HUNDREDS OF REPORTS","fecha":"JULY 1947","k":"s_4"}]},
  {"k":"s_5","z":"nocheV","o":{"ciudad":True,"sem":33},"actores":[{"look":"cliente","var":93,"s":1.0,"keys":[{"k":"s_5","x":300,"pose":"apunta","cara":"sorpresa"}]},{"look":"jugadora","var":94,"s":1.0,"keys":[{"k":"s_5","x":760,"pose":"telefono","cara":"sorpresa"}]}],
   "props":[{"tipo":"ovni","x":640,"y":700,"s":.6,"flota":10}]},
  {"k":"s_6","i":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220","props":[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"ARNOLD'S SKETCH","dato":"THIN · CRESCENT SHAPED","sello":"NOT A SAUCER","selloc":"rojo","filaDato":5}]}],
 emojis=[{"k":"witness","e":"🛸"},{"k":"headline","e":"📰","y":620},{"k":"hundreds","e":"😱","dur":1.2}],
 hints=[{"k":"s_5","tipo":"general"}],gancho2=4,cierre="DID YOU KNOW?",
 nota="24-jun-1947: Kenneth Arnold, piloto civil, vio nueve objetos brillantes cerca del monte Rainier. Comparó su movimiento con un platillo que rebota en el agua (según él mismo después; algunas citas iniciales también comparan la forma). El término 'flying saucer' lo acuñó la prensa de EE.UU. Para el 4 de julio había cientos de reportes. Arnold dibujó los objetos delgados y en forma de media luna. La escena 2 queda solo con el nombre y el movimiento: el dibujo del salto del platillo va en el inserto (bote con piedra = plato rebotando). Fuentes: Wikipedia (Kenneth Arnold UFO sighting; Flying saucer), TIME, Space.com, History.com.",
 fuentes=["https://en.wikipedia.org/wiki/Kenneth_Arnold_UFO_sighting","https://en.wikipedia.org/wiki/Flying_saucer","https://time.com/3930602/first-reported-ufo","https://www.space.com/12066-flying-saucers-turn-64-ufos-origins.html"])
