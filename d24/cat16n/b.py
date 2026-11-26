import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Your cat has a GPS on you. Let me show you how it works.",
"In 2021, scientists in Japan left cats alone in a room.",
"A speaker outside played their owner's voice.",
"A moment later, the same voice came from inside the room.",
"The cats looked startled, as if their owner had teleported.",
"That means your cat keeps a map of where you are, using only sound.",
"And here is the strange part.",
"It did not work with random noises, or with other cats. Only with the voice they know.",
"Tell me if your cat finds you in every room.",
"Follow to decode your cat."]
voz=[f.replace("2021","twenty twenty-one").replace("GPS","G P S") for f in frases]
M=[["gps",0,"^gps"],["show",0,"^show"],
["s_2021",1,None],["japan",1,"^japan"],["alone",1,"^alone"],
["s_out",2,None],["outside",2,"^outside"],["voice2",2,"^voice"],
["s_in",3,None],["same",3,"^same"],["inside",3,"^inside"],
["s_st",4,None],["startled",4,"^startled"],["teleported",4,"^teleported"],
["s_map",5,None],["map",5,"^map"],["sound",5,"^sound"],
["s_part",6,None],["strange",6,"^strange"],
["s_only",7,None],["noises",7,"^noises"],["only",7,"^only"],["know",7,"^know"],
["s_fin",8,None],["s_cta",9,None]]
OW=dict(look="jugadora",var=51,pelo="#5d4037",peloT="cola",camisa="#7e57c2",s=1.0)
CI=dict(look="inventor",var=52,lentes=True,pelo="#9e9e9e",camisa="#eceff1",s=0.97)
NA=dict(color="#e0a060",color2="#fbe9d4",oscuro="#b06a2c",lejos="#c98a4e",ojos="#4fc3f7")
NE=dict(color="#2b2b2b",color2="#5a5a5a",oscuro="#111111",lejos="#3a3a3a",ojos="#ffd54f")
BL=dict(color="#f2e6d4",color2="#ffffff",oscuro="#b08968",lejos="#d9c7ad",ojos="#4fc3f7")
P=[gato(x=330,y=1740,k=0,dir=1,fin="s_2021"),
   {"tipo":"senal","x":330,"y":1500,"s":1.0,"k":"gps","fin":"s_2021"},
   {"tipo":"pinGPS","x":760,"y":1290,"s":0.8,"k":"gps","fin":"s_2021"},
   {"tipo":"documento","x":2250,"y":1150,"s":0.95,"sello":"KYOTO 2021","selloc":"cian","k":"japan","cae":True,"z":1800,"fin":"s_out"},
   gato(x=2060,y=1740,k="alone",dir=-1,fin="s_out",**NA),
   {"tipo":"monitorOnda","x":2790,"y":1640,"s":0.9,"k":"outside","fin":"s_in"},
   {"tipo":"cartel","x":2820,"y":1330,"s":0.9,"texto":"OUTSIDE","k":"outside","cae":True,"z":1800,"fin":"s_in"},
   gato(x=3250,y=1740,k="s_out",dir=-1,fin="inside",**NA),
   gato(x=3250,y=1740,k="inside",dir=1,fin="s_map",**NA),
   {"tipo":"monitorOnda","x":3640,"y":1640,"s":0.9,"k":"inside","fin":"s_map"},
   {"tipo":"cartel","x":3600,"y":1330,"s":0.9,"texto":"INSIDE","k":"inside","cae":True,"z":1800,"fin":"s_map"},
   gato(x=4230,y=1740,k="s_map",dir=1,fin="s_part"),
   {"tipo":"senal","x":4230,"y":1500,"s":1.0,"k":"map","fin":"s_part"},
   {"tipo":"pinGPS","x":4520,"y":1290,"s":0.8,"k":"map","fin":"s_part","mov":[{"k":"map","x":4520,"y":1290},{"k":"sound","x":4860,"y":1290}]},
   gato(x=5560,y=1740,k="s_part",dir=1,s=0.8,**NE),
   gato(x=5860,y=1740,k="s_part",dir=-1,s=0.8,**BL),
   gato(x=6130,y=1740,k="s_part",dir=-1,**NA),
   {"tipo":"senal","x":6130,"y":1500,"s":1.0,"k":"only"}]
