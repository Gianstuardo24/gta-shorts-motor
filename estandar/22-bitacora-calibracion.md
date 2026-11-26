# 22 · BITÁCORA DE CALIBRACIÓN (se va llenando)

> **Qué es:** el registro de la calibración del libro de códigos, video por video.
> **Cambio de método (24-nov, 10:08, pedido de Tao):** las etiquetas las hago yo; **Tao aporta la parte humana**: su reacción como espectador. Reemplaza el reparto de la Parte C del doc 21, donde los dos etiquetábamos.
> **Sin código modificado.** Los videos de referencia se bajaron solo para estudio.

---

## 1. Método vigente
| Quién | Qué | Qué prueba |
|---|---|---|
| Claude | Etiqueta cada tramo **dos veces, en pasadas independientes** (la segunda, una instancia aparte que no ve la primera) | Si una etiqueta es **estable**. No prueba que sea correcta |
| Tao | Ve el video como espectador y anota dónde se iría, dónde no puede dejar de mirar, qué sorprende, qué sobra y si valió el tiempo | El **ancla externa**: lo que ninguna etiqueta puede inventar |
| Claude | Cruza las notas de Tao con etiquetas y mediciones | Si lo que se etiqueta tiene relación con lo que vive un espectador |

**Regla que se mantiene:** una etiqueta inestable no alimenta patrones.
**Regla nueva que sale del video 1:** donde se puede **medir**, se mide en vez de etiquetar (ver 2.4).

**Límites declarados:**
- Dos pasadas mías comparten mis sesgos.
- Un solo espectador (Tao). Sus notas son nivel C: observación, no prueba.
- No oigo el audio. Veo un cuadro cada 5 s y la lista de cortes; el texto son subtítulos automáticos.

---

## 2. Video 1 · Company Man, "Gatorade vs. Powerade"
| Dato | Valor |
|---|---|
| Canal | Company Man (1,8 M de suscriptores) |
| Vistas | 629 k (la mediana del canal es 159 k) |
| Duración | 12:31. Codificado de 0:24 a 11:15 (651 s); el patrocinio abre y cierra el video |
| Tramos | 25 |
| Pasada 1 | Sellada antes de recibir las notas de Tao (sha256 `7f007b8f…91c0d8`) |
| Pasada 2 | Hecha el 24-nov, 11:48, por una instancia aparte que solo recibió el libro de códigos, el texto por tramo, los cortes y los cuadros. No vio la pasada 1 ni mis descripciones |

### 2.1 Mediciones (no dependen de interpretación)
| Medida | Valor |
|---|---|
| Velocidad de la voz | **184 palabras por minuto** (entre 138 y 221 según el tramo) |
| Planos | 158 · mediana **3,0 s** · media 4,1 s |
| Planos de más de 10 s | 14, que suman **193 s de 651 (30 % del tiempo)** |
| Plano más largo | **22,9 s** (0:49): el gráfico de cuota de mercado |
| Otros planos largos | 17,2 s (titular, 9:22) · 16,3 s (gráfico de ventas, 3:59) · 15,2 s (cita en pantalla, 4:41) |
| Imagen frente a la palabra | En los 5 casos revisados, la imagen entra **entre 1 y 2,4 s antes** de la palabra clave (uno, 6,9 s antes) |

### 2.2 Notas de Tao como espectador (24-nov, 11:40)
| Nota | Dónde |
|---|---|
| **La voz se siente lenta.** A 1,25× se veía y se entendía mejor | Todo el video |
| **No valió los 13 minutos:** información estirada o lenta | Todo el video |
| Los cambios de escena están bien, pero faltan más cambios o más velocidad | Todo el video |
| **Se queda mucho tiempo en el gráfico**; el de cuota de mercado es visual pero monótono | Gráficos |
| Los gráficos muestran la relevancia del cambio mejor que casi cualquier otra cosa | Gráficos |
| La publicidad antigua de Gatorade llama la atención | Archivo |
| No podía dejar de mirar a un futbolista reciente y famoso: actualidad, fama, autoridad | Dentro de los dos primeros minutos (tramos 1 a 4), según Tao. El tramo 1 es el de corte más rápido del video: 13 cortes en 20 s |
| **Los elementos se anticipan bien a lo que se dice** (los billetes antes de la cifra, los atletas bebiendo antes de nombrar al público) | 3:05–3:25 |
| Le gustaría variar el orden: a veces el dato y luego la razón, a veces al revés | General |

