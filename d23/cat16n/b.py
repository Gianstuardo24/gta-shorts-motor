import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["Your cat's eyes glow at night because there's a mirror inside them.",
"Behind the eye, cats have a shiny layer called the tapetum lucidum.",
"Light goes in, hits that layer, and bounces back through the eye.",
"This gives the eye a second chance to catch the light.",
"Thanks to it, cats can see with about one sixth of the light we need.",
"The glow you see is that light bouncing back at you.",
"Tell me what color your cat's eyes glow.",
"Follow to decode your cat."]
voz=list(frases)
M=[["glow0",0,"^glow"],["mirror",0,"^mirror"],["s_layer",1,None],["shiny",1,"^shiny"],["tapetum",1,"^tapetum"],
["s_bounce",2,None],["hits",2,"^hits"],["bounces",2,"^bounces"],["s_second",3,None],["second",3,"^second"],
["s_sixth",4,None],["sixth",4,"^sixth"],["need",4,"^need"],["s_glow",5,None],["glow5",5,"^glow"],["back5",5,"^back"],
["s_fin",6,None],["s_cta",7,None]]
GLOW="#e6ff3a"
luz=[{"k":"s_bounce","x":330,"y":1560},{"k":"hits","x":560,"y":1585},{"k":"bounces","x":330,"y":1560}]
P=[{"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":0,"fin":"s_sixth"},
   gato(x=640,y=1745,s=0.95,k=0,fin="s_sixth",dir=-1,ojos=GLOW),
   {"tipo":"orbe","x":330,"y":1560,"s":0.8,"z":1900,"k":"s_bounce","fin":"s_second","mov":luz},
   gato(x=2050,y=1755,s=0.85,k="s_sixth",fin="s_glow",pose="parado",camina=True,ojos=GLOW,mov=[{"k":"s_sixth","x":1550,"y":1755},{"k":"s_sixth+2.2","x":2150,"y":1755}]),
   {"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":"s_glow"},
   gato(x=640,y=1745,s=0.95,k="s_glow",dir=-1,ojos=GLOW)]
A=[{"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"hasta":"s_sixth","keys":[
    {"k":0,"x":260,"y":1714,"pose":"sentado","cara":"neutral","z":1800},
    {"k":"glow0","x":260,"y":1714,"pose":"sentado","cara":"sorpresa","z":1800,"fx":"salto"},
    {"k":"s_layer","x":260,"y":1714,"pose":"telefono","cara":"neutral","z":1800},
    {"k":"second","x":260,"y":1714,"pose":"sentado","cara":"feliz","z":1800}]},
   {"look":"cliente","var":211,"s":0.9,"desde":"s_sixth","hasta":"s_glow","keys":[
    {"k":"s_sixth","x":2500,"y":1700,"pose":"camina","cara":"neutral","dir":-1,"a":[2350,1700],"dur":1.2},
    {"k":"sixth","x":2350,"y":1700,"pose":"piensa","cara":"sorpresa","dir":-1}]},
   {"look":"gamer","var":201,"camisa":"#26a69a","pelo":"#5d4037","peloT":"largo","s":1.0,"desde":"s_glow","keys":[
    {"k":"s_glow","x":260,"y":1714,"pose":"telefono","cara":"neutral","z":1800},
    {"k":"back5","x":260,"y":1714,"pose":"sentado","cara":"risa","z":1800}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.0,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala","luz":"tenue"},{"x0":1300,"x1":2600,"set":"calle","k":"s_sixth","luz":"tenue"}],
 "pan":[{"k":"s_sixth","x":1300,"dur":1.0},{"k":"s_glow","x":0,"dur":1.1}],
 "props":P,"actores":A,
 "burbujas":[{"k":"glow0","x":720,"y":1420,"texto":"I SEE ALL.","fin":"s_layer"},
             {"k":"glow5+0.6","x":700,"y":1420,"texto":"YOU'RE WELCOME.","fin":"s_fin"}],
 "zoom":[{"k":0.1,"s":1.3,"x":560,"y":1560,"dur":0.8},{"k":"mirror","s":1.05,"dur":0.6},
         {"k":"s_layer","s":1.9,"x":640,"y":1590,"dur":0.8},{"k":"s_second","s":1.3,"x":500,"y":1580,"dur":0.6},
         {"k":"s_sixth","s":1.0,"dur":0.5},{"k":"sixth","s":1.2,"x":2150,"y":1580,"dur":0.6},
         {"k":"s_glow","s":1.0,"dur":0.5},{"k":"glow5","s":1.4,"x":760,"y":1560,"dur":0.8},{"k":"back5+0.6","s":1.1,"x":540,"y":1560,"dur":0.6}],
 "titulos":[{"k":0.2,"texto":"GLOWING EYES","c":"amar","fin":"s_layer"},
            {"k":"tapetum","texto":"TAPETUM LUCIDUM","c":"cian","grande":True,"fin":"s_bounce"},
            {"k":"s_bounce","texto":"A MIRROR INSIDE","c":"amar","fin":"s_sixth"},
            {"k":"sixth","texto":"1/6 OF THE LIGHT","c":"verde","grande":True,"fin":"s_glow"},
            {"k":"s_glow","texto":"THE GLOW = BOUNCED LIGHT","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"shiny","texto":"A SHINY LAYER","c":"cian","fin":"s_bounce"},
          {"k":"second","texto":"A SECOND CHANCE","c":"verde","fin":"s_sixth"},
          {"k":"need","texto":"VS WHAT HUMANS NEED","c":"rosa","fin":"s_glow"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WHAT COLOR DO THEY GLOW?","cierre2":"Tell us. Comment","paises":["GREEN","GOLD","BLUE"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("salaV",{"hora":"noche","sinSofa":True,"var":2,"pared":["#3a3f5a","#262a40"]}),("nocheV",{"sem":7,"gente":False})])
e0=E["escenas"][0]
e0["zoom"]=[z for z in e0["zoom"] if z["k"] not in ("s_layer","s_second","glow5","back5+0.6")]
e0["props"]=[p for p in e0["props"] if p["tipo"]!="orbe"]
insertar(E,"s_layer","s_sixth",1300,"vitrinaV",{"fondo":["#123a3a","#0a1e24","#03080a"],"luz2":"150,255,210"},[{"tipo":"ojoGato","x":560,"y":1150,"s":1.25}])
insertar(E,"glow5","s_fin",0,"vitrinaV",{"fondo":["#0a0f0c","#050806","#000000"],"luz2":"120,255,170"},[{"tipo":"ojosBrillan","x":540,"y":1150,"s":1.4}])

g={"titulo":"Why Your Cat's Eyes Glow at Night 🐱","texto_pantalla":"GLOWING EYES","lote":"K2026112303","marca":"THE CATS DECODER",
"nota_datos":"Tapetum lucidum ('tapiz brillante'): capa reflectante detrás de la retina; refleja la luz de vuelta y le da a la retina una segunda oportunidad de captarla; el brillo de los ojos es esa luz reflejada. Los gatos necesitan cerca de 1/6 de la luz que necesitan los humanos (estimación citada por varias fuentes). Fuentes: The Conversation/GBH (2022), Popular Science, Adopt-a-Pet, NPR.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.wgbh.org/news/national/2022-04-11/why-do-cats-eyes-glow-in-the-dark","https://www.popsci.com/environment/why-cat-eyes-glow/","https://www.adoptapet.com/blog/behavior-training/why-do-cats-eyes-glow"],"escena":E}
guardar("K2026112303_src.json",g)
