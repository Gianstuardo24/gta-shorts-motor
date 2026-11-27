"""COFFEE 17h · Why Coffee Makes You RUN to the Bathroom · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 5 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "coffee17", "LOTE_COFFEE17", "ChiChibitsTV", "17"
MARCA, TEMA = "COFFEE, BUT WHY?", "cafe"
TITULO = "Why Coffee Makes You RUN to the Bathroom 🚽😳"
VOZ = ("am_michael", 1.25, "en-us")
INCLUYE = ["coffee21/bloque.js"]          # piezas del canal: cocina, persona, taza, vapor
F = ["If coffee sends you running to the bathroom, it's not just the caffeine. And there's a detail almost nobody knows.",
     "It usually hits in the morning, right after that first cup.",
     "In 1990, researchers in the UK tested it.",
     "They placed pressure sensors in volunteers' lower gut, and gave them a cup of coffee.",
     "In people who felt the urge, the gut started moving within four minutes. And it kept going for at least half an hour.",
     "They also tested it with plain hot water and no coffee, to compare results. Surprisingly, nothing happened. So it wasn't about a warm drink.",
     "But here's the detail almost nobody knows, and it changes who this happens to.",
     "Decaf did it too. Less than regular coffee, but still more than water.",
     "That's because coffee triggers a gut hormone called gastrin, even without caffeine.",
     "Gastrin tells your gut to get moving. It's the same kind of signal your body sends after you eat.",
     "And it doesn't happen to everyone. Only about 3 in 10 people feel it, and women far more than men.",
     "So if it happens to you, it's your gut waking up.",
     "Tell me if coffee does this to you. Follow for one coffee curiosity a day."]
REEMPLAZOS = [("In 1990,", "In nineteen ninety,"), ("about 3 in 10 people", "about three in ten people")]
PAUSAS = [1, 6, 7, 12]
CLAVES = {"x_running": (1, "running"), "x_its": (1, "it's"), "x_and1": (1, "And"), "x_right2": (2, "right"), "x_first": (2, "first"),
          "x_res": (3, "researchers"), "x_tested": (3, "tested"), "x_sensors": (4, "sensors"), "x_gave": (4, "gave"),
          "x_moving": (5, "moving"), "x_four": (5, "four"), "x_and5": (5, "And"), "x_half": (5, "half"), "x_nothing": (6, "nothing"), "x_so6": (6, "So"),
          "x_decaf": (8, "Decaf"), "x_less": (8, "Less"), "x_water8": (8, "water"), "x_gastrin": (9, "gastrin"), "x_even": (9, "even"),
          "x_gastrin2": (10, "Gastrin"), "x_same": (10, "same"), "x_eat": (10, "eat"), "x_three": (11, "3"), "x_women": (11, "women"),
          "x_gut12": (12, "gut"), "x_tell": ("L", 13), "s_cta": (13, "Follow")}
PLANOS = [("01", "p01", None, "gancho: toma café y se levanta rápido"),
          ("02", "p02", ("L", 2), "la silla da paso a la mañana: detalle de taza y paneo al pasillo"),
          ("03a", "p03a", ("L", 3), "cenital: la mesa del experimento"),
          ("03b", "p03b", ("L", 4), "lateral: voluntario parcial con el sensor"),
          ("04", "p04", ("L", 5), "travelling a lo largo del tubo"),
          ("05a", "p05a", ("L", 6), "la taza de café"),
          ("05b", "p05b", (6, "plain", -0.04), "corte por coincidencia de taza a taza: agua caliente"),
          ("06", "p06", ("L", 7), "tres columnas, activación en secuencia"),
          ("07", "p07", ("L", 9), "macro de la ficha y travelling siguiendo la señal"),
          ("08", "p08", ("L", 11), "plano frontal de diez figuras"),
          ("09", "p09", ("L", 12), "regreso a la escena inicial")]
CIERRE = {"cierre": "DOES IT HAPPEN TO YOU?", "cierre2": "Tell me. Comment", "paises": ["YES", "NO"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("x_running", .05, "impacto/kick_01.wav", .16, .06),            # 01: apoya la taza
       ("x_its", .05, "transicion/whoosh_04.wav", None, .06),          # 01: se levanta y sale
       ("c03a", .1, "sintet/hoja.wav", None, .10),                     # 03: la hoja del calendario
       ("x_sensors", -.1, "ui/pop_01.wav", None, .08),                 # 03: se coloca el sensor
       ("x_four", -.05, "ui/ding_01.wav", .7, .04),                    # 04: el cronómetro marca 4
       ("x_nothing", .3, "ui/pop_02.wav", None, .06),                  # 05: el reloj termina y nada pasó
       ("c06", .12, "ui/pop_03.wav", None, .07), ("c06", .92, "ui/pop_03.wav", None, .07), ("c06", 1.72, "ui/pop_03.wav", None, .07),   # 06: entran las tres columnas
       ("x_gastrin", -.06, "ui/ding_01.wav", .8, .05),                 # 07: se enciende la ficha
       ("x_three", -.05, "ui/pop_01.wav", None, .08), ("x_three", .15, "ui/pop_01.wav", None, .08), ("x_three", .35, "ui/pop_01.wav", None, .08),   # 08: tres de diez
       ("x_gut12", -.15, "impacto/kick_01.wav", .16, .06),             # 09: apoya la taza
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("RUN TO THE BATHROOM", 1.0)
PUBLICAR = "Vie 27/11 17:00"
DESC = "It's not just the caffeine. ☕\nSources: Brown, Cann & Read (1990), Gut; McGill Office for Science and Society."
FIRMA = "☕ Coffee, But Why? · Follow for one coffee curiosity a day."
TAGS = "#Shorts #coffee #coffeelover #coffeefacts #morningcoffee"
PREVIA = [(0.5, "01 toma café"), (2.9, "01 se levanta"), (8.3, "02 primera taza"), (11.9, "03 la mesa, 1990"), (16.2, "03 sensor y taza"), (20.2, "04 cuatro minutos"), (22.7, "04 media hora"),
          (23.8, "05 café"), (28.6, "05 agua: nada"), (38.2, "06 tres columnas"), (42.7, "07 gastrin"), (47.9, "07 después de comer"), (52.8, "08 tres de diez"), (61.0, "09 cierre")]