### 2.3 Cruce: lo que sintió Tao frente a lo medido y etiquetado
| Lo que sintió | Lo que encontré | Lectura (hipótesis, nivel C) |
|---|---|---|
| Lento, estirado | La voz va a **184 palabras por minuto**, que no es lenta | **La lentitud no era de la voz.** ~~11 de 25 tramos no mueven ninguna pregunta~~ **(retirado: esa etiqueta resultó inestable, ver 2.7).** Lo que sí se sostiene: 30 % del tiempo en planos de más de 10 s |
| No valió el tiempo | Las dos pasadas coinciden en que la pregunta se plantea al inicio y el video recorre décadas en orden. **No coinciden** en si el tramo 2 entrega el desenlace ni en cuántos tramos responden algo | Sin pregunta viva, queda una cronología: va en la línea de G1 (hueco de información) y G7 (el orden crea la tensión). **Ojo con G14:** la evidencia sobre revelar el desenlace es inconclusa, y esto es un solo video y un solo espectador |
| Mucho tiempo en el gráfico | Los planos de gráfico duran **22,9 s, 16,3 s y 11,5 s**, contra una mediana de 3,0 s | Coincide. Lo sintió justo donde la medición marca los planos más largos |
| El gráfico igual es lo que mejor explica | Los 3 gráficos caen en tramos de "situar" o "pagar" | El problema no fue el gráfico, sino **el gráfico quieto**. Un gráfico que se construye por partes tendría el mismo valor sin el plano largo |
| El archivo antiguo atrae | 9 de 25 tramos son de archivo de época | Va en la línea de G6 (lo concreto y específico) |
| Los elementos se anticipan bien | La imagen entra 1 a 2,4 s antes de la palabra | **Tao lo vio y yo no:** yo había etiquetado "muestra" en 22 de 25 tramos |

### 2.4 Qué cambia en el libro de códigos
| Cambio | Motivo |
|---|---|
| **"La imagen frente a la voz" deja de ser etiqueta y pasa a ser medición:** segundos entre el corte y la palabra clave | Con un cuadro cada 5 s no puedo distinguir "muestra" de "anticipa". Los tiempos de palabra y de corte sí lo miden |
| **Se agrega una medida: duración del plano más largo por tramo** | Fue lo que mejor coincidió con una molestia de Tao |
| **"Sonido" queda como dato solo humano** | No oigo el audio |
| **"Velocidad de la voz" no basta para explicar "lento"** | 184 palabras por minuto y aun así se sintió lento. Hace falta una medida de **novedad por minuto**; todavía no la tengo definida |
| "Quién sabe más" y "a qué apunta" | Sospecho que son inestables: casi no variaron en mi pasada (18 de 25 iguales). Lo dirá la pasada 2 |

### 2.5 Lo que este video enseña sobre la selección
- Lo elegí por su cifra: es el más visto entre los recientes del canal, 4 veces su mediana. **No lo había visto.**
- A Tao no le pareció bien construido. **Más visto que lo normal en su canal no significa bien hecho:** puede ser solo un tema que atrae.
- Sirve igual, como caso de **tema fuerte con construcción plana**. Pero la selección necesita un segundo filtro: videos que a Tao le parezcan atrapantes.

### 2.7 Acuerdo entre las dos pasadas (25 tramos)
| Dimensión | Coinciden | Por azar se esperaba | Corregido por azar (kappa) | Estado |
|---|---|---|---|---|
| **Tipo de imagen** | 88 % | 28 % | **0,83** | ✅ Estable |
| **Función del tramo** | 80 % | 16 % | **0,76** | ✅ Estable, con dos fronteras que afinar |
| A qué apunta | 88 % | 53 % | 0,75 | ⚠️ Dudosa: casi todo cayó en "comprensión", así que el video no la pone a prueba |
| Quién sabe más | 84 % | 56 % | 0,63 | ⚠️ Dudosa: 20 de 25 en "igual"; "público más" coincidió 1 vez de 3 |
| La imagen frente a la voz | 96 % | 82 % | 0,78 | ❌ **Estable pero equivocada:** las dos pasadas pusieron "muestra" y Tao vio que la imagen se anticipa. Se reemplaza por medición |
| **Qué hace con la pregunta abierta** | **48 %** | 14 % | **0,39** | ❌ **Inestable. Bloqueada** |

