# 20 · MOTOR DE INTELIGENCIA CREATIVA: arquitectura revisada (propuesta para revisión)

> **Encargo de Tao (24-nov, 00:50):** lo más importante del Estudio no es descubrir tendencias ni medir: es ser extraordinariamente bueno en **inteligencia creativa**. El motor que estudia, extrae, guarda, aplica y aprende pasa a ser el **núcleo**; descubrimiento, análisis y generación lo usan y lo alimentan.
> **Estado:** propuesta. **No modifiqué código.** Reemplaza el orden de prioridades del doc 19; la interfaz de tres áreas se mantiene.
> **Cómo se hizo:** leí en profundidad cómo guarda y usa el conocimiento la aplicación actual (esquemas de las tablas, los prompts de análisis y el punto exacto donde el conocimiento entra a la generación) e investigué cómo se extrae y se transfiere conocimiento de forma rigurosa.

---

## 0. La idea en una página
```
                         ┌───────────────────────────────┐
   Videos de referencia ─►│                               │◄─ Investigación externa
   (éxitos Y normales)    │      EL CEREBRO CREATIVO      │   (psicología, narrativa, cine)
                          │                               │
   Nuestros videos +     ─►│  Casos → Elementos → Patrones │
   retención + decisiones │        ↘ Mecanismos ↙         │
                          │   Evidencia a favor y en contra│
                          └──────┬───────────┬────────────┘
                                 │           │
                    ESTUDIAR ◄───┘           └───► APLICAR
                    COMPARAR                       (generación)
                         ▲                             │
                         └────────── APRENDER ◄────────┘
                              (resultado × decisión)
```
- **Un solo cerebro**, con cuatro procesos: **estudiar** un video, **comparar** varios, **aplicar** al crear y **aprender** del resultado.
- **Descubrimiento** deja de ser un fin: sirve para encontrar **qué estudiar** y **qué temas** tienen historia.
- **Análisis** deja de ser un informe de métricas: es el proceso de **aprender**.
- **Generación** deja de recibir un volcado de reglas: **consulta** al cerebro según el video que está haciendo.

---

## 1. Lo que ya existe, y lo que falta de verdad
### 1.1 El embrión es más serio de lo que dije en el doc 19
| Pieza | Qué hace hoy |
|---|---|
| `biblioteca.py` | Estudia un Short con hojas de fotogramas, mediciones por código y transcripción. Produce una bitácora segundo a segundo (qué se ve, qué se escucha, edición, **función** de cada tramo y por qué retiene) y **ya distingue "medido", "observado" e "hipótesis"** |
| Tabla `arsenal` | Piezas por área, con cómo usarla, por qué, **condición** (cuándo funciona y cuándo falla), origen, ejemplos, evidencia a favor y **en contra**, relaciones entre piezas (funciona con, falla con) y resultado propio (nos funcionó o no) |
| Operaciones del arsenal | Nueva, refuerzo, matiz, **contradice**, relación, archivar. Lo aprendido en otro nicho se marca aparte: enseña el mecanismo, pero **no prueba** que funcione en el nicho del canal |
| `arsenal_usos` | Une cada guion con las piezas que usó, el video y su resultado |
| `patrones.py` | Compara mediciones de virales contra un **grupo de control** (Shorts normales de los mismos canales) |
| `laboratorio.py` | Experimentos con 6 réplicas o más por variante y prueba de permutación |
| `reglas.py` + `conocimiento_log` | Cada cambio de una regla queda con su antes, su después, su motivo y sus fuentes |
| `revisar.py` + `director.py` | Guardan lo que se predijo de un guion y lo comparan con lo que pasó |
| `metricas_plus.py` | Curva de retención por video |

**Conclusión:** no hay que inventar el cerebro. Hay que **completarlo, unificarlo y ponerlo en el centro**.

