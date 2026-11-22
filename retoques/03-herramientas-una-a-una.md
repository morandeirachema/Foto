<!-- nav -->
[← Anterior](02-luminar-por-dentro.md) · [Índice](README.md) · [Siguiente →](04-flujo-base.md)
<!-- /nav -->

*Parte I · Fundamentos*

# 3. Las herramientas, una a una: dónde están, qué hacen y cuánto mover

Si no conoces Luminar, este es el capítulo de consulta. Para cada herramienta que usa la guía encontrarás **dónde está**, **qué hace en palabras sencillas**, **con qué valor empezar**, **hasta dónde llegar con un JPEG** y **cómo saber que te has pasado**. Tenlo abierto al lado mientras editas.

## 3.1. Antes de empezar: cómo se usa una herramienta

1. Abre la foto y pulsa **`E`** (pestaña **Tools**). A la derecha aparecen las herramientas, agrupadas por categorías (**Essentials**, **Landscape**, **Creative**, **Portrait**, **Professional**, **Image Quality**; [sección 2.1](02-luminar-por-dentro.md)).
2. **Haz clic en el nombre** de una herramienta para abrirla y ver sus deslizadores.
3. **Arrastra un deslizador** y mira la foto, no el número. El número que ves junto al deslizador es el que usa esta guía.
4. **Mantén pulsada `\`** para ver la foto original y suéltala para volver a la editada. Hazlo a menudo.
5. Para revisar detalles (ruido, enfoque, bordes), **`⌘1`** amplía al 100 %; **`⌘0`** vuelve a encajar la foto.
6. Para deshacer, **`⌘Z`**. En Dodge & Burn, la **flecha curva junto al nombre** de la herramienta la devuelve a cero (está documentado para esa herramienta; en las demás, búscalo junto al nombre o usa **`⌘Z`**).

> **Sobre los números de esta guía.** Son **puntos de partida para JPEG**, no valores oficiales: Skylum no publica la escala de cada deslizador. La primera vez que abras una herramienta, mira hasta dónde llega cada deslizador (por ejemplo, de −100 a +100) y anótalo en [PENDIENTES](../PENDIENTES.md). Si un valor de la guía no encaja con tu escala, guíate por la columna "te has pasado si…": esa no depende del número.

**Cómo mover un deslizador sin pasarte (método para cualquier herramienta):**
1. Llévalo **muy lejos** a propósito, hasta que el efecto se vea exagerado. Así ves qué hace.
2. **Vuelve a cero.**
3. Súbelo **poco a poco** hasta que la foto mejore, y para ahí.
4. Al final del todo, **baja un 20–30 %** lo que hayas subido. El ojo se acostumbra a los efectos fuertes mientras edita.

## 3.2. Develop (Essentials): la luz y el color de toda la foto

La herramienta principal. Se usa **sin máscara**, para toda la foto: si le pones una máscara, **toda** su corrección pasa a esa zona y el resto de la foto se queda sin corregir ([sección 5.2](05-ajustes-locales.md)).

| Deslizador | Qué hace | Empieza en | Límite en JPEG | Te has pasado si… |
|---|---|---|---|---|
| **Exposure** | Aclara u oscurece **toda** la foto | ±0,3 (hasta ±0,7) | ±1 | La foto entera se ve gris y plana, o el cielo se quema |
| **Smart Contrast** | Separa claros y oscuros | +10 a +25 | +40 | Los colores se vuelven pesados y las sombras, negras |
| **Highlights** | Baja **solo las zonas claras**: recupera cielo y nubes | −20 a −50 | −60 | Las nubes se ven grises y sucias o aparece un halo en el horizonte |
| **Shadows** | Sube **solo las zonas oscuras** | +15 a +40 | +50 | La foto pierde volumen (todo parece igual de claro) o aparece ruido |
| **Whites** | Mueve el punto más claro | Con **`J`**: sube hasta el primer aviso rojo y baja un poco | — | Aparecen zonas rojas grandes con **`J`** |
| **Blacks** | Mueve el punto más oscuro | Con **`J`**: baja hasta el primer aviso azul y sube un poco | — | Aparecen zonas azules grandes con **`J`** |
| **Temperature** | Más azul (−) o más amarillo (+) | ±5 a ±15 | ±25 | Los blancos dejan de parecer blancos, o un atardecer se vuelve gris |
| **Tint** | Más verde (−) o más magenta (+) | ±5 | ±15 | Las sombras o la piel se tiñen de verde o rosa |
| **Saturation** | Más color en **todos** los colores | 0 a +10 | +20 | Pieles naranjas, verdes fosforito |
| **Vibrance** | Más color sobre todo en los **apagados** | +5 a +20 | +30 | Colores "de cartel" |
| **Curves** | Contraste por zonas con puntos ([sección 6.1](06-herramientas-avanzadas.md)) | Una S muy suave | — | Negros o blancos sin detalle |

**El cuentagotas** (**`W`**, dentro de Develop → Color): haz clic en algo que deba ser gris o blanco neutro (una nube en sombra, una roca gris) y Luminar ajusta Temperature y Tint por ti.

## 3.3. Noiseless AI y Denoise (Image Quality / Essentials): el ruido

| Control | Qué hace | Empieza en | Te has pasado si… |
|---|---|---|---|
| **Nivel** de Noiseless AI (Low, Middle, High) | La intensidad general; Luminar propone uno al abrirla | **El que proponga** | — |
| **Luminosity Denoise** | Quita el granito gris | El del nivel propuesto; si el pelo parece de cera, baja de 10 en 10 | El pelaje, la piel o las estrellas parecen de plástico |
| **Color Denoise** | Quita las manchas de colores | El del nivel propuesto; puede subir sin miedo | Rara vez: los colores finos se apagan |
| **Details** | Recupera el detalle que la reducción de ruido se lleva | +10 | Vuelve el ruido o aparecen artefactos |
| **Sharpness** | Recupera la nitidez | 0 a +10 | Aparece un halo en los bordes |

**Denoise** (Essentials) tiene **Luminosity Denoise**, **Color Denoise** y **Boost**. Para ruido ligero: Luminosity +10 a +20, Color +20 a +30, Boost 0.

**Comprueba siempre al 100 %** (**`⌘1`**): a tamaño pantalla, el ruido y el exceso de reducción no se ven.

## 3.4. Enhance AI (Essentials): mejora general en un deslizador

| Deslizador | Qué hace | Empieza en | Límite | Te has pasado si… |
|---|---|---|---|---|
| **Accent AI** | Ajusta a la vez sombras, luces, contraste, color y detalle | +15 a +35 | +50 | La foto parece "procesada" o chillona |
| **Sky Enhancer AI** | Mejora un cielo **de día** (no funciona de noche; en gris si no detecta cielo) | +20 a +40 | +60 | El cielo se ve demasiado azul o aparecen bandas |

Si usas Accent AI alto, **baja Smart Contrast y Shadows** en Develop: suman efectos parecidos.

## 3.5. Color (Essentials): el color fino

| Control | Qué hace | Empieza en | Te has pasado si… |
|---|---|---|---|
| **Vibrance** | Como en Develop | +5 a +15 | Colores de cartel |
| **Remove Color Cast** | Deslizador que detecta y quita una dominante | Súbelo poco a poco; quédate con el resultado solo si convence | La foto pierde su ambiente (un atardecer neutro) |
| **HSL → Hue** | Cambia el tono de un color concreto | ±5 a ±10 | Colores imposibles (hierba azulada) |
| **HSL → Saturation** | Más o menos intensidad de un color concreto | −20 a +10 | Un color "salta" del resto |
| **HSL → Luminance** | Aclara u oscurece un color concreto | −20 a +10 | Bandas en el cielo al oscurecer el azul |

**Las tres correcciones de HSL que más usarás:**
- **Cielo más profundo:** Azul → Luminance **−15**.
- **Verdes menos artificiales:** Verde → Saturation **−15**.
- **Hierba seca dorada y no amarilla chillona:** Amarillo → Saturation **−10**.

## 3.6. Structure AI y Details (Essentials): textura y nitidez

| Control | Qué hace | Empieza en | Límite | Te has pasado si… |
|---|---|---|---|---|
| **Structure AI → Amount** | Detalle y claridad: textura del pelo, la roca, las dunas. Según Skylum, "reconoce a las personas" para no sobreprocesar caras y piel. En negativo, suaviza (efecto de desenfoque) | +10 a +25 | +35 | Halos alrededor del sujeto, aspecto "HDR" sucio, ruido en el cielo |
| **Structure AI → Boost** | Realza sobre todo los detalles pequeños; más agresivo que Amount | 0 a +10 | +20 | Grano y textura áspera |
| **Details → Small Details** | Nitidez de lo muy fino (pelo, plumas) | +10 a +20 | +30 | Grano áspero |
| **Details → Medium Details** | Nitidez de texturas medias | +5 a +15 | +25 | Aspecto "crujiente" |
| **Details → Large Details** | Contornos grandes | 0 a +10 | +15 | Halo claro alrededor del sujeto |
| **Details → Sharpen** | Enfoque general | +10 a +20 | +30 | Bordes con línea blanca |
| **Sharpening Masking** | Limita el enfoque a los bordes | **30–70** (valor que recomienda Skylum) | — | Si lo bajas mucho, se enfoca también el cielo |

**Regla:** en un JPEG, la cámara **ya enfocó**. Quédate en la parte baja de estos rangos.

## 3.7. Landscape (Landscape): neblina, dorado y vegetación

| Control | Qué hace | Empieza en | Límite | Te has pasado si… |
|---|---|---|---|---|
| **Dehaze** | Quita calima y neblina | +10 a +20 | +30 | Colores pesados, cielo demasiado oscuro, la foto pierde profundidad |
| **Golden Hour** | Calidez y brillo dorado | +10 a +20 | +30 | Todo naranja |
| **Foliage Enhancer** | Vegetación más viva | +10 a +20 | +30 | Verdes fosforito |

## 3.8. Dodge & Burn (Professional): aclarar u oscurecer pintando

La herramienta de los ajustes locales ([sección 5](05-ajustes-locales.md)).

| Control | Qué hace | Empieza en | Te has pasado si… |
|---|---|---|---|
| **Lighten / Darken** | Pincel que aclara u oscurece | — | — |
| **Brush Size** | Tamaño del pincel (**`[`** **`]`**) | Ojos: más pequeño que el iris. Sombras y cielo: más grande que la zona | — |
| **Softness** | Lo suave del borde del pincel (**`⇧[`** **`⇧]`**) | **Casi al máximo** | Si es baja, se ven las pinceladas |
| **Strength** | Cuánto cambia cada pasada | **Empieza en 15** y sube de 5 en 5 si no ves efecto | Manchas con la forma del pincel |
| **Overall Amount** | La intensidad de todo lo pintado | Al final, baja si se nota | La foto "parece retocada" |

## 3.9. Acabado: Vignette y Film Grain

| Control | Qué hace | Empieza en | Límite | Te has pasado si… |
|---|---|---|---|---|
| **Vignette → Amount** | A la izquierda (−) oscurece los bordes; a la derecha (+) los aclara | −10 a −20 | −30 | Esquinas negras "de filtro" |
| **Vignette → Inner Light** | Aclara la zona central, la que no oscurece el viñeteado | 0 a +10 | +20 | El centro parece iluminado con un foco |
| **Vignette → Choose Subject** | Centra el viñeteado sobre el sujeto (clic en la foto) | Sobre el animal | — | — |
| **Film Grain → Amount** | Añade grano fino; disimula las bandas del cielo | 5 a 10 | 15 | Grano visible a tamaño pantalla |

## 3.10. Herramientas avanzadas, en resumen

| Herramienta | Para qué | Empieza en | Detalle |
|---|---|---|---|
| **Supercontrast** (Professional) | Contraste por zonas | **Midtones** +10 a +20; el resto en 0 | [Sección 6.2](06-herramientas-avanzadas.md) |
| **Color Harmony** (Professional) | Ambiente y dominantes por zonas | **Warmth** ±5 a ±15; **Split Color Warmth → Warm** +10 a +15 | [Sección 6.3](06-herramientas-avanzadas.md) |
| **Light Depth** (Creative) | Luz distinta en primer plano y fondo | **Amount** +20 a +30 | [Sección 6.5](06-herramientas-avanzadas.md) |
| **Black & White** (Essentials) | Blanco y negro | **Blue** −30 a −50 en Luminance para oscurecer el cielo | [Sección 6.6](06-herramientas-avanzadas.md) |

## 3.11. Recorte y limpieza

| Herramienta | Atajo | Cómo |
|---|---|---|
| **Crop AI** | **`C`** | **Auto Straighten** para nivelar (**Horizon Alignment** en el Crop AI anterior); elige proporción; **`X`** cambia vertical/horizontal; sal de la herramienta para aplicar |
| **Erase** | **`⌘E`** | Pinta sobre lo que quieres quitar (pincel algo mayor que el objeto) y pulsa **Erase** |
| **Remove Dust Spots** | — | Quita automáticamente manchas de polvo del sensor; luego afina con Erase |
| **Clone** | **`⌘J`** | Haz clic para fijar de dónde copiar (**`⌥`**-clic lo cambia después); pinta con toques cortos |

## 3.12. Las demás herramientas, en una tabla

Las usa la guía en casos concretos. ✳️ = **inventa** contenido: perfecta para tu álbum; dilo si presentas la foto como documento ([sección 14](14-etica.md)).

| Herramienta (categoría) | Para qué | Controles clave | Empieza en |
|---|---|---|---|
| **Supersharp AI** (Image Quality) | Fotos algo movidas o blandas | Modo **Motion Blur** (movimiento) o **Universal**; nivel **Low / Middle / High** | Motion Blur, **Low** |
| ✳️ **Upscale** (Extra) | Ampliar una foto muy recortada | El factor, **hasta 6×** | **2×**, con el ruido ya quitado; el enfoque suave, después |
| **Face AI** (Portrait) | Caras con poca luz | **Face Light** | +10 a +20 |
| **Twilight Enhancer AI** (Landscape) | Luz de hora dorada o azul | Presets **Blush, Golden, Blue, Emerald, Mauve**; **Amount** | Preset y **Amount** 20–30 |
| **Water Enhancer AI** (Landscape) | Agua más clara y viva | **Amount**, **Blue**, **Green**, **Brightness**, **Contrast**; pincel **Draw/Erase** | **Amount** 20–30 |
| ✳️ **Sky AI** (Landscape) | Sustituir un cielo; Skylum lo diseña para cielos **planos o quemados** | Elegir cielo; **Relight Strength**, **Horizon Position**, **Close Gaps** | Elige el cielo y ajusta **Relight Strength** hasta que la luz del suelo encaje |
| ✳️ **Atmosphere AI** (Landscape) | Añadir niebla o bruma | Modo (**Fog**, **Mist**, **Haze**…), **Amount** | **Amount** 10–20 |
| **Magic Light AI** (Creative) | Rayos y brillo en bombillas y farolas | **Intensity**, **Size**, **Number of Beams** | **Intensity** 10–20 |
| **Color Transfer** (Creative) | Igualar la paleta con otra foto | Foto de referencia, **Amount** | **Amount** 30–50 |
| **Mood (LUT)** (Creative) | Un "look" de color predefinido | LUT, **Amount** | **Amount** 30–50 |
| **Matte** (Creative) | Aspecto mate, de película | **Amount**, **Fade** | **Amount** 10–20 |
| **Toning** (Creative) | Teñir luces y sombras (también en blanco y negro) | **Highlights/Shadows Saturation** y **Hue**, **Balance** | Saturation 10–20 |
| **Glow** (Creative) | Brillo soñador (incluye **Orton Effect**) | Tipo, **Amount** | **Amount** 10–20, con máscara fuera del sujeto |
| ✳️ **GenErase** (Extra) | Borrar objetos grandes o difíciles | Pinceles **Select/Deselect**, botón **Erase** (pulsa otra vez para otra versión) | Un objeto cada vez; selección generosa |
| ✳️ **GenExpand** (Extra) | Ampliar el lienzo | Cuánto amplías, **hasta 25 %** | **10 %**, de un lado cada vez |
| **Remove Powerlines** | Quitar cables del cielo | Automático; luego afina con Erase | — |

## 3.13. Hoja de bolsillo: los diez números de partida

Si solo te quedas con una tabla, que sea esta. Es el punto de partida para un JPEG típico de día; luego ajusta mirando la foto.

| Herramienta → control | Valor |
|---|---|
| Develop → Exposure | **+0,3** si está oscura / **−0,3** si está clara |
| Develop → Highlights | **−30** |
| Develop → Shadows | **+25** |
| Develop → Whites / Blacks | Con **`J`**, hasta el primer aviso |
| Develop → Smart Contrast | **+15** |
| Enhance AI → Accent AI | **+20** |
| Color → Vibrance | **+10** |
| Structure AI → Amount | **+15** |
| Details → Sharpen | **+10** (Sharpening Masking **50**) |
| Vignette → Amount | **−12** |

## Ejercicio (una tarde)

1. Con una foto cualquiera, abre **Develop** y aplica a cada deslizador el método de 3.1: llévalo al extremo, vuelve a cero y súbelo hasta que la foto mejore.
2. Anota el **número** en el que te paraste en cada uno y compáralo con la columna "empieza en".
3. Anota también **hasta dónde llega** cada deslizador y apúntalo en [PENDIENTES](../PENDIENTES.md).

**Aprobado cuando** reconoces a simple vista, en una foto ajena, cuándo se ha pasado alguien con Shadows, Structure AI o Saturation.

<!-- nav -->
[← Anterior](02-luminar-por-dentro.md) · [Índice](README.md) · [Siguiente →](04-flujo-base.md)
<!-- /nav -->
