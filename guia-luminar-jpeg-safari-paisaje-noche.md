# Mejorar JPEG de safari, paisaje y fotografía nocturna con Luminar
### Lo básico explicado, con conceptos que valen para cualquier editor

**Versión de la guía:** noviembre de 2026 · Luminar 1.29.x · válida también como referencia para Lightroom, darktable y otros editores

---

## Cómo está organizada

1. **Conceptos universales:** lo que hay que entender, uses el programa que uses.
2. **El flujo base en Luminar:** los 10 pasos que se repiten en cualquier foto.
3. **Safari** (fauna).
4. **Paisaje** (sabana, desierto, montaña, cielo).
5. **Fotografía nocturna** (cielo estrellado, luces artificiales, luna, fuego).
6. **Errores típicos y lista de comprobación.**
7. **Tabla de equivalencias** Luminar ↔ Lightroom ↔ darktable.

En cada paso encontrarás tres cosas:
- **Qué hacer** en Luminar, con valores orientativos para JPEG.
- **Por qué**, que es lo que te permite hacerlo en cualquier otro programa.
- **En otros editores**, con el nombre del ajuste equivalente.

> **Valores orientativos.** Son puntos de partida para JPEG. Cada foto es distinta: mueve el deslizador mirando la imagen, no el número.

---

# 1. CONCEPTOS UNIVERSALES

Estos conceptos son iguales en Luminar, Lightroom, darktable, Capture One, Photoshop o la app del móvil. Si los entiendes, cambiar de programa es solo aprender dónde está cada botón.

## 1.1. Qué tiene de especial un JPEG

Un JPEG es una foto **ya revelada por la cámara**: la cámara ha decidido el balance de blancos, el contraste, la saturación, el enfoque y la reducción de ruido, y después ha **comprimido** el resultado guardando solo 256 niveles por color.

**Consecuencias prácticas:**
- **Lo que está completamente blanco (quemado) o completamente negro no se puede recuperar.** No hay información que rescatar.
- **Los ajustes fuertes rompen la imagen:** aparecen **bandas** en cielos y degradados, **halos** en los bordes, **ruido** en las sombras y colores artificiales.
- **Regla de oro:** muchos ajustes pequeños mejor que pocos grandes. Si un deslizador necesita ir muy lejos, probablemente hay otra forma mejor (una máscara, otra herramienta).

## 1.2. Las cinco zonas de brillo

Toda foto se puede dividir por brillo. Todos los editores tienen un control para cada zona:

| Zona | Qué es | Control típico |
|---|---|---|
| **Negros** | El punto más oscuro | Blacks / Negros |
| **Sombras** | Zonas oscuras con detalle | Shadows / Sombras |
| **Medios tonos** | La mayor parte de la foto | Exposure / Exposición |
| **Luces** | Zonas claras con detalle | Highlights / Altas luces |
| **Blancos** | El punto más claro | Whites / Blancos |

**Por qué importa:** cuando una foto "está mal", casi siempre es porque una zona está demasiado clara u oscura respecto a las demás. En vez de subir o bajar toda la foto, tocas **solo la zona que falla**.

## 1.3. El histograma y el aviso de recorte

- El **histograma** es una gráfica del brillo: **izquierda oscuro, derecha claro**.
- Si la "montaña" toca el borde derecho, hay **luces quemadas**; si toca el izquierdo, **negros empastados**.
- El **aviso de recorte** pinta en la foto las zonas quemadas o empastadas. En Luminar se activa con **`J`**. En Lightroom, con la tecla `J` también. En darktable, con el indicador de sobreexposición.
- **No hay un histograma correcto:** una foto nocturna tiene que estar a la izquierda y una de arena blanca, a la derecha.

## 1.4. Balance de blancos: temperatura y matiz

- **Temperatura:** azul ↔ amarillo. Corrige una luz demasiado fría o cálida.
- **Matiz (tint):** verde ↔ magenta. Corrige dominantes raras.
- **Cuentagotas:** haces clic en algo que debería ser **gris o blanco neutro** y el programa corrige el resto.
- **Importante:** no se trata de dejar todo "neutro", sino de que el color sea **creíble**. Un atardecer tiene que ser cálido; una noche, ligeramente fría.

