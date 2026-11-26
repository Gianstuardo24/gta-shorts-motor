# 21 · PLAN POR ETAPAS, CALIBRACIÓN Y SELECCIÓN DE REFERENCIAS (para revisión)

> **Decisión de Tao (24-nov, 00:57):** aprobada la dirección del doc 20 como núcleo del Estudio, con ajustes.
> **Este documento:** (A) los ajustes incorporados, (B) la implementación por etapas, empezando por el respaldo y las verificaciones, (C) el protocolo de calibración y (D) la selección de referencias para que la revises **antes** de estudiar nada.
> **No se modificó código.** No se modifica hasta terminar esta revisión.
> **En segundo plano, sin fecha:** Reddit, Google Trends, automatizaciones y rediseño de la interfaz.

---

## A. Ajustes incorporados a la arquitectura
### A.1 Fiabilidad por código (tu punto 2)
| Regla | Detalle |
|---|---|
| El acuerdo se mide **por dimensión y por código** | Ver Parte C |
| Cada código tiene un estado | **Fiable · dudoso · no fiable · sin calibrar** |
| **Solo los códigos fiables alimentan patrones de forma automática** | Lo dudoso y lo no fiable se guarda marcado, queda fuera de Comparar y solo entra si una persona lo confirma |
| Un código no fiable se **redefine y se vuelve a calibrar** | No se "promedia" ni se deja pasar |
| Control de deriva | En cada tanda, un video se codifica dos veces a ciegas para ver si el acuerdo se mantiene |

### A.2 Exploración controlada (tu punto 4)
| Regla | Detalle |
|---|---|
| **Un solo elemento experimental por video** | Así el resultado se puede leer |
| Qué puede probarse | Un patrón con mecanismo plausible y, como mínimo, respaldo externo u observación con control. Nada "porque sí" |
| Dónde | En un tramo donde un fallo cueste poco. Nunca a la vez en título, apertura y estructura |
| **Piso de calidad** | Pasa los mismos controles que el resto. Si en la hoja de planos se ve peor que la solución conocida, se retira |
| Visible para ti | En cada aprobación aparece marcado "experimental", con su motivo |
| Registro obligatorio | Predicción escrita antes de publicar · elemento · tramo · resultado · conclusión |
| Sin datos suficientes | Queda "sin concluir". No cuenta ni a favor ni en contra |

### A.3 Criterio creativo (tu punto 5)
Recuperar patrones no es criterio. El criterio es decidir **qué necesita esta historia** antes de mirar la biblioteca.

| Paso | Qué se decide |
|---|---|
| **1. Diagnóstico de la historia** (antes de consultar) | Qué pregunta la sostiene · dónde está su fuerza (un hecho, un personaje, un objeto, un mecanismo) · dónde se va a caer (el tramo denso, la mitad, un final débil) · qué espera la audiencia |
| **2. Necesidades por tramo** | Qué función hace falta en cada parte: abrir, situar, sostener, girar, pagar |
| **3. Consulta** | Patrones que cumplen esa función en ese contexto |
| **4. Cinco salidas posibles por necesidad** | **Usar** un patrón tal cual · **adaptarlo** · **combinar** dos · **evitar** uno que calza en apariencia pero choca con la historia o el canal · **crear** una solución nueva |
| **5. Justificación** | Por qué esta salida y no las otras, en una o dos frases |

**Cuándo conviene crear algo nuevo:**
- Ningún patrón cumple la función en este contexto.
- Los que la cumplen se usaron hace poco en el canal.
- La historia tiene algo único (un objeto, una imagen, un dato) que ningún patrón aprovecha.

**Lo nuevo no se pierde:** una solución creada se guarda como elemento propio y, si se repite con buen resultado, puede llegar a patrón.

**Cómo se entrena el criterio (no solo el conocimiento):**
| Fuente | Qué enseña |
|---|---|
| Libro de decisiones | Cada decisión con su justificación y su resultado: son los casos de los que aprende |
| Predicciones contra resultados | Dónde juzga bien y dónde se equivoca |
| Tus correcciones | Cada vez que cambias una propuesta, se guarda **por qué** |
| Estudio de fracasos | Qué diagnóstico estaba mal |

**Cómo se mide:** acierto de las predicciones, y con qué frecuencia cambias lo que propone y por qué motivo.

