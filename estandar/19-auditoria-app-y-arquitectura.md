# 19 · AUDITORÍA DE LA APLICACIÓN Y ARQUITECTURA CONSOLIDADA (propuesta para revisión)

> **Encargo de Tao (24-nov, 00:39):** convertir la aplicación que ya existe en un estudio inteligente, con tres áreas (Crear, Analizar, Inteligencia), que descubra oportunidades por su cuenta y aprenda de los resultados.
> **Estado:** **propuesta.** No modifiqué nada de la aplicación. Nada se toca hasta que apruebes la arquitectura.
> **Una precisión sobre el punto de partida:** el encargo da la investigación por terminada. No lo está: la ronda 1 (doc 18) no pudo ver videos de referencia y no hay datos de retención de ningún largo. El estudio "inteligente" va a arrancar con **hipótesis**, no con certezas.

---

## 0. Qué inspeccioné y qué no
| Sí (solo lectura) | No |
|---|---|
| Listado completo de `~/gta-shorts/` y de `canales/`, `datos/`, `inteligencia/`, `escena/`, `estudio_faceless/` | No leí el código línea por línea: leí la cabecera de 38 módulos, sus servicios externos y sus archivos de datos |
| `estudio.py` (rutas), `estudio.html` e `inicio.html` (botones), títulos de `MANUAL.md` | **No vi la aplicación funcionando** ni cómo se ve en pantalla |
| Las tablas que crea el código en las tres bases | No abrí las bases: no sé cuántas filas tiene cada tabla ni qué tan al día están |
| El motor de largos, que está en mi espacio de trabajo en la nube | Nada de `secretos/` |
| | `~/Desktop/YouTube/` (lo conozco por los documentos del proyecto) |

**Consecuencia:** el mapa de funciones es fiable a nivel de módulo. Antes de tocar un módulo concreto, lo leo entero y te aviso.

---

## 1. Auditoría de la aplicación actual
### 1.1 Mapa de lo que existe
| Función | Piezas | Estado |
|---|---|---|
| **Interfaz** | `estudio.py` (servidor local, ~25 rutas de lectura y ~16 de acción) · `estudio.html` · `inicio.html` (calendario y videos del día) · `movil.py` (modo teléfono) · `panel.py` (panel antiguo) | Funciona. Hay dos generaciones de interfaz conviviendo |
| **Descubrimiento** | `radar.py` · `nichos.py` · `explorador.py` · `inteligencia.py` + `biblioteca.py` + `diario.py` · `analisis.py` ("un solo comando que hace todo") · `verificar.py` · `clasificar.py` · `puntaje.py` · `plataformas.py` (Instagram y TikTok) · `vigia.py` (Reddit y Hacker News) · `laboratorio_faceless.py` | Muy completo, **solo para Shorts** |
| **Conocimiento** | `arsenal.py` (banco acumulativo por áreas) · `ganchos.py` · `hooks.py` · `patrones.py` (fórmulas) · `reglas.py` (reglas con procedencia) · `procedencia.py` · `lecciones.py` · `MANUAL.md` | Rico, repartido en varios lugares |
| **Decisión** | `director.py` (propone qué hacer mañana por canal) · `semaforo.py` (¿el canal funciona?) · `laboratorio.py` (experimentos A/B con réplicas) · `reporte_semanal.py` | Bien pensado; ya separa datos, conocimiento y decisiones |
| **Generación de Shorts** | `lote.py` → `revisar.py` → `storyboard.py` → `voz.py` → `montar.py` / `escena/` → `subtitular.py` → `control_final.py` → `publicar.py` | Funciona |
| **Generación de largos** | `largo.py`, `planos_tiempo.py`, `escena_h.html` + `planos.js`, `revisar_largo.py`, `hoja_planos.py`, `render_h.py` | **No está en la aplicación** (ver 1.2) |
| **Medición** | `metricas.py` (datos y analítica de YouTube) · `metricas_plus.py` (enganche, curva de retención, origen del tráfico) · `fichas.py` | Funciona |
| **Publicación** | `publicar.py` (deja todo en `~/Desktop/YouTube`) · `subir_youtube.py` (por API, solo con tu OK) | Funciona |
| **Datos** | `datos/cerebro.db` (25 MB) · `datos/inteligencia.db` (18 MB) · `datos/metricas.db` · unas 28 tablas · `canales/*.json` (7 perfiles) | Tres bases con solapamiento |
| **Uso de Claude** | Más de 20 módulos llaman a `claude -p` | Dependencia central |

