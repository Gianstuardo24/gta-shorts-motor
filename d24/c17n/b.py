import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["Stop drinking decaf. At least until you hear this.",
"Most people pour it at night, to relax without the buzz.",
"To get that name, the green beans are soaked before roasting, to pull the caffeine out.",
"But the U.S. rule only asks to remove about 97 percent.",
"So your decaf still has caffeine: usually 2 to 15 milligrams a cup, against about 95 in a regular one.",
"Now the part nobody tells you about.",
"Caffeine takes about 5 hours just to drop by half.",
"So the earlier you drink it, the less is left at bedtime.",
"Tell me if you knew.",
"Follow for one coffee curiosity a day."]
voz=[f.replace("U.S.","U S").replace("97 percent","ninety-seven percent").replace("2 to 15","two to fifteen").replace("about 95","about ninety-five").replace("5 hours","five hours") for f in frases]
M=[["stop",0,"^stop"],["decaf0",0,"^decaf"],["hear",0,"^hear"],
["s_night",1,None],["pour",1,"^pour"],["relax",1,"^relax"],["buzz",1,"^buzz"],
["s_name",2,None],["beans",2,"^beans"],["soaked",2,"^soaked"],["roasting",2,"^roasting"],["pull",2,"^pull"],
["s_rule",3,None],["rule",3,"^rule"],["about",3,"^about"],
["s_rev",4,None],["still",4,"^still"],["usually",4,"^usually"],["against",4,"^against"],["regular",4,"^regular"],
["s_part",5,None],["matters",5,"^nobody"],
["s_half",6,None],["takes",6,"^takes"],["half",6,"^half"],
["s_sol",7,None],["earlier",7,"^earlier"],["s_fin",8,None],["s_cta",9,None]]
CL=dict(look="cliente",var=62,pelo="#d7a86e",camisa="#5c6bc0",s=1.0)
# 24-nov 23:30 · escenas largas (4-6 s): 6 escenas en vez de 11. Objeto premium / persona haciendo algo, alternados.
P=[{"tipo":"tazaPremium","x":540,"y":1300,"s":1.7,"texto":"DECAFFEINATED","banda":"DECAF","color":"#2e7d32","k":0,"fin":"s_night","z":1900},
   {"tipo":"sofa","x":2150,"y":1700,"s":1.1,"k":"s_night","fin":"s_name"},
   {"tipo":"lamparaPie","x":1420,"y":1640,"s":1.15,"k":"s_night","fin":"s_name","z":1500},
   {"tipo":"mesaCentro","x":2010,"y":1860,"s":1.0,"k":"s_night","fin":"s_name","z":1900},
   {"tipo":"mesaLab","x":3470,"y":1640,"s":0.9,"k":"s_rule","fin":"s_rev","z":1500},
   {"tipo":"neblina","x":540,"y":1690,"s":1.0,"k":0,"fin":"s_night","z":1950,"a":.2},
   {"tipo":"humo","x":3560,"y":1500,"s":0.55,"k":"s_rule","fin":"s_rev","z":1400,"a":.25}]
