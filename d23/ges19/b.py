import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["GTA 6 vendió 3.790 millones de dólares en su primer día.",
"Lo anunció Take-Two, la dueña de Rockstar.",
"Ojo: son ventas, no ganancia. Y es una estimación de la misma empresa.",
"GTA 5 había hecho 815 millones en sus primeras 24 horas.",
"O sea, más de cuatro veces más.",
"Take-Two dice que es el estreno más grande del entretenimiento, en cualquier formato.",
"Comenta si tú lo compraste el primer día.",
"Sigue el canal para más números de GTA 6."]
voz=["GTA seis vendió tres mil setecientos noventa millones de dólares en su primer día.",
"Lo anunció Téik Tu, la dueña de Rockstar.",
"Ojo. Son ventas, no ganancia. Y es una estimación de la misma empresa.",
"GTA cinco había hecho ochocientos quince millones en sus primeras veinticuatro horas.",
"O sea, más de cuatro veces más.",
"Téik Tu dice que es el estreno más grande del entretenimiento, en cualquier formato.",
"Comenta si tú lo compraste el primer día.",
"Sigue el canal para más números de GTA seis."]
M=[["vendio",0,"^vendi"],["tres",0,"^3"],["primer0",0,"^primer"],
["s_take",1,None],["duena",1,"^due"],
["s_ojo",2,None],["ganancia",2,"^ganancia"],["estim",2,"^estimaci"],
["s_gta5",3,None],["k815",3,"^815"],["horas",3,"^horas"],
["s_x4",4,None],["cuatro",4,"^cuatro"],
["s_rec",5,None],["estreno",5,"^estreno"],["formato",5,"^formato"],
["s_fin",6,None],["s_cta",7,None]]
GAM=dict(look="gamer",var=81,s=1.0)
P=[{"tipo":"bolsa_dinero","x":620,"y":1690,"s":1.2,"k":"tres","cae":True,"fin":"s_take"},
   {"tipo":"bolsa_dinero","x":780,"y":1690,"s":1.2,"k":"tres+0.2","cae":True,"fin":"s_take"},
   {"tipo":"bolsa_dinero","x":700,"y":1580,"s":1.2,"k":"tres+0.4","cae":True,"fin":"s_take"},
   {"tipo":"billetes","x":880,"y":1720,"s":1.3,"k":"tres+0.3","cae":True,"fin":"s_take"},
   {"tipo":"documento","x":2080,"y":1180,"s":0.9,"sello":"OFICIAL","selloc":"verde","k":"duena","cae":True,"z":1800,"fin":"s_ojo"},
   {"tipo":"grafico","x":2080,"y":1220,"s":1.0,"k":"s_ojo+0.2","z":1800,"fin":"s_gta5"},
   {"tipo":"sofa","x":3150,"y":1730,"s":1.2,"k":"s_gta5","fin":"s_rec"},
   {"tipo":"tv","x":3150,"y":1260,"s":1.15,"k":"s_gta5","fin":"s_rec"},
   {"tipo":"bolsa_dinero","x":3500,"y":1690,"s":1.1,"k":"cuatro","cae":True,"fin":"s_rec"},
   {"tipo":"bolsa_dinero","x":3620,"y":1690,"s":1.1,"k":"cuatro+0.15","cae":True,"fin":"s_rec"},
   {"tipo":"bolsa_dinero","x":3560,"y":1580,"s":1.1,"k":"cuatro+0.3","cae":True,"fin":"s_rec"},
   {"tipo":"trono","x":4430,"y":1640,"s":1.1,"k":"s_rec"}]