**Por código, dentro de las dos estables:**
| Código | Coinciden | Nota |
|---|---|---|
| Archivo de época | 9 de 9 | — |
| Dato o gráfico | 2 de 2 | — |
| Producto | 6 de 9 | Se confunde con "documento" cuando el tramo mezcla titular y producto |
| Documento o prueba | 5 de 7 | Ídem |
| Complicar · Pagar · Respirar | 4 de 4 · 2 de 2 · 2 de 2 | — |
| Avanzar | 6 de 9 | — |
| Abrir · Girar · Cerrar | 2 de 3 · 2 de 3 · 1 de 2 | — |
| **Situar** | **1 de 3** | Se confunde con "abrir" y "avanzar" |
| **Reflexionar** | **0 de 2** | Se confunde con "cerrar" y "avanzar" |

**Dónde falló "la pregunta abierta"** (13 de 25 tramos):
| Tramo | Pasada 1 | Pasada 2 |
|---|---|---|
| 2 | Revelar | Plantear |
| 4 | Ninguno | Responder a medias |
| 5 | Ninguno | Responder a medias |
| 6 | Ninguno | Demorar |
| 9 | Ninguno | Responder a medias |
| 10 | Ninguno | Responder a medias |
| 13 | Revelar | Demorar |
| 17 | Ninguno | Responder a medias |
| 19 | Ninguno | Demorar |
| 20 | Ninguno | Demorar |
| 22 | Revelar | Responder a medias |
| 24 | Ninguno | Revelar |
| 25 | Plantear | Suspender |

**Por qué falló:** en un video cronológico la pregunta se plantea al inicio y no se vuelve a nombrar. Decidir si un hecho "responde a medias" o "no toca nada" depende de cuánto crea cada codificador que ese hecho explica la brecha. La pasada 1 puso "ninguno" en 11 tramos; la pasada 2, en 2. Es la dimensión más importante en teoría y la menos estable en la práctica.

**Límites de esta medición:** 25 tramos, un video, y dos pasadas del mismo modelo. Con tan pocos casos, los códigos que aparecen 2 o 3 veces no dicen casi nada. Sirve para detectar lo que falla, no para certificar lo que funciona.

**Otros hallazgos de la pasada 2:**
- **El detector de cortes no ve las superposiciones.** En el tramo 2 marca un solo corte, pero sobre el gráfico aparece y desaparece una silueta. El "plano de 22,9 s" es en realidad el mismo gráfico en pantalla con una figura encima. No cambia la lectura (Tao sintió mucho tiempo en el gráfico), pero "duración del plano" hay que entenderla como "tiempo sin que cambie el fondo".
- **Una diferencia entre voz e imagen en el tramo 23:** la voz dice el doble de electrolitos y el envase en pantalla dice 50 % más. Ninguna pasada lo codificó como "contradice".

### 2.8 Decisiones para la ronda 2
| Dimensión | Decisión |
|---|---|
| Tipo de imagen | Se usa. Regla nueva para tramos mixtos: gana lo que ocupa más segundos |
| Función del tramo | Se usa. Se reescriben "situar" (solo contexto previo a la historia, no hechos de la historia) y "reflexionar" (opinión del narrador sin pedirle nada al público) |
| A qué apunta · Quién sabe más | Se siguen anotando, **sin alimentar patrones**, hasta verlas en videos donde varíen |
| La imagen frente a la voz | **Medición:** segundos entre el cambio de imagen y la palabra clave |
| **La pregunta abierta** | **Se reemplaza.** En vez de una etiqueta por tramo, un **registro de preguntas**: cada pregunta que el video abre, con el segundo y la frase que la abre, y el segundo y la frase que la responde. Solo cuenta lo que tiene una marca textual. De ahí salen medidas: cuántas preguntas hay abiertas en cada momento y cuánto tarda cada una en cerrarse |
| Sonido | Solo lo anota Tao |

La ronda 2 (videos 2 y 3) prueba si estos cambios suben el acuerdo.

