# 01 · Principios

> Las frases en cursiva son de Tao, tal como las dijo en el chat. Son la base de todo lo demás.

## P1. La variación es la retención
- *"La clave no es todos, sino el ir variando… La variación para la retención. Todos los patrones generalmente se sienten detectables… si repetimos siempre 3 cosas, se va a notar."*
- **Qué significa en la práctica:**
  - variar **tipo de plano, espacio, objeto, entrada y salida** de los personajes, transición y estilo de cifra;
  - nada de alternancias mecánicas (medio-primer-medio-primer): el espectador las detecta.
- **Cómo se revisa:** `hoja_planos.py`. Si en la hoja se ven 3 cuadros seguidos "parecidos", hay que cambiar.

## P2. Siempre pasa algo
- *"Si hay una pantalla que se queda quieta, da ganas de salir del video. Se siente lento… que siempre estén ocurriendo cosas, que sean sutiles, o que si la escena se queda harto tiempo, tenga que ver con lo que se está diciendo."*
- **Cada plano se mueve:** acerca, aleja, se desliza o cámara en mano suave.
- **Algo vivo en el cuadro:** gente al fondo, luces, pantallas, humo, partículas o un objeto que cae.
- **Si una toma tiene que durar** (una cifra, una lista), lo que se mueve es **el contenido de lo que se dice**: aparece la polaroid nombrada, se inclina la balanza o el gráfico se dibuja.

## P3. Lo que se dice, se ve
- *"Cuando menciona las 4 cosas que se necesitan, podría haber una pantalla que las muestre."*
- Cada frase tiene su imagen: **objeto protagonista**, gráfico explicativo, gesto del personaje o espacio nuevo.
- **No basta con "fondo + personaje"** (*"mucho fondo y personaje… que los objetos sean protagonistas, como el computador"*).

## P4. No repetir, salvo que la repetición cuente algo
- *"Tratar de no repetir escenas, a menos que sea muy pocas veces. Yo diría 5 máximo a lo largo del video."*
- *"Que hubiesen más planos y se repitiesen menos. A menos que hayan interacciones y acciones dentro de esos planos: zoom in o zoom out, elementos que se mueven, personajes que ingresan o salen, texto, interacciones."*
- **Lectura que aplico (la más estricta):** en todo el video hay **como máximo 5 regresos** a espacios ya vistos, sumando todos. Si Tao quería decir "5 por espacio", la regla igual se cumple.
- **Insertos:** una vez cada uno. Solo se repiten como **regreso a propósito** (callback), y eso se marca en el guion.
- **Tipos de plano:** pueden volver (son la gramática del video), pero nunca dos iguales seguidos, y solo si traen una acción nueva.

## P5. Cada parte de la historia ocurre en un espacio distinto
- *"La idea es que todo ocurra en distintos espacios, porque así son las historias."*
- Cada capítulo tiene **su lugar**, y los lugares cambian con la historia: laboratorio → despacho → cine → sala de prensa.
- También vale salir del escenario: insertos y escenas cortas fuera de los sets (*"que hayan distintas escenas fuera de esos escenarios"*).

## P6. Dimensión y detalle
- *"De cerca, de lado… darle más dimensión… con más detalle en la ropa, en los rostros, con más movimiento."*
- Primeros planos, planos de lado e inclinados, sobre el hombro, a través de objetos, y fondo desenfocado.
- Personajes con detalle: ropa con pliegues, caras expresivas, parpadeo, gestos y luz del set encima.

## P7. Fluidez
- *"La idea es que sean transiciones fluidas."* Nada abrupto.
- Entradas desde fuera del cuadro y caminando, y la cámara se acerca cuando el personaje llega.
- Las salidas de un inserto caen en **pausas de la voz**.

## P8. Limpieza
- *"Que no se superpongan los textos, que no haya algo cerca de los subtítulos."*
- Se revisa automáticamente (`revisar_largo.py`). Es lo que más corrigió Tao a ojo.

## P9. Un toque propio por video
- *"Los videos son diversos. No es como que si yo hago otro se parezca… quizás no es la idea hacer una regla general, pero sí hacer algo que por video se adapte al contenido y que le dé un toque especial."*
- **Cada video lleva 1–2 recursos visuales que nacen de su tema** y no se reutilizan en otro video. Ejemplos:
  - **Pixar:** tablero de corcho con las 4 polaroids, balanza $5M contra ???, efecto Génesis en la TV.
  - **Navy (Rabbit):** la "pantalla del piloto", distinta para cada video.
- Los recursos de un video **no se cuelan en otro**: los sets propios de Pixar (cinta de la bolsa "PIXR", vitrinas del museo) salieron en el de Coca-Cola y hubo que cambiarlos.

## P10. Verdad y suspenso
- Todo dato con **2 fuentes o más**. Lo polémico tiene que estar respaldado. Sin política.
- **No revelar el pago antes de tiempo:** ni en el intro, ni en el título, ni en la portada, ni en los capítulos.

## P11. Aprender de lo que funciona
- *"No se trata de siempre hacer lo mismo, sino de usar lo que funciona."*
- Se mide por tipo de video y de título (Test & Compare) y se anota qué gana en el proyecto.