### A.4 Un cerebro, muchos canales (tu punto 6)
| Regla | Detalle |
|---|---|
| Todo objeto lleva **alcance, canal y formato** | Universal · formato (largo o Short) · nicho · canal |
| Una consulta combina capas | Lo universal + lo del formato + lo del nicho + lo del canal. Lo específico pesa más que lo general |
| Los resultados se guardan **por canal** | Lo que funcionó en un canal no sube de capa sin repetirse en otro |
| La identidad vive en el perfil | `canales/*.json` (ya existen 7). Un canal nuevo es un perfil nuevo |
| Largos y Shorts no se mezclan | Cada formato con su evidencia |
| Todos los canales entran | Los cinco de la lista, y también ViceVerso, TheViceVerse, Repers y los futuros |

---

## B. Implementación por etapas
**Reglas para todas las etapas:**
1. Te aviso **antes** de cada cambio, con el archivo y qué cambia.
2. Todo archivo que se modifica deja una copia `.bak_<fecha>_<tema>`, como hasta ahora.
3. Los cambios a la base son **solo aditivos**: tablas y columnas nuevas. Nada se borra ni se renombra.
4. Cada etapa termina con una verificación y tiene forma de deshacerse.
5. Mientras la consola del Mac no me responda, los comandos los corres tú y yo leo el resultado desde un archivo.

### Secuencia
| # | Etapa | Toca código | Estado |
|---|---|---|---|
| 0 | Respaldo y verificaciones técnicas | No | ✅ **Completa (24-nov, 09:12)** |
| C | Calibración del libro de códigos | No | Después de la 0 |
| D | Revisión de la selección de referencias | No | Selección en la Parte D |
| 1 | Traer el motor de largos al Mac | Sí | Espera tu OK tras C y D |
| 2 | Modelo de la biblioteca | Sí (base de datos) | — |
| 3 | Estudiar largos | Sí | — |
| 4 | Primera tanda de estudio | No (uso) | — |
| 5 | Comparar | Sí | — |
| 6 | Aplicar, con criterio y exploración controlada | Sí | — |
| 7 | Aprender de lo propio | Sí | — |
| — | Botón único, interfaz, Reddit, Trends, automatizaciones | — | En segundo plano |

### Etapa 0 · Respaldo y verificaciones (tú, unos 10 min)
> **Corregida el 24-nov, 08:35**, tras el primer intento. Qué cambió y por qué:
> - **El comando de respaldo anterior tenía un error mío:** `--exclude 'tomas*'` también dejaba fuera `tomas.py` y sus versiones. Ahora las carpetas excluidas van por nombre exacto.
> - **Hay tareas programadas que escriben en las bases.** Los bloques ahora se detienen solos si encuentran una corriendo.
> - **La integridad se revisa sobre la copia del respaldo**, no sobre el original. Una huella (sha256) antes, en la copia y después prueba que el original no cambió y que la copia es idéntica.
> - Los bloques corren dentro de `bash`, para que se comporten igual sin importar la terminal.

**Cuándo NO correrla** (el Mac escribe solo en las bases):
| Tarea programada | Cuándo | Qué base toca |
|---|---|---|
| Métricas extra y fichas | 08:20, todos los días | `metricas.db` |
| **Corrida diaria** (`diario.py`) | **08:30 a ~09:15**, todos los días | `inteligencia.db` y `cerebro.db` |
| Foto de métricas | Cada hora, cerca del minuto :19 | `metricas.db` |
| Reporte semanal | Domingos, 09:30 | Solo lee |

**Ventana segura:** después de las 09:20, fuera de los minutos :15 a :25, y con el Estudio cerrado.

**Paso 1 · Comprobación previa** (10 s, solo lectura):
```bash
bash <<'FIN'
cd ~/gta-shorts || exit 1
{
echo; echo "===== PASO 1 · COMPROBACION PREVIA (Mac) · $(date) ====="
echo "== procesos que usan las bases =="
pgrep -fl "[Pp]ython[^ ]* (-u )?(estudio|movil|panel|diario|biblioteca|inteligencia|hooks|patrones|metricas|metricas_plus|fichas|lote)[.]py" || echo "ninguno"
echo "== ultima linea de la corrida diaria =="; tail -1 logs/diario.log
echo "== archivos temporales de las bases =="
find datos -maxdepth 1 \( -name "*-journal" -o -name "*-wal" -o -name "*-shm" \) | grep . || echo "ninguno"
echo "== tareas programadas =="; launchctl list | grep viceverso || echo "ninguna"
echo "== espacio =="
T=$(du -sk . | cut -f1); E=0
for d in venv venv_chatter models salida clips tomas tomas_mdm tomas_rabbit estudio_faceless/videos; do
  [ -d "$d" ] && E=$((E + $(du -sk "$d" | cut -f1)))
done
L=$(df -k "$HOME" | tail -1 | awk '{print $4}')
echo "respaldo estimado: $(( (T - E) / 1024 )) MB · libre en disco: $(( L / 1024 )) MB"
echo "== carpetas mas pesadas (MB) =="; du -sk */ | sort -n | tail -10 | awk '{printf "%6d  %s\n", $1/1024, $2}'
} >> estandar-produccion/verificacion_etapa0.txt 2>&1
tail -32 estandar-produccion/verificacion_etapa0.txt
FIN
```
**Cómo leerlo:** en "procesos que usan las bases" tiene que decir `ninguno`, y el espacio libre tiene que ser mayor que el respaldo estimado. Si no, no sigas.

