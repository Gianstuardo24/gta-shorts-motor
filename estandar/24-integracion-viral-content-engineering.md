# 24 · INTEGRACIÓN DE "VIRAL CONTENT ENGINEERING" (análisis, sin cambios aplicados)

> **Pedido de Tao (24-nov, 12:45):** incorporar el documento "Viral Content Engineering" a la arquitectura, **sin crear un segundo sistema ni otra biblioteca**. Solo análisis de integración: brechas e incorporaciones recomendadas.
> **Precisión de Tao:** no quiere evitar la repetición de fórmulas que funcionan. Quiere **identificarlas, guardarlas, reproducirlas, perfeccionarlas** y saber cuándo se agotan. Cuatro estados: prometedora, observada, probada, validada con resultados propios.
> **No se modificó código, bases de datos ni la arquitectura aprobada.** Las enmiendas de la Parte 6 quedan a tu decisión.

---

## 0. Veredicto en 6 líneas
1. **No es otro sistema: es el mismo, con otros nombres.** Sus seis módulos ya existen en el nuestro.
2. **Aporta una pieza que nos faltaba de verdad: la fórmula como objeto vivo**, con estado, historial de resultados, portafolio y señal de agotamiento.
3. **Corrige una regla nuestra.** El doc 20 penalizaba repetir; tu precisión lo invierte: repetir lo que funciona es la estrategia, y explorar es la minoría controlada.
4. Aporta tres disciplinas que tenemos débiles: **empaque** (título, miniatura y apertura como un todo), **compartibilidad** y **sonido**.
5. Aporta fuentes de formación. Entran como **afirmaciones a contrastar**, no como reglas.
6. Una advertencia que sale de la calibración de hoy: **"descomponer" un video con etiquetas interpretativas no es confiable.** Las fórmulas tienen que definirse con cosas medibles o con marcas visibles.

---

## 1. Módulo por módulo: qué ya existe
| Módulo de VCE | Lo que ya tenemos | Veredicto |
|---|---|---|
| 01 Research | Radar, nichos, inteligencia, laboratorio; tabla `virales` (23.162 filas), con columna de plataforma; `plataformas.py` ya trae TikTok e Instagram | **Redundante.** Solo falta registrar siempre el contexto del canal (tamaño, antigüedad) |
| 02 Deconstruction | Proceso "estudiar" + el evaluador v0 (doc 23) + registro de preguntas (doc 22) | **Se integra.** Le faltan empaque, compartibilidad y sonido |
| 03 Mechanism Library | Objeto "mecanismo" (doc 20) y los mecanismos G1–G14 con su evidencia (doc 18) | **Redundante.** Es lo mismo |
| 04 Formula Engine | Tabla `formulas`, pero es un texto por tema que se regenera en cada corrida; no hay fórmulas con identidad ni historial | **Brecha real** (Parte 3) |
| 05 Adaptation Engine | Proceso "aplicar": diagnóstico de la historia y cinco salidas (doc 21, A.3) | **Redundante**, con un ajuste: elegir primero la fórmula |
| 06 Testing & Learning | Proceso "aprender", `laboratorio.py`, y las métricas: retención, % visto, compartidos y suscriptores ganados **ya se guardan** | **Redundante en datos.** Falta usarlos para juzgar fórmulas |

**Lo que sería duplicar y no recomiendo:** una segunda biblioteca de mecanismos, otro registro de videos, y otro flujo de investigación.

---

