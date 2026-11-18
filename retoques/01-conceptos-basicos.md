<!-- nav -->
[← Anterior](00-introduccion.md) · [Índice](README.md) · [Siguiente →](02-luminar-por-dentro.md)
<!-- /nav -->

*Parte I · Fundamentos*

# 1. Conceptos básicos

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

**En JPEG, corrige poco.** La cámara ya ha aplicado un balance de blancos a los colores. Mover mucho la temperatura suele dar colores sucios. Si la dominante es fuerte, corrige un poco con Temperature y termina con **HSL** (sección 3, paso 7) o con **Color Harmony → Color Balance** (sección 5.3).

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

<!-- nav -->
[← Anterior](00-introduccion.md) · [Índice](README.md) · [Siguiente →](02-luminar-por-dentro.md)
<!-- /nav -->