## 1.5. Contraste global y contraste local

- **Contraste global:** separa más las zonas claras de las oscuras en toda la foto (deslizador de contraste, curva en S).
- **Contraste local (claridad, estructura, textura):** aumenta el contraste **dentro de cada zona pequeña**. Hace que se vean las texturas: el pelo de un animal, la corteza de un árbol, las ondas de una duna.
- **El exceso de contraste local** es el error más típico de la edición moderna: halos, aspecto "HDR" y fotos sucias.

## 1.6. Ruido y nitidez: siempre van juntos

- **Ruido:** el granito que aparece con ISO alto o al aclarar sombras.
- **Nitidez (enfoque):** refuerza los bordes.
- **El conflicto:** enfocar refuerza también el ruido, y quitar ruido ablanda los detalles. Por eso el orden lógico es **primero quitar ruido, después enfocar**, y **siempre revisando al 100 %**.

## 1.7. Ajustes globales y locales

- **Globales:** afectan a toda la foto. Sirven para corregir.
- **Locales (máscaras):** afectan a una zona. Sirven para **dirigir la mirada**: sujeto un poco más claro y nítido, fondo un poco más apagado.
- **Tipos de máscara que existen en casi todos los editores:** pincel, degradado lineal, degradado radial, por brillo, por color y, cada vez más, **automáticas con IA** (sujeto, cielo, personas).

## 1.8. El orden universal de trabajo

Funciona en cualquier programa:

1. **Calidad:** ruido y desenfoque.
2. **Geometría:** recorte, horizonte, perspectiva.
3. **Luz global:** exposición y zonas de brillo.
4. **Color global:** balance de blancos y saturación.
5. **Textura:** contraste local y nitidez.
6. **Ajustes locales:** sujeto, cielo, fondo.
7. **Retoque:** manchas y distracciones.
8. **Acabado:** viñeteado, grano.
9. **Revisión** al 100 % y con descanso.
10. **Exportación.**

---

# 2. EL FLUJO BASE EN LUMINAR (10 PASOS)

Este es el esqueleto que usarás en todas las fotos. Las partes de safari, paisaje y noche explican **qué cambia** en cada caso.

### Paso 1 · Preparar
- Añade la carpeta al catálogo y selecciona: **`P`** favorita, **`X`** rechazada, **`1`–`5`** estrellas.
- Luminar **no modifica tus JPEG**: guarda los ajustes aparte. Aun así, ten copia de los originales.
- **Por qué:** editar solo las mejores fotos ahorra muchísimo tiempo y mejora el resultado.

### Paso 2 · Ruido: Noiseless AI (solo si hace falta)
- **Image Quality → Noiseless AI.** Acepta el nivel que propone (*Low*, *Middle*, *High*) y revisa al 100 % (**`⌘1`**).
- Si la piel o el pelaje parecen de cera, baja **Luminosity Denoise** y sube **Details**.
- **Por qué primero:** los siguientes pasos (aclarar sombras, subir contraste) aumentan el ruido. Mejor empezar con una base limpia.
- **En otros editores:** Lightroom → *Reducción de ruido* (IA); darktable → *restauración neuronal* o *reducción de ruido (perfilado)*.

### Paso 3 · Recorte y horizonte
- **`C`** → **Auto Straighten** para nivelar y, si tu licencia lo tiene, mira las **composiciones sugeridas**.
- **Por qué:** un horizonte torcido arruina cualquier foto y el encuadre decide dónde mira el espectador.
- **En otros editores:** herramienta *Recortar* con enderezado automático.

### Paso 4 · Luz: Develop
- Pulsa **`J`** para ver el recorte.
- **Exposure** para el sujeto (±0,3 a ±0,7).
- **Highlights** abajo (−20 a −50) para recuperar cielo y luces.
- **Shadows** arriba (+15 a +40) para abrir sombras.
- **Whites** y **Blacks** hasta que el aviso de recorte apenas aparezca.
- **Smart Contrast** +10 a +25.
- **Por qué:** primero colocas cada zona de brillo en su sitio; luego das contraste.
- **En otros editores:** Lightroom → *Básico*; darktable → *exposición* + *ecualizador de tonos*.

