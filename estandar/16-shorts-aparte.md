# 16 · SHORTS: recomendaciones aparte

> **Alcance:** solo Shorts y Reels (vertical, 20–45 s).
> **Regla de separación `[TAO]`:** nada de este documento dicta la arquitectura de un largo. Y nada de la Biblia de largos (doc 15) se aplica a un Short sin pasar por aquí.
> **Detalle completo:** `claude/hooks-retencion-23-nov.md` y `claude/manual-fabrica-shorts-20-nov.md`. Este documento es el resumen y la frontera.

## 1. Por qué son dos oficios distintos
| | **Short** | **Largo (10–12 min)** |
|---|---|---|
| Cómo llega el espectador | No eligió verte: aparece al deslizar | Eligió el video por el título y la miniatura |
| Primera decisión | Deslizar o quedarse, en ~1 s | Seguir pasados los primeros 30 s |
| Métrica del gancho | **Visto vs. deslizado** | **% que sigue a los 30 s** |
| Métrica de fondo | % visto y duración media | Retención por tramos, comparada con largos de duración parecida |
| Estructura | Una sola idea: gancho → tensión → pago | Actos, capítulos y un libro de preguntas |
| Curiosidad | Un bucle, a lo más dos | Una pregunta mayor y varias menores encadenadas |
| Ritmo | Parejo y rápido de principio a fin | Cambia según el acto |
| Lugares | 1–2 | 8–12, con cambios de estado |
| Final | Paga y vuelve a la primera frase (para el loop) | Pico, reflexión, imagen final y puente |
| Lectura de datos | 24 h (inglés) y 72 h (español) | 28 días |
| Cuenta para monetizar | Vistas de Shorts | Horas de visualización |

## 2. Reglas propias del Short (vigentes)
### Gancho (0–3 s)
- **El primer cuadro es el objeto o el resultado,** en primer plano.
- **La primera frase es una afirmación concreta** que choca con una creencia. Sin saludo.
- **Texto en pantalla desde el cuadro 1,** de 3–7 palabras, que se entienda sin sonido.
- **Un cambio visual antes de los 2 s.**
- **Alternativa:** abrir con un conflicto en curso.
- **El gancho es verdad y el video lo cierra.**

### Retención
- **Un cambio de plano cada 2–4 s.**
- **Lo que se dice se ve.**
- **Segundo bucle hacia la mitad,** como afirmación.
- **Cada bloque sube la apuesta.**
- **Sin relleno:** la duración es la que el tema necesita.
- **El final paga y empata con el inicio.**

### Envíos (Instagram)
- **Un dato "para mandárselo a alguien".**
- **Cierre con invitación a comentar o enviar,** sin urgencia falsa.

## 3. Qué NO se traspasa del Short al largo
| Costumbre del Short | Por qué no va en el largo |
|---|---|
| Ritmo parejo y máximo todo el video | En 10 minutos cansa. El largo necesita respiros y un ritmo que cambia con la historia |
| Una sola idea | El largo necesita anécdotas, reflexión y varias preguntas |
| Cierre en loop | El largo cierra con un pico y una imagen final |
| Texto grande permanente | En horizontal tapa la imagen; el largo usa subtítulos y textos puntuales |
| Meta de cortes por minuto | En el largo, la variedad se informa pero no aprueba ni rechaza (doc 14) |
| Leer el resultado a las 24 h | El largo se lee a los 28 días |

## 4. Qué NO se traspasa del largo al Short
| Recurso del largo | Por qué no va en el Short |
|---|---|
| Apertura en frío de 20 s + promesa | El Short tiene ~1 s |
| Capítulos y tarjetas de lugar | No hay tiempo |
| Guion de color con arco | Un Short tiene un solo ánimo |
| Planos de ubicación | El tema tiene que estar en el cuadro 1 |
| Libro de preguntas | Un bucle basta |

## 5. Lo único que comparten
- Las reglas de verdad y de contenido (2 fuentes, sin política, sin caras reales ni marcas).
- No revelar el dato clave antes del final.
- Nada tapa nada; el texto se lee.
- La identidad del canal: colores, sonidos y objeto protagonista.
- El banco de piezas paramétricas (un mismo `sello()` o `mapa()` sirve a los dos formatos, con otro encuadre).

## 6. Relación entre los dos formatos (por decidir)
- **Un Short no es un recorte del largo.** Si se hace un Short del mismo tema, se escribe como Short: su propio gancho, una sola idea y su propio final.
- **Hipótesis `[HIP]`:** un Short que plantea la pregunta del largo y no la responde puede llevar gente al largo. No está probado en nuestros canales, y choca con la regla de que el gancho se cierra dentro del mismo video. Queda como experimento, no como norma.

## 7. Mejoras pendientes solo para Shorts (no tocan los largos)
1. Inserto de gancho en `t = 0` por defecto.
2. 3–5 insertos por Short (hoy 1–2).
3. Medidor de ritmo antes de entregar.
4. Comparar "visto vs. deslizado" contra las semanas anteriores del mismo canal, con 6–10 videos.

Todo cambio al código de la fábrica de Shorts se avisa antes.
