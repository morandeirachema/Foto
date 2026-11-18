<!-- Archivo generado por pdf/generar-guia.sh a partir de retoques/. No lo edites a mano. -->

# Mejorar JPEG de safari, paisaje y fotografía nocturna con Luminar
### Guía paso a paso, de lo básico a lo avanzado

**Versión de la guía:** noviembre de 2026 · Luminar for Desktop 1.29.x (Luminar Neo) · macOS

## Cómo está organizada

**Parte I · Fundamentos**
1. Conceptos básicos
2. Luminar por dentro

**Parte II · El método**

3. El flujo base: 10 pasos
4. Herramientas avanzadas

**Parte III · Por tipo de foto**

5. Safari (fauna)
6. Paisaje
7. Fotografía nocturna

**Parte IV · Más allá de una foto**

8. Recetas completas *(provisional)*
9. Trabajar en serie
10. Varias fotos en una, ampliar y generar
11. Exportar
12. Ética, concursos y ubicación
13. Disparar mejores JPEG la próxima vez

**Parte V · Referencia**

14. Errores típicos y lista de comprobación
15. Atajos de teclado
16. Glosario
17. Preguntas frecuentes
18. Fuentes

## Cómo leerla

- **Pensada para JPEG, y es justo lo que tienes:** las fotos de Namibia salieron solo en JPEG por un error de configuración de la cámara. Todo lo de esta guía se aplica tal cual a ellas. Para que no se repita, mira la [configuración básica de la a6700](../manejo-a6700/04-configuracion-basica.md).

- Cada paso indica **qué hacer** en Luminar y **por qué**. Si entiendes el porqué, sabrás adaptarlo a cada foto.
- Cuando el texto dice "sección 4.3", se refiere al apartado 4.3 (el capítulo 4).
- Los **nombres de herramientas, controles y atajos** están comprobados con la documentación oficial de Skylum (sección 18). Se mantienen en inglés, como aparecen en el programa.
- Los **valores numéricos** son puntos de partida para JPEG propuestos por esta guía, no valores oficiales. Cada foto es distinta: mueve el deslizador mirando la imagen, no el número.
- Los atajos son de **macOS**. En Windows, **`⌘`** suele corresponder a **Ctrl** y **`⌥`** a **Alt**.

---

*Parte I · Fundamentos*

# 1. Conceptos básicos

Antes de mover un deslizador, conviene entender **qué estás tocando**. Si entiendes estos conceptos, sabrás qué herramienta de Luminar usar en cada caso.

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

**En JPEG, corrige poco.** La cámara ya ha aplicado un balance de blancos a los colores. Mover mucho la temperatura suele dar colores sucios. Si la dominante es fuerte, corrige un poco con Temperature y termina con **HSL** (sección 3, paso 7) o con **Color Harmony → Color Balance** (sección 4.3).

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
- **Un calibrador de pantalla** es muy recomendable si imprimes o vendes fotos.
- **Comprueba en el móvil.** Mucha gente verá tus fotos en un teléfono.

## 1.10. Color: lo mínimo de teoría

- **Tono (Hue):** qué color es.
- **Saturación (Saturation):** cuánto color tiene, de gris a intenso.
- **Luminancia (Luminance):** cómo de claro u oscuro es ese color.

**Colores complementarios:** **naranja ↔ azul**, **amarillo ↔ violeta**, **rojo ↔ cian**, **verde ↔ magenta**.
- **Contraste complementario:** un animal cálido (león, impala) sobre un fondo frío (cielo, sombra azulada) destaca de forma natural.
- **Corregir una dominante es empujar hacia su complementario:** un cielo nocturno naranja se corrige hacia el azul; unas sombras verdosas, hacia el magenta.

**Pocos colores, más armonía.** En safari, la paleta natural es de **ocres, dorados y verdes apagados**. Si un color se sale (un vehículo rojo, una camiseta fosforito), desaturarlo con una máscara limpia la foto sin borrar nada.

---

*Parte I · Fundamentos*

# 2. Luminar por dentro

## 2.1. Catálogo y edición

- **Catálogo** (**`L`**): aquí ves, seleccionas y organizas. Añades carpetas (**`⌥⇧N`**), creas álbumes (**`⌘N`**) y marcas favoritas.
- **Edición:** aquí ajustas una foto. A la derecha hay tres pestañas: **Presets** (**`T`**), **Tools** (**`E`**) e **Info** (**`I`**, datos de la toma).

**Categorías de Tools:**

| Categoría | Herramientas | Para qué |
|---|---|---|
| **Essentials** | Develop, Enhance AI, Erase, Structure AI, Color, Black & White, Details, Denoise, Vignette | Lo básico de cualquier foto |
| **Landscape** | Sky AI, Sunrays, Twilight Enhancer AI, Atmosphere AI, Landscape, Water Enhancer AI | Cielo, neblina, agua, vegetación |
| **Creative** | Light Depth, Color Transfer, Magic Light AI, Dramatic, Mood (LUT), Toning, Matte, Neon & Glow, Mystical, Glow, Blur, Film Grain | Ambiente y estilo |
| **Portrait** | Studio Light, Bokeh AI, Face AI, Skin AI, Body AI, High Key | Personas |
| **Professional** | Supercontrast, Color Harmony, Dodge & Burn, Clone | Control fino de tono y color |
| **Image Quality** | Noiseless AI, Supersharp AI | Ruido y desenfoque |

**Pestaña Extra:** **HDR Merge**, **Panorama Stitching** y **Focus Stacking** (en *Merge Tools*), **Upscale** (en *Enhancement tools*) y las herramientas generativas **GenErase**, **GenSwap** y **GenExpand** (sección 10).

> **Versiones y licencias.** Algunas herramientas tienen una versión *Improved*, que requiere Luminar for Desktop 1.29.0 o posterior y una licencia que la incluya; otras dependen de la suscripción. Si no encuentras una herramienta, consulta la documentación oficial (sección 18).

## 2.2. Edición no destructiva y copias virtuales

- Luminar **no modifica tus JPEG**: guarda los ajustes en su catálogo. Puedes volver a una foto meses después y cambiar cualquier ajuste.
- **Copia virtual** (**`⌘'`**): crea otra versión de la misma foto sin duplicar el archivo. Úsala para probar el blanco y negro, otro recorte (horizontal y vertical) o una edición más atrevida.
- **Compare** (**`;`**): muestra versiones lado a lado.
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

**La misma herramienta varias veces.** Según la documentación de Skylum, las herramientas se pueden añadir *en cualquier orden, varias veces y con máscaras distintas*. Así puedes tener un **Develop** sin máscara que corrige toda la foto y un **segundo Develop**, con máscara, que solo aclara el animal. En esta guía lo llamamos **segunda instancia**.

