---
name: subir-videos
description: Subir y programar en YouTube los videos de un día con metricas/subir_youtube.py. Úsala cuando pidan subir o programar videos. Siempre con OK explícito de la persona.
---

# Subir videos

1. **Vista previa** (no sube nada):
   ```zsh
   ./venv/bin/python3 metricas/subir_youtube.py --dia <AAAA-MM-DD>
   ```
2. Muestra la lista a la persona: canal · hora · título y los ⛔ con su motivo.
3. **Pide un OK explícito** para subir esa lista exacta. Sin OK, no subes.
4. Con OK:
   ```zsh
   ./venv/bin/python3 metricas/subir_youtube.py --dia <AAAA-MM-DD> --subir
   ```
   - Agrega `--ahora` solo si la persona quiere publicar al tiro los atrasados.
5. Reporta los links y la hora en que sale cada uno.
6. Si dice "sin permiso" o "venció", la persona corre `./venv/bin/python3 metricas/subir_youtube.py --autorizar` (ver `GUIA-INICIO.md` §5). **Tú no tocas `secretos/`.**
