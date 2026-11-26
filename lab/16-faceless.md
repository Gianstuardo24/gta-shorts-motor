# 16 · Laboratorio faceless: qué aprendimos de 31 videos (22-nov-2026)

> Parte del cerebro de estudio. Lo leen el Director, el guionista y Claude antes de proponer canales, formatos o guiones.
> **Fuentes:** 31 videos bajados y analizados (transcripción + hoja de cuadros + cortes por minuto) en `estudio_faceless/`. Fichas completas en `16-faceless-fichas.md`.
> Los hechos de plataforma (§1) están **verificados en prensa y en el blog oficial**. El resto son **patrones**: se aplican como hipótesis y se miden con el reporte semanal.
> Si algo de aquí choca con el MANUAL, **manda el MANUAL**.

---

## 0. Qué se analizó

| Grupo | Videos | De quién |
|---|---|---|
| Los 11 de Tao | Subir videos y Shorts, 1.000 subs, recomendación con pocos subs, monetizar con Claude, historia animada, faceless en 4 min, monetizar en 8 días | Edu Serrano ×5, Ale Ferr ×3, Carlosyt, Katire Labs, Veloz Redes |
| Algoritmo | YouTube 2026 **(oficial)**, cambio de oct-2026 ×2, Shorts en 180 s, 5.400 Shorts estudiados, cambios 2026 | Creator Insider, vidIQ, Duodedos, dmscales, Marcus Jones, Edu Serrano |
| Faceless | Reglas 2026, los que crecen más rápido, nichos nuevos, no perder la monetización, la "mentira" de la IA, ¿vale la pena?, 7 niveles, paso a paso, 7 nichos | vidIQ ×3, vidIQ ES, Duodedos, Mario Ruiz, Ale Ferr, Romayroh, Eric Alanis |
| Casos | Shorts en 7 días ×2, canal hecho solo con Claude, 30 días de automatización, Beluga | Isaac, DonebyLaura, Adrián Sáenz, Stickman Matt, Paddy Galloway |

---

## 1. Lo que cambió en YouTube (hechos verificados)

| Fecha | Cambio | Qué significa para nosotros |
|---|---|---|
| **15-jul-2025** | Política de monetización de **"contenido inauténtico"**: lo producido en masa o repetitivo no se monetiza. Ejemplos de YouTube: historias narradas con diferencias superficiales y presentaciones con la misma narración | La IA está permitida si **mejora contenido original** |
| **Jul-2026** (aclaración) | 3 categorías que no se monetizan: **(1) genérico, repetitivo o de plantilla** (incluye apoyarse en IA, CGI o plantillas reutilizables para hacer videos casi idénticos), **(2) insatisfactorio o perturbador**, **(3) personas IA en temas sensibles** (salud, finanzas) | ⚠️ Nuestro motor es una "plantilla": cada video tiene que verse y contarse **distinto**. Finanzas o salud: **sin "persona IA experta"** |
| **1-oct-2026** | Los Shorts **originales** tienen prioridad en las recomendaciones. Bajan las cuentas que sobre todo **resuben clips ajenos sin cambios**. No alcanzan ajustes técnicos menores ni cambios de plantilla; hay que aportar voz, historia o punto de vista | ✅ Somos 100 % originales: el cambio nos favorece |
| **2-nov-2026** | Lo subido por API desde proyectos sin auditar **ya no queda privado** | `subir_youtube.py` sirve sin auditoría |
| **1-feb-2027** | ⭐ **YPP duplica la entrada** para canales nuevos: 1.000 subs **+ 8.000 h en 365 días o 20M vistas de Shorts en 90 días** (hoy 4.000 h o 10M). Los que ya están dentro no tienen que volver a calificar | Ver §8: cambia qué canales conviene abrir |
| Feb-2027 | Para **seguir activo** en YPP: 1.000 h en un año, o 1M de vistas de Shorts en 90 días, o 2 videos largos o 5 Shorts cada 90 días (según la prensa) | Fácil de cumplir si publicamos |
| 2026 | Escala: **>200.000 millones de vistas diarias de Shorts** y **>1.000 millones de horas diarias en TV** | El largo crece por la TV; el Short por la "fatiga de decisión" |

