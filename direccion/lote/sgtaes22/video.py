"""GTA ES 22h · La PS5 de GTA 6 que NO puedes comprar 🎮🚫 · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'sgtaes22', 'LOTE28_SGTAES22', 'ViceVersoGG', '22'
MARCA, TEMA = 'VICEVERSO GG', None
TITULO = 'La PS5 de GTA 6 que NO puedes comprar 🎮🚫'
VOZ = ('em_santa', 1.3, 'es')
F = ['Hay una PS5 de GTA 6 que no puedes comprar. Rockstar no la vende, a ningún precio. Y lo más raro es a quiénes se la dieron.',
     'Apareció en noviembre de 2026, justo antes del lanzamiento.',
     'Es una PS5 Pro oscura, con palmeras grabadas y franjas que van del turquesa al magenta.',
     'Viene en una maleta rígida, con dos controles a juego y una copia del juego.',
     'Muchos fans pidieron que saliera a la venta.',
     'Ahora, lo más raro: a quiénes se la dieron, y cuántas existen.',
     'Las primeras no fueron para gamers. Fueron para basquetbolistas del Miami Heat, un día antes del estreno.',
     'Después llegaron a streamers y creadores de contenido.',
     'Cada una trae su propio número de serie.',
     'Y según los reportes, existen solo unas 100 en todo el mundo.',
     'Rockstar ya dijo que no llegará a las tiendas.',
     'O sea, es una consola que no se compra. Te la tienen que regalar.',
     'Comenta cuánto pagarías por una. Sigue el canal para más de GTA 6.']
G2, N = 6, 13
REEMPLAZOS = []
PAUSAS = [1, 5, 6, 12]
CLAVES = {"x_tell": ("L", 13), "s_cta": (13, 'Sigue')}
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
CIERRE = {'cierre': '¿Y TÚ?', 'cierre2': 'Comenta', 'paises': ['SÍ', 'NO'], 'cta': 'SIGUE EL CANAL', 'like': 'LIKE'}
SFX = []
PORTADA = ("", 1.0)
PUBLICAR = "Sáb 28/11 22:00"
DESC = ""
FIRMA = 'Sigue a @ViceVersoGG 🎮'
TAGS = '#GTA6 #Shorts #RockstarGames #GTAVI #Gaming'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/ViceVersoGG"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('GTA 6', 'GTA seis'), ('PS5 Pro', 'pe ese cinco pro'), ('PS5', 'pe ese cinco'), ('noviembre de 2026', 'noviembre de dos mil veintiséis'), ('unas 100', 'unas cien'), ('Miami Heat', 'Maiami Jit'), ('streamers', 'estrímers')]
CLAVES.update({"x_comprar": (1, "comprar."), "x_rockstar": (1, "Rockstar"), "x_precio": (1, "precio."), "x_raro": (1, "raro"), "x_dieron": (1, "dieron."),
               "x_nov": (2, "noviembre"), "x_2026": (2, "2026,"), "x_antes": (2, "antes"), "x_oscura": (3, "oscura,"), "x_palmeras": (3, "palmeras"), "x_franjas": (3, "franjas"), "x_turquesa": (3, "turquesa"), "x_magenta": (3, "magenta."),
               "x_maleta": (4, "maleta"), "x_dos": (4, "dos"), "x_copia": (4, "copia"), "x_fans": (5, "fans"), "x_venta": (5, "venta."), "x_ahora": (6, "Ahora,"), "x_quienes": (6, "quiénes"), "x_cuantas": (6, "cuántas"),
               "x_gamers": (7, "gamers."), "x_basq": (7, "basquetbolistas"), "x_miami": (7, "Miami"), "x_dia": (7, "día"), "x_estreno": (7, "estreno."), "x_streamers": (8, "streamers"), "x_creadores": (8, "creadores"),
               "x_propio": (9, "propio"), "x_serie": (9, "serie."), "x_reportes": (10, "reportes,"), "x_100": (10, "100"), "x_mundo": (10, "mundo."), "x_dijo": (11, "dijo"), "x_tiendas": (11, "tiendas."),
               "x_nocompra": (12, "compra."), "x_regalar": (12, "regalar.")})
CIERRE = {'cierre': '¿CUÁNTO PAGARÍAS?', 'cierre2': 'Comenta tu precio', 'paises': ['NADA', 'MUCHO', 'TODO'], 'cta': 'SIGUE EL CANAL', 'like': 'LIKE'}
SFX = [("0", .38, "tao/clic_03.wav", None, .05),                       # 01: salta el broche
       ("0", .9, "tao/equipar.wav", None, .045),                       # 01: se abre la maleta
       ("x_precio", -.35, "tao/desequipar.wav", None, .045),           # 01: sin precio
       ("x_raro", -.05, "tao/clic_08.wav", None, .05),                 # 01: se cierra antes de mostrar todo
       ("c02", -.06, "tao/whoosh_carril.wav", None, .04),
       ("x_2026", -.1, "tao/clic_05.wav", None, .045),                 # 02: el calendario
       ("x_antes", .0, "tao/whoosh_carril.wav", None, .035),           # 02: paneo a la maleta
       ("x_palmeras", -.3, "tao/toque_01.wav", None, .045),            # 03: las palmeras grabadas
       ("x_franjas", -.3, "tao/whoosh_salto.wav", None, .04),          # 03: gira y aparecen las franjas
       ("x_magenta", -.2, "tao/dorado.wav", None, .04),                # 03: del turquesa al magenta
       ("x_dos", -.05, "tao/toque_01.wav", None, .045), ("x_dos", .25, "tao/toque_02.wav", None, .045), ("x_copia", -.05, "tao/clic_positivo.wav", None, .045),   # 04: dos controles y el juego
       ("x_venta", -.3, "tao/escudo.wav", None, .04),                  # 05: el vidrio no abre
       ("x_ahora", .0, "impacto/kick_01.wav", .25, .055),              # 06 · G2
       ("x_cuantas", -.2, "tao/clic_06.wav", None, .045),              # 06: la placa de serie
       ("x_gamers", -.2, "sintet/baja.wav", .6, .04),                  # 07: no fueron para gamers
       ("x_miami", -.3, "tao/equipar.wav", None, .045),                # 07: la entrega
       ("x_streamers", -.3, "tao/fin_carga_01.wav", None, .04),        # 08: se abre en el set
       ("x_creadores", -.12, "tao/toque_02.wav", None, .05),           # 08: corte por coincidencia
       ("x_propio", -.1, "tao/clic_05b.wav", None, .045), ("x_serie", -.2, "tao/clic_06.wav", None, .045),      # 09: placas
       ("x_100", -.1, "tao/contador_fin.wav", None, .05),              # 10: unas 100
       ("x_dijo", .0, "sintet/baja.wav", .9, .045),                    # 11: baja la persiana
       ("x_tiendas", -.1, "tao/hielo_golpe.wav", None, .04),           # 11: cierra
       ("x_regalar", -.3, "tao/premio.wav", None, .045),               # 12: te la regalan
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("NO SE VENDE", 15.3)
DESC = "Hay una consola de GTA 6 que no puedes comprar. 🎮🚫\nSegún los reportes existen solo unas 100: las primeras fueron para basquetbolistas del Miami Heat."
