import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b1979\b","nineteen seventy-nine"),(r"\b1982\b","nineteen eighty-two"),(r"\b1986\b","nineteen eighty-six"),(r"\b1989\b","nineteen eighty-nine"),
   (r"\b1991\b","nineteen ninety-one"),(r"\b1993\b","nineteen ninety-three"),(r"\b1995\b","nineteen ninety-five"),(r"\b1997\b","nineteen ninety-seven"),
   (r"\b2006\b","two thousand six"),(r"\b2026\b","twenty twenty-six"),(r"\b1980s\b","nineteen eighties"),
   (r"7\.4 billion","seven point four billion"),(r"135,000","one hundred thirty-five thousand"),(r"\b350 million","three hundred fifty million"),
   (r"\b30 million","thirty million"),(r"\b26 million","twenty-six million"),(r"\b50 million","fifty million"),(r"\b10 million","ten million"),(r"\b5 million","five million"),
   (r"\b80 percent","eighty percent"),(r"\b7 percent","seven percent"),(r"\b740\b","seven hundred forty"),(r"\b22 dollars","twenty-two dollars"),(r"\bat 39\b","at thirty-nine"),
   (r"\b1 billion","one billion"),(r"1\.5 billion","one point five billion"),(r"\b3 billion","three billion"),(r"4\.05 billion","four point oh five billion"),(r"\b2012\b","twenty twelve"),(r"\b2024\b","twenty twenty-four"),(r"\b1983\b","nineteen eighty-three"),(r"\b1985\b","nineteen eighty-five"),(r"November 19","November nineteenth"),(r"Inside Out 2","Inside Out two"),(r"NeXT","Next"),(r"RenderMan","Render Man"),(r"Lucasfilm","Lucas film"),(r"Catmull","Cat mull"),(r"Iger","Eye-ger"),(r"Toy Story 5","Toy Story five"),
   (r"Star Trek II","Star Trek Two"),(r"Terminator 2","Terminator Two"),(r"\bTV\b","T V")]
L=Largo(R); L.hints=[]
LUCAS=dict(look="ejecutivo",var=301,camisa="#6d4c41",pelo="#3e2723",barba="#3e2723",s=1.0)
CAT=dict(look="inventor",var=302,camisa="#455a64",pelo="#4e342e",barba="#4e342e",s=0.95)
JOBS=dict(look="ejecutivo",var=303,camisa="#212121",pelo="#3e2723",s=1.0)
LAS=dict(look="gamer",var=304,camisa="#e53935",pelo="#5d4037",s=1.0)
DIS=dict(look="ejecutivo",var=305,camisa="#37474f",pelo="#9e9e9e",s=1.0)
IGER=dict(look="ejecutivo",var=306,camisa="#1a237e",pelo="#cfd8dc",s=1.0)

# ---------- 0 · INTRO ----------
t=L.tramo("despacho80",capitulo="The $5 million sale")
t.dice("In 1986, George Lucas sold a small computer team for 5 million dollars.",
       "Twenty years later, that same team was sold again, for 7.4 billion.",
       "That team was Pixar.",
       "This is the full story of one of the biggest bargains in history.",
       "And of the man who needed to sell it.",
       "To understand how, we need four things: a secret lab, a divorce, a computer nobody wanted, and one giant bet.")
k4=t.m("k4",5,"^four")
k5=t.m("k5",0,"^5"); k74=t.m("k74",1,"^74"); kpx=t.m("px",2,"^pixar"); kman=t.m("man",4,None)
t.actor(LUCAS,[{"x":620,"pose":"ofrece","cara":"feliz","objeto":"documento"},{"k":k74,"x":620,"pose":"parado","cara":"sorpresa","fx":"tiembla"},{"k":kman,"x":620,"pose":"piensa","cara":"triste"}])
for j,dx in enumerate((1150,1330,1240)): t.prop("bolsa_dinero",dx,1690 if j<2 else 1580,1.2,k=f"{k74}+{0.2*j:.1f}",cae=True)

L.titulo(kpx,"PIXAR","amar",grande=True,fin=f"{kman}+1.5")
klab=t.m("lab",5,"^secret"); kdiv=t.m("div",5,"^divorce"); kcom=t.m("com",5,"^computer"); kbet=t.m("bet",5,"^giant")
L.inserto(k4,"b1","cuatroH",{"claves":[klab,kdiv,kcom,kbet]},mov="fijo")
L.sacudidas.append({"k":k74,"f":18})

# ---------- 1 · EL LABORATORIO ----------
t=L.tramo("lab80",capitulo="Lucas's secret lab")
t.dice("It starts in 1979.",
       "After Star Wars, George Lucas wanted to change the way movies were made.",
       "So he hired a group of computer experts, led by a scientist named Ed Catmull.",
       "Their job was to bring computers into filmmaking.")
kcat=t.m("cat",2,"^catmull"); kjob=t.m("job",3,None)
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":1,"titulo":"THE SECRET LAB","color":"cian"})
kaft=t.m("aft",1,"^after")
t.actor(LUCAS,[{"x":520,"pose":"parado","cara":"feliz"},{"k":kaft,"x":520,"pose":"piensa","cara":"neutral"},{"k":kcat,"x":520,"pose":"apunta","cara":"feliz"},{"k":kjob,"x":520,"pose":"cruzado","cara":"feliz"}])
L.hints.append({"k":kaft,"tipo":"primer","var":301,"push":1})
t.actor(CAT,[{"k":kcat,"x":1350,"pose":"saluda","cara":"feliz","dir":-1},{"k":kjob,"x":1350,"pose":"juega","cara":"feliz","dir":-1}],desde=kcat)

L.chip(kcat,"ED CATMULL · THE SCIENTIST","cian")

