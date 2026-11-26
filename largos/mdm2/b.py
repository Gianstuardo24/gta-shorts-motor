import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b1886\b","eighteen eighty-six"),(r"\b1888\b","eighteen eighty-eight"),(r"\b1891\b","eighteen ninety-one"),(r"\b1894\b","eighteen ninety-four"),
   (r"\b1899\b","eighteen ninety-nine"),(r"\b1920s\b","nineteen twenties"),(r"\b1959\b","nineteen fifty-nine"),(r"\b2010\b","twenty ten"),(r"\b1915\b","nineteen fifteen"),(r"\b1919\b","nineteen nineteen"),(r"\b1920\b","nineteen twenty"),(r"\b1921\b","nineteen twenty-one"),(r"\$25 million","twenty-five million dollars"),(r"Terre Haute","Terra Hote"),
   (r"\$2,300","twenty-three hundred dollars"),(r"\$1\b","one dollar"),(r"\$8 billion","eight billion dollars"),(r"July 21","July twenty-first"),
   (r"\b200 countries","two hundred countries"),(r"\b70 years","seventy years"),(r"5 cents","five cents"),(r"Biedenharn","Beeden-harn"),(r"Candler","Candler")]
L=Largo(R); L.hints=[]
CAN=dict(look="ejecutivo",var=701,camisa="#5d4037",pelo="#9e9e9e",barba="#9e9e9e",s=1.0)
THO=dict(look="ejecutivo",var=702,camisa="#263238",pelo="#3e2723",s=1.0)
WHI=dict(look="ejecutivo",var=703,camisa="#37474f",pelo="#4e342e",barba="#4e342e",s=0.95)
BIE=dict(look="inventor",var=704,camisa="#6d4c41",pelo="#3e2723",s=0.95)
SOB=dict(look="gamer",var=705,camisa="#8e24aa",s=0.9)
CLI=dict(look="jugadora",var=706,s=0.95)
EJE=dict(look="ejecutivo",var=707,camisa="#b71c1c",pelo="#cfd8dc",s=1.0)

# ---------- 0 · INTRO ----------
t=L.tramo("casona",capitulo="The $1 deal")
t.dice("In 1899, the owner of Coca-Cola signed a deal that gave away the right to bottle his drink across most of the United States.",
       "The price was $1, and he never even bothered to collect it.",
       "Decades later, his own company would spend a fortune trying to take that right back.",
       "So the big question is why anyone would sell something that big for a single dollar.",
       "The real reason is smarter than it looks, and it comes with a catch that lasted for seventy years.")
kbot=t.m("bot",0,"^bottle"); kone=t.m("one",1,"^1$"); knev=t.m("nev",1,"^never"); kfor=t.m("for",2,"^fortune"); kwhy=t.m("why",3,"^question"); kcat=t.m("cat",4,"^catch")
t.actor(CAN,[{"x":600,"pose":"parado","cara":"feliz"},{"k":kone,"x":600,"pose":"ofrece","cara":"feliz"},{"k":kfor,"x":600,"pose":"piensa","cara":"neutral"},{"k":kcat,"x":600,"pose":"cruzado","cara":"neutral"}])
t.prop("botella1899",1250,1700,0.42,k=kbot)
t.prop("moneda",1250,1150,1.2,k=kone,fin=kfor)
L.titulo(kone,"$1","amar",grande=True,fin=knev); L.chip(knev,"NEVER COLLECTED","rojo",fin=kfor)
L.inserto(kfor,kwhy,"balanzaH",{"izq":{"txt":"$1","sub":"THE PRICE IN 1899","n":1},"der":{"txt":"???","sub":"WHAT IT COST TO UNDO","n":9},"kder":f"{kfor}+0.8"},mov="fijo")
L.titulo(kcat,"THE REAL REASON","rosa",grande=True)

