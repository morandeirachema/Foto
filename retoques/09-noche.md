<!-- nav -->
[← Anterior](08-paisaje.md) · [Índice](README.md) · [Siguiente →](10-recetas.md)
<!-- /nav -->

*Parte III · Por tipo de foto*

# 9. Fotografía nocturna

## 9.1. Antes de empezar

La fotografía nocturna es la que **más sufre en JPEG**: mucho ruido, sombras muy oscuras y una reducción de ruido de la cámara que puede haber borrado estrellas débiles. Se puede mejorar mucho, pero con expectativas realistas.

| Tipo | Reto principal |
|---|---|
| **Cielo estrellado / Vía Láctea** | Ruido, estrellas débiles, contaminación lumínica |
| **Luces artificiales** (ciudad, lodge, campamento) | Mezcla de luces de colores, luces quemadas |
| **Fuego y linternas** | Dominante naranja fuerte, contraste extremo |
| **Luna** | Luna quemada o paisaje negro |

**Qué evitar de noche:**
- **Sky Enhancer AI:** no está pensado para cielos nocturnos.
- **Dehaze en toda la foto:** dispara el ruido y la dominante.
- **Structure AI en toda la foto y Details altos:** convierten el ruido en "estrellas falsas".

## 9.2. Cielo estrellado y Vía Láctea