**Paso 2 · Respaldo y verificaciones** (solo si el paso 1 salió limpio):
```bash
bash <<'FIN'
cd ~/gta-shorts || exit 1
R=estandar-produccion/verificacion_etapa0.txt
B=~/respaldos/gta-shorts_2026-11-24
PROC="[Pp]ython[^ ]* (-u )?(estudio|movil|panel|diario|biblioteca|inteligencia|hooks|patrones|metricas|metricas_plus|fichas|lote)[.]py"
if pgrep -fl "$PROC" > /dev/null; then echo "DETENIDO: hay un proceso usando las bases. No se copio nada."; exit 1; fi
export PATH="$HOME/.local/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin:$PATH"
{
echo; echo "===== PASO 2 · RESPALDO Y VERIFICACIONES (Mac) · $(date) ====="
echo "== huella de las bases ANTES =="; shasum -a 256 datos/cerebro.db datos/inteligencia.db datos/metricas.db
echo "== respaldo =="
mkdir -p "$B"
rsync -a --exclude '/venv/' --exclude '/venv_chatter/' --exclude '/models/' \
  --exclude '/salida/' --exclude '/clips/' \
  --exclude '/tomas/' --exclude '/tomas_mdm/' --exclude '/tomas_rabbit/' \
  --exclude '/estudio_faceless/videos/' --exclude '__pycache__/' \
  ./ "$B/"
echo "rsync termino con codigo $?"
du -sh "$B"
echo "programas .py: origen $(ls *.py | wc -l) · respaldo $(ls "$B"/*.py | wc -l)"
echo "archivos en el respaldo: $(find "$B" -type f | wc -l)"
echo "== huella de las bases EN EL RESPALDO (debe ser igual a ANTES) =="
(cd "$B" && shasum -a 256 datos/cerebro.db datos/inteligencia.db datos/metricas.db)
echo "== huella de las bases DESPUES (debe ser igual a ANTES) =="
shasum -a 256 datos/cerebro.db datos/inteligencia.db datos/metricas.db
echo "== integridad (se revisa la copia del respaldo, no el original) =="
for d in cerebro inteligencia metricas; do
  echo "$d: $(sqlite3 -readonly "$B/datos/$d.db" 'PRAGMA integrity_check;' | head -3 | tr '\n' ' ')"
done
echo "== tablas y filas (copia del respaldo) =="
for d in cerebro inteligencia metricas; do
  echo "-- $d"
  for t in $(sqlite3 -readonly "$B/datos/$d.db" "SELECT name FROM sqlite_master WHERE type='table' ORDER BY 1;"); do
    echo "$t: $(sqlite3 -readonly "$B/datos/$d.db" "SELECT COUNT(*) FROM \"$t\";")"
  done
done
echo "== arsenal por estado, area y origen =="
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'estado', estado, COUNT(*) FROM arsenal GROUP BY 2;"
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'area', area, COUNT(*) FROM arsenal WHERE estado='activa' GROUP BY 2;"
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'origen', origen, COUNT(*) FROM arsenal GROUP BY 2;"
sqlite3 -readonly "$B/datos/cerebro.db" "SELECT 'con uso propio', COUNT(*) FROM arsenal WHERE usos > 0;"
echo "== fichas de la biblioteca por tipo y categoria =="
sqlite3 -readonly "$B/datos/inteligencia.db" "SELECT tipo, categoria, COUNT(*) FROM analisis GROUP BY 1, 2;"
echo "== videos con curva de retencion =="
sqlite3 -readonly "$B/datos/metricas.db" "SELECT COUNT(DISTINCT id) FROM retencion;"
echo "== entorno =="
echo "macOS $(sw_vers -productVersion) · $(uname -m)"
./venv/bin/python3 -V
for c in claude ffmpeg sqlite3 rsync; do echo "$c: $(command -v $c || echo FALTA)"; done
ffmpeg -version 2>&1 | head -1
echo "Chrome: $(defaults read '/Applications/Google Chrome.app/Contents/Info' CFBundleShortVersionString 2>&1)"
echo "== paquetes del entorno (sin importarlos) =="
./venv/bin/python3 -B -c "
import importlib.util as u, importlib.metadata as m
for mod, dist in [('playwright','playwright'),('kokoro_onnx','kokoro-onnx'),('onnxruntime','onnxruntime'),('soundfile','soundfile'),('numpy','numpy'),('PIL','pillow')]:
    print(mod, m.version(dist) if u.find_spec(mod) else 'FALTA')
"
echo "== modelos de voz =="; ls -lh models
} >> "$R" 2>&1
echo "Listo. Resultado en ~/gta-shorts/$R"
FIN
```
**Qué excluye el respaldo:** `venv`, `venv_chatter`, `models`, `salida`, `clips`, `tomas`, `tomas_mdm`, `tomas_rabbit`, `estudio_faceless/videos` y los `__pycache__`. Nada más.
La copia incluye `secretos/` y queda solo en tu Mac. Yo no la leo.

