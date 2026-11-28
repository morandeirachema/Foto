<!-- nav -->
[← Anterior](07-safari.md) · [Índice](README.md) · [Siguiente →](09-noche.md)
<!-- /nav -->

*Parte III · Por tipo de foto*

# 8. Paisaje y ciudad

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

Cómo se hacen estas fotos con la cámara: [manejo 12 · Calle y arquitectura](../manejo-a6700/12-calle-y-arquitectura.md). Aquí, lo que cambia al editarlas.

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

<!-- nav -->
[← Anterior](07-safari.md) · [Índice](README.md) · [Siguiente →](09-noche.md)
<!-- /nav -->