### 2.6 Pasada 1: etiquetas por tramo
| # | Tiempo | Qué pasa | Función | Pregunta abierta | Apunta a | Imagen | Cortes/min |
|---|---|---|---|---|---|---|---|
| 1 | 0:24–0:44 | Presenta la rivalidad: Coca-Cola creó Powerade para competir con Gatorade y, tras casi 40 años, sigue lejos | Abrir | Plantear | Atención | Producto | 39.0 |
| 2 | 0:44–1:07 | Tamaño de la brecha: cuota de mercado de cada marca; reconoce un avance, pero no la ve líder | Situar | Revelar | Comprensión | Dato o gráfico | 2.6 |
| 3 | 1:07–1:20 | Anuncia el enfoque: rivalidad desigual pero movida, contada década por década | Abrir | Prometer respuesta | Comprensión | Producto | 13.8 |
| 4 | 1:20–2:03 | 1960s: médicos de la U. de Florida inventan Gatorade, para qué servía y el ruido tras un triunfo del equipo | Situar | Ninguno | Comprensión | Archivo de época | 8.4 |
| 5 | 2:03–2:20 | 1960s: una empresa de alimentos compra los derechos, llega a las tiendas y a la NFL | Avanzar | Ninguno | Comprensión | Archivo de época | 14.1 |
| 6 | 2:20–2:36 | 1970s: década tranquila; crecimiento lento y un chicle de la marca | Respirar | Ninguno | Atención | Archivo de época | 7.5 |
| 7 | 2:36–2:55 | 1970s: Olympade, el primer intento de Coca-Cola, y la oportunidad que dejó pasar | Avanzar | Responder a medias | Comprensión | Texto en pantalla | 9.5 |
| 8 | 2:55–3:18 | 1980s: Quaker Oats compra la empresa dueña; Gatorade era lo que más le interesaba | Avanzar | Ninguno | Comprensión | Documento o prueba | 7.8 |
| 9 | 3:18–3:59 | 1980s: expansión: público más amplio, sabores, NBA, el baño de Gatorade, otros países | Avanzar | Ninguno | Comprensión | Archivo de época | 17.6 |
| 10 | 3:59–4:10 | 1980s: resultado de la década: las ventas se multiplican | Pagar | Ninguno | Comprensión | Dato o gráfico | 5.5 |
| 11 | 4:10–4:35 | 1990s: todos quieren entrar al mercado; aparecen marcas chicas | Complicar | Plantear | Atención | Archivo de época | 16.8 |
| 12 | 4:35–5:00 | Pepsi lanza Mountain Dew Sport; la frase dura de su vocero contra Gatorade | Complicar | Demorar | Emoción | Documento o prueba | 7.2 |
| 13 | 5:00–5:34 | Mountain Dew Sport desaparece; llega All Sport, con gas, y luego lo relanzan sin gas | Girar | Revelar | Comprensión | Archivo de época | 22.9 |
| 14 | 5:34–6:08 | Entra Powerade: primero solo en máquinas, después en botella; comercial que se compara con Gatorade | Complicar | Responder a medias | Comprensión | Documento o prueba | 15.9 |
| 15 | 6:08–6:19 | Powerade apuesta al deporte internacional (FIFA, Olímpicos) | Avanzar | Responder a medias | Comprensión | Archivo de época | 10.9 |
| 16 | 6:19–6:48 | Gatorade sigue arriba: Michael Jordan y sus campañas; cuota de mercado en 2000 | Pagar | Responder a medias | Comprensión | Archivo de época | 4.1 |
| 17 | 6:48–7:16 | 2000s: Pepsi compra Quaker Oats por una cifra enorme; Gatorade vuelve a ser el motivo | Girar | Ninguno | Atención | Documento o prueba | 6.4 |
| 18 | 7:16–7:35 | Pepsi tiene que vender All Sport; desde ahí es un duelo entre dos marcas | Situar | Ninguno | Comprensión | Documento o prueba | 9.5 |
| 19 | 7:35–8:23 | Ida y vuelta de productos: cada marca responde con su versión (aguas, cero azúcar, etc.) | Avanzar | Ninguno | Comprensión | Producto | 10.0 |
| 20 | 8:23–8:49 | Figuras: el comercial de Jordan contra sí mismo; LeBron firma con Coca-Cola y años después cambia | Respirar | Ninguno | Emoción | Archivo de época | 20.8 |
| 21 | 8:49–9:15 | 2010s: Powerade crece; aparece un competidor nuevo, BodyArmor, ligado a Kobe Bryant | Complicar | Plantear | Comprensión | Producto | 25.4 |
| 22 | 9:15–9:54 | 2020s: Coca-Cola compra BodyArmor; ahora tiene dos marcas y sigue lejos de Gatorade | Girar | Revelar | Comprensión | Documento o prueba | 21.5 |
| 23 | 9:54–10:16 | 2023: Powerade cambia etiqueta y fórmula; el narrador no sabe si eso la hace mejor | Avanzar | Suspender | Comprensión | Documento o prueba | 8.2 |
| 24 | 10:16–10:43 | Resumen y opinión final sobre las dos marcas | Reflexionar | Ninguno | Comprensión | Producto | 37.8 |
| 25 | 10:43–11:15 | Preguntas al público y pedido de comentarios | Cerrar | Plantear | Atención | Producto | 9.4 |

