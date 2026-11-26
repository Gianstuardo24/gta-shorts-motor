import sys, json; sys.path.insert(0,'/home/claude/largos'); from largo import *
R=[(r"\b1942\b","nineteen forty-two"),(r"\b1947\b","nineteen forty-seven"),(r"\b1952\b","nineteen fifty-two"),
   (r"\b1992\b","nineteen ninety-two"),(r"\b1994\b","nineteen ninety-four"),(r"\b1995\b","nineteen ninety-five"),(r"\b1997\b","nineteen ninety-seven"),
   (r"\b2006\b","two thousand six"),(r"\b1950s\b","nineteen fifties"),(r"\b1970s\b","nineteen seventies"),(r"\b1980s\b","nineteen eighties"),
   (r"1,400","fourteen hundred"),(r"July 19","July nineteenth"),(r"July 26","July twenty-sixth"),(r"July 29","July twenty-ninth"),(r"July 8","July eighth"),
   (r"March 13","March thirteenth"),(r"February 25","February twenty-fifth"),(r"Washington, D\.C\.","Washington D C"),(r"\bD\.C\.","D C"),
   (r"A-10","A ten"),(r"8 p\.m\.","eight p m"),(r"10 p\.m\.","ten p m"),(r"\bUFO\b","U F O"),(r"\bUFOs\b","U F Os"),
   (r"Ruppelt","Roo pelt"),(r"Santilli","San tilly"),(r"Brazel","Bra zell"),(r"World War Two","World War Two")]
L=Largo(R); L.hints=[]
RAD=dict(look="gamer",var=601,camisa="#37474f",s=0.95)
SAM=dict(look="oficial",var=602,camisa="#4b5320",s=1.0)
RUP=dict(look="inventor",var=603,camisa="#556b2f",pelo="#3e2723",s=0.95)
TES=dict(look="jugadora",var=604,s=0.95)
AST=dict(look="sabio",var=605,s=0.95)
KNOX=dict(look="ejecutivo",var=606,camisa="#263238",pelo="#cfd8dc",s=1.0)
SAN=dict(look="ejecutivo",var=607,camisa="#5d4037",pelo="#212121",s=1.0)
HUM=dict(look="inventor",var=608,camisa="#455a64",s=0.95)
BRA=dict(look="sabio",var=609,camisa="#8d6e63",s=1.0)
SCH=dict(look="ejecutivo",var=610,camisa="#1a237e",pelo="#9e9e9e",s=1.0)
NAR=dict(look="gamer",var=611,camisa="#6a1b9a",s=0.95)

# ---------- 0 · INTRO ----------
t=L.tramo("cielo",capitulo="Five famous cases")
t.dice("Some UFO stories are so famous that they never really go away.",
       "Lights over a city at war, a crashed disc in the desert, and radar blips over the White House.",
       "There is also a film of an alien on an operating table, and a giant V of lights over Phoenix.",
       "Millions of people believed these stories, and some still do.",
       "But today, we know what really happened in each one of them.",
       "These are five famous UFO cases, counted down to the most famous of all, and how each one was finally solved.",
       "Our rule is simple: a case is only closed when the evidence closes it.")
kwar=t.m("war",1,"^war"); kdisc=t.m("disc",1,"^disc"); kblip=t.m("blip",1,"^blips"); kfilm=t.m("film",2,"^film"); kv=t.m("v",2,"^v$"); kmil=t.m("mil",3,"^millions")
kfive=t.m("five",5,"^five"); krule=t.m("rule",6,"^rule")
t.prop("ovni",975,950,1.1,k=t.key,fin=kmil)
t.prop("radar",500,1350,1.0,k=kblip,fin=kmil); t.prop("tv",975,1320,1.0,k=kfilm,ir=True,fin=kmil); t.prop("vLuces",1450,1000,1.0,k=kv,fin=kmil)
L.chip(kwar,"LOS ANGELES · 1942","rojo",fin=kdisc); L.chip(kdisc,"ROSWELL · 1947","amar",fin=kblip); L.chip(kblip,"WASHINGTON · 1952","cian",fin=kfilm)
L.chip(kfilm,"THE ALIEN AUTOPSY · 1995","rosa",fin=kv); L.chip(kv,"PHOENIX · 1997","verde",fin=kmil)
L.titulo(kfive,"5 UFO CASES, SOLVED","amar",grande=True,fin=krule)
L.chip(krule,"CLOSED ONLY BY EVIDENCE","verde")

