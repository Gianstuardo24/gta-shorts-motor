# MANUAL DE LA FÁBRICA DE SHORTS — lo aprobado por Tao

> Versión 22-nov-2026 (tarde). Son **decisiones del dueño**: se aplican siempre y no las cambia el análisis automático.
> Las reglas que salen de los datos (hooks, patrones) siguen en `datos/estrategia/reglas_vigentes.md`. Si chocan, **manda este manual**.
> Cada cambio nuevo que apruebe Tao se agrega aquí, con fecha.

---

## 1. Reglas fijas (todos los canales)

**Verdad y legalidad**
- Solo datos **verdaderos, verificados en 2 o más fuentes**. Si es estimación (ventas, costos), se dice **"estimación"** y quién la hizo.
- Nada de urgencia falsa, promesas de dinero ni "comparte o mala suerte".
- Material ajeno solo para **entender**. Nunca se usan tomas, audio ni marcas de agua de otros creadores.
- Visuales permitidos: material oficial, tomas propias, stock legal, imágenes de ChatGPT (marcadas como recreación) o **animación por código**. Sin caras reales, sin logos y sin deepfakes. Figuras públicas solo en contexto editorial.
- **Nunca se republica el mismo video.**

**Formato que funciona (20-nov):** el video **animado por código ("escena")** rinde mejor que las imágenes o las tomas en movimiento.
- La animación **recrea lo que va diciendo la voz**: textos, cifras, objetos y escenas que aparecen justo cuando se nombran.
- Tiene que ser **sofisticada**: muchas luces, profundidad y movimiento. Nada de tarjetas o stickers genéricos.
- Los elementos gráficos **dependen de cada video**, no hay un set fijo por canal. Por ejemplo, el café no siempre lleva granos y vapor.
- Mapas: estilo **mapa de GTA visto desde arriba**, con cuadras y colores por zona, no una mancha.
- El texto de arriba (subtítulos) va en el **idioma del guion**, con las palabras clave resaltadas.
- **Contar la historia con personajes (21-nov):** personajes propios estilo juguete (`figura`) que **hacen cosas**: caminan, se pasan objetos, reaccionan (salto, temblor), se sientan a jugar o celebran. Nada de personajes quietos.
- **Variedad:** cada personaje con cuerpo, peinado, ropa y rasgos distintos (`var`), y decorados distintos (sala, oficina, garage, cabina, trono, café, cielo, calle, estudio).
- **Transiciones de cine** cuando suman: barrido rápido, zoom de entrada, subida o zoom a un detalle en el remate. A veces conviene una escena continua sin corte, o un gráfico de datos.
- **Portada (21-nov):** cada video lleva `.portada.jpg` (fotograma con personajes + título grande, palabra clave en color), hecho con `escena/portada.py`. Si hay una cifra que cuenta, el fotograma va **después** de que termina de contar.
- **Meta de calidad:** ver `claude/referencia-calidad-21-nov.md`.

**Guion**
- **Lenguaje simple**, que entienda cualquiera. Sin palabras raras: por ejemplo, "probe" → "ship".
- **Menos información es mejor:** una idea central, contada clara.
- Gancho al inicio y cierre que invita a comentar. **Sin preguntas directas en la voz** (ver §6).
- **No empezar una frase con una palabra de una letra (22-nov):** la voz se la come ("O sea" → "Es decir", "Y eso…" → "Eso…").
- Las cifras se escriben con número en pantalla y en palabras para la voz (`frases` vs `frases_voz`).
- **Revisión:** si un guion no pasa `revisar.py`, **no se detiene ni se deja de lado**. Se corrige y se vuelve a revisar hasta que pase.

**Voz**
- Kokoro (local). GTA ES **`em_santa` más joven** (`joven.py`) · GTA EN, Rabbit y Café `am_michael` · MDM `bm_george` · Perros `af_heart` · Gatos `bf_emma`.
- La voz IA no entona bien las preguntas: por eso se evitan en el guion (§6). Nunca subir el tono con el método que suena a **helio**.
- Busca una voz más orgánica (pendiente probar Chatterbox).

**Música**