**El algoritmo según YouTube** (Creator Insider, sep-2026, con el director de Growth & Discovery):
- **Arma las recomendaciones por espectador** cuando abre la app. No "empuja" tu video.
- **Aprende por audiencias:** suscriptores, no suscriptores y nuevos. Un mal arranque con un grupo no lo condena para los demás.
- **Muchos videos hacen la mayor parte de sus vistas un mes o más después.** No hay que juzgar por las primeras horas.
- **No hay una métrica mágica:** CTR, tiempo absoluto y relativo, **encuestas de satisfacción**, likes y dislikes, con pesos distintos por persona y dispositivo.
- **Un canal = una audiencia o marca.** Probar temas nuevos no castiga.
- **CTR ≈ 10 % o menos es normal**, incluso en los mejores videos.
- No desactivar la notificación a suscriptores. Desactivar comentarios o anuncios no penaliza.

---

## 2. "Gurús" vs. fuente oficial

| Afirmación | Quién | Veredicto |
|---|---|---|
| Subir en "oculto" y publicar después; horas mágicas (1–3 AM) | Edu Serrano | ❌ Sin evidencia; la hora pesa menos que el nicho (ya era nuestra regla) |
| "Trust score" oculto, "cárcel de las 30k" | dmscales | ⚠️ Folclore. Útil: **verificar funciones avanzadas** del canal |
| Precalentar la cuenta 7 días; ≤4 videos/semana al inicio | Veloz Redes | ⚠️ Experiencia, sin fuente oficial |
| Ocultar el número de likes al inicio; audio en tendencia priorizado | Edu Serrano | ❌ Sin evidencia |
| ElevenLabs lleva "SynthID" y YouTube desmonetiza por eso | Veloz Redes | ❌ SynthID es de Google. Lo que sí existe es la política de **contenido inauténtico** |
| "Ganancia neta de información" (premia la info nueva) | Romayroh | ⚠️ Concepto de Google, no confirmado como regla de YouTube; coherente con "originalidad" |
| Test A/B: el ganador se elige por **cuota de tiempo de visualización**, no por CTR | Edu Serrano | ✅ Así funciona *Probar y comparar* |
| Shorts: "vio vs. deslizó" ≥70–80 %; <40 % casi nunca pasa de 10k | Edu Serrano / estudio de Paddy Galloway | ✅ Coherente con nuestros datos: **es nuestra métrica 1** |

---

## 3. Patrones que se repiten (lo que hacen los que funcionan)

**Ganchos (primeros 1–3 s)**
- **Síntoma exacto del espectador** ("300, 500, 1.000 vistas y se para") o **escena cómica concreta** ("4 visitas: 3 son tuyas y 1 de tu madre").
- **El espectador como personaje:** "Eres una empresa gigante de café y tienes un problema" → solución paso a paso → revelación ("era Nescafé"). En un caso pasó de flop a 80 % vio vs. deslizó y 96 % de retención.
- **4 tipos:** error ("este error mata…"), resultado ("cambié X y…"), contradicción ("subir más te hace crecer más lento") e historia o experimento propio.
- **Bucles abiertos encadenados:** "cada vez que cierras una pregunta, abres otra". Uno grande abierto hasta el final.
- **Lo que promete el título se repite en la intro.**

**Estructura**
- **Gancho → tensión → recompensa.** Sin recompensa clara al final, el Short muere.
- Tema: **¿da dopamina o deprime?** Los temas deprimentes rinden peor en Shorts.
- **Cada dato es un personaje que quiere algo**: "Tus órganos cuando caminas 10.000 pasos" llegó a 2M en 2 semanas. La lección es el **giro final**.
- Largo: alargar = más historia y ejemplos, **nunca relleno**. Error típico: minuto 1 brillante y minutos 10–20 flojos.
- Truco de guion: pedirle a Claude que lo lea **como un espectador que se aburre** y marque dónde se iría.

**Imagen (lo vimos en las hojas de cuadros)**
- Los faceless que ganan **cumplen los "trabajos" de una cara** de otra forma:
  - **personaje fijo** (gorila con opinión, gnomo 3D, muñeco presentador, Biscuit y Mochi);
  - **firma visual reconocible sin sonido** (Zack D. Films, líneas de neón naranjas, explicador con muñequito azul);
  - **narrador con postura**.
- Estilos baratos que funcionan:
  - **infografía animada** (fondo azul marino o blanco, titular con 1 palabra en color, tarjetas de "vidrio", ✗ tachado vs ✓, número gigante, "Paso 2 de 5");
  - **minimalismo** (blanco, frase en itálica con 1 palabra roja, muñeco de palo: 758k vistas);
  - **pizarra con un muñeco presentador**;
  - **captura anotada** (Paddy Galloway): fondo blanco, muestra real, etiqueta a mano en turquesa o rojo y flecha. Ideal para videos de análisis;
  - **2D plano de historia** con mapas y flechas.
