# 23 · EVALUADOR DE VIDEOS (v0) Y PRIMER PERFIL DE LARGOS FACELESS QUE RINDEN

> **Pedido de Tao (24-nov, 12:13):** que los videos los vea y analice Claude: vocabulario, tipo de lenguaje (formal o informal), cortes, relación entre lo que se muestra y lo que se dice. La idea es **construir un evaluador** que haga ese trabajo e identifique fórmulas.
> **Qué hay aquí:** el evaluador en su primera versión, aplicado a 8 largos de canales chicos que rinden muy por encima de su tamaño, y a los 3 videos de canales grandes vistos hoy.
> **No se tocó el Estudio.** El evaluador vive aparte; integrarlo es un paso posterior, con aviso.

---

## 1. Qué mide el evaluador (v0)
| Bloque | Medidas | De dónde sale |
|---|---|---|
| **Voz** | Palabras por minuto · en los primeros 30 s · pausas largas por minuto | Subtítulos con el tiempo de cada palabra |
| **Lenguaje** | Palabras por frase · facilidad de lectura · palabras largas · contracciones · uso de "tú" y de "yo" · cifras · preguntas · variedad de vocabulario · registro | Texto de los subtítulos (solo inglés por ahora) |
| **Imagen** | Cortes por minuto · plano mediano y más largo · tiempo sin ningún cambio · rachas quietas · cambios locales | Diferencia entre cuadros, 5 por segundo |
| **Gancho** | Cortes y quietud en los primeros 30 s · primera frase: largo, pregunta, cifra, "tú" | Lo anterior, acotado al inicio |
| **Sincronía** | En qué porcentaje de las frases cambia algo en pantalla mientras se dicen | Cruce de frases y cambios |
| **Relación entre imagen y frase** | Muestra al azar de frases con el cuadro que se ve mientras se dicen | **La miro yo.** Es juicio, no medición |

**Todo es medición, salvo la última fila.** No usa las etiquetas que fallaron en la calibración (doc 22).

**Registro (convención mía, no un estándar):** informal si hay 2 o más contracciones y 1,5 o más "tú" por cada 100 palabras; formal si casi no hay contracciones y abundan las palabras largas; neutro en el resto.

**Límites:**
- El lenguaje solo se mide en inglés; falta el español.
- Los subtítulos son automáticos: sirven para contar, no para citar.
- El detector de cortes no ve fundidos ni tomas continuas de juego.
- No oigo: música y efectos quedan fuera.

---

## 2. Los videos
**De los 10 que estaban bajados, 2 no sirven como referencia.** Lo supe al mirarlos:
| Video | Por qué queda fuera |
|---|---|
| "The Zanfretta Abductions" (Bedtime Stories) | Es un canal de 1,1 M de suscriptores. El caso chico era la versión en español |
| "Nobody Can Solve The Coffee Lid Problem" (Double Take) | No es faceless: tiene presentador a cámara y entrevistas, y lleva la marca de otro canal |

**Los 8 que quedan** (canales chicos; "veces" = vistas divididas por suscriptores):
| Video | Suscriptores | Veces | Palabras/min | Cortes/min | Sin cambio | Cambios locales/min | Frases con cambio | Palabras/frase | Lectura | "Tú"/100 | Contracc./100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Proxy · "What Happened to Nerf?" | 3,5 k | 748 | 202 | 31,9 | **1 %** | 15,0 | 100 | 15,8 | 66,5 | 1,36 | 1,3 |
| GTAbites · "GTA 6 Can Do Things We Never Imagined " | 6,1 k | 1149 | 178 | 15,2 | **1 %** | 10,1 | 99 | 10,8 | 76,9 | 3,68 | 3,31 |
| Fortune & Fall · "WTF Happened to Labubu?" | 6,7 k | 346 | 146 | 10,6 | **31 %** | 17,3 | 99 | 12,0 | 69,6 | 1,38 | 2,72 |
| Wade | K9 Dog Training · "Stop Calling It a Kiss: What Your Dog " | 8,4 k | 110 | 186 | 12,2 | **0 %** | 8,9 | 96 | 18,5 | 76,4 | 6,71 | 0,53 |
| SM Createx · "China’s 18,000-Person Building Mystery" | 93,9 k | 108 | 177 | 18,3 | **2 %** | 8,4 | — | — | — | — | — |
| Leo Bennett Reads Cats · "14 Things Cats SECRETLY Do When They T" | 4,9 k | 43 | 186 | 18,0 | **2 %** | 7,8 | 96 | 11,8 | 89,7 | 6,42 | 4,52 |
| Alienory · "1967: A RED UFO Lands in Front of Him…" | 5,2 k | 42 | 108 | 19,0 | **28 %** | 7,1 | 90 | 12,3 | 64,2 | 0,22 | 1,01 |
| Tyler Brooks · "Your Cat Doesn’t Think You're Petting " | 7,4 k | 39 | 207 | 12,1 | **4 %** | 7,8 | 96 | 10,7 | 87,2 | 3,55 | 4,48 |

