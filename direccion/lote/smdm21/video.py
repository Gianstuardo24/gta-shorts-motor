"""MDM 21h · NASA LOST a Spacecraft Over ONE Detail 🚀❌ · guion final del 28-nov (GUIONES_FINALES_28nov.md), palabra por palabra.
Dirección: paquete de escenas de Tao del 27-nov 19:10 (DIRECCION_VISUAL_28nov.md): una escena por línea. Las etiquetas "G2:" y "CTA:" no se dicen."""
ID, LOTE, CANAL, HORA = 'smdm21', 'LOTE28_SMDM21', 'MillionDollarMistake', '21'
MARCA, TEMA = 'MILLION DOLLAR MISTAKE', "mdm"
TITULO = 'NASA LOST a Spacecraft Over ONE Detail 🚀❌'
VOZ = ('bm_george', 1.25, 'en-gb')
F = ['NASA lost a hundred-million-dollar spacecraft over one detail. And that detail is something you learned in school.',
     'In December 1998, NASA launched a probe called Mars Climate Orbiter.',
     'Its job was to circle Mars and study its weather.',
     'It flew for more than nine months. Everything looked normal.',
     'In September 1999, it fired its engine to enter orbit and passed behind the planet.',
     'It never came back out.',
     'Now the detail you learned in school, the one nobody caught for months.',
     "It wasn't the engine. And it wasn't the computer on board.",
     "Two teams were sharing numbers about the thrusters. The contractor wrote them in pounds of force. NASA's team read them as newtons.",
     'One pound of force is about four and a half newtons. So every small correction was miscalculated by that much.',
     "After nine months of small errors, the probe arrived far too low, deep in Mars's atmosphere. It was never heard from again.",
     'Lesson: never assume the other team means what you mean. Check the units.',
     'Tell me if you still mix up miles and kilometers. Follow for the next million dollar mistake.']
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
FIRMA = '💸 Million Dollar Mistake · Big ideas. Bigger mistakes.'
TAGS = '#Shorts #MillionDollarMistake #business #mistakes #history'
PREVIA = "auto"
INCLUYE = ["b28.js"]
CARPETA = "/mnt/user-data/outputs/lote28/MillionDollarMistake"
# ---------- ajustes propios del video (se agregan debajo) ----------
REEMPLAZOS = [('December 1998', 'December nineteen ninety-eight'), ('September 1999', 'September nineteen ninety-nine')]
CLAVES.update({"x_lost": (1, "lost"), "x_detail": (1, "detail."), "x_school": (1, "school."), "x_launched": (2, "launched"), "x_called": (2, "called"),
               "x_weather": (3, "weather."), "x_nine": (4, "nine"), "x_normal": (4, "normal."), "x_fired": (5, "fired"), "x_behind": (5, "behind"),
               "x_school7": (7, "school,"), "x_months": (7, "months."), "x_engine": (8, "engine."), "x_computer": (8, "computer"),
               "x_contractor": (9, "contractor"), "x_pounds": (9, "pounds"), "x_nasa9": (9, "NASA's"), "x_newtons": (9, "newtons."),
               "x_four": (10, "four"), "x_every": (10, "every"), "x_much": (10, "much."), "x_low": (11, "low,"), "x_deep": (11, "deep"), "x_never": (11, "never"),
               "x_check": (12, "Check")})
CIERRE = {'cierre': 'MILES OR KILOMETERS?', 'cierre2': 'Do you mix them up? Comment', 'paises': ['YES', 'NEVER'], 'cta': 'FOLLOW FOR MORE', 'like': 'LIKE'}
SFX = [("x_detail", .9, "tao/alerta_suave.wav", None, .04),            # 01: la sonda se pierde detrás del planeta
       ("x_launched", -.45, "tao/pasada_nave.wav", None, .04),         # 02: despegue
       ("x_called", -.25, "tao/toque_01.wav", None, .045),             # 02: corte a la sonda suelta
       ("x_nine", -.05, "tao/clic_05.wav", None, .045),                # 04: nueve meses
       ("x_fired", -.02, "tao/whoosh_salto.wav", None, .04),           # 05: enciende el motor
       ("c06", .4, "sintet/baja.wav", .7, .04),                        # 06: la señal queda plana
       ("x_school7", .0, "impacto/kick_01.wav", .25, .055),            # 07 · G2: pulso de alerta
       ("x_engine", -.05, "tao/desequipar.wav", None, .045), ("x_computer", .15, "tao/desequipar.wav", None, .045),   # 08: sospechosos descartados
       ("x_pounds", -.2, "tao/clic_06.wav", None, .05),                # 09: libras-fuerza
       ("x_nasa9", -.8, "tao/whoosh_carril.wav", None, .035),          # 09: travelling por la línea
       ("x_newtons", -.2, "tao/clic_06.wav", None, .05),               # 09: newtons
       ("x_four", -.1, "tao/equipar.wav", None, .05),                  # 10: la balanza se equilibra
       ("x_deep", -.3, "sintet/baja.wav", .8, .045),                   # 11: entra demasiado bajo (sin explosión)
       ("x_check", .3, "tao/clic_positivo.wav", None, .05),            # 12: reglas alineadas y verificadas
       ("x_tell", -.1, "tao/whoosh_carril.wav", None, .04)]
PORTADA = ("LOST OVER ONE DETAIL", 2.4)
DESC = "One detail you learned in school cost NASA a spacecraft. 🚀\nMars Climate Orbiter, September 1999: pounds of force were read as newtons."