- Ritmo: los explicadores van a **8–17 cortes por minuto**. Una clase con pizarra baja a 2,5/min (se sostiene por el contenido).
- **Ilustrar cada frase.** "Una imagen durante 5 minutos" es lo que YouTube lee como bajo valor.

**Sonido**
- Beluga: **11 cambios de sonido en los primeros segundos**. El sonido sostiene tanto como la imagen.
- **La voz es lo más humano** de un faceless: las voces IA de catálogo suenan a "copia de copia". Los que ganan **clonan su voz** o usan locutor.

**Títulos y miniaturas**
- **~33–40 caracteres**; las **2 primeras palabras** son lo único que se ve al deslizar.
- **Números raros** (9; 97,1 %).
- **Título = afirmación, miniatura = intriga** (pausada justo antes de que pase algo).
- **Empaquetar todos los videos igual** para que se reconozca el canal.
- **Patrón > idea:** "A vs B: **la estafa / la gran mentira**" (Los Económanos) se lleva a cualquier tema. Copiar el **patrón**, nunca el video.

**Formatos repetibles**
- *Ranking your life at every level of wealth* → la misma estructura con oficios = ~15.000 USD/mes (estimación).
- "Your organs when ___"; "How I'd survive every ___ movie"; "Living in ___" (ya saturado).
- **Encontrar 1 formato y repetirlo hasta que deje de funcionar.**

---

## 4. Economía: dónde está la plata

| Concepto | Dato | Fuente |
|---|---|---|
| RPM Shorts | **~0,02–0,06 USD por 1.000 vistas**; 5M de vistas = "casi nada" | Carlosyt (2026), estudio de 2023 |
| RPM largos | **1–2 USD por 1.000** como base; animales y salud **3–5**; finanzas y tecnología **10–15** | Marcus Jones, Eric Alanis |
| Subs por 10k vistas | largos ~22 vs Shorts ~17 | estudio de Paddy Galloway |
| Q4 | **noviembre y diciembre pagan ~2×** (más anunciantes) | Mario Ruiz |
| Afiliados | desde el día 1, sin YPP: 94 USD en 30 días (caso realista); Audible ~10 € por prueba gratis; Amazon | Stickman Matt, Adrián Sáenz, Romayroh |
| Costo de producción | **clips IA ≈ 10–15 USD/min** (~210 USD por video de 14 min, ~14 h) · **imágenes IA ≈ 14 USD por video** (~2 h) · **nuestro motor por código ≈ 0 USD** (solo tiempo de render) | Adrián Sáenz |
| Expectativa realista | canal nuevo a 30 días: ~4.000 vistas, ~100 subs, ~3 USD/hora; los de 5 cifras tardaron 6–24 meses. La automatización es **ingreso extra** y los modelos fáciles de copiar **mueren** | Stickman Matt, Duodedos |

**Conclusión:**
- **Los Shorts dan alcance; los largos dan ingresos.**
- Con la regla de 2027 (8.000 h), un canal nuevo necesita **formatos con mucho tiempo de visualización**:
  - videos de 15–30 min;
  - series que se ven en TV;
  - "para dormir o estudiar" de 1–2,5 h (**2.000 vistas completas de un video de 2 h = 4.000 h**).

---

## 5. Mapa del mercado faceless (7 niveles, Ale Ferr)

| Nivel | Qué es | Riesgo |
|---|---|---|
| 1 | 100 % imágenes o clips IA + narración | **alto** (inauténtico) |
| 2 | IA hiperrealista tipo documental | alto + RPM bajo |
| 3 | Recopilación de clips de internet + voz | **muy alto desde oct-2026** |
| 4 | Tendencias con IA | caducan rápido |
| **5** | **Explicaciones animadas propias (2D)** | **seguro, evergreen** |
| 6 | Alta calidad con marca | — |
| 7 | Marca completa con equipo de animación | barrera altísima |

**Nuestra posición:** el motor nos deja en el **nivel 5 con costo de nivel 1**. Es la combinación más defendible.

**Nichos que aparecieron como frescos (2026):**
- supervivencia en películas de terror;
- **auge y caída económica** (productos, empresas, países);
- **finanzas en 2.ª persona** con muñeco ("Son las 7:41 de un martes y tú…");
- **autopsias históricas**;
- lore de sagas (Dune, Warhammer: con lectura real y "hecho por humanos");
- finanzas para una etapa de vida (50–60 años);
- cruceros;
- tecnología e IA.