### Paso 5 · Color: balance de blancos
- **Develop → Color:** cuentagotas (**`W`**) sobre algo neutro, o ajusta **Temperature** y **Tint**.
- **Por qué:** una dominante de color hace que todo lo demás parezca "raro" aunque la luz esté bien.
- **En otros editores:** Lightroom → *Balance de blancos*; darktable → *calibración de color*.

### Paso 6 · Mejora general: Enhance AI (con moderación)
- **Accent AI** 15–35. **Sky Enhancer AI** 20–40 si hay cielo con nubes.
- **Comprobación:** pasa el deslizador de 0 a tu valor varias veces. Si la versión editada te parece chillona, baja.
- **Por qué:** combina luz, color y detalle en un movimiento, pero es fácil pasarse.
- **En otros editores:** no hay equivalente exacto. Se consigue combinando *Intensidad*, *Claridad* y curvas.

### Paso 7 · Color fino: Color → HSL
- **Vibrance** +5 a +20 (mejor que Saturation).
- **HSL:** ajusta colores concretos (ver tablas en cada parte).
- **Por qué:** cada color de la escena necesita algo distinto; tocarlos por separado da colores naturales.
- **En otros editores:** Lightroom → *Mezcla de colores (HSL)*; darktable → *balance de color rgb* y *ecualizador de color*.

### Paso 8 · Textura y nitidez: Structure AI y Details
- **Structure AI** +10 a +25 (contraste local; protege caras).
- **Details** con valores bajos y **Details Masking** alto, para enfocar solo los bordes y no el cielo.
- **Por qué:** el contraste local da "cuerpo"; la nitidez define bordes. Ambos con moderación en JPEG.
- **En otros editores:** Lightroom → *Textura*, *Claridad*, *Enfoque*; darktable → *contraste local*, *nitidez*.

### Paso 9 · Ajustes locales: máscaras
- En cualquier herramienta, pestaña **Masking**: **Object Select AI** (un sujeto con un clic), **Mask AI** (cielo, personas, agua…), **Gradient** (**`G`**), **Radial** (**`R`**), **Brush** (**`B`**).
- **`/`** muestra la máscara; **`⌘I`** la invierte; **Feather** suaviza el borde.
- **Por qué:** dirigir la mirada es lo que separa una foto corregida de una foto buena.
- **En otros editores:** Lightroom → *Máscaras* (Seleccionar sujeto, Seleccionar cielo, degradados, pincel); darktable → *máscaras dibujadas, paramétricas* y *máscara de objeto IA*.

