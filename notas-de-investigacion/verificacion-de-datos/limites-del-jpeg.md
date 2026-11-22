# Verificación de las notas sobre los límites de la edición de JPEG

Verificación del 22 de noviembre de 2026. Objeto: las notas `jpeg_limits_and_workflow.md` (original en inglés, retirado del repo; queda en el historial de git, commit `0ad034a`) (inglés) y dos secciones del informe [`informes/edicion-jpeg-safari-paisaje-noche.md`](../../informes/edicion-jpeg-safari-paisaje-noche.md). La versión en castellano, con el estado de cada hallazgo, está en [`limites-del-jpeg-y-flujo.md`](../edicion-jpeg-safari-paisaje-noche/limites-del-jpeg-y-flujo.md).

Método: cada dirección citada se abrió con la herramienta normal de lectura de páginas. Esa herramienta devuelve respuestas de un modelo auxiliar sobre el contenido de la página y limita las citas a unos 125 caracteres, así que las frases largas se comprobaron por trozos consecutivos. Tres PDF (el artículo de York University y las dos patentes) se leyeron directamente, página a página. Cuando un sitio rechazó la petición (403), pidió pago (402) o falló, no se intentó ningún rodeo y el hallazgo quedó como "⚠️ no se pudo volver a comprobar". No se usó ninguna copia en archivo ni ningún otro sitio en sustitución de la fuente citada.

Límite de lo comprobado: "✅" significa que la página se abrió en esta verificación y respalda la afirmación; las citas literales se cotejaron con el texto que devolvió la herramienta, no con una búsqueda de cadena exacta sobre el HTML, de modo que una diferencia de puntuación o de comillas tipográficas podría haber pasado inadvertida.

## ¿Existe cada dirección y dice la página lo que se le atribuye?

### Conclusión
De 86 hallazgos con fuente, 54 quedan comprobados, 18 corregidos, 9 sin poder comprobarse y 5 retirados. No se encontró ninguna dirección inventada: todas las direcciones responden o respondieron (dos ya no existen). Sí hay cinco afirmaciones que la fuente citada no contiene, tres citas "literales" que no lo son y varios añadidos de las notas presentados como si fueran de la fuente.

### Hallazgos con fuente

Totales por estado y sección:

| Sección | ✅ | ❌ | ⚠️ | ✖ | Total |
|---|---|---|---|---|---|
| 1. Luces y sombras | 3 | 4 | 1 | 1 | 9 |
| 2. Balance de blancos | 2 | 2 | 0 | 2 | 6 |
| 3. Bandas | 10 | 2 | 0 | 1 | 13 |
| 4. Artefactos de compresión | 5 | 2 | 1 | 0 | 8 |
| 5. Procesado de la cámara | 10 | 1 | 0 | 0 | 11 |
| 6. Orden de operaciones | 2 | 2 | 0 | 0 | 4 |
| 7. Generaciones y exportación | 7 | 2 | 1 | 1 | 11 |
| 8. Espacio de color y ajustes | 8 | 1 | 2 | 0 | 11 |
| 9. Herramientas de IA | 4 | 2 | 3 | 0 | 9 |
| 10. Resolución | 3 | 0 | 1 | 0 | 4 |
| **Total** | **54** | **18** | **9** | **5** | **86** |

El hallazgo de la sección 3 con dos fuentes (Friedl y Have Camera Will Travel) cuenta como ❌ por la parte de Friedl; la parte de Have Camera Will Travel es ⚠️.

