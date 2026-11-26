# 15 · BIBLIA DE PRODUCCIÓN DE VIDEOS LARGOS (10–12 min)

> ⚠️ **Estado (24-nov, 00:20):** este documento es un **catálogo de técnicas e hipótesis** (nivel D). Sus números y umbrales quedaron retirados como norma; ver doc 18, Parte 4.3.
> **Alcance:** solo videos largos animados, en horizontal. Los Shorts tienen su documento aparte (16) y **no dictan nada de lo que hay aquí**.
> **Para los largos, este es el documento que manda.** Los docs 01–10 quedan como detalle e historia. Si algo choca, valen esta Biblia y el doc 14.
> **Base:** las correcciones de Tao (doc 11 y 12), las mediciones de nuestros 6 largos (doc 13 y 14) e investigación externa sobre documentales, explicadores animados, periodismo de investigación visual, visualización de datos, cine y animación.

## 0. Cómo leer esta Biblia
- **Etiquetas de evidencia:**
  - `[TAO]` pedido o aprobado por Tao;
  - `[MED]` medido en nuestros videos;
  - `[EXT]` investigación o fuente externa (lista al final);
  - `[OFICIO]` práctica de profesionales, sin estudio detrás;
  - `[HIP]` hipótesis nuestra, por probar.
- **Nada aquí está probado en la retención de nuestros canales.** Los "por qué" dicen por qué *podría* mejorar la experiencia.
- **Es una caja de herramientas, no una lista de obligaciones.** Cada video elige. Lo único obligatorio son las reglas duras de la Parte 13.
- **Cada recomendación tiene 4 partes:** qué hacer, cómo hacerlo en Canvas, cuándo usarlo y por qué.

### Nota técnica que condiciona todo
Nuestro motor dibuja cada cuadro como **función del tiempo** (`render(t)`): puede saltar a cualquier segundo sin haber dibujado los anteriores. Por eso:
- **Toda animación se escribe como fórmula de `t`**, sin estado acumulado. Un rebote es `e^(-k·d)·cos(w·d)`, con `d = t − inicio`. No es una simulación paso a paso.
- **El azar es determinista:** `rnd(i)` con semilla, para que una partícula esté en el mismo lugar cada vez que se dibuja el cuadro.
- **Los desenfoques se hacen dibujando a 1/4 de tamaño y agrandando,** no con `ctx.filter` (lento al renderizar).

---

## 1. Qué es un largo y qué tipos hacemos
**El contrato con el espectador:** quien abre un video de 10–12 minutos acepta invertir tiempo a cambio de una historia que avanza y de una pregunta que se responde al final. Un largo no es un Short estirado ni una lista de datos con imágenes.

| Tipo | Canal típico | Qué mantiene mirando | Arquitectura (Parte 2) |
|---|---|---|---|
| **El caso** (una historia con personas y una decisión) | MDM | Qué va a pasar y cuánto costó | Cuatro actos |
| **La investigación** (un misterio con evidencia) | Rabbit | Qué fue en realidad | Versiones enfrentadas |
| **La explicación** (cómo y por qué funciona algo) | Perros, Gatos, Café | Entender algo que ves todos los días | Escalera |
| **El top** (varios casos) | MDM, Rabbit | Cuál es el número 1 y por qué | Escalera con hilo |

---

## 2. Arquitectura narrativa
### 2.1 Los tres ladrillos (valen para todos los tipos)
| Ladrillo | Qué es | Fuente |
|---|---|---|
| **Anécdota** | Una secuencia de acciones: pasó esto, y eso llevó a esto otro. Tiene impulso propio, como un tren que va a alguna parte | `[EXT]` Ira Glass |
| **Carnada** | Plantear preguntas todo el tiempo y responderlas. Toda pregunta que se abre, se responde | `[EXT]` Ira Glass |
| **Reflexión** | El momento que dice por qué importa lo que acabas de ver | `[EXT]` Ira Glass |

Un buen relato va y viene entre acción y reflexión. Nuestros guiones actuales son casi pura información: les faltan anécdotas (acciones concretas de alguien) y reflexiones.

**Regla de unión `[OFICIO]`:** entre un momento y el siguiente tiene que caber un "pero" o un "por lo tanto". Si solo cabe "y después", no hay historia. Se revisa leyendo la lista de momentos, antes de escribir el guion.

### 2.2 Plantilla base de 10–12 min (cuatro actos)
Viene de la estructura de la televisión: una apertura en frío, cuatro actos con un remate cada uno y un epílogo `[EXT, oficio]`.

| Tramo | Minuto | Qué pasa | Imagen |
|---|---|---|---|
| **Apertura en frío** | 0:00–0:20 | El objeto o la escena más fuerte, sin contexto. Una contradicción | El tema llena el cuadro desde el primer cuadro |
| **Promesa** | 0:20–0:50 | Qué está en juego y qué vas a entender al final, **sin dar la respuesta** | Se presenta el motivo visual del video |
| **Acto 1: el mundo** | 0:50–3:00 | Quién, dónde, cómo era lo normal. Se responde una primera pregunta chica (~2:00). Remate 1 | Lugar 1 y 2 |
| **Acto 2: la complicación** | 3:00–6:00 | Obstáculos encadenados. **Giro del medio** (~5:30): algo cambia lo que creíamos. Remate 2 | Lugares 3–5; cambia el color |
| **Acto 3: la escalada** | 6:00–9:00 | Consecuencias cada vez mayores. El punto más tenso. Remate 3 | Lugares 6–8; planos más cortos |
| **Acto 4: el pago** | 9:00–10:30 | La respuesta (el pico) y la reflexión | La imagen más elaborada del video |
| **Epílogo** | 10:30–11:15 | Imagen de regreso al inicio, la lección y el puente al próximo video | Pantalla final sobre una escena viva |

