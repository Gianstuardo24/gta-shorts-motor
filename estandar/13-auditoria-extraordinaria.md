# 13 · Auditoría extraordinaria (23–24 nov 2026)

> Encargo: el prompt "Extraordinary Audit" que trajo Tao. Lo ejecutó Claude sobre el material real: los 6 largos renderizados, sus guiones, sus datos de planos y el estándar (docs 00–12).
> **Etiquetas:** `[MED]` medido u observado en nuestro material · `[EXT]` investigación externa con fuente · `[REC]` recomendación profesional · `[HIP]` hipótesis sin probar.
> ⚠️ **Corregido por el doc 14 (revisión crítica):** el "19 veces" de este informe estaba inflado por el umbral del detector; la diferencia real entre Pixar y el resto es de ~2 veces. Los umbrales de cortes y "looks" no son norma, y varias recomendaciones se eliminaron. **El plan vigente es el del doc 14.**
> **No hay datos de retención de ningún largo.** Nada de lo que sigue afirma que algo "sube la retención"; donde importa, propongo cómo medirlo.

## 0. Qué se auditó y qué falta
| Material | Estado |
|---|---|
| 6 videos renderizados (Pixar, Coca-Cola, Navy, 5 casos, Perros, Café) | ✅ medidos cuadro a cuadro |
| Datos de planos y guiones de los 6 | ✅ |
| Hojas de cuadros de Pixar, Navy y Café | ✅ miradas una por una |
| Estándar 00–12 | ✅ contrastado con las mediciones |
| Curvas de retención, CTR y % visto de los largos | ❌ no existen o no las tengo |
| Datos de los Shorts (vio vs. deslizó) | ❌ fuera de esta auditoría |
| Dónde se ven los videos (teléfono o TV) | ❌ |

---

## 1. Mediciones `[MED]`
Tres medidas nuevas, tomadas del video final y no del plan:
- **Cortes reales por minuto:** el mismo detector de cortes que usamos para analizar a otros creadores (ffmpeg, umbral 0,25).
- **"Looks" distintos:** un cuadro cada 3 s, agrupados por parecido de color. Cuenta cuántas imágenes realmente distintas tiene el video.
- **Look dominante:** qué parte del video ocupa la imagen más repetida.

| Video | Min | Planos por min **según el plan** | **Cortes reales** por min | Fuera del escenario | Espacios (visitas) | Looks distintos | Look dominante | Looks nuevos en la 2.ª mitad | Palabras/min |
|---|---|---|---|---|---|---|---|---|---|
| **Pixar** | 6,4 | 25,2 | **15,3** | 30 % | 14 (33) | **28** | 23 % | 6 | 179 |
| Coca-Cola | 6,1 | 21,2 | 7,3 | 7 % | 4 (11) | 8 | 51 % | 2 | 144 |
| Navy | 8,0 | 21,0 | **0,8** | 3 % | 5 (16) | 9 | 40 % | 2 | 142 |
| 5 casos | 9,4 | 20,1 | 3,2 | 6 % | 6 (11) | 14 | 34 % | 4 | 148 |
| Perros | 6,2 | 20,9 | 1,8 | 4 % | 3 (9) | 9 | 37 % | 1 | 170 |
| Café | 5,4 | 20,7 | 2,5 | 4 % | 1 (1) | 6 | 55 % | **0** | 153 |

Otros datos:
- **Duración de planos:** mediana 2,4–2,8 s y percentil 90 de 3,5–3,8 s en los seis. Todos los planos duran casi lo mismo.
- **Primeros 30 s:** Pixar tiene 8 cortes reales; Navy, 5 casos y Café tienen **0**.
- **Oscuridad:** brillo medio de 37–57 sobre 255, y 35–49 % de los pixeles casi negros, en los seis.
- **Etiquetas de texto:** 24–49 por video, además de 10–17 títulos y los subtítulos.

### El hallazgo central
**El plan dice lo mismo para los seis videos (~21 planos por minuto), pero lo que ve el espectador es 19 veces distinto:** 15,3 cortes reales por minuto en Pixar contra 0,8 en Navy.
- **Por qué:** en los videos flojos, casi todos los "planos" son reencuadres de cámara sobre el mismo escenario. Para nuestro sistema cuentan como plano nuevo. Para el ojo es la misma imagen.
- **Consecuencia:** la regla "encuadre nuevo cada 2,5–3,5 s" se cumple en los seis, y `revisar_largo.py` los aprueba todos. **Medimos lo que hace la cámara, no lo que cambia en la imagen.**
- **Confirma con números lo que Tao dijo a ojo** ("un video donde hay una escena y de repente se agregan cosas"): el camino es imágenes nuevas, no más tipos de plano.

---

## 2. Fase 1 · Auditoría forense: 24 debilidades y oportunidades (en orden de importancia)