# ---------- 5 · WASHINGTON 1952 ----------
t=L.tramo("cabina",capitulo="#5 Washington, 1952")
t.dice("Case number five takes us to Washington, D.C., in July 1952.",
       "On the night of July 19, radar screens at the city's airport lit up with blips that nobody could identify.",
       "Some of them seemed to fly over restricted airspace, near the White House and the Capitol.",
       "Pilots in the area reported strange lights, and fighter jets were sent up to check.",
       "But by the time the jets arrived, the blips were usually gone.",
       "One week later, on July 26, the whole thing happened again.")
kjul=t.m("jul",1,"^19$"); krest=t.m("rest",2,"^restricted"); kpil=t.m("pil",3,"^pilots"); kgone=t.m("gone",4,"^gone"); kagain=t.m("again",5,"^again")
L.titulo(t.key,"CASE 5 · WASHINGTON 1952","cian",fin=kjul)
t.actor(RAD,[{"x":600,"pose":"juega","cara":"neutral"},{"k":kjul,"x":600,"pose":"apunta","cara":"sorpresa"},{"k":kgone,"x":600,"pose":"piensa","cara":"neutral"},{"k":kagain,"x":600,"pose":"apunta","cara":"sorpresa","fx":"tiembla"}])
t.prop("radar",1250,1350,1.4,k=kjul)
L.chip(krest,"OVER THE WHITE HOUSE · THE CAPITOL","rojo",fin=kpil); L.chip(kgone,"JETS ARRIVE · BLIPS GONE","amar",fin=kagain); L.chip(kagain,"JULY 26 · AGAIN","rosa")

t=L.tramo("oficina")
t.dice("The story hit front pages across the country, and people wanted answers.",
       "So on July 29, the Air Force held a press conference, the biggest one the Pentagon had held since World War Two.",
       "Major General John Samford explained that the most likely cause was the weather.",
       "On hot summer nights, a layer of warm air can sit on top of cooler air, and that is called a temperature inversion.",
       "That layer can bend radar waves back down to the ground, so the radar picks up things like buildings, vehicles, or birds, and shows them as targets in the sky.",
       "The same layer can also make lights on the ground look like they are floating.")
kfront=t.m("front",0,"^front"); kpress=t.m("press",1,"^press"); ksam=t.m("sam",2,"^samford"); kwea=t.m("wea",2,"^weather"); kinv=t.m("inv",3,"^inversion"); kbend=t.m("bend",4,"^bend"); kflo=t.m("flo",5,"^floating")
t.actor(SAM,[{"x":975,"pose":"parado","cara":"neutral"},{"k":ksam,"x":975,"pose":"explica","cara":"neutral"},{"k":kwea,"x":975,"pose":"apunta","cara":"feliz"}],desde=kpress)
L.chip(kpress,"JULY 29 · BIGGEST SINCE WWII","amar",fin=ksam); L.chip(ksam,"MAJ. GEN. JOHN SAMFORD","cian",fin=kinv)
L.inserto(kinv,kflo,"tableroH",{"titulo":"TEMPERATURE INVERSION","filas":[["TOP","WARM AIR"],["BELOW","COOL AIR"],["RADAR","BENDS DOWN"]]},mov="fijo")
L.chip(kflo,"GROUND LIGHTS LOOK LIKE THEY FLOAT","verde")

t=L.tramo("oficina",luz="tenue")
t.dice("Not everyone was convinced, and even Captain Edward Ruppelt, who ran the Air Force's UFO project, had his doubts.",
       "But a later study by the Civil Aeronautics Administration found that blips like these were common, and that they almost always showed up during a temperature inversion.",
       "And Washington's hot, muggy summer nights are exactly the kind of weather that creates these radar ghosts.",
       "Verdict: mostly solved. It was the weather, playing tricks on the radar.")
