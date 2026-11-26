# Guía del motor "escena" (para Claude)

El video es **una animación por código** (`motor/escena/escena.html`, 1080×1920, 30 fps). Se describe en el guion `.json` y el motor la sincroniza con la voz palabra por palabra.

**Ejemplo completo que funciona:** `plantillas/guion-ejemplo.json`. Parte siempre copiándolo.

---

## 1. Guion (`guiones/<día>/<canal>-<HH>h.json`)

```json
{
  "titulo": "Why Your Dog Gets the Zoomies 🐶",
  "texto_pantalla": "THE ZOOMIES",
  "descripcion": "Those wild laps around the house have a real name. 👀",
  "hashtags": ["#zoomies"],
  "fuentes": ["https://…", "https://…"],
  "nota_datos": "qué dice cada fuente (para revisar)",
  "frases":     ["Texto en pantalla, frase 1.", "…"],
  "frases_voz": ["Lo que dice la voz, frase 1.", "…"],
  "escena": { "momentos": [], "escenas": [], "cierre": "", "cierre2": "", "paises": [], "cta": "", "like": "LIKE" }
}
```

**Campos**
- `frases` y `frases_voz` tienen **el mismo largo**. En `frases_voz` van las cifras escritas en palabras y **ningún `?`**.
- La **penúltima frase** es la invitación a comentar ("Tell me…") y la **última** es el CTA del canal.
- Opcionales:
  - `texto_portada`: título de la portada, si no es el título del video.
  - `portada_seg`: segundo del video que se usa de portada.
  - `fuente_texto`: línea "Fuente:" en la descripción.
  - `tema`: `"espacio"` cambia los efectos a glitch o electricidad.

## 2. Momentos (cuándo pasa cada cosa)

`["clave", índice_de_frase, "^prefijo"]` es el instante en que la voz dice la primera palabra de esa frase que empieza con el prefijo.
- Con `null` en vez de prefijo, es el **inicio** de la frase.
- Las claves que empiezan con `s_` marcan un **cambio de escena** (suena un whoosh corto). Ej.: `s_when`.
- `s_fin` = empieza el cierre. `s_cta` = la frase del CTA.
- En cualquier `k`, `fin`, `desde` o `hasta` puedes escribir `"clave+0.4"` o `"clave-0.2"` (segundos relativos). `0` = inicio del video.

## 3. Escena `pelicula` (el formato principal)

Una sola escena continua, dividida en **zonas** que la cámara recorre.

| Campo | Qué es |
|---|---|
| `zonas` | `[{x0, x1, set, luz, k}]` tramos del escenario. `set`: sala, oficina, estudio, garage, cabina, trono, cafe, calle, cielo, banco. `luz: "tenue"` apaga letreros detrás de los textos |
| `pan` | `[{k, x, dur}]` la cámara se mueve a `x` en el momento `k` |
| `zoom` | `[{k, s, x, y, dur}]` acerca (s 1.1–1.3) sobre un punto. `s: 1.0` vuelve |
| `props` | Objetos: `{tipo, x, y, s, k, fin, mov:[{k,x,y}], estados:[{k,…}]}` (ver lista abajo) |
| `actores` | Personas: `{look, var, camisa, pelo, s, desde, hasta, keys:[{k, x, y, pose, cara, z, fx}]}` |
| `extras` | Gente de fondo caminando: `{look, var, x0, x1, vel, y, s, luz, desde, hasta}` |
| `burbujas` | Globos de diálogo: `{k, de: índice_del_actor, texto, fin, dx}` (texto corto) |
| `titulos` | Etiqueta de neón: `{k, texto, c, fin, grande: true}` (`grande` = título enorme) |
| `chips` | Tarjetitas: `{k, texto, c, fin}` (pocas) |
| `numeros` | Cifra que cuenta: `{k, n, pre: "$", suf: "M", c, et: "rótulo", fin}` |
| `sacudidas` | `{k, f, dur}` temblor de cámara |
| `telefono` / `tablet` / `mando` / `barra` | Pantallas a cuadro completo (`{k, fin, …}`) |
| `escala` | 1.0–1.3 (zoom general; si algo no cabe, bájalo a 1.05) |
| `abre` | Abre desde un recuadro (efecto "cámara") |

**Elementos disponibles**
- **Colores (`c`):** `amar`, `cian`, `rosa`, `verde`, `rojo`.
- **Looks:** gamer, repartidor, rey, ejecutivo, inventor, piloto, jugador, jugadora, vendedor, oficial, sabio, cliente. `var` (un número) cambia cuerpo, peinado y rasgos: usa uno distinto por personaje.
- **Poses:** parado, camina, sentado, echado, juega, empuja, golpea.
- **Caras:** feliz, risa, sorpresa, triste, enojado.
- **`fx`:** salto, brinca, tiembla.
- **Props:** auto, billetes, bolsa_dinero, btc, caja_pizza, cajita, cartel, cheque, consola, control, corona, documento, escritorio, globos, grafico, jet, lupa, medusa, moneda, ovni, pizza, portatil, puerta, radar, sofa, taza, telefono, trono, tv, arena, baranda, dirigible, fuego, gato, jetski, linterna, muelle, orbe, pc, pelota, perro, sedan, surtidor, viento, volcan.
- **Animales:** `perro` y `gato`, con `pose` parado o sentado, `color`, `collar`, `cola`, `lengua`, `camina`, `dir` (−1 mira a la izquierda).

**Otras escenas** (tipo distinto de `pelicula`): versus, ranking, lista, contador, calendario, historia, mapa, etc. Busca `Object.assign(TIPOS` en `escena.html` para ver sus campos. El cierre es `{"tipo": "cierre", "desde": "s_fin"}`.

## 4. Grilla de pantalla (nada se toca)

| Elemento | Altura (y) |
|---|---|
| Subtítulos | hasta y≈390 (máx. 2 líneas; si no cabe, el motor los parte) |
| Etiqueta (`titulos`) | 525 |
| Tarjetita bajo etiqueta | 640 (sin etiqueta: 525; bajo título grande: 720) |
| Cifras (`numeros`) | ≥ 850, con el rótulo 110 px arriba |
| Suelo / personajes | ~1700–1780 |

- Personajes y objetos, **casi centrados**.
- Los globos salen de la cabeza de quien habla. Si se cortan en el borde, muévelos con `dx`.
- Lo que sale de una escena **no vuelve** (`fin`). El cierre aparece después de la última escena.

## 5. Revisar sin renderizar

```zsh
./venv/bin/python3 motor/producir.py guiones/2026-11-23/perros-18h.json --canal perros --dia 2026-11-23 --hora 18 --muestras 1 5 9 14 20
```

Deja una hoja de cuadros en `datos/trabajo/<lote>/muestras.png`. Ábrela y revisa:
- que nada choque;
- que se entienda sin sonido;
- que el cierre no tape nada.