t=L.tramo("lab80")
t.dice("Back then, that sounded crazy.",
       "Computers were slow, huge, and very expensive.",
       "But this team was brilliant.",
       "One of their early wins was a computer effect for Star Trek II, in 1982.",
       "Later, they made the first fully computer-animated character in a movie: a knight made of stained glass, for Young Sherlock Holmes.")
kslow=t.m("slow",1,"^slow"); kbri=t.m("bri",2,"^brilliant"); kst=t.m("st",3,"^star"); kkn=t.m("kn",4,"^knight")
t.actor(CAT,[{"x":450,"pose":"piensa","cara":"neutral"},{"k":kbri,"x":450,"pose":"celebra","cara":"risa","fx":"salto"}])


t.prop("tv",1450,1300,1.3,k=kst,ir=True,contenido="genesis",fin=kkn); t.prop("documento",1450,1180,1.0,k=kkn,sello="KNIGHT",selloc="cian",cae=True,z=1800)
L.chip(kslow,"SLOW · HUGE · EXPENSIVE","rojo",fin=kbri); L.chip(kst,"STAR TREK II · 1982","amar",fin=kkn); L.chip(kkn,"FIRST CGI CHARACTER · 1985","cian")

t=L.tramo("animacion")
t.dice("In 1983, a young animator joined the team. His name was John Lasseter.",
       "He came from Disney. And Disney had fired him.",
       "His crime: he would not stop pushing for computer animation.",
       "Remember that. It comes back later.")
kla=t.m("la",0,"^lasseter"); kfir=t.m("fir",1,"^fired"); kcri=t.m("cri",2,"^crime"); krem=t.m("rem",3,"^remember")
t.actor(LAS,[{"x":300,"pose":"camina","cara":"neutral","a":[800,SUELO],"dur":2.0},{"k":kfir,"x":800,"pose":"sostiene","cara":"triste","objeto":"cajita"},{"k":kcri,"x":800,"pose":"apunta","cara":"enojado"},{"k":krem,"x":800,"pose":"cruzado","cara":"feliz"}])
t.actor(CAT,[{"k":krem,"x":1400,"pose":"saluda","cara":"feliz","dir":-1}],desde=kcri)
t.prop("documento",1150,1130,0.9,k=kfir,sello="FIRED",selloc="rojo",cae=True,z=1800,fin=krem)
L.chip(kla,"JOHN LASSETER · ANIMATOR","rojo",fin=kfir); L.chip(kcri,"TOO PRO-COMPUTER FOR DISNEY","amar",fin=krem); L.titulo(krem,"REMEMBER THIS","rosa")

t=L.tramo("cineH")
t.dice("And they had an even bigger dream.",
       "One day, they wanted to make a full movie, made entirely on a computer.",
       "Lucas liked the tools.",
       "But a computer-made movie was not his priority.")
kful=t.m("ful",1,"^full"); kliked=t.m("liked",2,"^liked"); kprio=t.m("prio",3,"^priority")
a1=t.actor(CAT,[{"x":700,"pose":"arriba","cara":"feliz"},{"k":kliked,"x":700,"pose":"parado","cara":"neutral"},{"k":kprio,"x":700,"pose":"piensa","cara":"triste"}])
t.actor(LUCAS,[{"k":kliked,"x":1300,"pose":"cruzado","cara":"feliz","dir":-1},{"k":kprio,"x":1300,"pose":"cruzado","cara":"neutral","dir":-1}],desde=kliked)
L.burbuja(f"{kful}+0.2",a1,"A FULL MOVIE!",fin=kliked,dx=60)
L.titulo(kful,"THE DREAM","rosa")

# ---------- 2 · EL DIVORCIO ----------
t=L.tramo("casona",capitulo="The divorce sale")
t.dice("Then, in the mid 1980s, everything changed.",
       "Lucas was going through a costly divorce.",
       "His company needed cash.",
       "The computer group was expensive, and it was not making money.",
       "So Lucas decided to sell it.")
kcash=t.m("cash",2,"^cash"); kexp=t.m("exp",3,None); ksell=t.m("sell",4,"^sell")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":2,"titulo":"THE DIVORCE SALE","color":"rosa"})
t.actor(LUCAS,[{"x":800,"pose":"piensa","cara":"triste"},{"k":kcash,"x":800,"pose":"sostiene","cara":"triste","objeto":"billetes"},{"k":ksell,"x":800,"pose":"apunta","cara":"neutral"}])

t.prop("grafico",1350,1250,1.0,k=kexp,z=1800)
t.prop("cartel",1350,1700,1.2,k=ksell,texto="FOR SALE",cae=True)
L.chip(kcash,"NEEDED CASH","rojo")

t=L.tramo("reunion")
t.dice("He asked for about 30 million dollars.",
       "But a deal with other big companies fell apart.",
       "Then a man showed up who had just been pushed out of his own company.",
       "His name was Steve Jobs. Apple had forced him out the year before.")
k30=t.m("k30",0,"^30"); kfell=t.m("fell",1,"^fell"); kjobs=t.m("jobs",3,"^jobs"); kap=t.m("apple",3,"^apple")
t.actor(LUCAS,[{"x":450,"pose":"ofrece","cara":"feliz","objeto":"documento"},{"k":kfell,"x":450,"pose":"piensa","cara":"triste"}])
t.prop("documento",1000,1150,0.9,k=kfell,sello="NO DEAL",selloc="rojo",cae=True,z=1800,fin=kjobs)
t.actor(JOBS,[{"k":f"{kfell}+1.2","x":1900,"pose":"camina","cara":"neutral","dir":-1,"a":[1350,SUELO],"dur":1.6},{"k":kjobs,"x":1350,"pose":"saluda","cara":"feliz","dir":-1}],desde=f"{kfell}+1.2")
L.numero(k30,30000000,"ASKING PRICE",pre="$",c="amar",fin=kfell)
L.chip(kap,"PUSHED OUT OF APPLE","cian")