| Canal | Música |
|---|---|
| GTA ES / EN | **deep** (tranquila) |
| Rabbit | **dark** (misterio) |
| Café, MDM, Perros, Gatos | **deep** |
| Repers **animados** (avatares, historias) | **funk** (`musica_funk.py`, `repers/musica/funk-01..05.mp3`) |
| Repers **con personas** | **se alterna**: música de la app con su **drop** y el funk nuevo |

- **Nada de música animada ni infantil** ("de cabros chicos") en GTA, Rabbit ni en los Repers animados.
- **Repers (22-nov):** el beat tiene que **empezar antes** en el audio (pedido sobre "Cuando tu hijo te reta").
- Volumen final −14 LUFS.

**Efectos de sonido**
- **Prohibido** el whoosh largo que suena a giro (`WhipWhoosh_SEU04.8` / `whoosh_01`). Los whoosh cortos sí.
- **Pops más bajos.** No repetir el mismo efecto: hay que variar.
- Los efectos tienen que **calzar con el tema**: motor de auto en GTA, glitch o electricidad en aliens, caja registradora en precios.

**Títulos**
- **Cortos: hasta ~40 caracteres**, para que no se corten en el celular. Una idea, con el número o el misterio al principio.
- Emoji al final opcional (💸 👽 ☕ 🐶 🐱).

**Descripciones**
- **Insinúan y dejan la duda; no cuentan el video.** Sin precios, cifras ni el remate. Sin pregunta para comentarios.
- 1 o 2 frases cortas (máximo ~20 palabras), luego un **CTA breve**, luego **4–5 hashtags**.
- Si el video usa estimaciones, se agrega una línea de **fuente**.
- **La gente no lee la descripción:** lo que tiene que quedar, va en el gancho y el título.

**Publicación**
- **Sin comentario fijado.** Solo **título + descripción**.
- Los videos quedan en `~/Desktop/YouTube/<canal>/<día>/HHh - título.mp4` con su `.txt`. **Tao los ve y los descarga desde la página del Estudio**, que lee esa misma carpeta: reemplazar el archivo = reemplazarlo en la página.
- **Panel (22-nov):** en la sección VIDEOS, los próximos se ven en **bloques chicos por canal**. La sección "para subir ahora" no cambia.
- **Cada video con su `.txt` al lado.** Si un video se marcó como subido, su `.txt` se va a `Subidos`: no volver a dejar el video en la carpeta del día.
- En el celular: botón 📱 del panel (QR) → copiar título y descripción, guardar el video y marcarlo como subido. El Estudio se abre con `./venv/bin/python3 estudio.py` (ahí está `segno`, que dibuja el QR).

**Imágenes de marca** (logo y banner): se hacen en ChatGPT, **que no se vean tan IA**. El logo va pensado **circular**. Banner de YouTube: mínimo 2048×1152, todo lo importante dentro de la zona central.

---

## 2. Por canal

**Horas (22-nov, según los datos de vistas por hora de subida):** GTA EN pasa a **14h y 19h**, MDM a **18h y 21h**; el resto sigue igual. Se revisa el 29-nov.
**Perros y gatos a 2 al día (22-nov, desde el lunes 23):** perros **14h y 18h**, gatos **16h y 21h**.

### ViceVerso (GTA ES) — 2 al día (19h y 22h)
- **El juego ya salió (19-nov).** Todo en presente.
- **Micronicho en test (21-nov): "Los números de GTA 6"**. Fórmula: "GTA 6 tiene que ___ para ___".
- Ventas y costos siempre como **estimación**, con quién la hizo.
- Gatillos que rinden: **aversión a la pérdida** y consecuencia real para el jugador.
- Si un video programado ya no tiene sentido, **se descarta**.
- **No repetir:** el tema del mapa y Corea del Sur, Miami sin tomas reales para contrastar.
- ES y EN: **mismo tema con ángulo distinto**, nunca el mismo video el mismo día.

### TheViceVerse (GTA EN) — 2 al día (14h y 19h)
- **Micronicho en test (21-nov): "Hidden mechanics"**. Fórmula: "GTA 6 Has a Secret ___".
- Cada mecánica verificada en 2+ fuentes. **Inglés simple**.
- Robos de auto: mostrar con calma cómo saca al conductor; el personaje no desaparece de golpe.