krup=t.m("rup",0,"^ruppelt"); kcon=t.m("con",1,"^civil"); kgho=t.m("gho",2,"^ghosts"); kver=t.m("ver",3,"^verdict")
t.actor(RUP,[{"x":700,"pose":"piensa","cara":"neutral"},{"k":kcon,"x":700,"pose":"cruzado","cara":"neutral"},{"k":kver,"x":700,"pose":"parado","cara":"feliz"}])
t.prop("radar",1300,1350,1.1,k=kgho)
L.chip(krup,"CAPT. EDWARD RUPPELT · DOUBTS","amar",fin=kcon); L.chip(kcon,"CAA STUDY · INVERSIONS","cian",fin=kver)
t.prop("documento",1300,1150,1.0,k=kver,sello="WEATHER",selloc="verde",cae=True,z=1800)
L.titulo(kver,"MOSTLY SOLVED","verde",grande=True)

# ---------- 4 · PHOENIX 1997 ----------
t=L.tramo("desierto",capitulo="#4 The Phoenix Lights, 1997")
t.dice("Case number four is the Phoenix Lights, on March 13, 1997.",
       "That evening, thousands of people across Arizona saw lights in the sky.",
       "There were actually two different events that night, and that detail is the key to the whole case.",
       "The first one came around 8 p.m.: a giant V of lights, moving slowly across the state.",
       "The second came around 10 p.m.: a row of bright orange lights, floating over the mountains south of Phoenix, and then fading away one by one.")
kth=t.m("th",1,"^thousands"); ktwo=t.m("two",2,"^two"); k8=t.m("k8",3,"^8"); k10=t.m("k10",4,"^10"); kfade=t.m("fade",4,"^fading")
L.titulo(t.key,"CASE 4 · PHOENIX 1997","verde",fin=kth)
t.actor(TES,[{"x":450,"pose":"parado","cara":"neutral"},{"k":kth,"x":450,"pose":"apunta","cara":"sorpresa"},{"k":kfade,"x":450,"pose":"piensa","cara":"neutral"}])
t.prop("vLuces",1250,1050,1.3,k=k8,fin=k10,mov=[(k8,1650,1080),(f"{k8}+4.0",1000,1020)])
L.hints+= [{"k":k8,"tipo":"general"},{"k":k10,"tipo":"general"}]
for j in range(5): t.prop("bengala",900+j*190,1150+(j%2)*25,1.0,k=f"{k10}+{0.35*j:.2f}",fin=f"{kfade}+{0.5*j:.2f}")
L.chip(ktwo,"TWO EVENTS · ONE NIGHT","amar",fin=k8); L.chip(k8,"8 PM · A GIANT V","cian",fin=k10); L.chip(k10,"10 PM · ORANGE LIGHTS","rojo")

t=L.tramo("desierto",luz="tenue")
t.dice("Videos of the ten o'clock lights went on national TV, and the story exploded.",
       "Months later, the Air National Guard gave an answer for that second event.",
       "Planes from Maryland, called A-10s, were flying a training exercise named Operation Snowbird.",
       "Over the Barry M. Goldwater Range, they dropped flares, which are very bright lights that hang from small parachutes.",
       "From Phoenix, the mountains hid the ground, so the flares seemed to float in the air, and then vanish as they sank behind the ridge.")
ktv=t.m("tv",0,"^tv"); kang=t.m("ang",1,"^guard"); ka10=t.m("a10",2,"^snowbird"); kfl=t.m("fl",3,"^flares"); kpar=t.m("par",3,"^parachutes"); kridge=t.m("ridge",4,"^ridge")
t.prop("tv",500,1320,1.1,k=ktv,ir=True,fin=kang)
t.prop("jet",700,950,1.2,k=ka10); t.prop("jet",950,1050,1.0,k=f"{ka10}+0.3")
for j in range(5): t.prop("bengala",1050+j*170,950+(j%2)*30,1.0,k=f"{kfl}+{0.3*j:.2f}",mov=[(f"{kfl}+{0.3*j:.2f}",1050+j*170,950),(kridge,1050+j*170,1330)])
L.chip(kang,"AIR NATIONAL GUARD","cian",fin=ka10); L.chip(ka10,"A-10s · OPERATION SNOWBIRD","amar",fin=kfl); L.chip(kpar,"FLARES ON PARACHUTES","rojo",fin=kridge)
L.chip(kridge,"HIDDEN BY THE MOUNTAINS","verde")

