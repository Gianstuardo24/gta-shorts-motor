# 03 · Planos, cámara y personajes

> **Alcance (Tao, 24-nov):** todo lo de este documento vale para **Shorts y largos por igual**: variedad de tomas y dinamismo en todos los videos. El planificador de planos hoy solo existe en el motor de largos; llevarlo al motor de Shorts está pendiente. Mientras tanto, en Shorts se hace a mano: un encuadre distinto por frase (general, cara, objeto, detalle, recorrido), sin repetir dos seguidos.

## Ritmo
- **Encuadre nuevo cada ~2,5–3,5 s.** Tao pidió "3 o 4 segundos por encuadre" y aprobó la v9 a ~2,6 s.
- **Dónde se corta**, por prioridad: fin de frase > coma > entre palabras, o justo cuando aparece un objeto o un personaje cambia de acción (`planos_tiempo.py`).
- **Ningún plano en escenario dura más de 4,5 s**, y ninguno menos de 0,7 s (`revisar_largo.py` lo marca).
- **Tiempo fuera de los escenarios:** ~35–45 % (insertos y escenas cortas). En Pixar v8 era ~25 % y Tao dijo *"pasan mucho tiempo en las escenas"*.

## Los 16 tipos de plano
| Tipo | Qué es | Cuándo |
|---|---|---|
| General | todo el set | al llegar a un lugar nuevo o con cifra grande en pantalla |
| Recorrido | la cámara se desliza de lado, lento | cuando hay una cifra o un título que tiene que quedarse |
| Medio | de la cintura para arriba | lo normal al hablar de alguien |
| Primer plano | la cara | reacción o idea importante |
| Ojos | primerísimo primer plano | tensión o sorpresa |
| Zoom rápido | golpe a la cara con sacudida leve | palabra fuerte ("fired", "nobody") |
| Alejamiento | parte en la cara y se abre a todo el set | revelación del contexto |
| Paneo vertical | sube desde el objeto hasta la cara | conectar objeto y persona |
| De a dos | dos personajes | conversación o negociación |
| Sobre el hombro | nuca desenfocada del otro | uno le habla al otro |
| A través de | planta o marco de puerta desenfocado delante | espiar, intimidad |
| Inclinado (holandés) | cámara torcida | tensión o algo que sale mal |
| Objeto | la cámara va al objeto que aparece | cuando entra un objeto protagonista |
| Camina | el personaje cruza y la cámara lo sigue | movimiento, viaje, decisión |
| Cámara en mano | movimiento leve estilo documental | momentos de tensión |
| Manos (inserto) | teclado, teléfono, papeles, billetes | según la palabra que se dice |

**Reglas:**
- Nunca dos planos iguales seguidos, ni patrones alternos (medio-primer-medio).
- Lo ya usado pesa menos en la elección; un tipo vuelve solo con una acción nueva.
- **Cada plano se mueve:** acerca, aleja, se desliza o va en mano. Con más fuerza en ~40 % de los planos.
- **El personaje no es siempre "una persona parada en una escena"** (Tao): encuadre distinto, caminando, haciendo algo o solo sus manos.
- **Plano general obligado** mientras hay cifra grande, título grande o globo de diálogo, para no taparlos.
- **Encuadre con la cabeza lejos de los subtítulos:** la altura de la cámara ya lo cuida (medio y=1330, primer y=1265).

## Personajes que entran y salen
- **Desde fuera del cuadro:** si la primera acción de un personaje es caminar y empieza dentro del cuadro, se mueve a 230 px fuera (`planos_tiempo.py`, bloque FUERA).
- **Entradas caminando + zoom al llegar: de vez en cuando**, no con todos. Sobre todo cuando se presenta a alguien. Tao lo corrigió: *"no quiero que pase con todos los personajes, pero está bien de vez en cuando"*.
- **Salidas:** a veces un personaje se va caminando del cuadro.

## Gestos y poses
- **Gestos hacia el otro:** apunta, explica con las manos, ofrece o saluda, y el otro a veces reacciona. Si está solo, explica con las manos o apunta a un objeto del set.
- **Brazo de 2 partes (brazo + antebrazo, `brazoIK`):**
  - **Pensar:** el puño llega al mentón "como botón", con el **codo abajo** delante del pecho. Sin dedo en la mejilla y sin tapar la boca. Mirada hacia arriba y cabeza un poco inclinada.
  - **Aplaudir:** las manos se juntan **delante del pecho**, no detrás.
  - **Teléfono:** la mano llega a la oreja, con el codo hacia afuera (ahí se ve natural).
  - **Apuntar y ofrecer:** el brazo se estira hacia afuera; la mano nunca queda en la cara.
- **La mano siempre se dibuja delante de la cabeza** en las poses que la acercan a la cara.
- **Vida:** parpadeo, cabeza que se mueve un poco y un gesto de vez en cuando. Personajes de fondo como siluetas que cruzan.

## Profundidad e integración
- **Primer plano desenfocado en las esquinas** (planta, lámpara, escritorio, monitor, butacas, cordón de museo) con paralaje al pasar la cámara. Cada set define los suyos (`FRENTE`).
- **Fondo desenfocado** en los primeros planos (`desenfocarFondo`, versión rápida sin `ctx.filter`).
- **Luz del set sobre los personajes:** cálida en el despacho, fría en el laboratorio (`TINTE`).
- **Sombra de contacto doble** en los pies.

## Pendiente del motor
- Boca que se mueve, expresiones que cambian solas y más detalle de ropa y caras.
- Pasar detrás de los muebles.

