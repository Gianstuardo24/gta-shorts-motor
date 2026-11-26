import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Your dog can smell when you are stressed.",
"In 2022, scientists in Belfast collected sweat and breath from 36 people.",
"First while they were calm. Then right after a hard math problem.",
"Four dogs had to pick the stressed sample.",
"They got it right in almost 94 percent of the tests.",
"So when your dog stays close on a bad day, it may have smelled it first.",
"Tell me if your dog notices your bad days.",
"Follow to decode your dog."]
voz=[f.replace("2022","twenty twenty-two").replace("36 people","thirty-six people").replace("94 percent","ninety-four percent") for f in frases]
M=[["smell",0,"^smell"],["stressed0",0,"^stressed"],
["s_2022",1,None],["belfast",1,"^belfast"],["sweat",1,"^sweat"],["people",1,"^people"],
["s_first",2,None],["calm",2,"^calm"],["math",2,"^math"],
["s_four",3,None],["pick",3,"^pick"],
["s_right",4,None],["almost",4,"^almost"],["tests",4,"^tests"],
["s_so",5,None],["close",5,"^close"],["first5",5,"^first"],
["s_fin",6,None],["s_cta",7,None]]
OW=dict(look="jugadora",var=31,pelo="#5d4037",peloT="cola",camisa="#ef6c00",s=1.0)
CI=dict(look="inventor",var=32,lentes=True,pelo="#9e9e9e",camisa="#eceff1",s=0.97)
W=dict(color="#f2efe9",color2="#ffffff",oscuro="#c9bfae",lejos="#e0d8ca",collar="azul")
P=[perro(x=780,y=1760,s=1.0,k=0,dir=-1,fin="s_2022",estados=[{"k":"smell","lengua":True}]),
   {"tipo":"cajita","x":2050,"y":1690,"s":1.3,"color":"#90caf9","texto":"SWEAT","k":"sweat","cae":True,"fin":"s_first"},
   {"tipo":"cajita","x":2250,"y":1690,"s":1.3,"color":"#a5d6a7","texto":"BREATH","k":"sweat+0.3","cae":True,"fin":"s_first"},
   {"tipo":"cajita","x":3040,"y":1690,"s":1.5,"color":"#a5d6a7","texto":"CALM","k":"calm","cae":True,"fin":"s_four"},
   {"tipo":"cajita","x":3540,"y":1690,"s":1.5,"color":"#ef9a9a","texto":"STRESS","k":"math","cae":True,"fin":"s_four"},
   {"tipo":"cajita","x":4350,"y":1690,"s":1.4,"color":"#a5d6a7","texto":"CALM","k":"s_four","fin":"s_right"},
   {"tipo":"cajita","x":4950,"y":1690,"s":1.4,"color":"#ef9a9a","texto":"STRESS","k":"s_four","fin":"s_right"},
   perro(x=4200,y=1760,s=0.95,k="s_four",fin="s_right",pose="parado",camina=True,mov=[{"k":"s_four","x":4050,"y":1760},{"k":"pick","x":4500,"y":1760},{"k":"pick+0.8","x":4780,"y":1760}]),
   perro(x=5900,y=1760,s=0.95,k="s_right",fin="s_so",estados=[{"k":"almost","lengua":True}],**W),
   {"tipo":"sofa","x":7150,"y":1700,"s":1.1,"k":"s_so"},
   perro(x=7300,y=1760,s=1.0,k="s_so",fin="close",pose="parado",camina=True,mov=[{"k":"s_so","x":7650,"y":1760},{"k":"close","x":7120,"y":1760}],dir=-1),
   perro(x=7120,y=1760,s=1.0,k="close",dir=-1,estados=[{"k":"first5","lengua":True}])]