A=[{**CL,"desde":"s_night","hasta":"s_name","keys":[{"k":"s_night","x":1160,"y":1700,"a":[1720,1700],"dur":1.4,"ease":"eio","pose":"sostiene","cara":"feliz","objeto":"taza"},{"k":"relax","x":1720,"y":1700,"pose":"bebe","cara":"feliz","objeto":"taza"}]},
   {**CL,"desde":"s_part","keys":[{"k":"s_part","x":4300,"y":1700,"pose":"bebe","cara":"neutral","objeto":"taza"},{"k":"matters","x":4300,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {"look":"inventor","var":66,"lentes":True,"pelo":"#9e9e9e","camisa":"#eceff1","s":0.98,"desde":"s_rule","hasta":"s_rev","keys":[{"k":"s_rule","x":3060,"y":1700,"pose":"lee","cara":"neutral","objeto":"documento"},{"k":"about","x":3060,"y":1700,"pose":"explica","cara":"feliz"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.24,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala"},{"x0":1300,"x1":2600,"set":"sala","k":"s_night"},{"x0":2600,"x1":3900,"set":"oficina","k":"s_rule"},{"x0":3900,"x1":5200,"set":"calle","k":"s_part"}],
 "pan":[{"k":"s_night","x":1300,"dur":0.04,"corte":1,"dir":1},{"k":"s_rule","x":2600,"dur":0.8},{"k":"s_part","x":3900,"dur":0.8}],
 "props":P,"actores":A,
 "prohibidos":[{"k":"stop","x":540,"y":1175,"r":200}],
 "numeros":[{"k":"about","n":97,"suf":" %","c":"verde","etq":"CAFFEINE REMOVED","fin":"s_rev"},
            {"k":"usually","n":15,"pre":"2–","suf":" MG","c":"verde","etq":"DECAF · PER CUP","fin":"against"},
            {"k":"regular","n":95,"suf":" MG","c":"rojo","etq":"REGULAR CUP","fin":"s_part"}],
 "zoom":[],"planos_hint":[{"k":0,"tipo":"general"},{"k":"s_rule","tipo":"medio","var":66},{"k":"s_part","tipo":"general"}],
 "sacudidas":[{"k":"stop","f":12},{"k":"still","f":14},{"k":"half","f":12}],
 "titulos":[{"k":0.15,"texto":"STOP","c":"rojo","grande":True,"fin":"decaf0"},
            {"k":"s_night","texto":"1 · WHY PEOPLE DRINK IT","c":"cian","fin":"s_name"},
            {"k":"s_rule","texto":"3 · THE RULE","c":"amar","fin":"about"},
            {"k":"s_rev","texto":"4 · THE CATCH","c":"rojo","fin":"usually"},
            {"k":"s_part","texto":"5 · AT NIGHT","c":"cian","fin":"takes"}],
 "emojis":[{"k":"relax","e":"😌"},{"k":"still","e":"😬","dur":1.0},{"k":"matters","e":"🤫"}],
 "chips":[]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"DID YOU KNOW?","cierre2":"Yes or no? Comment","paises":["YES","NO"],"sfx":[],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[("vitrinaV",{"fondo":["#1d2a4a","#0d1428","#03050c"],"luz2":"200,215,255","pedestal":True}),("salaV",{"hora":"noche","sinSofa":True,"var":2,"pared":["#4a3f5c","#2e2740"]}),("labV",{"pantalla":"DECAF RULE","pantalla2":"U.S."}),("dormitorioV",{"persona":False,"pared":["#3a4766","#252d47"]})])
insertar(E,"s_name","s_rule",2600,"vitrinaV",{"fondo":["#cfe8c0","#6f9a5a","#16280e"],"luz2":"235,255,225","aroY":1400},[{"tipo":"remojo","x":540,"y":1640,"s":1.5,"texto":"SOAKED IN WATER","sub":"THE CAFFEINE COMES OUT"}])
insertar(E,"s_rev","s_part",3900,"vitrinaV",{"fondo":["#f0e2c8","#b89a6a","#2a1c0c"],"luz2":"255,240,210","aroY":1380},[{"tipo":"bolsaCafe","x":330,"y":1640,"s":2.0,"color":"#2e7d32","texto":"DECAF","sub":"2-15 MG"},{"tipo":"bolsaCafe","x":760,"y":1640,"s":2.0,"color":"#6d4c41","texto":"CAFFEINE","sub":"95 MG","k":"against","cae":True},{"tipo":"granos","x":540,"y":1700,"s":1.6,"n":14,"color":"#5d3a1a"}])
insertar(E,"takes","s_fin",3900,"vitrinaV",{"fondo":["#2a1d55","#120b2c","#030108"],"luz2":"200,150,255","aroY":1250},[{"tipo":"mitad","x":540,"y":1480,"s":0.95,"de":"takes","a":"half","texto":"CAFFEINE IN YOUR BODY","horas":5},{"tipo":"neblina","x":540,"y":1760,"s":1.0,"a":.18,"z":1950}])
g={"titulo":"Stop Drinking Decaf ❌☕😳","texto_pantalla":"STOP DRINKING DECAF","lote":"C2026112403","pausa_larga_antes":[1,5,6,9],"marca":"COFFEE, BUT WHY?","cuerpo":"pro",
"nota_datos":"Formato nuevo (24-nov): gancho + promesa, desarrollo, primera respuesta, segunda pregunta y segundo dato, cierre. El descafeinado no es libre de cafeína: en EE.UU. se exige quitar ~97 %. Quedan normalmente 2-15 mg por taza de 8 oz (FDA); una taza normal tiene ~95 mg. La cafeína se extrae del grano verde, antes de tostar. Vida media de la cafeína en adultos sanos: ~5 horas en promedio (rango habitual 3-7 h). NO se afirma que el descafeinado perjudique el sueño: no hay estudio verificado para esas dosis. Tampoco se dice que dosis pequeñas afecten el sueño: Gardiner et al. 2023 (Sleep) no hallaron efecto medible con 100 mg ni a 4 h de dormir; sí con 400 mg. Cierre de solución ('the earlier you drink it, the less is left at bedtime') = consecuencia directa de la vida media. Fuentes: FDA ('Spilling the Beans'), Wikipedia (Decaffeination; Caffeine). Disparador: alarma. Tipo de gancho: 8.",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/Decaffeination","https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much","https://en.wikipedia.org/wiki/Caffeine"],"escena":E}
guardar("C2026112403_src.json",g)
