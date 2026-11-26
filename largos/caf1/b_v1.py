import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b1980s\b","nineteen eighties"),(r"\b30 milliliters","thirty milliliters"),(r"\b25 to 30 seconds","twenty-five to thirty seconds"),
   (r"\b12 to 24 hours","twelve to twenty-four hours"),(r"\b1 ounce","one ounce"),(r"\b10 drinks","ten drinks"),(r"\b3 things","three things"),
   (r"Capuchin","Capu-chin"),(r"macchiato","mah-kee-AH-toe"),(r"Macchiato","Mah-kee-AH-toe"),(r"ristretto","ree-STRET-oh"),(r"Ristretto","Ree-STRET-oh"),
   (r"affogato","ah-fo-GAH-toe"),(r"Affogato","Ah-fo-GAH-toe"),(r"cortado","cor-TAH-doe"),(r"Cortado","Cor-TAH-doe"),(r"lungo","LOON-go"),(r"Lungo","LOON-go")]
L=Largo(R); L.hints=[]
BAR=dict(look="gamer",var=801,camisa="#5d4037",s=0.95)
CLI=dict(look="jugadora",var=802,s=0.95)
CL2=dict(look="ejecutivo",var=803,camisa="#1565c0",s=1.0)
ESP="#3e2010"; LEC="#f3e6d3"; ESPU="#fffaf0"; AGU="#7fb3d5"

# ---------- 0 · INTRO ----------
t=L.tramo("cafe",capitulo="One shot, ten drinks")
t.dice("Almost every drink on a coffee shop menu starts with the exact same thing: one shot of espresso.",
       "What changes is just three things: how much water you add, how much milk, and how much foam.",
       "Once you understand those 3 things, you can read any coffee menu in the world.",
       "So today, we will build 10 drinks from the same shot, one by one, and you will finally know what you are ordering.")
kshot=t.m("shot",0,"^espresso"); kthree=t.m("three",1,"^three"); kwat=t.m("wat",1,"^water"); kmil=t.m("mil",1,"^milk"); kfoam=t.m("foam",1,"^foam"); kmenu=t.m("menu",2,"^menu"); kten=t.m("ten",3,"^10")
t.actor(BAR,[{"x":600,"pose":"parado","cara":"feliz"},{"k":kshot,"x":600,"pose":"ofrece","cara":"feliz","objeto":"taza"},{"k":kten,"x":600,"pose":"celebra","cara":"risa"}])
t.prop("taza",1250,1600,1.3,k=kshot)
L.titulo(kshot,"ONE SHOT OF ESPRESSO","amar",fin=kthree)
L.chip(kwat,"WATER","cian",fin=kmil); L.chip(kmil,"MILK","amar",fin=kfoam); L.chip(kfoam,"FOAM","rosa",fin=kmenu)
L.titulo(kten,"1 SHOT · 10 DRINKS","amar",grande=True)

# ---------- 1 · ESPRESSO ----------
t=L.tramo("cafe",capitulo="1. Espresso")
t.dice("Drink number one is the base of everything: the espresso.",
       "Hot water is pushed through finely ground coffee under pressure, usually in about 25 to 30 seconds.",
       "That pressure is the secret: it pulls out a lot of flavor in very little time, and creates the golden foam on top, called crema.",
       "A single shot is small, around 30 milliliters, which is about 1 ounce.")
kpres=t.m("pres",1,"^pressure"); ksec=t.m("sec",2,"^secret"); kcre=t.m("cre",2,"^crema"); k30=t.m("k30",3,"^30")
L.titulo(t.key,"1 · ESPRESSO","amar",grande=True,fin=kpres)
t.actor(BAR,[{"x":550,"pose":"juega","cara":"neutral"},{"k":ksec,"x":550,"pose":"apunta","cara":"feliz"}])
t.prop("taza",1250,1600,1.4,k=t.key)
L.chip(kpres,"PRESSURE · 25-30 SECONDS","cian",fin=kcre); L.chip(kcre,"CREMA: THE GOLDEN FOAM","amar",fin=k30)
L.numero(k30,30,"ML · ONE SHOT",suf=" ml",c="amar")

