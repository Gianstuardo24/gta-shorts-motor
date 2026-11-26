import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Don't do this in front of your dog.",
"In 2008, scientists in London tested it with 29 dogs.",
"A stranger sat in front of each dog and did one simple thing.",
"21 of the 29 dogs copied him.",
"Then he only opened his mouth. Not one dog reacted.",
"The thing was a yawn. Your dog catches your yawns, just like people do.",
"Tell me if your dog does it too.",
"Follow to decode your dog."]
voz=[f.replace("2008","two thousand eight").replace("29 dogs","twenty-nine dogs").replace("21 of the 29","Twenty-one of the twenty-nine") for f in frases]
M=[["dont",0,"^don"],["front",0,"^front"],["dog0",0,"^dog"],
["s_2008",1,None],["london",1,"^london"],["tested",1,"^tested"],
["s_str",2,None],["sat",2,"^sat"],["simple",2,"^simple"],
["s_21",3,None],["copied",3,"^copied"],
["s_then",4,None],["mouth",4,"^mouth"],["one",4,"^one$"],["reacted",4,"^reacted"],
["s_rev",5,None],["yawn",5,"^yawn"],["catches",5,"^catches"],["people",5,"^people"],
["s_fin",6,None],["s_cta",7,None]]
OW=dict(look="jugador",var=21,pelo="#3e2723",camisa="#1e88e5",s=1.0)
CI=dict(look="inventor",var=22,lentes=True,pelo="#9e9e9e",camisa="#eceff1",s=0.97)
ST=dict(look="cliente",var=23,pelo="#6d4c41",camisa="#8e24aa",s=0.97)
W=dict(color="#f2efe9",color2="#ffffff",oscuro="#c9bfae",lejos="#e0d8ca",collar="azul")
B=dict(color="#5d4037",color2="#8d6e63",oscuro="#3e2723",lejos="#4e342e",collar="rojo")
P=[perro(x=800,y=1760,s=1.0,k=0,dir=-1,fin="s_2008"),
   {"tipo":"documento","x":2250,"y":1150,"s":0.95,"sello":"LONDON 2008","selloc":"cian","k":"london","cae":True,"z":1800,"fin":"s_str"},
   perro(x=2050,y=1760,s=0.9,k="tested",fin="s_str",dir=-1,**W),
   perro(x=3440,y=1760,s=1.0,k="s_str",fin="s_21",dir=-1,estados=[{"k":"simple+0.6","lengua":True}]),
   perro(x=4110,y=1760,s=0.8,k="s_21",fin="s_then",estados=[{"k":"copied","lengua":True}]),
   perro(x=4350,y=1765,s=0.8,k="s_21+0.2",fin="s_then",estados=[{"k":"copied","lengua":True}],**W),
   perro(x=4590,y=1760,s=0.8,k="s_21+0.4",fin="s_then",dir=-1,estados=[{"k":"copied","lengua":True}],**B),
   perro(x=6060,y=1760,s=1.0,k="s_then",fin="s_rev",dir=-1,**B),
   perro(x=7180,y=1760,s=1.0,k="s_rev",dir=-1,estados=[{"k":"yawn","lengua":True}])]