**Resultado:** todo queda en `estandar-produccion/verificacion_etapa0.txt`, a continuación de lo que yo verifiqué desde aquí.

#### Resultado del primer intento (24-nov, 08:23–08:35)
| Punto | Resultado |
|---|---|
| Ejecutar en el Mac | **No pude.** Mi consola del Mac sigue fallando, y escribir en la Terminal me está bloqueado por diseño |
| ¿Algo escribiendo en las bases? | **Sí.** La corrida diaria empezó a las 08:30 y escribió en `inteligencia.db` a las 08:32. Me detuve ahí |
| Respaldo | No hecho |
| Integridad de las bases | Sin revisar (no copié nada mientras se escribía) |
| Chrome | Instalado |
| Voz (`kokoro_onnx` 0.6.1, `onnxruntime`, `soundfile`, `numpy`, Pillow) | Instalados en el entorno |
| Modelos de voz | Presentes en `models/` (325 MB y 28 MB) |
| **`playwright`** | **Falta en el entorno.** El render lo necesita |
| `ffmpeg`, `claude`, `sqlite3` | Sin comprobar desde aquí; los revisa el paso 2 |

#### Resultado final de la etapa 0 (24-nov, 09:12) · COMPLETA
| Punto | Resultado |
|---|---|
| Procesos al momento del respaldo | Ninguno. La corrida diaria había terminado a las 08:58 |
| **Respaldo** | **Hecho:** `~/respaldos/gta-shorts_2026-11-24`, 1,5 GB, 4.079 archivos, 248 programas `.py` de 248 |
| Copia idéntica | La huella sha256 de las tres bases coincide antes, en la copia y después |
| **Integridad** | `cerebro.db`, `inteligencia.db` y `metricas.db`: **ok** las tres |
| Originales | Sin cambios (misma huella antes y después) |
| Entorno | macOS 26.6.1 (arm64) · Python 3.12.16 · ffmpeg 9.0.2 · Chrome 158 · `claude`, `sqlite3` y `rsync` presentes |
| Paquetes | `kokoro_onnx` 0.6.1, `onnxruntime` 1.31.1, `soundfile` 0.14.0, `numpy` 2.5.4, Pillow 13.0.0 |
| **Falta** | **`playwright`** (única dependencia faltante) |

**Qué hay hoy en el cerebro (línea base):**
| Dato | Valor | Lectura |
|---|---|---|
| Piezas del arsenal | 32, todas activas | 21 son de títulos; 7 de psicología; 1 de gancho; 1 de estructura |
| Origen de las piezas | 26 externas, 4 transversales, 2 propias | Casi todo viene de mirar a otros |
| **Piezas con uso propio registrado** | **0** (`arsenal_usos` vacía) | El ciclo de aprender de lo propio nunca se ha cerrado |
| Experimentos | 5 definidos, 0 videos asociados | Ninguno llegó a medirse |
| Reglas | 38 | — |
| Fichas de la biblioteca | 1.065: 771 de Shorts (288 de control) y 294 de largos | Los largos se estudiaron como fuente para Shorts, no como narrativa |
| Videos propios con curva de retención | 40 | Materia prima para la etapa 7 |

**Hallazgo para la etapa 1:** `escena/render.py` y `escena/voz_local.py` **ya están en el Mac, pero con rutas de mi espacio de trabajo** (Chrome de Linux y carpeta de modelos de la nube). Tal como están no pueden correr en el Mac. O sea: el motor de escenas animadas, vertical y horizontal, hoy solo funciona en la nube.

