"""DOGS 14h · Don't TRUST Your Dog's Tail Wag 🐶❓ · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'sdogs14', 'LOTE28_SDOGS14', 'DogDecoded', '14'
MARCA, TEMA = 'THE DOGS DECODER', "mascotas"
TITULO = "Don't TRUST Your Dog's Tail Wag 🐶❓"
VOZ = ('af_heart', 1.2, 'en-us')
F = ["Don't trust your dog's tail wag. Most people read it as happy, and they might be reading it wrong. But there's a detail almost nobody notices.",
     'In 2007, researchers in Italy filmed dogs while they looked at different things.',
     'Their owner. A stranger. A cat. And an unfamiliar, dominant dog.',
     "Every dog wagged. But the tail didn't swing evenly.",
     "With their owner, the wag leaned to the dog's right side.",
     'With the dominant dog, it leaned to the left.',
     'Now the detail almost nobody notices, the one other dogs read in a second.',
     'In 2013, the same team showed dogs videos of another dog wagging.',
     'When the wag leaned right, they stayed relaxed.',
     'When it leaned left, their heart rate went up and they looked anxious.',
     "That's because each side of the brain moves the opposite side of the tail. One side handles things to approach. The other, things to back away from.",
     "So a wag isn't always a happy wag. Watch which side it leans to.",
     "Tell me which way your dog's tail leans when you get home. Follow to decode your dog."]
G2, N = 7, 13
REEMPLAZOS = []
PAUSAS = [1, 6, 7, 12]
CLAVES = {"x_tell": ("L", 13), "s_cta": (13, 'Follow')}
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
          ("12", "p12", ("L", 12), 'línea 12'),
          ("13", "p13", ("L", 13), 'línea 13 · CTA')]
CIERRE = {'cierre': 'WHAT ABOUT YOU?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 14:00"
DESC = ""
FIRMA = '🐶 The Dogs Decoder · Follow to decode your dog.'
TAGS = '#Shorts #dogs #dogbehavior #doglover #dogfacts'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/DogDecoded"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('In 2007,', 'In two thousand seven,'), ('In 2013,', 'In twenty thirteen,')]
CLAVES.update({"x_happy": (1, "happy"), "x_wrong": (1, "wrong"), "x_detail": (1, "detail"), "x_filmed": (2, "filmed"),
               "x_stranger": (3, "stranger"), "x_cat": (3, "cat"), "x_dom": (3, "unfamiliar"), "x_but4": (4, "But"),
               "x_right5": (5, "right"), "x_left6": (6, "left"), "x_other": (7, "other"), "x_second": (7, "second"), "x_videos": (8, "videos"),
               "x_heart": (10, "heart"), "x_anx": (10, "anxious"), "x_opp": (11, "opposite"), "x_approach": (11, "approach"), "x_away": (11, "back"), "x_otra": (11, "other,"),
               "x_always": (12, "always"), "x_watch": (12, "Watch")})
CIERRE = {'cierre': 'LEFT OR RIGHT?', 'cierre2': 'Tell me. Comment', 'paises': ['LEFT', 'RIGHT'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
# Efectos: pocos, cortos y bajos (sonidos de Tao); solo acciones que se ven. (clave, desfase, archivo, duración, ganancia)
SFX = [("x_wrong", -.14, "tao/scratch.wav", None, .05),            # 01: la cola se congela
       ("x_detail", -.05, "tao/alerta_suave.wav", None, .05),       # 01: se marca el tramo de más
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),           # a la sala de observación
       ("x_filmed", .0, "tao/clic_06.wav", None, .06),              # 02: empieza a grabar
       ("c03", .04, "tao/toque_01.wav", None, .05), ("x_stranger", .0, "tao/toque_02.wav", None, .05), ("x_cat", .0, "tao/toque_01.wav", None, .05), ("x_dom", .0, "tao/toque_02.wav", None, .05),  # 03: entra cada estímulo
       ("x_right5", -.22, "tao/clic_positivo.wav", None, .05),      # 05: se marca la derecha
       ("x_left6", -.22, "tao/desequipar.wav", None, .05),          # 06: se marca la izquierda
       ("x_other", .02, "impacto/kick_01.wav", .2, .05),            # 07 · G2: la estela se congela
       ("x_videos", -.36, "tao/clic_05.wav", None, .06),            # 08: se enciende la pantalla
       ("x_heart", .0, "impacto/kick_01.wav", .12, .035), ("x_heart", .36, "impacto/kick_01.wav", .12, .035), ("x_heart", .66, "impacto/kick_01.wav", .12, .035), ("x_heart", .92, "impacto/kick_01.wav", .12, .035),  # 10: el pulso se acelera
       ("x_approach", -.3, "tao/clic_positivo.wav", None, .045), ("x_otra", -.05, "tao/desequipar.wav", None, .045),   # 11: cada mitad se enciende
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]         # cierre
PORTADA = ("DON'T TRUST THE WAG", 5.3)
DESC = "A wagging tail isn't always a happy tail. 🐶\nSource: University of Trento & University of Bari, Current Biology (2007, 2013)."
