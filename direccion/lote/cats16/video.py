"""CATS 16h · If You Have a CAT NEVER Throw THIS Away · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 3 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "cats16", "LOTE_CATS16", "CatDecoded", "16"
MARCA, TEMA = "THE CATS DECODER", "mascotas"
TITULO = "If You Have a CAT NEVER Throw THIS Away 🐱🚫"
VOZ = ("bf_emma", 1.2, "en-gb")
F = ["If you have a cat, never throw this away. Most people don't think twice about it, and it might be hurting yours.",
     "When cats feel stressed, their first move is to hide.",
     "In 2014, researchers in the Netherlands tested this with cats that had just arrived at a shelter.",
     "Half of them got something simple to hide in: a cardboard box. The other half got nothing.",
     "By day three, the cats with a box had already calmed down.",
     "Now the part that should worry you.",
     "The cats without a box to hide in needed about two weeks to reach that same state of calm.",
     "And in 2019, a second study found the same thing: cats with a box calmed down a week sooner.",
     "So if your cat is new or stressed, leave a box out. It costs nothing.",
     "Tell me the weirdest place your cat has squeezed into. Follow to decode your cat."]
REEMPLAZOS = [("In 2014,", "In twenty fourteen,"), ("in 2019,", "in twenty nineteen,")]
PAUSAS = [1, 5, 6, 9]
CLAVES = {"x_this": (1, "this"), "x_most": (1, "Most"), "x_and": (1, "and"), "x_hurt": (1, "hurting"), "x_hide": (2, "hide"),
          "x_res": (3, "researchers"), "x_tested": (3, "tested"), "x_cats3": (3, "cats"), "x_card": (4, "cardboard"), "x_other": (4, "other"),
          "x_already": (5, "already"), "x_without": (7, "without"), "x_two": (7, "two"), "x_reach": (7, "reach"),
          "x_second": (8, "second"), "x_cats8": (8, "cats"), "x_week": (8, "week"), "x_leave": (9, "leave"), "x_costs": (9, "costs"),
          "x_tell": ("L", 10), "s_cta": (10, "Follow")}
PLANOS = [("01", "p01", None, "gancho: la mano se lleva la caja y una pata la detiene"),
          ("02", "p02", ("L", 2), "corte al gato: recién llegado, busca dónde esconderse"),
          ("03", "p03", ("L", 3), "plano general simétrico: dos espacios iguales"),
          ("04", "p04", ("L", 4), "vista cenital: comparación en paralelo"),
          ("05a", "p05a", ("L", 5), "el calendario llega al día tres"),
          ("05b", "p05b", (5, "the", -0.04), "corte por coincidencia: de la hoja del calendario a la caja"),
          ("06", "p06", ("L", 6), "el otro lado, mismo encuadre"),
          ("07", "p07", ("L", 8), "segunda referencia: la misma comparación"),
          ("08", "p08", ("L", 9), "corte por coincidencia de la caja: la casa")]
CIERRE = {"cierre": "WEIRDEST SPOT?", "cierre2": "Tell me. Comment", "paises": ["BOX", "SINK", "BAG"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia)
SFX = [("x_and", .28, "impacto/kick_01.wav", .16, .07),               # 01: la pata detiene la caja
       ("c03", -0.28, "transicion/whoosh_02.wav", .28, .07),           # de la casa al refugio
       ("x_res", .55, "impacto/kick_01.wav", .16, .05),                # 03: se apoyan los transportines
       ("x_tested", -.02, "sintet/descuelga.wav", None, .10),          # 03: se abren las puertas
       ("x_card", .26, "impacto/kick_01.wav", .16, .06),               # 04: llega la caja
       ("c05a", .1, "sintet/hoja.wav", None, .12),                     # 05: se arranca la hoja
       ("x_without", -.2, "sintet/hoja.wav", None, .08), ("x_without", .25, "sintet/hoja.wav", None, .08), ("x_without", .7, "sintet/hoja.wav", None, .08), ("x_without", 1.15, "sintet/hoja.wav", None, .08),  # 06: corren las hojas
       ("x_week", -.1, "ui/pop_03.wav", None, .07), ("x_week", .08, "ui/pop_03.wav", None, .07), ("x_week", .25, "ui/pop_03.wav", None, .07), ("x_week", .42, "ui/pop_03.wav", None, .07),   # 07: una semana de hojas
       ("x_second", .3, "impacto/kick_01.wav", .16, .05),           # 07: llega la caja
       ("x_leave", .05, "impacto/kick_01.wav", .16, .05),              # 08: la mano deja la caja
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("NEVER THROW THIS AWAY", 1.0)
PUBLICAR = "Vie 27/11 16:00"
DESC = "Science says your cat might need it. 📦"
FIRMA = "🐱 The Cats Decoder · Follow to decode your cat."
TAGS = "#Shorts #cats #catbehavior #catlover #catfacts"
PREVIA = [(0.6, "01 gancho"), (4.6, "01 la pata"), (7.2, "02"), (12.6, "03"), (17.3, "04 cenital"), (18.95, "05 día tres"), (20.5, "05 sale"),
          (22.6, "06 mismo día"), (24.6, "06 corre"), (27.2, "06 dos semanas"), (29.3, "07 llega la caja"), (32.6, "07 una semana"), (35.2, "08 casa"), (40.5, "08 cierre")]