**✖ Retirados (5): la fuente no existe o no contiene la afirmación**
- "El RAW conserva en torno a un paso más de luces que el JPEG": la dirección devuelve 404. — [Life after Photoshop](https://lifeafterphotoshop.com/tag/highlight-recovery)
- "El valor máximo del JPEG es (255,255,255); escalar canales sube el brillo o deja las luces teñidas": la patente US 7,057,768 B2 ("Automatic Color Balance", Zaklika et al., Corel, 6 de junio de 2006) se leyó entera (12 páginas) y no lo dice ni menciona el JPEG. — [USPTO 7057768](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7057768)
- "Cada canal se satura a un nivel distinto; el balance cerca de las luces es 'particularly tricky'; el RAW registra cuándo recorta cada canal": la patente US 8,890,974 B2 ("Methods and Systems for Automatic White Balance", Buyue Zhang, Texas Instruments, 18 de noviembre de 2014) se leyó entera (17 páginas) y no contiene ni la frase ni la idea; trata de la calibración del balance automático. — [USPTO 8890974](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8890974)
- "Los huecos del histograma de menos de unos tres niveles no se ven": la página devuelve 410 (retirada por el sitio). — [Adorama](https://www.adorama.com/alc/the-pitfall-of-darkening-a-sky-part-1)
- "La horquilla recomendada para exportar es 85–92": la página existe, pero no da ninguna cifra de calidad. — [Uploadcare](https://uploadcare.com/blog/jpeg-quality-loss)

**❌ Corregidos (18)**

Citas "literales" que no lo son:
- "recovered cleanly from the JPEG" no aparece; la frase es "yet Leigh recovers it cleanly from the JPEG". — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- "corrected well with a straightforward adjustment in Lightroom" no aparece; la frase es "the JPEG corrects well with a straightforward adjustment in Lightroom". — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- "Manipulating WB in the sRGB colour space is challenging, even when WB is applied in a linearised sRGB space" no es literal ni está en el resumen de arXiv 2004.01354. La redacción real está en el artículo de York University: "Manipulating WB in the sRGB color space is challenging. Even when the exact illumination color temperature is used [...] and WB correction is applied in a “linearized” sRGB space [5, 16], the results are still poor". — [York University](https://yorkucvil.github.io/projects/public_html/ColorTemperatureTuning/files/ColorTemperatureTuning.pdf); [arXiv 2004.01354](https://arxiv.org/abs/2004.01354)

La fuente dice otra cosa:
- Friedl no dice que "un degradado de cielo difícil mostraba posterización en todos los niveles de calidad" ni que las bandas vengan del codificador: la imagen con bandas en todos los niveles es la del puente, y las tiene "including even “lossless TIFF”". — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)
- Friedl no dice "en la mayoría de las muestras, con un degradado de cielo como excepción": dice que 75 (tramo 70–76) iguala a simple vista al máximo "for all the samples except for the bridge". — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)
- El resumen de arXiv 1601.01339 no habla de mejora del contraste; habla de que el ruido de compresión perjudica a operaciones de tipo enfoque (desenfoque inverso y superresolución). — [arXiv 1601.01339](https://arxiv.org/abs/1601.01339)
- LetsEnhance dice de waifu2x, no de Gigapixel, que limpiaba artefactos JPEG y grano pero dejaba la imagen blanda. — [LetsEnhance](https://letsenhance.io/blog/all/lets-enhance-vs/amp/)
- El hilo de Topaz documenta artefactos del modelo sobre originales limpios ("No artifacts are present on the original images"), no sobre JPEG con artefactos previos; además es de octubre de 2024, no de 2025. — [Comunidad de Topaz](https://community.topazlabs.com/t/reported-core-model-artifact-cases/86980)
- DPReview compara el ruido al aclarar con la a6600, no con "sus rivales". — [DPReview](https://www.dpreview.com/reviews/sony-a6700-review)
- La frase de Unique Photo sobre lo recortado en el sensor está en una respuesta generada por IA ("UniqueBot"), no en la respuesta de la comunidad. — [Unique Photo](https://www.uniquephoto.com/community/qa/why-can-raw-files-recover-some-blown-highlights-that-jpegs-cannot)

Añadidos de las notas presentados como de la fuente (menores):
- Photodoto: "hacia 2006"; la página no muestra fecha. — [Photodoto](https://photodoto.com/raw-vs-jpg-correcting-underover-exposure)
- Cloudinary: "con independencia de la profundidad de bits" y "se dividen los coeficientes DCT" (la página dice "pixel values, DCT coefficients or something else"); "la principal fuente de pérdida"; "plataformas de mensajería" (solo Facebook y Twitter); `jpegtran` (solo en la dirección de un enlace) y "recodificar una vez a alta calidad" (la página dice "using a high(er) quality setting certainly makes sense"). Son cuatro hallazgos. — [Cloudinary](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Cambridge in Colour: el radio "0.2-0.3" no lleva unidad ("px" es añadido); "después de cambiar el tamaño" no es literal. Son dos hallazgos. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Sony Creative Look: la lista de parámetros omitía Fade y decía que todos los looks ofrecen Saturation, que no se puede ajustar en BW ni en SE. — [Sony](https://helpguide.sony.net/ilc/2320/v1/en/contents/0411B_creative_look.html)

**⚠️ No se pudieron volver a comprobar (9)**
- 403 (el sitio rechaza peticiones automáticas): [Pentax Forums](https://www.pentaxforums.com/forums/32-digital-processing-software-printing/379181-jpg-somehow-better-recovery-than-its-raw-version-post4516137.html); [Adobe Help, JPEG Artifacts Removal](https://helpx.adobe.com/photoshop/using/quick-actions/jpeg-artifacts-removal.html) (dos hallazgos, secciones 4 y 9); [foro de DPReview](https://www.dpreview.com/forums/threads/a7rv-heif-vs-jpeg.4714248); [Fred Miranda](https://www.fredmiranda.com/forum/topic/1937008/1/) y [PetaPixel, color gamut](https://petapixel.com/2024/04/11/color-gamut-in-smartphones-what-you-should-know) (un hallazgo); [PetaPixel, upscalers](https://petapixel.com/2026/08/6-best-image-upscalers-tested/); [PetaPixel, megapixels](https://petapixel.com/how-many-megapixels/).
- La lectura falló sin respuesta (ni página ni código de error) y no se insistió: [Finding the Universe](https://www.findingtheuniverse.com/best-noise-reduction-software).
- 402 (pide pago): [Photography Life](https://photographylife.com/jpeg-compression-levels-in-photoshop-and-lightroom).
- Además, la parte de [Have Camera Will Travel](https://havecamerawilltravel.com/lightroom/exporting-jpegs-lightroom-quality-settings/) (403) del hallazgo doble de la sección 3.

**✅ Comprobados (54).** El detalle, con la frase que lo respalda, está en la versión en castellano de las notas. Fuentes que respaldan íntegramente lo que se les atribuye: [Cambridge in Colour, posterización](https://cdn.cambridgeincolour.com/tutorials/posterization.htm) (todas las citas); las seis páginas de la [Guía de ayuda de la a6700](https://helpguide.sony.net/ilc/2320/v1/en/index.html); la [página de Sony sobre HEIF](https://support.d-imaging.sony.co.jp/support/ilc/heif/02/en/index.html); [Fstoppers, HEIF vs. JPEG](https://fstoppers.com/gear/heif-vs-jpeg-should-switch-your-cameras-default-file-format-900251); las citas de la [review de DPReview](https://www.dpreview.com/reviews/sony-a6700-review) (incluida la errata "boarding", que es de la fuente).

### Inferencias
- Los errores siguen un patrón: casi todos los graves vienen de hallazgos etiquetados como "fragmento" (los 5 retirados y 5 de las correcciones, entre ellas casi todas las de fondo). Los hallazgos "leídos" fallan sobre todo en detalles: citas retocadas en el tiempo verbal y glosas añadidas.
- Las tres conclusiones de las notas que más se debilitan son: el "paso extra" de luces del RAW (sin fuente tras la retirada), el argumento del recorte de canales en el balance de blancos (sin fuente tras retirar las dos patentes) y la horquilla "77–85" de exportación (la única prueba legible dice 70–76).

### Lagunas
- Nueve hallazgos siguen sin comprobarse porque los sitios no admiten lectura automática; alguien tendría que abrirlos a mano en un navegador.
- Del artículo arXiv 2004.01354 y del de arXiv 1601.01339 solo se comprobó el resumen; el cuerpo del PDF no se pudo leer como texto.

## ¿Qué hallazgos venían solo de fragmentos de búsqueda, y qué dice hoy la página?

### Conclusión
De los 32 hallazgos etiquetados como fragmento (o "no leído"), 13 quedan confirmados al abrir la página, 5 corregidos, 5 retirados y 9 sin poder comprobarse.

### Hallazgos con fuente
- Confirmados al abrir la página: [York University](https://yorkucvil.github.io/projects/public_html/ColorTemperatureTuning/files/ColorTemperatureTuning.pdf); [Adobe Research](https://research.adobe.com/publication/when-color-constancy-goes-wrong-correcting-improperly-white-balanced-images); [ExpertPhotography, bandas](https://expertphotography.com/color-banding) (dos hallazgos); [darktable](https://docs.darktable.org/usermanual/5.6/en/module-reference/processing-modules/dither-or-posterize/); [Adobe Community](https://community.adobe.com/t5/photoshop-ecosystem-discussions/apparent-bit-depth-problem-and-bit-depth-change-bug/td-p/9408809); [Shutterstock](https://submit.shutterstock.com/help/en/articles/10617487-what-does-overuse-of-noise-reduction-and-sharpening-look-like); [Unique Photo, orden](https://www.uniquephoto.com/community/qa/should-noise-reduction-be-applied-before-sharpening); [ExpertPhotography, JPEG to RAW AI](https://expertphotography.com/topaz-jpeg-to-raw-ai-review); [Fstoppers, reducción de ruido](https://fstoppers.com/reviews/who-makes-best-noise-reduction-software-722527); [Chase Jarvis](https://chasejarvis.com/blog/topaz-ai-image-upscaler/); [Adorama, impresión](https://www.adorama.com/alc/pixels-and-printing-size-matters); [Sony, tamaño de imagen de la α7R V](https://helpguide.sony.net/ilc/2230/v1/en/contents/TP0003057051.html).
- Corregidos, retirados y sin comprobar: los indicados en la pregunta anterior.

### Inferencias
- La página de Adorama sobre impresión resuelve una duda del original: la pauta 180/240/300 ppp sí está en esa página, con esas tres cifras.

### Lagunas
- Ninguna adicional.

## Aritmética de las notas y datos de la Sony a6700

### Conclusión
Las cuentas de impresión son correctas, con un único desliz menor. Los datos de la a6700 coinciden con la Guía de ayuda de Sony; Sony no declara la profundidad de bits del HEIF en la documentación de este modelo.

### Hallazgos con fuente
- Tamaño L en 3:2: "26M", 6192×4128 (25,56 MP calculados). Otros: M 13M 4384×2920; S 6.4M 3104×2064. — [Sony, JPEG Image Size/HEIF Image Size](https://helpguide.sony.net/ilc/2320/v1/en/contents/0404M_jpeg_image_size.html)
- Calidad: Extra fine, Fine, Standard, Light; la compresión aumenta y el tamaño disminuye en ese orden. En la guía en español: "Calidad JPEG/Calidad HEIF", con Extrafina, Fina, Estándar y Ligero. — [Sony EN](https://helpguide.sony.net/ilc/2320/v1/en/contents/0404M_jpeg_image_quality.html); [Sony ES](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404M_jpeg_image_quality.html)
- JPEG/HEIF Switch ("Conm JPEG/HEIF" en español): JPEG, "This setting gives priority to compatibility"; HEIF(4:2:0), "This setting gives priority to image quality and compression efficiency"; HEIF(4:2:2), "This setting gives priority to image quality"; "Depending on the computer or software, you may not be able to view or edit HEIF files." Ni la página en inglés ni la española contienen "10-bit", "8-bit" ni la palabra "bit". — [Sony EN](https://helpguide.sony.net/ilc/2320/v1/en/contents/201h_jpeg_heif_switch.html); [Sony ES](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_jpeg_heif_switch.html)
- Tampoco dan profundidad de bits para las fotos la página HLG Still Image ni las especificaciones, que solo dicen "HEIF (MPEG-A MIAF compliant)". — [Sony, HLG Still Image](https://helpguide.sony.net/ilc/2320/v1/en/contents/201h_HLG_photo.html); [Sony, Specifications](https://helpguide.sony.net/ilc/2320/v1/en/contents/221h_specifications_ilc2320.html)
- Los "10 bits" proceden de la página de Sony para la ILCE-1 ("a rich 10-bit color depth gradation expression") y de DPReview ("the a6700 can shoot 10-bit HLG stills in the HEIF format"). — [Sony, HEIF (ILCE-1)](https://support.d-imaging.sony.co.jp/support/ilc/heif/02/en/index.html); [DPReview](https://www.dpreview.com/reviews/sony-a6700-review)
- Color Space: sRGB, "This is the standard color space of the digital camera."; AdobeRGB, "This color space has a wide range of color reproduction."; "The file name of the recorded image starts with "_"."; "The [Color Space] setting is invalid when shooting images in the HEIF format." — [Sony, Color Space](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414_color_space.html)
- DRO: Off, Auto, Lv1–Lv5; "When shooting with [D-Range Optimizer], the image may be noisy."; fijo en Off en Sunset, Night Scene y Night Portrait, y en Auto en los demás modos de Scene Selection; también fijo en Off con Picture Profile distinto de Off y con Log Shooting en On (Flexible ISO). — [Sony, D-Range Optimizer](https://helpguide.sony.net/ilc/2320/v1/en/contents/0409B_d_range_optimizer.html)
- Creative Look: Contrast, Highlights, Shadows y Saturation de −9 a +9; Fade 0–9; Sharpness 0–9; Sharpness Range 1–5; Clarity 0–9; no se dan valores por defecto; "When this function is set to [BW] or [SE], [Saturation] cannot be adjusted." — [Sony, Creative Look](https://helpguide.sony.net/ilc/2320/v1/en/contents/0411B_creative_look.html)
- High ISO NR: Normal, Low, Off; fijo en Normal en Intelligent Auto y Scene Selection. — [Sony, High ISO NR](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414C_high_iso_nr.html)

### Inferencias
- Aritmética recalculada (1 in = 2,54 cm, a partir de 6192×4128): 30×45 cm a 240 ppp pide 2835×4252 (12,05 MP) y a 300 ppp, 3543×5315 (18,83 MP); la toma completa da 349,5 ppp. Los demás tamaños de la tabla (10×15, 13×18, 20×30, 40×60) también coinciden: 1048, 806 (lado corto), 524 y 262 ppp. Márgenes de recorte: 14,2 % para 300 ppp y 31,3 % para 240 ppp. Diagonal de 30×45: 54,1 cm (21,3 in); 3438/21,3 = 161 ppp; a 1,5–2 diagonales, 108–81 ppp.
- Único desliz: "2900×1900 px (5,4 MP)" son 5,5 MP; 5,4 MP corresponde a 2835×1890.
- La versión en español de la guía de Sony se consultó solo para los nombres de menú; los nombres de las demás páginas (Color Space, DRO, Creative Look, High ISO NR) no se comprobaron en español.

### Lagunas
- La profundidad de bits del HEIF sin HLG de la a6700 queda sin confirmar con documentación de Sony para este modelo.
- El número de edición del pie de las páginas de Sony lo dio la herramienta como 5-051-980-17(1); no se cotejó con el que cita `CLAUDE.md`, 5-051-980-47(1), que puede corresponder a la edición española.

## ¿Hay fuentes mal fechadas, mal tituladas o atribuidas a otro autor o sitio?

### Conclusión
No hay ningún autor ni sitio inventado. Hay una cita atribuida al artículo equivocado, una fecha sin respaldo, una fecha errónea y dos atribuciones de contenido a quien no lo dice.

### Hallazgos con fuente
- Cita atribuida a arXiv 2004.01354 ("Deep White-Balance Editing", Afifi y Brown, CVPR 2020) que en realidad parafrasea el artículo de York University ("Color Temperature Tuning", Afifi, Punnappurath, Abdelhamed, Karaimer, Abuolaim y Brown). — [arXiv](https://arxiv.org/abs/2004.01354); [York University](https://yorkucvil.github.io/projects/public_html/ColorTemperatureTuning/files/ColorTemperatureTuning.pdf)
- Photodoto: "hacia 2006" sin respaldo en la página, que no muestra fecha; el autor es John Watson. — [Photodoto](https://photodoto.com/raw-vs-jpg-correcting-underover-exposure)
- Hilo de Topaz: "de 2025" en las notas; se abrió el 28 de octubre de 2024. — [Comunidad de Topaz](https://community.topazlabs.com/t/reported-core-model-artifact-cases/86980)
- Unique Photo: contenido de una respuesta generada por IA presentado como respuesta de la comunidad. — [Unique Photo](https://www.uniquephoto.com/community/qa/why-can-raw-files-recover-some-blown-highlights-that-jpegs-cannot)
- LetsEnhance: resultado de waifu2x atribuido a Gigapixel. — [LetsEnhance](https://letsenhance.io/blog/all/lets-enhance-vs/amp/)
- Friedl: "el autor anotó en 2019" es una respuesta suya en los comentarios (4 de abril de 2019), no una nota del artículo, que es del 11 de julio de 2010. — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)
- Fechas y autores confirmados: Fstoppers, prueba de cuatro cámaras, Alex Cooke, 24 de junio de 2026 (el vídeo es de Leigh, canal Leigh & Raymond Photography); Fstoppers, HEIF, Alex Cooke, 8 de marzo de 2026; DPReview, Dan Bracaglia y Richard Butler, 2 de agosto de 2023; Cloudinary, Jon Sneyers, 4 de mayo de 2016; Afifi, Price, Cohen y Brown, CVPR 2019. — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184); [Fstoppers](https://fstoppers.com/gear/heif-vs-jpeg-should-switch-your-cameras-default-file-format-900251); [DPReview](https://www.dpreview.com/reviews/sony-a6700-review); [Cloudinary](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier); [Adobe Research](https://research.adobe.com/publication/when-color-constancy-goes-wrong-correcting-improperly-white-balanced-images)
- La página de Sony sobre el tamaño L en modo APS-C es la de la ILCE-7RM5, como ya advertían las notas. — [Sony](https://helpguide.sony.net/ilc/2230/v1/en/contents/TP0003057051.html)

### Inferencias
- La grafía británica ("colour", "linearised") de la cita atribuida a arXiv ya delataba que no era literal: los dos artículos usan grafía estadounidense.

### Lagunas
- El título y la fecha del artículo de PetaPixel de agosto de 2026 no se pudieron confirmar (403).

## Frases del informe que la fuente no respalda tal como están escritas

### Conclusión
En las secciones "El archivo de 8 bits deja unos dos pasos de sombra y ninguna luz" y "El orden de las decisiones" hay nueve frases que una fuente no respalda como están escritas, y dos más que citan fuentes que no se pudieron abrir. La más importante es la de la calidad de exportación "77–85" atribuida a Friedl (línea 23).

### Hallazgos con fuente

Los números de línea son los del informe a 22 de noviembre de 2026.

| Línea | Frase del informe | Problema | Frase corregida |
|---|---|---|---|
| 11 | "…mientras que el RAW era claramente mejor "even at just one stop over" ([Photodoto]…); esa prueba es de hacia 2006." | La cita se refiere solo al detalle en las luces, y la página no muestra fecha. | "…mientras que el RAW era mucho mejor conservando el detalle de las luces "even at just one stop over" ([Photodoto](https://photodoto.com/raw-vs-jpg-correcting-underover-exposure)); la página no indica fecha ni cámara." |
| 11 | "…mientras que una escena de cañón muy subexpuesta "recovered cleanly from the JPEG" ([Fstoppers]…)." | La cita no es literal. | "…mientras que, en una escena de cañón muy subexpuesta, el autor del vídeo "recovers it cleanly from the JPEG" ([Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184))." |
| 13 | "…así que una corrección posterior es una aproximación (fragmento: [York University]…; [arXiv 2004.01354]…)." | Ya no es un fragmento: el artículo de York se leyó y lo respalda; de arXiv se comprobó el resumen. | "…así que una corrección posterior es difícil y da resultados pobres incluso en un sRGB linealizado ([York University](https://yorkucvil.github.io/projects/public_html/ColorTemperatureTuning/files/ColorTemperatureTuning.pdf); [arXiv 2004.01354](https://arxiv.org/abs/2004.01354))." |
| 13 | "…"corrected well with a straightforward adjustment" ([Fstoppers]…)." | La cita no es literal. | "Las correcciones moderadas funcionan en la práctica: en un JPEG de una Nikon Z9 que el balance automático había dejado azulado, "the JPEG corrects well with a straightforward adjustment in Lightroom" ([Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184))." |
| 15 | "La cuantización del JPEG produce bandas con independencia de la profundidad de bits, los errores se quedan dentro de bloques de 8×8 (16×16 con submuestreo de color) y el color se guarda con menos resolución ([Cloudinary]…)." | "Con independencia de la profundidad de bits" no está en la fuente. | "La cuantización del JPEG es una causa de bandas, la mayor parte del error se queda dentro de bloques de 8×8 (16×16 con submuestreo de color) y, con submuestreo 4:2:0, el color se guarda a la mitad de resolución en cada dirección ([Cloudinary](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier))." |
| 17 | "…la reducción de ruido va siempre antes del enfoque y que el enfoque de salida va lo último, después de cambiar el tamaño ([Cambridge in Colour]…)." | "Después de cambiar el tamaño" no es literal: la página dice "at the very end of the image editing workflow" y que el enfoque de salida compensa el ablandamiento de la reducción. | "…la reducción de ruido va siempre antes del enfoque y que el enfoque de salida va al final del flujo de edición; como compensa el ablandamiento que produce reducir la imagen, se aplica después de cambiar el tamaño (esto último se deduce, la fuente no lo dice con esas palabras) ([Cambridge in Colour](https://www.cambridgeincolour.com/tutorials/image-sharpening.htm))." |
| 21 | "Luminar guarda las ediciones en un archivo `.state` por imagen, con historial ilimitado, y enlaza los originales sin moverlos ([Skylum]…)…" | La página citada dice `.state` y "unlimited undos", pero no dice que enlace los originales sin moverlos; solo habla de "non-destructive editing". | "Luminar guarda las ediciones de cada imagen en el catálogo como un archivo `.state`, lo que permite deshacer sin límite ("unlimited undos"), y describe la edición como no destructiva ([Skylum](https://support.skylum.com/saving-and-exporting-files/saving-adjustments-in-a-catalog)); la página citada no dice qué hace con los originales…" |
| 23 | "Pruebas informales sitúan la exportación "visualmente sin pérdida" hacia una calidad de 77–85 en la escala de Adobe, con los degradados de cielo como excepción ([Jeffrey Friedl]…)…" | Friedl no usa "visually lossless" ni da 77–85: dice que 75 (tramo 70–76) iguala a simple vista al máximo en todas sus muestras salvo la del puente, que tiene bandas incluso en el TIFF sin pérdida. | "Una prueba informal de 2010 con Lightroom concluyó que su calidad por defecto, 75 (tramo 70–76), da un resultado visible tan bueno como el máximo, con alrededor de un tercio del tamaño, en todas las muestras salvo una de líneas finas y degradados suaves que mostraba bandas incluso en el TIFF sin pérdida ([Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)); ninguna fuente comprobada da un umbral "visualmente sin pérdida"…" |
| 25 | "Subir Dehaze al máximo un momento es un método conocido para descubrir manchas tenues (fragmento: [Have Camera Will Travel]…)…" | No es un error demostrado: el sitio rechaza las peticiones automáticas (403) y sigue sin comprobarse. | Mantener la frase con su etiqueta "(fragmento)" y añadir "sin comprobar: el sitio no admite lectura automática". |

- Línea 25, cita de los Toon ("for small differences, such as pricked ears or alert expressions"): la página de Australian Photography no se pudo abrir (la herramienta falló dos veces sin respuesta). Queda como ⚠️ sin comprobar; no se propone corrección. — [Australian Photography](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)

Frases de esas secciones que sí quedan respaldadas:
- Línea 11: "at 3-stops under, the corrected JPG still looks okay"; la prueba de junio de 2026 con cuatro cámaras y una sola escena con ventaja clara del RAW. — [Photodoto](https://photodoto.com/raw-vs-jpg-correcting-underover-exposure); [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- Línea 15: la cita de "stretches", los cielos lisos y los histogramas por canal; el enfoque amplifica los artefactos; el ruido añadido como apaño ("You can apply noise to mask it", "workarounds", "the fundamental data simply isn't there"; artículo de Alex Cooke, 28 de enero de 2026). — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm); [Fstoppers](https://fstoppers.com/gear/precision-myth-photographers-guide-bit-depth-719847)
- Línea 17: "decent though boarding on aggressive". — [DPReview](https://www.dpreview.com/reviews/sony-a6700-review)
- Línea 21: "The generation count has a larger impact on the image quality than the actual quality settings you use"; "You should generally only save JPEG files once". — [Cloudinary](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier); [Skylum](https://support.skylum.com/saving-and-exporting-files/export-image)
- Línea 23: los espacios amplios y la posterización; las escalas no se trasladan entre programas; Skylum no documenta la escala de Quality ("Controls the quality of the exported image") ni los niveles de Sharpen ("Applies sharpening to the exported image"); las cuentas de 349 ppp y 4252×2835. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm); [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality); [Skylum](https://support.skylum.com/saving-and-exporting-files/export-image)
- Línea 25: Erase con Objects Removal y Remove Dust Spots; "Tools like Crop, Erase, and Background Removal cannot be synced." — [Skylum, Erase](https://support.skylum.com/editing-tools/essential-tools/erase); [Skylum, Syncing Adjustments](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/syncing-adjustments)

### Inferencias
- En la línea 11, las cifras de trabajo en negrita (255 perdido, +1 a +2 EV, +3 EV el borde) ya están presentadas como extrapolación; siguen siéndolo y no cambian con esta verificación.
- En la línea 13, el resumen "la cámara lo aplica a los datos lineales del sensor y después añade un revelado no lineal y el recorte a 8 bits" queda respaldado en lo del revelado no lineal; "el recorte a 8 bits" ya no tiene fuente (las patentes se retiraron) y es razonamiento.

### Lagunas
- Las afirmaciones de primera mano de esas secciones (el 91 % con balance fijo, el 68 % en dos días, unas 1.000 fotos en la hora de las 19:00, el polvo en al menos tres fotos) no eran objeto de esta verificación web. De pasada: `fotos-de-muestra.md` sí recoge el 91 % y el 68 %; hoy describe el polvo como "una mancha fija", lo que convendría cotejar con "las mismas manchas… en al menos tres fotos" de la línea 25.
- El informe enlaza Cambridge in Colour con `www.` y las notas con `cdn.`; solo se abrió la variante `cdn.`.
