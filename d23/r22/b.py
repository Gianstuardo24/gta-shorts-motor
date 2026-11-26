import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["In 1997, thousands of people saw strange lights over Phoenix, Arizona.",
"On March 13, around 10 p.m., a row of bright lights hung in the sky, then slowly vanished.",
"Months later, the Air National Guard explained it: they were flares.",
"A-10 jets from Maryland dropped them during a training exercise southwest of Phoenix.",
"They seemed to vanish because they fell behind the Sierra Estrella mountains.",
"An earlier V shape that night is still argued about. The military says it was planes in formation.",
"Tell me what you think people really saw.",
"Follow for the next case."]
voz=[f.replace("1997","nineteen ninety-seven").replace("March 13","March thirteenth").replace("10 p.m.","ten p.m.").replace("A-10","A ten") for f in frases]
M=[["thousands",0,"^thousands"],["lights0",0,"^lights"],["phoenix0",0,"^phoenix"],["s_night",1,None],["row",1,"^row"],["hung",1,"^hung"],["vanished",1,"^vanished"],
["s_months",2,None],["guard",2,"^guard"],["flares",2,"^flares"],["s_jets",3,None],["a10",3,"^jets"],["maryland",3,"^maryland"],["training",3,"^training"],
["s_mtn",4,None],["behind",4,"^behind"],["estrella",4,"^estrella"],["s_v",5,None],["shape",5,"^shape"],["argued",5,"^argued"],["formation",5,"^formation"],
["s_fin",6,None],["s_cta",7,None]]
def fila(x0,y,k,fin,n=6,dx=120,cae=None):
    out=[]
    for i in range(n):
        o={"tipo":"linterna","x":x0+i*dx,"y":y+(i%2)*25,"s":0.55,"k":k if i==0 else f"{k}+{0.15*i:.2f}" if isinstance(k,str) else k,"fin":fin,"z":1500}
        if cae: o["mov"]=[{"k":cae[0],"x":x0+i*dx,"y":y+(i%2)*25},{"k":cae[1],"x":x0+i*dx+40,"y":y+(cae[2] if len(cae)>2 else 700)}]
        out.append(o)
    return out
P=(fila(240,760,"row","s_months",cae=("row","s_months",300))+
   [{"tipo":"pc","x":1950,"y":1650,"s":1.2,"k":"s_months","texto":"FLARES","fin":"s_jets"},
    {"tipo":"documento","x":1950,"y":1100,"s":1.0,"sello":"FLARES","selloc":"verde","k":"flares","cae":True,"z":1800,"fin":"s_jets"},
    {"tipo":"jet","x":2400,"y":800,"s":1.5,"k":"s_jets","fin":"s_mtn","mov":[{"k":"s_jets","x":2500,"y":820},{"k":"s_mtn","x":3700,"y":760}]},
    {"tipo":"jet","x":2400,"y":950,"s":1.3,"k":"s_jets+0.3","fin":"s_mtn","mov":[{"k":"s_jets+0.3","x":2450,"y":960},{"k":"s_mtn","x":3600,"y":900}]}]+
   fila(2800,1000,"training","s_mtn",n=5,dx=150)+
   fila(4050,900,"s_mtn","s_v",n=5,dx=150,cae=("s_mtn","estrella+1.2"))+
   [{"tipo":"arena","x":4500,"y":1560,"s":1.4,"k":"s_mtn","z":1600,"fin":"s_v"},
    {"tipo":"jet","x":5300,"y":850,"s":0.8,"k":"s_v","fin":"s_fin","mov":[{"k":"s_v","x":5250,"y":900},{"k":"s_fin","x":6200,"y":820}]},
    {"tipo":"jet","x":5200,"y":980,"s":0.8,"k":"s_v+0.2","fin":"s_fin","mov":[{"k":"s_v+0.2","x":5100,"y":1000},{"k":"s_fin","x":6050,"y":940}]},
    {"tipo":"jet","x":5400,"y":980,"s":0.8,"k":"s_v+0.4","fin":"s_fin","mov":[{"k":"s_v+0.4","x":5400,"y":1000},{"k":"s_fin","x":6350,"y":940}]}])
