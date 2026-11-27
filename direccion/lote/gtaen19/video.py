"""GTA EN 19h · GTA 6 Just HUMILIATED Hollywood · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 11 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen. Las cifras son las aprobadas: no se actualizan.
Sin logos de juegos, películas ni plataformas; Hollywood no es una persona."""
ID, LOTE, CANAL, HORA = "gtaen19", "LOTE_GTAEN19", "TheViceVerseGG", "19"
MARCA, TEMA = "THE VICEVERSE GG", None
TITULO = "GTA 6 Just HUMILIATED Hollywood 🎬😳"
VOZ = ("am_michael", 1.3, "en-us")
F = ["GTA 6 just humiliated Hollywood with a record no one has ever touched. And that's not even its only win.",
     "It launched on November 19, after two delays.",
     "Before day one, it had already sold 32.5 million copies.",
     "Then Take-Two estimated its day one sales at 3.79 billion dollars.",
     "The biggest movie opening ever, Avengers: Endgame, made about 1.2 billion dollars in its opening weekend.",
     "So GTA 6 made about three times that in a single day. The biggest launch in entertainment history.",
     "But the biggest shock didn't come from the money. Sure, it was a surprise, but…",
     "…the critics left everyone speechless. When the reviews landed on Metacritic, fans couldn't believe it.",
     "The critics agreed on a 99 out of 100. A score no game had reached in 28 years, since Zelda: Ocarina of Time.",
     "Tell me if you think it's the best game in history, and if you've played it yet. Follow for more GTA 6 news."]
REEMPLAZOS = [("GTA 6", "GTA six"), ("November 19,", "November nineteenth,"), ("32.5 million", "thirty-two and a half million"), ("Take-Two", "Take Two"),
              ("3.79 billion", "three point seven nine billion"), ("1.2 billion", "one point two billion"), ("99 out of 100", "ninety-nine out of a hundred"),
              ("28 years", "twenty-eight years"), ("…the critics", "the critics")]
PAUSAS = [1, 6, 7, 9]
CLAVES = {"x_hum": (1, "humiliated"), "x_record": (1, "record"), "x_touched": (1, "touched"), "x_and": (1, "And"), "x_only": (1, "only"),
          "x_launched": (2, "launched"), "x_nov": (2, "November"), "x_19": (2, "19"), "x_two": (2, "two"), "x_sold": (3, "sold"), "x_325": (3, "32.5"), "x_mill3": (3, "million"),
          "x_est": (4, "estimated"), "x_day": (4, "day"), "x_379": (4, "3.79"), "x_bill": (4, "billion"), "x_movie": (5, "movie"), "x_12": (5, "1.2"), "x_wk": (5, "opening", 1),
          "s_6": ("L", 6), "x_three": (6, "three"), "x_single": (6, "single"), "x_launch": (6, "biggest"), "x_money": (7, "money"), "x_sure": (7, "Sure"),
          "x_landed": (8, "landed"), "x_99": (9, "99"), "x_out": (9, "out"), "x_score": (9, "score"), "x_28": (9, "28"), "x_oca": (9, "Ocarina"), "x_tell": ("L", 10), "s_cta": (10, "Follow")}
PLANOS = [("01", "p01", None, "gancho: la claqueta cae y el récord se quiebra"),
          ("02", "p02", ("L", 2), "cenital del calendario y la caja"),
          ("03", "p03", ("L", 3), "travelling corto por las cajas hasta el contador"),
          ("04", "p04", ("L", 4), "detalle del marcador del día uno"),
          ("05", "p05", ("L", 5), "comparación proporcional lado a lado"),
          ("06", "p06", ("L", 7), "el marcador se apaga; queda la sala"),
          ("07", "p07", ("L", 8), "cenital: caen las reseñas"),
          ("08", "p08", ("L", 10), "el 99 al centro; cierre")]
CIERRE = {"cierre": "BEST GAME EVER?", "cierre2": "Tell me. Comment", "paises": ["YES", "NO"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
SFX = [("x_hum", -.03, "sintet/claqueta.wav", None, .09), ("x_record", 0, "impacto/kick_01.wav", .16, .07),
       ("c02", -.28, "transicion/whoosh_02.wav", .28, .06), ("x_19", -.03, "ui/pop_01.wav", None, .07),
       ("c03", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_325", -.03, "ui/pop_01.wav", None, .08),
       ("c04", -.28, "transicion/whoosh_02.wav", .28, .05), ("x_379", -.03, "tematicos/caja_01.wav", None, .06),
       ("c05", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_12", -.03, "ui/pop_02.wav", None, .07), ("x_three", -.03, "ui/pop_01.wav", None, .07),
       ("x_money", -.3, "sintet/baja.wav", None, .08),
       ("x_landed", -.3, "sintet/hoja.wav", None, .05), ("x_landed", .1, "sintet/hoja.wav", None, .05), ("x_landed", .5, "sintet/hoja.wav", None, .05),
       ("x_99", -.03, "impacto/kick_01.wav", .16, .09), ("x_99", .02, "ui/ding_01.wav", None, .06), ("x_28", -.03, "ui/pop_02.wav", None, .06),
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]
PORTADA = ("HUMILIATED HOLLYWOOD", 1.0)
PUBLICAR = "Vie 27/11 19:00"
DESC = "And that's not even its only win. 🎬\nSources: Take-Two (Nov 20, 2026); The Walt Disney Company (2019)."
FIRMA = "Follow @TheViceVerseGG 🎮"
TAGS = "#GTA6 #Shorts #RockstarGames #GTAVI #Gaming"
PREVIA = [(0.6, "01 cae la claqueta"), (1.0, "01 el golpe"), (3.2, "01 el récord se quiebra"), (6.0, "01 no es su única copa"), (8.2, "02 19 de noviembre"), (9.2, "02 dos retrasos"),
          (11.0, "03 las cajas"), (12.9, "03 32.5 millones"), (17.4, "04 día uno"), (22.6, "05 la película"), (24.4, "05 fin de semana"), (27.0, "05 tres veces"), (30.0, "05 a escala"),
          (32.3, "06 se apaga"), (34.0, "06 la sala"), (37.6, "07 caen las reseñas"), (41.9, "07 99 de 100"), (46.3, "07 28 años"), (53.0, "08 cierre")]