# ---------- 1 · LA FUENTE ----------
t=L.tramo("cafe",capitulo="A drink for the soda fountain")
t.dice("Coca-Cola was invented in 1886, in Atlanta, by a pharmacist named John Pemberton.",
       "Back then, it was not sold in bottles: you drank it at a soda fountain, mixed by hand, for 5 cents a glass.",
       "A businessman named Asa Candler bought the rights to the drink, piece by piece, between 1888 and 1891, for about $2,300 in total.",
       "Candler was great at one thing: selling syrup to soda fountains, and putting the name Coca-Cola everywhere.")
kpem=t.m("pem",0,"^pemberton"); kfoun=t.m("foun",1,"^fountain"); kcent=t.m("cent",1,"^5"); kcan=t.m("can",2,"^candler"); k2300=t.m("k2300",2,"^2300"); ksyr=t.m("syr",3,"^syrup")
L.titulo(t.key,"ATLANTA · 1886","amar",fin=kpem)
t.actor(SOB,[{"x":1250,"pose":"parado","cara":"feliz","dir":-1},{"k":kfoun,"x":1250,"pose":"sostiene","cara":"feliz","dir":-1,"objeto":"taza"}],hasta=kcan)
t.actor(CLI,[{"x":700,"pose":"parado","cara":"feliz"},{"k":kcent,"x":700,"pose":"celebra","cara":"risa"}],hasta=kcan)
L.chip(kpem,"JOHN PEMBERTON · PHARMACIST","cian",fin=kfoun); L.chip(kcent,"5¢ A GLASS","verde",fin=kcan)
t.actor(CAN,[{"k":kcan,"x":975,"pose":"saluda","cara":"feliz"},{"k":ksyr,"x":975,"pose":"apunta","cara":"feliz"}],desde=kcan)
L.numero(k2300,2300,"WHAT CANDLER PAID · 1888-1891",pre="$",c="amar",fin=ksyr)
L.chip(ksyr,"HIS BUSINESS: SYRUP","rosa")

# ---------- 2 · LA PRIMERA BOTELLA ----------
t=L.tramo("casona",capitulo="The first bottle")
t.dice("In 1894, a candy store owner in Vicksburg, Mississippi, named Joseph Biedenharn, started putting Coca-Cola in bottles, so people could take it home.",
       "He even sent a case to Candler.",
       "Candler thanked him, and did nothing.",
       "One of his own nephews had already told him that bottles could sell a lot more Coca-Cola, but Candler stayed focused on the fountains.")
kbie=t.m("bie",0,"^biedenharn"); kcase=t.m("case",1,"^case"); knot=t.m("not",2,"^nothing"); kneph=t.m("neph",3,"^nephews")
t.actor(BIE,[{"x":500,"pose":"parado","cara":"feliz"},{"k":kcase,"x":500,"pose":"ofrece","cara":"feliz"}],hasta=knot)
t.actor(CAN,[{"x":1350,"pose":"parado","cara":"neutral","dir":-1},{"k":knot,"x":1350,"pose":"cruzado","cara":"neutral","dir":-1},{"k":kneph,"x":1350,"pose":"piensa","cara":"neutral","dir":-1}])
t.prop("botella1899",800,1700,0.35,k=kbie); t.prop("botella1899",900,1700,0.35,k=f"{kbie}+0.3")
L.chip(kbie,"VICKSBURG · 1894 · THE FIRST BOTTLES","amar",fin=kcase); L.titulo(knot,"\"THANKS.\" NOTHING ELSE.","rojo",fin=kneph)
L.chip(kneph,"FOCUSED ON THE FOUNTAINS","cian")

# ---------- 3 · EL TRATO ----------
t=L.tramo("reunion",capitulo="July 21, 1899")
t.dice("Then, in the summer of 1899, two lawyers from Chattanooga, Tennessee, came to see him in Atlanta.",
       "Their names were Benjamin Thomas and Joseph Whitehead, and they wanted the right to bottle Coca-Cola.",
       "On July 21, 1899, Candler signed the contract, giving them exclusive rights to bottle the drink across most of the United States.",
       "The price was $1, and Candler never collected it.")