t=L.tramo("desierto")
t.dice("And the first event, the giant V, has a different story.",
       "An amateur astronomer said he watched it through his telescope, and saw separate small planes flying in formation.",
       "There is no official report on that part.",
       "Verdict: the ten o'clock lights are solved, they were military flares. The V was very likely planes, but nobody ever officially closed it.")
kast=t.m("ast",1,"^astronomer"); kform=t.m("form",1,"^formation"); kno=t.m("no",2,"^official"); kver=t.m("ver",3,"^verdict")
t.actor(AST,[{"x":600,"pose":"parado","cara":"neutral"},{"k":kast,"x":600,"pose":"apunta","cara":"feliz"},{"k":kno,"x":600,"pose":"cruzado","cara":"neutral"}],desde=kast)
t.prop("vLuces",1250,1050,1.2,k=t.key,fin=kform)
L.hints.append({"k":kform,"tipo":"general"})
for j in range(5): t.prop("jet",1000+j*120,900+abs(j-2)*60,0.6,k=f"{kform}+{0.15*j:.2f}",fin=kver)
L.chip(kform,"SMALL PLANES IN FORMATION","cian",fin=kno); L.chip(kno,"NO OFFICIAL REPORT","amar",fin=kver)
L.inserto(kver,f"{kver}+5.5","tableroH",{"titulo":"PHOENIX 1997","filas":[["10 PM","FLARES"],["8 PM","PLANES"]]},mov="fijo")

# ---------- 3 · LOS ANGELES 1942 ----------
t=L.tramo("guerra42",capitulo="#3 The Battle of Los Angeles, 1942")
t.dice("Case number three is the Battle of Los Angeles, in February 1942.",
       "It was less than three months after Pearl Harbor, and the whole West Coast was on edge.",
       "Just two days earlier, a Japanese submarine had fired on an oil field near Santa Barbara.",
       "Then, in the early hours of February 25, radar picked up something near Los Angeles.",
       "Air raid sirens went off, the city went dark, and searchlights swept the sky.",
       "For about an hour, the army fired more than 1,400 anti-aircraft shells into the night.")
kpearl=t.m("pearl",1,"^pearl"); ksub=t.m("sub",2,"^submarine"); krad=t.m("rad",3,"^radar"); ksir=t.m("sir",4,"^sirens"); kshell=t.m("shell",5,"^1400")
L.titulo(t.key,"CASE 3 · LOS ANGELES 1942","rojo",fin=kpearl)
SOLD=dict(look="oficial",var=612,camisa="#4b5320",s=1.0); CIV=dict(look="jugadora",var=613,camisa="#795548",s=0.95)
t.actor(CIV,[{"x":1450,"pose":"parado","cara":"neutral","dir":-1},{"k":ksub,"x":1450,"pose":"piensa","cara":"triste","dir":-1},{"k":ksir,"x":1450,"pose":"apunta","cara":"sorpresa","dir":-1,"fx":"tiembla"}])
t.actor(SOLD,[{"k":krad,"x":550,"pose":"parado","cara":"neutral"},{"k":ksir,"x":550,"pose":"apunta","cara":"enojado"},{"k":kshell,"x":550,"pose":"arriba","cara":"enojado","fx":"tiembla"}],desde=krad)
L.chip(kpearl,"3 MONTHS AFTER PEARL HARBOR","amar",fin=ksub); L.chip(ksub,"SUB ATTACK · SANTA BARBARA","rojo",fin=krad)
t.prop("radar",1350,1350,1.0,k=krad,fin=ksir)
L.numero(kshell,1400,"ANTI-AIRCRAFT SHELLS",pre="+",c="rojo")
for j in range(6): t.prop("bengala",500+j*220,700+(j%3)*90,0.7,k=f"{kshell}+{0.25*j:.2f}")
L.sacudidas.append({"k":kshell,"f":16})

t=L.tramo("guerra42",luz="tenue")
t.dice("The next day, a newspaper photo showed searchlights crossing on something in the sky, and for decades, people pointed to it as proof of a giant craft.",
       "But no bombs fell, no plane was shot down, and no wreckage was ever found.",
       "The Secretary of the Navy, Frank Knox, called it a false alarm, caused by jittery nerves.",
       "Here is what most likely started it: an Air Force history written years later concluded that weather balloons, released that night, were probably the first targets.",
       "After that, panic did the rest, and smoke from the shells, caught in the searchlights, looked like even more targets.")
