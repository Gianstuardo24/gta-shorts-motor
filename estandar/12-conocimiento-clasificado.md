# 12 · Conocimiento clasificado (auditoría profunda, 23-nov)

> Método: el "Deep Learning & Creative Audit" que propuso ChatGPT, aplicado por Claude **con acceso real** a los archivos, renders, registros de planos y datos.
> Cada ítem lleva **ID**, **confianza** y **fuente**, para que nada se pierda y se pueda discutir.

## Fuentes auditadas
| Fuente | Estado |
|---|---|
| Chat principal, turnos 1686–1782 (fase MDM) + mensajes 23:04, 23:07 y 23:28 | ✅ |
| Memoria del proyecto `estrategia-shorts` (reglas de los Shorts, 16–23 nov) | ✅ |
| `referencia-calidad`, `hooks-retencion`, `curiosfer-investigacion`, `faceless-laboratorio`, `mdm-tops`, `mdm-miniaturas`, `largos-planos` | ✅ |
| Respuesta de ChatGPT del 23-nov (master prompt y sistema) | ✅ |
| Chat principal, turnos 1–1685 · `manual-fabrica-shorts` · `canales-perros-gatos` · `faceless-fichas` · `banco-angulos-virales` · `marketing-expertos` · `contenido-viral` · otros chats del proyecto | ⬜ pendiente (ver "Próximas tandas") |

**Escala de confianza:**
- **M:** medido en nuestros datos;
- **T:** pedido o confirmado por Tao;
- **V:** externo verificado (fuente oficial o estudio);
- **H:** hipótesis sin medir.

---

## A. Patrones en lo que pide Tao (análisis de frecuencia)
Agrupé todos los pedidos por tema. Lo que se repite muestra **dónde falla el sistema**, no solo qué le gusta.

| # | Patrón | Veces pedido | Ejemplos | Qué significa | Solución de fondo |
|---|---|---|---|---|---|
| 1 | **Variación / no repetir** | ≥10 | escenarios propios (21-nov), "la variación es la retención", menos repeticiones, escenas fuera de los sets, ≤5 regresos, micro-escenas | El motor tiende a **reutilizar** por defecto | Invertir el defecto: **lo nuevo es la norma y lo reutilizado la excepción**, con métricas de unicidad automáticas |
| 2 | **Nada tapa nada** | ≥8 | carteles y globos no tapan personas, THE DREAM, figura sobre subtítulos, sillón/cojín, cierre más arriba | El acomodo se hace a mano y sin medir | **Revisión automática de choques** entre todo lo que hay en pantalla, no solo la franja de subtítulos |
| 3 | **Ritmo** | ≥7 | voz más rápida, pausas cortas, cheque largo, 3–4 s por encuadre, mucho tiempo en escena | Sin un tope medido, el armado se alarga | Topes duros medidos (plano ≤4,5 s, ≥20 cambios por minuto) |
| 4 | **No revelar el pago** | ≥7 | descripciones sin precios, sin comentario fijado, título, portada, intro y capítulos | Es **un solo principio** que se pidió pieza por pieza | **Regla del pago único:** el pago se revela una vez, dentro del video, en su momento. Se revisa en todas las piezas a la vez |
| 5 | **Cuerpo natural** | ≥9 | patas de animales, sentarse de frente, auto vs. cuerpo, pararse sin deformar, mano tras la cabeza, dedo en la cara, codo, aplauso | Cada arreglo de poses rompe otra | **Hoja de poses** de regresión: todas las poses en una imagen cada vez que se toca el motor |
| 6 | **Pertinencia** | ≥8 | efectos de sonido del tema, efecto fiel (Star Trek), insertos según la frase, gráficos por video (no fijos por canal), música por canal, nada de stickers genéricos | Lo genérico se cuela cuando falta contexto | Regla: **cada elemento se justifica por la frase o el tema**; si no, no va |
| 7 | **Se ve trabajado** | ≥7 | sofisticado, luces, objetos con referencia real, no "tipo IA" ni "tipo Claude", detalle en ropa y caras, micro-escenas | La calidad sube por detalle acumulado | Biblioteca de detalles + **láminas ilustradas** + luz cinematográfica por defecto |
| 8 | **Ver antes de generar** | ≥4 | muestras de escenas antes del video completo, hoja de planos, "que no se detenga hasta que pase" | Las vueltas largas cuestan horas | **Puertas de aprobación** (guion visual → muestra → render) + autocorrección hasta pasar la revisión |
| 9 | **Aprender y medir** | ≥7 | análisis de hooks y psicología, títulos, mejores casos x20–x100, arsenal, reglas por tipo, medir tiempos | Es el pedido más estratégico y **la capa más vacía** | Ciclo de rendimiento automático (ver D) |

