"""RABBIT 18h · THE PENTAGON CONFIRMED THIS VIDEO IS REAL · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 8 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "rabbit18", "LOTE_RABBIT18", "TheRabbitLoop", "18"
MARCA, TEMA = "THE RABBIT LOOP", "espacio"
TITULO = "THE PENTAGON CONFIRMED THIS VIDEO IS REAL 🔺👽"
VOZ = ("am_michael", 1.3, "en-us")
F = ["The Pentagon confirmed this video is real. But wait until you hear the explanation. Careful, the detail at the end might surprise you.",
     "In 2019, sailors on a Navy warship filmed glowing triangles flying over the ship.",
     "The video leaked in 2021, and the Pentagon confirmed its own sailors shot it.",
     "Online, many people were sure it showed alien craft.",
     "In 2022, even a Navy intelligence official played it in front of the US Congress.",
     "But here's the catch with those triangles. They weren't what they looked like. In fact, those triangles were never really triangles.",
     "The shape came from the camera: light passing through night vision goggles turned into triangles.",
     "Any bright point of light, seen through that setup, can show up as a triangle.",
     "And the objects themselves, he said, were most likely drones.",
     "Tell me if that explanation is enough for you. Follow for the next case."]
REEMPLAZOS = [("In 2019,", "In twenty nineteen,"), ("in 2021,", "in twenty twenty-one,"), ("In 2022,", "In twenty twenty-two,")]
PAUSAS = [1, 5, 6, 9]
CLAVES = {"x_real": (1, "real"), "x_careful": (1, "Careful"), "x_sailors": (2, "sailors"), "x_filmed": (2, "filmed"), "x_2021": (3, "2021"), "x_conf3": (3, "confirmed"), "x_shot": (3, "shot"),
          "x_sure": (4, "sure"), "x_alien": (4, "alien"), "x_2022": (5, "2022"), "x_played": (5, "played"), "x_they": (6, "They"), "x_never": (6, "never"),
          "x_light": (7, "light"), "x_through": (7, "through"), "x_turned": (7, "turned"), "x_any": (8, "Any"), "x_seen": (8, "seen"), "x_tri8": (8, "triangle"),
          "x_objects": (9, "objects"), "x_most": (9, "most"), "x_tell": ("L", 10), "s_cta": (10, "Follow")}
PLANOS = [("01a", "p01a", None, "gancho: punto de vista dentro del visor"),
          ("01b", "p01b", (1, "But", -0.04), "corte al aparato"),
          ("02", "p02", ("L", 2), "plano general lateral: la cubierta"),
          ("03", "p03", ("L", 3), "detalle del documento"),
          ("04a", "p04a", ("L", 4), "montaje breve: en línea"),
          ("04b", "p04b", ("L", 5), "montaje breve: la pantalla de 2022"),
          ("05", "p05", ("L", 6), "pull-back motivado"),
          ("06", "p06", ("L", 7), "macro óptico"),
          ("07", "p07", ("L", 9), "transición por destello: plano amplio sobre el mar")]
CIERRE = {"cierre": "IS THAT ENOUGH?", "cierre2": "Yes or no? Comment", "paises": ["YES", "NO"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("x_real", -.02, "tematicos/obturador_01.wav", None, .10),      # 01: la imagen se congela
       ("c02", -0.28, "transicion/whoosh_02.wav", .28, .06),           # a la cubierta
       ("x_conf3", -.06, "impacto/kick_01.wav", .16, .08),             # 03: el sello
       ("c04a", .3, "ui/pop_03.wav", None, .06), ("c04a", .6, "ui/pop_03.wav", None, .06), ("c04a", .9, "ui/pop_03.wav", None, .06),   # 04: los comentarios
       ("x_they", -.1, "transicion/whoosh_02.wav", .28, .05),         # 05: la cámara se aparta
       ("x_turned", -.05, "ui/pop_01.wav", None, .08), ("x_seen", .4, "ui/pop_01.wav", None, .07), ("x_tri8", -.3, "ui/pop_01.wav", None, .07),   # 06: cada punto sale como triángulo
       ("c07", -.25, "transicion/whoosh_02.wav", .28, .06),            # destello hacia el mar
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("CONFIRMED REAL", 1.0)
PUBLICAR = "Vie 27/11 18:00"
DESC = "Navy footage. Confirmed real. The triangles are another story. 👀\nSources: Pentagon UFO videos (Wikipedia); Reuters, May 17 2022 hearing. Animation is an illustration."
FIRMA = "🐇 The Rabbit Teller · Follow @TheRabbitLoop: one story leads to another."
TAGS = "#Shorts #TheRabbitLoop #aliens #UFO #Pentagon"
PREVIA = [(1.0, "01 dentro del visor"), (2.1, "01 se congela"), (5.6, "01 el aparato"), (10.6, "02 cubierta"), (15.6, "03 documento"), (18.6, "04 en línea"), (23.4, "04 pantalla 2022"),
          (26.2, "05 dentro"), (30.2, "05 afuera: puntos"), (35.9, "06 punto a triángulo"), (39.9, "06 cualquier punto"), (41.0, "07 visor"), (43.3, "07 probable dron"), (47.6, "07 cierre")]
NIVEL_FX = 1.0   # producido antes del cambio de nivel del 27-nov: se conserva el nivel con que se aprobó
