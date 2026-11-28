<!-- nav -->
[← Anterior](01-conceptos-basicos.md) · [Índice](README.md) · [Siguiente →](03-herramientas-una-a-una.md)
<!-- /nav -->

*Parte I · Fundamentos*

# 2. Luminar por dentro

> 🟢 **Iniciación** · Da por sabido: el [capítulo 1](01-conceptos-basicos.md) · Te desbloquea: moverte por Luminar sin perderte: catálogo, edición, pestañas y copias virtuales.

## 2.1. Catálogo y edición

- **Catálogo** (**`L`**): aquí ves, seleccionas y organizas. Añades carpetas (**`⌥⇧N`**), creas álbumes (**`⌘N`**) y marcas favoritas.
- **Edición:** aquí ajustas una foto. A la derecha hay cinco pestañas: **Presets** (**`T`**), **Tools** (**`E`**), **Edits** (las herramientas que ya has aplicado a la foto: desde aquí las revisas y las cambias), **Extra** (herramientas generativas, Upscale y fusiones) e **Info** (**`I`**, datos de la toma).

**Categorías de Tools:**

| Categoría | Herramientas | Para qué |
|---|---|---|
| **Essentials** | Develop, Enhance AI, Erase, Structure AI, Color, Black & White, Details, Denoise, Vignette | Lo básico de cualquier foto |
| **Landscape** | Sky AI, Sunrays, Twilight Enhancer AI, Atmosphere AI, Landscape, Water Enhancer AI | Cielo, neblina, agua, vegetación |
| **Creative** | Light Depth, Color Transfer, Magic Light AI, Dramatic, Mood (LUT), Toning, Matte, Neon & Glow, Mystical, Glow, Blur, Film Grain | Ambiente y estilo |
| **Portrait** | Studio Light, Bokeh AI, Face AI, Skin AI, Body AI, High Key | Personas |
| **Professional** | Supercontrast, Color Harmony, Dodge & Burn, Clone | Control fino de tono y color |
| **Image Quality** | Noiseless AI, Supersharp AI | Ruido y desenfoque |

**Pestaña Extra:** **HDR Merge**, **Panorama Stitching** y **Focus Stacking** (en *Merge Tools*), **Upscale** y **Restoration** (en *Enhancement*) y las herramientas generativas **GenErase**, **GenSwap** y **GenExpand** (sección 12).

> **Versiones y licencias.** Algunas herramientas tienen una versión *Improved*, que requiere Luminar for Desktop 1.29.0 o posterior y una licencia que la incluya; otras dependen de la suscripción. Si no encuentras una herramienta, consulta la documentación oficial (sección 20).

## 2.2. Edición no destructiva y copias virtuales

