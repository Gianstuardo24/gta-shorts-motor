import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["GTA 6 hid a famous TV apartment in Vice City.",
"Go to Washington Island and find a small blue building by the water.",
"Take the stairs to the second floor. It's the last door on the left.",
"Fans say it matches the apartment from the show Dexter, almost exactly.",
"And at the dock nearby, there's a boat called Slice of Life. Same name as his.",
"The door is locked. For now, nobody has found a way in.",
"Tell me what you think is behind that door.",
"Follow for more GTA 6 secrets."]
voz=[f.replace("GTA 6","G T A six") for f in frases]
M=[["hid",0,"^hid"],["apartment0",0,"^apartment"],
["s_go",1,None],["island",1,"^island"],["blue",1,"^blue"],
["s_stairs",2,None],["second",2,"^second"],["last",2,"^last"],
["s_fans",3,None],["matches",3,"^matches"],["dexter",3,"^dexter"],
["s_dock",4,None],["boat",4,"^boat"],["slice",4,"^slice"],["same",4,"^same"],
["s_lock",5,None],["locked",5,"^locked"],["nobody",5,"^nobody"],
["s_fin",6,None],["s_cta",7,None]]
F1=dict(look="gamer",var=91,pelo="#3e2723",camisa="#e53935",lentes=False,s=0.97)
F2=dict(look="jugadora",var=92,pelo="#d7a86e",peloT="cola",camisa="#00897b",s=0.97)
P=[{"tipo":"puerta","x":800,"y":1700,"s":1.1,"k":0.0,"fin":"s_go"},
   {"tipo":"cartel","x":2000,"y":1180,"s":1.0,"texto":"WASHINGTON ISLAND","k":"island","fin":"s_stairs"},
   {"tipo":"puerta","x":3450,"y":1700,"s":1.1,"k":"s_stairs","fin":"s_fans"},
   {"tipo":"tv","x":4800,"y":1280,"s":1.3,"k":"s_fans","fin":"s_dock"},
   {"tipo":"documento","x":4300,"y":1130,"s":0.9,"sello":"MATCH","selloc":"verde","k":"matches","cae":True,"z":1800,"fin":"s_dock"},
   {"tipo":"muelle","x":5950,"y":1740,"s":1.2,"k":"s_dock","fin":"s_lock"},
   {"tipo":"jetski","x":6050,"y":1660,"s":1.1,"k":"boat","fin":"s_lock"},
   {"tipo":"puerta","x":7350,"y":1700,"s":1.2,"k":"s_lock"},
   {"tipo":"documento","x":7350,"y":1130,"s":0.95,"sello":"LOCKED","selloc":"rojo","k":"locked","cae":True,"z":1800}]
