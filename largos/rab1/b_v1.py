import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b2004\b","two thousand four"),(r"\b2007\b","two thousand seven"),(r"\b2015\b","twenty fifteen"),(r"\b2017\b","twenty seventeen"),(r"\b2018\b","twenty eighteen"),
   (r"\b2019\b","twenty nineteen"),(r"\b2020\b","twenty twenty"),(r"\b2021\b","twenty twenty-one"),(r"\b2023\b","twenty twenty-three"),(r"\b2025\b","twenty twenty-five"),(r"\b2022\b","twenty twenty-two"),(r"\b2012\b","twenty twelve"),(r"\b18\b","eighteen"),
   (r"November 14","November fourteenth"),(r"December 16","December sixteenth"),(r"April 27","April twenty-seventh"),
   (r"\b100 miles","one hundred miles"),(r"\b40 feet","forty feet"),(r"\b13,000 feet","thirteen thousand feet"),(r"\b40 miles","forty miles"),(r"\b435 miles","four hundred thirty-five miles"),
   (r"\b144\b","one hundred forty-four"),(r"\b143\b","one hundred forty-three"),(r"\b80,000 feet","eighty thousand feet"),
   (r"FLIR","fleer"),(r"GOFAST","Go Fast"),(r"GIMBAL","Gimbal"),(r"AARO","A R O"),(r"UAP","U A P"),(r"UFO","U F O"),(r"NASA","NASA"),(r"Blink-182","Blink one eighty-two"),(r"DeLonge","De Long")]
L=Largo(R)
PIL=dict(look="oficial",var=401,camisa="#556b2f",s=1.0)
PIL2=dict(look="oficial",var=402,camisa="#4b5320",s=1.0)
RAD=dict(look="gamer",var=403,camisa="#37474f",s=0.95)
PEN=dict(look="ejecutivo",var=404,camisa="#263238",pelo="#9e9e9e",s=1.0)
PER=dict(look="jugadora",var=405,s=0.95)
ESC=dict(look="sabio",var=406,s=0.95)

# 0 · intro
t=L.tramo("cielo",capitulo="Three videos")
t.dice("On April 27, 2020, the Pentagon officially released three videos.",
       "They showed objects that Navy pilots could not identify.",
       "Their names were FLIR, GIMBAL, and GOFAST.",
       "For years, people said these videos proved that something unknown was flying over the ocean.",
       "Pilots described things that moved in ways no aircraft they knew could move.",
       "Our rule here is simple: a case is only closed when the evidence closes it.",
       "Today, we open the complete file: what each video shows, what investigators found, and which case is still open.")
kvid=t.m("vid",0,"^videos"); knames=t.m("names",2,"^names"); kfile=t.m("file",6,"^complete")
t.prop("ovni",975,950,1.0,k=kvid)
t.prop("tv",450,1300,1.0,k=knames,ir=True); t.prop("tv",975,1300,1.0,k=f"{knames}+0.4",ir=True); t.prop("tv",1500,1300,1.0,k=f"{knames}+0.8",ir=True)
L.titulo(kvid,"3 NAVY VIDEOS","cian",fin=knames); L.chip(knames,"FLIR · GIMBAL · GOFAST","amar",fin=kfile)
L.titulo(kfile,"THE COMPLETE FILE","rosa",grande=True)

# 1 · Nimitz 2004
t=L.tramo("cabina",capitulo="2004: the Tic Tac")
t.dice("It starts on November 14, 2004, about 100 miles off the coast of Southern California.",
       "A Navy cruiser, the USS Princeton, had been tracking strange radar contacts.",
       "According to the radar operators, some contacts seemed to drop from very high altitudes, around 80,000 feet.",
       "Two fighter jets were sent to check one out.",
       "One was flown by Commander David Fravor, a veteran Navy pilot.",
       "The other was flown by Lieutenant Alex Dietrich.")
