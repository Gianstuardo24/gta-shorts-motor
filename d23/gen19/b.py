import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["GTA 6 has a literal Easter egg.",
"Climb a giant radio tower in Leonida. It takes about seven minutes.",
"At the top, there's a bird's nest full of colorful eggs.",
"Grab one and throw it off the edge.",
"A secret cutscene shows it smash on a car's windshield below.",
"No cash, no mission. The joke is the prize.",
"Tell me if you'd make that climb.",
"Follow for more GTA 6 secrets."]
voz=[f.replace("GTA 6","GTA six") for f in frases]
M=[["egg0",0,"^egg"],
["s_climb",1,None],["tower",1,"^tower"],["leonida",1,"^leonida"],["seven",1,"^seven"],
["s_top",2,None],["nest",2,"^nest"],["colorful",2,"^colorful"],
["s_grab",3,None],["throw",3,"^throw"],["edge",3,"^edge"],
["s_cut",4,None],["smash",4,"^smash"],["wind",4,"^windshield"],
["s_prize",5,None],["joke",5,"^joke"],["prize",5,"^prize"],
["s_fin",6,None],["s_cta",7,None]]
J=dict(look="jugador",var=111,s=1.0,os=1.6)
P=[{"tipo":"torre","x":560,"y":1720,"s":1.0,"h":1650,"k":0.0,"fin":"s_top"},
   {"tipo":"huevo","x":840,"y":1350,"s":4.5,"color":"rosa","k":0.15,"cae":True,"z":1900,"fin":"s_climb"},
   {"tipo":"baranda","x":1790,"y":1735,"s":1.3,"k":"s_top","z":1650,"fin":"s_cut"},
   {"tipo":"nido","x":2000,"y":1715,"s":1.1,"k":"nest","cae":True,"z":1700,"fin":"s_cut"},
   {"tipo":"huevo","x":1700,"y":1430,"s":1.6,"color":"cian","k":"throw+0.15","z":1950,"fin":"s_cut","gira":9,
    "mov":[{"k":"throw+0.15","x":1700,"y":1430},{"k":"throw+0.55","x":2050,"y":1180},{"k":"throw+1.3","x":2450,"y":2300}]},
   {"tipo":"sedan","x":3250,"y":1600,"s":1.2,"color":"amar","k":"s_cut","z":1700,
    "mov":[{"k":"s_cut","x":2700,"y":1600},{"k":"smash","x":3250,"y":1600}]},
   {"tipo":"huevo","x":3298,"y":200,"s":1.6,"color":"cian","k":"s_cut+0.2","z":1950,"fin":"smash","gira":9,
    "mov":[{"k":"s_cut+0.2","x":3298,"y":150},{"k":"smash","x":3298,"y":1490}]},
   {"tipo":"huevo","x":3298,"y":1495,"s":1.0,"color":"cian","roto":True,"k":"smash","z":1960},
   {"tipo":"baranda","x":4440,"y":1735,"s":1.3,"k":"s_prize","z":1650},
   {"tipo":"nido","x":4650,"y":1715,"s":1.1,"n":4,"k":"s_prize","z":1700}]