---

## 3. Video 2 · toldinstone, "Three Unfinished Roman Megaprojects"
| Dato | Valor |
|---|---|
| Canal | toldinstone (653 k suscriptores) |
| Vistas | 927 k (9,2 veces la mediana del canal) |
| Duración | 12:20. Codificado de 0:10 a 11:06, sin el patrocinio (5:43–6:55): 584 s |
| Tramos | 20 |
| Pasadas | Dos, independientes, con el libro de códigos versión 2. Pasada 1 sellada: sha256 `bba2afd9…46cbdb9` |

### 3.1 Notas de Tao como espectador (24-nov, 11:54)
| Nota |
|---|
| **No lo vio entero.** Monótono, con poca variación |
| **Las imágenes carecen de movimiento.** Ya está acostumbrado a que las cosas se muevan, "aunque sea un pequeño zoom" |
| **Lo más atractivo: el mapa cuando algo cambia en él o aparece una imagen** |
| Las imágenes quietas no le gustan |

### 3.2 Dos medidas nuevas, que salen de esta nota
| Medida | Qué mide | Cómo |
|---|---|---|
| **Tiempo sin ningún cambio en pantalla** | Cuánto del video pasa con la imagen totalmente quieta | Diferencia entre cuadros consecutivos (5 por segundo), mirando la zona de la pantalla que más cambia |
| **Cambios locales por minuto** | Cuántas veces aparece o se mueve algo en una zona sin que cambie el plano | Una zona cambia mucho y el conjunto, poco |

**Límite:** a esta resolución no detecta trazos finos (una línea que se dibuja sobre un mapa). Sí detecta una imagen que aparece.

### 3.3 Perfil medido de los tres videos
| Medida | 1 · Company Man | 2 · toldinstone | 3 · Kurzgesagt |
|---|---|---|---|
| Palabras por minuto | 184 | 132 | 164 |
| Cortes por minuto | 14,5 | 4,5 | 5,8 |
| Cambios locales por minuto | 7,2 | 1,0 | 11,6 |
| **Tiempo sin ningún cambio en pantalla** | **32 %** | **92 %** | **7 %** |
| Racha quieta más larga | 17,0 s | 32,8 s | 3,4 s |
| Tiempo en rachas quietas de 5 s o más | 22 % | 83 % | 0 % |
| **Reacción de Tao** | Lo terminó; lento, estirado; mejor a 1,25× | **No lo terminó**; quieto, monótono | Pendiente |

**Lectura (nivel C: un espectador, dos videos):** el video que Tao abandonó es el más quieto. Pero **con dos videos no se puede saber cuál medida manda:** el video 2 también tiene menos cortes y la voz más lenta. El video 3 las separa: pocos cortes y voz intermedia, pero casi nada de quietud.

### 3.4 Predicción registrada antes de que Tao vea el video 3
> **Si lo que lo expulsa es la pantalla quieta, el video 3 debería retenerlo mejor que los otros dos:** es el que menos tiempo pasa sin cambios (7 % contra 32 % y 92 %), aunque tiene **menos cortes** que el video 1 (5,8 contra 14,5 por minuto) y la voz va **más lenta** que en el video 1 (164 contra 184).
> **Si igual le parece lento o lo abandona,** la quietud no era la causa principal, y habrá que mirar el tema, el idioma o la cantidad de información nueva.

### 3.5 Acuerdo entre las dos pasadas (20 tramos, libro versión 2)
| Dimensión | Video 1 (kappa) | Video 2 (kappa) | Estado tras dos videos |
|---|---|---|---|
| **Tipo de imagen** | 0,83 | **0,80** (85 %) | ✅ **Estable en los dos** |
| **Registro de preguntas** (nuevo) | — | 5 de 6 emparejadas (**83 %**); el cierre coincide con 0 a 3 s de diferencia en 4 de 5 | ✅ **Mucho mejor que la etiqueta que reemplazó** (48 %). Falta repetirlo |
| A qué apunta | 0,75 | 0,78 | ⚠️ Sigue sin variar: 14 de 20 en "comprensión" |
| Quién sabe más | 0,63 | 0,69 | ⚠️ Ídem |
| **Función del tramo** | 0,76 | **0,35** (50 %) | ❌ **Cayó. No era estable: dependía del video** |