### 1.2 Las ocho brechas
| # | Brecha | Evidencia (lectura del código) | Por qué importa |
|---|---|---|---|
| 1 | **El largo no se estudia como narración.** El prompt para videos largos los trata como fuente de datos e ideas para hacer Shorts | `PROMPT_LARGO` | El foco principal no tiene proceso de estudio |
| 2 | **La evidencia de una pieza es un contador de ejemplos virales.** El grupo de control existe solo para mediciones numéricas, no para las piezas | Columna `evidencia`; `patrones.py` | Contar apariciones en éxitos no dice si la pieza también está en los fracasos (factor F3) |
| 3 | **El mecanismo es una lista cerrada de 7 "palancas"** más una frase escrita por Claude | Columna `palanca` | No distingue mecanismo con respaldo de etiqueta de marketing, ni enlaza con la investigación |
| 4 | **El resultado propio es binario y global:** funcionó o no, por vistas a 24 h | `nos_funciono`, `no_funciono` | No dice **en qué momento** del video estaba la pieza ni qué pasó con la retención ahí. Y mide popularidad |
| 5 | **Al pasar de la ficha a la pieza se pierde el tipo de afirmación.** La ficha separa medido, observado e hipótesis; la pieza guarda un solo "por qué" | Esquema de `arsenal` | Una interpretación termina leyéndose como un hecho |
| 6 | **Faltan tipos de conocimiento y campos.** No hay escenas, transiciones, técnicas de tensión, patrones de curiosidad y sorpresa, ni estrategias de apertura y cierre narrativos. No hay función narrativa, variaciones ni contextos de transferencia | Áreas del arsenal | Es la biblioteca que pides en el punto 2 |
| 7 | **La generación recibe un volcado, no una consulta.** Se anteponen al prompt archivos de texto **cortados por cantidad de caracteres** (7.000 de fórmulas, 9.000 de ganchos, 7.000 de arsenal) | `lote.py`, líneas 261–276 | Lo que entra depende de dónde cae el corte, no del tema ni de la historia. Empuja las mismas fórmulas a todos los videos |
| 8 | **El conocimiento está en paralelo** en `formulas`, `arsenal`, `reglas`, archivos de texto y los docs 00–19 | Inspección | Nada de lo investigado esta noche llega a la generación |

---

## 2. Los factores implicados: qué dice la investigación y qué obliga a diseñar
| # | Factor | Qué se sabe | Nivel | Consecuencia de diseño |
|---|---|---|---|---|
| F1 | **Transferir exige comparar** | Comparar dos casos a la vez produjo una ventaja marcada, frente a estudiarlos por separado, para abstraer el principio y usarlo en un problema nuevo. Cuanto más guiada la comparación, más transferencia (Gentner, Loewenstein y Thompson) | **A−** (experimentos replicados; en otro dominio) | Un video suelto no genera un principio. **La unidad de aprendizaje es la comparación**, no la ficha |
| F2 | **Se recuerda por parecido superficial** | Sin comparación, lo que viene a la mente al enfrentar un caso nuevo son casos que se parecen por fuera, no por estructura (misma línea de investigación) | **A−** | La biblioteca se indexa por **función y mecanismo**, no por formato ni por tema |
| F3 | **Mirar solo a los que ganaron engaña** | Quien aprende observando a los sobrevivientes submuestrea el fracaso y llega a creencias falsas: una práctica puede parecer efectiva sin tener relación con el resultado (Denrell) | **B+** (argumento formal; en organizaciones) | Cada patrón necesita saber **con qué frecuencia aparece en videos normales**. Los fracasos propios y ajenos se estudian igual que los éxitos |
| F4 | **La pericia solo crece donde hay regularidad y retroalimentación** | La intuición de un experto es fiable si el entorno es predecible y hubo oportunidad de aprender sus regularidades. La confianza subjetiva no indica acierto (Kahneman y Klein) | **B+** (síntesis de dos escuelas de investigación) | YouTube es un entorno ruidoso y de respuesta lenta. El "experto" se construye con **predicciones escritas, resultado y corrección**, no acumulando opiniones |
| F5 | **La IA mejora cada pieza y achata el conjunto** | Las historias escritas con ideas de un modelo se evaluaron mejor, pero quedaron más parecidas entre sí (Doshi y Hauser) | **B+** (un experimento; cuentos cortos) | La variedad no se va a dar sola. Hace falta un **mecanismo explícito de diversidad** al aplicar |
| F6 | **La codificación automática es desigual según qué se codifica** | El acuerdo de un modelo con codificadores humanos fue excelente en algunos códigos y débil en otros; subió cuando el modelo tenía que justificar; los libros de códigos hubo que reescribirlos y probarlos. Y acuerdo no es lo mismo que calidad | **B** | Libro de códigos propio, **justificación obligatoria**, fiabilidad medida código por código y un conjunto de calibración contigo |
| F7 | **Un modelo prefiere su propio texto** | Doc 18 | **B+** | Segundo juez en todo lo que yo escribo |
| F8 | **Un patrón es una hipótesis con grado de fe** | El formato clásico de patrón de diseño une contexto, problema (fuerzas en tensión), solución y enlaces a otros patrones. Sus autores marcaban su grado de fe en cada uno y advertían que todos seguían siendo hipótesis (Alexander) | **D** (método de oficio, muy probado en otros campos) | Cada entrada de la biblioteca lleva contexto, tensiones, límites, confianza y relaciones. Ninguna es una receta |
| F9 | **Reutilizar experiencia es un ciclo** | Recuperar casos parecidos, reutilizar, revisar la solución y retener lo aprendido (razonamiento basado en casos) | **B** (método establecido en IA) | Es el ciclo de **aplicar y aprender**: reemplaza al volcado de reglas |
| F10 | **Hay vocabulario preciso para descomponer una narración** | El código del enigma: plantear, prometer respuesta, demorar, despistar, responder a medias, suspender, revelar (Barthes). Suspenso, curiosidad y sorpresa según el orden (doc 18). Cuatro dimensiones medibles del enganche: comprensión, foco de atención, emoción y presencia (Busselle y Bilandzic) | **B** / **D** | Esto es el **libro de códigos**: en vez de "retiene porque es interesante", se anota qué movimiento del enigma ocurre y a qué dimensión del enganche apunta |
| F11 | **La retención propia tiene una resolución limitada** | La API de YouTube entrega la curva por fracción del video, con una medida relativa a videos de duración parecida. Según documentación de terceros, son hasta 100 puntos por video | **A** (oficial) / B (el detalle) | En un largo de 10 min, cada punto son unos 6 s. Se puede atribuir a un **tramo**, no a un plano. Sin vistas suficientes, la curva no sirve |
| F12 | **Los efectos son chicos y hay mucho ruido** | Doc 18 | **A−** | Ningún patrón es "la clave". Las conclusiones salen de acumular evidencia |

