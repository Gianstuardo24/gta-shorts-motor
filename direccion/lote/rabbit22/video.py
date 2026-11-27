"""RABBIT 22h · Don't TRUST the Flying Saucer Story · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 9 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "rabbit22", "LOTE_RABBIT22", "TheRabbitLoop", "22"
MARCA, TEMA = "THE RABBIT LOOP", "espacio"
TITULO = "Don't TRUST the Flying Saucer Story 🛸❓"
VOZ = ("am_michael", 1.3, "en-us")
F = ["Don't trust the flying saucer story. Everyone has heard it, but few know how it started. And the real story might surprise you.",
     "In June 1947, pilot Kenneth Arnold saw nine shiny objects near Mount Rainier.",
     "They were fast. Faster, he said, than any plane of his time.",
     "He said they moved like a saucer skipping across water.",
     "He was describing how they moved. Not their shape.",
     "But the papers ran it as flying saucers, and the name stuck.",
     "Now watch what one headline did to an entire country.",
     "Within weeks, hundreds of people across the US reported flying saucers.",
     "Many described round discs. The shape from the headline, not the one Arnold saw.",
     "Arnold's own drawing showed something flat and crescent shaped, almost like a boomerang. Not a round plate.",
     "So the classic flying saucer we all picture started as a headline. Not as something someone actually saw, like many people think.",
     "Tell me if you knew where the name came from. Follow for the next case."]
REEMPLAZOS = [("In June 1947,", "In June nineteen forty-seven,")]
PAUSAS = [1, 6, 7, 11]
CLAVES = {"x_few": (1, "few"), "c01b": ("L", 2), "x_nine": (2, "nine"), "x_faster": (3, "Faster"), "x_saucer": (4, "saucer"), "x_not": (5, "Not"),
          "x_stuck": (6, "stuck"), "x_one": (7, "one"), "x_within": (8, "Within"), "x_shape": (9, "shape"), "x_notone": (9, "not"),
          "x_something": (10, "something"), "x_boom": (10, "boomerang"), "x_notround": (10, "Not"), "x_so11": (11, "So"), "x_headline11": (11, "headline"), "x_not11": (11, "Not"),
          "x_tell": ("L", 12), "s_cta": (12, "Follow")}
PLANOS = [("01", "p01", None, "gancho y línea 2: punto de vista desde la cabina"),
          ("02a", "p02a", ("L", 3), "las estelas; la trayectoria se congela"),
          ("02b", "p02b", ("L", 4), "corte por coincidencia de la estela al rebote"),
          ("03", "p03", ("L", 5), "cenital: las ondas se apagan"),
          ("04a", "p04a", ("L", 6), "macro de papel: el teletipo"),
          ("04b", "p04b", (6, "saucers", -0.04), "golpe de prensa"),
          ("05", "p05", ("L", 7), "plano abierto; acumulación"),
          ("06", "p06", ("L", 9), "primer plano con giro corto"),
          ("07", "p07", ("L", 10), "cenital de lápiz y papel")]
CIERRE = {"cierre": "DID YOU KNOW?", "cierre2": "Yes or no? Comment", "paises": ["YES", "NO"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("x_few", .15, "sintet/tics.wav", 1.2, .08),                    # 01: arranca el reloj
       ("c02a", .1, "transicion/whoosh_01.wav", None, .06), ("c02a", 1.35, "transicion/whoosh_01.wav", None, .06),   # 02: pasan las estelas
       ("x_saucer", .11, "ui/pop_01.wav", None, .07), ("x_saucer", .49, "ui/pop_01.wav", None, .07), ("x_saucer", .87, "ui/pop_01.wav", None, .07), ("x_saucer", 1.25, "ui/pop_01.wav", None, .07),   # 02: los rebotes
       ("c04a", .25, "sintet/teclas.wav", .8, .10),                    # 04: escribe el teletipo
       ("c04b", .16, "impacto/kick_01.wav", .18, .09),                 # 04: golpe de prensa
       ("x_one", .25, "impacto/kick_01.wav", .16, .04), ("x_one", .95, "impacto/kick_01.wav", .16, .04),   # 05: caen los diarios
       ("x_shape", -.2, "sintet/hoja.wav", None, .08),                 # 06: el papel gira
       ("x_notround", 0, "sintet/hoja.wav", None, .10),                # 07: se desprende el círculo
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("DON'T TRUST THE STORY", 1.0)
PUBLICAR = "Vie 27/11 22:00"
DESC = "He never said what the papers printed. 📰\nSources: Kenneth Arnold UFO sighting and Flying saucer (Wikipedia); TIME; Space.com. Animation is an illustration."
FIRMA = "🐇 The Rabbit Teller · Follow @TheRabbitLoop: one story leads to another."
TAGS = "#Shorts #TheRabbitLoop #UFO #aliens #flyingsaucer"
PREVIA = [(3.9, "01 cabina"), (10.0, "01 nueve destellos"), (13.0, "02 rápidos"), (15.5, "02 la trayectoria"), (17.6, "02 rebota"), (20.3, "03 se hunde"), (22.8, "04 teletipo"),
          (24.2, "04 titular"), (27.0, "05 porche"), (31.6, "05 todo el país"), (34.0, "06 es papel"), (40.2, "07 el dibujo"), (44.5, "07 un titular"), (52.5, "07 cierre")]
