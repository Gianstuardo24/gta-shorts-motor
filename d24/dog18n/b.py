import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Your dog knows what you're hiding.",
"You can smile, act normal, say you're fine.",
"But in 2022, scientists in Belfast put four dogs to a test.",
"They took breath and sweat from 36 people: once calm, and once right after a hard math problem.",
"The dogs had to pick the second sample. They got it right almost 94 percent of the time.",
"What they smell is your stress. You can hide it from people, but not from your dog.",
"Tell me if your dog notices your bad days.",
"Follow to decode your dog."]
voz=[f.replace("2022","twenty twenty-two").replace("36 people","thirty-six people").replace("94 percent","ninety-four percent") for f in frases]
M=[["knows",0,"^knows"],["hiding",0,"^hiding"],
["s_smile",1,None],["smile",1,"^smile"],["normal",1,"^normal"],["fine",1,"^fine"],
["s_2022",2,None],["belfast",2,"^belfast"],["four",2,"^four"],["test",2,"^test"],
["s_col",3,None],["breath",3,"^breath"],["people",3,"^people"],["calm",3,"^calm"],["math",3,"^math"],
["s_pick",4,None],["pick",4,"^pick"],["second",4,"^second"],["almost",4,"^almost"],
["s_rev",5,None],["stress",5,"^stress"],["hide",5,"^hide"],["dog5",5,"^dog"],
["s_fin",6,None],["s_cta",7,None]]
OW=dict(look="jugadora",var=31,pelo="#5d4037",peloT="cola",camisa="#ef6c00",s=1.0)
CI=dict(look="inventor",var=32,lentes=True,pelo="#9e9e9e",camisa="#eceff1",s=0.97)
W=dict(color="#f2efe9",color2="#ffffff",oscuro="#c9bfae",lejos="#e0d8ca",collar="azul")
B=dict(color="#5d4037",color2="#8d6e63",oscuro="#3e2723",lejos="#4e342e",collar="rojo")
P=[perro(x=800,y=1760,s=1.0,k=0,dir=-1,fin="s_smile"),
   perro(x=2260,y=1760,s=0.95,k="s_smile",dir=-1,fin="s_2022"),
   {"tipo":"documento","x":3600,"y":1150,"s":0.95,"sello":"BELFAST 2022","selloc":"cian","k":"belfast","cae":True,"z":1800,"fin":"s_col"},
   perro(x=3330,y=1760,s=0.8,k="four",fin="s_col",dir=-1,**W),perro(x=3560,y=1765,s=0.8,k="four+0.15",fin="s_col",dir=-1,**B),
   {"tipo":"cajita","x":4650,"y":1690,"s":1.5,"color":"#a5d6a7","texto":"SAMPLE 1","k":"calm","cae":True,"fin":"s_pick"},
   {"tipo":"cajita","x":4950,"y":1690,"s":1.5,"color":"#ef9a9a","texto":"SAMPLE 2","k":"math","cae":True,"fin":"s_pick"},
   {"tipo":"cajita","x":5760,"y":1690,"s":1.4,"color":"#a5d6a7","texto":"1","k":"s_pick","fin":"s_rev"},
   {"tipo":"cajita","x":6200,"y":1690,"s":1.4,"color":"#ef9a9a","texto":"2","k":"s_pick","fin":"s_rev"},
   perro(x=5500,y=1760,s=0.95,k="s_pick",fin="s_rev",pose="parado",camina=True,mov=[{"k":"s_pick","x":5420,"y":1760},{"k":"pick","x":5800,"y":1760},{"k":"second","x":6060,"y":1760}],**W),
   perro(x=7120,y=1760,s=1.0,k="s_rev",dir=-1,estados=[{"k":"hide","lengua":True}])]
