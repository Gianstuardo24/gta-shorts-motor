import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Decaf coffee still has caffeine.",
"To be called decaf in the U.S., about 97 percent of the caffeine has to be removed.",
"That leaves a little: usually 2 to 15 milligrams in a cup.",
"A regular cup has around 95.",
"So it would take a lot of decaf to match one regular coffee.",
"And decaf was invented in Germany, in 1903, by a coffee merchant named Ludwig Roselius.",
"Tell me if you knew decaf wasn't caffeine free.",
"Follow for one coffee curiosity a day."]
voz=[f.replace("U.S.","U S").replace("97 percent","ninety-seven percent").replace("2 to 15","two to fifteen").replace("around 95","around ninety-five").replace("1903","nineteen oh three") for f in frases]
M=[["still",0,"^still"],["caffeine0",0,"^caffeine"],
["s_us",1,None],["about",1,"^about"],["removed",1,"^removed"],
["s_leaves",2,None],["little",2,"^little"],["milligrams",2,"^milligrams"],
["s_reg",3,None],["around",3,"^around"],
["s_lot",4,None],["lot",4,"^lot"],["match",4,"^match"],
["s_inv",5,None],["germany",5,"^germany"],["merchant",5,"^merchant"],["ludwig",5,"^ludwig"],
["s_fin",6,None],["s_cta",7,None]]
BA=dict(look="vendedor",var=61,pelo="#3e2723",camisa="#6d4c41",s=1.0)
CL=dict(look="cliente",var=62,pelo="#d7a86e",camisa="#00897b",s=0.97)
P=[{"tipo":"taza","x":760,"y":1560,"s":1.1,"k":0.0,"z":1800,"fin":"s_us"},
   {"tipo":"documento","x":2250,"y":1150,"s":0.95,"sello":"DECAF","selloc":"verde","k":"s_us","cae":True,"z":1800,"fin":"s_leaves"},
   {"tipo":"taza","x":3350,"y":1560,"s":1.0,"k":"s_leaves","z":1800,"fin":"s_reg"},
   {"tipo":"taza","x":4650,"y":1560,"s":1.3,"k":"s_reg","z":1800,"fin":"s_lot"},
   {"tipo":"taza","x":5700,"y":1600,"s":0.7,"k":"lot","cae":True,"z":1800,"fin":"s_inv"},{"tipo":"taza","x":5850,"y":1600,"s":0.7,"k":"lot+0.15","cae":True,"z":1800,"fin":"s_inv"},
   {"tipo":"taza","x":6000,"y":1600,"s":0.7,"k":"lot+0.3","cae":True,"z":1800,"fin":"s_inv"},{"tipo":"taza","x":6150,"y":1600,"s":0.7,"k":"lot+0.45","cae":True,"z":1800,"fin":"s_inv"},
   {"tipo":"taza","x":5775,"y":1470,"s":0.7,"k":"lot+0.6","cae":True,"z":1800,"fin":"s_inv"},{"tipo":"taza","x":5925,"y":1470,"s":0.7,"k":"lot+0.75","cae":True,"z":1800,"fin":"s_inv"},{"tipo":"taza","x":6075,"y":1470,"s":0.7,"k":"lot+0.9","cae":True,"z":1800,"fin":"s_inv"},
   {"tipo":"documento","x":7450,"y":1150,"s":0.95,"sello":"1903","selloc":"amar","k":"germany","cae":True,"z":1800},
   {"tipo":"bolsa_dinero","x":7500,"y":1690,"s":1.0,"k":"merchant"}]