**Relación clave:**
- Los patrones **2, 3 y 5** son errores que vuelven: se resuelven con **automatización**, no con memoria.
- Los patrones **1, 6 y 7** son creativos: se resuelven con **guion visual aprobado + biblioteca que crece + láminas**.
- El patrón **9** se resuelve con **datos de retención alineados a lo que había en pantalla**.

---

## B. Base de conocimiento clasificada

### B1. Reglas permanentes (no se rompen)
| ID | Regla | Conf. | Fuente |
|---|---|---|---|
| R-01 | Todo dato con 2 fuentes o más; sin política; sin urgencia falsa; sin promesas de dinero | T | reglas base |
| R-02 | Sin caras reales, logos, deepfakes ni personajes con derechos; material ajeno solo para entender | T | reglas base |
| R-03 | Nada tapa nada: textos, globos, carteles, papeles y cifras no tapan personas ni otros textos; la franja de subtítulos queda libre | T | 21-nov, 1707, 1717 |
| R-04 | Subtítulos de máximo 2 líneas | T | 21-nov |
| R-05 | Ninguna pregunta directa en la voz (tampoco en el gancho): se dice implícita ("la pregunta es si…") y se muestra grande en pantalla | T | 21-nov |
| R-06 | Regla del pago único: título, portada, descripción, intro y capítulos no revelan el dato clave | T | 22–23 nov |
| R-07 | Descripción: corta, plantea una duda, 4–5 hashtags, CTA breve. Sin "VIDEO RELACIONADO" y sin comentario fijado | T | 22-nov, 23-nov |
| R-08 | Nunca se republica el mismo video; ES y EN nunca el mismo video el mismo día | T | reglas base |
| R-09 | Máximo 2 Shorts por día por canal | T | 21-nov |
| R-10 | Nada se publica sin OK de Tao; se avisa antes de cambiar código | T | reglas base |
| R-11 | Un plano en escenario nunca dura más de 4,5 s | T | 1734 |
| R-12 | Ningún espacio vuelve más de 5 veces; ningún inserto se repite salvo regreso a propósito | T | 23:07, 1774 |
| R-13 | Cuerpo natural: manos delante de la cara, codo abajo, patas con muslo, articulación y almohadilla, proporciones reales, sentarse de frente sobre el cojín | T | 21-nov, 1736–1776 |
| R-14 | Un protagonista no se parece a nadie más (nada de corona ni barba igual en los demás) | T | 21-nov |
| R-15 | Lo que sale de una escena no reaparece en la siguiente ni queda quieto en el aire | T | 21-nov |
| R-16 | Pantalla completa y escena continua: nada de cuadros encajonados | T | 21-nov |
| R-17 | Palabras simples que entiende la mayoría ("probe" → "ship") | T | 20-nov |
| R-18 | Finanzas y salud: sin "persona IA experta", informativo y con fuentes | V | faceless-lab §1 |
| R-19 | Cada video se ve y se cuenta distinto (política de contenido "genérico o repetitivo") | V | YouTube, jul-2026 |

