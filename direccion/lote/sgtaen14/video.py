"""GTA EN 14h · DON'T Stop for This Car in GTA 6 🛸🚫 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'sgtaen14', 'LOTE28_SGTAEN14', 'TheViceVerseGG', '14'
MARCA, TEMA = 'THE VICEVERSE GG', None
TITULO = "DON'T Stop for This Car in GTA 6 🛸🚫"
VOZ = ('am_michael', 1.3, 'en-us')
F = ["Don't stop for this car in GTA 6. It looks abandoned, but it's bait. Careful, what's waiting in the woods is only the beginning.",
     'Head to the road east of Port Gellhorn, near the Starlet Motel.',
     'Go at night. Players say it shows up after 2 in the morning.',
     "You'll find a car left on the road with its door wide open.",
     'Next to it, a trail of clothes leads into the trees.',
     'Follow it, and a glowing UFO appears right above you. And yes, it takes you.',
     'Now the real secret, because that encounter is only the beginning.',
     "First, the game gives you a hidden trophy. It's called The Truth Is Out There.",
     'Then your character starts having strange dreams.',
     'Those dreams lead to a code, and to an underground lab.',
     'So the car was never the secret. It was the front door.',
     "Tell me if you've been abducted yet. Follow for more GTA 6 secrets."]
G2, N = 7, 12
REEMPLAZOS = []
PAUSAS = [1, 6, 7, 11]
CLAVES = {"x_tell": ("L", 12), "s_cta": (12, 'Follow')}
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
          ("12", "p12", ("L", 12), 'línea 12 · CTA')]
CIERRE = {'cierre': 'WHAT ABOUT YOU?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NO'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 14:00"
DESC = ""
FIRMA = 'Follow @TheViceVerseGG 🎮'
TAGS = '#GTA6 #Shorts #RockstarGames #GTAVI #Gaming'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/TheViceVerseGG"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('GTA 6', 'GTA six'), ('after 2 in the morning', 'after two in the morning')]
CLAVES.update({"x_abandoned": (1, "abandoned,"), "x_bait": (1, "bait."), "x_careful": (1, "Careful,"), "x_woods": (1, "woods"),
               "x_east": (2, "east"), "x_port": (2, "Port"), "x_starlet": (2, "Starlet"), "x_2": (3, "2"), "x_door": (4, "door"), "x_trees": (5, "trees."),
               "x_ufo": (6, "UFO"), "x_takes": (6, "takes"), "x_secret": (7, "secret,"), "x_beginning": (7, "beginning."),
               "x_trophy": (8, "trophy."), "x_called": (8, "called"), "x_code": (10, "code,"), "x_lab": (10, "lab."), "x_never": (11, "never"), "x_front": (11, "front")})
CIERRE = {'cierre': 'ABDUCTED YET?', 'cierre2': 'Tell me. Comment', 'paises': ['YES', 'NOT YET'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_bait", -.45, "tao/alerta_suave.wav", None, .04),            # 01: reflejo extraño que cruza el parabrisas
       ("x_woods", -.3, "tao/pasada_nave.wav", None, .035),            # 01: algo brilla en el bosque
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_port", -.05, "tao/clic_05.wav", None, .045), ("x_starlet", -.05, "tao/clic_06.wav", None, .045),   # 02: marcas del mapa
       ("x_2", -.25, "tao/contador_fin.wav", None, .05),               # 03: el reloj pasa de 1:59 a 2:00
       ("x_door", -.3, "tao/clic_03.wav", None, .04),                  # 04: la puerta abierta
       ("c05", .2, "tao/toque_01.wav", None, .04), ("c05", .6, "tao/toque_02.wav", None, .04), ("c05", 1.0, "tao/toque_01.wav", None, .04),   # 05: el rastro de ropa
       ("x_ufo", -.5, "tao/pasada_nave.wav", None, .05),               # 06: aparece el ovni
       ("x_takes", -.2, "sintet/sube.wav", .9, .045),                  # 06: te lleva
       ("x_secret", -.25, "impacto/kick_01.wav", .25, .055),           # 07 · G2
       ("x_secret", .0, "tao/logro.wav", None, .045),                  # 07: placa de logro
       ("x_called", .15, "tao/liberado.wav", None, .045),              # 08: el nombre del trofeo
       ("c09", .3, "tao/alerta_suave.wav", None, .035),                # 09: sueños
       ("x_code", -.3, "tao/confirmar.wav", None, .045),               # 10: el código se ordena
       ("x_lab", -.5, "tao/fin_carga_01.wav", None, .045),             # 10: se abre el laboratorio
       ("x_front", -.1, "tao/whoosh_salto.wav", None, .04),            # 11: corte por coincidencia de puertas
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("DON'T STOP FOR THIS CAR", 4.0)
DESC = "That abandoned car in GTA 6 is bait. 🛸\nRoad east of Port Gellhorn, near the Starlet Motel, at night. Hidden trophy: The Truth Is Out There."
