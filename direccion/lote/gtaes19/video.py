"""GTA ES 19h · GTA 5 HUMILLÓ a GTA 6 · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 12 del lote (27-nov). Las etiquetas "G2:" y "CTA:" del documento no se dicen. Sin logos ni personajes: dos carriles y dos autos genéricos."""
ID, LOTE, CANAL, HORA = "gtaes19", "LOTE_GTAES19", "ViceVersoGG", "19"
MARCA, TEMA = "VICEVERSO GG", None
TITULO = "GTA 5 HUMILLÓ a GTA 6 😳"
VOZ = ("em_santa", 1.3, "es")
F = ["GTA 5 humilló a GTA 6. Y no es por lo que crees. Cuidado, el detalle que viene después podría cambiar lo que piensas de GTA 6.",
     "GTA 5 vendió más de 215 millones de copias desde 2013, según Take-Two.",
     "Eso lo convierte en uno de los juegos más vendidos de la historia.",
     "Y GTA 6 partió fuerte: 32,5 millones vendidos antes de salir.",
     "Suena enorme. Y lo es.",
     "Pero hay un cálculo que casi nadie hace.",
     "Esos 32,5 millones son apenas el 15 por ciento de lo que lleva GTA 5.",
     "Para alcanzarlo, GTA 6 tendría que vender casi siete veces lo que ya vendió.",
     "Pero a GTA 5 le tomó 13 años llegar ahí. GTA 6 recién empieza.",
     "Comenta si crees que GTA 6 lo va a superar y en cuánto tiempo. Sigue el canal para más números de GTA 6."]
REEMPLAZOS = [("GTA 5", "GTA cinco"), ("GTA 6", "GTA seis"), ("215 millones", "doscientos quince millones"), ("desde 2013", "desde dos mil trece"), ("Take-Two", "Téik Tu"),
              ("32,5 millones", "treinta y dos coma cinco millones"), ("15 por ciento", "quince por ciento"), ("13 años", "trece años")]
PAUSAS = [1, 5, 6, 9]
CLAVES = {"x_hum": (1, "humilló"), "x_yno": (1, "Y"), "x_cui": (1, "Cuidado"), "x_215": (2, "215"), "x_mill": (2, "millones"), "x_desde": (2, "desde"), "x_2013": (2, "2013"), "s_3": ("L", 3),
          "x_partio": (4, "partió"), "x_325": (4, "32,5"), "x_antes": (4, "antes"), "s_5": ("L", 5), "s_7": ("L", 7), "x_325b": (7, "32,5"), "x_15": (7, "15"), "x_lleva": (7, "lleva"),
          "x_siete": (8, "siete"), "x_13": (9, "13"), "x_recien": (9, "recién"), "x_tell": ("L", 10), "s_cta": (10, "Sigue")}
PLANOS = [("01", "p01", None, "gancho: cenital de la pista, de la partida al auto que va adelante"),
          ("02", "p02", ("L", 2), "travelling por el contador y los años"),
          ("03", "p03", ("L", 4), "plano bajo en la salida"),
          ("04", "p04", ("L", 6), "cenital con la cinta de medir"),
          ("05", "p05", ("L", 8), "la cámara recorre los siete tramos"),
          ("06a", "p06a", ("L", 9), "el calendario de GTA 5"),
          ("06b", "p06b", (9, "GTA", 1, -0.1), "corte por coincidencia al calendario de GTA 6"),
          ("07", "p07", ("L", 10), "plano general, carriles abiertos; cierre")]
CIERRE = {"cierre": "¿LO VA A SUPERAR?", "cierre2": "Comenta: sí o no", "paises": ["SÍ", "NO"], "cta": "SIGUE EL CANAL", "like": "LIKE"}
SFX = [("x_hum", -.25, "transicion/whoosh_03.wav", .5, .06), ("x_215", -.03, "ui/pop_01.wav", None, .08), ("x_desde", -.1, "transicion/pasada_larga_02.wav", None, .05), ("x_2013", 0, "ui/pop_02.wav", None, .06),
       ("c03", -.28, "transicion/whoosh_02.wav", .28, .06), ("x_325", -.03, "ui/pop_01.wav", None, .08),
       ("c04", -.28, "transicion/whoosh_01.wav", .28, .05), ("x_15", -.03, "ui/ding_01.wav", None, .06),
       ("c05", -.28, "transicion/whoosh_02.wav", .28, .05), ("x_siete", 0, "ui/pop_01.wav", None, .07),
       ("c06a", -.28, "transicion/whoosh_01.wav", .28, .05), ("c06a", .25, "sintet/hoja.wav", None, .05), ("c06a", .6, "sintet/hoja.wav", None, .05), ("c06a", .95, "sintet/hoja.wav", None, .05), ("x_13", 0, "ui/pop_02.wav", None, .07),
       ("c06b", -.05, "impacto/kick_01.wav", .16, .07), ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]
PORTADA = ("HUMILLÓ A GTA 6", 0.2)
PUBLICAR = "Vie 27/11 19:00"
DESC = "Y no es por lo que crees. 😳\nFuente: Take-Two Interactive."
FIRMA = "Sigue a @ViceVersoGG 🎮"
TAGS = "#GTA6 #Shorts #RockstarGames #GTAVI #Gaming"
PREVIA = [(0.2, "01 la partida"), (1.3, "01 el que va adelante"), (3.2, "01 los dos carriles"), (6.6, "01 GTA 6"), (9.6, "02 215 millones"), (11.2, "02 desde 2013"), (14.6, "02 lo recorrido"),
          (17.6, "03 32,5 antes de salir"), (21.2, "03 enorme"), (23.6, "04 la cinta"), (27.4, "04 15 %"), (30.6, "05 tramos"), (32.4, "05 casi siete"), (35.3, "06 13 años"), (37.3, "06 recién empieza"), (44.0, "07 cierre")]
NIVEL_FX = 1.0   # producido antes del cambio de nivel del 27-nov: se conserva el nivel con que se aprobó
