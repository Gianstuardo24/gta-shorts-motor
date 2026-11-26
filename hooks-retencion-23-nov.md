# Hooks y retención: reglas verificadas (23-nov-2026)

> Lista propia. Las "122 reglas" son de un producto pagado (crearvideoviral.com) y no son públicas: **no las usamos ni las copiamos**.
> Solo entra lo que tiene fuente oficial o académica, o lo que se ve en nuestros propios datos.

## 0. Fuentes y confianza

| Tipo | Fuente | Qué aporta |
|---|---|---|
| **Oficial** | YouTube Help + blog.youtube (Todd Sherman y Jenny Hoyos) | "Visto vs. deslizado" es la métrica del gancho. Hoyos: "tienes un segundo para enganchar". |
| **Oficial** | Instagram (Adam Mosseri) | Las 3 señales que más pesan en Reels: **tiempo de visualización, likes por alcance y envíos por alcance**. Los envíos pesan más para llegar a gente que no te sigue. |
| **Oficial** | TikTok for Business | El gancho va en los primeros **3–6 s**. Casi todo el impacto en recuerdo ocurre en los primeros 6 s. |
| **Académica** | Loewenstein 1994; Golman y Loewenstein | La curiosidad nace de una **pregunta específica** y visible. Una pregunta vaga no la genera. |
| **Estudio externo** | Galloway 2023 (33 canales, 5.400 Shorts) | Los Shorts con más duración vista rinden más. Es de 2023: solo orientativo. |
| **Propia** | 5-ganchos.md (19-nov), laboratorio (2 videos de hooks), receta curiosfer y medición de cortes de hoy | Ver secciones 2 y 3. |
| **Descartado** | Cifras de blogs sin fuente primaria ("84 % se predice al segundo 3", "1,7 s", etc.) | No se usan. |

## 1. Qué se mide

| Plataforma | Gancho | Retención | Alcance |
|---|---|---|---|
| YouTube Shorts | **% visto vs. deslizado** | Duración media y % visto | Vistas a 24 h (EN) y 72 h (ES) |
| Instagram Reels | Tiempo de visualización | Tiempo de visualización | **Envíos por alcance** (gente nueva), likes por alcance (seguidores) |

- **Pendiente:** revisar si la API de YouTube entrega "visto vs. deslizado". Si no lo entrega, Tao lo mira en Studio.
- Siempre se compara **contra el propio canal**, no contra cifras genéricas.

## 2. Los 2 videos de hooks (laboratorio, 23-nov)

| | GastonGBG "Esta papa frita es una mentira" | Mutleysldn (sebo de vacuno) |
|---|---|---|
| Vistas / suscriptores | 28,1 M / 1,74 M (**16×**) | 12,1 M / 9.530 (**~1.265×**) |
| Duración | 54 s | 38 s |
| Cortes | **64 por minuto**. 6 en los primeros 4 s | 17 por minuto. Primer corte a los 6,3 s |
| Primer cuadro | El **resultado**: la papa mojándose en la salsa | **Conflicto en curso**: alguien echa aceite y lo frenan |
| Primera frase | **Contradicción**: "Me mintieron toda la vida: estas no son papas fritas" | **Interrupción**: "¿Qué es eso? No, aquí no usamos eso" |
| Mitad | **Segundo bucle**: "algo que no es una salsa" | Admite los contras (credibilidad) |
| Final | **Vuelve a la frase inicial**: "¿Viste que era mentira…?" (cierra el bucle) | Identidad: "esa es la diferencia entre nosotros y el resto" |

**En común:**
- El tema aparece en el **primer segundo**, sin intro.
- Hay un **objeto concreto** en pantalla desde el cuadro 1.
- La primera frase **choca con una creencia** común.
- El final **cierra** lo que abrió el gancho.

**Dos mecanismos de gancho:**
- **Ritmo:** cortes rápidos + el resultado primero (Gaston).
- **Escena viva:** la acción ya es tensión, así que no necesita cortes al inicio (Mutley).

## 3. Medición nuestra: lunes 23 v2

Detector de cortes de ffmpeg (umbral 0,25), el mismo método que usa el laboratorio.

| Video | Duración | Cortes duros | Por minuto |
|---|---|---|---|
| c21 | 32,9 s | 1 | 1,8 |
| r18 | 36,5 s | 1 | 1,6 |
| dog14n | 28,4 s | 3 | 6,3 |
| m18 | 41,3 s | 4 | 5,8 |

