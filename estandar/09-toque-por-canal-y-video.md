# 09 · Toque por canal y por video

## Diagnóstico de los 5 largos del 23-nov (contra este estándar)
| Video | Duración | Espacios usados | Insertos permitidos | Problema principal |
|---|---|---|---|---|
| rab1 · Navy videos | 8:20 | 19 tramos en **5** espacios (cielo ×7, oficina ×5, cabina ×4) | 4 (lupa, sello, papeles, edificio) | Pantallas iguales, escenas largas, casi sin insertos |
| rab2 · 5 casos OVNI | 9:46 | desierto ×5 (Phoenix **y** Roswell), oficina ×4 | 4 | Dos casos en el mismo desierto, pocos recursos por caso |
| dog1 · 8 señales | 6:33 | sala ×8, calle ×4, estudio ×2 | 1 (lupa) | Casi todo en el living |
| caf1 · 10 bebidas | 5:42 | **cafe ×13** (un solo espacio) | 1 (lupa) | Todo el video en el mismo café |
| mdm2 · Coca-Cola $1 | 6:25 | casona ×4, despacho ×3, reunión ×3 | MDM completo | El que más se acerca; le falta toque propio |

**Además, todos llevan la apertura vieja** (mundo de GTA de fondo los primeros ~0,6 s). Se arregló en el motor, pero hay que volver a renderizarlos.

**La causa común:** el banco de insertos y de sets se hizo para MDM. Los otros canales casi no tienen insertos (`CORTES_CANAL`), así que el armado automático se queda en el escenario. **Hay que darle a cada canal su propio banco.**

## Banco por canal (insertos y espacios a construir)
| Canal | Insertos propios | Espacios propios |
|---|---|---|
| **Rabbit Loop** (misterio, OVNI, ciencia) | pantalla IR (variantes), radar, diario genérico, expediente con sello y tachones, mapa con alfiler, diagrama animado, focos y antiaéreos, bengalas, globos, foto que se revela, TV de época | cubierta de portaaviones, sala de radar, cabina vista de lado, redacción de noche, sala de prensa, laboratorio de análisis, archivo, rancho, barrio de noche, sierra |
| **Dog/Cat Decoded** | repetición en cámara lenta con flechas, "visión de perro/gato" (filtro), oreja con ondas de sonido, corte del ojo, reloj, plato, correa, cama | living, parque, veterinaria, dormitorio, baño, cocina, puerta de entrada, auto |
| **Coffee But Why?** | taza en corte por capas con proporciones, molino, gotas de extracción, vaporizador de leche, termómetro, grano por dentro | barra italiana de pie, terraza, café moderno, cocina de casa, tostaduría, finca de café |
| **MDM** | ya tiene ~25 (ver `04`) | cada video suma 1–2 sets de época propios |

## Propuesta creativa por video

### rab1 · Navy videos — toque: **"la pantalla del piloto"**
Cada video de la Armada se muestra en **su propia pantalla recreada** (genérica, no el video real), y cada una es distinta y cuenta su caso:
| Pantalla | Cómo se ve | Qué explica |
|---|---|---|
| **FLIR1 / Tic Tac (2004)** | blanco-caliente, mancha ovalada con retícula que sale disparada por la izquierda | lo que vio la cámara |
| **GIMBAL (2015)** | gris oscuro, destello con aletas que **gira mientras el horizonte se inclina** | el debate: ¿gira el objeto o la cámara? |
| **GOFAST (2015)** | olas grises pasando rápido, punto chico, cifras de altura y distancia | por qué parece rápido y no lo es |

**Espacios por capítulo** (9 distintos, máximo 5 regresos):
1. *Three videos:* las 3 pantallas en un muro oscuro, cada una con lo suyo (gancho).
2. *2004: the Tic Tac:* cubierta del portaaviones al amanecer → sala de radar con puntos que bajan → cabina vista de lado (casco y reflejo en el visor) → mar visto desde arriba.
3. *2015:* cabina de otro avión (costa este) → pantallas GIMBAL y GOFAST.
4. *2017: the world finds out:* redacción de noche + portada de diario genérico que gira.
5. *The Pentagon confirms:* sala de prensa (podio y banderas sin escudo) + expediente con sello RELEASED.
6. *GOFAST: case closed:* **diagrama de paralaje animado** (avión, línea de visión, el objeto mucho más abajo de lo que parece), con las cifras ya verificadas del guion.
7. *GIMBAL: still debated:* laboratorio con **pantalla dividida**: "gira el objeto" contra "gira la cámara".
8. *The Tic Tac: still open:* mar de noche + expediente sin sello (OPEN).
9. *What the government says:* archivo con cajones de reportes.
10. *How to read a UFO video:* pizarra con 3 trucos animados (paralaje, destello, distancia).
11. *The scorecard:* tablero de aletas (ya existe).

