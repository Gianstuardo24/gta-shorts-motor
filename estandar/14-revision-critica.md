# 14 · Revisión crítica de la auditoría (24-nov-2026)

> Encargo de Tao: actuar como un revisor independiente que **no está de acuerdo** con la auditoría (doc 13) y dejar solo lo que sobreviva.
> Antes de opinar, puse a prueba las dos métricas nuevas de la auditoría. Los resultados cambian su titular.

## 0. Prueba de las métricas: el titular "19 veces" estaba inflado
**Qué probé:**
- el detector de cortes con 5 niveles de sensibilidad, en vez de uno;
- una medida de variedad que no depende del color ni del tipo de transición: comparo la **composición** de un cuadro cada 3 s (en gris).

| Video | Cortes/min (umbral 0,25, el de la auditoría) | Cortes/min (umbral 0,10) | Composiciones distintas por min | Cuadros seguidos con la misma composición |
|---|---|---|---|---|
| Pixar | 15,3 | 31,9 | **9,5** | 22 % |
| Coca-Cola | 7,3 | 17,4 | 6,9 | 39 % |
| Perros | 1,8 | 16,7 | 5,6 | 39 % |
| 5 casos | 3,2 | 13,5 | 5,2 | 45 % |
| Navy | 0,8 | 11,3 | 4,6 | 45 % |
| Café | 2,5 | 11,2 | 4,0 | 47 % |

**Conclusiones:**
1. **La diferencia real entre Pixar y los demás es de ~2 veces, no de 19.** El "19×" salía de un umbral que no detecta cortes entre escenas oscuras parecidas, que son justo las de Rabbit.
2. **La dirección del hallazgo sí se sostiene:** con cualquier medida, Pixar es el más variado, y Café y Navy los menos.
3. **Los "looks" por color mezclaban paleta con imagen.** Café no tiene 6 imágenes: tiene 22 composiciones, casi todas con la misma paleta. El problema de Café y Navy es **paleta y escenario únicos**, más que falta de encuadres.
4. **"0 cortes en los primeros 30 s"** también dependía del umbral. Lo retiro como dato.
5. **Ninguna de estas medidas está validada contra tu gusto ni contra la retención.** Hoy solo hay dos juicios tuyos claros: Pixar te gusta y Navy no.

---

## 1. Recomendaciones genéricas (consejo común de YouTube con otro nombre)
| Recomendación | Por qué es genérica |
|---|---|
| "Pero / por lo tanto" en el guion | Consejo de oficio conocido. Vale solo si se vuelve un chequeo concreto |
| Giros al 25, 50 y 75 % | Fórmula tomada de un formato de desafíos; no sale de nuestros datos |
| "Final diseñado" y regla del pico y el final | Principio general, sin un diseño concreto para nuestros videos |
| "Un solo punto de atención" | Principio básico de composición |
| "Identidad por canal" en 10 puntos | Lista razonable, pero cualquier consultor la habría escrito sin ver los videos |
| Abrir con el objeto | **Ya estaba en nuestras reglas** (`hooks-retencion`, H1–H4). La presenté como nueva |

## 2. Demasiado caras para lo que prometen
| Recomendación | Costo real | Problema |
|---|---|---|
| Método de 12 etapas con 4 aprobaciones tuyas por video | +1–2 h por video y más esperas | Tú pediste ver menos vueltas, no más puertas |
| Láminas de ChatGPT (15–30 por video) | 3–5 min cada una a mano en el navegador: 1–2,5 h por video, más emparejar el estilo | Beneficio sin probar. Se prueba con 3, no con 30 |
| 6–8 h por largo como norma | 3–6 veces el tiempo actual | Ningún dato dice que la retención suba en esa proporción |
| Rehacer los 5 largos antes de tener un solo dato | ~4–5 h | Es la apuesta más cara con menos evidencia |
| Cruzar la curva de retención con los planos | ~2–3 h de herramienta | Con menos de 100 vistas por video no hay curva que cruzar |
| Maqueta que crece, cámara mascota, rama fantasma | 1,5 h o más cada una | Efectos de un solo uso |
| Las 34 técnicas a la vez | — | Nadie aprende qué funciona si cambia 34 cosas |

