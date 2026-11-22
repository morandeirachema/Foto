<!-- nav -->
[← Anterior](03-herramientas-una-a-una.md) · [Índice](README.md) · [Siguiente →](05-ajustes-locales.md)
<!-- /nav -->

*Parte II · El método*

# 4. El flujo base: 10 pasos

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
- **Shadows y Highlights tienen un límite.** Si los llevas muy lejos en un JPEG, la foto se vuelve gris y plana. Si necesitas más, usa una máscara o las Curvas (sección 6.1).
- **Por qué:** primero colocas cada zona de brillo en su sitio; luego das contraste.

### Paso 5 · Color: balance de blancos

- **Develop → Color:** haz clic con el cuentagotas (**`W`**) sobre algo neutro (blanco o gris) o ajusta **Temperature** y **Tint**. El desplegable de presets de **White Balance** es, según Skylum, para archivos RAW: con tus JPEG, usa el cuentagotas y los deslizadores.
- **Mueve poco.** En un JPEG el balance de blancos ya está aplicado: una corrección pequeña funciona; una grande tiñe las luces o las sombras.
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

Aquí se trabaja por zonas: **Dodge & Burn** para aclarar u oscurecer pintando, y la pestaña **Masking** de otras herramientas (Structure AI, Color…) para lo demás. **Todo el paso a paso, desde cero, en la [sección 5](05-ajustes-locales.md).**

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
| **Un animal de noche bajo un foco naranja** | La ruta completa está en [9.3](09-noche.md#animales-en-una-charca-iluminada-con-focos): descarta las movidas → mira el canal rojo → **2** Noiseless AI → corrige el color solo a medias, baja el naranja en HSL o pasa a blanco y negro → comparte a tamaño pequeño | Neutralizar del todo; aclarar las sombras; enfocar; imprimir en grande |
| **Cielo azul despejado** (cualquier foto de día a f/7–f/11) | **10** **Remove Dust Spots**, empezando por arriba a la izquierda, que es donde están tus manchas → **9** oscurece el cielo solo un poco, con un **Linear Gradient** suave o **Mask AI** (cielo) → **10** **Film Grain** si aparecen bandas → revisa el cielo al 100 % | Structure AI, Details y Dehaze sobre el cielo; bajar mucho la luminancia del azul |
| **Dunas rojas o arena naranja** | Mira el canal rojo → **4** la luz antes que el color → **8** textura para las ondas de la arena → **7** si la arena ha perdido relieve, baja un poco la saturación del naranja en vez de subirla → revisa al 100 % la cresta de la duna contra el cielo: ni halo ni borde de color | Subir la saturación del rojo o el naranja con el canal rojo al límite; cambios grandes de Hue (parten la duna en dos colores) |
| **Una persona o un árbol a contraluz, con el fondo iluminado** (Deadvlei) | **10** polvo del cielo → **4** ajusta la foto entera para la duna y el cielo, que son lo claro → **9** aclara **solo** el sujeto en sombra con una máscara ([5.5](05-ajustes-locales.md)), como mucho un paso de luz; con la misma máscara, quita el tono azulado del suelo en sombra → opcional: **Erase** sobre turistas lejanos | Subir Shadows en toda la foto. Si al aclarar sale ruido, deja el sujeto en silueta |
| **Atardecer, amanecer o una silueta buscada** | **3** horizonte nivelado → **5** conserva la calidez: no neutralices → **4** baja un poco Whites cerca del sol; deja las siluetas negras → **7** Vibrance en pequeña cantidad → **10** Film Grain para el degradado del cielo | Balance de blancos neutro; subir Exposure junto al sol; Sky AI o Sunrays si la foto se presenta como lo que viste |
| **Estrellas o Vía Láctea** | Si hay una serie, [apílala antes](09-noche.md#apilar-una-serie-fuera-de-luminar) → después, toda la [sección 9.2](09-noche.md): color hacia un gris neutro, luz con Curves poco a poco, contraste solo en el núcleo con una máscara Radial, ruido con mano ligera, Film Grain contra las bandas | Sky Enhancer AI; Dehaze o Structure AI en toda la foto; enfocar el cielo; un cielo azul saturado; aclarar el suelo negro |
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
| **Algo movida o blanda** | **Supersharp AI**, modo **Motion Blur**, nivel **Low** (sube a Middle si no basta) | Mejora un movimiento ligero; una foto muy movida no se salva |
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

<!-- nav -->
[← Anterior](03-herramientas-una-a-una.md) · [Índice](README.md) · [Siguiente →](05-ajustes-locales.md)
<!-- /nav -->