kpr=t.m("pr",1,"^princeton"); k80=t.m("k80",2,"^80000"); kjets=t.m("jets",3,"^jets"); kfr=t.m("fr",4,"^fravor"); kdi=t.m("di",5,"^dietrich")
L.numero(k80,80000,"FEET · RADAR CONTACTS",c="rojo",fin=kjets)
L.titulo(t.key,"CASE 1 · NOVEMBER 2004","cian")
t.actor(RAD,[{"x":600,"pose":"juega","cara":"neutral"},{"k":kpr,"x":600,"pose":"apunta","cara":"sorpresa"}])
t.prop("radar",1150,1350,1.3,k=kpr)
t.actor(PIL,[{"k":kfr,"x":1550,"pose":"saluda","cara":"feliz","dir":-1}],desde=kfr)
L.chip(kpr,"USS PRINCETON · RADAR","verde",fin=k80); L.chip(kfr,"CMDR. DAVID FRAVOR","amar",fin=kdi); L.chip(kdi,"LT. ALEX DIETRICH","cian")
t.actor(dict(look="jugadora",var=408,camisa="#556b2f",s=0.95),[{"k":kdi,"x":1250,"pose":"saluda","cara":"feliz","dir":-1}],desde=kdi)

t=L.tramo("cielo")
t.dice("When they arrived, they saw a disturbance in the water.",
       "Above it, there was a white object, about 40 feet long, shaped like a Tic Tac candy.",
       "It had no wings, and no visible engines.",
       "One of the pilots later said it accelerated like nothing he had ever seen.",
       "Then it was gone.")
kwat=t.m("wat",0,"^water"); ktic=t.m("tic",1,"^tic"); kwing=t.m("wing",2,"^wings"); kacc=t.m("acc",3,"^accelerated"); kgone=t.m("gone",4,"^gone")
t.prop("jet",500,950,1.4,k=t.key); t.prop("jet",700,1080,1.2,k=t.key)
t.prop("orbe",1250,1250,1.4,k=ktic,fin=kgone,mov=[(ktic,1250,1250),(kacc,1250,1250),(f"{kacc}+0.8",2300,700)])
t.prop("viento",1250,1600,1.2,k=kwat,fin=kgone)
L.chip(ktic,"~40 FT · WHITE · NO WINGS","amar",fin=kacc); L.titulo(kgone,"GONE","rojo",grande=True)
L.sacudidas.append({"k":kacc,"f":16})

t=L.tramo("cabina")
t.dice("Later that day, another pilot, Chad Underwood, flew out with an infrared camera.",
       "An infrared camera does not see light. It sees heat.",
       "He recorded a short video of a small object on his screen.",
       "He was the one who first called it the Tic Tac.",
       "That video became known as FLIR.",
       "A copy leaked online in 2007, but for years, almost nobody paid attention.")
kund=t.m("und",0,"^underwood"); kheat=t.m("heat",1,"^heat"); krec=t.m("rec",2,"^recorded"); kcall=t.m("call",3,"^tic"); kflir=t.m("flir",4,"^flir"); kleak=t.m("leak",5,"^leaked")
L.chip(kheat,"INFRARED = HEAT","rojo",fin=krec)
t.actor(PIL2,[{"x":550,"pose":"juega","cara":"neutral"},{"k":kcall,"x":550,"pose":"apunta","cara":"risa"}])
t.prop("tv",1200,1300,1.4,k=krec,ir=True)
L.chip(kund,"LT. CHAD UNDERWOOD","verde",fin=krec); L.chip(kcall,"HE NAMED IT \"TIC TAC\"","amar",fin=kflir)
L.titulo(kflir,"VIDEO 1 · FLIR","cian"); L.chip(kleak,"LEAKED IN 2007","rojo")

# 2 · 2015 Atlantic
t=L.tramo("cielo",capitulo="2015: GIMBAL and GOFAST")
t.dice("Eleven years later, in January 2015, it happened again.",
       "This time, over the Atlantic Ocean, off the coast of Florida.",
       "Pilots from the aircraft carrier USS Theodore Roosevelt recorded two more videos.",
       "In one, an object seems to rotate in the sky. That one is GIMBAL.",
       "In the other, a small object seems to race above the waves. That one is GOFAST.")
kat=t.m("at",1,"^atlantic"); kroo=t.m("roo",2,"^roosevelt"); kgim=t.m("gim",3,"^gimbal"); kgf=t.m("gf",4,"^gofast")
L.titulo(t.key,"CASE 2 · JANUARY 2015","cian",fin=kroo)
t.prop("jet",450,1000,1.3,k=kroo)
t.prop("tv",850,1300,1.2,k=kgim,ir=True); t.prop("tv",1450,1300,1.2,k=kgf,ir=True)
L.chip(kat,"ATLANTIC · OFF FLORIDA","verde",fin=kgim); L.chip(kgim,"VIDEO 2 · GIMBAL","amar",fin=kgf); L.chip(kgf,"VIDEO 3 · GOFAST","rosa")