## 3. Conclusiones con evidencia débil
1. **El "19×"** (corregido arriba).
2. **Los umbrales "≥12 cortes/min", "look dominante ≤25 %" y "≥3 looks/min"** salen de un solo video (Pixar), que tampoco tiene retención medida. Eran una descripción de Pixar disfrazada de norma.
3. **"Más imágenes nuevas retienen más":** ningún estudio que cité lo dice. La teoría de eventos dice casi lo contrario: un corte no crea un evento nuevo. **La auditoría citó esa investigación y después puso una regla de cortes por minuto.** Es una contradicción interna.
4. **Los estudios de Mayer y de detalles irrelevantes miden aprendizaje, no retención.** Sirven para Perros y Café (explicar), y menos para MDM y Rabbit (historia).
5. **"Los Shorts como laboratorio de los largos":** son públicos y formatos distintos. Lo que gana en vertical de 40 s no tiene por qué ganar en horizontal de 10 min.
6. **"10 contra 10 Shorts":** las vistas de un Short dependen sobre todo del tema. Con 10 por lado, una diferencia de técnica se pierde en el ruido.
7. **Los conteos de las hojas** ("14 de 60 cuadros vacíos", "8 pantallas iguales") son a ojo, sobre un cuadro cada 8 s.
8. **"La oscuridad es un problema":** en Rabbit es identidad. Solo es defendible para Perros y Café, y es una opinión de diseño.
9. **"Etiquetas = redundancia":** en YouTube mucha gente mira sin sonido. No tengo ese dato para tus canales.

## 4. Reglas actuales que hay que conservar sí o sí
| Regla | Por qué |
|---|---|
| 2 fuentes por dato, sin caras reales ni logos, sin política | Es lo que hace defendible a los canales |
| Título, portada, descripción e intro no revelan el dato | Es tu regla más repetida y coincide con la teoría de la curiosidad |
| Nada sobre los subtítulos y ningún texto encimado | Es lo que más corregiste; ya está automatizado |
| Lo que se dice se ve, y el dato cae en la palabra | Coincide con la investigación (palabra e imagen a la vez) |
| **Tope de 4,5 s por plano** | Lo pediste tú ("3 o 4 segundos por encuadre"). **Retiro mi propuesta de planos de 6–8 s:** contradice tu pedido y no tengo datos |
| Cortes en las pausas de la voz | Gratis y limpio |
| Cuerpo natural, entradas desde fuera del cuadro | Errores que ya costaron horas |
| Variación y toque propio por video | Tu principio central; además protege contra la política de contenido repetitivo |
| Hoja de planos + tu OK antes del render | La única puerta que ya probó ahorrar renders |
| Avisar antes de tocar código; nunca dos renders a la vez | Estabilidad |
| Sin preguntas en la voz (mientras la voz no cambie) | Límite técnico real |

**Sobre "máximo 5 regresos":** Pixar tiene 19 y te gusta. Mi reformulación ("ningún regreso sin cambio") es una propuesta. **La regla es tuya y la decides tú.**

## 5. Ideas vistosas que pueden dañar la claridad
| Idea | Riesgo |
|---|---|
| 3–4 estilos visuales por video | El video se fragmenta y parece hecho por varias manos. **Máximo 2** |
| "Lo imaginado contra lo medido" (alien translúcido) | En un canal cuya promesa es la evidencia, mostrar aliens puede leerse como afirmarlos |
| Rama fantasma ("qué habría pasado") | Mezcla hecho con hipótesis en la imagen |
| Medidor de certeza + etiqueta de fuente + subtítulos | Más texto en pantalla. **Contradice mi propia regla** de bajar el texto |
| Ráfaga de montaje (4–6 imágenes en 2 s) | En videos que explican, es ruido |
| Marcador de promesa (5 carpetas, 10 tazas) | Le muestra al espectador cuánto falta |
| Silencios de ~1 s con voz IA | Pueden sonar a falla del video |
| Ocultar el subtítulo en los títulos | Inconsistente para quien lee |
| Corte por forma forzado | Si no nace solo del contenido, se nota el truco |
| Cámara mascota con lente deformado | El animal, que es el protagonista, deja de verse |

## 6. Redundancias
- Las debilidades 1, 3 y 8 de la auditoría son la misma: **las reglas no están en el código.**
- "Cortes reales", "looks por minuto" y "look dominante" miden lo mismo. **Basta una medida.**
- El tablero que se llena y el marcador de promesa son una sola idea; lo mismo el medidor de certeza con la etiqueta de fuente, y el vertido con el macro y la taza.
- El guion visual ya estaba en el doc 10, y los experimentos en el doc 12 con otra numeración.
- Las reglas de apertura repetían `hooks-retencion`.