# ---------- 2 · RISTRETTO Y LUNGO ----------
t=L.tramo("cafe",capitulo="2 & 3. Ristretto and lungo")
t.dice("Now, the first thing we can change is the water.",
       "Use less water with the same coffee, and you get a ristretto, which means restricted in Italian: shorter, thicker, and sweeter.",
       "Push more water through the same coffee, and you get a lungo, which means long: a bigger cup, but more bitter, because the water keeps pulling out the harsh parts.")
krist=t.m("rist",1,"^ristretto"); klun=t.m("lun",2,"^lungo"); kbit=t.m("bit",2,"^bitter")
t.prop("comparaBarras",975,1450,1.2,k=krist,v=[[20,"RISTRETTO","#ffb74d"],[30,"ESPRESSO","#8d6e63"],[55,"LUNGO","#4fc3f7"]])
L.chip(krist,"RISTRETTO = RESTRICTED","amar",fin=klun); L.chip(klun,"LUNGO = LONG","cian",fin=kbit); L.chip(kbit,"MORE WATER · MORE BITTER","rojo")

# ---------- 4 · AMERICANO ----------
t=L.tramo("cafe",capitulo="4. Americano")
t.dice("Drink number four adds the water after the shot is made: the americano.",
       "It is simply espresso with hot water poured on top, so it tastes closer to a regular cup of filter coffee.",
       "There is a popular story that American soldiers in Italy during World War Two asked for water in their espresso, to make it taste like coffee from home.",
       "It is a great story, but nobody has ever proven it, so take it with a grain of sugar.")
kafter=t.m("after",0,"^after"); kfil=t.m("fil",1,"^filter"); ksol=t.m("sol",2,"^soldiers"); kprov=t.m("prov",3,"^proven")
L.titulo(t.key,"4 · AMERICANO","cian",grande=True,fin=kafter)
t.actor(CL2,[{"x":600,"pose":"parado","cara":"neutral"},{"k":ksol,"x":600,"pose":"explica","cara":"feliz"},{"k":kprov,"x":600,"pose":"cruzado","cara":"risa"}])
t.prop("taza",1250,1600,1.3,k=t.key)
L.chip(kafter,"ESPRESSO + HOT WATER","cian",fin=ksol); L.chip(ksol,"THE SOLDIER STORY","amar",fin=kprov); L.chip(kprov,"NEVER PROVEN","rojo")

# ---------- 5 · MACCHIATO ----------
t=L.tramo("cafe",luz="tenue",capitulo="5. Macchiato")
t.dice("Now we start adding milk, a little at a time.",
       "Drink number five is the macchiato, which means stained, or marked, in Italian.",
       "It is an espresso marked with just a small spot of milk foam on top.",
       "Be careful, because in many big coffee chains, a macchiato is a large sweet milk drink, which is almost the opposite.")
kmac=t.m("mac",1,"^macchiato"); kspot=t.m("spot",2,"^spot"); kchain=t.m("chain",3,"^chains")
L.titulo(kmac,"5 · MACCHIATO","rosa",grande=True,fin=kspot)
t.actor(BAR,[{"x":550,"pose":"parado","cara":"feliz"},{"k":kspot,"x":550,"pose":"ofrece","cara":"feliz","objeto":"taza"},{"k":kchain,"x":550,"pose":"piensa","cara":"sorpresa"}])
L.chip(kspot,"ESPRESSO + A SPOT OF FOAM","rosa",fin=kchain); L.chip(kchain,"IN BIG CHAINS: A DIFFERENT DRINK","amar")

# ---------- 6 · CORTADO ----------
t=L.tramo("cafe",capitulo="6. Cortado")
t.dice("Drink number six comes from Spain: the cortado.",
       "The name comes from cortar, which means to cut, because the espresso is cut with about the same amount of warm milk.",
       "There is very little foam, so it is smooth, small, and still very strong.")
kcort=t.m("cort",0,"^cortado"); kcut=t.m("cut",1,"^cut"); ksmo=t.m("smo",2,"^smooth")
L.titulo(t.key,"6 · CORTADO","amar",grande=True,fin=kcut)
t.prop("comparaBarras",975,1450,1.2,k=kcut,v=[[50,"ESPRESSO","#8d6e63"],[50,"MILK","#f3e6d3"],[5,"FOAM","#fffaf0"]])
L.chip(kcut,"CORTAR = TO CUT","cian",fin=ksmo); L.chip(ksmo,"HALF ESPRESSO · HALF MILK","amar")