- **El dato clave no aparece antes del Acto 4**, tampoco en la apertura `[TAO]`.
- A ~165 palabras por minuto, el guion tiene **1.700–1.900 palabras**.

### 2.3 Arquitectura "versiones enfrentadas" (investigación, Rabbit)
Tomada de *The Thin Blue Line* de Errol Morris: los testimonios que se contradicen se recrean uno por uno, con un estilo marcado, y las recreaciones no se pueden armar en una sola imagen coherente `[EXT]`.

| Paso | Qué pasa | Imagen |
|---|---|---|
| 1. Lo que se contó | La versión famosa del caso | Recreación a color, tal como la contaron |
| 2. Lo que vieron | Cada testigo, por separado | La **misma escena repetida con diferencias**, una por testigo |
| 3. La evidencia | Qué quedó registrado | Estilo de "sensor": pantalla, radar, documento |
| 4. La explicación oficial | Qué dijo la investigación | La escena se recrea otra vez, ahora con la explicación |
| 5. Lo que no calza | Qué sigue sin explicarse | Vuelve la primera recreación, con la parte dudosa marcada |
| 6. Veredicto | Cerrado, parcial o abierto | El sello del expediente |

- **La línea de tiempo es el marco maestro:** todo se ordena sobre una sola línea visible, a la que se vuelve. Es el recurso central de Forensic Architecture, que sincroniza sobre una línea de tiempo el material de distintas fuentes `[EXT]`.
- **Regla de verdad `[TAO]`:** una recreación de un testimonio se rotula como testimonio. Una hipótesis nunca se muestra como hecho.
- **Aquí repetir una escena es el recurso, no un defecto:** cada repetición trae una diferencia que significa algo.

### 2.4 Arquitectura "escalera" (explicaciones y tops)
Las listas actuales (Perros, Café) son enumeraciones donde todo pesa igual `[MED]`.

| Regla | Qué hacer |
|---|---|
| **Orden por sorpresa, no por lógica** | Del más familiar al más inesperado. El último ítem es el que cambia cómo ves los anteriores |
| **Cada ítem es una mini-historia** | Lo que ya viste → lo que la gente cree → lo que dice el estudio → qué significa (reflexión) |
| **Un hilo que cruza la lista** | Una pregunta planteada en la apertura que solo responde el último ítem |
| **Tres movimientos, no doce ítems** | Agrupar: "lo que hace con la cara", "con el cuerpo", "con el espacio" |
| **Un ítem rompe la regla** | Hacia la mitad, un ítem contradice lo anterior. Es el giro del medio |
| **Peso desigual** | 2–3 ítems largos (90 s) y varios cortos (25 s). Nunca todos iguales |

### 2.5 El libro de preguntas (manejo de la curiosidad)
La curiosidad nace de una **pregunta específica y visible**; una pregunta vaga no la genera `[EXT]` (Loewenstein, ya en nuestras reglas).

**Qué es:** una tabla que acompaña al guion.
| Pregunta | Se abre en | Se cierra en | Tipo |
|---|---|---|---|
| ¿Cuánto terminó valiendo? | 0:10 | 9:20 | mayor |
| ¿Por qué necesitaba vender? | 0:50 | 2:10 | menor |

**Reglas `[OFICIO]`:**
1. Siempre hay **una pregunta mayor y al menos una menor abiertas**.
2. Una menor se cierra en 60–120 s. La mayor no se cierra antes del Acto 4.
3. **Al cerrar una, se abre otra** en la misma frase o en la siguiente.
4. Todo lo que se abre se cierra. Una pregunta sin respuesta es una promesa rota.

**Cómo abrir preguntas sin preguntas en la voz `[TAO]`:**
| Recurso | Ejemplo |
|---|---|
| Afirmar el hueco | "Nobody could explain why the radar showed nothing." |
| Contradicción | "He was the richest man in the room. And he was broke." |
| Pregunta dibujada | Una cifra tapada, un casillero vacío en el tablero, un "???" en la ficha |
| Anuncio parcial | "Three things saved it. The third one was an accident." |

### 2.6 Transiciones de capítulo
Un cambio de capítulo es el momento donde más conviene sostener al espectador. Marcar los límites entre eventos mejora el recuerdo de lo visto `[EXT]`. Tiene 4 piezas:

| Pieza | Qué es | Cómo en Canvas |
|---|---|---|
| **Remate** | La última frase deja un hueco | Guion |
| **Botón visual** | La última imagen queda sin resolver (la puerta que se abre, la mano sobre el teléfono) | Plano sostenido 0,6 s después de la voz; la acción queda a medio hacer |
| **Tarjeta** | Lugar y fecha del capítulo que viene, 1,5–2 s | Texto que entra con el sonido propio del canal |
| **Reentrada** | El capítulo nuevo abre en un lugar nuevo, con un plano de ubicación | Plano general con capas en paralaje |

**Tipos de remate (variar) `[EXT, oficio]`:** una revelación, una vuelta de tuerca, un detalle inquietante y silencioso, un reloj que corre. No todos tienen que ser fuertes: a veces rinde más un momento quieto que incomoda.

