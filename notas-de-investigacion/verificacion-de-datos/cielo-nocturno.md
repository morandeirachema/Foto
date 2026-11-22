# Verificación de datos: cielo nocturno

Registro de la verificación del 22 de noviembre de 2026 de las notas `notas-de-investigacion/edicion-jpeg-safari-paisaje-noche/night_sky_editing.md`. La versión verificada en castellano está en `notas-de-investigacion/edicion-jpeg-safari-paisaje-noche/cielo-nocturno.md`: cada hallazgo lleva allí su estado, la cita comprobada y su fuente.

Cómo se hizo: cada URL citada se descargó una vez con `curl` (identificación genérica de navegador), se pasó a texto y las citas literales se buscaron palabra por palabra con un script (solo se igualaron espacios y comillas tipográficas). Si un sitio rechazó la petición, era de pago o no estaba disponible, el hallazgo quedó como «⚠️ no se pudo volver a comprobar»: no se usaron copias de archivo ni otros nombres de servidor. Las inferencias no se verifican contra fuentes y siguen etiquetadas como inferencias.

## ¿Existe cada URL y dice la página lo que las notas le atribuyen?

### Conclusión
De 89 hallazgos con fuente, 66 se comprobaron tal cual, 10 se corrigieron, 12 no se pudieron volver a comprobar y 1 se retiró en parte. No se encontró ninguna fuente inventada: las páginas clave (Lonely Speck, Clarkvision, PetaPixel, Sony, Siril, StarStaX, Starry Landscape Stacker, Sequator, Affinity, National Parks at Night) existen y sostienen casi todo lo citado.

### Hallazgos con fuente

Totales por estado (viñetas de «Hallazgos con fuente» de las doce secciones; las dos tablas van aparte, más abajo):

| Estado | Hallazgos |
|---|---|
| ✅ comprobado | 66 |
| ❌ corregido | 10 |
| ⚠️ no se pudo volver a comprobar | 12 |
| ✖ retirado (en parte) | 1 |
| Total | 89 |

Citas literales y cifras: se buscaron 71 cadenas palabra por palabra; 70 están exactas en la página citada (o en una de las dos citadas) y 1 estaba mal transcrita.

