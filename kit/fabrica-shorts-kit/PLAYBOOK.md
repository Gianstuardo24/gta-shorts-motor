# PLAYBOOK · Cómo hacer Shorts que funcionan

> Lo aprendido haciendo y midiendo varios canales de Shorts a la vez: gaming, misterio, historia de negocios, café, perros y gatos.
> Son **reglas de partida**. Tus propios datos (el reporte semanal) mandan sobre ellas cuando los tengas.

---

## 1. Estrategia del canal

**Un micronicho por canal.**
- YouTube le muestra tu video nuevo a quien vio el anterior. Si cambias de tema, esa gente no hace clic y el canal "vuelve a cero".
- Elige **un ángulo específico**, no un tema general:
  - ❌ "datos de perros"
  - ✅ "por qué tu perro hace eso, explicado con ciencia"
- Repite la **misma fórmula** de título, gancho y gráfica hasta agotarla.

**Fórmula de título fija por micronicho.** Ejemplos que usamos:

| Micronicho | Fórmula |
|---|---|
| Conducta animal | "Why Your Dog ___" |
| Mecánicas ocultas de un juego | "[Juego] Has a Secret ___" |
| Historia de negocios | "He Sold It for $X. Today It's Worth $Y" |
| Casos de misterio cerrados | "The ___ UFO Was Finally Solved" |
| Historia de un producto | "A ___ Tried to Ban Coffee" |

**Ritmo**
- **Máximo 2 videos al día por canal.** Más no ayuda y baja la calidad.
- Canal nuevo: úsalo como persona unos días (mira videos del nicho, comenta) antes de subir.

**Test de micronicho**
- Cada test dura **7–14 días** (unos 14 videos).
- Se decide **cada domingo** con el reporte semanal (§6).

---

## 2. Gancho (los primeros 1–3 segundos)

1. **Prueba visual en el cuadro 0:** el objeto, el resultado o la escena ya en pantalla, más un texto de **4–6 palabras**. Antes de cualquier narración.
2. **Ataca algo que el público ya cree**, luego haz una promesa y después una promesa mayor.
   - Ej.: "Crees que X. No es así. Y hay algo peor…"
3. **Un objeto concreto** gana a lo general:
   - ✅ "el cajero automático"
   - ❌ "un detalle"
4. **El texto del gancho va en el video, grande.** La gente lee el gancho y el título, **no la descripción**.
5. **Voz IA y preguntas:** la voz sintética dice las preguntas como afirmación.
   - Escríbelas implícitas: "You'd think…", "La pregunta es si…", "Tell me if…".
   - La pregunta va **grande en pantalla**.
6. **Nunca empieces una frase con una palabra de una letra.** La voz se la come.
   - "O sea" → "Es decir"
   - "Y eso…" → "Eso…"

---

## 3. Estructura del video (20–40 s)

| Tramo | Qué pasa |
|---|---|
| 0–3 s | Gancho visual + texto corto |
| 1,5–4 s | Abre **una pregunta concreta** |
| ~50 % | Segunda capa: "y hay algo más…" antes de cerrar la primera |
| 70–90 % | **El remate** (la respuesta). No alargues después |
| Cierre | Pregunta grande para comentar + CTA hablado corto ("Follow for…") |

**Reglas**
- **Una idea central.** Menos información es mejor.
- **Lenguaje simple.** Que lo entienda cualquiera.
- Cada cifra va **con número en pantalla** y **en palabras para la voz** (`frases` vs `frases_voz`).
- Un estímulo nuevo cada ≤2,5 s es lo normal. No basta para destacar: lo que suma es **lo que muestra la imagen**.
- Cerrar con un cuadro parecido al primero (loop) ayuda a que lo vuelvan a ver.

---

## 4. Imagen (motor "escena")

**Lo que mejor nos rindió:** animación por código que **recrea lo que dice la voz**. Los textos, las cifras, los objetos y las escenas aparecen justo cuando se nombran. Rinde más que las fotos o el stock en movimiento.

