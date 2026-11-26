import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Your cat knows where you are, even when it can't see you.",
"In 2021, scientists in Japan played owners' voices to cats through speakers.",
"First, the voice came from outside the room.",
"Then, a moment later, the same voice came from inside.",
"The cats looked surprised, as if their owner had teleported.",
"That means your cat keeps a mental map of you, built from sound alone.",
"Tell me if your cat finds you in every room.",
"Follow to decode your cat."]
voz=[f.replace("2021","twenty twenty-one") for f in frases]
M=[["knows",0,"^knows"],["see",0,"^see"],
["s_2021",1,None],["japan",1,"^japan"],["voices",1,"^voices"],["speakers",1,"^speakers"],
["s_first",2,None],["outside",2,"^outside"],
["s_then",3,None],["same",3,"^same"],["inside",3,"^inside"],
["s_surp",4,None],["surprised",4,"^surprised"],["teleported",4,"^teleported"],
["s_map",5,None],["mental",5,"^mental"],["sound",5,"^sound"],
["s_fin",6,None],["s_cta",7,None]]
OW=dict(look="jugadora",var=51,pelo="#5d4037",peloT="cola",camisa="#7e57c2",s=1.0)
CI=dict(look="inventor",var=52,lentes=True,pelo="#9e9e9e",camisa="#eceff1",s=0.97)
NA=dict(color="#e0a060",color2="#fbe9d4",oscuro="#b06a2c",lejos="#c98a4e",ojos="#4fc3f7")
P=[gato(x=780,y=1740,k=0,dir=1,fin="s_2021"),
   {"tipo":"puerta","x":300,"y":1700,"s":1.1,"k":0.0,"fin":"s_2021"},
   {"tipo":"documento","x":2250,"y":1150,"s":0.95,"sello":"KYOTO 2021","selloc":"cian","k":"japan","cae":True,"z":1800,"fin":"s_first"},
   {"tipo":"monitorOnda","x":2050,"y":1640,"s":1.0,"k":"voices","fin":"s_first"},
   {"tipo":"puerta","x":2760,"y":1700,"s":1.1,"k":"s_first","fin":"s_then"},
   {"tipo":"tv","x":2800,"y":1250,"s":0.8,"k":"outside","fin":"s_then"},
   gato(x=3400,y=1740,k="s_first",dir=-1,fin="s_then",**NA),
   {"tipo":"tv","x":4900,"y":1300,"s":0.9,"k":"inside","fin":"s_surp"},
   gato(x=4350,y=1740,k="s_then",dir=-1,fin="inside",**NA),
   gato(x=4350,y=1740,k="inside",dir=1,fin="s_surp",**NA),
   gato(x=5650,y=1740,k="s_surp",dir=1,fin="s_map",s=1.0,**NA),
   gato(x=6960,y=1740,k="s_map",dir=-1)]
