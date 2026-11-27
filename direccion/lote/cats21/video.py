"""CATS 21h · YOUR CAT SECRETLY SPEAKS TO YOU · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 4 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "cats21", "LOTE_CATS21", "CatDecoded", "21"
MARCA, TEMA = "THE CATS DECODER", "mascotas"
TITULO = "YOUR CAT SECRETLY SPEAKS TO YOU 🤫"
VOZ = ("bf_emma", 1.2, "en-gb")
F = ["Your cat secretly speaks to you. And it might explain more than you think. Careful, there might be other details you're missing.",
     "Kittens meow to call their mother.",
     "But adult cats rarely meow at each other. They use scent, body language, hisses and growls.",
     "Cats living without people are mostly quiet.",
     "The meow is something they mostly save for us.",
     "Now the detail you might be missing.",
     "Your cat learns which meows work on you: one for food, one for the door, one for attention.",
     "Meowing at people is partly something they learn.",
     "That's why the early morning meow works so well. It learned that one from you.",
     "So when your cat meows at you, it's talking to you on purpose. Answer back.",
     "Tell me what your cat's meow usually means. Follow to decode your cat."]
REEMPLAZOS = []
PAUSAS = [1, 5, 6, 10]
CLAVES = {"x_speaks": (1, "speaks"), "x_explain": (1, "explain"), "x_careful": (1, "Careful"), "x_youre": (1, "you're"),
          "x_meow2": (2, "meow"), "x_mother": (2, "mother"), "x_scent": (3, "scent"), "x_body": (3, "body"), "x_hisses": (3, "hisses"),
          "x_meow5": (5, "meow"), "x_save": (5, "save"), "x_meows7": (7, "meows"), "x_food": (7, "food"), "x_one2": (7, "one", 1), "x_door": (7, "door"),
          "x_one3": (7, "one", 2), "x_att": (7, "attention"), "x_learn": (8, "learn"), "x_meow9": (9, "meow"), "x_well": (9, "well"), "x_learned": (9, "learned"),
          "x_meows10": (10, "meows"), "x_talking": (10, "talking"), "x_answer": (10, "Answer"), "x_tell": ("L", 11), "s_cta": (11, "Follow")}
PLANOS = [("01", "p01", None, "gancho: el gato maúlla y la persona se detiene"),
          ("02", "p02", ("L", 2), "corte por el maullido: el gatito y su madre"),
          ("03", "p03", ("L", 3), "plano lateral continuo: dos adultos se cruzan"),
          ("04a", "p04a", ("L", 4), "el doméstico maúlla a la persona"),
          ("04b", "p04b", (4, "without", -0.04), "corte por posición de cabeza: afuera, sin personas"),
          ("04c", "p04c", ("L", 5), "corte por posición de cabeza: de vuelta en casa"),
          ("05", "p05", ("L", 6), "tres viñetas con el mismo encuadre del gato"),
          ("06", "p06", ("L", 8), "plano medio: repite el maullido que funcionó"),
          ("07", "p07", ("L", 9), "plano bajo junto a la cama, amanecer"),
          ("08", "p08", ("L", 10), "vuelve el encuadre del inicio, transformado")]
CIERRE = {"cierre": "WHAT DOES IT MEAN?", "cierre2": "Tell me. Comment", "paises": [], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. Los maullidos van sin sonido: la biblioteca no tiene un maullido y no se inventa uno.
SFX = [("c03", -0.28, "transicion/whoosh_02.wav", .28, .06),           # del nido al muro
       ("x_food", -.05, "ui/pop_03.wav", None, .06), ("x_food", .12, "ui/pop_03.wav", None, .06),   # 05: cae la comida
       ("x_door", -.1, "sintet/descuelga.wav", None, .10),             # 05: se abre la puerta
       ("x_learn", -.1, "ui/pop_03.wav", None, .06),                   # 06: cae la comida
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]         # cierre
PORTADA = ("SECRETLY SPEAKS TO YOU", 1.0)
PUBLICAR = "Vie 27/11 21:00"
DESC = "Other cats almost never hear it. 🤫\nSources: Live Science; Bradshaw, The Domestic Cat (Cambridge University Press)."
FIRMA = "🐱 The Cats Decoder · Follow to decode your cat."
TAGS = "#Shorts #cats #catbehavior #catlover #catfacts"
PREVIA = [(1.0, "01 gancho"), (5.9, "01 de cerca"), (6.5, "02 gatito y madre"), (10.8, "03 se huelen"), (11.7, "03 postura"), (13.0, "04 en casa"), (14.5, "04 sin personas"),
          (16.9, "04 para nosotros"), (21.95, "05 comida"), (22.85, "05 puerta"), (23.8, "05 atención"), (25.9, "06 repite"), (29.4, "07 amanecer"), (37.5, "08 cierre")]
NIVEL_FX = 1.0   # producido antes del cambio de nivel del 27-nov: se conserva el nivel con que se aprobó
