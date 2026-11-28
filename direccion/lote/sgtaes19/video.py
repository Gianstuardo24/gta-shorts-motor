"""GTA ES 19h · Los jugadores CASTIGARON a GTA 6 😳👎 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'sgtaes19', 'LOTE28_SGTAES19', 'ViceVersoGG', '19'
MARCA, TEMA = 'VICEVERSO GG', None
TITULO = 'Los jugadores CASTIGARON a GTA 6 😳👎'
VOZ = ('em_santa', 1.3, 'es')
F = ['Los jugadores castigaron a GTA 6. La prensa le dio 99 de 100 y el público, menos de 6. Pero esa nota esconde algo que casi nadie revisa.',
     'En Metacritic, más de 150 críticos lo dejaron en 99 de 100.',
     'Pero ese sitio tiene otra nota: la de los usuarios.',
     'Se abrió el 20 de noviembre, un día y medio después del lanzamiento.',
     'Y en pocas horas cayó hasta 4,9 de 10.',
     'Ahora, lo que casi nadie revisa: quiénes pusieron esas notas.',
     'En Metacritic, cualquiera puede votar. No hace falta demostrar que tienes el juego.',
     'Miles de esas notas fueron un cero.',
     'Y hubo respuesta: fans de GTA fueron a bajarle la nota a Zelda Ocarina of Time, el juego que comparte el 99.',
     'También hay quejas reales, como que corre a 30 cuadros por segundo y algunos errores.',
     'O sea, esa nota mezcla quejas reales con una guerra entre fans.',
     'Comenta qué nota le pones tú y por qué. Sigue el canal para más de GTA 6.']
G2, N = 6, 12
REEMPLAZOS = []
PAUSAS = [1, 5, 6, 11]
CLAVES = {"x_tell": ("L", 12), "s_cta": (12, 'Sigue')}
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
CIERRE = {'cierre': '¿Y TÚ?', 'cierre2': 'Comenta', 'paises': ['SÍ', 'NO'], 'cta': 'SIGUE EL CANAL', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 19:00"
DESC = ""
FIRMA = 'Sigue a @ViceVersoGG 🎮'
TAGS = '#GTA6 #Shorts #RockstarGames #GTAVI #Gaming'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/ViceVersoGG"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('GTA 6', 'GTA seis'), ('99 de 100', 'noventa y nueve de cien'), ('menos de 6.', 'menos de seis.'), ('más de 150 críticos', 'más de ciento cincuenta críticos'), ('20 de noviembre', 'veinte de noviembre'), ('4,9 de 10', 'cuatro coma nueve de diez'), ('comparte el 99.', 'comparte el noventa y nueve.'), ('30 cuadros', 'treinta cuadros')]
CLAVES.update({"x_castig": (1, "castigaron"), "x_prensa": (1, "prensa"), "x_99": (1, "99"), "x_publico": (1, "público,"), "x_menos": (1, "menos"), "x_esconde": (1, "esconde"), "x_nadie": (1, "nadie"),
               "x_meta": (2, "Metacritic,"), "x_150": (2, "150"), "x_dejaron": (2, "dejaron"), "x_99b": (2, "99"), "x_otra": (3, "otra"), "x_usuarios": (3, "usuarios."),
               "x_20": (4, "20"), "x_nov": (4, "noviembre,"), "x_dia": (4, "día"), "x_lanz": (4, "lanzamiento."), "x_horas": (5, "horas"), "x_cayo": (5, "cayó"), "x_49": (5, "4,9"),
               "x_ahora": (6, "Ahora,"), "x_revisa": (6, "revisa:"), "x_quienes": (6, "quiénes"), "x_cualq": (7, "cualquiera"), "x_votar": (7, "votar."), "x_nohace": (7, "hace"), "x_juego": (7, "juego."),
               "x_miles": (8, "Miles"), "x_cero": (8, "cero."), "x_resp": (9, "respuesta:"), "x_fans": (9, "fans"), "x_bajarle": (9, "bajarle"), "x_zelda": (9, "Zelda"), "x_comparte": (9, "comparte"), "x_99c": (9, "99."),
               "x_quejas": (10, "quejas"), "x_30": (10, "30"), "x_errores": (10, "errores."), "x_mezcla": (11, "mezcla"), "x_reales": (11, "reales"), "x_guerra": (11, "guerra")})
CIERRE = {'cierre': '¿QUÉ NOTA LE PONES?', 'cierre2': 'Comenta por qué', 'paises': ['10', '5', '0'], 'cta': 'SIGUE EL CANAL', 'like': 'LIKE'}
SFX = [("x_castig", -.1, "impacto/kick_01.wav", .25, .055),            # 01: el pulgar abajo cae como sello
       ("x_prensa", -.3, "tao/whoosh_carril.wav", None, .035),         # 01: entran las dos notas
       ("x_99", -.1, "tao/clic_positivo.wav", None, .045), ("x_menos", -.05, "tao/alerta_suave.wav", None, .04),
       ("x_nadie", -.5, "tao/desequipar.wav", None, .045),             # 01: se corre la tarjeta y asoma lo de atrás
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_150", -.1, "tao/clic_05.wav", None, .045),                  # 02: más de 150 críticos
       ("x_99b", -.25, "tao/equipar.wav", None, .05),                  # 02: se agrupan en 99
       ("x_otra", -.3, "tao/whoosh_salto.wav", None, .04),             # 03: gira la tarjeta
       ("x_20", -.25, "tao/liberado.wav", None, .045),                 # 04: se abre el 20
       ("x_dia", -.15, "tao/tic_rueda.wav", None, .045),               # 04: avanza la línea de tiempo
       ("x_cayo", -.3, "sintet/baja.wav", .9, .045),                   # 05: cae en escalones
       ("x_49", -.1, "tao/hielo_golpe.wav", None, .045),               # 05: 4,9
       ("x_ahora", .0, "impacto/kick_01.wav", .25, .055),              # 06 · G2
       ("x_quienes", -.2, "tao/burbuja.wav", None, .04), ("x_quienes", .2, "tao/pop_burbuja.wav", None, .04),   # 06: aparecen los avatares
       ("x_votar", -.2, "tao/toque_01.wav", None, .045), ("x_votar", .25, "tao/toque_02.wav", None, .045),      # 07: votos a la urna
       ("x_nohace", -.15, "tao/clic_06.wav", None, .045),              # 07: no hace falta
       ("x_cero", -.15, "tao/hielo_congela.wav", None, .045),          # 08: los ceros
       ("x_bajarle", -.2, "tao/whoosh_carril.wav", None, .04),         # 09: la oleada de votos
       ("x_zelda", -.15, "tao/clic_05b.wav", None, .045),              # 09: el otro juego
       ("x_99c", -.3, "tao/clic_positivo.wav", None, .045),            # 09: comparten el 99
       ("x_30", -.1, "tao/contador_fin.wav", None, .045),              # 10: 30 FPS
       ("x_errores", -.3, "tao/scratch.wav", None, .035),              # 10: fallos visuales
       ("x_reales", -.3, "tao/toque_01.wav", None, .045), ("x_guerra", -.3, "tao/toque_02.wav", None, .045),    # 11: las dos capas
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("99 CONTRA MENOS DE 6", 5.0)
DESC = "La prensa le dio 99 de 100 a GTA 6. Los usuarios, menos de 6. 😳\nEn Metacritic cualquiera puede votar sin demostrar que tiene el juego."