### B2. Preferencias creativas de Tao
| ID | Preferencia | Fuente |
|---|---|---|
| P-01 | El video es una **película de micro-escenas** (POV, reflejos, detalles del lugar, manos); el set es un tipo de plano más | 23:28 |
| P-02 | Escenarios y fondos **propios por video y por escena**; a veces muchos personajes, a veces solo objetos | 23-nov |
| P-03 | Objetos protagonistas con detalle y referencia en objetos reales | 1693, 23-nov |
| P-04 | Luz nocturna cinematográfica variada (postes, lámparas, neón, penumbra) y **vida de fondo** | 21-nov |
| P-05 | La acción se muestra con zoom y detalle (un vidrio que se triza) en vez de texto; interfaces que se mueven (tablet que escribe sola, app, mando con botón) | 21-nov |
| P-06 | Transiciones de cine: fluidas, con desplazamiento, sin saltos ni barridos bruscos | 21-nov, 1742 |
| P-07 | Personajes como actores con rol, que interactúan; no quietos | 21-nov |
| P-08 | Títulos de Shorts de ~45 caracteres o menos, intensos y con la consecuencia real | Shorts |
| P-09 | Títulos de largos: moldes famosos, polémicos pero verdaderos, entendibles, con nombres conocidos solo si son protagonistas | 23-nov |
| P-10 | Ángulos que conectan con la vida del espectador: consecuencia, aversión a la pérdida, tono oscuro, siempre verdadero | Shorts |
| P-11 | MDM cierra con una enseñanza ("no cometas este error"); CTA hablado + flecha al canal ("Follow for the next million dollar mistake") | 21-nov |
| P-12 | Música: funk solo en Repers; ni en Rabbit ni en GTA música animada o infantil | 20-nov |
| P-13 | Efectos de sonido variados y del tema; whoosh corto sí, el whoosh largo de giro no; pops bajos | Shorts |
| P-14 | Imágenes de marca y miniaturas que no se vean "IA": diseñadas, simples, a pantalla completa | Shorts |
| P-15 | Videos que explican: decir **por qué** pasa | 23-nov |
| P-16 | Cada video con un toque propio; reglas por tipo de video, no una fórmula única | 23-nov |
| P-17 | Largos de 10–12 min | 1780 |

### B3. Estándares técnicos (cómo se cumple)
| ID | Estándar | Dónde |
|---|---|---|
| T-01 | Voz 1,18× con pausas de 0,20 s y 0,28 s | `compactar_voz.py` |
| T-02 | Encuadre cada 2,4–3,4 s, cortando en pausas | `planos_tiempo.py` |
| T-03 | Entradas desde fuera del cuadro (±230 px) | `planos_tiempo.py` (FUERA) |
| T-04 | Topes de insertos: capítulo 1,9 s · cheque 4,9 s · balanza 4,4 s · tablero 6,5 s | `recortar_insertos.py` |
| T-05 | Títulos y cifras: máximo 6 s, con plano general mientras están | `planos_tiempo.py` |
| T-06 | Etiquetas abajo a la izquierda; los letreros del set se apagan cuando aparece una etiqueta | `chipDoc`, `__HT` |
| T-07 | Corte limpio; mismo lugar = deslizamiento; fundido smoothstep | `escena_h.html`, `transH` |
| T-08 | Apertura sin el mundo de GTA de fondo | `escena_h.html` |
| T-09 | Revisión de subtítulos, planos y repeticiones + hoja de planos | `revisar_largo.py`, `hoja_planos.py`, `revisar_insertos.py` |
| T-10 | Efectos sintéticos por inserto y subida de tensión antes de cifras | `sintet_sfx.py`, `SFXSET` |
| T-11 | `planos_hint` siempre en el `b.py` | `b.py` |

### B4. Hipótesis por validar (no son reglas todavía)
| ID | Hipótesis | De dónde sale | Cómo se valida |
|---|---|---|---|
| H-01 | En largos, un plano cada ~2,8 s retiene más que uno cada 5–8 s | referencias (curiosfer 3–5 s; explicadores 8–17 cortes/min) | curva de retención: piloto de micro-escenas vs. largo actual |
| H-02 | 35–45 % del tiempo fuera del set es el punto justo | Pixar (Tao lo aprobó) | comparar las caídas en planos de set vs. insertos |
| H-03 | Las láminas ilustradas se perciben más "trabajadas" que el código solo | la imagen de referencia de Tao | piloto A/B visto por Tao + retención |
| H-04 | Los títulos con pregunta rinden menos (−18 %), salvo los moldes famosos | vidIQ (V) | Test & Compare del largo de los 5 casos |
| H-05 | La animación tipo escena rinde más que las imágenes en movimiento | análisis del 20-nov (M, muestra chica) | seguir midiendo por formato |
| H-06 | La aversión a la pérdida es el gancho que más rinde en GTA ES/EN | Tao (M en sus canales) | ranking de ganchos del reporte semanal |
| H-07 | La voz IA de catálogo baja la percepción de calidad; una voz propia o clonada sube | faceless-lab (V/H) | probar Chatterbox o la voz de Tao en un canal |
| H-08 | Un personaje fijo por canal cumple el "trabajo de la cara" | faceless-lab (patrón) | Biscuit/Mochi en Perros y Gatos |
| H-09 | Los largos se juzgan a los 28 días, no a las 24 h | Creator Insider (V) | comparar a la misma edad |

