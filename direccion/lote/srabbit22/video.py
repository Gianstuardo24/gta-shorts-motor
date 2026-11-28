"""RABBIT 22h · Your BRAIN Is LYING About This Mars Photo 🗿🤥 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'srabbit22', 'LOTE28_SRABBIT22', 'TheRabbitLoop', '22'
MARCA, TEMA = 'THE RABBIT LOOP', "espacio"
TITULO = 'Your BRAIN Is LYING About This Mars Photo 🗿🤥'
VOZ = ('am_michael', 1.3, 'en-us')
F = ['Your brain is lying about this Mars photo. NASA took it in 1976 and people everywhere saw the same thing. What few people know is that NASA itself helped start the story.',
     'In July 1976, the Viking 1 spacecraft was circling Mars, looking for a landing site.',
     'One photo showed a hill more than a mile long. With two eyes, a nose and a mouth.',
     'Many people saw a giant face staring up from Mars.',
     'And some became convinced that someone had built it.',
     'Now the part few people know: how NASA itself helped start the story.',
     "NASA's scientists believed it was just a hill with strange shadows.",
     'But when NASA released the photo, its own note said the hill resembled a human head.',
     'That was enough. The face on Mars became famous.',
     'In 1998, a new spacecraft shot it again, ten times sharper. And in 2001, sharper still.',
     'The face was gone. It was a rocky hill, like many others around it.',
     "So nobody built a face. Your brain did. It's wired to find faces, even in rocks and shadows.",
     "Tell me the strangest place you've seen a face. Follow for the next case."]
G2, N = 6, 13
REEMPLAZOS = []
PAUSAS = [1, 5, 6, 12]
CLAVES = {"x_tell": ("L", 13), "s_cta": (13, 'Follow')}
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
          ("12", "p12", ("L", 12), 'línea 12'),
          ("13", "p13", ("L", 13), 'línea 13 · CTA')]
CIERRE = {'cierre': 'WHAT ABOUT YOU?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 22:00"
DESC = ""
FIRMA = '🐇 The Rabbit Teller · Follow @TheRabbitLoop: one story leads to another.'
TAGS = '#Shorts #TheRabbitLoop #UFO #aliens #mystery'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/TheRabbitLoop"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('in 1976', 'in nineteen seventy-six'), ('In July 1976,', 'In July nineteen seventy-six,'), ('In 1998,', 'In nineteen ninety-eight,'), ('in 2001,', 'in two thousand one,')]
CLAVES.update({"x_lying": (1, "lying"), "x_1976": (1, "1976"), "x_everywhere": (1, "everywhere"), "x_few": (1, "few"), "x_nasa": (1, "itself"),
               "x_viking": (2, "Viking"), "x_landing": (2, "landing"), "x_mile": (3, "mile"), "x_eyes": (3, "eyes,"), "x_nose": (3, "nose"), "x_mouth": (3, "mouth."),
               "x_built": (5, "built"), "x_itself": (6, "itself"), "x_story": (6, "story."), "x_hill": (7, "hill"), "x_shadows": (7, "shadows."),
               "x_released": (8, "released"), "x_note": (8, "note"), "x_head": (8, "head."), "x_famous": (9, "famous."),
               "x_1998": (10, "1998,"), "x_sharper": (10, "sharper."), "x_2001": (10, "2001,"), "x_still": (10, "still."),
               "x_gone": (11, "gone."), "x_others": (11, "others"), "x_brain": (12, "brain"), "x_wired": (12, "wired"), "x_rocks": (12, "rocks")})
CIERRE = {'cierre': 'WHERE DID YOU SEE ONE?', 'cierre2': 'Tell me. Comment', 'paises': ['CLOUDS', 'A WALL', 'MY FOOD'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_lying", .4, "tao/alerta_suave.wav", None, .04),            # 01: cambia la luz y el rostro se deshace
       ("x_1976", -.15, "tao/clic_08.wav", None, .05),                # 01: la foto
       ("x_everywhere", -.2, "sintet/hoja.wav", .6, .045),            # 01: se multiplica
       ("x_few", -.2, "sintet/hoja.wav", .5, .04),                    # 01: entra la nota
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_landing", -.5, "sintet/baja.wav", .8, .04),                # 02: baja al terreno
       ("x_eyes", -.05, "tao/toque_01.wav", None, .045), ("x_nose", -.05, "tao/toque_02.wav", None, .045), ("x_mouth", -.05, "tao/toque_01.wav", None, .045),   # 03: ojos, nariz, boca
       ("c05", .25, "tao/equipar.wav", None, .045),                   # 05: la figura tallada se superpone
       ("x_itself", .0, "impacto/kick_01.wav", .25, .055),            # 06 · G2: la nota
       ("x_shadows", -.6, "tao/clic_06.wav", None, .045),             # 07: mueven la luz
       ("x_head", -.9, "tao/clic_positivo.wav", None, .045),          # 08: la frase de la nota
       ("x_famous", -.3, "ui/ding_01.wav", .6, .035),                 # 09: se hace famosa
       ("x_1998", .55, "tao/toque_02.wav", None, .05), ("x_2001", .55, "tao/toque_01.wav", None, .05),          # 10: cortes por coincidencia
       ("x_wired", -.3, "tao/alerta_suave.wav", None, .04),           # 12: aparecen los rasgos
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("YOUR BRAIN IS LYING", 0.6)
DESC = "Nobody built a face on Mars. Your brain did. 🗿\nViking 1, July 1976. Sharper photos in 1998 and 2001 showed a rocky hill."
