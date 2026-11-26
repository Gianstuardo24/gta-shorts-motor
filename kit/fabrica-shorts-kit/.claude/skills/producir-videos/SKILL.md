---
name: producir-videos
description: Escribir los guiones y producir los videos de un día para uno o más canales (guion → video + portada + .txt), dejándolos en el Estudio. Úsala con pedidos como "haz los videos de mañana" o "produce 2 de perros".
---

# Producir videos

## Antes

- Lee `PLAYBOOK.md`, `motor/GUIA-MOTOR.md`, el `canales/<id>.json` y `planes/<id>.md` del canal.
- Revisa qué se publicó antes en la carpeta de salida y en `guiones/`, para **no repetir tema**.
- Si existe `analisis/reporte_*.md`, lee el último: lo que funcionó manda.

## Por cada video

1. **Tema:** uno del plan (o nuevo, dentro del micronicho). Busca **2+ fuentes** en la web y anótalas en `fuentes` y `nota_datos`.
2. **Guion** en `guiones/<AAAA-MM-DD>/<id>-<HH>h.json`. Copia la forma de `plantillas/guion-ejemplo.json`.
   - 6–8 frases. Gancho con objeto concreto. Remate al 70–90 %. Penúltima: "Tell me…" / "Comenta…". Última: `cta_voz` del canal.
   - Título con la `formula_titulo`, ≤40 caracteres. `descripcion`: 1–2 frases que insinúan.
   - Escena `pelicula` con el protagonista del canal **haciendo cosas** en cada idea; zonas con decorados distintos.
3. **Revisa los cuadros** antes de renderizar:
   ```zsh
   ./venv/bin/python3 motor/producir.py guiones/<día>/<id>-<HH>h.json --canal <id> --dia <día> --hora <HH> --muestras 1 4 8 12 16 20
   ```
   Abre `datos/trabajo/<lote>/muestras.png`. Corrige si algo choca, se corta o no se entiende.
4. **Renderiza** (sin `--muestras`). Los videos se hacen **de a uno**, nunca dos a la vez.
5. **Confirma:**
   - que existan el `.mp4`, el `.txt` y la `.portada.jpg`;
   - mira la portada;
   - el `.txt` no lleva comentario fijado ni "video relacionado".

## Al terminar

Dile a la persona, breve:
- qué videos quedaron (canal · hora · título);
- que recargue el Estudio (Cmd+R);
- cualquier dato que sea estimación.

Espera su feedback **antes** de producir el día siguiente.