### Producción y medición
| # | Hallazgo | Evidencia |
|---|---|---|
| 1 | **El armado y la revisión optimizan la métrica equivocada** (reencuadres en vez de imágenes nuevas) | `[MED]` tabla de arriba |
| 2 | **Trabajamos a ciegas:** ningún largo tiene retención medida y las pruebas de títulos están preparadas, pero sin correr | `[MED]` |
| 3 | **El estándar escrito no lo cumple ni la referencia.** Pide 35–45 % fuera del escenario y Pixar tiene 30 %. Pide máximo 5 regresos y Pixar tiene 19. Pide voz a 1,18× y solo Pixar la tiene (179 palabras/min contra 142–153) | `[MED]` Las reglas no están en el código |
| 4 | **Solo MDM tiene banco de insertos.** El resto pasa 3–7 % del tiempo fuera del escenario | `[MED]` |
| 5 | **El tiempo se gasta al revés:** 5 largos en 2 h 20 min, sin guion visual, y los errores se descubren después del render | `[MED]` + `[EXT]` Kurzgesagt declara ~1.200 horas por video y que el guion es su cuello de botella |

### Imagen
| # | Hallazgo | Evidencia |
|---|---|---|
| 6 | **Todos los canales comparten el mismo look:** fondo oscuro con conos de luz. Un canal de perros y uno de café se ven como un canal de ovnis de noche | `[MED]` brillo y % de negro casi iguales; hojas de Navy y Café |
| 7 | **El tema del video no es el protagonista.** Café: la taza es un ícono chico en una esquina y no hay un solo primer plano de la bebida en 43 cuadros. Navy: el "objeto" es un punto blanco sobre una pantalla gris, igual para los 3 casos, en 8 o más cuadros | `[MED]` hojas |
| 8 | **Cuadros casi vacíos:** en Navy, ~14 de 60 cuadros son cielo oscuro con un avión diminuto | `[MED]` hoja |
| 9 | **Personajes de pie, de frente, solos y chicos** bajo un foco. Ilustran que "alguien habla", no la acción. Fuera de Pixar casi no interactúan | `[MED]` hojas |
| 10 | **La novedad se acaba pronto:** Café no muestra ninguna imagen nueva en su segunda mitad; Perros, una; Navy, dos | `[MED]` |
| 11 | **Ritmo de metrónomo:** todos los planos duran 2,4–3,8 s. No hay ráfagas ni planos sostenidos | `[MED]` + `[EXT]` en el cine, la duración de los planos cambia según el momento de la historia (Cutting) |
| 12 | **El color no ordena la historia:** en Navy, 3 looks ocupan el 85 % del video. En Pixar cada capítulo tiene su color | `[MED]` |
| 13 | **El mismo gráfico se repite:** barras de proporción en 9 o más cuadros de Café; la línea de tiempo 3 veces; el tablero 4 veces en 5 casos. **También Pixar:** la vitrina del museo aparece 7 veces y sus últimos 40 s son casi el mismo cuadro | `[MED]` |
| 14 | **Hasta 3 capas de texto a la vez:** subtítulos, etiqueta y título. Una etiqueta cada 8–11 s | `[MED]` + `[EXT]` principio de redundancia de Mayer (ver Fase 3) |

### Historia
| # | Hallazgo | Evidencia |
|---|---|---|
| 15 | **Pixar revela la respuesta en los segundos 5–10** ("7.4 billion", "That team was Pixar"), mientras el título y la portada la esconden | `[MED]` guion. Ya estaba pendiente como "Pixar v2" |
| 16 | **Guiones de "y después":** las frases que empiezan con And/Then superan a las que empiezan con But/So en 5 de 6 videos (5 casos: 28 contra 12). Perros y Café son enumeraciones sin cadena de causa | `[MED]` + `[EXT]` regla "pero / por lo tanto" de Parker y Stone |
| 17 | **Navy abre con una fecha y una institución,** sobre un cielo vacío y sin un solo corte en 30 s. A los 24 s habla de "nuestra regla" antes de plantear qué está en juego | `[MED]` + `[EXT]` YouTube mide la intro como el % que sigue mirando a los 30 s |
| 18 | **No hay giros planeados a mitad de video:** los capítulos informan parejo | `[MED]` + `[EXT]` práctica de MrBeast (documento filtrado, no confirmado) |
| 19 | **Los seis terminan igual:** "Tell me… / Comment…" + "Follow…" + ~20 s de tarjeta fija, idéntica entre canales salvo el logo. Las listas cierran con un resumen | `[MED]` + `[EXT]` regla del pico y el final |
| 20 | **En las listas todo pesa igual:** Café son 12 ítems en 5:42 (~28 s cada uno), cada uno con el mismo gráfico | `[MED]` |
| 21 | **Hay una pregunta en la voz de Perros** (4:00, "So why do they happen?"), contra la regla R-05 | `[MED]` |

### Oportunidades
| # | Oportunidad | Tipo |
|---|---|---|
| 22 | **Los Shorts como laboratorio visual:** juntan vistas más rápido que los largos, así que sirven para probar técnicas antes de llevarlas a un largo | `[REC]` |
| 23 | **Curva de retención cruzada con nuestro registro de planos:** sabemos qué había en pantalla en cada segundo | `[REC]` |
| 24 | **Piezas reutilizables + láminas ilustradas** para subir el detalle sin subir el tiempo en la misma proporción | `[HIP]` |

