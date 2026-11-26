# 17 · SISTEMA UNIVERSAL DE GENERACIÓN DE VIDEOS (el cerebro creativo del estudio)

> ⚠️ **Estado (24-nov, 00:20):** este documento es un **catálogo de técnicas e hipótesis** (nivel D). Sus números y umbrales quedaron retirados como norma; ver doc 18, Parte 4.3.
> **Encargo de Tao (24-nov, 00:13):** convertir toda la investigación, las auditorías y el estándar en un sistema universal, que sirva para cualquier tema y cualquier canal futuro.
> **Qué es:** una **capa de decisiones** que se pone encima del estudio que ya existe. Decide qué contar, cómo abrir, en qué orden revelar, qué mostrar y cómo revisar.
> **Qué no es:** una aplicación nueva. El motor, el armado, el render, la voz y el Estudio **siguen igual**. Cambia lo que entra al motor y lo que se revisa antes de producir.
> **Alcance:** largos de 10–12 min. Los Shorts usan solo los módulos 1 y 2, con sus reglas propias (doc 16).
> **Etiquetas:** `[TAO]` pedido o aprobado por Tao · `[MED]` medido en nuestros videos · `[EXT]` investigación externa (fuentes al final) · `[OFICIO]` práctica profesional · `[HIP]` hipótesis sin probar.
> **Límite honesto:** los puntajes de este documento sirven para **detectar debilidades**. Ninguno está validado contra la retención de nuestros canales.

---

## 0. Arquitectura del sistema
### 0.1 Tres capas
| Capa | Qué contiene | Cambia cuando… | Dónde vive |
|---|---|---|---|
| **Núcleo universal** | Los 9 módulos de este documento: criterios, procedimientos y revisiones | Aprendemos algo que se repite en 2 canales o más | `estandar-produccion/` (MAESTRO) |
| **Ficha de canal** | Tema, audiencia, tono, límites editoriales, identidad visual y lo aprendido en ese canal | Se crea un canal o un dato de ese canal lo corrige | `canales/<canal>/ficha.json` (nuevo) |
| **Expediente del video** | Los 13 archivos que produce cada video, del tema a los resultados | En cada video | `<carpeta del video>/expediente/` (nuevo) |

**Regla de diseño:** el núcleo nunca nombra un tema ni un canal. Todo lo que depende del canal se lee de la ficha. Así, agregar un canal es **llenar una ficha**, no reescribir el método.

### 0.2 Los 9 módulos
| # | Módulo | Pregunta que responde | Entra | Sale |
|---|---|---|---|---|
| M1 | Inteligencia de contenido | ¿Qué hace interesante este tema y cuál es su mejor ángulo? | Tema + ficha de canal + hoja de hechos | `02_interes.json`, `03_angulo.md` |
| M2 | Motor de ganchos | ¿Cómo se abre? | Ángulo + activos del tema | `04_ganchos.json` |
| M3 | Motor narrativo | ¿En qué orden se cuenta en 10–12 min? | Ángulo + gancho + hechos | `06_arquitectura.json` |
| M4 | Arquitectura de retención | ¿Dónde se va a caer la atención, antes de producir? | Arquitectura + guion | `08_retencion.json` |
| M5 | Motor visual | ¿Qué se muestra y cómo? | Guion + ficha de canal | `09_plan_visual.json` |
| M6 | Adaptación a canal | ¿Cómo cambia todo lo anterior según el canal? | 5 datos del canal | `ficha.json` |
| M7 | Flujo de producción | ¿Qué se entrega en cada etapa? | Todo | Los 13 archivos del expediente |
| M8 | Control de calidad | ¿Qué está débil y cómo se arregla? | Expediente | `12_qc.json` |
| M9 | Aprendizaje continuo | ¿Qué aprendimos y dónde se guarda? | Expediente + datos de YouTube | `13_resultados.json` + ficha y núcleo actualizados |

### 0.3 Qué cambia en el estudio actual (resumen; detalle en la Parte 10)
| Componente que ya existe | Qué pasa con él |
|---|---|
| Motor (`escena_h.html`, `planos.js`), render, voz, `rearmar_largo.sh` | **Se mantiene.** |
| `b.py` de cada video | **Se mantiene.** Pasa a escribirse a partir de `09_plan_visual.json`, no desde cero |
| `planos_tiempo.py` | **Mejora:** lee el ritmo por acto y el banco del canal desde la ficha |
| `revisar_largo.py`, `revisar_insertos.py`, `hoja_planos.py` | **Mejoran:** suman los detectores del M8 |
| `banco-angulos-virales`, `hooks-retencion`, `mdm-tops` | **Se integran** como material del M1 y el M2 |
| `fichas.py`, `reporte_semanal.py`, datos en Supabase | **Mejoran:** alimentan el M9 (pendiente tu OK) |
| Estudio (entrega y publicación) | **Se mantiene.** |
| **Nuevo:** fichas de canal, plantillas del expediente, radiografía del guion, registro de aprendizaje | Archivos de datos y revisiones. No tocan el motor |

---

## M1 · Inteligencia de contenido
**Objetivo:** recibir cualquier tema y decidir si vale un video, cuál es su mejor ángulo y en qué orden se revela.

### 1.1 Principios (qué hace interesante a algo)
| Principio | Qué dice | Qué implica |
|---|---|---|
| **Lo interesante contradice una creencia** | Una idea interesa cuando niega algo que su público da por hecho. Si lo confirma, es "obvio". Si no toca nada que crea, es "irrelevante". Si niega algo demasiado arraigado sin respaldo, es "absurdo" `[EXT]` (Davis) | El primer paso es escribir **qué cree el público**, no qué sabemos nosotros |
| **Interés = novedad + sentir que lo puedo entender** | El interés aparece con dos evaluaciones a la vez: esto es nuevo o complejo, y soy capaz de entenderlo `[EXT]` (Silvia) | Lo nuevo sin un ancla conocida no interesa: confunde |
| **La curiosidad necesita saber algo** | La curiosidad nace de un hueco entre lo que sé y lo que quiero saber, y es más alta cuando la persona sabe una parte, ni nada ni todo `[EXT]` (Loewenstein; Kang y colegas) | Antes de abrir un hueco hay que dar el contexto mínimo |
| **Romper el patrón y después repararlo** | La sorpresa aparece cuando falla lo que la persona esperaba, y solo vale si después se entiende por qué `[EXT, oficio]` (Heath) | Una sorpresa que no se explica es un truco |
| **Misterio, suspenso y sorpresa son tres cosas** | Si el público sabe que hay una bomba bajo la mesa, hay minutos de tensión; si no lo sabe, solo hay segundos de sorpresa `[EXT, oficio]` (Hitchcock) | Cada dato importante se decide: se guarda, se anticipa o se suelta de golpe |

### 1.2 Procedimiento (6 pasos)
**Paso 1 · Hoja de hechos.** Antes de opinar. Cada dato con 2 fuentes, nivel de certeza (confirmado / estimado / disputado) y si existe evidencia visual.

