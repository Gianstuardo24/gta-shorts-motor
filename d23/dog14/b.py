import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["Those puppy eyes your dog gives you are not an accident.",
"In 2019, scientists compared the faces of dogs and wolves.",
"Dogs have a small muscle that lifts the inner eyebrow. Wolves almost don't have it.",
"That lift makes their eyes look bigger, a bit like a sad human face.",
"And it works on us. In an earlier study, shelter dogs that raised their eyebrows more got adopted faster.",
"Scientists think humans favored those faces over thousands of years, without even noticing.",
"Tell me if your dog uses this look on you.",
"Follow to decode your dog."]
voz=[f.replace("2019","twenty nineteen") for f in frases]
M=[["puppy",0,"^puppy"],["accident",0,"^accident"],["s_lab",1,None],["faces1",1,"^faces"],["wolves1",1,"^wolves"],
["s_muscle",2,None],["muscle",2,"^muscle"],["eyebrow",2,"^eyebrow"],["wolves2",2,"^wolves"],["s_big",3,None],["bigger",3,"^bigger"],["sad",3,"^sad"],
["s_shelter",4,None],["shelter",4,"^shelter"],["adopted",4,"^adopted"],["s_us",5,None],["favored",5,"^favored"],["noticing",5,"^noticing"],["s_fin",6,None],["s_cta",7,None]]
P=[{"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":0},
   perro(x=720,y=1740,s=1.05,k=0,dir=-1,estados=[{"k":"accident","lengua":True},{"k":"s_lab","lengua":False}]),
   perro(x=1650,y=1740,s=1.05,k="s_lab",dir=1,fin="s_shelter"),
   perro(x=2150,y=1740,s=1.12,k="s_lab",dir=-1,fin="s_shelter",**LOBO),
   {"tipo":"documento","x":1650,"y":1260,"s":0.85,"sello":"HAS IT","selloc":"verde","k":"eyebrow","cae":True,"z":1800},
   {"tipo":"documento","x":2150,"y":1260,"s":0.85,"sello":"ALMOST NONE","selloc":"rojo","k":"wolves2","cae":True,"z":1800},
   {"tipo":"cajita","x":2950,"y":1740,"s":2.0,"color":"#8d6e63","k":"s_shelter","z":1600},
   perro(x=2950,y=1620,s=0.95,k="s_shelter",dir=1,color="#f1e3c8",color2="#fffaf0",oscuro="#b89b72",lejos="#d8c6a6",collar=None,z=1650,estados=[{"k":"adopted","lengua":True,"collar":"rosa"}]),
   {"tipo":"documento","x":2950,"y":1170,"s":0.95,"sello":"ADOPTED","selloc":"verde","k":"adopted","cae":True,"z":1800}]