A=[{**OW,"hasta":"s_2021","keys":[{"k":0,"x":760,"y":1700,"pose":"telefono","cara":"feliz","dir":-1},{"k":"gps","x":760,"y":1700,"pose":"piensa","cara":"sorpresa","dir":-1}]},
   {**CI,"desde":"s_2021","hasta":"s_out","keys":[{"k":"s_2021","x":1160,"y":1700,"a":[1660,1700],"dur":1.3,"ease":"eio","pose":"sostiene","cara":"neutral","objeto":"documento"},{"k":"alone","x":1660,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**OW,"desde":"s_map","hasta":"s_part","keys":[{"k":"s_map","x":4520,"y":1700,"pose":"parado","cara":"feliz","dir":-1},{"k":"map","x":4520,"y":1700,"a":[4860,1700],"dur":1.6,"ease":"eio","pose":"saluda","cara":"feliz"}]},
   {**OW,"desde":"only","keys":[{"k":"only","x":6560,"y":1700,"a":[5330,1700],"dur":0.01,"pose":"saluda","cara":"feliz"},{"k":"know","x":5330,"y":1700,"pose":"saluda","cara":"risa"}]}]
A[3]["keys"]=[{"k":"only","x":5330,"y":1700,"pose":"saluda","cara":"feliz"},{"k":"know","x":5330,"y":1700,"pose":"celebra","cara":"risa"}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_2021"},{"x0":2600,"x1":3900,"set":"sala","k":"s_out"},
          {"x0":3900,"x1":5200,"set":"sala","k":"s_map"},{"x0":5200,"x1":6600,"set":"cafe","k":"s_part"}],
 "pan":[{"k":"s_2021","x":1300,"dur":0.8},{"k":"s_out","x":2600,"dur":0.8},{"k":"s_map","x":3900,"dur":0.8},{"k":"s_part","x":5200,"dur":0.8}],
 "props":P,"actores":A,
 "burbujas":[],
 "numeros":[],
 "zoom":[],"planos_hint":[{"k":"gps","tipo":"objeto"}],
 "sacudidas":[{"k":"gps","f":12},{"k":"startled","f":14},{"k":"only","f":10}],
 "titulos":[{"k":0.15,"texto":"GPS ON YOU","c":"rojo","grande":True,"fin":"show"},
            {"k":"s_2021","texto":"1 · THE TEST","c":"cian","fin":"s_out"},
            {"k":"s_out","texto":"2 · VOICE OUTSIDE","c":"rosa","fin":"s_in"},
            {"k":"s_in","texto":"3 · SAME VOICE, INSIDE","c":"verde","fin":"startled"},
            {"k":"s_map","texto":"4 · A MAP OF YOU","c":"amar","fin":"s_part"},
            {"k":"s_part","texto":"5 · THE STRANGE PART","c":"rojo","fin":"only"},
            {"k":"only","texto":"ONLY YOUR VOICE","c":"verde","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"japan","texto":"KYOTO UNIVERSITY","c":"cian","fin":"s_out"},
          {"k":"sound","texto":"USING ONLY SOUND","c":"amar","fin":"s_part"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS FIND YOU?","cierre2":"Yes or no? Comment","paises":["YES","NO","ALWAYS"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
poner_sets(E,[("salaV",{"hora":"noche","sinSofa":True,"var":2,"pared":["#e9d6e6","#cdb2c9"]}),("labV",{"pantalla":"VOICE TEST","pantalla2":"KYOTO"}),("cocinaV",{}),("dormitorioV",{"persona":False,"pared":["#5a6b8a","#3a4766"]}),("cafeGatosV",{})])
insertar(E,"show","s_2021",1300,"vitrinaV",{"fondo":["#12301e","#0a1c12","#030806"],"luz2":"150,255,190"},[{"tipo":"pinGPS","x":540,"y":1560,"s":2.6},{"tipo":"senal","x":540,"y":1120,"s":1.8}])
insertar(E,"voice2","s_in",2600,"vitrinaV",{"fondo":["#1e3a5a","#0d1e30","#03080f"],"luz2":"150,210,255"},[{"tipo":"monitorOnda","x":540,"y":1650,"s":1.4}])
insertar(E,"startled","s_map",3900,"vitrinaV",{"fondo":["#f6d6a8","#d99a5a","#4a2410"]},[gato(x=540,y=2100,s=3.3,dir=1,**NA)])
insertar(E,"noises","only",5200,"vitrinaV",{"fondo":["#3a0d0d","#1c0606","#080202"],"luz2":"255,150,150"},[{"tipo":"monitorOnda","x":360,"y":1640,"s":1.1},gato(x=760,y=1740,s=1.5,dir=-1,**NE)])
g={"titulo":"Your Cat Has a GPS on You 📍🐱","texto_pantalla":"GPS ON YOU","lote":"K2026112403","marca":"THE CATS DECODER",
"nota_datos":"Formato nuevo (24-nov). Takagi et al. (2021), PLOS ONE, Universidad de Kioto: con el gato solo en una sala, se reprodujo la voz de su dueño por un parlante fuera y luego por otro dentro; los gatos mostraron sorpresa ('teletransporte'). Conclusión: mantienen una representación mental de dónde está su dueño a partir del sonido. En los experimentos 2 y 3 (maullidos de otros gatos y sonidos no vocales) no apareció el mismo efecto. 'GPS' es metáfora del título; el video la explica. Disparador: sentirse observado.",
"frases":frases,"frases_voz":voz,"fuentes":["https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0257611","https://www.kyoto-u.ac.jp/en"],"escena":E}
guardar("K2026112403_src.json",g)
