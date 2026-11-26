# 06 · Transiciones y sonido

## Transiciones
- **Cortes limpios:** la cámara salta de una vez, sin cuadros intermedios de otra parte del mundo. Era el "salto raro" del cheque y pasaba en todos los cortes; ya está arreglado en `escena_h.html`.
- **Mismo lugar:** si la escena sigue en el mismo set (como en "Back then"), la cámara **se desliza suave** (1,0 s), sin barrido.
- **Entre escenarios:** casi siempre deslizamiento rápido (~0,55 s) o **fundido suave** (curva smoothstep, 0,42 s).
  - Orden actual en `largo.py`: `TT = desliza, fundido, desliza, desliza, luz, desliza, fundido`.
- **Hacia y desde insertos:** corte seco, fundido o luz, alternados (`TI` y `TRD`).
- **Prohibido:** flash, papel, tinta, iris y barrido brusco. Tao: *"no me gusta la transición… muy, muy abrupta… la idea es que sean transiciones fluidas"*.
- **Entradas de personajes desde fuera del cuadro**, nunca "aparecer" en medio del set.
- **Inicio del video:** el primer set se arma sobre fondo neutro (sin el mundo de GTA).

## Sonido
- **Cada plano de afuera suena.** Los efectos están hechos con código (`escena/sintet_sfx.py`), sin material de terceros:
  - teclas;
  - timbre y teléfono que se descuelga;
  - claqueta y proyector;
  - dados;
  - billetes;
  - hoja y lápiz;
  - chinche en el corcho;
  - pitidos de computador;
  - ciudad de noche;
  - subida y bajada de tono;
  - tics de la línea de tiempo;
  - balanza;
  - aletas del tablero.
- **Momentos de la música:** subida de tensión (riser) justo antes de cada cifra grande y del lado ganador de la balanza; golpe suave en cada capítulo.
- **Lo que cae suena** al tocar el suelo.
- **Cada inserto nuevo necesita su sonido** (si no lo tiene, se agrega a `sintet_sfx.py` y a `SFXSET`).
- **Música por canal:**
  - MDM: piano o deep;
  - Rabbit: dark;
  - Café, Perros y Gatos: deep.
- **Control:** volumen medio y máximo con `volumedetect` antes de entregar. **Tao escucha los efectos nuevos la primera vez que salen.**

## Audio de los Shorts (25-nov)
- **Ningún efecto sobre la primera palabra de una escena:** el whoosh de cambio termina antes (−0,34 s) y va bajo.
- **Volumen con ganancia fija** + limitador suave; nada de normalización automática que suba y baje (se oye como "corte"). Compresor suave en la voz.
- **La música baja antes de cada frase** (0,22 s de anticipación).
- **Pausa entre frases:** márgenes 0,07 s al inicio y 0,08 s al final (antes 0,15 / 0,10).
- **Pausas estratégicas (Tao, 25-nov):** **0,37 s** después del gancho inicial, **antes y después del segundo gancho** y antes del CTA; **0,28 s** en el resto. En el guion: `"pausa_larga_antes": [1, i_gancho2, i_gancho2+1, i_cta]` (por defecto [1, última]).
- **Primera palabra audible:** la voz sintética dice muy bajo palabras cortas al inicio ("To", "But"); `voz_local.arranque()` las sube hasta +14 dB solo donde hay voz.