## 2.4. Capas

- **Añadir una capa:** el icono **+** del panel **Layers** abre *Add New Layer*, con estas opciones: **My Images** (otra foto tuya), **Flares**, **Light Leaks**, **Stardust Bokeh** y **Sparklers**.
- **Propiedades de la capa:** **Opacity**, **Blend Modes**, **Horizontal Flip**, **Vertical Flip** e **Image Mapping**. Cada capa tiene su pestaña **Masking** (Brush, Linear Gradient, Radial Gradient, Mask AI).
- **Background Removal AI:** separa el sujeto del fondo dentro de una capa.
- **Quitar u ocultar:** clic derecho → **Remove Layer** o **Hide Layer**.

Para la edición normal de un JPEG de viaje bastan las **herramientas con máscara**. Las capas sirven sobre todo para combinar imágenes, un uso que en fotos documentales conviene evitar (sección 12).

---

*Parte II · El método*

# 3. El flujo base: 10 pasos

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
- **Auto Straighten** nivela el horizonte automáticamente; el deslizador **Straighten** lo ajusta a mano.
- **Smart Compositions** (Crop AI Improved, según versión y licencia) propone varios recortes e indica la regla usada: tercios, proporción áurea, espiral áurea, triángulo áureo o centrado.
- **Proporciones** (desplegable de Ratio): Free, Original, Transposed, 1:1, 4:5, 2:3, 4:3, 5:7, 16:9, 16:10, 21:9, entre otras. **`X`** cambia entre horizontal y vertical.
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
- **Shadows y Highlights tienen un límite.** Si los llevas muy lejos en un JPEG, la foto se vuelve gris y plana. Si necesitas más, usa una máscara o las Curvas (sección 4.1).
- **Por qué:** primero colocas cada zona de brillo en su sitio; luego das contraste.

### Paso 5 · Color: balance de blancos

- **Develop → Color:** elige un preset de **White Balance**, haz clic con el cuentagotas (**`W`**) sobre algo neutro o ajusta **Temperature** y **Tint**.
- **Remove Color Cast** (en la herramienta **Color**) detecta y corrige una dominante automáticamente. Pruébalo y quédate con el resultado solo si te convence.
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
- **Comprobación:** al 100 %, mira un borde entre el sujeto y el cielo. Si ves una línea clara o un contorno, has enfocado de más.

### Paso 9 · Ajustes locales: máscaras

Repite **Develop** (u otra herramienta) y usa su pestaña **Masking** (sección 2.3).

**El esquema de tres zonas:**
1. **Sujeto:** un poco más claro, contrastado y nítido.
2. **Fondo** (la máscara del sujeto invertida con **`⌘I`**): un poco más oscuro, menos saturado y con menos textura.
3. **Bordes:** un poco más oscuros (**Vignette** o un **Gradient** en el borde que distrae).

- **Feather:** suaviza la transición. **`/`** para revisar la máscara.
- **Por qué:** dirigir la mirada es lo que separa una foto corregida de una foto buena.

### Paso 10 · Acabado, revisión y exportación