### 1.2 Hallazgos, por importancia
| # | Hallazgo | Evidencia | Por qué importa |
|---|---|---|---|
| 1 | **El motor de largos no está en la aplicación.** Vive solo en mi espacio de trabajo en la nube. En el Mac, `escena/` tiene solo el motor vertical. El Estudio no tiene ni un botón ni una ruta para largos | Inspección directa | Los largos son el foco principal y hoy dependen de una sesión de chat. Es el riesgo más grande |
| 2 | **Toda la aplicación está construida para Shorts.** El manual se llama "Fábrica de Shorts"; el control final exige vertical y 180 s como máximo; los radares miden Shorts | Cabeceras de los módulos | Nada descubre ni mide oportunidades de video largo |
| 3 | **El descubrimiento está duplicado.** Al menos 9 módulos hacen tareas que se pisan, y la interfaz ofrece 8 o más botones de análisis (Rápido, Explorar, Completo, De noche, Corrida diaria, Buscar virales, Actualizar fórmulas…) | Botones de `estudio.html` | Es la confusión que ya me habías señalado. `analisis.py` ya quiso ser "el único comando": es la base natural del botón único |
| 4 | **El conocimiento vive en 6 lugares que no se hablan:** tabla `reglas`, `arsenal`, `formulas`, `4-lecciones.md`, `MANUAL.md` y la carpeta `estandar-produccion/` (docs 00–18) | Inspección | Lo que aprendimos esta noche no llega a los prompts que generan videos |
| 5 | **Buena parte del "aprendizaje continuo" ya existe.** `reglas.py` guarda cada cambio con su motivo y sus fuentes; `laboratorio.py` exige 6 réplicas alternadas por variante; `semaforo.py` usa una regla decidida antes de ver los datos | Cabeceras | No hay que construir desde cero: hay que **extender** |
| 6 | **"Viral" se define por vistas respecto de lo normal del canal.** Es una buena medida de descubrimiento, pero es popularidad | `inteligencia.py`, `puntaje.py` | Hay que etiquetarla como tal. No dice nada de retención |
| 7 | **La "psicología" del arsenal son etiquetas puestas por Claude** ("palancas") | `ganchos.py`, `arsenal.py` | Son nivel C o D. Hay que reetiquetarlas con los mecanismos del doc 18 |
| 8 | **Más de 150 archivos de versiones anteriores** (`*_v1.py`, `estudio_v14.html`…) conviven con los vigentes en la carpeta principal | Listado | Estorban al mantener. Se pueden mover a un archivo sin borrar nada |
| 9 | **Las tareas programadas existen, pero tú las corres a mano** porque el Mac no queda encendido de noche | `programar_*.sh` + lo que me has dicho | El análisis diario tiene que ser opcional y por tramos cortos |

### 1.3 Fuentes de datos: qué hay y qué no
| Fuente | Estado | Límite que no se puede ignorar |
|---|---|---|
| YouTube: búsqueda y datos públicos (API oficial) | **En uso** | Cuota diaria. Solo entrega vistas, no retención ajena |
| YouTube: analítica de tus canales | **En uso** (retención, enganche, tráfico) | Solo de tus canales |
| Búsqueda web (Claude) | **En uso** | — |
| Hacker News | **En uso** (`vigia.py`) | — |
| Reddit | **En uso** con acceso público sin cuenta (`vigia.py`) | **Riesgo:** varias fuentes secundarias indican que el uso comercial requiere acuerdo con Reddit y que el acceso sin autenticar puede estar bloqueado. No lo verifiqué en la fuente oficial. Hay que decidir si se mantiene |
| Instagram (API de Meta) y TikTok | Preparado (`plataformas.py`) | Límites de Meta; TikTok por archivo |
| **Google Trends** | **No disponible.** Existe una API oficial, en fase alfa y solo para quienes postulan y son aceptados. Sus valores son interés relativo, no cantidades absolutas | Se puede postular. Mientras tanto, el sistema no muestra "demanda de búsqueda" como número |