---

## 3. Arquitectura
### 3.1 El cerebro y sus cuatro procesos
| Proceso | Pregunta | Entra | Sale |
|---|---|---|---|
| **Estudiar** | ¿Qué hay dentro de este video y cómo está construido? | Un video (ajeno o propio) | Un **caso** con sus **elementos** |
| **Comparar** | ¿Qué se repite en los buenos y falta en los normales? ¿Se sostiene en otro nicho? | Varios casos | **Patrones** con su evidencia, o el descarte de un candidato |
| **Aplicar** | Para este tema, canal e historia, ¿qué conviene usar y cómo combinarlo? | Encargo del video | Propuestas justificadas + **registro de decisiones** |
| **Aprender** | ¿Qué pasó donde usamos cada cosa? | Decisiones + retención + pruebas | Evidencia propia, a favor o en contra; creencias corregidas |

### 3.2 Cómo se conectan los módulos al cerebro
| Módulo actual | Hoy | En la arquitectura revisada |
|---|---|---|
| Descubrimiento (`analisis.py`, `explorador.py`, `inteligencia.py`…) | Busca virales y nichos | Propone **qué estudiar** (pares de éxito y normal del mismo canal) y **qué temas** tienen material narrativo. Lo que encuentra entra como caso, no como lista |
| `biblioteca.py` | Ficha de Shorts | Proceso **Estudiar**, con un modo para largos |
| `arsenal.py`, `patrones.py`, `hooks.py`, `ganchos.py` | Cuatro bancos | **Una biblioteca**: procesos Comparar y la consulta de Aplicar |
| `lote.py`, `storyboard.py`, motor de largos | Reciben texto cortado | **Consultan** la biblioteca y registran qué usaron y dónde |
| `metricas_plus.py`, `fichas.py`, `laboratorio.py`, `reporte_semanal.py` | Informes | Proceso **Aprender** |
| `reglas.py` | Reglas con procedencia | Queda para lo que no es hipótesis: reglas éticas, de proceso y tus preferencias |
| `director.py`, `semaforo.py` | Proponen decisiones | Siguen igual; leen del cerebro |

