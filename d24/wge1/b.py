import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["GTA 6 was hiding in another Rockstar game. And nobody saw it for years.",
"In 2018, Rockstar released Red Dead Redemption 2.",
"This January, fans digging through its files found a boat texture nobody had seen.",
"It had a ship name painted on it: The Leonida.",
"Now here's why that name matters.",
"Leonida is the state where GTA 6 takes place.",
"Some fans call it a planned tease. Others say it's a leftover. Rockstar hasn't said a word.",
"Tell me which one you believe.",
"Follow for more GTA 6 secrets."]
V=[f.replace("GTA 6","GTA six").replace("2018","twenty eighteen").replace("Redemption 2","Redemption two") for f in F]
G=dict(look="gamer",var=81,pelo="#212121",camisa="#7e57c2",lentes=False,s=1.0)
video("G2026112501en_src.json","G2026112501en","THE VICEVERSE GG","GTA 6 Was Hiding in Another Game 🤫👀","HIDING IN ANOTHER GAME",F,V,
 marcas=[("hiding",0,"^hiding"),("files",2,"^files"),("found",2,"^found"),("leonida",3,"^leonida"),("matters",4,"^matters"),("state",5,"^state"),("tease",6,"^tease"),("leftover",6,"^leftover")],
 escenas=[
  {"z":"cuartoGamerV","o":{"era":2026},"actores":[{**G,"keys":[{"k":0,"x":420,"pose":"juega","cara":"sorpresa"}]}],"props":[{"tipo":"humo","x":860,"y":1500,"s":.4,"a":.12}]},
  {"k":"s_1","i":["#4a2a14","#22120a","#060302"],"luz2":"255,210,160","pedestal":True,"props":[{"tipo":"calendario","x":540,"y":1300,"s":1.6,"mes":"OCTOBER","anio":2018,"dia":26,"color":"#bf360c"}]},
  {"k":"s_2","z":"salaIBMV","actores":[{"look":"jugadora","var":82,"s":1.0,"keys":[{"k":"s_2","x":380,"pose":"teclea","cara":"neutral"},{"k":"found","x":380,"pose":"teclea","cara":"sorpresa"}]}],"props":[{"tipo":"lupa","x":780,"y":1250,"s":1.2,"k":"found","flota":6}]},
  {"k":"s_3","z":"marNocheV","o":{"hora":"atardecer","lunaX":-120},"props":[{"tipo":"bote","x":560,"y":1240,"s":1.15,"nombre":"THE LEONIDA","nk":"leonida"},{"tipo":"neblina","x":540,"y":1150,"a":.10}]},
  {"k":"s_4","z":"casaPalmasV","o":{"sinCasa":True},"actores":[{**G,"keys":[{"k":"s_4","x":420,"pose":"piensa","cara":"sorpresa"}]}]},
  {"k":"s_5","i":["#e8e2d2","#a89878","#2a2214"],"luz2":"255,245,220","props":[{"tipo":"papel","x":540,"y":1760,"s":1.25,"titulo":"GTA 6 · THE MAP","dato":"STATE: LEONIDA","sello":"MATCH","selloc":"verde","filaDato":5}]},
  {"k":"s_6","z":"nocheV","o":{"ciudad":True,"sem":9},"actores":[{**G,"keys":[{"k":"s_6","x":330,"pose":"explica","cara":"feliz"}]},{"look":"jugadora","var":82,"s":1.0,"keys":[{"k":"s_6","x":760,"pose":"cruzado","cara":"neutral"},{"k":"leftover","x":760,"pose":"explica","cara":"feliz"}]}]}],
 emojis=[{"k":"hiding","e":"🤫"},{"k":"found","e":"👀"},{"k":"matters","e":"🤯","dur":1.2}],sacudidas=[{"k":"leonida","f":12}],
 gancho2=4,cierre="PLANNED OR LEFTOVER?",cierre2="Your guess. Comment",paises=["PLANNED","LEFTOVER"],
 nota="Red Dead Redemption 2 salió el 26-oct-2018. En enero de 2026 (GameRoll en X, 24-ene-2026) se encontró en sus archivos una textura de bote sin usar con nombres de barcos; uno es 'The Leonida'. Leonida es el estado de GTA 6. Sin confirmación de Rockstar. Fuentes: Daily Dot (28-ene-2026), Attack of the Fanboy. Disparador: secreto. Gancho tipo 2.",
 fuentes=["https://dailydot.com/rdr2-gta6-the-leonida-easter-egg","https://attackofthefanboy.com/?p=1049353"])
