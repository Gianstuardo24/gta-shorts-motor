import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["Sleeping next to your dog might be better than sleeping next to a person.",
"In 2018, researchers at Canisius College surveyed 962 women in the US.",
"More than half shared their bed with a dog.",
"Women said dogs bothered their sleep less than human partners, and less than cats.",
"With a dog in bed, they also felt more comfort and security.",
"Researchers think it's because dogs sleep on a schedule closer to ours.",
"Tell me where your dog sleeps.",
"Follow to decode your dog."]
voz=[f.replace("2018","twenty eighteen").replace("962","nine hundred sixty-two").replace("the US","the U.S.") for f in frases]
M=[["sleeping",0,"^sleeping"],["person",0,"^person"],["s_lab",1,None],["canisius",1,"^canisius"],["p962",1,"^962"],
["s_half",2,None],["half",2,"^half"],["bed2",2,"^bed"],["s_vs",3,None],["less1",3,"^less"],["partners",3,"^partners"],["cats",3,"^cats"],
["s_safe",4,None],["comfort",4,"^comfort"],["security",4,"^security"],["s_sched",5,None],["schedule",5,"^schedule"],["ours",5,"^ours"],
["s_fin",6,None],["s_cta",7,None]]
BIS=dict(collar="rosa")  # Biscuit: perro dorado, collar rosa
P=[{"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":0},
   perro(x=780,y=1748,s=1.0,k=0,fin="s_lab",pose="echado",dir=-1,cola=3),
   {"tipo":"pc","x":1950,"y":1650,"s":1.1,"k":"s_lab","texto":"SLEEP SURVEY","fin":"s_vs"},
   {"tipo":"grafico","x":2250,"y":1180,"s":1.0,"k":"half","cae":True,"fin":"s_vs"},
   gato(x=3130,y=1745,s=0.85,k="s_vs",fin="s_safe",dir=-1),
   perro(x=3480,y=1748,s=0.95,k="s_vs",fin="s_safe",dir=-1,estados=[{"k":"less1","lengua":True}]),
   {"tipo":"documento","x":3130,"y":1300,"s":0.8,"sello":"WAKES YOU","selloc":"rojo","k":"cats","cae":True,"z":1800,"fin":"s_safe"},
   {"tipo":"documento","x":3480,"y":1250,"s":0.8,"sello":"LESS","selloc":"verde","k":"cats+0.5","cae":True,"z":1800,"fin":"s_safe"},
   perro(x=780,y=1748,s=1.0,k="s_safe",pose="echado",dir=-1,cola=4,estados=[{"k":"comfort","lengua":True}])]
