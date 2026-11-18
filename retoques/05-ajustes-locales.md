<!-- nav -->
[← Anterior](04-flujo-base.md) · [Índice](README.md) · [Siguiente →](06-herramientas-avanzadas.md)
<!-- /nav -->

*Parte II · El método*

# 5. Ajustes locales: aclarar u oscurecer solo una parte

Hasta ahora, cada ajuste cambiaba **toda** la foto. Este capítulo enseña a cambiar **solo una zona**: aclarar los ojos de un animal, abrir una sombra bajo su cabeza u oscurecer un cielo que distrae. Está pensado para quien empieza de cero. Cada caso explica **qué** quieres conseguir, **cómo** se hace en Luminar clic a clic y **qué significa técnicamente** para la foto.

> **Antes de empezar:** haz primero el flujo base completo ([sección 4](04-flujo-base.md)). Los ajustes locales son el **último retoque** sobre una foto que ya está bien en conjunto. Si la foto entera está oscura, se arregla con **Develop**, no zona a zona.

## 5.1. Qué es un ajuste local (y qué le pasa a la foto)

**La idea.** Una foto son millones de píxeles, y cada uno tiene un brillo y un color. Un ajuste global cambia todos los píxeles por igual. Un ajuste local cambia solo los píxeles de una zona y deja el resto como estaba.

**La máscara.** Para decirle a Luminar qué zona cambiar se usa una **máscara**: un "mapa" del tamaño de la foto que indica, píxel a píxel, cuánto efecto recibe cada uno.
- Donde la máscara está **llena**, el ajuste se aplica entero.
- Donde está **vacía**, no se aplica nada.
- En el **borde** de la máscara hay una zona de transición en la que el efecto va de entero a nada. Ese borde suave es lo que hace que el retoque no se note.

Luminar enseña la máscara como una **capa roja translúcida** sobre la foto: rojo = zona afectada. Se activa y desactiva con **`/`** (o en las acciones de la máscara, **Show**).

**Qué significa técnicamente aclarar u oscurecer una zona:**
- **Aclarar** sube el brillo de esos píxeles; **oscurecer** lo baja. Las texturas y los colores siguen ahí; solo cambia su luminosidad.
- **En un JPEG el margen es pequeño** ([sección 1.1](01-conceptos-basicos.md)): si aclaras mucho una sombra, aparece el **ruido** que estaba escondido en lo oscuro, y en zonas lisas (cielo, piel) pueden aparecer **bandas**. Lo que está completamente negro o completamente blanco **no tiene detalle que rescatar**: solo se vuelve gris.
- **Por qué funciona para la mirada:** el ojo del espectador va primero a lo más claro y contrastado ([sección 1.7](01-conceptos-basicos.md)). Aclarar un poco el sujeto y oscurecer un poco el fondo **dirige la mirada** sin que nadie note que has tocado nada.