kphoto=t.m("photo",0,"^photo"); kdec=t.m("dec",0,"^decades"); kno=t.m("no",1,"^bombs"); kknox=t.m("knox",2,"^knox"); kfalse=t.m("false",2,"^false"); kbal=t.m("bal",3,"^balloons"); kpan=t.m("pan",4,"^panic")
t.actor(CIV,[{"x":700,"pose":"parado","cara":"sorpresa"},{"k":kdec,"x":700,"pose":"apunta","cara":"sorpresa"},{"k":kno,"x":700,"pose":"piensa","cara":"neutral"}],hasta=kknox)
t.prop("documento",1300,1150,1.0,k=kphoto,sello="1942 PHOTO",selloc="amar",cae=True,z=1800,fin=kknox)
t.actor(KNOX,[{"k":kknox,"x":700,"pose":"parado","cara":"neutral"},{"k":kfalse,"x":700,"pose":"cruzado","cara":"enojado"},{"k":kbal,"x":700,"pose":"apunta","cara":"neutral"}],desde=kknox)
t.prop("documento",1350,1150,1.0,k=kfalse,sello="FALSE ALARM",selloc="rojo",cae=True,z=1800,fin=kbal)
t.prop("globos",1300,950,1.0,k=kbal,mov=[(kbal,1300,1000),(kpan,1300,800)])
L.chip(kno,"NO BOMBS · NO WRECKAGE","amar",fin=kknox); L.chip(kknox,"FRANK KNOX · NAVY SECRETARY","cian",fin=kbal); L.chip(kbal,"WEATHER BALLOONS","verde",fin=kpan)
L.chip(kpan,"SMOKE + SEARCHLIGHTS = MORE TARGETS","rojo")

t=L.tramo("guerra42")
t.dice("And that famous photo was heavily retouched before it was printed, which made the beams look like they met on a solid object.",
       "The saddest part is that five people died that night, in car crashes during the blackout, and from heart attacks.",
       "Verdict: solved. It was a real panic, with no enemy in the sky.")
kret=t.m("ret",0,"^retouched"); kdied=t.m("died",1,"^died"); kver=t.m("ver",2,"^verdict")
L.chip(kret,"THE PHOTO WAS RETOUCHED","amar",fin=kdied); L.chip(kdied,"5 PEOPLE DIED","rojo",fin=kver)
t.prop("documento",975,1150,1.0,k=kver,sello="NO ENEMY",selloc="verde",cae=True,z=1800)
L.titulo(kver,"SOLVED","verde",grande=True)

# ---------- 2 · ALIEN AUTOPSY 1995 ----------
t=L.tramo("setTVH",capitulo="#2 The Alien Autopsy, 1995")
t.dice("Case number two is the Alien Autopsy film, from 1995.",
       "That year, a British producer named Ray Santilli showed the world a black-and-white film.",
       "It seemed to show doctors cutting open the body of an alien.",
       "He said it was secret military footage from 1947, from the Roswell crash, and that he had bought it from the original cameraman.",
       "It aired on TV in dozens of countries, and millions of people watched it.")
ksan=t.m("san",1,"^santilli"); kdoc=t.m("doc",2,"^doctors"); kmil=t.m("mil",3,"^military"); kaired=t.m("aired",4,"^aired")
L.titulo(t.key,"CASE 2 · THE ALIEN AUTOPSY","rosa",fin=ksan)
t.actor(SAN,[{"x":550,"pose":"parado","cara":"feliz"},{"k":kdoc,"x":550,"pose":"apunta","cara":"feliz"},{"k":kaired,"x":550,"pose":"celebra","cara":"risa"}],desde=ksan)
t.prop("tv",1250,1300,1.4,k=kdoc,ir=True)
L.chip(ksan,"RAY SANTILLI · PRODUCER","amar",fin=kmil); L.chip(kmil,"\"MILITARY FOOTAGE FROM 1947\"","rojo",fin=kaired); L.chip(kaired,"SHOWN IN DOZENS OF COUNTRIES","cian")