**Paso 2 · Mapa de creencias de la audiencia.** Tres listas, usando la audiencia de la ficha de canal:
- **Lo que ya sabe** (sirve de ancla).
- **Lo que cree** (es lo que se puede contradecir).
- **Lo que nunca se preguntó** (es el riesgo de "irrelevante").

**Paso 3 · Pasar el tema por las 12 lentes.** Adaptadas del índice de Davis `[EXT]`. Cada lente funciona en los dos sentidos.
| # | Lente | Forma |
|---|---|---|
| 1 | Organización | Lo que parece caos tiene un orden (o al revés) |
| 2 | Composición | Lo que parecen cosas distintas es una sola (o al revés) |
| 3 | Abstracción | Lo que parece cosa de una persona es de un sistema (o al revés) |
| 4 | Generalización | Lo que parece local es general (o al revés) |
| 5 | Estabilidad | Lo que parece fijo está cambiando (o al revés) |
| 6 | Función | Lo que parece no servir, sirve (o al revés) |
| 7 | Evaluación | Lo que parece malo fue bueno (o al revés) |
| 8 | Relación | Lo que parece no tener que ver, está conectado (o al revés) |
| 9 | Coexistencia | Lo que parece compatible no lo es (o al revés) |
| 10 | Covariación | Lo que parece subir junto, va en sentido contrario |
| 11 | Oposición | Lo que parece igual es opuesto (o al revés) |
| 12 | Causa | Lo que parece la causa es el efecto (o al revés) |

Se anotan las lentes que dan una afirmación **verdadera y respaldada por la hoja de hechos**. Cada una es un candidato a ángulo. Si ninguna da nada, el tema es informativo: o se busca otro enfoque, o se descarta.

**Paso 4 · Inventario de activos del tema.** Lo que el tema "tiene" para trabajar. Alimenta al M2 y al M5.
| Activo | Pregunta para detectarlo |
|---|---|
| A1 Cifra extrema | ¿Hay un número verificado que sorprende por sí solo? |
| A2 Creencia rota | ¿Qué cree la gente que no es así? |
| A3 Contradicción | ¿Hay dos hechos verdaderos que parecen no poder ser ciertos a la vez? |
| A4 Decisión con costo | ¿Alguien eligió algo y pagó por ello? |
| A5 Objeto | ¿Hay un objeto sin el cual la historia no se puede contar? |
| A6 Escala | ¿Hay algo cuyo tamaño solo se entiende comparándolo? |
| A7 Misterio | ¿Queda algo sin explicar? |
| A8 Riesgo | ¿Qué se podía perder, y quién? |
| A9 Vuelco en el tiempo | ¿El antes y el después son opuestos? |
| A10 Cercanía | ¿Le pasa al espectador, o tiene algo así en su casa? |

**Paso 5 · Puntuar los ángulos candidatos.**
| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| Creencia que contradice | Ninguna | Una creencia débil | Una creencia común y firme |
| Pregunta mayor | No cabe en una frase | Cabe, pero es vaga | Una frase específica que el espectador puede repetir |
| Lo que está en juego | Nada | Abstracto | Alguien concreto gana o pierde algo concreto |
| Agente | Solo datos | Una institución | Una persona (o animal, u objeto) que hace algo |
| Se puede mostrar | Solo ideas | Algunos objetos y lugares | Objeto protagonista, lugares y acción |
| Pago | Decepciona o no existe | Correcto | Cambia cómo se ve el tema |
| Dura 10 minutos | Se responde en 30 s | Necesita relleno | La respuesta exige recorrer varios pasos |

- **Puertas (si falla una, el ángulo se descarta):** todo es verdad y tiene 2 fuentes · el pago existe y está en los hechos · cumple los límites editoriales de la ficha.
- **Se elige** el de mayor puntaje. Con menos de 8 sobre 14, se busca otro ángulo o se baja el video a formato corto.
- **Contra la repetición:** si el ángulo usa la misma lente que los últimos 2 videos del canal, se prefiere el segundo mejor.

**Paso 6 · Plan de revelación.** Cada hecho de la hoja recibe un papel y un tratamiento.
| Papel | Qué hace | Dónde va |
|---|---|---|
| **Ancla** | Contexto que el público ya conoce o entiende en 5 s | Apertura y Acto 1 |
| **Semilla** | Abre una pregunta | Donde haga falta una pregunta nueva |
| **Escalón** | Hace avanzar la historia | Actos 1–3 |
| **Giro** | Cambia lo que creíamos | Mitad y Acto 3 |
| **Pago** | Responde la pregunta mayor | Acto 4. Nunca antes |
| **Eco** | Dice por qué importa | Después del pago |
| **Descarte** | Verdadero pero no sirve a la pregunta mayor | Fuera del video |

| Tratamiento | Cuándo se usa | Efecto |
|---|---|---|
| **Guardar** (misterio) | El pago y los giros | Curiosidad: quiero saber |
| **Anticipar** (suspenso) | Una amenaza, un plazo, un error que el protagonista no ve | Tensión: sé lo que viene y él no |
| **Soltar** (sorpresa) | Datos menores que rompen una expectativa | Sacudida breve; hay que explicarla enseguida |

### 1.3 Salida exacta: `02_interes.json` y `03_angulo.md`
```json
{
  "tema": "",
  "creencias": {"sabe": [], "cree": [], "nunca_pregunto": []},
  "lentes": [{"lente": 7, "afirmacion": "", "hechos": ["H3", "H9"]}],
  "activos": {"A1": "", "A3": "", "A5": ""},
  "angulos": [{"texto": "", "puntaje": 11, "puertas": "ok"}],
  "angulo_elegido": 0,
  "pregunta_mayor": "",
  "pago": "H12",
  "plan_revelacion": [{"hecho": "H1", "papel": "ancla", "trato": "dar"}]
}
```
`03_angulo.md` es media página: la creencia, el ángulo, la pregunta mayor, el pago y por qué ganó.

---

## M2 · Motor de ganchos
**Objetivo:** elegir cómo se abre el video con un método, no con plantillas.

### 2.1 El gancho de un largo tiene tres capas
| Capa | Tiempo | Trabajo | Falla típica |
|---|---|---|---|
| **Clic** | Título + miniatura | Abrir un hueco específico | Revela el pago, o promete algo que el video no da |
| **Confirmación** | 0–5 s | Mostrar que el video es lo que prometió el empaque: el tema en el primer cuadro | Empieza con contexto, fecha o presentación del canal |
| **Promesa** | 5–30 s | Decir qué está en juego y qué se va a entender, sin dar la respuesta | Da la respuesta (como Pixar v1 `[MED]`) o no plantea nada |

- YouTube recomienda que el título represente el video con exactitud, porque si no, la gente deja de mirar y eso afecta el alcance `[EXT, oficial]`.
- También indica que los primeros segundos son el momento en que el espectador decide quedarse o irse `[EXT, oficial]`.
- **Las tres capas se diseñan juntas** y se complementan: el título promete, la miniatura muestra el objeto, los primeros 5 s confirman y los 30 s abren la pregunta mayor.