**Los 3 de canales grandes** (vistos en la calibración):
| Video | Suscriptores | Veces | Palabras/min | Cortes/min | Sin cambio | Cambios locales/min | Frases con cambio | Palabras/frase | Lectura | "Tú"/100 | Contracc./100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Company Man · "Gatorade vs. Powerade" | 1,8 M | 0 | 181 | 13,7 | **32 %** | 7,1 | 95 | 20,1 | 56,5 | 1,25 | 0,72 |
| toldinstone · "Three Unfinished Roman Megaprojects" | 653,0 k | 1 | 134 | 4,3 | **76 %** | 1,6 | 40 | 19,9 | 51,7 | 0,62 | 1,43 |
| Kurzgesagt – In a Nuts · "Astronomy Is In Crisis...And It's Incr" | 25,8 M | 0 | 168 | 5,8 | **7 %** | 11,6 | 99 | 16,2 | 60,7 | 0,81 | 1,88 |

---

## 3. Lo que tienen en común los 8 (mediana) frente a los 3 grandes
| Medida | **8 chicos que rinden** | Company Man | toldinstone | Kurzgesagt |
|---|---|---|---|---|
| Tiempo sin ningún cambio en pantalla | **2,0 %** | 32 % | 76 % | 7 % |
| Tiempo en rachas quietas de 5 s o más | **0,0 %** | 23 % | 67 % | 0 % |
| Pantalla quieta en los primeros 30 s | **3,0 %** | 47 % | 96 % | 0 % |
| Frases durante las que algo cambia en pantalla | **96 %** | 95 % | 40 % | 99 % |
| Cortes por minuto | **16,6** | 13,7 | 4,3 | 5,8 |
| Cambios locales por minuto | **8,7** | 7,1 | 1,6 | 11,6 |
| Palabras por minuto | **182,0** | 181 | 134 | 168 |
| Pausas largas por minuto | **0,9** | 1,5 | 8,8 | 2,7 |
| Palabras por frase | **12,0** | 20,1 | 19,9 | 16,2 |
| Facilidad de lectura (Flesch; más alto, más fácil) | **76,4** | 56,5 | 51,7 | 60,7 |
| Palabras largas (8 letras o más) | **9,2 %** | 14,9 % | 14,4 % | 13,2 % |
| Contracciones por 100 palabras | **2,7** | 0,72 | 1,43 | 1,88 |
| "Tú" por 100 palabras | **3,5** | 1,25 | 0,62 | 0,81 |
| Cifras por 100 palabras | **1,0** | 2,42 | 1,36 | 0,91 |
| Preguntas por 100 frases | **2,4** | 4,5 | 0,0 | 3,5 |

**Reacción de Tao a los grandes:** Company Man, lento y estirado; toldinstone, abandonado por quieto.

---

## 4. Relación entre imagen y frase (muestra mirada por Claude)
8 frases al azar por video, en 4 videos, cada una con el cuadro que se ve mientras se dice.
| Video | La imagen fue hecha o elegida para esa frase | Cómo lo hace |
|---|---|---|
| "What Happened to Nerf?" | 6 de 8 (las otras 2: un signo de pregunta cuando la voz pregunta) | Comerciales y fotos del producto exacto que se nombra, con marcas gráficas encima |
| "WTF Happened to Labubu?" | 8 de 8 | **Tarjetas gráficas hechas para cada frase:** el recibo con el precio que se dice, la grilla de series, el gráfico del "pico", tres tarjetas para tres ideas |
| "Stop Calling It a Kiss…" (perros) | 8 de 8 | Una imagen de la situación exacta que describe cada frase, alternada con un presentador a cámara |
| "Coffee Lid" (descartado) | — | Presentador y material filmado |

**Total en los 3 válidos: 22 de 24 frases con una imagen hecha para esa frase.**
El de Labubu es el más cercano a lo que nuestro motor ya sabe hacer: gráficos por código, uno por idea.

---

## 5. Fórmula candidata (hipótesis, nivel C)
| # | Rasgo común | Dato |
|---|---|---|
| 1 | **La pantalla casi nunca se queda quieta** | Mediana de 2 % del tiempo sin cambios, y prácticamente ninguna racha quieta de 5 s |
| 2 | **Cada frase tiene su imagen** | En 96 a 100 % de las frases algo cambia en pantalla; en la muestra, la imagen estaba hecha para la frase |
| 3 | **Lenguaje llano y hablado** | Frases de unas 12 palabras, lectura fácil, contracciones, pocas palabras largas |
| 4 | **Le hablan al espectador** | "Tú" unas 3 veces cada 100 palabras; en perros y gatos, más de 6 |
| 5 | **Voz ágil y sin pausas** | Unas 180 palabras por minuto. Excepción: el canal de casos OVNI (108, con muchas pausas) |
| 6 | **El inicio no se detiene** | En los primeros 30 s, entre 6 y 11 cortes y casi nada de quietud |

**Por nicho:** los de negocios usan más cifras (hasta 4 por cada 100 palabras); los de mascotas, casi ninguna y mucho "tú".