kchat=t.m("chat",0,"^chattanooga"); ktho=t.m("tho",1,"^thomas"); kwhi=t.m("whi",1,"^whitehead"); ksig=t.m("sig",2,"^signed"); kexc=t.m("exc",2,"^exclusive"); kpri=t.m("pri",3,"^price")
t.actor(THO,[{"k":ktho,"x":1150,"pose":"saluda","cara":"feliz","dir":-1},{"k":ksig,"x":1150,"pose":"parado","cara":"feliz","dir":-1}],desde=kchat)
t.actor(WHI,[{"k":kwhi,"x":1450,"pose":"saluda","cara":"feliz","dir":-1},{"k":ksig,"x":1450,"pose":"celebra","cara":"risa","dir":-1}],desde=kchat)
t.actor(CAN,[{"x":550,"pose":"parado","cara":"neutral"},{"k":ksig,"x":550,"pose":"ofrece","cara":"feliz"}])
L.chip(kchat,"TWO LAWYERS FROM CHATTANOOGA","cian",fin=ktho); L.chip(ktho,"BENJAMIN THOMAS","amar",fin=kwhi); L.chip(kwhi,"JOSEPH WHITEHEAD","amar",fin=ksig)
L.inserto(ksig,kpri,"tableroH",{"titulo":"THE CONTRACT · 1899","filas":[["WHAT","BOTTLING"],["WHERE","MOST OF THE US"],["PRICE","$1"]]},mov="fijo")
L.titulo(kpri,"$1 · NEVER COLLECTED","amar",grande=True)

# ---------- 4 · LA RAZON REAL ----------
t=L.tramo("casona",capitulo="The real reason")
t.dice("So here is the real reason, and it has three parts.",
       "First, Candler truly believed that bottling would never be a big business, because the money was at the soda fountains.",
       "Second, he worried about quality, so the contract let him take the rights back if the bottlers ever sold a bad product.",
       "And third, the most important part: he kept the syrup.",
       "Every single bottle they filled needed Coca-Cola syrup, and the only place to buy it was from Candler.",
       "In his mind, he was not giving anything away. Someone else would do the hard work, and he would sell them the syrup.")
kthree=t.m("three",0,"^three"); k1=t.m("k1",1,"^never"); k2=t.m("k2",2,"^quality"); k3=t.m("k3",3,"^syrup"); kevery=t.m("every",4,"^every"); kmind=t.m("mind",5,"^mind")
t.actor(CAN,[{"x":550,"pose":"parado","cara":"neutral"},{"k":k1,"x":550,"pose":"explica","cara":"neutral"},{"k":k3,"x":550,"pose":"apunta","cara":"feliz"},{"k":kmind,"x":550,"pose":"cruzado","cara":"risa"}])
L.inserto(k1,k3,"tableroH",{"titulo":"WHY $1","filas":[["1","NO FUTURE"],["2","QUALITY"],["3","KEEPS SYRUP"]]},mov="fijo")
t.prop("botella1899",1150,1700,0.35,k=kevery); t.prop("botella1899",1300,1700,0.35,k=f"{kevery}+0.3"); t.prop("botella1899",1450,1700,0.35,k=f"{kevery}+0.6")
L.chip(kevery,"EVERY BOTTLE NEEDS HIS SYRUP","rosa",fin=kmind)
L.titulo(kmind,"OTHERS DO THE WORK","verde")

# ---------- 5 · LO QUE PASO ----------
t=L.tramo("despacho80",capitulo="The bottlers take over")
t.dice("Thomas, Whitehead, and a third partner, John Lupton, quickly realized they could not bottle a whole country by themselves.",
       "So they divided the United States into territories, and sold the bottling rights for each one to local business owners.",
       "Those local bottlers used their own money to build plants, buy trucks, and put Coca-Cola in stores far away from any soda fountain.",
       "Better bottling machines arrived, the bottles got cheaper and better, and bottled Coca-Cola took off.",
       "By 1920, the number of bottling plants had grown from the first two to nearly one thousand.")