A=[{**F1,"hasta":"s_go","keys":[{"k":0,"x":320,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"apartment0","x":320,"y":1700,"pose":"piensa","cara":"neutral"}]},
   {**F2,"desde":"s_go","hasta":"s_stairs","keys":[{"k":"s_go","x":1380,"y":1700,"pose":"camina","cara":"feliz"},{"k":"island","x":1600,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**F2,"desde":"s_stairs","hasta":"s_fans","keys":[{"k":"s_stairs","x":2700,"y":1700,"pose":"camina","cara":"neutral"},{"k":"last","x":3080,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**F1,"desde":"s_fans","hasta":"s_dock","keys":[{"k":"s_fans","x":4260,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"dexter","x":4260,"y":1700,"pose":"apunta","cara":"sorpresa","fx":"brinca"}]},
   {**F2,"desde":"s_dock","hasta":"s_lock","keys":[{"k":"s_dock","x":5520,"y":1700,"pose":"parado","cara":"neutral"},{"k":"slice","x":5520,"y":1700,"pose":"apunta","cara":"risa"}]},
   {**F1,"desde":"s_lock","keys":[{"k":"s_lock","x":6860,"y":1700,"pose":"empuja","cara":"neutral"},{"k":"locked","x":6860,"y":1700,"pose":"golpea","cara":"enojado"},{"k":"nobody","x":6860,"y":1700,"pose":"piensa","cara":"neutral"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle","luz":"tenue"},{"x0":1300,"x1":2600,"set":"calle","k":"s_go"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_stairs","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"sala","k":"s_fans"},{"x0":5200,"x1":6500,"set":"cielo","k":"s_dock"},{"x0":6500,"x1":7900,"set":"oficina","k":"s_lock","luz":"tenue"}],
 "pan":[{"k":"s_go","x":1300,"dur":0.9},{"k":"s_stairs","x":2600,"dur":0.9},{"k":"s_fans","x":3900,"dur":0.9},{"k":"s_dock","x":5200,"dur":0.9},{"k":"s_lock","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"nobody","de":5,"texto":"NO WAY IN.","fin":"s_fin","dx":150}],
 "numeros":[],
 "zoom":[{"k":0.1,"s":1.12,"x":560,"y":1450,"dur":0.6},{"k":"apartment0","s":1.0,"dur":0.3},{"k":"s_stairs","s":1.0,"dur":0.3},
         {"k":"last","s":1.18,"x":3300,"y":1500,"dur":0.4},{"k":"s_fans","s":1.0,"dur":0.3},{"k":"dexter","s":1.22,"x":4320,"y":1420,"dur":0.4},{"k":"s_dock","s":1.0,"dur":0.3},
         {"k":"boat","s":1.1,"x":5800,"y":1550,"dur":0.4},{"k":"s_lock","s":1.0,"dur":0.3},{"k":"locked","s":1.12,"x":7120,"y":1450,"dur":0.4},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"locked","f":14}],
 "titulos":[{"k":0.2,"texto":"A FAMOUS TV APARTMENT","c":"amar","fin":"s_go"},
            {"k":"s_go","texto":"STEP 1","c":"cian","fin":"s_stairs"},
            {"k":"s_stairs","texto":"STEP 2","c":"cian","fin":"s_fans"},
            {"k":"s_fans","texto":"THE MATCH","c":"verde","grande":True,"fin":"s_dock"},
            {"k":"s_dock","texto":"THE BOAT","c":"rosa","grande":True,"fin":"s_lock"},
            {"k":"s_lock","texto":"LOCKED","c":"rojo","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"blue","texto":"SMALL BLUE BUILDING","c":"cian","fin":"s_stairs"},
          {"k":"last","texto":"2ND FLOOR · LAST DOOR, LEFT","c":"amar","fin":"s_fans"},
          {"k":"slice","texto":"\"SLICE OF LIFE\"","c":"rosa","fin":"s_lock"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WHAT'S INSIDE?","cierre2":"Your guess. Comment","paises":["NOTHING","A MISSION","A SECRET"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[("nocheV",{"sem":61,"ciudad":True}),("casaPalmasV",{"hora":"dia","sinCasa":True}),None,("salaV",{"hora":"noche","sinSofa":True,"var":2,"pared":["#2a3350","#1a2138"]}),("casaPalmasV",{"hora":"tarde","sinCasa":True}),None])
quitar_props(E,["tv"])
insertar(E,"hid","s_go",1300,"vitrinaV",{"fondo":["#12324a","#0a1c2c","#03080e"],"luz2":"190,230,255"},[{"tipo":"puerta","x":540,"y":1650,"s":2.0}])
insertar(E,"slice","s_lock",6500,"vitrinaV",{"fondo":["#ff8a50","#b23c17","#2a0a02"],"luz2":"255,220,190"},[{"tipo":"jetski","x":540,"y":1500,"s":2.4}])
g={"titulo":"GTA 6 Hid Dexter's Apartment 🚪","texto_pantalla":"THE LOCKED DOOR","lote":"G2026112401en","marca":"THE VICEVERSE GG",
"nota_datos":"Micronicho EN: secretos. En Washington Island (este de Vice City) hay un edificio azul pequeño; en el segundo piso, último departamento a la izquierda, la puerta está cerrada. Los fans lo identifican como casi idéntico al complejo de departamentos de la serie Dexter; en el muelle del lado oeste hay un bote llamado 'Slice of Life', igual que el del personaje. Sin confirmación de Rockstar; nadie ha logrado entrar. Fuentes: esports.gg; Quero Bolsa (lista de 44 easter eggs, #5). No se muestra al personaje ni imágenes de la serie.",
"frases":frases,"frases_voz":voz,"fuentes":["https://esports.gg/news/grand-theft-auto-6/gta-6-fans-think-theyve-spotted-a-dexter-morgan-easter-egg/","https://querobolsa.com.br/revista/easter-eggs-de-gta-6"],"escena":E}
guardar("G2026112401en_src.json",g)
