import sys; sys.path.insert(0,'/home/claude/d24'); from comun import *
frases=["The Navy's pyramid UFOs were explained in front of Congress.",
"In 2019, sailors on a warship filmed glowing triangles flying overhead.",
"The video leaked in 2021, and the Pentagon confirmed the footage was real.",
"Then in 2022, a Navy intelligence official showed it at a public hearing.",
"The triangle shape came from the camera: light passing through night vision goggles.",
"As for the objects, he said they were most likely drones.",
"Tell me if that explanation is enough for you.",
"Follow for the next case."]
voz=[f.replace("2019","twenty nineteen").replace("2021","twenty twenty-one").replace("2022","twenty twenty-two") for f in frases]
M=[["pyramid",0,"^pyramid"],["congress",0,"^congress"],
["s_2019",1,None],["warship",1,"^warship"],["triangles",1,"^triangles"],
["s_leak",2,None],["leaked",2,"^leaked"],["pentagon",2,"^pentagon"],["real",2,"^real"],
["s_2022",3,None],["official",3,"^official"],["hearing",3,"^hearing"],
["s_shape",4,None],["camera",4,"^camera"],["goggles",4,"^goggles"],
["s_obj",5,None],["drones",5,"^drones"],
["s_fin",6,None],["s_cta",7,None]]
def tri(cx,cy,k,fin=None,sc=1.0):
    o={"tipo":"trianguloP","x":cx,"y":cy,"s":sc,"k":k,"z":1800}
    if fin: o["fin"]=fin
    return o
SA=dict(look="ejecutivo",var=41,pelo="#3e2723",camisa="#1a237e",s=0.97)
P=[tri(560,900,0.0,"s_2019",0.9),
   tri(1800,820,"triangles","s_leak",0.6),tri(2100,950,"triangles+0.2","s_leak",0.5),tri(2330,800,"triangles+0.4","s_leak",0.55),
   {"tipo":"telefono","x":3500,"y":1500,"s":1.1,"k":"leaked","z":1800,"fin":"s_2022"},
   {"tipo":"documento","x":3480,"y":1100,"s":0.95,"sello":"REAL FOOTAGE","selloc":"verde","k":"real","cae":True,"z":1800,"fin":"s_2022"},
   {"tipo":"tv","x":4850,"y":1250,"s":1.3,"k":"official","fin":"s_shape"},
   {"tipo":"lupa","x":6150,"y":1250,"s":1.5,"k":"camera","z":1800,"fin":"s_obj"},
   tri(5900,1000,"s_shape","s_obj",0.6),
   {"tipo":"orbe","x":7150,"y":950,"s":0.8,"k":"drones","z":1800},{"tipo":"orbe","x":7400,"y":1050,"s":0.7,"k":"drones+0.2","z":1800},{"tipo":"orbe","x":7600,"y":900,"s":0.75,"k":"drones+0.4","z":1800}]