klup=t.m("lup",0,"^lupton"); kterr=t.m("terr",1,"^territories"); kown=t.m("own",2,"^own"); kmac=t.m("mac",3,"^machines"); k1000=t.m("k1000",4,"^thousand")
t.actor(THO,[{"x":550,"pose":"parado","cara":"feliz"},{"k":kterr,"x":550,"pose":"apunta","cara":"feliz"}])
t.actor(dict(look="inventor",var=708,camisa="#455a64",s=0.95),[{"k":klup,"x":900,"pose":"saluda","cara":"feliz"}],desde=klup)
L.chip(klup,"JOHN LUPTON · THIRD PARTNER","cian",fin=kterr); L.chip(kterr,"THE US, SPLIT INTO TERRITORIES","amar",fin=kown)
L.chip(kown,"BOTTLERS PAY FOR EVERYTHING","verde",fin=kmac)
for j in range(5): t.prop("botella1899",1050+j*120,1700,0.32,k=f"{kmac}+{0.25*j:.2f}")
L.titulo(kmac,"BOTTLES TAKE OFF","verde",grande=True,fin=k1000)
L.numero(k1000,1000,"BOTTLING PLANTS BY 1920",pre="~",c="verde")

# ---------- 5b · LA BOTELLA ----------
t=L.tramo("cafe",capitulo="The bottle everyone copied")
t.dice("Success brought a new problem: copycats.",
       "Dozens of drinks with names that sounded like Coca-Cola were sold in plain bottles that looked just the same.",
       "So in 1915, the bottlers asked for a bottle so unique that you could recognize it by touch in the dark, or even broken on the ground.",
       "The winner was the curvy contour bottle, designed by a glass company in Terre Haute, Indiana, and it is still the shape on Coca-Cola today.")
kcopy=t.m("copy",0,"^copycats"); kplain=t.m("plain",1,"^plain"); kdark=t.m("dark",2,"^dark"); kcont=t.m("cont",3,"^contour")
L.titulo(kcopy,"COPYCATS","rojo",grande=True,fin=kplain)
for j in range(4): t.prop("botella1899",700+j*180,1700,0.32,k=f"{kplain}+{0.2*j:.1f}",fin=kcont)
L.chip(kdark,"1915 · RECOGNIZE IT IN THE DARK","amar",fin=kcont)
t.prop("botella1899",975,1700,0.51,k=kcont)
L.chip(kcont,"THE CONTOUR BOTTLE","verde")

# ---------- 6 · LA TRAMPA ----------
t=L.tramo("reunion",capitulo="The catch")
t.dice("But the contract had a catch that nobody saw coming.",
       "It was written to last forever, and it locked the price of the syrup that Coca-Cola sold to the bottlers.",
       "That fixed price is one of the reasons a Coca-Cola cost just 5 cents for about 70 years, all the way until 1959.",
       "Great for customers, but terrible for the company when costs went up and it could not charge the bottlers more.",
       "Starting in the 1920s, Coca-Cola began a long and very expensive process of buying back the bottling rights that Candler had sold for one dollar.")
kforev=t.m("forev",1,"^forever"); klock=t.m("lock",1,"^locked"); k70=t.m("k70",2,"^70"); kcost=t.m("cost",3,"^costs"); kback=t.m("back",4,"^buying")
L.titulo(t.key,"THE CATCH","rojo",grande=True,fin=kforev)
t.actor(EJE,[{"x":600,"pose":"parado","cara":"neutral"},{"k":kcost,"x":600,"pose":"piensa","cara":"triste"},{"k":kback,"x":600,"pose":"ofrece","cara":"neutral"}])
L.chip(kforev,"A CONTRACT FOREVER","rojo",fin=klock); L.chip(klock,"SYRUP PRICE · LOCKED","amar",fin=k70)
L.numero(k70,70,"YEARS AT 5¢",c="verde",fin=kcost)
L.chip(kback,"1920s · BUYING IT BACK","rosa")