### The Rabbit Loop — 2 al día (18h y 22h)
- **100 % aliens. Micronicho en test (21-nov): "Casos OVNI cerrados"**. Fórmula: "The ___ UFO Was Finally Solved".
- Tono de misterio, **música dark**, nada infantil.

### Coffee, But Why? (@ChiChibitsTV) — 2 al día (17h y 21h)
- **Micronicho en test (21-nov): "El café prohibido"**. Fórmula: "A ___ Tried to Ban Coffee".
- **Informativo, nunca médico.**

### Million Dollar Mistake — 2 al día (18h y 21h)
- **Micronicho: "Lo vendió por $X, hoy vale $Y"**. Casos en `claude/mdm-banco-casos-21-nov.md`; el valor de "hoy" se verifica el día del video.
- Títulos cortos que dejan la duda. Cada caso como **mini película** con personajes. Cierre con **enseñanza**.
- No se dibujan personajes con derechos (Superman, Marvel…): se cuenta con documentos, cheques y cifras.

### The Dogs Decoder y The Cats Decoder — 2 al día (perros 14h y 18h, gatos 16h y 21h)
- Handles **@TheDogsDecoder** y **@TheCatsDecoder**. Paquete completo en `claude/canales-perros-gatos-21-nov.md`.
- Micronicho "Why your dog/cat does that", con ciencia. Protagonistas fijos: **Biscuit** (perro dorado, collar rosa) y **Mochi** (gata atigrada gris).
- Solo conducta con estudio o fuente veterinaria. **Nada de salud.**
- Para medirlos hay que autorizar cada canal en `metricas.py --autorizar` (lo hace Tao).

### Number Signs — **en pausa**

### Repers — 1 al día por cuenta (IG, TikTok, YT)
- Se intercalan videos **con personas** y **animados**. Se prueba una estructura a la vez y se mide.
- Textos alineados al nicho (nostalgia Kinect, sin control, sin VR). Aprobado: "es como el Wii, pero en el celular" / "Like the Wii, but on your phone".
- **Desde el próximo post (21-nov): el Wii o el Kinect van en el gancho o el título**, no solo en la descripción, porque la gente lee el gancho y no la descripción.
  - Siempre como comparación ("como el Wii…", "like Kinect…"), con Repers visible y sin logos de Nintendo ni Microsoft.

---

## 3. Micronichos y test (21-nov)

**Ritmo:** máximo **2 videos al día por canal**.
**Calendario:** días de test en `datos/tests.json` (🟡 TEST del 21-nov al 4-dic, 🔴 ANÁLISIS el 29-nov y el 5-dic).

**Regla:** un solo micronicho por canal, con la misma fórmula de título, gancho y gráfica, hasta agotarlo.

| Canal | Micronicho | Test |
|---|---|---|
| GTA ES | Los números de GTA 6 | 7 días (14 videos) |
| GTA EN | Hidden mechanics | 7 días (14 videos) |
| Rabbit | Casos OVNI cerrados | 7 días (14 videos) |
| Café | El café prohibido | 10 días (10 videos) |
| MDM | Lo vendió por $X, hoy vale $Y | ~2 semanas |
| Perros / Gatos | Why your dog/cat does that | 1 semana (2 al día, 14 videos) |

**Cómo se decide (cada domingo):** % que lo vio vs. pasó de largo, % promedio visto, suscriptores por cada 1.000 vistas, contra el promedio de los 14 días anteriores. Mejora en 2 de 3 → **se queda**. Empeora en las 3 → **nicho de reserva**.

## 4. Reglas del algoritmo (21-nov, de Mario Ruiz)
1. **No mezclar temas** dentro del nicho.
2. **Personalidad:** tráiler del canal con la voz de Tao (pendiente).
3. **Ángulo específico**, nunca temas generales.
4. **Mirar los datos** desde los 3–4 primeros videos.
5. **Encadenar videos** con listas de reproducción por micronicho (y pantallas finales en videos largos). **En el `.txt` NO va `VIDEO RELACIONADO`** (22-nov): Tao copia la descripción completa.
6. Canal nuevo: usarlo como humano unos días antes de subir.
7. **Gancho:** atacar algo que el público ya cree + promesa + promesa mayor.
8. **Título y miniatura** hablan de lo que quiere el espectador.
9. **El video cumple lo que promete el título.**

