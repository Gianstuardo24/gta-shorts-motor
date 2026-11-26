import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["GTA 6 tiene que superar un número enorme: 215 millones.",
"Son las copias que vendió GTA 5 desde 2013, según Take-Two.",
"Es uno de los juegos más vendidos de la historia.",
"Y GTA 6 partió fuerte: 32,5 millones vendidos antes de salir.",
"O sea, ya lleva cerca del 15 por ciento del camino.",
"Pero a GTA 5 le tomó 13 años llegar a esa cifra.",
"Comenta si crees que GTA 6 lo va a superar.",
"Sigue el canal para más números de GTA 6."]
voz=["GTA seis tiene que superar un número enorme. Doscientos quince millones.",
"Son las copias que vendió GTA cinco desde dos mil trece, según Téik Tu.",
"Es uno de los juegos más vendidos de la historia.",
"Y GTA seis partió fuerte. Treinta y dos coma cinco millones vendidos antes de salir.",
"O sea, ya lleva cerca del quince por ciento del camino.",
"Pero a GTA cinco le tomó trece años llegar a esa cifra.",
"Comenta si crees que GTA seis lo va a superar.",
"Sigue el canal para más números de GTA seis."]
M=[["superar",0,"^superar"],["enorme",0,"^enorme"],
["s_copias",1,None],["vendio",1,"^vendi"],["segun",1,"^seg"],
["s_uno",2,None],["historia",2,"^historia"],
["s_partio",3,None],["fuerte",3,"^fuerte"],["antes",3,"^antes"],
["s_lleva",4,None],["cerca",4,"^cerca"],["camino",4,"^camino"],
["s_pero",5,None],["tomo",5,"^tom"],["cifra",5,"^cifra"],
["s_fin",6,None],["s_cta",7,None]]
GAM=dict(look="gamer",var=81,pelo="#3e2723",camisa="#e53935",lentes=False,s=1.0)
JU=dict(look="jugadora",var=85,peloT="cola",pelo="#d7a86e",camisa="#00897b",s=0.97)
P=[{"tipo":"consola","x":760,"y":1690,"s":1.2,"k":0.0,"fin":"s_copias"},
   {"tipo":"documento","x":2250,"y":1160,"s":0.95,"sello":"DESDE 2013","selloc":"cian","k":"vendio","cae":True,"z":1800,"fin":"s_uno"},
   {"tipo":"trofeo","x":3350,"y":1640,"s":1.2,"k":"historia","fin":"s_partio"},
   {"tipo":"cajita","x":4560,"y":1690,"s":1.8,"color":"#7e57c2","texto":"GTA 6","k":"fuerte","cae":True,"fin":"s_lleva"},
   {"tipo":"cajita","x":4790,"y":1690,"s":1.8,"color":"#7e57c2","texto":"GTA 6","k":"fuerte+0.2","cae":True,"fin":"s_lleva"},
   {"tipo":"cajita","x":4675,"y":1530,"s":1.8,"color":"#ec407a","texto":"GTA 6","k":"fuerte+0.4","cae":True,"fin":"s_lleva"},
   {"tipo":"cartel","x":6100,"y":1180,"s":1.2,"texto":"META: 215 M","k":"camino","fin":"s_pero"},
   {"tipo":"cronometro","x":7450,"y":1300,"s":1.2,"texto":"13 AÑOS","k":"tomo","z":1800}]