---

## 3. Fase 2 · Cada regla, puesta a prueba
| Regla actual | Veredicto | Por qué | Cómo quedaría |
|---|---|---|---|
| Encuadre nuevo cada 2,5–3,5 s | **MODIFICAR** | Se cumple en los seis y no distingue al mejor del peor `[MED]` | **≥12 cortes reales por minuto, medidos en el render.** Con ritmo variable: ráfagas de 0,8–1,5 s y planos sostenidos |
| Ningún plano de más de 4,5 s | **EXPERIMENTAR** | Un plano de 6–8 s con una acción que avanza (una firma, un vertido) puede sostenerse `[HIP]`. Tao ya lo dijo: si dura, que tenga que ver con lo que se dice | Tope de 4,5 s si no pasa nada nuevo; hasta 8 s si hay una acción continua |
| 35–45 % fuera del escenario | **QUITAR como meta** | Es un sustituto. La referencia tiene 30 % `[MED]` | **Look dominante ≤25 % y ≥3 looks distintos por minuto** (Pixar: 23 % y 4,4) |
| 16 tipos de plano | **MANTENER como vocabulario, QUITAR como señal de calidad** | Son reencuadres. No crean imágenes nuevas `[MED]` | — |
| Máximo 5 regresos a un espacio | **MODIFICAR** | Pixar tiene 19 y es lo que le gusta a Tao `[MED]`. Volver a un lugar ayuda a ubicarse `[EXT]` | **Ningún regreso sin cambio de estado** (hora, gente, objetos, ángulo). Ningún espacio ocupa más del 20 % del video |
| Insertos una sola vez | **MODIFICAR** | Un motivo que vuelve **y avanza** (el marcador que se llena) es estructura | Una vez los decorativos. Los motivos vuelven solo si cambian |
| Siempre pasa algo | **MODIFICAR** | El movimiento atrae la mirada `[EXT]`. Si es decorativo, compite con lo importante. Los detalles llamativos pero irrelevantes perjudican el aprendizaje `[EXT]` | **Movimiento con función.** Un solo punto de atención por plano. Nada se mueve al lado de una cifra que hay que leer |
| El gráfico entra antes de la palabra | **MANTENER, con precisión** | Palabra e imagen a la vez se entienden mejor `[EXT]` | El contenedor entra antes; **el dato cae en la palabra** |
| Un toque propio por video | **MANTENER + AGREGAR** | Falta el nivel del canal | **Firma de canal** (estable) + **motivo del video** (cambia, y vuelve 3 veces o más: se planta, crece y paga) |
| Nada sobre los subtítulos; sin textos encimados | **MANTENER** | — | — |
| Etiquetas de texto libres | **EXPERIMENTAR** | 3 capas de texto `[MED]`; redundancia `[EXT]` | Máximo 1 texto además del subtítulo. Etiquetas solo para nombres, fechas y fuentes |
| Sin preguntas en la voz | **MANTENER (límite técnico) + EXPERIMENTAR** | La pregunta es una herramienta de curiosidad | Probar una voz que sí pueda preguntar |
| No revelar el dato clave | **MANTENER + AGREGAR** | Hoy se rompe dentro del video `[MED]` | También vale para los **primeros 30 s** |
| Voz a 1,18× | **MODIFICAR** | No se aplicó a 5 de 6 `[MED]`. Un caso de misterio puede ir más lento | Meta de palabras por minuto **por canal**, aplicada por código |
| Transiciones fluidas, sin cortes bruscos | **MODIFICAR** | Entre imágenes distintas, el corte seco es el recurso normal del cine | Fluida dentro de un lugar. **Corte seco o corte por forma** entre micro-escenas |
| Largos de 10–12 min | **EXPERIMENTAR** | Sin datos, alargar es un riesgo | Partir en 8–10 min y dejar que la retención decida |
| 2 fuentes por dato | **MANTENER + AGREGAR** | Mostrar el método genera confianza `[EXT]` | Etiqueta de fuente en pantalla (Rabbit, MDM) |
| Hoja de planos + OK de Tao | **MANTENER + AGREGAR** | Llega tarde | Guion visual antes de construir + revisión perceptual |

**Reglas que faltan (AGREGAR):**
1. **Apertura:** primer cuadro con el objeto o el resultado, grande. 6 o más imágenes distintas en los primeros 30 s. Lo que está en juego va antes que cualquier frase del canal.
2. **Giros planeados** cerca del 25 %, 50 % y 75 % del video.
3. **Final diseñado:** imagen de regreso + hilo abierto hacia el próximo video. La pantalla final va sobre una escena viva.
4. **Color y estilo por capítulo.**
5. **Tamaño del protagonista:** el sujeto principal ocupa un tercio o más del alto del cuadro en la mayoría de los planos.
6. **Chequeo "pero / por lo tanto"** del guion antes de grabar la voz.
7. **Brillo por canal:** Perros, Gatos y Café son de día y cálidos.
8. **La novedad se reparte:** al menos 1/3 de los looks nuevos aparece en la segunda mitad.

