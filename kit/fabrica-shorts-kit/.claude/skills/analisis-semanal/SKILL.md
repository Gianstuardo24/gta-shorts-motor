---
name: analisis-semanal
description: Leer el reporte semanal de métricas y decidir por canal (se queda / ajustar / nicho de reserva) con la regla del PLAYBOOK. Úsala los domingos o cuando pregunten cómo van los canales.
---

# Análisis semanal

1. Actualiza los datos y genera el reporte:
   ```zsh
   ./venv/bin/python3 metricas/metricas.py && ./venv/bin/python3 metricas/metricas_plus.py && ./venv/bin/python3 metricas/fichas.py && ./venv/bin/python3 metricas/reporte_semanal.py
   ```
   Si falla por permisos vencidos, dile a la persona que corra `./venv/bin/python3 metricas/metricas.py --autorizar`. No lo hagas tú.
2. Lee `analisis/reporte_<fecha>.md`.
3. Por canal, explica **en 3 líneas**:
   - la decisión;
   - **por qué**: cuál de las 3 cifras movió la aguja;
   - **una sola** acción para la semana: cambiar gancho, fórmula u hora, o pasar a un nicho de reserva.
4. Usa la ficha (gancho, formato, voz) de los mejores y peores para decir **qué** repetir y qué evitar.
5. Cuidado con las conclusiones:
   - menos de 3 videos → no se decide;
   - <20 vistas a 24 h → primero revisar distribución en Studio;
   - un cambio cuenta solo si da ≥1,5× la mediana en 2 de 3 videos.
6. Si la persona aprueba un cambio, **avísale qué archivo vas a cambiar** (`canales/<id>.json` o `planes/<id>.md`) y hazlo.
