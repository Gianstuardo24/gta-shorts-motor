# Guía de inicio · Fábrica de Shorts (Mac)

**Qué es:** una fábrica de Shorts **animados por código**, sin cara y sin material ajeno.
- Tu Claude conversa contigo para definir el canal, escribe los guiones, produce los videos y los deja en una página (el **Estudio**) desde donde los copias, los descargas o los subes.
- Después mide qué funcionó y lo usa para la semana siguiente.

**Necesitas:**
- un Mac (Apple Silicon o Intel), ~3 GB libres;
- **Claude Code** (plan Pro o Max);
- una cuenta de Google con tu canal de YouTube.

---

## 1. Instalar (una vez, ~10 min)

1. Descomprime la carpeta `fabrica-shorts-kit` donde quieras. Por ejemplo, en Documentos.
2. Abre la **Terminal** y escribe `cd ` (con espacio). Arrastra la carpeta a la ventana y aprieta Enter.
3. Corre:
   ```zsh
   bash instalar.sh
   ```
   - Si falta **Homebrew**, el script te dice qué pegar (pide tu contraseña del Mac).
   - Al final debe decir **✅ el motor funciona**.

## 2. Crear tu canal (conversando con Claude)

1. En esa misma carpeta, abre Claude Code:
   ```zsh
   claude
   ```
2. Dile:
   > Quiero crear mi canal de Shorts. Lee el PLAYBOOK y guíame.
3. Te va a hacer preguntas y proponer 3 micronichos.
4. Cuando elijas, deja escrito tu **Plan de canal** (`planes/`) y la configuración (`canales/`).
5. Si quieres, borra el canal de ejemplo: pídele que renombre `canales/ejemplo.json` a `canales/_ejemplo.json`.

**Personaliza el Estudio** en `config.json`: nombre, carpeta donde quedan los videos, zona horaria y colores.

## 3. Producir y ver los videos

- **Pídele:** "Haz los 2 videos de mañana para <canal>".
  - Escribe el guion con fuentes, revisa los cuadros y renderiza.
  - Cada video tarda ~3–6 min.
- **Ábrelos** en el Estudio:
  ```zsh
  ./venv/bin/python3 estudio/estudio.py
  ```
  Ve a **http://localhost:8765**. Ahí puedes ver el video, copiar el título y la descripción, descargarlo y marcarlo **✓ Subido**.
- **Para subir a mano desde el celular:** descarga el video, ábrelo en la app de YouTube, pega el título y la descripción, y prográmalo.

## 4. Métricas (para saber qué funciona)

**En Google Cloud** (lo haces tú, una vez):

1. Entra a **console.cloud.google.com** y crea un proyecto. Por ejemplo, "Mi fábrica".
2. En **APIs y servicios → Biblioteca**, activa **YouTube Data API v3** y **YouTube Analytics API**.
3. En **Google Auth Platform**:
   - **Branding:** ponle un nombre a la app.
   - **Audiencia:** elige **Externo**.
   - Aprieta **Publicar app** para dejarla **In production**. En Testing, los permisos vencen cada 7 días.
4. En **Clientes → Crear cliente**:
   - Elige el tipo **App de escritorio**.
   - **Descarga el JSON**, guárdalo como `secretos/oauth_cliente.json` y **no lo compartas con nadie**.

**En la Terminal** (en la carpeta del kit):

```zsh
./venv/bin/python3 metricas/metricas.py --autorizar      # una vez por canal: eliges la cuenta y luego EL CANAL
bash metricas/programar.sh                                # métricas solas: cada hora + reporte los domingos
```

- Si Google dice **"no verificó esta app"**, aprieta **Configuración avanzada → Ir a…**. Es tu propia app.
- Los domingos queda un reporte en `analisis/` (también en la pestaña **Reporte** del Estudio). Pídele a Claude:
  > Revisa la semana

## 5. Subida automática (opcional)

```zsh
./venv/bin/python3 metricas/subir_youtube.py --autorizar                 # una vez por canal (permiso solo para subir)
./venv/bin/python3 metricas/subir_youtube.py --dia 2026-11-24            # vista previa
./venv/bin/python3 metricas/subir_youtube.py --dia 2026-11-24 --subir    # sube y programa a la hora del .txt
```

- Sube cada video **privado y programado**: YouTube lo publica solo, a la hora.
- Desde nov-2026, los proyectos sin auditar ya **no quedan bloqueados en privado**.
- El cupo es de **100 subidas al día**.
- **Gasto de Claude: cero.** Es un programa normal que corre en tu Mac.

## 6. Si algo falla

- Abre Claude en la carpeta y cuéntale qué pasó, pegando el mensaje de error. **Nunca pegues** nada de `secretos/`.
- No corras dos videos a la vez: el motor usa una sola carpeta de trabajo.

## 7. Qué hay en la carpeta

| | |
|---|---|
| `PLAYBOOK.md` | Lo aprendido: nicho, ganchos, estructura, imagen, sonido y cómo medir |
| `CLAUDE.md` + `.claude/skills/` | Las instrucciones y habilidades de tu Claude |
| `motor/` | El que hace los videos (voz Kokoro + animación + música + efectos) |
| `estudio/` | La página de los videos |
| `metricas/` | Métricas, reporte semanal y subida |
| `LICENCIAS.md` | Qué puedes usar y cómo |
