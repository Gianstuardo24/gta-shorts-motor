import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["In 1971, Nike paid 35 dollars for its logo.",
"Phil Knight needed a logo for his new shoes, so he asked a design student, Carolyn Davidson.",
"She charged 2 dollars an hour, and worked about 17 hours.",
"Knight looked at her swoosh and said he didn't love it, but maybe it would grow on him.",
"That 35 dollar drawing became one of the most famous logos on Earth.",
"Twelve years later, Nike surprised her with a gold swoosh ring and 500 shares of stock.",
"Lesson: a small job can become the face of a giant. Tell me what you would have charged.",
"Follow for the next million dollar mistake."]
voz=[f.replace("1971","nineteen seventy-one").replace("35 dollar ","thirty-five dollar ").replace("35 dollars","thirty-five dollars").replace("2 dollars","two dollars").replace("17 hours","seventeen hours").replace("500 shares","five hundred shares") for f in frases]
M=[["k1971",0,"^1971"],["d35",0,"^35"],["logo0",0,"^logo"],
["s_ask",1,None],["shoes",1,"^shoes"],["student",1,"^student"],["carolyn",1,"^carolyn"],
["s_rate",2,None],["d2",2,"^2$"],["hours",2,"^17"],
["s_knight",3,None],["swoosh",3,"^swoosh"],["love",3,"^love"],["grow",3,"^grow"],
["s_famous",4,None],["famous",4,"^famous"],["earth",4,"^earth"],
["s_1983",5,None],["surprised",5,"^surprised"],["ring",5,"^ring"],["shares",5,"^500"],
["s_les",6,None],["face",6,"^face"],["s_fin",6,"^tell"],["s_cta",7,None]]
KN=dict(look="ejecutivo",var=71,pelo="#c9a227",camisa="#263238",s=1.0)
CA=dict(look="jugadora",var=72,pelo="#5d4037",peloT="cola",camisa="#ef6c00",s=0.97)
P=[{"tipo":"escritorio","x":820,"y":1720,"s":1.1,"k":0.0,"z":1650,"fin":"s_rate"},
   {"tipo":"cajita","x":780,"y":1560,"s":1.6,"color":"#ff7043","texto":"SHOES","k":"shoes","cae":True,"z":1660,"fin":"s_rate"},
   {"tipo":"escritorio","x":2000,"y":1720,"s":1.1,"k":"s_rate","z":1650,"fin":"s_knight"},
   {"tipo":"documento","x":1990,"y":1180,"s":0.85,"sello":"SKETCH 1","selloc":"rojo","k":"s_rate+0.4","cae":True,"z":1800,"fin":"s_knight"},
   {"tipo":"documento","x":2260,"y":1100,"s":0.85,"sello":"SKETCH 2","selloc":"amar","k":"d2","cae":True,"z":1800,"fin":"s_knight"},
   {"tipo":"cronometro","x":1620,"y":1250,"s":1.0,"texto":"17.5 H","k":"hours","z":1800,"fin":"s_knight"},
   {"tipo":"escritorio","x":3300,"y":1720,"s":1.1,"k":"s_knight","z":1650,"fin":"s_famous"},
   {"tipo":"documento","x":3560,"y":1150,"s":0.95,"sello":"THE SWOOSH","selloc":"verde","k":"swoosh","cae":True,"z":1800,"fin":"s_famous"},
   {"tipo":"trofeo","x":4560,"y":1700,"s":1.3,"k":"famous","cae":True,"fin":"s_1983"},
   {"tipo":"cajita","x":4200,"y":1740,"s":1.9,"color":"#ff7043","texto":"SHOES","k":"s_famous","z":1600,"fin":"s_1983"},
   {"tipo":"cajita","x":4200,"y":1570,"s":1.9,"color":"#ffab91","texto":"SHOES","k":"s_famous+0.3","cae":True,"z":1600,"fin":"s_1983"},
   {"tipo":"cajita","x":4900,"y":1740,"s":1.9,"color":"#ff7043","texto":"SHOES","k":"earth","cae":True,"z":1600,"fin":"s_1983"},
   {"tipo":"cajita","x":5830,"y":1560,"s":1.5,"color":"#ffd23f","texto":"RING","k":"ring","cae":True,"z":1800},
   {"tipo":"documento","x":5840,"y":1130,"s":0.9,"sello":"500 SHARES","selloc":"verde","k":"shares","cae":True,"z":1800}]