### 2.7 El final
Las experiencias se recuerdan sobre todo por su momento más intenso y por cómo terminan `[EXT]` (Fredrickson y Kahneman).
- **El pico se diseña:** la imagen más trabajada del video va en la revelación.
- **El último cuadro es una imagen, no una plantilla:** vuelve el objeto del inicio, cambiado.
- **Puente:** una frase y una imagen del próximo caso.
- **La pantalla final va encima de una escena que sigue viva** (un ciclo de ambiente de la Parte 6.4), no sobre un fondo quieto de 20 s como hoy `[MED]`.

---

## 3. Ritmo y progresión visual
### 3.1 El ritmo sigue a la historia
En el cine, la duración de los planos cambia según el tramo: más largos en la presentación, más cortos al entrar al clímax y otra vez más largos al cerrar `[EXT]` (Cutting). Nuestros planos duran todos casi lo mismo `[MED]`.

| Tramo | Duración de plano | Movimiento |
|---|---|---|
| Apertura | 1,5–2,5 s | Mucho |
| Acto 1 | 3–4 s | Suave |
| Acto 2 | 2,5–3,5 s | Medio |
| Acto 3 | 1,8–3 s | Creciente |
| Pico | Ráfaga breve y después **un plano de 4,5 s** | El plano largo es el respiro |
| Epílogo | 3,5–4,5 s | Lento |

- **Tope de 4,5 s por plano `[TAO]`.**
- **Cómo:** en `planos_tiempo.py`, el intervalo de corte deja de ser fijo y se lee de una tabla por capítulo.
- Todo esto es `[HIP]`: no hay estudios de YouTube que lo prueben.

### 3.2 Alternar denso y liviano
Después de un tramo de datos (cifras, fechas, nombres) va un tramo de acción o de imagen sin datos nuevos. Las personas aprenden mejor cuando el material viene en tramos y sin adornos que compiten `[EXT]` (Mayer). Regla práctica: **nunca más de 3 datos nuevos seguidos sin una imagen que respire**.

### 3.3 Guion de color
En Pixar, el guion de color es una tira de miniaturas que muestra de un vistazo el arco emocional de toda la película, con formas y color `[EXT]`.

| Qué | Cómo en Canvas | Cuándo | Por qué |
|---|---|---|---|
| Una fila de muestras de color, una por capítulo: tono dominante, brillo y un acento | Cada capítulo tiene su paleta (`fondo`, `medio`, `acento`, `luz`). Encima del cuadro se pinta un degradado con `globalCompositeOperation = 'soft-light'`. Entre capítulos, la paleta se mezcla durante 1 s | Antes de construir. Se aprueba mirando la tira completa | El color ordena la historia y marca los cambios `[OFICIO]`. En Navy, 3 colores ocupan el 85 % del video `[MED]` |
| **Un solo color de acento** reservado para "lo importante" en todo el video | Una constante por video. Solo la usa el elemento clave de cada plano | Siempre | Resaltar lo esencial ayuda a entender `[EXT]` (señalización, Mayer) |
| Arco de brillo | El brillo medio del capítulo sigue a la historia: baja en las malas noticias y sube en la resolución | Casos e investigaciones | Mismo recurso que usa el guion de color |

**Un solo lenguaje gráfico por video.** El color cambia; el estilo de dibujo no. Máximo 2 estilos (doc 14).

### 3.4 Progresión de escala
Que el video "crezca": se empieza cerca y chico (un objeto, una mano) y se termina grande (la ciudad, el mapa, la multitud). O al revés, si la historia va de lo enorme a lo íntimo. Se decide una vez, en el mapa visual. `[OFICIO]`

### 3.5 La novedad se reparte
En Café no aparece ninguna imagen nueva en la segunda mitad `[MED]`. Al planificar, cada acto estrena al menos **un lugar, un tipo de gráfico y un recurso** que no se vio antes. Los mejores se guardan para los Actos 3 y 4.

---

## 4. Dirección y composición
### 4.1 Por qué se corta
La regla de seis de Walter Murch ordena las razones de un corte por importancia: emoción (51 %), historia (23 %), ritmo (10 %), trayectoria de la mirada (7 %), plano de la pantalla (5 %) y espacio (4 %). Si hay que sacrificar algo, se sacrifica desde abajo `[EXT, oficio]`.
- **Para nosotros:** un corte se justifica porque cambia lo que se siente o lo que se sabe. "Tocaba cortar" es la razón más débil.

