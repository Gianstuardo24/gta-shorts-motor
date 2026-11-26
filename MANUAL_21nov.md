# MANUAL DE LA FÁBRICA DE SHORTS — lo aprobado por Tao

> Versión 21-nov-2026. Son **decisiones del dueño**: se aplican siempre y no las cambia el análisis automático.
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
- **Contar la historia con personajes (21-nov):** personajes propios estilo juguete (`figura`, escena `historia`) que **hacen cosas**: caminan, se pasan objetos, reaccionan (salto, temblor), se sientan a jugar o celebran. Nada de personajes quietos.
- **Variedad:** cada personaje con cuerpo, peinado, ropa y rasgos distintos (`var`), y decorados distintos (sala, oficina, garage, cabina, trono, café, cielo, calle).
- **Transiciones de cine** cuando suman: barrido rápido con líneas de velocidad, zoom de entrada, subida o zoom a un detalle en el remate. No es absoluto: a veces conviene una escena continua sin corte, o un gráfico de datos.
- **Portada (21-nov):** cada video lleva `.portada.jpg` (fotograma con personajes + título grande, palabra clave en color), hecho con `escena/portada.py`. Sobre todo en GTA, MDM y Rabbit.

**Guion**
- **Lenguaje simple**, que entienda cualquiera. Sin palabras raras: por ejemplo, "probe" → "ship".
- **Menos información es mejor:** una idea central, contada clara. Por ejemplo, en el video de ventas de GTA quedó solo cuánto costó y si ya lo recuperó.
- Gancho al inicio y cierre que invita a comentar. **Sin preguntas directas en la voz** (ver §6): "La pregunta es si…", "Comenta si…", y la pregunta grande en pantalla.
- Las cifras se escriben con número en pantalla y en palabras para la voz (`frases` vs `frases_voz`).
- **Revisión:** si un guion no pasa `revisar.py`, **no se detiene ni se deja de lado**. Se corrige y se vuelve a revisar hasta que pase.

**Voz**
- Kokoro (local). GTA ES **`em_santa` más joven** (21-nov, `joven.py`) · GTA EN, Rabbit y Café `am_michael` · MDM `bm_george`.
- La voz IA no entona bien las preguntas: por eso se evitan en el guion (§6). Nunca subir el tono con el método que suena a **helio**.
- Busca una voz más orgánica (pendiente probar Chatterbox).

**Música**

| Canal | Música |
|---|---|
| GTA ES / EN | **deep** (tranquila) |
| Rabbit | **dark** (misterio) |
| Café | **deep** |
| MDM | **deep** |
| Repers **animados** (avatares, historias) | **funk** (`musica_funk.py`, `repers/musica/funk-01..05.mp3`) |
| Repers **con personas** | **se alterna**: música de la app con su **drop** (golpe al empezar jumping o sentadillas) y el funk nuevo (5 pistas, o nuevas cada vez) |

- **Nada de música animada ni infantil** ("de cabros chicos") en GTA, Rabbit ni en los Repers animados.
- Volumen final −14 LUFS.

**Efectos de sonido**
- **Prohibido** el whoosh largo que suena a giro (`WhipWhoosh_SEU04.8` / `whoosh_01`). Los whoosh cortos sí.
- **Pops más bajos.** No repetir el mismo efecto: hay que variar.
- Los efectos tienen que **calzar con el tema**: motor de auto en GTA, glitch o electricidad en aliens, caja registradora en precios, vinilo o grabadora donde calce.

**Títulos**
- **Cortos: hasta ~40 caracteres**, para que no se corten en el celular. Una idea, con el número o el misterio al principio.
- Emoji al final opcional (💸 👽 ☕).
- Ejemplos aprobados: "We Sent Our Address To Aliens. 👽", "¿GTA 6 ya recuperó lo que costó? 💸", "Coffee Beans Aren't Beans ☕".

