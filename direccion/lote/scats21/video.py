"""CATS 21h · Your Cat Will NEVER Taste THIS 🍰🚫 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'scats21', 'LOTE28_SCATS21', 'CatDecoded', '21'
MARCA, TEMA = 'THE CATS DECODER', "mascotas"
TITULO = 'Your Cat Will NEVER Taste THIS 🍰🚫'
VOZ = ('bf_emma', 1.2, 'en-gb')
F = ["Your cat will never taste this. It can eat it, but something is always missing. Careful, your cat isn't being picky, it was born without something.",
     'Back in the 1970s, scientists noticed something odd about cats.',
     'Give most animals sugar water and plain water, and they pick the sweet one.',
     "Cats don't care. To them, both seem the same.",
     'For decades, nobody could explain why.',
     'Now the thing every cat is born without, the part nobody tells you about.',
     "In 2005, scientists in Philadelphia looked inside the cat's DNA.",
     'To taste sweet, a tongue needs a sensor made of two parts.',
     'In cats, one of those parts is broken. A chunk of the gene that builds it is simply missing.',
     "So cats can't detect sweet at all. The rest of their taste, like for meat, still works.",
     "And it's not just house cats. Tigers and cheetahs have the same broken gene.",
     "So if your cat licks your dessert, it isn't tasting the sweet part.",
     'Tell me the weirdest food your cat has tried to steal. Follow to decode your cat.']
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
PUBLICAR = "Sáb 28/11 21:00"
DESC = ""
FIRMA = '🐱 The Cats Decoder · Follow to decode your cat.'
TAGS = '#Shorts #cats #catbehavior #catlover #catfacts'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/CatDecoded"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('the 1970s', 'the nineteen seventies'), ('In 2005,', 'In two thousand five,')]
CLAVES.update({"x_eat": (1, "eat"), "x_missing1": (1, "missing."), "x_careful": (1, "Careful,"), "x_sugar": (3, "sugar"), "x_plain": (3, "plain"), "x_pick": (3, "pick"),
               "x_both": (4, "both"), "x_born6": (6, "born"), "x_nobody": (6, "nobody"), "x_inside": (7, "inside"), "x_dna": (7, "DNA."), "x_two": (8, "two"),
               "x_broken": (9, "broken."), "x_chunk": (9, "chunk"), "x_gone": (9, "missing."), "x_sweet": (10, "sweet"), "x_meat": (10, "meat,"),
               "x_tigers": (11, "Tigers"), "x_cheetahs": (11, "cheetahs"), "x_dessert": (12, "dessert,"), "x_sweetpart": (12, "sweet")})
CIERRE = {'cierre': 'WEIRDEST FOOD?', 'cierre2': 'Tell me. Comment', 'paises': ['CHEESE', 'BREAD', 'OTHER'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_missing1", -.15, "tao/alerta_suave.wav", None, .045),     # 01: el gato pierde interés (acento frío)
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),             # al laboratorio de los 70
       ("x_sugar", -.15, "tao/toque_01.wav", None, .05),              # 03: aparecen los terrones
       ("x_pick", -.05, "tao/clic_positivo.wav", None, .045),         # 03: eligen el dulce
       ("c05", .1, "sintet/hoja.wav", .8, .05),                       # 05: pasan las hojas
       ("x_born6", .0, "impacto/kick_01.wav", .2, .05),               # 06 · G2: el sensor incompleto
       ("x_nobody", -.25, "tao/whoosh_salto.wav", None, .04),         # 06: corte a macro
       ("x_inside", -.2, "ui/ding_01.wav", .7, .04),                  # 07: se ilumina un tramo
       ("x_two", -.02, "tao/equipar.wav", None, .05),                 # 08: las dos piezas encajan
       ("x_broken", -.5, "tao/desequipar.wav", None, .05),            # 09: una pieza está rota
       ("x_chunk", -.2, "tao/clic_05.wav", None, .045),               # 09: baja al gen
       ("x_sweet", -.05, "tao/toque_02.wav", None, .05),              # 10: el terrón rebota
       ("x_meat", -.1, "tao/clic_positivo.wav", None, .05),           # 10: el sensor de la carne responde
       ("x_tigers", -.1, "tao/toque_01.wav", None, .045), ("x_cheetahs", .35, "tao/toque_02.wav", None, .045),   # 11: cortes entre retratos
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]           # cierre
PORTADA = ("NEVER TASTE THIS", 4.6)
DESC = "Your cat isn't being picky. It was born without something. 🐱\nSource: Monell Chemical Senses Center, PLoS Genetics (2005)."