A=[{**KN,"hasta":"s_rate","keys":[{"k":0,"x":560,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"s_ask","x":560,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"carolyn","x":560,"y":1700,"pose":"ofrece","cara":"feliz","objeto":"documento"}]},
   {**CA,"desde":"student","hasta":"s_rate","keys":[{"k":"student","x":930,"y":1700,"pose":"saluda","cara":"feliz","dir":-1},{"k":"carolyn","x":900,"y":1700,"pose":"parado","cara":"feliz","dir":-1}]},
   {**CA,"desde":"s_rate","hasta":"s_knight","keys":[{"k":"s_rate","x":1740,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"d2","x":1740,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"hours","x":1740,"y":1700,"pose":"celebra","cara":"risa"}]},
   {**KN,"desde":"s_knight","hasta":"s_famous","keys":[{"k":"s_knight","x":3140,"y":1700,"pose":"cruzado","cara":"neutral"},{"k":"love","x":3140,"y":1700,"pose":"piensa","cara":"triste"},{"k":"grow","x":3140,"y":1700,"pose":"apunta","cara":"neutral"}]},
   {**CA,"desde":"s_knight","hasta":"s_famous","keys":[{"k":"s_knight","x":3620,"y":1700,"pose":"ofrece","cara":"feliz","dir":-1,"objeto":"documento"},{"k":"love","x":3620,"y":1700,"pose":"parado","cara":"sorpresa","dir":-1}]},
   {"look":"cliente","var":73,"s":0.95,"desde":"s_famous","hasta":"s_1983","keys":[{"k":"s_famous","x":4380,"y":1700,"pose":"celebra","cara":"risa"}]},
   {"look":"gamer","var":74,"s":0.95,"camisa":"#1565c0","desde":"s_famous","hasta":"s_1983","keys":[{"k":"s_famous","x":4740,"y":1700,"pose":"apunta","cara":"feliz","dir":-1},{"k":"earth","x":4740,"y":1700,"pose":"celebra","cara":"risa","dir":-1,"fx":"salto"}]},
   {**KN,"pelo":"#b0a070","desde":"s_1983","keys":[{"k":"s_1983","x":5560,"y":1700,"pose":"parado","cara":"feliz"},{"k":"ring","x":5560,"y":1700,"pose":"ofrece","cara":"risa","objeto":"cajita"},{"k":"s_les","x":5560,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**CA,"desde":"s_1983","keys":[{"k":"s_1983","x":6130,"y":1700,"pose":"parado","cara":"neutral","dir":-1},{"k":"surprised","x":6130,"y":1700,"pose":"parado","cara":"sorpresa","dir":-1,"fx":"salto"},{"k":"shares","x":6130,"y":1700,"pose":"celebra","cara":"risa","dir":-1}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.1,
 "zonas":[{"x0":-300,"x1":1300,"set":"oficina"},{"x0":1300,"x1":2600,"set":"estudio","k":"s_rate"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_knight","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"calle","k":"s_famous"},{"x0":5200,"x1":6600,"set":"banco","k":"s_1983"}],
 "pan":[{"k":"s_rate","x":1300,"dur":1.0},{"k":"s_knight","x":2600,"dur":0.9},{"k":"s_famous","x":3900,"dur":0.9},{"k":"s_1983","x":5300,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"love","de":3,"texto":"I DON'T LOVE IT.","fin":"s_famous","dx":110},{"k":"surprised+0.3","de":8,"texto":"FOR ME?","fin":"shares","dx":-70}],
 "numeros":[{"k":"d35","n":35,"pre":"$","c":"amar","etq":"NIKE'S LOGO · 1971","fin":"s_ask"},
            {"k":"shares","n":500,"suf":" SHARES","c":"verde","etq":"NIKE STOCK · 1983","fin":"s_les"}],
 "zoom":[{"k":0.1,"s":1.06,"dur":0.6},{"k":"carolyn","s":1.15,"x":1000,"y":1450,"dur":0.5},{"k":"s_rate","s":1.0,"dur":0.4},{"k":"swoosh","s":1.12,"x":3400,"y":1350,"dur":0.4},
         {"k":"s_famous","s":1.0,"dur":0.4},{"k":"ring","s":1.15,"x":5840,"y":1450,"dur":0.4},{"k":"s_les","s":1.0,"dur":0.5}],
 "sacudidas":[{"k":"d35","f":12},{"k":"famous","f":14}],
 "titulos":[{"k":0.2,"texto":"1971","c":"amar","fin":"s_ask"},
            {"k":"s_ask","texto":"HE NEEDED A LOGO","c":"cian","fin":"s_rate"},
            {"k":"s_rate","texto":"$2 AN HOUR","c":"rosa","fin":"s_knight"},
            {"k":"s_knight","texto":"THE SWOOSH","c":"amar","grande":True,"fin":"s_famous"},
            {"k":"s_famous","texto":"ON EVERY SHOE","c":"cian","fin":"s_1983"},
            {"k":"s_1983","texto":"12 YEARS LATER","c":"verde","fin":"s_les"},
            {"k":"s_les+0.4","texto":"THE LESSON","c":"rojo","fin":"s_fin"}],
 "chips":[{"k":"hours","texto":"TOTAL: $35","c":"amar","fin":"s_knight"},
          {"k":"grow","texto":"\"MAYBE IT WILL GROW ON ME\"","c":"cian","fin":"s_famous"},
          {"k":"face","texto":"SMALL JOB · GIANT FACE","c":"amar","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"YOUR PRICE?","cierre2":"What would you have charged? Comment","paises":["$35","$1 MILLION","SHARES"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[None,("tallerV",{}),None,None,("corporativoV",{"ticker":"NKE ▲","hora":"noche"})])
insertar(E,"hours","s_knight",2600,"mesaCenitalV",{"titulo":"LOGO DESIGN · INVOICE","monto":"$35","firma":"hours"},[])
insertar(E,"earth","s_1983",5300,"vitrinaV",{"fondo":["#ff8a50","#b23c17","#2a0a02"],"luz2":"255,220,190","pedestal":True},[{"tipo":"trofeo","x":540,"y":1300,"s":2.2}])
g={"titulo":"Nike's Logo Cost Just $35 👟","texto_pantalla":"LOGO FOR $35","lote":"M2026112401","marca":"MILLION DOLLAR MISTAKE",
"nota_datos":"1971: Carolyn Davidson, estudiante de diseño gráfico en Portland State University, diseñó el Swoosh para Phil Knight; cobró US$2 por hora, 17,5 horas según la empresa = US$35. Knight dijo: 'I don't love it, but maybe it will grow on me'. 1983: Nike le regaló un anillo de oro con el Swoosh y un diamante, y 500 acciones. Fuentes: Wikipedia (Swoosh), Nike (oficial), CNBC. Banco MDM caso 8.",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/Swoosh","https://about.nike.com/","https://www.cnbc.com/"],"escena":E}
guardar("M2026112401_src.json",g)
