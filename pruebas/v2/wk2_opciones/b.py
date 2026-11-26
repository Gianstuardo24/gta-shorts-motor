# 27i bloque 4 · PRUEBA TÉCNICA: wk2 con v2=True y una opción distinta por plano (paneo, fundido, negro sin efecto,
# fondo base pedido, cámara fija y sin acabado). Comprueba que el constructor y el planificador escriben lo que pide cada plano.
import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Your cat secretly speaks to you. And it might explain more than you think. Careful, there might be other details you're missing.",
"Kittens meow to call their mother.",
"But adult cats rarely meow at each other. They use scent, body language, hisses and growls.",
"Cats living without people are mostly quiet.",
"The meow is something they mostly save for us.",
"Now the detail you might be missing.",
"Your cat learns which meows work on you: one for food, one for the door, one for attention.",
"Meowing at people is partly something they learn.",
"That's why the early morning meow works so well. It learned that one from you.",
"So when your cat meows at you, it's talking to you on purpose. Answer back.",
"Tell me what your cat's meow usually means.",
"Follow to decode your cat."]
P=dict(look="cliente",var=103,pelo="#4e342e",camisa="#3949ab",s=1.0)
video("K2026112502_src.json","K2026112502","THE CATS DECODER","YOUR CAT SECRETLY SPEAKS TO YOU 🤫","SECRETLY SPEAKS TO YOU",F,
 marcas=[("speaks",0,"^speaks"),("missing",0,"^missing"),("kittens",1,"^kittens"),("rarely",2,"^rarely"),("hisses",2,"^hisses"),("quiet",3,"^quiet"),("us",4,"^us"),("detail",5,"^detail"),("food",6,"^food"),("door",6,"^door"),("attention",6,"^attention"),("learn",7,"^learn"),("morning",8,"^morning"),("answer",9,"^answer")],
 escenas=[
  {"z":"cafeGatosV","props":[gato(x=380,y=1740,dir=1,color="#ff9800"),gato(x=760,y=1740,dir=-1,color="#9e9e9e"),{"tipo":"rotulo","x":540,"y":1200,"s":1.0,"texto":"...","color":"#ffffff"}]},
  {"k":"s_1","i":["#f0e2c8","#b89a6a","#2a1c0c"],"luz2":"255,240,210","pedestal":True,"props":[gato(x=440,y=1300,s=1.3,dir=1,color="#ff9800"),gato(x=660,y=1300,s=.7,dir=-1,color="#ffb74d"),{"tipo":"rotulo","x":660,"y":1000,"s":1.0,"texto":"MEW!","color":"#ffcc80","k":"kittens"}]},
  {"k":"s_2","z":"parqueV","o":{"hora":"noche"},"props":[gato(x=330,y=1740,dir=1,color="#616161"),gato(x=760,y=1740,dir=-1,color="#bcaaa4"),{"tipo":"rotulo","x":330,"y":1250,"s":.9,"texto":"HISS","color":"#ef5350","k":"hisses"},{"tipo":"rotulo","x":760,"y":1250,"s":.9,"texto":"GRR","color":"#ef5350","k":"hisses"}]},
  {"k":"s_3","z":"montanaV","transicion":"paneo","props":[gato(x=300,y=1740,dir=1,color="#795548"),gato(x=560,y=1760,s=.75,dir=-1,color="#9e9e9e"),gato(x=820,y=1740,dir=-1,color="#5d4037"),{"tipo":"rotulo","x":560,"y":1250,"s":1.0,"texto":"...","color":"#ffffff","k":"quiet"},{"tipo":"neblina","y":1750,"a":.14}]},
  {"k":"s_4","z":"salaV","transicion":"fundido","o":{"hora":"tarde","var":2,"sinSofa":True},"actores":[{**P,"keys":[{"k":"s_4","x":380,"pose":"explica","cara":"feliz"}]}],
   "props":[gato(x=760,y=1740,dir=-1,color="#ff9800"),{"tipo":"rotulo","x":760,"y":1250,"s":1.0,"texto":"MEOW","color":"#ffd54f","k":"us","flota":6},{"tipo":"lamparaPie","x":1000,"y":1640,"s":1.0,"z":1500}]},
  {"k":"s_5","i":["#2a1d3a","#140c1f","#040208"],"luz2":"230,200,255","pedestal":True,"props":[gato(x=540,y=1300,s=1.6,dir=-1,color="#ff9800"),{"tipo":"lupa","x":760,"y":1080,"s":1.4,"flota":6}]},
  {"k":"s_6","i":["#e9dcc8","#a88b66","#24180c"],"luz2":"255,240,210","props":[{"tipo":"puerta","x":270,"y":1700,"s":.8},gato(x=760,y=1720,s=1.2,dir=-1,color="#ff9800"),{"tipo":"cajita","x":560,"y":1720,"s":1.3,"color":"#ffcc80","texto":"FOOD","k":"food","cae":True},{"tipo":"rotulo","x":270,"y":1180,"s":1.0,"texto":"DOOR","color":"#90caf9","k":"door"},{"tipo":"rotulo","x":760,"y":1120,"s":1.0,"texto":"ATTENTION","color":"#f48fb1","k":"attention"}]},
  {"k":"s_7","z":"cocinaV","transicion":"negro","efecto_corte":"ninguno","actores":[{**P,"keys":[{"k":"s_7","x":360,"pose":"ofrece","cara":"feliz","objeto":"cajita"}]}],"props":[gato(x=760,y=1740,dir=-1,color="#ff9800"),{"tipo":"rotulo","x":760,"y":1250,"s":1.0,"texto":"MEOW","color":"#ffd54f","flota":6}]},
  {"k":"s_8","z":"dormitorioV","entorno":"base","o":{"persona":True,"zzz":True,"pared":["#3a4766","#252d47"]},"props":[gato(x=780,y=1740,dir=-1,color="#ff9800"),{"tipo":"rotulo","x":780,"y":1250,"s":1.0,"texto":"MEOW!","color":"#ffd54f","k":"morning","flota":8}]},
  {"k":"s_9","z":"salaV","camara":"fija","acabado":"ninguno","o":{"hora":"noche","var":3,"sinSofa":True},"actores":[{**P,"keys":[{"k":"s_9","x":360,"pose":"explica","cara":"risa"}]}],"props":[gato(x=760,y=1740,dir=-1,color="#ff9800"),{"tipo":"lamparaPie","x":1000,"y":1640,"s":1.0,"z":1500}]}],
 emojis=[{"k":"speaks","e":"🤫"},{"k":"detail","e":"👀","y":600},{"k":"morning","e":"⏰"},{"k":"answer","e":"🐱","dur":1.2}],
 gancho2=5,cierre="WHAT DOES IT MEAN?",cierre2="Tell me. Comment",paises=["FOOD","DOOR","LOVE"],
 nota="Gatitos maúllan a la madre; adultos casi no se maúllan entre sí; gatos ferales maúllan poco (Behavioural Processes, citado por Live Science); el maullido a humanos es en parte aprendido (Bradshaw). Guion aprobado por Tao 25-nov (línea base).",
 fuentes=["https://www.livescience.com/why-cats-meow.html","https://en.wikipedia.org/wiki/Cat_communication","https://phys.org/news/2024-07-cats-meow-humans.html"], v2=True)
