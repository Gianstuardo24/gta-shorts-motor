"""RABBIT 18h · Scientists CHASED This Signal for 17 YEARS 📡👽 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'srabbit18', 'LOTE28_SRABBIT18', 'TheRabbitLoop', '18'
MARCA, TEMA = 'THE RABBIT LOOP', "espacio"
TITULO = 'Scientists CHASED This Signal for 17 YEARS 📡👽'
VOZ = ('am_michael', 1.3, 'en-us')
F = ['Scientists chased this signal for 17 years. It looked like the mysterious bursts that come from deep space. Careful, the answer was closer than anyone imagined.',
     'In 1998, a giant radio telescope in Parkes, Australia, started picking up strange signals.',
     'Each one lasted just a few thousandths of a second.',
     'They looked a lot like fast radio bursts, real flashes that come from far outside our galaxy.',
     'But these had a problem. No other telescope in the world could see them.',
     'Now the answer that was closer than anyone imagined. And one clue was the time of day.',
     'The signals kept showing up around lunchtime.',
     'In 2015, a student named Emily Petroff and her team added a new sensor. It caught the signals at the same frequency a microwave oven uses.',
     'So they tested the microwave in the staff kitchen. Heating food normally did nothing.',
     'Then they opened the door before it finished. And the signal appeared.',
     "So for 17 years, the mystery wasn't in deep space. It was someone in a hurry to eat.",
     "Tell me if you'd have guessed the microwave. Follow for the next case."]
G2, N = 6, 12
REEMPLAZOS = []
PAUSAS = [1, 5, 6, 11]
CLAVES = {"x_tell": ("L", 12), "s_cta": (12, 'Follow')}
PLANOS = [("01", "p01", None, 'línea 1 · gancho'),
          ("02", "p02", ("L", 2), 'línea 2'),
          ("03", "p03", ("L", 3), 'línea 3'),
          ("04", "p04", ("L", 4), 'línea 4'),
          ("05", "p05", ("L", 5), 'línea 5'),
          ("06", "p06", ("L", 6), 'línea 6 · G2'),
          ("07", "p07", ("L", 7), 'línea 7'),
          ("08", "p08", ("L", 8), 'línea 8'),
          ("09", "p09", ("L", 9), 'línea 9'),
          ("10", "p10", ("L", 10), 'línea 10'),
          ("11", "p11", ("L", 11), 'línea 11'),
          ("12", "p12", ("L", 12), 'línea 12 · CTA')]
CIERRE = {'cierre': 'WHAT ABOUT YOU?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 18:00"
DESC = ""
FIRMA = '🐇 The Rabbit Teller · Follow @TheRabbitLoop: one story leads to another.'
TAGS = '#Shorts #TheRabbitLoop #UFO #aliens #mystery'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/TheRabbitLoop"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('17 years', 'seventeen years'), ('In 1998,', 'In nineteen ninety-eight,'), ('In 2015,', 'In twenty fifteen,')]
CLAVES.update({"x_17": (1, "17"), "x_bursts": (1, "bursts"), "x_careful": (1, "Careful,"), "x_closer": (1, "closer"), "x_parkes": (2, "Parkes,"), "x_strange": (2, "strange"),
               "x_frb": (4, "fast"), "x_real": (4, "real"), "x_outside": (4, "outside"), "x_noother": (5, "No"),
               "x_closer6": (6, "closer"), "x_clue": (6, "clue"), "x_time": (6, "time"), "x_lunch": (7, "lunchtime."),
               "x_emily": (8, "Emily"), "x_sensor": (8, "sensor."), "x_caught": (8, "caught"), "x_freq": (8, "frequency"), "x_microwave": (8, "microwave"),
               "x_tested": (9, "tested"), "x_nothing": (9, "nothing."), "x_opened": (10, "opened"), "x_appeared": (10, "appeared."),
               "x_wasnt": (11, "wasn't"), "x_hurry": (11, "hurry")})
CIERRE = {'cierre': 'WOULD YOU HAVE GUESSED?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO WAY'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("0", .85, "tao/alerta_suave.wav", None, .045), ("x_bursts", -.05, "tao/alerta_suave.wav", None, .04),   # 01: llega el pulso
       ("x_careful", -.35, "tao/whoosh_salto.wav", None, .04),        # 01: giro al receptor
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_strange", -.05, "tao/burbuja.wav", None, .04),             # 02: señales extrañas
       ("c03", .72, "tao/tic_rep.wav", None, .05), ("c03", 1.82, "tao/tic_rep.wav", None, .05),               # 03: el pulso aparece y se va
       ("x_real", -.1, "ui/ding_01.wav", .6, .035),                   # 04: destello lejano
       ("x_noother", -.05, "tao/desequipar.wav", None, .04),          # 05: los demás no ven nada
       ("x_clue", .2, "impacto/kick_01.wav", .25, .055),              # 06 · G2: el reloj
       ("x_lunch", -.2, "tao/clic_positivo.wav", None, .045),         # 07: la franja del almuerzo
       ("x_caught", -.3, "tao/toque_01.wav", None, .045),             # 08: corte al sensor
       ("x_microwave", -.3, "tao/equipar.wav", None, .05),            # 08: las frecuencias coinciden
       ("c09", .2, "tao/clic_06.wav", None, .04),                     # 09: se enciende el microondas
       ("x_opened", -.1, "sintet/descuelga.wav", None, .07),          # 10: abren la puerta
       ("x_opened", .5, "tao/whoosh_salto.wav", None, .04), ("x_opened", .72, "tao/alerta_suave.wav", None, .05),   # 10: giro al receptor y pulso
       ("x_wasnt", .35, "tao/toque_02.wav", None, .045),              # 11: corte por coincidencia
       ("c12", 1.3, "tao/fin_carga_01.wav", None, .045),              # 12: beep suave
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("17 YEARS CHASING A SIGNAL", 1.2)
DESC = "For 17 years, the mystery signal wasn't coming from deep space. 📡\nParkes radio telescope, Australia. Solved in 2015 by Emily Petroff and her team."