### B5. Experimentos pendientes (uno a la vez, con fecha)
| ID | Experimento | Métrica | Estado |
|---|---|---|---|
| X-01 | Piloto de micro-escenas (Navy, 0–44 s) vs. versión actual | opinión de Tao → retención a 30 s y % visto | propuesto |
| X-02 | Láminas IA + código vs. solo código | tiempo de producción + opinión + retención | propuesto |
| X-03 | 3 títulos en Test & Compare por largo (famoso / polémico / molde que esconde) | cuota de tiempo de visualización | Pixar y 5 casos listos para subir |
| X-04 | Voz más joven (Chatterbox) | retención + comentarios | pendiente |
| X-05 | Personaje fijo con opinión (Perros/Gatos) | vio vs. deslizó, % visto | pendiente |

### B6. Errores que no deben volver (con la causa)
| ID | Error | Causa | Prevención |
|---|---|---|---|
| E-01 | Sets propios de Pixar en Coca-Cola | biblioteca sin "dueño" | marcar los sets por video; la revisión avisa |
| E-02 | Inserto que no calza con la frase (claqueta en "short video") | palabras clave muy amplias | elegir por frase + lista de exclusión |
| E-03 | Pantallas iguales en casos distintos (Rabbit) | un solo contenido de TV | la revisión marca pantallas repetidas |
| E-04 | Un video entero en el mismo espacio (Café) | sin mapa de espacios | contar regresos en la revisión |
| E-05 | Fondo de GTA en la apertura | mundo por defecto | ✅ arreglado |
| E-06 | `L.hints` no llegaba al armado | paso faltante | ✅ checklist |
| E-07 | La cifra `$1` se perdía en bash | comillas dobles | comillas simples |
| E-08 | La botella de contorno de Coca-Cola en la miniatura | forma protegida | regla R-02 |
| E-09 | Errores de hecho (censores vs. revisores en Corea; "Superman got nothing") | redacción que exagera | verificación + revisar palabras fuertes |
| E-10 | "VIDEO RELACIONADO" en las descripciones | plantilla vieja | ✅ quitado del generador |

### B7. Oportunidades que no estamos aprovechando
| ID | Oportunidad | Por qué importa | Esfuerzo |
|---|---|---|---|
| O-01 | **Curva de retención alineada con el registro de planos:** sabemos qué había en pantalla en cada segundo, así que cada caída se puede atribuir a un tipo de plano, inserto o capítulo | casi nadie tiene ese dato; convierte el gusto en evidencia | medio |
| O-02 | Banco de recursos **por canal** (hoy solo MDM tiene) | causa raíz de los videos lentos | medio |
| O-03 | Láminas ilustradas animadas | salto de detalle con poco tiempo | medio |
| O-04 | 2–3 Shorts por largo que lleven al largo con el campo "video relacionado" de Studio (no en la descripción) | los largos dan ingresos y los Shorts, alcance | bajo |
| O-05 | Personaje fijo o firma visual por canal | reemplaza la cara en un canal sin rostro | medio |
| O-06 | Formatos de mucho tiempo de visualización antes del cambio de YPP del 1-feb-2027 | los canales nuevos necesitan 8.000 h | alto |
| O-07 | Capa 3D (cámara que viaja por un mundo) | es lo que distingue a los referentes | alto |

---

## C. Crítica a la propuesta de ChatGPT (qué tomo y qué corrijo)
**Tomo:**
- las 3 capas: ADN creativo, inteligencia creativa e inteligencia de rendimiento;
- separar reglas de hipótesis y marcar la confianza;
- el ciclo posterior a la publicación con "knowledge update";
- el puntaje del storyboard;
- "los archivos son la fuente de verdad".

