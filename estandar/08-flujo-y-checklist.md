# 08 · Flujo de trabajo y checklist

## Orden de trabajo
1. **Tema y ángulo** (`banco-angulos-virales-23-nov.md`) + **toque propio** del video (`09`).
2. **Investigación:** 2 fuentes o más por dato.
3. **Guion pensado para lo visual** (`02`) + **mapa de espacios** (un espacio por capítulo, máximo 5 regresos) + lista de insertos y gráficos.
4. **Voz:**
   ```
   python3 escena/voz_local.py src.json vz.wav <voz> <vel> <lang>
   python3 compactar_voz.py vz_orig.wav vz_palabras_orig.json frases.json 1.18 vz.wav vz_palabras.json
   ```
5. **`b.py` del video:** tramos, actores, props, insertos, `L.hints`. Antes del `json.dump`:
   ```
   g["escena"]["escenas"][0]["planos_hint"] = L.hints
   ```
   Sets nuevos se prueban con:
   ```
   T=1.4 python3 escena/probar_sets_h.py datos.json out.png set1 'set2:{"op":1}'
   ```
6. **Armar** (voz → tiempos → resolver → recortar insertos → planos automáticos → datos.json):
   ```
   /home/claude/rearmar_largo.sh <carpeta> <ID>
   ```
7. **Revisar** (los 3 son obligatorios):
   ```
   python3 /home/claude/revisar_insertos.py <carpeta>/datos.json
   python3 /home/claude/revisar_largo.py <carpeta>/datos.json /tmp/rev
   python3 /home/claude/hoja_planos.py <carpeta>/datos.json /mnt/user-data/outputs/<id>_planos 30
   ```
8. **Muestra de 90 s** y **hoja de planos → OK de Tao**.
9. **Render final** (nunca en paralelo con otra prueba):
   ```
   PARTES=2 /home/claude/render_largo.sh guion_final.json vz.wav vz_palabras.json out.mp4 <estilo>
   ```
10. **Miniaturas A/B/C + .txt + Test & Compare → Estudio** (`07`).

## Checklist antes del render final
- [ ] Ningún plano en escenario dura más de 4,5 s; promedio ~2,5–3,5 s.
- [ ] Tiempo fuera de los escenarios ~35–45 %.
- [ ] Espacios: máximo 5 regresos en todo el video, y cada regreso trae algo nuevo.
- [ ] Insertos: todos distintos, salvo los regresos a propósito marcados; cada uno calza con su frase.
- [ ] Ningún inserto pegado a otro ni cruzando un cambio de tramo (`revisar_insertos.py` limpio).
- [ ] Pantallas y efectos: distintos entre sí y fieles al contenido.
- [ ] Gráficos: entran antes de la palabra clave y duran lo suficiente para leerse.
- [ ] Franja de subtítulos libre y ningún texto encima de otro (`revisar_largo.py` sin avisos).
- [ ] Personajes: entran desde fuera del cuadro; caminando solo de vez en cuando; manos delante de la cara; codos abajo.
- [ ] Transiciones: sin flash, papel, tinta ni barrido brusco; mismo lugar = deslizamiento suave.
- [ ] Inicio sin el mundo de GTA de fondo.
- [ ] Intro, capítulos, título y portada no revelan el pago.
- [ ] Cada inserto nuevo tiene sonido.
- [ ] Ningún set propio de otro video.

## Checklist antes de entregar
- [ ] Ver la hoja de contacto del render (1 cuadro cada 8 s) y los regresos a propósito.
- [ ] Volumen (`volumedetect`): sin picos raros.
- [ ] `.txt` con título, descripción, capítulos, fuentes y 4–5 hashtags, sin "VIDEO RELACIONADO".
- [ ] 3 títulos y 3 miniaturas para Test & Compare.
- [ ] Archivos en `<canal>/Nuevos Largos/` con el formato del Estudio.

## Tiempos reales (para estimar sin inflar)
| Tarea | Tiempo observado |
|---|---|
| Investigación y guion verificado (10–12 min) | ~35 min |
| Voz | ~15 min |
| Sets nuevos | ~8–10 min cada uno |
| Insertos nuevos | ~5 min cada uno (8 en ~40 min) |
| `b.py` + armado + revisión + hoja de planos | ~30–40 min |
| Muestra de 90 s | ~7 min |
| Render final de 6–9 min | ~18–25 min |
| Miniaturas A/B/C | ~15 min |
| **Largo nuevo con el motor actual** | **~1 h si no necesita sets nuevos; ~2,5–3 h con sets e insertos nuevos** |
| 5 largos encadenados (23-nov) | ~2 h 20 min en total |

## Límites conocidos
- El servidor tiene **2 CPU**. El render final ya corre en 2 partes; no se puede acelerar más.
- Código del motor (`escena_h.html`, `planos.js`, `largo.py`, `planos_tiempo.py`): **se avisa a Tao antes de cambiarlo** y siempre se deja un respaldo `.bak_<fecha>_<tema>`.
- Lo que está dentro de `/*PLANOS_INI*/…/*PLANOS_FIN*/` en `escena_h.html` se edita en `planos.js` y después se corre `bash sync_planos.sh`.