---

## 4. Fase 3 · Investigación externa
| Hallazgo | Fuente | Qué implica para nosotros | Cuidado |
|---|---|---|---|
| Las personas dividen lo que ven en **eventos**. Los límites aparecen cuando cambia la acción, el lugar o el tiempo. Un corte por sí solo no crea un evento nuevo | Zacks y colegas (teoría de segmentación de eventos) `[EXT]` | Organizar el video en **eventos claros**, no en cantidad de cortes | Estudios de comprensión y memoria, no de retención en YouTube |
| **Marcar** los límites entre eventos mejora el recuerdo | Estudio de señalización de eventos (Cognitive Research, 2016) `[EXT]` | Las tarjetas de capítulo sirven si marcan lugar y tiempo | Ídem |
| Los planos del cine se acortaron con las décadas, llevan más movimiento, y **su duración varía según el tramo de la historia** | Cutting y colegas `[EXT]` | Ritmo variable por acto, no parejo | Describe películas; no prueba causa |
| La mirada va a las **caras, al movimiento y al centro**, y casi todos miran el mismo punto | Tim Smith (teoría atencional de la continuidad) `[EXT]` | Un punto de atención por plano; usar el inicio de un movimiento para dirigir la mirada | — |
| **Coherencia, señalización, redundancia, contigüidad temporal y segmentación** | Mayer (aprendizaje multimedia) `[EXT]` | Quitar adornos, resaltar lo esencial, no duplicar texto y voz, imagen y palabra a la vez, partir en tramos | Mide aprendizaje, no retención |
| Los detalles interesantes pero irrelevantes **perjudican** el aprendizaje (efecto pequeño; peor cuando son fijos) | Metaanálisis de Sundar y Adesope `[EXT]` | "Siempre pasa algo" tiene que ser pertinente | Ídem |
| Las experiencias se recuerdan sobre todo por su **momento más intenso y su final** | Fredrickson y Kahneman, 1993; metaanálisis de 2022 `[EXT]` | Diseñar el pico (la revelación) y el último cuadro | No hay estudio en YouTube |
| Entre escena y escena debe haber un **"pero" o un "por lo tanto"**, nunca un "y después" | Parker y Stone, charla en NYU `[EXT, oficio]` | Chequeo simple del guion | Regla de oficio |
| El **primer minuto** es el que más cuida; re-engancha cada ~3 min; "deja de anunciar y empieza a mostrar" | Documento interno de MrBeast `[EXT, oficio; autenticidad no confirmada]` | Giros a intervalos | Otro formato y otra escala |
| La **intro** se mide a los 30 s; hay "picos" y "caídas"; la "retención típica" compara con tus últimos 10 videos de largo parecido | Ayuda de YouTube `[EXT, oficial]` | Son las métricas del ciclo de aprendizaje | Los momentos clave necesitan 100 vistas o más |
| Reconstrucción en 3D + línea de tiempo momento a momento; mostrar el proceso genera confianza | Equipo de Investigaciones Visuales del NYT (GIJN) `[EXT]` | Identidad de Rabbit: mostrar la evidencia y el método | Periodismo, no entretenimiento |
| ~1.200 horas por video; el guion es el cuello de botella | Kurzgesagt `[EXT]` | La calidad se decide en el guion y el guion visual | No es un modelo a copiar |

**Lo que NO encontré:** un estudio confiable que relacione la frecuencia de cortes con la retención en YouTube. Lo que circula son cifras de blogs sin fuente primaria. Por eso el ritmo queda como experimento.

---

## 5. Fase 4 · Sistema creativo por canal `[REC]`
### Million Dollar Mistake — "la sala del trato"
1. **Identidad:** papel cálido, verde oscuro y oro; cada época con sus objetos reales.
2. **Técnicas firma:** etiqueta de precio viva; libro de cuentas en dos columnas.
3. **Transiciones firma:** corte por forma sobre el objeto del trato; odómetro de años.
4. **Espacios:** salas de trato por época, vistas desde la mesa, la puerta o la ventana.
5. **Objetos:** cheque, contrato, balanza, llave.
6. **Estructura:** el trato en frío → "quién vendería esto" → cadena de causas → la cifra → la lección.
7. **Información:** valor en el tiempo sobre el objeto mismo; línea "qué habría pasado" marcada como hipótesis.
8. **Variedad:** 12 o más espacios y 25 o más looks por video (la base es Pixar).
9. **Evitar:** barras genéricas, neón, la vitrina repetida.
10. **Recurrente:** la "ficha del trato" (precio de entonces / hoy: ???) que se completa al final.

