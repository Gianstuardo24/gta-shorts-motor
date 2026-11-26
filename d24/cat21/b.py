import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Your cat doesn't just like that box. It needs it.",
"In 2014, researchers in the Netherlands tested cats that had just arrived at a shelter.",
"Half got a hiding box. The other half got nothing.",
"The cats with a box were less stressed, and they settled in days faster.",
"For a cat, a small closed space means safety: nothing can sneak up from behind.",
"So when yours squeezes into a box, it's choosing a safe spot to relax.",
"Tell me the weirdest place your cat has squeezed into.",
"Follow to decode your cat."]
voz=[f.replace("2014","twenty fourteen") for f in frases]
M=[["box0",0,"^box"],["needs",0,"^needs"],
["s_2014",1,None],["netherlands",1,"^netherlands"],["shelter",1,"^shelter"],
["s_half",2,None],["hiding",2,"^hiding"],["nothing",2,"^nothing"],
["s_less",3,None],["stressed",3,"^stressed"],["faster",3,"^faster"],
["s_why",4,None],["safety",4,"^safety"],["behind",4,"^behind"],
["s_so",5,None],["squeezes",5,"^squeezes"],["relax",5,"^relax"],
["s_fin",6,None],["s_cta",7,None]]
NAR=dict(look="jugadora",var=51,pelo="#5d4037",peloT="cola",camisa="#7e57c2",s=1.0)
CI=dict(look="inventor",var=52,lentes=True,pelo="#9e9e9e",camisa="#eceff1",s=0.97)
GR=dict(color="#8d8d94",color2="#d6d6dc",oscuro="#55555e",lejos="#6e6e76",ojos="#8bc34a")
NA=dict(color="#e0a060",color2="#fbe9d4",oscuro="#b06a2c",lejos="#c98a4e",ojos="#4fc3f7")
P=[{"tipo":"cajita","x":800,"y":1690,"s":2.6,"color":"#c49a6c","texto":"BOX","k":0.0,"z":1650,"fin":"s_2014"},
   gato(x=800,y=1700,k=0,dir=-1,fin="s_2014",s=0.75,z=1700),
   {"tipo":"documento","x":2250,"y":1160,"s":0.95,"sello":"2014 STUDY","selloc":"cian","k":"netherlands","cae":True,"z":1800,"fin":"s_half"},
   gato(x=2000,y=1740,k="shelter",fin="s_half",**GR),
   {"tipo":"cajita","x":2960,"y":1690,"s":2.4,"color":"#c49a6c","texto":"BOX","k":"hiding","cae":True,"z":1650,"fin":"s_less"},
   gato(x=2960,y=1700,k="hiding+0.4",fin="s_less",s=0.7,z=1700,**NA),
   gato(x=3560,y=1740,k="nothing",fin="s_less",dir=-1,**GR),
   {"tipo":"cajita","x":4600,"y":1690,"s":2.4,"color":"#c49a6c","texto":"BOX","k":"s_less","z":1650,"fin":"s_why"},
   gato(x=4600,y=1700,k="s_less",fin="s_why",s=0.7,z=1700,pose="echado",**NA),
   {"tipo":"grafico","x":4250,"y":1150,"s":1.0,"k":"stressed","z":1800,"fin":"s_why"},
   {"tipo":"cajita","x":5850,"y":1690,"s":2.6,"color":"#c49a6c","texto":"SAFE","k":"s_why","z":1650,"fin":"s_so"},
   gato(x=5850,y=1700,k="s_why",fin="s_so",s=0.75,z=1700),
   {"tipo":"cajita","x":7250,"y":1690,"s":2.6,"color":"#c49a6c","texto":"BOX","k":"s_so","z":1650},
   gato(x=6900,y=1740,k="s_so",fin="squeezes",dir=1),
   gato(x=7250,y=1700,k="squeezes",s=0.75,z=1700,pose="echado")]
