# RECETA DIARIA (Shorts) — apuntes para retomar si pierdo contexto
- Carpeta del día: /home/claude/dNN/<slot>/  (slots: gen14 gen19 = GTA EN TheViceVerseGG · ges19 ges22 = GTA ES ViceVersoGG · dog14 dog18 = DogDecoded · cat16 cat21 = CatDecoded · c17 c21 = ChiChibitsTV (café) · m18 m21 = MillionDollarMistake · r18 r22 = TheRabbitLoop)
- Cada video: b.py (copiado/adaptado del día anterior; importa dNN/comun.py) genera <ID>_src.json → /home/claude/hacer.sh DIR ID voz vel lang pausa → /home/claude/render_par.sh DIR/ID.json DIR/vz.wav DIR/vz_palabras.json DIR/v1.mp4 deep
- Luego: portada (escena/portada.py v1.mp4 SEG "TEXTO" portada.jpg), txt (txt.py), ficha (ficha.py). Ver mk.sh.
- Entrega: copiar a /mnt/user-data/outputs/dNNn/ y device_commit_files a ~/Desktop/YouTube/<Canal>/2026-11-DD <Día>/"HHh - Título sin emoji".{mp4,txt,portada.jpg}; ficha json → ? (ver cómo se hizo: outputs/d23n/*.json nombrados Canal_fecha_HHh.json)
- Reglas: verdad con 2+ fuentes · sin preguntas con signos en la voz · título ≤45 car. · descripción corta sin revelar + firma + 4–5 hashtags · sin "VIDEO RELACIONADO" · CTA final hablado · nunca 2 renders en paralelo · no repetir temas (ver lista en d22/d23 y Desktop/YouTube/*/Subidos)
- Temas ya usados d22–d23: ver `for x in d2*/*/; ...*_src.json` (titulo)

## Lecciones del 24-nov (tanda d24)
- **Cola de renders:** usar SIEMPRE `/home/claude/d24/q.sh SLOT ID VOZ VEL LANG [joven]` (flock en /tmp/render.lock). Nunca lanzar `uno.sh` directo: dos renders a la vez = prohibido.
- `uno.sh` deja hoja de control en `/tmp/qc_SLOT.jpg` (8 cuadros). `empacar.sh` arma mp4+txt+portada+ficha en `/mnt/user-data/outputs/d24n/`.
- **Utilería con contenido fijo de otro video (NO usar):** `calendarioP` (muestra "MARCH 13 1997"), look `oficial` (funcionario otomano con turbante), set `investigaV` (fotos de ovnis en el tablero: solo Rabbit), `oficina81V`, `tiendaJuegosV` (solo GTA). Para fechas: `documento` con `sello`.
- **Encuadre:** actores entre cam+150 y cam+930. Un zoom con x lejos del personaje lo saca de cuadro: centrar el zoom entre personaje y objeto, s<=1.15 si hay dos cosas; s 1.2-1.3 solo sobre la cara.
- Burbujas: `dx` hacia el centro de pantalla; con zoom activo se cortan.
- `"gamer", var=81` sale canoso con lentes: fijar `pelo`, `camisa`, `lentes=False`.
- Marcadores: el regex se compara con las palabras de `frases` (texto escrito, p. ej. "^1976", "^3"). En español usar palabras iguales en frases y voz.
- Variedad pedida por Tao (vale para Shorts y largos): por video, 2+ cortes a detalle distintos (`insertar`), entrada caminando (`pose camina` con dos keys de x), zoom a la cara en la reacción, sets distintos por zona. Pendiente: llevar `planos.js` (largos) al motor de Shorts `escena.html`.
- Al salir de un `insertar` hay 1 cuadro de barrido (fondo neón con líneas): es del motor, no un error del guion.
- `chk.py [slots]` (en d24): avisa zooms con x dentro de un inserto (rompen el corte a detalle) y actores fuera de cuadro. Pasarlo ANTES de encolar.
- `cartelPiso` es un cartel de "piso mojado" (no acepta texto): para letreros usar `cartel` con `texto` (y~1180). `botella1899` es una botella de gaseosa. `casaPalmasV` con casa dice "BELVILLE": usar `sinCasa`.
- Títulos `grande` chocan con letreros del set (`tiendaJuegosV`, `cuartoGamerV`): no usar `grande` ahí.
- Portada: elegir un segundo que NO sea el cuadro de barrido de salida de un inserto; el signo "≠" no existe en la fuente.
- Nombre de archivo sin ":" al entregar al Mac.
- Tanda del 24-nov: 14 videos entregados en ~70 min (18:35–19:40), con ~2 min por render y 1–3 renders por video.

