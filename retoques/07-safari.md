<!-- nav -->
[← Anterior](06-herramientas-avanzadas.md) · [Índice](README.md) · [Siguiente →](08-paisaje.md)
<!-- /nav -->

*Parte III · Por tipo de foto*

# 7. Safari (fauna)

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
- Si recortas mucho, piensa en **Upscale** al final (sección 12.4).
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
| **Animal más presente** | **Dodge & Burn → Lighten**, pincel grande y suave sobre el animal | **Strength** baja |
| **Fondo más discreto** | **Color** con la máscara del animal (**Copy**/**Paste**) invertida (**`⌘I`**); **Dodge & Burn → Darken** suave donde distraiga | Saturation −10 |
| **Ojo con brillo** | **Dodge & Burn → Lighten**, pincel pequeño, poca **Strength** | Solo el iris |

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
- **Upscale** solo si has recortado mucho, y siempre al final.

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
- Structure AI bajo: las rayas ya tienen todo el contraste que necesitan.

**Leopardo en un árbol (luz moteada):**
- **Dodge & Burn → Darken** sobre las manchas de luz en las ramas; **Lighten** suave en la cara del leopardo.
- **Dodge & Burn → Darken** sobre los huecos de cielo entre las ramas, para que no distraigan.

**Elefantes y rinocerontes:**
- **Structure AI** +20/+30 y **Medium Details**: la textura de la piel es su mayor atractivo.
- Si están cubiertos de barro rojizo, no lo "corrijas": es parte de la escena.

**Polvo levantado por los animales:**
- Es atmósfera, sobre todo a contraluz. No uses **Dehaze**: lo eliminaría.

**Foto desde el vehículo con el animal muy lejos:**
- Recorte fuerte + **Upscale** al final.
- Expectativas realistas: servirá de recuerdo o para la pantalla del móvil, no para imprimir grande.

<!-- nav -->
[← Anterior](06-herramientas-avanzadas.md) · [Índice](README.md) · [Siguiente →](08-paisaje.md)
<!-- /nav -->