t=L.tramo("reunion",luz="tenue",capitulo="The sugar war")
t.dice("The worst moment came right after Candler's family sold the company in 1919, to a group of investors led by Ernest Woodruff, for $25 million.",
       "After World War One, the price of sugar jumped, and sugar was the main ingredient in the syrup.",
       "The new owners tried to cancel the syrup price deal, and in 1920, the bottlers took them to court.",
       "The judge sided with the bottlers: the 1899 contract was perpetual, so the company could not pass the higher sugar price on to them.",
       "Then the sugar market collapsed, and Coca-Cola was left holding millions of dollars of overpriced sugar.",
       "In 1921, both sides finally agreed to raise the syrup price, but only slightly.")
k1919=t.m("k1919",0,"^woodruff"); k25=t.m("k25",0,"^25"); ksug=t.m("sug",1,"^sugar"); kcourt=t.m("court",2,"^court"); kjud=t.m("jud",3,"^perpetual"); kcol=t.m("col",4,"^collapsed"); k1921=t.m("k1921",5,"^slightly")
t.actor(EJE,[{"x":550,"pose":"parado","cara":"feliz"},{"k":kcourt,"x":550,"pose":"apunta","cara":"enojado"},{"k":kjud,"x":550,"pose":"cruzado","cara":"triste"},{"k":kcol,"x":550,"pose":"piensa","cara":"triste","fx":"tiembla"}])
t.actor(THO,[{"k":kcourt,"x":1350,"pose":"cruzado","cara":"enojado","dir":-1},{"k":kjud,"x":1350,"pose":"celebra","cara":"risa","dir":-1}],desde=kcourt)
L.numero(k25,25000000,"PAID FOR COCA-COLA · 1919",pre="$",c="amar",fin=ksug)
L.chip(ksug,"SUGAR PRICES JUMP","rojo",fin=kcourt); L.chip(kcourt,"1920 · BOTTLERS SUE","amar",fin=kjud)
t.prop("documento",975,1150,1.0,k=kjud,sello="PERPETUAL",selloc="rojo",cae=True,z=1800,fin=kcol)
L.chip(kcol,"STUCK WITH EXPENSIVE SUGAR","rojo",fin=k1921); L.chip(k1921,"1921 · A SMALL RAISE","cian")

t=L.tramo("despacho80",luz="tenue")
t.dice("And that buyback never really ended.",
       "In 2010, to take control of its biggest bottler in North America, Coca-Cola took on about $8 billion of that bottler's debt.",
       "That is what it can cost to undo a one-dollar deal.")
kend=t.m("end",0,"^ended"); k2010=t.m("k2010",1,"^2010"); k8=t.m("k8",1,"^8"); kundo=t.m("undo",2,"^undo"); kthat=t.m("that",2,"^that"); kdeal=t.m("deal",2,"^deal")
t.actor(EJE,[{"x":600,"pose":"parado","cara":"neutral"},{"k":k8,"x":600,"pose":"ofrece","cara":"sorpresa","fx":"tiembla"}])
L.numero(k8,8000000000,"DEBT TAKEN ON · 2010",pre="$",c="rojo",fin=kthat)
L.inserto(kthat,f"{kdeal}-0.5","balanzaH",{"izq":{"txt":"$1","sub":"1899","n":1},"der":{"txt":"$8B","sub":"2010 · ONE BOTTLER","n":15},"kder":kundo},mov="fijo")
L.sacudidas.append({"k":k8,"f":16})