## 2. Disciplinas: qué cubrimos y qué no
| Disciplina de VCE | Cobertura actual | Brecha |
|---|---|---|
| A. Psicología de la atención | Doc 18: hueco de información, sorpresa, interés, fluidez, concreción, tensión, emoción | **Identificación** (verse reflejado) y **satisfacción** como objetivo distinto de la retención |
| B. Hooks | Doc 18 y arsenal (1 pieza de gancho activa); el evaluador mide los primeros 30 s | Gancho **visual** y promesa implícita: hoy solo medimos el verbal y el ritmo |
| C. Storytelling | Registro de preguntas (se abre, se cierra, cuánto tarda) | Escalada y giros: nuestras etiquetas para eso fallaron en la calibración |
| D. Retención | Curvas propias (40 videos); quietud, cortes y cambios locales | Cruzar la curva con lo que pasaba en pantalla (etapa 7, ya prevista) |
| **E. Viralidad y distribución** | Casi nada | **Brecha:** por qué se comparte; diferencia entre vistas, retención y seguidores |
| **F. Empaque** | Doc 07 (reglas) y 21 piezas de título en el arsenal | **Brecha:** título, miniatura y apertura analizados como una sola promesa, y si el video la paga |
| **G. Producción: sonido** | No lo medimos | **Brecha:** música, efectos y silencios |

---

## 3. La fórmula como objeto vivo (el aporte principal)
### 3.1 Qué es una fórmula, para que no sea una plantilla
Una fórmula no es un guion con huecos. Es una **receta con un núcleo fijo y partes libres**.
| Parte | Qué contiene | Ejemplo, con datos de hoy (doc 23) |
|---|---|---|
| **Promesa y empaque** | Cómo se presenta | Marca conocida + pregunta corta: "¿Qué le pasó a ___?" |
| **Estructura** | Qué preguntas se abren, en qué orden y cuándo se cierran | Auge → el error → la caída → dónde está hoy |
| **Perfil medido** | Los rangos en que se mueve | Pantalla quieta cerca de 2 % · una imagen por frase · unas 180 palabras por minuto · lenguaje llano · unas 4 cifras por cada 100 palabras |
| **Mecanismos** | Por qué creemos que funciona | Hueco de información sobre algo que el público ya conoce |
| **Núcleo** | Lo que no se toca al reproducirla | Marca reconocible, la pregunta, el momento del error |
| **Partes libres** | Lo que cambia en cada video | Tema, imágenes, tono, ejemplos, duración |
| **Dónde aplica** | Formato, plataforma, nicho, canal | Largo · YouTube · negocios · Million Dollar Mistake |
| **Estado e historial** | Ver 3.2 | **Observada:** 2 videos externos (748 y 346 veces su tamaño), sin grupo de control |

### 3.2 Los cuatro estados que pediste
Calzan casi uno a uno con la escalera del doc 20. Propongo usar tus nombres.
| Estado | Qué significa | Cómo se llega | Equivale a (doc 20) |
|---|---|---|---|
| **Prometedora** | La dice un experto, o aparece en 1 o 2 videos | Basta registrarla con su fuente | Idea |
| **Observada** | Se repite en varios videos ajenos que rinden; mejor si falta en los videos normales de esos canales | Estudio con el evaluador, ojalá con control | Observado · con control |
| **Probada** | La usamos en videos propios y hay resultados medidos | Usos registrados con todas sus métricas | Probado en lo propio |
| **Validada** | Resultados propios consistentes sobre lo típico del canal | El criterio que ya usa `laboratorio.py` (réplicas alternadas y prueba estadística) | Principio provisional |
| En agotamiento · Retirada | Dejó de rendir | Señales de 3.5 | Debilitado |

**El estado vale por contexto.** Una fórmula validada en los largos de Million Dollar Mistake no queda validada en los Shorts de Dog Decoded.

**Dónde estamos hoy:** **cero fórmulas probadas.** La tabla de usos del arsenal está vacía (etapa 0). El primer objetivo es llevar dos o tres a "probada".

### 3.3 Qué elementos explican el resultado (con honestidad)
| Método | Qué permite decir | Límite |
|---|---|---|
| Comparar videos que usan la fórmula con y sin un elemento | "Este elemento aparece más en los que rinden" | Correlación, y pocos casos |
| Variar **un solo elemento** en un video propio | "Con este cambio, el resultado fue distinto" | Hacen falta varias repeticiones |
| Mirar la curva de retención en el momento exacto del elemento | "Aquí se fue la gente" o "aquí se quedó" | Solo en videos propios |

