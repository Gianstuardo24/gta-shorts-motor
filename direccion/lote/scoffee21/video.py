"""COFFEE 21h · Your Coffee Is LYING to Your Brain ☕🤥 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'scoffee21', 'LOTE28_SCOFFEE21', 'ChiChibitsTV', '21'
MARCA, TEMA = 'COFFEE, BUT WHY?', "cafe"
TITULO = 'Your Coffee Is LYING to Your Brain ☕🤥'
VOZ = ('am_michael', 1.25, 'en-us')
F = ["Your coffee is lying to your brain. It feels like energy, but it isn't giving you any. Careful, the real trick shows up hours later.",
     'From the moment you wake up, your brain builds up a chemical called adenosine.',
     "The more it piles up, the sleepier you feel. It's your body's tiredness signal.",
     'Caffeine has almost the same shape as that chemical.',
     'So it slips into the same spots in your brain, and blocks them.',
     "The tiredness signal can't get through. And you feel awake.",
     "Now the part that shows up hours later, and it's why the crash hits so hard.",
     "Your coffee didn't remove the tiredness. It only covered it.",
     'While the caffeine sits there, your brain keeps making adenosine. It just has nowhere to go.',
     'Then the caffeine wears off, and all of it rushes in at once.',
     "And if you drink coffee every day, your brain adapts by building more of those spots. That's why one cup stops feeling like enough.",
     "So coffee doesn't give you energy. It just hides how tired you are.",
     'Tell me how many cups it takes you to feel awake. Follow for one coffee curiosity a day.']
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
PUBLICAR = "Sáb 28/11 21:00"
DESC = ""
FIRMA = '☕ Coffee, But Why? · Follow for one coffee curiosity a day.'
TAGS = '#Shorts #coffee #coffeelover #coffeefacts #morningcoffee'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/ChiChibitsTV"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = []
INCLUYE = ["b28.js", "coffee21/bloque.js"]      # piezas del canal (taza, vapor, persona, mano mostaza) vienen del bloque del 27-nov
CLAVES.update({"x_energy": (1, "energy,"), "x_isnt": (1, "isn't"), "x_careful": (1, "Careful,"), "x_hours": (1, "hours"), "x_adenosine": (2, "adenosine."),
               "x_sleepier": (3, "sleepier"), "x_signal": (3, "signal."), "x_same": (4, "same"), "x_slips": (5, "slips"), "x_blocks": (5, "blocks"),
               "x_awake": (6, "awake."), "x_hours7": (7, "hours"), "x_crash": (7, "crash"), "x_remove": (8, "remove"), "x_covered": (8, "covered"),
               "x_keeps": (9, "keeps"), "x_nowhere": (9, "nowhere"), "x_wears": (10, "wears"), "x_rushes": (10, "rushes"), "x_once": (10, "once."),
               "x_adapts": (11, "adapts"), "x_more": (11, "more"), "x_enough": (11, "enough."), "x_hides": (12, "hides")})
CIERRE = {'cierre': 'HOW MANY CUPS?', 'cierre2': 'Tell me. Comment', 'paises': ['1', '2', '3+'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_isnt", -.1, "tao/alerta_suave.wav", None, .045),          # 01: aparece la sombra
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_adenosine", -.1, "tao/clic_05.wav", None, .045),           # 02: se nombra
       ("x_sleepier", -.4, "sintet/baja.wav", .8, .045),              # 03: baja a la persona
       ("x_same", -.25, "tao/equipar.wav", None, .05),                # 04: las formas coinciden
       ("x_slips", -.05, "tao/toque_01.wav", None, .045), ("x_slips", .25, "tao/toque_02.wav", None, .045), ("x_slips", .52, "tao/toque_01.wav", None, .045),   # 05: la cafeína ocupa los encajes
       ("x_awake", -.9, "sintet/sube.wav", .7, .045),                 # 06: sube a la persona
       ("x_crash", .0, "impacto/kick_01.wav", .25, .055),             # 07 · G2: golpe grave
       ("x_covered", -.5, "tao/whoosh_carril.wav", None, .04),        # 08: la capa cubre la señal
       ("x_nowhere", -.1, "tao/alerta_suave.wav", None, .04),         # 09: se acumula
       ("x_wears", -.2, "tao/desequipar.wav", None, .05),             # 10: la cafeína se va
       ("x_rushes", -.15, "tao/whoosh_salto.wav", None, .045),        # 10: entra todo de golpe
       ("x_more", -.4, "tao/clic_positivo.wav", None, .045),          # 11: aparecen más encajes
       ("x_hides", -.3, "tao/alerta_suave.wav", None, .04),           # 12: vuelve la sombra
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("YOUR COFFEE IS LYING", 3.9)
DESC = "Coffee doesn't give you energy. It hides how tired you are. ☕\nCaffeine blocks adenosine, the brain's tiredness signal."