**Regla de honestidad para el descubrimiento:** cada cifra de una oportunidad lleva su fuente y su fecha. Si una fuente no existe, la casilla dice "sin dato". No se rellena con estimaciones.

---

## 2. Propuesta de interfaz: tres áreas
### 2.1 Estructura
```
┌──────────────────────────────────────────────────────────────┐
│  CREAR          ANALIZAR          INTELIGENCIA               │
└──────────────────────────────────────────────────────────────┘

CREAR
 ├─ Oportunidades   3–5 tarjetas por canal, ya investigadas
 │                  [Investigar más]  [Desarrollar]
 ├─ En desarrollo   cada video con su etapa y la decisión que espera de ti
 │                  (empaque · hoja de planos · render)
 └─ Por publicar    calendario, copiar título y descripción, modo teléfono

ANALIZAR
 └─ [ EJECUTAR ANÁLISIS ]   alcance: un video · un canal · todo
    Resultado: qué cambió, qué significa, qué hacer

INTELIGENCIA
 ├─ Novedades       solo lo que cambió desde la última vez
 ├─ Lo que sabemos  hipótesis, en prueba, apoyado, descartado (con su evidencia)
 ├─ Experimentos    en curso y terminados
 └─ Canales         identidad, estado y semáforo de cada uno
```

### 2.2 Adónde va cada cosa que existe hoy
| Hoy | Queda en | Cómo |
|---|---|---|
| Inicio (calendario, videos del día, teléfono) | **Crear → Por publicar** | Igual que ahora |
| Lote, Aprobar y producir, Rehacer, Usar la nueva | **Crear → En desarrollo** | Mismos comandos por debajo |
| Radar ES y EN, Explorar, Nichos, Buscar virales, Corrida diaria, Completo, De noche, Rápido | **Analizar → un botón** | Siguen existiendo por dentro. El botón elige cuánto profundizar según el tiempo disponible |
| Fórmulas vivas, Arsenal, Ganchos, Aprendizajes | **Inteligencia → Lo que sabemos** | Una sola vista |
| Semana, Evaluar, Semáforo, Director | **Inteligencia → Novedades y Canales** | — |
| Laboratorio | **Inteligencia → Experimentos** | — |
| Kit visual, Fichas, Tomas, Formatos | **Interno** | Se ejecutan como parte de Crear; visibles en un apartado "Avanzado" |
| `panel.py` (panel antiguo) | **Se retira de la vista** | El archivo no se borra |
| Repers (tandas, rendimiento) | **Se mantiene como está** | Fuera de este rediseño, salvo que digas otra cosa |

**Principio:** ninguna función desaparece. Lo que hoy es un botón pasa a ser un paso interno. Hay un apartado "Avanzado" para cuando quieras ejecutar algo suelto.

---

## 3. Arquitectura de descubrimiento
### 3.1 Flujo
```
Fuentes            Recolectores (ya existen)        Nuevo
────────           ─────────────────────────        ─────────────────────────
YouTube API   →    analisis.py / explorador.py  →   modo LARGOS (8–20 min)
Web           →    búsqueda de Claude           →   normalizar a "oportunidad"
HN / Reddit*  →    vigia.py                     →   tabla `oportunidades`
Tus canales   →    metricas.py + plus           →   evaluación con evidencia
                                                 →  3–5 tarjetas por canal
```
\* Reddit, sujeto a la decisión de 1.3.

### 3.2 Qué se descubre y con qué
| Tipo de oportunidad | Cómo se detecta | Ya existe |
|---|---|---|
| Videos exitosos de la competencia | Video muy por encima de lo normal de su canal | Sí (para Shorts) |
| Micronichos en crecimiento | Fuerza y constancia del nicho; canales chicos con aciertos | Sí (`explorador.py`, para Shorts) |
| Temas en tendencia | Videos recientes con muchas vistas por hora | Sí (`nichos.py`) |
| Temas perennes | Videos antiguos que siguen sumando vistas entre dos fotos | Parcial: hay que comparar fotos en el tiempo |
| Temas poco atendidos | Mucho interés y pocos videos buenos y recientes | **Nuevo** |
| Preguntas de alto interés | Búsqueda web y comunidades | Parcial (`vigia.py`) |
| Historias inusuales | Búsqueda web dirigida por el perfil del canal | **Nuevo** |
| Canales nuevos posibles | Explorador de nichos | Sí |

