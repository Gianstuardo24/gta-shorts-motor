import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Nobody can open this door in GTA 6. And it belongs to one of TV's most dangerous characters.",
"It's on Washington Island: a small blue building by the water.",
"Second floor. Last door on the left.",
"The door is locked, and so far no player has found a way in.",
"Then fans noticed the building looks almost exactly like one from TV.",
"It's the apartment of Dexter: television's famous serial killer.",
"And here is the detail that sold it.",
"At the dock next door, there's a boat named Slice of Life. The same name as his.",
"Tell me what you think is behind that door.",
"Follow for more GTA 6 secrets."]
voz=[f.replace("GTA 6","G T A six").replace("TV","T V") for f in frases]
M=[["nobody",0,"^nobody"],["door0",0,"^door"],["belongs",0,"^belongs"],["dangerous",0,"^dangerous"],
["s_isl",1,None],["island",1,"^island"],["blue",1,"^blue"],
["s_floor",2,None],["second",2,"^second"],["last",2,"^last"],
["s_lock",3,None],["locked",3,"^locked"],["way",3,"^way"],
["s_fans",4,None],["noticed",4,"^noticed"],["exactly",4,"^exactly"],
["s_dex",5,None],["dexter",5,"^dexter"],["killer",5,"^killer"],
["s_det",6,None],["detail",6,"^detail"],
["s_dock",7,None],["boat",7,"^boat"],["slice",7,"^slice"],["same",7,"^same"],
["s_fin",8,None],["s_cta",9,None]]
F1=dict(look="gamer",var=91,pelo="#3e2723",camisa="#e53935",lentes=False,s=0.97)
F2=dict(look="jugadora",var=92,pelo="#d7a86e",peloT="cola",camisa="#00897b",s=0.97)
P=[{"tipo":"puerta","x":760,"y":1700,"s":1.25,"k":0.0,"fin":"s_isl"},
   {"tipo":"candado","x":760,"y":1480,"s":0.55,"sacude":True,"k":"nobody","z":1800,"fin":"s_isl"},
   {"tipo":"cartel","x":1960,"y":1160,"s":0.85,"texto":"WASHINGTON ISLAND","k":"island","cae":True,"z":1800,"fin":"s_floor"},
   {"tipo":"puerta","x":3450,"y":1700,"s":1.25,"k":"s_floor","fin":"s_fans"},
   {"tipo":"candado","x":3450,"y":1480,"s":0.55,"sacude":True,"k":"locked","z":1800,"fin":"s_fans"},
   {"tipo":"tv","x":4780,"y":1290,"s":1.2,"k":"noticed","fin":"s_dex"},
   {"tipo":"claqueta","x":6080,"y":1690,"s":1.0,"texto":"TV SHOW","k":"s_dex","fin":"s_dock"},
   {"tipo":"muelle","x":7150,"y":1740,"s":1.2,"k":"s_dock"},
   {"tipo":"jetski","x":7250,"y":1660,"s":1.1,"k":"boat","mece":0.03,"flota":6},
   {"tipo":"cartel","x":6900,"y":1180,"s":1.0,"texto":"SLICE OF LIFE","k":"slice","cae":True,"z":1800}]