t=L.tramo("despacho80")
t.dice("Jobs talked the price down to 10 million dollars.",
       "5 million went to Lucasfilm, for the technology.",
       "The other 5 million stayed inside, to keep the team running.",
       "In February 1986, the group became its own company.",
       "They called it Pixar.")
k10=t.m("k10",0,"^10"); kluc=t.m("luc",1,"^lucasfilm"); kins=t.m("ins",2,"^inside"); kfeb=t.m("feb",3,"^february"); kpix=t.m("pix",4,"^pixar")
t.actor(JOBS,[{"x":600,"pose":"apunta","cara":"feliz"},{"k":kins,"x":600,"pose":"ofrece","cara":"feliz","objeto":"cheque"},{"k":kpix,"x":600,"pose":"celebra","cara":"risa","fx":"salto"}])
t.actor(LUCAS,[{"x":1400,"pose":"cruzado","cara":"neutral","dir":-1},{"k":kluc,"x":1400,"pose":"sostiene","cara":"feliz","dir":-1,"objeto":"cheque"}],hasta=kfeb)
t.actor(CAT,[{"k":kfeb,"x":1400,"pose":"celebra","cara":"risa","dir":-1,"fx":"brinca"}],desde=kfeb)
L.numero(k10,10000000,"WHAT JOBS PAID",pre="$",c="verde",fin=kluc)
L.chip(kluc,"$5M → LUCASFILM","amar",fin=kins); L.chip(kins,"$5M → TO RUN PIXAR","verde",fin=kfeb)
L.titulo(kpix,"PIXAR · 1986","amar",grande=True)

# ---------- 3 · LA COMPUTADORA ----------
t=L.tramo("vitrina",capitulo="The $135,000 computer")
t.dice("Here is the twist.",
       "Jobs did not buy Pixar to make movies.",
       "He wanted to sell a powerful graphics machine, the Pixar Image Computer.",
       "It cost 135,000 dollars.",
       "And you needed another expensive computer just to run it.")
kmov=t.m("mov",1,"^movies"); kmach=t.m("mach",2,"^machine"); k135=t.m("k135",3,"^135"); kano=t.m("ano",4,"^another")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":3,"titulo":"THE $135,000|COMPUTER","color":"amar"})
t.actor(JOBS,[{"x":450,"pose":"piensa","cara":"neutral"},{"k":kmach,"x":450,"pose":"apunta","cara":"feliz"}])
t.prop("compu85",1010,1720,1.05,k=kmach,precio="$135,000")
t.prop("pc",1650,1720,1.1,k=kano,texto="+1 MORE",z=1700,cae=True)

L.chip(kmov,"NOT FOR MOVIES","rojo",fin=kmach)

t=L.tramo("medicoH")
t.dice("Hospitals and labs were curious.",
       "But only around a hundred were sold.",
       "Meanwhile, Jobs was busy building another computer company, called NeXT.",
       "Pixar kept losing money.",
       "And Jobs kept writing checks.")
khund=t.m("hund",1,"^hundred"); knx=t.m("nx",2,"^next"); klos=t.m("los",3,"^losing"); kchk=t.m("chk",4,"^checks")
t.actor(dict(look="cliente",var=310,s=0.95),[{"x":1350,"pose":"piensa","cara":"neutral","dir":-1},{"k":khund,"x":1350,"pose":"cruzado","cara":"neutral","dir":-1}])
t.actor(dict(look="vendedor",var=311,s=1.0),[{"x":650,"pose":"ofrece","cara":"feliz","objeto":"cajita"},{"k":khund,"x":650,"pose":"piensa","cara":"triste"}],hasta=kchk)
t.actor(JOBS,[{"k":kchk,"x":650,"pose":"ofrece","cara":"triste","objeto":"cheque"}],desde=kchk)
for j in range(3): t.prop("cheque",1000+j*160,1250-j*60,0.9,k=f"{kchk}+{0.25*j:.2f}",cae=True,texto="$$$",z=1800)
L.chip(khund,"ONLY ~100 SOLD","rojo",fin=knx); L.chip(knx,"ALSO RUNNING NeXT","cian",fin=klos)
L.chip(klos,"LOSING MONEY","rojo")

t=L.tramo("setTVH",capitulo="How Pixar survived")
t.dice("By 1991, he had put in around 50 million dollars of his own money.",
       "To survive, Pixar cut jobs and made TV commercials.",
       "It also sold its software, RenderMan, to other studios.",
       "RenderMan helped create the effects in movies like Terminator 2.")
k50=t.m("k50",0,"^50"); kcut=t.m("cut",1,"^cut"); kad=t.m("ad",1,"^commercials"); krm=t.m("rm",2,"^renderman"); kt2=t.m("t2",3,"^terminator")
t.actor(JOBS,[{"x":500,"pose":"piensa","cara":"triste","fx":"tiembla"},{"k":kad,"x":500,"pose":"apunta","cara":"neutral"}])
t.actor(CAT,[{"k":krm,"x":1450,"pose":"juega","cara":"feliz","dir":-1},{"k":kt2,"x":1450,"pose":"celebra","cara":"risa","dir":-1}],desde=krm)



L.chip(kcut,"JOB CUTS · TV ADS","amar",fin=krm); L.chip(kt2,"TERMINATOR 2 · 1991","cian")

# ---------- 4 · LOS CORTOS ----------
t=L.tramo("animacion",capitulo="The lamp and the Oscar")
t.dice("But one small team inside Pixar never gave up on the dream.",
       "It was led by John Lasseter, the animator Disney had fired.",
       "In 1986, he made a short film about two desk lamps.",
       "It became the first computer-animated film ever nominated for an Oscar.")
