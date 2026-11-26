import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Don't throw away that box. Your cat might need it.",
"In 2014, researchers in the Netherlands studied cats that had just arrived at a shelter.",
"Half of them got a box to hide in. The other half got nothing.",
"The cats with a box were less stressed in their first days.",
"Now the part about the cats without one.",
"They took about two weeks to catch up.",
"So if your cat is new or stressed, give it a box to hide in.",
"Tell me the weirdest place your cat has squeezed into.",
"Follow to decode your cat."]
V=[f.replace("2014","twenty fourteen") for f in F]
P=dict(look="cliente",var=85,pelo="#c49a6c",camisa="#8e24aa",s=1.0)
video("K2026112501_src.json","K2026112501","THE CATS DECODER","Don't Throw Away That Box 📦🚫","DON'T THROW AWAY THAT BOX",F,V,
 marcas=[("throw",0,"^throw"),("need",0,"^need"),("shelter",1,"^shelter"),("half",2,"^half"),("nothing",2,"^nothing"),("less",3,"^less"),("without",4,"^without"),("weeks",5,"^weeks"),("give",6,"^give")],
 escenas=[
  {"i":["#3a2a1a","#1c140c","#050302"],"luz2":"255,225,180","pedestal":True,"props":[{"tipo":"cajaGato","x":540,"y":1300,"s":1.4,"k":0.3,"color":"#ff9800"},{"tipo":"neblina","y":1700,"a":.12}]},
  {"k":"s_1","z":"refugioV","titulo":("NETHERLANDS, 2014","cian"),"actores":[{"look":"inventor","var":86,"lentes":True,"pelo":"#5d4037","camisa":"#eceff1","s":.98,"keys":[{"k":"s_1","x":360,"pose":"lee","cara":"neutral","objeto":"documento"}]}],
   "props":[gato(x=780,y=1740,dir=-1,color="#9e9e9e")]},
  {"k":"s_2","i":["#e9dcc8","#a88b66","#24180c"],"luz2":"255,240,210","props":[{"tipo":"cajaGato","x":310,"y":1680,"s":.95,"k":"half","color":"#ff9800"},gato(x=790,y=1700,s=1.2,dir=-1,color="#9e9e9e"),
    {"tipo":"rotulo","x":310,"y":1200,"s":1.0,"texto":"BOX","color":"#66bb6a","k":"half"},{"tipo":"rotulo","x":790,"y":1200,"s":1.0,"texto":"NO BOX","color":"#ef5350","k":"nothing"}]},
  {"k":"s_3","z":"salaV","o":{"hora":"tarde","var":1,"sinSofa":True},"actores":[{**P,"keys":[{"k":"s_3","x":330,"pose":"explica","cara":"feliz"}]}],
   "props":[{"tipo":"cajaGato","x":760,"y":1760,"s":.9,"color":"#ff9800"},{"tipo":"lamparaPie","x":1000,"y":1640,"s":1.0,"z":1500}]},
  {"k":"s_4","z":"dormitorioV","o":{"persona":False,"pared":["#3a4766","#252d47"]},"props":[gato(x=540,y=1760,s=1.1,dir=-1,color="#9e9e9e")]},
  {"k":"s_5","i":["#16243f","#0b1222","#020408"],"luz2":"190,210,255","pedestal":True,"props":[{"tipo":"calendario","x":540,"y":1300,"s":1.7,"mes":"TO CATCH UP","anio":"DAYS","dia":14,"color":"#ef5350"}]},
  {"k":"s_6","z":"cocinaV","actores":[{**P,"keys":[{"k":"s_6","x":360,"pose":"ofrece","cara":"feliz","objeto":"cajita"}]}],"props":[{"tipo":"cajaGato","x":780,"y":1760,"s":.9,"k":"give","color":"#9e9e9e"}]}],
 prohibidos=[{"k":"throw","x":540,"y":1130,"r":230,"ins":1}],sacudidas=[{"k":"throw","f":12}],
 emojis=[{"k":"need","e":"🐱"},{"k":"without","e":"😿"},{"k":"give","e":"📦","dur":1.2}],
 gancho2=4,cierre="DOES YOURS LOVE BOXES?",paises=["YES","NO","ALWAYS"],
 nota="Vinke, Godijn y van der Leij (2014), Applied Animal Behaviour Science, Universidad de Utrecht: 19 gatos recién llegados a un refugio holandés; 10 con caja para esconderse y 9 sin caja. Los con caja tuvieron puntajes de estrés significativamente más bajos los primeros días; el grupo sin caja tardó cerca de 2 semanas en igualar (día 14). Esconderse es conducta de afrontamiento. Solución = recomendación del propio estudio para refugios. Disparador: prohibición. Gancho tipo 8.",
 fuentes=["https://doi.org/10.1016/j.applanim.2014.09.002","https://www.uu.nl/"])
