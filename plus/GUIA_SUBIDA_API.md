# Subida automática a YouTube (API) · guía

**Qué hace:** `subir_youtube.py` sube los videos del día a tus canales, cada uno **privado y programado** a la hora de su `.txt`. Después los marca como subidos en el Estudio (igual que el botón ✓ Subido).
**Gasto de Claude:** ninguno. Lo corres tú en el Mac. Es un programa normal y no usa tokens.

---

## 1. Lo que cambió (2-nov-2026)

- **Antes:** si un proyecto de la API no estaba auditado, todo lo que subía quedaba privado y bloqueado.
- **Ahora:** YouTube **ya no bloquea** esos videos. No hace falta auditoría para publicar.
- **Cupo por defecto:** **100 subidas al día** por proyecto, en un cupo aparte del resto. Tú subes unas 14 al día, así que sobra.

## 2. Una sola vez (lo haces tú en Google Cloud)

1. Entra a **console.cloud.google.com** y abre **el mismo proyecto** que usa `metricas.py`.
2. Ve a **Google Auth Platform → Audiencia (Audience)**.
   - Si dice **Testing**, aprieta **Publicar app (Publish app)** para pasarla a **In production**.
   - **Por qué:** en Testing, los permisos **vencen cada 7 días**.
3. Vuelve a autorizar las métricas, una vez por canal:
   ```zsh
   cd ~/gta-shorts && ./venv/bin/python3 metricas.py --autorizar
   ```
   - Los permisos que se dieron estando en Testing siguen venciendo, por eso hay que darlos de nuevo.
4. Autoriza la **subida**, una vez por canal (7 veces; en cada una eliges el canal):
   ```zsh
   cd ~/gta-shorts && ./venv/bin/python3 subir_youtube.py --autorizar
   ```
   - Si Google muestra **"Google no verificó esta app"**, aprieta **Configuración avanzada → Ir a …**. Es tu propia app y nadie más la usa.
   - El permiso de subida se guarda **aparte**, en `secretos/subir/`. `metricas.py` no lo toca.

## 3. Prueba (1 video)

```zsh
cd ~/gta-shorts
./venv/bin/python3 subir_youtube.py --dia 2026-11-23                              # vista previa: no sube nada
./venv/bin/python3 subir_youtube.py --dia 2026-11-23 --canal DogDecoded --subir   # sube solo Perros
```

Revisa en **YouTube Studio → Contenido** que el video diga **Programado** con la hora correcta.

## 4. Uso diario

```zsh
cd ~/gta-shorts && ./venv/bin/python3 subir_youtube.py --dia 2026-11-24 --subir
```

| Marca | Qué significa |
|---|---|
| 🗓️ | Queda programado para esa hora |
| ⛔ | No se sube. Abajo dice por qué: falta el título, la hora ya pasó, ya se subió, falta el permiso… |
| 🚀 | Se publica al tiro (solo si agregas `--ahora`, para los atrasados) |

- **Nunca sube dos veces lo mismo.** Lo ya subido queda anotado en `datos/subidas_api.json`.
- Antes de subir, **revisa que el permiso sea del canal correcto**. Si no lo es, no sube.
- El título y la descripción salen **completos** del `.txt` (lo que hoy copias y pegas).
- La categoría va por carpeta: GTA → Gaming, Perros y Gatos → Mascotas, MDM y Café → Educación, Rabbit → Entretenimiento.
  - Se cambia en `CATEGORIA`, al inicio de `subir_youtube.py`.

## 5. Lo que sigue siendo a mano

- **Repers:** IG, TikTok y YouTube de Repers no entran en este script.
- **Contenido alterado o sintético:** si algún video lo necesita, márcalo en Studio. El script no lo marca.
- **Portada:** queda como está hoy, dentro del video. El script no sube miniatura.

## 6. Si algún día necesitas más de 100 subidas al día

- Hay que pasar una **auditoría**: formulario *YouTube API Services – Audit and Quota Extension Form*.
- **Qué decir:** herramienta interna de una persona, que sube a **sus propios canales** desde su computador. No tiene usuarios externos y no junta datos de terceros.
- **Hoy no hace falta.**