**Ya saturados:** "Viviendo en [país]"; historia genérica con IA; "para dormir" genérico.

**Método para elegir nicho:**
1. Canales de **<3–6 meses** que ya despegan.
2. **Más vistas que suscriptores.**
3. **Casi nadie en español.**
4. **Barato de producir.**
5. **Chequeo de saturación** del formato: cuántos canales usaron ese título en 90 días.
6. **Cuadro vacío en la cuadrícula formato × tema.**

---

## 6. Riesgos y cómo los cubrimos

| Riesgo | Cómo nos protegemos |
|---|---|
| "Plantilla repetitiva" (jul-2026) | Escenas, personajes, decorados y estructura **distintos por video**; guion con ángulo y postura; nada de "misma narración con otra imagen" |
| Persona IA en temas sensibles | Finanzas y salud: narrador sin hacerse pasar por experto; informativo, con fuentes; nada de consejo |
| Voz de catálogo | Probar **voz clonada de Tao** o una voz propia por canal; **tráiler del canal con Tao** (puede ir oculto, como "avance del canal") |
| Copiar a otros | Ya es regla: material ajeno solo para entender. Del lote, **descartar**: copiar transcripciones ajenas, resubir el mismo video, clips de películas |
| Formato fácil de copiar | Nuestro foso: motor propio + verificación 2+ fuentes + estilo película |
| Expectativas | Medir contra nosotros mismos (reporte semanal); paciencia: los videos maduran en semanas |

---

## 7. Aplicación a nuestros canales actuales (propuestas: Tao decide)

1. **Perros y Gatos:**
   - **Biscuit y Mochi con opinión propia** (hablan o piensan en 1.ª persona, con un rasgo predecible).
   - Serie "**Your dog's brain when ___**" con el cerebro, la nariz o la cola como personajes con cara.
2. **MDM:**
   - Estructura **"Eres X y tienes un problema" → solución → revelación**.
   - Patrón "**A vs B: la estafa**".
   - Versión larga "**auge y caída**" (por qué X está muriendo o cuesta tanto).
3. **Café:** "Eres un rey y tienes que prohibir el café…" (2.ª persona) + revelación.
4. **GTA ES/EN:**
   - Ahora que el juego salió, priorizar **novedad verificada** (noticias del día = información nueva).
   - Evergreen solo con ángulo propio.
5. **Todos:**
   - **Presentador o firma fija** por canal.
   - **Tráiler con la voz de Tao.**
   - **Funciones avanzadas verificadas**.
   - **Listas de reproducción** por micronicho.
   - En Shorts: campo **"Video relacionado"** de Studio apuntando a un largo cuando exista.
6. **Shorts:**
   - Umbral de **≥70 % vio vs. deslizó**.
   - Probar **45–60 s solo si el guion lo sostiene** (A/B de duración).
   - Checklist de tema: dopamina, algo en juego en el segundo 1, recompensa clara.

---

## 8. Canales faceless nuevos (largos + Shorts): propuestas ordenadas

**Criterios:**
- se puede hacer con nuestro motor;
- RPM;
- tiempo de visualización (por la regla de 8.000 h);
- riesgo de política;
- competencia en español.

| # | Canal (idea) | Formato | RPM | Por qué | Riesgo |
|---|---|---|---|---|---|
| 1 | **Finanzas contadas como historia** (derivado de MDM): auge y caída de empresas y productos, "A vs B: la estafa" | largos 12–20 min + Shorts anzuelo, personajes que actúan, cifras animadas | **alto (10–15)** | RPM alto, ya sabemos verificar cifras, nicho fresco en español | medio: nada de consejo ni "persona experta IA"; fuentes en pantalla |
| 2 | **Historia animada en serie** (episodios de 15–25 min, "historia con personajes") | estilo película: mapas, decorados, actores | medio | evergreen, se ve en TV, nivel 5 seguro | **competencia directa** (motores gratis de otros): diferenciar por ángulo (autopsias, "eres X en el año Y") |
| 3 | **Para dormir o estudiar** (historia o ciencia calma, 1–2 h) | escenas lentas + voz calma + música suave | medio | **horas de visualización masivas** (el camino más corto a 8.000 h) | **alto si es genérico**: necesita voz propia, guion con fuentes no-Wikipedia y "cuadro vacío" (ej. historia naval, historia de una industria) |
| 4 | **Explicador de tecnología e IA** con muñeco presentador + infografía | 10–20 min | **alto (~10)** | RPM alto, afiliados de herramientas | saturación media; requiere novedad constante |
| 5 | **Curiosidades con personaje** (tipo gnomo, en español) | Shorts + compilados largos | bajo | rápido de probar | RPM bajo; sirve como anzuelo |

