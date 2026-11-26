import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["In 1633, drinking coffee in public in Istanbul could get you killed.",
"Sultan Murad IV closed the city's coffeehouses.",
"The reason: coffeehouses were where people met and talked, and he feared plots against him.",
"Rebel soldiers had killed his older brother, so he trusted no one.",
"Stories say he walked the streets in disguise, looking for coffee drinkers.",
"The ban didn't last. After his death, the coffeehouses came back.",
"Tell me if you'd have risked it for a cup.",
"Follow for more banned coffee stories."]
voz=[f.replace("1633","sixteen thirty-three").replace("Murad IV","Murad the Fourth") for f in frases]
M=[["drinking",0,"^drinking"],["istanbul",0,"^istanbul"],["killed0",0,"^killed"],["s_closed",1,None],["murad",1,"^murad"],["closed",1,"^closed"],
["s_why",2,None],["talked",2,"^talked"],["plots",2,"^plots"],["s_bro",3,None],["brother",3,"^brother"],["trusted",3,"^trusted"],
["s_dis",4,None],["disguise",4,"^disguise"],["drinkers",4,"^drinkers"],["s_back",5,None],["last",5,"^last"],["came",5,"^came"],["s_fin",6,None],["s_cta",7,None]]
SUL=dict(look="rey",var=21,corona=False,s=1.0,pelo="#2b1b14",barba="#2b1b14")
P=[{"tipo":"taza","x":620,"y":1600,"s":1.3,"k":0.0,"fin":"s_closed"},{"tipo":"cajita","x":620,"y":1720,"s":1.5,"color":"#3e2723","k":0.0,"fin":"s_closed"},
   {"tipo":"documento","x":1950,"y":1180,"s":1.0,"sello":"CLOSED","selloc":"rojo","k":"closed","z":1800,"fin":"s_why"},
   {"tipo":"trono","x":3250,"y":1640,"s":1.1,"k":"s_why","fin":"s_dis"},
   {"tipo":"taza","x":5550,"y":1600,"s":1.3,"k":"s_back"},{"tipo":"cajita","x":5550,"y":1720,"s":1.5,"color":"#3e2723","k":"s_back"}]
