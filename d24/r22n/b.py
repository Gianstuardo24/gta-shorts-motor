import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Don't trust the Roswell story.",
"In 1947, a rancher in New Mexico found foil, rubber, and sticks on his land.",
"The Army announced it had recovered a flying disc.",
"One day later, it changed the story: just a weather balloon.",
"That was a cover story too. In 1994, the Air Force admitted the truth.",
"It was Project Mogul: secret balloons built to listen for Soviet nuclear tests.",
"Tell me if you think that is the whole story.",
"Follow for the next case."]
voz=[f.replace("1947","nineteen forty-seven").replace("1994","nineteen ninety-four") for f in frases]
M=[["dont",0,"^don"],["story0",0,"^story"],
["s_1947",1,None],["rancher",1,"^rancher"],["foil",1,"^foil"],["sticks",1,"^sticks"],
["s_army",2,None],["disc",2,"^disc"],
["s_day",3,None],["changed",3,"^changed"],["balloon",3,"^balloon"],
["s_cover",4,None],["y1994",4,"^1994"],["truth",4,"^truth"],
["s_mogul",5,None],["mogul",5,"^mogul"],["listen",5,"^listen"],["soviet",5,"^soviet"],
["s_fin",6,None],["s_cta",7,None]]
RA=dict(look="cliente",var=71,pelo="#6d4c41",camisa="#8d6e63",s=0.97)
OF=dict(look="ejecutivo",var=72,pelo="#3e2723",camisa="#556b2f",s=0.97)
P=[{"tipo":"ovni","x":560,"y":820,"s":1.1,"k":0.0,"fin":"s_1947"},
   {"tipo":"cajita","x":2080,"y":1700,"s":1.2,"color":"#b0bec5","texto":"FOIL","k":"foil","cae":True,"fin":"s_army"},
   {"tipo":"cajita","x":2230,"y":1705,"s":1.0,"color":"#5d4037","texto":"STICKS","k":"sticks","cae":True,"fin":"s_army"},
   {"tipo":"documento","x":3560,"y":1160,"s":0.95,"sello":"FLYING DISC","selloc":"amar","k":"disc","cae":True,"z":1800,"fin":"s_day"},
   {"tipo":"globos","x":4830,"y":1150,"s":1.2,"k":"balloon","z":1800,"fin":"s_cover"},
   {"tipo":"documento","x":6130,"y":1180,"s":1.0,"sello":"1994 REPORT","selloc":"amar","k":"y1994","cae":True,"z":1800,"fin":"s_mogul"},
   {"tipo":"globos","x":7200,"y":1000,"s":1.5,"k":"mogul","z":1800},
   {"tipo":"monitorOnda","x":7500,"y":1640,"s":1.0,"k":"listen"},
   {"tipo":"radar","x":7250,"y":1650,"s":0.9,"k":"soviet"}]