- Además hay 3–5 cambios de set por paneo continuo: en total, **un cambio visual cada 6–8 s**.
- **Referencias:** curiosfer, un plano cada 3–5 s (12–15/min); Mutley, 17/min; Gaston, 64/min.
- **Conclusión:** nuestro ritmo visual es **3 a 10 veces más lento**. Es la brecha concreta más grande.

## 4. Reglas

### Gancho (0–3 s)
- **H1. El primer cuadro es el objeto o el resultado** del video, en primer plano: un inserto en t = 0. Nunca un plano general de entrada.
- **H2. La primera frase es una afirmación concreta** que choca con una creencia, con un nombre propio o una cifra. Sin saludo ni contexto.
- **H3. Texto en pantalla desde el cuadro 1:** 3–7 palabras que se entiendan sin sonido.
- **H4. Al menos un cambio visual antes de los 2 s:** corte, zoom de golpe o entrada de un objeto.
- **H5. Alternativa al ritmo:** abrir con un conflicto en curso (alguien interrumpe o descubre algo).
- **H6. Regla de oro (ya vigente):** el gancho es verdad hoy y el video lo cierra.

### Retención (3 s → final)
- **R1. Un cambio de plano cada 2–4 s:** inserto, ángulo nuevo, zoom o set nuevo. **Meta: ≥15 por minuto** (hoy 2–6).
- **R2. Lo que se dice se ve:** cada frase tiene su imagen.
- **R3. Segundo bucle al 40–60 %,** como afirmación y no como pregunta (la voz IA no lleva preguntas). Ej.: "Y lo de la salsa es todavía más raro."
- **R4. Escalada:** cada bloque sube la apuesta (cifra mayor o consecuencia mayor).
- **R5. Sin relleno:** si una frase no avanza la promesa ni lleva al pago, se corta.
- **R6. El final paga y vuelve a la primera frase,** para que el loop empate.

### Envíos (Instagram)
- **S1. Un dato "para mandárselo a alguien":** una sorpresa útil o algo que le pasa al espectador. Los envíos por alcance son la señal más fuerte para llegar a gente nueva.
- **S2. Cierre con invitación a comentar o enviar.** Sin urgencia falsa.

## 5. Cambios propuestos al motor (se avisa antes de tocar código)

1. **Inserto de gancho en t = 0** por defecto. Ya es posible: `insertar(E, "0", …)`.
2. **Pasada de ritmo automática:** si no hay corte en los últimos 3 s, agregar un zoom de golpe (1,0 → 1,12) al inicio de cada frase. Toca `comun.py`: **requiere OK de Tao**.
3. **3–5 insertos por Short** (hoy 1–2), con la biblioteca de utilería que ya existe.
4. **Medidor `ritmo.sh`** (script nuevo): cortes por minuto + primer corte. Se revisa antes de entregar.

**Estimación realista:** puntos 2 y 4, ~1–2 h con pruebas. Punto 3, ~10–15 min extra por Short.

## 6. Cómo se prueba
- **No se republica el mismo video.** Por eso no hay A/B con el mismo guion.
- Se aplica el ritmo nuevo a **todos los videos nuevos de un canal** y se compara contra sus semanas anteriores:
  - "visto vs. deslizado";
  - % visto;
  - vistas a 24 h (EN) o 72 h (ES).
- Con 6–10 videos ya se ve si la tendencia cambia. Con menos, solo se anotan como señal.

## Fuentes
- [YouTube Help: rendimiento del contenido (visto vs. deslizado)](https://support.google.com/youtube/answer/12220281)
- [blog.youtube: Shorts deep dive (Todd Sherman y Jenny Hoyos)](https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/)
- [Social Media Today: señales de Instagram 2025 (Mosseri)](https://www.socialmediatoday.com/news/instagram-shares-algorithm-2025/738034/)
- [Search Engine Journal: envíos por alcance (Mosseri)](https://www.searchenginejournal.com/instagram-algorithm-shift-why-sends-matter-more-than-ever/521389/)
- [TikTok for Business: buenas prácticas creativas](https://ads.tiktok.com/help/article/creative-best-practices)
- [TikTok SMB Creative Playbook](https://ads.tiktok.com/business/library/SMB_Creative_Playbook.pdf)
- [Golman y Loewenstein: Information Gaps (CMU)](https://www.cmu.edu/dietrich/sds/docs/golman/Information%20Gaps--Golman%20and%20Loewenstein.pdf)
- [Paddy Galloway: estudio de 3.300 M de vistas en Shorts (2023)](https://threadreaderapp.com/thread/1646898356419981315.html)