**La regla de oro:** cambios **pequeños**. Si al comparar con el original (**`\`**) el retoque "salta a la vista", es demasiado.

## 5.2. Cómo funcionan las máscaras en Luminar

En Luminar no hay un panel de ajustes locales aparte: **cada herramienta tiene su propia pestaña Masking**. El camino es siempre el mismo:

1. Abre una herramienta en el panel **Edit** y **haz el ajuste** (por ejemplo, sube un control).
2. Abre la pestaña **Masking** de esa herramienta.
3. Elige el tipo de máscara y marca la zona.
4. El ajuste de esa herramienta queda **solo** en la zona marcada.

**Una máscara por herramienta.** Esto es lo importante para empezar: si usas **Develop** para corregir la foto entera y luego le pones una máscara, la corrección pasa a afectar **solo** a la zona de la máscara. Por eso el método de esta guía es:
- **Develop, sin máscara**, para la luz y el color de toda la foto ([sección 4](04-flujo-base.md)).
- **Dodge & Burn** para aclarar u oscurecer zonas **pintando** (5.4 a 5.6). No necesita máscara: el pincel es la máscara.
- **Otras herramientas, cada una con su máscara**, para lo demás: textura del sujeto, color del fondo, etc. (5.7).

> **¿Se puede añadir Develop dos veces, cada una con su máscara?** La documentación de Skylum dice, al hablar de capas, que las herramientas se pueden aplicar "varias veces y con máscaras distintas", pero **no explica cómo** hacerlo con la misma herramienta en una foto. Compruébalo en tu versión ([PENDIENTES](../PENDIENTES.md)). Si se puede, es la forma más precisa de aclarar u oscurecer una zona seleccionada con Mask AI u Object Select AI. Si no, usa los métodos de este capítulo.

**Los tipos de máscara:**

| Máscara | Atajo | Cómo se marca | Para qué |
|---|---|---|---|
| **Brush** | **`B`** | Pintas. Modo **Paint** añade y modo **Erase** quita. Controles **Size**, **Softness** y **Strength**. **`[`**/**`]`** cambian el tamaño | Zonas con forma irregular |
| **Radial** | **`R`** | Arrastras un círculo. El círculo interior marca el tamaño; el exterior, lo suave del borde. **Standard** protege el centro; **Inverted** aplica el efecto dentro | Una zona redonda: una cara, el núcleo de la Vía Láctea |
| **Linear Gradient** | **`G`** | Arrastras un degradado: líneas superior e inferior para la transición, punto central para moverlo y rotarlo | Cielo o suelo con horizonte recto |
| **Mask AI** | **`A`** | Eliges categorías: personas, cielo, edificios, vehículos, agua, plantas, montañas, suelo natural, suelo artificial | Cielo, agua, vegetación… en un clic |
| **Object Select AI** | — | Pasas el ratón y resalta un objeto; clic para seleccionarlo; **Subtract** para quitar zonas | Un animal, una persona |
| **Luminosity** | — | Un deslizador elige un rango de brillo (de sombras a luces), con **Feathering** | "Solo las sombras" o "solo las luces" |
| **Color** | — | Haces clic en un color; un deslizador **Range** decide cuántos tonos parecidos entran | "Solo los verdes", "solo el naranja del vehículo" |

**Acciones de la máscara:** **Feather** (suaviza el borde) · **Shift Edge** (amplía o encoge el borde) · **Invert** (**`⌘I`**, invierte: el sujeto pasa a ser "todo menos el sujeto") · **Copy** y **Paste** (copian la máscara a otra herramienta) · **Fill** y **Clear** (cubrir toda la foto o borrar la máscara) · **Show** (**`/`**).

## 5.3. Qué herramienta para cada cosa

| Quieres… | Herramienta | Cómo |
|---|---|---|
| Aclarar los ojos | **Dodge & Burn → Lighten** | Pincel pequeño sobre el iris (5.4) |
| Abrir una sombra (bajo la cabeza, una ladera) | **Dodge & Burn → Lighten** | Pincel grande y muy suave (5.5) |
| Oscurecer un cielo, un borde o un fondo que distrae | **Dodge & Burn → Darken** | Pincel grande y suave (5.6) |
| Más textura solo en el animal | **Structure AI** + máscara **Object Select AI** | 5.7 |
| Menos color en el fondo | **Color** (Saturation) + la misma máscara, **invertida** | 5.7 |
| Que el sujeto destaque con luz | **Vignette** con **Choose Subject** | 5.7 |
| Primer plano más claro y fondo más frío, o al revés | **Light Depth** (Brightness Near/Far, Warmth Near/Far) | [sección 6.5](06-herramientas-avanzadas.md) |
| Más contraste solo en el cielo o solo en el suelo | **Supercontrast** + **Mask AI** o **Linear Gradient** | [sección 6.2](06-herramientas-avanzadas.md) |

## 5.4. Paso a paso: aclarar los ojos de un animal

**Qué:** que el ojo tenga un poco más de luz que la cara que lo rodea, para que la mirada del espectador vaya ahí.

**Cómo:**
1. Amplía la foto sobre el ojo (**`⌘1`** para el 100 %; con la **barra espaciadora** + arrastrar te mueves por la foto).
2. Abre **Dodge & Burn** (herramientas **Professional** del panel Edit).
3. Elige **Lighten**.
4. **Brush Size:** algo **más pequeño que el iris**. Cámbialo con **`[`** y **`]`**.
5. **Softness:** alta, para que el borde no se note (**`⇧[`**/**`⇧]`**).
6. **Strength:** **baja**. Mejor varias pasadas suaves que una fuerte.
7. Pinta **solo el iris**, sin tocar el blanco del ojo ni el párpado.
8. Si te pasas, cambia a **Erase** y pinta encima para quitarlo.
9. Ajusta el total con **Overall Amount** y sal de la herramienta para aplicar.
10. Comprueba con **`\`** (mantener): el ojo debe verse "vivo", no "encendido".

**Qué significa técnicamente:** subes el brillo de unas decenas de píxeles. El ojo gana **contraste local** con su entorno, y por eso atrae la mirada. Cada pasada **suma**: tres pasadas suaves equivalen a una más fuerte, pero con más control.

**Cuidado:**
- **No pintes un brillo** donde no lo hay: en fotografía de naturaleza se considera manipulación ([sección 14](14-etica.md)).
- En un ojo muy oscuro, aclarar mucho saca **ruido** (granito de colores). Si aparece, para.

## 5.5. Paso a paso: abrir una zona de sombra

**Qué:** recuperar algo de detalle en una sombra concreta (la tripa y el cuello de un animal con luz de mediodía, una ladera en sombra) sin aclarar el resto de la foto.

**Cómo:**
1. Comprueba primero si basta con **Shadows** en Develop (afecta a todas las sombras de la foto). Si solo una zona necesita luz, sigue.
2. **Dodge & Burn → Lighten**.
3. **Brush Size:** **grande**, más que la zona. **Softness:** al máximo. **Strength:** muy baja.
4. Pinta la sombra con pasadas largas. Ve mirando la foto a tamaño completo (**`⌘0`**), no ampliada: estás cambiando cómo se ve la zona dentro del conjunto.
5. Para cuando la sombra deje ver forma y textura **pero siga siendo una sombra**.
6. Comprueba al 100 % (**`⌘1`**) que no ha aparecido ruido ni bandas.

**Qué significa técnicamente:** subes la luminosidad de los píxeles oscuros de esa zona. En un JPEG, las sombras guardan **pocos niveles de brillo** y algo de **ruido**, y al aclararlas ambos se notan. Por eso el límite no lo pones tú, lo pone el archivo: cuando aparece el granito o la sombra se vuelve gris y plana, has llegado al final.

**Cuidado:** una sombra aclarada de más deja la foto **plana**: sin sombras no hay volumen. La luz dura de mediodía se nota y está bien que se note.

## 5.6. Paso a paso: oscurecer un cielo o un fondo que distrae

**Qué:** que una zona clara que no es el sujeto (un cielo blanquecino, una rama iluminada, un borde brillante) pese menos en la foto.

**Cómo:**
1. **Dodge & Burn → Darken**.
2. **Brush Size:** grande. **Softness:** alta. **Strength:** baja.
3. Pinta la zona que distrae. Cerca del sujeto (el horizonte, el contorno del animal), reduce el pincel y ve con calma.
4. Si oscureces el sujeto sin querer, **Erase** sobre él.
5. Compara con **`\`**: el fondo debe "retirarse", no ennegrecerse.

**Alternativas:**
- **Bordes claros de la foto:** **Vignette** con **Amount** negativo oscurece los bordes de forma uniforme ([sección 4](04-flujo-base.md), paso 10).
- **Un cielo entero, con precisión en el horizonte:** si tu versión permite añadir **Develop** otra vez (5.2), usa Develop + **Mask AI → cielo** + **Exposure** negativa.

**Qué significa técnicamente:** bajas el brillo de esos píxeles. El sujeto no cambia, pero **en comparación** parece más claro. Es contraste entre zonas: el ojo mide la luz de forma relativa.

**Cuidado:** si el cielo ya está **quemado** (blanco puro), oscurecerlo lo vuelve **gris**, no azul: no hay color que recuperar.

## 5.7. Paso a paso: el sujeto más presente, el fondo más discreto

**Qué:** el clásico de la fotografía de fauna. El animal, con un poco más de textura; el fondo, con un poco menos de color.

**Cómo:**
1. **Structure AI**: sube **Amount** con moderación.
2. En su pestaña **Masking**, **Object Select AI**: pasa el ratón sobre el animal y haz clic cuando lo resalte. Si se ha comido algo del fondo, **Subtract** y clic en esa zona.
3. Pulsa **`/`** y revisa los bordes: orejas, cuernos, bigotes. Corrige con **Feather** o con **Brush** (modo Paint para añadir, Erase para quitar).
4. En las acciones de la máscara, **Copy**.
5. Abre la herramienta **Color**. Baja un poco **Saturation**.
6. En su **Masking**, **Paste** (la misma máscara del animal) y luego **Invert** (**`⌘I`**): ahora la máscara es "todo menos el animal".
7. Opcional: **Vignette** con **Choose Subject** sobre el animal, para que la luz caiga hacia él.

**Qué significa técnicamente:** **Structure AI** aumenta el **contraste local** (la diferencia entre píxeles vecinos), que es lo que el ojo percibe como textura y nitidez. **Saturation** baja la intensidad del color de los píxeles del fondo, que deja de competir con el sujeto. La máscara compartida (Copy/Paste) garantiza que las dos cosas usan **exactamente el mismo borde**.

## 5.8. Comprobar y corregir

| Lo que ves | Qué es | Cómo se arregla |
|---|---|---|
| Una línea o un "aura" alrededor del sujeto | **Halo**: el borde de la máscara es demasiado duro o no coincide con el sujeto | **Feather** más alto o **Shift Edge**; revisa con **`/`** |
| Granito de colores en una zona aclarada | **Ruido** que estaba escondido en la sombra | Menos **Strength** o **Overall Amount**; si hace falta, más **Color Denoise** en Noiseless AI ([sección 4](04-flujo-base.md)) |
| Escalones en un cielo oscurecido | **Bandas**: un JPEG tiene pocos tonos en zonas lisas | Retoque más suave; **Film Grain** bajo para disimularlas |
| Manchas claras u oscuras con la forma del pincel | Pinceladas con **Softness** baja o **Strength** alta | **Erase**, y repite con más Softness y menos Strength |
| La foto parece "retocada" | Demasiada diferencia entre zonas | Baja **Overall Amount**; compara con **`\`** |

## 5.9. Ejercicio (una tarde)

1. Elige una foto de un animal con el ojo visible y una zona de sombra.
2. Haz el flujo base completo ([sección 4](04-flujo-base.md)).
3. Haz una **copia virtual** (**`⌘'`**) para poder comparar.
4. En la copia: aclara el ojo (5.4), abre la sombra (5.5) y oscurece lo que distraiga (5.6).
5. Ponlas lado a lado con **Compare** (**`;`**).
6. Pregúntale a alguien cuál prefiere **sin decirle qué has hecho**.

**Aprobado cuando:** prefiere la retocada y no sabe decir qué has cambiado.

## Fuentes de este capítulo

- [Dodge & Burn](https://support.skylum.com/editing-tools/professional-tools/dodge-and-burn) · [Masking Options](https://support.skylum.com/editing-tools/masking-options) · [Brush Mask](https://support.skylum.com/editing-tools/masking-options/brush-mask) · [Radial Mask](https://support.skylum.com/editing-tools/masking-options/using-a-radial-mask) · [Linear Gradient Mask](https://support.skylum.com/editing-tools/masking-options/linear-gradient-mask) · [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions) · [Layers](https://support.skylum.com/editing-tools/layers)

<!-- nav -->
[← Anterior](04-flujo-base.md) · [Índice](README.md) · [Siguiente →](06-herramientas-avanzadas.md)
<!-- /nav -->
