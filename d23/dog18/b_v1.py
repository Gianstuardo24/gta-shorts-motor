import sys; sys.path.insert(0,'/home/claude/d23'); from comun import *
frases=["When your dog suddenly races around the house like a rocket, there's a name for it.",
"Vets call it FRAPs: frenetic random activity periods.",
"Most of the time, it's a burst of built-up energy or excitement.",
"It often happens after a bath, after time in a crate, or when you get home.",
"It's most common in puppies and young dogs, and it usually lasts just a few minutes.",
"Vets say it's normal. Just keep them away from slippery floors while they zoom.",
"Tell me when your dog gets the zoomies.",
"Follow to decode your dog."]
voz=[f.replace("FRAPs","FRAPS") for f in frases]
M=[["races",0,"^races"],["rocket",0,"^rocket"],["name",0,"^name"],["s_frap",1,None],["fraps",1,"^frap"],["frenetic",1,"^frenetic"],
["s_energy",2,None],["energy",2,"^energy"],["excitement",2,"^excitement"],["s_when",3,None],["bath",3,"^bath"],["crate",3,"^crate"],["home",3,"^home"],
["s_pup",4,None],["puppies",4,"^puppies"],["minutes",4,"^minutes"],["s_safe",5,None],["normal",5,"^normal"],["slippery",5,"^slippery"],["s_fin",6,None],["s_cta",7,None]]
run=[{"k":0.0,"x":900,"y":1760},{"k":"races","x":900,"y":1760},{"k":"races+0.7","x":150,"y":1760},{"k":"races+1.4","x":900,"y":1760},{"k":"races+2.1","x":150,"y":1760},{"k":"races+2.8","x":760,"y":1745}]
P=[{"tipo":"sofa","x":330,"y":1720,"s":1.3,"k":0},
   perro(x=900,y=1760,s=1.0,k=0,fin="s_frap",pose="parado",camina=True,mov=run,lengua=True),
   perro(x=760,y=1745,s=1.0,k="s_frap",dir=-1,fin="s_when",estados=[{"k":"energy","lengua":True}]),
   {"tipo":"puerta","x":1950,"y":1700,"s":1.1,"k":"s_when"},
   perro(x=1450,y=1760,s=1.0,k="s_when",fin="s_pup",pose="parado",camina=True,lengua=True,mov=[{"k":"s_when","x":1450,"y":1760},{"k":"s_when+0.8","x":2300,"y":1760},{"k":"s_when+1.6","x":1500,"y":1760},{"k":"s_when+2.4","x":2250,"y":1760},{"k":"s_when+3.2","x":1600,"y":1760}]),
   perro(x=2900,y=1760,s=0.6,k="s_pup",fin="s_safe",pose="parado",camina=True,lengua=True,mov=[{"k":"s_pup","x":2750,"y":1760},{"k":"s_pup+0.8","x":3500,"y":1760},{"k":"s_pup+1.6","x":2800,"y":1760},{"k":"s_pup+2.4","x":3450,"y":1760},{"k":"s_pup+3.2","x":3150,"y":1760}]),
   perro(x=3400,y=1770,s=0.55,k="s_pup+0.3",fin="s_safe",pose="parado",camina=True,lengua=True,color="#f2efe9",color2="#ffffff",oscuro="#c9bfae",lejos="#e0d8ca",collar="azul",mov=[{"k":"s_pup+0.3","x":3500,"y":1770},{"k":"s_pup+1.1","x":2800,"y":1770},{"k":"s_pup+1.9","x":3450,"y":1770},{"k":"s_pup+2.7","x":2900,"y":1770},{"k":"s_pup+3.5","x":3300,"y":1770}]),
   perro(x=760,y=1745,s=1.0,k="s_safe",dir=-1,estados=[{"k":"normal","lengua":True}])]
A=[{"look":"gamer","var":101,"camisa":"#5c6bc0","pelo":"#2b1b14","s":1.0,"hasta":"s_when","keys":[
    {"k":0,"x":300,"y":1714,"pose":"sentado","cara":"sorpresa","z":1800},
    {"k":"rocket","x":300,"y":1714,"pose":"sentado","cara":"risa","z":1800,"fx":"salto"},
    {"k":"s_frap","x":300,"y":1714,"pose":"sentado","cara":"feliz","z":1800}]},
   {"look":"gamer","var":101,"camisa":"#5c6bc0","pelo":"#2b1b14","s":1.0,"desde":"home","hasta":"s_pup","keys":[
    {"k":"home","x":1950,"y":1700,"pose":"saluda","cara":"feliz"},{"k":"home+0.8","x":1950,"y":1700,"pose":"celebra","cara":"risa","fx":"salto"}]},
   {"look":"gamer","var":101,"camisa":"#5c6bc0","pelo":"#2b1b14","s":1.0,"desde":"s_safe","keys":[
    {"k":"s_safe","x":300,"y":1714,"pose":"sentado","cara":"feliz","z":1800}]}]