**Por qué cayó "función":** el video 2 son tres historias cortas seguidas. Las fronteras se vuelven borrosas: el arranque de cada historia (¿abrir o situar?), los desenlaces (¿girar, pagar o avanzar?). Reescribir "situar" y "reflexionar" no lo arregló.
**Prueba hecha después (no cuenta como confirmación):** agrupando la función en cuatro categorías gruesas (preparar, desarrollar, resolver, cerrar), el acuerdo sube a 0,81 en el video 1 y a 0,60 en el video 2. Mejora, pero sigue dudosa.

**Dónde falló "tipo de imagen":** el libro no decía dónde va el arte antiguo auténtico (un fresco romano, un busto). Una pasada lo puso como "pintura o ilustración" o "el objeto real"; la otra, como "archivo de época". Se corrige con una regla.

### 3.6 Lo que se concluye después de dos videos
| Qué | Fiabilidad | Decisión |
|---|---|---|
| **Mediciones** (voz, cortes, plano más largo, tiempo sin cambios, cambios locales, adelanto de la imagen) | No dependen de quién mire | **Base del análisis** |
| **Tipo de imagen** | Estable en los dos videos | Se usa. Regla nueva: arte auténtico de la época = "archivo de época" |
| **Registro de preguntas** con marca en el texto | Buen acuerdo en un video | Se usa, a confirmar en el video 3 |
| Función del tramo | Inestable | **No alimenta patrones.** Se prueba la versión de cuatro categorías en el video 3 |
| A qué apunta · Quién sabe más | Sin poner a prueba | No alimentan patrones |
| Pregunta abierta por tramo · Imagen frente a la voz (como etiqueta) | Fallaron | Eliminadas |

**La lección de fondo:** lo que se **mide** o se apoya en una **marca visible** (una frase, un tipo de imagen) es confiable. Lo que exige **interpretar la intención** de un tramo no lo es, al menos con este libro de códigos. El cerebro creativo tiene que construirse sobre lo primero.

### 3.7 Pasada 1 del video 2: tramos, imagen y quietud
| # | Tiempo | Qué pasa | Imagen | Plano más largo | Sin ningún cambio |
|---|---|---|---|---|---|
| 1 | 0:10–0:36 | Apertura: las hazañas romanas, y que a veces no terminaron; anuncia tres proyectos | Pintura o ilustración | 9.8 s | 96 % |
| 2 | 0:36–0:55 | N.º 3, mover el Tíber: por qué el río era vital para Roma | Pintura o ilustración | 8.5 s | 96 % |
| 3 | 0:55–1:38 | Las inundaciones: cuántas hubo y el relato de una, según un historiador antiguo | Documento o prueba | 42.3 s | 99 % |
| 4 | 1:38–2:00 | Más daños: muelles, almacenes, tiendas, enfermedades; empeoran con los siglos | Pintura o ilustración | 22 s | 100 % |
| 5 | 2:00–2:31 | César propone desviar el río: el plan del canal largo hasta la costa | Mapa o esquema | 15.8 s | 98 % |
| 6 | 2:31–2:55 | El plan más factible, rodear Roma; lo asesinan antes de empezar | Mapa o esquema | 20.7 s | 98 % |
| 7 | 2:55–3:36 | Augusto se conforma con dragar; el plan de Tiberio es rechazado; el río siguió inundando | Pintura o ilustración | 16.2 s | 92 % |
| 8 | 3:36–4:09 | N.º 2, el canal de Corinto: el rodeo peligroso del Peloponeso | Mapa o esquema | 25.3 s | 90 % |
| 9 | 4:09–4:50 | El istmo y la pista para arrastrar barcos por tierra; quiénes la usaron | Mapa o esquema | 23.7 s | 86 % |
| 10 | 4:50–5:20 | Por qué nadie cortaba el canal: la roca y la creencia de que un mar estaba más alto | Pintura o ilustración | 16.8 s | 99 % |
| 11 | 5:20–5:43 | César y Calígula lo pensaron; solo Nerón lo empezó; lo deja para después de la pausa | Texto en pantalla | 15.2 s | 63 % |
| 12 | 6:55–7:18 | Nerón inaugura la obra; quiénes cavaron y los pozos de inspección | Pintura o ilustración | 8.5 s | 97 % |
| 13 | 7:18–7:42 | Hasta dónde llegó la excavación por cada lado | Mapa o esquema | 24 s | 100 % |
| 14 | 7:42–8:10 | La muerte de Nerón detiene la obra; queda como símbolo de soberbia | Pintura o ilustración | 11.2 s | 69 % |
| 15 | 8:10–8:36 | Nadie lo retoma hasta el siglo XIX; el canal moderno borró las huellas | El objeto o lugar real | 9.0 s | 98 % |
| 16 | 8:36–9:10 | N.º 1, una capital para Germania: otros restos de conquistas que no cuajaron | Mapa o esquema | 30.6 s | 94 % |
| 17 | 9:10–9:38 | Los romanos fundan una ciudad civil al este del Rin | Mapa o esquema | 14.6 s | 94 % |
| 18 | 9:38–10:23 | Cómo era la ciudad y qué encontraron los arqueólogos | El objeto o lugar real | 45 s | 81 % |
| 19 | 10:23–10:48 | Cuándo se fundó y cuándo se abandonó | Dato o gráfico | 24.5 s | 99 % |
| 20 | 10:48–11:06 | El destino de la estatua y del sitio | El objeto o lugar real | 17.8 s | 98 % |