### 2.2 Las 10 familias: por qué funcionan y cuándo
| # | Familia | Mecanismo | Úsala cuando… | Riesgo | Prueba de honestidad |
|---|---|---|---|---|---|
| 1 | **Informativo** | Claridad: el espectador sabe qué obtiene | El público ya busca el tema, o el título ya abrió el hueco | No deja nada por resolver | ¿El video entrega exactamente eso? |
| 2 | **Sorpresa** | Falla lo que el espectador esperaba | Hay una creencia rota (A2) | Dura segundos; sin un "cómo es posible" detrás, se agota | ¿El dato es literal, sin adjetivos nuestros? |
| 3 | **Contradicción** | Dos verdades que no calzan piden una explicación | Hay A3. Es la más útil en largos: resolverla exige recorrer la historia | Si una de las dos mitades es exagerada, cae todo | ¿Las dos mitades tienen 2 fuentes? |
| 4 | **Afirmación que suena imposible** | Niega algo muy arraigado; está al borde de lo "absurdo" | Hay un hecho extremo verificado **y** un ancla de credibilidad inmediata (fecha, fuente, objeto) | Incredulidad o sensación de engaño | ¿"Imposible" describe cómo se ve, no lo que es? ¿El video explica por qué pasó? |
| 5 | **Hueco de curiosidad** | Se señala algo y se guarda una pieza específica | El público ya conoce una parte del tema | Si es vago, no genera nada; si no se paga, traiciona | ¿El espectador podría decir qué le falta saber? |
| 6 | **Comparación inesperada** | Vuelve entendible una magnitud y sorprende por la pareja | Hay A6: cifras grandes o escalas abstractas | Comparación forzada o inexacta | ¿Las dos cantidades están en la misma unidad y verificadas? |
| 7 | **Lo que está en juego** | Suspenso: el público sabe lo que puede perderse y espera | Hay A4 o A8: una decisión, un plazo, un riesgo | Inflar lo que estaba en juego | ¿Lo que se podía perder está documentado? |
| 8 | **Narrativo** | Una acción en curso arrastra: se quiere ver cómo sigue | Hay un agente con una decisión | Lento si en 5 s no se ve qué está en juego | ¿La escena ocurrió, o está rotulada como recreación? |
| 9 | **Interrupción de patrón** | Lo que rompe la costumbre llama la atención | El tema está muy visto, o el canal viene abriendo siempre igual | Truco sin relación con el contenido | Una vez visto el video, ¿la apertura tiene sentido? |
| 10 | **Cifra específica** | Un número preciso es concreto y creíble | La cifra sorprende **y** se entiende sin ayuda | Una cifra sin referencia no dice nada; puede ser el pago | ¿Es la cifra exacta de la fuente? ¿No es el dato clave? |

### 2.3 El ejemplo de Tao, analizado
| | "GTA 6 sold an extraordinary amount in one day." | "What GTA 6 did in a single day seems impossible." |
|---|---|---|
| Familia | Informativo con adjetivo | Afirmación que suena imposible + hueco |
| Qué entrega | La categoría de la respuesta: vendió mucho | Solo señala: "lo que hizo" no dice qué fue |
| Quién juzga | Nosotros ("extraordinary") | El espectador: "imposible" lo invita a medirlo contra lo que cree |
| Qué queda abierto | Casi nada: falta el número | Dos preguntas: qué hizo, y cómo pudo pasar |
| Qué promete | Un dato | Una explicación ("seems" anuncia que hay una razón) |
| Debilidad | Cierra el hueco al abrirlo | Es vaga: necesita un ancla concreta al lado (el objeto, la fecha) o suena a truco |

**Lo que enseña el ejemplo:**
1. **Un adjetivo nuestro no es un gancho.** "Extraordinary" le pide al espectador que nos crea. La segunda frase le pide que **compare con lo que él esperaba**.
2. **Señalar sin nombrar abre el hueco.** Pero solo funciona si el espectador ya sabe algo (qué es GTA, qué es "un día de ventas").
3. **La segunda frase obliga al video a explicar.** Si el video solo da la cifra, la promesa queda rota. Por eso el gancho se elige **después** de saber qué paga el video.
4. **Hay una tercera vía, casi siempre mejor:** un ancla concreta + el hueco. Forma: *[hecho verificado y específico]. [Por qué eso no debería haber pasado].* Las cifras salen de la hoja de hechos; nunca se inventan ni se redondean hacia arriba.

### 2.4 Método de generación
1. **Tomar los activos** del M1 (A1–A10) y el nivel de conocimiento de la audiencia.
2. **Filtrar familias** con esta tabla:

| Situación | Familias que sirven | Familias que no |
|---|---|---|
| El público conoce bien el tema | 3, 2, 9, 5 | 1 |
| El público no sabe nada del tema | 7, 8, 6 (dan el ancla primero) | 5 (no hay hueco sin saber algo) |
| El dato clave es una cifra | 5, 3, 7. La cifra se guarda | 10 con esa cifra |
| Hay otra cifra fuerte que no es el pago | 10 + 6 | — |
| Hay protagonista y decisión | 8, 7 | 1 |
| Es un mecanismo ("cómo funciona") | 2, 3, 6 | 8 (salvo que haya un inventor o un caso) |
| Tema sensible (salud, dinero) | 1, 5, 6 | 4 y 7 exagerados |

3. **Generar al menos 6 conceptos de 4 familias distintas.** Dos conceptos cuentan como distintos solo si difieren en **2 o más** de: activo que usan, primera imagen, pieza que guardan, pregunta que abren, emoción.
4. **Cada concepto es una ficha,** no una frase:

```json
{"familia": 3, "activo": "A3",
 "primer_cuadro": "", "frase_0_5s": "", "texto_en_pantalla": "",
 "promesa_5_30s": "", "guarda": "", "pregunta_que_abre": "",
 "se_paga_en": "momento 14", "titulo_que_combina": "", "miniatura_que_combina": ""}
```

### 2.5 Método de selección
**Puertas (si falla una, el concepto se descarta):**
1. Es verdad literal, con 2 fuentes.
2. El video lo paga: apunta a un momento concreto de la arquitectura.
3. No revela el dato clave.
4. Se entiende en 5 s sin contexto.
5. La voz no hace una pregunta directa `[TAO]`.

**Puntaje (0–2 cada uno):**
| Criterio | Qué se mira |
|---|---|
| Especificidad | Nombres, objetos y hechos concretos, no adjetivos |
| Tamaño del hueco | El espectador puede decir con sus palabras qué quiere saber |
| Cercanía | Toca algo que la audiencia de la ficha conoce o le importa |
| Primer cuadro | El tema llena el cuadro desde el segundo 0 |
| Combina con el empaque | Título, miniatura y apertura se completan sin repetirse |
| Aguante | La pregunta que abre dura hasta el Acto 4 |