**Descripciones**
- **Insinúan y dejan la duda; no cuentan el video.** Sin precios, cifras ni el remate. Sin pregunta para comentarios.
- 1 o 2 frases cortas (máximo ~20 palabras), luego un **CTA breve**, luego **4–5 hashtags**.
- Ejemplos: "Mismo juego. Precio muy distinto. 👀" · "Escapar de la policía ya no será tan fácil. 🐕" · "Everyone talks about the size. But here's the detail nobody noticed. 🌴"
- Si el video usa estimaciones, se agrega una línea de **fuente** ("Fuente: estimación de Sensor Tower (no oficial)").

**Publicación**
- **Sin comentario fijado**, para dejar el suspenso al video. Solo **título + descripción**.
- Los videos quedan listos en `~/Desktop/YouTube/<canal>/<día>/HHh - título.mp4` con su `.txt`. Tao solo los sube.
- En el celular: botón 📱 del panel (QR) → copiar título y descripción, guardar el video y marcarlo como subido.

**Imágenes de marca** (logo y banner): se hacen en ChatGPT, **que no se vean tan IA**. El logo va pensado **circular**.

---

## 2. Por canal

### ViceVerso (GTA ES) — 2 al día (19h y 22h)
- **El juego ya salió (19-nov).** Nada de contenido de expectativa ni futuro ("irá a…"). Todo en presente.
- **Micronicho en test (21-nov): "Los números de GTA 6"** — dinero, récords, cuánto cuesta o vende algo, dentro y fuera del juego (estilo annoyingmath: un número grande como meta). Fórmula de título: "GTA 6 tiene que ___ para ___".
- Ventas y costos siempre como **estimación**, con quién la hizo.
- Gatillos que rinden: **aversión a la pérdida** ("lo que pierdes si…") y consecuencia real para el jugador.
- Los temas pierden vigencia rápido. Si un video programado ya no tiene sentido (por ejemplo, el bar de los Cayos), **se descarta**.
- **No repetir:** el tema del mapa y Corea del Sur (y no decir "censores", eran revisores), Miami sin tomas reales para contrastar.
- ES y EN: **mismo tema con ángulo distinto**, y **nunca el mismo video el mismo día** (2 o 3 días de diferencia).

### TheViceVerse (GTA EN) — 2 al día (13h y 20h)
- **Micronicho en test (21-nov): "Hidden mechanics"** — secretos y mecánicas del juego que nadie explica (estilo Viceprint, 353 mil vistas en 16 h). Fórmula: "GTA 6 Has a Secret ___".
- Cada mecánica verificada en 2+ fuentes. Si Tao graba clips de su consola, se usan (son material propio); si no, animación.
- **Inglés simple**. El video de precios por país no rindió en EN (se bajó).

### The Rabbit Loop — 2 al día (18h y 22h)
- **100 % aliens. Micronicho en test (21-nov): "Casos OVNI cerrados"** — misterio primero, respuesta oficial después (AARO y otros informes). Piloto: "The 'Jellyfish' UFO Over Iraq". Fórmula: "The ___ UFO Was Finally Solved".
- Reserva si no rinde: mensajes enviados al espacio, luego señales sin explicar.
- Tono de misterio, **música dark**, nada infantil.
- Referencia que le encanta: "They Fooled a Robot Into Stabbing" (título claro, explicación, imágenes, dato relevante).

### Coffee, But Why? (@ChiChibitsTV) — 2 al día (17h y 21h)
- **Micronicho en test (21-nov): "El café prohibido"** — prohibiciones, escándalos, crímenes y guerras por el café (piloto: "A King Tried to Ban Coffee"). Fórmula: "A ___ Tried to Ban Coffee".
- **Informativo, nunca médico:** sin afirmaciones de salud ni sobre la cafeína.
- En inglés, formato "But why?". La firma es el CTA.