**Registro de preguntas (pasada 1):**
| Pregunta | Se abre | Se cierra | Tipo |
|---|---|---|---|
| ¿Cuáles son los tres proyectos y por qué quedaron sin terminar? | 0:30 | 10:38 | explícita |
| ¿Se hizo el desvío del Tíber que propuso César? | 2:03 | 2:52 | implícita |
| ¿Prosperó el plan de Tiberio de desviar afluentes? | 3:06 | 3:26 | implícita |
| ¿Qué pasó con el intento de Nerón? | 5:32 | 7:42 | explícita |
| ¿Qué fue de la ciudad romana en Germania? | 9:10 | 10:38 | implícita |

---

## 4. Video 3 · Kurzgesagt, "Astronomy Is In Crisis...And It's Incredibly Exciting"
Ya medido (tabla 3.3). Pendiente: que Tao lo vea, y las dos pasadas.

---

## 5. Corrección de rumbo: qué videos estudiar (24-nov, 12:09, pedido de Tao)
**Objeción de Tao:** no tiene sentido estudiar estos canales. Hay que estudiar **canales faceless de YouTube que estén teniendo éxito** y **canales de Shorts virales**.

**Tiene razón. Dónde me equivoqué:**
| Lo que hice | Por qué no sirve |
|---|---|
| Elegí canales famosos y antiguos (Company Man, toldinstone, Kurzgesagt) por juicio propio | Tienen público fiel que tolera su estilo; uno es un estudio con presupuesto grande. No se parecen a un canal faceless nuevo |
| Medí "destacado" contra la mediana del propio canal | En un canal grande eso mide cuánto atrae el tema, no si el video está bien hecho |
| Ignoré lo que ya teníamos | El estudio de micronichos del 22-nov ya había encontrado **canales chicos y nuevos con videos que rinden 40 a 750 veces su tamaño**, en nuestros nichos, y 10 de esos videos ya están bajados en el Mac |

**Lo que no se pierde:**
- El **método de medición** (voz, cortes, quietud, cambios locales) sirve para cualquier video.
- Las **reacciones de Tao**: voz más rápida, nada de imagen quieta, que algo cambie en pantalla.
- La lección sobre qué etiquetas son confiables.

**Nueva población de referencia (propuesta, a confirmar):**
| Grupo | Criterio | De dónde sale |
|---|---|---|
| **Largos faceless que rinden** | Sin cara · canal chico o nuevo · vistas muy por encima de sus suscriptores · en nuestros nichos o cercanos | Estudio de micronichos (22 y 23-nov) y las bases del Estudio (categoría "outlier chico") |
| **Shorts virales faceless** | Aparte, sin mezclar con los largos | Las 771 fichas de Shorts que ya tiene la biblioteca, 288 de ellas de control |
| Marcas faceless grandes (tipo fern o neo) | Solo como techo de calidad, no como modelo a copiar | Doc 21, reserva |

**La selección del doc 21 (Parte D) queda sin efecto.**