t=L.tramo("setTVH",luz="tenue")
t.dice("Experts argued about it for years, and many said the body looked like a dummy.",
       "Then, in 2006, Santilli and his partner Gary Shoefield admitted that the film was a reconstruction.",
       "They said they had seen real footage in 1992, but it had decayed, so they decided to rebuild it.",
       "The body was a model, made by a sculptor named John Humphreys, inside a flat in London.",
       "Nobody has ever shown the so-called original footage.",
       "Verdict: solved. The film the world watched was staged.")
kexp=t.m("exp",0,"^dummy"); kadm=t.m("adm",1,"^admitted"); krec=t.m("rec",1,"^reconstruction"); kdec=t.m("dec",2,"^decayed"); khum=t.m("hum",3,"^humphreys"); knob=t.m("nob",4,"^nobody"); kver=t.m("ver",5,"^verdict")
t.actor(SAN,[{"x":500,"pose":"parado","cara":"neutral"},{"k":kadm,"x":500,"pose":"cruzado","cara":"triste"},{"k":kdec,"x":500,"pose":"explica","cara":"neutral"}],hasta=khum)
t.actor(HUM,[{"k":khum,"x":1350,"pose":"sostiene","cara":"feliz","dir":-1}],desde=khum)
t.prop("documento",1300,1150,1.0,k=krec,sello="RECONSTRUCTION",selloc="rojo",cae=True,z=1800,fin=khum)
L.chip(kexp,"\"IT LOOKS LIKE A DUMMY\"","amar",fin=kadm); L.chip(kadm,"2006 · THEY ADMIT IT","rojo",fin=khum); L.chip(khum,"JOHN HUMPHREYS · SCULPTOR","cian",fin=knob)
L.chip(knob,"NO ORIGINAL FOOTAGE","amar",fin=kver)
L.titulo(kver,"SOLVED","verde",grande=True)

# ---------- 1 · ROSWELL 1947 ----------
t=L.tramo("desierto",capitulo="#1 Roswell, 1947")
t.dice("And case number one is the most famous UFO case of all time: Roswell, New Mexico, in 1947.",
       "That summer, a rancher named Mac Brazel found strange debris on his land: sticks, foil, rubber, tape, and paper.",
       "In early July, he took some of it to the local sheriff, who called the nearby Army airfield.",
       "On July 8, the base put out a stunning press release, saying they had recovered a flying disc.",
       "The very next day, the Army changed its story, and said it was just a weather balloon.",
       "After that, for about thirty years, almost nobody talked about it.")
kmost=t.m("most",0,"^roswell"); kbra=t.m("bra",1,"^brazel"); kdeb=t.m("deb",1,"^debris"); ksh=t.m("sh",2,"^sheriff"); kdisc=t.m("disc",3,"^disc"); kbal=t.m("bal",4,"^balloon"); kthirty=t.m("thirty",5,"^thirty")
L.titulo(t.key,"CASE 1 · ROSWELL 1947","amar",grande=True,fin=kbra)
t.actor(BRA,[{"x":550,"pose":"parado","cara":"neutral"},{"k":kdeb,"x":550,"pose":"apunta","cara":"sorpresa"},{"k":ksh,"x":550,"pose":"sostiene","cara":"neutral","objeto":"cajita"},{"k":kthirty,"x":550,"pose":"piensa","cara":"neutral"}],desde=kbra)
for j,(dx,dy) in enumerate(((1100,1690),(1260,1700),(1420,1685),(1580,1700))): t.prop("documento",dx,dy,0.35,k=f"{kdeb}+{0.2*j:.1f}",fin=kdisc)
L.chip(kbra,"MAC BRAZEL · RANCHER","cian",fin=kdeb); L.chip(kdeb,"STICKS · FOIL · RUBBER · TAPE","amar",fin=kdisc)
t.prop("documento",1300,1150,1.0,k=kdisc,sello="FLYING DISC",selloc="rojo",cae=True,z=1800,fin=kbal)
t.prop("documento",1300,1150,1.0,k=kbal,sello="WEATHER BALLOON",selloc="amar",cae=True,z=1800,fin=kthirty)
L.chip(kthirty,"30 YEARS OF SILENCE","rosa")

t=L.tramo("oficina",luz="tenue")
t.dice("Then, in the late 1970s and the 1980s, new witnesses came forward, with stories of a crashed ship, and even alien bodies.",
       "Roswell became a legend, and the questions grew so loud that a congressman, Steven Schiff, asked a government watchdog to investigate.",
       "In 1994, the Air Force published its answer.",
       "The debris was not a weather balloon, because that had been a cover story.",
       "It came from Project Mogul, a top secret program.")