**No hay aplicación nueva ni base nueva.** Se extiende `datos/cerebro.db`.

---

## 4. La biblioteca
### 4.1 Cinco tipos de objeto
| Objeto | Qué es | Ejemplo | ¿Existe? |
|---|---|---|---|
| **Caso** | Un video estudiado, con sus datos y su estructura | "Video X, canal Y, 12 min, 4× lo normal de su canal" | Sí: tabla `analisis` (falta el modo largo) |
| **Elemento** | Algo concreto que ocurre en un caso, en un tramo preciso | "0:00–0:12: abre con el resultado y calla la causa" | **Nuevo** |
| **Patrón** | Lo que tienen en común varios elementos; la entrada reutilizable | "Desenlace primero" | Parcial: `arsenal` |
| **Mecanismo** | El principio psicológico o narrativo que podría explicar el efecto, con su evidencia externa | "Hueco de información" (doc 18, G1) | **Nuevo** (hoy es una etiqueta) |
| **Evidencia** | Cada dato a favor o en contra de un patrón, con su tipo | "Presente en 5 de 6 éxitos y en 4 de 6 normales" | Parcial: contadores |

**Por qué separar elemento de patrón:** el elemento es una **observación** (está en el video, se puede señalar). El patrón es una **abstracción nuestra**. Si se mezclan, se pierde la diferencia entre lo visto y lo interpretado: es la brecha 5.

### 4.2 Los tipos de patrón
Los doce que pides, ordenados en cinco familias.

| Familia | Tipos |
|---|---|
| **Apertura y cierre** | Ganchos · estrategias de apertura · estrategias de cierre |
| **Estructura** | Estructuras de historia · fórmulas narrativas |
| **Tensión y curiosidad** | Técnicas de retención · patrones de curiosidad y sorpresa · construcción de tensión |
| **Imagen** | Tipos de escena · recursos visuales · transiciones |
| **Sonido y montaje** | Recursos audiovisuales (ritmo, silencio, música, efectos) |
| *(aparte)* | **Mecanismos psicológicos**: no son patrones, son lo que los explica |

### 4.3 La ficha de un patrón
| Campo | Qué contiene | Ya existe en `arsenal` |
|---|---|---|
| Nombre y tipo | — | Sí (`nombre`, `area`) |
| **Función narrativa** | Qué trabajo hace en la historia: abrir una pregunta, demorar, dar un respiro, pagar… | **No** |
| Contexto | Dónde aparece: formato, momento del video, tipo de tema | Parcial (`tema`, `idioma`) |
| **Tensiones** | Qué fuerzas equilibra (por ejemplo, guardar contra parecer truco) | **No** |
| Cómo se construye | Descripción concreta, sin plantilla de frases | Sí (`pieza`, `como_usar`) |
| **Mecanismos probables** | Enlaces a mecanismos, cada uno con su nivel de evidencia | No (hoy: `palanca`) |
| Ejemplos | Elementos reales, **incluidos casos donde está y el video no destacó** | Parcial (`ejemplos`) |
| **Variaciones** | Formas distintas del mismo patrón | **No** |
| Límites | Cuándo falla y qué debe ser verdad | Sí (`condicion`) |
| Combinaciones | Funciona con, choca con | Sí (`relaciones`) |
| **Evidencia externa** | Nivel A–E y fuente | No |
| **Evidencia observada** | En cuántos éxitos y en cuántos normales aparece; en cuántos nichos | Parcial (`evidencia`, `en_contra`) |
| **Evidencia propia** | Usos, y qué pasó **en el tramo donde se usó** | Parcial (`usos`, `nos_funciono`) |
| Confianza y estado | Idea · observado · con control · probado en lo propio · principio provisional · debilitado | Parcial (`estado`) |
| **Alcance** | Universal · formato · nicho · canal | Parcial (`temas_ok`) |

### 4.4 Tipos de afirmación (se guardan por separado)
| Tipo | Ejemplo | Quién puede escribirla |
|---|---|---|
| **Medido** | "El primer corte llega a los 6,3 s" | El código |
| **Observado** | "En el primer cuadro hay un cheque firmándose" | Quien mira el video; se puede comprobar |
| **Interpretado** | "El cheque funciona como promesa de una cifra" | Análisis; lleva justificación |
| **Hipótesis** | "Abrir con el objeto sostiene los primeros 30 s" | Comparación; lleva cómo se refutaría |
| **Principio respaldado** | "Un hueco específico sube el clic" | Solo con evidencia externa A o B, o con prueba propia repetida |