### Paso 10 · Acabado, revisión y exportación
- **Erase** (**`⌘E`**) para manchas y distracciones pequeñas.
- **Vignette** −10 a −20, si encaja.
- **Film Grain** 5–10 si ves bandas en el cielo.
- **`\`** (mantener) para comparar con el original. Revisa al 100 %, descansa 5 minutos y **baja lo que sobre**.
- **Exportar** (**`⇧⌘E`**): JPEG calidad 90–95 %, **sRGB**.

---

# 3. SAFARI (FAUNA)

## 3.1. Problemas típicos de las fotos de safari

| Problema | Por qué ocurre |
|---|---|
| **Ruido** | Amanecer y atardecer, teleobjetivo, velocidad alta → ISO alto |
| **Animal oscuro, cielo quemado** | Animales a contraluz o con el cielo detrás |
| **Luz dura de mediodía** | Sombras negras bajo los ojos y la tripa, contraste excesivo |
| **Calima, polvo y aire caliente** | Fotos "lavadas", con poco contraste y menos nitidez a distancia |
| **Animal pequeño en el encuadre** | Estaba lejos → hay que recortar mucho |
| **Ligero movimiento** | Desde el vehículo, con el animal en movimiento o con poca luz |
| **Fondo que distrae** | Ramas, hierba, vehículos, otros animales |
| **Dominante de color** | Luz anaranjada al amanecer, tierra roja que tiñe todo |

## 3.2. Flujo de safari paso a paso

**1. Ruido (casi siempre necesario)**
- **Noiseless AI**, nivel propuesto. Sube **Details** para no perder pelo, plumas y textura de piel.
- **Por qué:** el pelaje es lo primero que se estropea con una reducción de ruido fuerte. Mejor un poco de grano que un animal de plástico.

**2. Movimiento (solo si lo hay)**
- **Supersharp AI → Motion Blur, Low.** Revisa al 100 %: si inventa textura, bájalo o quítalo.
- **Por qué:** recupera algo de nitidez en fotos ligeramente movidas, pero no hace milagros.

**3. Recorte pensando en el animal**
- Deja **espacio hacia donde mira o se mueve** el animal.
- Pon el **ojo** cerca de un punto fuerte de los tercios.
- Quita del borde lo que distraiga (un trozo de vehículo, una rama cortada).
- Si recortas más de la mitad de la foto, piensa en **Upscale ×2** al final.
- **Concepto universal:** el ojo del animal es el centro de interés; todo el encuadre se construye a partir de él.

**4. Luz: expón para el animal**
- **Exposure** hasta que el animal tenga el brillo correcto, aunque el fondo quede algo claro u oscuro.
- **Highlights** −30 a −50 si hay cielo detrás.
- **Shadows** +20 a +40 para abrir la sombra bajo la cabeza y la tripa (luz dura).
- **Whites/Blacks** con **`J`**.
- **Por qué:** el espectador mira al animal. Si el animal está bien, el resto puede estar algo peor.

**5. Quitar la calima**
- **Landscape → Dehaze** +10 a +20.
- **Por qué:** la calima reduce el contraste a distancia. Dehaze lo recupera, pero en exceso oscurece y satura demasiado.
- **En otros editores:** *Eliminar neblina* (Lightroom), *eliminación de neblina* (darktable).

**6. Color creíble**
- **Balance de blancos:** respeta la luz cálida del amanecer o del atardecer; corrige solo si el animal parece naranja fosforito.
- **HSL útil en safari:**

| Quiero… | Color | Ajuste |
|---|---|---|
| Hierba seca dorada, no amarilla chillona | Amarillo | Saturation −10; Hue un poco hacia naranja |
| Verdes de la vegetación menos artificiales | Verde | Saturation −10 a −20 |
| Tierra roja menos intensa | Naranja / rojo | Saturation −5 a −15 |
| Cielo azul más profundo | Azul | Luminance −10 a −20 |
| Pelaje cálido natural | Naranja | Luminance +5 |

- **Vibrance** +10 mejor que Saturation.

**7. El animal como protagonista (ajustes locales)**

| Ajuste | Cómo | Valores |
|---|---|---|
| **Seleccionar el animal** | Develop (segunda instancia) → Masking → **Object Select AI** → clic sobre el animal → **Feather** 5–15 | — |
| **Animal más presente** | Con esa máscara | Exposure +0,2/+0,3; Smart Contrast +10 |
| **Textura del pelo** | Structure AI con la misma máscara (Copy/Paste) | Amount +15/+25 |
| **Fondo más discreto** | Máscara invertida (**`⌘I`**) | Exposure −0,2; Saturation −10; Structure AI −10/−20 |
| **Ojo con brillo** | Dodge & Burn o pincel pequeño | +0,2 de exposición en el ojo |

- **Por qué:** es exactamente lo que haría un fotógrafo en el laboratorio: aclarar lo importante y oscurecer lo secundario. La mirada va a lo más claro, nítido y contrastado.
- **En otros editores:** Lightroom → *Seleccionar sujeto* + *Invertir*; darktable → *máscara de objeto IA* en una segunda instancia de *exposición*.

**8. Limpieza**
- **Erase** para motas de polvo, pequeñas ramas o insectos que distraigan.
- **Importante:** en una foto documental, **no borres elementos de la escena** (otros animales, vehículos visibles, collares de seguimiento) ni uses herramientas generativas. Muchos concursos de naturaleza lo prohíben.

**9. Acabado**
- **Vignette** −10 a −15 si el fondo es claro en los bordes.
- **Upscale ×2** si recortaste mucho.

## 3.3. Casos concretos de safari

**Animal a contraluz (silueta con borde iluminado):**
- Decide: ¿silueta o detalle? Si es **silueta**, baja Blacks y deja el animal oscuro; resalta el borde de luz con Highlights un poco arriba.
- Si quieres **detalle**, máscara del animal con Exposure +0,4/+0,6 y Noiseless AI antes (esa zona tendrá ruido).

**Mediodía con luz dura:**
- Shadows +30/+40 y Highlights −30.
- Structure AI moderado: la luz dura ya tiene mucho contraste.
- **Blanco y negro** suele funcionar muy bien con esta luz.

**Amanecer y atardecer:**
- Conserva la calidez. Noiseless AI casi siempre.
- Light Depth (opcional) para reforzar el sentido de la luz.

**Pájaros en vuelo contra el cielo:**
- Exposure para el pájaro; máscara del cielo (Mask AI → Sky) con Exposure −0,2 para que no quede blanco.
- Details con Masking alto para no enfocar el cielo.

---

# 4. PAISAJE

## 4.1. Problemas típicos

| Problema | Por qué ocurre |
|---|---|
| **Cielo quemado, suelo oscuro** | El cielo es mucho más brillante que el suelo |
| **Horizonte torcido** | Fotos rápidas a mano |
| **Foto plana y sin profundidad** | Calima, luz de mediodía |
| **Colores apagados o exagerados** | Ajustes de la cámara |
| **Bandas en el cielo** | Degradados suaves en un JPEG de 8 bits |

## 4.2. Flujo de paisaje paso a paso

**1. Horizonte y encuadre**
- **`C`** → **Auto Straighten**.
- Regla de tercios: el horizonte **en el tercio superior** (si el suelo es lo interesante) o en el **inferior** (si lo interesante es el cielo). Casi nunca en el centro.
- **Concepto universal:** un buen paisaje tiene **primer plano, plano medio y fondo**. El recorte debe mantener los tres.

**2. Equilibrar cielo y suelo (el paso más importante)**
- **Highlights** −30 a −60 para el cielo.
- **Shadows** +20 a +40 para el suelo.
- Después, ajuste local:
  - **Cielo:** Develop → Masking → **Mask AI → Sky** → Exposure −0,2/−0,4; o un **Gradient** (**`G`**) de arriba abajo.
  - **Suelo:** **Gradient** desde abajo → Exposure +0,2; Shadows +15.
- **Por qué:** es lo que hacían los fotógrafos con filtros degradados delante del objetivo. Ahora se hace al editar.
- **En otros editores:** Lightroom → *Seleccionar cielo* o *Degradado lineal*; darktable → *máscara dibujada de degradado*.

**3. Profundidad**
- **Dehaze** +10 a +20 si hay calima (no más: oscurece y satura).
- **Light Depth:** primer plano un poco más claro y cálido; fondo algo más frío.
- **Concepto universal (perspectiva atmosférica):** lo cercano es más contrastado, cálido y saturado; lo lejano, más claro, frío y suave. Reforzar esa diferencia da sensación de profundidad.

**4. Color**
- **Enhance AI:** Accent 20–30, **Sky Enhancer** 25–40.
- **HSL útil en paisaje:**

| Quiero… | Color | Ajuste |
|---|---|---|
| Cielo más profundo (sin bandas) | Azul | Luminance −10 a −20 (no más en JPEG) |
| Verdes naturales | Verde / amarillo | Saturation −10 a −20 |
| Arena o dunas más cálidas | Naranja | Saturation +5 a +10; Luminance +5 |
| Roca rojiza menos intensa | Rojo / naranja | Saturation −5 a −10 |
| Agua turquesa | Aguamarina | Hue hacia aguamarina |

**5. Textura**
- **Structure AI** +15 a +25, **con la máscara del cielo invertida** (el cielo no necesita textura; si la sube, aparecen ruido y bandas).
- **Dunas y roca:** Structure AI algo más alto y Light Depth para marcar las crestas.

**6. Acabado**
- **Vignette** muy suave (−10).
- **Film Grain** 5–10 si el cielo muestra bandas.

## 4.3. Casos concretos de paisaje

**Desierto y dunas:**
- La cámara suele **subexponer** la arena clara: Exposure +0,3/+0,5.
- Highlights −20 para no perder la textura de la arena.
- La luz rasante (amanecer y atardecer) marca las ondas: refuérzala con Structure AI y Dodge & Burn.

**Atardecer:**
- No neutralices el color: como mucho Temperature −5 si es exagerado.
- **Twilight Enhancer AI** suave, o Sky Enhancer bajo.
- Siluetas de árboles: Blacks abajo para que sean negras de verdad.

**Sabana con cielo de tormenta:**
- Mask AI → Sky: Exposure −0,3, Structure AI +15 (las nubes sí agradecen textura).
- Suelo: Gradient con Exposure +0,2. El contraste entre cielo oscuro y suelo iluminado es el atractivo.

**Cambiar el cielo (Sky AI):** técnicamente fácil, pero en una foto documental o de viaje **convierte la foto en un montaje**. Úsalo solo en fotos creativas y dilo si las compartes.

---

# 5. FOTOGRAFÍA NOCTURNA

## 5.1. Lo que hay que saber antes

La fotografía nocturna es la que **más sufre en JPEG**: mucho ruido, sombras muy oscuras y la reducción de ruido de la cámara ya ha borrado parte de las estrellas débiles. Se puede mejorar mucho, pero con expectativas realistas.

**Cuatro tipos de foto nocturna, con tratamientos distintos:**

| Tipo | Reto principal |
|---|---|
| **Cielo estrellado / Vía Láctea** | Ruido, estrellas débiles, contaminación lumínica |
| **Luces artificiales** (ciudad, lodge, campamento) | Mezcla de luces de colores, luces quemadas |
| **Fuego y linternas** | Dominante naranja fuerte, contraste extremo |
| **Luna** | Luna quemada o paisaje negro |

## 5.2. Cielo estrellado y Vía Láctea

**1. Ruido, con cuidado**
- **Noiseless AI**, normalmente *Middle*.
- **Riesgo:** la reducción de ruido fuerte **borra estrellas pequeñas** (las confunde con ruido). Mira al 100 % y baja Luminosity Denoise hasta que vuelvan a verse.
- **Alternativa en otro programa:** si tienes varias fotos iguales seguidas, apilarlas con un programa de astrofotografía (por ejemplo, Sequator en Windows o Starry Landscape Stacker en Mac) reduce el ruido mucho mejor que cualquier IA. Luego terminas en Luminar.

**2. Balance de blancos**
- El cielo nocturno suele quedar naranja (contaminación lumínica) o verdoso.
- **Temperature** hacia el azul hasta que el cielo sea **gris azulado oscuro**, no naranja ni morado. Corrige el verde con **Tint** hacia magenta.
- **Concepto universal:** un cielo nocturno creíble es neutro o ligeramente azul. Las estrellas deben verse blancas con matices, no todas del mismo color.

**3. Luz**
- **Exposure** +0,3/+0,7 si está muy oscura (vigila el ruido).
- **Blacks** un poco **abajo** (−5 a −15): un cielo negro profundo disimula el ruido y da contraste a las estrellas. Si lo dejas gris, la foto parece sucia.
- **Highlights** −10/−20 si hay alguna luz quemada.
- **Shadows** con cuidado: es la zona con más ruido.

**4. La Vía Láctea**
- **Radial** (**`R`**) o **Brush** (**`B`**) sobre el núcleo de la Vía Láctea → Exposure +0,2; Smart Contrast +15; **Structure AI** +10/+20.
- **Dehaze** local +10/+15 sobre la Vía Láctea: aumenta el contraste de las nubes de estrellas.
- **Por qué local:** si subes el contraste en todo el cielo, sube también el ruido del fondo.

**5. Contaminación lumínica en el horizonte**
- **Gradient** desde el horizonte hacia arriba → Exposure −0,2; Temperature un poco hacia el azul para neutralizar el naranja.

**6. Primer plano (paisaje bajo las estrellas)**
- Suele estar muy oscuro: **Mask AI → Sky** invertida (**`⌘I`**) → Exposure +0,3/+0,5 y Noiseless.
- **No lo aclares demasiado:** una silueta oscura o un primer plano tenue es más creíble que uno iluminado como de día.

**7. Acabado**
- **Details** muy bajo y con Masking alto: el enfoque fuerte convierte el ruido en "estrellas falsas".
- **Vignette** suave.
- Revisa al 100 %: busca bandas en el cielo, halos alrededor del horizonte y estrellas convertidas en manchas.

## 5.3. Luces artificiales (lodge, campamento, ciudad)

- **Balance de blancos:** no neutralices del todo las bombillas cálidas; deja algo de calidez para que la escena sea acogedora.
- **Highlights** −30/−50 para recuperar las luces; si las bombillas están quemadas, déjalas: es normal.
- **Noiseless AI** casi siempre.
- **Magic Light AI** (opcional, muy sutil) para dar un pequeño resplandor a farolas o bombillas.
- **HSL:** baja la saturación del naranja (−10) si la luz es demasiado intensa.

## 5.4. Fuego de campamento y linternas

- **Decide el color:** la luz del fuego es muy naranja. Corrige un poco (Temperature −10 o cuentagotas sobre algo claro), pero **no la vuelvas blanca**: el fuego tiene que seguir pareciendo fuego.
- **Shadows** +20 para ver las caras; **Highlights** −40 para que la llama tenga forma.
- **Mask AI → People** con Face Light suave si hay personas.
- **Vignette** algo más marcada (−20) para concentrar la luz en el fuego.

## 5.5. Luna

- **Luna sola (con teleobjetivo):** baja **Highlights** y **Exposure** hasta ver los cráteres; **Structure AI** +20 y **Details** moderado. Fondo negro (Blacks abajo).
- **Luna en un paisaje:** en un JPEG suele estar quemada (es mucho más brillante que el paisaje). Si lo está, **no se puede recuperar**: acepta un punto blanco o haz una foto aparte de la luna.

---

# 6. ERRORES TÍPICOS Y LISTA DE COMPROBACIÓN

## 6.1. Los errores más frecuentes (en cualquier editor)

| Error | Cómo se reconoce | Solución |
|---|---|---|
| **Exceso de saturación** | Colores "fosforito", pieles naranjas | Vibrance en vez de Saturation; HSL a la baja |
| **Exceso de contraste local** | Halos, aspecto HDR sucio | Baja Structure AI / Claridad; enmascara el cielo |
| **Sombras abiertas de más** | Foto gris y plana, ruido | Menos Shadows; Blacks abajo |
| **Reducción de ruido excesiva** | Pelo, piel o estrellas de plástico | Baja la intensidad; sube Details |
| **Enfocar el ruido** | Grano áspero, estrellas falsas | Primero ruido, luego nitidez; Masking alto |
| **Bandas en el cielo** | Escalones en el degradado | Ajustes más suaves; Film Grain ligero |
| **Bordes de máscara visibles** | Línea alrededor del sujeto | Feather; ajustes locales más suaves |
| **Color poco creíble** | Atardecer neutro, noche naranja | Recuerda cómo era la luz real |
| **Editar con la pantalla al máximo brillo** | Las fotos salen oscuras en otros sitios | Brillo de pantalla moderado |

## 6.2. Lista de comprobación

```
PREPARAR
[ ] Selección hecha (P / X / estrellas) y copia de los originales
[ ] 30 s de análisis: ¿qué es el sujeto? ¿qué distrae? ¿cómo era la luz?