klas=t.m("las",1,"^lasseter"); klamp=t.m("lamp",2,"^lamps"); knom=t.m("nom",3,"^nominated")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":4,"titulo":"THE LAMP AND|THE OSCAR","color":"verde"})
t.actor(LAS,[{"x":700,"pose":"juega","cara":"feliz"},{"k":klas,"x":700,"pose":"saluda","cara":"risa"},{"k":klamp,"x":700,"pose":"juega","cara":"feliz"},{"k":knom,"x":700,"pose":"celebra","cara":"sorpresa","fx":"salto"}])

t.prop("linterna",1150,1150,1.0,k=klamp); t.prop("linterna",1350,1200,0.7,k=f"{klamp}+0.3")
L.chip(klas,"THE ANIMATOR DISNEY FIRED","rojo",fin=klamp); L.chip(knom,"FIRST CGI OSCAR NOMINATION","amar")

t=L.tramo("premiacionH")
t.dice("Two years later, his film Tin Toy went further.",
       "In 1989, it became the first computer-animated film to win an Oscar.",
       "It was proof that the dream could work.")
kwin=t.m("win",1,"^win"); kproof=t.m("proof",2,"^proof")
t.actor(LAS,[{"x":975,"pose":"parado","cara":"feliz"},{"k":kwin,"x":975,"pose":"arriba","cara":"risa","fx":"brinca"}])

L.chip(kwin,"FIRST CGI FILM TO WIN AN OSCAR","amar")
L.titulo(kproof,"PROOF","verde",grande=True)
L.sacudidas.append({"k":kwin,"f":14})

# ---------- 5 · LA APUESTA ----------
t=L.tramo("reunion",capitulo="The big bet")
t.dice("In 1991, Disney came knocking.",
       "Disney agreed to pay about 26 million dollars for Pixar to make three movies.",
       "But the deal favored Disney, which kept most of the profits.",
       "The first movie would be about toys that come to life.")
k26=t.m("k26",1,"^26"); kfav=t.m("fav",2,"^favored"); ktoy=t.m("toy",3,"^toys")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":5,"titulo":"THE BIG BET","color":"cian"})
t.actor(DIS,[{"x":1400,"pose":"saluda","cara":"feliz","dir":-1},{"k":k26,"x":1400,"pose":"ofrece","cara":"feliz","dir":-1,"objeto":"documento"}])
t.actor(JOBS,[{"x":550,"pose":"parado","cara":"neutral"},{"k":kfav,"x":550,"pose":"piensa","cara":"neutral"}])
t.prop("cajita",975,1700,1.3,k=ktoy,texto="TOYS",color="amar",cae=True)

L.chip(kfav,"DISNEY KEPT MOST OF THE PROFITS","rojo",fin=ktoy)

t=L.tramo("servidoresH")
t.dice("Nobody had ever made a full movie on computers.",
       "It took the team more than four years.",
       "The whole company was betting on this one film.")
kfour=t.m("four",1,"^four"); kbet=t.m("bet",2,"^betting"); khal=kbet
t.actor(LAS,[{"x":550,"pose":"juega","cara":"feliz"},{"k":khal,"x":550,"pose":"parado","cara":"sorpresa","fx":"tiembla"},{"k":kbet,"x":550,"pose":"juega","cara":"enojado"}])
t.actor(CAT,[{"x":1400,"pose":"juega","cara":"feliz","dir":-1},{"k":khal,"x":1400,"pose":"piensa","cara":"triste","dir":-1},{"k":kbet,"x":1400,"pose":"juega","cara":"enojado","dir":-1}])

L.chip(kfour,"4+ YEARS OF WORK","cian",fin=kbet); L.titulo(kbet,"ALL IN","rojo",grande=True)

t=L.tramo("reunion")
t.dice("On November 19, 1993, the team showed Disney the first half of the movie.",
       "Disney hated it. Even Tom Hanks, the voice of Woody, thought his character was a jerk.",
       "Disney stopped production.",
       "The Pixar team locked themselves away and rewrote the story.",
       "They made Woody kinder, and Disney let them keep going.")
kbf=t.m("bf",0,"^november"); khat=t.m("hat",1,"^hated"); kjerk=t.m("jerk",1,"^jerk"); kstop=t.m("stop",2,"^stopped"); kre=t.m("re",3,"^rewrote"); kkind=t.m("kind",4,"^kinder")
t.actor(LAS,[{"x":450,"pose":"ofrece","cara":"feliz","objeto":"documento"},{"k":khat,"x":450,"pose":"parado","cara":"sorpresa","fx":"tiembla"},{"k":kre,"x":450,"pose":"juega","cara":"enojado"},{"k":kkind,"x":450,"pose":"celebra","cara":"risa","fx":"salto"}])
t.actor(DIS,[{"x":1450,"pose":"parado","cara":"neutral","dir":-1},{"k":khat,"x":1450,"pose":"cruzado","cara":"enojado","dir":-1},{"k":kkind,"x":1450,"pose":"saluda","cara":"feliz","dir":-1}])
t.prop("documento",975,1120,0.9,k=kstop,sello="STOP",selloc="rojo",cae=True,z=1800,fin=kre)

L.titulo(kbf,"BLACK FRIDAY · 1993","rojo",fin=khat); L.chip(kjerk,"WOODY WAS A JERK","rojo",fin=kstop); L.chip(kstop,"PRODUCTION STOPPED","rojo",fin=kre); L.chip(kkind,"BACK ON","verde")
L.sacudidas.append({"k":kstop,"f":16})

t=L.tramo("cineH")
t.dice("In November 1995, Toy Story came out.",
       "It was the first feature film made entirely on computers.",
       "Tom Hanks and Tim Allen voiced Woody and Buzz.",
       "And it was a smash hit, earning more than 350 million dollars around the world.")