### 4.2 Reglas de composición
| Qué | Cómo en Canvas | Cuándo | Por qué |
|---|---|---|---|
| **Un punto de atención por plano** | Antes de dibujar el plano se define `foco = {x, y}`. Todo lo demás baja contraste (`globalAlpha` 0,6–0,8) o se desenfoca | Siempre | Al ver una película, casi todos miran el mismo punto, y la mirada va a las caras y a lo que se mueve `[EXT]` (Smith) |
| **Trayectoria de la mirada entre cortes** | El `foco` del plano nuevo cae a menos de ~15 % del ancho de donde estaba el foco anterior. Se calcula al armar los planos y se ajusta el encuadre | En cortes rápidos (menos de 2,5 s) | El ojo no tiene que buscar. Es el 4.º criterio de Murch `[EXT]` |
| **El tema ocupa un tercio o más del alto** | Regla de tamaño al encuadrar: `alto_sujeto / alto_cuadro ≥ 0,33` en la mayoría de los planos | Siempre, salvo en planos de ubicación | En Café y Navy el tema casi no se ve `[MED]`. Además, se ve en pantallas chicas |
| **Tres capas de profundidad** | Frente, medio y fondo en lienzos o grupos separados. Al mover la cámara, cada capa se desplaza `dx × factor` (frente 1,4 · medio 1 · fondo 0,4) | En planos de lugar y movimientos de cámara | Es la cámara multiplano de Disney: capas que se mueven a distinta velocidad dan sensación de profundidad `[EXT]` |
| **Giro aparente** | El fondo y el frente se mueven en sentidos opuestos | Para "rodear" un objeto importante | Variante del multiplano que da efecto de rotación `[EXT]` |
| **Perspectiva atmosférica** | Las capas lejanas se pintan con menos contraste y tiradas al color del cielo (mezcla de 30–60 %) | Exteriores | Profundidad sin 3D `[OFICIO]` |
| **Altura de cámara con sentido** | Se mueve la línea del horizonte: baja = el sujeto se ve poderoso; alta = se ve chico o vigilado. En 2D se logra con la posición del suelo y el escalado de los objetos | Poder, amenaza, soledad | Lenguaje de cámara clásico `[OFICIO]` |
| **Simular lentes** | "Gran angular": mucha diferencia de paralaje entre capas y sujeto chico. "Tele": capas casi pegadas, fondo grande y borroso | Gran angular para lugares; tele para caras y tensión | Variedad sin dibujar más `[OFICIO]` |
| **Encuadre dentro del encuadre** | Una puerta, una ventana o una pantalla dibujada en la capa del frente, con `clip()` | Espiar, encierro, recuerdo | Cambia la sensación sin cambiar el lugar |
| **Luz que dirige** | Degradado radial con `globalCompositeOperation = 'lighter'` sobre el foco, y `'multiply'` en los bordes | Siempre que el plano sea oscuro | En cuadros oscuros hay menos opciones de adónde mirar; la luz decide `[EXT]` (Smith y Cutting) |

### 4.3 Los cinco movimientos
Del análisis de Tony Zhou sobre Kurosawa `[EXT, oficio]`: en cada plano puede moverse la naturaleza, un grupo, un individuo, la cámara y el corte. No hace falta que se muevan los cinco a la vez, porque cansa.

| Movimiento | Cómo en Canvas | Cuándo |
|---|---|---|
| **Naturaleza** (lluvia, viento, humo, polvo, olas) | Partículas con posición `f(t, i)`. Humo: círculos con `alpha` que baja y radio que crece. Lluvia: líneas con desplazamiento `(t·v) % alto` | Cuando el personaje está quieto: el plano igual vive |
| **Grupo** (una reacción que se contagia) | Varios personajes con la misma acción, desfasada 0,1 s cada uno | Reacciones: sorpresa, aplauso, pánico |
| **Individuo** (el gesto que muestra lo que siente) | Poses exageradas: quien duda, camina de lado a lado; quien se avergüenza, se encoge | Siempre que haya emoción |
| **Cámara** (con principio, medio y fin) | Todo movimiento arranca suave, viaja y **se detiene en algo**. Easing de entrada y de salida | Para llevar la mirada de A a B |
| **Corte** (cortar en movimiento) | El corte cae a mitad de un gesto o de un objeto que cruza | Para que el corte no se note |

**Regla que sale de aquí:** elegir **2 de los 5** por plano. Y cada movimiento de cámara tiene que terminar en algo que valga la pena ver.

---

## 5. Diversidad de escenas y narración con el entorno
### 5.1 El entorno cuenta la historia
En el diseño de parques temáticos y videojuegos, la historia se mete en el espacio mismo: el visitante deduce qué pasó a partir de lo que ve, uniendo causa y efecto `[EXT]` (Don Carson).

| Qué | Cómo en Canvas | Cuándo | Por qué |
|---|---|---|---|
| **Viñetas de causa y efecto** | Objetos que cuentan algo sin texto: una silla volcada, una taza fría, cajas a medio embalar, un calendario tachado | En cada lugar, 2–3 | El espectador deduce, y deducir es participar `[EXT]` |
| **Cambio de estado al volver** | Cada lugar tiene 2–3 estados (`antes`, `durante`, `después`) con opciones del set: `luz`, `hora`, `objetos`, `gente` | Cada vez que se vuelve a un lugar | Volver a un lugar ayuda a ubicarse; que haya cambiado muestra el paso del tiempo. Responde a la preocupación de Tao por las repeticiones |
| **Ficha de lugar** | Por cada espacio: época, 5 objetos reales de esa época, fuente de luz, 2 colores, qué cuenta | Al planificar | Evita el "escenario genérico" `[TAO]` |
| **De lo general al detalle** | Secuencia: ubicación (2 s) → medio → detalle del objeto → cara | Al entrar a un lugar nuevo | Orienta antes de mostrar |
| **Hora y clima con función** | Parámetros `hora` (color del cielo y de la luz) y `clima` (partículas) | La hora marca el paso del tiempo; el clima, el ánimo | Usa el movimiento de la naturaleza |

### 5.2 Micro-escenas
El vocabulario de 14 tipos está en el doc 10. Las tres que más faltan hoy:
- **punto de vista** (lo que ve el personaje);
- **detalle del lugar** (el rincón del escritorio);
- **objeto que prueba** (la evidencia).

### 5.3 Metas de variedad (orientativas)
- Un lugar nuevo por capítulo: 8–12 en un video de 10–12 min.
- Ningún lugar ocupa más del 20 % del video.
- Ningún regreso sin cambio de estado.
- **Se informan en la hoja de planos; no aprueban ni rechazan** (doc 14).