**1. Ruido, con cuidado**
- **Noiseless AI**, normalmente en *Middle*.
- **Riesgo:** una reducción de ruido fuerte **borra las estrellas pequeñas** porque las confunde con ruido. Mira al 100 % y baja **Luminosity Denoise** hasta que vuelvan a verse.
- **Color Denoise:** el ruido de color (manchas moradas y verdes) es lo que más ensucia un cielo nocturno.
- **Apilar fotos:** si hiciste varias fotos iguales seguidas, apílalas **antes** de editar: es lo que más reduce el ruido. Luminar no lo hace; el paso a paso está al final de esta sección ([Apilar una serie](#apilar-una-serie-fuera-de-luminar)).

**2. Balance de blancos**
- **Mira primero de qué color es el cielo y por qué.** Naranja o amarillo junto al horizonte, sobre un pueblo o un lodge: contaminación lumínica. Una **banda verde suave** cerca del horizonte en un cielo muy oscuro, como el de Namibia: casi seguro es **luminiscencia atmosférica** (*airglow*), luz natural del propio aire. Es real: no la borres.
- **Si toda la foto tira a marrón o a naranja** (pasa con un balance de blancos fijo de día), mueve **Temperature** un poco hacia el azul, hasta que el cielo sea **gris neutro oscuro o algo cálido**. No busques un azul intenso: el cielo nocturno real casi nunca es azul.
- **Tint** hacia el magenta solo si **toda** la foto está verdosa. Si el verde es una banda en el horizonte, déjala, o bájale un poco la saturación con una máscara.
- Las estrellas deben verse blancas con matices, no todas del mismo color.
- **Dos gustos, los dos defendibles.** Roger Clark defiende el color natural, con balance de luz de día: cielo neutro o cálido y Vía Láctea parda ([Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)). Ian Norman prefiere un cielo más frío, en torno a 3900 K ([Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)). Para un álbum de recuerdo, quédate cerca de lo que viste.

**3. Luz**
- **Exposure** +0,3/+0,7 si está muy oscura (vigila el ruido).
- **Blacks** un poco **abajo** (−5 a −15) **solo si el cielo se ve gris**: un cielo oscuro disimula el ruido y da contraste a las estrellas.
- **Si la foto ya salió oscura** (cielo casi negro y Vía Láctea apenas visible), **no bajes Blacks**: perderías las estrellas débiles. Sube la luz poco a poco con **Curves** (sección 6.1), mirando al 100 %. Hacia un paso de luz (+1 EV) empiezan a verse bandas y ruido en un JPEG: ese es tu límite, y el motivo para apilar si tienes una serie (más abajo).
- **Highlights** −10/−20 si hay alguna luz quemada.
- **Shadows** con cuidado: es la zona con más ruido.

**4. La Vía Láctea**
- **Supercontrast → Highlights** con máscara **Radial** (**`R`**) sobre el núcleo, en modo **Inverted** para que actúe dentro del círculo: realza las nubes de estrellas sin tocar el fondo.
- **Structure AI** +10/+20 con la misma máscara (**Copy**/**Paste** de la máscara).
- **Dodge & Burn → Lighten** (**Strength** 10) sobre el núcleo, si necesita más luz.
- **Landscape → Dehaze** con la misma máscara, **+10**: aumenta el contraste de las nubes de estrellas.
- **Por qué en local:** si subes el contraste en todo el cielo, sube también el ruido del fondo.

**5. Contaminación lumínica en el horizonte**
- **Color Harmony** con un **Gradient** desde el horizonte hacia arriba: **Warmth** −5 a −10 para neutralizar el naranja; y **Dodge & Burn → Darken** (**Strength** 15) sobre el resplandor.
- Si el resplandor es fuerte, **no intentes eliminarlo**: déjalo como un degradado cálido suave. Si lo quitas del todo, queda una banda gris sucia.

**6. Primer plano**
- Suele estar muy oscuro: **Dodge & Burn → Lighten** suave sobre el suelo ([sección 5.5](05-ajustes-locales.md)), o **Light Depth → Brightness Near**.
- **No lo aclares demasiado.** Una silueta oscura o un primer plano tenue es más creíble que uno iluminado como de día.
- **De noche, la máscara de cielo puede fallar** porque el límite entre cielo y suelo apenas se ve. Revísala con **`/`** y corrígela con **Brush**, o usa un **Gradient** en el horizonte.

**7. Acabado**
- **Details:** Sharpen **0 a +5** y **Sharpening Masking** **60–70** (alto: solo enfoca los bordes claros). El enfoque fuerte convierte el ruido en estrellas falsas.
- **Vignette** −10.
- Revisa al 100 %: bandas en el cielo, halos en el horizonte, estrellas convertidas en manchas.

**Estrellas alargadas (pequeños trazos):** salen cuando la exposición fue demasiado larga para la focal usada. No tienen arreglo real al editar. Para la próxima vez, consulta la sección 15.3.

### Apilar una serie (fuera de Luminar)

**Qué es:** el programa alinea las estrellas de varias fotos iguales y hace la media. El ruido, que es distinto en cada foto, se cancela; la señal, que es la misma, se queda. Con 10 fotos, el ruido baja en teoría a un tercio, y el archivo resultante (TIFF de 16 bits) aguanta mucho mejor que un JPEG el aclarado de la Vía Láctea.

**Qué necesitas:** varias fotos **seguidas**, con el **trípode quieto** y **los mismos ajustes**. Búscalas en el catálogo: misma exposición e ISO, con segundos de diferencia.

Las herramientas de fusión de Luminar (HDR Merge, Panorama Stitching y Focus Stacking) no incluyen un apilado para reducir ruido, así que hace falta otro programa. Para Mac:

| Programa | Precio | Para qué | Enlace |
|---|---|---|---|
| **Starry Landscape Stacker** | Unos 40 USD; tiene versión de prueba | Alinea el cielo y deja el suelo quieto con una máscara. Es el equivalente en Mac de Sequator | <https://sites.google.com/site/starrylandscapestacker/home> |
| **Siril** | Gratis | Apila y corrige degradados de fondo (*background extraction*). No tiene "suelo fijo" de un clic | <https://siril.org/> |
| **StarStaX** | Las versiones antiguas, gratis | Solo para **trazas de estrellas**: suma los trazos de una serie larga | <https://starstax.net/> |

Sequator, que citan muchas guías, solo existe para Windows.

**Paso a paso:**
1. **No edites las fotos antes.** Ni ruido, ni enfoque, ni correcciones de lente: estropean el apilado.
2. Abre la serie en el programa. **No está confirmado que acepten JPEG**: pruébalo con la versión de prueba ([PENDIENTES](../PENDIENTES.md)). Si no los acepta, convierte antes los JPEG a TIFF, sin editarlos.
3. Marca el cielo (en Starry Landscape Stacker, pintando la máscara) y apila.
4. Guarda el resultado como **TIFF de 16 bits**.
5. Añade ese TIFF al catálogo de Luminar (admite TIFF de 8 y 16 bits) y edítalo con los pasos de esta sección. Notarás que Noiseless AI casi no hace falta.

Un apilado de fotos del mismo sitio y del mismo momento no es un montaje. Si enseñas la foto, basta con decir "apilado de 10 tomas".

## 9.3. Luces artificiales (lodge, campamento, ciudad)

- **Balance de blancos:** no neutralices del todo las bombillas cálidas. Algo de calidez hace la escena acogedora.
- **Highlights** −30/−50 para recuperar las luces. Si las bombillas están quemadas, déjalas: es normal.
- **Noiseless AI** casi siempre.
- **Magic Light AI** (opcional, **Intensity** 10–20) añade rayos y brillo a bombillas y farolas.
- **HSL:** naranja → Saturation **−10** si la luz es demasiado intensa.
- **Luces de distintos colores:** neutraliza la que más se vea y deja la otra con su color.

### Animales en una charca iluminada con focos

Es el caso más difícil del viaje: ISO muy alto (hasta 12800), todo teñido de **naranja** por el foco y el fondo negro. **Un color neutro no se puede recuperar de un JPEG así**: bajo esa luz casi toda la información está en el canal rojo. Esto es criterio de esta guía (no hay tutoriales de referencia para este caso), así que pruébalo con una foto y ajusta:

1. **Descarta primero las movidas.** A 1/25 s, un animal que se mueve sale borroso, y eso no tiene arreglo.
2. **Mira el canal rojo** en el histograma (sección 1.3). Si toca el borde derecho, no subas la exposición ni la saturación.
3. **Noiseless AI**, con el nivel propuesto. Revisa la piel del animal al 100 %: si parece de cera, baja **Luminosity Denoise**.
4. **Elige una de tres salidas:**
   - **Corrección parcial:** **Temperature** hacia el azul solo hasta que el animal deje de verse de un único naranja. Si sigues, aparecen colores falsos.
   - **Menos saturación:** herramienta **Color → HSL → Saturation**, naranja hacia abajo. Conserva el ambiente y recupera textura en la piel.
   - **Blanco y negro** (**Black & White**): elimina la dominante y disimula el ruido de color. Suele ser la que mejor queda.
5. **Deja el fondo negro.** Aclarar las sombras solo saca ruido.
6. **Compártela a tamaño pequeño.** A 2000 px el ruido se ve mucho menos que al 100 %; no es una foto para imprimir en grande.

## 9.4. Fuego de campamento y linternas

- **Decide el color.** La luz del fuego es muy naranja. Corrige un poco (Temperature **−5 a −10**), pero **no la vuelvas blanca**: el fuego tiene que seguir pareciendo fuego.
- **Shadows** +20 para ver las caras; **Highlights** −40 para que la llama tenga forma.
- Si hay personas, **Face AI → Face Light** (+10 a +20) o **Dodge & Burn → Lighten** (**Strength** 15) sobre las caras.
- **Vignette** algo más marcada (−20) para concentrar la luz en el fuego.
- **No enfoques las llamas ni las chispas**: el enfoque convierte su movimiento en ruido.

## 9.5. Luna

- **Luna sola, con teleobjetivo:** baja **Highlights** y **Exposure** hasta ver los cráteres; **Structure AI** +20 y **Details** moderado. Fondo negro (**Blacks** abajo).
- **Luna en un paisaje:** en un JPEG suele estar quemada, porque es mucho más brillante que el paisaje. Si lo está, **no se puede recuperar**: acepta un punto blanco o hazle una foto aparte.
- **Añadir una luna de otra foto** (**Layers → + → My Images**) es un montaje: hazlo solo en fotos creativas y dilo al compartirla (sección 14).

## 9.6. Hora azul y crepúsculo

El mejor momento para la "foto nocturna" con JPEG suele ser **antes** de la noche cerrada, cuando el cielo aún tiene luz azul y el ruido es mucho menor.
- Balance de blancos: deja el azul.
- **Highlights** −30 en las luces artificiales; **Shadows** +10 a +20.
- Ruido: a menudo basta con **Denoise** (Luminosity Denoise +10 a +20, Color Denoise +20 a +30).
- **Twilight Enhancer AI** (preset **Blue**) puede reforzar el ambiente, con **Amount** 20–30.

## Ejercicio (una tarde)

1. Elige una foto nocturna de Namibia (estrellas, fuego o luces).
2. Primero **Noiseless AI**, revisando al 100 % que no desaparezcan las estrellas pequeñas.
3. Corrige el balance de blancos hasta un cielo gris azulado (o un fuego que siga pareciendo fuego).
4. Compara con **`\`** y revisa al 100 % las esquinas.

**Aprobado cuando** el ruido no se ve a tamaño pantalla y el color de la noche es creíble.

<!-- nav -->
[← Anterior](08-paisaje.md) · [Índice](README.md) · [Siguiente →](10-recetas.md)
<!-- /nav -->
