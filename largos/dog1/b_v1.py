import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b2007\b","two thousand seven"),(r"\b2013\b","twenty thirteen"),(r"\b2015\b","twenty fifteen"),(r"\b2016\b","twenty sixteen"),(r"\b2018\b","twenty eighteen"),
   (r"\b2019\b","twenty nineteen"),(r"\b2021\b","twenty twenty-one"),(r"\b1990s\b","nineteen nineties"),(r"\b1872\b","eighteen seventy-two"),(r"\b40 dogs","forty dogs"),(r"\b25 dogs","twenty-five dogs"),(r"\b31 percent","thirty-one percent"),(r"\b57 percent","fifty-seven percent"),
   (r"\b43 percent","forty-three percent"),(r"\b2 percent","two percent"),(r"\b55 percent","fifty-five percent"),(r"\b962\b","nine hundred sixty-two"),
   (r"\b43 other","forty-three other"),(r"\b30 minutes","thirty minutes"),(r"FRAPs","fraps"),(r"\bUS\b","U S")]
L=Largo(R)
BIS=dict(pose="sentado",collar="rosa",color="#d9a35b",cola=5)
def biscuit(t,sx,k=None,fin=None,**o):
    d=dict(BIS); d.update(o); return t.prop("perro",sx,1700,1.15,k=k,fin=fin,**d)
DUE=dict(look="jugadora",var=501,s=1.0)

# 0 · intro
t=L.tramo("sala",capitulo="Your dog is talking")
t.dice("Your dog is talking to you all day.",
       "Not with words, but with its head, its eyes, its tail, and even where it sleeps.",
       "Scientists have studied many of these signals.",
       "Today, Biscuit and I will decode eight of them, one by one, with real studies behind each one.",
       "Each one comes with an honest note about what the study can and cannot tell us.",
       "Some of them might change the way you look at your dog.")
kwords=t.m("words",1,"^words"); ksci=t.m("sci",2,"^scientists"); kseven=t.m("seven",3,"^eight")
biscuit(t,1150); t.prop("sofa",975,1730,1.2)
t.actor(DUE,[{"x":700,"y":1712,"pose":"sentado","cara":"feliz","z":1810},{"k":kseven,"x":700,"y":1712,"pose":"sentado","cara":"risa","z":1810}])
L.titulo(t.key,"YOUR DOG IS TALKING","amar",fin=kwords); L.chip(kwords,"HEAD · EYES · TAIL · SLEEP","cian",fin=kseven)
L.titulo(kseven,"8 SIGNALS, DECODED","verde",grande=True)

# 1 · head tilt
t=L.tramo("estudio",capitulo="1. The head tilt")
t.dice("Signal number one: the head tilt.",
       "You say something, and your dog turns its head to one side.",
       "For years, almost nobody had studied it.",
       "Then, in 2021, researchers in Hungary noticed something while testing dogs that can learn the names of toys.",
       "Most dogs cannot even learn the names of two toys. But a few can learn many. The scientists called them gifted word learners.")
ktilt=t.m("tilt",1,"^turns"); knob=t.m("nob",2,"^nobody"); khun=t.m("hun",3,"^hungary"); kgift=t.m("gift",4,"^gifted")
L.titulo(t.key,"SIGNAL 1 · THE HEAD TILT","amar",grande=True,fin=ktilt)
biscuit(t,1150,fin=khun,estados=[{"k":ktilt,"inclina":0.35}])
t.actor(DUE,[{"x":600,"pose":"apunta","cara":"feliz"}],hasta=khun)
t.actor(dict(look="inventor",var=502,s=0.95),[{"k":khun,"x":550,"pose":"piensa","cara":"neutral"},{"k":kgift,"x":550,"pose":"apunta","cara":"sorpresa"}],desde=khun)
for j,c in enumerate(("rosa","cian","amar","verde")): t.prop("pelota",1050+j*150,1700,1.3,k=f"{kgift}+{0.2*j:.1f}",color={"rosa":"#ff4fa3","cian":"#2be8ff","amar":"#ffd23f","verde":"#5eff9f"}[c])
L.chip(knob,"BARELY STUDIED","rojo",fin=khun); L.chip(kgift,"\"GIFTED WORD LEARNERS\"","verde")