Por eso el pedido dice bien "explican **potencialmente**": con pocos videos no hay certeza, hay hipótesis ordenadas por fuerza.

### 3.4 Repetir y explorar: la regla del portafolio
| Tipo de video | Qué hace | Proporción |
|---|---|---|
| **Explotar** | Usa una fórmula probada o validada, con su núcleo intacto | La mayoría |
| **Perfeccionar** | Lo mismo, variando un solo elemento, con predicción registrada | Parte de los anteriores |
| **Explorar** | Prueba una fórmula prometedora u observada | Una minoría fija, que decides tú por canal |

- **Cada canal mantiene un portafolio** de dos a cuatro fórmulas activas, para no depender de una.
- **Cuándo innovar:** ninguna fórmula calza con la historia, una muestra agotamiento, o toca la cuota de exploración.
- **El criterio creativo no desaparece:** pasa a ser elegir bien la fórmula, respetar su núcleo y resolver las partes libres.
- **Mientras no haya fórmulas probadas, todo es exploración.** Es la situación de hoy.

### 3.5 Cómo se detecta el agotamiento
| Señal | De dónde sale |
|---|---|
| Sus últimos usos rinden bajo lo típico del canal, varios seguidos | Métricas propias |
| Su resultado cae uso tras uso | Historial de la fórmula |
| Muchos canales usan el mismo molde de título en poco tiempo | Radar (saturación) |
| Dejan de aparecer videos nuevos que rindan con esa fórmula | Radar |

Son **señales, no umbrales.** El sistema avisa y tú decides.

### 3.6 Un riesgo que hay que cuidar
Nuestro laboratorio faceless del 22-nov recogió que YouTube castiga el contenido "producido en masa con plantilla" (pendiente de verificar en la fuente oficial). **Repetir una fórmula no es repetir un video:** se repite el mecanismo y la estructura; el guion, las escenas y las imágenes son distintos cada vez.

---

## 4. Fuentes de formación gratuita o barata
**Regla de entrada:** lo que dice un experto se registra como **afirmación**, con quién lo dijo y si es fuente original o interpretación de otro. Queda en estado "prometedora" hasta contrastarlo.

| Fuente | Qué hay gratis | Qué extraer | Verificado hoy |
|---|---|---|---|
| **Fuentes oficiales** (Creator Insider de YouTube, ayuda de YouTube, portales de creadores de TikTok e Instagram) | Todo | Cómo recomiendan y qué miden. **Mandan sobre cualquier experto** | Creator Insider ya está en nuestro laboratorio; el resto, por revisar |
| **Paddy Galloway** | Entrevistas largas con transcripción (Creator Science n.º 152 y 209; Colin & Samir), hilos públicos | Análisis de casos atípicos, formatos repetibles, empaque | Sí |
| **Colin & Samir** | Su programa y episodios; el curso cuesta 299 USD | Empaque, narrativa, economía del creador | Sí (precio en su sitio) |
| **Ed Lawrence · Film Booth** | Canal, boletín y entrevistas | Volver interesante una idea, intros, uso de historia en videos educativos | Sí |
| **Ali Abdaal** | Curso por correo de 7 días, plantillas y canal; la academia cuesta 995 USD | Sistemas de producción | Sí (precio en su sitio) |
| **George Blackman** | Material público sobre guiones | Guion y retención | Solo vi que es instructor invitado de Colin & Samir |
| **Creator Science** (Jay Clouse) | Entrevistas con transcripción a varios de los anteriores | Una puerta de entrada a muchos expertos | Sí |
| **Clash · Short-Form Kickstart** | — | — | **No la encontré.** Sigue sin estar disponible |
| Ya en nuestro laboratorio | vidIQ, Edu Serrano, Ale Ferr y otros (31 fichas del 22-nov) | Ya extraído, con sus contradicciones marcadas | — |