## Desde el 24-nov noche: flujo nuevo de Shorts
- **Cola con planificador:** `d24/q2.sh SLOT ID VOZ VEL LANG [joven]` (usa `uno2.sh`: b.py → voz → `post.py` (caminatas) → `planos_shorts.py` → render). No escribir `zoom` a mano: `"zoom":[]`. Forzar un plano: `"planos_hint":[{"k":"marca","tipo":"primer","var":N}]`.
- **Revisión:** `python3 ver_planos.py SLOT` → `/tmp/pl_SLOT.jpg` (un cuadro por plano con su tipo). `python3 medir.py SLOT/v1.mp4` (quietud y cambios). `python3 chk.py SLOT`.
- **Caminar:** key con `"a":[x,y],"dur":1.3,"ease":"eio"` (parte fuera de cuadro: cam-140).
- **Guion:** título primero (disparador emocional, molde corto) → 1.ª frase sigue el disparador y NO revela → desarrollo → revelación en la penúltima frase → "Tell me…" → "Follow…".
- **Sets:** evitar los base (oficina, estudio, calle, sala, cafe, garage, banco): son oscuros y la cara queda apagada. Usar sets V y no repetir set en un video.
- **Durante un inserto:** terminar antes (`fin`) las cifras y títulos grandes que choquen con el papel o el objeto (texto sobre texto).
- Objetos nuevos: `bolsaCafe{texto,sub,color}`, `granos{n,color}`, `cafetera`. `prohibidos:[{"k","x","y","r"}]` dibuja el círculo de prohibido.

## Formato cerrado con Tao (24-nov, 21:40) — usar desde el 25-nov
- **Guion (9-10 frases):** 0 gancho que sigue al título + promesa · 1-3 por qué/desarrollo · 4 primera respuesta · 5 "And here is the part…" (segunda pregunta) · 6 segundo dato · 7 "Tell me…" · 8 "Follow…".
- **Título:** primero. Corto, cotidiano, con disparador emocional (Don't Trust / Stop / Don't Do This / He Lost / Nobody Can / humilló). Emojis de emoción o prohibición. Los dos del canal con disparadores distintos. Nada que el video no pague.
- **Portada:** el cuadro del gancho o de un detalle que NO revele la respuesta (no cifras finales). Evitar el instante del fundido (queda oscuro): usar la mitad del inserto.
- **Escenas:** 5-6 sets V distintos + 4-5 insertos (uno con `papel`), títulos chicos numerados "1 · …", `prohibidos` en el gancho si el título es una negación.
- **insertar(E,k_in,k_out,vuelta,…):** `vuelta` = x de cámara de la zona en que se está (0, 1300, 2600…). Si k_out no tiene paneo propio y `vuelta` está mal, la cámara vuelve a otra escena (error de m21n).
- **Cola:** `q2.sh`; revisar con `ver_planos.py`, `medir.py`, `chk.py`; empaquetar con `empacar2.sh` (prefijo NUEVO) o `empacar.sh` (por hora).
- Plantillas buenas: `d24/c17n/b.py` (café), `d24/gen14n/b.py`, `d24/ges19n/b.py`, `d24/cat16n/b.py`, `d24/dog14n/b.py`.

## 24-nov 23:40 — estándar nuevo de Shorts (muestra 2 del descafeinado aprobada para mostrar)
- Plantilla: `d24/c17n/b.py` (7 escenas, `"cuerpo":"pro"`, `emojis`, `tazaPremium`, `remojo`, `mitad` como inserto, `neblina`, `humo`, `lamparaPie`, `mesaCentro`, `mesaLab`).
- Tema de fondo por canal automático en `comun.guardar()` (TEMAS). Poner `"cuerpo":"pro"` en cada guion.
- Textos: sueltos, sin marcos, sin borde negro, sin líneas. No amontonar.
- Respaldos del motor: escena.html.bak_24nov_2255 / _2305 / _2312 / _2345 / bak_25nov_0010 / _0030.
- 25-nov 00:40: muestra 4 = plantilla final c17n. Cada guion lleva "pausa_larga_antes":[1, i_gancho2, i_gancho2+1, i_cta]. Títulos sin número (el motor los quita). Audio: whoosh −0,34 s, ganancia fija, arranque() en voz.
- Criterios de escena generales: doc 04, sección "Criterios de escena para CUALQUIER tema de Short".

## 25-nov madrugada — tanda del 25 (formato.py)
- Guiones con `d24/formato.py` → `video(...)` (escenas de alto nivel: {"z": set, ...} o {"i": fondo3, ...} inserto). Slots d24/wr1..wm2. Empaquetado: `d24/lista25.sh` (funciones v_SLOT [seg_portada]) → empacar25.sh → /mnt/user-data/outputs/d25/<Canal>/.
- Horarios por canal (de los slots del 24): MDM 18/21 · GTA EN 14/19 · GTA ES 19/22 · Dogs 14/18 · Cats 16/21 · Coffee 17/21 · Rabbit 18/22.
- Lecciones de la noche: patrones de marcadores en MINÚSCULA ("^leonida"); el motor ahora acepta "marcador+0.5" (tk); los cortes de cámara son instantáneos (antes 2 cuadros de fondo vacío); prohibido sobre un inserto: {"ins": n}; humo/neblina/lámpara/rótulo no cuentan como objeto para el planificador; barras2 acepta etiqueta [valor, nombre, color, "32,5"]; pose `explica` = codos abajo y antebrazos abiertos (revisar hoja_poses.py cada vez).
- Escenas especiales nuevas: `marNocheV` {barco, jet, mira, tri, tictac, hora:'atardecer'}, `montanaV` {avion, objetos}. Objetos: dron, nvPantalla, bokehNV, capas, bote, zapatilla (sin logo), anillo, cajaGato, visionPerro, periodico, sobre, rebota, calendario, rotulo, humo, neblina, lamparaPie, mesaCentro, mesaLab, tazaPremium, remojo, mitad{n0,n1,half,sinReloj}.