## 7. Oportunidades que pasé por alto
| Oportunidad | Por qué importa | Costo |
|---|---|---|
| **Publicar ya para tener una línea base** | Sin un video público con datos, todo lo demás es opinión | 0 |
| **Luz y color por canal** (Perros y Café de día) | Cambia todos los cuadros de todos los videos de ese canal de una vez | ~1 h, una sola vez |
| **Personaje v2** (volumen, ropa, expresiones) | También afecta todos los cuadros. Ya estaba planificado en `referencia-calidad` y quedó sin hacer | 2–3 h, una sola vez |
| **La voz** | La auditoría casi no la tocó, y tú ya pediste una más joven y natural | Probar 1 canal |
| **El tema y el empaque** | Suele pesar más que cualquier mejora visual. Tenemos 3 títulos por video listos y sin correr | 0 |
| **Leer en el teléfono** | El subtítulo se probó en pantalla grande. Nunca revisamos un cuadro al tamaño de un celular, como sí hacemos con las miniaturas | 15 min |
| **Versión en español de los largos** | Misma imagen, otra voz y otros textos: casi otro video por ~15 % del trabajo | Por verificar |
| **El sonido** | Recomendé sonido sin haberlo evaluado. No puedo escucharlo; tu oído es la única revisión | Tu revisión |
| **Banco mínimo por canal** | 8–10 piezas donde el tema es el protagonista suben la variedad de forma automática en todos los videos del canal | ~1,5 h por canal |

## 8. En qué no estaría de acuerdo un director de animación de primer nivel
1. **"Están contando cortes y no están mirando la actuación."** Un personaje que piensa, duda o reacciona bien sostiene 5 s sin corte. Los nuestros no actúan: no mueven la boca y las poses no tienen anticipación ni remate.
2. **"Un video con un estilo fuerte gana a uno con cuatro estilos."** Pediría un guion de color: una paleta por acto dentro de **un** mismo lenguaje.
3. **"El guion visual no es una tabla."** Se dibuja en miniaturas, porque la composición no se decide con palabras.
4. **"Arreglen el diseño del personaje antes de inventar 34 técnicas."** El atractivo del personaje está en cada cuadro.
5. **"Las láminas de IA van a pelear con el vector."** Dos lenguajes gráficos en un video se notan.
6. **"El corte se justifica por la historia, no por una cuota."**

## 9. En qué no estaría de acuerdo un analista de retención con experiencia
1. **"Sin impresiones no hay retención que mejorar."** En canales chicos el cuello de botella suele ser que el video no se muestra ni se cliquea. Primero tema, título y miniatura.
2. **"No optimicen un promedio; miren dónde cae la curva."** Lo normal es que la mayor caída esté al principio. Poner el esfuerzo parejo en los 10 minutos es gastar donde ya no hay gente.
3. **"Su plan de experimentos no tiene potencia."** Pocos videos, pocas vistas y muchas variables a la vez. Un cambio por vez, y aceptar que varias preguntas no se podrán responder pronto.
4. **"Shorts y largos son negocios distintos."** No extrapolen.
5. **"La duración la decide el contenido."** 10–12 min sin datos puede ser relleno.
6. **"Constancia."** Un canal que publica largos de forma regular aprende más rápido que uno que pule un video un mes.
7. **"La voz y los primeros 15 s pesan más que el plano 140."**

## 10. Si solo hubiera 20 % más de tiempo por video (~30 min en un largo de 2,5 h)
| Minutos | En qué | Por qué |
|---|---|---|
| 15 | **Diseñar a mano los primeros 30 s:** el tema como protagonista desde el primer cuadro y 5–6 imágenes propias | Es donde YouTube mide la intro y donde más conviene concentrar el oficio |
| 10 | **Marcar en el guion 5 momentos** donde el tema tiene que llenar el cuadro (la taza, el objeto, el gesto del perro), y construir esas 5 piezas | Ataca la debilidad más clara: el tema no es protagonista |
| 5 | **Leer el guion como espectador aburrido** y revisar que el dato clave no salga antes de tiempo | Cuesta casi nada |

Todo lo demás (luz por canal, voz, chequeos) se hace **una sola vez** y queda automático.

---

## Plan estratégico revisado
### Principios
1. **Primero datos, después rediseño.** Nada grande sin una línea base.
2. **Primero lo que mejora todos los cuadros** (luz, personaje, voz, banco del canal), después lo que mejora un video.
3. **El oficio se concentra en el inicio** y en pocos momentos elegidos.
4. **Un cambio por vez.**
5. **Las métricas nuevas informan; no aprueban ni rechazan** hasta estar validadas contra tu juicio.

