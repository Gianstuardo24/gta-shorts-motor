# 10 · Lenguaje de película: el video como un montón de micro-escenas

> Pedido de Tao (23-nov, 23:28): *"Que los videos sean un cúmulo de todas esas escenas contando la historia. Eso lo hace ver una película más que un video donde hay una escena y de repente se agregan cosas."*
> Imagen de referencia que le gustó: la vista desde la cabina (nariz del avión, mar de noche y la retícula sobre la mancha blanca). Es creativa, es un plano distinto y **muestra lo que se vio**.

## La idea, afinada
- **Hoy:** pensamos en **escenarios** (un set con personajes) y les agregamos insertos.
- **Lo que pide Tao:** pensar en **planos**. Cada frase tiene una **micro-escena diseñada para ella**, con su propia composición, perspectiva y movimiento. El set con personajes pasa a ser **un tipo de plano más**, no la base del video.
- **Prueba rápida:** si se quita la voz, ¿la secuencia de imágenes cuenta la historia? En una película, sí.

## Tipos de micro-escena (el vocabulario)
| Tipo | Qué muestra | Ejemplo |
|---|---|---|
| **Punto de vista (POV)** | lo que ve el personaje | desde la cabina hacia la mancha (la imagen de Tao) |
| **Reflejo** | lo que ve, reflejado en él | la mancha en el visor del casco |
| **Detalle del lugar** | un rincón del set donde estamos | escritorio con taza humeante, reloj de pared, ventana con lluvia, teléfono |
| **Manos** | la acción sin mostrar la cara | manos que abren la carpeta, firman o marcan |
| **Establecimiento** | dónde y cuándo | portaaviones al amanecer, edificio de noche |
| **Reacción** | cara iluminada por lo que mira | piloto con la luz de la pantalla |
| **Objeto que prueba** | la evidencia | foto, cinta, documento, pantalla |
| **Dato en el mundo** | la cifra dentro de algo físico | el número en el calendario, en el radar, en un letrero |
| **Diagrama** | cómo funciona algo | trayectoria tipo plano técnico, triángulo de paralaje |
| **Metáfora** | una idea abstracta hecha objeto | balanza, sello que no baja |
| **Tiempo** | paso del tiempo | hoja de calendario que cae, sol que se mueve, reloj |
| **Mapa** | lugar y distancia | carta náutica con la línea "100 mi" |
| **Contraste** | A contra B | pantalla dividida, jet normal que se queda atrás |
| **Montaje rápido** | muchas cosas en poco tiempo | 3 pantallas de celular en 2 s |

**Regla:** en cada minuto hay **al menos 6 tipos distintos**, y ningún tipo se repite seguido.

## Registros visuales (otros estilos, como pidió Tao)
Cada video elige **3–4 registros** y los asigna a una **función de la historia**. Así los cambios de estilo cuentan algo y no se sienten al azar.
| Registro | Cómo se ve | Para qué |
|---|---|---|
| Recreación de color | ilustración cinematográfica con luz de borde (como la imagen) | los hechos, el "estar ahí" |
| Noir / archivo | oscuro, lámpara, polvo en el aire | investigación, documentos |
| Pantalla / HUD | infrarrojo blanco-caliente, retícula, cifras | lo que registró una máquina |
| Plano técnico | líneas blancas sobre azul | explicaciones |
| Época | sepia o blanco y negro con grano | el pasado (1942, 1947, 1899) |
| Recortes de papel | collage, diarios, fotos | noticias y opinión pública |
| Maqueta | ciudad en miniatura vista desde arriba | mapas y escala |

## Movimientos (distintas mociones)
- **Cámara:**
  - acercamiento y alejamiento lentos;
  - paneo y subida/bajada;
  - **cambio de foco** (del visor al reflejo);
  - **paralaje** (capas a distinta velocidad);
  - golpe de zoom;
  - **cámara lenta y rampa de velocidad**;
  - mano suave;
  - **vértigo** (zoom contra traslado) para revelaciones;
  - **corte por forma** (la mancha ovalada → una cápsula → la luna).
- **Dentro del plano:** al menos **2 cosas se mueven**: humo, polvo, olas, luz que parpadea, contenido de pantalla, una mano o un papel.

## Densidad
- **Video de 10–12 min ≈ 200–250 planos** (uno cada ~2,8 s).
- **≥60 % son micro-escenas únicas.** El resto son regresos con cambio (otro ángulo, otra hora, otra acción).
- **Detalles del lugar:** cada set lleva **3–5 detalles propios** (con su luz y sus colores), para cortar dentro del mismo lugar sin salir de la historia.