# 3 · 2017
t=L.tramo("sala",luz="tenue",capitulo="2017: the world finds out")
t.dice("Then, on December 16, 2017, The New York Times published a story that went around the world.",
       "It revealed that the Pentagon had run a program to study UFO reports.",
       "It was called the Advanced Aerospace Threat Identification Program, and it ran until 2012.",
       "And it came with two of the videos: FLIR and GIMBAL.",
       "They were released by a group co-founded by Tom DeLonge, the guitarist of Blink-182.",
       "A few months later, GOFAST came out too.")
knyt=t.m("nyt",0,"^york"); kprog=t.m("prog",1,"^program"); kaatip=t.m("aatip",2,"^advanced"); ktwo=t.m("two",3,"^two"); kdel=t.m("del",4,"^delonge"); kgf2=t.m("gf2",5,"^gofast")
L.titulo(t.key,"DECEMBER 2017","rosa",fin=kprog)
t.prop("sofa",975,1730,1.2); t.prop("tv",975,1260,1.2,ir=True,k=ktwo)
t.actor(PER,[{"x":820,"y":1712,"pose":"sentado","cara":"neutral","z":1810},{"k":ktwo,"x":820,"y":1712,"pose":"sentado","cara":"sorpresa","fx":"tiembla","z":1810}])
t.actor(dict(look="cliente",var=407,s=0.95),[{"x":1130,"y":1712,"pose":"sentado","cara":"neutral","z":1810},{"k":ktwo,"x":1130,"y":1712,"pose":"sentado","cara":"sorpresa","z":1810}])
t.prop("documento",1600,1150,0.9,k=kprog,sello="UFO PROGRAM",selloc="rojo",cae=True,z=1800,fin=kdel)
L.chip(kprog,"A SECRET PENTAGON UFO PROGRAM","rojo",fin=kaatip); L.chip(kaatip,"AATIP · UNTIL 2012","amar",fin=ktwo); L.chip(kdel,"RELEASED BY TOM DeLONGE'S GROUP","cian",fin=kgf2); L.chip(kgf2,"GOFAST: 2018","amar")

# 4 · oficial
t=L.tramo("oficina",capitulo="The Pentagon confirms")
t.dice("In 2019, the Navy confirmed the videos were real.",
       "It also said it could not identify the objects.",
       "The Navy even wrote new rules so pilots could report these sightings.",
       "Then, on April 27, 2020, the Pentagon released all three videos officially.",
       "It said it wanted to clear up any confusion about whether the footage was real.",
       "And its statement said the objects remain characterized as unidentified.")
kreal=t.m("real",0,"^real"); kid=t.m("id",1,"^identify"); krul=t.m("rul",2,"^rules"); krel=t.m("rel",3,"^released"); kuni=t.m("uni",5,"^unidentified")
t.actor(PEN,[{"x":550,"pose":"parado","cara":"neutral"},{"k":krel,"x":550,"pose":"ofrece","cara":"neutral","objeto":"documento"},{"k":kuni,"x":550,"pose":"cruzado","cara":"neutral"}],os=1.0)
t.prop("documento",1250,1130,0.9,k=kreal,sello="REAL",selloc="verde",cae=True,z=1800,fin=krul)
t.prop("documento",1250,1130,0.9,k=krul,sello="NEW RULES",selloc="amar",cae=True,z=1800,fin=krel)
t.prop("tv",1300,1300,1.1,k=krel,ir=True)
L.chip(kreal,"NAVY: THE VIDEOS ARE REAL","verde",fin=krul); L.chip(krul,"NEW REPORTING RULES","amar",fin=krel)
L.titulo(kuni,"\"UNIDENTIFIED\"","rojo",grande=True)

# 5 · GOFAST resuelto
t=L.tramo("cielo",capitulo="GOFAST: case closed")
t.dice("Now, let's open each case, one by one.",
       "First, GOFAST.",
       "The video makes the object look like it is skimming the ocean at high speed.",
       "But the screen also shows numbers: the camera angle, the distance, and the jet's altitude.",
       "In 2023, a NASA study team did the math.",
       "Their conclusion: the video gives an impression of great speed, but the numbers tell a much less extraordinary story.")
