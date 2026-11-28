<!-- nav -->
[← Anterior](05-ajustes-locales.md) · [Índice](README.md) · [Siguiente →](07-safari.md)
<!-- /nav -->

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

<!-- nav -->
[← Anterior](05-ajustes-locales.md) · [Índice](README.md) · [Siguiente →](07-safari.md)
<!-- /nav -->