t=L.tramo("sala")
t.dice("When their owners said a toy's name, the gifted dogs tilted their heads 43 percent of the time.",
       "The other dogs did it just 2 percent of the time.",
       "The researchers think the tilt may happen when a dog is processing something meaningful, like a word it knows.",
       "So when Biscuit tilts her head at the word walk, she may be pulling up a memory.",
       "To be fair, it was a small study, just 40 dogs, so scientists say more research is needed.",
       "Try it yourself: say a word your dog knows well, like ball or walk, and watch the head.")
k43=t.m("k43",0,"^43"); k2=t.m("k2",1,"^2"); kmean=t.m("mean",2,"^meaningful"); kwalk=t.m("walk",3,"^walk"); ksmall=t.m("small",4,"^small"); ktry=t.m("try",5,"^try")
biscuit(t,1200,estados=[{"k":k43,"inclina":0.35},{"k":k2,"inclina":0.0},{"k":kwalk,"inclina":-0.35,"cola":9}])
t.actor(DUE,[{"x":650,"pose":"parado","cara":"feliz"},{"k":kwalk,"x":650,"pose":"apunta","cara":"risa"}])
L.numero(k43,43,"GIFTED DOGS · HEAD TILTS",suf="%",c="verde",fin=k2); L.numero(k2,2,"TYPICAL DOGS",suf="%",c="rojo",fin=kmean)
L.chip(kmean,"PROCESSING A WORD IT KNOWS","cian",fin=kwalk)
L.chip(ksmall,"SMALL STUDY · 40 DOGS","rojo",fin=ktry); L.chip(ktry,"TRY IT: \"BALL\" · \"WALK\"","verde")
L.burbuja(f"{kwalk}+0.3",None,"WALK?!",fin=ksmall,dx=0)
L.burbujas[-1].update({"x":t.X(1200),"y":1270}); L.burbujas[-1].pop("de")

# 2 · tail
t=L.tramo("calle",luz="tenue",capitulo="2. Which way the tail wags")
t.dice("Signal number two: the direction of the wag.",
       "A wagging tail does not always mean happy.",
       "In 2007, Italian scientists found that dogs tend to wag more to the right when they see something they like, such as their owner.",
       "And more to the left when they see something they want to back away from.")
knot=t.m("not",1,"^always"); kright=t.m("right",2,"^right"); kleft=t.m("left",3,"^left")
L.titulo(t.key,"SIGNAL 2 · THE TAIL","cian",grande=True,fin=knot)
biscuit(t,975,pose="parado",cola=7,estados=[{"k":kleft,"cola":2}])
t.actor(DUE,[{"k":kright,"x":1500,"pose":"saluda","cara":"feliz","dir":-1}],desde=kright,hasta=kleft)
t.prop("perro",1550,1700,1.0,k=kleft,pose="parado",color="#5d4037",color2="#8d6e63",oscuro="#3e2723",lejos="#4e342e",dir=-1,cola=1)
L.chip(knot,"NOT ALWAYS HAPPY","rojo",fin=kright); L.chip(kright,"MORE TO THE RIGHT → LIKES IT","verde",fin=kleft); L.chip(kleft,"MORE TO THE LEFT → BACK AWAY","rojo")

t=L.tramo("sala",luz="tenue")
t.dice("In 2013, the same team showed videos of wagging dogs to 43 other dogs.",
       "When the dog on screen wagged to the left, the watching dogs' heart rates went up, and they looked more anxious.",
       "When it wagged to the right, they stayed relaxed.",
       "The scientists say it may not be a deliberate message. It could simply come from which side of the brain is more active.",
       "And always read the tail together with the rest of the body, not on its own.")
k43b=t.m("k43b",0,"^43"); kanx=t.m("anx",1,"^anxious"); krel=t.m("rel",2,"^relaxed"); kbrain=t.m("brain",3,"^brain")
t.prop("tv",975,1260,1.25); t.prop("sofa",975,1730,1.2)
biscuit(t,975,estados=[{"k":kanx,"cola":0.5},{"k":krel,"cola":6}])
L.numero(k43b,43,"DOGS WATCHED THE VIDEOS",c="cian",fin=kanx)
L.chip(kanx,"LEFT WAG → HEART RATE UP","rojo",fin=krel); L.chip(krel,"RIGHT WAG → RELAXED","verde",fin=kbrain); kbody=t.m("body",4,"^body")
L.chip(kbrain,"LEFT BRAIN vs RIGHT BRAIN","amar",fin=kbody); L.chip(kbody,"READ THE WHOLE BODY","cian")