### The Rabbit Loop — "el expediente"
1. **Identidad:** azul noche, con estilos de evidencia: pantalla de sensor, archivo, plano técnico.
2. **Técnicas firma:** medidor de certeza (confirmado / testimonio / hipótesis); etiqueta de fuente.
3. **Transiciones firma:** entrar a una foto hasta que se vuelve escena; línea de barrido.
4. **Espacios:** el lugar real reconstruido, con mapa y hora.
5. **Objetos:** carpeta, sello, cinta, alfiler.
6. **Estructura:** lo que se dijo → lo que vieron los testigos (recreación) → la evidencia → la explicación → el sello.
7. **Información:** mapa con triangulación, diagrama que nace de la escena, relojes sincronizados.
8. **Variedad:** cada caso con su color y su recreación.
9. **Evitar:** personajes bajo un foco en el vacío, cielos vacíos, la misma pantalla para todos los casos.
10. **Recurrente:** el tablero de casos que se llena y el número de expediente.

### Dog Decoded / Cat Decoded — "la casa, a la altura del animal"
1. **Identidad:** de día, cálida y luminosa; el animal grande en cuadro.
2. **Técnicas firma:** cámara a la altura de la mascota; repetición lenta con flechas; vista de los sentidos.
3. **Transiciones firma:** el animal pasa frente a la cámara y tapa el cuadro.
4. **Espacios:** las piezas de la casa a lo largo del día (la luz de la ventana marca la hora).
5. **Objetos:** correa, plato, juguete, cama.
6. **Estructura:** la conducta que ya viste → la explicación popular → lo que dice el estudio → qué hacer.
7. **Información:** etiquetas pegadas al cuerpo (oreja, cola) que siguen el movimiento.
8. **Variedad:** una pieza y una hora por señal.
9. **Evitar:** fondo negro, gráficos de barras, humano de pie explicando.
10. **Recurrente:** Biscuit y Mochi fijos + la "tarjeta de decodificación" al cierre de cada señal.

### Coffee But Why? — "la barra, de cerca"
1. **Identidad:** macro, cálida, táctil; la taza es la protagonista.
2. **Técnicas firma:** taza de laboratorio en corte; diales de receta.
3. **Transiciones firma:** el líquido llena el cuadro y descubre la escena siguiente; vapor.
4. **Espacios:** la barra desde arriba, la máquina por dentro, el origen en un mapa.
5. **Objetos:** portafiltro, jarra, vaso, grano.
6. **Estructura:** "pides esto y no sabes qué es" → se arma → por qué sabe así → mito u origen verificado → la chuleta.
7. **Información:** proporciones como capas reales dentro del vaso; temperatura y tiempo en diales.
8. **Variedad:** cada bebida con su vaso, su ángulo y su color.
9. **Evitar:** persona de pie explicando, el mismo gráfico de barras.
10. **Recurrente:** el ticket de pedido que imprime el nombre de cada bebida.

---

## 6. Fase 5 · Lenguaje visual nuevo: 34 técnicas `[REC]` (su efecto en la retención es `[HIP]`)
**Dificultad:** B = menos de 30 min · M = 30–90 min · A = más de 90 min. **Canales:** M = MDM, R = Rabbit, P = Perros/Gatos, C = Café.

