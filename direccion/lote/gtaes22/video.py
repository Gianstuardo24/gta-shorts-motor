"""GTA ES 22h · La prensa se RINDIÓ ante GTA 6 · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 13 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen. Sin medios, críticos ni citas inventadas; sin personajes ni logos."""
ID, LOTE, CANAL, HORA = "gtaes22", "LOTE_GTAES22", "ViceVersoGG", "22"
MARCA, TEMA = "VICEVERSO GG", None
TITULO = "La prensa se RINDIÓ ante GTA 6 🏆😳"
VOZ = ("em_santa", 1.3, "es")
F = ["La prensa se rindió ante GTA 6. Y lo hizo de una forma que nadie había logrado. Pero hay un detalle que casi nadie te cuenta.",
     "Las reseñas de la prensa salieron el 18 de noviembre.",
     "En Metacritic, el sitio que promedia a los críticos, sacó una puntuación de 99 de 100.",
     "Ese puntaje solo lo tenía un juego: Zelda Ocarina of Time, de 1998.",
     "Para muchos, fue considerado el mejor juego de la historia.",
     "Pero ahora, el detalle que casi nadie te cuenta.",
     "Ocarina llegó a 99 con 22 reseñas. En cambio, GTA 6 lo hizo con más de 140.",
     "Con más críticos opinando, es mucho más difícil mantener un promedio tan alto.",
     "O sea, el mismo número, pero con seis veces más críticos opinando.",
     "Esto, sin duda, es una cifra a tener en cuenta.",
     "Comenta si crees que se merece el 99 de 100. Y si no, en cuánto lo calificarías y por qué. Sigue el canal para más números de GTA 6."]
REEMPLAZOS = [("GTA 6", "GTA seis"), ("18 de noviembre", "dieciocho de noviembre"), ("99 de 100", "noventa y nueve de cien"), ("de 1998", "de mil novecientos noventa y ocho"),
              ("a 99 con 22 reseñas", "a noventa y nueve con veintidós reseñas"), ("más de 140", "más de ciento cuarenta")]
PAUSAS = [1, 5, 6, 10]
CLAVES = {"x_rin": (1, "rindió"), "x_ylo": (1, "Y"), "x_pero": (1, "Pero"), "x_det": (1, "detalle"), "x_18": (2, "18"), "x_prom": (3, "promedia"), "x_99": (3, "99"), "x_100": (3, "100"),
          "x_zelda": (4, "Zelda"), "x_1998": (4, "1998"), "x_mejor": (5, "mejor"), "s_7": ("L", 7), "x_99b": (7, "99"), "x_22": (7, "22"), "x_cambio": (7, "cambio"), "x_140": (7, "140"),
          "x_dificil": (8, "difícil"), "s_9": ("L", 9), "x_mismo": (9, "mismo"), "x_seis": (9, "seis"), "x_tell": ("L", 11), "s_cta": (11, "Sigue")}
PLANOS = [("01", "p01", None, "gancho: la pared de tarjetas forma el 99"),
          ("02a", "p02a", ("L", 2), "cenital del calendario"),
          ("02b", "p02b", ("L", 3), "corte al marcador"),
          ("03", "p03", ("L", 4), "plano medio simétrico: dos pedestales"),
          ("04", "p04", ("L", 6), "alejamiento desde el 99: las fichas de cada tablero"),
          ("06", "p06", ("L", 8), "plano lateral: la balanza"),
          ("07", "p07", ("L", 10), "el 99 al centro; cierre")]
CIERRE = {"cierre": "¿SE MERECE EL 99?", "cierre2": "Comenta: sí o no", "paises": ["SÍ", "NO"], "cta": "SIGUE EL CANAL", "like": "LIKE"}
SFX = [("0", .12, "sintet/hoja.wav", None, .05), ("0", .45, "sintet/hoja.wav", None, .05), ("x_rin", .3, "ui/ding_01.wav", None, .05),
       ("c02a", -.28, "transicion/whoosh_02.wav", .28, .06), ("x_18", -.03, "ui/pop_01.wav", None, .07),
       ("c02b", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_99", -.03, "ui/ding_01.wav", None, .07),
       ("c03", -.28, "transicion/whoosh_02.wav", .28, .05), ("x_zelda", 0, "ui/pop_02.wav", None, .06), ("x_1998", -.03, "ui/pop_01.wav", None, .06),
       ("c04", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_22", -.03, "ui/pop_01.wav", None, .07), ("x_140", -.03, "ui/pop_01.wav", None, .08),
       ("c06", -.28, "transicion/whoosh_02.wav", .28, .05), ("x_seis", -.03, "ui/pop_02.wav", None, .07),
       ("c07", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]
PORTADA = ("LA PRENSA SE RINDIÓ", 14.6)
PUBLICAR = "Vie 27/11 22:00"
DESC = "Mismo número. Historia distinta. 🏆"
FIRMA = "Sigue a @ViceVersoGG 🎮"
TAGS = "#GTA6 #Shorts #RockstarGames #GTAVI #Gaming"
PREVIA = [(0.2, "01 la pared"), (1.6, "01 forma el 99"), (6.4, "01 el detalle"), (9.4, "02 18 de noviembre"), (12.4, "02 el promedio"), (14.5, "02 99 de 100"), (16.4, "03 solo un juego"), (19.2, "03 de 1998"),
          (22.0, "03 el mejor"), (23.2, "04 desde el 99"), (27.4, "04 22 reseñas"), (30.7, "04 más de 140"), (33.4, "06 la balanza"), (38.0, "06 seis veces"), (40.6, "07 el 99"), (49.4, "07 cierre")]