---

## 6. Técnicas de animación en Canvas 2D
### 6.1 Los 12 principios de la animación, en código
Los formularon Thomas y Johnston en Disney: sirven para que lo dibujado parezca obedecer a la física y, además, para el ritmo emocional y el atractivo del personaje `[EXT]`.

| Principio | Cómo en Canvas (como función de `t`) | Cuándo |
|---|---|---|
| **Entrada y salida suaves** | `ease = u<.5 ? 2u² : 1−(−2u+2)²/2`. Ningún movimiento es lineal | Siempre |
| **Anticipación** | Antes del movimiento, 0,12–0,2 s en sentido contrario al 8–12 % de la distancia | Saltos, giros, lanzar, levantarse |
| **Continuación y solapamiento** | Las partes "colgantes" (pelo, corbata, cola, brazo) siguen al cuerpo con retraso: `ang_hijo(t) = ang_padre(t − 0,08)` más una oscilación que se apaga | Al frenar o girar |
| **Aplastar y estirar** | `scale(1+s, 1−s)` conservando el área; `s` proporcional a la velocidad | Caídas, rebotes, sorpresas |
| **Arcos** | Las manos y los objetos viajan por una curva (Bézier cuadrática), no en línea recta | Gestos y lanzamientos |
| **Acción secundaria** | Un movimiento menor que acompaña: parpadeo, dedo que golpea la mesa, respiración (`sin(t·2)·2 px`) | Planos de más de 2 s |
| **Ritmo del movimiento** | Rápido = liviano o nervioso; lento = pesado o triste. Se define por personaje | Personalidad |
| **Exageración** | Las poses clave se llevan 20–30 % más lejos de lo real | Reacciones |
| **Puesta en escena** | Una sola acción a la vez. La silueta del personaje se entiende en negro | Siempre |
| **Atractivo** | Diseño del personaje: proporciones claras, ojos expresivos, ropa con detalle | "Personaje v2" (pendiente) |

### 6.2 Animación limitada: la que podemos sostener
La televisión resolvió hacer mucha animación con poco: poses sostenidas, ciclos que se repiten, mover solo la boca, y recorrer con la cámara una ilustración fija. El anime lo convirtió en estilo, con imágenes fijas muy detalladas, pausas dramáticas y movimiento de cámara `[EXT]`.

| Qué | Cómo en Canvas | Cuándo | Por qué |
|---|---|---|---|
| **Pose fuerte + cámara que se mueve** | El personaje queda en una pose clave muy clara; se mueven la cámara, la luz y las partículas | Momentos dramáticos | Más barato y, bien hecho, más cinematográfico |
| **Ciclos** | Caminar, escribir, respirar: una función periódica `f(t % periodo)` | Fondo y acciones repetitivas | Reutilizable en todos los videos |
| **Ilustración detallada + recorrido** | Un plano muy trabajado (o una lámina) recorrido con paralaje de 3 capas | Planos de ubicación y de autor | Mucho detalle con poco movimiento |
| **Cuadro de barrido** | En un movimiento muy rápido, 2–3 cuadros con el objeto estirado en la dirección del movimiento | Golpes, giros rápidos | Da velocidad sin más dibujos |
| **Banco de piezas** | Secuencias paramétricas que se repiten entre videos con otros datos (ver Parte 10) | Siempre | Es la clave de la escala |

### 6.3 Que los personajes actúen
Es la crítica más dura del doc 14: hoy los personajes no actúan.

| Qué | Cómo en Canvas | Cuándo | Por qué |
|---|---|---|---|
| **Mirada con intención** | Las pupilas se desplazan hacia el objeto o la persona que importa (`dx, dy` hacia el `foco`), con un salto rápido de 0,1 s | Antes de que aparezca algo importante | La mirada de un personaje guía la del espectador `[OFICIO]` |
| **Boca que habla** (cuando el personaje "dice" algo en la escena) | Apertura de boca `= |sin(t·16)|` filtrada por un ritmo de sílabas, activa solo en su turno | Diálogos mudos, llamadas | Hoy nadie mueve la boca |
| **Reacción antes que acción** | El personaje reacciona (cejas, hombros) 0,2 s **antes** de moverse | Sorpresas, decisiones | Es la anticipación aplicada a la actuación |
| **Reacción en cadena** | El segundo personaje reacciona 0,15–0,3 s después del primero | Escenas de a dos | Movimiento de grupo |
| **Manos ocupadas** | Cada personaje tiene algo que hacer con las manos según el lugar (taza, lápiz, teléfono) | Planos de más de 2,5 s | Evita al personaje "de pie explicando" `[MED]` |

### 6.4 Movimiento procedural (gratis una vez hecho)
| Qué | Cómo en Canvas |
|---|---|
| Vaivén de reposo | `sin(t·w + fase_i)` con fase distinta por personaje |
| Cuerdas, cables, banderas | Cadena de puntos con onda viajera `sin(t·w − i·k)` |
| Multitudes | El mismo personaje con variantes de color y fase por `rnd(i)` |
| Dibujo de líneas | `setLineDash([L, L])` y `lineDashOffset = L·(1−u)` para que la línea "se dibuje" |
| Escritura a mano | Texto revelado con `clip()` que avanza, más una punta de lápiz en el borde |
| Conteos | Número `= round(lerp(a, b, ease(u)))`, con un pequeño rebote al llegar |
| Transformar una forma en otra | Las dos formas se guardan con la misma cantidad de puntos y se mezclan punto a punto |

