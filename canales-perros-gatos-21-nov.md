# Canales de perros y gatos — paquete de lanzamiento (21-nov-2026)

> Pedido de Tao: un canal de perros y uno de gatos, 1–2 videos al día, el micronicho más potente de cada animal y un **animal protagonista fijo**. Mientras tanto se suben los videos de prueba y se ve qué tal.

## 1. Decisión (nombres elegidos por Tao, 21-nov)
| | Perros | Gatos |
|---|---|---|
| **Nombre** | **The Dogs Decoder** | **The Cats Decoder** |
| **Handle** | @TheDogsDecoder | @TheCatsDecoder |
| Descartado | "Dog Decoded" (no estaba disponible) | — |
| **Micronicho** | "Why your dog does that": conducta explicada con ciencia (estudios reales) | "Why your cat does that": lo mismo, con gatos |
| **Fórmula de título** | Why Your Dog ___ | Why Your Cat ___ |
| **Protagonista** | **Biscuit**: perro dorado mestizo, collar rosa, sentado junto a su humano en el sofá | **Mochi**: gata atigrada gris, ojos verdes, junto a su humano en el sofá |
| **Voz** | `af_heart` 1.2, en-us | `bf_emma` 1.2, en-gb |
| **CTA hablado** | "Follow to decode your dog." | "Follow to decode your cat." |
| **Marca en el video** | THE DOGS DECODER | THE CATS DECODER |
| **Hora** (1 al día para partir) | 18h | 21h |
| Música | deep | deep |
| Carpeta | `~/Desktop/YouTube/DogDecoded` | `~/Desktop/YouTube/CatDecoded` |

**Por qué este micronicho:** responde preguntas que la gente ya busca ("why does my dog…"), se puede verificar con estudios y da para muchos videos con el mismo formato.

## 2. Textos del canal
**Descripción, The Dogs Decoder**
> Why does your dog do that? 🐶
> Short, science-backed answers about dog behavior: head tilts, puppy eyes, zoomies, tail wags and more. Every fact comes from real studies and vet sources.
> One dog mystery decoded every day. Follow to decode your dog.

**Descripción, The Cats Decoder**
> Why does your cat do that? 🐱
> Short, science-backed answers about cat behavior: slow blinks, kneading, purring, the 3 a.m. zoomies and more. Every fact comes from real studies and vet sources.
> One cat mystery decoded every day. Follow to decode your cat.

## 3. Logo y banner
- **Hechos en ChatGPT (21-nov)**, en la cuenta de Tao, en los chats "Create Dog Profile Image" y "Create Cat Profile Image". Cada chat tiene el perfil circular y el banner 16:9, con el mismo estilo vector.
- Versiones hechas con el motor (respaldo): `~/gta-shorts/assets/perfil_dog_decoded.png`, `banner_dog_decoded.png`, `perfil_cat_decoded.png`, `banner_cat_decoded.png`. Tienen el nombre antiguo en el banner.
- Banner de YouTube: mínimo 2048×1152. Si el de ChatGPT sale más chico, se escala a 2560×1440 antes de subirlo.

## 4. Videos
### Hechos (21-nov)
| Canal | Título | Dato verificado |
|---|---|---|
| Perros | Why Your Dog Tilts Its Head 🐶 | Sommese et al. 2021, *Animal Cognition* (Budapest): perros que saben nombres de juguetes ladearon la cabeza en 43% de los ensayos vs 2% los típicos; cada perro, siempre al mismo lado. |
| Gatos | Why Your Cat Slow Blinks at You 🐱 | Humphrey et al. 2020, *Scientific Reports* (Sussex y Portsmouth): los gatos devuelven más parpadeos lentos y se acercan más a un desconocido tras un parpadeo lento que con cara neutral. |