kwit=t.m("wit",0,"^witnesses"); kleg=t.m("leg",1,"^legend"); ksch=t.m("sch",1,"^schiff"); k94=t.m("k94",2,"^1994"); kcov=t.m("cov",3,"^cover"); kmog=t.m("mog",4,"^mogul")
t.actor(TES,[{"x":500,"pose":"parado","cara":"sorpresa"},{"k":kleg,"x":500,"pose":"apunta","cara":"sorpresa"}],hasta=ksch)
t.actor(SCH,[{"k":ksch,"x":800,"pose":"parado","cara":"neutral"},{"k":k94,"x":800,"pose":"cruzado","cara":"neutral"},{"k":kmog,"x":800,"pose":"apunta","cara":"sorpresa"}],desde=ksch)
L.chip(kwit,"NEW WITNESSES · LATE 1970s","amar",fin=ksch); L.chip(ksch,"REP. STEVEN SCHIFF","cian",fin=k94)
t.prop("documento",1350,1150,1.0,k=kcov,sello="COVER STORY",selloc="rojo",cae=True,z=1800,fin=kmog)
L.titulo(kmog,"PROJECT MOGUL","rojo",grande=True)

t=L.tramo("desierto")
t.dice("Its goal was to fly long trains of balloons, high in the sky, carrying microphones to listen for Soviet nuclear tests.",
       "One of those trains was launched in June 1947, and it was lost, not far from the Brazel ranch.",
       "The materials matched: balloons, foil radar reflectors, sticks, and tape.",
       "So yes, there was a cover-up, but it was hiding a spy program, not a spaceship.")
ktr=t.m("tr",0,"^trains"); ksov=t.m("sov",0,"^soviet"); klost=t.m("lost",1,"^lost"); kmat=t.m("mat",2,"^matched"); kspy=t.m("spy",3,"^spy")
for j in range(4): t.prop("globos",700+j*170,700+j*120,0.8,k=f"{ktr}+{0.2*j:.1f}",mov=[(f"{ktr}+{0.2*j:.1f}",700+j*170,750+j*120),(klost,1100+j*170,1000+j*130)])
L.chip(ksov,"LISTENING FOR SOVIET NUCLEAR TESTS","cian",fin=klost); L.chip(klost,"LOST IN JUNE 1947","amar",fin=kmat)
L.inserto(kmat,kspy,"tableroH",{"titulo":"THE DEBRIS MATCHED","filas":[["1","BALLOONS"],["2","FOIL"],["3","STICKS"]]},mov="fijo")
L.titulo(kspy,"A SPY PROGRAM","verde",grande=True)

t=L.tramo("oficina")
t.dice("And the alien bodies are covered by a second report.",
       "In 1997, the Air Force released The Roswell Report: Case Closed.",
       "It explained that, in the 1950s, the Air Force dropped human-sized test dummies from high balloons over New Mexico.",
       "Over the years, some witnesses likely mixed those memories, and other events, with the 1947 crash.",
       "Verdict: solved. It was a spy balloon, a secret, and decades of mixed-up memories.")
kbod=t.m("bod",0,"^bodies"); k97=t.m("k97",1,"^closed"); kdum=t.m("dum",2,"^dummies"); kmix=t.m("mix",3,"^mixed"); kver=t.m("ver",4,"^verdict")
t.actor(SCH,[{"x":600,"pose":"parado","cara":"neutral"},{"k":kdum,"x":600,"pose":"apunta","cara":"sorpresa"},{"k":kver,"x":600,"pose":"parado","cara":"feliz"}])
t.prop("documento",1300,1150,1.0,k=k97,sello="CASE CLOSED",selloc="verde",cae=True,z=1800,fin=kmix)
L.chip(k97,"\"THE ROSWELL REPORT: CASE CLOSED\" · 1997","cian",fin=kdum); L.chip(kdum,"1950s · TEST DUMMIES","amar",fin=kmix); L.chip(kmix,"MIXED-UP MEMORIES","rosa",fin=kver)
L.titulo(kver,"SOLVED","verde",grande=True)