A=[{"look":"jugadora","var":104,"s":1.0,"peloT":"cola","pelo":"#3b2a1e","camisa":"#7e57c2","hasta":"s_lab","keys":[
    {"k":0,"x":300,"y":1714,"pose":"sentado","cara":"neutral","z":1800},
    {"k":"person","x":300,"y":1714,"pose":"sentado","cara":"feliz","z":1800}]},
   {"look":"inventor","var":103,"s":0.95,"desde":"s_lab","hasta":"s_vs","pelo":"#8d6e63","peloT":"corto","camisa":"#eceff1","lentes":True,"keys":[
    {"k":"s_lab","x":1700,"y":1700,"pose":"parado","cara":"neutral"},
    {"k":"p962","x":1700,"y":1700,"pose":"apunta","cara":"feliz"},
    {"k":"half","x":1700,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {"look":"gamer","var":122,"s":0.95,"camisa":"#546e7a","pelo":"#1d1d1d","desde":"s_vs","hasta":"s_safe","keys":[
    {"k":"s_vs","x":2780,"y":1700,"pose":"parado","cara":"neutral"},
    {"k":"partners","x":2780,"y":1700,"pose":"cruzado","cara":"enojado"}]},
   {"look":"jugadora","var":104,"s":1.0,"peloT":"cola","pelo":"#3b2a1e","camisa":"#7e57c2","desde":"s_safe","keys":[
    {"k":"s_safe","x":300,"y":1714,"pose":"sentado","cara":"feliz","z":1800},
    {"k":"security","x":300,"y":1714,"pose":"sentado","cara":"risa","z":1800}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.0,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala","luz":"tenue"},{"x0":1300,"x1":2600,"set":"estudio","k":"s_lab"},{"x0":2600,"x1":3900,"set":"sala","k":"s_vs","luz":"tenue"}],
 "pan":[{"k":"s_lab","x":1300,"dur":1.0},{"k":"s_vs","x":2600,"dur":0.9},{"k":"s_safe","x":0,"dur":1.1}],
 "props":P,"actores":A,
 "burbujas":[{"k":"sleeping+0.8","x":700,"y":1430,"texto":"MY SIDE.","fin":"s_lab"},
             {"k":"s_vs+0.6","de":2,"texto":"ZZZ... SNORE","fin":"cats","dx":60},
             {"k":"s_sched+0.5","x":700,"y":1430,"texto":"SAME BEDTIME.","fin":"s_fin"}],
 "numeros":[{"k":"p962","n":962,"suf":" WOMEN","c":"cian","etq":"SURVEYED","fin":"s_half"},
            {"k":"half","n":55,"suf":"%","c":"amar","etq":"SHARE THEIR BED WITH A DOG","fin":"s_vs"}],
 "zoom":[{"k":0.1,"s":1.25,"x":560,"y":1560,"dur":0.8},{"k":"person","s":1.05,"dur":0.6},{"k":"s_lab","s":1.0,"dur":0.5},
         {"k":"s_vs","s":1.0,"dur":0.5},{"k":"cats+0.5","s":1.2,"x":3420,"y":1520,"dur":0.6},
         {"k":"s_safe","s":1.0,"dur":0.5},{"k":"comfort","s":1.2,"x":560,"y":1560,"dur":0.7},{"k":"s_sched","s":1.05,"dur":0.6}],
 "titulos":[{"k":0.2,"texto":"DOG IN YOUR BED","c":"amar","fin":"s_lab"},
            {"k":"s_lab","texto":"CANISIUS COLLEGE · 2018","c":"cian","fin":"s_vs"},
            {"k":"s_vs","texto":"WHO WAKES YOU UP","c":"rosa","fin":"s_safe"},
            {"k":"s_safe+1.0","texto":"COMFORT + SECURITY","c":"verde","grande":True,"fin":"s_sched"},
            {"k":"s_sched","texto":"SAME SCHEDULE","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"less1","texto":"DOGS BOTHER SLEEP LESS","c":"verde","fin":"s_safe"},
          {"k":"ours","texto":"CLOSER TO OURS","c":"cian","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WHERE DOES YOURS SLEEP?","cierre2":"Tell us. Comment","paises":["MY BED","ITS BED","SOFA"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("salaV",{"hora":"noche","sinSofa":True,"var":1}),("labV",{"pantalla":"barras","pantalla2":"onda"}),("dormitorioV",{"persona":False})])
quitar_props(E,["pc"])
E["escenas"][0]["zoom"]=[z for z in E["escenas"][0]["zoom"] if z["k"]!=0.1]
insertar(E,"0","s_lab",1300,"dormitorioV",{"zzz":True},[perro(x=660,y=1098,s=0.9,pose="echado",dir=-1,cola=3)])
insertar(E,"schedule","s_fin",0,"vitrinaV",{"fondo":["#2a3a6a","#141c38","#05070f"],"luz2":"170,190,255"},[{"tipo":"cronometro","x":540,"y":1500,"s":1.6,"texto":"NIGHT"}])

g={"titulo":"Why Your Dog Sleeps Next to You 🐶","texto_pantalla":"DOG IN YOUR BED","lote":"D2026112303","marca":"THE DOGS DECODER",
"nota_datos":"Hoffman, Stutz y Vasilopoulos 2018, Anthrozoös (Canisius College, Buffalo NY): encuesta a 962 mujeres de EE.UU.; 55% compartía la cama con al menos un perro, 31% con un gato, 57% con pareja. Los perros fueron percibidos como menos disruptivos que las parejas humanas y los gatos, y con más sensación de comodidad y seguridad. Hoffman: el sueño de los perros coincide más con el de los humanos que el de los gatos. Es una encuesta (autorreporte). Fuentes: Canisius College, CBS News, AJC, HuffPost.",
"frases":frases,"frases_voz":voz,"fuentes":["https://canisius.edu/node/1733","https://www.cbsnews.com/texas/news/women-sleep-better-with-dogs-study","https://www.ajc.com/news/national/study-suggests-women-may-sleep-better-with-dogs-bed-over-humans/0icLXGEHKQi2kQiYQtLwRN"],"escena":E}
guardar("D2026112303_src.json",g)