**Otro riesgo:** la corrida diaria actualiza `yt-dlp` cada mañana dentro del mismo entorno. El entorno cambia solo todos los días.

**0.3 Línea base de generación** (yo, en mi espacio de trabajo, sin tocar el Mac): guardo los cuadros de una muestra de 20 s de un largo existente. Sirve para comprobar, después de cada etapa, que el motor produce exactamente lo mismo.
**Pendiente de definir contigo:** la prueba equivalente para un Short. No la invento sin leer antes el script de render del Mac.

### Etapa 1 · Traer el motor de largos al Mac
| | |
|---|---|
| **Qué** | Copiar a `~/gta-shorts/largos/` los 14 scripts y el motor horizontal. No cambia su comportamiento |
| **Ajustes necesarios (ya identificados)** | El render busca Chrome en una ruta de Linux; en el Mac es otra · La voz busca los modelos en una ruta de mi espacio de trabajo · **`playwright` no está en el entorno del Mac:** hay que instalarlo (con tu OK) o cambiar la forma de manejar Chrome · Lo mismo aplica a `escena/render.py` y `escena/voz_local.py`, que ya están en el Mac |
| **No toca** | Nada de lo que hoy usa el Estudio para Shorts |
| **Verificación** | Renderizar en el Mac la misma muestra de 20 s y comparar con la línea base |
| **Deshacer** | Borrar la carpeta `largos/` |
| **Esfuerzo** | 1,5–2 h |
| **Riesgo** | Diferencias de tipografías o de versión de Chrome entre Linux y Mac pueden cambiar algún cuadro. Se revisa a ojo |

### Etapa 2 · Modelo de la biblioteca
| | |
|---|---|
| **Qué** | Columnas nuevas en `arsenal` (función, tensiones, variaciones, alcance, canal, formato, escalón, nivel externo, conteo en normales) · tablas nuevas `elementos`, `mecanismos`, `evidencia`, `codigos` · tramo y predicción en `arsenal_usos` |
| **Carga** | Los mecanismos del doc 18 como origen "externo" · cada pieza actual del arsenal recibe su escalón real (la mayoría quedará en "observado", sin control) |
| **No toca** | Ninguna columna ni tabla existente |
| **Verificación** | Regenerar `arsenal_guionista.md` y `reglas_vigentes.md` antes y después: tienen que salir **idénticos**. Así se prueba que la generación actual no cambió |
| **Deshacer** | Restaurar `cerebro.db` del respaldo |
| **Esfuerzo** | 2–3 h |

### Etapa 3 · Estudiar largos
| | |
|---|---|
| **Qué** | Modo largo en `biblioteca.py`: segmentación por eventos, libro de códigos, justificación obligatoria, elementos con su tipo de afirmación |
| **Depende de** | La calibración (Parte C): el libro de códigos entra ya corregido |
| **Compuerta** | Un código que no esté "fiable" no pasa a Comparar |
| **Verificación** | El modo Short sigue produciendo la misma ficha para un video ya analizado |
| **Esfuerzo** | 3 h |

### Etapa 4 · Primera tanda
| | |
|---|---|
| **Qué** | Estudiar los pares aprobados de la Parte D |
| **Cómo** | Por tramos, de a 2 videos, con pausas, para no calentar el Mac |
| **Esfuerzo** | 3–4 h de proceso, repartidas |
| **Resultado** | Casos y elementos reales. Es también la primera prueba de verdad del método |

### Etapa 5 · Comparar
| | |
|---|---|
| **Qué** | Tabla de presencia en destacados y en normales · escalera · fichas de patrón · unificación de `patrones.py`, `hooks.py` y `ganchos.py` sobre la misma biblioteca |
| **Verificación** | Ningún patrón sube de escalón sin cumplir su requisito; se revisa una muestra a mano |
| **Esfuerzo** | 2 h |

### Etapa 6 · Aplicar
| | |
|---|---|
| **Qué** | Diagnóstico de la historia (A.3) · consulta a la biblioteca en vez de archivos cortados · diversidad · exploración controlada (A.2) · registro de decisiones |
| **Dónde** | `lote.py`, `storyboard.py` y el motor de largos |
| **Verificación** | Un Short y un largo de prueba, comparados con los que salen hoy. Los revisas tú |
| **Deshacer** | Un interruptor vuelve al método actual |
| **Esfuerzo** | 3–4 h |

