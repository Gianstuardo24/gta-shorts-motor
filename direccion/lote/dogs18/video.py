"""DOGS 18h · STOP Buying RED TOYS For Your Dog · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 2 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "dogs18", "LOTE_DOGS18", "DogDecoded", "18"
MARCA, TEMA = "THE DOGS DECODER", "mascotas"
TITULO = "STOP Buying RED TOYS For Your Dog 🐶🔴🚫"
VOZ = ("af_heart", 1.2, "en-us")
F = ["Stop buying red toys for your dog. At least until you see this. Careful, you might be wasting your money on the wrong colors.",
     "For years, people thought dogs saw the world in black and white.",
     "In 1989, scientist Jay Neitz showed that dogs do see color, just fewer than us.",
     "We have three types of color cells in our eyes. Dogs have only two.",
     "Specifically, blues and yellows. Reds look dark and muddy instead, almost brownish gray.",
     "Now the part almost nobody notices. And it's where your money goes to waste.",
     "Green grass looks dull to them too. So a red ball on the lawn almost blends in.",
     "That bright toy you paid for is hard for your dog to spot. That's why it may run right past it.",
     "So for games outside, pick blue or yellow. Those are the colors dogs see best.",
     "Tell me what color your dog's favorite toy is. Follow to decode your dog."]
REEMPLAZOS = [("In 1989,", "In nineteen eighty-nine,")]
PAUSAS = [1, 5, 6, 9]
CLAVES = {"x_see": (1, "see"), "x_wrong": (1, "wrong"), "x_black": (2, "black"), "x_sci": (3, "scientist"), "x_dogs3": (3, "dogs"), "x_color3": (3, "color"),
          "x_three": (4, "three"), "x_dogs4": (4, "Dogs"), "x_two": (4, "two"), "x_blues": (5, "blues"), "x_yellows": (5, "yellows"), "x_reds": (5, "Reds"), "x_muddy": (5, "muddy"),
          "x_dull": (7, "dull"), "x_red7": (7, "red"), "x_blends": (7, "blends"), "x_hard": (8, "hard"), "x_run": (8, "run"), "x_past": (8, "past"),
          "x_blue": (9, "blue"), "x_yellow": (9, "yellow"), "x_those": (9, "Those"), "x_tell": ("L", 10), "s_cta": (10, "Follow")}
PLANOS = [("01a", "p01a", None, "gancho, macro: la mano elige la pelota roja"),
          ("01b", "p01b", (1, "At", -0.04), "corte por coincidencia: la misma pelota en el pasto"),
          ("02", "p02", ("L", 2), "punto de vista del perro: la creencia antigua"),
          ("03", "p03", ("L", 3), "cenital: 1989 y la placa de prueba"),
          ("04", "p04", ("L", 4), "corte por el giro del disco: tres conos contra dos"),
          ("05", "p05", ("L", 5), "cámara fija: cambia la paleta"),
          ("06", "p06", ("L", 6), "plano bajo, a ras de pasto"),
          ("07", "p07", ("L", 8), "seguimiento lateral"),
          ("08", "p08", ("L", 9), "plano abierto con acercamiento suave")]
CIERRE = {"cierre": "WHAT COLOR IS IT?", "cierre2": "Tell me. Comment", "paises": ["RED", "BLUE", "YELLOW"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("x_see", -.05, "transicion/whoosh_04.wav", None, .06),        # 01: cambia la paleta
       ("c03", .1, "sintet/hoja.wav", None, .10),                      # 03: la hoja del calendario
       ("x_sci", .4, "impacto/kick_01.wav", .16, .05),                 # 03: se apoya la placa
       ("x_dogs3", -.03, "ui/pop_01.wav", None, .08), ("x_color3", -.2, "ui/pop_01.wav", None, .08),   # 03: se encienden los dos discos
       ("c04", .1, "ui/pop_03.wav", None, .07), ("x_three", .05, "ui/pop_03.wav", None, .07), ("x_three", .27, "ui/pop_03.wav", None, .07),   # 04: tres conos
       ("x_dogs4", 0, "ui/pop_02.wav", None, .07), ("x_two", -.06, "ui/pop_02.wav", None, .07),         # 04: dos conos
       ("x_muddy", -.08, "transicion/whoosh_04.wav", None, .06),       # 05: cambia la paleta
       ("x_dull", -.3, "transicion/whoosh_05.wav", None, .05), ("x_blends", -.45, "transicion/whoosh_05.wav", None, .05),   # 06: el pasto y después la pelota
       ("x_blue", .22, "impacto/kick_01.wav", .16, .05), ("x_yellow", .22, "impacto/kick_01.wav", .16, .05),   # 08: caen las pelotas
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("STOP BUYING RED TOYS", 1.0)
PUBLICAR = "Vie 27/11 18:00"
DESC = "There's a reason your dog keeps losing that ball. 🎾"
FIRMA = "🐶 The Dogs Decoder · Follow to decode your dog."
TAGS = "#Shorts #dogs #dogbehavior #doglover #dogfacts"
PREVIA = [(0.9, "01 elige la roja"), (1.9, "01 en el pasto"), (3.6, "01 como la ve el perro"), (9.3, "02 casi gris"), (13.4, "03 1989"), (18.1, "04 conos 3 y 2"), (20.6, "05"),
          (22.6, "05 cambia la paleta"), (26.5, "06 a ras de pasto"), (29.4, "06 el pasto"), (31.9, "06 la pelota"), (36.4, "07 pasa de largo"), (40.8, "08 elige"), (45.5, "08 cierre")]