A=[{**CL,"hasta":"s_us","keys":[{"k":0,"x":320,"y":1700,"pose":"sostiene","cara":"feliz","objeto":"taza"},{"k":"still","x":320,"y":1700,"pose":"piensa","cara":"sorpresa","fx":"brinca"}]},
   {**BA,"desde":"s_us","hasta":"s_leaves","keys":[{"k":"s_us","x":1380,"y":1700,"pose":"camina","cara":"neutral"},{"k":"about","x":1680,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**CL,"desde":"s_leaves","hasta":"s_reg","keys":[{"k":"s_leaves","x":2960,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"milligrams","x":2960,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**BA,"desde":"s_reg","hasta":"s_lot","keys":[{"k":"s_reg","x":4260,"y":1700,"pose":"ofrece","cara":"feliz","objeto":"taza"},{"k":"around","x":4260,"y":1700,"pose":"arriba","cara":"risa"}]},
   {**CL,"desde":"s_lot","hasta":"s_inv","keys":[{"k":"s_lot","x":5480,"y":1700,"pose":"parado","cara":"neutral"},{"k":"lot","x":5480,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"match","x":5480,"y":1700,"pose":"celebra","cara":"risa"}]},
   {"look":"sabio","var":65,"s":0.97,"desde":"s_inv","keys":[{"k":"s_inv","x":6760,"y":1700,"pose":"camina","cara":"neutral"},{"k":"germany","x":6980,"y":1700,"pose":"sostiene","cara":"feliz","objeto":"taza"},{"k":"ludwig","x":6980,"y":1700,"pose":"saluda","cara":"feliz"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.08,
 "zonas":[{"x0":-300,"x1":1300,"set":"cafe"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_us"},{"x0":2600,"x1":3900,"set":"cafe","k":"s_leaves","luz":"tenue"},
          {"x0":3900,"x1":5200,"set":"cafe","k":"s_reg"},{"x0":5200,"x1":6500,"set":"cafe","k":"s_lot"},{"x0":6500,"x1":7900,"set":"calle","k":"s_inv"}],
 "pan":[{"k":"s_us","x":1300,"dur":0.9},{"k":"s_leaves","x":2600,"dur":0.9},{"k":"s_reg","x":3900,"dur":0.9},{"k":"s_lot","x":5200,"dur":0.9},{"k":"s_inv","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"still","de":0,"texto":"WAIT, WHAT?","fin":"s_us","dx":150}],
 "numeros":[{"k":"about","n":97,"suf":" %","c":"verde","etq":"CAFFEINE REMOVED","fin":"s_leaves"},
            {"k":"around","n":95,"suf":" MG","c":"rojo","etq":"REGULAR CUP","fin":"s_lot"}],
 "zoom":[{"k":0.1,"s":1.1,"x":560,"y":1450,"dur":0.6},{"k":"still","s":1.25,"x":380,"y":1420,"dur":0.4},{"k":"s_us","s":1.0,"dur":0.3},
         {"k":"little","s":1.15,"x":3250,"y":1450,"dur":0.4},{"k":"s_reg","s":1.0,"dur":0.3},{"k":"s_lot","s":1.0,"dur":0.3},{"k":"lot","s":1.12,"x":5780,"y":1500,"dur":0.5},
         {"k":"s_inv","s":1.0,"dur":0.3},{"k":"ludwig","s":1.2,"x":7040,"y":1420,"dur":0.4},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"caffeine0","f":12}],
 "titulos":[{"k":0.2,"texto":"DECAF","c":"verde","grande":True,"fin":"still"},
            {"k":"s_us","texto":"THE U.S. RULE","c":"cian","fin":"about"},
            {"k":"s_leaves","texto":"2 TO 15 MG","c":"amar","grande":True,"fin":"s_reg"},
            {"k":"s_reg","texto":"REGULAR COFFEE","c":"rojo","fin":"around"},
            {"k":"s_lot","texto":"DECAF vs REGULAR","c":"rosa","fin":"s_inv"},
            {"k":"s_inv","texto":"GERMANY · 1903","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"milligrams","texto":"USUALLY · PER CUP","c":"amar","fin":"s_reg"},
          {"k":"ludwig","texto":"LUDWIG ROSELIUS","c":"cian","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DID YOU KNOW?","cierre2":"Yes or no? Comment","paises":["YES","NO"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[None,("labV",{"pantalla":"DECAF RULE","pantalla2":"97 %"}),None,None,("cocinaV",{}),("estambulV",{})])
insertar(E,"caffeine0","s_us",1300,"vitrinaV",{"fondo":["#cfe8c0","#6f9a5a","#16280e"],"luz2":"235,255,225","pedestal":True},[{"tipo":"taza","x":540,"y":1320,"s":2.8}])
insertar(E,"merchant","ludwig",6500,"mesaCenitalV",{"titulo":"PATENT · DECAF COFFEE","monto":"1903","firma":"merchant"},[])
g={"titulo":"Decaf Still Has Caffeine ☕","texto_pantalla":"DECAF ≠ ZERO","lote":"C2026112401","marca":"COFFEE, BUT WHY?",
"nota_datos":"El descafeinado no es libre de cafeína. En EE.UU. se exige quitar al menos ~97 % de la cafeína. Queda poco: normalmente 2-15 mg por taza de 8 oz (FDA); una taza normal tiene ~95 mg o más (95-200 según Wikipedia/USDA). La descafeinación la inventó el comerciante alemán Ludwig Roselius (1903, patentada en 1906; Kaffee HAG). Fuentes: FDA ('Spilling the Beans'), Wikipedia (Decaffeination).",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/Decaffeination","https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much"],"escena":E}
guardar("C2026112401_src.json",g)