## Cómo se produce (3 caminos)
| Camino | Cómo | Ventaja | Costo |
|---|---|---|---|
| **A. Todo código** | cada micro-escena se dibuja con código | estilo 100 % parejo, sin límites | 8–20 min por micro-escena; un video entero sería demasiado lento |
| **B. Ilustración + animación** | ChatGPT hace la **lámina** (como la imagen de Tao) y el código la anima encima: paralaje, retícula, luces, olas, partículas, textos | detalle de "trabajado" muy rápido | parejar el estilo entre láminas, límite de imágenes del plan de ChatGPT, nada de caras ni texto dentro de la imagen |
| **C. Mezcla** ⭐ | **biblioteca de código** para lo que se repite con datos (calendario, sello, carpeta, mapa, pantallas, diagramas, cifras) + **láminas** para los planos de autor (POV, establecimientos, ambientes, 15–30 por video) | lo mejor de los dos; la biblioteca crece con cada video | hay que armar el motor de láminas (~1 h, una vez) |

**Recomendación: C.** Cada pieza de código es **paramétrica** (`calendario(fecha)`, `sello(texto)`, `mapa(lugar, distancia)`), así que se reutiliza con otro contenido y se ve distinta. Las láminas dan el salto de detalle.

**Reglas de las láminas:**
- estilo fijo por canal (prompt base + paleta + imagen de referencia);
- **sin texto, sin logos, sin caras reconocibles**; personas solo de espalda o en silueta;
- el texto y los datos siempre los pone el código;
- cada lámina da **2–3 planos** (encuadres distintos de la misma imagen).

## Nuevo paso en el flujo: guion visual antes de construir
Antes de programar, se arma la **lista de planos** (storyboard en tabla):

| tiempo | frase | micro-escena | registro | movimiento | qué se mueve | sonido |
|---|---|---|---|---|---|---|

**Tao la aprueba**, y recién después se construye. Es más barato corregir una tabla que un render.

## Piloto: Navy UFO, 0–44 s (16 micro-escenas, ningún set viejo)
| t | Frase | Micro-escena | Registro | Movimiento / qué se mueve |
|---|---|---|---|---|
| 0,0 | "On April 27, 2020," | calendario de escritorio: cae la hoja y queda APR 27 2020 | noir | acercamiento; vapor de una taza, polvo en la luz |
| 2,6 | "the Pentagon officially released three videos." | vista desde arriba: manos dejan 3 cintas y un sello RELEASED golpea | noir | corte con golpe; papeles que se levantan |
| 5,3 | "They showed objects" | pantalla IR a pantalla completa: la retícula busca y entra la mancha | HUD | zoom de retícula; cifras que cambian |
| 7,3 | "that Navy pilots could not identify." | visor del casco de lado, con la mancha reflejada | recreación | cambio de foco visor → reflejo |
| 9,2 | "FLIR, GIMBAL, and GOFAST." | muro oscuro: 3 pantallas que se encienden **una por palabra**, cada una distinta | HUD | se encienden con chispazo; la cámara se aleja |
| 12,3 | "For years, people said these videos proved…" | montaje de 3 pantallas de celular genéricas con vistas y comentarios | pantalla | deslizamiento de dedo |
| 15,0 | "…something unknown was flying over the ocean." | **POV desde la cabina** (la imagen de Tao) | recreación | paralaje del mar; la mancha pulsa |
| 18,1 | "Pilots described things that moved in ways…" | plano técnico: la trayectoria de la mancha con giros secos | plano técnico | la línea se dibuja |
| 20,8 | "no aircraft they knew could move." | un jet común sigue la línea y se queda atrás | plano técnico | el jet frena; el trazo sigue |
| 23,4 | "Our rule here is simple:" | archivo oscuro: se enciende una lámpara sobre una carpeta | noir | luz que se enciende; polvo |
| 26,0 | "a case is only closed when the evidence closes it." | sello CLOSED que baja y **se frena antes de tocar** | noir | el sello baja y se queda vibrando |
| 28,6 | "Today, we open the complete file:" | manos abren la carpeta con 3 pestañas | noir | la tapa se abre; página que pasa |
| 31,5 | "what each video shows, what investigators found," | dentro: fotos IR con clips y notas con tachones | noir | recorrido lento sobre los papeles |
| 34,0 | "and which case is still open." | pestaña roja OPEN; la cámara entra hasta llenar el cuadro | noir | acercamiento → negro |
| 36,4 | "It starts on November 14, 2004," | carta náutica: costa del sur de California, se dibuja la línea y cae un alfiler | mapa | trazo; el alfiler rebota |
| 40,0 | "about 100 miles off the coast of Southern California." | amanecer en el mar, portaaviones genérico en el horizonte | recreación | paneo lateral; olas, humo, gaviotas |

**Ritmo del piloto:** 16 micro-escenas en 44 s (≈2,75 s cada una), 5 registros, **0 sets viejos**.
