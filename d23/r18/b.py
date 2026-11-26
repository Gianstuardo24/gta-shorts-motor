import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["This UFO photo fooled experts for 21 years. It was made of foam.",
"In April 1990, during a wave of UFO reports in Belgium, a photo of a black triangle with lights appeared.",
"Experts analyzed it again and again, and some said it looked real.",
"Then in 2011, the man who took it told Belgian TV it was a hoax.",
"He was 18. With friends, he cut a triangle of foam, painted it black, added lights, and hung it up.",
"The photo was fake. The wave of sightings in Belgium is still debated.",
"Tell me if you would have believed it.",
"Follow for the next case."]
voz=[f.replace("21 years","twenty-one years").replace("1990","nineteen ninety").replace("2011","twenty eleven").replace("He was 18.","He was eighteen.") for f in frases]
M=[["photo0",0,"^photo"],["fooled",0,"^fooled"],["foam0",0,"^foam"],["s_1990",1,None],["belgium",1,"^belgium"],["triangle1",1,"^triangle"],["lights1",1,"^lights"],
["s_exp",2,None],["analyzed",2,"^analyzed"],["real",2,"^real"],["s_2011",3,None],["tv",3,"^tv"],["hoax",3,"^hoax"],
["s_made",4,None],["cut",4,"^cut"],["painted",4,"^painted"],["added",4,"^added"],["hung",4,"^hung"],["s_fake",5,None],["fake",5,"^fake"],["debated",5,"^debated"],
["s_fin",6,None],["s_cta",7,None]]
def tri(cx,cy,k,fin,sc=1.0,z=None):
    pts=[(cx,cy-110*sc),(cx-130*sc,cy+90*sc),(cx+130*sc,cy+90*sc),(cx,cy+10*sc)]
    out=[]
    for i,(x,y) in enumerate(pts):
        o={"tipo":"orbe","x":x,"y":y,"s":0.95*sc if i<3 else 0.6*sc,"k":k if isinstance(k,str) else k,"fin":fin}
        if z: o["z"]=z
        out.append(o)
    return out
P=(tri(540,900,0.0,"s_exp")+
   [{"tipo":"pc","x":1950,"y":1650,"s":1.2,"k":"s_exp","texto":"PHOTO 1990","fin":"s_2011"},
    {"tipo":"documento","x":1950,"y":1130,"s":1.0,"sello":"REAL?","selloc":"amar","k":"real","cae":True,"z":1800,"fin":"s_2011"},
    {"tipo":"tv","x":3250,"y":1230,"s":1.3,"k":"s_2011","fin":"s_made"},
    {"tipo":"documento","x":3250,"y":1000,"s":0.9,"sello":"HOAX","selloc":"rojo","k":"hoax","cae":True,"z":1800,"fin":"s_made"},
    {"tipo":"cajita","x":4550,"y":1600,"s":2.2,"color":"#37474f","texto":"FOAM","k":"cut","z":1700,"fin":"s_fake"}]+
   tri(4550,1180,"added","s_fake",sc=0.9,z=1800)+
   tri(5850,1000,"s_fake","s_fin"))