### Lo que esto NO prueba
- **Son rasgos en común, no causas.** Falta compararlos con videos **normales de esos mismos canales**. Si los normales también tienen estos rasgos, el rasgo no explica el éxito.
- Son 8 videos, de 4 nichos.
- Coinciden con lo que a Tao le molestó de los otros videos, pero eso es un espectador.
- La comparación con los 3 grandes mezcla género, presupuesto y público.

---

## 7. Nuestros 6 largos frente al perfil (24-nov, 12:40)
Mismo evaluador, misma resolución que las referencias.
| Video | Minutos | Palabras/min | Cortes duros/min | Sin cambio | Cambios locales/min | Frases con cambio | Palabras/frase | Lectura | Contracc./100 | "Tú"/100 | Preguntas/100 frases |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MDM · Pixar | 6,7 | 188 | 8,5 | 5 % | 6,2 | 100 % | 9,3 | 73,6 | 0,5 | 0,25 | 0,0 |
| MDM 2 | 6,4 | 151 | 3,1 | 5 % | 5,1 | 100 % | 17,1 | 63,7 | 0,22 | 0,32 | 0,0 |
| Rabbit 1 | 8,3 | 147 | 0,2 | 7 % | 7,6 | 100 % | 10,4 | 70,4 | 0,25 | 0,25 | 0,0 |
| Rabbit 2 | 9,8 | 153 | 1,9 | 8 % | 3,9 | 100 % | 14,9 | 68,2 | 0,21 | 0,07 | 0,0 |
| Dog 1 | 6,5 | 178 | 0,3 | 5 % | 3,5 | 100 % | 12,1 | 80,2 | 0,54 | 2,34 | 1,1 |
| Coffee 1 | 5,7 | 162 | 0,9 | 6 % | 3,9 | 100 % | 16,7 | 72,9 | 0,0 | 1,38 | 0,0 |
| **8 chicos que rinden (mediana)** | **15** | **182** | **16,6** | **2 %** | **8,7** | **96 %** | **12** | **76** | **2,7** | **3,5** | **2,4** |

### Dónde ya estamos a la par
| Medida | Nosotros | Ellos |
|---|---|---|
| **Pantalla quieta** | 5 a 8 %, y casi todo es la pantalla final fija de 18 s que cierra cada video | 2 % |
| **Cada frase con su cambio en pantalla** | 100 % | 96 % |
| **Lenguaje simple** | Lectura 64 a 80; frases de 9 a 17 palabras | 76; 12 |
| **Inicio sin quietud** | 0 a 15 % en los primeros 30 s | 3 % |

### Dónde hay distancia
| # | Brecha | Nosotros | Ellos | Nota |
|---|---|---|---|---|
| 1 | **Imágenes realmente nuevas** | 0,2 a 8,5 cortes duros por minuto | 16,6 | Es la mayor. Nuestro motor mueve la cámara dentro de un mismo mundo; ellos saltan a una imagen distinta cada 3 o 4 s. Confirma el hallazgo central del doc 13 |
| 2 | **Tono hablado** | Casi sin contracciones (0 a 0,5) | 2,7 | Escribimos más "de libro" |
| 3 | **Hablarle al espectador** | "Tú" 0,1 a 2,3 | 3,5 (mascotas: más de 6) | En Dog 1: 2,3 contra 6,4 a 6,7 de los canales de mascotas |
| 4 | **Preguntas en la voz** | 0 en cinco de los seis | 2,4 | Veníamos aplicando a los largos una regla que nació para Shorts |
| 5 | **Velocidad de la voz** | Tres videos van a 147–153 | 182 | MDM Pixar (188) y Dog 1 (178) ya están en rango |
| 6 | **Duración** | 5,7 a 9,8 min | 9,5 a 21 | Ninguno de los nuestros llega a los 10–12 que fijamos |
| 7 | Cosas que aparecen | 3,5 a 7,6 por minuto | 8,7 | Brecha menor |

### Límites de esta comparación
- **El detector de cortes no ve nuestras transiciones suaves** ni los reencuadres. Nuestra cifra de "cortes duros" subestima el cambio real. Pero mide bien algo cierto: cuántas veces aparece una imagen del todo distinta.
- Las brechas son contra **rasgos en común** de 8 videos, no contra causas probadas. Cerrar una brecha es una hipótesis a probar, no una garantía.
- No se comparan títulos, miniaturas ni tema, que pesan en el clic.

---

## 8. Siguientes pasos posibles
| # | Paso | Para qué |
|---|---|---|
| 1 | ✅ Pasar nuestros largos por el evaluador | Hecho: sección 7 |
| 2 | Bajar 1 o 2 videos normales de cada canal chico y medirlos | Convertir "rasgos en común" en "lo que distingue al que rinde" |
| 3 | Lenguaje en español y más nichos | Cubrir nuestros canales en español |
| 4 | Lo mismo para Shorts virales, por separado | Pedido de Tao |
| 5 | Integrar el evaluador al Estudio (etapa 3) | Solo con aviso y aprobación |

**Dónde está el evaluador:** `estandar-produccion/evaluador_v0.py`. Es una copia de respaldo; no está conectada a nada del Estudio.