- **Desempate:** la familia que el canal no usó en sus últimos 3 videos.
- **Decide Tao** entre los 3 mejores, en la puerta de empaque.
- **Los otros 2 no se pierden:** sus títulos van a Test & Compare, que es nuestra única prueba causal.

---

## M3 · Motor narrativo
**Objetivo:** convertir el ángulo en una historia de 10–12 min que no se parezca a la anterior.

### 3.1 Elegir la arquitectura por las propiedades del tema
| Si el tema es sobre todo… | Arquitectura | Esqueleto |
|---|---|---|
| Una persona o empresa que decide algo | **Caso** | Mundo → complicación → escalada → pago (doc 15, 2.2) |
| Una verdad discutida, con evidencia | **Versiones enfrentadas** | Lo que se contó → testigos → evidencia → explicación → lo que no calza → veredicto (doc 15, 2.3) |
| Cómo o por qué funciona algo | **Explicación en capas** | Lo que se ve → la explicación común → por qué no alcanza → el mecanismo real → qué cambia saberlo |
| Un problema que alguien intenta resolver | **Intento y falla** | El problema → intento 1 falla → intento 2 falla por otra razón → la idea que lo resuelve → su costo |
| Un auge y una caída (o al revés) | **Arco** | La cima → cómo llegó → la grieta que nadie vio → la caída → qué queda |
| Dos cosas que se comparan | **Duelo** | Lo que parecen → asalto 1 → asalto 2 (se invierte) → lo que de verdad los separa |
| Varios casos o ítems | **Escalera con hilo** | Pregunta que cruza → ítems de menor a mayor sorpresa → un ítem rompe la regla → el último responde (doc 15, 2.4) |

- Si calzan dos, gana la que tenga **un agente que hace algo**.
- **No se usa la misma arquitectura en 3 videos seguidos** de un canal, salvo que el canal sea de un solo tipo por definición.

### 3.2 Las piezas que toda arquitectura necesita
| Pieza | Regla | Fuente |
|---|---|---|
| **Pregunta mayor** | Una sola, abierta antes del segundo 30 y cerrada en el último acto | `[OFICIO]` |
| **Conflicto** | Alguien o algo se opone: una persona, un límite físico, una creencia, el tiempo | `[OFICIO]` |
| **Anécdotas** | Tramos de acción donde una cosa lleva a otra | `[EXT]` Ira Glass |
| **Reflexiones** | Momentos breves que dicen por qué importa | `[EXT]` Ira Glass |
| **Uniones** | Entre momentos cabe "pero" o "por lo tanto" | `[OFICIO]` |
| **Libro de preguntas** | Una mayor y al menos una menor abiertas siempre | doc 15, 2.5 |

### 3.3 Escalada: cuatro maneras de subir
| Tipo | Cómo sube | Ejemplo de forma |
|---|---|---|
| **Lo que está en juego** | De poco a mucho | Un sueldo → la empresa → la industria |
| **Escala** | De uno a muchos | Una casa → una ciudad → un país |
| **Cercanía** | De lejos a "te pasa a ti" | Un laboratorio → tu cocina |
| **Certeza** | De rumor a prueba (o de certeza a duda) | Se dijo → se midió → se confirmó |

Cada video elige **1 o 2** y las anota. Si ningún acto sube en ninguna, el video es plano.

### 3.4 Giros: cinco tipos
| Tipo | Qué cambia |
|---|---|
| Inversión | Lo que parecía bueno era malo, o al revés |
| Causa oculta | La razón verdadera era otra |
| Protagonista equivocado | La historia era de otra persona u otra cosa |
| Costo | Lo logrado tuvo un precio que no se había contado |
| Evidencia nueva | Aparece un dato que obliga a reordenar lo anterior |

- **Mínimo:** un giro en la mitad. Un segundo giro en el Acto 3 si los hechos lo dan.
- **Un giro tiene que estar sembrado:** al verlo, el espectador puede mirar atrás y encontrar la pista. Si no, es un truco.
- **Nunca se fabrica un giro.** Si los hechos no lo tienen, se usa una escalada.

### 3.5 Finales: cinco tipos (se rotan)
| Tipo | Forma |
|---|---|
| Regreso | Vuelve la imagen del inicio, cambiada |
| Ironía | El resultado contradice la intención original |
| Pregunta que queda | Lo que sigue sin resolverse, dicho como afirmación |
| Lección | Qué decisión enseña (firma de MDM `[TAO]`) |
| Ventana | Lo mismo está pasando hoy en otra parte |

### 3.6 Huella del video (contra la repetición)
Cada video guarda su huella: `arquitectura · familia de gancho · tipos de escalada · tipos de giro · tipo de final`.
**Si la huella coincide en 4 de 5 con alguno de los últimos 3 videos del canal, se cambia al menos una pieza.** Es la versión narrativa de "la variación es la retención" `[TAO]`.

### 3.7 Salida exacta: `06_arquitectura.json`
```json
{
  "arquitectura": "intento_y_falla",
  "pregunta_mayor": "",
  "escalada": ["en_juego", "escala"],
  "momentos": [
    {"n": 1, "acto": "apertura", "min": "0:00", "que_pasa": "", "union": "",
     "papel": "semilla", "hechos": ["H1"], "abre": ["Q1"], "cierra": [], "emocion": "asombro"}
  ],
  "giros": [{"momento": 9, "tipo": "causa_oculta", "sembrado_en": 4}],
  "final": "regreso",
  "huella": "intento_y_falla·3·en_juego+escala·causa_oculta·regreso"
}
```

---

## M4 · Arquitectura de retención
**Objetivo:** encontrar los tramos débiles **en el papel**, antes de grabar la voz.
**Principio:** lo que sostiene la atención es que **pase algo nuevo en la historia**. Un corte no crea un evento nuevo `[EXT]` (Zacks), y no encontré ningún estudio confiable que relacione la frecuencia de cortes con la retención en YouTube. El ritmo de corte queda como hipótesis.

### 4.1 Radiografía del guion
El guion se parte en tramos de 20–40 s (uno por momento). Para cada tramo se llena una fila:

| Campo | Qué se anota | Señal de alarma |
|---|---|---|
| Función | Semilla, escalón, giro, pago, eco o respiro | 3 tramos seguidos con la misma función |
| Preguntas abiertas | Cuáles siguen abiertas al terminar el tramo | Ninguna menor abierta |
| Novedad | Qué hay de nuevo: hecho, lugar, personaje, tipo de imagen | Nada nuevo |
| Cambio | Qué cambió en la historia: lugar, tiempo, objetivo o creencia | Nada cambió en 2 tramos seguidos |
| Carga | Cuántos datos nuevos trae (cifras, nombres, fechas) | Más de 3 sin un respiro después |
| Emoción | Una palabra: asombro, tensión, alivio, humor, inquietud, ternura | 3 tramos seguidos con la misma |
| Tensión prevista | 0 a 3, a juicio del guionista | 2 tramos seguidos en 0–1 fuera del epílogo |
| Anticipación visual | Qué imagen se sembró y aún no se paga | Ninguna durante todo un acto |
| Unión con el siguiente | Pero / por lo tanto / y después | "Y después" |