A=[{"look":"cliente","var":81,"s":0.95,"hasta":"s_exp","keys":[{"k":0,"x":300,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"belgium","x":300,"y":1700,"pose":"telefono","cara":"sorpresa"}]},
   {"look":"jugadora","var":82,"s":0.95,"hasta":"s_exp","keys":[{"k":0,"x":780,"y":1705,"pose":"parado","cara":"sorpresa","dir":-1},{"k":"lights1","x":780,"y":1705,"pose":"piensa","cara":"sorpresa","dir":-1}]},
   {"look":"inventor","var":83,"s":0.95,"desde":"s_exp","hasta":"s_2011","lentes":True,"pelo":"#9e9e9e","peloT":"corto","camisa":"#eceff1","objeto":"lupa","os":0.7,"keys":[{"k":"s_exp","x":1650,"y":1700,"pose":"sostiene","cara":"neutral"},{"k":"real","x":1650,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {"look":"ejecutivo","var":84,"s":0.95,"desde":"s_exp","hasta":"s_2011","keys":[{"k":"s_exp","x":2250,"y":1700,"pose":"piensa","cara":"neutral","dir":-1},{"k":"real","x":2250,"y":1700,"pose":"piensa","cara":"sorpresa","dir":-1}]},
   {"look":"gamer","var":85,"s":0.95,"desde":"s_2011","hasta":"s_made","camisa":"#455a64","pelo":"#6d4c41","keys":[{"k":"s_2011","x":2900,"y":1700,"pose":"parado","cara":"neutral"},{"k":"hoax","x":2900,"y":1700,"pose":"apunta","cara":"risa"}]},
   {"look":"gamer","var":86,"s":0.85,"desde":"s_made","hasta":"s_fake","camisa":"#7e57c2","pelo":"#3e2723","peloT":"rulos","keys":[{"k":"s_made","x":4150,"y":1700,"pose":"sostiene","cara":"feliz"},{"k":"painted","x":4150,"y":1700,"pose":"golpea","cara":"feliz"},{"k":"hung","x":4150,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {"look":"jugadora","var":87,"s":0.85,"desde":"s_made","hasta":"s_fake","peloT":"cola","pelo":"#d7a86e","keys":[{"k":"s_made","x":4900,"y":1705,"pose":"parado","cara":"feliz","dir":-1},{"k":"hung","x":4900,"y":1705,"pose":"celebra","cara":"risa","dir":-1}]},
   {"look":"cliente","var":88,"s":0.9,"desde":"s_fake","keys":[{"k":"s_fake","x":5600,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"debated","x":5600,"y":1700,"pose":"apunta","cara":"sorpresa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.05,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle","luz":"tenue"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_exp","luz":"tenue"},{"x0":2600,"x1":3900,"set":"estudio","k":"s_2011"},
          {"x0":3900,"x1":5200,"set":"garage","k":"s_made"},{"x0":5200,"x1":6500,"set":"calle","k":"s_fake","luz":"tenue"}],
 "pan":[{"k":"s_exp","x":1300,"dur":0.9},{"k":"s_2011","x":2600,"dur":0.9},{"k":"s_made","x":3900,"dur":0.9},{"k":"s_fake","x":5200,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"hung+0.4","de":5,"texto":"PERFECT.","fin":"s_fake","dx":60}],
 "numeros":[{"k":"fooled","n":21,"suf":" YEARS","c":"cian","etq":"FOOLING EXPERTS","fin":"s_1990"}],
 "zoom":[{"k":0.1,"s":1.15,"x":540,"y":1150,"dur":0.8},{"k":"s_1990","s":1.0,"dur":0.6},{"k":"real","s":1.12,"x":1950,"y":1400,"dur":0.5},{"k":"s_2011","s":1.0,"dur":0.4},
         {"k":"hoax","s":1.15,"x":3250,"y":1300,"dur":0.4},{"k":"s_made","s":1.0,"dur":0.4},{"k":"added","s":1.15,"x":4550,"y":1400,"dur":0.5},{"k":"s_fake","s":1.0,"dur":0.5}],
 "sacudidas":[{"k":"hoax","f":12}],
 "titulos":[{"k":0.2,"texto":"BELGIUM · 1990","c":"rojo","fin":"s_exp"},
            {"k":"s_exp","texto":"EXPERTS STUDY IT","c":"cian","fin":"s_2011"},
            {"k":"s_2011","texto":"2011 CONFESSION","c":"amar","fin":"s_made"},
            {"k":"s_made","texto":"FOAM + LIGHTS","c":"verde","grande":True,"fin":"s_fake"},
            {"k":"s_fake","texto":"PHOTO: FAKE","c":"rojo","grande":True,"fin":"debated"},
            {"k":"debated","texto":"THE WAVE: STILL DEBATED","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"triangle1","texto":"BLACK TRIANGLE, LIGHTS","c":"cian","fin":"s_exp"},
          {"k":"tv","texto":"ON BELGIAN TV","c":"amar","fin":"s_made"},
          {"k":"cut","texto":"HE WAS 18","c":"cian","fin":"s_fake"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WOULD YOU BELIEVE IT?","cierre2":"Yes or no? Comment","paises":["YES","NO"],
 "sfx":[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.0,"fade":0.4,"g":0.08}],"cta":"FOLLOW FOR MORE","like":"LIKE"}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("nocheV",{"sem":11,"gente":True}),("investigaV",{}),("noticiasV",{"cintillo":"2011: THE UFO PHOTO WAS A HOAX"}),("tallerV",{}),("nocheV",{"sem":23,"ciudad":False,"montes":True})])
quitar_props(E,["pc","tv"])
e0=E["escenas"][0];e0["zoom"]=[z for z in e0["zoom"] if z["k"] not in (0.1,)]
insertar(E,"0","s_1990",0,"vitrinaV",{"fondo":["#1d2a4a","#0d1428","#03050c"],"luz2":"200,215,255"},[{"tipo":"fotoOvni","x":540,"y":1330,"s":1.3}])
insertar(E,"hung","s_fake",5200,"vitrinaV",{"fondo":["#4c4f56","#2a2c32","#08090b"],"luz2":"255,226,160"},[{"tipo":"trianguloP","x":540,"y":1150,"s":1.9}])

g={"titulo":"The Famous UFO Photo Was Foam 👽","texto_pantalla":"FOAM + LIGHTS","lote":"R2026112301","marca":"THE RABBIT LOOP",
"nota_datos":"Foto de Petit-Rechain (Bélgica), 4-abr-1990, durante la ola OVNI belga 1989-1990: triángulo negro con luces. Expertos la analizaron como auténtica. 26-jul-2011, Patrick (M.) dijo en RTL que era un fraude: tenía 18 años; con amigos cortó un triángulo de poliestireno/frigolite, lo pintó de negro, le puso luces y lo colgó. 21 años después (1990→2011). La ola de avistamientos sigue en debate. Fuentes: AFP (Phys.org), Reuters (IBTimes/Artdaily), VRT, Wikipedia, The Week.",
"frases":frases,"frases_voz":voz,"fuentes":["https://phys.org/news/2011-07-belgium-ufo-puzzled-nasa-polystyrene.html","https://vrtnws.be/p.xVJ01BYxD","https://theweek.com/articles/905215/30-years-later-still-dont-know-what-really-happened-during-belgian-ufo-wave"],"escena":E}
guardar("R2026112301_src.json",g)