A=[{"look":"cliente","var":42,"s":0.97,"hasta":"s_2019","keys":[{"k":0,"x":300,"y":1700,"pose":"apunta","cara":"sorpresa"},{"k":"congress","x":300,"y":1700,"pose":"piensa","cara":"neutral"}]},
   {**SA,"desde":"s_2019","hasta":"s_leak","keys":[{"k":"s_2019","x":1640,"y":1700,"pose":"parado","cara":"neutral"},{"k":"triangles","x":1640,"y":1700,"pose":"apunta","cara":"sorpresa","fx":"brinca"}]},
   {"look":"gamer","var":43,"camisa":"#455a64","s":0.97,"desde":"s_leak","hasta":"s_2022","keys":[{"k":"s_leak","x":2680,"y":1700,"pose":"camina","cara":"neutral"},{"k":"s_leak+0.9","x":2960,"y":1700,"pose":"telefono","cara":"sorpresa"},{"k":"real","x":2960,"y":1700,"pose":"apunta","cara":"sorpresa"}]},
   {**SA,"var":44,"desde":"s_2022","hasta":"s_shape","keys":[{"k":"s_2022","x":4300,"y":1700,"pose":"parado","cara":"neutral"},{"k":"official","x":4300,"y":1700,"pose":"apunta","cara":"neutral"}]},
   {"look":"inventor","var":45,"lentes":True,"s":0.97,"desde":"s_shape","hasta":"s_obj","keys":[{"k":"s_shape","x":5560,"y":1700,"pose":"piensa","cara":"neutral"},{"k":"goggles","x":5560,"y":1700,"pose":"apunta","cara":"feliz"}]},
   {**SA,"var":44,"desde":"s_obj","keys":[{"k":"s_obj","x":6820,"y":1700,"pose":"cruzado","cara":"neutral"},{"k":"drones","x":6820,"y":1700,"pose":"apunta","cara":"neutral"}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.05,
 "zonas":[{"x0":-300,"x1":1300,"set":"calle","luz":"tenue"},{"x0":1300,"x1":2600,"set":"cielo","k":"s_2019"},{"x0":2600,"x1":3900,"set":"estudio","k":"s_leak"},
          {"x0":3900,"x1":5200,"set":"estudio","k":"s_2022"},{"x0":5200,"x1":6500,"set":"oficina","k":"s_shape","luz":"tenue"},{"x0":6500,"x1":7900,"set":"cielo","k":"s_obj"}],
 "pan":[{"k":"s_2019","x":1300,"dur":0.9},{"k":"s_leak","x":2600,"dur":0.9},{"k":"s_2022","x":3900,"dur":0.9},{"k":"s_shape","x":5200,"dur":0.9},{"k":"s_obj","x":6500,"dur":0.9}],
 "props":P,"actores":A,
 "burbujas":[{"k":"drones","de":5,"texto":"MOST LIKELY DRONES.","fin":"s_fin","dx":200}],
 "numeros":[],
 "zoom":[{"k":0.1,"s":1.08,"x":480,"y":1350,"dur":0.7},{"k":"congress","s":1.0,"dur":0.4},{"k":"triangles","s":1.15,"x":1900,"y":1050,"dur":0.5},{"k":"s_leak","s":1.0,"dur":0.3},
         {"k":"real","s":1.12,"x":3220,"y":1300,"dur":0.4},{"k":"s_2022","s":1.0,"dur":0.3},{"k":"hearing","s":1.2,"x":4380,"y":1420,"dur":0.4},{"k":"s_shape","s":1.0,"dur":0.3},
         {"k":"goggles","s":1.12,"x":5800,"y":1250,"dur":0.4},{"k":"s_obj","s":1.0,"dur":0.3},{"k":"s_fin","s":1.0,"dur":0.3}],
 "sacudidas":[{"k":"triangles","f":12}],
 "titulos":[{"k":0.2,"texto":"THE PYRAMID UFOS","c":"rojo","fin":"s_2019"},
            {"k":"s_2019","texto":"FILMED AT SEA · 2019","c":"cian","fin":"s_leak"},
            {"k":"s_leak","texto":"LEAKED · 2021","c":"amar","fin":"s_2022"},
            {"k":"s_2022","texto":"PUBLIC HEARING · 2022","c":"verde","fin":"s_shape"},
            {"k":"s_shape","texto":"WHY A TRIANGLE","c":"amar","grande":True,"fin":"s_obj"},
            {"k":"s_obj","texto":"THE OBJECTS","c":"rojo","fin":"s_fin"}],
 "chips":[{"k":"pentagon","texto":"PENTAGON: IT'S REAL FOOTAGE","c":"verde","fin":"s_2022"},
          {"k":"official","texto":"NAVY INTELLIGENCE","c":"cian","fin":"s_shape"},
          {"k":"goggles","texto":"NIGHT VISION + CAMERA LENS","c":"amar","fin":"s_obj"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"ENOUGH FOR YOU?","cierre2":"Yes or no? Comment","paises":["YES","NO"],
 "sfx":[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.0,"fade":0.4,"g":0.08}],"cta":"FOLLOW FOR MORE","like":"LIKE"}
poner_sets(E,[("nocheV",{"sem":19,"ciudad":False,"montes":False}),("nocheV",{"sem":5,"ciudad":False,"montes":False}),("noticiasV",{"cintillo":"2021: PENTAGON CONFIRMS UFO VIDEO IS REAL"}),("noticiasV",{"cintillo":"2022: FIRST PUBLIC UFO HEARING IN 50 YEARS"}),("labV",{"pantalla":"NIGHT VISION","pantalla2":"LENS EFFECT"}),("nocheV",{"sem":88,"ciudad":True})])
quitar_props(E,["tv"])
insertar(E,"pyramid","s_2019",1300,"vitrinaV",{"fondo":["#12301e","#0a1c12","#030806"],"luz2":"150,255,190"},[{"tipo":"trianguloP","x":540,"y":1150,"s":1.9}])
insertar(E,"camera","goggles",5200,"vitrinaV",{"fondo":["#1d2a4a","#0d1428","#03050c"],"luz2":"200,215,255"},[{"tipo":"lupa","x":540,"y":1300,"s":3.2}])
g={"titulo":"The Pyramid UFOs Were a Camera Trick 🔺","texto_pantalla":"WHY A TRIANGLE","lote":"R2026112401","marca":"THE RABBIT LOOP",
"nota_datos":"Julio 2019: personal del USS Russell (Armada de EE.UU.) grabó con visión nocturna objetos con forma de triángulo/pirámide. El video se filtró en abril de 2021 y el Pentágono (Sue Gough) confirmó que lo tomó personal de la Armada. 17-may-2022, audiencia pública en la Cámara (la primera sobre ovnis en más de 50 años): Scott Bray, subdirector de Inteligencia Naval, mostró el video y dijo que la forma triangular se debe a la luz que pasa por los lentes de visión nocturna y luego es grabada por una cámara réflex, y que con razonable confianza los objetos eran sistemas aéreos no tripulados (drones). Fuentes: audiencia del Congreso (C-SPAN/Reuters), Wikipedia (Pentagon UFO videos), Mick West (efecto bokeh).",
"frases":frases,"frases_voz":voz,"fuentes":["https://en.wikipedia.org/wiki/Pentagon_UFO_videos","https://www.reuters.com/"],"escena":E}
guardar("R2026112401_src.json",g)