kfirst=t.m("first",1,"^first"); kskim=t.m("skim",2,"^skimming"); knum=t.m("num",3,"^numbers"); knasa=t.m("nasa",4,"^nasa")
L.titulo(kfirst,"FILE 1 · GOFAST","rosa",grande=True,fin=kskim)
t.prop("jet",500,1000,1.3)
t.prop("orbe",1300,1550,0.8,k=kskim,mov=[(kskim,1300,1580),(f"{kskim}+2.0",1700,1580)],fin=knasa)
t.prop("tv",1300,1250,1.2,k=knum,ir=True)
t.actor(ESC,[{"k":knasa,"x":975,"pose":"piensa","cara":"neutral"}],desde=knasa)
L.chip(knum,"ANGLE · RANGE · ALTITUDE","amar",fin=knasa)

t=L.tramo("cielo")
t.dice("The object was not near the water. It was about 13,000 feet up.",
       "It was moving at about 40 miles per hour, a typical wind speed at that height.",
       "The jet was flying at around 435 miles per hour. That is what made the object look so fast.",
       "It is like looking out the window of a fast car: a slow bird can seem to race past.",
       "And on the infrared camera, the object was colder than the ocean. No sign of an engine.",
       "In 2025, the Pentagon's UFO office, AARO, reached a similar answer: about 13,000 feet up, moving with the wind.")
k13=t.m("k13",0,"^13000"); k40=t.m("k40",1,"^40"); k435=t.m("k435",2,"^435"); kcar=t.m("car",3,"^car"); kcold=t.m("cold",4,"^colder"); kaaro=t.m("aaro",5,"^aaro")
t.prop("jet",450,1050,1.3)
t.prop("orbe",1350,900,0.8,k=k13,mov=[(k13,1350,900),(f"{k13}+12",1600,880)])
t.prop("viento",1350,950,1.0,k=k40)
L.numero(k13,13000,"REAL ALTITUDE (FEET)",c="cian",fin=k40); L.numero(k40,40,"SPEED (MPH) · LIKE THE WIND",c="verde",fin=k435)
L.numero(k435,435,"THE JET'S SPEED (MPH)",c="amar",fin=kcar); L.chip(kcar,"A PARALLAX ILLUSION","rosa",fin=kcold)
L.chip(kcold,"COLDER THAN THE OCEAN","cian",fin=kaaro); L.chip(kaaro,"AARO 2025: MOVING WITH THE WIND","verde")

t=L.tramo("oficina",luz="tenue")
t.dice("Some researchers still argue about the exact speed.",
       "But the idea of a craft racing over the waves is gone.",
       "Case closed: an object drifting with the wind.")
kgo=t.m("go",1,"^gone"); kclo=t.m("clo",2,"^closed")
t.actor(ESC,[{"x":600,"pose":"piensa","cara":"neutral"},{"k":kclo,"x":600,"pose":"apunta","cara":"feliz"}])
t.prop("documento",1250,1150,1.0,k=kclo,sello="SOLVED",selloc="verde",cae=True,z=1800)
L.chip(t.key,"SPEED STILL DEBATED","amar",fin=kgo)
L.titulo(kclo,"GOFAST: SOLVED","verde",grande=True)

# 6 · GIMBAL debate
t=L.tramo("cabina",capitulo="GIMBAL: still debated")
t.dice("Next, GIMBAL.",
       "In this video, the object seems to tilt and rotate, like no normal aircraft.",
       "Investigator Mick West argues that what rotates is not the object, but a glare in the camera.",
       "The camera sits on a moving mount called a gimbal. When it turns, the glare turns with it.")
krot=t.m("rot",1,"^rotate"); kwest=t.m("west",2,"^west"); kmount=t.m("mount",3,"^mount")
L.titulo(t.key,"FILE 2 · GIMBAL","amar",grande=True,fin=krot)
t.prop("tv",1250,1300,1.4,k=krot,ir=True)
t.actor(ESC,[{"k":kwest,"x":550,"pose":"apunta","cara":"feliz"}],desde=kwest)
L.chip(kwest,"THEORY: CAMERA GLARE","cian",fin=kmount); L.chip(kmount,"THE CAMERA ROTATES, NOT THE OBJECT","cian")