- **Erase** (**`⌘E`**): pintas sobre lo que quieres quitar y pulsas **Erase**. Luminar rellena la zona generando textura a partir de lo que la rodea. Con **Deselect** quitas partes de la selección; **`[`** y **`]`** cambian el tamaño del pincel.
- **Clone** (**`⌘J`**): cuando Erase no acierta, Clone copia píxeles de otra zona. **`⌥`**-clic elige el origen; **Radius**, **Softness** y **Opacity** controlan el pincel. Mejor muchos toques cortos con poca opacidad.
- **Vignette:** −10 a −20, si encaja. **Choose Subject** coloca el centro del viñeteado sobre el sujeto.
- **Film Grain:** **Amount** 5–10 si ves bandas en el cielo.
- **`\`** (mantener) para comparar con el original. Revisa al 100 %, descansa 5 minutos y **baja lo que sobre**.
- **Exportar** (**`⇧⌘E`**): sección 11.

**La regla del descanso.** Tras un rato mirando una foto, el ojo se acostumbra a la saturación y al contraste, y siempre parece que "falta un poco más". Por eso las fotos editadas de un tirón suelen verse exageradas al día siguiente. Descansa, vuelve a mirarlas y baja lo que sobre.

---

*Parte II · El método*

# 4. Herramientas avanzadas

No son imprescindibles, pero dan un control que las herramientas básicas no tienen.

## 4.1. Curves (dentro de Develop)

- **Eje horizontal:** el brillo **original**, de oscuro (izquierda) a claro (derecha).
- **Eje vertical:** el brillo **resultante**.
- **Línea recta en diagonal:** la foto sin cambios.
- **Subir** un punto aclara esa zona; **bajarlo** la oscurece. Luminar admite hasta **10 puntos**.
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

## 4.2. Supercontrast (Professional)

Controla el contraste por separado en tres zonas:
- **Highlights**, **Midtones** y **Shadows:** cuánto contraste hay en cada zona (a la derecha, más).
- **Highlights Balance**, **Midtones Balance** y **Shadows Balance:** dónde está el punto medio de cada zona, es decir, qué parte de la foto cuenta como luces, medios o sombras.

**Usos prácticos:**
- **Paisaje:** más contraste en los **Midtones** (roca, hierba) sin endurecer el cielo ni ensuciar las sombras.
- **Fauna:** dar cuerpo al pelaje (Midtones) sin quemar el cielo.
- **Noche:** contraste en **Highlights** (estrellas, Vía Láctea) sin tocar **Shadows**, donde está el ruido.

Empieza con **Midtones** +10/+20 y el resto en 0.

## 4.3. Color Harmony (Professional)

| Control | Qué hace | Uso típico |
|---|---|---|
| **Brilliance** | Colores más ricos | Alternativa suave a Saturation |
| **Warmth** | Positivo calienta; negativo enfría | Ajustar el ambiente tras el balance de blancos |
| **Color Contrast** (**Amount**, **Hue**) | Aumenta la diferencia **entre colores**, no entre luces y sombras | Separar un animal cálido de un fondo verde |
| **Split Color Warmth** (**Warm**, **Cool**) | **Warm:** a la izquierda neutraliza los tonos cálidos y a la derecha los realza. **Cool:** a la izquierda enfría azules y cianes y a la derecha los neutraliza | Arena más dorada sin cambiar el cielo |
| **Color Balance** | Para **Shadows**, **Midtones** o **Highlights**: Cyan–Red, Magenta–Green y Yellow–Blue | Quitar una dominante solo en una zona |

**El uso más útil en JPEG:** **Color Balance** para corregir una dominante **solo en una zona de brillo**. Por ejemplo, si el cielo nocturno está bien pero las sombras son verdosas, en **Shadows** mueve Magenta–Green un poco hacia el magenta.

## 4.4. Dodge & Burn (Professional)

La técnica clásica de laboratorio: **aclarar** y **oscurecer** pintando.

- **Lighten:** aclara. **Darken:** oscurece. **Erase:** borra trazos equivocados.
- **Brush Size** (**`[`**, **`]`**), **Softness** (**`⇧[`**, **`⇧]`**) y **Strength** (intensidad de cada trazo).
- **Overall Amount:** intensidad global de todo lo pintado.

**Cómo usarlo:**
- **Lighten** con poca **Strength** sobre lo que debe destacar: el ojo, la cresta de una duna, la luz en una nube.
- **Darken** sobre lo que distrae: una rama clara, un borde brillante.
- **Muchas pasadas suaves** mejor que una fuerte. Al final, ajusta **Overall Amount**.

**Ejercicio:** en una foto de dunas, aclara las caras iluminadas y oscurece las caras en sombra. Verás aparecer el volumen.

## 4.5. Light Depth (Creative)

Usa un **mapa de profundidad** calculado por IA para iluminar de forma distinta lo cercano y lo lejano, como un foco suave colocado en la escena. Sustituye a la antigua herramienta Relight AI.

- **Amount:** intensidad general.
- **Depth Mask:** dónde cae el centro de la luz según la profundidad.
- **Softness:** cómo de gradual es el paso de la luz a la sombra.
- **Warmth:** temperatura de la luz.
- **Brightness Near / Warmth Near:** brillo y temperatura del **primer plano**.
- **Brightness Far / Warmth Far:** brillo y temperatura del **fondo**.

**Perspectiva atmosférica.** Lo cercano parece más claro, contrastado y cálido; lo lejano, más suave y frío. Para reforzarla: **Brightness Near** un poco arriba, **Warmth Near** un poco cálido y **Warmth Far** un poco frío. Con valores pequeños.

## 4.6. Black & White (Essentials)

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

## 4.7. Herramientas de Landscape

| Herramienta | Qué hace | Cuándo |
|---|---|---|
| **Landscape** | **Dehaze** (quita neblina ajustando a la vez contraste, claridad y color), **Golden Hour** (calidez y brillo dorado), **Foliage Enhancer** y **Foliage Hue** (vegetación más viva y su tono) | Calima, vegetación apagada |
| **Water Enhancer AI** | Agua más clara y viva: **Amount**, **Blue**, **Green**, **Original Color**, **Brightness**, **Contrast**, **Depth** y un pincel (**Draw**, **Erase**, **Restore**) para elegir la zona | Ríos, lagos, mar |
| **Twilight Enhancer AI** | Luz y color de hora azul u hora dorada. Presets **Blush**, **Golden**, **Blue**, **Emerald** y **Mauve**, con ajustes de **Sky**, **Dawn**, **Scene Enhancements** y **Water Reflection** | Fotos de crepúsculo o con poca luz |
| **Sky AI** | Sustituye el cielo | Solo fotos creativas (sección 12) |
| **Atmosphere AI** | **Añade** niebla, bruma o neblina (Fog, Layered Fog, Mist, Haze o, en la versión Improved, Ground Fog, Wispy Fog y Heavy Fog) | Solo fotos creativas: añade algo que no estaba |

> **Precaución:** **Dawn** (en Twilight Enhancer AI), **Sky AI** y **Atmosphere AI** añaden luz, cielo o niebla que no existían. En fotos documentales, evítalos o úsalos de forma muy sutil y dilo al compartir la foto.

## 4.8. Herramientas creativas

| Herramienta | Qué hace | Precaución |
|---|---|---|
| **Film Grain** | Grano: **Amount**, **Size**, **Roughness** | **Amount** bajo. Disimula las bandas |
| **Matte** | Aspecto suave y envejecido: **Amount**, **Fade** (resta detalle en las zonas oscuras), **Contrast**, **Vividness** y tonalidad de color | Quita profundidad a los negros |
| **Toning** | Tiñe por separado luces y sombras: **Highlights/Shadows Saturation** y **Hue**, y **Balance** | Sutil; también útil en blanco y negro |
| **Mood (LUT)** | Aplica una tabla LUT (incluidas o tuyas en formato **.cube**) con **Amount**, **Contrast** y **Saturation** | Baja **Amount** para un efecto suave |
| **Glow** | Brillo suave: tipos **Soft Focus**, **Glow**, **Orton Effect** y **Orton Effect Soft** | Ablanda la imagen; usa una máscara para proteger el sujeto |
| **Mystical** | Brillo etéreo: suaviza la luminosidad y sube contraste y saturación | Según Skylum, por debajo de 40 da un resultado más realista |
| **Dramatic** | Aspecto áspero y cinematográfico: reduce saturación y contraste, al estilo del *bleach bypass* | Estético, no correctivo |
| **Magic Light AI** | Destellos y rayos en fuentes de luz artificiales: **Intensity**, **Size**, **Beam Width**, **Glow**, **Clearness**, **Number of Beams** | Solo bombillas y farolas, muy suave |
| **Color Transfer** | Aplica la paleta de color de una foto de referencia | No funciona con fotos en blanco y negro |

---

*Parte III · Por tipo de foto*

# 5. Safari (fauna)

## 5.1. Problemas típicos

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

## 5.2. Paso a paso

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
- Si recortas mucho, piensa en **Upscale** al final (sección 10.4).
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
| **Seleccionar el animal** | Develop (segunda instancia) → Masking → **Object Select AI** → clic sobre el animal → **Feather** | — |
| **Animal más presente** | Con esa máscara | Exposure +0,2/+0,3; Smart Contrast +10 |
| **Textura del pelo** | **Structure AI** con la misma máscara (**Copy**/**Paste** de la máscara) | +15/+25 |
| **Fondo más discreto** | Otra instancia con la máscara invertida (**`⌘I`**) | Exposure −0,2; Saturation −10 |
| **Ojo con brillo** | **Dodge & Burn → Lighten**, pincel pequeño, poca **Strength** | Solo el iris |

**El ojo, en detalle:**
- Aclara **solo el iris**, no todo el ojo.
- **Brillo del ojo:** si existe, no lo agrandes. Si no existe, **no lo pintes**: en fotografía de naturaleza se considera manipulación.
- Comprueba al 100 % que el ojo no parece de cristal.

**8. Limpieza**
- **Remove Dust Spots** quita automáticamente las manchas de polvo del sensor o del objetivo. Después puedes afinar con **Erase**. El polvo del sensor aparece **en el mismo sitio** en varias fotos: revisa toda la serie.
- **Erase** para motas, ramitas o insectos pequeños que distraigan.
- **Importante:** en una foto documental, **no borres elementos de la escena** (otros animales, vehículos, collares de seguimiento) ni uses herramientas generativas (sección 12).

**9. Acabado**
- **Vignette** −10 a −15 si el fondo es claro en los bordes; **Choose Subject** para centrarlo en el animal.
- **Upscale** solo si has recortado mucho, y siempre al final.

## 5.3. Casos concretos

**Animal a contraluz:**
- Decide: ¿silueta o detalle? Para una **silueta**, baja **Blacks** y deja el animal oscuro; resalta el borde de luz con **Highlights**.
- Para ver **detalle**, máscara del animal con Exposure +0,4/+0,6, y antes **Noiseless AI** (esa zona tendrá ruido).

**Mediodía con luz dura:**
- Shadows +30/+40 y Highlights −30.
- **Structure AI** moderado: la luz dura ya tiene mucho contraste.
- El **blanco y negro** suele funcionar muy bien (sección 4.6).

**Amanecer y atardecer:**
- Conserva la calidez. Casi siempre hará falta Noiseless AI.
- **Light Depth** (opcional) para reforzar la dirección de la luz.

**Pájaros en vuelo contra el cielo:**
- Exposure para el pájaro. Con **Mask AI → cielo**, Exposure −0,2 para que el cielo no quede blanco.
- **Details** con **Details Masking** alto para no enfocar el cielo.

**Plumas blancas (garzas, pelícanos, águilas pescadoras):**
- El blanco se quema enseguida. Con **`J`**, baja **Whites** y **Highlights** hasta que el plumaje recupere textura. Si ya está quemado, no hay nada que hacer.
- **No subas la exposición de toda la foto.** Aclara el resto con la máscara del pájaro invertida.
- Las plumas blancas **en sombra** son un buen punto neutro para el cuentagotas.

**Animales oscuros (búfalo, gorila, cuervo):**
- Un búfalo tiene que ser oscuro: no lo aclares de más.
- Para ver detalle, máscara del animal con Shadows +20 y Structure AI +15. Vigila el ruido.

**Cebras:**
- Las rayas blancas se queman y las negras se empastan: Highlights −30 y Blacks un poco arriba.
- Structure AI bajo: las rayas ya tienen todo el contraste que necesitan.

**Leopardo en un árbol (luz moteada):**
- **Dodge & Burn → Darken** sobre las manchas de luz en las ramas; **Lighten** suave en la cara del leopardo.
- **Mask AI → cielo** (los huecos entre las ramas) con Exposure −0,3 para que no distraigan.

**Elefantes y rinocerontes:**
- **Structure AI** +20/+30 y **Medium Details**: la textura de la piel es su mayor atractivo.
- Si están cubiertos de barro rojizo, no lo "corrijas": es parte de la escena.

**Polvo levantado por los animales:**
- Es atmósfera, sobre todo a contraluz. No uses **Dehaze**: lo eliminaría.

**Foto desde el vehículo con el animal muy lejos:**
- Recorte fuerte + **Upscale** al final.
- Expectativas realistas: servirá de recuerdo o para la pantalla del móvil, no para imprimir grande.

---

*Parte III · Por tipo de foto*

# 6. Paisaje

## 6.1. Problemas típicos

| Problema | Por qué ocurre |
|---|---|
| **Cielo quemado, suelo oscuro** | El cielo es mucho más brillante que el suelo |
| **Horizonte torcido** | Fotos rápidas a mano |
| **Foto plana y sin profundidad** | Calima, luz de mediodía |
| **Colores apagados o exagerados** | Ajustes de la cámara |
| **Bandas en el cielo** | Degradados suaves en un JPEG de 8 bits |
| **Distorsión y esquinas oscuras** | Gran angular, sobre todo en móviles |

## 6.2. Paso a paso

**1. Horizonte y encuadre**
- **`C`** → **Auto Straighten**.
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
  - **Cielo:** Develop (segunda instancia) → Masking → **Mask AI → cielo** → Exposure −0,2/−0,4. O un **Gradient** (**`G`**) de arriba abajo.
  - **Suelo:** **Gradient** desde abajo → Exposure +0,2; Shadows +15.
- **¿Mask AI o Gradient?** **Mask AI** respeta las formas (montañas, árboles). El **Gradient** es más natural con horizontes rectos (mar, sabana plana) y no deja bordes raros alrededor de los árboles.
- **Luminosity Masking** es otra opción: selecciona solo las zonas más claras (el cielo) por su brillo.

**4. Profundidad**
- **Landscape → Dehaze** +10 a +20 si hay calima. Más oscurece y satura.
- **Light Depth:** primer plano un poco más claro y cálido; fondo algo más frío (sección 4.5).
- **Perspectiva atmosférica:** lo cercano es más contrastado, cálido y saturado; lo lejano, más claro, frío y suave. Reforzar esa diferencia da profundidad.
- **Error frecuente:** un Dehaze fuerte en toda la foto **elimina** esa perspectiva. Mejor un Dehaze suave, o con máscara solo donde haga falta.

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
- **Supercontrast → Midtones** +10/+20 como alternativa más limpia (sección 4.2).
- **Dunas y roca:** algo más de Structure AI, y Light Depth para marcar las crestas.

**7. Acabado**
- **Vignette** muy suave (−10).
- **Film Grain** con **Amount** bajo si el cielo muestra bandas.

## 6.3. Casos concretos

**Desierto y dunas:**
- La cámara suele **subexponer** la arena clara: Exposure +0,3/+0,5.
- Highlights −20 para no perder la textura de la arena.
- La luz rasante marca las ondas: refuérzala con **Structure AI** y **Dodge & Burn**.
- **Color Harmony → Split Color Warmth → Warm** a la derecha: arena más dorada sin tocar el cielo azul.

**Atardecer:**
- No neutralices el color. Como mucho, Temperature un poco más fría si el naranja es exagerado.
- **Sky Enhancer AI** bajo, o **Color Harmony → Warmth** suave.
- **Twilight Enhancer AI** (preset **Golden** o **Blush**) es otra opción, con **Amount** bajo. Revisa que no añada luz que no había.
- Siluetas de árboles: **Blacks** abajo, para que sean negras de verdad.
- **El sol** casi siempre estará quemado, y es normal. Lo que importa es que el halo de alrededor tenga degradado y no un borde duro.

**Sabana con cielo de tormenta:**
- **Mask AI → cielo:** Exposure −0,3 y Structure AI +15 (las nubes sí agradecen textura).
- **Suelo:** **Gradient** con Exposure +0,2. El atractivo está en el contraste entre el cielo oscuro y el suelo iluminado.

**Montaña:**
- Las montañas lejanas suelen salir azuladas y planas por la atmósfera. **Dehaze** suave con **Mask AI → montañas** les devuelve el relieve.
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
- **Twilight Enhancer AI**, preset **Blue**, con **Amount** bajo, si quieres reforzarlo.

**Cambiar el cielo (Sky AI):** técnicamente es fácil, pero en una foto documental o de viaje **convierte la foto en un montaje**. Úsalo solo en fotos creativas y dilo si las compartes.

---

*Parte III · Por tipo de foto*

# 7. Fotografía nocturna

## 7.1. Antes de empezar

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

## 7.2. Cielo estrellado y Vía Láctea

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
- Develop (segunda instancia) con máscara **Radial** (**`R`**) o **Brush** (**`B`**) sobre el núcleo: Exposure +0,2 y Smart Contrast +15.
- **Structure AI** +10/+20 con la misma máscara (**Copy**/**Paste** de la máscara).
- **Supercontrast → Highlights** con la misma máscara: realza las nubes de estrellas sin tocar el fondo.
- **Landscape → Dehaze** con la misma máscara, suave: aumenta el contraste de las nubes de estrellas.
- **Por qué en local:** si subes el contraste en todo el cielo, sube también el ruido del fondo.

**5. Contaminación lumínica en el horizonte**
- **Gradient** desde el horizonte hacia arriba: Exposure −0,2 y Temperature un poco hacia el azul.
- Si el resplandor es fuerte, **no intentes eliminarlo**: déjalo como un degradado cálido suave. Si lo quitas del todo, queda una banda gris sucia.

**6. Primer plano**
- Suele estar muy oscuro: **Mask AI → cielo**, invertida (**`⌘I`**), con Exposure +0,3/+0,5.
- **No lo aclares demasiado.** Una silueta oscura o un primer plano tenue es más creíble que uno iluminado como de día.
- **De noche, la máscara de cielo puede fallar** porque el límite entre cielo y suelo apenas se ve. Revísala con **`/`** y corrígela con **Brush**, o usa un **Gradient** en el horizonte.

**7. Acabado**
- **Details** muy bajo y **Details Masking** alto: el enfoque fuerte convierte el ruido en estrellas falsas.
- **Vignette** suave.
- Revisa al 100 %: bandas en el cielo, halos en el horizonte, estrellas convertidas en manchas.

**Estrellas alargadas (pequeños trazos):** salen cuando la exposición fue demasiado larga para la focal usada. No tienen arreglo real al editar. Para la próxima vez, consulta la sección 13.3.

## 7.3. Luces artificiales (lodge, campamento, ciudad)

- **Balance de blancos:** no neutralices del todo las bombillas cálidas. Algo de calidez hace la escena acogedora.
- **Highlights** −30/−50 para recuperar las luces. Si las bombillas están quemadas, déjalas: es normal.
- **Noiseless AI** casi siempre.
- **Magic Light AI** (opcional y muy suave) añade rayos y brillo a bombillas y farolas.
- **HSL:** baja la saturación del naranja si la luz es demasiado intensa.
- **Luces de distintos colores:** neutraliza la que más se vea y deja la otra con su color.

## 7.4. Fuego de campamento y linternas

- **Decide el color.** La luz del fuego es muy naranja. Corrige un poco (Temperature un poco más fría), pero **no la vuelvas blanca**: el fuego tiene que seguir pareciendo fuego.
- **Shadows** +20 para ver las caras; **Highlights** −40 para que la llama tenga forma.
- Si hay personas, **Mask AI → personas** con un Develop suave, o **Face AI → Face Light**.
- **Vignette** algo más marcada (−20) para concentrar la luz en el fuego.
- **No enfoques las llamas ni las chispas**: el enfoque convierte su movimiento en ruido.

## 7.5. Luna

- **Luna sola, con teleobjetivo:** baja **Highlights** y **Exposure** hasta ver los cráteres; **Structure AI** +20 y **Details** moderado. Fondo negro (**Blacks** abajo).
- **Luna en un paisaje:** en un JPEG suele estar quemada, porque es mucho más brillante que el paisaje. Si lo está, **no se puede recuperar**: acepta un punto blanco o hazle una foto aparte.
- **Añadir una luna de otra foto** (**Layers → + → My Images**) es un montaje: hazlo solo en fotos creativas y dilo al compartirla (sección 12).

## 7.6. Hora azul y crepúsculo

El mejor momento para la "foto nocturna" con JPEG suele ser **antes** de la noche cerrada, cuando el cielo aún tiene luz azul y el ruido es mucho menor.
- Balance de blancos: deja el azul.
- **Highlights** abajo en las luces artificiales; **Shadows** suaves.
- Ruido: a menudo basta con **Denoise** suave.
- **Twilight Enhancer AI** (preset **Blue**) puede reforzar el ambiente, con **Amount** bajo.

---

*Parte IV · Más allá de una foto*

# 8. Recetas completas

> ⚠️ **Provisional.** Estas recetas combinan los pasos de la guía para cinco situaciones típicas, pero **todavía no se han probado con fotos reales**. Los valores son puntos de partida. Se revisarán con fotos de muestra. Mira siempre la imagen, no el número.

## 8.1. León al amanecer, con luz cálida y algo de ruido

*Situación: ISO alto, teleobjetivo, el león mira a la izquierda, fondo de hierba seca desenfocada.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Noiseless AI | Nivel propuesto; Details con cuidado |
| 2 | Crop | Espacio a la izquierda; el ojo en un punto fuerte de los tercios |
| 3 | Develop | Exposure +0,2; Highlights −25; Shadows +20; Whites/Blacks con `J`; Smart Contrast +10 |
| 4 | Develop → Color | Sin tocar la temperatura: la calidez es real |
| 5 | Enhance AI | Accent AI +20 |
| 6 | Color → HSL | Amarillo: Saturation −10; naranja: Luminance +5 |
| 7 | Develop (2.ª instancia) + Object Select AI del león | Exposure +0,2; Smart Contrast +10 |
| 8 | Structure AI, misma máscara | +20 |
| 9 | Develop (3.ª instancia), máscara invertida | Exposure −0,15; Saturation −10 |
| 10 | Dodge & Burn → Lighten | Iris, con poca Strength |
| 11 | Vignette + Choose Subject | Amount −12 |

## 8.2. Elefante a mediodía, en blanco y negro

*Situación: luz cenital, sombras negras bajo la cabeza, cielo blanquecino.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Crop | Elefante entero o cortado a media pata, nunca por las rodillas |
| 2 | Develop | Highlights −40; Shadows +35; Blacks −10 |
| 3 | Black & White | Convert to B&W; Luminance: Blue −40, Yellow −10 |
| 4 | Develop → Curves | S marcada |
| 5 | Structure AI + Object Select AI del elefante | +30 |
| 6 | Develop (2.ª instancia) + Mask AI → cielo | Exposure −0,3 |
| 7 | Dodge & Burn | Lighten en las arrugas iluminadas; Darken en el suelo |
| 8 | Vignette | Amount −15 |

## 8.3. Dunas al atardecer

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

## 8.4. Vía Láctea sobre una acacia

*Situación: ISO 6400, 20 s, gran angular, cielo anaranjado por un pueblo lejano.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Noiseless AI | Middle; Color Denoise alto; Luminosity Denoise bajado hasta ver las estrellas pequeñas |
| 2 | Crop | Horizonte en el tercio inferior; acacia fuera del centro |
| 3 | Develop → Color | Temperature hacia el azul; Tint hacia el magenta hasta un cielo gris azulado |
| 4 | Develop | Exposure +0,4; Blacks −10; Shadows +5 |
| 5 | Develop (2.ª instancia) + Radial sobre el núcleo | Exposure +0,2; Smart Contrast +15 |
| 6 | Supercontrast, misma máscara | Highlights +15 |
| 7 | Develop (3.ª instancia) + Gradient desde el horizonte | Exposure −0,2; Temperature un poco más fría |
| 8 | Develop (4.ª instancia) + Mask AI → cielo invertida | Exposure +0,3, con contención |
| 9 | Details | Muy bajo; Details Masking alto |
| 10 | Vignette | Amount −10 |

## 8.5. Cena alrededor del fuego

*Situación: ISO alto, caras naranjas, fondo negro, llamas quemadas.*

| Orden | Herramienta | Ajuste |
|---|---|---|
| 1 | Noiseless AI | Nivel propuesto (probablemente High) |
| 2 | Develop → Color | Temperature un poco más fría, sin perder el naranja |
| 3 | Develop | Highlights −40; Shadows +20; Blacks −5 |
| 4 | Color → HSL | Naranja: Saturation −10 |
| 5 | Develop (2.ª instancia) + Mask AI → personas | Exposure +0,15 |
| 6 | Vignette | Amount −20 |

---

*Parte IV · Más allá de una foto*

# 9. Trabajar en serie

Tras un safari puedes volver con miles de fotos. Editarlas una a una es inviable.

## 9.1. Sincronizar ajustes (Sync Adjustments)

1. Edita bien **una foto representativa** de una situación (misma luz, mismo animal).
2. Con ella seleccionada (borde naranja), selecciona las demás en el catálogo o en la tira de fotos (**Filmstrip**): **`⇧`**-clic para un rango, **`⌘`**-clic para fotos sueltas. Las demás aparecen con borde blanco.
3. Clic derecho → **Adjustments → Sync Adjustments** (**`⇧⌘S`**).
4. Revisa cada foto y retoca lo que cambie, sobre todo la exposición.

**Copiar y pegar ajustes:** **`⌘C`** en la foto editada y **`⌘V`** en la otra.

**Qué tener en cuenta:**
- Según Skylum, las herramientas de IA (Accent AI, Structure AI, Skin AI) se sincronizan de forma más fiable entre fotos distintas.
- **Crop**, **Erase** y **Background Removal** **no se sincronizan**: hay que hacerlos foto a foto.
- **Revisa las máscaras** en cada foto sincronizada: el animal no estará en el mismo sitio en todas.
- Las miniaturas del catálogo son previsualizaciones: revisa el resultado en la vista de una sola foto.

## 9.2. Presets propios

1. Ajusta una foto (o modifica un preset existente).
2. En el desplegable **Actions**, abajo, elige **Save as Preset**.
3. El preset se guarda en la pestaña **My Presets**, donde puedes renombrarlo. Su menú permite **Edit**, **Rename**, **Delete** y **Show in Finder**.

**Consejos:**
- Crea presets **de base**, no de "look". Por ejemplo, "Safari amanecer ISO alto" (Noiseless AI, Accent AI suave) o "Noche estrellada" (Noiseless AI, Blacks abajo, Details bajo).
- Un preset es un **punto de partida**: aplícalo y ajusta.
- **Crop AI** no se guarda en los presets.

## 9.3. Coherencia en una serie

Una serie de fotos de viaje se ve profesional cuando las fotos **parecen de la misma familia**:
- **Mismo balance de blancos** para la misma situación de luz.
- **Misma intensidad** de saturación y contraste.
- **Mismo tratamiento de los negros**: todos profundos o todos levantados.
- Si mezclas color y blanco y negro, **agrupa**: un bloque de blanco y negro, no fotos sueltas.
- **Color Transfer** puede igualar la paleta de una foto con la de otra (no funciona con fotos en blanco y negro).

**Truco:** mira todas las fotos del álbum juntas en el catálogo. La que "salta" por más saturada, más oscura o de otro color es la que hay que corregir.

---

*Parte IV · Más allá de una foto*

# 10. Varias fotos en una, ampliar y generar

Estas herramientas están en la pestaña **Extra**. La documentación de Skylum no detalla qué formatos de entrada admite cada una. Con RAW hay más margen, pero puedes probar con tus JPEG.

## 10.1. HDR Merge

**Qué es:** combina varias fotos de la misma escena con exposiciones distintas (una oscura para el cielo, una clara para el suelo) en una sola imagen con todo el rango.

- **Dónde:** Extra → **Merge Tools** → **HDR Merge**.
- **Cómo:** arrastra las fotos horquilladas a HDR Merge, ajusta las opciones (icono de tres puntos) y pulsa **Continue**.
- **Opciones:**
  - **Auto Alignment:** alinea las tomas si disparaste a mano.
  - **Ghost Reduction:** corrige lo que se movió entre tomas (hierba, agua, personas). Eliges la foto de referencia y la intensidad.
  - **Chromatic Aberration Reduction:** quita los bordes de color.
- **Resultado:** un **TIFF** en la carpeta HDR, que luego editas como cualquier foto. El aspecto "HDR" exagerado viene de la edición posterior, no de la fusión: edita con suavidad.
- **Con fauna, casi nunca:** los animales se mueven entre una toma y otra.

## 10.2. Panorama Stitching

**Qué es:** une varias fotos de la misma escena tomadas girando la cámara.

- **Cómo:** selecciona las fotos, arrástralas a **Panorama Stitching**, ajusta las opciones (distorsión, viñeteado, aberración cromática, fantasmas) y pulsa **Start**.
- **Proyecciones:** **Spherical**, **Cylinder**, **Mercator**, **Plane** y **Fisheye**.
- **Tamaño máximo de exportación:** 15.000 px.
- **Después:** recorta a mano los bordes irregulares.
- **Consejos de toma de Skylum:** mantén constantes la luz y la exposición (exposición y balance de blancos en manual), bloquea el enfoque, gira con suavidad y, si puedes, usa trípode.

## 10.3. Focus Stacking

**Qué es:** une **hasta 100 fotos** con distinto punto de enfoque para que toda la escena salga nítida (por ejemplo, un paisaje con una flor muy cerca).

- **Dónde:** Extra → **Merge Tools** → **Focus Stacking**.
- **Cómo:** selecciona las fotos en el catálogo y arrástralas a Focus Stacking. El icono del engranaje activa **Auto Alignment** y **Chromatic Aberration Reduction**. Pulsa **Stack**.
- **Resultado:** un **TIFF** en la carpeta Focus Stacking.
- Lo ideal es disparar con trípode.

## 10.4. Upscale

**Qué es:** aumenta la resolución con IA, **hasta 6×**.

- **Dónde:** Extra → **Enhancement tools** → **Upscale**.
- **Límites:** entrada mínima de 257 × 257 px; entrada máxima de 16.000 px en el lado largo; salida máxima de 32.000 px en el lado largo.
- **Cuándo usarlo:** **al final**, después de todos los ajustes, y solo si lo necesitas (un recorte fuerte que quieres imprimir o ver en grande).
- **Revisa al 100 %:** en pelo y plumas puede inventar textura.

## 10.5. Herramientas generativas: GenErase, GenSwap y GenExpand

Generan con IA contenido que **no estaba** en la foto.

- **GenExpand** amplía el lienzo **hasta un 25 %** y rellena el espacio nuevo. Skylum recomienda ampliaciones pequeñas (en torno al 10 %), de un lado cada vez. El resultado se guarda como **TIF**. La versión *Regular* admite una descripción en texto (en inglés funciona mejor) y necesita conexión a internet; la versión *Improved* no necesita texto.
- **GenErase** y **GenSwap** borran o sustituyen elementos generando contenido nuevo.

> En fotos documentales, de naturaleza o de concurso, estas herramientas **convierten la foto en una ilustración** (sección 12).

---

*Parte IV · Más allá de una foto*

# 11. Exportar

## 11.1. El cuadro de exportación

**Export** (**`⇧⌘E`**) ofrece:
- **Formatos:** JPEG, PNG, TIFF, JPEG 2000, Photoshop (PSD, **sin capas**), PDF y DNG.
- **Quality**, **Sharpen** y **Color Space:** las opciones disponibles dependen del formato.
- **Resize:** tamaño original, **Long Edge** (lado largo), **Short Edge** (lado corto) o **Dimensions** (ancho y alto), además de **Resolution**.
- **Signature:** firma o marca de agua (imagen o texto). Se aplica solo al archivo exportado.

Luminar **recuerda la configuración** de la última exportación. Revísala antes de cada uso.

## 11.2. Ajustes recomendados por uso

*Recomendaciones de esta guía, no de Skylum.*

| Uso | Formato | Tamaño | Calidad | Sharpen |
|---|---|---|---|---|
| **Archivo personal** | JPEG | Original | Máxima o casi | No |
| **Redes sociales, mensajería** | JPEG | Long Edge de unos 2.000 px | Alta | Bajo |
| **Pantalla grande o TV 4K** | JPEG | Long Edge de 3.840 px | Alta | Bajo |
| **Imprimir** | TIFF o JPEG a máxima calidad | Según el tamaño de la copia (11.3) | Máxima | Moderado |
| **Seguir editando en otro programa** | TIFF | Original | — | No |

- **Redes sociales:** cada red cambia a menudo sus tamaños recomendados. Consulta el actual antes de exportar.
- **Espacio de color:** para pantallas y web, **sRGB**, que es el estándar. Un espacio más amplio no recupera colores que el JPEG original no tiene, y algunas aplicaciones y webs pueden mostrarlo con los colores apagados. Para imprimir, usa el que te pida el laboratorio.

## 11.3. Imprimir

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

## 11.4. Nombres de archivo

Una convención sencilla ahorra búsquedas: `AAAA-MM-DD_lugar_tema_numero.jpg`. Por ejemplo, `2026-08-14_masai-mara_leon_01.jpg`. Guarda las exportaciones en una carpeta distinta de la de los originales.

---

*Parte IV · Más allá de una foto*

# 12. Ética, concursos y ubicación

## 12.1. Corregir no es cambiar la escena

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

## 12.2. Herramientas que crean contenido

**GenErase**, **GenSwap**, **GenExpand**, **Sky AI**, **Atmosphere AI** y la luz **Dawn** de **Twilight Enhancer AI** añaden o inventan elementos. Son útiles en fotos creativas, pero:
- Convierten una foto documental en una ilustración.
- Suelen estar prohibidas en concursos de naturaleza y en fotoperiodismo.
- Si compartes una foto con contenido generado o sustituido, **dilo**.

## 12.3. Ubicación GPS y fauna amenazada

Muchas cámaras y todos los móviles guardan la **ubicación GPS** en el archivo. Para especies amenazadas (rinocerontes, pangolines, grandes felinos, aves en el nido), publicar la ubicación exacta puede ayudar a los cazadores furtivos.

- **Antes de publicar** fotos de especies amenazadas, **quita la ubicación** del archivo exportado. La documentación de exportación de Skylum no menciona una opción para quitar metadatos. En macOS, puedes hacerlo en **Vista Previa**: menú Herramientas → Mostrar inspector → pestaña de ubicación → Eliminar información de ubicación.
- **No des la ubicación exacta en el texto** ("cerca del lodge X, junto al río Y").

## 12.4. Personas

- Pide permiso para fotografiar a personas, sobre todo a niños y en comunidades locales.
- No alteres el tono de piel de nadie más allá de corregir la luz.

---

*Parte IV · Más allá de una foto*

# 13. Disparar mejores JPEG la próxima vez

La mejor edición empieza en la cámara. Si disparas en JPEG, estos ajustes amplían el margen para editar en Luminar.

> ⚠️ **Lo primero, con la a6700: que dispare en RAW.** En Namibia todas las fotos salieron solo en JPEG por un error de configuración. Comprueba `Formato archivo` = **RAW** (también después de cargar cada memoria) y que tus archivos sean **`.ARW`**: [configuración básica](../manejo-a6700/04-configuracion-basica.md). Los ajustes de esta página son para cuando, por lo que sea, solo tengas JPEG.

> Los nombres de los menús cambian según la marca. Consulta el manual de tu cámara. Con la **Sony a6700**, la configuración completa, con las rutas de menú verificadas, está en [Manejo de la a6700](../manejo-a6700/README.md).

## 13.1. Ajustes de la cámara

| Ajuste | Recomendación | Por qué |
|---|---|---|
| **Calidad JPEG** | La máxima y el tamaño más grande | Menos compresión, menos bandas |
| **Estilo de imagen** (Picture Style en Canon, Picture Control en Nikon, Creative Look o Creative Style en Sony) | **Neutro** o **Estándar** con algo menos de contraste | Deja más detalle en luces y sombras para editar |
| **Nitidez en cámara** | Algo por debajo del valor estándar | Es más fácil añadir nitidez al editar que quitar la que sobra |
| **Reducción de ruido en cámara** | Baja | La reducción de ruido de la cámara puede borrar detalle que luego no se recupera |
| **Balance de blancos** | Uno fijo (por ejemplo, "Luz de día") para atardeceres | El automático tiende a "corregir" y apagar los colores del atardecer |
| **Espacio de color** | sRGB, si no tienes un motivo para usar otro | Es el estándar de pantallas y web |
| **RAW + JPEG** | Si la tarjeta y la cámara lo permiten | El RAW es el seguro para las fotos importantes |

## 13.2. Al disparar

- **Protege las luces.** En JPEG, las luces quemadas no se recuperan y las sombras sí se pueden abrir un poco. Si dudas, usa algo de compensación de exposición negativa.
- **Activa el aviso de sobreexposición** en la pantalla de la cámara.
- **Fauna:** prioriza una velocidad de obturación alta. Un poco de ruido tiene arreglo; una foto movida, no.
- **Desde el vehículo:** apoya el objetivo y pide que apaguen el motor si es posible: la vibración mueve la foto.
- **Polvo:** cambia de objetivo lo menos posible y con la cámara hacia abajo.

## 13.3. Noche: estrellas nítidas

- **Trípode** y disparo retardado o con mando a distancia.
- **Enfoque manual** sobre una estrella brillante, con la imagen ampliada en la pantalla.
- **Diafragma** lo más abierto posible.
- **Tiempo máximo sin trazos, regla del 500 (aproximada):** 500 ÷ (focal × factor de recorte) = segundos. Por ejemplo, con 14 mm en *full frame*: 500 ÷ 14 ≈ 36 s; en APS-C (×1,5): 500 ÷ 21 ≈ 24 s. Con sensores de muchos megapíxeles, conviene un tiempo más corto.
- **Balance de blancos fijo:** evita que cada foto salga con un color distinto.
- **Varias tomas iguales seguidas:** te permiten apilarlas después para reducir el ruido (sección 7.2).
- **Evita la luna llena** para la Vía Láctea: su luz borra las estrellas débiles.

---

*Parte V · Referencia*

# 14. Errores típicos y lista de comprobación

## 14.1. Los errores más frecuentes

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

## 14.2. Lista de comprobación

```
PREPARAR
[ ] Selección hecha (P / X / estrellas) y copia de los originales
[ ] 30 s de análisis: ¿qué es el sujeto? ¿qué distrae? ¿cómo era la luz?
[ ] Pantalla con brillo moderado, sin True Tone ni Night Shift