**Calendario sugerido (realista):**
- **Antes del 1-feb-2027** (10 semanas), con las reglas de hoy (4.000 h):
  - lanzar **1 canal largo** (#1 o #2);
  - hacer el **piloto de 3 episodios** en ~1 semana de trabajo del motor;
  - medir 3 semanas.
- Llegar a 4.000 h antes de febrero **solo pasa con un éxito**: no planificar contando con eso.
- Después de febrero la meta es **8.000 h**, así que los formatos largos y en serie pesan aún más.
- Los Shorts actuales siguen como **alcance y laboratorio de ganchos**.

**Cambios al motor que habilitan esto:**
1. **Modo documental largo:** escenas encadenadas por capítulos, mapas con rutas, línea de tiempo.
2. **Presentador fijo** + **pizarra o tarjetas de infografía** (estilo "explicador": titular, ✗/✓, número gigante, "Paso N de M").
3. **Personajes-objeto con cara** (órganos, monedas, productos).
4. **Capítulos** y descripción explicativa (para la búsqueda y para que la IA cite el video).
5. **CTA en 3 puntos** (inicio, mitad, final) y **afiliados** en la descripción cuando aplique.
6. **Chequeo de saturación** antes de lanzar un formato (contar canales con ese título en 90 días).

### 8b. Largos en los canales que YA tenemos (idea de Tao, 22-nov)

Además de los Shorts, cada canal suma **videos largos faceless que amplían su micronicho**.

**Por qué conviene:**
- El canal ya tiene público.
- Los Shorts hacen de anzuelo, enlazando al largo con el campo "video relacionado" de Studio.
- Las horas de los largos cuentan para el YPP; las de los Shorts, no.

| Canal | Shorts (micronicho) | Largo propuesto | Duración |
|---|---|---|---|
| Rabbit Loop | casos OVNI cerrados | **"El expediente completo"**: 1 caso por episodio con capítulos (contexto → testigos → evidencia → investigación oficial → cierre) | 12–20 min |
| MDM | cosas vendidas baratas que hoy valen fortunas | **"La historia completa"** del trato: auge, error y cuánto valdría hoy | 10–15 min |
| Café | el café prohibido | **Documental de historia del café** (después, versión calma para estudiar) | 12–20 min |
| GTA EN | secretos y mecánicas ocultas | **"Todas las mecánicas ocultas, explicadas"** (lista con capítulos) | 10–15 min |
| GTA ES | los números de GTA 6 | **"GTA 6 en números"**: la economía completa de Leonida | 10–12 min |
| Perros / Gatos | qué piensa tu animal | **"Todo lo que tu perro/gato te dice"** con el protagonista fijo | 10–15 min |

**Reglas:**
- **Semilla = el Short que mejor rindió** de ese canal.
- El largo **amplía** el tema; nunca se arma pegando Shorts.
- De cada largo salen **2–3 Shorts nuevos** que llevan al largo.
- Video horizontal 16:9 con portada horizontal, capítulos y más de 8 min (para los anuncios a mitad de video).

**Piloto:** 2 canales, 1 largo por semana durante 3 semanas. Se mide retención a los 30 s, duración media y horas de visualización.

---

## 9. Pendientes para decidir (Tao)

- [ ] ¿Abrimos un canal largo antes del 1-feb-2027? ¿Cuál: #1 finanzas-historia o #2 historia en serie?
- [ ] ¿Grabamos el **tráiler con la voz de Tao** y probamos **voz clonada** para un canal?
- [ ] ¿Aplicamos a Perros y Gatos la idea de "personaje con opinión" + "brain when ___"?
- [ ] ¿Sumamos **afiliados** (Amazon/Audible) en las descripciones donde calce?

**Fuentes de los hechos de §1:**
- blog.youtube: cambios a YPP (ago-2026)
- Music Business Worldwide; The Next Web (umbrales y mantenimiento 2027)
- TechCrunch; TechRepublic (3 categorías de contenido inauténtico, jul-2026)
- Search Engine Journal; Android Authority; outlierkit (actualización de Shorts originales, 1-oct-2026)
- AOL / Yahoo Tech (política de jul-2025)
- Creator Insider "YouTube Algorithm 2026" (video oficial)