# 3 · puppy eyes
t=L.tramo("estudio",capitulo="3. Puppy eyes")
t.dice("Signal number three: puppy eyes.",
       "When your dog raises its inner eyebrows, its eyes look bigger, and a little sad.",
       "In 2019, scientists found that dogs have a small muscle that makes this move easy.",
       "It has a long name: the levator anguli oculi medialis.",
       "Wolves, their wild relatives, barely have it.",
       "Dogs also make this face more often, and more intensely, than wolves.")
kbrow=t.m("brow",1,"^eyebrows"); kmus=t.m("mus",2,"^muscle"); kname=t.m("name",3,"^levator"); kwolf=t.m("wolf",4,"^wolves"); kmore=t.m("more",5,"^often")
L.titulo(t.key,"SIGNAL 3 · PUPPY EYES","rosa",grande=True,fin=kbrow)
biscuit(t,800,mira=1)
t.prop("perro",1350,1700,1.15,k=kwolf,pose="sentado",color="#8d8d94",color2="#d6d6dc",oscuro="#55555e",lejos="#6e6e76",cola=0,dir=-1)
L.zoom.append({"k":kbrow,"s":1.35,"x":t.X(800),"y":1450,"dur":0.5}); L.zoom.append({"k":kmus,"s":1.0,"dur":0.5})
L.chip(kmus,"A SPECIAL EYEBROW MUSCLE","verde",fin=kname); L.chip(kname,"LEVATOR ANGULI OCULI MEDIALIS","cian",fin=kwolf); L.chip(kwolf,"WOLVES: BARELY","rojo",fin=kmore); L.chip(kmore,"DOGS: MORE OFTEN, MORE INTENSE","amar")

t=L.tramo("calle",luz="tenue")
t.dice("An earlier study found that shelter dogs that raised their eyebrows more were adopted faster.",
       "Scientists think that, over thousands of years, humans may have favored dogs with this look, without even realizing it.",
       "So yes, puppy eyes work on you. And that is not an accident.")
kshel=t.m("shel",0,"^adopted"); kfav=t.m("fav",1,"^favored"); kwork=t.m("work",2,"^work")
biscuit(t,1100)
t.actor(DUE,[{"x":600,"pose":"parado","cara":"neutral"},{"k":kshel,"x":600,"pose":"celebra","cara":"risa"},{"k":kwork,"x":600,"pose":"ofrece","cara":"risa","objeto":"pelota"}],os=0.9)
t.prop("cartel",1550,1700,1.1,texto="SHELTER")
L.chip(kshel,"ADOPTED FASTER","verde",fin=kfav); L.chip(kfav,"HUMANS PICKED THIS LOOK","amar",fin=kwork); L.titulo(kwork,"NOT AN ACCIDENT","rosa",grande=True)

# 4 · stare
t=L.tramo("sala",luz="tenue",capitulo="4. The long stare")
t.dice("Signal number four: the long, soft stare.",
       "In 2015, scientists in Japan measured a hormone called oxytocin, often linked to bonding, in dogs and their owners.",
       "After 30 minutes together, the pairs that looked at each other the longest had higher oxytocin, in both the dog and the human.",
       "Wolves raised by people did not show the same effect.",
       "A soft, relaxed stare at you is very different from a stiff stare at a stranger.")
kjap=t.m("jap",1,"^oxytocin"); k30=t.m("k30",2,"^30"); kboth=t.m("both",2,"^both"); kwol=t.m("wol",3,"^wolves"); ksoft=t.m("soft",4,"^soft")
L.titulo(t.key,"SIGNAL 4 · THE STARE","verde",grande=True,fin=kjap)
biscuit(t,1150,mira=-1)
t.actor(DUE,[{"x":700,"y":1712,"pose":"sentado","cara":"feliz","z":1810},{"k":kboth,"x":700,"y":1712,"pose":"sentado","cara":"risa","z":1810}])
t.prop("sofa",900,1730,1.2)
L.chip(kjap,"OXYTOCIN · THE BONDING HORMONE","rosa",fin=k30); L.numero(k30,30,"MINUTES TOGETHER",c="cian",fin=kboth)
L.chip(kboth,"IT ROSE IN BOTH","verde",fin=kwol); L.chip(kwol,"NOT IN WOLVES","rojo",fin=ksoft); L.chip(ksoft,"SOFT STARE = BONDING","amar")