La última es la idea central del motor de 3Blue1Brown, que es programático como el nuestro: cualquier objeto puede transformarse en otro `[EXT]`. Sirve para que una cifra se vuelva un gráfico, o un mapa se vuelva una ruta.

---

## 7. Visualización creativa de la información
### 7.1 Principios (con respaldo de investigación)
| Principio | Qué significa para nosotros | Fuente |
|---|---|---|
| **Congruencia** | La forma del gráfico se parece a lo que explica: el tiempo va de izquierda a derecha, lo que sube se dibuja hacia arriba, el espacio se muestra como espacio | `[EXT]` Tversky |
| **Aprehensión** | Las animaciones fallan cuando van más rápido o más cargadas de lo que se puede percibir. Los procesos se muestran **en pasos**, con pausa y con lo importante resaltado | `[EXT]` Tversky |
| **Transiciones por etapas** | Al pasar de un gráfico a otro, los elementos se mueven en etapas y conservan su identidad (la misma barra sigue siendo la misma barra). Mejora la lectura | `[EXT]` Heer y Robertson |
| **Posición antes que área** | Las personas comparan mejor posiciones sobre una escala común; después largos; después ángulos; lo peor son las áreas | `[EXT]` Cleveland y McGill |
| **Repetir, no agrandar** | Para mostrar más cantidad, se dibujan más figuras del mismo tamaño, no una figura más grande | `[EXT]` Isotype (Neurath) |
| **Guiar la lectura** | Resaltar, guiar las transiciones y ordenar: las tácticas del relato con datos cuando manda el autor | `[EXT]` Segel y Heer |
| **Palabra e imagen a la vez** | El elemento clave aparece en la palabra que lo nombra | `[EXT]` Mayer · `[TAO]` |

**Advertencia:** estos estudios miden comprensión y lectura de gráficos, no retención. Y contar filas de figuritas no siempre es más preciso que una barra: se usa para **impacto**, no para precisión.

### 7.2 Catálogo: qué forma para qué información
| Información | Forma | Cómo en Canvas | Cuándo |
|---|---|---|---|
| Una cantidad grande | **Unidades repetidas:** 1 figura = N | Cuadrícula de íconos que se llena por filas; cada ícono entra con rebote y un desfase de 20 ms | Cuando importa el impacto |
| Dos cantidades muy distintas | **Comparación física:** las dos en la misma escala, y la cámara tiene que alejarse para que la grande quepa | `scale` de la cámara animado de 1 a 0,1 | "Era 1.480 veces más" |
| Cambio en el tiempo | **Línea sobre escala común** que se dibuja | `lineDashOffset`; el punto actual va con el acento | Subidas y caídas |
| Antes y después | **Cortina:** una línea vertical barre y cambia el estado | Dos dibujos y un `clip()` cuyo borde se mueve | Transformaciones |
| Proceso con pasos | **Diagrama que se arma por etapas,** un paso por frase | Cada paso entra, se resalta y se atenúa al llegar el siguiente | Explicaciones |
| Cómo es algo por dentro | **Corte transversal** con capas | Formas con `clip()` de la silueta; las capas se llenan de abajo hacia arriba | Café, anatomía simple, máquinas |
| Dónde y por dónde | **Mapa con ruta** | Línea que se dibuja, alfiler que cae y una mini-escala | Viajes, distancias |
| Quién estaba dónde y cuándo | **Reconstrucción en planta** con fichas y reloj | Vista desde arriba; las fichas siguen trayectorias `f(t)`; reloj sincronizado | Investigaciones |
| Hechos simultáneos | **Pantalla dividida** con un solo reloj | 2–3 zonas con `clip()` | "Mientras tanto…" |
| Una lista | **Tablero que se llena** | Tablero fijo; cada ítem se clava cuando se nombra | Enumeraciones `[TAO]` |
| Dinero que se mueve | **Flujo:** fichas o billetes que viajan de A a B | Partículas por una curva; el grosor muestra la cantidad | Tratos, repartos |
| Proporciones | **Barra única partida** (no torta) | Un rectángulo dividido; las divisiones se animan | Recetas, porcentajes |
| Evidencia | **Documento anotado** | Hoja con texto simulado; un círculo o subrayado se dibuja a mano; etiqueta de fuente | Rabbit, MDM |
| Una idea abstracta | **Metáfora física:** balanza, puente que se rompe, reloj de arena | Pieza a medida | Una o dos por video |
| Escala humana | **Comparar con algo conocido** (una persona, una cancha, un edificio) | Silueta de referencia al lado | Tamaños y distancias |

### 7.3 Reglas de uso
1. **Un gráfico, una idea.** Si necesita leyenda larga, está mal elegido.
2. **Se arma delante del espectador,** nunca aparece completo.
3. **Vive dentro del mundo** cuando se puede (en la pizarra, en la pantalla del lugar, sobre la mesa), no flotando `[TAO]`.
4. **Ningún gráfico se repite igual** dentro del video `[TAO]`. Si vuelve, vuelve transformado desde el anterior.
5. **Mientras el gráfico se lee, nada más se mueve.**

---

## 8. Identidad visual por canal (largos)
Un lenguaje fuerte por canal, no cuatro estilos mezclados.

