import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["Coffee comes from Ethiopia, and Ethiopia's own church once banned it.",
"For a long time, the Ethiopian Orthodox Church opposed coffee.",
"Many priests saw it as a Muslim drink, so Christians were told to avoid it.",
"That started to change in the late 1800s.",
"Emperor Menelik the Second drank coffee himself, and a church leader helped change the clergy's minds.",
"Today, the coffee ceremony is a big part of Ethiopian life.",
"Tell me if you knew coffee came from Ethiopia.",
"Follow for more banned coffee stories."]
voz=[f.replace("1800s","eighteen hundreds") for f in frases]
M=[["comes",0,"^comes"],["ethiopia0",0,"^ethiopia"],["banned",0,"^banned"],["s_church",1,None],["opposed",1,"^opposed"],
["s_priests",2,None],["muslim",2,"^muslim"],["avoid",2,"^avoid"],["s_change",3,None],["late",3,"^late"],
["s_men",4,None],["menelik",4,"^menelik"],["drank",4,"^drank"],["leader",4,"^leader"],["minds",4,"^minds"],["s_today",5,None],["ceremony",5,"^ceremony"],
["s_fin",6,None],["s_cta",7,None]]
P=[{"tipo":"cartel","x":820,"y":1500,"s":1.0,"texto":"ETHIOPIA","k":"ethiopia0","fin":"s_church"},
   {"tipo":"taza","x":330,"y":1600,"s":1.3,"k":0.0,"fin":"s_church"},{"tipo":"cajita","x":330,"y":1720,"s":1.5,"color":"#3e2723","k":0.0,"fin":"s_church"},
   {"tipo":"documento","x":1950,"y":1120,"s":1.0,"sello":"BANNED","selloc":"rojo","k":"opposed","cae":True,"z":1800,"fin":"s_change"},
   {"tipo":"trono","x":3250,"y":1640,"s":1.1,"k":"s_change","fin":"s_today"},
   {"tipo":"documento","x":3450,"y":1120,"s":0.9,"sello":"ALLOWED","selloc":"verde","k":"minds","cae":True,"z":1800,"fin":"s_today"},
   {"tipo":"taza","x":4550,"y":1600,"s":1.3,"k":"s_today"},{"tipo":"cajita","x":4550,"y":1720,"s":1.5,"color":"#3e2723","k":"s_today"}]
A=[{"look":"cliente","var":41,"s":0.95,"hasta":"s_church","keys":[{"k":0,"x":560,"y":1700,"pose":"sostiene","cara":"feliz","objeto":"taza"},{"k":"banned","x":560,"y":1700,"pose":"sostiene","cara":"sorpresa","objeto":"taza","fx":"tiembla"}]},
   {"look":"sabio","var":42,"s":1.0,"desde":"s_church","hasta":"s_change","keys":[{"k":"s_church","x":1650,"y":1700,"pose":"cruzado","cara":"enojado"},{"k":"muslim","x":1650,"y":1700,"pose":"apunta","cara":"enojado"}]},
   {"look":"sabio","var":43,"s":0.95,"desde":"s_church","hasta":"s_change","keys":[{"k":"s_church","x":2250,"y":1705,"pose":"cruzado","cara":"neutral","dir":-1},{"k":"avoid","x":2250,"y":1705,"pose":"apunta","cara":"enojado","dir":-1}]},
   {"look":"rey","var":44,"s":1.0,"desde":"s_change","hasta":"s_today","pelo":"#1d1d1d","barba":"#1d1d1d","keys":[{"k":"s_change","x":3250,"y":1600,"pose":"sentado","cara":"neutral","z":1660},{"k":"drank","x":3250,"y":1600,"pose":"sentado","cara":"feliz","objeto":"taza","z":1660}]},
   {"look":"sabio","var":45,"s":0.95,"desde":"s_men","hasta":"s_today","keys":[{"k":"s_men","x":2850,"y":1700,"pose":"parado","cara":"neutral"},{"k":"leader","x":2850,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"minds","x":2850,"y":1700,"pose":"celebra","cara":"risa"}]},
   {"look":"jugadora","var":46,"s":0.95,"desde":"s_today","keys":[{"k":"s_today","x":4250,"y":1700,"pose":"ofrece","cara":"feliz","objeto":"taza"}]},
   {"look":"cliente","var":47,"s":0.95,"desde":"s_today","keys":[{"k":"s_today","x":4850,"y":1705,"pose":"sostiene","cara":"risa","objeto":"taza","dir":-1}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.1,
 "zonas":[{"x0":-300,"x1":1300,"set":"cafe"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_church","luz":"tenue"},{"x0":2600,"x1":3900,"set":"trono","k":"s_change"},{"x0":3900,"x1":5200,"set":"cafe","k":"s_today"}],
 "pan":[{"k":"s_church","x":1300,"dur":1.0},{"k":"s_change","x":2600,"dur":0.9},{"k":"s_today","x":3900,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"drank+0.3","de":3,"texto":"MORE, PLEASE.","fin":"s_today","dx":60}],
 "zoom":[{"k":0.1,"s":1.06,"dur":0.6},{"k":"opposed","s":1.12,"x":1950,"y":1450,"dur":0.4},{"k":"s_change","s":1.0,"dur":0.4},{"k":"drank","s":1.12,"x":3150,"y":1450,"dur":0.5},{"k":"s_today","s":1.0,"dur":0.4}],
 "titulos":[{"k":0.2,"texto":"COFFEE'S HOME","c":"amar","fin":"s_church"},
            {"k":"s_church","texto":"BANNED BY THE CHURCH","c":"rojo","fin":"s_change"},
            {"k":"s_change","texto":"LATE 1800s","c":"cian","fin":"s_men"},
            {"k":"s_men","texto":"EMPEROR MENELIK II","c":"amar","fin":"s_today"},
            {"k":"s_today","texto":"THE COFFEE CEREMONY","c":"verde","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"muslim","texto":"SEEN AS A \"MUSLIM DRINK\"","c":"rojo","fin":"s_change"},
          {"k":"leader","texto":"A CHURCH LEADER HELPED","c":"verde","fin":"s_today"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DID YOU KNOW?","cierre2":"Yes or no? Comment","paises":["YES","NO"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
g={"titulo":"Coffee Was Banned Where It Was Born ☕","texto_pantalla":"COFFEE'S HOME","lote":"C2026112302","marca":"COFFEE, BUT WHY?",
"nota_datos":"El café es originario de Etiopía. La Iglesia Ortodoxa Etíope prohibió/condenó el café (visto como 'bebida musulmana') desde antes del s. XVIII; las actitudes se suavizaron en la segunda mitad del s. XIX (consumo creció 1880-1886). Según Richard Pankhurst, se debió en gran parte al emperador Menelik II, que lo bebía, y al Abuna Matewos, que disipó la creencia del clero. Hoy la ceremonia del café es central en la vida etíope. Fuentes: Wikipedia (History of coffee, cita Pankhurst), Anadolu Agency / Daily Sabah, Culture Trip, TWL Ethiopia.",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/History_of_coffee","https://aa.com.tr/en/culture-and-art/for-ethiopians-coffees-more-than-just-a-drink/45856","https://theculturetrip.com/articles/things-you-didnt-know-about-coffee"],"escena":E}
guardar("C2026112302_src.json",g)
