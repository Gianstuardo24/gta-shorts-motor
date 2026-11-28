"""MDM 18h · How ONE Joke DESTROYED a Company 💍😳 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'smdm18', 'LOTE28_SMDM18', 'MillionDollarMistake', '18'
MARCA, TEMA = 'MILLION DOLLAR MISTAKE', "mdm"
TITULO = 'How ONE Joke DESTROYED a Company 💍😳'
VOZ = ('bm_george', 1.25, 'en-gb')
F = ["One joke destroyed a company: an empire with over a thousand stores. But the joke isn't even the worst part.",
     'In 1991, Gerald Ratner ran a jewelry chain his family had built in Britain.',
     'Its jewelry was cheap, and people loved it.',
     'That April, he gave a speech to thousands of business leaders in London.',
     'He joked that he could sell a set of drinking glasses so cheap because it was, in his words, total crap.',
     "Then he said his earrings cost less than a sandwich, and wouldn't last as long.",
     'Now the worst part, the one that turned a joke into a disaster.',
     'He had told that joke before, and nothing had happened.',
     'But this time, the newspapers picked it up. And his customers read that he was laughing at what they bought.',
     "They stopped coming. About 500 million pounds of the company's value disappeared.",
     'Eighteen months later, he was out of the business.',
     'Lesson: never joke about the quality of what you sell. Your customers might be listening one day.',
     "Tell me if you'd keep buying from a brand after that. Follow for the next million dollar mistake."]
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
FIRMA = '💸 Million Dollar Mistake · Big ideas. Bigger mistakes.'
TAGS = '#Shorts #MillionDollarMistake #business #mistakes #history'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/MillionDollarMistake"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('In 1991,', 'In nineteen ninety-one,'), ('500 million pounds', 'five hundred million pounds')]
CLAVES.update({"x_empire": (1, "empire"), "x_thousand": (1, "thousand"), "x_but": (1, "But"), "x_worst": (1, "worst"),
               "x_ratner": (2, "Ratner"), "x_family": (2, "family"), "x_loved": (3, "loved"), "x_speech": (4, "speech"), "x_thousands": (4, "thousands"),
               "x_glasses": (5, "glasses"), "x_cheap5": (5, "cheap"), "x_crap": (5, "crap."), "x_earrings": (6, "earrings"), "x_sandwich": (6, "sandwich,"), "x_last": (6, "last"),
               "x_worst7": (7, "worst"), "x_disaster": (7, "disaster."), "x_nothing": (8, "nothing"),
               "x_newspapers": (9, "newspapers"), "x_customers": (9, "customers"), "x_laughing": (9, "laughing"),
               "x_stopped": (10, "stopped"), "x_500": (10, "500"), "x_disappeared": (10, "disappeared."), "x_out": (11, "out"),
               "x_quality": (12, "quality"), "x_listening": (12, "listening")})
CIERRE = {'cierre': 'WOULD YOU KEEP BUYING?', 'cierre2': 'Yes or no? Comment', 'paises': ['YES', 'NEVER'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_but", -.45, "tao/whoosh_salto.wav", None, .04),            # 01: entra el micrófono
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_loved", -.1, "tao/clic_positivo.wav", None, .045),         # 03: les encanta
       ("c04", -.06, "tao/whoosh_carril.wav", None, .04),             # al auditorio
       ("x_glasses", -.3, "ui/ding_01.wav", .7, .04),                 # 05: levanta el vaso (tintineo)
       ("x_crap", -.5, "tao/scratch.wav", None, .045),                # 05: el gesto se vuelve incómodo (el tintineo termina seco)
       ("x_sandwich", -.5, "tao/whoosh_carril.wav", None, .035),      # 06: de los aretes al sándwich
       ("x_last", -.1, "tao/desequipar.wav", None, .045),             # 06: el arete se rompe
       ("x_worst7", .0, "impacto/kick_01.wav", .25, .055),            # 07 · G2: la onda se vuelve diarios
       ("x_nothing", .75, "tao/toque_02.wav", None, .045),            # 08: corte por coincidencia
       ("x_newspapers", -.2, "sintet/hoja.wav", .8, .05),             # 09: salen los diarios
       ("x_customers", -.9, "tao/whoosh_carril.wav", None, .035),     # 09: travelling a las tiendas
       ("x_500", -.5, "sintet/baja.wav", .8, .05),                    # 10: cae la línea de valor
       ("x_disappeared", -.1, "tao/hielo_golpe.wav", .7, .035),       # 10: se fragmenta
       ("x_listening", -.3, "tao/clic_06.wav", None, .05),            # 12: se apaga la vitrina
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("ONE JOKE DESTROYED IT", 5.9)
DESC = "One speech. About £500 million in company value gone. 💍\nGerald Ratner, Royal Albert Hall, April 1991."
