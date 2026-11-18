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
- **Apilar fotos:** si hiciste varias fotos iguales seguidas, un programa de astrofotografía puede apilarlas y reducir mucho el ruido (por ejemplo, Sequator en Windows o Starry Landscape Stacker en Mac). Las herramientas de fusión de Luminar (HDR Merge, Panorama Stitching y Focus Stacking) no incluyen un apilado para reducir ruido. Después terminas la edición en Luminar.

**2. Balance de blancos**
- El cielo nocturno suele salir naranja (contaminación lumínica) o verdoso.
- **Temperature** hacia el azul hasta que el cielo sea **gris azulado oscuro**, no naranja ni morado. El verde se corrige con **Tint** hacia el magenta.
- Un cielo nocturno creíble es neutro o ligeramente azul. Las estrellas deben verse blancas con matices, no todas del mismo color.

**3. Luz**
- **Exposure** +0,3/+0,7 si está muy oscura (vigila el ruido).
- **Blacks** un poco **abajo** (−5 a −15). Un cielo negro profundo disimula el ruido y da contraste a las estrellas; si lo dejas gris, la foto parece sucia.
- **Highlights** −10/−20 si hay alguna luz quemada.
- **Shadows** con cuidado: es la zona con más ruido.

**4. La Vía Láctea**
- **Supercontrast → Highlights** con máscara **Radial** (**`R`**) sobre el núcleo, en modo **Inverted** para que actúe dentro del círculo: realza las nubes de estrellas sin tocar el fondo.
- **Structure AI** +10/+20 con la misma máscara (**Copy**/**Paste** de la máscara).
- **Dodge & Burn → Lighten** muy suave sobre el núcleo, si necesita más luz.
- **Landscape → Dehaze** con la misma máscara, suave: aumenta el contraste de las nubes de estrellas.
- **Por qué en local:** si subes el contraste en todo el cielo, sube también el ruido del fondo.

**5. Contaminación lumínica en el horizonte**
- **Color Harmony** con un **Gradient** desde el horizonte hacia arriba: **Warmth** un poco negativa para neutralizar el naranja; y **Dodge & Burn → Darken** suave sobre el resplandor.
- Si el resplandor es fuerte, **no intentes eliminarlo**: déjalo como un degradado cálido suave. Si lo quitas del todo, queda una banda gris sucia.

**6. Primer plano**
- Suele estar muy oscuro: **Dodge & Burn → Lighten** suave sobre el suelo ([sección 5.5](05-ajustes-locales.md)), o **Light Depth → Brightness Near**.
- **No lo aclares demasiado.** Una silueta oscura o un primer plano tenue es más creíble que uno iluminado como de día.
- **De noche, la máscara de cielo puede fallar** porque el límite entre cielo y suelo apenas se ve. Revísala con **`/`** y corrígela con **Brush**, o usa un **Gradient** en el horizonte.

**7. Acabado**
- **Details** muy bajo y **Details Masking** alto: el enfoque fuerte convierte el ruido en estrellas falsas.
- **Vignette** suave.
- Revisa al 100 %: bandas en el cielo, halos en el horizonte, estrellas convertidas en manchas.

**Estrellas alargadas (pequeños trazos):** salen cuando la exposición fue demasiado larga para la focal usada. No tienen arreglo real al editar. Para la próxima vez, consulta la sección 15.3.

## 9.3. Luces artificiales (lodge, campamento, ciudad)

- **Balance de blancos:** no neutralices del todo las bombillas cálidas. Algo de calidez hace la escena acogedora.
- **Highlights** −30/−50 para recuperar las luces. Si las bombillas están quemadas, déjalas: es normal.
- **Noiseless AI** casi siempre.
- **Magic Light AI** (opcional y muy suave) añade rayos y brillo a bombillas y farolas.
- **HSL:** baja la saturación del naranja si la luz es demasiado intensa.
- **Luces de distintos colores:** neutraliza la que más se vea y deja la otra con su color.

## 9.4. Fuego de campamento y linternas

- **Decide el color.** La luz del fuego es muy naranja. Corrige un poco (Temperature un poco más fría), pero **no la vuelvas blanca**: el fuego tiene que seguir pareciendo fuego.
- **Shadows** +20 para ver las caras; **Highlights** −40 para que la llama tenga forma.
- Si hay personas, **Mask AI → personas** con un Develop suave, o **Face AI → Face Light**.
- **Vignette** algo más marcada (−20) para concentrar la luz en el fuego.
- **No enfoques las llamas ni las chispas**: el enfoque convierte su movimiento en ruido.

## 9.5. Luna

- **Luna sola, con teleobjetivo:** baja **Highlights** y **Exposure** hasta ver los cráteres; **Structure AI** +20 y **Details** moderado. Fondo negro (**Blacks** abajo).
- **Luna en un paisaje:** en un JPEG suele estar quemada, porque es mucho más brillante que el paisaje. Si lo está, **no se puede recuperar**: acepta un punto blanco o hazle una foto aparte.
- **Añadir una luna de otra foto** (**Layers → + → My Images**) es un montaje: hazlo solo en fotos creativas y dilo al compartirla (sección 14).

## 9.6. Hora azul y crepúsculo

El mejor momento para la "foto nocturna" con JPEG suele ser **antes** de la noche cerrada, cuando el cielo aún tiene luz azul y el ruido es mucho menor.
- Balance de blancos: deja el azul.
- **Highlights** abajo en las luces artificiales; **Shadows** suaves.
- Ruido: a menudo basta con **Denoise** suave.
- **Twilight Enhancer AI** (preset **Blue**) puede reforzar el ambiente, con **Amount** bajo.

<!-- nav -->
[← Anterior](08-paisaje.md) · [Índice](README.md) · [Siguiente →](10-recetas.md)
<!-- /nav -->