kts=t.m("ts",0,"^toy"); kfirst=t.m("first",1,"^first"); k350=t.m("k350",3,"^350")

t.actor(dict(look="cliente",var=320,s=0.95),[{"x":820,"y":1712,"pose":"sentado","cara":"feliz","z":1810},{"k":k350,"x":820,"y":1712,"pose":"sentado","cara":"risa","fx":"brinca","z":1810}])
t.actor(dict(look="jugadora",var=321,s=0.95),[{"x":1130,"y":1712,"pose":"sentado","cara":"sorpresa","z":1810},{"k":k350,"x":1130,"y":1712,"pose":"sentado","cara":"risa","fx":"brinca","z":1810}])
L.chip(kfirst,"FIRST FULL COMPUTER-ANIMATED FILM","verde",fin=k350)
L.numero(k350,350000000,"WORLDWIDE",pre="+$",c="verde")

t=L.tramo("premiacionH")
t.dice("It earned three Oscar nominations, including Best Original Screenplay, the first ever for an animated film.",
       "And John Lasseter received a special Oscar for leading the team.")
kosc=t.m("osc",0,"^three"); kscr=t.m("scr",0,"^screenplay"); kspec=t.m("spec",1,"^special")
t.actor(LAS,[{"x":975,"pose":"parado","cara":"feliz"},{"k":kspec,"x":975,"pose":"arriba","cara":"risa","fx":"brinca"}])

L.chip(kosc,"3 OSCAR NOMINATIONS","amar",fin=kspec); L.chip(kspec,"SPECIAL OSCAR FOR LASSETER","verde")

# ---------- 6 · LA SEMANA DEL BILLON ----------
t=L.tramo("bolsaH",capitulo="The billion-dollar week")
t.dice("Jobs saw his chance.",
       "One week after Toy Story opened, he took Pixar public on the stock market.",
       "It was risky, because Pixar had made only one movie.",
       "The shares were priced at 22 dollars.",
       "By the end of the first day, they were at 39.",
       "That day, the market valued Pixar at about 1.5 billion dollars.")
kpub=t.m("pub",1,"^public"); krisk=t.m("risk",2,"^risky"); k22=t.m("k22",3,"^22"); k39=t.m("k39",4,"^39")
L.chip(krisk,"ONLY ONE MOVIE","rojo",fin=k22)
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":6,"titulo":"THE BILLION-|DOLLAR WEEK","color":"verde"})
t.actor(JOBS,[{"x":500,"pose":"piensa","cara":"feliz"},{"k":kpub,"x":500,"pose":"apunta","cara":"feliz"},{"k":k39,"x":500,"pose":"celebra","cara":"risa","fx":"salto"}])

k15=t.m("k15",5,"^15")
L.numero(k22,22,"PRICE PER SHARE",pre="$",c="cian",fin=k39);

L.sacudidas.append({"k":k39,"f":16})

t=L.tramo("bolsaH")
t.dice("Jobs owned about 80 percent of the company.",
       "In one day, the man Apple had pushed out became a billionaire.",
       "Not because of Apple. Because of Pixar.")
k80=t.m("k80",0,"^80"); kbil=t.m("bil",1,"^billionaire"); knot=t.m("not",2,"^not")
t.actor(JOBS,[{"x":975,"y":1600,"pose":"sentado","cara":"feliz","z":1660},{"k":kbil,"x":975,"y":1600,"pose":"sentado","cara":"risa","fx":"brinca","z":1660}])
t.prop("trono",975,1640,1.1)
for j,dx in enumerate((600,1350,1450)): t.prop("bolsa_dinero",dx,1690,1.2,k=f"{kbil}+{0.2*j:.1f}",cae=True)
L.numero(k80,80,"OF PIXAR",suf="%",c="amar",fin=kbil)
L.titulo(kbil,"BILLIONAIRE","amar",grande=True,fin=knot); L.chip(knot,"THANKS TO PIXAR, NOT APPLE","verde")

# ---------- 7 · 7.400 MILLONES ----------
t=L.tramo("despacho80",capitulo="Disney pays $7.4 billion")
t.dice("Now Pixar had the power.",
       "In 1997, Jobs got a new deal with Disney. This time, they split the profits equally.",
       "That same year, Jobs went back to Apple, the company that had pushed him out.",
       "Hit after hit followed: Finding Nemo, The Incredibles, and more.")
ksplit=t.m("split",1,"^split"); kback=t.m("back",2,"^apple"); khit=t.m("hit",3,"^hit")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":7,"titulo":"$7.4 BILLION","color":"amar"})
t.actor(JOBS,[{"x":550,"pose":"cruzado","cara":"feliz"},{"k":ksplit,"x":550,"pose":"ofrece","cara":"feliz","objeto":"documento"}])
t.actor(DIS,[{"x":1400,"pose":"parado","cara":"neutral","dir":-1},{"k":ksplit,"x":1400,"pose":"saluda","cara":"feliz","dir":-1}])

for j in range(3): t.prop("cajita",800+j*180,1700,1.1,k=f"{khit}+{0.3*j:.1f}",cae=True,texto=["NEMO","HIT","HIT"][j],color=["cian","amar","rosa"][j])
L.chip(ksplit,"PROFITS SPLIT 50/50","verde",fin=kback); L.chip(kback,"JOBS RETURNS TO APPLE","cian",fin=khit)

t=L.tramo("restauranteH")
t.dice("But Jobs and Disney's boss, Michael Eisner, did not get along.",
       "Meanwhile, Disney's own animated films were struggling.",
       "For a while, it looked like Pixar might walk away from Disney.")
