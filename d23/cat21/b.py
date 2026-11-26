import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["Your cat knows its name. It just doesn't always answer.",
"In 2019, scientists in Japan tested 78 cats, at home and in cat cafes.",
"Owners said four words that sounded like the cat's name, then the real name.",
"The cats tuned out the first words, then reacted to their own name: ears, head, tail, or a meow.",
"It even worked when a stranger said it.",
"So if your cat ignores you, it may still know you called.",
"Tell me if yours comes when you call.",
"Follow to decode your cat."]
voz=[f.replace("2019","twenty nineteen").replace("78","seventy-eight") for f in frases]
M=[["knows",0,"^knows"],["answer",0,"^answer"],["s_jp",1,None],["japan",1,"^japan"],["c78",1,"^78"],["cafes",1,"^cafes"],
["s_words",2,None],["four",2,"^four"],["sounded",2,"^sounded"],["real",2,"^real"],["s_react",3,None],["tuned",3,"^tuned"],["reacted",3,"^reacted"],["ears",3,"^ears"],["meow",3,"^meow"],
["s_str",4,None],["stranger",4,"^stranger"],["s_ign",5,None],["ignores",5,"^ignores"],["called",5,"^called"],["s_fin",6,None],["s_cta",7,None]]
P=[{"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":0,"fin":"s_jp"},
   gato(x=820,y=1740,k=0,dir=1,fin="s_jp"),
   # cafe con varios gatos
   gato(x=1500,y=1740,s=0.8,k="s_jp",fin="s_words",color="#e0a060",color2="#fbe9d4",oscuro="#b06a2c",lejos="#c98a4e",ojos="#8bc34a"),
   gato(x=1800,y=1650,s=0.7,k="s_jp+0.2",fin="s_words",z=1700,color="#2b2b2b",color2="#5a5a5a",oscuro="#111111",lejos="#3a3a3a",ojos="#ffd54f",dir=-1),
   gato(x=2150,y=1740,s=0.8,k="s_jp+0.4",fin="s_words",color="#f2e6d4",color2="#ffffff",oscuro="#b08968",lejos="#d9c7ad",ojos="#4fc3f7",dir=-1),
   {"tipo":"cajita","x":1800,"y":1745,"s":1.6,"color":"#8d6e63","k":"s_jp","fin":"s_words","z":1640},
   # prueba de nombre
   gato(x=3150,y=1740,k="s_words",dir=1,fin="real+0.4"),
   gato(x=3150,y=1740,k="real+0.4",dir=-1,fin="stranger+0.4",lento=True),
   gato(x=3150,y=1740,k="stranger+0.4",dir=1,fin="s_ign"),
   gato(x=4500,y=1740,k="s_ign",dir=1)]
