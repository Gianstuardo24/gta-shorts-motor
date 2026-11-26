# 05 · Textos y subtítulos

## La franja de subtítulos es sagrada
- **Nada entra en la franja de subtítulos** (arriba del cuadro): ni caras, ni la parte alta de objetos (etiquetas, precios, carteles), ni letreros del set.
- **Cómo se cuida:**
  - `planos_tiempo.libre_arriba()`: si un objeto alto subiría a la franja, baja el encuadre o abre el plano;
  - altura de cámara de los planos de personaje (la cabeza no toca);
  - los carteles que caen (FOR SALE) caen desde más abajo;
  - **franja oscura suave** detrás de los subtítulos para que se lean sobre fondos cargados;
  - `revisar_largo.py` mide los bordes detrás de cada letra y avisa.
- **Subtítulos:** máximo 2 líneas. Si no cabe, la frase sale en 2 partes seguidas.

## Ningún texto encima de otro
- *"Mira eso que dice THE DREAM… se superpone a otro texto… no superposiciones en textos."*
- **Etiquetas y chips** van **abajo a la izquierda, estilo noticiero** (`chipDoc` con x=-585, y=1262 y 1352).
- **Los letreros propios del set** (pantalla de cine, cartel de premios, letrero de servidores, cinta de la bolsa) **se apagan** cuando aparece una etiqueta (`window.__HT`).
- **En los insertos no salen etiquetas** ni cifras del HUD.
- **Los textos dentro de un inserto se ajustan a su ancho** (como las leyendas de las polaroids).
- **Revisar en la hoja de planos** que no haya 2 textos a la vez en la misma zona.

## Cifras y títulos grandes
- **Más grandes o distintos** que una etiqueta común (Tao: *"textos más grandes o distintos"*).
- **Estilos que se alternan:** 3 estilos de cifra sin caja, cifras 3D y billetes. Nunca la misma cifra con el mismo look en todo el video.
- **Duración:** ~5–6 s y nunca más de 6 s. Mientras están, el plano es general o recorrido (sin zoom que tape caras) y ningún corte afuera las tapa.
- **Título grande:** centrado arriba del medio (y≈470), sin chocar con subtítulos.
- **Tablero de aletas (tableroH):** máximo 6,5 s, filas de 14 caracteres o menos, solo A–Z, 0–9 y $.

## Marcas y caras
- **Sin logos ni marcas reales en pantalla:** diarios, empresas y productos genéricos. El nombre puede decirse en la voz.
- **Sin caras reales** ni personajes con derechos (tampoco en miniaturas).
- **Formas protegidas:** se evitan las botellas o envases icónicos (la botella de contorno de Coca-Cola se cambió por una recta).

## Textos en pantalla de los Shorts (Tao, 24-nov 23:05–23:27)
- **Nada de píldoras ni marcos** para títulos, cifras, fichas o letreros.
- **Estilo como el STOP:** texto suelto, blanco o del color del canal, con **brillo suave**; **sin borde negro**, **sin subrayados ni barritas**.
- **Fechas** en una hoja de calendario; **cifras** grandes y sueltas que cuentan hasta el valor.
- **No amontonar:** subtítulo + un título + un dato como máximo a la vez; si hay objeto con texto, el título se va antes.
- **Palabras difíciles se muestran en dibujo** (soaked → estanque con la cafeína saliendo); "a la mitad" → medidor con la marca HALF, centrado.
- **Emojis** que saltan, al centro de la pantalla.