## Planos en Shorts (desde el 24-nov)
- **Planificador:** `/home/claude/planos_shorts.py DIR ID`. Corre después de la voz y antes del render (`d24/uno2.sh`, cola `q2.sh`). Reemplaza los zooms escritos a mano.
- **Un encuadre por tramo de voz (1,6–2,9 s)**, sin repetir tipo seguido ni dentro de los últimos 3 planos.
- **13 tipos en vertical:** general, recorre, medio, primer plano, ojos, zoom rápido, aleja, acerca, vertical (del objeto a la cara), de a dos, inclinado, cámara en mano, objeto. Más: sigue al que camina, encuadre de burbuja y empuje lento en los insertos.
- **Aún no en Shorts:** sobre el hombro y "a través de" (necesitan la capa de primer plano desenfocado de los largos).
- **Reglas propias del vertical:** las cifras, títulos y chips van fuera del zoom, así que el plano solo cuida que la cabeza quede bajo esos textos; con burbuja se encuadra la burbuja entera; ningún personaje queda cortado a la mitad por el borde.
- **Motor `escena.html`:** se agregó inclinación (`r`) y cámara en mano (`mano`) al zoom de las escenas película. Respaldos: `escena.html.bak_24nov_planos`, `…_objetos`.
- **Caminar:** el motor solo camina con `"a":[x,y]` + `"dur"` en la key. La pose `camina` sola deja al personaje quieto y luego salta (error del 24-nov, corregido con `d24/post.py`).

| Medición (zona de la escena) | Tiempo casi quieto | Cambios de encuadre/min |
|---|---|---|
| Los 14 Shorts del 24-nov, a mano | 19–45 % (típico 27 %) | 22–36 |
| Con planificador (Café, Apple, Gatos) | 15 %, 7 %, 11 % | 33, 40, 37 |
| Descafeinado rehecho (planificador + detalle propio) | 9 % | 40 |
| Referencia: faceless destacados, largos (doc 23) | 2 % | — |

- **Detalle propio del tema (Tao):** además de los planos, cada video lleva objetos y momentos de su tema (café: taza, bolsas "DECAF"/"CAFFEINE", granos, máquina, de noche). Objetos nuevos en el motor: `bolsaCafe` (texto, sub, color), `granos` (n, color), `cafetera`.
- **No repetir escenas dentro de un video:** `d24/chk.py` lo avisa.

### Planificador v2 (24-nov, 21:30) — pedido de Tao: que no se repita la forma
- **Ninguna forma de plano se repite dentro del video** mientras queden formas sin usar. Formas: general, recorre, medio, primer, ojos, rápido, aleja, acerca, vertical, de a dos, inclinado, cámara en mano, objeto, manos, tercio, balanceo, alto, sigue al que camina, burbuja.
- **Cada detalle (inserto) lleva un movimiento distinto:** empuje, abre, sube, baja, deriva, inclina; y el **papel** se recorre de arriba abajo hasta el dato.
- **La cámara viaja** al encuadre nuevo (0,3 s) en vez de cortar en seco; los cortes a un detalle van con un **fundido corto**.
- **Perros y gatos pueden ser el sujeto** del plano (primer plano, ojos, de a dos).
- **Objetos vivos:** los que flotan se mecen; los protagonistas laten (`flota`, `mece`, `late`; lo pone `d24/post.py`).
- **Objetos nuevos en el motor:** `nariz`, `ojosPerro`, `senal`, `pinGPS`, `papel{titulo,dato,sello,filaDato}`, `candado{sacude}`, `barras2{a,b,suf}`, `claqueta{texto}`.
- **Referencia de Tao:** un Reel de 67 s con un solo corte: la cámara viaja de objeto en objeto y cada idea es un objeto numerado. Se copia el principio (cámara continua, objeto protagonista, partes numeradas); el acabado 3D no está al alcance del motor 2D.

| Los 7 del formato nuevo (24-nov) | Planos | Formas distintas | Tiempo casi quieto |
|---|---|---|---|
| Stop Drinking Decaf | 15 | 15 | 8 % |
| Don't Do This in Front of Your Dog | 12 | 11 | 11 % |
| Your Cat Has a GPS on You | 14 | 13 | 7 % |
| He Lost 10% of Apple in 12 Days | 15 | 15 | 14 % |
| Don't Trust the Roswell Story | 12 | 12 | 20 % |
| Nobody Can Open This Door in GTA 6 | 14 | 14 | 13 % |
| GTA 6 humilló a Hollywood | 14 | 14 | 13 % |

## Shorts desde el 24-nov noche (pedidos de Tao 22:54–23:28)
- **Planos de 4 a 6 s** (`planos_shorts.py`: objetivo 4,0–5,4 s); al cortar, **zoom de entrada y de salida** en vez de fundido a negro; viaje entre encuadres 0,5–0,8 s.
- **Menos escenas, más largas:** unas 6–7 por video, alternando objeto premium y persona haciendo algo.
- **Personaje `figuraPro`** (`"cuerpo":"pro"` en el guion): proporciones reales, rodilla, hombro, **codo que se dobla**, **manos delante de la cabeza**, pulgar, ropa por oficio (chaqueta con solapa y pañuelo, bata con faldón y bolsillo, delantal con costura), pliegues, botamanga, cordones, cara con iris, párpados, cejas y nariz. Hoja de control: `d24/hoja_poses.py` cada vez que se toque el cuerpo.
- **Las personas hacen algo:** poses `bebe`, `lee`, `explica`, `teclea`, `aplaude`; al **ofrecer o apuntar con un objeto**, el brazo va doblado y la mano adelante, no un palo estirado.
- **Escena "pro":** capa `acabadoPro` (rayos de luz, neblina al piso, polvo en la luz, grano, luz con dirección, primer término desenfocado, viñeta) y objetos `humo`, `neblina`, `lamparaPie`, `mesaCentro`, `mesaLab`.