A=[{"look":"gamer","var":101,"camisa":"#5c6bc0","pelo":"#2b1b14","s":1.0,"keys":[
    {"k":0,"x":300,"y":1714,"pose":"sentado","cara":"neutral","z":1800},
    {"k":"puppy","x":300,"y":1714,"pose":"sentado","cara":"feliz","z":1800},
    {"k":"s_us","x":300,"y":1714,"pose":"sentado","cara":"risa","z":1800}]},
   {"look":"inventor","var":103,"s":0.95,"desde":"s_lab","hasta":"s_shelter","pelo":"#8d6e63","peloT":"corto","camisa":"#eceff1","lentes":True,"objeto":"lupa","os":0.7,"keys":[
    {"k":"s_lab","x":1900,"y":1700,"pose":"sostiene","cara":"neutral"},
    {"k":"muscle","x":1900,"y":1700,"pose":"apunta","cara":"feliz","dir":-1},
    {"k":"wolves2","x":1900,"y":1700,"pose":"apunta","cara":"sorpresa","dir":1}]},
   {"look":"jugadora","var":104,"s":0.95,"desde":"s_shelter","hasta":"s_us","peloT":"cola","pelo":"#3b2a1e","keys":[
    {"k":"s_shelter","x":3500,"y":1700,"pose":"parado","cara":"neutral","dir":-1,"a":[3250,1700],"dur":1.0},
    {"k":"s_shelter+1.0","x":3250,"y":1700,"pose":"piensa","cara":"neutral","dir":-1},
    {"k":"adopted","x":3250,"y":1700,"pose":"celebra","cara":"risa","dir":-1,"fx":"salto"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.0,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala","luz":"tenue"},{"x0":1300,"x1":2600,"set":"estudio","k":"s_lab"},{"x0":2600,"x1":3900,"set":"calle","k":"s_shelter"}],
 "pan":[{"k":"s_lab","x":1300,"dur":1.0},{"k":"s_shelter","x":2600,"dur":0.9},{"k":"s_us","x":0,"dur":1.1}],
 "props":P,"actores":A,
 "zoom":[{"k":0.1,"s":1.25,"x":540,"y":1540,"dur":0.8},{"k":"accident","s":1.05,"dur":0.6},{"k":"s_lab","s":1.0,"dur":0.5},
         {"k":"eyebrow","s":1.25,"x":1700,"y":1520,"dur":0.6},{"k":"wolves2","s":1.2,"x":2100,"y":1520,"dur":0.6},{"k":"s_big","s":1.35,"x":1650,"y":1560,"dur":0.6},
         {"k":"s_shelter","s":1.0,"dur":0.5},{"k":"s_us","s":1.0,"dur":0.6},{"k":"noticing","s":1.2,"x":560,"y":1520,"dur":0.8}],
 "titulos":[{"k":0.2,"texto":"PUPPY EYES","c":"amar","fin":"s_lab"},
            {"k":"s_lab","texto":"DOGS VS WOLVES · 2019","c":"cian","fin":"s_big"},
            {"k":"s_big","texto":"BIGGER EYES","c":"rosa","fin":"s_shelter"},
            {"k":"s_shelter","texto":"SHELTER DOGS","c":"verde","fin":"s_us"},
            {"k":"favored","texto":"WE CHOSE THEM","c":"amar","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"eyebrow","texto":"LIFTS THE INNER EYEBROW","c":"verde","fin":"s_big"},
          {"k":"sad","texto":"LIKE A SAD HUMAN FACE","c":"rosa","fin":"s_shelter"},
          {"k":"adopted","texto":"ADOPTED FASTER","c":"verde","fin":"s_us"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES IT WORK ON YOU?","cierre2":"Yes or no? Comment","paises":["YES","NO"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
# --- 23-nov: escenarios propios + inserto ---
poner_sets(E,[("salaV",{"hora":"tarde","sinSofa":True,"sofa":["#c0623a","#8a3f22"]}),("labV",{"pantalla":"caras","pantalla2":"foto"}),("refugioV",{})])
quitar_props(E,["cajita"])
for p in E["escenas"][0]["props"]:
    if p.get("tipo")=="perro" and p.get("x")==2950: p["y"]=1740
E["escenas"][0]["zoom"]=[z for z in E["escenas"][0]["zoom"] if z["k"] not in ("s_big",)]
insertar(E,"s_big","sad",1300,"vitrinaV",{"fondo":["#f6cf94","#c98a4a","#3a2414"]},
         [perro(x=540,y=2050,s=3.4,k="s_big",dir=1,fin="sad",mira=True,collar="rosa")])

g={"titulo":"Why Your Dog Makes Puppy Eyes 🐶","texto_pantalla":"PUPPY EYES","lote":"D2026112301","marca":"THE DOGS DECODER",
"nota_datos":"Kaminski et al. 2019, PNAS: músculo levator anguli oculi medialis presente en perros, casi ausente en lobos; perros mueven la ceja más seguido e intenso; parece expresión triste humana. Estudio previo (2013): perros de refugio que levantaban más la ceja fueron adoptados más rápido. Fuentes: PNAS/PubMed, National Geographic, PBS NOVA.",
"frases":frases,"frases_voz":voz,"fuentes":["https://pubmed.ncbi.nlm.nih.gov/31209036/","https://www.nationalgeographic.com/animals/article/dogs-eyebrows-humans-communication","https://www.pbs.org/wgbh/nova/article/puppy-dog-eyes"],"escena":E}
guardar("D2026112301_01_src.json",g)