### 4.5 Una ficha de ejemplo, llenada con honestidad
```
PATRÓN        Desenlace primero
Tipo          Estructura · estrategia de apertura
Función       Cambia la pregunta de "¿qué pasó?" a "¿cómo fue posible?"
Contexto      Largos con un resultado llamativo y un camino poco obvio
Tensiones     Entregar el dato (confianza) contra quedarse sin pregunta
Construcción  Se muestra el resultado en los primeros segundos; se calla
              la causa o el camino; el resto del video lo reconstruye
Mecanismos    Estructura de curiosidad (doc 18, G7) · nivel B+
Ejemplos      Ninguno estudiado todavía con este método
Variaciones   Resultado completo · resultado sin la cifra · resultado
              en imagen y sin palabras
Límites       Falla si el camino es obvio una vez conocido el final
Combina con   (hipótesis) línea de tiempo maestra
Choca con     (hipótesis) cifra tapada
Evidencia     Externa: B+ (experimentos de lectura)
              Observada: sin datos    Propia: sin datos
              Nota: contradice nuestra costumbre de no revelar; esa
              costumbre está sin probar (doc 18, G14)
Estado        Idea
Alcance       Por determinar
```
Así se ve una entrada el primer día: mucha estructura y casi ninguna evidencia propia. Lo valioso es que **dice exactamente qué le falta**.

---

## 5. Proceso 1: estudiar un video
| Paso | Qué se hace | Detalle |
|---|---|---|
| 1. Elegir con control | Nunca un éxito solo: entra con un video **normal del mismo canal**, de duración y antigüedad parecidas | Es lo que hice a mano con los 16 títulos del doc 18. Responde a F3 |
| 2. Capturar | Transcripción con tiempos, hojas de fotogramas, cortes y mediciones | `laboratorio_faceless.py` y `biblioteca.py` ya lo hacen |
| 3. Segmentar por eventos | El largo se parte donde cambia el lugar, el tiempo, el objetivo o lo que creíamos; no cada N segundos | Doc 18 (V5) |
| 4. Codificar | Cada tramo se anota con el libro de códigos (abajo), **con justificación** | F6, F10 |
| 5. Extraer elementos | Lo que parece estar haciendo un trabajo concreto se guarda como elemento, con su tramo | — |
| 6. Las ocho preguntas | Por cada elemento: qué es · cómo está construido · qué mecanismo podría explicarlo · qué función cumple · por qué podría sostener la atención · dónde más serviría · qué variaciones admite · qué límites tiene | Son las de tu punto 1. Las dos primeras son **observación**; las demás, **interpretación o hipótesis**, y se guardan como tales |
| 7. Control de calidad | Una segunda pasada independiente sobre una muestra; lo que no coincide se marca como dudoso | F6 |

### El libro de códigos (versión inicial, a calibrar contigo)
| Dimensión | Códigos |
|---|---|
| Función del tramo | Abrir · situar · avanzar · complicar · girar · respirar · pagar · reflexionar · cerrar |
| Movimiento del enigma | Plantear · prometer respuesta · demorar · despistar · responder a medias · suspender · revelar |
| Manejo de la información | El público sabe menos, igual o más que el protagonista |
| Dimensión del enganche | Comprensión · atención · emoción · presencia |
| Imagen | Protagonista del cuadro · tipo de escena · relación con lo que se dice (muestra, anticipa, contradice, adorna) |
| Edición | Cambio de evento · cambio de plano dentro del evento · movimiento con función |
| Sonido | Voz sola · música · efecto con función · silencio |

**Calibración:** tú y yo codificamos por separado 2 o 3 videos. Donde no coincidimos, el código está mal definido y se reescribe. Los códigos con poco acuerdo se marcan como **poco fiables** y no alimentan patrones.

---

