import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["Blockbuster lost everything. And it all came down to one decision. But there's a detail almost nobody knows.",
"In 2000, Blockbuster was the king of movie rentals, with about 9,000 stores.",
"Netflix was a small startup mailing DVDs, and losing money.",
"Its founders got a meeting with Blockbuster's CEO. Their offer: sell Netflix for 50 million dollars.",
"He listened. At first, he laughed, and then he followed with a flat no.",
"Now the detail almost nobody knows.",
"Netflix's founders got the invitation less than 12 hours before the meeting. With the clock against them and almost broke, they spent money they didn't have on a jet, just to hear that no.",
"They walked in wearing shorts, flip-flops and a Hawaiian shirt.",
"Ten years later, Blockbuster filed for bankruptcy. Netflix became worth billions.",
"Today, only one Blockbuster is still alive, in Oregon.",
"Lesson: when a small player changes how people buy, take the meeting seriously.",
"Tell me if you would have bought it.",
"Follow for the next million dollar mistake."]
V=[f.replace("In 2000","In two thousand").replace("9,000","nine thousand").replace("50 million","fifty million").replace("12 hours","twelve hours") for f in F]
E1=dict(look="ejecutivo",var=104,pelo="#9e9e9e",camisa="#263238",corbata="#1565c0",s=1.0)
N1=dict(look="jugador",var=105,pelo="#4e342e",camisa="#ff7043",s=1.0)
N2=dict(look="jugador",var=106,pelo="#212121",camisa="#26c6da",s=1.0)
video("M2026112502_src.json","M2026112502","MILLION DOLLAR MISTAKE","Blockbuster LOST Everything in ONE Decision 📼❌","LOST EVERYTHING",F,V,
 marcas=[("lost0",0,"^lost"),("decision",0,"^decision"),("king",1,"^king"),("m9000",1,"^9"),("dvds",2,"^dvds"),("losing",2,"^losing"),("m50",3,"^50"),("laughed",4,"^laughed"),("flat",4,"^flat"),("detail",5,"^detail"),("hours",6,"^hours"),("jet",6,"^jet"),("shorts",7,"^shorts"),("bankruptcy",8,"^bankruptcy"),("billions",8,"^billions"),("one",9,"^one"),("lesson",10,"^lesson")],
 escenas=[
  {"z":"nocheV","o":{"ciudad":True,"sem":51},"props":[{"tipo":"cartel","x":540,"y":1330,"s":1.2,"texto":"VIDEO RENTALS","z":1500},{"tipo":"neblina","x":540,"y":1800,"a":.14}]},
  {"k":"s_1","i":["#16243f","#0b1222","#020408"],"luz2":"190,210,255","pedestal":True,"titulo":("2000","amar"),"props":[{"tipo":"cartel","x":540,"y":1300,"s":1.1,"texto":"VIDEO RENTALS"}]},
  {"k":"s_2","i":["#1c1c24","#0c0c12","#020203"],"luz2":"190,210,255","pedestal":True,"props":[{"tipo":"sobre","x":540,"y":1300,"s":1.3,"color":"#1565c0","texto":"DVD BY MAIL"}]},
  {"k":"s_3","z":"corporativoV","o":{"ticker":"NEW DEAL ▼"},"actores":[{**N1,"keys":[{"k":"s_3","x":300,"pose":"explica","cara":"feliz"}]},{**E1,"keys":[{"k":"s_3","x":780,"pose":"cruzado","cara":"neutral"}]}]},
  {"k":"s_4","z":"palacioV","actores":[{**E1,"keys":[{"k":"s_4","x":420,"pose":"cruzado","cara":"neutral"},{"k":"laughed","x":420,"pose":"aplaude","cara":"risa"},{"k":"flat","x":420,"pose":"cruzado","cara":"neutral"}]}]},
  {"k":"flat","i":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220","props":[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"OFFER · 2000","dato":"NETFLIX FOR $50 MILLION","sello":"REJECTED","selloc":"rojo","filaDato":5}]},
  {"k":"s_5","i":["#10182a","#070b14","#010205"],"luz2":"200,220,255","pedestal":True,"props":[{"tipo":"lupa","x":540,"y":1250,"s":2.0,"flota":6},{"tipo":"neblina","y":1700,"a":.12}]},
  {"k":"s_6","z":"montanaV","o":{"avion":1},"props":[{"tipo":"neblina","x":540,"y":1750,"a":.12}]},
  {"k":"s_7","z":"corporativoV","actores":[{**N1,"keys":[{"k":"s_7","x":300,"pose":"explica","cara":"feliz"}]},{**N2,"keys":[{"k":"s_7","x":560,"pose":"cruzado","cara":"neutral"}]},{**E1,"keys":[{"k":"s_7","x":860,"pose":"piensa","cara":"neutral"}]}]},
  {"k":"s_8","i":["#1c1c24","#0c0c12","#020203"],"luz2":"255,210,150","pedestal":True,"props":[{"tipo":"calendario","x":540,"y":1300,"s":1.7,"mes":"BANKRUPTCY","anio":2010,"color":"#c62828"}]},
  {"k":"s_9","z":"nocheV","o":{"ciudad":True,"sem":52},"props":[{"tipo":"cartel","x":540,"y":1330,"s":1.0,"texto":"LAST STORE","z":1500},{"tipo":"neblina","x":540,"y":1800,"a":.14}]},
  {"k":"s_10","z":"tallerV","actores":[{**N1,"keys":[{"k":"s_10","x":420,"pose":"explica","cara":"feliz"}]}],"props":[{"tipo":"sobre","x":820,"y":1700,"s":.6,"color":"#1565c0","z":1800}]}],
 numeros=[{"k":"m9000","n":9000,"c":"amar","etq":"STORES","fin":"s_2"},{"k":"m50","n":50,"pre":"$","suf":" M","c":"verde","etq":"ASKING PRICE","fin":"s_4"},{"k":"hours","n":12,"suf":" H","c":"rosa","etq":"LESS THAN · NOTICE","fin":"s_7","y":760}],
 emojis=[{"k":"lost0","e":"😬"},{"k":"laughed","e":"😂","y":560},{"k":"jet","e":"✈️"},{"k":"lesson","e":"💡","dur":1.2}],
 gancho2=5,cierre="WOULD YOU BUY IT?",cierre2="Tell me. Comment",paises=["YES","NO"],
 nota="Sept 2000, Dallas: Hastings, Randolph y McCarthy ofrecieron Netflix por US$50 M; Antioco lo rechazó. Aviso con menos de 12 h (Inc., Randolph 'That Will Never Work'); arrendaron un jet y llegaron en shorts, chalas y camisa hawaiana (ACS, Randolph). 'Laughed': versión de Randolph; Hastings dice que no llegó a tanto. Blockbuster ~9.000 tiendas (Fortune); quiebra 2010; queda una tienda en Bend, Oregon. Guion aprobado por Tao 25-nov (línea base).",
 fuentes=["https://fortune.com/2023/04/14/netflix-cofounder-marc-randolph-recalls-blockbuster-rejecting-chance-to-buy-it/","https://ia.acs.org.au/article/2016/netflix-pitched-itself-to-blockbuster-for--50m.html","https://marketplace.org/2020/09/08/ceo-reed-hastings-on-how-netflix-beat-blockbuster"])
