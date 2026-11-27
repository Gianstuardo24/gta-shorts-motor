"""GTA EN 14h · GTA 6 Was HIDING in Another Game · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 10 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen. Sin logos ni interfaces: el nombre va pintado en el casco."""
ID, LOTE, CANAL, HORA = "gtaen14", "LOTE_GTAEN14", "TheViceVerseGG", "14"
MARCA, TEMA = "THE VICEVERSE GG", None
TITULO = "GTA 6 Was HIDING in Another Game 🤫👀"
VOZ = ("am_michael", 1.3, "en-us")
F = ["GTA 6 was hiding in another game. And nobody saw it for years. But that's not even the strangest part.",
     "In 2018, Rockstar released Red Dead Redemption 2.",
     "This January, fans digging through its files found a boat texture nobody had seen.",
     "At first, it looked like just another unused file.",
     "Then they read the ship's name painted on it: The Leonida.",
     "Now the strangest part, the one no one talks about.",
     "What people didn't know was that Leonida is the state where GTA 6 takes place.",
     "And in 2018, nobody outside Rockstar knew that name. GTA 6 wasn't revealed until five years later.",
     "Some fans call it a planned tease. Others say it's a leftover. Rockstar hasn't said a word.",
     "Tell me which one you believe. Follow for more GTA 6 secrets."]
REEMPLAZOS = [("GTA 6", "GTA six"), ("In 2018,", "In twenty eighteen,"), ("in 2018,", "in twenty eighteen,"), ("Redemption 2.", "Redemption two.")]
PAUSAS = [1, 5, 6, 9]
CLAVES = {"x_and": (1, "And"), "x_but": (1, "But"), "x_2018": (2, "2018"), "x_dig": (3, "digging"), "x_found": (3, "found"), "x_tex": (3, "texture"),
          "x_read": (5, "read"), "x_the": (5, "The", 3), "s_6": ("L", 6), "x_leo7": (7, "Leonida"), "x_state": (7, "state"), "x_gta7": (7, "GTA"),
          "x_2018b": (8, "2018"), "x_nobody": (8, "nobody"), "x_knew": (8, "knew"), "x_wasnt": (8, "wasn't"), "x_five": (8, "five"),
          "x_planned": (9, "planned"), "x_others": (9, "Others"), "x_left": (9, "leftover"), "x_rock": (9, "Rockstar"), "x_tell": ("L", 10), "s_cta": (10, "Follow")}
PLANOS = [("01", "p01", None, "gancho: travelling paralelo junto al casco"),
          ("02", "p02", ("L", 2), "corte sobre el movimiento del barco: la escena fechada"),
          ("03", "p03", ("L", 3), "macro motivado por el farol"),
          ("04", "p04", ("L", 4), "detalle: la textura se gira y se lee el nombre"),
          ("05", "p05", ("L", 7), "corte por coincidencia de las letras al mapa"),
          ("06", "p06", ("L", 8), "el cofre y las hojas del calendario"),
          ("07a", "p07a", ("L", 9), "cenital de las dos fichas"),
          ("07b", "p07b", (9, "word", 0.25), "salida al barco y cierre")]
CIERRE = {"cierre": "PLANNED OR LEFTOVER?", "cierre2": "Your guess. Comment", "paises": ["PLANNED", "LEFTOVER"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
SFX = [("c02", -.28, "transicion/whoosh_02.wav", .28, .06), ("x_2018", -.05, "ui/pop_01.wav", None, .07),
       ("c03", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_found", 0, "ui/ding_01.wav", None, .05),
       ("x_read", 0, "transicion/whoosh_03.wav", .3, .05), ("x_the", -.45, "sintet/hoja.wav", None, .05),
       ("c05", -.05, "impacto/kick_01.wav", .16, .08), ("x_gta7", 0, "ui/pop_02.wav", None, .06),
       ("x_knew", 0, "ui/pop_03.wav", None, .07),
       ("x_wasnt", 0, "sintet/hoja.wav", None, .05), ("x_wasnt", .3, "sintet/hoja.wav", None, .05), ("x_wasnt", .6, "sintet/hoja.wav", None, .05), ("x_wasnt", .9, "sintet/hoja.wav", None, .05), ("x_five", 0, "sintet/hoja.wav", None, .05),
       ("x_five", .4, "ui/ding_01.wav", None, .06),
       ("x_planned", -.2, "sintet/hoja.wav", None, .05), ("x_left", -.2, "sintet/hoja.wav", None, .05),
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]
PORTADA = ("HIDING IN ANOTHER GAME", 1.0)
PUBLICAR = "Vie 27/11 14:00"
DESC = "Fans found it in old files. Rockstar hasn't said a word. 👀"
FIRMA = "Follow @TheViceVerseGG 🎮"
TAGS = "#GTA6 #Shorts #RockstarGames #GTAVI #Gaming"
PREVIA = [(1.0, "01 el barco"), (4.9, "01 junto al casco"), (7.6, "02 2018"), (11.4, "03 el farol"), (13.8, "03 la marca"), (16.2, "04 una textura más"), (18.5, "04 se gira"), (19.9, "04 The Leonida"),
          (22.8, "04 el nombre"), (23.5, "05 las mismas letras"), (27.3, "05 Leonida"), (29.0, "06 2018"), (31.3, "06 bajo llave"), (34.4, "06 cinco años después"), (37.9, "07 dos fichas"), (39.2, "07 sin veredicto"), (44.0, "07 cierre")]
