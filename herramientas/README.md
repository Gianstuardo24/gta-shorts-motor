# herramientas/ · Inspección del motor (E1, 26-nov-2026)

> Etapa **E1** del plan 27d. **Solo leen**: no corrigen, no modifican ni sobrescriben escenas, configuraciones, renders ni el motor. No cambian producción (todavía no están conectadas al pipeline; eso es la E3).
> Modo **aviso**: informan y salen con 0. `--estricto` (salir con 1 si hay errores) existe para etapas futuras y no se usa.

| Herramienta | Qué hace |
|---|---|
| `claves.py` | Réplica exacta de `tk()` del motor (cómo resuelve las claves de tiempo) y **mapa de los campos** con claves, sacado del código del motor `725e0dba` |
| `validar.py` | **Validador de claves de tiempo.** Errores: clave inexistente (el motor usaría el inicio de la escena en silencio), desplazamiento mal escrito, número escrito como texto, tipo inválido, inicio de escena irresoluble, efecto del cierre sobre `s_fin`. Avisos: algo que empieza cuando la escena ya no se ve, fin antes del inicio, escenas desordenadas, **cortes de zona y de cámara desfasados** (cuadros con encuadre intermedio). Info: tiempos antes del inicio de su escena |
| `validar.py --cobertura` | Compara los usos de claves del motor con la foto `campos_motor.json`: avisa si el motor empieza a usar claves en un lugar que el mapa no conoce |
| `saltos.py` | **Detector de cuadros aislados.** Revisa todos los cuadros de un video: islas de 1 o 2 cuadros que no se parecen a lo de antes ni a lo de después. Con `--datos`, revisa además los cuadros intermedios que predice el validador en cada corte. Informe, tiras de imagen y estado "revisar" u "ok" |

## Uso
```bash
cd /home/claude/herramientas
python3 validar.py datos.json                       # producción (render desde 0)
python3 validar.py --t0 0.15 datos.json             # planos de prueba (render desde 0,15 s)
python3 validar.py --detalle datos.json             # muestra también los informativos
python3 validar.py --cobertura                      # ¿el motor usa claves en un lugar nuevo?
python3 saltos.py video.mp4 --datos datos.json --salida /tmp/tiras   # con los datos del render: más preciso
python3 saltos.py video.mp4                         # sin datos: solo islas claramente aisladas
```
- El validador revisa los **datos que recibe el motor** (los que arma `armar_escena.py`), no el guion `{ID}.json`, que tiene otra forma.

## Pruebas (en `pruebas/`)
| Prueba | Qué comprueba |
|---|---|
| `mutaciones_claves.py` | 17 errores puestos a propósito en copias de los datos congelados: todos detectados |
| `cruce_claves_motor.py` | El validador contra el **motor real** (su `tk()` envuelto solo en la memoria de la página): 0 falsos negativos |
| `evaluar_saltos.py` | El detector sobre los 7 videos entregados, los 4 planos aprobados y el plano 10 v2 |
| `pruebas_saltos.py` | 8 alteraciones en memoria de cuadros aprobados (cuadro ajeno, dos seguidos, mezclas, repetido, destello) |