**Dos avisos:**
- En la búsqueda aparecen sitios que revenden estos cursos a 23–29 USD. Son copias no autorizadas; no las usemos.
- Varias de estas personas venden cursos. Lo que enseñan gratis sirve, pero su incentivo es convencer.

### 4.1 Cómo se contrastan los expertos
| Paso | Qué se hace |
|---|---|
| 1 | Cada afirmación se anota con su fuente y su tipo: oficial, experto con datos, experto con opinión |
| 2 | Se busca si otra fuente dice lo contrario |
| 3 | Se contrasta con lo oficial, con nuestras mediciones y con nuestros experimentos |
| 4 | Solo entonces cambia de estado |

**Contradicciones que ya tenemos anotadas:** pruebas A/B en canales chicos (un experto dice que no, otro que sí); "precalentar" la cuenta y publicar de madrugada (lo dicen expertos, lo niega la fuente oficial); la duración ideal de un Short.
**Una coincidencia útil:** Galloway sostiene que se sobrestima el apetito del público por lo nuevo y se subestima su deseo de ver más de lo que ya le gusta. Va en la dirección de tu precisión. Sigue siendo la opinión de un experto, no una prueba.

---

## 5. Separación de evidencia
Cada fórmula, patrón y afirmación lleva estas marcas, y su estado vale solo dentro de ellas:
| Marca | Valores |
|---|---|
| Formato | Largo · Short |
| **Plataforma** (nueva) | YouTube · TikTok · Instagram |
| Nicho | Negocios · misterios · mascotas · café · juegos… |
| Canal | Cada uno de los nuestros |
| **Idioma** (nueva) | Español · inglés |

Una fórmula sube de alcance (de un canal a un nicho, de un nicho a universal) solo si se repite en otro contexto.

---

## 6. Enmiendas que esto pide a la arquitectura aprobada
**Ninguna está aplicada. Necesitan tu aprobación.**
| # | Enmienda | Por qué | Costo |
|---|---|---|---|
| 1 | **La fórmula entra como un patrón compuesto**, dentro de la misma biblioteca, con núcleo, partes libres, estado e historial | Es la pieza que falta. Como patrón compuesto no hace falta un sexto objeto ni otra tabla | Unos campos más en la etapa 2 |
| 2 | **Cambiar las reglas de diversidad del doc 20.** "Huella" y "uso reciente" pasan a cuidar que no se repitan **tema, imágenes y frases**, no la fórmula | Hoy castigarían justo lo que quieres explotar | Solo redacción |
| 3 | **Usar tus cuatro estados** en lugar de los nombres de la escalera | Mismo contenido, nombres más claros | Solo nombres |
| 4 | **Portafolio por canal** y regla de explotar, perfeccionar y explorar | Reemplaza "un elemento experimental por video" como regla única | Etapa 6 |
| 5 | **Seguimiento de agotamiento** | Para saber cuándo dejar una fórmula | Etapa 7 |
| 6 | Marcas de **plataforma e idioma** en la evidencia | Para TikTok, Reels y los canales en español | Etapa 2 |

**No cambia:** los cuatro procesos, los objetos, la prioridad del cerebro sobre lo demás, ni el orden de etapas. No se agrega ninguna etapa.

---

## 7. Brechas, por prioridad
| # | Brecha | Por qué mejora la inteligencia creativa | Cuándo |
|---|---|---|---|
| 1 | **Fórmula como objeto vivo** | Convierte aciertos sueltos en ventaja acumulada: lo que funciona se puede repetir, mejorar y vigilar | Etapas 2, 5, 6 y 7 |
| 2 | **Grupo de control para largos** (videos normales de los mismos canales) | Sin eso, una fórmula "observada" es solo un parecido entre videos | Antes de la etapa 5 |
| 3 | **Empaque** (título, miniatura, apertura y si el video paga la promesa) | Es lo que decide el clic, y hoy el evaluador no lo mira | Ampliar el evaluador |
| 4 | **Sonido** (música, efectos, silencios), medido | Es una disciplina entera que hoy no vemos | Ampliar el evaluador |
| 5 | **Compartibilidad y conversión** | Los datos ya se guardan (compartidos, suscriptores ganados), pero no se usan para juzgar fórmulas | Etapa 7 |
| 6 | **Ingreso ordenado de lo que dicen los expertos** | Hoy está en fichas sueltas; así cada afirmación tiene estado y contraste | Etapa 2 |
| 7 | **Evaluador en español y para Shorts** | La mitad de nuestros canales | Ampliar el evaluador |
| 8 | Talking head y marca personal | Fuera de nuestros canales actuales; queda anotado para después | Sin fecha |