# ---------- 7 · VEREDICTO ----------
t=L.tramo("casona",luz="tenue",capitulo="Mistake or genius")
t.dice("So, the final question is whether it was a mistake.",
       "In one way, yes: Candler gave away a business that turned out to be enormous, and his company paid for it for decades.",
       "But in another way, that one-dollar deal built the machine that took Coca-Cola everywhere.",
       "Local bottlers spent their own money and effort to put it in every town, and today Coca-Cola says its drinks are sold in more than 200 countries.",
       "Candler thought he was selling a small side business, and he was really selling the future of his own drink.")
kyes=t.m("yes",1,"^yes"); kmach=t.m("mach",2,"^machine"); k200=t.m("k200",3,"^200"); kfut=t.m("fut",4,"^future")
t.actor(CAN,[{"x":975,"pose":"parado","cara":"neutral"},{"k":kyes,"x":975,"pose":"piensa","cara":"triste"},{"k":kmach,"x":975,"pose":"apunta","cara":"feliz"},{"k":kfut,"x":975,"pose":"cruzado","cara":"neutral"}])
L.chip(kyes,"A MISTAKE: HE GAVE IT AWAY","rojo",fin=kmach); L.chip(kmach,"GENIUS: OTHERS BUILT IT","verde",fin=k200)
L.numero(k200,200,"COUNTRIES",pre="+",c="amar",fin=kfut)
L.titulo(kfut,"HE SOLD THE FUTURE","amar",grande=True)

t=L.tramo("despacho80")
t.dice("Tell me if you would have signed that contract.",
       "Follow for the next million dollar mistake.")
t.actor(CAN,[{"x":700,"pose":"parado","cara":"feliz"},{"k":t.m("tell",0,"^tell"),"x":700,"pose":"ofrece","cara":"feliz"}])
t.prop("documento",1300,1150,1.0,k=t.key,sello="$1",selloc="amar",cae=True,z=1800)

meta={"titulo":"Why Coca-Cola Sold Its Bottles for $1","texto_pantalla":"$1 · NEVER COLLECTED","lote":"L2026112302mdm","marca":"MILLION DOLLAR MISTAKE","tema":"",
"nota_datos":"Fuentes (23-nov): Wikipedia 'Fixed price of Coca-Cola 1886-1959' (contrato 1899 por $1 nunca cobrado; precio fijo; Candler creia que el embotellado no prenderia y podia quitar la franquicia si vendian producto inferior); Tennessee Encyclopedia (21-jul-1899, derechos exclusivos en casi todo EE. UU.; desde los 1920 la compania recompra las franquicias); History.com y Coca-Cola United (Biedenharn 1894 en Vicksburg mando una caja; sobrino de Candler; Candler siguio con las fuentes); The Coca-Cola Company (Thomas, Whitehead y Lupton; territorios y embotelladores locales); Business Insider/Butler (se quedo con el jarabe); SEC 10-Q/424B5 2010 (adquisicion del negocio norteamericano de CCE, ~US$8.000 M de deuda asumida); banco MDM #4 (Candler pago ~US$2.300 en 1888-1891).",
"fuentes":["https://en.wikipedia.org/wiki/Fixed_price_of_Coca-Cola_from_1886_to_1959","https://tennesseeencyclopedia.net/entries/coca-cola-bottling-company/","https://www.history.com/this-day-in-history/coca-cola-sold-in-glass-bottles-for-first-time","https://www.coca-colacompany.com/company/history/the-asa-candler-era","https://www.sec.gov/Archives/edgar/data/0000021344/000104746910009180/a2200783z424b5.htm"]}
g=L.armar(meta,cola=18.0,final={"marca":"MILLION DOLLAR MISTAKE","texto":"THANKS FOR WATCHING","a":"WATCH THIS NEXT","b":"SUBSCRIBE FOR MORE"})
g["cortes_no"]=["roto","claqueta","render","rollo","proyector","guion","edificio"]
json.dump(g,open("L2026112302mdm_src.json","w"),ensure_ascii=False)
w=sum(len(f.split()) for f in L.frases); print("frases",len(L.frases),"palabras",w,"tramos",len(L.tramos))