| # | Técnica | Cómo se hace, exactamente | Cuándo y para qué | Dif. | Reúso | Canal |
|---|---|---|---|---|---|---|
| 1 | Gancho en frío con objeto | 3 s de macro del objeto en acción (la pluma firma, la retícula encuentra la mancha) antes de cualquier contexto | Segundo 0 | B | alto | todos |
| 2 | Entrar a la evidencia | La cámara entra a una foto o pantalla hasta que su contenido pasa a ser la escena | Pasar de "lo que dice el archivo" a "lo que pasó" | M | alto | R, M |
| 3 | Medidor de certeza | Etiqueta de 3 estados junto a cada afirmación; cambia de color cuando llega evidencia | Separar hecho, testimonio e hipótesis | B | alto | R |
| 4 | Etiqueta de fuente | Abajo a la izquierda, 2 s: "Source: informe, año", cuando cae un dato | Credibilidad | B | alto | R, M |
| 5 | Tablero que se llena | Tablero fijo que suma un elemento por capítulo; se vuelve a él entre capítulos, con su estado nuevo | Sensación de avance; motivo que vuelve y cambia | M | alto | R, M |
| 6 | Reconstrucción en planta | Mapa visto desde arriba con fichas que se mueven y un reloj | Quién estaba dónde y cuándo | M | alto | R, M |
| 7 | Relojes sincronizados | Pantalla dividida en 2–3 lugares con un solo reloj | Hechos simultáneos | M | medio | R, M |
| 8 | Diagrama que nace de la escena | La escena se congela y pierde color; las líneas se dibujan encima | Explicar sin salir del lugar | M | alto | R, C, P |
| 9 | Lo imaginado contra lo medido | Capa translúcida estilizada (lo que se creyó) que se disuelve en lo que registró el sensor | Mostrar aliens sin afirmar que lo eran | M | medio | R |
| 10 | Odómetro de años | Contador que rueda mientras los objetos del fondo cambian por década | Saltos de tiempo | M | alto | M, R |
| 11 | Etiqueta de precio viva | Etiqueta colgada del objeto que se reimprime al pasar el tiempo; la cifra final va tapada hasta la revelación | Tensión sobre la cifra | B | alto | M |
| 12 | Libro de cuentas dividido | Dos columnas ("lo que recibió" / "en qué se convirtió") que se llenan a mano | Contraste acumulado | M | alto | M |
| 13 | Corte por forma | El contorno de un objeto calza con el del plano siguiente (cheque → entrada de cine → pantalla) | Unir épocas o ideas | M | alto | todos |
| 14 | Maqueta que crece | Miniatura isométrica que suma bloques por hito | Crecimiento de una empresa | A | medio | M |
| 15 | Rama fantasma | Línea de tiempo translúcida de "qué habría pasado", marcada como hipótesis, que se apaga | La lección | M | medio | M |
| 16 | Cámara mascota | Punto de vista a 30 cm del suelo; los humanos son piernas | Empatía con el animal | M | alto | P |
| 17 | Vista de sentidos | El olor como cintas de color y el oído como anillos sobre la misma escena | Lo que el animal percibe | M | alto | P |
| 18 | Repetición con flechas | El gesto a media velocidad con flechas y ángulos | Enseñar a reconocer la señal | B | alto | P |
| 19 | Etiquetas pegadas al cuerpo | Rótulos anclados a oreja o cola que siguen el movimiento | Leer el cuerpo | M | alto | P |
| 20 | Silueta con zonas | Silueta del animal con la zona que actúa iluminada (sin afirmaciones médicas) | Explicar el porqué | M | medio | P |
| 21 | El día en la casa | La luz de la ventana recorre el día y marca los capítulos | Estructura de lista sin números | M | alto | P |
| 22 | Taza de laboratorio en corte | Capas que se llenan con física y regla de proporciones al costado | Armar cada bebida | M | alto | C |
| 23 | Transición por vertido | El líquido llena el cuadro y descubre la escena siguiente | Cambio de bebida | M | alto | C |
| 24 | Macro táctil | Burbujas de crema, molienda, vapor (partículas) a cuadro completo | Hacer protagonista a la bebida | M | alto | C |
| 25 | Ticket de pedido | Una impresora térmica imprime el nombre: es la tarjeta de capítulo | Capítulos | B | alto | C |
| 26 | Diales de receta | Temperatura, tiempo y presión se mueven mientras se arma la bebida | Datos sin gráfico de barras | B | alto | C |
| 27 | Ráfaga de montaje | 4–6 imágenes en 2–3 s al ritmo de la música, seguidas de un plano sostenido | Enumeraciones | B | alto | todos |
| 28 | Plano sostenido con acción | 6–8 s sin corte mientras una acción avanza | Momentos de peso | B | alto | todos |
| 29 | Foco dirigido | En la palabra clave, todo se atenúa menos el elemento que importa | Señalar | B | alto | todos |
| 30 | Pantalla final viva | Los botones finales van sobre la última escena, que sigue animada, con un avance del próximo caso | Final y siguiente video | M | alto | todos |
| 31 | Marcador de promesa | Elemento chico y fijo (5 carpetas, 10 tazas) que muestra lo que falta | Listas | B | alto | R, C, P |
| 32 | Cambio de estilo por acto | Color y estilo cambian en cada giro | Marcar que "ahora es otra cosa" | M | alto | todos |
| 33 | Subtítulo que cede | El subtítulo se oculta mientras hay un título diseñado | Evitar texto doble | B | alto | todos |
| 34 | Silencio diseñado | 0,8–1,2 s sin voz y con caída de sonido antes de una revelación | El pico | B | alto | todos |

---

## 7. Fase 6 · Método de producción rediseñado `[REC]`
| # | Etapa | Entregable | Puerta |
|---|---|---|---|
| 1 | Investigación | **Hoja de hechos:** dato, 2 fuentes, nivel de certeza, qué evidencia visual existe | Claude |
| 2 | Empaque primero | 3 opciones de **título + miniatura + promesa**; el dato clave queda definido y "embargado" | Tao |
| 3 | Arquitectura | **Lista de momentos** unidos con "pero / por lo tanto"; gancho; giros al 25, 50 y 75 %; pico; final; curva de ritmo | Claude |
| 4 | Guion | Texto con meta de palabras por minuto; leído "como un espectador que se aburre" | Tao (opcional) |
| 5 | Mapa visual | Por capítulo: lugar, estilo, color, motivo, elemento recurrente | — |
| 6 | **Guion visual** | Tabla plano por plano + puntaje del doc 12 | **Tao** |
| 7 | Construcción | Piezas reutilizables + láminas; hoja de poses | — |
| 8 | Prueba animada | 60–90 s en baja resolución, con voz | **Tao** |
| 9 | Sonido | Lista de sonidos por plano; silencios diseñados | — |
| 10 | **Revisión perceptual** | Cortes reales por minuto, looks por minuto, look dominante, choques de texto, tamaño del protagonista, embargo del dato, brillo por canal | Automática |
| 11 | Render y empaque | Video, 3 títulos, 3 miniaturas, descripción | Tao |
| 12 | Aprendizaje | A los 7 y 28 días: curva de retención contra el registro de planos → actualización del maestro | Claude |

---