A=[{"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"hasta":"s_jp","keys":[
    {"k":0,"x":260,"y":1714,"pose":"sentado","cara":"feliz","z":1800},{"k":"answer","x":260,"y":1714,"pose":"sentado","cara":"risa","z":1800}]},
   {"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"desde":"s_words","hasta":"s_str","keys":[
    {"k":"s_words","x":2850,"y":1700,"pose":"parado","cara":"feliz"},{"k":"real","x":2850,"y":1700,"pose":"apunta","cara":"risa"},{"k":"reacted","x":2850,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {"look":"ejecutivo","var":221,"s":1.0,"desde":"s_str","hasta":"s_ign","keys":[
    {"k":"s_str","x":3600,"y":1700,"pose":"parado","cara":"neutral","dir":-1,"a":[3420,1700],"dur":0.6},{"k":"stranger","x":3420,"y":1700,"pose":"apunta","cara":"sorpresa","dir":-1}]},
   {"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"desde":"s_ign","keys":[
    {"k":"s_ign","x":4150,"y":1700,"pose":"saluda","cara":"feliz"},{"k":"called","x":4150,"y":1700,"pose":"piensa","cara":"risa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.0,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala","luz":"tenue"},{"x0":1300,"x1":2600,"set":"sala","k":"s_jp","luz":"tenue"},{"x0":2600,"x1":3900,"set":"sala","k":"s_words"},{"x0":3900,"x1":5200,"set":"sala","k":"s_ign","luz":"tenue"}],
 "pan":[{"k":"s_jp","x":1300,"dur":1.0},{"k":"s_words","x":2600,"dur":0.9},{"k":"s_ign","x":3900,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":0.3,"de":0,"texto":"MOCHI!","fin":"answer","dx":150},
             {"k":"four","de":1,"texto":"MOCHA","fin":"four+0.6"},{"k":"four+0.6","de":1,"texto":"MATCHA","fin":"sounded+0.3"},{"k":"sounded+0.3","de":1,"texto":"MOJI","fin":"real"},{"k":"real","de":1,"texto":"MOCHI!","fin":"s_react+0.8"},
             {"k":"stranger","de":2,"texto":"MOCHI?","fin":"s_ign","dx":-90},{"k":"s_ign","de":3,"texto":"MOCHI!","fin":"called"}],
 "numeros":[{"k":"c78","n":78,"suf":" CATS","c":"cian","etq":"TESTED IN JAPAN","fin":"s_words"}],
 "zoom":[{"k":0.1,"s":1.2,"x":560,"y":1540,"dur":0.8},{"k":"s_jp","s":1.0,"dur":0.5},{"k":"s_words","s":1.0,"dur":0.5},
         {"k":"s_str","s":1.0,"dur":0.5},{"k":"s_ign","s":1.0,"dur":0.5},{"k":"called","s":1.2,"x":4350,"y":1550,"dur":0.8}],
 "titulos":[{"k":0.2,"texto":"THE NAME TEST","c":"amar","fin":"s_jp"},
            {"k":"s_jp","texto":"JAPAN · 2019","c":"cian","fin":"s_words"},
            {"k":"s_words","texto":"4 SIMILAR WORDS","c":"amar","fin":"s_react"},
            {"k":"s_react","texto":"THEN THEIR NAME","c":"verde","fin":"s_str"},
            {"k":"s_str","texto":"EVEN FROM A STRANGER","c":"rosa","fin":"s_ign"},
            {"k":"ignores","texto":"IGNORED ≠ NOT HEARD","c":"amar","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"ears","texto":"EARS · HEAD · TAIL · MEOW","c":"verde","fin":"s_str"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DOES YOURS COME?","cierre2":"Yes or no? Comment","paises":["YES","NO","SOMETIMES"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("salaV",{"hora":"dia","sinSofa":True,"var":2,"pared":["#e9d6e6","#cdb2c9"]}),("cafeGatosV",{}),("cocinaV",{}),("dormitorioV",{"persona":False,"pared":["#5a6b8a","#3a4766"]})])
quitar_props(E,["cajita"])
insertar(E,"four","s_react",2600,"vitrinaV",{"fondo":["#1e3a5a","#0d1e30","#03080f"],"luz2":"150,210,255"},[{"tipo":"monitorOnda","x":540,"y":1650,"s":1.4,"pant":"nombres"}])
insertar(E,"reacted","s_str",2600,"vitrinaV",{"fondo":["#f6d6a8","#d99a5a","#4a2410"]},[gato(x=540,y=2100,s=3.3,dir=1)])

g={"titulo":"Why Your Cat Ignores Its Name 🐱","texto_pantalla":"THE NAME TEST","lote":"K2026112302","marca":"THE CATS DECODER",
"nota_datos":"Saito et al. 2019, Scientific Reports (Sophia Univ./Univ. of Tokyo): 78 gatos de casas y cafés de gatos; 4 palabras parecidas y luego el nombre; respondieron más a su nombre (orejas, cabeza, cola, maullido); también con voz de un extraño; un gato que no responde igual puede reconocer su nombre. Fuentes: National Geographic, Scientific American, Univ. of Tokyo, Science News.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.scientificamerican.com/article/cats-recognize-their-own-names-even-if-they-choose-to-ignore-them/","https://www.u-tokyo.ac.jp/focus/en/press/z0508_00040.html","https://www.nationalgeographic.com/animals/article/cats-recognize-names-dogs-pets"],"escena":E}
guardar("K2026112302_01_src.json",g)
