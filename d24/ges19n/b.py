import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["GTA 6 humilló a Hollywood. Y lo hizo en un solo día.",
"El récord era de una película: el tráiler de Deadpool y Wolverine, con 365 millones de vistas en 24 horas.",
"En mayo de 2025 salió el segundo tráiler de GTA 6.",
"Sumando todas las plataformas, llegó a 475 millones en un día.",
"O sea, un videojuego le ganó al cine por más de 100 millones.",
"Y aquí viene lo más loco.",
"Todavía faltaba un año y medio para que el juego saliera.",
"Comenta si tú lo viste ese día.",
"Sigue el canal para más números de GTA 6."]
voz=["GTA seis humilló a Jóligud. Y lo hizo en un solo día.",
"El récord era de una película. El tráiler de Dedpul y Wúlverin, con trescientos sesenta y cinco millones de vistas en veinticuatro horas.",
"En mayo de dos mil veinticinco salió el segundo tráiler de GTA seis.",
"Sumando todas las plataformas, llegó a cuatrocientos setenta y cinco millones en un día.",
"O sea, un videojuego le ganó al cine por más de cien millones.",
"Y aquí viene lo más loco.",
"Todavía faltaba un año y medio para que el juego saliera.",
"Comenta si tú lo viste ese día.",
"Sigue el canal para más números de GTA seis."]
M=[["humillo",0,"^humill"],["hizo",0,"^hizo"],["solo",0,"^solo"],
["s_rec",1,None],["pelicula",1,"^pel"],["con",1,"^con$"],["vistas",1,"^vistas"],
["s_mayo",2,None],["mayo",2,"^mayo"],["segundo",2,"^segundo"],
["s_sum",3,None],["plataformas",3,"^plataformas"],["llego",3,"^lleg"],
["s_gano",4,None],["gano",4,"^gan"],["por",4,"^por$"],
["s_loco",5,None],["loco",5,"^loco"],
["s_falta",6,None],["medio",6,"^medio"],["saliera",6,"^saliera"],
["s_fin",7,None],["s_cta",8,None]]
GAM=dict(look="gamer",var=81,pelo="#3e2723",camisa="#e53935",lentes=False,s=1.0)
JU=dict(look="jugadora",var=85,peloT="cola",pelo="#d7a86e",camisa="#00897b",s=0.97)
CI=dict(look="ejecutivo",var=86,pelo="#263238",camisa="#37474f",s=0.97)
P=[{"tipo":"claqueta","x":800,"y":1690,"s":1.1,"texto":"CINE","k":0.0,"fin":"s_rec"},
   {"tipo":"trofeo","x":2180,"y":1640,"s":1.0,"k":"pelicula","fin":"s_mayo"},
   {"tipo":"telefono","x":3540,"y":1500,"s":1.1,"k":"segundo","z":1800,"fin":"s_sum"},
   {"tipo":"consola","x":3300,"y":1690,"s":1.1,"k":"s_mayo","fin":"s_sum"},
   {"tipo":"documento","x":4780,"y":1160,"s":1.0,"sello":"OFICIAL","selloc":"verde","k":"plataformas","cae":True,"z":1800,"fin":"s_gano"},
   {"tipo":"trofeo","x":6100,"y":1640,"s":1.1,"k":"gano","cae":True,"fin":"s_loco"},
   {"tipo":"documento","x":7420,"y":1130,"s":0.95,"sello":"19 NOV 2026","selloc":"rojo","k":"medio","cae":True,"z":1800},
   {"tipo":"cronometro","x":7400,"y":1620,"s":0.8,"texto":"1,5 AÑOS","k":"medio+0.3","z":1800,"late":0.04}]
