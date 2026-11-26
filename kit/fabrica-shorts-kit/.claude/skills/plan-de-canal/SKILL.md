---
name: plan-de-canal
description: Crear o afinar un canal de Shorts conversando con la persona. Termina en planes/<id>.md y canales/<id>.json. Úsala cuando quiera un canal nuevo, cambiar de nicho o revisar su propuesta.
---

# Plan de canal

**Objetivo:** que la persona salga con **un micronicho claro**, una **fórmula fija** y **14 temas verificables**, listos para producir.

## Pasos

1. **Lee** `PLAYBOOK.md` (§1, §2 y §8) y `plantillas/plan-de-canal.md`.
2. **Pregunta en tandas cortas** (máx. 3 preguntas por mensaje):
   - ¿Sobre qué te gustaría hacer videos? ¿Qué sabes o te apasiona?
   - ¿Para quién? ¿En qué idioma?
   - ¿Hay canales que te gusten? (solo para entender el patrón; nunca se copian)
3. **Propón 3 micronichos** con ángulo específico. De cada uno:
   - fórmula de título + 2 títulos de ejemplo;
   - qué cree ya el público (para el gancho);
   - **riesgo**: ¿hay datos verificables para 14+ videos? ¿Hay temas de salud, dinero o legales?
4. Que la persona **elija uno**. Afina la fórmula (título ≤40 caracteres, gancho, cuadro 0, cierre, CTA).
5. **Busca en la web** 14 temas con **2+ fuentes** cada uno. Descarta los que no se puedan verificar.
6. Escribe `planes/<id>.md` (con la plantilla) y **muéstraselo**. Ajusta hasta que diga OK.
7. Crea `canales/<id>.json` copiando la forma de `canales/ejemplo.json`:
   - `id`, `nombre`, `handle` (sin @, en minúsculas, como en youtube.com/@…), `carpeta` (sin espacios);
   - `idioma`, `voz`, `velocidad`, `musica`, `categoria` (20 Gaming · 15 Mascotas · 27 Educación · 24 Entretenimiento · 22 Personas y blogs);
   - `horas`, `marca`, `acento`, `micronicho`, `formula_titulo`, `cta_voz`, `firma`, `hashtags` (3), `protagonista`, `reglas`.
8. Si `canales/ejemplo.json` no es un canal real, sugiere renombrarlo a `_ejemplo.json` para que no aparezca en el Estudio.

## Reglas

- Un canal = un micronicho. Si la persona quiere varios temas, son varios canales.
- Nada de temas que necesiten caras reales, marcas, personajes con derechos o material ajeno.
- Salud, dinero y temas legales: solo informativo, y dilo en `reglas`.