## 6. Proceso 2: comparar y abstraer
### 6.1 Tres comparaciones
| Comparación | Pregunta | Qué descarta |
|---|---|---|
| **Éxito contra normal, mismo canal** | ¿Este elemento está en el bueno y falta en el normal? | Lo que el canal hace siempre |
| **Varios éxitos entre sí** | ¿Qué tienen en común por estructura, aunque por fuera no se parezcan? | Lo que es propio de un solo video |
| **Entre nichos** | ¿El patrón aparece con otro tema y otro formato? | Lo que solo vale en un nicho |

### 6.2 La tabla que evita el autoengaño
| | Está en videos destacados | Está en videos normales |
|---|---|---|
| **Patrón presente** | a | b |
| **Patrón ausente** | c | d |

Un patrón solo es candidato si aparece **claramente más** en los destacados (a frente a b). Hoy el arsenal solo cuenta "a".

### 6.3 Qué hace transferible a un patrón
1. Se puede describir **sin nombrar el tema** del video.
2. Tiene una **función** identificable.
3. Hay al menos un **mecanismo** con respaldo que lo explicaría.
4. Aparece en **más de un canal**, idealmente en más de un nicho.
5. Se conocen **sus límites**: al menos un caso donde está y no funcionó.

### 6.4 La escalera de un patrón
| Escalón | Requisito |
|---|---|
| Idea | Viene de la investigación o de un solo caso |
| Observado | Elementos en varios casos, comparados entre sí |
| Con control | Aparece más en destacados que en normales, en más de un canal |
| Probado en lo propio | Lo usamos, con predicción previa, y el tramo respondió como se esperaba, más de una vez |
| Principio provisional | Lo anterior, repetido en otro canal o tema, sin resultados en contra |
| Debilitado | Resultados en contra. No se borra: se anota por qué |

**Nada sube por aparecer en un video viral.**

---

## 7. Proceso 3: aplicar al generar
### 7.1 De volcado a consulta
| Hoy | Propuesta |
|---|---|
| Se pegan al prompt miles de caracteres de fórmulas, ganchos y arsenal, cortados por tamaño | Se arma un **encargo** del video y se **consulta** la biblioteca con él |

### 7.2 El ciclo
| Paso | Qué pasa |
|---|---|
| 1. Encargo | Tema, canal, formato, hechos, pregunta mayor, y qué sabe y qué espera la audiencia (doc 18) |
| 2. Recuperar | Patrones por **función necesaria** (abrir, sostener la mitad, pagar…) y por **contexto**. No por parecido de tema (F2) |
| 3. Proponer | Dos o tres **combinaciones distintas**, cada una con su justificación: qué patrón, para qué, por qué aquí y qué riesgo tiene |
| 4. Revisar | Compatibilidades (funciona con, choca con), límites, y diversidad (7.3) |
| 5. Decidir | Eliges tú en la puerta de empaque, como hoy |
| 6. Registrar | Qué patrón se usó, **en qué tramo**, y qué se predice que pase |

### 7.3 Contra la uniformidad (F5)
- **Huella:** ningún video repite la misma combinación de apertura, estructura y cierre que los últimos del canal.
- **Cuota de exploración:** en cada video, al menos un patrón viene de los escalones bajos de la escalera. Sin eso, la biblioteca nunca prueba nada nuevo y se queda con lo primero que funcionó.
- **Uso reciente:** un patrón muy usado en el canal baja de prioridad.
- **Rechazo motivado:** el sistema también dice qué patrón **no** usa y por qué.

### 7.4 Criterio, no fórmula
El sistema no elige "el patrón con más puntos". Razona desde la historia: qué necesita este video en cada tramo y qué patrón cumple esa función en este contexto. Los patrones son vocabulario; la frase la arma el video.

---

## 8. Proceso 4: aprender de lo nuestro
### 8.1 El cruce
```
Registro de decisiones     Registro de planos        Curva de retención
(patrón P en 0:00–0:25) +  (qué había en pantalla) + (hasta 100 puntos)
                    └──────────────┬──────────────┘
          ¿Cómo se comportó la curva en ese tramo,
          frente a lo típico del canal en esa misma posición?
```
| Qué se aprende | Con qué dato |
|---|---|
| Aperturas y ganchos | % que sigue a los 30 s frente a lo típico; títulos por prueba A/B |
| Estructura | Forma de la curva completa frente a lo típico |
| Escenas, recursos, transiciones | Pendiente local de la curva en el tramo, **descontando la caída normal de esa posición** |
| Momentos de interés | Picos (se vuelve a mirar) |
| Fracasos | Las mayores caídas, con lo que había en pantalla y en el guion |

