<!-- nav -->
[← Anterior](12-varias-fotos.md) · [Índice](README.md) · [Siguiente →](14-etica.md)
<!-- /nav -->

*Parte IV · Más allá de una foto*

# 13. Exportar

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
| **Imprimir** | TIFF o JPEG a máxima calidad | Según el tamaño de la copia (11.3) | Máxima | Moderado |
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

**Si te quedas corto:** **Upscale** al final de la edición (empieza por 2×; [sección 12.4](12-varias-fotos.md)), y revisa al 100 % que no invente textura en el pelo o las plumas. Pide una **prueba pequeña** antes de la copia grande.

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
- **Sharpen** del cuadro de exportación: **moderado**. La copia pierde algo de nitidez al imprimirse; no lo subas tanto que aparezcan bordes blancos.
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

<!-- nav -->
[← Anterior](12-varias-fotos.md) · [Índice](README.md) · [Siguiente →](14-etica.md)
<!-- /nav -->