### Million Dollar Mistake — **2 al día (15h y 20h)** (21-nov; antes 1 por semana)
- **Micronicho (21-nov): "Lo vendió por $X, hoy vale $Y"** — cosas valiosas vendidas o rechazadas por poco, y su valor actual, con **animación (escena)**.
- Casos verificados en `claude/mdm-banco-casos-21-nov.md` (proyecto). El valor de "hoy" se verifica **el día que se hace el video** (las acciones y el bitcoin cambian).
- Títulos **cortos que dejan la duda**, sin "Worth it?": "10,000 Bitcoin for 2 Pizzas", "Pixar Was Sold for $5 Million".
- Cada caso contado como **mini película** con personajes (ej.: Laszlo en el computador, el repartidor llega con las pizzas).
- Cierre con una **enseñanza** acorde al nombre del canal ("no cometas este error").
- Voz británica `bm_george`.

### Number Signs — **en pausa**
- Tao todavía no crea el canal. No se genera nada.

### Repers — 1 al día por cuenta (IG, TikTok, YT)
- Se intercalan videos **con personas** (tomas reales) y **animados** (avatares, historias). Se prueba una estructura a la vez y se mide.
- Las pausas (agitar la polera, cansado) sirven como hook o intermedio.
- Música: ver la tabla de arriba.

---

## 3. Micronichos y test (21-nov)

**Ritmo:** máximo **2 videos al día por canal** (MDM 15h y 20h; Café 17h y 21h). YouTube dice que no hay un número mágico: más videos solo dan más oportunidades si cada uno tiene su propia idea.
**Calendario:** días de test marcados en `datos/tests.json` (🟡 TEST del 21-nov al 4-dic, 🔴 ANÁLISIS el 29-nov y el 5-dic).

Base: el video de Mario Ruiz "9 errores que el algoritmo odia" + los Shorts de Viceprint y annoyingmath.

**Regla:** un solo micronicho por canal, con la misma fórmula de título, gancho y gráfica, hasta agotarlo. Después se rota a otro.

| Canal | Micronicho | Test |
|---|---|---|
| GTA ES | Los números de GTA 6 | 7 días (14 videos) |
| GTA EN | Hidden mechanics | 7 días (14 videos) |
| Rabbit | Casos OVNI cerrados | 7 días (14 videos) |
| Café | El café prohibido | 10 días (10 videos) |
| MDM | Lo vendió por $X, hoy vale $Y | ~2 semanas |

**Cómo se decide (cada domingo):**
- Datos de YouTube Studio por Short: **% que lo vio vs. pasó de largo**, **% promedio visto**, **suscriptores por cada 1.000 vistas**.
- Se compara contra el **promedio del mismo canal en los 14 días anteriores**.
- Mejora en 2 de 3 → **se queda**. Empeora en las 3 → **nicho de reserva**.

## 4. Reglas del algoritmo (21-nov, de Mario Ruiz)
1. **No mezclar temas** dentro del nicho: micronicho hasta agotarlo.
2. **Personalidad:** tráiler del canal de 30–60 s con la voz de Tao (pendiente que lo grabe).
3. **Ángulo específico**, nunca temas generales.
4. **Mirar los datos** desde los 3–4 primeros videos, no subir a ciegas.
5. **Encadenar videos:** cada `.txt` lleva `VIDEO RELACIONADO:` apuntando al anterior del mismo micronicho; Tao lo elige al subir.
6. Canal nuevo: usarlo como humano unos días antes de subir (Café, Number Signs).
7. **Gancho:** atacar algo que el público ya cree + promesa + promesa mayor.
8. **Título y miniatura** hablan de lo que quiere el espectador, no de la herramienta.
9. **El video cumple lo que promete el título** (YouTube lee audio y transcripción).

## 5. Cómo se trabaja
- **Avisar antes** de cambiar código existente. Archivos y contenido nuevo se pueden hacer directo.
- Tareas pesadas **de a poco**, para que el Mac no se caliente. El Mac no queda prendido de noche.
- Las contraseñas y los cambios de cuenta los hace Tao.
- Nunca mostrar claves, tokens ni correos.