### 8.2 Los fracasos se estudian a propósito
- Todo video que queda **por debajo** de lo típico del canal recibe el mismo estudio que un éxito.
- La pregunta no es "qué salió mal" en general: es **qué predijimos y no pasó**.
- Un resultado en contra se anota en el patrón. Si se repite, el patrón baja un escalón.

### 8.3 Cuándo cambia una creencia
| Situación | Qué pasa |
|---|---|
| El resultado coincide con la predicción | Suma evidencia propia. No sube de escalón por una sola vez |
| El resultado contradice la predicción | Se anota; se busca otra explicación (tema, fecha, miniatura) antes de culpar al patrón |
| Se repite la contradicción | El patrón se debilita, y se corrige su ficha (límites, contexto) |
| No hay vistas suficientes | "Sin datos". No cambia nada |

### 8.4 Lo que este proceso no puede hacer
- No puede atribuir un efecto a un plano: la resolución es de varios segundos (F11).
- No separa del todo el patrón del tema.
- Con pocas vistas, no concluye.
- Nunca sabrá la retención de los videos ajenos.

---

## 9. Qué se toca de lo que existe (cuando lo apruebes)
| Pieza | Cambio | Tipo |
|---|---|---|
| Tabla `arsenal` | Columnas nuevas: función, tensiones, variaciones, alcance, escalón, nivel externo, conteo en normales | Aditivo |
| Tabla `elementos` | Nueva: caso, tramo, descripción, tipo de afirmación, códigos, justificación | Nueva |
| Tabla `mecanismos` | Nueva: nombre, qué dice la investigación, nivel, fuente, límites. Se carga con el doc 18 | Nueva |
| Tabla `evidencia` | Nueva: patrón, tipo (externa, observada, propia), a favor o en contra, fuente, fecha | Nueva |
| `arsenal_usos` | Se agregan tramo y predicción | Aditivo |
| `biblioteca.py` | Modo largo: reemplaza el prompt que solo saca ideas para Shorts | Extensión |
| `patrones.py`, `hooks.py`, `ganchos.py` | Se integran como procesos de Comparar sobre la misma biblioteca | Unificación, sin borrar |
| `lote.py`, `storyboard.py`, motor de largos | Consulta a la biblioteca en vez de archivos cortados | Cambio acotado |
| `metricas_plus.py` | Cruce con decisiones y planos | Extensión |
| `reglas.py`, `laboratorio.py`, `conocimiento_log` | Sin cambios | — |

---

## 10. Cómo cambia el plan del doc 19
**Se mantiene:** la interfaz de tres áreas, el botón único, la regla de silencio y traer el motor de largos al Mac.
**Cambia:** el orden. Primero el cerebro; la interfaz, al final y liviana.

| # | Etapa | Por qué en este orden | Esfuerzo |
|---|---|---|---|
| 0 | Respaldo | — | 15 min |
| 1 | Traer el motor de largos al Mac | Sigue siendo el mayor riesgo | 1,5–2 h |
| 2 | **Modelo de la biblioteca:** tablas y columnas; carga de los mecanismos del doc 18; migración del arsenal actual, marcando cada pieza con su escalón real | Sin esto, nada de lo demás tiene dónde vivir | 2–3 h |
| 3 | **Estudiar largos:** libro de códigos, modo largo y calibración contigo con 2–3 videos | Es la brecha 1 y habilita la ronda 2 de investigación | 3 h + tu tiempo de calibración |
| 4 | **Primera tanda de estudio:** 8–10 pares (éxito y normal) de nichos distintos | Llena la biblioteca con casos reales | 3–4 h de proceso, por tramos |
| 5 | **Comparar:** tabla de presencia, escalera y fichas de patrón | Convierte casos en conocimiento | 2 h |
| 6 | **Aplicar:** consulta en la generación, diversidad y registro de decisiones | Es la brecha 7 | 3 h |
| 7 | **Aprender:** cruce de decisiones, planos y retención; estudio de fracasos | Necesita videos publicados con vistas | 2–3 h |
| 8 | Botón único de análisis y las tres áreas | La interfaz muestra lo que el cerebro ya sabe hacer | 3–4 h |

