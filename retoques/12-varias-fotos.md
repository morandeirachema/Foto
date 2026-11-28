<!-- nav -->
[← Anterior](11-trabajar-en-serie.md) · [Índice](README.md) · [Siguiente →](13-exportar.md)
<!-- /nav -->

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

<!-- nav -->
[← Anterior](11-trabajar-en-serie.md) · [Índice](README.md) · [Siguiente →](13-exportar.md)
<!-- /nav -->