# ---------- 7 · CAPPUCCINO ----------
t=L.tramo("cafe",capitulo="7. Cappuccino")
t.dice("Drink number seven is probably the most famous one: the cappuccino.",
       "The classic recipe is easy to remember, because it comes in thirds: one third espresso, one third steamed milk, and one third foam.",
       "The name comes from the Capuchin friars, an order of monks whose brown robes were about the same color as coffee mixed with milk.")
kcap=t.m("cap",0,"^cappuccino"); kthird=t.m("third",1,"^thirds"); kfri=t.m("fri",2,"^friars")
L.titulo(t.key,"7 · CAPPUCCINO","rosa",grande=True,fin=kthird)
t.prop("comparaBarras",975,1450,1.2,k=kthird,v=[[33,"ESPRESSO","#8d6e63"],[33,"MILK","#f3e6d3"],[33,"FOAM","#fffaf0"]],fin=kfri)
t.actor(dict(look="sabio",var=804,camisa="#6d4c41",s=0.95),[{"k":kfri,"x":975,"pose":"saluda","cara":"feliz"}],desde=kfri)
L.chip(kthird,"1/3 · 1/3 · 1/3","amar",fin=kfri); L.chip(kfri,"NAMED AFTER THE CAPUCHIN FRIARS","cian")

# ---------- 8 · FLAT WHITE ----------
t=L.tramo("cafe",luz="tenue",capitulo="8. Flat white")
t.dice("Drink number eight is the flat white, and it starts a friendly fight between two countries.",
       "Australia and New Zealand both say they invented it, back in the 1980s.",
       "It has more milk than a cortado, but only a thin, silky layer of foam on top, so the coffee taste stays strong.",
       "Think of it as a smaller, stronger latte.")
kfight=t.m("fight",0,"^fight"); kaus=t.m("aus",1,"^australia"); kthin=t.m("thin",2,"^thin"); kthink=t.m("think",3,"^smaller")
L.titulo(t.key,"8 · FLAT WHITE","verde",grande=True,fin=kfight)
t.actor(CLI,[{"k":kaus,"x":550,"pose":"apunta","cara":"enojado"}],desde=kaus,hasta=kthin)
t.actor(CL2,[{"k":kaus,"x":1400,"pose":"apunta","cara":"enojado","dir":-1}],desde=kaus,hasta=kthin)
L.chip(kaus,"AUSTRALIA vs NEW ZEALAND","rojo",fin=kthin)
t.prop("comparaBarras",975,1450,1.2,k=kthin,v=[[35,"ESPRESSO","#8d6e63"],[60,"MILK","#f3e6d3"],[10,"FOAM","#fffaf0"]])
L.chip(kthin,"THIN, SILKY FOAM","amar",fin=kthink); L.titulo(kthink,"A SMALLER, STRONGER LATTE","verde")

# ---------- 9 · LATTE ----------
t=L.tramo("cafe",capitulo="9. Latte")
t.dice("And drink number nine is the biggest of the milk drinks: the latte.",
       "Its full name is caffè latte, which simply means coffee and milk.",
       "It is mostly steamed milk, with a shot of espresso and a thin layer of foam, which is why it is the softest drink on the menu.",
       "Fun fact: if you go to Italy and just ask for a latte, you might get a glass of plain milk.")
klat=t.m("lat",0,"^latte"); kfull=t.m("full",1,"^coffee"); kmost=t.m("most",2,"^mostly"); kitaly=t.m("italy",3,"^italy")
L.titulo(t.key,"9 · LATTE","amar",grande=True,fin=kfull)
t.prop("comparaBarras",975,1450,1.2,k=kmost,v=[[20,"ESPRESSO","#8d6e63"],[75,"MILK","#f3e6d3"],[8,"FOAM","#fffaf0"]],fin=kitaly)
L.chip(kfull,"CAFFÈ LATTE = COFFEE AND MILK","cian",fin=kmost); L.chip(kmost,"MOSTLY MILK","amar",fin=kitaly)
t.actor(CLI,[{"k":kitaly,"x":700,"pose":"parado","cara":"sorpresa","objeto":"taza"}],desde=kitaly)
L.chip(kitaly,"IN ITALY: \"LATTE\" = MILK","rojo")

