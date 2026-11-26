import sys; sys.path.insert(0,'/home/claude/d24'); from formato import *
F=["GTA 6 just humiliated Hollywood with a record no one has ever touched. And that's not even its only win.",
"It launched on November 19, after two delays.",
"Before day one, it had already sold 32.5 million copies.",
"Then Take-Two estimated its day one sales at 3.79 billion dollars.",
"The biggest movie opening ever, Avengers: Endgame, made about 1.2 billion dollars in its opening weekend.",
"So GTA 6 made about three times that in a single day. The biggest launch in entertainment history.",
"But the biggest shock didn't come from the money. Sure, it was a surprise, but…",
"the critics left everyone speechless. When the reviews landed on Metacritic, fans couldn't believe it.",
"The critics agreed on a 99 out of 100. A score no game had reached in 28 years, since Zelda: Ocarina of Time.",
"Tell me if you think it's the best game in history, and if you've played it yet.",
"Follow for more GTA 6 news."]
V=[f.replace("GTA 6","GTA six").replace("November 19","November nineteenth").replace("32.5 million","thirty-two and a half million").replace("3.79 billion","three point seven nine billion").replace("1.2 billion","one point two billion").replace("Take-Two","Take Two").replace("a 99 out of 100","a ninety-nine out of a hundred").replace("28 years","twenty-eight years") for f in F]
G=dict(look="gamer",var=99,pelo="#3e2723",camisa="#00acc1",lentes=False,s=1.0)
G2P=dict(look="jugador",var=98,pelo="#212121",camisa="#ab47bc",s=1.0)
video("G2026112502en_src.json","G2026112502en","THE VICEVERSE GG","GTA 6 Just HUMILIATED Hollywood 🎬😳","HUMILIATED HOLLYWOOD",F,V,
 marcas=[("hollywood",0,"^hollywood"),("win",0,"^win"),("delays",1,"^delays"),("m32",2,"^million"),("m379",3,"^billion"),("movie",4,"^movie"),("m12",4,"^billion"),("three",5,"^three"),("history",5,"^history"),("shock",6,"^shock"),("speechless",7,"^speechless"),("m99",8,"^99"),("zelda",8,"^zelda")],
 escenas=[
  {"z":"escenarioV","actores":[{**G,"keys":[{"k":0,"x":540,"pose":"celebra","cara":"risa"}]}],"props":[{"tipo":"billetes","x":260,"y":1700,"s":1.4,"z":1900},{"tipo":"bolsa_dinero","x":840,"y":1700,"s":1.3,"z":1900},{"tipo":"humo","x":540,"y":1800,"s":.8,"a":.12}]},
  {"k":"s_1","i":["#3a0d2a","#1c0614","#050104"],"luz2":"255,120,200","pedestal":True,"props":[{"tipo":"calendario","x":540,"y":1300,"s":1.7,"mes":"NOVEMBER","anio":2026,"dia":19,"color":"#c2185b"}]},
  {"k":"s_2","z":"tiendaJuegosV","actores":[{"look":"vendedor","var":100,"s":1.0,"keys":[{"k":"s_2","x":330,"pose":"ofrece","cara":"feliz","objeto":"cajita"}]},{**G,"keys":[{"k":"s_2","x":760,"pose":"celebra","cara":"risa"}]}]},
  {"k":"s_3","i":["#1b3a1f","#0c1d0f","#020603"],"luz2":"190,255,190","props":[{"tipo":"billetes","x":540,"y":1700,"s":2.4},{"tipo":"bolsa_dinero","x":300,"y":1720,"s":1.8},{"tipo":"bolsa_dinero","x":790,"y":1720,"s":1.8}]},
  {"k":"s_4","z":"nocheV","o":{"ciudad":True,"sem":42},"props":[{"tipo":"cartel","x":540,"y":1330,"s":1.1,"texto":"CINEMA","z":1500},{"tipo":"neblina","x":540,"y":1800,"a":.14}]},
  {"k":"s_5","i":["#2a1d55","#120b2c","#030108"],"luz2":"255,215,140","props":[{"tipo":"barras2","x":540,"y":1650,"s":1.6,"a":[3.79,"GTA 6 · 1 DAY","#ff4081","3.79"],"b":[1.2,"MOVIE · 1 WEEKEND","#90a4ae","1.2"],"suf":" B"}]},
  {"k":"s_6","z":"nocheV","o":{"ciudad":True,"sem":41},"actores":[{**G,"keys":[{"k":"s_6","x":420,"pose":"piensa","cara":"sorpresa"}]}]},
  {"k":"s_7","z":"cuartoGamerV","o":{"era":2026},"actores":[{**G2P,"keys":[{"k":"s_7","x":420,"pose":"teclea","cara":"sorpresa"}]}]},
  {"k":"s_8","i":["#3b2a0a","#1c1405","#050301"],"luz2":"255,215,120","pedestal":True,"props":[{"tipo":"trofeo","x":540,"y":1330,"s":1.3}]}],
 numeros=[{"k":"m32","n":32,"suf":".5 M","c":"cian","etq":"COPIES BEFORE LAUNCH","fin":"s_3"},{"k":"m379","n":3,"pre":"$","suf":".79 B","c":"verde","etq":"DAY ONE SALES","fin":"s_4"},{"k":"m99","n":99,"c":"amar","etq":"METACRITIC","fin":"s_fin","y":760}],
 emojis=[{"k":"hollywood","e":"🤯"},{"k":"shock","e":"👀"},{"k":"speechless","e":"😶"}],
 gancho2=6,cierre="BEST GAME EVER?",cierre2="Tell me. Comment",paises=["YES","NO"],
 nota="GTA VI salió el 19-nov-2026 tras dos retrasos. Take-Two (20-nov-2026): 32,5 M de unidades antes del lanzamiento; US$3.790 M estimados en ventas del primer día, 'biggest entertainment launch in history'. Avengers: Endgame: US$1.209 mil M de estreno global (Disney, 5 días). Metacritic 99, mismo puntaje que Ocarina of Time (1998). Sin imágenes de la película ni de Zelda (solo texto). Guion aprobado por Tao 25-nov (línea base).",
 fuentes=["https://abcnews.com/GMA/Culture/grand-theft-auto-vi-breaks-1st-day-sales-record/story?id=138328412","https://thewaltdisneycompany.com/?p=15501","https://www.videogamer.com/news/gta-6-breaks-entertainment-record-day-one-sales/"])
