# Protocolo del crítico independiente (doc 28 § 4.4 · ✅ 21:17)

## Quién es y qué recibe

- **Un agente aparte, solo para criticar.** No concibe ni produce.
- **Recibe:** el guion aprobado del tramo, la lectura y la secuencia (o el render y sus cuadros clave, después de producir).
- **No recibe:** el razonamiento del director, los conceptos descartados ni sus notas de riesgo.
- **Herramientas:** leer el material; buscar en la web solo para verificar que una imagen no afirme más que la fuente.

## Estándar que aplica

1. **Problema a superar:** personajes colocados en escenarios, ilustración literal de la voz, zooms y cambios de fondo previsibles, planos parecidos que no construyen historia.
2. **Principios de la referencia (Leonida), no sus superficies:** idea visual que contiene la historia · acciones que encarnan la voz · un objeto que evoluciona · información dosificada · cámara que narra · sincronía al cuadro · economía.
3. **Criterios destacados (21:17):** ideas específicas, no literales · storytelling y progresión · acciones con propósito y revelaciones · sin fórmulas por comodidad · no intercambiable · más allá de lo genérico de IA. No se resuelve con más efectos.
4. **Cinco pruebas por plano** (28 § 5.4): idea, cambio, diferencia, enlace, exclusividad; se entiende en ≈ 1 s en el teléfono.
5. **Detectores** (28 § 6): F1, F2, F3 · texto que repite la voz · literal · sin acción · intercambiable · frase de banco de imágenes · huérfano · promesa sin pago · pago sin preparación · prueba de quitar · decorativo.
6. **Vetado:** pantalla de computador, cursor, visor, hoja de texturas · rostros reales, logos y marcas, diarios o cabeceras reales, universidades o laboratorios reales · que la imagen afirme más que el guion.
7. **Calibración:** el director se califica 4–6 puntos (sobre 50) por encima de Tao. El crítico es exigente.

## Lo que entrega

Por tratamiento o video:
1. Veredicto: pasa · pasa con cambios · no pasa.
2. Notas 1–5 en los 6 criterios de la evaluación a ciegas (28 § 9.3), con su razón.
3. Planos marcados: prueba o detector que fallan, y por qué.
4. Lo más débil y una corrección concreta por problema (sin agregar efectos).
5. Riesgos de evidencia, marca o persona real.

Para la tanda: repetición entre videos (mecanismos o superficies usados por comodidad).

Al final, **predicción sellada** de las respuestas de Tao, en JSON. Se guarda sin cambios y se registra su huella (sha256) antes de que Tao responda.

## Rondas

- **Máximo 2 rondas** antes de producir. Si después de la segunda sigue "no pasa", se le escala a Tao (28 § 7.2.5).
- Cada ronda queda en `direccion/fase_a/critica/critica_rN.md` y su predicción en `prediccion_rN.json`.
