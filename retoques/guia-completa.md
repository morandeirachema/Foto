<!-- Archivo generado por pdf/generar-guia.sh a partir de retoques/. No lo edites a mano. -->

# Mejorar JPEG de safari, paisaje y fotografía nocturna con Luminar
### Guía paso a paso, de lo básico a lo avanzado

**Versión de la guía:** noviembre de 2026 · Luminar for Desktop 1.29.x (Luminar Neo) · macOS

## Cómo está organizada

**Parte I · Fundamentos**
1. Conceptos básicos
2. Luminar por dentro
3. Las herramientas, una a una: dónde están, qué hacen y cuánto mover

**Parte II · El método**

4. El flujo base: 10 pasos
5. Ajustes locales: aclarar u oscurecer solo una parte
6. Herramientas avanzadas

**Parte III · Por tipo de foto**

7. Safari (fauna)
8. Paisaje y ciudad
9. Fotografía nocturna

**Parte IV · Más allá de una foto**

10. Recetas completas *(provisional)*
11. Trabajar en serie
12. Varias fotos en una, ampliar y generar
13. Exportar
14. Ética, concursos y ubicación
15. Disparar mejores JPEG la próxima vez

**Parte V · Referencia**

16. Errores típicos y lista de comprobación
17. Atajos de teclado
18. Glosario
19. Preguntas frecuentes
20. Fuentes

## Cómo leerla

- **Pensada para JPEG, y es justo lo que tienes:** las fotos de Namibia salieron solo en JPEG por un error de configuración de la cámara. Todo lo de esta guía se aplica tal cual a ellas. Para que no se repita, mira la [configuración básica de la a6700](../manejo-a6700/04-configuracion-basica.md).