CALIDAD
[ ] Ruido: Noiseless AI (vigilar pelo / estrellas al 100 %)
[ ] Movimiento: Supersharp AI Low (solo si hace falta)

GLOBAL
[ ] Recorte y horizonte (C)
[ ] Luz: Exposure, Highlights, Shadows, Whites, Blacks con J
[ ] Balance de blancos creíble (W)
[ ] Dehaze suave si hay calima
[ ] Enhance AI moderado
[ ] HSL: los colores de la escena, uno a uno
[ ] Structure AI / Details con moderación

LOCAL
[ ] Sujeto: Object Select AI → +luz, +textura
[ ] Fondo (⌘I): −luz, −saturación
[ ] Cielo / suelo: Mask AI o Gradient
[ ] Noche: Vía Láctea con Radial; horizonte con Gradient

ACABADO
[ ] Erase (solo distracciones pequeñas; nada de cambiar la escena en fotos documentales)
[ ] Vignette suave
[ ] Film Grain si hay bandas

REVISIÓN Y SALIDA
[ ] \ para comparar con el original
[ ] Revisión al 100 % (⌘1)
[ ] Descanso → segunda mirada → bajar lo que sobre
[ ] Exportar (⇧⌘E): JPEG 90–95 %, sRGB
```

---

# 7. TABLA DE EQUIVALENCIAS

| Concepto | Luminar | Lightroom | darktable |
|---|---|---|---|
| Ruido con IA | Noiseless AI | Reducción de ruido (IA) | Restauración neuronal |
| Ruido clásico | Denoise / Develop → Noise Reduction | Detalle → Reducción de ruido | Reducción de ruido (perfilado) |
| Desenfoque / movimiento | Supersharp AI | — (no hay equivalente directo) | — |
| Recorte y horizonte | Crop (`C`) | Recortar | Recortar y rotar |
| Exposición | Develop → Exposure | Exposición | Exposición |
| Luces / sombras | Highlights / Shadows | Altas luces / Sombras | Ecualizador de tonos |
| Blancos / negros | Whites / Blacks | Blancos / Negros | Exposición + curva / ecualizador |
| Contraste | Smart Contrast / Curves | Contraste / Curva | Balance de color rgb / curva |
| Balance de blancos | Develop → Color | Balance de blancos | Calibración de color |
| Intensidad / saturación | Vibrance / Saturation | Intensidad / Saturación | Balance de color rgb |
| Color por canales | Color → HSL | Mezcla de colores (HSL) | Ecualizador de color |
| Quitar calima | Landscape → Dehaze | Eliminar neblina | Eliminación de neblina |
| Contraste local | Structure AI | Claridad / Textura | Contraste local |
| Nitidez | Details | Enfoque | Nitidez / contraste local |
| Máscara de sujeto IA | Object Select AI | Seleccionar sujeto | Máscara de objeto IA |
| Máscara de cielo | Mask AI → Sky | Seleccionar cielo | Máscara paramétrica / IA |
| Degradado | Gradient (`G`) | Degradado lineal | Máscara dibujada (degradado) |
| Radial | Radial (`R`) | Degradado radial | Máscara dibujada (elipse) |
| Pincel | Brush (`B`) | Pincel | Máscara dibujada (pincel) |
| Aclarar / oscurecer pintando | Dodge & Burn | Pincel con exposición | Exposición + máscara dibujada |
| Profundidad de luz | Light Depth | — (se hace con máscaras) | — (se hace con máscaras) |
| Borrar | Erase (`⌘E`) | Quitar | Retoque |
| Viñeteado | Vignette | Viñeta tras recorte | Viñeteado |
| Grano | Film Grain | Grano | Grano |
| Ampliar | Upscale | Superresolución | Restauración neuronal (upscale) |
| Comparar con el original | `\` | `\` | Instantáneas |
| Ver recorte | `J` | `J` | Indicador de sobreexposición |

---

## Fuentes

- [Documentación oficial de Luminar (Skylum)](https://support.skylum.com/llms.txt)
- [Develop / Develop RAW](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- [Noiseless AI](https://support.skylum.com/editing-tools/image-quality-tools/noiseless-ai)
- [Supersharp AI](https://support.skylum.com/editing-tools/image-quality-tools/supersharp-ai)
- [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai) · [Object Select AI](https://support.skylum.com/editing-tools/masking-options/object-select-ai)
- [Light Depth](https://support.skylum.com/editing-tools/creative-tools/light-depth) · [Magic Light AI](https://support.skylum.com/editing-tools/creative-tools/magic-light-ai)
- [Crop AI](https://support.skylum.com/editing-tools/crop-ai-tool)
- [Atajos de teclado de macOS](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- [Manual de darktable 5.6](https://docs.darktable.org/usermanual/5.6/en/)