A=[{**CI,"hasta":"s_rec","keys":[{"k":0,"x":380,"y":1700,"pose":"cruzado","cara":"feliz"},{"k":"humillo","x":380,"y":1700,"pose":"piensa","cara":"sorpresa","fx":"tiembla"},{"k":"solo","x":380,"y":1700,"pose":"cruzado","cara":"triste"}]},
   {**CI,"desde":"s_rec","hasta":"s_mayo","keys":[{"k":"s_rec","x":1680,"y":1700,"pose":"celebra","cara":"risa"},{"k":"con","x":1680,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**JU,"desde":"s_mayo","hasta":"s_sum","keys":[{"k":"s_mayo","x":2460,"y":1700,"a":[2960,1700],"dur":1.3,"ease":"eio","pose":"telefono","cara":"feliz"},{"k":"segundo","x":2960,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {"look":"ejecutivo","var":82,"camisa":"#263238","pelo":"#3e2723","s":1.0,"desde":"s_sum","hasta":"s_gano","keys":[{"k":"s_sum","x":4300,"y":1700,"pose":"telefono","cara":"feliz"},{"k":"llego","x":4300,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {**GAM,"desde":"s_gano","hasta":"s_loco","keys":[{"k":"s_gano","x":5560,"y":1700,"pose":"juega","cara":"feliz","objeto":"control"},{"k":"gano","x":5560,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {**GAM,"desde":"s_loco","keys":[{"k":"s_loco","x":6860,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"loco","x":6860,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"saliera","x":6860,"y":1700,"pose":"cruzado","cara":"sorpresa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"estudio"},{"x0":1300,"x1":2600,"set":"calle","k":"s_rec"},{"x0":2600,"x1":3900,"set":"sala","k":"s_mayo"},
          {"x0":3900,"x1":5200,"set":"oficina","k":"s_sum"},{"x0":5200,"x1":6500,"set":"sala","k":"s_gano"},{"x0":6500,"x1":7900,"set":"calle","k":"s_loco"}],
 "pan":[{"k":"s_rec","x":1300,"dur":0.8},{"k":"s_mayo","x":2600,"dur":0.8},{"k":"s_sum","x":3900,"dur":0.8},{"k":"s_gano","x":5200,"dur":0.8},{"k":"s_loco","x":6500,"dur":0.8}],
 "props":P,"actores":A,
 "prohibidos":[{"k":"humillo","x":800,"y":1590,"r":150}],
 "burbujas":[{"k":"saliera","de":5,"texto":"¡NI SALÍA!","fin":"s_fin","dx":150}],
 "numeros":[{"k":"llego","n":475,"suf":" M","c":"amar","etq":"VISTAS EN 24 HORAS","fin":"s_gano"}],
 "zoom":[],"planos_hint":[{"k":"solo","tipo":"primer","var":86}],
 "sacudidas":[{"k":"humillo","f":14},{"k":"llego","f":14},{"k":"loco","f":10}],
 "titulos":[{"k":0.15,"texto":"HUMILLADO","c":"rojo","grande":True,"fin":"hizo"},
            {"k":"s_rec","texto":"1 · EL RÉCORD DEL CINE","c":"amar","fin":"con"},
            {"k":"s_mayo","texto":"2 · MAYO 2025","c":"cian","fin":"s_sum"},
            {"k":"s_sum","texto":"3 · EL RESULTADO","c":"verde","fin":"llego"},
            {"k":"s_gano","texto":"JUEGO 1 · CINE 0","c":"rosa","grande":True,"fin":"gano"},
            {"k":"s_loco","texto":"4 · LO MÁS LOCO","c":"rojo","fin":"medio"}],
 "chips":[{"k":"plataformas","texto":"TODAS LAS PLATAFORMAS","c":"cian","fin":"llego"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"¿LO VISTE ESE DÍA?","cierre2":"Comenta: sí o no","paises":["SÍ","NO"],"sfx":[],"cta":"SIGUE EL CANAL","like":"LIKE"}
poner_sets(E,[("escenarioV",{}),("nocheV",{"sem":7,"ciudad":True}),("cuartoGamerV",{"era":"2025"}),("corporativoV",{"ticker":"TTWO ▲","hora":"tarde"}),("salaV",{"hora":"noche","sinSofa":True,"var":3,"pared":["#3a2a5a","#241a3a"]}),("casaPalmasV",{"hora":"tarde","sinCasa":True})])
insertar(E,"hizo","s_rec",1300,"vitrinaV",{"fondo":["#3a0d0d","#1c0606","#080202"],"luz2":"255,150,150","pedestal":True},[{"tipo":"claqueta","x":540,"y":1380,"s":2.1,"texto":"HOLLYWOOD"}])
insertar(E,"con","s_mayo",2600,"vitrinaV",{"fondo":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220"},[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"RÉCORD · 24 HORAS","dato":"365 MILLONES","sello":"CINE","selloc":"amar","filaDato":6}])
insertar(E,"gano","s_loco",6500,"vitrinaV",{"fondo":["#5a2a7a","#2a1040","#0a0414"],"luz2":"255,120,220"},[{"tipo":"barras2","x":540,"y":1650,"s":1.6,"a":[365,"CINE","#78909c"],"b":[475,"GTA 6","#ff4081"],"suf":" M"}])
insertar(E,"medio","saliera",6500,"vitrinaV",{"fondo":["#1d1440","#0d0820","#030108"],"luz2":"200,150,255"},[{"tipo":"cronometro","x":540,"y":1620,"s":1.9,"texto":"1,5 AÑOS"}])
g={"titulo":"GTA 6 humilló a Hollywood 🎬👎","texto_pantalla":"HUMILLÓ A HOLLYWOOD","lote":"G2026112403","marca":"VICEVERSO GG",
"nota_datos":"Formato nuevo (24-nov). Tráiler 2 de GTA VI (6-may-2025): más de 475 millones de vistas en 24 horas sumando todas las plataformas (Rockstar; presentación a inversionistas de Take-Two, ago-2026, citada por FandomWire). Récord anterior: tráiler de Deadpool & Wolverine, 365 millones en 24 h (The Hollywood Reporter). 475-365 = 110 → 'más de 100 millones'. GTA VI salió el 19-nov-2026: 18 meses después. 'Humilló' es figura del título; el video la paga con las cifras. Disparador: rivalidad.",
"frases":frases,"frases_voz":voz,"fuentes":["https://fandomwire.com/every-record-gta-6-has-officially-broken-so-far/","https://www.hollywoodreporter.com/"],"escena":E}
guardar("G2026112403_src.json",g)