t=L.tramo("oficina",luz="tenue")
t.dice("Others disagree.",
       "And even West says the video alone does not explain everything the pilots reported.",
       "No official report has closed this case.",
       "So for now, GIMBAL stays in the debate pile.")
kdis=t.m("dis",0,"^disagree"); kalo=t.m("alo",1,"^alone"); knoo=t.m("noo",2,"^official"); kpile=t.m("pile",3,"^debate")
t.actor(ESC,[{"x":550,"pose":"cruzado","cara":"neutral"}])
t.actor(PIL,[{"x":1450,"pose":"cruzado","cara":"enojado","dir":-1},{"k":kalo,"x":1450,"pose":"apunta","cara":"neutral","dir":-1}])
t.prop("documento",975,1150,1.0,k=kpile,sello="DEBATED",selloc="amar",cae=True,z=1800)
L.chip(kdis,"OTHERS DISAGREE","rojo",fin=knoo); L.chip(knoo,"NO OFFICIAL ANSWER","amar",fin=kpile)
L.titulo(kpile,"GIMBAL: DEBATED","amar",grande=True)

# 7 · Tic Tac abierto
t=L.tramo("cielo",capitulo="The Tic Tac: still open")
t.dice("Finally, the Tic Tac.",
       "This is the hardest one.",
       "The video itself is blurry and short.",
       "But it is backed by something the others lack: four aviators who say they saw the object with their own eyes.",
       "As of today, no official report has explained it.")
khard=t.m("hard",1,"^hardest"); kblur=t.m("blur",2,"^blurry"); kfour=t.m("four",3,"^four"); kexp=t.m("exp",4,"^explained")
L.titulo(t.key,"FILE 3 · THE TIC TAC","rojo",grande=True,fin=khard)
t.prop("tv",1250,1300,1.3,k=kblur,ir=True,fin=kfour)
for j,dx in enumerate((500,750,1200,1450)): t.actor(PIL if j%2==0 else PIL2,[{"k":kfour,"x":dx,"pose":"apunta","cara":"sorpresa","dir":1 if dx<975 else -1}],desde=kfour,var=410+j)
t.prop("orbe",975,1050,1.0,k=kfour)
L.chip(kfour,"4 AVIATORS SAW IT","amar",fin=kexp); L.titulo(kexp,"STILL OPEN","rojo",grande=True)

# 8 · contexto oficial
t=L.tramo("oficina",capitulo="What the government says")
t.dice("And the bigger picture is just as strange.",
       "After the videos came out, Congress asked for an official report.",
       "In 2021, US intelligence reviewed 144 reports, mostly from Navy pilots.",
       "Only one was explained with high confidence: a large, deflating balloon.",
       "The other 143 remained unexplained.",
       "In 18 of them, the objects seemed to move in unusual ways.",
       "Officials also said there was no clear sign that any of them came from another world.")
k144=t.m("k144",2,"^144"); kbal=t.m("bal",3,"^balloon"); k143=t.m("k143",4,"^143"); k18=t.m("k18",5,"^18"); kworld=t.m("world",6,"^world")
t.actor(PEN,[{"x":550,"pose":"ofrece","cara":"neutral","objeto":"documento"},{"k":kworld,"x":550,"pose":"cruzado","cara":"neutral"}],os=1.0)
L.numero(k144,144,"REPORTS REVIEWED · 2021",c="cian",fin=kbal)
t.prop("globos",1300,1300,1.2,k=kbal,fin=k143)
L.chip(kbal,"1 EXPLAINED: A BALLOON","verde",fin=k143); L.numero(k143,143,"UNEXPLAINED",c="rojo",fin=k18); L.numero(k18,18,"UNUSUAL MOVEMENT",c="amar",fin=kworld)
L.chip(kworld,"NO SIGN OF ANOTHER WORLD","amar")

t=L.tramo("oficina",luz="tenue")
t.dice("In 2022, the Pentagon created a new office to investigate these reports. It is called AARO.",
       "Its job is to take every case, one by one, and look for an answer.",
       "GOFAST is one of the cases where it published an answer.")