E={"momentos":M,"escenas":[{"tipo":"pelicula","desde":"0","escala":1.0,
 "zonas":[{"x0":-300,"x1":1300,"set":"sala","luz":"tenue"},{"x0":1300,"x1":2600,"set":"sala","k":"s_when"},{"x0":2600,"x1":3900,"set":"calle","k":"s_pup"}],
 "pan":[{"k":"s_when","x":1300,"dur":0.9},{"k":"s_pup","x":2600,"dur":0.9},{"k":"s_safe","x":0,"dur":1.1}],
 "props":P,"actores":A,
 "extras":[{"look":"cliente","var":131,"x0":2600,"x1":3900,"vel":60,"y":1380,"s":0.55,"luz":0.45,"desde":"s_pup","hasta":"s_safe"},{"look":"jugadora","var":132,"x0":2600,"x1":3900,"vel":-70,"off":500,"y":1380,"s":0.55,"luz":0.45,"desde":"s_pup","hasta":"s_safe"}],
 "burbujas":[{"k":"rocket","de":0,"texto":"AGAIN?!","fin":"s_frap","dx":150}],
 "zoom":[{"k":0.1,"s":1.1,"x":540,"y":1550,"dur":0.6},{"k":"s_frap","s":1.0,"dur":0.5},{"k":"energy","s":1.25,"x":700,"y":1560,"dur":0.6},
         {"k":"s_when","s":1.0,"dur":0.5},{"k":"s_pup","s":1.15,"x":3150,"y":1620,"dur":0.6},{"k":"s_safe","s":1.0,"dur":0.5}],
 "sacudidas":[{"k":"races","f":6,"dur":2.6}],
 "titulos":[{"k":0.2,"texto":"THE ZOOMIES","c":"amar","fin":"s_frap"},
            {"k":"fraps","texto":"F.R.A.P.s","c":"cian","grande":True,"fin":"s_energy"},
            {"k":"s_energy","texto":"PURE ENERGY","c":"amar","fin":"s_when"},
            {"k":"s_when","texto":"WHEN IT HAPPENS","c":"rosa","fin":"s_pup"},
            {"k":"s_pup","texto":"PUPPIES + YOUNG DOGS","c":"cian","fin":"s_safe"},
            {"k":"s_safe","texto":"NORMAL","c":"verde","fin":"s_fin"}],
 "chips":[{"k":"frenetic","texto":"FRENETIC RANDOM ACTIVITY PERIODS","c":"cian","fin":"s_energy"},
          {"k":"bath","texto":"AFTER A BATH","c":"cian","fin":"crate"},
          {"k":"crate","texto":"OUT OF THE CRATE","c":"amar","fin":"home"},
          {"k":"home","texto":"WHEN YOU GET HOME","c":"rosa","fin":"s_pup"},
          {"k":"minutes","texto":"A FEW MINUTES","c":"cian","fin":"s_safe"},{"k":"slippery","texto":"NO SLIPPERY FLOORS","c":"rojo","fin":"s_fin"}]},
 {"tipo":"cierre","desde":"s_fin"}],
 "cierre":"WHEN DOES YOURS ZOOM?","cierre2":"Tell us when. Comment","paises":["BATH","HOME","NIGHT"],"cta":"FOLLOW FOR MORE","like":"LIKE","sfx":[]}
g={"titulo":"Why Your Dog Gets the Zoomies 🐶","texto_pantalla":"THE ZOOMIES","lote":"D2026112302","marca":"THE DOGS DECODER",
"nota_datos":"FRAPs (frenetic random activity periods): liberación de energía/emoción; frecuentes tras el baño, al salir del canil o al llegar el dueño; más comunes en cachorros y perros jóvenes; duran pocos minutos; normales; pisos duros/resbalosos aumentan riesgo de caída. Fuentes: Cornell Riney Canine Health Center, Live Science, Discover, Rover (veterinaria).",
"frases":frases,"frases_voz":voz,"fuentes":["https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/health-info/what-are-zoomies","https://www.livescience.com/","https://www.discovermagazine.com/why-do-dogs-suddenly-get-the-zoomies-45351"],"escena":E}
guardar("D2026112302_01_src.json",g)