## 6. Estilo "película" (21-nov, aprendido con Tao)
Motor: `escena/escena.html`, tipo `pelicula`. Una sola escena continua por video, dividida en **zonas** que la cámara recorre.

**Imagen**
- **Pantalla completa** siempre. Excepción: Rabbit abre con el **encuadre de cámara** (visor IR) y luego se abre a pantalla completa (`abre`).
- **Lento y fluido:** paneos y zooms ~1.6× más largos, sacudidas suaves. Los cambios de escena son desplazamientos, no saltos.
- **Se construye de a poco:** primero el suelo, luego los elementos.
- **Luz de noche variada** por zona: postes, lámparas colgantes, neón (con textos propios), penumbra. Viñeta.
- **Vida de fondo:** gente caminando, alguien mirando a los lados (`extras`).
- **Mostrar, no escribir:** zoom al detalle (vidrio que se triza), dinero que cae, el teléfono con la app, la tablet que se escribe sola, el mando con el botón resaltado, la barra de energía, números que cuentan.
- **Títulos clave grandes** de neón (`grande:true`), como PIXAR o PARALLAX.

**Nada tapa nada**
- Los **globos** salen de la cabeza de quien habla (`de: índice del actor`).
- **Carteles, papeles y números** no tapan personas ni textos. Los números van arriba (y≈800).
- **Tarjetitas: pocas**, y arriba, justo bajo el título (`chipY` 680). Si hay espacio arriba, no se ponen abajo sobre los objetos.
- Si no cabe, **zoom out** (`escala` 1.05–1.1).
- Los objetos que salen de una escena **no reaparecen** en la siguiente (`fin`).
- Los personajes que salen se **desvanecen**.
- El cierre aparece **después** de que se fue la última escena.

**Personajes = actores con rol**
- El protagonista tiene identidad fija.
- El resto **no se le parece**: sin corona, sin peinado que parezca corona, sin la misma barba.
- Proporciones reales:
  - El auto es más alto que la mitad del cuerpo.
  - Dentro del auto solo se ve por la ventana (`dentro`).
- Evitar transiciones que deforman, como pararse de una silla: el rey se queda sentado.

**Guion y voz**
- **Preguntas implícitas:** la voz IA dice las preguntas como afirmación.
  - Se escribe "La pregunta es si ya lo recuperó" o "Comenta si…".
  - La pregunta va **grande en pantalla**.
- **CTA hablado** al final, por canal:

| Canal | CTA |
|---|---|
| Rabbit | "Follow for the next case." |
| GTA EN | "Follow for more GTA 6 secrets." |
| GTA ES | "Sigue el canal para más números de GTA 6." |
| MDM | "Follow for the next million dollar mistake." (favorito de Tao) |
| Café | "Follow for more banned coffee stories." |

- **Voces:**
  - GTA ES: `em_santa` más joven (`joven.py`, +2 semitonos, formante 1.06).
  - MDM: `bm_george`, la voz perfecta.
  - Rabbit, Café y GTA EN: `am_michael`.

**Cierre**
- Pregunta grande y caja con "Comenta…".
- Opciones **grandes, juntas y con el mismo espacio** entre ellas.
- **LIKE** con corazón y flecha corta al botón de like.
- **SEGUIR** con flecha al canal.
- Estilo de botones: **con relieve** (elegido por Tao el 21-nov, no el vidrio neón). La caja de la pregunta va un poco separada de las opciones.

**Herramientas**
| Archivo | Para qué |
|---|---|
| `muestras.py` | Cuadros sueltos para revisar sin renderizar |
| `ajustar_tiempos.py` | Mueve los tiempos si cambia la voz |
| `joven.py` | Voz más joven |
| `portada.py` | Portadas |

## 7. Canales nuevos (pendiente)
- **Perros** y **gatos**: un canal cada uno, 1–2 videos al día.
- Cada uno con el micronicho más potente para su animal y un **animal protagonista fijo**.