## 8. Fase 7 · Hoja de ruta de experimentos
**Límites honestos:**
- No se republica un mismo video, así que no hay prueba A/B con el mismo guion.
- La única prueba aleatoria de verdad que tenemos es **Test & Compare** (títulos y miniaturas).
- Lo demás es comparación entre videos del mismo canal, a la misma edad. Es correlación, no causa.
- Con pocas vistas no hay curva útil.

| # | Hipótesis | Qué cambia | Qué queda igual | Métrica | Esfuerzo | Cuántos |
|---|---|---|---|---|---|---|
| X1 | Más imágenes nuevas retienen más | Micro-escenas (≥12 cortes reales/min, ≥3 looks/min) | Canal, tema, duración, voz | % a los 30 s; retención al 25/50/75 % | alto | 4–6 largos contra los actuales; antes, 10 Shorts contra 10 |
| X2 | Abrir con el objeto retiene más que abrir con la fecha | Primeros 3 s | El resto del Short | Vio vs. deslizó | bajo | 10 contra 10 Shorts por canal |
| X3 | El ritmo variable se siente menos monótono | Ráfagas + planos sostenidos | Guion e imágenes | Caídas a mitad de video | bajo | 4–6 videos |
| X4 | Menos texto en pantalla no baja la retención | Sin etiquetas, salvo nombres y fuentes | Todo lo demás | % visto | bajo | 10 contra 10 Shorts |
| X5 | Perros y Café de día rinden más que de noche | Color y luz | Guion | Vio vs. deslizó; % visto | medio | 10 contra 10 Shorts |
| X6 | El final vivo lleva más gente al siguiente video | Pantalla final sobre escena + avance | Video | Clics en la pantalla final | medio | 4–6 largos |
| X7 | Qué molde de título gana | 3 títulos por video | Video | Cuota de tiempo de visualización | bajo | Cada largo (causal) |
| X8 | Ritmo de voz por canal | 150 contra 175 palabras/min | Guion | % visto | bajo | 10 contra 10 Shorts |
| X9 | Los giros planeados frenan la caída a mitad de video | Giros al 25, 50 y 75 % | Tema | Pendiente de la curva entre giros | medio | 4–6 largos |

**Orden:** X7 (ya está listo) → X2 y X5 en Shorts (baratos y rápidos) → X1 (el piloto) → el resto.

---

## 9. Fase 8 · Veredicto
### A. Diagnóstico
Tenemos **un motor rápido y un video bueno**. Pixar funciona porque recibió horas de corrección a mano y tiene 28 imágenes distintas. Los otros cinco salieron del mismo motor en una noche, y ahí se ve lo que el motor hace por defecto: **un escenario oscuro, personajes de pie y la cámara reencuadrando.** El estándar describía a Pixar con reglas que no explican por qué es bueno, y la revisión automática aprobaba todo. El problema no es de talento ni de técnica. Es de **qué medimos y dónde ponemos las horas.**

### B. Las 10 debilidades más importantes
1. Medimos reencuadres, no imágenes nuevas.
2. No hay datos de retención en ningún largo.
3. Todos los canales tienen el mismo look oscuro.
4. El tema del video no es el protagonista de la imagen.
5. La novedad visual se agota en la primera mitad.
6. Guiones de "y después", y listas donde todo pesa igual.
7. Aperturas sin imagen ni conflicto (0 cortes en 30 s).
8. El estándar no se cumple porque no está en el código.
9. Las horas van al render y no al guion visual.
10. Finales idénticos, con 20 s de tarjeta fija.

### C. Las 10 oportunidades más grandes
1. Revisión perceptual automática (cortes reales, looks, look dominante).
2. Micro-escenas con piezas reutilizables + láminas.
3. Identidad visual por canal (color, luz, firma).
4. Shorts como laboratorio de técnicas.
5. Curva de retención contra el registro de planos.
6. Guion visual aprobado antes de construir.
7. Motivos que vuelven y avanzan (tablero, ficha del trato).
8. Mostrar la evidencia y la fuente (Rabbit).
9. Ritmo variable y silencios diseñados.
10. Final vivo, enlazado con el siguiente video.

### D. Las 10 reglas que cambiaría ya
1. "Encuadre cada 2,5–3,5 s" → **≥12 cortes reales por minuto** en el render.
2. "35–45 % fuera" → **look dominante ≤25 % y ≥3 looks por minuto.**
3. "Máximo 5 regresos" → **ningún regreso sin cambio de estado.**
4. "Siempre pasa algo" → **movimiento con función y un solo punto de atención.**
5. "Insertos una vez" → **decorativos una vez; los motivos vuelven si cambian.**
6. "No revelar" → también en los **primeros 30 s**.
7. Nueva: **apertura con objeto y 6 o más imágenes en 30 s.**
8. Nueva: **color y luz por canal y por capítulo.**
9. Nueva: **chequeo "pero / por lo tanto"** y giros al 25, 50 y 75 %.
10. Nueva: **el guion visual se aprueba antes de construir.**

