# 04 · Escenarios, insertos y gráficos

## Espacios
- **Cada capítulo en un espacio distinto**, que cambia con la historia.
- **Máximo 5 regresos** a espacios ya vistos en todo el video. Cada regreso trae algo nuevo: otra hora (día/noche), otro ángulo o un objeto u otra acción.
- **Exteriores y lugares públicos** con vida: siluetas que cruzan, autos, luces que cambian.
- **Las pantallas dentro del set muestran contenido distinto y relacionado** con lo que se dice. Nunca la misma imagen en dos pantallas o en dos casos (la queja de Tao en Rabbit: *"las naves del computador son todas iguales"*).
- **Sets propios de un video no se reutilizan en otro:** la cinta "PIXR" de bolsaH, las vitrinas "1986 · $5M / 2006 · $7.4B" de museoH y la mesaCenital del contrato eran de Pixar.
- **Apertura:** el set inicial se arma sobre fondo neutro, sin el mundo synthwave de GTA detrás (arreglado el 23-nov en `escena_h.html`).

## Insertos (planos fuera del escenario)
- **Una vez cada uno.** Solo se repiten como **regreso a propósito** que sirve a la historia (cheque de $5M al final, balanza en la pregunta final).
- **Se eligen por lo que dice la frase** (palabra clave), no al azar del set. Si un inserto no calza con la frase, no va. Ejemplos de errores corregidos:
  - claqueta en "short video";
  - guion en "story";
  - teclado en "program";
  - teléfono en la autopsia;
  - papeles en "sign".
- **Nunca un inserto pegado a otro**, ni un corte afuera mientras hay un título grande o un globo.
- **Duración:** 1,8–2,8 s en general. Topes por tipo (`recortar_insertos.py`):
  - capítulo 1,9 s;
  - cheque 4,9 s;
  - balanza 4,4 s;
  - tablero de aletas (tableroH) 6,5 s;
  - tablero de polaroids 7 s.
- **Vuelven a la escena en una pausa de la voz** y nunca cruzan un cambio de tramo. Si no, la cámara regresa a un escenario viejo (`revisar_insertos.py`).
- **Cada canal tiene su banco propio.** Hoy Rabbit tiene solo 4 insertos permitidos y Perros, Gatos y Café solo la lupa (`CORTES_CANAL`). **Por eso esos videos se sienten lentos.** Ver `09`.

## Gráficos que explican
- **Aparecen antes de la palabra clave** y el dato cae cuando se dice. En la balanza, el lado de $5M entra primero y el de $7.4B cae justo en "7.4 billion".
- **Duran lo suficiente para leerse:** ~5–6 s en títulos y cifras grandes (PIXAR quedó en ~5,5 s), y después la escena vuelve a variar.
- **Enumeraciones → una pantalla que las muestre**, con cada ítem entrando cuando se nombra (las 4 polaroids clavadas con hilo rojo).
- **Comparaciones → balanza** o barras dentro del mundo, no un cuadro flotante.
- **Dinero:**
  - billetes con detalle;
  - pila en **pirámide**, no torre (salvo que la torre se vea entera);
  - cifras sin "caja de IA" (numeroDoc en 3 estilos que se alternan).
- **Capítulos:** tarjeta tipo cine (capituloH), sin caja de IA.
- **Los efectos tienen que mostrar lo que es:** en Star Trek II se mostraba un alien y Tao lo marcó. Ahora es el planeta muerto que una ola de fuego transforma (el efecto real, a nuestro estilo).
- **Física:** lo que cae rebota, se aplasta, levanta polvo y suena.