## 8. Lo que recomiendo NO incorporar
| Qué | Por qué |
|---|---|
| Las 10 estructuras narrativas como taxonomía fija | Úsalas como hipótesis de fórmulas, no como categorías. Clasificar videos en ellas exige el tipo de etiqueta que falló hoy |
| "Descomponer" con etiquetas interpretativas por tramo | La calibración mostró que no son estables (doc 22) |
| Cursos de pago | Tu decisión, y lo gratuito alcanza para empezar |
| Un documento por experto o por fuente | Todo entra a la misma biblioteca; no más documentos |

## 9. Investigación y formación continua, sin duplicar
| Qué | Dónde vive | Documento |
|---|---|---|
| Lo que dicen los expertos | Biblioteca: afirmaciones con fuente y estado | Ninguno nuevo |
| Mecanismos y su evidencia | Biblioteca; hoy, doc 18 | El mismo |
| Fórmulas | Biblioteca: patrones compuestos | Ninguno nuevo |
| Videos estudiados | `analisis` y el evaluador | Ninguno nuevo |
| Lista de fuentes | La Parte 4 de este documento, hasta que pase a la biblioteca | Este |

**Ritmo:** se estudia una fuente cuando hay una pregunta abierta que esa fuente puede responder, no por acumular.

## 10. Lo que necesito que decidas
1. ¿Apruebas las seis enmiendas de la Parte 6?
2. ¿Qué proporción de exploración quieres por canal?
3. ¿Bajamos uno o dos videos normales de cada canal chico, para tener el grupo de control?

---

## Fuentes consultadas hoy
- Colin & Samir, curso y precio: https://www.colinandsamir.com/playbook · https://courses.colinandsamir.com/offers/ErBX2pQN
- Colin & Samir con Paddy Galloway: https://www.colinandsamir.com/resources/the-new-rules-of-youtube-from-paddy-galloway
- Creator Science, entrevistas a Paddy Galloway: https://podcast.creatorscience.com/guests/paddy-galloway
- Creator Science, entrevista a Ed Lawrence: https://podcast.creatorscience.com/ed-lawrence/
- Ali Abdaal, academia y precio: https://aliabdaal.com/?p=62615
- Resumen del texto público de Galloway sobre dominar un nicho: https://youmind.com/landing/x-viral-articles/youtube-niche-domination-playbook


## Ajustes de Tao a las enmiendas (24-nov, 18:49)
- **Enmienda 5:** una fórmula que rinde menos **no se retira**. Pasa a **descanso** y se vuelve a probar más adelante, porque puede volver a funcionar. Una baja con pocos videos puede ser azar: el aviso exige varios videos seguidos.
- **Enmienda 6:** la marca de plataforma e idioma es una **etiqueta, no un filtro**. Un gancho visto en TikTok o Reels se usa en Shorts como "prometedor" y se prueba con datos propios. Los ganchos son lo que mejor viaja entre plataformas de video vertical.
- **Estado:** las seis enmiendas siguen **sin aplicar**; falta la aprobación explícita de Tao.

## Descanso de una fórmula (regla de partida, 24-nov 20:10)
No hay dato propio todavía. Se parte con esto y se ajusta con resultados:
| Paso | Regla |
|---|---|
| Cuándo descansa | Varios usos seguidos bajo lo típico del canal (no uno solo) |
| Cuánto | **2 semanas** (unas 28 publicaciones del canal) |
| Cómo vuelve | **3 videos de prueba** |
| Si rinde | Vuelve a la cartera |
| Si no rinde | Descansa el doble y se prueba otra vez |

