import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Red Dead Redemption 2 was hiding the name of GTA 6's map since 2018.",
"This January, fans digging through the game's files found a boat texture nobody had ever seen.",
"It had a ship name painted on it: The Leonida.",
"Leonida is the state where GTA 6 takes place.",
"The texture was never used in the game, so nobody noticed for 8 years.",
"Some fans call it a planned tease. Others say it's just a leftover. Rockstar has not said a word.",
"Tell me which one you believe.",
"Follow for more GTA 6 secrets."]
voz=[f.replace("Redemption 2","Redemption Two").replace("GTA 6","G T A six").replace("2018","twenty eighteen").replace("8 years","eight years") for f in frases]
M=[["hiding",0,"^hiding"],["name0",0,"^name"],["y2018",0,"^2018"],
["s_jan",1,None],["files",1,"^files"],["boat",1,"^boat"],["nobody1",1,"^nobody"],
["s_name",2,None],["painted",2,"^painted"],["leonida",2,"^leonida"],
["s_state",3,None],["state",3,"^state"],
["s_unused",4,None],["never",4,"^never"],["y8",4,"^8"],
["s_fans",5,None],["tease",5,"^tease"],["leftover",5,"^leftover"],["rockstar",5,"^rockstar"],
["s_fin",6,None],["s_cta",7,None]]
F1=dict(look="gamer",var=91,pelo="#3e2723",camisa="#e53935",s=0.95)
F2=dict(look="jugadora",var=92,pelo="#d7a86e",peloT="cola",camisa="#00897b",s=0.95)
P=[{"tipo":"consola","x":760,"y":1690,"s":1.1,"k":0.0,"fin":"s_jan"},
   {"tipo":"documento","x":800,"y":1150,"s":0.95,"sello":"RDR2 · 2018","selloc":"amar","k":"y2018","cae":True,"z":1800,"fin":"s_jan"},
   {"tipo":"pc","x":1950,"y":1650,"s":1.2,"texto":"RDR2 FILES","k":"s_jan","fin":"s_name"},
   {"tipo":"lupa","x":2230,"y":1250,"s":1.3,"k":"files","z":1800,"fin":"s_name"},
   {"tipo":"muelle","x":3300,"y":1730,"s":1.2,"k":"s_name","fin":"s_state"},
   {"tipo":"cartel","x":3250,"y":1180,"s":1.3,"texto":"THE LEONIDA","k":"leonida","cae":True,"z":1800,"fin":"s_state"},
   {"tipo":"cartel","x":4650,"y":1180,"s":1.2,"texto":"WELCOME TO LEONIDA","k":"state","fin":"s_unused"},
   {"tipo":"documento","x":5850,"y":1180,"s":1.0,"sello":"UNUSED","selloc":"rojo","k":"never","cae":True,"z":1800,"fin":"s_fans"},
   {"tipo":"cronometro","x":6130,"y":1560,"s":0.9,"texto":"8 YEARS","k":"y8","z":1800,"fin":"s_fans"}]