### Pasos
| # | Paso | Quién | Tiempo | Se considera logrado cuando… |
|---|---|---|---|---|
| 1 | Subir Pixar con sus 3 títulos y 3 miniaturas en Test & Compare. Decirme qué largos están públicos y con cuántas vistas | Tao | 10 min | Hay un largo público midiendo |
| 2 | Decidir qué hacer con los otros 5 largos (ver "Decisión" abajo) | Tao | — | — |
| 3 | **Arreglos globales, una sola vez:** luz y color de día para Perros y Café · voz estándar aplicada por código · chequeos nuevos en la revisión (dato clave en los primeros 30 s, pregunta en la voz) · informe de variedad por composición | Claude (aviso antes de tocar código) | ~1,5 h | Los 6 videos se pueden volver a renderizar con esos arreglos |
| 4 | **Banco mínimo de Rabbit:** 8–10 piezas con el tema como protagonista (3 pantallas de sensor distintas, radar, expediente con sello, mapa, diagrama de paralaje) | Claude | ~1,5 h | El armado automático las usa solo |
| 5 | **Piloto de 60 s de Navy,** solo con código. Aparte, **3 láminas de prueba** para medir costo y si calzan con el estilo | Claude | ~1,5 h + 30 min | Tú comparas el piloto con la versión actual y decides sobre las láminas |
| 6 | **Un largo de Rabbit** con el banco nuevo, los primeros 30 s diseñados a mano y 5 momentos marcados | Claude + tu OK a la hoja de planos | ~3 h | Publicado |
| 7 | Leer los datos cuando el video tenga vistas suficientes (varios cientos) y comparar con Pixar a la misma edad | Claude | 30 min | Una conclusión escrita, con su nivel de confianza |
| 8 | Recién entonces: personaje v2, banco de otro canal o prueba de voz, **de a uno** | — | — | — |

### Decisión que te toca en el paso 2
| Opción | Costo | A favor | En contra |
|---|---|---|---|
| A. Publicarlos como están | 0 | Línea base inmediata | Llevan la entrada de GTA y no te convencen |
| **B. Arreglos baratos + nuevo render, y publicar 2–3** (recomendada) | ~20 min de render cada uno, casi sin trabajo mío | Línea base sin los defectos más visibles | Siguen siendo "versión vieja" |
| C. Rehacerlos todos al lenguaje nuevo | 4–5 h | Quedan como quieres | Apuesta cara, sin datos |

### Lo que eliminé de la auditoría
| Eliminado | Motivo |
|---|---|
| El titular "19 veces" y los umbrales de cortes y looks como norma | Artefacto de medición; salían de un solo video |
| Planos sostenidos de 6–8 s | Contradice tu pedido; sin datos |
| Giros fijos al 25, 50 y 75 % | Fórmula ajena |
| Método de 12 etapas | Pasa a 3 puertas: empaque → hoja de planos → render |
| Guion visual plano por plano de todo el video | Queda solo para los primeros 30 s y los 5 momentos marcados |
| 6–8 h por largo como norma | Sin evidencia |
| Láminas como camino principal | Pasan a prueba de 3 |
| 4 estilos por video | Máximo 2 |
| Alien translúcido, rama fantasma, marcador de promesa, ráfagas, ocultar subtítulos, cámara mascota, maqueta | Riesgo de claridad o costo |
| Medidor de certeza | Queda solo la etiqueta de fuente, con mesura y solo en Rabbit |
| Shorts como laboratorio de la imagen de los largos | Solo sirven para probar ganchos y títulos |
| Cruce de la curva de retención con los planos | Se pospone hasta tener vistas |
| "Un tercio de la novedad en la segunda mitad" | Sin validar |

### Lo que sobrevive de las 34 técnicas (8)
1. Gancho con el objeto en el primer cuadro (ya era regla).
2. Entrar a la evidencia (Rabbit).
3. Diagrama que nace de la escena (Rabbit, Perros, Café).
4. Ficha del trato con la cifra tapada (MDM).
5. Taza en corte + macro (Café).
6. Repetición lenta con flechas y etiquetas pegadas al cuerpo (Perros y Gatos).
7. Tablero que se llena entre capítulos (Rabbit, MDM).
8. Foco dirigido en la palabra clave (todos).

### Lo que sigue en pie del diagnóstico
- Las reglas no estaban en el código y la revisión aprobaba todo.
- No hay datos de ningún largo.
- En Café, Perros y Navy el tema no es el protagonista y casi todo pasa en un solo escenario con una sola paleta.
- Pixar es ~2 veces más variado que el resto, con cualquier medida.
- Pixar revela la respuesta en los segundos 5–10.
- Los seis guiones cierran con la misma fórmula.