### 4.2 Los 12 detectores de tramo débil
| # | Detector | Cómo se detecta | Cómo se arregla |
|---|---|---|---|
| 1 | **Valle sin pregunta** | Tramo sin ninguna pregunta menor abierta | Mover una semilla hacia atrás, o cerrar la pregunta anterior más tarde |
| 2 | **Tramo borrable** | Se quita y nada posterior deja de entenderse | Cortarlo, o darle un hecho que algo posterior necesite |
| 3 | **Más de lo mismo** | Su resumen es "otro ejemplo de lo anterior" | Fundirlo con el anterior, o invertirlo (el caso que contradice) |
| 4 | **Muro de datos** | Más de 3 datos nuevos sin respiro | Repartir, o convertir 2 en imagen sin voz |
| 5 | **Meseta** | 3 tramos con la misma emoción o la misma función | Insertar un contraste: respiro, humor seco, detalle humano |
| 6 | **Cadena floja** | Unión "y después" | Reordenar hasta que quepa "pero" o "por lo tanto"; si no cabe, sobra uno de los dos |
| 7 | **Pago temprano** | El dato clave, o algo que lo deja deducir, aparece antes del Acto 4 | Reemplazar por una referencia que lo señale sin decirlo |
| 8 | **Promesa huérfana** | Una pregunta abierta o una promesa del gancho no tiene cierre | Cerrarla o quitarla |
| 9 | **Giro sin siembra** | El giro no tiene pista previa | Agregar la pista 2–4 tramos antes |
| 10 | **Mitad hundida** | Entre el 40 y el 60 % no hay giro ni escalada | Mover ahí el giro principal |
| 11 | **Acto sin estreno** | Un acto no trae lugar, gráfico ni recurso nuevo | Guardar uno de los mejores recursos para ese acto |
| 12 | **Final que se desinfla** | Después del pago quedan más de 90 s, o cierra con un resumen | Recortar; terminar en imagen y puente |

### 4.3 Anticipación visual (sembrar y pagar con imágenes)
| Recurso | Cómo se hace |
|---|---|
| Objeto sembrado | Un objeto aparece en el fondo antes de que la voz lo nombre, y después pasa a ser protagonista |
| Casillero vacío | Un tablero, una ficha o un mapa con espacios sin llenar a la vista |
| Cifra tapada | El número existe en pantalla, pero cubierto |
| Puerta entreabierta | El plano termina justo antes de mostrar lo que hay |
| Reloj visible | Un plazo que avanza en pantalla (suspenso: el espectador sabe lo que viene) |

### 4.4 Salida exacta: `08_retencion.json`
La tabla de la radiografía, la lista de detectores que saltaron con su arreglo, y la **curva de tensión prevista** (un número por tramo). Se revisa de un vistazo: tiene que subir por actos, con respiros, y no tener dos valles seguidos.
**Regla:** el guion no pasa a voz con detectores 7, 8 o 9 activos.

---

## M5 · Motor visual
**Objetivo:** decidir qué se muestra y cómo, con criterio, y dejarlo listo para el motor de Canvas. El **cómo se dibuja** cada cosa está en el doc 15 (Partes 4–7).

### 5.1 Las cinco decisiones por momento
**1. ¿Qué tipo de contenido tiene la frase?** → eso decide la forma.
| La frase habla de… | Se muestra como… |
|---|---|
| Una acción | La acción, con las manos o el cuerpo que la hacen |
| Un objeto | El objeto en primer plano, con un detalle que lo ubique en su época |
| Un lugar | Plano de ubicación con 3 capas, y después un detalle |
| Una cantidad | Unidades repetidas, o comparación física |
| Una comparación | Las dos cosas en la misma escala |
| Un proceso | Diagrama que se arma por pasos |
| Una relación en el espacio | Mapa o vista desde arriba |
| Una relación en el tiempo | Línea de tiempo, o el mismo lugar en dos estados |
| Una evidencia | Documento, foto o pantalla, con la parte clave marcada |
| Una idea abstracta | Metáfora física (máximo 1–2 por video) |
| Una emoción | Cara o gesto en primer plano, con reacción antes de la acción |
| Un testimonio o una hipótesis | Recreación **rotulada** como tal |

**2. ¿Merece una visualización propia?**
| Sí, si… | No, si… |
|---|---|
| Responde o acerca a la pregunta mayor | Es un dato de paso |
| Es una cifra que solo se entiende comparada | La cifra se entiende sola |
| La relación es difícil de decir en palabras (espacio, proporción, simultaneidad) | Una frase la deja clara |
| Es un giro o el pago | — |

Meta orientativa: **6–10 visualizaciones propias** por video; el resto son planos de escena.

**3. ¿Qué entorno?**
- El lugar **real** donde ocurrió, si se conoce. Si no, el lugar que el público asocia al tema.
- El entorno aporta 2–3 objetos que cuentan algo sin texto.
- Si el lugar ya salió, vuelve en **otro estado**.

**4. ¿Qué encuadre comunica mejor?**
| Lo que hay que comunicar | Encuadre |
|---|---|
| Dónde estamos | General, con profundidad |
| Qué siente | Primer plano |
| Qué ve | Punto de vista |
| Qué hace | Manos, detalle |
| Relación entre dos | Plano de a dos, o sobre el hombro |
| Quién manda | Cámara baja para el fuerte, alta para el débil |
| Posiciones y recorridos | Desde arriba |
| Tamaño | Con una referencia humana al lado |
| Soledad o pequeñez | Sujeto chico en un cuadro grande (uso contado) |

**5. ¿Quién es el protagonista del cuadro?** Lo que nombra la frase. Si la frase nombra una taza, el cuadro es de la taza, no de alguien que habla de la taza `[TAO]`.

### 5.2 El objeto protagonista del video
Se elige **uno** con estos criterios:
1. Sin él, la historia no se puede contar.
2. Puede aparecer al menos 3 veces y **cambiar de estado**: se planta, se complica, paga.
3. Se reconoce en la miniatura.
4. No tiene marca ni forma protegida.

### 5.3 Cuándo usar cada recurso mayor
| Recurso | Úsalo cuando… | No lo uses cuando… |
|---|---|---|
| **Diagrama** | Hay un mecanismo con partes que se relacionan | Solo adorna una afirmación |
| **Mapa** | La distancia, la ruta o la ubicación explican algo | El lugar es solo un nombre |
| **Reconstrucción** | Importa quién estaba dónde y cuándo, y hay registro | No hay evidencia: sería inventar |
| **Simulación** | Hay un "qué pasa si" con reglas físicas o numéricas conocidas | Los parámetros serían supuestos nuestros |
| **Línea de tiempo** | El orden o la duración explican el resultado | Son solo fechas |
| **Recreación con personajes** | Hay una decisión o un conflicto entre personas | Sería "alguien de pie explicando" |