## 5. Cómo se trabaja
- **Avisar antes** de cambiar código existente. Archivos y contenido nuevo se pueden hacer directo.
- **Día por día (22-nov):** los videos se generan desde cero **un día a la vez**. Se adelantan más días solo cuando el nicho está claro.
- **Esperar todo el feedback** de Tao antes de regenerar: no rehacer el mismo video muchas veces por cambios sueltos.
- Tareas pesadas **de a poco**. El Mac no queda prendido de noche.
- Las contraseñas y los cambios de cuenta los hace Tao. Nunca mostrar claves, tokens ni correos.
- **Mientras se renderizan videos para hoy, no se prueban otras cosas en paralelo** (el contenedor tiene 2 núcleos y todo se atrasa).
- **Antes de dar un video por listo:** buscar `?` en `frases_voz`, revisar que nada choque (tarjetitas, globos, números), mirar el cierre y confirmar que tiene su `.txt`.
- Si se pierde la conexión con el Mac, los videos se mandan por el chat para que Tao los descargue.

## 6. Estilo "película" (21-nov, aprendido con Tao)
Motor: `escena/escena.html`, tipo `pelicula`. Una sola escena continua por video, dividida en **zonas** que la cámara recorre.

**Imagen**
- **Pantalla completa** siempre. Excepción: Rabbit abre con el **encuadre de cámara** y luego se abre (`abre`).
- **Lento y fluido:** paneos y zooms ~1.6× más largos, sacudidas suaves.
- **Se construye de a poco:** primero el suelo, luego los elementos.
- **Luz de noche variada** por zona. Viñeta.
- **Vida de fondo:** gente caminando, alguien mirando a los lados (`extras`).
- **Mostrar, no escribir:** zoom al detalle, dinero que cae, el teléfono con la app, la tablet, el mando, la barra de energía, números que cuentan.
- **Títulos clave grandes** de neón (`grande:true`), como PIXAR.
- **Decorado `cielo`:** la luna queda arriba a la derecha y choca con subtítulos y marca. En esas zonas, zoom ≥1.1 centrado en y ~1420 para que la luna salga de cuadro.

**Textos de arriba y distancias (22-nov)**
- **Los elementos siempre mantienen distancia entre sí.**
- **Subtítulos: máximo 2 líneas** (terminan en y≈390). Si la frase no cabe, se muestra en partes seguidas (lo hace el motor).
- **Etiqueta (título) en y 525**, separada de los subtítulos.
- **Tarjetita bajo la etiqueta:** y 640. Sin etiqueta, sube a 525. Bajo un título grande: 720.
- **Cifras: y ≥ 850**, con su rótulo 110 px arriba. Si hay cifra y título grande a la vez, la tarjetita va bajo la cifra.
- Cifras y elementos se quedan **casi centrados**: así se ven como parte del video, separados de subtítulos y etiquetas.
- Letreros de neón del decorado detrás de una cifra o etiqueta: se quitan (`luz: tenue`).

**Nada tapa nada, nada choca**
- Los **globos** salen de la cabeza de quien habla (`de`). **No se cortan en el borde:** texto corto y, si hay zoom, centrado entre quien habla y el resto (`dx` para correr el globo).
- **Carteles, papeles y números** no tapan personas ni textos. Los papeles se apoyan en algo (escritorio, caja); no quedan flotando sobre la gente.
- **Tarjetitas: pocas.** El motor las ubica solo (ver distancias arriba). Si hay una cifra, nunca quedan encima de ella.
- Si no cabe, **zoom out** (`escala` 1.05–1.1).
- Los objetos que salen de una escena **no reaparecen** (`fin`), tampoco al pasar la cámara de vuelta.
- Los personajes que salen se **desvanecen**.
- El cierre aparece **después** de que se fue la última escena.