- Cada paso indica **qué hacer** en Luminar y **por qué**. Si entiendes el porqué, sabrás adaptarlo a cada foto.
- Cuando el texto dice "sección 5.3", se refiere al apartado 5.3, dentro del capítulo 5.
- **¿Empiezas de cero en edición?** Lee en orden los capítulos 1 a 5. El 3 es la ficha de cada herramienta, con los números de partida: tenlo abierto mientras editas. El 5 enseña a aclarar u oscurecer solo una parte de la foto (los ojos, una sombra, el cielo), explicando qué haces, cómo y qué significa para la foto.
- Los **nombres de herramientas, controles y atajos** están comprobados con la documentación oficial de Skylum (sección 20). Se mantienen en inglés, como aparecen en el programa.
- Los **valores numéricos** son puntos de partida para JPEG propuestos por esta guía, no valores oficiales. Cada foto es distinta: mueve el deslizador mirando la imagen, no el número.
- Los atajos son de **macOS**: **`⌘`** es Comando, **`⌥`** Opción, **`⇧`** Mayúsculas y **`⌃`** Control. Si tu teclado es español, mira cómo se escriben **`\`**, **`/`**, **`;`**, **`[`** y **`]`** en la [sección 17](17-atajos.md#si-tu-teclado-es-español).

---

*Parte I · Fundamentos*

# 1. Conceptos básicos

> 🟢 **Iniciación** · Da por sabido: nada · Te desbloquea: entender qué le pasa a un JPEG cuando lo editas: histograma, balance, contraste, ruido, máscaras y color.

Antes de mover un deslizador, conviene entender **qué estás tocando**. Este capítulo resume lo imprescindible para retocar; la explicación completa, con la cámara, está en [Conceptos](../conceptos/README.md): [la luz](../conceptos/01-la-luz.md), [el histograma](../conceptos/03-histograma.md), [el balance de blancos](../conceptos/04-balance-de-blancos.md) y [por qué funciona](../conceptos/09-por-que-funciona.md). Si entiendes estos conceptos, sabrás qué herramienta de Luminar usar en cada caso.

## 1.1. Qué tiene de especial un JPEG

Un JPEG es una foto **ya revelada por la cámara**. La cámara ha decidido el balance de blancos, el contraste, la saturación, el enfoque y la reducción de ruido, y después ha **comprimido** el resultado guardando solo 256 niveles por color.

**Consecuencias prácticas:**
- **Lo que está completamente blanco (quemado) o completamente negro no se puede recuperar.** No hay información que rescatar.
- **Los ajustes fuertes rompen la imagen:** aparecen **bandas** en cielos y degradados, **halos** en los bordes, **ruido** en las sombras y colores artificiales.
- **Regla de oro:** mejor muchos ajustes pequeños que pocos grandes. Si un deslizador necesita ir muy lejos, probablemente hay otra forma mejor (una máscara, otra herramienta).

### JPEG frente a RAW

| | JPEG | RAW |
|---|---|---|
| Niveles por color | 256 (8 bits) | 4.096–16.384 (12–14 bits) |
| Margen para recuperar luces | Casi nulo | Bastante más |
| Margen para aclarar sombras | Poco, con ruido y bandas | Bastante |
| Balance de blancos | Ya aplicado: corregirlo mucho degrada el color | Se elige al editar |
| Ruido | Ya reducido por la cámara (a veces se lleva detalle) | Intacto: tú decides cómo reducirlo |

**Conclusión:** con JPEG editas **dentro de un margen estrecho**. Esta guía está pensada para sacar lo mejor de ese margen sin romperlo.

### Por qué aparecen las bandas

Un cielo azul que pasa de claro a oscuro puede tener muy pocos tonos distintos en un JPEG. Si estiras ese degradado (más contraste, azul más oscuro, Dehaze), esos tonos se reparten en un espacio mayor y se ven los **escalones**. Además, la compresión JPEG trabaja en bloques de 8 × 8 píxeles: en zonas lisas, al forzar el contraste, pueden aparecer cuadraditos.

**Cómo evitarlas:** ajustes moderados en el cielo, máscaras para que el cielo no reciba contraste local y un poco de **Film Grain** al final, que disimula los escalones.

### Comprimir una sola vez

Cada vez que se **guarda** un JPEG, se vuelve a comprimir y pierde un poco. Luminar trabaja de forma **no destructiva**: los ajustes se guardan aparte y el JPEG original no se toca. Solo comprimes una vez: **al exportar**. Por eso:
- No exportes un JPEG para volver a abrirlo, seguir editando y exportarlo otra vez. Edita siempre sobre el original.
- Si necesitas un archivo intermedio, exporta en **TIFF** (sin pérdida).

## 1.2. Las cinco zonas de brillo

Toda foto se puede dividir por brillo. En **Develop**, Luminar tiene un control para cada zona:

| Zona | Qué es | Control en Develop |
|---|---|---|
| **Negros** | El punto más oscuro | Blacks |
| **Sombras** | Zonas oscuras con detalle | Shadows |
| **Medios tonos** | La mayor parte de la foto | Exposure |
| **Luces** | Zonas claras con detalle | Highlights |
| **Blancos** | El punto más claro | Whites |

**Por qué importa:** cuando una foto "está mal", casi siempre es porque una zona está demasiado clara u oscura respecto a las demás. En vez de subir o bajar toda la foto, tocas **solo la zona que falla**.

**Cada zona en la escena real:**

| Zona | En safari | En paisaje | De noche |
|---|---|---|---|
| Negros | Sombras profundas bajo un árbol | Grietas, siluetas | El cielo entre estrellas |
| Sombras | Tripa y cuello del animal | Laderas en sombra | Primer plano |
| Medios | El cuerpo del animal | Hierba, roca | Casi no hay |
| Luces | Cielo, arena | Nubes iluminadas | Vía Láctea, estrellas brillantes |
| Blancos | Brillo en el ojo | Nieve, sol | Farolas, luna, fuego |

## 1.3. El histograma y el aviso de recorte

- El **histograma** es una gráfica del brillo: **izquierda oscuro, derecha claro**.
- Si la "montaña" toca el borde derecho, hay **luces quemadas**; si toca el izquierdo, **negros empastados**.
- El **aviso de recorte** pinta en la foto las zonas quemadas o empastadas. En Luminar se activa y desactiva con **`J`**.
- **Dónde está en Luminar:** menú **View > Show Histogram**. Un **clic sobre el histograma** alterna entre la vista conjunta y los canales **rojo, verde y azul** por separado. Los **dos triángulos** de las esquinas superiores activan los avisos: el izquierdo pinta en azul los negros puros y el derecho, en rojo, los blancos puros.
- **Mira los canales por separado cuando domina un color** (dunas rojas, un atardecer, un animal bajo un foco naranja). Si el canal rojo ya toca el borde derecho, no añadas calidez ni saturación: ese color no tiene más margen.
- **No hay un histograma correcto:** una foto nocturna tiene que estar a la izquierda y una de arena blanca, a la derecha.

**El recorte permitido.** No todo recorte es un error. Puedes dejar quemados el **sol**, las **farolas**, los **reflejos del sol** en el agua o en un ojo y una **luna pequeña** en un paisaje. Lo que no debe quemarse es lo que tiene textura y el espectador mira: nubes, plumas blancas, nieve, la piel del sujeto.

## 1.4. Balance de blancos: temperatura y matiz

- **Temperature:** azul ↔ amarillo. Corrige una luz demasiado fría o cálida.
- **Tint:** verde ↔ magenta. Corrige dominantes raras.
- **Cuentagotas** (**`W`**, con Develop → Color abierto): haces clic en algo que debería ser **gris o blanco neutro** y Luminar corrige el resto.
- **Importante:** no se trata de dejar todo "neutro", sino de que el color sea **creíble**. Un atardecer tiene que ser cálido; una noche, ligeramente fría.

**Dónde hacer clic con el cuentagotas (y dónde no):**

| Buen punto neutro | Mal punto neutro |
|---|---|
| Nubes grises en sombra | Nubes al atardecer (son naranjas de verdad) |
| Roca gris, asfalto | Arena (casi siempre es cálida) |
| Plumas blancas en sombra | Plumas blancas al sol del atardecer |
| La carrocería blanca o gris de un vehículo | La piel o el pelaje de un animal |
| Nieve en sombra | Hierba seca |

**En JPEG, corrige poco.** La cámara ya ha aplicado un balance de blancos a los colores. Mover mucho la temperatura suele dar colores sucios. Si la dominante es fuerte, corrige un poco con Temperature y termina con **HSL** (sección 4, paso 7) o con **Color Harmony → Color Balance** (sección 6.3).

**Una foto con dos luces distintas** (sol y sombra, fuego y luna) **nunca** quedará neutra en todas partes. Decide qué zona debe ser neutra y corrige las demás con máscaras.

## 1.5. Contraste global y contraste local

- **Contraste global:** separa más las zonas claras de las oscuras en toda la foto (**Smart Contrast**, curva en S).
- **Contraste local** (**Structure AI**, **Details**): aumenta el contraste **dentro de cada zona pequeña**. Hace que se vean las texturas: el pelo de un animal, la corteza de un árbol, las ondas de una duna.
- **El exceso de contraste local** es el error más típico de la edición moderna: halos, aspecto "HDR" y fotos sucias.

**Las tres escalas del contraste en Luminar.** La herramienta **Details** las separa:

| Escala | Qué resalta | Deslizador |
|---|---|---|
| **Pequeña** | Pelo, plumas, granos de arena | Small Details |
| **Media** | Arrugas de la piel del elefante, corteza, ondas de duna | Medium Details |
| **Grande** | Contornos de los objetos, volumen | Large Details |

El **halo** aparece cuando el contraste local es demasiado fuerte: alrededor de un animal oscuro sobre un cielo claro sale una "aura" clara. Si lo ves, baja **Large Details** o **Structure AI**, o protege el cielo con una máscara.

## 1.6. Ruido y nitidez: siempre van juntos

- **Ruido:** el granito que aparece con ISO alto o al aclarar sombras.
- **Nitidez:** refuerza los bordes.
- **El conflicto:** enfocar refuerza también el ruido, y quitar ruido ablanda los detalles. Por eso el orden lógico es **primero quitar ruido, después enfocar**, y **siempre revisando al 100 %** (**`⌘1`**).

**Dos tipos de ruido**, con su deslizador propio en **Noiseless AI**, **Denoise** y **Develop**:
- **Ruido de luminosidad** (**Luminosity Denoise**): granito gris, como arena. Es el más visible en el cielo y en las sombras.
- **Ruido de color** (**Color Denoise**): manchitas de colores en las sombras.

**Regla práctica:** quita casi todo el ruido de color y solo parte del de luminosidad. Un grano fino y gris parece fotográfico; una foto sin ningún grano parece de plástico.

**Dos usos de la nitidez que se confunden:**
1. **Nitidez general:** un JPEG ya viene enfocado por la cámara, a menudo de más. Por eso en JPEG conviene enfocar poco.
2. **Nitidez dirigida:** resaltar lo que importa (el ojo, la textura), mejor con una máscara solo en el sujeto.

## 1.7. Ajustes globales y locales

- **Globales:** afectan a toda la foto. Sirven para corregir.
- **Locales (máscaras):** afectan a una zona. Sirven para **dirigir la mirada**: el sujeto un poco más claro y nítido, el fondo un poco más apagado.

**Hacia dónde va la mirada.** El ojo del espectador tiende a ir a lo que es:
1. **Más claro** que su entorno.
2. **Más contrastado.**
3. **Más nítido.**
4. **Más saturado**, o de un color distinto al resto.
5. Una **cara** o un **ojo**, sobre todo si mira a cámara.

Editar en local consiste en que el sujeto gane un poco en esas cosas y el fondo **pierda un poco**. Las diferencias deben ser pequeñas: si se notan, la foto parece retocada.

## 1.8. El orden de trabajo

1. **Calidad:** ruido y desenfoque.
2. **Geometría:** recorte, horizonte, perspectiva.
3. **Luz global:** exposición y zonas de brillo.
4. **Color global:** balance de blancos y saturación.
5. **Textura:** contraste local y nitidez.
6. **Ajustes locales:** sujeto, cielo, fondo.
7. **Retoque:** manchas y distracciones.
8. **Acabado:** viñeteado, grano.
9. **Revisión** al 100 % y tras un descanso.
10. **Exportación.**

**Por qué este orden:**
- El ruido se quita **primero** porque aclarar y contrastar lo amplifican.
- El recorte va **antes** que la luz porque, si quitas una zona muy clara o muy oscura del borde, la luz que necesitas cambia.
- La luz va **antes** que el color porque el brillo cambia cómo percibimos la saturación.
- Los ajustes locales van **después** de los globales: son retoques sobre una base equilibrada. Si luego cambias lo global, tendrás que rehacer lo local.

## 1.9. Tu pantalla y tu entorno

- **Brillo moderado.** Con el brillo al máximo, tus fotos saldrán **oscuras** en otras pantallas y en papel.
- **Desactiva** el brillo automático, **True Tone** y **Night Shift** mientras editas (en macOS, en Ajustes del Sistema → Pantallas). Cambian el color de la pantalla según la hora y la luz ambiente.
- **Luz ambiente tenue y constante.** No edites con el sol dando en la pantalla.
- **Un calibrador de pantalla** es muy recomendable si imprimes o vendes fotos. Un aviso: un artículo de soporte de Skylum (marcado como posiblemente desactualizado y pensado para Windows) dice que Luminar muestra las fotos en sRGB y **no lee el perfil personalizado del monitor**. Si calibras, compara la foto exportada en Vista Previa antes de fiarte del color para imprimir ([PENDIENTES](../PENDIENTES.md)).
- **Comprueba en el móvil.** Mucha gente verá tus fotos en un teléfono.

## 1.10. Color: lo mínimo de teoría

- **Tono (Hue):** qué color es.
- **Saturación (Saturation):** cuánto color tiene, de gris a intenso.
- **Luminancia (Luminance):** cómo de claro u oscuro es ese color.

**Colores complementarios:** **naranja ↔ azul**, **amarillo ↔ violeta**, **rojo ↔ cian**, **verde ↔ magenta**.
- **Contraste complementario:** un animal cálido (león, impala) sobre un fondo frío (cielo, sombra azulada) destaca de forma natural.
- **Corregir una dominante es empujar hacia su complementario:** un cielo nocturno naranja se corrige hacia el azul; unas sombras verdosas, hacia el magenta.

**Pocos colores, más armonía.** En safari, la paleta natural es de **ocres, dorados y verdes apagados**. Si un color se sale (un vehículo rojo, una camiseta fosforito), desaturarlo con una máscara limpia la foto sin borrar nada.

## Ejercicio (15 minutos)

1. Abre una foto tuya en Luminar y pulsa **`J`**: ¿qué zonas salen marcadas como quemadas o empastadas?
2. Busca en la foto las **cinco zonas de brillo** (1.2): señala un negro, una sombra, un medio tono, una luz y un blanco.
3. Mantén **`\`** sobre una foto ya editada por otra persona (o una tuya antigua) y di qué crees que se tocó.

**Aprobado cuando** sabes explicar, sin mirar, por qué un JPEG aguanta menos que un RAW.

---

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

---

*Parte I · Fundamentos*

# 3. Las herramientas, una a una: dónde están, qué hacen y cuánto mover

> 🟢 **Iniciación** → 🔵 · Da por sabido: el [capítulo 2](02-luminar-por-dentro.md) · Te desbloquea: saber dónde está cada herramienta, qué hace y con qué número empezar.

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

---

*Parte II · El método*

# 4. El flujo base: 10 pasos

> 🔵 **Básico** · Da por sabido: los capítulos [1](01-conceptos-basicos.md) a [3](03-herramientas-una-a-una.md) · Te desbloquea: editar cualquier foto en diez pasos, elegir la ruta según lo que hay en ella y rescatar un JPEG difícil.

Este es el esqueleto que usarás en todas las fotos. Las secciones de safari, paisaje y noche explican **qué cambia** en cada caso.

> **Valores orientativos.** Los números de esta guía son puntos de partida para JPEG, no valores oficiales de Skylum. Cada foto es distinta: mueve el deslizador mirando la imagen, no el número.

### Paso 1 · Preparar

- Añade la carpeta al catálogo (**`⌥⇧N`**) y selecciona: **`P`** favorita, **`X`** rechazada, **`U`** sin marca, **`1`–`5`** estrellas.
- Luminar **no modifica tus JPEG**. Aun así, ten copia de los originales.
- **Por qué:** editar solo las mejores fotos ahorra muchísimo tiempo y mejora el resultado.

**Seleccionar tras un viaje, en tres pasadas:**
1. **Rápida:** avanza con **`→`** y rechaza con **`X`** lo que esté claramente mal (desenfocado, ojos cerrados, animal de espaldas). Si dudas, no la rechaces.
2. **De cada ráfaga o situación**, marca con **`P`** solo la mejor (o las dos mejores). Compáralas con **`;`** y míralas al 100 % (**barra espaciadora** en edición).
3. **Estrellas** a las favoritas: por ejemplo, **5** para las que imprimirías y **3** para las del álbum.

**Antes de tocar nada, 30 segundos de análisis:**
- **¿Qué es el sujeto?** (el animal, el árbol solitario, la Vía Láctea)
- **¿Qué distrae?** (un borde muy claro, una rama, un color chillón)
- **¿Cómo era la luz?** (cálida, dura, azulada, mezcla de luces)

### Paso 2 · Ruido: Noiseless AI (solo si hace falta)

- **Image Quality → Noiseless AI.** Analiza la foto y propone un nivel (*Low*, *Middle* o *High*). Acéptalo y revisa al 100 % (**`⌘1`**).
- **Luminosity Denoise:** granito gris. Si la piel o el pelaje parecen de cera, bájalo.
- **Color Denoise:** manchas de color.
- **Details:** equilibra reducción de ruido y detalle. Si lo subes demasiado, vuelve el ruido o aparecen artefactos.
- **Sharpness:** compensa la suavidad que deja la reducción de ruido. En exceso, crea halos.
- **¿Noiseless AI o Denoise?** **Denoise** (Essentials) es la herramienta clásica, con **Luminosity Denoise**, **Color Denoise** y **Boost** (más agresividad). Para ruido ligero puede bastar. Con ISO alto, empieza por Noiseless AI.
- **Por qué primero:** los pasos siguientes (aclarar sombras, subir contraste) aumentan el ruido. Mejor empezar con una base limpia.

### Paso 3 · Recorte y horizonte: Crop AI

- **`C`** abre el recorte.
- **Auto Straighten** nivela el horizonte automáticamente; el deslizador **Straighten** lo ajusta a mano. Estos nombres son los de **Crop AI Improved** (versión 1.29.0 o posterior, con una licencia que lo incluya). En el Crop AI anterior, la nivelación automática se llama **Horizon Alignment**.
- **Smart Compositions** (Crop AI Improved, según versión y licencia) propone varios recortes e indica la regla usada: tercios, proporción áurea, espiral áurea, triángulo áureo o centrado.
- **Proporciones:** el Crop AI anterior las lista en el desplegable **Ratio** (Free, Original, Transposed, 1:1, 4:5, 2:3, 4:3, 5:7, 16:9, 16:10, 21:9, entre otras); en Crop AI Improved el control se llama **Aspect Ratio** y Skylum no enumera sus opciones. **`X`** cambia entre horizontal y vertical.
- **Perspectiva:** si hay árboles o edificios que "caen", usa **Develop → Transform** (Vertical, Horizontal, Aspect).
- **Por qué:** un horizonte torcido arruina cualquier foto y el encuadre decide dónde mira el espectador.

### Paso 4 · Luz: Develop

- Pulsa **`J`** para ver el aviso de recorte.
- **Exposure:** para el sujeto (±0,3 a ±0,7).
- **Highlights:** abajo (−20 a −50) para recuperar cielo y luces.
- **Shadows:** arriba (+15 a +40) para abrir sombras.
- **Whites** y **Blacks:** hasta que el aviso de recorte apenas aparezca.
- **Smart Contrast:** +10 a +25.
- **El truco de los extremos:** con **`J`** activo, sube **Whites** hasta que aparezca el primer aviso y retrocede un poco; baja **Blacks** hasta el primer aviso y retrocede. Así usas todo el rango sin perder detalle.
- **Shadows y Highlights tienen un límite.** Si los llevas muy lejos en un JPEG, la foto se vuelve gris y plana. Si necesitas más, usa una máscara o las Curvas (sección 6.1).
- **Por qué:** primero colocas cada zona de brillo en su sitio; luego das contraste.

### Paso 5 · Color: balance de blancos

- **Develop → Color:** haz clic con el cuentagotas (**`W`**) sobre algo neutro (blanco o gris) o ajusta **Temperature** y **Tint**. El desplegable de presets de **White Balance** es, según Skylum, para archivos RAW: con tus JPEG, usa el cuentagotas y los deslizadores.
- **Mueve poco.** En un JPEG el balance de blancos ya está aplicado: una corrección pequeña funciona; una grande tiñe las luces o las sombras.
- **Remove Color Cast** (en la herramienta **Color**) es un deslizador que detecta y corrige una dominante. Súbelo poco a poco y quédate con el resultado solo si te convence.
- **Por qué:** una dominante de color hace que todo parezca "raro" aunque la luz esté bien.

### Paso 6 · Mejora general: Enhance AI (con moderación)

- **Accent AI:** 15–35. Un solo deslizador que mueve por dentro sombras, luces, contraste, tono, saturación, exposición y detalle.
- **Sky Enhancer AI:** 20–40 si hay cielo de día. Funciona desde la hora azul del amanecer hasta la del atardecer, y **no está pensado para cielos nocturnos**. Si sus controles aparecen en gris, no ha detectado cielo.
- **Comprobación:** pasa el deslizador de 0 a tu valor varias veces. Si la versión editada parece chillona, baja.
- **Si usas mucho Accent AI, haz el Develop más suave.** Ambos tocan sombras, luces y contraste, y sus efectos se suman.

### Paso 7 · Color fino: herramienta Color

- **Vibrance:** +5 a +20. Sube sobre todo los colores apagados y deja en paz los que ya son intensos. Con piel, arena o pelaje, casi siempre es mejor que **Saturation**, que sube todos los colores por igual.
- **HSL:** el desplegable cambia entre **Hue**, **Saturation** y **Luminance**. Después ajustas cada color por separado (ver tablas en cada sección).
- **Hue Shift:** desplaza todos los tonos a la vez. Para correcciones sutiles o efectos fuertes.
- **El truco de la luminancia:** para que un color "pese" más sin saturarlo, **bájale la luminancia**. Un cielo con el azul en Luminance −15 parece más profundo y natural que con el azul en Saturation +15.
- **Por qué:** cada color de la escena necesita algo distinto.

> **Nombres de los colores en HSL.** Esta guía usa los nombres de color habituales (rojo, naranja, amarillo, verde, aguamarina, azul…). La documentación de Skylum no enumera los canales de HSL: si tu versión no muestra exactamente ese color, usa el más próximo.

### Paso 8 · Textura y nitidez: Structure AI y Details

- **Structure AI:** +10 a +25. Contraste local "inteligente" que protege las caras.
- **Details:** **Small Details** para pelo y plumas; **Medium Details** para texturas; **Large Details** con mucho cuidado (es el que más halos crea). **Sharpen** bajo.
- **Details Masking** y **Sharpening Masking:** limitan el enfoque a los bordes y lo apartan de zonas lisas como el cielo. Para **Sharpening Masking**, Skylum recomienda valores de 30–70.
- **Details Protection** (en Details Masking) evita que las zonas ya detalladas queden sobreprocesadas.
- **Develop → Sharpness** tiene su propio enfoque (**Sharpen**, **Radius**, **Masking**). Tus JPEG ya vienen enfocados por la cámara: déjalo a cero y, si hace falta nitidez, usa solo **Details**, con poco.
- **Comprobación:** al 100 %, mira un borde entre el sujeto y el cielo. Si ves una línea clara o un contorno, has enfocado de más.

### Paso 9 · Ajustes locales: máscaras

Aquí se trabaja por zonas: **Dodge & Burn** para aclarar u oscurecer pintando, y la pestaña **Masking** de otras herramientas (Structure AI, Color…) para lo demás. **Todo el paso a paso, desde cero, en la [sección 5](05-ajustes-locales.md).**

**El esquema de tres zonas:**
1. **Sujeto:** un poco más claro, contrastado y nítido.
2. **Fondo** (la máscara del sujeto invertida con **`⌘I`**): un poco más oscuro, menos saturado y con menos textura.
3. **Bordes:** un poco más oscuros (**Vignette** o un **Gradient** en el borde que distrae).

- **Feather:** suaviza la transición. **`/`** para revisar la máscara.
- **Por qué:** dirigir la mirada es lo que separa una foto corregida de una foto buena.

### Paso 10 · Acabado, revisión y exportación

- **Erase** (**`⌘E`**): pintas sobre lo que quieres quitar y pulsas **Erase**. Luminar rellena la zona generando textura a partir de lo que la rodea. Con **Deselect** quitas partes de la selección; **`[`** y **`]`** cambian el tamaño del pincel.
- **Clone** (**`⌘J`**): cuando Erase no acierta, Clone copia píxeles de otra zona. un clic fija el origen y **`⌥`**-clic lo cambia después; **Radius**, **Softness** y **Opacity** controlan el pincel. Mejor muchos toques cortos con poca opacidad.
- **Vignette:** −10 a −20, si encaja. **Choose Subject** coloca el centro del viñeteado sobre el sujeto.
- **Film Grain:** **Amount** 5–10 si ves bandas en el cielo.
- **`\`** (mantener) para comparar con el original. Revisa al 100 %, descansa 5 minutos y **baja lo que sobre**. Para saber cuánto sobra: [¿Me he pasado? La prueba de dos minutos](16-errores-y-lista.md#163-me-he-pasado-la-prueba-de-dos-minutos).
- **Exportar** (**`⇧⌘E`**): sección 13.

**La regla del descanso.** Tras un rato mirando una foto, el ojo se acostumbra a la saturación y al contraste, y siempre parece que "falta un poco más". Por eso las fotos editadas de un tirón suelen verse exageradas al día siguiente. Descansa, vuelve a mirarlas y baja lo que sobre.

## ¿Qué hay en tu foto? La ruta según el contenido

Los 10 pasos son los mismos en todas las fotos; lo que cambia es **cuáles pesan** en cada una. Mira la foto, busca en la tabla lo que contiene y sigue la ruta: los números son los **pasos de este capítulo**. Si la foto contiene dos cosas (un animal bajo un cielo con manchas, una persona delante de una duna), sigue las dos filas.

Antes, dos comprobaciones de 20 segundos que deciden casi todo:
- **¿Para qué es la foto?** Para el móvil casi todo vale; para imprimir, el ruido y los recortes fuertes se notan.
- **¿Qué está ya en el límite?** Pulsa **`J`** y mira el histograma por canales (sección 1.3). Lo que está quemado no vuelve, y el color que ya toca el borde no admite más.

> Las rutas son criterio de esta guía, montado a partir de lo que recomiendan fotógrafos de fauna, paisaje y cielo nocturno para RAW y rebajado para JPEG. Están **por probar con tus fotos**, igual que las [recetas](10-recetas.md). Las cantidades van en palabras: empieza con los valores de [las herramientas, una a una](03-herramientas-una-a-una.md), o con menos.

| Si en la foto hay… | Haz esto, en este orden | No toques |
|---|---|---|
| **Un animal de buen tamaño, a la sombra o al anochecer** (sale azulado y apagado) | **2** ruido suave → **3** recorte moderado, con aire hacia donde mira → **5** un poco más cálido con Temperature → **4** sube Exposure y Shadows con moderación → **9** máscara del animal (**Object Select AI**): algo más de luz y de Structure AI; la misma máscara invertida (**`⌘I`**): fondo un poco más oscuro y menos saturado; **Dodge & Burn** pequeño en el ojo → **10** comprueba que el animal no parezca pegado | El cuentagotas sobre la luz cálida (se la lleva); desenfocar el fondo; enfocar el fondo |
| **Un animal pequeño y lejano** | **1** decide que es una foto para móvil o copia pequeña → **2** ruido antes de recortar, juzgado al tamaño final → **3** recorte fuerte: el ojo en un tercio y aire hacia donde mira → **5** y **4** como en la fila anterior → **9** diferencias pequeñas entre animal y fondo: en un animal pequeño el borde de la máscara es impreciso → **10** exporta a unos 2000 px; **Upscale 2×** solo para imprimir | Enfocar un ojo que mide cuatro píxeles; Upscale 4× o 6× |
| **Un animal con luz plana de mediodía o calima** | **10** manchas de polvo del cielo, lo primero → **3** recorta para sacar al animal del centro y quitar lo que estorba en los bordes → **4** Smart Contrast o una curva en S suave → **7** Vibrance, no Saturation → **9** **Dehaze** bajo, con máscara solo en la lejanía → vuelve a mirar el cielo: Dehaze saca manchas nuevas | Golden Hour y calidez añadida sobre luz plana; Dehaze fuerte. Si el contraste no tiene arreglo, prueba en blanco y negro |
| **Un animal de noche bajo un foco naranja** | La ruta completa está en [9.3](09-noche.md#animales-en-una-charca-iluminada-con-focos): descarta las movidas → mira los canales (el azul estará vacío) → **2** Noiseless AI → corrige el color solo a medias, baja el naranja en HSL o pasa a blanco y negro → comparte a tamaño pequeño | Neutralizar del todo; aclarar las sombras; enfocar; imprimir en grande |
| **Cielo azul despejado** (cualquier foto de día a f/7–f/11) | **10** **Remove Dust Spots**, empezando por arriba, en el tercio izquierdo, que es donde está tu mancha fija → **9** oscurece el cielo solo un poco, con un **Linear Gradient** suave o **Mask AI** (cielo) → **10** **Film Grain** si aparecen bandas → revisa el cielo al 100 % | Structure AI, Details y Dehaze sobre el cielo; bajar mucho la luminancia del azul |
| **Dunas rojas o arena naranja** | Mira el canal rojo → **4** la luz antes que el color → **8** textura para las ondas de la arena → **7** si la arena ha perdido relieve, baja un poco la saturación del naranja en vez de subirla → revisa al 100 % la cresta de la duna contra el cielo: ni halo ni borde de color | Subir la saturación del rojo o el naranja con el canal rojo al límite; cambios grandes de Hue (parten la duna en dos colores) |
| **Una persona o un árbol a contraluz, con el fondo iluminado** (Deadvlei) | **10** polvo del cielo → **4** ajusta la foto entera para la duna y el cielo, que son lo claro → **9** aclara **solo** el sujeto en sombra con una máscara ([5.5](05-ajustes-locales.md)), como mucho un paso de luz; con la misma máscara, quita el tono azulado del suelo en sombra → opcional: **Erase** sobre turistas lejanos | Subir Shadows en toda la foto. Si al aclarar sale ruido, deja el sujeto en silueta |
| **Atardecer, amanecer o una silueta buscada** | **3** horizonte nivelado → **5** conserva la calidez: no neutralices → **4** baja un poco Whites cerca del sol; deja las siluetas negras → **7** Vibrance en pequeña cantidad → **10** Film Grain para el degradado del cielo | Balance de blancos neutro; subir Exposure junto al sol; Sky AI o Sunrays si la foto se presenta como lo que viste |
| **Estrellas o Vía Láctea** | Si hay una serie, [apílala antes](09-noche.md#apilar-una-serie-fuera-de-luminar) → después, toda la [sección 9.2](09-noche.md): color hacia un gris neutro, luz con Curves poco a poco, contraste solo en el núcleo con una máscara Radial, ruido con mano ligera, Film Grain contra las bandas | Sky Enhancer AI; Dehaze o Structure AI en toda la foto; enfocar el cielo; un cielo azul saturado; aclarar el suelo negro |
| **Gente en la calle** (luz dura, sombras, un gesto) | **3** recorte que deje el gesto con aire, y el horizonte o las verticales rectas → **4** contraste con una curva en S suave → si la foto es de luz y sombra, **blanco y negro** ([6.6](06-herramientas-avanzadas.md#66-black--white-essentials)) → **9** **Dodge & Burn**: aclara la cara o el gesto, oscurece los bordes que distraen → **2** ruido, si es de noche, con mano ligera | Borrar a gente con GenErase en una foto documental; caras de cera por exceso de Noiseless AI; enfocar el grano |
| **Un edificio, una fachada o un interior** | **3** **Crop AI → Straighten** y, si se caen las verticales, **Develop → Transform → Vertical** ([8.4](08-paisaje.md#84-ciudad-calle-y-arquitectura)) → **4** Highlights abajo para el cielo y las ventanas → **5** en la hora azul, no calientes → **8** Structure AI con máscara solo en la fachada; si hay horquillado, **HDR Merge** antes de todo ([12.1](12-varias-fotos.md#121-hdr-merge)) | Enderezar un contrapicado hecho a propósito; Structure AI sobre el cielo; HDR con halos alrededor del edificio |
| **Fuego, linternas o luces del lodge** | **5** deja la luz cálida; si importa el cielo, enfríalo aparte con una máscara → **4** baja un poco Whites; el centro de la llama puede quedar blanco → **7** naranja algo menos saturado para recuperar textura en caras y suelo → **10** Film Grain en la zona donde la luz se apaga | Bajar mucho Highlights sobre llamas quemadas (se vuelven grises); enfocar llamas y chispas |

**Qué decide el contenido, en resumen:** dónde va la máscara (paso 9), qué color está en riesgo (pasos 5 y 7) y a qué tamaño puede verse la foto (pasos 1 y 10). Lo demás no cambia. La mayoría de las fotos de día necesitan solo polvo, recorte, balance de blancos, luz y exportar.

**¿No has hecho nunca una máscara?** Es mover primero los deslizadores de una herramienta, abrir su pestaña **Masking**, elegir el tipo, marcar la zona en la foto y revisarla con **`/`**. Está explicado desde cero en la [sección 5.2](05-ajustes-locales.md) y, clic a clic con ejemplos, en las secciones 5.4 a 5.7.

## Rescatar un JPEG difícil

Con un JPEG no hay RAW al que volver, pero Luminar tiene herramientas para casi cada problema. Lo importante es saber **qué se puede arreglar, qué solo se puede disimular y qué no tiene arreglo**. Las herramientas marcadas con ✳️ **inventan** contenido: úsalas sin problema en tu álbum, y dilo si presentas la foto como documento ([sección 14](14-etica.md)).

| Problema | Qué hacer en Luminar | Qué esperar |
|---|---|---|
| **Muy oscura** | Develop: Exposure **+0,5 a +1**, Shadows **+30 a +50**; antes, **Noiseless AI** (nivel propuesto o uno más) | Se arregla bastante; el límite lo pone el ruido que aparece en las sombras |
| **Cielo quemado (blanco puro)** | Highlights **−50 a −60** suaviza el borde. Para tener cielo: ✳️ **Sky AI** (sustituye el cielo) | Sin Sky AI **no se recupera**: no hay información. Con Sky AI, cielo nuevo |
| **Mucho ruido** (ISO alto, noche) | **Noiseless AI** en **High**; Color Denoise alto; Details **+10** para no perder pelo | Muy buen resultado; revisa al 100 % que el pelo o las estrellas no parezcan de plástico |
| **Algo movida o blanda** | **Supersharp AI**, modo **Motion Blur**, nivel **Low** (sube a Middle si no basta). Si solo está blanda una zona, limítalo a ella con una máscara **Brush** | Mejora un movimiento ligero; una foto muy movida no se salva |
| **Desenfocada** (el foco se fue al fondo) | Supersharp AI, modo **Universal**, nivel **Low** | Mejora poco: el desenfoque real no se puede reconstruir |
| **Animal muy pequeño** (recorte fuerte) | Recorta, quita el ruido y después ✳️ **Upscale** (2×, 4× o 6×; empieza por 2×); el enfoque suave, al final | Válida para pantalla o una copia pequeña; revisa al 100 % que no invente textura |
| **Color raro** (dominante) | **Remove Color Cast**; si no basta, Temperature y Tint **±10**; dominante solo en las sombras: Color Harmony → Color Balance | Se corrige bien si no es extrema |
| **Plana, sin contraste** (calima, nublado) | **Dehaze +15**, Smart Contrast **+20**, Supercontrast → Midtones **+15** | Mejora mucho |
| **Bandas en el cielo** | Retoques más suaves en el cielo; **Film Grain** Amount **8** | Se disimulan, no desaparecen |
| **Manchas de polvo del sensor** (puntos grises en el cielo, siempre en el mismo sitio) | **Remove Dust Spots**; luego Erase en las que queden. Vuelve a mirar el cielo después de Dehaze o de subir el contraste: hacen visibles manchas que antes no se veían | Se arregla del todo, pero **foto a foto**: Erase no se sincroniza |
| **Un cable, una rama, un vehículo que estorba** | **Erase** (pequeño); ✳️ **GenErase** (grande o difícil); cables en el cielo: **Remove Powerlines** | Se arregla del todo |
| **Encuadre demasiado justo** | ✳️ **GenExpand**: amplía hasta un 25 %, mejor de un lado cada vez | Útil para ganar aire o cambiar la proporción |
| **Contraluz con el animal negro** | Shadows **+40**; Dodge & Burn → Lighten sobre el animal ([sección 5.5](05-ajustes-locales.md)) | Vuelve algo de detalle; con mucho ruido, acepta la silueta |

**El orden en una foto difícil:** primero el ruido y el movimiento (Noiseless AI, Supersharp AI), luego la luz y el color, luego las herramientas que inventan contenido y, casi al final, Upscale. Después de ampliar solo queda un enfoque suave (Structure AI o Details), como recomienda Skylum ([sección 12.4](12-varias-fotos.md)).

## Ejercicio (una tarde)

1. Elige **tres** fotos de Namibia: una de fauna, una de paisaje y una difícil (oscura, con ruido o quemada).
2. Edita cada una con los **10 pasos**, con este capítulo y la [hoja de bolsillo](03-herramientas-una-a-una.md) abiertos.
3. La difícil, con la tabla de **Rescatar un JPEG difícil**.
4. Al día siguiente, míralas de nuevo y **baja un 20–30 %** lo que se te haya ido.

**Aprobado cuando** haces los 10 pasos de memoria y las tres fotos mejoran sin que se note el retoque.

---

*Parte II · El método*

# 5. Ajustes locales: aclarar u oscurecer solo una parte

> 🔵 **Básico** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: aclarar u oscurecer solo una parte (los ojos, una sombra, el cielo) sin que se note.

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

**Una máscara por herramienta.** Esto es lo importante para empezar: si usas **Develop** para corregir la foto entera y luego le pones una máscara, la corrección pasa a afectar **solo** a la zona de la máscara.

> **Ejemplo con números.** Pones **Exposure +0,3** en Develop y toda la foto se aclara. Después añades a ese mismo Develop una **máscara sobre el león**. Resultado: el **+0,3 queda solo en el león**, y **el resto de la foto vuelve a como estaba antes** de Develop, sin su corrección. La máscara no añade un segundo ajuste: **limita el que ya tiene esa herramienta**. Por eso el método de esta guía es:
- **Develop, sin máscara**, para la luz y el color de toda la foto ([sección 4](04-flujo-base.md)).
- **Dodge & Burn** para aclarar u oscurecer zonas **pintando** (5.4 a 5.6). No necesita máscara: el pincel es la máscara.
- **Otras herramientas, cada una con su máscara**, para lo demás: textura del sujeto, color del fondo, etc. (5.7).

> **¿Se puede añadir Develop dos veces, cada una con su máscara?** La documentación de Skylum dice que sí: en la pestaña **Edits** "puedes añadir la misma herramienta más de una vez", y al hablar de capas, "varias veces y con máscaras distintas". Lo que **no explica son los pasos**. Compruébalo en tu versión ([PENDIENTES](../PENDIENTES.md)). Si se puede, es la forma más precisa de aclarar u oscurecer una zona seleccionada con Mask AI u Object Select AI. Si no, usa los métodos de este capítulo.

**Los tipos de máscara:**

| Máscara | Atajo | Cómo se marca | Para qué |
|---|---|---|---|
| **Brush** | **`B`** | Pintas. Modo **Paint** añade y modo **Erase** quita. Controles **Size**, **Softness** y **Strength**. **`[`**/**`]`** cambian el tamaño | Zonas con forma irregular |
| **Radial** | **`R`** | Arrastras un círculo. El círculo interior marca el tamaño; el exterior, lo suave del borde. **Standard** protege el centro; **Inverted** aplica el efecto dentro | Una zona redonda: una cara, el núcleo de la Vía Láctea |
| **Linear Gradient** | **`G`** | Arrastras un degradado: líneas superior e inferior para la transición, punto central para moverlo; arrastra justo fuera del punto para rotarlo | Cielo o suelo con horizonte recto |
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
| Escalones en un cielo oscurecido | **Bandas**: un JPEG tiene pocos tonos en zonas lisas | Retoque más suave; **Film Grain** (Amount 5–10) para disimularlas |
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

---

*Parte II · El método*

# 6. Herramientas avanzadas

> 🔴 **Avanzado** · Da por sabido: el [flujo base](04-flujo-base.md) y los [ajustes locales](05-ajustes-locales.md) · Te desbloquea: curvas, Supercontrast, Color Harmony, Dodge & Burn, Light Depth y el blanco y negro.

No son imprescindibles, pero dan un control que las herramientas básicas no tienen.

## 6.1. Curves (dentro de Develop)

- **Eje horizontal:** el brillo **original**, de oscuro (izquierda) a claro (derecha).
- **Eje vertical:** el brillo **resultante**.
- **Línea recta en diagonal:** la foto sin cambios.
- **Mueve** un punto y mira la foto. Lo habitual en una curva es que subir aclare y bajar oscurezca, pero la documentación de Skylum lo describe al revés ("drag down to lighten"): compruébalo en tu versión ([PENDIENTES](../PENDIENTES.md)). Luminar admite hasta **10 puntos**.
- Selector de curva: **White** (brillo general), **Red**, **Green** y **Blue**.

**Las cuatro curvas más útiles:**

| Curva | Forma | Efecto | Cuándo |
|---|---|---|---|
| **S suave** | Un punto un poco abajo en las sombras y otro un poco arriba en las luces | Más contraste sin tocar los extremos | Contraste "limpio", casi siempre |
| **S invertida** | Al revés | Menos contraste | Luz de mediodía muy dura |
| **Negros levantados** | El extremo izquierdo, hacia arriba | Negros grisáceos, aspecto de película | Estilo; con cuidado en JPEG |
| **Medios arriba** | Un solo punto en el centro, hacia arriba | Aclara sin tocar blancos ni negros | Foto algo oscura sin quemar el cielo |

**Curvas por canal:**
- **Sombras verdosas:** en **Green**, baja un poco la parte izquierda.
- **Luces demasiado amarillas:** en **Blue**, sube un poco la parte derecha.

## 6.2. Supercontrast (Professional)

Controla el contraste por separado en tres zonas:
- **Highlights**, **Midtones** y **Shadows:** cuánto contraste hay en cada zona (a la derecha, más).
- **Highlights Balance**, **Midtones Balance** y **Shadows Balance:** dónde está el punto medio de cada zona, es decir, qué parte de la foto cuenta como luces, medios o sombras.

**Usos prácticos:**
- **Paisaje:** más contraste en los **Midtones** (roca, hierba) sin endurecer el cielo ni ensuciar las sombras.
- **Fauna:** dar cuerpo al pelaje (Midtones) sin quemar el cielo.
- **Noche:** contraste en **Highlights** (estrellas, Vía Láctea) sin tocar **Shadows**, donde está el ruido.

Empieza con **Midtones** +10/+20 y el resto en 0.

## 6.3. Color Harmony (Professional)

| Control | Qué hace | Uso típico |
|---|---|---|
| **Brilliance** | Colores más ricos | Alternativa suave a Saturation |
| **Warmth** | Positivo calienta; negativo enfría | Ajustar el ambiente tras el balance de blancos |
| **Color Contrast** (**Amount**, **Hue**) | Aumenta la diferencia **entre colores**, no entre luces y sombras | Separar un animal cálido de un fondo verde |
| **Split Color Warmth** (**Warm**, **Cool**) | **Warm:** a la izquierda neutraliza los tonos cálidos y a la derecha los realza. **Cool:** a la izquierda enfría azules y cianes y a la derecha los neutraliza | Arena más dorada sin cambiar el cielo |
| **Color Balance** | Para **Shadows**, **Midtones** o **Highlights**: Cyan–Red, Magenta–Green y Yellow–Blue | Quitar una dominante solo en una zona |

**El uso más útil en JPEG:** **Color Balance** para corregir una dominante **solo en una zona de brillo**. Por ejemplo, si el cielo nocturno está bien pero las sombras son verdosas, en **Shadows** mueve Magenta–Green un poco hacia el magenta.

## 6.4. Dodge & Burn (Professional)

La técnica clásica de laboratorio: **aclarar** y **oscurecer** pintando.

- **Lighten:** aclara. **Darken:** oscurece. **Erase:** borra trazos equivocados.
- **Brush Size** (**`[`**, **`]`**), **Softness** (**`⇧[`**, **`⇧]`**) y **Strength** (intensidad de cada trazo).
- **Overall Amount:** intensidad global de todo lo pintado.

**Cómo usarlo:**
- **Lighten** con **Strength** 10–15 sobre lo que debe destacar: el ojo, la cresta de una duna, la luz en una nube.
- **Darken** sobre lo que distrae: una rama clara, un borde brillante.
- **Muchas pasadas suaves** mejor que una fuerte. Al final, ajusta **Overall Amount**.

**Ejercicio:** en una foto de dunas, aclara las caras iluminadas y oscurece las caras en sombra. Verás aparecer el volumen.

## 6.5. Light Depth (Creative)

Usa un **mapa de profundidad** calculado por IA para iluminar de forma distinta lo cercano y lo lejano, como un foco suave colocado en la escena. Sustituye a la antigua herramienta Relight AI.

- **Amount:** intensidad general.
- **Depth Mask:** dónde cae el centro de la luz según la profundidad.
- **Softness:** cómo de gradual es el paso de la luz a la sombra.
- **Warmth:** temperatura de la luz.
- **Brightness Near / Warmth Near:** brillo y temperatura del **primer plano**.
- **Brightness Far / Warmth Far:** brillo y temperatura del **fondo**.

**Perspectiva atmosférica.** Lo cercano parece más claro, contrastado y cálido; lo lejano, más suave y frío. Para reforzarla: **Brightness Near** +10, **Warmth Near** +5 y **Warmth Far** −5. Valores pequeños: si se nota el efecto, es demasiado.

## 6.6. Black & White (Essentials)

El blanco y negro no es quitar el color, sino **decidir qué gris recibe cada color**.

- **Convert to B&W:** activa la conversión.
- **Modo Luminance:** seis deslizadores (**Red**, **Yellow**, **Green**, **Cyan**, **Blue** y **Magenta**) que deciden lo claro u oscuro que queda cada color.
- **Modo Saturation:** devuelve a cada color parte de su tono original.
- **Color selectivo:** con la máscara de la herramienta puedes dejar un elemento en color. Úsalo con mucha moderación.

**Recetas:**

| Escena | En Luminance | Efecto |
|---|---|---|
| Cielo azul con nubes | **Blue** −30/−50 | Cielo oscuro, nubes que destacan |
| León en hierba seca | **Yellow** −10/−20 | La hierba se oscurece y el león destaca |
| Vegetación verde | **Green** +15 | Vegetación luminosa |
| Personas | **Red** +10 | Piel más limpia |

**Cuándo funciona:** luz dura de mediodía, cielos de tormenta, animales con textura (elefantes, rinocerontes, cebras) o colores que no aportan nada.

**Después de convertir:** el blanco y negro suele necesitar **más contraste** que el color. Usa una curva en S, Supercontrast y Dodge & Burn.

## 6.7. Herramientas de Landscape

| Herramienta | Qué hace | Cuándo |
|---|---|---|
| **Landscape** | **Dehaze** (quita neblina ajustando a la vez contraste, claridad y color), **Golden Hour** (calidez y brillo dorado), **Foliage Enhancer** y **Foliage Hue** (vegetación más viva y su tono) | Calima, vegetación apagada |
| **Water Enhancer AI** | Agua más clara y viva: **Amount**, **Blue**, **Green**, **Original Color**, **Brightness**, **Contrast**, **Depth** y un pincel (**Draw**, **Erase**, **Restore**) para elegir la zona | Ríos, lagos, mar |
| **Twilight Enhancer AI** | Luz y color de hora azul u hora dorada. Presets **Blush**, **Golden**, **Blue**, **Emerald** y **Mauve**, con ajustes de **Sky**, **Dawn**, **Scene Enhancements** y **Water Reflection** | Fotos de crepúsculo o con poca luz |
| **Sky AI** | Sustituye el cielo | Solo fotos creativas (sección 14) |
| **Atmosphere AI** | **Añade** niebla, bruma o neblina (Fog, Layered Fog, Mist, Haze o, en la versión Improved, Ground Fog, Wispy Fog y Heavy Fog) | Solo fotos creativas: añade algo que no estaba |

> **Precaución:** **Dawn** (en Twilight Enhancer AI), **Sky AI** y **Atmosphere AI** añaden luz, cielo o niebla que no existían. En fotos documentales, evítalos o úsalos de forma muy sutil y dilo al compartir la foto.

## 6.8. Herramientas creativas

| Herramienta | Qué hace | Precaución |
|---|---|---|
| **Film Grain** | Grano: **Amount**, **Size**, **Roughness** | **Amount** 5–10. Disimula las bandas |
| **Matte** | Aspecto suave y envejecido: **Amount**, **Fade** (resta detalle en las zonas oscuras), **Contrast**, **Vividness** y tonalidad de color | Quita profundidad a los negros |
| **Toning** | Tiñe por separado luces y sombras: **Highlights/Shadows Saturation** y **Hue**, y **Balance** | Sutil; también útil en blanco y negro |
| **Mood (LUT)** | Aplica una tabla LUT (incluidas o tuyas en formato **.cube**) con **Amount**, **Contrast** y **Saturation** | **Amount** 30–50 para un efecto suave |
| **Glow** | Brillo suave: tipos **Soft Focus**, **Glow**, **Orton Effect** y **Orton Effect Soft** | Ablanda la imagen; usa una máscara para proteger el sujeto |
| **Mystical** | Brillo etéreo: suaviza la luminosidad y sube contraste y saturación | Según Skylum, por debajo de 40 da un resultado más realista |
| **Dramatic** | Aspecto áspero y cinematográfico: reduce saturación y contraste, al estilo del *bleach bypass* | Estético, no correctivo |
| **Magic Light AI** | Destellos y rayos en fuentes de luz artificiales: **Intensity**, **Size**, **Beam Width**, **Glow**, **Clearness**, **Number of Beams** | Solo bombillas y farolas, muy suave |
| **Color Transfer** | Aplica la paleta de color de una foto de referencia | No funciona con fotos en blanco y negro |

## Ejercicio (una tarde)

1. **Curvas:** haz una S suave y compárala (con **`\`**) con el mismo contraste hecho con Smart Contrast.
2. **Dodge & Burn:** en una foto de dunas o de un animal con luz lateral, aclara las caras iluminadas y oscurece las sombras.
3. **Blanco y negro:** convierte una foto de cielo con nubes y prueba **Blue** a −40 en Luminance.

**Aprobado cuando** sabes decir qué herramienta de este capítulo usarías para: más contraste sin tocar el cielo, una dominante solo en las sombras, más volumen en una duna y un cielo dramático en blanco y negro.

---

*Parte III · Por tipo de foto*

# 7. Safari (fauna)

> 🔵 **Básico** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: la foto de fauna terminada: el ojo, el pelaje, el fondo y el color de la luz.

## 7.1. Problemas típicos

| Problema | Por qué ocurre |
|---|---|
| **Ruido** | Amanecer y atardecer, teleobjetivo, velocidad alta → ISO alto |
| **Animal oscuro, cielo quemado** | Animales a contraluz o con el cielo detrás |
| **Luz dura de mediodía** | Sombras negras bajo los ojos y la tripa, contraste excesivo |
| **Calima, polvo y aire caliente** | Fotos "lavadas", con poco contraste y menos nitidez a distancia |
| **Animal pequeño en el encuadre** | Estaba lejos → hay que recortar mucho |
| **Ligero movimiento** | Desde el vehículo, con el animal en movimiento o con poca luz |
| **Fondo que distrae** | Ramas, hierba, vehículos, otros animales |
| **Dominante de color** | Luz anaranjada al amanecer, tierra roja que lo tiñe todo |
| **Manchas oscuras en el cielo** | Polvo en el sensor o en el objetivo |
| **Imagen que "ondula"** | Aire caliente sobre el suelo: el animal lejano se ve blando y deformado |

## 7.2. Paso a paso

**1. Ruido (casi siempre necesario)**
- **Noiseless AI**, con el nivel propuesto. Sube **Details** con cuidado para no perder pelo, plumas y textura de piel.
- **Por qué:** el pelaje es lo primero que se estropea con una reducción de ruido fuerte. Mejor un poco de grano que un animal de plástico.

**2. Movimiento (solo si lo hay)**
- **Supersharp AI**, modo **Motion Blur**, nivel **Low** (los niveles son Low, Middle y High). Revisa al 100 %: si inventa textura, baja de nivel o quítalo.
- **Lo que no tiene arreglo:** un animal **desenfocado** (el foco se fue a la hierba) o muy movido. La **ondulación por el calor** tampoco: no es desenfoque, es deformación.

**3. Recorte pensando en el animal**
- Deja **espacio hacia donde mira o se mueve** el animal.
- Pon el **ojo** cerca de un punto fuerte de los tercios.
- Quita del borde lo que distraiga (un trozo de vehículo, una rama cortada).
- **No cortes por las articulaciones:** evita cortar justo por las rodillas, las patas o la punta de la cola.
- **Orejas y cuernos dentro:** un cuerno cortado por el borde molesta más que un poco de espacio sobrante.
- Si recortas mucho y vas a imprimir, piensa en **Upscale** casi al final: ruido antes, enfoque suave después (sección 12.4).
- El ojo del animal es el centro de interés: construye el encuadre a partir de él.

**4. Luz: expón para el animal**
- **Exposure** hasta que el animal tenga el brillo correcto, aunque el fondo quede algo claro u oscuro.
- **Highlights** −30 a −50 si hay cielo detrás.
- **Shadows** +20 a +40 para abrir la sombra bajo la cabeza y la tripa.
- **Whites** y **Blacks** con **`J`**.
- **Por qué:** el espectador mira al animal. Si el animal está bien, el resto puede estar algo peor.

**5. Quitar la calima**
- **Landscape → Dehaze** +10 a +20.
- En exceso oscurece y satura demasiado.

**6. Color creíble**
- **Balance de blancos:** respeta la luz cálida del amanecer o del atardecer. Corrige solo si el animal parece naranja fosforito.
- **HSL útil en safari:**

| Quiero… | Color | Ajuste |
|---|---|---|
| Hierba seca dorada, no amarilla chillona | Amarillo | Saturation −10; Hue un poco hacia naranja |
| Vegetación menos artificial | Verde | Saturation −10 a −20 |
| Tierra roja menos intensa | Naranja / rojo | Saturation −5 a −15 |
| Cielo azul más profundo | Azul | Luminance −10 a −20 |
| Pelaje cálido natural | Naranja | Luminance +5 |

- **Vibrance** +10 mejor que Saturation.

**7. El animal como protagonista (ajustes locales)**

| Ajuste | Cómo | Valores |
|---|---|---|
| **Textura del pelo** | **Structure AI** → Masking → **Object Select AI** → clic sobre el animal → **Feather** | +15/+25 |
| **Animal más presente** | **Dodge & Burn → Lighten**, pincel grande y suave sobre el animal | **Strength** 15, **Softness** casi al máximo |
| **Fondo más discreto** | **Color** con la máscara del animal (**Copy**/**Paste**) invertida (**`⌘I`**); **Dodge & Burn → Darken** suave donde distraiga | Saturation −10 |
| **Ojo con brillo** | **Dodge & Burn → Lighten**, pincel más pequeño que el iris, **Strength** 15 | Solo el iris, 2–3 pasadas |

**El ojo, en detalle:**
- Aclara **solo el iris**, no todo el ojo.
- **Brillo del ojo:** si existe, no lo agrandes. Si no existe, **no lo pintes**: en fotografía de naturaleza se considera manipulación.
- Comprueba al 100 % que el ojo no parece de cristal.

**8. Limpieza**
- **Remove Dust Spots** quita automáticamente las manchas de polvo del sensor o del objetivo. Después puedes afinar con **Erase**. El polvo del sensor aparece **en el mismo sitio** en varias fotos: revisa toda la serie.
- **Erase** para motas, ramitas o insectos pequeños que distraigan.
- **Importante:** en una foto documental, **no borres elementos de la escena** (otros animales, vehículos, collares de seguimiento) ni uses herramientas generativas (sección 14).

**9. Acabado**
- **Vignette** −10 a −15 si el fondo es claro en los bordes; **Choose Subject** para centrarlo en el animal.
- **Upscale** solo si has recortado mucho, casi al final: ruido antes, enfoque suave después.

## 7.3. Casos concretos

**Animal a contraluz:**
- Decide: ¿silueta o detalle? Para una **silueta**, baja **Blacks** y deja el animal oscuro; resalta el borde de luz con **Highlights**.
- Para ver **detalle**, **Dodge & Burn → Lighten** sobre el animal ([sección 5.5](05-ajustes-locales.md)), y antes **Noiseless AI** (esa zona tendrá ruido).

**Mediodía con luz dura:**
- Shadows +30/+40 y Highlights −30.
- **Structure AI** moderado: la luz dura ya tiene mucho contraste.
- El **blanco y negro** suele funcionar muy bien (sección 6.6).

**Amanecer y atardecer:**
- Conserva la calidez. Casi siempre hará falta Noiseless AI.
- **Light Depth** (opcional) para reforzar la dirección de la luz.

**Pájaros en vuelo contra el cielo:**
- Exposure (Develop) para el pájaro. Si el cielo queda blanco, **Dodge & Burn → Darken** suave sobre el cielo ([sección 5.6](05-ajustes-locales.md)).
- **Details** con **Details Masking** alto para no enfocar el cielo.

**Plumas blancas (garzas, pelícanos, águilas pescadoras):**
- El blanco se quema enseguida. Con **`J`**, baja **Whites** y **Highlights** hasta que el plumaje recupere textura. Si ya está quemado, no hay nada que hacer.
- **No subas la exposición de toda la foto.** Aclara el resto con la máscara del pájaro invertida.
- Las plumas blancas **en sombra** son un buen punto neutro para el cuentagotas.

**Animales oscuros (búfalo, gorila, cuervo):**
- Un búfalo tiene que ser oscuro: no lo aclares de más.
- Para ver detalle, **Dodge & Burn → Lighten** muy suave en las sombras del animal y **Structure AI** +15 con la máscara del animal. Vigila el ruido.

**Cebras:**
- Las rayas blancas se queman y las negras se empastan: Highlights −30 y Blacks un poco arriba.
- **Structure AI** +5 a +10: las rayas ya tienen todo el contraste que necesitan.

**Leopardo en un árbol (luz moteada):**
- **Dodge & Burn → Darken** sobre las manchas de luz en las ramas; **Lighten** (**Strength** 10–15) en la cara del leopardo.
- **Dodge & Burn → Darken** sobre los huecos de cielo entre las ramas, para que no distraigan.

**Elefantes y rinocerontes:**
- **Structure AI** +20/+30 y **Medium Details**: la textura de la piel es su mayor atractivo.
- Si están cubiertos de barro rojizo, no lo "corrijas": es parte de la escena.

**Polvo levantado por los animales:**
- Es atmósfera, sobre todo a contraluz. No uses **Dehaze**: lo eliminaría.

**Foto desde el vehículo con el animal muy lejos:**
- Recorte fuerte + **Upscale** al final.
- Expectativas realistas: servirá de recuerdo o para la pantalla del móvil, no para imprimir grande.

## Ejercicio (una tarde)

1. Elige **cinco** fotos de animales de Namibia con problemas distintos (ruido, contraluz, luz dura, fondo que distrae, recorte fuerte).
2. Edita cada una con el paso a paso de 7.2 y el caso concreto de 7.3 que le toque.
3. En una de ellas, aplica el **ojo, en detalle** y compara con **`\`**.

**Aprobado cuando** en las cinco el animal es lo primero que mira alguien que no conoce la foto.

---

*Parte III · Por tipo de foto*

# 8. Paisaje y ciudad

> 🔵 **Básico** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: cielo y suelo equilibrados, profundidad, y la calle y la arquitectura con las verticales rectas.

## 8.1. Problemas típicos

| Problema | Por qué ocurre |
|---|---|
| **Cielo quemado, suelo oscuro** | El cielo es mucho más brillante que el suelo |
| **Horizonte torcido** | Fotos rápidas a mano |
| **Foto plana y sin profundidad** | Calima, luz de mediodía |
| **Colores apagados o exagerados** | Ajustes de la cámara |
| **Bandas en el cielo** | Degradados suaves en un JPEG de 8 bits |
| **Distorsión y esquinas oscuras** | Gran angular, sobre todo en móviles |

## 8.2. Paso a paso

**1. Horizonte y encuadre**
- **`C`** → **Auto Straighten** (**Horizon Alignment** en el Crop AI anterior).
- **Horizonte en el tercio superior** si lo interesante es el suelo, **en el inferior** si es el cielo. Casi nunca en el centro, salvo en reflejos simétricos.
- **Primer plano, plano medio y fondo:** un buen paisaje suele tener los tres. El recorte debe mantenerlos.
- **Líneas que guían** (un camino, un río, la cresta de una duna): recorta para que entren desde una esquina y lleven hacia el sujeto.

**2. Corrección del objetivo (si hace falta)**
- **Develop → Optics:** **Lens Distortion** para enderezar o curvar las líneas; **Devignette** si las esquinas están oscuras.
- **Auto Defringe** si ves bordes de color en ramas contra el cielo.
- **Auto Distortion Corrections** y **Auto Fix Chromatic Aberrations** solo funcionan con RAW. Con JPEG, ajusta a mano.

**3. Equilibrar cielo y suelo (el paso más importante)**
- **Highlights** −30 a −60 para el cielo; **Shadows** +20 a +40 para el suelo.
- Después, en local:
  - **Cielo:** **Dodge & Burn → Darken**, pincel grande y suave ([sección 5.6](05-ajustes-locales.md)). Para más contraste solo en el cielo, **Supercontrast** con máscara **Mask AI → cielo** o **Gradient** (**`G`**).
  - **Suelo:** **Dodge & Burn → Lighten** (**Strength** 15), o **Light Depth → Brightness Near** (+10 a +20) si el suelo es el primer plano.
- **¿Mask AI o Gradient?** **Mask AI** respeta las formas (montañas, árboles). El **Gradient** es más natural con horizontes rectos (mar, sabana plana) y no deja bordes raros alrededor de los árboles.
- **Luminosity Masking** es otra opción: selecciona solo las zonas más claras (el cielo) por su brillo.

**4. Profundidad**
- **Landscape → Dehaze** +10 a +20 si hay calima. Más oscurece y satura.
- **Light Depth:** primer plano un poco más claro y cálido; fondo algo más frío (sección 6.5).
- **Perspectiva atmosférica:** lo cercano es más contrastado, cálido y saturado; lo lejano, más claro, frío y suave. Reforzar esa diferencia da profundidad.
- **Error frecuente:** un Dehaze fuerte en toda la foto **elimina** esa perspectiva. Mejor un Dehaze de **+10**, o con máscara solo donde haga falta.

**5. Color**
- **Enhance AI:** **Accent AI** 20–30; **Sky Enhancer AI** 25–40.
- **Landscape → Foliage Enhancer** para dar vida a la vegetación; **Foliage Hue** ajusta su tono de verde.
- **HSL útil en paisaje:**

| Quiero… | Color | Ajuste |
|---|---|---|
| Cielo más profundo (sin bandas) | Azul | Luminance −10 a −20 (no más en JPEG) |
| Verdes naturales | Verde / amarillo | Saturation −10 a −20 |
| Arena o dunas más cálidas | Naranja | Saturation +5 a +10; Luminance +5 |
| Roca rojiza menos intensa | Rojo / naranja | Saturation −5 a −10 |
| Agua turquesa | Aguamarina | Hue hacia aguamarina |

**6. Textura**
- **Structure AI** +15 a +25 con la **máscara del cielo invertida**. El cielo no necesita textura: si se la das, aparecen ruido y bandas.
- **Supercontrast → Midtones** +10/+20 como alternativa más limpia (sección 6.2).
- **Dunas y roca:** algo más de Structure AI, y Light Depth para marcar las crestas.

**7. Acabado**
- **Vignette** muy suave (−10).
- **Film Grain** con **Amount** 5–10 si el cielo muestra bandas.

## 8.3. Casos concretos

**Desierto y dunas:**
- La cámara suele **subexponer** la arena clara: Exposure +0,3/+0,5.
- Highlights −20 para no perder la textura de la arena.
- La luz rasante marca las ondas: refuérzala con **Structure AI** y **Dodge & Burn**.
- **Color Harmony → Split Color Warmth → Warm** a la derecha: arena más dorada sin tocar el cielo azul.

**Atardecer:**
- No neutralices el color. Como mucho, Temperature **−5** si el naranja es exagerado.
- **Sky Enhancer AI** +10 a +20, o **Color Harmony → Warmth** +5 a +10.
- **Twilight Enhancer AI** (preset **Golden** o **Blush**) es otra opción, con **Amount** 20–30. Revisa que no añada luz que no había.
- Siluetas de árboles: **Blacks** abajo, para que sean negras de verdad.
- **El sol** casi siempre estará quemado, y es normal. Lo que importa es que el halo de alrededor tenga degradado y no un borde duro.

**Sabana con cielo de tormenta:**
- **Cielo:** **Structure AI** +15 con **Mask AI → cielo** (las nubes sí agradecen textura) y **Dodge & Burn → Darken** para oscurecerlo.
- **Suelo:** **Dodge & Burn → Lighten** (**Strength** 15). El atractivo está en el contraste entre el cielo oscuro y el suelo iluminado.

**Montaña:**
- Las montañas lejanas suelen salir azuladas y planas por la atmósfera. **Dehaze** +10 a +15 con **Mask AI → montañas** les devuelve el relieve.
- **Supercontrast** con la misma máscara para marcar el relieve sin tocar el cielo.
- **Nieve:** blanca con textura, no gris ni quemada. Cuidado con **Whites**.

**Agua (ríos, cascadas, mar, lagos):**
- **Water Enhancer AI:** **Amount**, **Blue**, **Green**, **Brightness** y **Contrast** para el agua, con **Draw**/**Erase** para elegir la zona. Con moderación: un turquesa exagerado se ve artificial enseguida.
- **Mask AI → agua** permite tratar el agua con cualquier otra herramienta.
- **Reflejos:** un reflejo suele ser **algo más oscuro** que la escena real. Si lo aclaras igual que el cielo, parece falso.
- **Agua sedosa** (exposición larga): baja **Highlights** para que tenga matices y no sea una mancha blanca.

**Bosque y selva:**
- Muchos verdes y luz moteada: Saturation de los verdes −10/−20 y Hue un poco hacia el amarillo.
- Contraste moderado: un bosque muy contrastado parece sucio.
- Si hay niebla, no la quites: es la atmósfera.

**Hora azul (justo después de la puesta de sol):**
- La escena es azulada de verdad. No calientes el balance de blancos.
- Las luces artificiales (pueblo, lodge) se ven cálidas: el contraste naranja/azul es el atractivo.
- **Twilight Enhancer AI**, preset **Blue**, con **Amount** 20–30, si quieres reforzarlo.

**Cambiar el cielo (Sky AI):** técnicamente es fácil, pero en una foto documental o de viaje **convierte la foto en un montaje**. Úsalo solo en fotos creativas y dilo si las compartes.

## 8.4. Ciudad: calle y arquitectura

Cómo se hacen estas fotos con la cámara: [manejo 13 · Calle y arquitectura](../manejo-a6700/13-calle-y-arquitectura.md). Aquí, lo que cambia al editarlas.

**Verticales y horizonte:**
- **Horizonte:** **Crop AI** → **Straighten** o **Auto Straighten** (sección 4, paso 3).
- **Verticales que se caen:** en **Develop**, la sección **Transform** tiene **Vertical** (inclina la foto para enderezar un edificio fotografiado desde la calle), **Horizontal** y **Aspect** (compensa el estiramiento que deja la corrección). Según Skylum son controles manuales ("use these sliders to adjust perspective distortion manually"). Al corregir se pierden los bordes: deja margen al disparar. Skylum dice que los controles de Develop **cambian entre archivos RAW y no RAW** y no aclara si Transform aparece con un JPEG: compruébalo ([PENDIENTES](../PENDIENTES.md)).
- **Barriles y cojines** (líneas rectas que se curvan en los bordes): **Develop → Lens Distortion**. Con el JPEG de la a6700 la cámara ya corrige la distorsión del objetivo, así que normalmente no hace falta.
- **No lo enderezes todo.** Un contrapicado fuerte hecho a propósito se deja como está.

**Calle:**
- **Blanco y negro** (sección 6.6) cuando la foto es de luz y sombra, no de color. Sube el contraste con **Curves** en S suave (6.1).
- **Dodge & Burn** (6.4): aclara la cara o el gesto y oscurece lo que distrae en los bordes. Es lo que hacían en el laboratorio Cartier-Bresson, Fan Ho y Adams ([los maestros](../conceptos/11-los-maestros.md)).
- **Ruido de ISO alto de noche:** **Noiseless AI** al principio (paso 2). Un poco de grano en la calle de noche es aceptable; las caras de cera no.
- **No borres a la gente con GenErase** en una foto de calle documental: deja de ser lo que pasó (sección 14).

**Arquitectura:**
- **Cielo sin quemar y fachada con detalle:** **Highlights** abajo y **Shadows** arriba con moderación; si la foto viene de un horquillado, **HDR Merge** (12.1).
- **Hora azul:** no calientes el balance de blancos; el contraste entre ventanas naranjas y cielo azul es la foto.
- **Textura de la piedra:** **Structure AI** con máscara sobre la fachada, no sobre el cielo.

## Ejercicio (una tarde)

1. Elige un paisaje de Namibia con el cielo más claro que el suelo.
2. Equilibra cielo y suelo (paso 3) y da profundidad (paso 4).
3. Haz una **copia virtual** con un tratamiento distinto (por ejemplo, más cálido o en blanco y negro) y compáralas con **`;`**.

**Aprobado cuando** el cielo tiene textura, el suelo tiene luz, y no aparecen bandas ni halos en el horizonte.

---

*Parte III · Por tipo de foto*

# 9. Fotografía nocturna

> 🔵 **Básico** → 🔴 · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: estrellas, Vía Láctea, focos, fuego y luna sin ruido ni colores falsos, y apilar una serie.

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
- **Dos gustos, los dos defendibles.** Roger Clark defiende el color natural, con balance de luz de día: cielo neutro o cálido y Vía Láctea parda ([Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)). Ian Norman busca un balance neutro, que en sus fotos acaba en torno a 3900 K, más frío que el de luz de día ([Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)). Para un álbum de recuerdo, quédate cerca de lo que viste.

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
| **Starry Landscape Stacker** | Unos 40 USD; la versión de prueba es igual, pero pone marca de agua | Alinea el cielo y deja el suelo quieto con una máscara. Hace en Mac lo que Sequator en Windows (comparación de esta guía) | <https://sites.google.com/site/starrylandscapestacker/home> |
| **Siril** | Gratis | Apila y corrige degradados de fondo (*background extraction*). Alinea por las estrellas, así que el suelo queda borroso y hay que tratarlo aparte | <https://siril.org/> |
| **StarStaX** | Las versiones antiguas, gratis (ya no se mantienen) | Sobre todo para **trazas de estrellas**: se queda con lo más claro de cada foto de una serie larga; no alinea el cielo | <https://starstax.net/> |

Sequator, que citan muchas guías, solo existe para Windows ([lo dice su página de descargas](https://sites.google.com/view/sequator/download)).

**Paso a paso:**
1. **No edites las fotos antes.** Ni ruido, ni enfoque, ni correcciones de lente: estropean el apilado.
2. Abre la serie en el programa. **Starry Landscape Stacker acepta JPEG**, aunque su autor los desaconseja por la calidad ([requisitos](https://sites.google.com/site/starrylandscapestacker/restrictions-and-requirements-version-1-9)). En Siril no está confirmado: si no los abre, convierte antes los JPEG a TIFF, sin editarlos.
3. Marca el cielo (en Starry Landscape Stacker, pintando la máscara) y apila.
4. Guarda el resultado como **TIFF de 16 bits**.
5. Añade ese TIFF al catálogo de Luminar (admite TIFF de 8 y 16 bits) y edítalo con los pasos de esta sección. Notarás que Noiseless AI casi no hace falta.

Un apilado de fotos del mismo sitio y del mismo momento es una técnica admitida incluso en concursos de fotografía de paisaje natural ([normas de los NLPA](https://www.naturallandscapeawards.com/rules/)). Si enseñas la foto, basta con decir "apilado de 10 tomas".

## 9.3. Luces artificiales (lodge, campamento, ciudad)

- **Balance de blancos:** no neutralices del todo las bombillas cálidas. Algo de calidez hace la escena acogedora.
- **Highlights** −30/−50 para recuperar las luces. Si las bombillas están quemadas, déjalas: es normal.
- **Noiseless AI** casi siempre.
- **Magic Light AI** (opcional, **Intensity** 10–20) añade rayos y brillo a bombillas y farolas.
- **HSL:** naranja → Saturation **−10** si la luz es demasiado intensa.
- **Luces de distintos colores:** neutraliza la que más se vea y deja la otra con su color.

### Animales en una charca iluminada con focos

Es el caso más difícil del viaje: ISO muy alto (hasta 12800), todo teñido de **naranja** por el foco y el fondo negro. **Un color neutro no se puede recuperar de un JPEG así**: bajo esa luz casi toda la información está en el canal rojo y **el canal azul está vacío** (medido en una foto del viaje: rojo 179, verde 65 y azul 1 sobre el elefante). Esto es criterio de esta guía (no hay tutoriales de referencia para este caso), así que pruébalo con una foto y ajusta:

1. **Descarta primero las movidas.** Casi todas las fotos de la charca se hicieron por debajo de 1/60 s: un animal que se mueve sale borroso, y eso no tiene arreglo.
2. **Mira los canales** en el histograma (sección 1.3). Verás el azul pegado a la izquierda: por eso no hay color neutro que recuperar. Si el rojo toca el borde derecho, no subas la exposición ni la saturación.
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

---

*Parte IV · Más allá de una foto*

# 10. Recetas completas

> 🔵 **Básico** · Da por sabido: los capítulos [4](04-flujo-base.md) a [9](09-noche.md) · Te desbloquea: recetas completas, de principio a fin, para las fotos típicas.

> ⚠️ **Provisional.** Estas recetas combinan los pasos de la guía para cinco situaciones típicas, pero **todavía no se han probado con fotos reales**. Los valores son puntos de partida. Se revisarán con fotos de muestra. Mira siempre la imagen, no el número.

## 10.1. León al amanecer, con luz cálida y algo de ruido

*Situación: ISO alto, teleobjetivo, el león mira a la izquierda, fondo de hierba seca desenfocada.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Noiseless AI | Nivel propuesto; Details con cuidado |
| 2 | Crop | Espacio a la izquierda; el ojo en un punto fuerte de los tercios |
| 3 | Develop | Exposure +0,2; Highlights −25; Shadows +20; Whites/Blacks con `J`; Smart Contrast +10 |
| 4 | Develop → Color | Sin tocar la temperatura: la calidez es real |
| 5 | Enhance AI | Accent AI +20 |
| 6 | Color → HSL | Amarillo: Saturation −10; naranja: Luminance +5 |
| 7 | Dodge & Burn → Lighten | Pincel grande y suave sobre el león; Strength baja |
| 8 | Structure AI + Object Select AI del león | +20 |
| 9 | Color + la máscara del león (Copy/Paste) invertida | Saturation −10 |
| 10 | Dodge & Burn → Lighten | Iris, con poca Strength |
| 11 | Vignette + Choose Subject | Amount −12 |

## 10.2. Elefante a mediodía, en blanco y negro

*Situación: luz cenital, sombras negras bajo la cabeza, cielo blanquecino.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Crop | Elefante entero o cortado a media pata, nunca por las rodillas |
| 2 | Develop | Highlights −40; Shadows +35; Blacks −10 |
| 3 | Black & White | Convert to B&W; Luminance: Blue −40, Yellow −10 |
| 4 | Develop → Curves | S marcada |
| 5 | Structure AI + Object Select AI del elefante | +30 |
| 6 | Dodge & Burn | Lighten en las arrugas iluminadas; Darken en el suelo y, si sigue demasiado claro, en el cielo |
| 7 | Vignette | Amount −15 |

## 10.3. Dunas al atardecer

*Situación: JPEG de móvil, luz rasante, cielo naranja, algunas bandas en el cielo.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Crop | Horizonte en el tercio superior; cresta en diagonal desde una esquina |
| 2 | Develop | Exposure +0,2; Highlights −30; Shadows +10 |
| 3 | Color Harmony | Split Color Warmth → Warm +15 |
| 4 | Supercontrast | Midtones +15 |
| 5 | Structure AI + Mask AI → cielo invertida | +20 |
| 6 | Dodge & Burn | Lighten en las caras iluminadas; Darken en las caras en sombra |
| 7 | Film Grain | Amount bajo, para disimular las bandas |

## 10.4. Vía Láctea sobre una acacia

*Situación: ISO 6400, 20 s, gran angular, cielo anaranjado por un pueblo lejano.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Noiseless AI | Middle; Color Denoise alto; Luminosity Denoise bajado hasta ver las estrellas pequeñas |
| 2 | Crop | Horizonte en el tercio inferior; acacia fuera del centro |
| 3 | Develop → Color | Temperature un poco hacia el azul, hasta un cielo gris neutro o algo cálido; la banda verde del horizonte (*airglow*) se queda |
| 4 | Develop | Exposure +0,4; Shadows +5; Blacks −10 solo si el cielo se ve gris |
| 5 | Supercontrast + Radial (Inverted) sobre el núcleo | Highlights +15 |
| 6 | Dodge & Burn → Lighten | Muy suave sobre el núcleo |
| 7 | Color Harmony + Gradient desde el horizonte | Warmth un poco negativa |
| 8 | Dodge & Burn → Lighten | Muy suave sobre la acacia y el suelo, con contención |
| 9 | Details | Muy bajo; Details Masking alto |
| 10 | Vignette | Amount −10 |

## 10.5. Cena alrededor del fuego

*Situación: ISO alto, caras naranjas, fondo negro, llamas quemadas.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Noiseless AI | Nivel propuesto (probablemente High) |
| 2 | Develop → Color | Temperature un poco más fría, sin perder el naranja |
| 3 | Develop | Highlights −40; Shadows +20; Blacks −5 |
| 4 | Color → HSL | Naranja: Saturation −10 |
| 5 | Face AI | Face Light, suave |
| 6 | Vignette | Amount −20 |

---

*Parte IV · Más allá de una foto*

# 11. Trabajar en serie

> 🔵 **Básico** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: editar cientos de fotos coherentes entre sí: seleccionar, sincronizar y presets.

Tras un safari puedes volver con miles de fotos. Editarlas una a una es inviable.

## 11.1. Sincronizar ajustes (Sync Adjustments)

1. Edita bien **una foto representativa** de una situación (misma luz, mismo animal).
2. Con ella seleccionada (borde naranja), selecciona las demás en el catálogo o en la tira de fotos (**Filmstrip**): **`⇧`**-clic para un rango, **`⌘`**-clic para fotos sueltas. Las demás aparecen con borde blanco.
3. Clic secundario (**`⌃`**-clic, o clic con dos dedos en el trackpad) → **Adjustments → Sync Adjustments** (**`⇧⌘S`**).
4. Revisa cada foto y retoca lo que cambie, sobre todo la exposición.

**Copiar y pegar ajustes:** **`⌘C`** en la foto editada y **`⌘V`** en la otra.

**Qué tener en cuenta:**
- Según Skylum, las herramientas de IA (Accent AI, Structure AI, Skin AI) se sincronizan de forma más fiable entre fotos distintas.
- **Crop**, **Erase** y **Background Removal** **no se sincronizan**: hay que hacerlos foto a foto.
- **Revisa las máscaras** en cada foto sincronizada: el animal no estará en el mismo sitio en todas.
- Las miniaturas del catálogo son previsualizaciones: revisa el resultado en la vista de una sola foto.

**Receta para una sesión con el mismo color raro.** Si disparaste con el balance de blancos fijo, todas las fotos de una misma luz tienen **la misma dominante** (azulada a la sombra o al anochecer, naranja bajo los focos). Corrige **una** (ruido, balance de blancos y luz), sincroniza esos ajustes con el resto de la sesión y deja para cada foto lo que no se sincroniza o cambia de sitio: recorte, manchas de polvo y máscaras.

## 11.2. Presets propios

> **Aviso:** según Skylum, **aplicar un preset sobrescribe los cambios** que ya hayas hecho en la foto. Aplica el preset **primero** y ajusta después.

1. Ajusta una foto (o modifica un preset existente).
2. En el desplegable **Actions**, abajo, elige **Save as Preset**.
3. El preset se guarda en la pestaña **My Presets**, donde puedes renombrarlo. Su menú permite **Edit**, **Rename**, **Delete** y **Show in Finder**.

**Consejos:**
- Crea presets **de base**, no de "look". Por ejemplo, "Safari amanecer ISO alto" (Noiseless AI, Accent AI suave) o "Noche estrellada" (Noiseless AI, Blacks abajo, Details bajo).
- Un preset es un **punto de partida**: aplícalo y ajusta.
- **Crop AI** no se guarda en los presets.

## 11.3. Coherencia en una serie

Una serie de fotos de viaje se ve profesional cuando las fotos **parecen de la misma familia**:
- **Mismo balance de blancos** para la misma situación de luz.
- **Misma intensidad** de saturación y contraste.
- **Mismo tratamiento de los negros**: todos profundos o todos levantados.
- Si mezclas color y blanco y negro, **agrupa**: un bloque de blanco y negro, no fotos sueltas.
- **Color Transfer** puede igualar la paleta de una foto con la de otra (no funciona con fotos en blanco y negro).

**Truco:** mira todas las fotos del álbum juntas en el catálogo. La que "salta" por más saturada, más oscura o de otro color es la que hay que corregir.

## 11.4. Tus fotos del viaje: de la tarjeta a la selección

Antes de editar la primera foto de un viaje, tres cosas, en este orden.

**1. Copia de seguridad, antes de nada.** Las fotos que solo están en un sitio no están a salvo. La regla clásica **3-2-1**: **3** copias, en **2** soportes distintos (el ordenador y un disco externo, por ejemplo), y **1** de ellas fuera de casa o en la nube. Haz las copias de los **originales** antes de abrirlos en Luminar.

**2. Lleva las fotos a Luminar.** **Add Folder with Images** (**`⌥⇧N`**) añade la carpeta al catálogo. Luminar enlaza esa carpeta: no la copia ni toca tus JPEG, y las ediciones se guardan en su catálogo ([sección 2.2](02-luminar-por-dentro.md)). Haz copia de seguridad también del catálogo: **File > Catalog > Backup** (se recupera con **File > Catalog > Restore from Backup**).

**3. Elige antes de editar.** Con miles de fotos, editar sin elegir es imposible:
1. **Primera pasada:** rechaza (**`X`**) lo claramente fallido. Rápido: si dudas, no la rechaces.
2. **Segunda pasada:** de cada ráfaga o situación, marca (**`P`**) la mejor, comparándolas con **`;`** y al 100 %.
3. **Tercera pasada:** estrellas (**`1`–`5`**) a las favoritas. Las de **5** son tu selección final: crea un álbum con ellas (**`⌘N`**).

Edita primero esa selección final, con el [flujo base](04-flujo-base.md) y los [ajustes locales](05-ajustes-locales.md). Después, el resto **en serie** (11.1).

> **Las fotos de Namibia están en JPEG.** Todo lo de esta guía se aplica tal cual. Elige con más cuidado que con RAW: una foto quemada o muy oscura en JPEG no tiene arreglo.

## Ejercicio (una tarde)

1. Elige **10** fotos de la misma situación (el mismo animal, la misma luz).
2. Edita bien una y sincroniza el resto (**`⇧⌘S`**); revisa las máscaras y la exposición de cada una.
3. Guarda los ajustes como **preset** propio.

**Aprobado cuando** las diez, vistas juntas en el catálogo, parecen de la misma familia.

---

*Parte IV · Más allá de una foto*

# 12. Varias fotos en una, ampliar y generar

> 🔴 **Avanzado** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: HDR, panorámicas, apilado de enfoque, ampliar y las herramientas generativas.

Estas herramientas están en la pestaña **Extra**. La documentación de Skylum no detalla qué formatos de entrada admite cada una. Con RAW hay más margen, pero puedes probar con tus JPEG.

## 12.1. HDR Merge

**Qué es:** combina varias fotos de la misma escena con exposiciones distintas (una oscura para el cielo, una clara para el suelo) en una sola imagen con todo el rango.

- **Dónde:** Extra → **Merge Tools** → **HDR Merge**.
- **Cómo:** arrastra las fotos horquilladas a HDR Merge, ajusta las opciones (icono de tres puntos) y pulsa **Continue**.
- **Opciones:**
  - **Auto Alignment:** alinea las tomas si disparaste a mano.
  - **Ghost Reduction:** corrige lo que se movió entre tomas (hierba, agua, personas). Eliges la foto de referencia y la intensidad.
  - **Chromatic Aberration Reduction:** quita los bordes de color.
- **Resultado:** un **TIFF** en la carpeta HDR, que luego editas como cualquier foto. El aspecto "HDR" exagerado viene de la edición posterior, no de la fusión: edita con suavidad.
- **Con fauna, casi nunca:** los animales se mueven entre una toma y otra.

## 12.2. Panorama Stitching

**Qué es:** une varias fotos de la misma escena tomadas girando la cámara.

- **Cómo:** selecciona las fotos, arrástralas a **Panorama Stitching**, ajusta las opciones (distorsión, viñeteado, aberración cromática, fantasmas) y pulsa **Start**.
- **Proyecciones:** **Spherical**, **Cylinder**, **Mercator**, **Plane** y **Fisheye**.
- **Tamaño máximo de exportación:** 15.000 px.
- **Después:** recorta a mano los bordes irregulares.
- **Consejos de toma** (Skylum los da para panorámicas hechas a partir de vídeo; valen igual para fotos): mantén constantes la luz y la exposición (exposición y balance de blancos en manual), bloquea el enfoque, gira con suavidad y, si puedes, usa trípode.

## 12.3. Focus Stacking

**Qué es:** une **hasta 100 fotos** con distinto punto de enfoque para que toda la escena salga nítida (por ejemplo, un paisaje con una flor muy cerca).

- **Dónde:** Extra → **Merge Tools** → **Focus Stacking**.
- **Cómo:** selecciona las fotos en el catálogo y arrástralas a Focus Stacking. El icono del engranaje activa **Auto Alignment** y **Chromatic Aberration Reduction**. Pulsa **Stack**.
- **Resultado:** un **TIFF** en la carpeta Focus Stacking.
- Lo ideal es disparar con trípode.

## 12.4. Upscale

**Qué es:** aumenta la resolución con IA, **hasta 6×**.

- **Dónde:** Extra → **Enhancement tools** → **Upscale**.
- **Límites:** entrada mínima de 257 × 257 px; entrada máxima de 16.000 px en el lado largo; salida máxima de 32.000 px en el lado largo.
- **Factores:** 2×, 4× y 6×.
- **Cuándo usarlo:** solo si lo necesitas (un recorte fuerte que quieres imprimir o ver en grande), casi al final de la edición.
- **El orden que recomienda Skylum:** quita el ruido **antes** (Noiseless AI o la reducción de ruido de Develop), amplía y enfoca **después**, con suavidad, con Structure AI o Details.
- **Revisa al 100 %:** en pelo y plumas puede inventar textura.

## 12.5. Herramientas generativas: GenErase, GenSwap y GenExpand

Generan con IA contenido que **no estaba** en la foto.

- **GenExpand** amplía el lienzo **hasta un 25 %** y rellena el espacio nuevo. Skylum recomienda ampliaciones pequeñas (en torno al 10 %), de un lado cada vez. **GenExpand Improved** (versión 1.29.0 o posterior, con una licencia que lo incluya) admite hasta dos lados por generación. El resultado se guarda como **TIF**. La versión *Regular* admite una descripción en texto (en inglés funciona mejor) y necesita conexión a internet; la versión *Improved* no necesita texto.
- **GenErase** y **GenSwap** borran o sustituyen elementos generando contenido nuevo.

> En fotos documentales, de naturaleza o de concurso, estas herramientas **convierten la foto en una ilustración** (sección 14).

---

*Parte IV · Más allá de una foto*

# 13. Exportar

> 🔵 **Básico** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: exportar bien para la pantalla, la familia y el papel.

## 13.1. El cuadro de exportación

**Export** (**`⇧⌘E`**) ofrece:
- **Formatos:** JPEG, PNG, TIFF, JPEG 2000, Photoshop (PSD, **sin capas**), PDF y DNG.
- **Quality**, **Sharpen** y **Color Space:** las opciones disponibles dependen del formato.
- **Resize:** tamaño original, **Long Edge** (lado largo), **Short Edge** (lado corto) o **Dimensions** (ancho y alto), además de **Resolution**.
- **Signature:** firma o marca de agua (imagen o texto). Se aplica solo al archivo exportado.

Luminar **recuerda la configuración** de la última exportación. Revísala antes de cada uso.

## 13.2. Ajustes recomendados por uso

*Recomendaciones de esta guía, no de Skylum.*

| Uso | Formato | Tamaño | Calidad | Sharpen |
|---|---|---|---|---|
| **Archivo personal** | JPEG | Original | Máxima o casi | No |
| **Redes sociales, mensajería** | JPEG | Long Edge de unos 2.000 px | Alta | Bajo |
| **Pantalla grande o TV 4K** | JPEG | Long Edge de 3.840 px | Alta | Bajo |
| **Imprimir** | TIFF o JPEG a máxima calidad | Según el tamaño de la copia (13.3) | Máxima | Moderado |
| **Seguir editando en otro programa** | TIFF | Original | — | No |

- **Redes sociales:** cada red cambia a menudo sus tamaños recomendados. Consulta el actual antes de exportar.
- **Espacio de color:** para pantallas y web, **sRGB**, que es el estándar. Un espacio más amplio no recupera colores que el JPEG original no tiene, y algunas aplicaciones y webs pueden mostrarlo con los colores apagados. Para imprimir, usa el que te pida el laboratorio.

## 13.3. Imprimir

**Píxeles necesarios según el tamaño de la copia:**

| Copia | A 300 ppp | A 200 ppp |
|---|---|---|
| 10 × 15 cm | 1.181 × 1.772 px | 787 × 1.181 px |
| 20 × 30 cm | 2.362 × 3.543 px | 1.575 × 2.362 px |
| 30 × 45 cm | 3.543 × 5.315 px | 2.362 × 3.543 px |
| 50 × 75 cm | 5.906 × 8.858 px | 3.937 × 5.906 px |

*Cálculo: centímetros ÷ 2,54 × ppp. 300 ppp es la resolución de referencia para copias que se miran de cerca; para copias grandes que se ven de lejos se puede bajar.*

**Consejos:**
- Una copia en papel suele verse **más oscura** que en la pantalla. Haz una **copia virtual** (**`⌘'`**) para imprimir y ajusta en ella.
- Pide una **prueba pequeña** antes de una copia grande.