# 5 · sleep
t=L.tramo("sala",luz="tenue",capitulo="5. Where your dog sleeps")
t.dice("Signal number five: where your dog sleeps.",
       "A 2018 survey of 962 women in the US found that 55 percent shared their bed with at least one dog.",
       "For comparison, 31 percent shared it with a cat, and 57 percent with a human partner.",
       "Dogs were rated as less disruptive in bed than human partners, and even less than cats.",
       "They were also linked with stronger feelings of comfort and security.",
       "One reason may be that a dog's sleep schedule is closer to ours than a cat's.",
       "Keep in mind, it was a survey, so it shows how people feel, not a lab measurement.")
k962=t.m("k962",1,"^962"); k55=t.m("k55",1,"^55"); kcomp=t.m("comp",2,"^31"); kless=t.m("less",3,"^disruptive"); ksec=t.m("sec",4,"^comfort"); ksch=t.m("sch",5,"^schedule"); ksurv=t.m("surv",6,"^survey")
L.titulo(t.key,"SIGNAL 5 · SLEEPING CLOSE","cian",grande=True,fin=k962)
t.prop("sofa",975,1730,1.4)
t.prop("perro",1150,1690,1.0,pose="echado",collar="rosa",color="#d9a35b",cola=1,z=1820)
t.actor(DUE,[{"x":800,"y":1712,"pose":"sentado","cara":"feliz","z":1810}])
L.numero(k962,962,"WOMEN SURVEYED",c="cian",fin=k55); L.numero(k55,55,"SHARE THE BED WITH A DOG",suf="%",c="verde",fin=kcomp); L.chip(kcomp,"CAT 31% · PARTNER 57%","amar",fin=kless)
L.chip(kless,"LESS DISRUPTIVE THAN PARTNERS","amar",fin=ksec); L.chip(ksec,"COMFORT · SECURITY","verde",fin=ksch); L.chip(ksch,"SIMILAR SLEEP SCHEDULE","cian",fin=ksurv); L.chip(ksurv,"A SURVEY, NOT A LAB TEST","rojo")

# 6 · zoomies
t=L.tramo("calle",capitulo="6. The zoomies")
t.dice("Signal number six: the zoomies.",
       "Suddenly, your dog runs in circles, like it is being chased by nothing.",
       "Experts call these frenetic random activity periods, or FRAPs.",
       "They often happen after a bath, after being let out, or when you come home.",
       "They are more common in puppies and young dogs, and they usually last just a few minutes.",
       "It is a normal way to release energy. Just keep your dog away from slippery floors and stairs.")
krun=t.m("run",1,"^runs"); kfr=t.m("fr",2,"^fraps"); kbath=t.m("bath",3,"^bath"); kpup=t.m("pup",4,"^puppies"); knorm=t.m("norm",5,"^normal")
L.titulo(t.key,"SIGNAL 6 · THE ZOOMIES","rojo",grande=True,fin=krun)
mv=[(krun,700,1700)]+[(f"{krun}+{0.5*i:.1f}",[1300,1500,1100,700,500,900,1300][i%7],[1700,1650,1600,1650,1700,1720,1700][i%7]) for i in range(1,18)]
t.prop("perro",700,1700,1.1,pose="parado",collar="rosa",color="#d9a35b",cola=12,k=t.key,mov=mv,estados=[{"k":knorm,"cola":4}])
L.chip(kfr,"FRAPs","cian",fin=kbath); L.chip(kbath,"AFTER A BATH · WHEN YOU COME HOME","amar",fin=kpup); L.chip(kpup,"PUPPIES · A FEW MINUTES","verde",fin=knorm)
L.chip(knorm,"NORMAL · AVOID SLIPPERY FLOORS","verde")

