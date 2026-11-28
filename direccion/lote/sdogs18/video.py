"""DOGS 18h · NEVER Pet Another Dog in Front of YOURS 🐶🚫 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'sdogs18', 'LOTE28_SDOGS18', 'DogDecoded', '18'
MARCA, TEMA = 'THE DOGS DECODER', "mascotas"
TITULO = 'NEVER Pet Another Dog in Front of YOURS 🐶🚫'
VOZ = ('af_heart', 1.2, 'en-us')
F = ["Never pet another dog in front of yours. It looks harmless, but your dog might take it personally. Careful, a simple test showed how far they'll go.",
     'In 2014, scientists at the University of California visited 36 dogs at home.',
     'They asked each owner to ignore their dog and pet a stuffed dog instead. One that barked, whined and wagged its tail.',
     'Then they did the same with a plastic pumpkin, and with a book read out loud.',
     'With the book, only about 2 in 10 dogs pushed or touched their owner.',
     'With the fake dog, it was almost 8 in 10.',
     'Now the part that should worry you, because some dogs went further than pushing.',
     'About a third squeezed in between their owner and the fake dog.',
     'And some even snapped at it.',
     'The test was borrowed from one used with six-month-old babies.',
     'The scientists said the dogs seemed to be protecting their bond with their owner.',
     "So to your dog, it might not be just a pat. It's someone taking their place.",
     'Tell me what your dog does when you pet another dog. Follow to decode your dog.']
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
PUBLICAR = "Sáb 28/11 18:00"
DESC = ""
FIRMA = '🐶 The Dogs Decoder · Follow to decode your dog.'
TAGS = '#Shorts #dogs #dogbehavior #doglover #dogfacts'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/DogDecoded"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('In 2014,', 'In twenty fourteen,'), ('36 dogs', 'thirty-six dogs'), ('2 in 10', 'two in ten'), ('8 in 10', 'eight in ten')]
CLAVES.update({"x_harmless": (1, "harmless"), "x_personally": (1, "personally"), "x_careful": (1, "Careful"), "x_36": (2, "36"),
               "x_stuffed": (3, "stuffed"), "x_barked": (3, "barked"), "x_wagged": (3, "wagged"), "x_pumpkin": (4, "pumpkin"), "x_book": (4, "book"),
               "x_2": (5, "2"), "x_8": (6, "8"), "x_worry": (7, "worry"), "x_further": (7, "further"), "x_squeezed": (8, "squeezed"),
               "x_snapped": (9, "snapped"), "x_six": (10, "six-month-old"), "x_bond": (11, "bond"), "x_place": (12, "place")})
CIERRE = {'cierre': 'WHAT DOES YOURS DO?', 'cierre2': 'Tell me. Comment', 'paises': ['PUSHES IN', 'BARKS', 'NOTHING'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_personally", -.3, "tao/alerta_suave.wav", None, .05),     # 01: el perro lo nota (cambio de foco)
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),             # a la casa de la visita
       ("x_36", -.05, "tao/clic_06.wav", None, .05),                   # 02: se anota el número
       ("x_barked", -.05, "tao/burbuja.wav", None, .05), ("x_barked", .22, "tao/burbuja.wav", None, .05),   # 03: el peluche "ladra"
       ("x_pumpkin", -.3, "tao/toque_01.wav", None, .05), ("x_book", -.3, "tao/toque_02.wav", None, .05),    # 04: cortes por coincidencia
       ("x_2", -.05, "tao/clic_positivo.wav", None, .05), ("x_8", -.05, "tao/clic_positivo.wav", None, .055), # 05 y 06: aparece la cifra
       ("x_further", .0, "impacto/kick_01.wav", .2, .05),             # 07 · G2: el perro se mete
       ("x_snapped", -.18, "tao/whoosh_salto.wav", None, .045),       # 09: el amago
       ("x_six", -.5, "tao/whoosh_carril.wav", None, .04),            # 10: paneo a la otra ficha
       ("x_bond", -.2, "ui/ding_01.wav", .7, .04),                    # 11: la línea se enciende
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]           # cierre
PORTADA = ("NEVER PET ANOTHER DOG", 5.7)
DESC = "It's not just a pat. To your dog, it's someone taking their place. 🐶\nSource: UC San Diego study on jealousy in dogs, PLOS ONE (2014)."