A=[{**F1,"hasta":"s_jan","keys":[{"k":0,"x":330,"y":1700,"pose":"juega","cara":"feliz","objeto":"control"},{"k":"name0","x":330,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {**F2,"desde":"s_jan","hasta":"s_name","keys":[{"k":"s_jan","x":1380,"y":1700,"pose":"camina","cara":"neutral"},{"k":"s_jan+0.9","x":1640,"y":1700,"pose":"sostiene","cara":"neutral","objeto":"lupa"},{"k":"boat","x":1640,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**F1,"desde":"s_name","hasta":"s_state","keys":[{"k":"s_name","x":2900,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"leonida","x":2900,"y":1700,"pose":"apunta","cara":"sorpresa","fx":"brinca"}]},
   {**F2,"desde":"s_state","hasta":"s_unused","keys":[{"k":"s_state","x":4250,"y":1700,"pose":"saluda","cara":"feliz"},{"k":"state","x":4250,"y":1700,"pose":"apunta","cara":"risa"}]},
   {**F1,"desde":"s_unused","hasta":"s_fans","keys":[{"k":"s_unused","x":5520,"y":1700,"pose":"cruzado","cara":"neutral"},{"k":"y8","x":5520,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {**F2,"desde":"s_fans","keys":[{"k":"s_fans","x":6820,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"rockstar","x":6820,"y":1700,"pose":"piensa","cara":"neutral"}]},
   {**F1,"desde":"s_fans","keys":[{"k":"s_fans","x":7240,"y":1700,"pose":"parado","cara":"neutral","dir":-1},{"k":"leftover","x":7240,"y":1700,"pose":"cruzado","cara":"neutral","dir":-1}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_jan","luz":"tenue"},{"x0":2600,"x1":3900,"set":"cielo","k":"s_name"},
          {"x0":3900,"x1":5200,"set":"calle","k":"s_state"},{"x0":5200,"x1":6500,"set":"oficina","k":"s_unused","luz":"tenue"},{"x0":6500,"x1":7900,"set":"sala","k":"s_fans"}],
 "pan":[{"k":"s_jan","x":1300,"dur":0.9},{"k":"s_name","x":2600,"dur":0.9},{"k":"s_state","x":3900,"dur":0.9},{"k":"s_unused","x":5200,"dur":0.9},{"k":"s_fans","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"tease","de":5,"texto":"PLANNED.","fin":"leftover","dx":40},{"k":"leftover","de":6,"texto":"LEFTOVER.","fin":"s_fin","dx":-170}],
 "numeros":[{"k":"y8","n":8,"suf":" YEARS","c":"cian","etq":"UNNOTICED","fin":"s_fans"}],
 "zoom":[{"k":0.1,"s":1.12,"x":420,"y":1450,"dur":0.6},{"k":"y2018","s":1.0,"dur":0.4},{"k":"boat","s":1.2,"x":1900,"y":1450,"dur":0.4},{"k":"s_name","s":1.0,"dur":0.3},
         {"k":"s_state","s":1.0,"dur":0.3},{"k":"state","s":1.12,"x":4500,"y":1500,"dur":0.5},{"k":"s_unused","s":1.0,"dur":0.3},
         {"k":"never","s":1.15,"x":5800,"y":1350,"dur":0.4},{"k":"y8","s":1.0,"dur":0.3},{"k":"rockstar","s":1.1,"x":7060,"y":1450,"dur":0.5},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"leonida","f":14}],
 "titulos":[{"k":0.2,"texto":"HIDDEN SINCE 2018","c":"amar","fin":"s_jan"},
            {"k":"s_jan","texto":"JANUARY 2026","c":"cian","fin":"s_name"},
            {"k":"leonida","texto":"THE LEONIDA","c":"rosa","grande":True,"fin":"s_state"},
            {"k":"s_state","texto":"GTA 6'S STATE","c":"verde","fin":"s_unused"},
            {"k":"s_unused","texto":"NEVER USED","c":"rojo","fin":"s_fans"},
            {"k":"s_fans","texto":"TEASE OR LEFTOVER","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"boat","texto":"UNUSED BOAT TEXTURE","c":"cian","fin":"s_name"},
          {"k":"rockstar","texto":"ROCKSTAR: NO COMMENT","c":"rojo","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"TEASE OR LEFTOVER?","cierre2":"Which one? Comment","paises":["TEASE","LEFTOVER"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[("cuartoGamerV",{"era":"2018"}),None,("nocheV",{"sem":31,"ciudad":False,"montes":True}),("casaPalmasV",{"hora":"dia","sinCasa":True}),("labV",{"pantalla":"TEXTURE: UNUSED","pantalla2":"RDR2 · 2018"}),None])
insertar(E,"painted","s_state",3900,"vitrinaV",{"fondo":["#12324a","#0a1c2c","#03080e"],"luz2":"190,230,255"},[{"tipo":"cartel","x":540,"y":1250,"s":2.3,"texto":"THE LEONIDA"}])
insertar(E,"files","boat",1300,"mesaCenitalV",{"titulo":"RDR2 · GAME FILES","monto":"boat_texture","firma":"files"},[])
g={"titulo":"RDR2 Hid a GTA 6 Secret for 8 Years 🚢","texto_pantalla":"HIDDEN SINCE 2018","lote":"G2026112402en","marca":"THE VICEVERSE GG",
"nota_datos":"Micronicho EN: secretos. En enero de 2026 (GameRoll en X, 24-ene-2026) se encontró en los archivos de Red Dead Redemption 2 (2018) una textura de bote parcialmente sin usar con nombres de barcos; uno es 'The Leonida'. Leonida es el estado de GTA 6. La textura no se usó en el juego. Sin confirmación de Rockstar: unos fans creen que fue un adelanto planeado, otros que es un sobrante de desarrollo. '8 años' = 2018→2026. Fuentes: Daily Dot (28-ene-2026), Attack of the Fanboy.",
"frases":frases,"frases_voz":voz,"fuentes":["https://dailydot.com/rdr2-gta6-the-leonida-easter-egg","https://attackofthefanboy.com/?p=1049353"],"escena":E}
guardar("G2026112402en_src.json",g)