**Regla de verdad visual:** lo que no está documentado se muestra con otro tratamiento (silueta, línea punteada, rótulo), para que el espectador distinga lo sabido de lo supuesto.

### 5.4 Salida exacta: `09_plan_visual.json`
```json
{
  "objeto_protagonista": {"que": "", "estados": ["plantado", "complicado", "pago"]},
  "guion_de_color": [{"acto": 1, "fondo": "", "acento": "", "brillo": 0.6}],
  "momentos": [
    {"n": 1, "contenido": "objeto", "forma": "primer_plano_objeto",
     "visualizacion_propia": false, "lugar": "", "estado_lugar": "antes",
     "encuadre": "detalle", "protagonista": "", "movimientos": ["camara", "naturaleza"],
     "pieza": "banco:sello", "siembra": "", "rotulo": ""}
  ],
  "piezas_nuevas": [{"nombre": "", "parametros": [], "queda_en_banco": true}]
}
```
`pieza` apunta a una pieza del banco del canal o a una nueva. De aquí sale el `b.py`.

---

## M6 · Adaptación a canal
### 6.1 Qué es universal y qué es del canal
| Universal (núcleo) | Del canal (ficha) |
|---|---|
| Cómo se detecta lo interesante (M1) | Qué sabe y qué cree **esa** audiencia |
| Familias de gancho y su selección (M2) | Qué familias se permiten, y cuáles rindieron |
| Arquitecturas, escalada, giros y finales (M3) | Cuáles son habituales y cuáles se evitan |
| Radiografía y detectores (M4) | Umbrales (cuánta carga de datos aguanta el público) |
| Decisiones visuales (M5) | Colores, luz, tipografía, objeto y gráfico firma, banco de piezas |
| Reglas de verdad y control de calidad (M8) | Límites editoriales propios |
| Método de aprendizaje (M9) | Lo aprendido en ese canal |

### 6.2 La ficha de canal
Tú entregas **5 datos**: tema, audiencia, tono, límites editoriales e identidad visual. El resto se deriva y se va corrigiendo con datos.
```json
{
  "canal": "",
  "tema": {"territorio": "", "fuera_de_alcance": []},
  "audiencia": {"quien": "", "sabe": [], "cree": [], "le_importa": [],
                "nivel": "curioso_general", "idioma": "en"},
  "tono": {"voz": "", "palabras_por_min": 165, "humor": "seco",
           "trato": "de igual a igual", "vocabulario_max": "secundaria"},
  "limites": {"prohibido": ["politica"], "sensibles": [],
              "rotulos_obligatorios": [], "fuentes_minimas": 2},
  "identidad": {"idea": "", "colores": {}, "luz": "", "tipografia": "",
                "objeto_firma": "", "grafico_firma": "", "transicion_firma": "",
                "sonido_firma": "", "evitar": []},
  "narrativa": {"arquitecturas_habituales": [], "final_habitual": "",
                "ganchos_permitidos": [1,2,3,5,6,7,8,9,10], "ganchos_vetados": []},
  "banco_piezas": [],
  "ultimas_huellas": [],
  "aprendido": [{"fecha": "", "que": "", "estado": "hipotesis", "evidencia": ""}]
}
```

### 6.3 Qué se deriva de cada dato
| Dato | Qué ajusta |
|---|---|
| **Tema** | Qué tipos de activo son frecuentes → arquitecturas probables. Qué recursos visuales se necesitan primero en el banco |
| **Audiencia** | El mapa de creencias del M1. Cuánto contexto necesita la apertura. Cuánta carga de datos aguanta un tramo. Vocabulario |
| **Tono** | Voz, velocidad, humor, tipo de final, intensidad permitida en los ganchos |
| **Límites** | Puertas extra del M8. Familias de gancho vetadas. Rótulos obligatorios |
| **Identidad** | Colores, luz, objeto y gráfico firma, transición y sonido. Lo que se evita |

### 6.4 Dar de alta un canal nuevo
| Paso | Qué | Tiempo estimado |
|---|---|---|
| 1 | Llenar los 5 datos con Tao | 15 min |
| 2 | Derivar el resto de la ficha | 15 min |
| 3 | Probar el M1 con 3 temas del canal: ¿salen ángulos con 8 puntos o más? | 20 min |
| 4 | Definir colores y luz en el motor (se avisa antes) | 30–40 min |
| 5 | Banco mínimo: 8–10 piezas donde el tema es protagonista | ~1,5 h |
| 6 | Primer video con el flujo completo | ~3 h |

**Total: una tarde para tener un canal nuevo con su primer video,** con el método sin tocar.

### 6.5 Prueba de universalidad (cómo quedaría en áreas nuevas)
Solo la configuración; ningún dato de contenido.
| Canal hipotético | Activos frecuentes | Arquitecturas probables | Recursos visuales que más pesan | Límite editorial propio |
|---|---|---|---|---|
| **Ingeniería** | A6 escala, A8 riesgo, A5 objeto | Intento y falla · explicación en capas | Corte transversal, diagrama por pasos, simulación con reglas conocidas | No simplificar hasta volver falso; unidades correctas |
| **Historia** | A4 decisión, A9 vuelco, A7 misterio | Caso · arco · versiones enfrentadas | Mapa, línea de tiempo, lugar en dos estados | Separar hecho de interpretación; sin política actual |
| **Psicología** | A2 creencia rota, A10 cercanía | Explicación en capas · duelo | Metáfora física, repetición con etiquetas, experimento recreado | Informativo, con fuentes; sin diagnósticos ni consejos clínicos; decir el tamaño y los límites del estudio |
| **Economía** | A1 cifra, A3 contradicción | Arco · caso · intento y falla | Flujo de dinero, unidades repetidas, barra partida | Sin promesas de dinero ni recomendaciones de inversión |
| **Ciencia** | A2, A6, A7 | Explicación en capas · versiones enfrentadas | Diagrama, escala comparada, simulación | Distinguir consenso de hipótesis |
| **Tecnología** | A9, A4, A8 | Intento y falla · arco | Diagrama, objeto que evoluciona, línea de tiempo | Sin logos ni interfaces reales; cifras con fecha |

---

## M7 · Flujo completo de producción
**15 etapas, 3 aprobaciones de Tao.** Las demás etapas son trabajo interno con una salida fija. Las 3 puertas son las del doc 14.