keis=t.m("eis",0,"^eisner"); kstr=t.m("str",1,"^struggling"); kwalk=t.m("walk",2,"^walk")
a2=t.actor(JOBS,[{"x":600,"pose":"cruzado","cara":"enojado"},{"k":kwalk,"x":600,"pose":"camina","cara":"enojado","dir":-1,"a":[250,SUELO],"dur":1.5}])
t.actor(DIS,[{"x":1350,"pose":"cruzado","cara":"enojado","dir":-1}])
L.burbuja(f"{keis}+0.5",a2,"NO DEAL.",fin=kwalk)
L.chip(keis,"JOBS VS. EISNER","rojo",fin=kstr); L.chip(kstr,"DISNEY ANIMATION STRUGGLING","amar",fin=kwalk)

t=L.tramo("reunion")
t.dice("Then Disney got a new boss, Bob Iger.",
       "Together, Disney and Pixar films had already earned more than 3 billion dollars.",
       "And in 2006, Disney bought Pixar for 7.4 billion dollars, paid in Disney stock.",
       "Jobs became Disney's largest single shareholder, with about 7 percent.",
       "Compared with the 10 million Jobs put in, that is 740 times more.",
       "And John Lasseter, the animator Disney had fired, became the creative boss of Disney animation.")
kig=t.m("ig",0,"^iger"); k3b=t.m("k3b",1,"^3"); kb74=t.m("b74",2,"^74"); ksh=t.m("sh",3,"^largest"); k740=t.m("k740",4,"^740")
L.numero(k3b,3000000000,"DISNEY + PIXAR FILMS",pre="+$",c="cian",fin=kb74)
t.actor(IGER,[{"x":1400,"pose":"saluda","cara":"feliz","dir":-1},{"k":kb74,"x":1400,"pose":"ofrece","cara":"feliz","dir":-1,"objeto":"cheque"}])
t.actor(JOBS,[{"k":kig,"x":550,"pose":"parado","cara":"neutral"},{"k":kb74,"x":550,"pose":"celebra","cara":"risa","fx":"salto"}])
for j,dx in enumerate((850,1000,925)): t.prop("bolsa_dinero",dx,1690 if j<2 else 1580,1.2,k=f"{kb74}+{0.2*j:.1f}",cae=True)
L.chip(kig,"NEW BOSS: BOB IGER","cian",fin=k3b)

L.chip(ksh,"DISNEY'S LARGEST SHAREHOLDER","amar",fin=k740)
klb=t.m("lb",5,"^lasseter")
L.titulo(k740,"740x","verde",grande=True,fin=klb); L.chip(klb,"FIRED → CREATIVE BOSS","amar")
t.actor(LAS,[{"k":klb,"x":975,"pose":"celebra","cara":"risa","fx":"salto"}],desde=klb)
t.prop("corona",975,1230,1.0,k=f"{klb}+0.4",cae=True,z=1850)
L.sacudidas.append({"k":kb74,"f":20})

# ---------- 8 · HOY ----------
t=L.tramo("cineH",capitulo="Pixar today")
t.dice("And Pixar never stopped.",
       "In 2026, Toy Story 5 passed 1 billion dollars at the box office.",
       "It became Pixar's sixth film to do it.",
       "And in 2024, Inside Out 2 broke the record for the highest-grossing animated film.",
       "All of that from a team once sold for 5 million dollars.")
kts5=t.m("ts5",1,"^1"); k6=t.m("k6",2,"^sixth"); kio=t.m("io",3,"^inside"); kall=t.m("all",4,"^sold")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":8,"titulo":"PIXAR TODAY","color":"rosa"})

t.actor(dict(look="jugador",var=330,s=0.95),[{"x":820,"y":1712,"pose":"sentado","cara":"feliz","z":1810},{"k":kts5,"x":820,"y":1712,"pose":"sentado","cara":"risa","fx":"brinca","z":1810}])
t.actor(dict(look="jugadora",var=331,s=0.95),[{"x":1130,"y":1712,"pose":"sentado","cara":"feliz","z":1810},{"k":kts5,"x":1130,"y":1712,"pose":"sentado","cara":"risa","fx":"brinca","z":1810}])
L.numero(kts5,1000000000,"TOY STORY 5 · 2026",pre="$",c="verde",fin=k6)
L.chip(k6,"PIXAR'S 6TH BILLION-DOLLAR FILM","amar",fin=kio); L.chip(kio,"ANIMATION RECORD · 2024","cian",fin=kall); L.chip(kall,"ONCE SOLD FOR $5 MILLION","rojo")

# ---------- 9 · EL GIRO FINAL ----------
t=L.tramo("casona",capitulo="The final twist")
t.dice("And here is the final twist.",
       "In 2012, George Lucas sold his whole company, Lucasfilm, with Star Wars inside, to Disney.",
       "The price was 4.05 billion dollars.",
       "That is less than what Disney paid for Pixar.",
       "The small group Lucas sold for 5 million ended up selling for more than Lucasfilm and Star Wars together.")
ktw=t.m("tw",0,"^twist"); kluc12=t.m("l12",1,"^lucasfilm"); k405=t.m("k405",2,"^405"); kless=t.m("less",3,"^less"); kmore=t.m("more",4,"^more")
L.titulo(ktw,"THE FINAL TWIST","rosa",grande=True,fin=kluc12)
t.actor(LUCAS,[{"k":kluc12,"x":550,"pose":"ofrece","cara":"feliz","objeto":"documento"},{"k":kless,"x":550,"pose":"piensa","cara":"sorpresa"}],desde=kluc12)
t.actor(IGER,[{"k":kluc12,"x":1400,"pose":"saluda","cara":"feliz","dir":-1}],desde=kluc12)