| | **Million Dollar Mistake** | **The Rabbit Loop** | **Dog / Cat Decoded** | **Coffee But Why?** |
|---|---|---|---|---|
| **Idea** | La sala del trato | El expediente | La casa, a la altura del animal | La barra, de cerca |
| **Color** | Verde oscuro, papel, oro | Azul noche, ámbar de lámpara, verde de radar | Día: crema, celeste, madera clara | Marrones cálidos, crema, cobre |
| **Luz** | Lámparas de escritorio, ventanas | Linterna, pantalla, luna | Sol por la ventana, que se mueve con la hora | Luz lateral cálida, vapor a contraluz |
| **Arquitectura** | Cuatro actos | Versiones enfrentadas | Escalera | Escalera |
| **Protagonista del cuadro** | El objeto del trato | La evidencia | El animal, grande | La bebida, en macro |
| **Gráfico firma** | Ficha del trato con la cifra tapada | Línea de tiempo maestra + tablero de casos | Etiquetas pegadas al cuerpo | Taza en corte con capas |
| **Transición firma** | Corte por forma sobre el objeto | Entrar a una foto o pantalla | El animal cruza y tapa el cuadro | El líquido llena el cuadro |
| **Sonido firma** | Sello y pluma | Clic de proyector y estática | Patas y collar | Vapor y taza |
| **Evitar** | Barras genéricas, neón | Personajes bajo un foco en el vacío; aliens afirmados | Fondo negro; humano de pie explicando | Persona de pie explicando; barras repetidas |

---

## 9. Sonido en el largo (lo mínimo)
- **Cada lugar tiene su ambiente** (cuarto, calle, mar) a volumen bajo: ayuda a sentir el cambio de espacio.
- **Cada imagen nueva suena** `[TAO]`.
- **La música cambia con los actos,** igual que el color.
- **Antes del pico, el sonido baja.** Probar primero si con voz IA no suena a falla (doc 14).
- **Nadie ha evaluado todavía el sonido de un largo completo.** La única revisión posible es el oído de Tao.

---

## 10. Sistema de producción y escala
### 10.1 Tres niveles de pieza
| Nivel | Qué es | Ejemplos | Se reutiliza |
|---|---|---|---|
| **Fichas del canal** | Colores, luz, tipografía, sonidos, transición firma | Tabla de la Parte 8 | En todos los videos del canal |
| **Piezas paramétricas** | Funciones que reciben datos y dibujan | `calendario(fecha)`, `sello(texto, color)`, `mapa(puntos, ruta)`, `unidades(n, icono)`, `corteTaza(capas)`, `lineaTiempo(años)`, `documento(resaltados)` | Entre videos y canales, con otro contenido y los colores del canal |
| **Piezas de autor** | Hechas para un video | La pantalla del GIMBAL, la balanza de Pixar | Poco; son el "toque propio" `[TAO]` |

**Regla de escala:** cada video nuevo deja **2–3 piezas paramétricas nuevas** en el banco. A los 10 videos, el banco tiene 30–40 piezas más y los videos salen más variados sin costar más.

### 10.2 Flujo con 3 puertas
| Etapa | Entregable | Aprueba |
|---|---|---|
| 1. Hechos | Hoja de hechos: dato, 2 fuentes, certeza | Claude |
| 2. **Empaque** | 3 títulos + 3 ideas de miniatura + la promesa. El dato clave queda "embargado" | **Tao** |
| 3. Arquitectura | Lista de momentos (con "pero / por lo tanto"), libro de preguntas, tipo de arquitectura | Claude |
| 4. Guion | 1.700–1.900 palabras, leído "como espectador aburrido" | — |
| 5. Mapa visual | Tabla por capítulo: lugar, estado, color, gráfico, recurso nuevo. Guion de color en una tira | — |
| 6. Guion visual parcial | Plano por plano **solo de los primeros 30 s y de 5 momentos marcados** | — |
| 7. Construcción | Piezas nuevas + armado automático | — |
| 8. **Hoja de planos** + revisión automática | Un cuadro por plano | **Tao** |
| 9. **Render** | Video, descripción, capítulos, 3 títulos y 3 miniaturas | **Tao** |

### 10.3 Presupuesto de tiempo
| Nivel | Tiempo | Qué incluye |
|---|---|---|
| **Estándar** | ~3 h | Arquitectura + armado automático con el banco del canal + primeros 30 s a mano + 5 momentos marcados |
| **Insignia** | ~5–6 h | Lo anterior + 8–10 piezas de autor + guion de color completo |

Cuál se usa y con qué frecuencia lo decide Tao. No hay evidencia de que el nivel insignia retenga más.

### 10.4 Qué se automatiza (una vez)
- Voz estándar por canal.
- Colores y luz del canal.
- Chequeos: textos encimados, franja de subtítulos, dato clave en los primeros 30 s, pregunta en la voz, planos de más de 4,5 s.
- Informe de variedad: composiciones por minuto, lugares, regresos sin cambio.
- Trayectoria de la mirada entre cortes.

---

## 11. Medición de los largos
- **Qué mira YouTube en el informe de retención `[EXT, oficial]`:**
  - la **intro**: el porcentaje que sigue mirando pasados los primeros 30 s;
  - los **picos** (partes que se vuelven a ver o se comparten) y las **caídas** (donde la gente se va o salta);
  - la **retención típica**: compara con tus últimos 10 videos de largo parecido.