**Jugar con los aliens (sin mentir):** en los momentos de "lo que la gente pensó", un platillo y un alien **de diseño propio** aparecen en el cielo estilizados, como en una película vieja. Cuando llega la explicación, se desarman en lo que era (destello, ave, globo). Así hay aliens en pantalla sin afirmar que lo eran.

### rab2 · 5 casos — toque: **"el expediente que se cierra (o no)"**
- Cada caso **abre con su carpeta** (#5 … #1) y **cierra con un sello** que se estampa (SOLVED / PARTLY / OPEN, según el guion). El marcador final se va llenando caso a caso.
- Cada caso tiene sus espacios y su recurso propio:
| Caso | Espacios | Recurso propio |
|---|---|---|
| #5 Washington 1952 | sala de radar del aeropuerto de noche → sala de prensa de 1952 (flashes, micrófonos antiguos) | **diagrama de inversión térmica**: la capa de aire caliente dobla el haz del radar |
| #4 Phoenix 1997 | patio de barrio de noche con vecinos mirando arriba → sierra al sur de la ciudad | **V de luces** sobre la cuadrícula de la ciudad; después, **bengalas que bajan lento y se esconden tras la sierra**, con reloj 8:30 PM / 10:00 PM (dos eventos distintos) |
| #3 Los Ángeles 1942 | ciudad en apagón → despacho de 1942 | **focos que barren el cielo + destellos antiaéreos + sirena** |
| #2 Autopsia alien 1995 | living de 1995 con TV de tubo → taller del escultor (moldes y arcilla, nada gráfico) | **película granulada en blanco y negro** que se revela como montaje, con sello RECONSTRUCTION |
| #1 Roswell 1947 | rancho de día (molino, cerca, restos de papel de aluminio y varillas) → campo de lanzamiento al amanecer | **tren de globos Mogul** subiendo (largo, con reflectores de radar) |
- **Intro y marcador:** en el archivo, con las 5 carpetas sobre la mesa.
- El desierto queda solo para un caso.

### dog1 · 8 señales — toque: **"el decodificador"**
- Cada señal tiene una **repetición en cámara lenta** del gesto, con flechas de movimiento, y una tarjeta "LO QUE SIGNIFICA".
- **"Visión de perro":** el mismo plano con el filtro de color que ven los perros (azul-amarillo), usado una vez, en el momento que calce.
- **Espacios distintos por señal:** living (inclinar la cabeza), parque (cola), cocina (ojos de cachorro), sofá (mirada larga), dormitorio (dónde duerme), baño y pasillo (zoomies), pasto (reverencia de juego), cama (bostezo).
- **El porqué en imagen:** cada causa que explica el guion tiene su inserto (la oreja con ondas de sonido, la energía que se acumula como una barra que se llena, etc.).

### caf1 · 10 bebidas — toque: **"la taza en corte"**
- Cada bebida se arma **por capas** en una taza transparente en corte (espresso, agua, leche, espuma), con proporciones marcadas. La taza cambia de forma según la bebida.
- **Un espacio por bebida o grupo:** barra de pie (espresso, ristretto, lungo), terraza (cortado), café moderno (flat white, latte), cocina de casa (americano), chocolatería (mocha), cocina con frasco (cold brew). Ningún origen geográfico se afirma sin verificar.
- **Cafeína:** la comparación de mg ya verificada (Mayo Clinic) como balanza o barras dentro del mundo.

### mdm2 · Coca-Cola $1 — toque: **"el color del tiempo"**
- La historia empieza en **sepia en 1899** y **va ganando color** a medida que avanza, hasta el color pleno de hoy.
- **Espacios:** fuente de soda de farmacia → despacho de 1899 (la firma) → embotelladora con cinta → almacén de pueblo → sala de directorio → hoy. La casona queda con máximo 2 regresos.

## Títulos nuevos para el video de 5 casos (pedido de Tao: que planteen si están resueltos)
| Título | Molde | Fricción |
|---|---|---|
| ⭐ **Were These UFO Cases Really Solved?** | pregunta corta de molde famoso ("Was X Just Lucky?") | ¿y si no? |
| **5 "Solved" UFO Cases** | las comillas dudan de la palabra | ¿por qué entre comillas? |
| **Case Closed? 5 Famous UFO Mysteries** | "Case Closed" es el nombre real del informe de 1997 sobre Roswell | ¿cerrado de verdad? |
| **The UFO Cases They Say Are Closed** | "They say" | ¿quién lo dice? |

Para Test & Compare: las 3 primeras. El video responde la pregunta, así que el título no promete algo falso.
