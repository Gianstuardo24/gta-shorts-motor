"""GTA EN 19h · This PARROT Knows Where the MONEY Is 🦜💰 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'sgtaen19', 'LOTE28_SGTAEN19', 'TheViceVerseGG', '19'
MARCA, TEMA = 'THE VICEVERSE GG', None
TITULO = 'This PARROT Knows Where the MONEY Is 🦜💰'
VOZ = ('am_michael', 1.3, 'en-us')
F = ["This parrot knows where the money is. Lots of players walk past it and miss the cash. But there's more hidden there than the parrot tells you.",
     "It's right at the start of the game, in Key Lento.",
     'Your neighbor Shirley sends you to buy rum at a store called Three Sheets Liquor.',
     'Lots of players grab the bottle and leave.',
     'But listen. You can hear animals somewhere in the back.',
     "Behind the store, there's a hidden yard full of smuggled exotic animals. And a few guys guarding it.",
     "Now the part the parrot doesn't tell you, and it's where the rest of the cash is.",
     "In one cage, there's a red parrot. Ask it about the cash, and it tells you to check the generator.",
     "Look at the wall vent right next to it. Inside, there's about 1,300 dollars.",
     "But don't leave yet. The back room has a safe and a money counter, with even more.",
     'So one talking parrot can hand you over 2,000 dollars before the story even gets going.',
     'Tell me if you found the parrot on your own. Follow for more GTA 6 secrets.']
G2, N = 7, 12
REEMPLAZOS = []
PAUSAS = [1, 6, 7, 11]
CLAVES = {"x_tell": ("L", 12), "s_cta": (12, 'Follow')}
PLANOS = [("01", "p01", None, 'línea 1 · gancho'),
          ("02", "p02", ("L", 2), 'línea 2'),
          ("03", "p03", ("L", 3), 'línea 3'),
          ("04", "p04", ("L", 4), 'línea 4'),
          ("05", "p05", ("L", 5), 'línea 5'),
          ("06", "p06", ("L", 6), 'línea 6'),
          ("07", "p07", ("L", 7), 'línea 7 · G2'),
          ("08", "p08", ("L", 8), 'línea 8'),
          ("09", "p09", ("L", 9), 'línea 9'),
          ("10", "p10", ("L", 10), 'línea 10'),
          ("11", "p11", ("L", 11), 'línea 11'),
          ("12", "p12", ("L", 12), 'línea 12 · CTA')]
CIERRE = {'cierre': 'WHAT ABOUT YOU?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 19:00"
DESC = ""
FIRMA = 'Follow @TheViceVerseGG 🎮'
TAGS = '#GTA6 #Shorts #RockstarGames #GTAVI #Gaming'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/TheViceVerseGG"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('GTA 6', 'GTA six'), ('1,300 dollars', 'thirteen hundred dollars'), ('2,000 dollars', 'two thousand dollars')]
CLAVES.update({"x_money": (1, "money"), "x_walk": (1, "walk"), "x_cash1": (1, "cash."), "x_more": (1, "more"), "x_key": (2, "Key"),
               "x_rum": (3, "rum"), "x_three": (3, "Three"), "x_grab": (4, "grab"), "x_leave": (4, "leave."), "x_hear": (5, "hear"), "x_back": (5, "back."),
               "x_yard": (6, "yard"), "x_animals": (6, "animals."), "x_guys": (6, "guys"), "x_tell7": (7, "tell"), "x_rest": (7, "rest"),
               "x_ask": (8, "Ask"), "x_tells": (8, "tells"), "x_gen": (8, "generator."), "x_vent": (9, "vent"), "x_inside": (9, "Inside,"), "x_1300": (9, "1,300"),
               "x_room": (10, "room"), "x_safe": (10, "safe"), "x_counter": (10, "counter,"), "x_even": (10, "even"), "x_hand": (11, "hand"), "x_2000": (11, "2,000")})
CIERRE = {'cierre': 'FOUND THE PARROT?', 'cierre2': 'On your own? Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_money", -.45, "tao/toque_01.wav", None, .045),              # 01: el loro inclina la cabeza
       ("x_cash1", -.2, "tao/moneda.wav", None, .05),                  # 01: cae la moneda
       ("x_more", -.05, "tao/alerta_suave.wav", None, .035),           # 01: la rejilla avisa
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_key", -.1, "tao/clic_05.wav", None, .045),                  # 02: Key Lento
       ("c03", .5, "tao/burbuja.wav", None, .045),                    # 03: el encargo
       ("x_three", -.15, "tao/clic_positivo.wav", None, .045),         # 03: se enciende el letrero
       ("x_grab", -.1, "tao/equipar.wav", None, .05),                  # 04: toma la botella
       ("x_hear", -.2, "sintet/aletas.wav", .9, .05),                  # 05: sonido guía detrás de la puerta
       ("c06", .05, "tao/whoosh_salto.wav", None, .04),                # 06: se abre al patio
       ("x_guys", -.3, "tao/toque_02.wav", None, .045),                # 06: los guardias
       ("x_tell7", .0, "impacto/kick_01.wav", .25, .055),              # 07 · G2
       ("x_rest", -.3, "tao/clic_06.wav", None, .045),                 # 07: cambio de foco al generador
       ("x_ask", -.1, "tao/burbuja.wav", None, .045), ("x_tells", .0, "tao/pop_burbuja.wav", None, .045),   # 08: pregunta y respuesta (íconos)
       ("x_gen", -.3, "tao/clic_05b.wav", None, .045),                 # 08: el generador
       ("x_inside", -.35, "tao/desequipar.wav", None, .05),            # 09: sale la tapa de la rejilla
       ("x_1300", -.1, "tao/compra.wav", None, .045),                  # 09: la cifra
       ("x_safe", -.05, "tao/tic_rueda.wav", None, .045),              # 10: la caja fuerte
       ("x_counter", -.1, "sintet/billetes.wav", 1.0, .04),            # 10: el contador de billetes
       ("x_hand", -.2, "tao/whoosh_carril.wav", None, .035),           # 11: se junta el dinero
       ("x_2000", -.1, "tao/logro.wav", None, .045),                   # 11: el total
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("THIS PARROT KNOWS", 1.0)
DESC = "A talking parrot in GTA 6 tells you where the cash is. 🦜\nBehind Three Sheets Liquor in Key Lento: check the wall vent next to the generator."