### 3.3 Cómo se evalúa cada oportunidad
Cada criterio indica **si es un dato o un juicio**. No hay nota única que los sume: los pesos serían inventados.

| Criterio | Qué se mira | Tipo |
|---|---|---|
| Demanda e interés | Vistas de los videos recientes del tema, respecto de lo normal de sus canales | Dato (popularidad) |
| Dirección de la tendencia | Vistas por hora; videos nuevos por semana | Dato |
| Competencia y saturación | Cuántos videos recientes hay y de qué tamaño son los canales | Dato |
| Rendimiento relativo | Cuántas veces supera lo normal de su canal | Dato |
| Evidencia factual | Cuántas fuentes sólidas tiene la historia | Dato (verificación) |
| Potencial narrativo | ¿Hay agente, conflicto y pregunta? | **Juicio** (nivel D) |
| Potencial de gancho | Qué mecanismos del doc 18 puede activar, y qué espera la audiencia | **Juicio** (nivel D) |
| Potencial visual | Objeto protagonista, lugares, qué se puede mostrar | **Juicio** (nivel D) |
| Dificultad de producción | Piezas que ya están en el banco frente a piezas nuevas | Dato (estimación) |

**La tarjeta que ves:**
```
THE RABBIT LOOP · oportunidad
"<tema>"                                   evidencia factual: 4 fuentes
Por qué ahora:  3 videos de 10–15 min en 30 días, 6× lo normal de sus canales
Competencia:    pocos canales, ninguno animado          (fuente: YouTube, 23-nov)
Ángulo posible: <la creencia que contradice>            (juicio)
Riesgo:         el dato central depende de una sola fuente primaria
Producción:     6 piezas del banco, 4 nuevas (~3 h)
[Investigar más]   [Desarrollar]   [Descartar]
```
Lo descartado se guarda, para no volver a proponerlo.

---

## 4. Integración de la inteligencia creativa
| Decisión | Hoy | Propuesta | Base |
|---|---|---|---|
| Tema | `director.py` + banco de ángulos | Sale de una oportunidad evaluada | Parte 3 |
| Gancho | Prompts de `lote.py` con el arsenal | Modelo de expectativa + conceptos por mecanismo + segundo juez | Doc 18, Parte 2 |
| Título y miniatura | 3 variantes | 3 variantes **de mecanismo distinto**, a prueba A/B, con predicción escrita | Doc 18, Parte 8 |
| Estructura | Fija | Se elige entre suspenso, curiosidad o sorpresa, según el tema | Doc 18 (G7) |
| Guion | `revisar.py` (datos y calidad) | Se suma la revisión de promesas sin pago y el grafo de causas | Docs 17 y 18 |
| Duración de plano | Fija | Los cinco criterios adaptativos | Doc 18, 5.3 |
| Disposición en pantalla | Revisión de subtítulos | Verificador de choques y tapados | Doc 18, 6.2 |
| Variedad | A ojo | Informe de repetición (informa, no bloquea) | Doc 14 |
| Sonido | Por plano | Igual; lo sigues validando tú | — |

**Cómo llega esto a los prompts:** los módulos que llaman a Claude leen sus reglas de **una sola tabla**, donde cada regla tiene su nivel de evidencia y su alcance. Ningún prompt lleva reglas escritas a mano. Así, cuando una hipótesis cambia de estado, cambia en todos los módulos a la vez.

---

## 5. Motor único de análisis
**Un botón. Tres alcances** (un video, un canal, todo). El motor decide qué pasos corren y por cuánto tiempo.

| Paso | Qué hace | Pieza que ya existe |
|---|---|---|
| 1 | Foto de las métricas | `metricas.py` |
| 2 | Enganche, retención y tráfico | `metricas_plus.py` |
| 3 | Unir cada video con lo que lleva dentro | `fichas.py` |
| 4 | Largos: dónde cae la curva y qué había en pantalla | **Nuevo** (cruce con el registro de planos) |
| 5 | Pruebas A/B y experimentos: ¿alguno concluyó? | `laboratorio.py` (más anotar el resultado de YouTube) |
| 6 | Descubrimiento externo, con presupuesto de tiempo | `analisis.py`, `explorador.py`, `vigia.py` |
| 7 | Propuestas de cambio al conocimiento | `reglas.py` (operaciones con motivo) |
| 8 | Resultado: **solo lo que cambió** | **Nuevo** (comparar con la corrida anterior) |