A=[{**NAR,"hasta":"s_2014","keys":[{"k":0,"x":320,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"needs","x":320,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {**CI,"desde":"s_2014","hasta":"s_half","keys":[{"k":"s_2014","x":1380,"y":1700,"pose":"camina","cara":"neutral"},{"k":"s_2014+0.9","x":1650,"y":1700,"pose":"sostiene","cara":"neutral","objeto":"lupa"},{"k":"shelter","x":1650,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**CI,"desde":"s_less","hasta":"s_why","keys":[{"k":"s_less","x":4800,"y":1700,"pose":"piensa","cara":"neutral","dir":-1},{"k":"faster","x":4800,"y":1700,"pose":"celebra","cara":"feliz","dir":-1}]},
   {**NAR,"desde":"s_so","keys":[{"k":"s_so","x":6760,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"squeezes","x":6760,"y":1700,"pose":"apunta","cara":"risa"},{"k":"relax","x":6760,"y":1700,"pose":"cruzado","cara":"feliz"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_2014"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_half","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"oficina","k":"s_less"},{"x0":5200,"x1":6500,"set":"sala","k":"s_why","luz":"tenue"},{"x0":6500,"x1":7900,"set":"sala","k":"s_so"}],
 "pan":[{"k":"s_2014","x":1300,"dur":0.9},{"k":"s_half","x":2600,"dur":0.9},{"k":"s_less","x":3900,"dur":0.9},{"k":"s_why","x":5200,"dur":0.9},{"k":"s_so","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[],
 "numeros":[],
 "zoom":[{"k":0.1,"s":1.12,"x":560,"y":1550,"dur":0.6},{"k":"needs","s":1.0,"dur":0.3},{"k":"shelter","s":1.18,"x":2000,"y":1600,"dur":0.4},{"k":"s_half","s":1.0,"dur":0.3},
         {"k":"s_less","s":1.0,"dur":0.3},{"k":"stressed","s":1.15,"x":4500,"y":1450,"dur":0.4},{"k":"s_why","s":1.0,"dur":0.3},{"k":"safety","s":1.25,"x":5850,"y":1580,"dur":0.5},
         {"k":"s_so","s":1.0,"dur":0.3},{"k":"relax","s":1.2,"x":7200,"y":1580,"dur":0.5},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"needs","f":10}],
 "titulos":[{"k":0.2,"texto":"THE BOX","c":"amar","grande":True,"fin":"s_2014"},
            {"k":"s_2014","texto":"SHELTER CATS · 2014","c":"cian","fin":"s_half"},
            {"k":"s_half","texto":"BOX vs NO BOX","c":"rosa","grande":True,"fin":"s_less"},
            {"k":"s_less","texto":"LESS STRESS","c":"verde","grande":True,"fin":"s_why"},
            {"k":"s_why","texto":"WHY IT WORKS","c":"amar","fin":"s_so"},
            {"k":"s_so","texto":"A SAFE SPOT","c":"verde","fin":"s_fin"}],
 "chips":[{"k":"netherlands","texto":"UTRECHT UNIVERSITY","c":"cian","fin":"s_half"},
          {"k":"faster","texto":"SETTLED IN FASTER","c":"verde","fin":"s_why"},
          {"k":"behind","texto":"NOTHING SNEAKS UP","c":"amar","fin":"s_so"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WEIRDEST SPOT?","cierre2":"Tell us where. Comment","paises":["BOX","SINK","BAG"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
poner_sets(E,[("salaV",{"hora":"dia","sinSofa":True,"var":1,"pared":["#f3e2c7","#e0c9a4"]}),("labV",{"pantalla":"SHELTER STUDY","pantalla2":"2014"}),("refugioV",{}),("labV",{"pantalla":"STRESS ▼","pantalla2":"WITH BOX"}),("dormitorioV",{"persona":False,"pared":["#5a6b8a","#3a4766"]}),("salaV",{"hora":"tarde","sinSofa":True,"var":2,"pared":["#e9d6e6","#cdb2c9"]})])
insertar(E,"needs","s_2014",1300,"vitrinaV",{"fondo":["#f6d6a8","#d99a5a","#4a2410"]},[gato(x=540,y=2100,s=3.3,dir=1)])
insertar(E,"behind","s_so",6500,"vitrinaV",{"fondo":["#2a3350","#141a2c","#05070d"],"luz2":"180,200,255"},[gato(x=540,y=1750,s=2.2,dir=-1,pose="echado")])
g={"titulo":"Your Cat Needs That Box 📦","texto_pantalla":"WHY THE BOX","lote":"K2026112402","marca":"THE CATS DECODER",
"nota_datos":"Vinke, Godijn y van der Leij (2014), Applied Animal Behaviour Science, Universidad de Utrecht: 19 gatos recién llegados a un refugio holandés; 10 con caja para esconderse y 9 sin caja. Los con caja tuvieron puntajes de estrés (Cat-Stress-Score) significativamente más bajos en los primeros días y se adaptaron más rápido; el grupo sin caja tardó ~2 semanas en igualar. Esconderse es una conducta de afrontamiento del gato ante el estrés. La frase sobre 'nada se acerca por detrás' es la explicación conductual habitual (espacio cerrado = refugio).",
"frases":frases,"frases_voz":voz,"fuentes":["https://doi.org/10.1016/j.applanim.2014.09.002","https://www.uu.nl/"],"escena":E}
guardar("K2026112402_src.json",g)