**Personajes = actores con rol**
- El protagonista tiene identidad fija. El resto **no se le parece**.
- Proporciones reales: el auto más alto que la mitad del cuerpo; dentro del auto solo se ve por la ventana (`dentro`). Para **agacharse en el auto**, el actor baja ~115 px y desaparece de la ventana.
- **Sentado de frente:** las dos piernas hacia abajo con rodillas. Nunca una pierna hacia el lado.
- **Sentado en el sillón:** delante del respaldo, sobre el cojín y con los pies en el suelo (con `sofa` y 1720 s 1.3 → actor y ~1714, `z` 1800). Nada de verse detrás o encima del sillón.
- Evitar transiciones que deforman, como pararse de una silla.
- **Animales siempre bien compuestos,** guiados por animales reales: lomo, grupa, muslo doblado, codo, rodilla, corvejón, almohadillas. Nada de patas como palitos o bloques. Tamaño real junto a una persona (perro `s` 1.0, gato ~0.9). Revisar en zoom con `muestras.py` antes de renderizar.

**Objetos nuevos (22-nov):** `linterna` (linterna de papel que flota), `baranda` (malecón), `muelle` (muelle sobre el agua, con ondas) y `volcan` (volcán con humo).

**Guion y voz**
- **Preguntas implícitas:** la voz IA dice las preguntas como afirmación. Vale también para el **gancho inicial** ("You'd think…", no "You think…?").
  - Se escribe "La pregunta es si ya lo recuperó", "Comenta si…" o "Tell me if…".
  - La pregunta va **grande en pantalla**.
- **CTA hablado** al final, por canal:

| Canal | CTA |
|---|---|
| Rabbit | "Follow for the next case." |
| GTA EN | "Follow for more GTA 6 secrets." |
| GTA ES | "Sigue el canal para más números de GTA 6." |
| MDM | "Follow for the next million dollar mistake." (favorito de Tao) |
| Café | "Follow for more banned coffee stories." |
| Perros | "Follow to decode your dog." |
| Gatos | "Follow to decode your cat." |

**Cierre**
- Pregunta grande, caja con "Comenta…" y opciones: los 3 **juntos y más arriba** (21-nov), bien separados del LIKE.
- Opciones **grandes, juntas y con el mismo espacio** entre ellas.
- **LIKE** con corazón y flecha corta al botón de like. **SEGUIR** con flecha al canal.
- Estilo de botones: **con relieve** (elegido por Tao, no el vidrio neón).
- El cierre usa el momento `s_fin`: si la última frase trae lección + "Tell me…", `s_fin` va en "Tell" y la lección tiene su propio momento.

**Herramientas**
| Archivo | Para qué |
|---|---|
| `muestras.py` | Cuadros sueltos para revisar sin renderizar |
| `ajustar_tiempos.py` | Mueve los tiempos si cambia la voz |
| `joven.py` | Voz más joven |
| `portada.py` | Portadas |
| `resolver.py` + `hacer.sh` (22-nov, en el contenedor) | Permiten escribir tiempos como `momento+0.4`; `hacer.sh` hace voz → tiempos → guion final de una vez |
| `metricas_plus.py` + `fichas.py` (22-nov) | Enganche real (vio vs. deslizó), curva de retención, fuentes de tráfico y la ficha de cada video (gancho, formato, voz). Fichas en `datos/fichas/` |
| `reporte_semanal.py` + `programar_reporte.sh` (22-nov) | Reporte de cada domingo 09:30 en `analisis/`, con la regla de §3 |
| `subir_youtube.py` + `GUIA_SUBIDA_API.md` (22-nov) | Sube y programa por API (permiso aparte en `secretos/subir/`). Solo con OK de Tao |
| `laboratorio_faceless.py` (22-nov) | Baja videos ajenos **solo para estudiarlos** (transcripción, hoja de cuadros, cortes) en `estudio_faceless/` |
| `kit/fabrica-shorts-kit.zip` (22-nov) | Versión para otras personas (Mac + su propio Claude) |

## 7. Canales nuevos
- **The Dogs Decoder** y **The Cats Decoder** (21-nov): paquete completo en `claude/canales-perros-gatos-21-nov.md`. Configuración en `canales/perros.json` y `canales/gatos.json`.