A=[{"look":"cliente","var":91,"s":0.95,"hasta":"s_months","keys":[{"k":0,"x":250,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"vanished","x":250,"y":1700,"pose":"piensa","cara":"sorpresa"}]},
   {"look":"jugadora","var":92,"s":0.95,"hasta":"s_months","keys":[{"k":0,"x":520,"y":1705,"pose":"telefono","cara":"sorpresa"}]},
   {"look":"gamer","var":93,"s":0.9,"hasta":"s_months","keys":[{"k":0,"x":800,"y":1705,"pose":"parado","cara":"sorpresa","dir":-1},{"k":"hung","x":800,"y":1705,"pose":"celebra","cara":"sorpresa","dir":-1}]},
   {"look":"ejecutivo","var":94,"s":1.0,"desde":"s_months","hasta":"s_jets","camisa":"#4e5b31","keys":[{"k":"s_months","x":1650,"y":1700,"pose":"parado","cara":"neutral"},{"k":"flares","x":1650,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {"look":"cliente","var":95,"s":0.9,"desde":"s_v","keys":[{"k":"s_v","x":5450,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"argued","x":5450,"y":1700,"pose":"piensa","cara":"sorpresa"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.05,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle","luz":"tenue"},{"x0":1300,"x1":2600,"set":"oficina","k":"s_months","luz":"tenue"},{"x0":2600,"x1":3900,"set":"cielo","k":"s_jets","luz":"tenue"},
          {"x0":3900,"x1":5100,"set":"cielo","k":"s_mtn","luz":"tenue"},{"x0":5100,"x1":6400,"set":"cielo","k":"s_v","luz":"tenue"}],
 "pan":[{"k":"s_months","x":1300,"dur":0.9},{"k":"s_jets","x":2600,"dur":0.9},{"k":"s_mtn","x":3900,"dur":0.9},{"k":"s_v","x":5100,"dur":0.9}],
 "props":P,"actores":A,
 "zoom":[{"k":0.1,"s":1.12,"x":540,"y":1250,"dur":0.8},{"k":"row","s":1.05,"x":540,"y":1100,"dur":0.6},{"k":"s_months","s":1.0,"dur":0.5},{"k":"flares","s":1.12,"x":1950,"y":1350,"dur":0.5},
         {"k":"s_jets","s":1.0,"dur":0.4},{"k":"s_mtn","s":1.05,"x":4450,"y":1300,"dur":0.5},{"k":"s_v","s":1.0,"dur":0.5}],
 "titulos":[{"k":0.2,"texto":"PHOENIX · 1997","c":"rojo","fin":"s_night"},
            {"k":"s_night","texto":"MARCH 13 · 10 P.M.","c":"cian","fin":"s_months"},
            {"k":"flares","texto":"FLARES","c":"verde","grande":True,"fin":"s_jets"},
            {"k":"s_jets","texto":"A-10 TRAINING","c":"amar","fin":"s_mtn"},
            {"k":"s_mtn","texto":"BEHIND THE MOUNTAINS","c":"cian","fin":"s_v"},
            {"k":"s_v","texto":"THE V SHAPE?","c":"rojo","grande":True,"fin":"s_fin"}],
 "chips":[{"k":"thousands","texto":"THOUSANDS OF WITNESSES","c":"amar","fin":"s_night"},
          {"k":"guard","texto":"AIR NATIONAL GUARD","c":"cian","fin":"s_jets"},
          {"k":"maryland","texto":"FROM MARYLAND","c":"amar","fin":"s_mtn"},
          {"k":"formation","texto":"MILITARY: PLANES IN FORMATION","c":"amar","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WHAT DID THEY SEE?","cierre2":"Flares or not? Comment","paises":["FLARES","SOMETHING ELSE"],
 "sfx":[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.0,"fade":0.4,"g":0.08}],"cta":"FOLLOW FOR MORE","like":"LIKE"}
# --- 23-nov: escenarios propios + insertos ---
poner_sets(E,[("nocheV",{"sem":31,"gente":True,"montes":True}),("hangarV",{}),("nocheV",{"sem":37,"ciudad":False,"montes":True,"jets":False}),("nocheV",{"sem":41,"montes":True}),("nocheV",{"sem":53,"ciudad":False})])
quitar_props(E,["pc"])
e0=E["escenas"][0];e0["zoom"]=[z for z in e0["zoom"] if z["k"]!="flares"]
insertar(E,"s_night","row",0,"vitrinaV",{"fondo":["#2a3050","#141830","#04050c"],"luz2":"200,210,255"},[{"tipo":"calendarioP","x":540,"y":1150,"s":3.2,"mes":"MARCH","dia":"13","anio":"1997"}])
insertar(E,"flares","s_jets",2600,"vitrinaV",{"fondo":["#1a1430","#0a0818","#020106"],"luz2":"255,200,120"},[{"tipo":"bengala","x":540,"y":900,"s":1.5}])

g={"titulo":"What the Phoenix Lights Really Were 👽","texto_pantalla":"FLARES","lote":"R2026112302","marca":"THE RABBIT LOOP",
"nota_datos":"13-mar-1997, Arizona: miles de testigos. ~22:00, fila de luces brillantes que 'flotaban o caían lentamente'. La Guardia Nacional (Capt. Eileen Bienz) determinó meses después que eran bengalas de iluminación lanzadas por A-10 de la Guardia Nacional Aérea de Maryland (Operación Snowbird) en el polígono al suroeste de Phoenix (Barry M. Goldwater); 'desaparecían' al caer tras la sierra Estrella. El 'V' de ~20:00 se atribuye a A-10 en formación; testigos lo discuten. Fuentes: Phoenix New Times, Arizona Republic, Skeptoid, Wikipedia, Plane & Pilot.",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.phoenixnewtimes.com/arts-culture/the-phoenix-lights-are-no-mystery-6661825/","https://skeptoid.com/episodes/41","https://en.wikipedia.org/wiki/Phoenix_Lights"],"escena":E}
guardar("R2026112302_src.json",g)