# 7 · play bow
t=L.tramo("calle",luz="tenue",capitulo="7. The play bow")
t.dice("Signal number seven: the play bow.",
       "Front legs down, back end up, tail wagging.",
       "Wolves and coyotes do it too. Even Charles Darwin described this posture, back in 1872.",
       "Animal behavior scientist Marc Bekoff studied it in the 1990s.",
       "He found the bow works like a message: whatever I do next, I am still just playing.",
       "A 2016 study found that play bows often come right after a short pause, like a reset button that starts the game again.")
kfront=t.m("front",1,"^front"); kdar=t.m("dar",2,"^darwin"); kbek=t.m("bek",3,"^bekoff"); kmsg=t.m("msg",4,"^message"); kres=t.m("res",5,"^reset")
L.chip(kdar,"WOLVES · COYOTES · DARWIN 1872","amar",fin=kbek)
L.titulo(t.key,"SIGNAL 7 · THE PLAY BOW","verde",grande=True,fin=kfront)
t.prop("perro",800,1700,1.15,pose="echado",collar="rosa",color="#d9a35b",cola=9,estados=[{"k":kres,"pose":"parado"}])
t.prop("perro",1300,1700,1.0,pose="parado",color="#5d4037",color2="#8d6e63",oscuro="#3e2723",lejos="#4e342e",dir=-1,cola=8,collar=None)
L.chip(kbek,"MARC BEKOFF · 1990s","cian",fin=kmsg); L.chip(kmsg,"\"I'M STILL JUST PLAYING\"","verde",fin=kres); L.chip(kres,"A RESET BUTTON FOR PLAY","amar")

# 8 · yawn
t=L.tramo("sala",luz="tenue",capitulo="8. The yawn")
t.dice("And a bonus, signal number eight: the yawn.",
       "You yawn, and a moment later, your dog yawns too.",
       "In 2013, researchers in Tokyo had 25 dogs watch their owners and strangers yawn.",
       "The dogs yawned more when their owner yawned than when a stranger did.",
       "They yawned less at fake yawns, and their heart rates did not suggest stress.",
       "The researchers think contagious yawning in dogs may be linked to an emotional connection.",
       "But dogs can also yawn when they feel tense, so look at the situation, too.")
ky=t.m("y",1,"^yawn"); k25=t.m("k25",2,"^25"); kown=t.m("own",3,"^owner"); kfake=t.m("fake",4,"^fake"); kemo=t.m("emo",5,"^emotional"); ktense=t.m("tense",6,"^tense")
L.titulo(t.key,"SIGNAL 8 · THE YAWN","rosa",grande=True,fin=ky)
t.prop("sofa",975,1730,1.2)
t.actor(DUE,[{"x":800,"y":1712,"pose":"sentado","cara":"neutral","z":1810},{"k":ky,"x":800,"y":1712,"pose":"sentado","cara":"sorpresa","z":1810}])
biscuit(t,1200,estados=[{"k":f"{ky}+0.8","lengua":1},{"k":k25,"lengua":0}])
L.numero(k25,25,"DOGS IN THE STUDY",c="cian",fin=kown); L.chip(kown,"MORE YAWNS FOR THE OWNER","verde",fin=kfake)
L.chip(kfake,"FEWER FOR FAKE YAWNS · NO STRESS SIGNS","amar",fin=kemo); L.chip(kemo,"AN EMOTIONAL LINK?","rosa",fin=ktense); L.chip(ktense,"ALSO A SIGN OF TENSION","rojo")

# recap
t=L.tramo("sala",capitulo="Recap")
t.dice("So, let's recap.",
       "The head tilt: your dog may be processing a word it knows.",
       "The tail: right often means I like this. Left, I'm not so sure.",
       "Puppy eyes: a face humans may have shaped over thousands of years.",
       "The soft stare: a bonding moment for both of you.",
       "Sleeping close: comfort and security.",
       "The zoomies: pure energy release.",
       "The play bow: I'm still just playing.",
       "And the yawn: maybe, a little bit of connection.",
       "Your dog is not just cute. It is talking to you all the time.",
       "And the more of these signals you learn to read, the better you can answer back.")
r=[t.m(f"r{i}",i,None) for i in range(1,9)]; kfin=t.m("fin8",9,"^talking")
L.titulo(t.key,"RECAP","amar",fin=r[0])
for i,(txt,c) in enumerate([("1 · HEAD TILT","amar"),("2 · TAIL DIRECTION","cian"),("3 · PUPPY EYES","rosa"),("4 · SOFT STARE","verde"),("5 · SLEEPING CLOSE","cian"),("6 · ZOOMIES","rojo"),("7 · PLAY BOW","verde"),("8 · THE YAWN","rosa")]):
    L.chip(r[i],txt,c,fin=r[i+1] if i<7 else kfin)
