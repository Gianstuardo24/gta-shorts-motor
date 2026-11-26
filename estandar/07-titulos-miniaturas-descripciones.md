# 07 · Títulos, miniaturas y descripciones

> Detalle y bancos completos: `claude/mdm-tops-23-nov.md` y `claude/mdm-miniaturas-23-nov.md`.

## Regla de fricción (la principal)
- *"La idea no es revelar info en portada o título, sino generar una fricción en el espectador, la duda… la urgencia de no querer perderse algo."*
- **Ni el título ni la portada revelan el dato clave** (cuánto, quién, cómo termina).
- **Se complementan:** el título promete y la portada muestra el objeto; no repiten la misma frase.
- **La urgencia sale de la curiosidad**, nunca de urgencia falsa ("antes de que lo borren", cuentas regresivas).

## Cómo escribir el título
- **Basado en moldes famosos** que ya funcionan (*"guíate en los títulos famosos"*):
  - *The Worst Deal in [X] History*;
  - *The Man Who Sold [X]*;
  - *How [A] Destroyed [B]*;
  - *The Decline of X… What Happened?*;
  - *Why Nobody [hace X] Anymore*;
  - *Was [X] Just Lucky?*
- **Que se entienda a la primera, sin rebuscar:** "con man" no se entiende; "George Lucas" no es tan llamativo como "Hollywood".
- **Corto:** ~5 palabras rinde mejor. Las preguntas solo funcionan en moldes cortos y famosos; en general rinden −18 %.
- **Polémico pero verdadero:** "worst" es opinión, así que se permite si la base es un hecho verificado.
- **Nombres que se buscan** (Musk, Steve Jobs, Apple, Disney): solo si son **protagonistas reales** del caso.
- **Alternar moldes** entre videos para que el canal no se vuelva repetitivo.
- **Test & Compare con 3 títulos:** uno con nombre famoso, uno polémico y uno con molde que esconde la respuesta. Se anota cuál gana.

## Miniaturas
1. **Fondo en ChatGPT** (navegador integrado, chat "Create Thumbnail Background"):
   - 16:9, sin texto, logos, personas ni caras;
   - render 3D cinematográfico con objetos originales;
   - colores del canal;
   - objeto en la mitad derecha y el 40 % izquierdo oscuro para el texto;
   - esquina inferior derecha libre (ahí va la duración).
2. **Componer** con `miniatura_largo.py` (fuente Anton y logo del canal):
   ```
   python3 miniatura_largo.py fondo.png salida.jpg 'LINEA 1|LINEA 2' --destacar 1 --lado izq --ancho 430 --logo assets/logo_xxx.png
   ```
   Usar comillas simples si el texto lleva `$`.
3. **Revisar en chico** (~360 px de ancho): se lee en 1 segundo.
4. **3 variantes (A/B/C)** para Test & Compare, cada una con otra duda ("$5M vs ???", "DON'T SELL THIS", "NOBODY WANTED IT").

## Descripción
- **Corta**, sin revelar el pago, con capítulos. Los nombres de capítulo tampoco revelan: "Disney pays $7.4 billion" pasó a "The Disney deal".
- **Fuentes** al final, **4–5 hashtags**.
- **Nunca** "VIDEO RELACIONADO" ni comentario fijado.

## Entrega en el Estudio
- **Carpeta:** `~/Desktop/YouTube/<canal>/Nuevos Largos/`.
- **Archivos:**
  - `MM-DD HHh - Título.mp4`;
  - `MM-DD HHh - Título.txt`, con TÍTULO y DESCRIPCIÓN en el formato del Estudio;
  - `MM-DD HHh - Título.portada.jpg`;
  - `Test & Compare - <tema>.txt`, con los 3 títulos y las 3 miniaturas.
- **Tao sube y activa Test & Compare.** No se publica sin su OK.

## Títulos y portadas que no revelan (Tao, 24-nov 20:20)
- **El título planta una duda; no entrega la respuesta.** Tampoco la portada: si el título esconde y la portada lo dice, se pierde.
- **Tema claro, respuesta escondida.** Se tiene que entender hacia dónde va, sin decirlo directo.
- **Variar un elemento por vez** para saber qué movió el resultado: cifra exacta / cifra aproximada ("menos de $1.000") / sin cifra ("casi nada").
- **Palancas que entran a la lista:** misterio ("percibe algo que tú no"), negación como desafío ("no bosteces frente a tu perro"), urgencia, miedo o seguridad sin explicitarlo, camino fácil.
- **Límite: esconder sí, mentir no.** Cada título pasa una prueba: *¿el video entrega lo que promete?* Si la promesa no se paga, no va. Para la urgencia se busca un hecho real que la sostenga (p. ej. Los Ángeles, 1942) en vez de afirmar un peligro que no existe.

| Revela (no) | Esconde (sí) |
|---|---|
| Your Dog Can Smell Your Stress | Your Dog Senses Something You Can't |
| Decaf Still Has Caffeine | Bad News If You Drink Decaf |
| Your Dog Catches Your Yawns | Don't Yawn in Front of Your Dog |
| Roswell Was Real. It Wasn't Aliens | What Really Fell at Roswell |
| Nike's Logo Cost Just $35 | The World's Most Famous Logo Cost Almost Nothing |

## Disparador emocional (Tao, 24-nov 20:43–20:56)
- **El título se escribe primero; el contenido después.** La primera frase del video sigue el disparador del título.
- **Cada título lleva un disparador emocional.** Si el texto no lo trae, lo pone el emoji.
- **Títulos cotidianos, cortos, de una frase.** Palabras fuertes: "lost" pega más que "sold"; "a bargain" más que "almost nothing".
- **Moldes aprobados por Tao:** "Don't Trust the ___ Story" · "Stop ___ing ___" · "Don't Do This in Front of Your ___" · "He Lost ___ in ___ Days" · "Your ___ Knows What You're Hiding".
- **Los dos videos de un canal en un día no repiten disparador.**

| Disparador | Ejemplo aprobado |
|---|---|
| Desconfianza | Don't Trust the Roswell Story 👽❓ |
| Alarma | Stop Drinking Decaf ❌☕😳 |
| Prohibición | Don't Do This in Front of Your Dog 🐶🚫 |
| Secreto que te toca | Your Dog Knows What You're Hiding 👻 |
| Pérdida | He Lost 10% of Apple in 12 Days 👎 |

**Emojis: dos tipos**
| Tipo | Qué hace | Estado |
|---|---|---|
| De emoción o prohibición (❌ 🚫 👎 😳) | Sube la intensidad sin afirmar otra cosa | Se usan |
| De pista no literal (👻 en perros) | Hace esperar algo distinto de lo que el video entrega | **En prueba**, pedida por Tao: medir permanencia y "me gusta" contra videos sin esa pista |

**Límite que se mantiene:** el video paga lo que el título promete. "Se sintió estafado" (Apple) se descartó porque Wayne dice que no se arrepiente.