kao=t.m("ao",0,"^aaro"); kjob=t.m("job",1,"^job"); kpub=t.m("pub",2,"^published")
t.actor(PEN,[{"x":600,"pose":"apunta","cara":"neutral"},{"k":kpub,"x":600,"pose":"ofrece","cara":"feliz","objeto":"documento"}],os=1.0)
t.prop("escritorio",1250,1720,1.1,z=1650); t.prop("pc",1250,1640,1.1,texto="AARO",z=1700)
L.chip(kao,"AARO · CREATED IN 2022","cian",fin=kpub); L.chip(kpub,"GOFAST: ANSWER PUBLISHED","verde")

t=L.tramo("sala",luz="tenue")
t.dice("In July 2023, David Fravor testified before Congress, under oath, about what he saw.",
       "Former Navy pilot Ryan Graves told the same hearing that sightings like these were routine for pilots.",
       "At the same hearing, a former intelligence officer made bigger claims about hidden programs.",
       "The Pentagon said it found no verifiable information to back those claims.")
kcong=t.m("cong",0,"^congress"); kgra=t.m("gra",1,"^graves"); kbig=t.m("big",2,"^bigger"); kver=t.m("ver",3,"^verifiable")
L.chip(kgra,"RYAN GRAVES: \"ROUTINE\"","cian",fin=kbig)
t.actor(PIL,[{"x":600,"pose":"saluda","cara":"neutral"}],hasta=kbig)
t.actor(dict(look="ejecutivo",var=420,camisa="#5d4037",s=1.0),[{"k":kbig,"x":600,"pose":"apunta","cara":"neutral"}],desde=kbig)
t.actor(PEN,[{"k":kver,"x":1400,"pose":"cruzado","cara":"neutral","dir":-1}],desde=kver)
L.chip(kcong,"UNDER OATH · JULY 2023","amar",fin=kgra); L.chip(kver,"PENTAGON: NO VERIFIABLE INFO","rojo")

# 8b · guia para leer un video OVNI
t=L.tramo("estudio",capitulo="How to read a UFO video")
t.dice("Before the final verdict, here is a quick guide to reading any UFO video.",
       "First, distance. Without knowing how far away something is, you cannot know its size or its speed.",
       "Second, the camera. Infrared cameras show heat, and a hot spot can bloom into a glare that hides the real shape.",
       "Third, motion. When the camera itself is moving fast, slow things can look fast.",
       "Fourth, the other evidence. Radar, eyewitnesses, and other sensors can make a case much stronger.",
       "That is exactly why the Tic Tac is still open: it has more than just a video.")
kg1=t.m("g1",1,"^distance"); kg2=t.m("g2",2,"^camera"); kg3=t.m("g3",3,"^motion"); kg4=t.m("g4",4,"^evidence"); kg5=t.m("g5",5,"^tic")
L.titulo(t.key,"HOW TO READ A UFO VIDEO","cian",fin=kg1)
t.actor(ESC,[{"x":500,"pose":"apunta","cara":"feliz"},{"k":kg3,"x":500,"pose":"piensa","cara":"neutral"},{"k":kg5,"x":500,"pose":"apunta","cara":"feliz"}])
t.prop("tv",1250,1300,1.3,k=kg2,ir=True,fin=kg4); t.prop("radar",1250,1350,1.2,k=kg4)
L.chip(kg1,"1 · DISTANCE","amar",fin=kg2); L.chip(kg2,"2 · THE CAMERA","rojo",fin=kg3); L.chip(kg3,"3 · MOTION","cian",fin=kg4); L.chip(kg4,"4 · OTHER EVIDENCE","verde",fin=kg5); L.chip(kg5,"THE TIC TAC HAS MORE","rosa")

# 9 · marcador y cierre
t=L.tramo("cielo",capitulo="The scorecard")
t.dice("So here is the scorecard.",
       "GOFAST: solved. An object drifting with the wind.",
       "GIMBAL: still debated.",
       "The Tic Tac: still open.",
       "Three videos, three different answers.",
       "And maybe that is the real lesson: one blurry video is never the whole story.",
       "So next time you see a UFO video, remember the guide: distance, camera, motion, and other evidence.")