| # | Etapa | Entra | Sale (exacto) | Componente | Puerta |
|---|---|---|---|---|---|
| 1 | Análisis del tema | Tema + ficha | `02_interes.json` (borrador: creencias, lentes, activos) | M1 | — |
| 2 | Investigación y verificación | Borrador | `01_hechos.json`: cada dato con 2 fuentes, certeza y evidencia visual | Búsqueda + regla de 2 fuentes | Automática: ningún dato sin 2 fuentes |
| 3 | Ángulo | Hechos + interés | `03_angulo.md` + ángulos puntuados + plan de revelación | M1 | — |
| 4 | Ganchos | Ángulo + activos | `04_ganchos.json`: 6 fichas o más, de 4 familias, puntuadas | M2 | — |
| 5 | Título y miniatura | Los 3 mejores ganchos | `05_empaque.json`: 3 combinaciones título + miniatura + promesa; dato clave embargado | `miniatura_largo.py`, `mdm-tops` | **Tao (1)** |
| 6 | Arquitectura | Gancho elegido + hechos | `06_arquitectura.json`: momentos, uniones, libro de preguntas, giros, final, huella | M3 | — |
| 7 | Guion | Arquitectura | `07_guion.json`: 1.700–1.900 palabras, por momento, en el tono de la ficha | Guion | — |
| 8 | Análisis de retención | Guion | `08_retencion.json`: radiografía, detectores, curva de tensión | M4 | Automática: sin detectores 7, 8 y 9 |
| 9 | Plan visual | Guion | `09_plan_visual.json`: objeto protagonista, guion de color, decisión por momento, piezas nuevas | M5 | — |
| 10 | Guion visual | Plan visual | Plano por plano de **los primeros 30 s y 5 momentos marcados** | doc 15, 10.2 | — |
| 11 | Dirección plano por plano | Plan visual + voz | `datos.json` + **hoja de planos** | `b.py`, `rearmar_largo.sh`, `planos_tiempo.py`, `hoja_planos.py` | **Tao (2)** |
| 12 | Animación | `datos.json` | Piezas nuevas construidas; 2–3 quedan en el banco del canal | Motor, `planos.js` | — |
| 13 | Sonido | Lista de planos | Sonido por imagen nueva, ambiente por lugar, música por acto | `sintet_sfx.py` | — |
| 14 | Control de calidad final | Todo | `12_qc.json` + render + descripción + capítulos + 3 títulos y 3 miniaturas | M8, `revisar_largo.py`, `render_largo.sh` | **Tao (3)** |
| 15 | Análisis posterior | Datos de YouTube | `13_resultados.json` a los 7 y 28 días + actualización de ficha o núcleo | M9 | — |

**Tiempo estimado con el motor actual:** ~3 h el video estándar, ~5–6 h el insignia (doc 15, 10.3). Las etapas 1–10 suman ~1 h 15 min: es trabajo de pensar, no de renderizar, y es donde se decide el video.

---

## M8 · Control de calidad
**Dos niveles:** **bloqueo** (no se produce hasta arreglarlo) y **aviso** (se informa y se decide).

| # | Qué detecta | Cómo se detecta | Nivel | Cómo se arregla |
|---|---|---|---|---|
| 1 | **Gancho débil** | Falla una puerta del M2, o tiene menos de 8 sobre 12 | Bloqueo si falla una puerta; aviso si es puntaje | Volver a 2.4 con otra familia; agregar ancla concreta; quitar adjetivos |
| 2 | **Historia genérica** | Ángulo con menos de 8 sobre 14; ninguna lente da resultado; la huella repite 4 de 5 | Aviso | Otra lente; buscar un agente; cambiar una pieza de la huella |
| 3 | **Información que sobra** | Hechos con papel "descarte" dentro del guion; tramos borrables | Aviso | Cortar. La duración la decide el contenido |
| 4 | **Imagen repetitiva** | Mismo lugar sin cambio de estado; mismo gráfico dos veces; composiciones seguidas iguales en la hoja de planos; un acto sin estreno | Aviso | Cambio de estado; transformar el gráfico; guardar un recurso para ese acto |
| 5 | **Uniones flojas** | "Y después" entre momentos; cambio de capítulo sin remate ni reentrada | Aviso | Reordenar; escribir el remate; abrir en lugar nuevo |
| 6 | **Promesas sin cumplir** | Preguntas del libro sin cierre; el gancho apunta a un momento que no existe; el título promete algo que el video no da | **Bloqueo** | Cerrar o quitar la promesa |
| 7 | **Afirmaciones sin respaldo** | Frases del guion sin hecho asociado; palabras fuertes sin fuente; una hipótesis mostrada como hecho; cifras redondeadas hacia arriba | **Bloqueo** | Buscar la fuente, bajar el tono a lo verificado, o rotular |
| 8 | **Mala comunicación visual** | El cuadro no tiene de protagonista lo que nombra la frase; un gráfico con más de una idea; texto encima de texto; algo sobre los subtítulos; tema a menos de un tercio del cuadro | Bloqueo para textos y subtítulos `[TAO]`; aviso para el resto | Aplicar 5.1; partir el gráfico; reencuadrar |
| 9 | **Ritmo irregular** | Curva de tensión con dos valles seguidos; muro de datos; todos los planos con la misma duración; planos de más de 4,5 s | Bloqueo para más de 4,5 s `[TAO]`; aviso para el resto | Mover el giro; repartir datos; ritmo por acto |
| 10 | **Pago revelado antes de tiempo** | El dato clave en título, miniatura, descripción, capítulos o primeros 30 s | **Bloqueo** `[TAO]` | Reemplazar por una referencia que lo señale |
| 11 | **Límites del canal** | Algo de la lista "prohibido" o "sensibles" de la ficha | **Bloqueo** | Quitar o rotular |

### Formato del informe (`12_qc.json`, resumido para Tao)
```
BLOQUEOS (0)
AVISOS (3)
 · Tramo 11: muro de datos (5 cifras en 28 s) → mover 2 a imagen sin voz
 · Acto 3: sin recurso nuevo → guardar el corte transversal para aquí
 · Huella: repite 4 de 5 con el video anterior → cambiar el tipo de final
PUNTAJES  ángulo 11/14 · gancho 10/12
```
**El informe siempre dice cómo arreglar cada cosa.** Un aviso sin arreglo no sirve.

---

## M9 · Aprendizaje continuo
### 9.1 Qué se guarda de cada video (`13_resultados.json`)
- **Lo que decidimos** (ya está en el expediente): lente, ángulo, familia de gancho, arquitectura, huella, duración, palabras por minuto, lugares, visualizaciones propias.
- **Lo que pasó** (lo reporta YouTube): impresiones, CTR, % que sigue a los 30 s, retención al 25/50/75 %, las 3 caídas más grandes y qué había en pantalla, título ganador en Test & Compare.
- **A los 7 y a los 28 días.** Los largos se comparan solo con largos de duración parecida.
- **Nunca se inventa un dato.** Si no hay vistas suficientes, se anota "sin datos".

### 9.2 Los estados del conocimiento
| Estado | Qué significa | Cómo sube |
|---|---|---|
| **Hipótesis** | Idea razonable, sin datos nuestros | — |
| **Señal** | Se vio en 3 videos o más del mismo canal, en la misma dirección | Se anota en la ficha del canal |
| **Regla** | Se confirmó con prueba causal (Test & Compare), o se repitió en 6 videos o más | Queda en la ficha del canal |
| **Regla universal** | Es regla en 2 canales distintos o más | Sube al núcleo |