A=[{"look":"cliente","var":31,"s":0.95,"barba":"#4e342e","hasta":"s_closed","keys":[{"k":0,"x":350,"y":1700,"pose":"sostiene","cara":"feliz","objeto":"taza"},{"k":"killed0","x":350,"y":1700,"pose":"sostiene","cara":"sorpresa","objeto":"taza","fx":"tiembla"}]},
   {"look":"sabio","var":32,"s":0.95,"hasta":"s_closed","keys":[{"k":0,"x":880,"y":1705,"pose":"sostiene","cara":"risa","objeto":"taza","dir":-1},{"k":"killed0","x":880,"y":1705,"pose":"parado","cara":"sorpresa","dir":-1}]},
   {"look":"oficial","var":33,"s":1.0,"desde":"s_closed","hasta":"s_why","keys":[{"k":"s_closed","x":1650,"y":1690,"pose":"apunta","cara":"enojado"}]},
   {"look":"cliente","var":34,"s":0.95,"desde":"s_closed","hasta":"s_why","keys":[{"k":"s_closed","x":2200,"y":1700,"pose":"sostiene","cara":"triste","objeto":"taza","dir":-1}]},
   {**SUL,"desde":"s_why","hasta":"s_dis","keys":[{"k":"s_why","x":3250,"y":1600,"pose":"sentado","cara":"neutral","z":1660},{"k":"plots","x":3250,"y":1600,"pose":"sentado","cara":"enojado","fx":"tiembla","z":1660},{"k":"trusted","x":3250,"y":1600,"pose":"sentado","cara":"enojado","z":1660}]},
   {"look":"cliente","var":35,"s":0.9,"desde":"s_why","hasta":"s_bro","keys":[{"k":"s_why","x":2850,"y":1700,"pose":"juega","cara":"risa"}]},
   {"look":"sabio","var":36,"s":0.9,"desde":"s_why","hasta":"s_bro","keys":[{"k":"s_why","x":3500,"y":1705,"pose":"piensa","cara":"feliz","dir":-1}]},
   {"look":"cliente","var":37,"s":1.0,"desde":"s_dis","hasta":"s_back","capa":"#37474f","keys":[{"k":"s_dis","x":4000,"y":1700,"pose":"camina","cara":"neutral","a":[4500,1700],"dur":2.5},{"k":"s_dis+2.5","x":4500,"y":1700,"pose":"parado","cara":"enojado","mira":2.5}]},
   {"look":"cliente","var":38,"s":0.95,"desde":"s_back","keys":[{"k":"s_back","x":5250,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {"look":"jugadora","var":39,"s":0.95,"desde":"s_back","keys":[{"k":"s_back","x":5850,"y":1705,"pose":"sostiene","cara":"feliz","objeto":"taza","dir":-1}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.1,
 "zonas":[{"x0":-300,"x1":1300,"set":"cafe","luz":"tenue"},{"x0":1300,"x1":2600,"set":"calle","k":"s_closed","luz":"tenue"},{"x0":2600,"x1":3900,"set":"trono","k":"s_why"},
          {"x0":3900,"x1":5000,"set":"calle","k":"s_dis","luz":"tenue"},{"x0":5000,"x1":6300,"set":"cafe","k":"s_back"}],
 "pan":[{"k":"s_closed","x":1300,"dur":1.0},{"k":"s_why","x":2600,"dur":0.9},{"k":"s_dis","x":3900,"dur":0.9},{"k":"s_back","x":5000,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"talked","de":5,"texto":"BLAH BLAH...","fin":"s_bro","dx":60}],
 "zoom":[{"k":0.1,"s":1.06,"dur":0.6},{"k":"closed","s":1.15,"x":1950,"y":1450,"dur":0.4},{"k":"s_why","s":1.0,"dur":0.4},{"k":"trusted","s":1.12,"x":3250,"y":1450,"dur":0.5},{"k":"s_dis","s":1.0,"dur":0.4},{"k":"s_back","s":1.0,"dur":0.4}],
 "sacudidas":[{"k":"killed0","f":10}],
 "titulos":[{"k":0.2,"texto":"ISTANBUL · 1633","c":"amar","fin":"s_closed"},
            {"k":"s_closed","texto":"COFFEEHOUSES CLOSED","c":"rojo","fin":"s_why"},
            {"k":"s_why","texto":"SULTAN MURAD IV","c":"cian","fin":"s_dis"},
            {"k":"s_dis","texto":"IN DISGUISE","c":"rosa","fin":"s_back"},
            {"k":"s_back","texto":"THE BAN ENDED","c":"verde","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"plots","texto":"FEAR OF PLOTS","c":"rojo","fin":"s_bro"},
          {"k":"brother","texto":"HIS BROTHER WAS KILLED","c":"amar","fin":"s_dis"},
          {"k":"disguise","texto":"(STORIES SAY)","c":"amar","fin":"s_back"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WOULD YOU RISK IT?","cierre2":"Yes or no? Comment","paises":["YES","NO"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("cafeOtomanoV",{}),("estambulV",{}),("palacioV",{"estilo":"otomano"}),("estambulV",{"var":1}),("cafeOtomanoV",{})])
quitar_props(E,["cajita","taza"])
e0=E["escenas"][0];e0["zoom"]=[z for z in e0["zoom"] if z["k"]!="closed"]
insertar(E,"0","istanbul",0,"vitrinaV",{"fondo":["#6b3a1a","#3a1e0c","#0d0603"],"luz2":"255,200,130"},[{"tipo":"tazaTurca","x":520,"y":1450,"s":1.7}])
insertar(E,"closed","s_why",2600,"vitrinaV",{"fondo":["#5a2a1a","#2a120a","#0a0402"],"luz2":"255,190,120"},[{"tipo":"edicto","x":540,"y":1200,"s":1.55,"titulo":"BY ORDER OF THE SULTAN","texto":"COFFEEHOUSES CLOSED"}])

g={"titulo":"A Sultan Made Coffee a Death Crime ☕","texto_pantalla":"ISTANBUL · 1633","lote":"C2026112301","marca":"COFFEE, BUT WHY?",
"nota_datos":"1633: el sultán otomano Murad IV cerró los cafés de Estambul y castigó con la muerte beber café en público; temía que los cafés fueran lugares de complots (los jenízaros, que frecuentaban cafés, habían matado a su hermano Osman II). Relatos (no confirmados) dicen que recorría la ciudad disfrazado buscando bebedores. La prohibición se levantó tras su muerte. Fuentes: Atlas Obscura, NPR, History.com, Popular Science.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.atlasobscura.com/articles/was-coffee-ever-illegal","https://www.npr.org/sections/thesalt/2012/01/10/144988133/drink-coffee-off-with-your-head","https://www.history.com/articles/coffee-houses-revolutions"],"escena":E}
guardar("C2026112301_src.json",g)