- **Presupuesto de tiempo:** eliges "10 min", "30 min" o "lo que tome". Trabaja por tramos, con pausas, para no calentar el Mac.
- **Si no hay datos suficientes, lo dice** y no concluye nada.

---

## 6. Análisis diario (opcional)
| Qué | Cómo |
|---|---|
| Cuándo corre | Cuando tú lo activas, o al abrir el Estudio si pasaron más de 20 h. Nunca de madrugada |
| Qué hace | Pasos 1–3 y 5 siempre; el 6 con presupuesto corto; el 7 solo si hay evidencia nueva |
| Cuándo avisa | Solo si: hay una oportunidad nueva que pasa el filtro · un video se aleja claramente de lo típico del canal · una prueba concluyó · cambió el semáforo de un canal |
| Cuándo calla | En cualquier otro caso. Sin informe "sin novedades" |
| Manual | El mismo botón de Analizar |

**Alternativa que puedo ofrecer:** una tarea programada **en la nube** que haga cada día solo el descubrimiento externo (búsqueda web) y te deje las oportunidades. No puede leer las bases del Mac si está apagado, así que no reemplaza el análisis de tus métricas.

---

## 7. Base de conocimiento
**No se crea una base nueva.** Se extiende `datos/cerebro.db`, que ya tiene `reglas`, `conocimiento_log`, `experimentos`, `exp_videos`, `arsenal` y `decisiones`.

| Cambio | Detalle | Tipo |
|---|---|---|
| Columnas nuevas en `reglas` | `nivel` (A–E) · `alcance` (universal, formato, nicho, canal) · `origen` (investigación externa o resultado propio) · `estado` (idea, en prueba, apoyada, estándar provisional, descartada) | Aditivo |
| Tabla `fuentes` | Cada fuente externa con su enlace y su fiabilidad | Nueva |
| Tabla `oportunidades` | Lo descubierto, su evaluación y qué pasó con ello | Nueva |
| Tabla `decisiones_video` | Por video: ganchos considerados y el elegido, mecanismos, estructura, criterio de ritmo, títulos a prueba, predicción | Nueva |
| `arsenal` | Reetiquetar "psicología" con los mecanismos del doc 18. Lo aprendido de otros nichos sigue marcado "probar antes de confiar" | Aditivo |
| Carga inicial | Los hallazgos del doc 18 entran como filas de origen "externo"; tus pedidos, como preferencias del canal | Datos |

**Separaciones que se respetan:**
- Investigación externa aparte de resultados propios.
- Lo de un canal no sube a "nicho" o "formato" sin repetirse en otro canal.
- Lo de Shorts no se aplica a largos, ni al revés.

---

## 8. Flujo de generación actualizado
```
Oportunidad → Hechos → Ángulo → Ganchos → [TÚ: empaque]
→ Estructura → Guion → Revisión (datos, promesas, causas)
→ Plan visual → Armado → Verificadores → [TÚ: hoja de planos]
→ Render → Control final → [TÚ: render] → Por publicar
→ Prueba A/B + predicción → Medición → Conocimiento
```
- **Largos:** el motor se instala en el Mac (`~/gta-shorts/largos/`) y se conecta al Estudio.
- **Shorts:** su flujo actual no cambia. Tiene su propio control final y su propia evaluación (doc 16).
- **Tus aprobaciones siguen siendo tres.**
- **Canal nuevo:** un perfil en `canales/` (ya existe el formato) más su fila de identidad. No requiere rediseñar nada.

---