L.chip(kless,"LESS THAN PIXAR'S $7.4B","amar",fin=kmore)
L.titulo(kmore,"PIXAR > STAR WARS","verde",grande=True)
L.sacudidas.append({"k":kless,"f":14})

# ---------- 10 · LA LECCION ----------
t=L.tramo("museoH",capitulo="The lesson")
t.dice("To be fair, Lucas did not sell because he was foolish.",
       "He sold because he needed money, fast.",
       "And the deal let Lucasfilm keep using the technology.",
       "But the team, the dream, and the future went with Pixar.",
       "Even Jobs did not see the future clearly. He bought Pixar to sell computers, and the computers failed.",
       "What saved Pixar was the part nobody was paying for: the stories.")
kfast=t.m("fast",1,"^fast"); ktech=t.m("tech",2,"^technology"); kfut=t.m("fut",3,"^future")
L.inserto(t.key,t.key+"+2.4","capituloH",{"num":10,"titulo":"THE LESSON","color":"amar"})
t.actor(LUCAS,[{"x":700,"pose":"piensa","cara":"neutral"},{"k":kfast,"x":700,"pose":"sostiene","cara":"triste","objeto":"billetes"},{"k":kfut,"x":700,"pose":"piensa","cara":"triste"}])
t.prop("documento",1300,1130,0.9,k=ktech,sello="TECH RIGHTS",selloc="verde",cae=True,z=1800,fin=kfut)
t.actor(CAT,[{"k":kfut,"x":1500,"pose":"camina","cara":"feliz","dir":1,"a":[1900,SUELO],"dur":2.0}],desde=kfut)
L.chip(kfast,"NEEDED MONEY, FAST","rojo",fin=ktech)
kev=t.m("ev",4,"^even"); ksto=t.m("sto",5,"^stories")
L.chip(kfut,"THE FUTURE LEFT WITH PIXAR","cian",fin=kev); L.chip(kev,"JOBS'S COMPUTERS FAILED","rojo",fin=ksto); L.titulo(ksto,"THE STORIES","amar",grande=True)

t=L.tramo("museoH")
t.dice("So, in short.",
       "Lucas sold for 5 million because he needed cash.",
       "Jobs poured in 50 million to keep it alive.",
       "A fired animator made a lamp come to life.",
       "And Disney paid 7.4 billion to get it all.")
kr5=t.m("r5",1,"^5"); kr50=t.m("r50",2,"^50"); krl=t.m("rl",3,"^lamp"); kr74=t.m("r74",4,"^74")
L.titulo(t.key,"IN SHORT","cian",fin=kr5)
L.chip(kr5,"LUCAS: $5M FOR CASH","rojo",fin=kr50); L.chip(kr50,"JOBS: $50M TO SURVIVE","amar",fin=krl); L.chip(krl,"LASSETER: THE LAMP","cian",fin=kr74); L.chip(kr74,"DISNEY: $7.4B","verde")
t.actor(LUCAS,[{"x":450,"pose":"piensa","cara":"triste"}],hasta=kr50)
t.actor(JOBS,[{"k":kr50,"x":800,"pose":"ofrece","cara":"neutral","objeto":"cheque"}],desde=kr50,hasta=krl)
t.actor(LAS,[{"k":krl,"x":1150,"pose":"juega","cara":"feliz"}],desde=krl,hasta=kr74)
t.actor(IGER,[{"k":kr74,"x":1500,"pose":"celebra","cara":"risa","dir":-1,"fx":"salto"}],desde=kr74)
t.prop("linterna",1300,1150,0.9,k=krl,fin=kr74)

t=L.tramo("despacho80")
t.dice("Lesson: when you sell something to fix today's problem, ask what it could become in someone else's hands.",
       "Tell me if you would have sold.",
       "Follow for the next million dollar mistake.")
kles=t.m("les",0,None); kask=t.m("ask",0,"^ask"); ktell=t.m("tell",1,"^tell"); kfol=t.m("fol",2,"^follow")
t.actor(LUCAS,[{"x":700,"pose":"piensa","cara":"triste"}])

L.titulo(kles,"THE LESSON","rojo")
L.chip(kask,"ASK WHAT IT COULD BECOME","amar")