### Etapa 7 · Aprender
| | |
|---|---|
| **Qué** | Cruce de decisiones, planos y curva de retención · estudio obligatorio de los videos bajo lo típico · cambio de escalón con evidencia propia |
| **Depende de** | Videos publicados con vistas suficientes |
| **Esfuerzo** | 2–3 h |

**Total con código: 17–21 h, en 7–9 sesiones.** Las etapas 0, C y D no tocan código y pueden hacerse ya.

---

## C. Protocolo de calibración
### C.1 Qué vamos a hacer
1. **Yo segmento** cada video por eventos y te entrego la lista de tramos con sus tiempos.
2. **Los dos codificamos por separado**, sin ver lo del otro. Yo dejo mi codificación guardada antes de recibir la tuya.
3. **Comparo código por código** y te muestro dónde coincidimos y dónde no.
4. **Discutimos los desacuerdos.** Tres salidas posibles: yo interpreté mal · el código está mal definido · los dos tenemos razón y el código hay que partirlo en dos.
5. **Se corrige el libro de códigos** y se repite sobre un tercer video si hace falta.

### C.2 Qué codificas tú
Para cada tramo, una opción por dimensión (formulario de selección, sin escribir):
| Dimensión | Opciones |
|---|---|
| Función del tramo | Abrir · situar · avanzar · complicar · girar · respirar · pagar · reflexionar · cerrar |
| Movimiento del enigma | Plantear · prometer respuesta · demorar · despistar · responder a medias · suspender · revelar · ninguno |
| Quién sabe más | El público menos · igual · más que el protagonista · no aplica |
| A qué apunta | Comprensión · atención · emoción · presencia |
| Relación de la imagen con la voz | Muestra · anticipa · contradice · adorna |
| Cambio de evento | Sí · no |
| Sonido con función | Sí (cuál) · no |

Además, una pregunta abierta por video: **¿en qué momento te dieron ganas de irte, y en cuál no podías dejar de mirar?** Es el dato más valioso, y no depende de ningún código.

### C.3 Cómo se mide el acuerdo
| Medida | Para qué |
|---|---|
| % de coincidencia por dimensión | Vista general |
| Acuerdo corregido por azar, por dimensión | Coincidir por casualidad es fácil cuando hay pocas opciones |
| Acuerdo por código | Entre los tramos donde alguno de los dos usó ese código, en cuántos coincidimos |
| Tabla de confusiones | Qué códigos se confunden entre sí (por ejemplo, "demorar" con "suspender") |

**Clasificación (provisional, por convención habitual en análisis de contenido; con tan pocos tramos es solo orientativa):**
| Estado | Criterio |
|---|---|
| Fiable | Coincidimos casi siempre y las confusiones son raras |
| Dudoso | Coincidimos la mayoría de las veces, con una confusión sistemática identificable |
| No fiable | Coincidimos poco, o cada uno lo entiende distinto |
| Sin calibrar | Apareció muy pocas veces para decir algo |

No pongo un umbral numérico fijo: con 40–50 tramos, un porcentaje exacto daría una precisión que no existe. Te muestro los números y la tabla de confusiones, y decidimos código por código.

**Advertencia:** coincidir no garantiza tener razón. Si los dos compartimos un sesgo, coincidiremos igual. Por eso la pregunta abierta y, más adelante, los datos de retención.

### C.4 Cuánto tiempo te toma (corrijo mi estimación anterior)
Dije 30–40 min. **Era poco:** para codificar la función de un tramo hay que ver el video entero.
| Opción | Qué | Tu tiempo |
|---|---|---|
| **A (recomendada)** | 2 videos completos de 11–13 min, unos 20–25 tramos cada uno | 50–60 min |
| B | 3 videos | 75–90 min |
| C (liviana) | 1 video completo y los primeros 3 min de otros dos | 35–40 min. Calibra bien las aperturas y poco el resto |

### C.5 Videos propuestos para calibrar
Tres tipos distintos, de duración parecida a la que queremos producir. Con la opción A, los dos primeros.
| # | Video | Tipo | Duración |
|---|---|---|---|
| 1 | Company Man · "Gatorade vs. Powerade" | Explicación de negocios | 13 min |
| 2 | toldinstone · "Three Unfinished Roman Megaprojects" | Historia narrada | 12 min |
| 3 | Kurzgesagt · "Astronomy Is In Crisis...And It's Incredibly Exciting" | Educación animada | 11 min |

---

