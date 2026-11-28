"""CATS 16h · Don't TRUST Your Cat's Favorite Plant 🌿❓ · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'scats16', 'LOTE28_SCATS16', 'CatDecoded', '16'
MARCA, TEMA = 'THE CATS DECODER', "mascotas"
TITULO = "Don't TRUST Your Cat's Favorite Plant 🌿❓"
VOZ = ('bf_emma', 1.2, 'en-gb')
F = ["Don't trust your cat's favorite plant. Everyone thinks the plant called catnip just makes cats go crazy for fun. But that's only half the story.",
     "You've seen it. A cat sniffs catnip, rubs its face on it, and rolls on the floor.",
     'In 2021, scientists in Japan wanted to know why cats do that.',
     "They studied catnip and a similar plant, silver vine, and found the chemical that sets cats off. It switches on the pleasure system in the cat's brain.",
     'So yes, it feels good. For about five to fifteen minutes.',
     'Now the other half of the story, the one almost every cat owner misses.',
     "The scientists noticed something. The cats weren't just playing. They were rubbing the plant onto their face and head.",
     'So they brought in mosquitoes.',
     'Cats that had rubbed on the plant got far fewer mosquitoes landing on them.',
     'The same chemical that excites the cat keeps the bugs away. And the leopards and jaguars in the study did it too.',
     "So it's not just a party. Your cat may be putting on bug spray.",
     'Tell me if your cat goes crazy for catnip, or just ignores it. Follow to decode your cat.']
G2, N = 6, 12
REEMPLAZOS = []
PAUSAS = [1, 5, 6, 11]
CLAVES = {"x_tell": ("L", 12), "s_cta": (12, 'Follow')}
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
          ("12", "p12", ("L", 12), 'línea 12 · CTA')]
CIERRE = {'cierre': 'WHAT ABOUT YOU?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 16:00"
DESC = ""
FIRMA = '🐱 The Cats Decoder · Follow to decode your cat.'
TAGS = '#Shorts #cats #catbehavior #catlover #catfacts'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/CatDecoded"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('In 2021,', 'In twenty twenty-one,')]
CLAVES.update({"x_crazy": (1, "crazy"), "x_half": (1, "half"), "x_rubs": (2, "rubs"), "x_rolls": (2, "rolls"), "x_why": (3, "why"),
               "x_silver": (4, "silver"), "x_chemical": (4, "chemical"), "x_pleasure": (4, "pleasure"), "x_five": (5, "five"), "x_fifteen": (5, "fifteen"),
               "x_other": (6, "other"), "x_misses": (6, "misses."), "x_rubbing": (7, "rubbing"), "x_face": (7, "face"), "x_head": (7, "head."),
               "x_fewer": (9, "fewer"), "x_bugs": (10, "bugs"), "x_leopards": (10, "leopards"), "x_jaguars": (10, "jaguars"), "x_spray": (11, "spray.")})
CIERRE = {'cierre': 'CRAZY OR NOT?', 'cierre2': 'Tell me. Comment', 'paises': ['GOES CRAZY', 'IGNORES IT'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("0", .55, "tao/whoosh_carril.wav", None, .04),               # 01: la hoja se retira del lente
       ("x_rolls", -.2, "tao/toque_01.wav", None, .05),               # 02: se echa a rodar
       ("c03", -.06, "tao/whoosh_carril.wav", None, .04),             # a la mesa botánica
       ("x_silver", -.05, "tao/clic_05.wav", None, .045),             # 04: segunda etiqueta
       ("x_chemical", -.1, "tao/burbuja.wav", None, .045), ("x_chemical", .25, "tao/burbuja.wav", None, .04),   # 04: salen las partículas
       ("x_pleasure", -.1, "ui/ding_01.wav", .7, .045),               # 04: se enciende el centro
       ("x_five", -.02, "tao/tic_rueda.wav", None, .05), ("x_fifteen", .0, "tao/tic_rueda.wav", None, .05),     # 05: la banda de tiempo
       ("x_other", .0, "impacto/kick_01.wav", .2, .05), ("x_other", -.05, "tao/escudo.wav", None, .035),        # 06 · G2: la sombra con forma de escudo
       ("c08", .15, "tao/alerta_suave.wav", None, .045),              # 08: aparecen los mosquitos
       ("x_fewer", -.05, "tao/clic_positivo.wav", None, .045),        # 09: la comparación
       ("x_leopards", -.5, "tao/whoosh_carril.wav", None, .04), ("x_jaguars", .3, "tao/whoosh_carril.wav", None, .04),  # 10: travelling a cada felino
       ("x_spray", -.4, "tao/escudo.wav", None, .035),                # 11: los mosquitos se alejan
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]           # cierre
PORTADA = ("DON'T TRUST THE PLANT", 3.4)
DESC = "Catnip isn't just a party for your cat. 🐱\nSource: Iwate University, Science Advances (2021)."