**Corrijo:**
1. **Faltan canales:** habla de 4 marcas, pero también están GTA ES/EN, Repers y Number Signs. Y deja fuera **todo lo aprendido en los Shorts**, que es la mayor parte del conocimiento.
2. **Contradicción:** dice "no usamos imágenes", pero la dirección nueva incluye láminas ilustradas. Hay que decidirlo (experimento X-02), no prohibirlo de antemano.
3. **El puntaje tiene pesos inventados.** Lo hago **medible** con lo que ya calculamos (ver D) y lo calibro con la retención real.
4. **"Investiga externamente":** ChatGPT puede inventar fuentes. Todo lo que traiga pasa por la regla de 2 fuentes antes de entrar aquí.
5. **Dos cerebros se desalinean.** La fuente de verdad es este proyecto. ChatGPT recibe una copia de `MAESTRO.md` y lo que propone vuelve aquí filtrado. Nunca al revés.
6. **No tiene nuestros números de base** (cortes por minuto, vio vs. deslizó, duración de planos). Sin eso, sus recomendaciones son genéricas.

---

## D. Cómo usamos los prompts de forma inteligente
| Prompt de ChatGPT | Quién lo ejecuta | Cómo |
|---|---|---|
| Master Prompt | ChatGPT, en un proyecto **"YouTube Creative Intelligence"** | versión corregida (`master_prompt_chatgpt.md`) + `MAESTRO.md` como archivo del proyecto |
| Deep Learning & Creative Audit | **Claude**, sobre el material real (este documento); ChatGPT como segunda opinión | por tandas de fuentes; cada hallazgo entra aquí con ID y confianza |
| Post-Publication Learning Loop | **Claude** con datos automáticos; ChatGPT revisa la interpretación | a los 7 y 28 días de cada largo: curva de retención (API de YouTube Analytics) + registro de planos → caídas y picos por plano → "knowledge update" |
| Storyboard Quality Score | **Claude**, calculado, antes de cada render | 8 criterios medidos (abajo) + juicio de Tao |

### Puntaje del storyboard, medible (sobre 100)
| Criterio | Cómo se mide | Peso |
|---|---|---|
| Variedad de espacios | espacios distintos ÷ capítulos; regresos ≤5 | 15 |
| Variedad de planos | entropía de tipos de plano; sin repeticiones seguidas | 10 |
| Acción en el plano | % de planos con ≥2 cosas que se mueven | 15 |
| Progresión narrativa | cada capítulo agrega dato, giro o consecuencia (revisión de Claude + Tao) | 20 |
| Originalidad | % de micro-escenas únicas (meta ≥60 %) y toque propio presente | 15 |
| Representación de información | % de cifras, listas y comparaciones con gráfico propio | 10 |
| Ritmo y anticipación | plano promedio de 2,5–3,5 s; gráficos que entran antes de la palabra | 10 |
| Identidad del canal | registros y recursos del canal presentes | 5 |
El puntaje **detecta debilidades**, no aprueba por sí solo. Los pesos se recalibran cuando haya curvas de retención.

---

## E. Las 5 mejoras que haría primero
1. **Captura sin pérdida:** cada pedido de Tao se anota en el registro en el mismo turno. Y se completa el registro con las sesiones anteriores (tandas pendientes).
2. **Revisión automática ampliada:** choques entre todos los elementos, hoja de poses, repetición de espacios, insertos y pantallas, y ritmo. Los errores repetidos dejan de depender de que yo me acuerde.
3. **Guion visual + puntaje** antes de construir (puerta de aprobación).
4. **Piloto de micro-escenas** con láminas + biblioteca paramétrica.
5. **Ciclo de rendimiento** con la curva de retención alineada al registro de planos.

## Próximas tandas de auditoría
1. Chat principal, turnos 1–1685, en bloques de ~150 turnos. Solo extraigo los mensajes de Tao, porque sus pedidos son la fuente.
2. Documentos pendientes de la tabla de fuentes.
3. Otros chats del proyecto, por búsqueda de temas.

Cada tanda agrega filas aquí, al registro (11) y rearma `MAESTRO.md`.