- **Un cambio por video.** Si cambian cinco cosas, no se aprende ninguna.
- **Lo que solo se puede probar de verdad** son títulos y miniaturas. Todo lo demás es correlación, y se escribe así.
- **Un aprendizaje también puede bajar:** si 3 videos lo contradicen, vuelve a hipótesis.
- **Los pedidos de Tao no pasan por este filtro:** son regla desde que los dice (doc 11).

### 9.3 El ciclo
1. Publicar. 2. Leer a los 7 y 28 días. 3. Escribir **una** conclusión con su estado. 4. Actualizar la ficha del canal (o el núcleo). 5. Rearmar `MAESTRO.md`.

---

## 10. Cómo evoluciona el estudio actual
### 10.1 Componente por componente
| Componente | Hoy | Mejora | Tipo | Esfuerzo |
|---|---|---|---|---|
| Elección de tema y ángulo | Banco de ángulos + criterio del momento | M1 con hoja de hechos, 12 lentes, activos y puntaje | Procedimiento + plantilla | 30 min (plantillas) |
| Ganchos | Reglas H1–H6 (pensadas para Shorts) | M2: 6 conceptos de 4 familias, puertas y puntaje; 3 capas para largos | Procedimiento + plantilla | Incluido arriba |
| Títulos y miniaturas | Moldes + 3 variantes | Salen de los 3 mejores ganchos; van a Test & Compare | Procedimiento | 0 |
| Guion | Estructura fija de 7 pasos | 7 arquitecturas, libro de preguntas, huella | Procedimiento | 0 |
| Revisión del guion | Lectura | Radiografía + 12 detectores | **Script nuevo** (`radiografia.py`): cuenta palabras, cifras por tramo, uniones, preguntas sin cierre | ~1,5 h |
| Plan visual | Se decide al escribir `b.py` | `09_plan_visual.json` antes del `b.py` | Plantilla | 20 min |
| `planos_tiempo.py` | Ritmo parejo; banco fijo en el código | Ritmo por acto y banco leídos de la ficha | **Cambio de código** (se avisa) | ~1 h |
| Identidad por canal | Repartida en el código | `ficha.json` por canal | Datos + **cambio de código** para leerla | ~40 min las 4 fichas + ~1 h |
| `revisar_largo.py` | Subtítulos, duración de planos | + pago temprano, pregunta en la voz, lugar sin cambio, gráfico repetido, informe de variedad | **Cambio de código** (ya previsto en doc 14) | ~1,5 h |
| Aprendizaje | Notas sueltas en el proyecto | `13_resultados.json` + estados en la ficha | Datos; `reporte_semanal.py` (pendiente tu OK) | ~1 h |
| Motor, render, voz, Estudio | — | **Sin cambios** | — | 0 |

**Total: ~7 h, repartidas.** Las plantillas y los procedimientos (lo que más cambia la calidad de las decisiones) son ~1 h y no tocan código.

### 10.2 Orden propuesto (respeta el plan del doc 14: primero datos)
| # | Qué | Por qué primero |
|---|---|---|
| 1 | Publicar Pixar con Test & Compare (Tao) | Sin un largo público no hay nada que aprender |
| 2 | Plantillas del expediente + fichas de los 4 canales | No toca código; ordena todo lo demás |
| 3 | Aplicar M1–M4 **en papel** al próximo largo de Rabbit | Prueba el cerebro sin gastar un render |
| 4 | Arreglos del doc 14 (luz por canal, chequeos nuevos) | Mejoran todos los cuadros |
| 5 | `radiografia.py` | Automatiza lo que en el paso 3 se hizo a mano |
| 6 | Ficha leída por el código | Deja listo el alta de canales nuevos |
| 7 | Registro de aprendizaje | Cuando haya datos que registrar |

---

## 11. Ejemplo corto: el sistema aplicado a un tema ya verificado
Tema: la venta del equipo de animación por computador en 1986 (datos del guion de Pixar, ya verificados: vendido en 1986 por 5 millones de dólares; comprado en 2006 por 7.400 millones).

| Paso | Resultado |
|---|---|
| Creencia | "Los grandes del cine saben reconocer lo que vale" |
| Lentes que dan resultado | 7 Evaluación (lo que parecía un buen trato fue el peor) · 6 Función (lo que parecía no servir para hacer películas, sirvió) |
| Activos | A4 decisión con costo · A5 el cheque · A9 vuelco en el tiempo · A1 cifra (es el pago: se guarda) |
| Pregunta mayor | En qué se convirtió lo que vendió |
| Arquitectura | Caso |
| Escalada | Lo que está en juego + escala |

**Seis conceptos de apertura, de familias distintas** (formas; el texto final sale de la hoja de hechos):
| Familia | Primer cuadro | Qué guarda |
|---|---|---|
| 5 Hueco | El cheque de 5 millones, firmándose | Quién compra, y cuánto valdría después |
| 3 Contradicción | Un despacho lleno de premios y una mesa vacía | Por qué alguien con ese éxito necesita vender |
| 7 En juego | Un calendario y una cifra que hay que juntar | Qué es lo único que le queda por vender |
| 8 Narrativo | Dos personas y una pluma, en 1986 | Qué se está firmando |
| 6 Comparación | Una balanza: 5 millones a un lado, el otro tapado | El otro lado |
| 9 Interrupción | Empieza por el final: una sala de prensa en 2006, sin decir de qué | Todo el camino |

**Lo que el sistema habría detectado en la versión publicada:** detector 7 (pago temprano): el guion decía la cifra final y el nombre en los segundos 5–10 `[MED]`.

---

## Fuentes nuevas de este documento
- Davis, "That's Interesting!" (1971), síntesis: https://www.sfu.ca/~palys/interest.htm · resumen de las 12 categorías: https://cdn.odi.org/media/documents/6479.pdf
- Silvia, evaluaciones que producen interés: https://pressbooks.pub/principalsofpsychf24/?p=104 · Silvia y Kashdan: https://mason.gmu.edu/~tkashdan/publications/silvia%20kashdan%20compass%202009.pdf
- Kang y colegas (2009), curiosidad y confianza: https://www.cmu.edu/dietrich/sds/docs/loewenstein/WickCandleLearning.pdf · replicación: https://pmc.ncbi.nlm.nih.gov/articles/PMC10243256
- Hitchcock, suspenso y sorpresa (Bordwell): https://www.davidbordwell.net/blog/2013/11/29/hitchcock-lessing-and-the-bomb-under-the-table/
- Heath, *Made to Stick* (resumen): https://engineerguy.com/white-papers/made-to-stick.htm
- Ayuda de YouTube, títulos y miniaturas: https://support.google.com/youtube/answer/12340300 · rendimiento del contenido: https://support.google.com/youtube/answer/16559650
- Las demás fuentes (Loewenstein, Glass, Zacks, Mayer, Murch, Cutting, Tversky, Heer, Segel, Cleveland y McGill) están en los docs 13 y 15 y en `hooks-retencion-23-nov.md`.