## D. Selección de referencias para tu revisión
> ⚠️ **Sin efecto desde el 24-nov, 12:09.** Tao pidió estudiar canales faceless que estén teniendo éxito y Shorts virales, no canales famosos. La nueva población está en el doc 22, sección 5.
### D.1 Cómo se eligió, y sus límites
- **Datos reales, tomados hoy** de la página de videos de cada canal: título, vistas (redondeadas por YouTube), antigüedad y duración.
- **Destacado** = el más visto entre los videos elegibles del canal. **Normal** = el más cercano a la **mediana** del canal, con duración parecida.
- **Elegibles:** de 5 a 40 min y con 2 meses o más.
- **La elección de canales es juicio mío** (nivel D): canales reconocidos por su construcción narrativa o visual. **No vi ninguno de estos videos**; no puedo afirmar que sean buenos referentes hasta estudiarlos.
- **Lo que el par controla:** el tamaño del canal. **Lo que no controla:** el tema ni la miniatura. Y vistas no es retención.
- **Canales descartados por formato:** Vox, MrBallen, Kings and Generals, The Infographics Show (sus videos recientes duran más de 40 min o son compilados); Veritasium y Johnny Harris (casi no hay diferencia entre su destacado y su mediana, y duran 26–40 min).

### D.2 Tanda 1 propuesta: 10 pares, 8 disciplinas
| # | Disciplina | Canal (suscriptores) | Destacado | Normal | Veces la mediana |
|---|---|---|---|---|---|
| 1 | Empresas y documentales | **Company Man** (1,8 M) | "Gatorade vs. Powerade" · 629 k · 2 meses · 13 min | "Dollar Tree - The Rise and Fall?" · 159 k · 4 meses · 12 min | 4,0 |
| 2 | Empresas y documentales | **MagnatesMedia** (1,86 M) | "The INSANE Truth About IKEA" · 2,3 M · 2 años · 31 min | "The Banana Billionaire: The INSANE True Story" · 639 k · 3 años · 21 min | 3,6 |
| 3 | Misterios e investigación | **fern** (5,72 M) | "The Most Disgusting Influencer Campaign of 2026" · 11,0 M · 2 meses · 21 min | "The Dark Web's New Deadliest Drug" · 4,7 M · 5 meses · 27 min | 2,3 |
| 4 | Misterios e investigación | **neo** (3,05 M) | "How the U.S. Found Saddam Hussein" · 16,0 M · 1 año · 21 min | "The Deepwater Horizon Disaster" · 5,8 M · 1 año · 24 min | 2,8 |
| 5 | Historia | **toldinstone** (653 k) | "Three Unfinished Roman Megaprojects" · 927 k · 2 meses · 12 min | "The Decline and Fall of Sparta" · 101 k · 8 meses · 11 min | 9,2 |
| 6 | Ciencia y tecnología | **Practical Engineering** (4,85 M) | "Stopping the Unstoppable" · 5,6 M · 2 meses · 16 min | "Hurricane vs. Tiny Houses" · 1,1 M · 11 meses · 22 min | 5,1 |
| 7 | Educación animada | **Kurzgesagt** (25,8 M) | "This Woman Cured Her Cancer with an Insane Method" · 21,0 M · 2 meses · 15 min | "Astronomy Is In Crisis...And It's Incredibly Exciting" · 6,3 M · 11 meses · 11 min | 3,3 |
| 8 | Psicología | **Pursuit of Wonder** (3,52 M) | "Game Theory: A Simple Strategy That Will Change Your Life Forever" · 2,8 M · 1 año · 18 min | "Yes, You Will Die. But What Happens Next Is Worse." · 299 k · 10 meses · 12 min | 9,4 |
| 9 | Ensayos audiovisuales | **Nerdwriter1** (3,24 M) | "How Marlon Brando Changed Acting" · 1,2 M · 1 año · 10 min | "Two Ways To Film The Same Scene (#2)" · 192 k · 1 año · 11 min | 6,3 |
| 10 | Entretenimiento narrativo | **TierZoo** (3,95 M) | "Are Scorpions Overpowered?" · 14,0 M · 4 años · 10 min | "Are Centipedes OP?" · 2,4 M · 2 años · 14 min | 5,8 |

**Por qué dos canales en empresas y en misterios:** son las disciplinas más cercanas a Million Dollar Mistake y a The Rabbit Loop.

### D.3 Pares más limpios y más débiles
| Calidad del par | Pares | Por qué |
|---|---|---|
| **Limpios** (misma época y duración parecida) | 1, 4, 5, 9 | La diferencia de vistas no se explica por antigüedad ni por largo |
| Aceptables | 3, 6, 7, 8 | Antigüedad o duración algo distintas |
| **Débiles** | 2, 10 | Años de diferencia entre los dos videos: el más antiguo tuvo más tiempo para sumar vistas |