- Las citas de Roger Clark pedidas están palabra por palabra: «a daylight white balance is the correct white balance to show the true colors» (la frase sigue «of the night sky»), «rarely, if ever, black or blue», «a brownish red», «There are no green stars», «Less than 1% of stars are blue», «too many nightscapes are artificially turned blue in post processing», y la línea del oxígeno a 557.7 nm, «Originates from 90 to 100 km high». Autor Roger N. Clark; publicado el 22 de diciembre de 2013 y actualizado el 20 de septiembre de 2019 — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Ian Norman, todo comprobado: el orden de siete pasos, «+2.45 stops», «about 3900 K» con Tint +14, Clarity y Vibrance/Saturation por debajo de +50, luminancia «between about 20% and 50%», color por defecto 25/50/50, «RAW Lightroom post processing method». El artículo es del 7 de septiembre de 2015, actualizado el 9 de junio de 2019, y no menciona ni JPEG ni Dehaze — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Matt Suess, todo comprobado: «I keep the slider around plus 12», «starts outlining the stars», «Halos are the giveaway of an over-processed night sky», «Clean it first, then you can color it», «a touch of grain», «garish and electric», «The thumbnail will lie to you». Autor del artículo Michael Bonocore, 24 de junio de 2026, marcado «Sponsored» y «This article was brought to you by DxO» — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Siril: «The JPEG format is however only coded in 8-bit» y «must therefore generally be used at the end of the processing chain» están literales; la segunda frase se refiere a todos los formatos comunes de la página, no solo al JPEG — [documentación de Siril](https://siril.readthedocs.io/en/stable/file-formats/Common.html)

Los diez hallazgos corregidos (❌), con lo que dice la fuente:

1. **Sony, High ISO NR (sección 2).** La página de la propia a6700 solo dice Normal / Low / Off y que queda fija en Normal en Intelligent Auto y Scene Selection. Ni ella ni la del otro modelo citado (es la ZV-E10M2) dicen que no esté disponible en RAW ni que no actúe sobre el RAW. La afirmación «it is a JPEG-pipeline process» queda sin fuente — [Sony a6700](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414C_high_iso_nr.html); [ZV-E10M2](https://helpguide.sony.net/ilc/2430/v1/en/contents/0414C_high_iso_nr.html)
2. **Star Eater, cita mal transcrita (sección 2).** El texto dice «easily mistakes sharp pinpoint stars for noise», no «easily mistake…» — [Lonely Speck](https://www.lonelyspeck.com/sony-star-eater-and-how-to-fix-it/)
3. **Clark y el balance fluorescente (sección 3).** Lo llama «technically incorrect» porque las líneas del *airglow* son de átomos distintos de los de una lámpara fluorescente, no «porque el airglow sea luz de líneas de emisión» — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
4. **Astropix y el balance automático (sección 3).** Dice que el automático «can work well with some cameras and some scenes, but it doesn't work with all» y que con una cámara sin modificar «You can just try auto white balance»; no dice que no funcione bien en astrofotografía — [Astropix](https://astropix.com/books/BGAIP/chapter2/202.html)
5. **Starry Landscape Stacker y el JPEG (sección 5, tabla y laguna).** La página oficial de requisitos dice: «JPEG files are supported for input but are strongly discouraged because of the low image quality». Las notas decían que no se había podido confirmar — [requisitos de SLS](https://sites.google.com/site/starrylandscapestacker/restrictions-and-requirements-version-1-9)
6. **Starry Sky Stacker (sección 5).** Su ficha de la App Store no menciona formatos de entrada; lo de «RAW, TIFF o JPEG» no está en la página citada. La montura ecuatorial sí — [App Store](https://apps.apple.com/us/app/starry-sky-stacker/id1332533290?mt=12)
7. **Pippit (sección 5).** La página dice que Affinity Photo «Works well for post-stack processing of astrophotos» y que no tiene apilado propio, a 69,99 USD; no habla de paisaje nocturno de Vía Láctea y contradice la ayuda y la web oficiales de Affinity — [Pippit](https://www.pippit.ai/resource/astrophotography-software)
8. **Clark y el origen del color del cielo (sección 7).** Dice que el *airglow* suele ser más brillante que la luz estelar dispersada; cita la contaminación lumínica como un componente más, no como fuente principal — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
9. **Balance automático «con luz mixta» y «bajar Whites» (sección 10, dos viñetas).** Ni Fstoppers ni TechRadar hablan de luz mixta; Digital Photography School no dice que se baje Whites para limitar el recorte (propone subirlo para dar contraste) — [Fstoppers](https://fstoppers.com/astrophotography/five-reasons-never-use-auto-white-balance-night-photos-708387); [Digital Photography School](https://digital-photography-school.com/6-easy-steps-post-processing-low-light-photo-lightroom/)
10. **Norman y el 50 % (sección 12).** La pauta es 20–50 %, y subir el deslizador produce un efecto «muddying»; el artículo no dice que la imagen se vuelva turbia por encima del 50 % — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)

(Recuento: el punto 5 es una celda de la tabla de programas y no cuenta como viñeta; el punto 9 son dos viñetas. Los otros ocho puntos son una viñeta cada uno: 8 + 2 = 10 hallazgos corregidos.)

Retirado (✖): el hilo del grupo de Fstoppers sobre declarar montajes devuelve HTTP 404 — [Fstoppers](https://fstoppers.com/groups/landscape-and-nature-photography/324393/composite-disclosure-mandatory)

### Inferencias
- Los errores encontrados son de dos tipos: lecturas que van algo más allá de lo que dice la página (puntos 3, 4, 8, 9 y 10) y datos que venían de fragmentos de buscador y no estaban en la página (puntos 1, 6 y 7). Ninguno parece una invención deliberada.
- La corrección con más consecuencias prácticas es la 5: el paso «convertir antes a TIFF» deja de ser necesario para que Starry Landscape Stacker abra los archivos.
- La corrección 1 quita el apoyo a la frase de la conclusión de la sección 2 «High ISO NR is a JPEG-only process»; lo que sí se sostiene es que el ajuste existe en la a6700 con tres valores.

### Lagunas
- No se pudo volver a comprobar nada de estas páginas, que rechazaron la petición: Photography Life (HTTP 403; cuatro hallazgos), Capture the Atlas Academy (403; dos), DPReview (403; uno), uniquephoto (403; dos, uno de ellos en parte), DarkSky (403; dos), Fred Miranda (403; dos, en parte), Inside Imaging (certificado TLS caducado; uno).
- Tres datos de la investigación original venían de fragmentos sin URL y no se pueden volver a comprobar: que Sequator sea solo para Windows, que funcione en Mac solo con CrossOver y que Siril «does not handle the ground-freezing task».

## Tabla de programas: versión, precio, macOS, formatos y funciones, comprobados hoy

### Conclusión
Las cinco filas se sostienen con las páginas oficiales de hoy, salvo la celda de entrada JPEG de Starry Landscape Stacker, que pasa de «sin confirmar» a confirmada y desaconsejada. Sequator sigue siendo el único programa que no es para macOS, y su condición de «solo Windows» no figura en sus propias páginas.

### Hallazgos con fuente
- **Starry Landscape Stacker.** 39,99 USD («Only for Mac») y 39,99 GBP; «Requires macOS 11.5 or later»; versión 1.10.1 con fecha «Oct 12» (sin año), 1.10.0 del 31 de mayo de 2025; «Built for M1 Macs. I do not have an M1 Mac and cannot test this.» en la nota de la 1.9.4 (8 de diciembre de 2021) — [App Store](https://apps.apple.com/us/app/starry-landscape-stacker/id550326617?mt=12)
- **SLS, entrada.** «All input images must be either RAW files from supported cameras, or TIFF files. TIFF files should be 16-bit […] JPEG files are supported for input but are strongly discouraged because of the low image quality. FITS files are not supported.» La misma página pide que la serie dure menos de 30 minutos (máximo 120) — [requisitos de SLS](https://sites.google.com/site/starrylandscapestacker/restrictions-and-requirements-version-1-9)
- **SLS, versión de prueba.** «It is identical to Starry Landscape Stacker except it watermarks the output image and it has a "Buy" button in the tool bar». La página dice «Version 1.10.2 and later», y las notas del desarrollador que la 1.10.1 «was released summer 2026»: no cuadra con el «Oct 12» de la App Store y no se ha podido aclarar — [versión de prueba](https://sites.google.com/site/starrylandscapestacker/free-trial); [notas de la 1.10.1](https://sites.google.com/site/starrylandscapestacker/new-in-version-1-10-1)
- **SLS, funciones.** Máscara de cielo con puntos rojos, «islands of sky», «Min Horizon Noise» y «Min Horizon Star Dupe»: todo en las notas de la versión 1.7, de enero de 2019. El historial de la App Store dice que la serie 1.10 sustituyó los algoritmos de mediana por variantes de media truncada, así que los nombres pueden haber cambiado — [notas de la 1.7](https://www.sites.google.com/site/starrylandscapestacker/new-in-version-1-7)
- **SLS, consejos del desarrollador.** «Typically 20 to 50 images collected over a period of 5 to 10 minutes will be stacked»; «convert your RAW files to 16-bit TIFF files»; la página principal dice «at least 10, more is better» — [preguntas frecuentes](https://sites.google.com/view/stacking-apps/frequently-asked-questions); [página principal](https://sites.google.com/site/starrylandscapestacker/home)
- **Siril.** «Download SIRIL version 1.4.5 released on October 28, 2026»; descargas para macOS Intel y Apple Silicon; extracción de fondo polinómica y RBF en el tutorial oficial — [siril.org](https://siril.org/download/); [tutorial](https://siril.org/tutorials/gradient/)
- **Affinity.** «Affinity is free for individuals»; «Fully optimized for macOS. Runs natively on Apple silicon and Intel.» La web no menciona la astrofotografía; la Astrophotography Stack Persona está en la ayuda de Affinity Photo 2 — [affinity.studio](https://www.affinity.studio/); [ayuda](https://affinity.help/photo2/en-US.lproj/pages/Astrophotography/astro_creating.html)
- **StarStaX.** «Coming soon to the Mac App Store»; «Requires macOS 15.4 or later, on Apple silicon or Intel»; seis modos de fusión, relleno de huecos, modo cometa y eliminación de estelas, todo literal; versiones antiguas «no longer maintained and are provided as-is». La dirección antigua de markus-enzweiler.de responde HTTP 301 hacia starstax.net — [StarStaX](https://starstax.net/)
- **Sequator.** «Sequator is a free software»; «Support RAW & 16-bit TIFF»; el manual solo cita el JPEG como salida. Ni la página principal ni el manual contienen la palabra «Windows» — [Sequator](https://sites.google.com/view/sequator/); [manual](https://sites.google.com/view/sequator/manual)

### Inferencias
- La entrada JPEG solo está declarada por escrito en Starry Landscape Stacker. Para Siril, Affinity y el StarStaX nuevo sigue sin haber una frase oficial.

### Lagunas
- La versión vigente de Starry Landscape Stacker (1.10.1 o 1.10.2) y el año del «Oct 12».
- Si la aplicación gratuita actual de Affinity conserva la persona de apilado: solo lo afirma un blog ([zelpio](https://www.zelpio.com/blog/affinity-v3-astrophotography-review/)).
- Precio y fecha del StarStaX nuevo: no están en su página.

## Datos de la Sony a6700 en su propia Guía de ayuda

### Conclusión
La reducción de ruido de exposición larga está comprobada en la página de la ILCE-6700, en inglés y en castellano. La de ISO alta existe con Normal / Low / Off, pero la guía no dice a qué archivos afecta.

### Hallazgos con fuente
- Long Exposure NR: «When you set the shutter speed to 1 second(s) or longer […] noise reduction is turned on for the duration that the shutter is open»; no disponible con obturador electrónico ni en [Cont. Shooting] o [Cont. Bracket] — [inglés](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414_long_exposure_nr.html); [castellano](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_long_exposure_nr.html)
- High ISO NR: «Normal: Activates high ISO noise reduction normally. Low: […] moderately. Off: Does not activate»; fija en [Normal] en [Intelligent Auto] y [Scene Selection]. En castellano, «RR ISO Alta»: Normal / Bajo / Desactivar — [inglés](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414C_high_iso_nr.html); [castellano](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414C_high_iso_nr.html)

### Inferencias
- Ninguna.

### Lagunas
- La guía no indica los valores de fábrica de ninguno de los dos ajustes ni si High ISO NR afecta al RAW.

## Hallazgos que venían solo de fragmentos de buscador

### Conclusión
De los 34 hallazgos que procedían en todo o en parte de fragmentos, 15 quedan comprobados al leer la página, 6 corregidos, 12 sin poder comprobarse y 1 retirado en parte.

### Hallazgos con fuente
- Comprobados al leer la página: Improve Photography, AstroBackyard, Fstoppers (balance manual; reducción por IA a 50; declarar montajes), Adobe Community, Topaz Community, Alan Dyer (amazingsky.net y PetaPixel 2022), manual de Sequator, tutorial de degradados de Siril, PIXLS.US, ayuda de Affinity y Sky at Night, Greg Benz, Universe Today, Great Big Photography World, LinkedIn Learning (solo el título) y Wikipedia. Las citas exactas están en la versión en castellano de las notas.
- Corregidos (6): Sony High ISO NR, Astropix, Starry Sky Stacker, Pippit y las dos viñetas de la sección 10 (ver la lista de arriba).

### Inferencias
- Los fragmentos fallaron sobre todo en los matices; conviene no citar ninguno sin leer la página.

### Lagunas
- Las páginas que rechazaron la petición son, casi todas, las que solo se conocían por fragmentos (ver la primera sección).

## Frases y celdas del informe y de la guía que una fuente no respalda tal como están

### Conclusión
Hay diez puntos que corregir en la sección del informe y seis en la sección «Apilar una serie» de la guía. El más importante es el mismo en los dos: Starry Landscape Stacker sí admite JPEG.

### Hallazgos con fuente

Informe, `informes/edicion-jpeg-safari-paisaje-noche.md`:

| Línea | Qué dice | Problema | Frase corregida |
|---|---|---|---|
| 63 | «La documentación de Siril dice que el JPEG de 8 bits "must therefore generally be used at the end of the processing chain"» | La frase citada habla de todos los formatos comunes, no solo del JPEG ([Siril](https://siril.readthedocs.io/en/stable/file-formats/Common.html)) | La documentación de Siril dice que el JPEG «is however only coded in 8-bit» y que los formatos comunes, el JPEG entre ellos, «must therefore generally be used at the end of the processing chain». |
| 65 | «Matt Suess mantiene un filtro de tipo Dehaze "around plus 12"…» | El filtro es ClearView, de Nik Color Efex; el 12 es de su escala, no de la de Dehaze ([PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)) | Matt Suess mantiene el filtro ClearView de Nik Color Efex, que quita la neblina como un Dehaze, «around plus 12» (en la escala de ese filtro) porque con más «starts outlining the stars». |
| 77, celda «Entrada JPEG» | «**Sin confirmar** en ninguna página oficial leída; RAW y TIFF sí están documentados…» | La página oficial de requisitos lo confirma ([SLS](https://sites.google.com/site/starrylandscapestacker/restrictions-and-requirements-version-1-9)) | **Admitida, pero desaconsejada**: «JPEG files are supported for input but are strongly discouraged because of the low image quality». RAW y TIFF de 16 bits son la entrada recomendada; el desarrollador suele apilar 20–50 tomas y pide al menos 10. |
| 77, celda «Función» | «seis algoritmos de resultado, incluido el rechazo de valores atípicos» | Los seis resultados están en la web; el rechazo de atípicos sale de notas de 2019, y la serie 1.10 cambió los algoritmos de mediana | Alinea el cielo y deja el suelo fijo con una máscara que se pinta; da seis resultados con algoritmos distintos (los de rechazo de valores atípicos constan en la versión 1.7; la serie 1.10 los cambió en parte). |
| 77, celda «Precio» | «versión de prueba en la web del desarrollador» | Correcto; falta un dato útil ([SLS](https://sites.google.com/site/starrylandscapestacker/free-trial)) | …versión de prueba en la web del desarrollador, idéntica salvo que pone marca de agua en el resultado. |
| 78 | «sin "suelo fijo" de un clic (fragmento)» | El fragmento no tenía URL y no se puede volver a comprobar; lo comprobable es que el primer plano se procesa aparte ([PIXLS.US](https://pixls.us/articles/processing-a-nightscape-in-siril/)) | Apilador gratuito con extracción de fondo (degradados); al alinear por las estrellas el primer plano queda borroso y hay que procesarlo aparte. |
| 79 | «Astrophotography Stack Persona (fragmento)» | Ya está leída, pero la página es de Affinity Photo 2 ([ayuda](https://affinity.help/photo2/en-US.lproj/pages/Astrophotography/astro_creating.html)) | Astrophotography Stack Persona, documentada para Affinity Photo 2; sin confirmar en la aplicación gratuita actual. |
| 81 | «Solo Windows (fragmento)» | Ni la web ni el manual de Sequator indican la plataforma; el fragmento no se puede volver a comprobar | Solo Windows según listados de terceros (su web no indica la plataforma); «Support RAW & 16-bit TIFF». |
| 83 | «probar la versión de prueba de Starry Landscape Stacker directamente con los JPEG; si los rechaza, convertirlos sin editar a TIFF de 16 bits, apilar…» | No los rechaza: los admite y los desaconseja | cargar los JPEG directamente en la versión de prueba de Starry Landscape Stacker, que los admite aunque los desaconseja por su calidad, apilar, exportar un TIFF de 16 bits… |
| 85 | «Un apilado del mismo sitio y del mismo momento no es un montaje según las normas consultadas» | Las normas no dicen eso: lo cuentan entre las técnicas permitidas («Compositing or other techniques are permitted for reasons such as […] image stacking/averaging») y, de noche, piden tomas hechas sin mover la cámara y dentro de unos 20–30 minutos ([NLPA](https://www.naturallandscapeawards.com/rules/)) | Un apilado del mismo sitio y del mismo momento está permitido por las normas consultadas, que admiten el «image stacking/averaging» con tomas hechas sin mover la cámara y casi a la vez; aun así, es buena práctica indicar «apilado de 10 tomas». |

Guía, `retoques/09-noche.md`, sección «Apilar una serie (fuera de Luminar)»:

| Línea | Qué dice | Problema | Frase corregida |
|---|---|---|---|
| 80 | «Unos 40 USD; tiene versión de prueba» · «Es el equivalente en Mac de Sequator» | El precio y la prueba son correctos; lo de «equivalente» es una inferencia sin fuente | Unos 40 USD; la versión de prueba es igual, pero pone marca de agua · Alinea el cielo y deja el suelo quieto con una máscara. Hace en Mac lo que Sequator en Windows (comparación de esta guía). |
| 81 | «No tiene "suelo fijo" de un clic» | Sin fuente comprobable; sí consta que el suelo se procesa aparte ([PIXLS.US](https://pixls.us/articles/processing-a-nightscape-in-siril/)) | Apila y corrige degradados de fondo (*background extraction*). Alinea por las estrellas, así que el suelo queda borroso y hay que tratarlo aparte. |
| 82 | «Solo para **trazas de estrellas**: suma los trazos de una serie larga» | Su web dice que también sirve para *light painting* y para reducir ruido promediando ([StarStaX](https://starstax.net/)); las versiones antiguas no se mantienen | Sobre todo para **trazas de estrellas**: se queda con lo más claro de cada foto de una serie larga. Las versiones antiguas son gratis, pero ya no se mantienen. |
| 84 | «Sequator, que citan muchas guías, solo existe para Windows.» | Su propia web no indica la plataforma; el dato es de terceros y no se pudo volver a comprobar | Sequator, que citan muchas guías, no tiene versión para Mac según los listados consultados (su web no indica la plataforma). |
| 88 | «**No está confirmado que acepten JPEG**: pruébalo con la versión de prueba (PENDIENTES). Si no los acepta, convierte antes los JPEG a TIFF, sin editarlos.» | Starry Landscape Stacker sí los acepta ([SLS](https://sites.google.com/site/starrylandscapestacker/restrictions-and-requirements-version-1-9)); en Siril sigue sin confirmación expresa | Abre la serie en el programa. **Starry Landscape Stacker acepta JPEG**, aunque su autor los desaconseja por la calidad; en Siril no está confirmado: si no los abre, convierte antes los JPEG a TIFF, sin editarlos. |
| 93 | «Un apilado de fotos del mismo sitio y del mismo momento no es un montaje.» | Sin fuente en la guía; las normas consultadas lo cuentan como técnica permitida ([NLPA](https://www.naturallandscapeawards.com/rules/)) | Un apilado de fotos del mismo sitio y del mismo momento es una técnica admitida incluso en concursos de fotografía de paisaje natural. Si enseñas la foto, basta con decir "apilado de 10 tomas". |

Comprobado y sin problemas en esas dos secciones: las citas de Clark, Norman y Suess; las de Starry Landscape Stacker («captured in rapid succession with identical exposure settings»); la fila de StarStaX del informe; Siril 1.4.5 y sus dos versiones para Mac; «Free for individuals» de Affinity; el muaré de National Parks at Night; la reducción de ruido de exposición larga de Sony; el hilo de Adobe Community, y las tres páginas de Skylum citadas («is not designed to work with night skies»; fusiones HDR Merge, Focus Stacking y Panorama Stitching; TIFF de 8 y 16 bits).

### Inferencias
- Si se aplica la corrección del JPEG, también hay que revisar la casilla correspondiente de `PENDIENTES.md` y la frase de `CLAUDE.md` «sin confirmar que acepten JPEG»: para Starry Landscape Stacker ya está confirmado; para Siril, no.
- Fuera del alcance pedido, pero en la misma guía: la línea 38 de `retoques/09-noche.md` dice que Norman «prefiere un cielo más frío». La fuente dice que busca un balance neutro que le acaba en unos 3900 K y que el balance «accurate» es probablemente el de luz de día. Propuesta: «Ian Norman busca un balance neutro, que en sus fotos acaba en torno a 3900 K, más frío que el de luz de día».

### Lagunas
- No se revisó el resto del informe ni de la guía fuera de las dos secciones pedidas.
- No se modificó ningún archivo del repositorio aparte de los dos de salida; el original en inglés sigue en su sitio.
