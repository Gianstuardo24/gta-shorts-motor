# pruebas/ · Red de seguridad del motor (E0, 26-nov-2026)

> Creado en la etapa **E0 · Base segura** del plan 27d. Sirve para comprobar que ningún cambio altera lo que ya existe.
> **Regla:** el corpus y las líneas base **no se modifican sin la autorización de Tao**.

## Qué hay
| Carpeta o archivo | Qué es | ¿En git? |
|---|---|---|
| `corpus/manifiesto.json` | Lista de referencias congeladas, con origen y suma sha256 de cada archivo | Sí |
| `corpus/produccion/<slot>/` | Los 7 videos entregados el 25-nov: `datos_render.json` (los datos **exactos** con que se renderizaron, copiados de la carpeta temporal del render), guion, `b.py`, voz, palabras y planos | Sí |
| `corpus/planos/<04,05,06,10>/` | Planos aprobados: datos, voz, palabras, generador y datos de testigo | Sí |
| `corpus/motor_entrega_25nov/` | El motor con que se renderizaron los 7 videos (sha256 `75bb7c44…`, igual a `escena.html.bak_p27_paso0`) | Sí |
| `referencias_video/` | Los videos entregados y aprobados (≈209 MB) | **No**: van al respaldo fechado |
| `lineas_base/` | Huellas de referencia: `rapido_*.json`, `completo_*.json` y `camino_real/*.framemd5` | Sí |
| `informes/` | Resultados de las comparaciones de la E0 | Sí |
| `regresion.py` | Comparación con semilla fija, niveles **rápido** y **completo** | Sí |
| `render_semilla.py` | Corre `escena/render.py` **sin modificarlo**, con semilla fija (D4: solo pruebas) | Sí |
| `comparar_entregados.py` | Control de cordura con tolerancia contra los videos entregados | Sí |
| `datos_pipeline.py` | Comparación de **datos**: `resolver.py` → `post.py` → `planos_shorts.py` sobre entradas congeladas; el guion final y `planos.log` tienen que salir idénticos byte a byte | Sí |
| `cadena_e0.sh` | Las comparaciones largas de la E0, en orden (registro en `informes/cadena_e0.log`) | Sí |
| `respaldar.sh` · `verificar_respaldo.sh` · `comprobar_respaldo.sh` | Arman el respaldo fechado, lo restauran en una carpeta nueva y lo comprueban (el tercero viaja dentro del respaldo y no depende del contenedor) | Sí |
| `congelar_corpus.py` | Cómo se armó el corpus (se corrió una sola vez) | Sí |
| `entorno.txt` | Versiones del sistema, del navegador, de ffmpeg y de Python | Sí |

## Cómo se usa
```bash
cd /home/claude/pruebas
# rápido (≈1,5 min, 521 cuadros): después de CADA cambio
flock /tmp/render.lock python3 regresion.py --nivel rapido --base lineas_base/rapido_motor_725e0dba.json
# completo (≈23 min, 11.376 cuadros): al cierre de cada etapa
flock /tmp/render.lock python3 regresion.py --nivel completo --base lineas_base/completo_motor_725e0dba.json
# con imágenes de los cuadros distintos para diagnosticar
... --diferencias informes/diferencias
# datos del pipeline (segundos, no renderiza): cuando se toque resolver.py, post.py o planos_shorts.py
python3 datos_pipeline.py
# respaldo fechado y prueba de recuperación
./respaldar.sh ETIQUETA && ./verificar_respaldo.sh /home/claude/.respaldos/<fecha>_ETIQUETA prueba
```
- La salida es **0** si todo es idéntico y **1** si cambió algún cuadro.
- Nunca dos renders a la vez: siempre con `flock /tmp/render.lock`.

## Qué significa "idéntico"
La huella es SHA-256 de los **píxeles** del lienzo en cada instante, con `Math.random` reemplazado por una semilla fija solo dentro de la herramienta. El motor solo usa `Math.random` en el grano del acabado "pro".