biscuit(t,1150,estados=[{"k":r[0],"inclina":0.35},{"k":r[1],"inclina":0,"cola":9},{"k":r[6],"pose":"parado","cola":10}])
t.actor(DUE,[{"x":650,"pose":"parado","cara":"feliz"},{"k":kfin,"x":650,"pose":"celebra","cara":"risa"}])
L.titulo(kfin,"YOUR DOG IS TALKING","amar",grande=True)

t=L.tramo("sala",luz="tenue")
t.dice("Comment which signal your dog uses the most.",
       "Follow to decode your dog.")
biscuit(t,975,cola=8)

L.sfx=[]
meta={"titulo":"Everything Your Dog Is Telling You (Science Explained)","texto_pantalla":"8 SIGNALS, DECODED","lote":"L2026112301dog","marca":"THE DOGS DECODER",
"nota_datos":"1) Sommese et al. 2021, Animal Cognition (ELTE, Hungria): 40 perros (7 'gifted word learners' + 33 tipicos); ladeo de cabeza 43% vs 2% al oir nombres de juguetes; hipotesis: procesar estimulos con significado. Fuentes: Discover, Scientific American, Smithsonian, PMC, Business Insider. 2) Quaranta, Siniscalchi, Vallortigara 2007 (Curr Biol): cola a la derecha ante el dueno, izquierda ante algo de lo que retirarse; Siniscalchi et al. 2013 (Curr Biol): 43 perros, cola izquierda -> mas frecuencia cardiaca y ansiedad; puede no ser mensaje intencional. Fuentes: NatGeo, NPR, PubMed, Phys.org, CSMonitor. 3) Kaminski et al. 2019 PNAS (musculo LAOM; lobos casi no lo tienen; perros lo usan mas); estudio 2013: perros de refugio que suben mas la ceja adoptados antes. Fuentes: PubMed, NatGeo, PBS. 4) Nagasawa et al. 2015 Science: oxitocina sube en perro y dueno con mas mirada; no en lobos criados por humanos. Fuentes: NatGeo, SciAm. 5) Hoffman et al. 2018 Anthrozoos (Canisius): 962 mujeres, 55% duerme con perro; menos disruptivos que parejas y gatos; encuesta. Fuentes: Canisius, CBS, AJC. 8) Romero, Konno, Hasegawa 2013 PLOS ONE (U. Tokio): 25 perros bostezan mas con el dueno que con extranos, menos con bostezos falsos, sin cambios de ritmo cardiaco; bostezo tambien puede ser ansiedad (NatGeo). Fuentes: NatGeo, Phys.org, ScienceDaily, U. Tokio. 6) FRAPs: Cornell Riney Canine Health Center, Discover. 7) Bekoff 1995 (play bow = 'sigo jugando'); Byosiere, Espinosa, Smuts 2016 (despues de pausas). Fuentes: SciAm blog, estudio 2016, Cogprints.",
"fuentes":["https://pmc.ncbi.nlm.nih.gov/articles/PMC9107419","https://www.scientificamerican.com/article/why-do-dogs-tilt-their-heads-to-the-side","https://pubmed.ncbi.nlm.nih.gov/24184108/","https://www.nationalgeographic.com/animals/article/left-or-right-tail-wags-elicit-different-emotional-responses-from-dogs","https://pubmed.ncbi.nlm.nih.gov/31209036/","https://canisius.edu/node/1733","https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/health-info/what-are-zoomies","https://web-archive.southampton.ac.uk/cogprints.org/158/1/199709003.html"]}
g=L.armar(meta,cola=18.0,final={"marca":"THE DOGS DECODER","texto":"FOLLOW TO DECODE YOUR DOG","a":"WATCH THIS NEXT","b":"SUBSCRIBE FOR MORE"})
json.dump(g,open("L2026112301dog_src.json","w"),ensure_ascii=False)
w=sum(len(f.split()) for f in L.frases); print("frases",len(L.frases),"palabras",w,"tramos",len(L.tramos))