CALIDAD
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
[ ] Sujeto: Object Select AI → +luz, +textura
[ ] Fondo (⌘I): −luz, −saturación
[ ] Cielo / suelo: Mask AI (A) o Gradient (G)
[ ] Noche: Vía Láctea con Radial (R); horizonte con Gradient
[ ] Bordes de máscara revisados con /

ACABADO
[ ] Remove Dust Spots / Erase (solo distracciones pequeñas)
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

---

*Parte V · Referencia*

# 15. Atajos de teclado (macOS)

Atajos según la documentación oficial de Skylum. En Windows, **`⌘`** suele corresponder a **Ctrl** y **`⌥`**, a **Alt**.

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

---

*Parte V · Referencia*

# 16. Glosario

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
| **Instancia** | Una herramienta repetida en la misma foto, normalmente con otra máscara |
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

# 17. Preguntas frecuentes

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
Algunas dependen de tu versión o licencia (por ejemplo, las versiones *Improved* requieren Luminar for Desktop 1.29.0 o posterior y una licencia que las incluya). Consulta la documentación oficial (sección 18).

**¿Cómo sé si me he pasado editando?**
Tres pruebas: compara con **`\`**; mira la miniatura junto a otras fotos sin editar; y vuelve a mirarla al día siguiente. Si "salta" por artificial, baja.

---

*Parte V · Referencia*

# 18. Fuentes

Los nombres de las herramientas, los controles, los atajos y los límites técnicos de esta guía se han comprobado con la documentación oficial de Skylum (noviembre de 2026). Los valores numéricos de ajuste son **recomendaciones de esta guía**, no de Skylum.

**General**
- [Índice de la documentación de Luminar](https://support.skylum.com/llms.txt)
- [Atajos de teclado (Desktop)](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- [Sincronizar ajustes](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/syncing-adjustments)
- [Presets](https://support.skylum.com/presets) · [Personalizar presets](https://support.skylum.com/presets/customizing-presets)
- [Exportar](https://support.skylum.com/saving-and-exporting-files/export-image)

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
- [Luminosity Masking](https://support.skylum.com/editing-tools/masking-options/luminosity-masking) · [Color Masking](https://support.skylum.com/editing-tools/masking-options/color-masking) · [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions)
- [Layers](https://support.skylum.com/editing-tools/layers) · [Layer Properties](https://support.skylum.com/editing-tools/layers/layer-properties) · [Añadir y quitar capas](https://support.skylum.com/editing-tools/layers/adding-and-removing-a-layer)

**Recorte y herramientas Extra**
- [Crop AI](https://support.skylum.com/editing-tools/crop-ai-tool)
- [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge) · [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching) · [Focus Stacking](https://support.skylum.com/extra-tools/focus-stacking) · [Upscale](https://support.skylum.com/extra-tools/upscale)
- [GenErase](https://support.skylum.com/extra-tools/generative-tools/generase) · [GenSwap](https://support.skylum.com/extra-tools/generative-tools/genswap) · [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand)