A=[{**F1,"hasta":"s_isl","keys":[{"k":0,"x":330,"y":1700,"pose":"empuja","cara":"neutral"},{"k":"nobody","x":330,"y":1700,"pose":"golpea","cara":"enojado"},{"k":"belongs","x":330,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {**F2,"desde":"s_isl","hasta":"s_floor","keys":[{"k":"s_isl","x":1160,"y":1700,"a":[1620,1700],"dur":1.3,"ease":"eio","pose":"apunta","cara":"feliz"},{"k":"blue","x":1620,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**F2,"desde":"s_floor","hasta":"s_fans","keys":[{"k":"s_floor","x":2460,"y":1700,"a":[3060,1700],"dur":1.5,"ease":"eio","pose":"parado","cara":"neutral"},{"k":"s_lock","x":3060,"y":1700,"pose":"empuja","cara":"neutral"},{"k":"locked","x":3060,"y":1700,"pose":"golpea","cara":"enojado"},{"k":"way","x":3060,"y":1700,"pose":"piensa","cara":"triste"}]},
   {**F1,"desde":"s_fans","hasta":"s_dex","keys":[{"k":"s_fans","x":4260,"y":1700,"pose":"juega","cara":"neutral","objeto":"control"},{"k":"exactly","x":4260,"y":1700,"pose":"apunta","cara":"sorpresa","fx":"brinca"}]},
   {**F1,"desde":"s_dex","hasta":"s_dock","keys":[{"k":"s_dex","x":5560,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"killer","x":5560,"y":1700,"pose":"cruzado","cara":"sorpresa","fx":"tiembla"},{"k":"detail","x":5560,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**F2,"desde":"s_dock","keys":[{"k":"s_dock","x":6760,"y":1700,"pose":"parado","cara":"neutral"},{"k":"slice","x":6760,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"same","x":6760,"y":1700,"pose":"celebra","cara":"risa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle"},{"x0":1300,"x1":2600,"set":"calle","k":"s_isl"},{"x0":2600,"x1":3900,"set":"sala","k":"s_floor"},
          {"x0":3900,"x1":5200,"set":"sala","k":"s_fans"},{"x0":5200,"x1":6500,"set":"estudio","k":"s_dex"},{"x0":6500,"x1":7900,"set":"cielo","k":"s_dock"}],
 "pan":[{"k":"s_isl","x":1300,"dur":0.8},{"k":"s_floor","x":2600,"dur":0.8},{"k":"s_fans","x":3900,"dur":0.8},{"k":"s_dex","x":5200,"dur":0.8},{"k":"s_dock","x":6500,"dur":0.8}],
 "props":P,"actores":A,
 "burbujas":[{"k":"way","de":2,"texto":"NO WAY IN.","fin":"s_fans","dx":-40}],
 "numeros":[],
 "zoom":[],"planos_hint":[{"k":"killer","tipo":"primer","var":91}],
 "sacudidas":[{"k":"nobody","f":14},{"k":"dexter","f":16},{"k":"slice","f":10}],
 "titulos":[{"k":0.15,"texto":"LOCKED","c":"rojo","grande":True,"fin":"belongs"},
            {"k":"s_isl","texto":"1 · WHERE IT IS","c":"cian","fin":"s_floor"},
            {"k":"s_floor","texto":"2 · THE DOOR","c":"amar","fin":"s_fans"},
            {"k":"s_fans","texto":"3 · THE CLUE","c":"verde","fin":"s_dex"},
            {"k":"dexter","texto":"DEXTER","c":"rojo","grande":True,"fin":"s_det"},
            {"k":"s_det","texto":"4 · THE DETAIL","c":"rosa","fin":"s_dock"}],
 "chips":[{"k":"blue","texto":"SMALL BLUE BUILDING","c":"cian","fin":"s_floor"},
          {"k":"last","texto":"2ND FLOOR · LAST DOOR, LEFT","c":"amar","fin":"s_lock"},
          {"k":"same","texto":"SAME NAME AS HIS BOAT","c":"rosa","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WHAT'S INSIDE?","cierre2":"Your guess. Comment","paises":["NOTHING","A MISSION","A SECRET"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[("nocheV",{"sem":61,"ciudad":True}),("parqueV",{"hora":"dia"}),("salaV",{"hora":"noche","sinSofa":True,"var":1,"pared":["#2a3350","#1a2138"]}),("cuartoGamerV",{"era":"2026"}),("escenarioV",{}),("casaPalmasV",{"hora":"tarde","sinCasa":True})])
quitar_props(E,["tv"])
insertar(E,"door0","belongs",0,"vitrinaV",{"fondo":["#12324a","#0a1c2c","#03080e"],"luz2":"190,230,255"},[{"tipo":"puerta","x":540,"y":1720,"s":2.3},{"tipo":"candado","x":540,"y":1330,"s":1.0,"sacude":True}])
insertar(E,"last","s_lock",2600,"vitrinaV",{"fondo":["#3a2a12","#1c1408","#080502"],"luz2":"255,220,150"},[{"tipo":"candado","x":540,"y":1500,"s":2.4,"sacude":True}])
insertar(E,"dexter","s_det",5200,"vitrinaV",{"fondo":["#3a0d0d","#1c0606","#080202"],"luz2":"255,150,150","pedestal":True},[{"tipo":"claqueta","x":540,"y":1380,"s":2.1,"texto":"DEXTER"}])
insertar(E,"slice","same",6500,"vitrinaV",{"fondo":["#ff8a50","#b23c17","#2a0a02"],"luz2":"255,220,190"},[{"tipo":"jetski","x":540,"y":1520,"s":2.4,"flota":10,"mece":0.04},{"tipo":"cartel","x":540,"y":1120,"s":1.5,"texto":"SLICE OF LIFE"}])
g={"titulo":"Nobody Can Open This Door in GTA 6 🚪🔒","texto_pantalla":"NOBODY CAN OPEN IT","lote":"G2026112403en","marca":"THE VICEVERSE GG",
"nota_datos":"Formato nuevo (24-nov). En Washington Island (este de Vice City) hay un edificio azul pequeño; segundo piso, último departamento a la izquierda: la puerta está cerrada y nadie ha logrado entrar. Los fans lo identifican como casi idéntico al complejo de departamentos de la serie Dexter (personaje: asesino en serie de la TV); en el muelle hay un bote llamado 'Slice of Life', igual que el del personaje. Sin confirmación de Rockstar. No se muestran imágenes ni personajes de la serie. Fuentes: esports.gg; Quero Bolsa (lista de 44 easter eggs, #5). Disparador: prohibido + misterio.",
"frases":frases,"frases_voz":voz,"fuentes":["https://esports.gg/news/grand-theft-auto-6/gta-6-fans-think-theyve-spotted-a-dexter-morgan-easter-egg/","https://querobolsa.com.br/revista/easter-eggs-de-gta-6"],"escena":E}
guardar("G2026112403en_src.json",g)