A=[{**CI,"desde":"s_2021","hasta":"s_first","keys":[{"k":"s_2021","x":1380,"y":1700,"pose":"camina","cara":"neutral"},{"k":"japan","x":1660,"y":1700,"pose":"sostiene","cara":"neutral","objeto":"documento"},{"k":"speakers","x":1660,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**CI,"desde":"s_surp","hasta":"s_map","keys":[{"k":"s_surp","x":6020,"y":1700,"pose":"piensa","cara":"neutral","dir":-1},{"k":"teleported","x":6020,"y":1700,"pose":"apunta","cara":"risa","dir":-1}]},
   {**OW,"desde":"s_map","keys":[{"k":"s_map","x":7700,"y":1700,"pose":"camina","cara":"feliz","dir":-1},{"k":"mental","x":7300,"y":1700,"pose":"saluda","cara":"feliz","dir":-1},{"k":"sound","x":7300,"y":1700,"pose":"cruzado","cara":"feliz","dir":-1}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_2021"},{"x0":2600,"x1":3900,"set":"sala","k":"s_first","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"sala","k":"s_then","luz":"tenue"},{"x0":5200,"x1":6500,"set":"oficina","k":"s_surp"},{"x0":6500,"x1":7900,"set":"sala","k":"s_map"}],
 "pan":[{"k":"s_2021","x":1300,"dur":0.9},{"k":"s_first","x":2600,"dur":0.9},{"k":"s_then","x":3900,"dur":0.9},{"k":"s_surp","x":5200,"dur":0.9},{"k":"s_map","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[],
 "numeros":[],
 "zoom":[{"k":0.1,"s":1.15,"x":700,"y":1580,"dur":0.6},{"k":"see","s":1.0,"dur":0.3},{"k":"s_first","s":1.0,"dur":0.3},
         {"k":"outside","s":1.12,"x":3000,"y":1450,"dur":0.4},{"k":"s_then","s":1.0,"dur":0.3},{"k":"inside","s":1.15,"x":4550,"y":1500,"dur":0.4},{"k":"s_surp","s":1.0,"dur":0.3},
         {"k":"surprised","s":1.3,"x":5650,"y":1600,"dur":0.4},{"k":"teleported","s":1.0,"dur":0.3},{"k":"s_map","s":1.0,"dur":0.3},{"k":"sound","s":1.15,"x":7120,"y":1580,"dur":0.5},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"surprised","f":12}],
 "titulos":[{"k":0.2,"texto":"IT KNOWS WHERE YOU ARE","c":"amar","fin":"s_2021"},
            {"k":"s_2021","texto":"JAPAN · 2021","c":"cian","fin":"s_first"},
            {"k":"s_first","texto":"VOICE: OUTSIDE","c":"rosa","grande":True,"fin":"s_then"},
            {"k":"s_then","texto":"VOICE: INSIDE","c":"verde","grande":True,"fin":"s_surp"},
            {"k":"s_surp","texto":"SURPRISED","c":"rojo","grande":True,"fin":"s_map"},
            {"k":"s_map","texto":"A MAP OF YOU","c":"amar","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"speakers","texto":"OWNERS' VOICES · SPEAKERS","c":"cian","fin":"s_first"},
          {"k":"teleported","texto":"\"TELEPORTED\"","c":"amar","fin":"s_map"},
          {"k":"sound","texto":"BUILT FROM SOUND","c":"verde","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS FIND YOU?","cierre2":"Yes or no? Comment","paises":["YES","NO","ALWAYS"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
poner_sets(E,[("salaV",{"hora":"noche","sinSofa":True,"var":2,"pared":["#e9d6e6","#cdb2c9"]}),("labV",{"pantalla":"VOICE TEST","pantalla2":"KYOTO"}),("salaV",{"hora":"dia","sinSofa":True,"var":1,"pared":["#f3e2c7","#e0c9a4"]}),("salaV",{"hora":"dia","sinSofa":True,"var":3,"pared":["#f3e2c7","#e0c9a4"]}),("labV",{"pantalla":"REACTION","pantalla2":"SURPRISE"}),("salaV",{"hora":"tarde","sinSofa":True,"var":2,"pared":["#e9d6e6","#cdb2c9"]})])
quitar_props(E,["tv"])
insertar(E,"see","s_2021",1300,"vitrinaV",{"fondo":["#2a3350","#141a2c","#05070d"],"luz2":"180,200,255"},[{"tipo":"ojoGato","x":540,"y":1300,"s":2.0}])
insertar(E,"teleported","s_map",6500,"vitrinaV",{"fondo":["#f6d6a8","#d99a5a","#4a2410"]},[gato(x=540,y=2100,s=3.3,dir=1)])
insertar(E,"voices","speakers",1300,"vitrinaV",{"fondo":["#1e3a5a","#0d1e30","#03080f"],"luz2":"150,210,255"},[{"tipo":"monitorOnda","x":540,"y":1650,"s":1.4}])
g={"titulo":"Your Cat Tracks You by Voice 🐱","texto_pantalla":"IT TRACKS YOUR VOICE","lote":"K2026112401","marca":"THE CATS DECODER",
"nota_datos":"Takagi et al. (2021), PLOS ONE, Universidad de Kioto: a gatos (en casa y en cat cafés) se les reprodujo la voz de su dueño por un parlante fuera de la sala y luego por otro dentro; los gatos mostraron más sorpresa cuando la voz 'se teletransportó'. Conclusión: los gatos mantienen una representación mental de dónde está su dueño a partir del sonido (cognición socio-espacial).",
"frases":frases,"frases_voz":voz,"fuentes":["https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0257611","https://www.kyoto-u.ac.jp/en"],"escena":E}
guardar("K2026112401_src.json",g)