- Luminar **no modifica tus JPEG**: guarda los ajustes en su catálogo. Puedes volver a una foto meses después y cambiar cualquier ajuste.
- **Copia virtual** (**`⌘'`**): crea otra versión de la misma foto sin duplicar el archivo. Úsala para probar el blanco y negro, otro recorte (horizontal y vertical) o una edición más atrevida.
- **Compare** (**`;`**): compara versiones (Skylum solo documenta el nombre del atajo; mira en tu versión cómo las muestra).
- **`\`** (mantener pulsado): muestra el original mientras lo mantienes.
- **Revert to Original** (**`⇧⌘R`**): descarta todos los ajustes.
- **Copia de seguridad:** las ediciones viven en el catálogo de Luminar. Haz copia del catálogo además de tus fotos.

## 2.3. Las máscaras en Luminar

En Luminar, la mayoría de las herramientas tienen su propia pestaña **Masking**. Abres una herramienta (por ejemplo, Develop), ajustas y, en su pestaña **Masking**, decides dónde se aplica.

**Tipos de máscara:**

| Máscara | Atajo | Cómo funciona |
|---|---|---|
| **Mask AI** | **`A`** | Selecciona por categorías: personas, cielo, edificios, vehículos, agua, plantas, montañas, suelo natural y suelo artificial. Se pueden combinar varias |
| **Object Select AI** | — | Al pasar el ratón por encima, resalta el objeto que reconoce; haz clic para seleccionarlo. Haz clic en otras zonas para añadirlas y usa **Subtract** para quitar zonas |
| **Brush** | **`B`** | Pintas a mano. **`[`** y **`]`** cambian el tamaño; **`⇧[`** y **`⇧]`**, la dureza |
| **Radial** | **`R`** | Elipse: para el centro de interés o la Vía Láctea |
| **Gradient** | **`G`** | Degradado lineal: para cielo y suelo |
| **Luminosity** | — | Un deslizador elige un rango de brillo (de sombras a luces) |
| **Color** | — | Haces clic en un color de la foto; un deslizador de rango decide cuánto se parecen los tonos incluidos |

**Ajustes y acciones de la máscara:**
- **Feather:** suaviza el borde. **Shift Edge:** expande o contrae el borde.
- **Fill** (cubrir toda la foto), **Clear** (borrar la máscara), **Invert** (**`⌘I`**) y **Show** (**`/`**, muestra la máscara en rojo).
- **Copy** y **Paste:** copian una máscara de una herramienta a otra. Así aplicas Develop y Structure AI exactamente a la misma zona.

**Revisa siempre los bordes con `/`.** Las máscaras IA suelen fallar en cuernos, orejas, bigotes y ramas finas: corrígelas con **Brush**.

**Una máscara por herramienta.** La máscara limita el efecto de **esa** herramienta a una zona. Por eso **Develop** se usa sin máscara, para toda la foto, y las zonas se trabajan con **Dodge & Burn** (pintando luz y sombra) y con **otras herramientas, cada una con su máscara**. Todo el método, paso a paso, en la [sección 5](05-ajustes-locales.md). La documentación de Skylum dice que **se puede añadir la misma herramienta más de una vez** (lo menciona al hablar de la pestaña **Edits** y de las capas), pero no explica los pasos: compruébalo en tu versión ([PENDIENTES](../PENDIENTES.md)).

## 2.4. Capas

- **Añadir una capa:** el icono **+** del panel **Layers** abre *Add New Layer*, con estas opciones: **My Images** (otra foto tuya), **Flares**, **Light Leaks**, **Stardust Bokeh** y **Sparklers**.
- **Propiedades de la capa:** **Opacity**, **Blend Modes**, **Horizontal Flip**, **Vertical Flip** e **Image Mapping**. Cada capa tiene su pestaña **Masking** (Brush, Linear Gradient, Radial Gradient, Mask AI).
- **Background Removal AI:** separa el sujeto del fondo dentro de una capa.
- **Quitar u ocultar:** clic secundario (**`⌃`**-clic, o clic con dos dedos en el trackpad) → **Remove Layer** o **Hide Layer**.

Para la edición normal de un JPEG de viaje bastan las **herramientas con máscara**. Las capas sirven sobre todo para combinar imágenes, un uso que en fotos documentales conviene evitar (sección 14).

## Ejercicio (15 minutos)

1. Añade una carpeta al catálogo (**`⌥⇧N`**) y marca 5 fotos con **`P`** y 5 con **`X`**.
2. Crea una **copia virtual** (**`⌘'`**) de una foto y conviértela a blanco y negro; compara las dos con **`;`**.
3. En cualquier herramienta, abre la pestaña **Masking**, prueba **Mask AI** (**`A`**) y mira la máscara con **`/`**.

**Aprobado cuando** sabes ir del catálogo a la edición y volver, y encontrar la pestaña Masking de una herramienta sin buscar.

<!-- nav -->
[← Anterior](01-conceptos-basicos.md) · [Índice](README.md) · [Siguiente →](03-herramientas-una-a-una.md)
<!-- /nav -->