# ---------- SCORECARD ----------
t=L.tramo("cielo",capitulo="The scorecard")
t.dice("So here is the scorecard.",
       "Washington was weather that tricked the radar, Phoenix was military flares, and probably planes, and Los Angeles was a panic with no enemy.",
       "The autopsy was a staged film, and Roswell was a spy balloon.",
       "Notice the pattern: each case looked impossible because one piece of the story was missing.",
       "It was a weather layer, a mountain ridge, a wartime panic, a confession, and a secret program.",
       "Once that missing piece shows up, the mystery closes.")
ksc=t.m("sc",1,"^washington"); kpat=t.m("pat",3,"^pattern"); kpie=t.m("pie",4,"^weather"); kclo=t.m("clo",5,"^closes")
L.inserto(ksc,kpat,"tableroH",{"titulo":"THE SCORECARD","filas":[["WASHINGTON","WEATHER"],["PHOENIX","FLARES"],["LOS ANGELES","PANIC"],["THE AUTOPSY","STAGED"],["ROSWELL","SPY BALLOON"]]},mov="fijo")
L.titulo(kpat,"ONE MISSING PIECE","amar",grande=True,fin=kpie)
L.chip(kpie,"WEATHER · RIDGE · PANIC · CONFESSION · SECRET","cian",fin=kclo)
t.prop("ovni",975,950,1.0,k=kclo)

t=L.tramo("cabina",luz="tenue")
t.dice("That does not mean every UFO case is solved, because some files are still open.",
       "Tell me which case you want me to open next.",
       "Follow The Rabbit Loop: one story leads to another.")
t.actor(NAR,[{"x":700,"pose":"juega","cara":"neutral"},{"k":t.m("tell",1,"^tell"),"x":700,"pose":"saluda","cara":"feliz"}])
t.prop("radar",1250,1350,1.2)

L.sfx=[{"f":"extra/CbRadioStatic_S08TE.394.wav","k":"0","off":0.0,"dur":1.2,"fade":0.5,"g":0.1}]
meta={"titulo":"5 Famous UFO Cases, Finally Solved","texto_pantalla":"5 CASES · SOLVED","lote":"L2026112302rab","marca":"THE RABBIT LOOP","tema":"",
"nota_datos":"Fuentes verificadas (23-nov): Washington 1952 — prensa 29-jul-1952 de Samford (la mayor desde la 2a Guerra), inversion de temperatura; Ruppelt con dudas; Condon Report 1969. Phoenix 1997 — dos eventos (V ~20h, luces ~22h); bengalas de A-10 de la ANG de Maryland, Operacion Snowbird, Barry M. Goldwater Range; astronomo aficionado vio aviones en formacion (sin informe oficial). Los Angeles 1942 — 25-feb-1942, >1.400 proyectiles, Knox 'false alarm'/'jittery nerves', globos meteorologicos (historia de la USAF), 5 muertos (accidentes y ataques cardiacos), foto retocada. Alien Autopsy — Santilli 1995; 2006 admitio 'reconstruccion' con Gary Shoefield; escultor John Humphreys. Roswell — Brazel, comunicado 8-jul-1947 'flying disc', globo meteorologico al dia siguiente; Schiff pidio a la GAO; informe USAF 1994 Project Mogul; 'The Roswell Report: Case Closed' 1997 (maniquies de prueba de los 50).",
"fuentes":["https://en.wikipedia.org/wiki/1952_Washington,_D.C.,_UFO_incident","https://en.wikipedia.org/wiki/Phoenix_Lights","https://en.wikipedia.org/wiki/Battle_of_Los_Angeles","https://en.wikipedia.org/wiki/Alien_autopsy","https://en.wikipedia.org/wiki/Roswell_incident","https://www.af.mil/News/Article-Display/Article/2215813/"]}
g=L.armar(meta,cola=18.0,final={"marca":"THE RABBIT LOOP","texto":"ONE STORY LEADS TO ANOTHER","a":"WATCH THIS NEXT","b":"SUBSCRIBE FOR MORE"})
g["escena"]["escenas"][0]["planos_hint"]=L.hints
json.dump(g,open("L2026112302rab_src.json","w"),ensure_ascii=False)
w=sum(len(f.split()) for f in L.frases); print("frases",len(L.frases),"palabras",w,"tramos",len(L.tramos))