- **Comparar solo contra videos de duración parecida.** El porcentaje visto depende mucho de la duración, y por eso un estudio de 5,3 millones de videos propone una medida calibrada por duración `[EXT]` (Wu y colegas).
- **Leer a los 28 días, no a las 24 horas** (ya está en nuestras reglas).
- **Un cambio por video.** Sin eso no se sabe qué funcionó.
- **Qué se anota de cada largo:** tipo de arquitectura, duración, palabras por minuto, lugares, composiciones por minuto, % a los 30 s, retención al 25/50/75 %, dónde están las 3 caídas más grandes y qué había en pantalla.
- **Hoy no hay ningún largo con datos.** El primer paso sigue siendo publicar (doc 14).

---

## 12. Lista de comprobación
**Antes del guion**
- [ ] Tipo de video y arquitectura elegidos.
- [ ] Empaque aprobado; dato clave embargado.
- [ ] Lista de momentos unida con "pero / por lo tanto".
- [ ] Libro de preguntas: una mayor y menores encadenadas; todas se cierran.

**Antes de construir**
- [ ] Mapa visual: un lugar por capítulo, con su estado y su color.
- [ ] Guion de color en una tira; un solo acento.
- [ ] Cada acto estrena un lugar, un gráfico y un recurso.
- [ ] Los primeros 30 s y 5 momentos, plano por plano.
- [ ] Cada gráfico: una idea, forma congruente, se arma por pasos.

**Antes del render**
- [ ] Hoja de planos aprobada por Tao.
- [ ] El tema es protagonista en la mayoría de los planos.
- [ ] Ningún regreso a un lugar sin cambio de estado.
- [ ] Cada plano: un punto de atención y 2 de los 5 movimientos.
- [ ] Revisión automática sin avisos.
- [ ] El final es una imagen, no una plantilla.

## 13. Reglas duras (no se negocian)
1. Todo dato con 2 fuentes; sin política; sin caras reales, logos ni personajes con derechos.
2. Una recreación de un testimonio o de una hipótesis se rotula como tal.
3. Título, miniatura, descripción, capítulos y primeros 30 s no revelan el dato clave.
4. Nada sobre los subtítulos; ningún texto encima de otro.
5. Ningún plano de más de 4,5 s.
6. Sin preguntas directas en la voz.
7. Cuerpo natural; los personajes entran desde fuera del cuadro.
8. Hoja de planos y OK de Tao antes del render; nunca dos renders a la vez.
9. Se avisa antes de cambiar el código del motor.

---

## Fuentes
- Ira Glass, los ladrillos del relato: https://jeffwerner.ca/?p=445 · https://ethos3.com/?p=7022
- Estructura de actos en televisión: https://fiveable.me/tv-writing/unit-5/cliffhangers-hooks/study-guide/eDEGKp0N9glftkLe · https://fiveable.me/tv-writing/unit-4/pacing-rhythm/study-guide/A3UvieGSWvPuIinV
- Errol Morris, *The Thin Blue Line*: https://www.slantmagazine.com/dvd/the-thin-blue-line/ · https://www.deepfocusreview.com/definitives/the-thin-blue-line/
- Forensic Architecture: https://mubi.com/notebook/posts/remains-to-be-seen-the-video-work-of-forensic-architecture · https://forensic-architecture.org/methodology/situated-testimony
- Walter Murch, regla de seis: https://wikis.utexas.edu/display/rtf318/Murch%27s+Rule+of+Six
- Tony Zhou sobre Kurosawa: https://theplaylist.net/watch-video-essay-akira-kurosawa-composing-movement-20150324
- Guion de color (Pixar): https://www.moma.org/audio/playlist/192/2575 · https://www.studiobinder.com/blog/what-is-a-color-script-definition/
- Cámara multiplano: https://en.wikipedia.org/wiki/Multiplane_camera
- Doce principios de la animación: https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation
- Animación limitada: https://en.wikipedia.org/wiki/Limited_animation · https://pixune.com/blog/what-is-limited-animation/
- 3Blue1Brown y Manim: https://www.3blue1brown.com/lessons/manim-demo/
- Narración con el entorno (Don Carson): https://www.gamedeveloper.com/design/environmental-storytelling-creating-immersive-3d-worlds-using-lessons-learned-from-the-theme-park-industry
- Tversky, Morrison y Betrancourt, "Animation: can it facilitate?": https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf
- Heer y Robertson, transiciones animadas: https://idl.uw.edu/papers/animated-transitions
- Segel y Heer, visualización narrativa: https://idl.uw.edu/papers/narrative
- Cleveland y McGill, percepción gráfica: https://vis.arc.vt.edu/%7Enpolys/projects/safas/science.pdf
- Isotype: https://isotyperevisited.org/2012/08/introduction.php · crítica: https://journals.uc.edu/index.php/vl/article/view/5954
- Mayer, principios multimedia: https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf
- Zacks y colegas, límites de eventos: https://pmc.ncbi.nlm.nih.gov/articles/PMC5734104 · https://link.springer.com/article/10.1186/s41235-016-0043-2
- Cutting, ritmo del cine: https://link.springer.com/10.1186/s41235-016-0029-0
- Smith, Levin y Cutting, atención al ver cine: https://ualresearchonline.arts.ac.uk/id/eprint/21182/2/cf891501-bc1c-4904-bcee-5170766e6e53.pdf
- Fredrickson y Kahneman, pico y final: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/fredr-kahneman-jpsp1993.pdf
- Ayuda de YouTube, retención: https://support.google.com/youtube/answer/9314415
- Wu, Rizoiu y Xie, "Beyond Views": https://arxiv.org/abs/1709.02541