A=[{**OW,"hasta":"s_smile","keys":[{"k":0,"x":380,"y":1700,"pose":"cruzado","cara":"feliz"},{"k":"hiding","x":380,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {**OW,"desde":"s_smile","hasta":"s_2022","keys":[{"k":"s_smile","x":1160,"y":1700,"a":[1700,1700],"dur":1.4,"ease":"eio","pose":"saluda","cara":"feliz"},{"k":"normal","x":1700,"y":1700,"pose":"saluda","cara":"risa"},{"k":"fine","x":1700,"y":1700,"pose":"celebra","cara":"feliz"}]},
   {"look":"cliente","var":33,"s":0.97,"desde":"s_smile","hasta":"s_2022","keys":[{"k":"s_smile","x":2040,"y":1700,"pose":"saluda","cara":"feliz","dir":-1}]},
   {**CI,"desde":"s_2022","hasta":"s_col","keys":[{"k":"s_2022","x":2960,"y":1700,"pose":"sostiene","cara":"neutral","objeto":"lupa"},{"k":"four","x":2960,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {"look":"cliente","var":34,"camisa":"#00897b","s":0.97,"desde":"s_col","hasta":"s_pick","keys":[{"k":"s_col","x":4280,"y":1700,"pose":"parado","cara":"feliz"},{"k":"math","x":4280,"y":1700,"pose":"piensa","cara":"triste","fx":"tiembla"}]},
   {**CI,"desde":"s_pick","hasta":"s_rev","keys":[{"k":"s_pick","x":5400,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"almost","x":5400,"y":1700,"pose":"celebra","cara":"risa"}]},
   {**OW,"desde":"s_rev","keys":[{"k":"s_rev","x":6800,"y":1700,"pose":"piensa","cara":"triste"},{"k":"hide","x":6800,"y":1700,"pose":"cruzado","cara":"triste"},{"k":"dog5","x":6800,"y":1700,"pose":"parado","cara":"feliz"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"calle","k":"s_smile"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_2022"},
          {"x0":3900,"x1":5200,"set":"oficina","k":"s_col"},{"x0":5200,"x1":6500,"set":"estudio","k":"s_pick"},{"x0":6500,"x1":7900,"set":"sala","k":"s_rev"}],
 "pan":[{"k":"s_smile","x":1300,"dur":0.8},{"k":"s_2022","x":2600,"dur":0.8},{"k":"s_col","x":3900,"dur":0.8},{"k":"s_pick","x":5200,"dur":0.8},{"k":"s_rev","x":6500,"dur":0.8}],
 "props":P,"actores":A,
 "burbujas":[{"k":"fine","de":1,"texto":"I'M FINE!","fin":"s_2022","dx":40}],
 "numeros":[{"k":"people","n":36,"suf":" PEOPLE","c":"cian","etq":"BREATH + SWEAT","fin":"calm"},
            {"k":"almost","n":94,"suf":" %","c":"verde","etq":"RIGHT","fin":"s_rev"}],
 "zoom":[],"planos_hint":[{"k":"hiding","tipo":"objeto"},{"k":"stress","tipo":"primer","var":31}],
 "sacudidas":[{"k":"hiding","f":12},{"k":"stress","f":14}],
 "titulos":[{"k":0.15,"texto":"IT KNOWS","c":"amar","grande":True,"fin":"hiding"},
            {"k":"s_smile","texto":"YOU ACT NORMAL","c":"rosa","fin":"s_2022"},
            {"k":"s_2022","texto":"BELFAST · 2022","c":"cian","fin":"s_col"},
            {"k":"s_col","texto":"TWO SAMPLES","c":"amar","fin":"breath"},
            {"k":"s_pick","texto":"PICK SAMPLE 2","c":"verde","fin":"almost"},
            {"k":"stress","texto":"YOUR STRESS","c":"rojo","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"four","texto":"4 DOGS","c":"cian","fin":"s_col"},
          {"k":"math","texto":"A HARD MATH PROBLEM","c":"rojo","fin":"s_pick"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS NOTICE?","cierre2":"Yes or no? Comment","paises":["YES","NO","ALWAYS"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
poner_sets(E,[("salaV",{"hora":"noche","sinSofa":True,"var":1}),("parqueV",{"hora":"dia"}),("labV",{"pantalla":"SMELL TEST","pantalla2":"4 DOGS"}),("cocinaV",{}),("refugioV",{}),("dormitorioV",{"persona":False,"pared":["#5a6b8a","#3a4766"]})])
insertar(E,"hiding","s_smile",1300,"vitrinaV",{"fondo":["#2a3350","#141a2c","#05070d"],"luz2":"180,200,255"},[perro(x=540,y=1900,s=2.6,dir=1)])
insertar(E,"breath","people",3900,"mesaCenitalV",{"titulo":"SAMPLES · BREATH + SWEAT","monto":"36 PEOPLE","firma":"breath"},[])
insertar(E,"hide","dog5",6500,"vitrinaV",{"fondo":["#ffd59a","#e89a4a","#5a2a0a"]},[perro(x=540,y=1900,s=2.6,dir=-1,lengua=True)])
g={"titulo":"Your Dog Knows What You're Hiding 👻","texto_pantalla":"IT KNOWS","lote":"D2026112404","marca":"THE DOGS DECODER",
"nota_datos":"Versión nueva (gancho que no revela; revelación al final). Wilson et al. (2022), PLOS ONE, Queen's University Belfast: aliento y sudor de 36 personas, antes (calma) y después de una tarea aritmética difícil. 4 perros entrenados eligieron la muestra de estrés en 675 de 720 pruebas = 93,75 % → 'almost 94 percent'. Lo que huelen es el cambio de olor por estrés. El emoji de fantasma del título es una prueba pedida por Tao (pista que no es literal): medir permanencia. Tipo de gancho: 2 (secreto) + emoción.",
"frases":frases,"frases_voz":voz,"fuentes":["https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0274143","https://www.qub.ac.uk/"],"escena":E}
guardar("D2026112404_src.json",g)
