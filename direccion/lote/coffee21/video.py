"""COFFEE 21h · NEVER Use Boiling Water for Your Coffee · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 6 del lote (27-nov). Las etiquetas "G2:" y "CTA:" y la nota entre paréntesis de la línea 4 no se dicen."""
ID, LOTE, CANAL, HORA = "coffee21", "LOTE_COFFEE21", "ChiChibitsTV", "21"
MARCA, TEMA = "COFFEE, BUT WHY?", "cafe"
TITULO = "NEVER Use Boiling Water for Your Coffee ☕🚫"
VOZ = ("am_michael", 1.25, "en-us")
F = ["Never use boiling water for your coffee. Lots of people do it every morning, but it might be ruining every cup. And the solution might surprise you.",
     "Boiling water feels like the right choice. Hotter water, stronger coffee.",
     "But the National Coffee Association recommends water just below boiling.",
     "Between 195 and 205 degrees Fahrenheit. Water boils at 212.",
     "Hotter than that can pull too much out of the coffee. That's when it turns bitter and harsh.",
     "Now the part almost nobody does right. There's a simple fix that could save every cup, and it takes just 30 seconds.",
     "You don't need a thermometer, or a fancy kettle.",
     "And you don't need to buy more expensive coffee either.",
     "Just let the water boil, then wait about 30 seconds before you pour.",
     "That small wait brings it down to the right range.",
     "But don't wait too long. Below that range, coffee can taste weak and sour.",
     "Tell me if your coffee usually tastes bitter. Follow for one coffee curiosity a day."]
REEMPLAZOS = [("Between 195 and 205 degrees", "Between one ninety-five and two oh five degrees"), ("boils at 212.", "boils at two twelve."), ("just 30 seconds", "just thirty seconds"), ("about 30 seconds", "about thirty seconds")]
PAUSAS = [1, 5, 6, 11]
CLAVES = {"x_morning": (1, "morning"), "x_ruin": (1, "ruining"), "x_every2": (1, "every", 1), "x_and1": (1, "And"), "x_hotter": (2, "Hotter"), "x_stronger": (2, "stronger"),
          "x_nat": (3, "National"), "x_rec": (3, "recommends"), "x_195": (4, "195"), "x_205": (4, "205"), "x_fahr": (4, "Fahrenheit"), "x_water4": (4, "Water"), "x_212": (4, "212"),
          "x_pull": (5, "pull"), "x_thats": (5, "That's"), "x_bitter5": (5, "bitter"), "x_fix": (6, "simple"), "x_30a": (6, "30"),
          "x_thermo": (7, "thermometer"), "x_fancy": (7, "fancy"), "x_exp": (8, "expensive"), "x_boil9": (9, "boil"), "x_wait9": (9, "wait"), "x_before": (9, "before"),
          "x_right": (10, "right"), "x_dont": (11, "don't"), "x_below": (11, "Below"), "x_weak": (11, "weak"), "x_tell": (12, "usually", -0.1), "s_cta": (12, "Follow")}
PLANOS = [("01a", "p01a", None, "gancho, macro del vertido"),
          ("01b", "p01b", (1, "Lots", -0.04), "corte a la reacción parcial"),
          ("02", "p02", ("L", 2), "plano lateral siguiendo la mano"),
          ("03", "p03", ("L", 3), "cenital limpio: tarjeta y termómetro"),
          ("04", "p04", ("L", 5), "macro lateral"),
          ("05", "p05", ("L", 6), "plano fijo: se apaga el hervidor"),
          ("06", "p06", ("L", 7), "cenital: las manos despejan la mesa"),
          ("07", "p07", ("L", 9), "detalle siguiendo el vertido"),
          ("08a", "p08a", ("L", 10), "el termómetro en el rango"),
          ("08b", "p08b", ("L", 11), "comparación lado a lado"),
          ("09", "p09", ("L", 12), "plano medio; cierre en la taza")]
CIERRE = {"cierre": "IS YOURS BITTER?", "cierre2": "Yes or no? Comment", "paises": ["YES", "NO"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("x_hotter", -.1, "sintet/descuelga.wav", None, .10),           # 02: gira la perilla
       ("c03", -0.28, "transicion/whoosh_02.wav", .28, .06),           # a la vista cenital
       ("x_195", -.06, "ui/pop_01.wav", None, .08), ("x_205", -.06, "ui/pop_01.wav", None, .08),   # 03: los números de la tarjeta
       ("x_212", .1, "ui/ding_01.wav", .7, .04),                       # 03: la aguja llega al hervor
       ("x_bitter5", .1, "transicion/whoosh_04.wav", None, .06),       # 04: aparta la jarra
       ("x_fix", .12, "sintet/descuelga.wav", None, .10),              # 05: apaga el fuego
       ("x_30a", -.2, "impacto/kick_01.wav", .16, .05),                # 05: apoya el reloj
       ("x_thermo", .15, "transicion/whoosh_05.wav", None, .05), ("x_fancy", .15, "transicion/whoosh_05.wav", None, .05), ("x_exp", .15, "transicion/whoosh_05.wav", None, .05),   # 06: despeja la mesa
       ("x_wait9", -.1, "sintet/tics.wav", 1.1, .09),                  # 07: corre el reloj
       ("x_weak", 0, "transicion/whoosh_04.wav", None, .06),           # 08: aparta la taza pálida
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("NEVER USE BOILING WATER", 1.0)
PUBLICAR = "Vie 27/11 21:00"
DESC = "Thirty seconds can change your whole cup. ☕\nSource: National Coffee Association."
FIRMA = "☕ Coffee, But Why? · Follow for one coffee curiosity a day."
TAGS = "#Shorts #coffee #coffeelover #coffeefacts #morningcoffee"
PREVIA = [(1.2, "01 vertido"), (4.6, "01 prueba"), (5.7, "01 mueca"), (11.4, "02 sube el fuego"), (19.4, "03 tarjeta"), (21.0, "03 hierve a 212"), (23.6, "04 saca de más"),
          (31.9, "05 se apaga y 30"), (34.0, "06 despeja"), (37.4, "06 queda lo simple"), (40.0, "07 espera"), (41.3, "07 vierte"), (43.6, "08 en el rango"), (46.6, "08 pálida")]
NIVEL_FX = 1.0   # producido antes del cambio de nivel del 27-nov: se conserva el nivel con que se aprobó