# ---------- INSERTOS (23-nov): planos de detalle sin personajes ----------
kagain=L.tramos[0].m("again",1,"^same")
L.inserto("b0",kagain,"chequeH",{"fecha":"FEBRUARY 1986","para":"LUCASFILM LTD.","monto":"5,000,000.00","letras":"Five million and 00/100","memo":"computer division","vel":0.75},mov="acerca")
L.inserto(kagain,kpx,"balanzaH",{"izq":{"txt":"$5M","sub":"1986 · WHAT IT SOLD FOR","n":1},"der":{"txt":"$7.4B","sub":"2006 · WHAT DISNEY PAID","n":15},"kder":k74},mov="aleja")
L.inserto(kslow,kbri,"vitrina",None,[{"tipo":"cronometro","x":975,"y":1640,"s":1.8,"texto":"SLOW..."}])
L.inserto(kluc,kfeb,"mesaCenital",{"titulo":"SALE AGREEMENT","monto":"$10,000,000","separa":kluc,"izq":"LUCASFILM","der":"PIXAR","fajos":6})
L.inserto(k50,kcut,"pilaH",{"monto":"$50,000,000","sub":"JOBS'S OWN MONEY","filas":[6,5,4,3,2,1]},mov="sube")
L.inserto(krm,kt2,"vitrina",None,[{"tipo":"disquete","x":975,"y":1250,"s":2.0,"etiqueta":"RENDERMAN"}])
L.inserto(k26,kfav,"mesaCenital",{"titulo":"3-PICTURE DEAL","monto":"$26,000,000","firma":k26,"fajos":3})
L.inserto(k39,k15,"vitrina",None,[{"tipo":"comparaBarras","x":975,"y":1730,"s":0.6,"v":[[22,"OPEN","#4fc3f7"],[39,"CLOSE · DAY 1","#69f0ae"]],"pre":"$","suf":"","dec":0,"k":k39}])
L.inserto(k15,"b19","diarioH",{"fecha":"NOVEMBER 30, 1995","titular":"PIXAR SOARS|IN STOCK DEBUT","bajada":"Shares jump from $22 to $39 on day one"},mov="fijo")
L.inserto(ksplit,kback,"mesaCenital",{"titulo":"NEW DEAL · 1997","monto":"50 / 50","separa":ksplit,"izq":"DISNEY","der":"PIXAR","fajos":6})
L.inserto(kb74,ksh,"tableroH",{"titulo":"DEAL · 2006","filas":[["SOLD TO","DISNEY"],["PAID IN","DISNEY STOCK"],["PRICE","$7,400,000,000"]]},mov="paneo")
L.inserto(kfour,kbet,"vitrina",None,[{"tipo":"cronometro","x":975,"y":1640,"s":1.8,"texto":"4+ YEARS"}])
L.inserto(kts,kfirst,"vitrina",None,[{"tipo":"calendarioP","x":975,"y":1180,"s":2.6,"mes":"NOVEMBER","dia":"22","anio":"1995"}])
L.inserto(k6,kio,"vitrina",None,[{"tipo":"trofeo","x":975,"y":1650,"s":2.2,"texto":"6TH $1B FILM"}])
L.inserto(kev,ksto,"vitrina",None,[{"tipo":"compu85","x":1010,"y":1720,"s":1.05,"precio":"FAILED"}])
# recuerdos a proposito (storytelling): vuelven el cheque del inicio y la balanza, solo en estos dos momentos
L.inserto(kall,f"{kall}+2.6","chequeH",{"k":"b0","fecha":"FEBRUARY 1986","para":"LUCASFILM LTD.","monto":"5,000,000.00","letras":"Five million and 00/100","memo":"computer division","vel":2.0},mov="acerca")
L.inserto(ktell,kfol,"balanzaH",{"izq":{"txt":"$5M","sub":"WHAT LUCAS GOT","n":1},"der":{"txt":"$7.4B","sub":"WHAT IT BECAME","n":15},"kder":ktell},mov="fijo")
L.inserto(k405,kless,"numeroH",{"texto":"$4.05B","estilo":"verde","sub":"ALL OF LUCASFILM · 2012"},mov="golpe")
L.inserto(kless,kmore,"balanzaH",{"izq":{"txt":"$4.05B","sub":"2012 · ALL OF LUCASFILM","n":9},"der":{"txt":"$7.4B","sub":"2006 · PIXAR ALONE","n":15}},mov="baja")
L.sfx+=[{"f":"extra/ESM_SPG_fx_action_transaction_cash_register_ding_02.wav","k":k74,"off":0.0,"dur":0.9,"g":0.12},
       {"f":"extra/ESM_SPG_fx_action_transaction_cash_register_ding_03.wav","k":kb74,"off":0.0,"dur":0.9,"g":0.12}]
meta={"titulo":"Pixar Was Sold for $5 Million: The Full Story","texto_pantalla":"$5M → $7.4B","lote":"L2026112301mdm","marca":"MILLION DOLLAR MISTAKE",
"nota_datos":"Fuentes: alvyray.com (Pixar spinout $10M: $5M a Lucasfilm por tecnologia, $5M operacion), Cord Cutters News, NYT 1986 (tech-insider), The Register/WSJ (Lucas pedia $30M), IEEE Spectrum (trato con GM/Philips no se dio), biography.com (Image Computer $135k, ~100 vendidas, $50M de Jobs hasta 1991, 1997 50/50), The History of Computing, Hollywood Reporter (RenderMan, T2), Wikipedia/Computer History/Guinness (Luxo Jr. primera nominacion CGI; Tin Toy primer Oscar CGI 1989), Time y No Film School (trato Disney 1991 $26M 3 peliculas; la empresa apostada), Cult of Mac (trato inclinado a Disney; IPO 29-nov-1995 $22 a $39; ~80%), Yahoo/CBR/Time (Black Friday 1993), Entrepreneur ($350M+), UPI/AOL/Fortune (multimillonario), NPR/CBS/NBC/Al Jazeera ($7.4B en acciones 2006, Jobs mayor accionista ~7%), Cartoon Brew y TheWrap (Toy Story 5 > $1B, sexta de Pixar).",
"fuentes":["https://www.alvyray.com/Pixar/PixarMyth1.htm","https://www.theregister.com/2011/10/06/steve_jobs_bio_1?page=6","https://www.biography.com/business-leaders/steve-jobs-pixar-animation-history","https://www.guinnessworldrecords.com/world-records/777092-first-computer-animated-film-to-win-an-academy-award","https://time.com/4118006/20-years-toy-story-pixar/","https://www.cultofmac.com/apple-history/pixar-ipo-makes-steve-jobs-billionaire","https://www.npr.org/transcripts/5171459","https://www.cartoonbrew.com/box-office-report/toy-story-5-billion-dollar-box-office-264930.html"]}
L.variar_transiciones()
g=L.armar(meta,cola=18.0,final={"marca":"MILLION DOLLAR MISTAKE","texto":"THANKS FOR WATCHING","a":"WATCH THIS NEXT","b":"SUBSCRIBE FOR MORE"})
g["escena"]["escenas"][0]["hud"]="doc"; g["escena"]["escenas"][0]["planos_hint"]=L.hints
json.dump(g,open("L2026112301mdm_src.json","w"),ensure_ascii=False)
w=sum(len(f.split()) for f in L.frases); print("frases",len(L.frases),"palabras",w,"tramos",len(L.tramos))