## Banco de formas creativas (elegir según el contenido; cada una, una vez por video)
| Si la voz habla de… | Recurso visual | ¿Existe? |
|---|---|---|
| una lista de 3–5 cosas | tablero de corcho con polaroids, tablero de aletas (aeropuerto) | ✅ cuatroH · tableroH |
| A contra B, antes y después | balanza, pantalla dividida, barras dentro del mundo | ✅ balanzaH · comparaBarras |
| un año o una fecha | línea de tiempo que corre hasta el año | ✅ lineaTiempoH |
| una firma, un trato | cheque que se escribe, contrato que se firma o se rompe | ✅ chequeH · (rompe) |
| dinero | billetes contados, pila de dinero, gráfico que sube o cae | ✅ |
| una empresa, un estudio | edificio por fuera, de noche, con ventanas encendiéndose | ✅ edificioH |
| una película, un estreno | claqueta, rollo, proyector | ✅ |
| animación o tecnología | render de malla a imagen | ✅ renderH |
| un riesgo, una apuesta | dados y fichas | ✅ dadosH |
| una noticia | **portada de diario genérico que gira y se detiene** | ⬜ nuevo |
| un documento oficial | **expediente que se abre, sello APPROVED/CLOSED, tachones negros** | ⬜ nuevo |
| un lugar o un viaje | **mapa con ruta y alfiler** | ⬜ nuevo |
| un radar, una señal | **pantalla de radar con barrido y puntos** | ⬜ nuevo |
| un video de cámara militar | **pantalla infrarroja (blanco-caliente) con retícula y cifras**, distinta en cada video | ⬜ nuevo |
| una explicación física | **diagrama animado** (triángulo de paralaje, capa de aire caliente) | ⬜ nuevo |
| una investigación | lupa sobre la foto, foto que se revela en la bandeja | ✅ lupa · ⬜ revelado |
| un engaño revelado | **taller con el muñeco a medio hacer** (sin nada gráfico) | ⬜ nuevo |
| una alerta | sirena, focos que barren el cielo, destellos antiaéreos | ⬜ nuevo |
| una transmisión de TV | TV de época con señal y estática | ✅ tv / setTVH |
| cómo funciona algo por dentro | **corte transversal** (taza, cerebro, ojo) con capas que se llenan | ⬜ nuevo |
| un sentido del animal | **"visión de perro/gato"**: el mismo plano con otro filtro de color o nitidez | ⬜ nuevo |
| una reacción | repetición en cámara lenta con flechas de movimiento | ⬜ nuevo |

**Regla del banco:** un recurso nuevo se diseña **para el tema** (la pantalla IR del GOFAST tiene olas y cifras de altura; la del GIMBAL, el destello que gira). Después puede pasar a otro video **solo si se ve distinto**.

## Criterios de escena para CUALQUIER tema de Short (desde la muestra 5 del descafeinado, 25-nov)
Plantilla: `d24/c17n/b.py`. Se revisan en cada guion antes de renderizar:
1. **Objeto protagonista premium del tema** en primer plano o sobre podio (`vitrinaV` con `pedestal`), con letrero suelto arriba. Abre el video (gancho) cuando el título es sobre un objeto.
2. **La palabra difícil o el proceso se dibuja** (soaked → `remojo`). Si una frase tiene un verbo que no todos entienden, va un objeto que lo muestre.
3. **La cifra clave tiene un indicador visual** (`mitad`, contador, calendario, barras, papel con dato), centrado, sin otro texto encima.
4. **Personas haciendo algo propio del tema** (`bebe`, `lee`, `explica`, `teclea`, `apunta` con objeto) en escenarios vestidos (lámpara, mesa, mesón…), nunca solo paradas. `"cuerpo":"pro"`.
5. **Ambiente:** `neblina`, `humo`, rayos y polvo (`acabadoPro` automático con cuerpo pro).
6. **6–8 escenas de 3–7 s**, alternando inserto de objeto y escena con persona; 3 insertos como mínimo.
7. **Textos sueltos sin marco ni número**, máximo dos a la vez con el subtítulo; si un objeto trae texto, el título se va antes.
8. **Emoji que salta** en 2–3 momentos de emoción, al centro.
9. **Guion:** gancho + promesa → desarrollo → primera respuesta → **segundo gancho con fricción** → dato → **frase de solución** → pregunta → CTA. `"pausa_larga_antes": [1, i_gancho2, i_gancho2+1, i_cta]`.
10. **Al menos una escena especial por video** (fuera del formato habitual, grande, propia del tema): mar de noche con buque y mira (`marNocheV`), montaña con avión y objetos en cadena (`montanaV`), visión humano vs perro (`visionPerro`), platillo rebotando (`rebota`), periódico de época (`periodico`), etc. Si el tema no tiene una, se dibuja una nueva.
11. **Primera escena = el gancho:** muestra el objeto o situación del título sin revelar la respuesta (taza con prohibido, caja con gato, precio "???", periódico con titular).
