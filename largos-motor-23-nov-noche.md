# Largos — cambios del motor y videos del 23-nov (noche)

> Complementa `claude/largos-planos-23-nov.md` (cómo se arman los planos). Aquí: lo que se cambió después del feedback de Tao en Pixar y lo que se aprendió armando 5 largos seguidos.

## 1. Cambios pedidos por Tao en Pixar (aplican a todos los largos)
- **Entradas fuera de cuadro:** si en el guion un personaje entra caminando pero parte dentro del cuadro (como Lasseter en Pixar), `planos_tiempo.py` lo mueve a 230 px **fuera del borde** más cercano y ajusta la duración del paso.
- **Transiciones más suaves:** nuevo **`fundido`** a negro de ~0,8 s (en `planos.js`, función `transH`). Se sacaron el barrido rápido y el iris.
  - Entre escenarios: desliza / fundido / luz.
  - Insertos: seco / fundido / luz.
- **Tableros (`tableroH`):** ahora duran hasta **6,5 s** (`recortar_insertos.py`), para que se alcancen a leer. Cada fila debe tener **≤14 caracteres** y solo A-Z, 0-9 y $ (si no, el efecto de letras no termina de girar).
- **Insertos por video (`g["cortes_no"]`):** lista de insertos que no calzan con ese tema (ej. Coca-Cola sin contrato roto ni claqueta).
- **`bolsaH` tiene el ticker de Pixar** por defecto: no usarlo en otros videos sin pasarle `ticker`.
- **Insertos automáticos por canal (`CORTES_CANAL`):** la tabla de insertos nació con MDM (claqueta, guion, teclado…) y en otros temas se veía mal (una claqueta por "a short video", un teléfono en el caso del autopsia).
  - Rabbit: solo lupa, sello, papeles y edificio.
  - Perros / Gatos / Café: solo lupa.
  - MDM: todos.
  - "sign" ya no dispara el inserto de papeles ("no sign of an engine").
- **Pistas de plano (`L.hints`):** no estaban llegando al armado de planos. Ahora el `b.py` debe agregar `g["escena"]["escenas"][0]["planos_hint"]=L.hints` antes de guardar. Sirve para forzar un plano general cuando algo importante pasa en el cielo (luces, OVNI).
- **Objeto en la mano (`"objeto":"documento"` con `ofrece`):** tapa la cara en los primeros planos. Mejor que el documento **caiga como objeto** a un lado.

## 2. Escenarios y objetos nuevos
| Nombre | Qué es | Para |
|---|---|---|
| `desierto` | Noche, mesetas, cactus saguaro, estrellas, luna | Roswell, Phoenix, Área 51 |
| `guerra42` | Ciudad a oscuras con reflectores que barren el cielo y postes de luz | Batalla de Los Ángeles 1942, ataques aéreos |
| `vLuces` (objeto) | 7 luces en formación de V que laten | Phoenix Lights y similares |

- `trianguloP` **no es un OVNI**: es el triángulo de espuma de los Shorts de café.
- `botella1899` en horizontal va con escala ~0,35–0,45 (si no, queda más alta que un personaje).
- `comparaBarras` en horizontal: escala ~0,46, y=1640, `dec=0` y `suf` con la unidad (por defecto pone " M" de millones). Forzar plano general con `L.hints` mientras está en pantalla.

## 3. Largos hechos esta noche
| Canal | Video | Duración | Ángulo del banco |
|---|---|---|---|
| Rabbit | The Navy's UFO Videos: What They Really Show | 8:20 | R4 + R5 |
| Dogs Decoder | Your Dog Is Telling You Something (8 señales) | 6:33 | P2 |
| Rabbit | 5 Famous UFO Cases, Finally Solved | 9:46 | R4 |
| MDM | Why Coca-Cola Sold Its Bottles for $1 | 6:25 | M1 / M4 |
| Café | Every Coffee Drink, Explained | 5:42 | C1 / C2 |

**Tiempo real medido:** guion nuevo ~25–35 min; voz 5–9 min; revisión de hoja y arreglos ~15–20 min; render ~15–25 min (2 CPU). Con varias en cadena se solapan: voz de una mientras se renderiza otra.

**Dónde quedaron (Estudio):** cada uno en `Nuevos Largos` de su canal (`TheRabbitLoop`, `DogDecoded`, `ChiChibitsTV`, `MillionDollarMistake`), con `.txt`, `.portada.jpg` (miniatura A), miniatura B y `Test & Compare - ….txt` con 2 títulos alternativos.

**Miniaturas:** fondo hecho en ChatGPT (estilo vector, sin texto ni logos) + texto con `miniatura_largo.py` y el logo del canal (`--logo`). Ojo: en bash, `"$1"` se borra; usar comillas simples para textos con `$`. En Coca-Cola se usó una **botella recta genérica**: la botella con curvas es diseño protegido de la marca.

**Revisión nueva antes de renderizar (`revisar_insertos.py datos.json`):** un inserto que termina **después** de que cambia el tramo vuelve a la escena anterior por un instante (pasó en Coca-Cola, con la balanza al final de un tramo). Regla: el inserto debe terminar **≥1,2 s antes** de la última palabra del tramo.

**Sets con texto de Pixar por defecto (no usar en otros temas sin pasarles opciones):** `bolsaH` (ticker PIXR), `museoH` (vitrinas con computador, rollo, Óscar y placas 1986 · $5M / 2006 · $7.4B), `mesaCenital` (LUCASFILM / PIXAR). Coca-Cola se tuvo que renderizar de nuevo por esto.