- **Personajes que hacen cosas**: caminan, se pasan objetos, reaccionan, celebran. Nada de personajes quietos.
- **Protagonista fijo** por canal: siempre el mismo, reconocible.
- **Cambio de plano en cada idea** (cada 2–3 s): cara → objeto → detalle.
- **Mostrar, no escribir**: zoom al detalle, dinero que cae, números que cuentan, la pantalla del teléfono.
- **Títulos clave grandes** de neón para las 2–3 palabras que importan.
- **Nada tapa nada**: subtítulos, etiqueta, tarjetitas y cifras siempre separados (ver `motor/GUIA-MOTOR.md`).

**Lo que está prohibido**
- Caras reales
- Logos y marcas
- Deepfakes
- Personajes con derechos (superhéroes, mascotas de marcas…)
- Tomas, audio o marcas de agua de otros creadores
- Las imágenes generadas con IA solo valen **rotuladas como recreación**

---

## 5. Sonido

- **Voz:** Kokoro (local y gratis). Una voz fija por canal.
- **Música:** tranquila (`deep`) o de misterio (`dark`), **baja** (la música se agacha sola cuando habla la voz). Nada de música infantil si tu público es adulto.
- **Efectos:** cortos y **variados**.
  - Nunca el mismo efecto seguido.
  - Pops bajos.
  - Que calcen con el tema: motor en autos, glitch en misterio, caja registradora en precios.
- **Volumen final:** −14 LUFS (lo hace el motor).

---

## 6. Medir y decidir

**Mira los datos desde los 3–4 primeros videos.** No esperes a tener 40.

**Las 3 cifras de la decisión semanal** (las calcula `metricas/reporte_semanal.py`):

| Cifra | Qué mide |
|---|---|
| % que lo vio vs. lo deslizó | El gancho |
| % promedio visto | El guion |
| Suscriptores por cada 1.000 vistas | Si el canal promete algo que quieren seguir |

**Regla de decisión** (esta semana vs. los 14 días anteriores):

| Resultado | Qué hacer |
|---|---|
| Mejora en 2 de 3 | ✅ **Se queda** |
| Empeora en las 3 | 🔁 **Nicho de reserva** (pruebas otro) |
| Lo demás | 🛠️ **Ajustar** una sola cosa (gancho, fórmula u hora) |

**Lectura de cifras**
- **La retención alta no da alcance por sí sola.** Juzga por vistas a las 24 h junto con el % visto.
- **Menos de 20 vistas a las 24 h** suele ser un problema de distribución, no del gancho. Revisa en Studio el estado del video, las impresiones y si el audio y la imagen están completos.
- Para decir que un cambio funcionó, pide **≥1,5× la mediana del canal en 2 de 3 videos**. Una diferencia de ±15 % es ruido.
- **No traduzcas literal** un video a otro idioma el mismo día. Dale **otro ángulo** con el mismo objeto.
- **La hora de subida importa menos que el nicho.** Pruébala solo cuando el nicho ya funcione.

---

## 7. Empaque y publicación

**Título**
- **Hasta ~40 caracteres** para que no se corte en el celular.
- El número o el misterio al principio. Emoji opcional al final.

**Descripción**
- 1–2 frases que **insinúan** sin contar el remate.
- Luego un CTA corto y **4–5 hashtags**.
- Si usas estimaciones, agrega una línea de fuente.

**Publicación**
- Sin comentario fijado.
- El video cumple lo que promete el título. Nada de clickbait vacío.
- **Nunca republiques el mismo video.**

---

## 8. Verdad y legalidad (no se negocia)

- Solo datos **verdaderos, verificados en 2 o más fuentes**. Las estimaciones se dicen como **"estimación"** y con quién la hizo.
- Nada de urgencia falsa, promesas de dinero, "comparte o mala suerte".
- Temas de salud, dinero o legales: **informativo, nunca consejo**.
- Figuras públicas solo en contexto editorial.
- Material ajeno **solo para entender** qué funciona. Se extrae el patrón y nunca se copia el video.

---

## 9. Cómo se trabaja con Claude

- **Día por día:** se producen los videos de un día. Se adelantan más solo cuando el nicho está claro.
- **Revisar antes de dar por listo:**
  - que no haya `?` en `frases_voz`;
  - que nada choque en pantalla (usa `--muestras`);
  - mirar el cierre;
  - confirmar que tiene su `.txt`.
- **Junta todo el feedback** antes de rehacer un video. Así no se rehace muchas veces por cambios sueltos.
- Las contraseñas, los permisos de Google y los cambios de cuenta **los haces tú**. Claude nunca debe ver tus claves.