### D.4 Reserva (para cambiar o ampliar)
| Disciplina | Canal | Destacado · Normal | Nota |
|---|---|---|---|
| Empresas | Wendover Productions | "How the Channel Tunnel Works" 2,3 M · "How Nike Lost Its Way" 1,1 M | Temas muy distintos entre sí |
| Empresas y tecnología | ColdFusion | "OpenAI is Suddenly in Trouble" 2,2 M · "How The Internet's Favourite AI Employee Went Rogue" 919 k | — |
| Misterios | Thoughty2 | "This 800-Year-Old Book Has a Page Nobody Can Explain" 2,6 M · "There's a 2,500 Mile Hedge in India and Nobody Told You" 606 k | Par limpio; temas cercanos a Rabbit; presentador a cámara |
| Misterios | LEMMiNO | "Cicada 3301: An Internet Mystery" 43 M · "Consumed by the Apocalypse" 7,0 M | Referente del género, pero videos de hace 5 y 8 años |
| Historia | Extra History | "The History of Perfume…" 464 k · "Where Did Playing Cards Come From?" 226 k | Animado; par limpio; poca diferencia |
| Tecnología | New Mind | "The Forbidden Knowledge of Washers" 2,6 M · "The Science Of Engine Oils" 279 k | Par muy limpio (misma época y duración) |
| Tecnología | Real Engineering | "NASA'S Plutonium Problem" 4,1 M · "How We Built The ISS" 1,6 M | — |
| Educación animada | CGP Grey | "There's No Crying in Flag Design" 20 M · "Why Runways Have to Be Repainted" 4,1 M | — |
| Educación animada | TED-Ed | "4 ways to fix your attention span" 4,7 M · "Plato's infamous Ship of State thought experiment" 583 k | Duran 5–6 min |
| Psicología | Academy of Ideas | "Carl Jung and The Most Important Rule of Life" 811 k · "Why Men Fear Women" 77 k | — |
| Ensayos | Every Frame a Painting | "Jackie Chan - How to Do Action Comedy" 25 M · "Vancouver Never Plays Itself" 2,1 M | Par de la misma época (hace 11 años); el contenido mismo enseña lenguaje visual |
| Entretenimiento | SunnyV2 | "He Went On Joe Rogan... Then Killed Someone 38 Days Later" 9,0 M · "The Unexpected Flop Of Lazarbeam's Video Game" 3,1 M | 9 min cada uno |

### D.5 Dos pares extra, de nuestros propios nichos (opcionales)
| Para | Canal | Destacado | Normal | Veces |
|---|---|---|---|---|
| Dog y Cat Decoded | Animalogic (2,15 M) | "There's No Such Thing As A Giraffe" · 205 k · 2 meses · 21 min | "Dogs Almost Went Extinct And Were Saved By This Underdog" · 47 k · 3 meses · 21 min | 4,4 |
| Coffee But Why? | James Hoffmann (2,58 M) | "The Truly Absurd Secrets of An Incredible Americano" · 1,8 M · 6 meses · 25 min | "Wendougee: The Most Interesting Manufacturer in China?" · 731 k · 6 meses · 33 min | 2,5 |

### D.6 Una advertencia que sale de estos mismos datos
En el doc 18 anoté, como pista, que los títulos vagos aparecían entre los menos vistos. **Aquí hay un caso en contra:** el destacado de Practical Engineering se llama "Stopping the Unstoppable", que es un hueco puro, sin nombrar nada. Es justo la razón por la que nada sube de escalón por unos pocos títulos.

### D.7 Lo que necesito que decidas sobre la selección
1. ¿Los 10 pares, o prefieres cambiar alguno por uno de la reserva?
2. ¿Sumamos los dos pares de nuestros nichos (serían 12 pares, 24 videos)?
3. ¿Algún canal que tú consideres referente y que no esté?
4. **Tu visto bueno para bajar estos videos solo para estudio** (transcripción, fotogramas y cortes), como ya hace `laboratorio_faceless.py`. Material ajeno: se usa para entender, nunca se reutiliza.

---

## E. Qué sigue, en orden
| # | Quién | Qué |
|---|---|---|
| 1 | Tú | Correr la etapa 0 (respaldo y verificaciones) |
| 2 | Yo | Leer `verificacion_etapa0.txt` y decirte qué encontré |
| 3 | Tú | Elegir opción de calibración (A, B o C) y revisar la selección (D.7) |
| 4 | Los dos | Calibración |
| 5 | Yo | Libro de códigos corregido y plan de la etapa 1 en detalle, con aviso antes de tocar nada |
