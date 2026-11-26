import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["The Pentagon confirmed this video is real. But wait until you hear the explanation. Careful, the detail at the end might surprise you.",
"In 2019, sailors on a Navy warship filmed glowing triangles flying over the ship.",
"The video leaked in 2021, and the Pentagon confirmed its own sailors shot it.",
"Online, many people were sure it showed alien craft.",
"In 2022, even a Navy intelligence official played it in front of the US Congress.",
"But here's the catch with those triangles. They weren't what they looked like. In fact, those triangles were never really triangles.",
"The shape came from the camera: light passing through night vision goggles turned into triangles.",
"Any bright point of light, seen through that setup, can show up as a triangle.",
"And the objects themselves, he said, were most likely drones.",
"Tell me if that explanation is enough for you.",
"Follow for the next case."]
V=[f.replace("2019","twenty nineteen").replace("2021","twenty twenty-one").replace("2022","twenty twenty-two") for f in F]
OF=dict(look="ejecutivo",var=71,pelo="#3e2723",camisa="#263238",corbata="#1565c0",s=1.0)
GA=dict(look="gamer",var=72,pelo="#212121",camisa="#5c6bc0",lentes=False,s=1.0)
video("R2026112501_src.json","R2026112501","THE RABBIT LOOP","THE PENTAGON CONFIRMED THIS VIDEO IS REAL 🔺👽","CONFIRMED REAL",F,V,
 marcas=[("real0",0,"^real"),("careful",0,"^careful"),("tri1",1,"^triangles"),("leaked",2,"^leaked"),("own",2,"^own"),("alien",3,"^alien"),("even",4,"^even"),("congress",4,"^congress"),("catch",5,"^catch"),("never",5,"^never"),("goggles",6,"^goggles"),("point",7,"^point"),("drones",8,"^drones")],
 escenas=[
  {"z":"marNocheV","o":{"barco":1,"mira":1,"tri":3,"rec":"REC  ·  NAVY","miraY":700},"props":[{"tipo":"neblina","x":540,"y":1150,"a":.10}]},
  {"k":"s_1","i":["#1a2340","#0b1020","#02040a"],"luz2":"160,255,170","titulo":("JULY 2019","cian"),"props":[{"tipo":"nvPantalla","x":540,"y":1640,"s":1.1},{"tipo":"neblina","y":1800,"a":.14}]},
  {"k":"s_2","i":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220","props":[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"PENTAGON STATEMENT","dato":"FILMED BY NAVY PERSONNEL","sello":"CONFIRMED","selloc":"verde","filaDato":5}]},
  {"k":"s_3","z":"cuartoGamerV","o":{"era":2026},"actores":[{**GA,"keys":[{"k":"s_3","x":420,"pose":"teclea","cara":"sorpresa"}]}],"props":[{"tipo":"rotulo","x":760,"y":1150,"s":1.0,"texto":"ALIENS?!","color":"#a5d6a7","k":"alien","flota":6}]},
  {"k":"s_4","z":"noticiasV","o":{"cintillo":"UFO HEARING · US CONGRESS"},
   "actores":[{**OF,"keys":[{"k":"s_4","x":420,"pose":"lee","cara":"neutral","objeto":"documento"},{"k":"congress","x":420,"pose":"explica","cara":"neutral"}]}]},
  {"k":"s_5","i":["#10182a","#070b14","#010205"],"luz2":"160,255,170","props":[{"tipo":"trianguloP","x":540,"y":1450,"s":1.3,"flota":6},{"tipo":"lupa","x":700,"y":1250,"s":1.6,"flota":6}]},
  {"k":"s_6","i":["#183a22","#0a1c10","#020604"],"luz2":"180,255,190","props":[{"tipo":"bokehNV","x":540,"y":1560,"s":1.0}]},
  {"k":"s_7","i":["#1a2340","#0b1020","#02040a"],"luz2":"160,255,170","props":[{"tipo":"nvPantalla","x":540,"y":1640,"s":1.1},{"tipo":"neblina","y":1800,"a":.12}]},
  {"k":"s_8","z":"investigaV","titulo":("MOST LIKELY DRONES","verde"),
   "actores":[{"look":"inventor","var":73,"lentes":True,"pelo":"#9e9e9e","camisa":"#eceff1","s":.98,"keys":[{"k":"s_8","x":360,"pose":"explica","cara":"feliz"}]}],
   "props":[{"tipo":"dron","x":720,"y":1080,"s":2.4,"k":"drones"},{"tipo":"humo","x":200,"y":1700,"s":.5,"a":.14}]}],
 emojis=[{"k":"real0","e":"👽","y":1150},{"k":"catch","e":"🤨"},{"k":"drones","e":"🛸","dur":1.2}],
 sacudidas=[{"k":"own","f":10}],hints=[{"k":0,"tipo":"general"}],gancho2=5,cierre="IS THAT ENOUGH?",
 nota="Julio 2019: personal del USS Russell grabó con visión nocturna objetos triangulares. Filtrado en 2021; el Pentágono confirmó que lo grabó personal de la Armada. 17-may-2022: audiencia en la Cámara; Scott Bray mostró el video y explicó que la forma triangular se debe a la luz que pasa por las gafas de visión nocturna y la graba una cámara; los objetos probablemente eran drones. Guion aprobado por Tao 25-nov (línea base).",
 fuentes=["https://en.wikipedia.org/wiki/Pentagon_UFO_videos","https://www.reuters.com/world/us/us-congress-holds-first-hearing-ufos-half-century-2022-05-17/"])