## 9. Requisitos técnicos
| Requisito | Estado |
|---|---|
| `claude` en la terminal del Mac | Ya está (lo usan más de 20 módulos) |
| API de YouTube y permisos de analítica por canal | Ya están |
| ffmpeg, voz local, navegador para el render | Ya están para Shorts. **Por verificar** que el motor de largos corre igual en el Mac (hoy corre en un servidor Linux) |
| Funciones avanzadas de YouTube en cada canal | **Por confirmar contigo.** Sin eso no hay pruebas A/B |
| Google Trends | Postular al acceso alfa (opcional) |
| Reddit | Decidir: mantener, registrar una aplicación o quitar |
| Respaldo antes de cada etapa | Copia de la carpeta (sin `venv` ni videos) |
| Acceso mío al Mac | Hoy puedo leer y escribir archivos, pero **la consola no responde**. Sin consola no puedo probar nada en el Mac: tendrías que correr tú los comandos de verificación |

---

## 10. Hoja de ruta por etapas
Cada etapa termina con una prueba de que lo anterior sigue funcionando. Tiempos estimados según la velocidad real de este proyecto.

| # | Etapa | Evidencia | Confianza | Impacto esperado | Esfuerzo | Verificación |
|---|---|---|---|---|---|---|
| 0 | Respaldo de la carpeta y lista de comandos de prueba | — | — | Seguridad | 15 min | Existe la copia |
| 1 | **Traer el motor de largos al Mac** y conectarlo al Estudio, sin cambiar su comportamiento | Inspección directa (hallazgo 1) | Alta | Alto: elimina el mayor riesgo | 1,5–2 h | Rehacer una muestra de 20 s de un largo existente y comparar |
| 2 | Extender la base de conocimiento y cargar el doc 18 | Hallazgos 4 y 5 | Alta | Medio: es la base de todo lo demás | 1,5 h | Las reglas actuales siguen leyéndose igual |
| 3 | Botón único de análisis (envoltorio sobre lo que existe); los botones viejos pasan a "Avanzado" | Hallazgo 3; tu pedido | Alta | Alto en simplicidad | 2 h | Cada análisis antiguo sigue corriendo desde "Avanzado" |
| 4 | Tres áreas en la interfaz | Tu pedido | Media: no he visto la interfaz actual funcionando | Alto en simplicidad | 2–3 h | Todo lo de Inicio sigue disponible |
| 5 | Descubrimiento para largos + tarjetas de oportunidad | Hallazgo 2 | Media | Alto, si las oportunidades resultan buenas (hipótesis) | 3 h | Las cifras de 5 tarjetas coinciden con YouTube al revisarlas a mano |
| 6 | Inteligencia creativa en los prompts + registro de decisiones + verificador de pantalla | Doc 18 | Media: son hipótesis | Desconocido hasta medir | 3–4 h | Un Short y un largo de prueba salen igual o mejor |
| 7 | Análisis diario opcional, con regla de silencio | Tu pedido | Alta | Medio | 1 h | Dos corridas seguidas sin cambios no producen aviso |
| 8 | Ordenar: mover las versiones viejas a `_archivo/` | Hallazgo 8 | Alta | Bajo, pero facilita todo | 30 min | El Estudio abre igual |

**Total: 15–18 h de trabajo, en 6–8 sesiones.** El orden importa: la 1 y la 2 primero.
**Lo que no depende del código y puede empezar ya:** subir Pixar con su prueba A/B, y la ronda 2 de investigación.

---

## 11. Decisiones que necesito de ti
1. **¿Apruebas la arquitectura?** (o qué cambiarías)
2. **Canales fuera de la lista** (ViceVerso, TheViceVerse, Repers, Number Signs): ¿quedan como están, dentro de las mismas tres áreas?
3. **Análisis diario:** ¿al abrir el Estudio, solo manual, o además la tarea en la nube para el descubrimiento?
4. **Reddit:** ¿se mantiene, se registra una aplicación o se quita?
5. **Google Trends:** ¿postulamos al acceso?
6. **La consola del Mac:** necesito que vuelva a responder, o que corras tú las verificaciones.

---

## Fuentes de este documento
- API de Google Trends (alfa): https://developers.google.com/search/apis/trends · https://developers.google.com/search/blog/2025/07/trends-api
- Reddit (fuentes secundarias, fiabilidad baja; falta leer los términos oficiales): https://gologin.com/blog/reddit-data-api/ · https://www.activepieces.com/blog/reddit-api-access-in-2026-how-to-get-started
- Todo lo demás sale de la inspección directa de `~/gta-shorts/` y de los docs 14, 17 y 18.