A=[{**GAM,"hasta":"s_take","keys":[{"k":0,"x":330,"y":1700,"pose":"juega","cara":"feliz"},{"k":"tres","x":330,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {"look":"ejecutivo","var":82,"camisa":"#263238","pelo":"#3e2723","s":1.0,"desde":"s_take","hasta":"s_gta5","keys":[{"k":"s_take","x":1650,"y":1700,"pose":"telefono","cara":"feliz"},{"k":"duena","x":1650,"y":1700,"pose":"apunta","cara":"feliz"},{"k":"s_ojo","x":1650,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"estim","x":1650,"y":1700,"pose":"cruzado","cara":"neutral"}]},
   {"look":"jugador","var":83,"s":0.95,"desde":"s_gta5","hasta":"s_rec","keys":[{"k":"s_gta5","x":3150,"y":1712,"pose":"sentado","cara":"feliz","z":1810},{"k":"cuatro","x":3150,"y":1712,"pose":"sentado","cara":"sorpresa","fx":"tiembla","z":1810}]},
   {**GAM,"desde":"s_rec","keys":[{"k":"s_rec","x":4430,"y":1600,"pose":"sentado","cara":"feliz","z":1660},{"k":"estreno","x":4430,"y":1600,"pose":"sentado","cara":"risa","fx":"brinca","z":1660}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.1,
 "zonas":[{"x0":-300,"x1":1300,"set":"banco"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_take"},{"x0":2600,"x1":3900,"set":"sala","k":"s_gta5","luz":"tenue"},{"x0":3900,"x1":5200,"set":"trono","k":"s_rec"}],
 "pan":[{"k":"s_take","x":1300,"dur":0.9},{"k":"s_gta5","x":2600,"dur":0.9},{"k":"s_rec","x":3900,"dur":0.9}],
 "props":P,"actores":A,
 "numeros":[{"k":"tres","n":3790,"pre":"US$","suf":" MILLONES","loc":"es-CL","c":"amar","etq":"PRIMER DÍA","fin":"s_take"},
            {"k":"k815","n":815,"pre":"US$","suf":" MILLONES","loc":"es-CL","c":"cian","etq":"GTA 5 · PRIMERAS 24 HORAS","fin":"s_x4"}],
 "zoom":[{"k":0.1,"s":1.06,"dur":0.6},{"k":"tres","s":1.15,"x":620,"y":1500,"dur":0.4},{"k":"s_take","s":1.0,"dur":0.4},
         {"k":"cuatro","s":1.12,"x":3300,"y":1500,"dur":0.3},{"k":"s_rec","s":1.0,"dur":0.4}],
 "sacudidas":[{"k":"tres","f":18},{"k":"cuatro","f":22}],
 "titulos":[{"k":0.2,"texto":"DÍA 1","c":"amar","fin":"s_take"},
            {"k":"s_take","texto":"TAKE-TWO","c":"cian","fin":"s_ojo"},
            {"k":"s_ojo","texto":"OJO","c":"rojo","grande":True,"fin":"s_gta5"},
            {"k":"s_gta5","texto":"GTA 5 (2013)","c":"cian","fin":"s_x4"},
            {"k":"s_x4","texto":"MÁS DE 4 VECES","c":"verde","grande":True,"fin":"s_rec"},
            {"k":"s_rec","texto":"RÉCORD DEL ENTRETENIMIENTO","c":"amar","fin":"s_fin"}],
 "chips":[{"k":"duena","texto":"DUEÑA DE ROCKSTAR","c":"cian","fin":"s_ojo"},
          {"k":"ganancia","texto":"VENTAS, NO GANANCIA","c":"rojo","fin":"s_gta5"},
          {"k":"estim","texto":"ESTIMACIÓN DE LA EMPRESA","c":"amar","fin":"s_gta5"},
          {"k":"formato","texto":"EN CUALQUIER FORMATO","c":"rosa","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"¿LO COMPRASTE EL DÍA 1?","cierre2":"Comenta: sí o no","paises":["SÍ","NO"],
 "sfx":[{"f":"extra/CarEngineRev_BW.52086.wav","k":"0","off":0.0,"dur":1.3,"fade":0.5,"g":0.13},
        {"f":"extra/ESM_SPG_fx_action_transaction_cash_register_ding_02.wav","k":"tres","off":0.0,"dur":0.9,"g":0.12}],"cta":"SIGUE EL CANAL"}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("tiendaJuegosV",{}),("corporativoV",{"ticker":"TTWO ▲","hora":"noche"}),("cuartoGamerV",{"era":"2013"}),("escenarioV",{})])
quitar_props(E,["tv","trono"])
e0=E["escenas"][0];e0["zoom"]=[z for z in e0["zoom"] if z["k"]!="tres"]
e0["props"].append({"tipo":"trofeo","x":4720,"y":1700,"s":1.05,"k":"s_rec","texto":"RÉCORD","z":1600})
insertar(E,"tres","s_take",1300,"mesaCenitalV",{"titulo":"VENTAS · DÍA 1","monto":"US$ 3.790 M","billetes":True,"billete":"US$ 10.000"},[])

g={"titulo":"GTA 6 hizo 3.790 millones en 1 día 💰","texto_pantalla":"US$3.790 MILLONES","lote":"G2026112301","marca":"VICEVERSO GG",
"nota_datos":"Take-Two (comunicado 8-K SEC, 20-nov-2026): GTA VI 'day one retail sales' US$3,79 mil millones, estimación de la empresa hasta el fin del 19-nov, a nivel mundial; récord del entretenimiento en cualquier medio. No es ganancia. GTA V: 11,21 M unidades y US$815,7 M en sus primeras 24 horas (Guinness, vía Fox). 3790/815,7 = 4,6 → 'más de cuatro veces'. GTA V salió en 2013.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.sec.gov/Archives/edgar/data/0000946581/000162828026075217/exhibit9918k.htm","https://www.fox5ny.com/news/gta-vi-pulls-estimated-1-84-billion-release-day-more-than-double-gta-vs-launch-record"],"escena":E}
guardar("G2026112301_src.json",g)