A=[{**OW,"hasta":"s_2022","keys":[{"k":0,"x":330,"y":1700,"pose":"piensa","cara":"triste"},{"k":"stressed0","x":330,"y":1700,"pose":"cruzado","cara":"triste","fx":"tiembla"}]},
   {**CI,"desde":"s_2022","hasta":"s_first","keys":[{"k":"s_2022","x":1380,"y":1700,"pose":"camina","cara":"neutral"},{"k":"s_2022+0.9","x":1650,"y":1700,"pose":"sostiene","cara":"neutral","objeto":"lupa"},{"k":"sweat","x":1650,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {"look":"cliente","var":33,"s":0.97,"desde":"s_first","hasta":"s_four","keys":[{"k":"s_first","x":3290,"y":1700,"pose":"parado","cara":"feliz"},{"k":"math","x":3290,"y":1700,"pose":"piensa","cara":"triste","fx":"tiembla"}]},
   {**CI,"desde":"s_right","hasta":"s_so","keys":[{"k":"s_right","x":5520,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"almost","x":5520,"y":1700,"pose":"celebra","cara":"risa"}]},
   {**OW,"desde":"s_so","keys":[{"k":"s_so","x":6820,"y":1700,"pose":"piensa","cara":"triste"},{"k":"close","x":6820,"y":1700,"pose":"parado","cara":"feliz"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_2022"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_first","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"oficina","k":"s_four"},{"x0":5200,"x1":6500,"set":"oficina","k":"s_right"},{"x0":6500,"x1":7900,"set":"sala","k":"s_so"}],
 "pan":[{"k":"s_2022","x":1300,"dur":0.9},{"k":"s_first","x":2600,"dur":0.9},{"k":"s_four","x":3900,"dur":0.9},{"k":"s_right","x":5200,"dur":0.9},{"k":"s_so","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[],
 "numeros":[{"k":"people","n":36,"suf":" PEOPLE","c":"cian","etq":"SWEAT + BREATH","fin":"s_first"},
            {"k":"almost","n":94,"suf":" %","c":"verde","etq":"CORRECT","fin":"s_so"}],
 "zoom":[{"k":0.1,"s":1.12,"x":560,"y":1560,"dur":0.6},{"k":"s_2022","s":1.0,"dur":0.3},{"k":"sweat","s":1.12,"x":1900,"y":1500,"dur":0.4},{"k":"people","s":1.0,"dur":0.3},
         {"k":"math","s":1.15,"x":3350,"y":1450,"dur":0.4},{"k":"s_four","s":1.0,"dur":0.3},{"k":"pick+0.8","s":1.2,"x":4800,"y":1600,"dur":0.4},{"k":"s_right","s":1.0,"dur":0.3},
         {"k":"s_so","s":1.0,"dur":0.3},{"k":"close","s":1.2,"x":6960,"y":1550,"dur":0.5},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"almost","f":12}],
 "titulos":[{"k":0.2,"texto":"IT SMELLS YOUR STRESS","c":"amar","fin":"s_2022"},
            {"k":"s_2022","texto":"BELFAST · 2022","c":"cian","fin":"people"},
            {"k":"s_first","texto":"CALM vs STRESSED","c":"rosa","grande":True,"fin":"s_four"},
            {"k":"s_four","texto":"4 DOGS, 1 JOB","c":"verde","fin":"s_right"},
            {"k":"s_so","texto":"ON A BAD DAY","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"belfast","texto":"QUEEN'S UNIVERSITY BELFAST","c":"cian","fin":"s_first"},
          {"k":"math","texto":"A HARD MATH PROBLEM","c":"rojo","fin":"s_four"},
          {"k":"pick","texto":"PICK THE STRESSED ONE","c":"amar","fin":"s_right"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS NOTICE?","cierre2":"Yes or no? Comment","paises":["YES","NO","ALWAYS"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
poner_sets(E,[("salaV",{"hora":"tarde","sinSofa":True,"var":3,"pared":["#f0dcc0","#d9bf9c"]}),("labV",{"pantalla":"SAMPLES","pantalla2":"36 PEOPLE"}),("cocinaV",{}),("labV",{"pantalla":"TEST","pantalla2":"4 DOGS"}),None,("salaV",{"hora":"noche","sinSofa":True,"var":1})])
insertar(E,"smell","s_2022",1300,"vitrinaV",{"fondo":["#ffd59a","#e89a4a","#5a2a0a"]},[perro(x=540,y=1900,s=2.6,dir=1,lengua=True)])
insertar(E,"tests","s_so",6500,"mesaCenitalV",{"titulo":"RESULTS · 720 TESTS","monto":"93.75 %","firma":"tests"},[])
g={"titulo":"Your Dog Can Smell Your Stress 🐶","texto_pantalla":"IT SMELLS STRESS","lote":"D2026112402","marca":"THE DOGS DECODER",
"nota_datos":"Wilson et al. (2022), PLOS ONE, Queen's University Belfast: muestras de sudor y aliento de 36 personas, tomadas antes (calma) y después de una tarea aritmética difícil (estrés). 4 perros entrenados para elegir la muestra de estrés: 675 aciertos en 720 pruebas = 93,75 % → 'almost 94 percent'. El estudio muestra que los perros distinguen el olor; que por eso se acerquen en un mal día es una interpretación → 'it may have'.",
"frases":frases,"frases_voz":voz,"fuentes":["https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0274143","https://www.qub.ac.uk/"],"escena":E}
guardar("D2026112402_src.json",g)