# ---------- 10 · MOCHA Y AFFOGATO ----------
t=L.tramo("cafe",luz="tenue",capitulo="10. Mocha, and a dessert")
t.dice("Drink number ten adds one more ingredient: chocolate.",
       "A mocha is basically a latte with chocolate, and its name comes from Mocha, a port in Yemen that was once one of the biggest coffee markets in the world.",
       "And as a bonus, here is a dessert: the affogato, which means drowned.",
       "It is a scoop of vanilla ice cream, drowned in a hot shot of espresso.")
kcho=t.m("cho",0,"^chocolate"); kmoc=t.m("moc",1,"^mocha"); kyem=t.m("yem",1,"^yemen"); kaff=t.m("aff",2,"^affogato"); kice=t.m("ice",3,"^ice")
L.titulo(t.key,"10 · MOCHA","rosa",grande=True,fin=kmoc)
L.chip(kmoc,"LATTE + CHOCOLATE","amar",fin=kyem); L.chip(kyem,"NAMED AFTER A PORT IN YEMEN","cian",fin=kaff)
L.titulo(kaff,"BONUS · AFFOGATO","verde",fin=kice); L.chip(kice,"ICE CREAM + ESPRESSO","amar")
t.actor(BAR,[{"x":975,"pose":"parado","cara":"feliz"},{"k":kaff,"x":975,"pose":"ofrece","cara":"risa","objeto":"taza"}])

# ---------- RECAP ----------
t=L.tramo("cafe",capitulo="The cheat sheet")
t.dice("So here is your cheat sheet.",
       "Less milk to more milk: macchiato, cortado, cappuccino, flat white, and latte.",
       "Water changes the strength, milk changes the softness, and foam changes the texture.",
       "One shot, and a whole menu.",
       "Comment your usual order below.",
       "Follow Coffee But Why for more coffee answers.")
kless=t.m("less",1,"^macchiato"); kwch=t.m("wch",2,"^water"); kone=t.m("one",3,"^menu")
L.inserto(kless,kwch,"tableroH",{"titulo":"THE CHEAT SHEET","filas":[["MACCHIATO","A SPOT OF FOAM"],["CORTADO","HALF MILK"],["CAPPUCCINO","THIRDS"],["FLAT WHITE","THIN FOAM"],["LATTE","MOSTLY MILK"]]},mov="fijo")
L.chip(kwch,"WATER = STRENGTH · MILK = SOFTNESS · FOAM = TEXTURE","cian",fin=kone)
L.titulo(kone,"ONE SHOT · A WHOLE MENU","amar",grande=True)
t.actor(BAR,[{"x":700,"pose":"parado","cara":"feliz"},{"k":kone,"x":700,"pose":"saluda","cara":"risa"}])

meta={"titulo":"Every Coffee Drink, Explained","texto_pantalla":"1 SHOT · 10 DRINKS","lote":"L2026112301caf","marca":"COFFEE BUT WHY?","tema":"",
"nota_datos":"Fuentes (23-nov): Merriam-Webster (espresso 'pressed-out', macchiato 'con una mancha', cappuccino por los frailes capuchinos), Wikipedia Cappuccino y Britannica (color de los habitos), Kaldi's Coffee y Breville (flat white Australia/NZ 1980s; latte = leche en Italia), History Oasis y Merriam-Webster (mocha por el puerto de Mokha, Yemen), Jamie Oliver/Scotsman (macchiato 'stained'; en cadenas es otra bebida). Ratios de leche/espuma son aproximados y cambian segun la cafeteria. Historia del americano y los soldados: no comprobada (se dice en el video).",
"fuentes":["https://www.merriam-webster.com/wordplay/where-do-we-get-cappuccino-from","https://en.wikipedia.org/wiki/Cappuccino","https://kaldiscoffee.com/pages/espresso-drinks-explained","https://www.breville.com/en-us/blog/coffee-and-espresso/how-are-flat-whites-cappuccinos-lattes-different"]}
g=L.armar(meta,cola=18.0,final={"marca":"COFFEE BUT WHY?","texto":"FOLLOW FOR MORE COFFEE ANSWERS","a":"WATCH THIS NEXT","b":"SUBSCRIBE FOR MORE"})
json.dump(g,open("L2026112301caf_src.json","w"),ensure_ascii=False)
w=sum(len(f.split()) for f in L.frases); print("frases",len(L.frases),"palabras",w,"tramos",len(L.tramos))
