"""MDM 21h · Blockbuster LOST Everything in ONE Decision · guion oficial del 25-nov (GUIONES_FINALES_25nov.md), palabra por palabra.
Dirección: paquete 7 del lote (27-nov). Las etiquetas "G2:", "Lesson:" y "CTA:" del documento no se dicen. Sin logos: no hay archivos."""
ID, LOTE, CANAL, HORA = "mdm21", "LOTE_MDM21", "MillionDollarMistake", "21"
MARCA, TEMA = "MILLION DOLLAR MISTAKE", "mdm"
TITULO = "Blockbuster LOST Everything in ONE Decision 📼❌"
VOZ = ("bm_george", 1.25, "en-gb")
F = ["Blockbuster lost everything. And it all came down to one decision. But there's a detail almost nobody knows.",
     "In 2000, Blockbuster was the king of movie rentals, with about 9,000 stores.",
     "Netflix was a small startup mailing DVDs, and losing money.",
     "Its founders got a meeting with Blockbuster's CEO. Their offer: sell Netflix for 50 million dollars.",
     "He listened. At first, he laughed, and then he followed with a flat no.",
     "Now the detail almost nobody knows.",
     "Netflix's founders got the invitation less than 12 hours before the meeting. With the clock against them and almost broke, they spent money they didn't have on a jet, just to hear that no.",
     "They walked in wearing shorts, flip-flops and a Hawaiian shirt.",
     "Ten years later, Blockbuster filed for bankruptcy. Netflix became worth billions.",
     "Today, only one Blockbuster is still alive, in Oregon.",
     "When a small player changes how people buy, take the meeting seriously.",
     "Tell me if you would have bought it. Follow for the next million dollar mistake."]
REEMPLAZOS = [("In 2000,", "In two thousand,"), ("about 9,000 stores", "about nine thousand stores"), ("for 50 million dollars", "for fifty million dollars"), ("less than 12 hours", "less than twelve hours")]
PAUSAS = [1, 5, 6, 11]
CLAVES = {"x_lost": (1, "lost"), "x_and1": (1, "And"), "x_but": (1, "But"), "x_king": (2, "king"), "x_9000": (2, "9,000"), "x_small": (3, "small"), "x_mailing": (3, "mailing"), "x_losing": (3, "losing"),
          "x_offer": (4, "offer"), "x_50": (4, "50"), "x_listened": (5, "listened"), "x_laughed": (5, "laughed"), "x_followed": (5, "followed"), "x_no": (5, "no"),
          "x_inv": (7, "invitation"), "x_12": (7, "12"), "x_broke": (7, "broke"), "x_spent": (7, "spent"), "x_jet": (7, "jet"), "x_hear": (7, "hear"),
          "x_shorts": (8, "shorts"), "x_flip": (8, "flip"), "x_haw": (8, "Hawaiian"), "x_later": (9, "later"), "x_filed": (9, "filed"),
          "x_one10": (10, "one"), "x_oregon": (10, "Oregon"), "x_take": (11, "take"), "x_tell": ("L", 12), "s_cta": (12, "Follow")}
PLANOS = [("01", "p01", None, "gancho, macro: el VHS y el reflejo de la tienda vacía"),
          ("02", "p02", ("L", 2), "transición por el reflejo: travelling por los estantes"),
          ("03", "p03", ("L", 3), "cenital de la caja postal y el DVD"),
          ("04", "p04", ("L", 4), "plano frontal fijo: la mesa de la reunión"),
          ("05", "p05", ("L", 5), "detalle: la mano y la carpeta"),
          ("06a", "p06a", ("L", 6), "corte seco en el no: cenital del reloj y la invitación"),
          ("06b", "p06b", (7, "With", -0.04), "corte por coincidencia del reloj al boleto"),
          ("07", "p07", ("L", 8), "plano bajo de la entrada"),
          ("08a", "p08a", ("L", 9), "transición temporal: diez años y la persiana"),
          ("08b", "p08b", (9, "Netflix", -0.04), "la sala con la pantalla"),
          ("09a", "p09a", ("L", 10), "plano general: el mapa esquemático"),
          ("09b", "p09b", ("L", 11), "cierre en la carpeta")]
CIERRE = {"cierre": "WOULD YOU BUY IT?", "cierre2": "Tell me. Comment", "paises": ["YES", "NO"], "cta": "FOLLOW FOR MORE", "like": "LIKE"}
SFX = [("0", .7, "impacto/kick_01.wav", .16, .07), ("x_lost", .45, "sintet/proyector.wav", .5, .05),   # 01: entra y sale el casete
       ("c02", -.28, "transicion/whoosh_02.wav", .28, .06),             # del reflejo a la tienda
       ("x_9000", -.03, "ui/pop_01.wav", None, .08),                    # 02: el contador se detiene
       ("x_mailing", 0, "sintet/hoja.wav", None, .06), ("x_losing", .05, "tematicos/moneda_01.wav", None, .06), ("x_losing", .45, "tematicos/moneda_02.wav", None, .05),   # 03
       ("x_offer", -.15, "sintet/hoja.wav", None, .06),                 # 04: la carpeta se desliza
       ("x_no", -.02, "impacto/kick_01.wav", .16, .09),                 # 05: el no
       ("c06a", .25, "sintet/tics.wav", 2.4, .05), ("x_12", -.2, "ui/pop_01.wav", None, .07),   # 06: el reloj y la nota
       ("x_spent", .05, "sintet/billetes.wav", None, .06), ("x_jet", -.3, "transicion/pasada_larga_02.wav", None, .06),
       ("x_filed", -.1, "sintet/baja.wav", None, .07),                  # 08: la persiana
       ("c08b", -.28, "transicion/whoosh_02.wav", .28, .05),
       ("x_oregon", -.12, "ui/ding_01.wav", None, .06),                 # 09: la única que queda
       ("x_tell", -.28, "transicion/whoosh_02.wav", .28, .07)]          # cierre
PORTADA = ("LOST EVERYTHING", 46.25)
PUBLICAR = "Vie 27/11 21:00"
DESC = "One meeting. One decision. One detail almost nobody knows. 📼\nSources: Fortune (2023); Marc Randolph, That Will Never Work; Marketplace."
FIRMA = "💸 Million Dollar Mistake · Big ideas. Bigger mistakes."
TAGS = "#Shorts #MillionDollarMistake #business #Netflix #Blockbuster"
PREVIA = [(0.5, "01 entra el casete"), (3.6, "01 el reflejo"), (6.8, "01 tienda vacía"), (7.3, "02 la misma, llena"), (11.4, "02 9,000"), (14.6, "03 sobre y DVD"), (18.4, "04 dos sillas"), (21.4, "04 la oferta"),
          (23.2, "05 la toma"), (26.2, "05 el no"), (29.6, "06 el reloj"), (32.6, "06 menos de 12"), (36.9, "06 el pasaje"), (41.4, "07 de espaldas"), (44.4, "08 diez años"), (45.9, "08 persiana"),
          (47.4, "08 la pantalla"), (51.4, "09 Oregon"), (54.8, "09 la carpeta"), (59.6, "09 cierre")]
NIVEL_FX = 1.0   # producido antes del cambio de nivel del 27-nov: se conserva el nivel con que se aprobó