### E. Marco nuevo: "eventos, imágenes, movimiento, sonido"
1. **Evento:** cada 20–40 s cambia algo en la historia (lugar, tiempo, meta o lo que creíamos). Se marca.
2. **Imagen:** cada evento tiene 6–10 imágenes propias. El protagonista va grande, con un solo punto de atención.
3. **Movimiento:** dentro de la imagen se mueve lo que la voz nombra. El ritmo sigue a la historia.
4. **Sonido:** cada imagen suena, y los silencios preparan los picos.

Se revisa en ese orden: si falla el evento, no lo arregla ninguna cámara.

### F. Identidad por canal
- **MDM:** la sala del trato (papel, verde y oro; la ficha del trato).
- **Rabbit:** el expediente (evidencia, medidor de certeza, tablero de casos).
- **Perros y Gatos:** la casa a la altura del animal (de día; cámara mascota; tarjeta de decodificación).
- **Café:** la barra de cerca (macro; taza en corte; ticket de pedido).

### G. Hoja de ruta de 30 días
| Semana | Qué | Resultado |
|---|---|---|
| 1 | Revisión perceptual en `revisar_largo.py` · piloto de micro-escenas (Navy, 44 s) · subir Pixar y 5 casos con Test & Compare · Pixar v2 sin revelar en la intro | Métricas nuevas en cada video; primera muestra del lenguaje nuevo |
| 2 | Identidad de 1 canal (color, luz, firma) + banco de 15–20 piezas · X2 y X5 en Shorts | Un canal que se reconoce; primeros datos de ganchos |
| 3 | 1 largo completo con el método nuevo (guion visual → prueba animada → render) · conectar la curva de retención | Primer largo "película" |
| 4 | Segundo canal · primer ciclo de aprendizaje con datos · decidir el ritmo de publicación | Estándar actualizado con evidencia |

### H. Datos que necesito de Tao
1. ¿Qué largos ya están publicados, y cuántas vistas tienen?
2. Acceso a la **curva de retención** (por la API o exportada de Studio) y al CTR de cada largo.
3. En los Shorts: **vio vs. deslizó** y % visto por video.
4. ¿Los canales tienen **funciones avanzadas** activadas? Sin eso no hay Test & Compare.
5. ¿En qué dispositivo se ven más: teléfono o TV?
6. ¿Cuántas imágenes por día deja generar tu plan de ChatGPT?

### I. Las 3 decisiones estratégicas
1. **Cantidad o profundidad.** Hoy sale un largo por hora y se nota. Propongo 1–2 largos por semana en total, con 6–8 horas cada uno, mientras se construye el lenguaje. Los Shorts sostienen la frecuencia.
2. **Láminas ilustradas, sí o no.** Dan detalle rápido, pero cambian la identidad ("todo por código") y hay que emparejar el estilo. Se decide con el piloto.
3. **Qué canal es el buque insignia.** Rabbit tiene la brecha más grande y a ti te importa. MDM tiene la mejor base. Recomiendo **Rabbit**, porque es donde el lenguaje nuevo se va a notar más.

---

## Fuentes
- Zacks y colegas, límites de eventos y memoria: https://pmc.ncbi.nlm.nih.gov/articles/PMC2819197 · https://pmc.ncbi.nlm.nih.gov/articles/PMC5734104
- Señalizar límites de eventos mejora la memoria: https://link.springer.com/article/10.1186/s41235-016-0043-2
- Mayer, principios de diseño multimedia: https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf
- Cutting y colegas, cambios en el cine de Hollywood: https://pmc.ncbi.nlm.nih.gov/articles/PMC3485803 · https://link.springer.com/10.1186/s41235-016-0029-0
- Smith, Levin y Cutting, percepción de imágenes editadas: https://ualresearchonline.arts.ac.uk/id/eprint/21182/2/cf891501-bc1c-4904-bcee-5170766e6e53.pdf
- Detalles seductores (metaanálisis): https://news.wsu.edu/2020/03/19/seductive-details-inhibit-learning/
- Fredrickson y Kahneman, 1993: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/fredr-kahneman-jpsp1993.pdf · metaanálisis de 2022: https://ideas.repec.org/a/eee/jobhdp/v170y2022ics0749597822000334.html
- Parker y Stone, "but / therefore": https://nofilmschool.com/2015/04/tony-zhou-storytelling-video-essay-f-fake-therefore-but-and-then
- Documento de MrBeast (autenticidad no confirmada): https://simonwillison.net/2024/Sep/15/how-to-succeed-in-mrbeast-production/ · https://www.creatorhandbook.net/leaked-document-allegedly-reveals-mrbeasts-secrets-to-youtube-success-the-key-takeaways/
- Ayuda de YouTube, momentos clave de retención: https://support.google.com/youtube/answer/9314415 · https://support.google.com/youtube/answer/12942217
- NYT Visual Investigations (GIJN): https://gijn.org/stories/turning-dead-ends-into-breakthroughs-using-visual-investigation-techniques/
- Kurzgesagt, proceso: https://kurzgesagt.org/youtube/ · https://kottke.org/20/02/how-to-make-a-kurzgesagt-video-in-just-1200-hours