A=[{**OW,"hasta":"s_2008","keys":[{"k":0,"x":360,"y":1700,"pose":"parado","cara":"neutral"},{"k":"dont","x":360,"y":1700,"pose":"cruzado","cara":"sorpresa","fx":"brinca"},{"k":"dog0","x":360,"y":1700,"pose":"piensa","cara":"neutral"}]},
   {**CI,"desde":"s_2008","hasta":"s_str","keys":[{"k":"s_2008","x":1160,"y":1700,"a":[1660,1700],"dur":1.3,"ease":"eio","pose":"sostiene","cara":"neutral","objeto":"documento"},{"k":"tested","x":1660,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**ST,"desde":"s_str","hasta":"s_21","keys":[{"k":"s_str","x":2560,"y":1700,"a":[2980,1700],"dur":1.2,"ease":"eio","pose":"parado","cara":"neutral"},{"k":"simple","x":2980,"y":1700,"pose":"arriba","cara":"sorpresa"}]},
   {**CI,"desde":"s_21","hasta":"s_then","keys":[{"k":"s_21","x":4820,"y":1700,"pose":"piensa","cara":"neutral","dir":-1},{"k":"copied","x":4820,"y":1700,"pose":"celebra","cara":"risa","dir":-1}]},
   {**ST,"desde":"s_then","hasta":"s_rev","keys":[{"k":"s_then","x":5560,"y":1700,"pose":"parado","cara":"sorpresa"},{"k":"one","x":5560,"y":1700,"pose":"cruzado","cara":"neutral"}]},
   {**OW,"desde":"s_rev","keys":[{"k":"s_rev","x":6820,"y":1700,"pose":"arriba","cara":"sorpresa"},{"k":"catches","x":6820,"y":1700,"pose":"apunta","cara":"risa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_2008"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_str"},
          {"x0":3900,"x1":5200,"set":"calle","k":"s_21"},{"x0":5200,"x1":6500,"set":"estudio","k":"s_then"},{"x0":6500,"x1":7900,"set":"sala","k":"s_rev"}],
 "pan":[{"k":"s_2008","x":1300,"dur":0.8},{"k":"s_str","x":2600,"dur":0.8},{"k":"s_21","x":3900,"dur":0.8},{"k":"s_then","x":5200,"dur":0.8},{"k":"s_rev","x":6500,"dur":0.8}],
 "props":P,"actores":A,
 "prohibidos":[{"k":"dont","x":360,"y":1420,"r":170}],
 "burbujas":[{"k":"simple","de":2,"texto":"???","fin":"s_21","dx":120},{"k":"yawn","de":5,"texto":"YAAAWN...","fin":"s_fin","dx":150}],
 "numeros":[{"k":"s_21","n":21,"suf":" OF 29","c":"verde","etq":"DOGS COPIED HIM","fin":"copied"}],
 "zoom":[],"planos_hint":[{"k":"dog0","tipo":"objeto"},{"k":"reacted","tipo":"primer","var":23}],
 "sacudidas":[{"k":"dont","f":14},{"k":"yawn","f":14}],
 "titulos":[{"k":0.15,"texto":"DON'T","c":"rojo","grande":True,"fin":"front"},
            {"k":"s_2008","texto":"LONDON · 2008","c":"cian","fin":"s_str"},
            {"k":"s_str","texto":"ONE SIMPLE THING","c":"rosa","fin":"s_21"},
            {"k":"s_then","texto":"SAME TEST, NO TRICK","c":"amar","fin":"s_rev"},
            {"k":"yawn","texto":"A YAWN","c":"verde","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"tested","texto":"29 DOGS","c":"cian","fin":"s_str"},
          {"k":"one","texto":"0 OF 29","c":"rojo","fin":"s_rev"},
          {"k":"people","texto":"IT'S CONTAGIOUS","c":"amar","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS DO IT?","cierre2":"Yes or no? Comment","paises":["YES","NO","SOMETIMES"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
poner_sets(E,[("salaV",{"hora":"tarde","sinSofa":True,"var":3,"pared":["#f0dcc0","#d9bf9c"]}),("labV",{"pantalla":"THE TEST","pantalla2":"29 DOGS"}),("refugioV",{}),("parqueV",{"hora":"dia"}),("salaV",{"hora":"dia","sinSofa":True,"var":1,"pared":["#dfe9f0","#b9cbd8"]}),("dormitorioV",{"persona":False,"pared":["#5a6b8a","#3a4766"]})])
insertar(E,"front","s_2008",1300,"vitrinaV",{"fondo":["#2a1a0a","#160d05","#060301"],"luz2":"255,214,150"},[{"tipo":"ojosPerro","x":540,"y":1480,"s":1.35}])
insertar(E,"copied","s_then",5200,"mesaCenitalV",{"titulo":"THE TEST · RESULTS","monto":"21 / 29","firma":"copied"},[])
insertar(E,"catches","people",6500,"vitrinaV",{"fondo":["#bfe3ff","#6aa6d6","#163a5a"],"luz2":"230,245,255"},[perro(x=540,y=1900,s=2.6,dir=-1,lengua=True)])
g={"titulo":"Don't Do This in Front of Your Dog 🐶🚫","texto_pantalla":"DON'T DO THIS","lote":"D2026112403","marca":"THE DOGS DECODER",
"nota_datos":"Versión nueva (gancho que no revela; revelación al final). Joly-Mascheroni, Senju y Shepherd (2008), Biology Letters (Birkbeck, Universidad de Londres): 29 perros; un desconocido se sentó frente a cada perro y bostezó: 21 de 29 (72 %) bostezaron. En el control (solo abrir la boca) ningún perro bostezó. 'Don't do this' se paga al final: es un bostezo, inofensivo. Tipo de gancho: 8 (reto/negación).",
"frases":frases,"frases_voz":voz,"fuentes":["https://royalsocietypublishing.org/doi/10.1098/rsbl.2008.0333","https://www.bbk.ac.uk/"],"escena":E}
guardar("D2026112403_src.json",g)
