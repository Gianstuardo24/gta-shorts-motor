"""COFFEE 17h · STOP Fixing Bitter Coffee With SUGAR ☕🚫 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'scoffee17', 'LOTE28_SCOFFEE17', 'ChiChibitsTV', '17'
MARCA, TEMA = 'COFFEE, BUT WHY?', "cafe"
TITULO = 'STOP Fixing Bitter Coffee With SUGAR ☕🚫'
VOZ = ('am_michael', 1.25, 'en-us')
F = ["If your coffee tastes bitter, stop fixing it with sugar. Almost nobody knows there's another way. And it's probably already in your kitchen.",
     'When coffee turns bitter, most people reach for sugar.',
     'Sugar adds sweetness on top. But the bitter taste is still in the cup.',
     'In 1997, scientists in Philadelphia tested a different idea.',
     'They gave 21 volunteers drinks that mixed bitter and sweet, and asked them to rate each one.',
     "Now the other way almost nobody knows, the one that's already in your kitchen.",
     "You don't need a new machine. And you don't need more expensive coffee.",
     'The scientists added a kind of salt to those bitter drinks.',
     'The bitterness dropped. And the drinks even tasted sweeter, without any extra sugar.',
     "That's because sodium blocks part of the bitter signal on your tongue.",
     "In coffee, a tiny pinch is enough. You shouldn't taste the salt at all.",
     'So next time your coffee is bitter, try a pinch of salt before the sugar.',
     "Tell me if you'd dare to put salt in your coffee. Follow for one coffee curiosity a day."]
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
PUBLICAR = "Sáb 28/11 17:00"
DESC = ""
FIRMA = '☕ Coffee, But Why? · Follow for one coffee curiosity a day.'
TAGS = '#Shorts #coffee #coffeelover #coffeefacts #morningcoffee'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/ChiChibitsTV"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('In 1997,', 'In nineteen ninety-seven,'), ('21 volunteers', 'twenty-one volunteers')]
INCLUYE = ["b28.js", "coffee21/bloque.js"]      # piezas del canal (taza, vapor, persona, mano mostaza) vienen del bloque del 27-nov
CLAVES.update({"x_stop": (1, "stop"), "x_another": (1, "another"), "x_kitchen": (1, "kitchen."), "x_reach": (2, "reach"),
               "x_top": (3, "top."), "x_but": (3, "But"), "x_still": (3, "still"), "x_tested": (4, "tested"),
               "x_21": (5, "21"), "x_mixed": (5, "mixed"), "x_rate": (5, "rate"), "x_nobody": (6, "nobody"), "x_already": (6, "already"),
               "x_machine": (7, "machine."), "x_expensive": (7, "expensive"), "x_salt": (8, "salt"),
               "x_dropped": (9, "dropped."), "x_sweeter": (9, "sweeter,"), "x_without": (9, "without"),
               "x_sodium": (10, "sodium"), "x_blocks": (10, "blocks"), "x_pinch": (11, "pinch"), "x_enough": (11, "enough."),
               "x_try": (12, "try"), "x_before": (12, "before")})
CIERRE = {'cierre': 'WOULD YOU DARE?', 'cierre2': 'Yes or no? Comment', 'paises': ['YES', 'NO WAY'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_stop", -.1, "tao/scratch.wav", None, .045),                # 01: "stop"
       ("x_kitchen", -.3, "ui/ding_01.wav", .7, .04),                 # 01: el salero del fondo
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_reach", .1, "tao/clic_06.wav", None, .05),                 # 02: toma la cuchara
       ("x_but", -.05, "tao/alerta_suave.wav", None, .045),           # 03: lo amargo sigue ahí
       ("c04", -.06, "tao/whoosh_carril.wav", None, .04),             # al laboratorio
       ("x_21", -.05, "tao/clic_positivo.wav", None, .05),            # 05: los 21
       ("x_mixed", -.8, "tao/whoosh_carril.wav", None, .04),         # 05: paneo a las mezclas
       ("c06", .3, "sintet/descuelga.wav", None, .07),                # 06: se abre el cajón
       ("c06", 1.3, "impacto/kick_01.wav", .2, .05),                  # 06 · G2: aparece el salero
       ("x_already", -.3, "ui/ding_01.wav", .7, .04),                 # 06: acento sobre el salero
       ("x_machine", -.25, "tao/desequipar.wav", None, .045), ("x_expensive", -.15, "tao/desequipar.wav", None, .045),   # 07: se descartan
       ("x_salt", .17, "tao/pop_burbuja.wav", None, .05),             # 08: el cristal entra al líquido
       ("x_dropped", -.45, "sintet/baja.wav", .7, .05), ("x_sweeter", -.3, "sintet/sube.wav", .7, .05),                  # 09: baja lo amargo, sube lo dulce
       ("x_blocks", -.05, "tao/equipar.wav", None, .05),              # 10: el sodio tapa dos receptores
       ("x_pinch", -.05, "tao/tic_rep.wav", None, .05), ("x_pinch", .25, "tao/tic_rep.wav", None, .045),                 # 11: cae la pizca
       ("x_before", .5, "tao/clic_positivo.wav", None, .045),         # 12: prueba y sonríe
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("STOP FIXING IT WITH SUGAR", 2.7)
DESC = "Bitter coffee? There's another way, and it's probably already in your kitchen. ☕\nSource: Monell Chemical Senses Center, Nature (1997)."