A=[{**J,"hasta":"s_top","keys":[{"k":0,"x":330,"y":1700,"pose":"piensa","cara":"sorpresa","z":1900},
     {"k":"s_climb","x":330,"y":1700,"pose":"apunta","cara":"feliz","z":1900},
     {"k":"tower","x":330,"y":1700,"pose":"parado","cara":"feliz","a":[560,1700],"dur":0.6,"z":1900},
     {"k":"tower+0.6","x":560,"y":1700,"pose":"arriba","cara":"enojado","a":[560,1250],"dur":2.4,"z":1900},
     {"k":"tower+3.0","x":560,"y":1250,"pose":"arriba","cara":"triste","fx":"tiembla","z":1900}]},
   {**J,"desde":"s_top","hasta":"s_cut","keys":[{"k":"s_top","x":1620,"y":1712,"pose":"parado","cara":"neutral","z":1800},
     {"k":"nest","x":1620,"y":1712,"pose":"celebra","cara":"sorpresa","fx":"salto","z":1800},
     {"k":"s_grab","x":1620,"y":1712,"pose":"sostiene","cara":"risa","objeto":"huevo","z":1800},
     {"k":"throw","x":1620,"y":1712,"pose":"golpea","cara":"risa","objeto":"","z":1800}]},
   {"look":"cliente","var":112,"s":0.95,"desde":"s_cut","hasta":"s_prize","keys":[{"k":"s_cut","x":3560,"y":1710,"pose":"parado","cara":"neutral","dir":-1},{"k":"smash","x":3560,"y":1710,"pose":"apunta","cara":"risa","dir":-1,"fx":"brinca"}]},
   {**J,"desde":"s_prize","keys":[{"k":"s_prize","x":4200,"y":1712,"pose":"cruzado","cara":"neutral","z":1800},{"k":"joke","x":4200,"y":1712,"pose":"celebra","cara":"risa","fx":"brinca","z":1800}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.1,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle","luz":"tenue"},{"x0":1300,"x1":2600,"set":"cielo","k":"s_top"},{"x0":2600,"x1":3900,"set":"calle","k":"s_cut"},{"x0":3900,"x1":5200,"set":"cielo","k":"s_prize"}],
 "pan":[{"k":"s_top","x":1300,"dur":0.9},{"k":"s_cut","x":2700,"dur":0.9},{"k":"s_prize","x":3950,"dur":0.9}],
 "props":P,"actores":A,
 "numeros":[{"k":"seven","n":7,"suf":" MINUTES","c":"amar","etq":"ABOUT THIS LONG TO CLIMB","fin":"s_top"}],
 "zoom":[{"k":0.1,"s":1.06,"dur":0.6},{"k":"nest","s":1.15,"x":1900,"y":1500,"dur":0.4},{"k":"s_cut","s":1.0,"dur":0.4},
         {"k":"smash","s":1.25,"x":3300,"y":1500,"dur":0.25},{"k":"s_prize","s":1.0,"dur":0.4}],
 "sacudidas":[{"k":"smash","f":22}],
 "titulos":[{"k":0.2,"texto":"A LITERAL EASTER EGG","c":"rosa","fin":"s_climb"},
            {"k":"s_climb+0.35","texto":"THE RADIO TOWER","c":"cian","fin":"s_top"},
            {"k":"s_top","texto":"AT THE TOP","c":"amar","fin":"s_cut"},
            {"k":"s_cut","texto":"SECRET CUTSCENE","c":"rosa","fin":"s_prize"},
            {"k":"s_prize","texto":"THE REWARD?","c":"cian","fin":"joke"},
            {"k":"joke+0.3","texto":"THE JOKE","c":"amar","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"colorful","texto":"A NEST FULL OF EGGS","c":"verde","fin":"s_grab"},
          {"k":"edge","texto":"THROW IT","c":"rosa","fin":"s_cut"},
          {"k":"smash","texto":"SPLAT","c":"amar","fin":"s_prize"},
          {"k":"s_prize+0.3","texto":"NO CASH · NO MISSION","c":"rojo","fin":"joke"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WOULD YOU CLIMB IT?","cierre2":"Comment: yes or no","paises":["YES","NO"],
 "sfx":[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.1,"fade":0.5,"g":0.1},
        {"f":"extra/Whip_Whoosh_BW.11026.wav","k":"throw","off":0.0,"dur":0.8,"g":0.14},
        {"f":"extra/BRS_Comedy_Blip_Bubble_Burst_Small_1.wav","k":"smash","off":0.0,"dur":0.6,"g":0.16}],"cta":"FOLLOW FOR MORE"}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("torreV",{"hora":"tarde","sinTorre":True}),("torreV",{"cima":True,"hora":"tarde"}),("casaPalmasV",{"hora":"dia","sinCasa":True}),("torreV",{"cima":True,"hora":"noche"})])
e0=E["escenas"][0];e0["zoom"]=[z for z in e0["zoom"] if z["k"]!="smash"]
insertar(E,"smash","s_prize",3950,"vitrinaV",{"fondo":["#8fc3e8","#3a6a9a","#0a1a2a"],"luz2":"230,245,255"},[{"tipo":"huevoRoto","x":540,"y":1300,"s":2.0}])

g={"titulo":"GTA 6 Has a Literal Easter Egg 🥚","texto_pantalla":"LITERAL EASTER EGG","lote":"G2026112301en","marca":"THE VICEVERSE GG",
"nota_datos":"Micronicho EN: secretos. Torre de radio/comunicaciones en Leonida (games.gg: South Vice-Dale County radio tower). Subida ~7 minutos (IBTimes, video de xGarbett 18-nov-2026). Arriba: nido con huevos de colores; tomar uno y lanzarlo activa una cinemática: el huevo golpea el parabrisas de un auto abajo (IBTimes; ProdigyGamers). Sin objeto valioso ni recompensa de misión: el premio es la broma (IBTimes). Arriba también hay un influencer con paracaídas y reto de base jump (ProdigyGamers) — no se menciona.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.ibtimes.co.uk/gta-6-player-discovers-literal-easter-egg-leonida-1833342","https://prodigygamers.com/?p=37889","https://games.gg/grand-theft-auto-vi/guides/grand-theft-auto-6-easter-eggs-and-secrets-known-clues/"],"escena":E}
guardar("G2026112301en_src.json",g)