ks1=t.m("s1",1,"^gofast"); ks2=t.m("s2",2,"^gimbal"); ks3=t.m("s3",3,"^tic"); kthree=t.m("three",4,"^three"); kles=t.m("les",5,"^lesson")
L.titulo(t.key,"THE SCORECARD","cian",fin=ks1)
L.chip(ks1,"GOFAST · SOLVED ✓","verde",fin=ks2); L.chip(ks2,"GIMBAL · DEBATED","amar",fin=ks3); L.chip(ks3,"TIC TAC · OPEN","rojo",fin=kthree)
t.prop("tv",500,1300,1.0,k=kthree,ir=True); t.prop("tv",975,1300,1.0,k=f"{kthree}+0.3",ir=True); t.prop("tv",1450,1300,1.0,k=f"{kthree}+0.6",ir=True)
kchk=t.m("chk",6,"^guide")
L.titulo(kles,"NEVER THE WHOLE STORY","rosa",fin=kchk); L.chip(kchk,"DISTANCE · CAMERA · MOTION · EVIDENCE","amar")

t=L.tramo("cabina",luz="tenue")
t.dice("Some of these stories end with a balloon. Some end with a camera glare. And some, so far, do not end at all.",
       "Tell me which case you want me to open next.",
       "Follow The Rabbit Loop: one story leads to another.")
t.actor(RAD,[{"x":700,"pose":"juega","cara":"neutral"}])
t.prop("radar",1250,1350,1.2)

L.sfx=[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.2,"fade":0.5,"g":0.1},
       {"f":"extra/ElectricZapBuzz_S011SF.344.wav","k":kacc,"off":0.0,"dur":0.8,"g":0.1}]
meta={"titulo":"The Navy UFO Videos: The Complete File","texto_pantalla":"3 VIDEOS · 3 ANSWERS","lote":"L2026112301rab","marca":"THE RABBIT LOOP","tema":"",
"nota_datos":"Fuentes: Wikipedia (Pentagon UFO videos; Underwood nombro 'Tic Tac'; NYT 16-dic-2017), History.com y The Black Vault (Nimitz 14-nov-2004, objeto blanco ~40-46 pies sin alas, 4 aviadores), CBS (100 millas, filtraciones 2007 y 2017, 'accelerated like nothing'), migflug (video de Underwood; AARO lo lista sin resolver), Aviation Pros e IFLScience (GIMBAL y GOFAST, Atlántico enero 2015), The Black Vault (TTSA, GOFAST marzo 2018, Navy sept-2019 'UAP'), ABC7 (nuevas reglas de reporte 2019), TechSpot/ABS-CBN (Tom DeLonge, Blink-182), TWZ y GeekWire (liberacion oficial 27-abr-2020, 'unidentified'), NASA UAP study 2023 via Metabunk y Washington Examiner (13.000 pies, ~40 mph, mas frio que el oceano, jet ~435 mph), Liberation Times (NASA sin posicion oficial), AARO 2025 via The Black Vault (13.000 pies, se movia con el viento, 5-92 mph), PetaPixel y Boing Boing (Mick West: reflejo/gimbal), ODNI 2021 via CBS/Stripes/TechSpot (144 reportes, 1 globo), TechCrunch/ABC/House Oversight (audiencia 26-jul-2023; Pentagono sin info verificable).",
"fuentes":["https://en.wikipedia.org/wiki/Pentagon_UFO_videos","https://www.history.com/articles/uss-nimitz-2004-tic-tac-ufo-encounter","https://www.cbsnews.com/news/pentagon-videos-unidentied-aerial-phenomena-ufo/","https://www.theblackvault.com/documentarchive/pentagon-releases-aaro-report-on-go-fast-video-analysis/","https://petapixel.com/2022/03/14/famous-navy-ufo-video-was-actually-camera-glare-evidence-suggests","https://www.cbsnews.com/news/pentagon-ufo-report-released-many-uap-cases-remain-unexplained","https://oversight.house.gov/hearing/unidentified-anomalous-phenomena-implications-on-national-security-public-safety-and-government-transparency"]}
g=L.armar(meta,cola=18.0,final={"marca":"THE RABBIT LOOP","texto":"ONE STORY LEADS TO ANOTHER","a":"WATCH THIS NEXT","b":"SUBSCRIBE FOR MORE"})
json.dump(g,open("L2026112301rab_src.json","w"),ensure_ascii=False)
w=sum(len(f.split()) for f in L.frases); print("frases",len(L.frases),"palabras",w,"tramos",len(L.tramos))