### Siguientes (guiones listos para hacer)
**Perros — Why Your Dog Stares at You**
- Nagasawa et al. 2015, *Science* (Azabu, Japón): 30 perros con sus dueños, 30 minutos. Las miradas largas subieron la oxitocina del dueño y del perro. En lobos criados por personas, no. (Fuentes: Scientific American, National Geographic, Smithsonian, Frontiers.)
- Voz: "When your dog stares at you, something happens in both your bodies." … "Tell me how long your dog stares at you." Cierre: DOES YOURS STARE? → ALL DAY / NOT MUCH.

**Gatos — Why Your Cat Kneads You**
- De gatitos, amasan la panza de la madre para que salga la leche. De adultos, cuando están tranquilos, a menudo antes de dormir. Tienen glándulas de olor en las patas: al amasar te dejan su olor. (Fuentes: VCA, PetMD, PDSA, Scientific American.)
- Voz: "Your cat kneads you like dough. It started when it was a newborn kitten." … "Translation: you've been claimed." … "Tell me where your cat kneads you." Cierre: BLANKET OR YOU? → BLANKET / ME.

## 5. Motor
- `UTILERIA.perro` y `UTILERIA.gato`: siluetas hechas con puntos de referencia de animales reales (lomo, grupa, muslo doblado, codo, rodilla, corvejón, almohadillas) y curva suave.
- Poses: `sentado`, `parado` y `echado` (este último solo el perro).
- Opciones: `inclina` (cabeza ladeada), `collar`, `lengua`, `cola`, `camina`, `lento` (parpadeo lento del gato), `amasa` (gato amasando), colores (`color`, `color2`, `oscuro`, `lejos`, `ojos`).
- `UTILERIA.pelota`: pelota de tenis.
- Tamaño: el perro con `s` 1.0 y el gato con `s` ~0.9, al lado de una persona con `s` 1.0.
- Configuración: `canales/perros.json` y `canales/gatos.json`.

## 6. Cuidado
- Solo conducta con estudio o fuente veterinaria (2+ fuentes). **Nada de salud ni consejos médicos.**
- Canal nuevo: idealmente usarlo unos días como persona (ver y comentar videos de perros/gatos) antes de subir seguido.

## 7. Reglas por tipo de video (Tao, 23-nov)
> No todos los videos tienen que ser iguales. Cada **tipo** tiene sus reglas, y se ajustan según cómo rinda cada uno.

**Origen:** a Tao le gustó el video de los zoomies (ya subido), pero le faltó **por qué pasa** (qué lo provoca, por qué después del baño).

| Tipo | Cuándo se usa | Reglas | Ejemplo de título |
|---|---|---|---|
| **Explicar una conducta** | Una conducta concreta ("¿por qué hace X?") | 1. **Cuándo pasa** (disparadores). 2. **Por qué pasa** (qué ocurre en el cuerpo o la cabeza, con fuente). 3. **Ejemplo** que el dueño reconozca. | Why Your Dog Goes Crazy After a Bath |
| **Lo que te está diciendo** | Una señal o gesto ("si te lame…") | Qué significa + **cómo reconocerlo** en tu animal. Tono cercano: el animal "te habla". | What Your Cat Means When It Headbutts You |
| **Lista / ranking** | Varias conductas, razas, etc. | Ítems cortos, sin explicar cada mecanismo. **De menos a más sorprendente**; el mejor, al final. | 5 Things Your Dog Only Does With You |
| **Dato sorprendente** | Un dato que rompe una creencia ("no tiene 7, tiene 15") | El dato en el segundo 1 + **contexto o cálculo** + cómo aplicarlo a tu animal. | Your Dog Isn't 7. It's 15. |

**Medir siempre:** cada video queda anotado con **su tipo y su fórmula de título**. Cada semana se compara **por tipo y por título**, no solo video por video, y las reglas se cambian según lo que rinda.

Referencia de mercado: `claude/micronichos-mercado-23-nov.md`. Los títulos que más rinden en perros y gatos prometen "la razón" o "lo que te está diciendo", pero eso es una hipótesis hasta medirlo en nuestros canales.