A=[{**GAM,"hasta":"s_copias","keys":[{"k":0,"x":320,"y":1700,"pose":"juega","cara":"feliz","objeto":"control"},{"k":"enorme","x":320,"y":1700,"pose":"apunta","cara":"sorpresa","fx":"brinca"}]},
   {"look":"ejecutivo","var":82,"camisa":"#263238","pelo":"#3e2723","s":1.0,"desde":"s_copias","hasta":"s_uno","keys":[{"k":"s_copias","x":1660,"y":1700,"pose":"sostiene","cara":"feliz","objeto":"documento"},{"k":"segun","x":1660,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**JU,"desde":"s_uno","hasta":"s_partio","keys":[{"k":"s_uno","x":2680,"y":1700,"pose":"camina","cara":"feliz"},{"k":"s_uno+0.9","x":2960,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"historia","x":2960,"y":1700,"pose":"celebra","cara":"risa"}]},
   {**GAM,"desde":"s_partio","hasta":"s_lleva","keys":[{"k":"s_partio","x":4200,"y":1700,"pose":"parado","cara":"feliz"},{"k":"fuerte","x":4200,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {**JU,"desde":"s_lleva","hasta":"s_pero","keys":[{"k":"s_lleva","x":5480,"y":1700,"pose":"camina","cara":"neutral"},{"k":"cerca","x":5700,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"camino","x":5700,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**GAM,"desde":"s_pero","keys":[{"k":"s_pero","x":6860,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"tomo","x":6860,"y":1700,"pose":"cruzado","cara":"sorpresa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_copias"},{"x0":2600,"x1":3900,"set":"estudio","k":"s_uno"},
          {"x0":3900,"x1":5200,"set":"calle","k":"s_partio"},{"x0":5200,"x1":6500,"set":"calle","k":"s_lleva","luz":"tenue"},{"x0":6500,"x1":7900,"set":"sala","k":"s_pero"}],
 "pan":[{"k":"s_copias","x":1300,"dur":0.9},{"k":"s_uno","x":2600,"dur":0.9},{"k":"s_partio","x":3900,"dur":0.9},{"k":"s_lleva","x":5200,"dur":0.9},{"k":"s_pero","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"cifra","de":5,"texto":"¿LO LOGRA?","fin":"s_fin","dx":160}],
 "numeros":[{"k":"enorme","n":215,"suf":" MILLONES","c":"amar","etq":"COPIAS DE GTA 5","fin":"s_copias"},
            {"k":"cerca","n":15,"suf":" %","c":"verde","etq":"DEL CAMINO","fin":"s_pero"}],
 "zoom":[{"k":0.1,"s":1.1,"x":500,"y":1450,"dur":0.6},{"k":"enorme","s":1.0,"dur":0.3},{"k":"segun","s":1.22,"x":1720,"y":1420,"dur":0.4},{"k":"s_uno","s":1.0,"dur":0.3},
         {"k":"historia","s":1.12,"x":3200,"y":1500,"dur":0.4},{"k":"s_partio","s":1.0,"dur":0.3},{"k":"antes","s":1.12,"x":4480,"y":1500,"dur":0.4},{"k":"s_lleva","s":1.0,"dur":0.3},
         {"k":"s_pero","s":1.0,"dur":0.3},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"enorme","f":14},{"k":"fuerte","f":12}],
 "titulos":[{"k":0.2,"texto":"LA META DE GTA 6","c":"rosa","fin":"enorme"},
            {"k":"s_copias","texto":"GTA 5 · DESDE 2013","c":"cian","fin":"s_uno"},
            {"k":"s_uno","texto":"DE LOS MÁS VENDIDOS","c":"amar","fin":"s_partio"},
            {"k":"fuerte","texto":"32,5 MILLONES","c":"verde","grande":True,"fin":"s_lleva"},
            {"k":"s_pero","texto":"PERO...","c":"rojo","fin":"tomo"}],
 "chips":[{"k":"segun","texto":"FUENTE: TAKE-TWO","c":"amar","fin":"s_uno"},
          {"k":"antes","texto":"ANTES DE SALIR","c":"verde","fin":"s_lleva"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"¿LO SUPERA?","cierre2":"Comenta: sí o no","paises":["SÍ","NO"],"sfx":[],"cta":"SIGUE EL CANAL","like":"LIKE"}
poner_sets(E,[("cuartoGamerV",{"era":"2013"}),("corporativoV",{"ticker":"TTWO ▲","hora":"tarde"}),("escenarioV",{}),("nocheV",{"sem":3,"ciudad":True}),("casaPalmasV",{"hora":"tarde","sinCasa":True}),("cuartoGamerV",{"era":"2013"})])
insertar(E,"enorme","s_copias",1300,"mesaCenitalV",{"titulo":"VENTAS · GTA 5","monto":"215 M","billetes":True,"billete":"US$ 10.000"},[])
insertar(E,"tomo","s_fin",6500,"vitrinaV",{"fondo":["#1d1440","#0d0820","#030108"],"luz2":"200,150,255"},[{"tipo":"cronometro","x":540,"y":1450,"s":2.2,"texto":"13 AÑOS"}])
g={"titulo":"GTA 6 tiene que superar 215 millones 🎯","texto_pantalla":"215 MILLONES","lote":"G2026112402","marca":"VICEVERSO GG",
"nota_datos":"GTA V (2013): más de 215 millones de copias vendidas según Take-Two (cifra de sus informes trimestrales; es un piso, la cifra actual puede ser mayor). GTA VI: 32,5 millones de unidades vendidas antes del lanzamiento (Take-Two, comunicado del 20-nov-2026). 32,5/215 = 15,1 % → 'cerca del 15 por ciento'. 2013→2026 = 13 años.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.take2games.com/ir","https://www.gtaboom.com/take-two-reports-142-billion-quarter-as-gta-6-hype-increases-e8b7"],"escena":E}
guardar("G2026112402_src.json",g)