## 13.4. Nombres de archivo

Una convención sencilla ahorra búsquedas: `AAAA-MM-DD_lugar_tema_numero.jpg`. Por ejemplo, `2026-08-14_masai-mara_leon_01.jpg`. Guarda las exportaciones en una carpeta distinta de la de los originales.

## 13.5. Tus fotos: compartir con la familia e imprimir

**Paso 1 · Mira cuántos píxeles tiene la foto.** En Luminar, pestaña **Info** (**`I`**). Con la a6700 en tamaño **L (26M)** y proporción 3:2, un JPEG tiene **6192 × 4128 píxeles** (según la Guía de ayuda de Sony). Si la cámara estaba en un tamaño menor (M o S), o si has recortado, tendrás menos.

**Paso 2 · Exporta dos versiones de cada foto buena.**

| Para qué | Resize | Calidad | Por qué |
|---|---|---|---|
| **Compartir** (WhatsApp, álbum compartido, correo) | **Long Edge** de unos 2.000 px | Alta | Se ve bien en móviles y pantallas, y las aplicaciones la comprimen menos |
| **Imprimir** | **Tamaño original** | Máxima | El laboratorio necesita todos los píxeles |

**Paso 3 · Calcula hasta qué tamaño puedes imprimir.** La cuenta: **píxeles ÷ ppp × 2,54 = centímetros**. A **300 ppp** la copia aguanta mirarla de cerca; a **200 ppp**, sigue viéndose bien a la distancia normal de un cuadro ([13.3](13-exportar.md#133-imprimir)).

| Tu foto | Píxeles | A 300 ppp | A 200 ppp |
|---|---|---|---|
| **Entera** (L 26M, sin recortar) | 6192 × 4128 | **52 × 35 cm** | **79 × 52 cm** |
| **Recortada a la mitad del ancho** | 3096 × 2064 | **26 × 17 cm** | **39 × 26 cm** |
| **Recortada a un tercio del ancho** | 2064 × 1376 | **17 × 12 cm** | **26 × 17 cm** |

*Cuentas redondeadas al centímetro.*

**Si te quedas corto:** **Upscale** casi al final de la edición, con el ruido ya quitado y el enfoque suave después (empieza por 2×; [sección 12.4](12-varias-fotos.md)), y revisa al 100 % que no invente textura en el pelo o las plumas. Pide una **prueba pequeña** antes de la copia grande.

**Para la familia:** elige pocas y buenas. Una selección de 20–30 fotos editadas con el mismo estilo ([sección 11](11-trabajar-en-serie.md)) se disfruta más que 300 sin elegir.

## 13.6. Consejos para las fotos que vas a imprimir

Una copia en papel enseña cosas que la pantalla del móvil esconde. Antes de mandar una foto a imprimir, repasa esta lista.

**Elegir la foto**
- **Nítida al 100 %** (**`⌘1`**) en lo que importa: el ojo del animal, el primer plano del paisaje. Lo que en el móvil parece nítido puede no serlo en 30 cm de papel.
- **Sin manchas de polvo:** en grande se ven. Pasa **Remove Dust Spots** y revisa el cielo de esquina a esquina.
- **Sin bandas ni ruido exagerado:** míralo al 100 % en el cielo y en las sombras.

**El tamaño y la proporción**
- Las fotos de la a6700 son **3:2**, igual que las copias de **10 × 15**, **20 × 30** y **30 × 45 cm**: entran **sin recortar**.
- Para otros formatos hay que recortar antes, para decidir tú qué se pierde: **13 × 18** se parece a **5:7**, que está en la lista de proporciones del recorte; para **A4** (21 × 29,7 cm), usa **Enter Custom** e introduce esa proporción.
- Comprueba los píxeles con la tabla de la [sección 13.5](13-exportar.md#135-tus-fotos-compartir-con-la-familia-e-imprimir) antes de elegir el tamaño.

**Ajustar para el papel** (hazlo en una **copia virtual**, **`⌘'`**, para no tocar la versión de pantalla)
- **Un poco más clara:** el papel refleja la luz y no la emite, así que la copia suele verse **más oscura** que la pantalla. Empieza con **Exposure +0,1 a +0,2**.
- **No empastes las sombras:** el papel no llega a un negro tan profundo como una pantalla. Si al editar dejaste sombras casi negras, ábrelas un poco (**Shadows +5 a +10**).
- **Edita con la pantalla a brillo moderado** ([sección 1.9](01-conceptos-basicos.md)). Con el brillo al máximo, todas las copias salen oscuras.

**Exportar**
- **Tamaño original**, **calidad máxima** y **sRGB**, salvo que el laboratorio pida otra cosa.
- **Si imprimes en casa:** desde la versión 1.29.0 ([registro de cambios](https://skylum.com/whats-new/luminar-neo/68)), el menú **Export** tiene **Print…** (*Home Printing*), con perfiles **ICC** de impresora y papel, **Soft Proofing** (simula en pantalla cómo quedarán los colores en ese papel) y **Print Sharpening** (None, Low, Medium o High). Una prueba pequeña en papel sigue siendo la mejor comprobación.
- **Sharpen** del cuadro de exportación: **moderado** ("bajo" y "moderado" son palabras de esta guía: Skylum no documenta qué niveles ofrece Sharpen al exportar; elige el intermedio de los que veas). La copia pierde algo de nitidez al imprimirse; no lo subas tanto que aparezcan bordes blancos.
- Si te quedas corto de píxeles, **Upscale** al final (empieza por 2×) y revisa al 100 %.

**Imprimir**
- Pide primero una **prueba pequeña** (10 × 15) de la misma foto, en el mismo laboratorio y papel.
- **Papel mate:** sin reflejos, colores y negros más suaves; muy bonito en paisaje y en blanco y negro. **Papel brillante:** colores y negros más intensos, pero refleja la luz.
- Si la prueba sale oscura o con otro color, corrige **en la copia virtual** y vuelve a probar.

## Ejercicio (una tarde, y una visita al laboratorio)

1. Elige **una** foto que quieras imprimir y repasa la lista de 13.6.
2. Haz una **copia virtual** para papel (Exposure +0,1 a +0,2) y expórtala a tamaño original.
3. Exporta también la versión para compartir (lado largo de unos 2.000 px) y mándala a la familia.
4. Pide una **prueba de 10 × 15** y compárala con la pantalla.

**Aprobado cuando** la prueba en papel se parece a lo que veías en pantalla, o sabes qué corregir en la copia virtual.

---

*Parte IV · Más allá de una foto*

# 14. Ética, concursos y ubicación

> 🟢 **Iniciación** · Da por sabido: nada · Te desbloquea: saber qué es corregir y qué es manipular, y qué hacer con el GPS y la fauna amenazada.

> **Tus fotos, tu decisión.** Estas normas son para **concursos** y para fotos que publiques **como documento** ("esto pasó así"). En tu álbum personal puedes usar **todas** las herramientas, también las generativas: borrar un cable, cambiar un cielo quemado o ampliar el lienzo. Lo único que pide la honestidad es **no presentar como real lo que has inventado**. Cómo sacar el máximo partido a un JPEG difícil, en [Rescatar un JPEG difícil](04-flujo-base.md#rescatar-un-jpeg-difícil).

## 14.1. Corregir no es cambiar la escena

En fotografía documental, de naturaleza y de viaje, la línea general es: **puedes corregir la foto, pero no cambiar la escena**.

| Normalmente aceptado | Normalmente no aceptado |
|---|---|
| Exposición, contraste, color, curvas | Añadir o quitar animales, personas o elementos significativos |
| Recorte | Cambiar el cielo (**Sky AI**) |
| Reducción de ruido, nitidez | Añadir una luna, un sol o niebla (**Atmosphere AI**) que no estaban |
| Ajustes locales moderados (Dodge & Burn) | Ampliar la foto con IA generativa (**GenExpand**) |
| Quitar polvo del sensor | Borrar collares de seguimiento o anillas |
| Blanco y negro | Pintar un brillo en el ojo |

**Las reglas exactas cambian de un concurso a otro.** Algunos concursos de naturaleza piden a los finalistas el archivo original para comprobar que no se ha alterado la escena. Lee siempre las bases antes de editar. Si dudas, guarda una **copia virtual** sin los retoques dudosos.

## 14.2. Herramientas que crean contenido

**GenErase**, **GenSwap**, **GenExpand**, **Sky AI**, **Sunrays** (añade un sol que no estaba), **Atmosphere AI** y la luz **Dawn** de **Twilight Enhancer AI** añaden o inventan elementos. Son útiles en fotos creativas, pero:
- Convierten una foto documental en una ilustración.
- Suelen estar prohibidas en concursos de naturaleza y en fotoperiodismo.
- Si compartes una foto con contenido generado o sustituido, **dilo**.

## 14.3. Ubicación GPS y fauna amenazada

Muchas cámaras y todos los móviles guardan la **ubicación GPS** en el archivo. Para especies amenazadas (rinocerontes, pangolines, grandes felinos, aves en el nido), publicar la ubicación exacta puede ayudar a los cazadores furtivos.

- **Antes de publicar** fotos de especies amenazadas, **quita la ubicación** del archivo exportado. La documentación de exportación de Skylum no menciona una opción para quitar metadatos. En macOS, Apple documenta cómo hacerlo en la app **Fotos** (Imagen → Ubicación → Ocultar ubicación). En **Vista Previa**, Herramientas → Mostrar inspector enseña la ubicación; que desde ahí se pueda eliminar está por comprobar ([PENDIENTES](../PENDIENTES.md)).
- **No des la ubicación exacta en el texto** ("cerca del lodge X, junto al río Y").

## 14.4. Personas

- Pide permiso para fotografiar a personas, sobre todo a niños y en comunidades locales.
- No alteres el tono de piel de nadie más allá de corregir la luz.

---

*Parte IV · Más allá de una foto*

# 15. Disparar mejores JPEG la próxima vez

> 🔵 **Básico** · Da por sabido: el [capítulo 1](01-conceptos-basicos.md) · Te desbloquea: ajustar la cámara para que el JPEG llegue con margen, y lo que enseñan tus fotos de Namibia.

La mejor edición empieza en la cámara. Si disparas en JPEG, estos ajustes amplían el margen para editar en Luminar.

> ⚠️ **Lo primero, con la a6700: que dispare en RAW.** En Namibia todas las fotos salieron solo en JPEG por un error de configuración. Comprueba `Formato archivo` = **RAW** (también después de cargar cada memoria) y que tus archivos sean **`.ARW`**: [configuración básica](../manejo-a6700/04-configuracion-basica.md). Los ajustes de esta página son para cuando, por lo que sea, solo tengas JPEG.

> Los nombres de los menús cambian según la marca. Consulta el manual de tu cámara. Con la **Sony a6700**, la configuración completa, con las rutas de menú verificadas, está en [Manejo de la a6700](../manejo-a6700/README.md).

## 15.1. Ajustes de la cámara

| Ajuste | Recomendación | Por qué |
|---|---|---|
| **Calidad JPEG** | La máxima y el tamaño más grande | Menos compresión, menos bandas |
| **Estilo de imagen** (Picture Style en Canon, Picture Control en Nikon, Creative Look o Creative Style en Sony) | **Neutro** o **Estándar** con algo menos de contraste | Deja más detalle en luces y sombras para editar |
| **Nitidez en cámara** | Algo por debajo del valor estándar | Es más fácil añadir nitidez al editar que quitar la que sobra |
| **Reducción de ruido en cámara** | Baja | La reducción de ruido de la cámara puede borrar detalle que luego no se recupera |
| **Balance de blancos** | Un preajuste **fijo y acorde con la luz**: "Luz de día" al sol y en atardeceres, "Sombra" o "Nublado" cuando el sujeto está a la sombra o el sol ya se ha puesto, y Kelvin de noche ([balance de blancos](../conceptos/04-balance-de-blancos.md)) | El automático tiende a "corregir" y apagar los colores del atardecer. Uno fijo los conserva, pero hay que **cambiarlo cuando cambia la luz**: "Luz de día" a la sombra deja la foto azulada |
| **Espacio de color** | sRGB, si no tienes un motivo para usar otro | Es el estándar de pantallas y web |
| **RAW + JPEG** | Si la tarjeta y la cámara lo permiten | El RAW es el seguro para las fotos importantes |

## 15.2. Al disparar

- **Protege las luces.** En JPEG, las luces quemadas no se recuperan y las sombras sí se pueden abrir un poco. Si dudas, usa algo de compensación de exposición negativa.
- **Activa el aviso de sobreexposición** en la pantalla de la cámara.
- **Fauna:** prioriza una velocidad de obturación alta. Un poco de ruido tiene arreglo; una foto movida, no.
- **Desde el vehículo:** apoya el objetivo y pide que apaguen el motor si es posible: la vibración mueve la foto.
- **Polvo:** cambia de objetivo lo menos posible y con la cámara hacia abajo.

## 15.3. Noche: estrellas nítidas

- **Trípode** y disparo retardado o con mando a distancia.
- **Enfoque manual** sobre una estrella brillante, con la imagen ampliada en la pantalla.
- **Diafragma** lo más abierto posible.
- **Tiempo máximo sin trazos, regla del 500 (aproximada):** 500 ÷ (focal × factor de recorte) = segundos. Por ejemplo, con 14 mm en *full frame*: 500 ÷ 14 ≈ 36 s; en APS-C (×1,5): 500 ÷ 21 ≈ 24 s. Con sensores de muchos megapíxeles, conviene un tiempo más corto.
- **Balance de blancos fijo:** evita que cada foto salga con un color distinto.
- **Varias tomas iguales seguidas:** te permiten apilarlas después para reducir el ruido (sección 9.2).
- **Evita la luna llena** para la Vía Láctea: su luz borra las estrellas débiles.

## 15.4. Lo que enseñan tus fotos de Namibia

Medidas las 2.731 fotos del viaje (noviembre de 2026), salen seis cosas que se arreglan **en la cámara**, no en Luminar. Los datos y cómo se midieron están en las [notas de las fotos](../notas-de-investigacion/edicion-jpeg-safari-paisaje-noche/fotos-de-muestra.md):

| Lo que pasó | Cómo se ve | Para la próxima vez |
|---|---|---|
| **Polvo en el sensor** | Una mancha gris fija en el cielo, arriba, en el tercio izquierdo: aparece en 99 de las 147 fotos con cielo liso, en seis días distintos | Comprueba y limpia el sensor antes de salir ([equipo, polvo en el sensor](../manejo-a6700/15-equipo-accesorios.md#polvo-en-el-sensor-comprobarlo-y-limpiarlo)) |
| **Vía Láctea oscura** (20 s, f/2, ISO 1600) | Cielo casi negro; al aclarar en Luminar salen bandas y ruido | Mira el **histograma** tras la primera toma: si la montaña está pegada al borde izquierdo, sube a **ISO 3200** ([astro](../manejo-a6700/10-astrofotografia.md)). En JPEG, la luz que falta no se recupera después |
| **Charca con focos, todo naranja** | Animales de un solo color; no se puede neutralizar | Balance de blancos en **Kelvin**, bajando hacia 3200 K hasta que el color sea creíble **en la revisión**, antes de la serie ([charcas](../manejo-a6700/07-fauna-de-noche.md)) |
| **Charca por debajo de 1/60 s** | 116 de las 122 fotos nocturnas de la charca se hicieron más lentas que 1/60 s (algunas, a 1/25 s): riesgo de animales movidos | **1/60 s** como mínimo con el animal quieto; si se mueve, más rápido y más ISO: el ruido tiene arreglo y el movimiento no |
| **Fotos azuladas a la sombra** | Dominante fría medida en el león a la sombra (18:24, antes de la puesta de sol); la última hora de la tarde sale algo más fría que el resto. El 91 % del viaje se hizo con un balance de blancos **fijo**, sin que se sepa cuál | El fijo es la regla de esta guía, pero **cambia con la luz**: "Sombra" (7000 K) con el animal a la sombra, "Nublado" (6000 K) con el cielo tapado o el sol ya puesto ([balance de blancos](../conceptos/04-balance-de-blancos.md)). Dime qué balance tenías puesto ([PENDIENTES](../PENDIENTES.md)). Lo bueno del fijo: la dominante es igual en toda la sesión y se corrige una vez y se sincroniza ([11.1](11-trabajar-en-serie.md)) |
| **Animales muy pequeños** en el encuadre | Recortes de 2–3 veces: solo valen para el móvil | A 350 mm y aun así lejos: espera a que se acerque, o cuenta la escena con el animal pequeño a propósito ([composición](../conceptos/06-composicion.md)) |

**Dos mejoras más de formato:**
- **RAW**, lo primero ([configuración básica](../manejo-a6700/04-configuracion-basica.md)). Todo lo anterior duele mucho menos con un RAW.
- **Si algún día quieres un archivo ya revelado mejor que el JPEG**, la a6700 graba **HEIF**: `MENU → Toma → [Calid. img/grab.] → [Conm JPEG/HEIF]`, con `HEIF(4:2:2)` para dar prioridad a la calidad. Sony avisa de que no todos los programas lo abren, y la lista de formatos de Skylum incluye HEIC sin nombrar el HEIF de Sony: **prueba una foto en Luminar antes de fiarte** ([PENDIENTES](../PENDIENTES.md)).

Y para la noche: haz siempre **10 tomas iguales seguidas** de cada encuadre. Es lo que permite [apilar](09-noche.md#apilar-una-serie-fuera-de-luminar).

---

*Parte V · Referencia*

# 16. Errores típicos y lista de comprobación

> ✅ **Lista** · Da por sabido: el [flujo base](04-flujo-base.md) · Te desbloquea: revisar una foto antes de exportarla y saber si te has pasado.

## 16.1. Los errores más frecuentes

| Error | Cómo se reconoce | Solución en Luminar |
|---|---|---|
| **Exceso de saturación** | Colores "fosforito", pieles naranjas | Vibrance en vez de Saturation; HSL a la baja |
| **Exceso de contraste local** | Halos, aspecto HDR sucio | Bajar Structure AI y Large Details; máscara para el cielo |
| **Sombras abiertas de más** | Foto gris y plana, ruido | Menos Shadows; Blacks abajo |
| **Reducción de ruido excesiva** | Pelo, piel o estrellas de plástico | Bajar Luminosity Denoise; Details con cuidado |
| **Enfocar el ruido** | Grano áspero, estrellas falsas | Primero el ruido, luego la nitidez; Details Masking alto |
| **Bandas en el cielo** | Escalones en el degradado | Ajustes más suaves; Film Grain ligero |
| **Bordes de máscara visibles** | Línea alrededor del sujeto | Feather, Shift Edge; revisar con `/` |
| **Color poco creíble** | Atardecer neutro, noche naranja | Recordar cómo era la luz real |
| **Pantalla demasiado brillante** | Las fotos se ven oscuras en otras pantallas | Brillo de pantalla moderado |
| **Viñeteado evidente** | Esquinas negras "de filtro" | Vignette suave |
| **Dehaze fuerte en toda la foto** | Colores pesados, sin profundidad | Dehaze más bajo o con máscara |
| **Fotos de una serie que no casan** | Una más saturada u oscura que las demás | Sync Adjustments y revisión conjunta |
| **Editar cansado** | Al día siguiente todo parece exagerado | Descansar y bajar lo que sobre |

## 16.2. Lista de comprobación

```
PREPARAR
[ ] Selección hecha (P / X / estrellas) y copia de los originales
[ ] 30 s de análisis: ¿qué es el sujeto? ¿qué distrae? ¿cómo era la luz?
[ ] Pantalla con brillo moderado, sin True Tone ni Night Shift

CALIDAD
[ ] Histograma por canales si domina un color (dunas, focos, atardecer)
[ ] Ruido: Noiseless AI (vigilar pelo / estrellas al 100 %)
[ ] Movimiento: Supersharp AI, Motion Blur, Low (solo si hace falta)

GLOBAL
[ ] Recorte y horizonte (C)
[ ] Optics si hay distorsión o esquinas oscuras
[ ] Luz: Exposure, Highlights, Shadows, Whites, Blacks con J
[ ] Balance de blancos creíble (W)
[ ] Landscape → Dehaze suave si hay calima
[ ] Enhance AI moderado (Sky Enhancer solo de día)
[ ] Color: Vibrance y HSL, color por color
[ ] Structure AI / Details con moderación

LOCAL
[ ] Ojos: Dodge & Burn → Lighten, pincel pequeño, Strength baja
[ ] Sujeto: Dodge & Burn → Lighten (luz) · Structure AI + Object Select AI (textura)
[ ] Fondo: Color + máscara del sujeto invertida (⌘I) · Dodge & Burn → Darken
[ ] Cielo / suelo: Dodge & Burn · Mask AI (A) o Gradient (G) en otras herramientas
[ ] Noche: Vía Láctea con Supercontrast + Radial (R); horizonte con Gradient
[ ] Bordes de máscara revisados con /

ACABADO
[ ] Manchas de polvo en el cielo: Remove Dust Spots (repasar tras Dehaze)
[ ] Erase (solo distracciones pequeñas)
[ ] Vignette suave
[ ] Film Grain si hay bandas

REVISIÓN Y SALIDA
[ ] \ para comparar con el original
[ ] Revisión al 100 % (⌘1)
[ ] Descanso → segunda mirada → bajar lo que sobre
[ ] Comprobar en el móvil
[ ] Quitar el GPS si es fauna amenazada
[ ] Exportar (⇧⌘E) con el tamaño y la calidad de su uso
```

## 16.3. ¿Me he pasado? La prueba de dos minutos

Mientras editas, el ojo se acostumbra: cada cambio parece poco y siempre "falta un poco más". Por eso no sirve preguntarte si te gusta; sirven **pruebas que no dependen de tu ojo cansado**. Haz estas cinco, en orden, antes de exportar cualquier foto.

| # | Prueba | Cómo | Te has pasado si… |
|---|---|---|---|
| 1 | **Antes y después** | Mantén **`\`** (o usa el icono **Visibility**; si no lo ves, activa **View > Show Photo Actions Panel**) tres o cuatro veces | Al ver el original sientes **alivio**, o la editada parece otra foto y no la misma con mejor luz |
| 2 | **De lejos** | **`⌘0`** y aléjate un paso de la pantalla, o mira la miniatura en el catálogo | El ojo se va a un **color**, un **halo** o un **borde** antes que al sujeto |
| 3 | **De cerca** | **`⌘1`** en tres sitios: el borde del sujeto, una zona lisa (cielo) y el detalle fino (pelo, estrellas) | Hay una línea alrededor del sujeto, escalones o grano áspero en el cielo, pelo de alambre o de cera |
| 4 | **Los límites** | **`J`** y el histograma (sección 1.3) | Hay **más** zonas rojas o azules que antes de empezar: esas las has creado tú |
| 5 | **A la mitad** | En la herramienta que más has movido, baja el deslizador **a la mitad**. Repite con las dos siguientes | La foto **no empeora** con la mitad: quédate con la mitad |

**Y una sexta, la mejor: el día siguiente.** Vuelve a abrir la foto sin haber mirado otras antes. Lo que sobra se ve en dos segundos. Lo normal es bajar un 20–30 %.

### Qué mirar en cada parte de la foto

| Mira… | Te has pasado si… | Qué bajar |
|---|---|---|
| **El pelaje o la piel del animal** | Naranja o amarillo "de dibujos animados"; el pelo parece alambre, o cera | Saturation o Vibrance; Structure AI y Details; Luminosity Denoise |
| **Los ojos** | Son lo más brillante de la foto, con el blanco puro o aspecto de cristal | **Strength** de Dodge & Burn, o borra parte de lo pintado |
| **El sujeto contra el fondo** | Parece una **pegatina**: borde claro u oscuro, o el fondo mucho más oscuro o borroso de lo creíble | La diferencia entre la máscara y su inversa; sube **Feather** |
| **El cielo de día** | Azul marino o turquesa, más oscuro que el suelo; escalones en el degradado; una franja clara sobre el horizonte o la duna | Luminancia y saturación del azul; Dehaze; la fuerza de la máscara del cielo |
| **La arena y las dunas** | Naranja fosforito y sin ondas: el color ha tapado el relieve | Saturación del naranja y del rojo |
| **La hierba y los árboles** | Verde neón o amarillo limón | Saturación del verde y del amarillo en HSL |
| **Las sombras** | Grises y lechosas, con manchas de color; toda la foto tiene aspecto "HDR" | Shadows; Accent AI; Structure AI |
| **Los blancos** (nubes, pelaje claro, sal) | Se han vuelto **grises** | Highlights menos abajo; Whites un poco arriba |
| **El cielo nocturno** | Azul saturado; estrellas con un anillo oscuro o claro; el fondo tiene "gusanos" o manchas; la Vía Láctea parece pintada | Temperature; Dehaze y Structure AI del núcleo; Noiseless AI |
| **El fuego y las luces** | La llama es gris; todo es de un único naranja | Highlights menos abajo; saturación del naranja |
| **Los bordes de la foto** | La viñeta se ve como un círculo oscuro | Vignette |
| **La foto junto a sus vecinas** | Destaca en la serie por color o contraste | Iguala con Sync Adjustments y revisa |

### Tres reglas para no llegar a pasarte

1. **Entre dos valores, el menor.** En un JPEG, cada ajuste fuerte saca ruido, bandas o halos.
2. **Un solo protagonista por foto.** Si has subido el color, deja tranquilo el contraste; si has trabajado el sujeto, no toques también el cielo.
3. **Enséñala en el móvil a alguien.** Si lo primero que dice es "qué colores" y no "qué leona", el retoque se nota más que la foto.

Para lo que cada herramienta hace cuando te pasas, mira la columna "te has pasado si…" de [las herramientas, una a una](03-herramientas-una-a-una.md).

---

*Parte V · Referencia*

# 17. Atajos de teclado (macOS)

> 📋 **Referencia** · Da por sabido: nada · Te desbloquea: editar sin buscar en los menús.

Atajos de **macOS**, según la documentación oficial de Skylum. Esta guía no cubre Windows.

## Los símbolos de las teclas del Mac

| Símbolo | Tecla | Dónde está |
|---|---|---|
| **`⌘`** | Comando (*Command*) | A los lados de la barra espaciadora |
| **`⌥`** | Opción (*Option*) | Entre Control y Comando |
| **`⇧`** | Mayúsculas (*Shift*) | En los extremos de la fila inferior de letras |
| **`⌃`** | Control | Abajo a la izquierda |

Un atajo como **`⇧⌘E`** se hace manteniendo Mayúsculas y Comando, y pulsando E. **`⌥`**-clic es hacer clic con Opción pulsada. El **clic secundario** ("clic derecho") es **`⌃`**-clic, o un clic con dos dedos en el trackpad.

## Catálogo y selección

| Atajo | Acción |
|---|---|
| **`L`** | Ir al catálogo |
| **`⌥⇧N`** | Añadir una carpeta con imágenes |
| **`⌘N`** | Nuevo álbum |
| **`P`** / **`X`** / **`U`** | Favorita / rechazada / sin marca |
| **`1`–`5`** / **`0`** | Estrellas / quitar las estrellas |
| **`→`** / **`←`** | Foto siguiente / anterior |
| **`⌘`**-clic / **`⇧`**-clic | Seleccionar fotos sueltas / un rango |
| **`⌘F`** | Buscar en el catálogo |
| **`⌘'`** | Crear una copia virtual |
| **`;`** | Comparar |
| **`F`** | Vista previa a pantalla completa |

## Edición

| Atajo | Acción |
|---|---|
| **`T`** / **`E`** / **`I`** | Pestañas Presets / Tools / Info |
| **Barra espaciadora** | Alternar entre ajustar a la pantalla y 100 % |
| **`⌘1`** / **`⌘0`** | Zoom al 100 % / ajustar a la pantalla |
| **`⌘+`** / **`⌘−`** | Acercar / alejar |
| **`C`** | Recortar (dentro del recorte, **`X`** cambia la orientación) |
| **`W`** | Cuentagotas (con Develop → Color abierto) |
| **`J`** | Mostrar u ocultar el aviso de recorte |
| **`\`** (mantener) | Ver el original |
| **`⌘E`** | Erase |
| **`⌘J`** | Clone (**`⌥`**-clic cambia el punto de origen) |
| **`⌘Z`** / **`⇧⌘Z`** | Deshacer / rehacer |
| **`⌘C`** / **`⌘V`** | Copiar / pegar ajustes |
| **`⇧⌘S`** | Sincronizar ajustes |
| **`⇧⌘R`** | Volver al original |
| **`⇧⌘E`** | Exportar |

## Máscaras

| Atajo | Acción |
|---|---|
| **`A`** | Mask AI |
| **`B`** / **`R`** / **`G`** | Brush / Radial / Gradient |
| **`/`** | Mostrar u ocultar la máscara |
| **`⌘I`** | Invertir la máscara |
| **`[`** / **`]`** | Pincel más pequeño / más grande |
| **`⇧[`** / **`⇧]`** | Menos / más suavidad del pincel |

## Si tu teclado es español

La tabla de Skylum usa caracteres que en el teclado de Estados Unidos tienen tecla propia. En un teclado de Mac en español (ISO), algunos de esos caracteres no tienen tecla propia y se escriben así:

| Carácter | Para qué | En el teclado español de Mac |
|---|---|---|
| **`\`** | Ver el original | **`⌥º`** (la tecla a la izquierda del 1) |
| **`/`** | Mostrar la máscara | **`⇧7`** |
| **`;`** | Comparar | **`⇧,`** |
| **`[`** / **`]`** | Tamaño del pincel | **`⌥`** + la tecla a la derecha de la P / **`⌥+`** |
| **`'`** | Copia virtual (**`⌘'`**) | Tecla propia, a la derecha del 0 |

La documentación de Skylum no dice si Luminar reconoce estos atajos cuando el carácter necesita **`⌥`** o **`⇧`**. Pruébalos en tu Mac ([PENDIENTES](../PENDIENTES.md)). Si alguno no responde, tienes dos salidas:

- **Usa el control en pantalla:** **Show** en las acciones de la máscara y los deslizadores **Size** y **Softness** del pincel hacen lo mismo que sus atajos. Para ver el original sin el atajo, usa el **icono Visibility**, que muestra el antes y el después de una foto editada (si no lo ves, activa **View > Show Photo Actions Panel**). Para comparar, Skylum solo documenta el nombre del atajo.
- **Añade la distribución "ABC" (EE. UU.)** en Ajustes del Sistema → Teclado → *Introducción de texto* → **Editar** → **+**, y cambia a ella mientras editas (**`⌃`** + barra espaciadora; o la tecla 🌐, si la tienes configurada para cambiar de fuente de entrada). Con ella, las teclas están donde dice la tabla de Skylum: **`[`** y **`]`** a la derecha de la P, **`;`** y **`'`** a la derecha de la L, **`/`** junto al Mayúsculas derecho.

---

*Parte V · Referencia*

# 18. Glosario

> 📋 **Referencia** · Da por sabido: nada · Te desbloquea: entender cualquier palabra de Luminar y del retoque.

Los términos de Luminar y del retoque. Los de cámara, luz y exposición (ISO, apertura, ETTR, hiperfocal…) están en el [glosario de conceptos](../conceptos/13-glosario.md).

| Término | Significado |
|---|---|
| **8 bits** | 256 niveles por color, como en un JPEG |
| **Bandas** | Escalones visibles en un degradado suave |
| **Contraluz** | La luz principal está detrás del sujeto |
| **Copia virtual** | Otra versión de la misma foto, sin duplicar el archivo |
| **Dominante** | Un color que tiñe toda la foto |
| **Feather** | Suavizado del borde de una máscara |
| **Halo** | Contorno claro u oscuro alrededor de un objeto por exceso de contraste local |
| **Histograma** | Gráfica de la distribución del brillo |
| **Hora azul** | Tras la puesta o antes de la salida del sol, cuando el cielo es azul intenso |
| **Hora dorada** | Primera y última hora de sol, con luz cálida y rasante |
| **HSL** | Tono (Hue), saturación (Saturation) y luminancia (Luminance) de cada color |
| **Máscara** | El mapa de la zona a la que se aplica una herramienta; Luminar la muestra en rojo con **`/`** |
| **ISO** | Sensibilidad de la cámara; cuanto más alto, más ruido |
| **No destructivo** | Los ajustes se guardan aparte y el original no cambia |
| **Perspectiva atmosférica** | Lo lejano se ve más claro, frío y suave por el aire |
| **ppp** | Píxeles por pulgada al imprimir |
| **Recorte (clipping)** | Zonas totalmente blancas o negras, sin detalle |
| **Ruido** | Granulado (de luminosidad o de color) por ISO alto o sombras aclaradas |
| **sRGB** | El espacio de color estándar de pantallas y web |
| **Viñeteado** | Oscurecimiento de las esquinas |

---

*Parte V · Referencia*

# 19. Preguntas frecuentes

> 📋 **Referencia** · Da por sabido: nada · Te desbloquea: las respuestas rápidas a las dudas más frecuentes.

**¿Merece la pena editar JPEG, o debería pasarme a RAW?**
Merece la pena: un JPEG se puede mejorar mucho. Pero si tu cámara lo permite, dispara en **RAW + JPEG** en los viajes importantes. El RAW es el seguro para las fotos que de verdad te importan.

**¿Sirve esta guía para fotos del móvil?**
Sí. Los JPEG del móvil suelen venir muy procesados (nitidez, saturación, reducción de ruido). Por eso conviene **ir aún más suave** con Structure AI, Details y Saturation.

**Accent AI lo hace casi todo. ¿Por qué no usar solo eso?**
Porque decide por ti y actúa sobre toda la foto. Úsalo como base suave y haz el resto con herramientas que controlas.

**Mi foto está quemada. ¿Alguna herramienta lo arregla?**
No. Lo completamente blanco en un JPEG no tiene información. Bajar Highlights suaviza el borde de la zona quemada, pero no recupera detalle.

**¿Qué hago si el resultado de una herramienta de IA no me convence?**
Bájala, o quítala y hazlo a mano. Las herramientas de IA son atajos, no obligaciones.

**No encuentro una herramienta de la guía.**
Algunas dependen de tu versión o licencia (por ejemplo, las versiones *Improved* requieren Luminar for Desktop 1.29.0 o posterior y una licencia que las incluya). Consulta la documentación oficial (sección 20).

**¿Cómo sé si me he pasado editando?**
Tres pruebas: compara con **`\`**; mira la miniatura junto a otras fotos sin editar; y vuelve a mirarla al día siguiente. Si "salta" por artificial, baja.

---

*Parte V · Referencia*

# 20. Fuentes

> ✅ **Fuentes** · Da por sabido: nada · Te desbloquea: comprobar de dónde sale cada dato de esta guía.

Los nombres de las herramientas, los controles, los atajos y los límites técnicos de esta guía se han comprobado con la documentación oficial de Skylum (noviembre de 2026). Los valores numéricos de ajuste son **recomendaciones de esta guía**, no de Skylum.

**General**
- [Índice de la documentación de Luminar](https://support.skylum.com/llms.txt)
- [Atajos de teclado (Desktop)](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- [Sincronizar ajustes](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/syncing-adjustments)
- [Presets](https://support.skylum.com/presets) · [Personalizar presets](https://support.skylum.com/presets/customizing-presets)
- [Exportar](https://support.skylum.com/saving-and-exporting-files/export-image) · [Imprimir en casa](https://support.skylum.com/printing/home-printing)
- [Recorrido por Luminar](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough) · [Empezar a editar (pestaña Edits)](https://support.skylum.com/editing-tools/start-editing-with-edit-view)
- [Histograma](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/histogram) · [Favoritas, rechazadas e icono Visibility](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images)
- [Aplicar presets](https://support.skylum.com/presets/browsing-and-applying-presets) · [Copia de seguridad del catálogo](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-a-catalog)
- [Formatos admitidos](https://support.skylum.com/about-luminar-for-desktop/supported-file-types-and-cameras) · [Buenas prácticas con Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale)
- [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai) · [Añadir una carpeta](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/adding-a-folder-for-editing) · [Guardar los ajustes en el catálogo](https://support.skylum.com/saving-and-exporting-files/saving-adjustments-in-a-catalog) · [Registro de cambios](https://skylum.com/whats-new/luminar-neo/68)
- [Sunrays](https://support.skylum.com/editing-tools/landscape-tools/sunrays) · [Reconstruir una zona borrosa (Supersharp AI con máscara)](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- [Por qué cambian los colores al exportar (perfil del monitor)](https://support.skylum.com/why-do-photo-colors-change-after-export-in-luminar-for-desktop)

**Essentials**
- [Develop / Develop RAW](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- [Erase](https://support.skylum.com/editing-tools/essential-tools/erase)
- [Color](https://support.skylum.com/editing-tools/essential-tools/color)
- [Black & White](https://support.skylum.com/editing-tools/essential-tools/black-and-white)
- [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- [Denoise](https://support.skylum.com/editing-tools/essential-tools/denoise)
- [Vignette](https://support.skylum.com/editing-tools/essential-tools/vignette)

**Image Quality**
- [Noiseless AI](https://support.skylum.com/editing-tools/image-quality-tools/noiseless-ai)
- [Supersharp AI](https://support.skylum.com/editing-tools/image-quality-tools/supersharp-ai)

**Landscape**
- [Landscape Tools](https://support.skylum.com/editing-tools/landscape-tools) · [Landscape](https://support.skylum.com/editing-tools/landscape-tools/landscape)
- [Twilight Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/twilight-enhancer-ai)
- [Water Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/water-enhancer-ai)
- [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai)
- [Sky AI](https://support.skylum.com/editing-tools/landscape-tools/sky-ai)

**Creative**
- [Creative Tools](https://support.skylum.com/editing-tools/creative-tools)
- [Light Depth](https://support.skylum.com/editing-tools/creative-tools/light-depth) · [Magic Light AI](https://support.skylum.com/editing-tools/creative-tools/magic-light-ai) · [Color Transfer](https://support.skylum.com/editing-tools/creative-tools/color-transfer)
- [Film Grain](https://support.skylum.com/editing-tools/creative-tools/film-grain) · [Matte](https://support.skylum.com/editing-tools/creative-tools/matte) · [Toning](https://support.skylum.com/editing-tools/creative-tools/toning) · [Mood (LUT)](https://support.skylum.com/editing-tools/creative-tools/mood-lut)
- [Glow](https://support.skylum.com/editing-tools/creative-tools/glow) · [Mystical](https://support.skylum.com/editing-tools/creative-tools/mystical) · [Dramatic](https://support.skylum.com/editing-tools/creative-tools/dramatic)

**Portrait y Professional**
- [Portrait Tools](https://support.skylum.com/editing-tools/portrait-tools) · [Face AI](https://support.skylum.com/editing-tools/portrait-tools/face-ai)
- [Professional Tools](https://support.skylum.com/editing-tools/professional-tools)
- [Supercontrast](https://support.skylum.com/editing-tools/professional-tools/supercontrast) · [Color Harmony](https://support.skylum.com/editing-tools/professional-tools/color-harmony) · [Dodge & Burn](https://support.skylum.com/editing-tools/professional-tools/dodge-and-burn) · [Clone](https://support.skylum.com/editing-tools/professional-tools/clone)

**Máscaras y capas**
- [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai) · [Object Select AI](https://support.skylum.com/editing-tools/masking-options/object-select-ai)
- [Masking Options](https://support.skylum.com/editing-tools/masking-options) · [Brush Mask](https://support.skylum.com/editing-tools/masking-options/brush-mask) · [Radial Mask](https://support.skylum.com/editing-tools/masking-options/using-a-radial-mask) · [Linear Gradient Mask](https://support.skylum.com/editing-tools/masking-options/linear-gradient-mask)
- [Luminosity Masking](https://support.skylum.com/editing-tools/masking-options/luminosity-masking) · [Color Masking](https://support.skylum.com/editing-tools/masking-options/color-masking) · [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions)
- [Layers](https://support.skylum.com/editing-tools/layers) · [Layer Properties](https://support.skylum.com/editing-tools/layers/layer-properties) · [Añadir y quitar capas](https://support.skylum.com/editing-tools/layers/adding-and-removing-a-layer)

**Recorte y herramientas Extra**
- [Crop AI](https://support.skylum.com/editing-tools/crop-ai-tool)
- [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge) · [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching) · [Focus Stacking](https://support.skylum.com/extra-tools/focus-stacking) · [Upscale](https://support.skylum.com/extra-tools/upscale)
- [GenErase](https://support.skylum.com/extra-tools/generative-tools/generase) · [GenSwap](https://support.skylum.com/extra-tools/generative-tools/genswap) · [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand)

**Fuera de Luminar** (criterio de edición y programas de apilado; no son fuentes de Skylum)
- Color del cielo nocturno: [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky) · [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Cámara y Mac: [Guía de ayuda de la Sony a6700](https://helpguide.sony.net/ilc/2320/v1/es/index.html) · [fuentes de entrada del teclado en macOS](https://support.apple.com/es-es/guide/mac-help/mchlp1406/mac)
- Apilado en Mac: [Starry Landscape Stacker](https://sites.google.com/site/starrylandscapestacker/home) · [Siril](https://siril.org/) · [StarStaX](https://starstax.net/)
- Límites del JPEG: [posterización](https://www.cambridgeincolour.com/tutorials/posterization.htm) y [enfoque](https://www.cambridgeincolour.com/tutorials/image-sharpening.htm), en Cambridge in Colour