**Total: 20–25 h, en 8–10 sesiones.** Son más que en el doc 19 porque la profundidad está en las etapas 2 a 7.
**Sin depender del código:** subir Pixar con su prueba A/B, y la calibración del libro de códigos, que se puede hacer en papel.

---

## 11. Cómo sabremos si el cerebro mejora
| Indicador | Qué mide |
|---|---|
| Acuerdo contigo en la calibración, código por código | Si lo que extrae es fiable |
| Acierto de las predicciones (predicho contra ocurrido) | Si entiende, o solo describe |
| Patrones por escalón | Cuánto es idea y cuánto está probado |
| Creencias corregidas | Si aprende de los errores, o solo acumula |
| Variedad de las combinaciones usadas por canal | Si evita la uniformidad |
| Patrones con casos en contra anotados | Si conoce sus límites |

Un cerebro con muchas entradas y pocas correcciones no está aprendiendo.

---

## 12. Límites que conviene aceptar desde ya
1. **Los mecanismos son explicaciones probables, no causas demostradas.**
2. **Lo ajeno se mide por vistas relativas;** su retención no se conocerá nunca.
3. **La extracción la hace un modelo:** será desigual según el código. Por eso la calibración y la justificación.
4. **Estudiar cuesta:** tiempo de Claude, y el Mac trabajando por tramos.
5. **El experto tarda:** al principio, casi toda la biblioteca estará en el escalón "idea".
6. **No vi todavía ningún video de referencia.** La etapa 4 es la primera vez que este método se prueba de verdad; puede obligar a corregir el libro de códigos y esta arquitectura.

---

## 13. Decisiones que necesito de ti
1. ¿Apruebas esta arquitectura como reemplazo del orden del doc 19?
2. **Calibración:** ¿puedes codificar conmigo 2–3 videos (unos 30–40 min en total)? Es lo que más sube la calidad de todo lo demás.
3. **Primera tanda:** ¿qué 8–10 canales de referencia quieres estudiar? Propongo partir de los 4 del doc 18 y sumar historia, investigación, tecnología y educación animada.
4. **Cuota de exploración:** ¿aceptas que cada video pruebe a propósito al menos un patrón poco probado?
5. Siguen abiertas las del doc 19: canales fuera de la lista, análisis diario, Reddit, Google Trends y la consola del Mac.

---

## Fuentes de este documento
- Gentner, Loewenstein y Thompson (2003), comparación y transferencia: https://www.kellogg.northwestern.edu/academics-research/research/detail/2003/learning-and-transfer-a-general-role-for-analogical-encoding
- Denrell (2003), submuestreo del fracaso: https://www.gsb.stanford.edu/faculty-research/publications/vicarious-learning-undersampling-failure-myths-management
- Kahneman y Klein (2009), condiciones de la pericia: https://pubmed.ncbi.nlm.nih.gov/19739881/
- Doshi y Hauser (2024), creatividad individual y diversidad colectiva: https://pubmed.ncbi.nlm.nih.gov/38996021/
- Aamodt y Plaza (1994), razonamiento basado en casos: https://www.cs.auckland.ac.nz/~ian/CBR/AICom.pdf
- Alexander, *A Pattern Language*: https://en.wikipedia.org/wiki/A_Pattern_Language · https://en.wikipedia.org/wiki/Pattern_language
- Barthes, código hermenéutico: https://en.wikipedia.org/wiki/S/Z
- Busselle y Bilandzic (2009), enganche narrativo: https://opus.bibliothek.uni-augsburg.de/opus4/files/39512/39512.pdf
- Codificación cualitativa con modelos: https://arxiv.org/html/2401.15170v2 · https://arxiv.org/pdf/2607.28890
- API de YouTube Analytics, métricas: https://developers.google.com/youtube/analytics/metrics
- Lectura directa de `biblioteca.py`, `arsenal.py`, `patrones.py`, `laboratorio.py`, `reglas.py`, `procedencia.py`, `lote.py`, `storyboard.py`, `revisar.py`, `director.py`, `metricas_plus.py` y `fichas.py`.
- Docs 18 y 19 de esta carpeta.