A=[{**RA,"hasta":"s_1947","keys":[{"k":0,"x":300,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"story0","x":300,"y":1700,"pose":"cruzado","cara":"neutral"}]},
   {**RA,"desde":"s_1947","hasta":"s_army","keys":[{"k":"s_1947","x":1370,"y":1700,"pose":"camina","cara":"neutral"},{"k":"s_1947+1.0","x":1680,"y":1700,"pose":"parado","cara":"neutral"},{"k":"foil","x":1680,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**OF,"desde":"s_army","hasta":"s_day","keys":[{"k":"s_army","x":3000,"y":1700,"pose":"sostiene","cara":"feliz","objeto":"documento"},{"k":"disc","x":3000,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**OF,"var":73,"desde":"s_day","hasta":"s_cover","keys":[{"k":"s_day","x":4300,"y":1700,"pose":"cruzado","cara":"neutral"},{"k":"balloon","x":4300,"y":1700,"pose":"apunta","cara":"neutral"}]},
   {"look":"ejecutivo","var":74,"s":0.97,"desde":"s_cover","hasta":"s_mogul","keys":[{"k":"s_cover","x":5580,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"truth","x":5580,"y":1700,"pose":"ofrece","cara":"neutral","objeto":"documento"}]},
   {"look":"inventor","var":75,"s":0.95,"lentes":True,"desde":"s_mogul","keys":[{"k":"s_mogul","x":6900,"y":1700,"pose":"apunta","cara":"neutral"},{"k":"listen","x":6900,"y":1700,"pose":"telefono","cara":"neutral"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.05,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle","luz":"tenue"},{"x0":1300,"x1":2600,"set":"calle","k":"s_1947"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_army"},
          {"x0":3900,"x1":5200,"set":"estudio","k":"s_day"},{"x0":5200,"x1":6500,"set":"oficina","k":"s_cover","luz":"tenue"},{"x0":6500,"x1":7900,"set":"garage","k":"s_mogul"}],
 "pan":[{"k":"s_1947","x":1300,"dur":0.9},{"k":"s_army","x":2600,"dur":0.9},{"k":"s_day","x":3900,"dur":0.9},{"k":"s_cover","x":5200,"dur":0.9},{"k":"s_mogul","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"changed","de":3,"texto":"JUST A BALLOON.","fin":"s_cover","dx":150}],
 "numeros":[],
  "zoom":[],
 "sacudidas":[{"k":"dont","f":14},{"k":"mogul","f":12}],
 "titulos":[{"k":0.15,"texto":"DON'T TRUST IT","c":"rojo","grande":True,"fin":"s_1947"},
            {"k":"s_1947","texto":"NEW MEXICO","c":"amar","fin":"s_army"},
            {"k":"s_army","texto":"STORY 1: A DISC","c":"cian","fin":"s_day"},
            {"k":"s_day","texto":"STORY 2: A BALLOON","c":"verde","fin":"s_cover"},
            {"k":"s_cover","texto":"ALSO A COVER STORY","c":"rojo","fin":"y1994"},
            {"k":"mogul","texto":"PROJECT MOGUL","c":"amar","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"sticks","texto":"FOIL · RUBBER · STICKS","c":"cian","fin":"s_army"},
          {"k":"soviet","texto":"LISTENING FOR NUCLEAR TESTS","c":"rojo","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"THE WHOLE STORY?","cierre2":"Yes or no? Comment","paises":["YES","NO"],
 "sfx":[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.0,"fade":0.4,"g":0.08}],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[("nocheV",{"sem":47,"ciudad":False,"montes":True}),("parqueV",{"hora":"tarde"}),None,None,("investigaV",{}),("hangarV",{})])
insertar(E,"story0","s_1947",1300,"vitrinaV",{"fondo":["#12301e","#0a1c12","#030806"],"luz2":"150,255,190"},[{"tipo":"ovni","x":540,"y":1250,"s":2.4}])
insertar(E,"rancher","foil",1300,"vitrinaV",{"fondo":["#c9a26a","#7a5a2c","#1c1206"],"luz2":"255,230,180"},[{"tipo":"cajita","x":540,"y":1500,"s":3.0,"color":"#b0bec5","texto":"DEBRIS"}])
insertar(E,"y1994","s_mogul",6500,"vitrinaV",{"fondo":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220"},[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"AIR FORCE REPORT","dato":"BALLOON STORY: A COVER","sello":"1994","selloc":"rojo","filaDato":6}])
insertar(E,"balloon","s_cover",5200,"vitrinaV",{"fondo":["#8fc3e8","#3a6a9a","#0a1a2a"],"luz2":"230,245,255"},[{"tipo":"globos","x":540,"y":1250,"s":2.4}])
g={"titulo":"Don't Trust the Roswell Story 👽❓","texto_pantalla":"DON'T TRUST IT","lote":"R2026112403","marca":"THE RABBIT LOOP",
"nota_datos":"Roswell, 1947: el ranchero W. 'Mac' Brazel encontró restos (papel metálico, goma, cinta, palos de madera) en su rancho cerca de Corona, Nuevo México. 8-jul-1947: la base aérea de Roswell anunció que había recuperado un 'disco volador'. En menos de un día el Ejército lo cambió por 'globo meteorológico'. 1994: informe de la Fuerza Aérea de EE.UU.: era un globo del Proyecto Mogul, programa secreto de globos de gran altura para detectar pruebas nucleares soviéticas; reconoce que lo del globo meteorológico fue una tapadera. Fuentes: USAF 'The Roswell Report' (1994), Wikipedia (Roswell incident).",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/Roswell_incident","https://www.af.mil/"],"escena":E}
guardar("R2026112403_src.json",g)