## Lista corta de ganchos y prueba por rotación (pedido de Tao, 24-nov 20:10)
**Idea de Tao:** una lista no muy extensa de ganchos o formatos que funcionen por una lógica (factores psicológicos), variar desde ahí, ver cuál rinde mejor en cada canal y probarlos todos.

| # | Tipo | Por qué engancha | Ejemplo del 24-nov |
|---|---|---|---|
| 1 | Contradicción | Rompe lo que creías | "Roswell Was Real. It Wasn't Aliens" |
| 2 | Secreto escondido | Falta una pieza y quieres verla | "RDR2 Hid a GTA 6 Secret for 8 Years" |
| 3 | Cifra que choca | El número no calza con lo esperado | "He Sold 10% of Apple for $800" |
| 4 | Te toca a ti | Habla de tu vida o tu mascota | "Your Dog Can Smell Your Stress" |
| 5 | Mito derribado | Algo cotidiano era falso | "Decaf Still Has Caffeine" |
| 6 | Comparación inesperada | Junta dos cosas que no esperabas | "El tráiler de GTA 6: 475 millones en 1 día" (le ganó a una película) |
| 7 | Error con consecuencia | Quieres saber cuánto costó | "Nike's Logo Cost Just $35" |
| 8 | Reto o instrucción | Te pide hacer algo | "Your Dog Catches Your Yawns" (bosteza frente a tu perro) |

**Estado de los 8 tipos:** prometedores. Ninguno está probado con datos propios.

**Cómo se prueban**
- Cada canal **rota los 8 tipos**, sin repetir el mismo dos veces seguidas. El tipo se anota en la ficha de cada video.
- Para que el tema no confunda el resultado, un mismo tipo se usa con temas distintos.
- **Medidas** (YouTube Analytics): cuántos siguen después de los 3 primeros segundos, y qué porcentaje del video ven.
- **Ritmo real:** con 2 videos al día por canal, cada tipo sale unas 2 veces por semana. **Primera lectura útil a las 3–4 semanas** (6–8 usos por tipo y canal). Antes de eso es ruido.
- Los ganchos vistos en TikTok o Reels entran a esta lista como prometedores (enmienda 6: la plataforma es etiqueta, no filtro).

**Clasificación de los 14 del 24-nov (primera ronda)**
| Canal | Video | Tipo |
|---|---|---|
| TheViceVerseGG | GTA 6 Hid Dexter's Apartment | 2 |
| TheViceVerseGG | RDR2 Hid a GTA 6 Secret for 8 Years | 2 |
| ViceVersoGG | El tráiler de GTA 6: 475 millones en 1 día | 6 |
| ViceVersoGG | GTA 6 tiene que superar 215 millones | 3 |
| DogDecoded | Your Dog Catches Your Yawns | 8 |
| DogDecoded | Your Dog Can Smell Your Stress | 4 |
| CatDecoded | Your Cat Tracks You by Voice | 4 |
| CatDecoded | Your Cat Needs That Box | 4 |
| ChiChibitsTV | Decaf Still Has Caffeine | 5 |
| ChiChibitsTV | Same Coffee. Same Milk. 3 Different Drinks | 6 |
| MillionDollarMistake | Nike's Logo Cost Just $35 | 7 |
| MillionDollarMistake | He Sold 10% of Apple for $800 | 3 |
| TheRabbitLoop | The Pyramid UFOs Were a Camera Trick | 5 |
| TheRabbitLoop | Roswell Was Real. It Wasn't Aliens | 1 |

**Lo que muestra la tabla:** hoy se repitieron tipos dentro del mismo canal (GTA inglés 2 y 2; Gatos 4 y 4). Desde la próxima tanda, los dos videos de un canal usan tipos distintos.
