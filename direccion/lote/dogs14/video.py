"""DOGS 14h · YOUR DOG KNOWS WHAT YOU'RE HIDING · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 1 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen."""
ID, LOTE, CANAL, HORA = "dogs14", "LOTE_DOGS14", "DogDecoded", "14"
MARCA, TEMA = "THE DOGS DECODER", "mascotas"
TITULO = "YOUR DOG KNOWS WHAT YOU'RE HIDING 👻"
VOZ = ("af_heart", 1.2, "en-us")
F = ["Your dog knows what you're hiding. Even when you act normal. But a study found something nobody tells you.",
     "You can smile and say you're fine.",
     "But in 2022, scientists in Belfast put four dogs to a test.",
     "They took breath and sweat from 36 people, twice. Once calm, and minutes later, right after a stressful math test.",
     "They only kept people whose heart rate and blood pressure went up. So the only difference between the two samples was stress.",
     "Now the part nobody tells you about.",
     "The dogs never saw those people. They only got the samples.",
     "And they picked the stressed one almost 94 percent of the time.",
     "When you get stressed, your body releases hormones like adrenaline and cortisol. That changes the chemicals in your breath and sweat, and gives you a particular smell. That's what your dog can smell.",
     "You can hide it from people, but not from your dog.",
     "Tell me if your dog notices your bad days. Follow to decode your dog."]
REEMPLAZOS = [("in 2022,", "in twenty twenty-two,"), ("36 people", "thirty-six people"), ("94 percent", "ninety-four percent")]
PAUSAS = [1, 5, 6, 10]
CLAVES = {"x_hiding": (1, "what"), "x_even": (1, "Even"), "x_but": (1, "But"), "x_nobody": (1, "nobody"), "x_fine": (2, "say"),
          "x_four": (3, "four"), "x_test": (3, "test", -0.1), "x_twice": (4, "twice"), "x_calm": (4, "Once"), "x_min": (4, "minutes"), "x_math": (4, "math"),
          "x_kept": (5, "kept"), "x_heart": (5, "heart"), "x_blood": (5, "blood"), "x_up": (5, "went"), "x_so": (5, "So"),
          "x_never": (7, "never"), "x_only7": (7, "only"), "x_samples": (7, "samples"), "x_picked": (8, "picked"),
          "x_body": (9, "your"), "x_that": (9, "That"), "x_gives": (9, "gives"), "x_part": (9, "particular"), "x_thats": (9, "That's"),
          "x_butnot": (10, "but"), "x_tell": ("L", 11), "s_cta": (11, "Follow")}
PLANOS = [("01", "p01", None, "gancho: la sonrisa en el espejo y la nariz del perro"),
          ("02", "p02", ("L", 2), "corte por la mirada del perro: la sonrisa de cerca"),
          ("03", "p03", ("L", 3), "cuatro perros frente a la trampilla cerrada"),
          ("04a", "p04a", ("L", 4), "interior, vista cenital: la muestra tranquila"),
          ("04b", "p04b", (4, "right", -0.04), "corte por coincidencia: el mismo gesto, minutos después"),
          ("05", "p05", ("L", 5), "las muestras en pares sobre la tira de medición"),
          ("06", "p06", ("L", 6), "la trampilla separa los dos lados"),
          ("07a", "p07a", ("L", 8), "la nariz frente a los tres frascos"),
          ("07b", "p07b", (8, "almost", -0.03), "corte cenital a la planilla de aciertos"),
          ("08", "p08", ("L", 9), "A y B a la altura del perro"),
          ("09", "p09", ("L", 10), "vuelve el encuadre del inicio, transformado")]
CIERRE = {"cierre": "DOES YOURS NOTICE?", "cierre2": "Yes or no? Comment", "paises": ["YES", "NO", "ALWAYS"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
# Efectos: solo acciones que se ven. (clave de tiempo, desfase, archivo, duración, ganancia). Sin sonidos de escritura.
SFX = [("c03", -0.28, "transicion/whoosh_02.wav", .28, .07),          # del espejo a la sala de la prueba
       ("x_test", .02, "sintet/descuelga.wav", None, .12),              # 03: se abre la trampilla
       ("x_calm", -.12, "ui/pop_01.wav", None, .10),                    # 04: la gasa cae en el frasco A
       ("x_min", -.2, "sintet/tics.wav", .86, .10),                     # 04: corre el reloj
       ("c04b", -.06, "ui/ding_01.wav", .7, .05),                       # 04: suena el reloj y entra el corte por coincidencia
       ("x_math", .12, "ui/pop_01.wav", None, .10),                     # 04: la gasa cae en el frasco B
       ("x_kept", .1, "impacto/kick_01.wav", .16, .05),                 # 05: baja el primer par que no cumple
       ("x_up", .16, "impacto/kick_01.wav", .16, .06),                  # 05: bajan los otros
       ("c06", .55, "sintet/descuelga.wav", None, .10),                 # 06: sube la puerta
       ("x_only7", -.1, "transicion/whoosh_01.wav", None, .06),         # 06: la bandeja cruza la trampilla
       ("x_picked", .46, "ui/ding_01.wav", .8, .05),                    # 07: se enciende la luz del frasco elegido
       ("c07b", .12, "ui/pop_03.wav", None, .08), ("c07b", .38, "ui/pop_03.wav", None, .08), ("c07b", .58, "ui/pop_02.wav", None, .09), ("c07b", .88, "ui/pop_03.wav", None, .08),  # 07: los sellos
       ("x_part", -.05, "transicion/pasada_larga_02.wav", 1.0, .05),    # 08: aparece el rastro
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]          # cierre
PORTADA = ("YOUR DOG KNOWS", 1.0)
PUBLICAR = "Vie 27/11 14:00"
DESC = "You can fake a smile. Not for your dog. 🐶"
FIRMA = "🐶 The Dogs Decoder · Follow to decode your dog."
TAGS = "#Shorts #dogs #dogbehavior #doglover #dogfacts"
PREVIA = [(0.5, "01 gancho"), (3.7, "01 primer plano"), (6.6, "02"), (10.85, "03"), (13.0, "04 muestra A"), (16.6, "04 muestra B"), (19.9, "05 tira"),
          (22.9, "05 par válido"), (24.9, "06 lado humano"), (28.6, "06 lado perro"), (30.4, "07 elige"), (31.9, "07 planilla"), (40.5, "08 rastro"), (47.8, "09 cierre")]
