# Auditoría para consultar y revisar el repo (28 de noviembre de 2026)

## Lo que pidió el dueño

«Audita, ordena y encuentra gaps en todo el repositorio para que sea más fácil de consultar y revisar». Durante el trabajo añadió: un artículo de **mejoras de equipo** (tiene un GorillaPod de 5 kg, un trípode de aluminio, el 11 mm, el Viltrox y, unos meses, el 70-350 prestado); un **TL;DR** en el README; basar la fauna en sus **próximos destinos** (Sri Lanka, Botswana, el Pantanal) y en las **aves de España**, quitando los nombres de lugar que no aportan; en los maestros, **fotos que pueda hacer un aficionado**, **modernas** y con **cámaras actuales**; y **qué mirar en la foto y el histograma nada más disparar**.

## Cómo se auditó

Con scripts sobre todo el repo, no a ojo: la estructura de cada capítulo (nivel, parte, «si sale mal», ejercicio, referencias, «por qué funciona»), las marcas desfasadas, los recuentos de los README, los números de los textos de enlace, los archivos sin índice, las PENDIENTES por sección, las preguntas de la autoevaluación y los **299 enlaces externos** (con `curl`).

## Lo encontrado y lo hecho

| Hallazgo | Qué se hizo |
|---|---|
| No había una entrada rápida: el README era largo y no había índice cruzado | **TL;DR** al principio del README e [INDICE](../INDICE.md) por tema, por problema y por pregunta |
| Marcas 🆕 sin fecha, unas de una semana y otras del mismo día | Fuera; lo nuevo va con fecha en [NOVEDADES](../NOVEDADES.md). `comprobar.py` rechaza 🆕 |
| Retoques no tenía línea de nivel; dos hojas de manejo y conceptos tampoco | Línea de nivel en los 20 capítulos de retoques, el cuaderno y la verificación in situ. `comprobar.py` la exige (salvo en las chuletas) |
| Sin ejercicio en el safari de día y en el Viltrox | Ejercicios nuevos, más el de [aves](../manejo-a6700/08-aves.md#ejercicio-cuatro-mañanas) y el de [mejoras de equipo](../manejo-a6700/18-mejoras-de-equipo.md#ejercicio-una-tarde) |
| `informes/` y `notas-de-investigacion/` sin índice; 8 notas y un informe no enlazados desde ningún sitio | [Índice de informes](README.md) e [índice de notas](../notas-de-investigacion/README.md). `comprobar.py` avisa de cualquier informe o nota sin enlazar |
| PENDIENTES: 69 comprobaciones abiertas sin resumen | Tabla de resumen al principio, con por dónde empezar; `comprobar.py` las cuenta por sección |
| Los recuentos de los README se desfasaban con cada capítulo nuevo | `comprobar.py` compara las insignias y la tabla del README principal con los archivos |
| Riesgo de textos de enlace con el número viejo tras renumerar | `comprobar.py` compara el número del texto («capítulo 9», «Manejo 9», «9 ·») con el del archivo |
| La fauna estaba escrita para un parque de Namibia (Etosha) | Reescrita por tipo de destino y de vehículo para Sri Lanka, Botswana y el Pantanal; [fauna de noche](../manejo-a6700/07-fauna-de-noche.md) con charcas, salidas nocturnas y barca; unas 150 menciones de lugares que no aportaban, generalizadas |
| No había nada de aves | Capítulo nuevo [manejo 8 · Aves](../manejo-a6700/08-aves.md) |
| Astro escrito para las fechas y la latitud de un viaje | [Astrofotografía](../manejo-a6700/10-astrofotografia.md) y [estrellas con tierra](../manejo-a6700/09-estrellas-con-tierra.md) por latitud: Botswana, el Pantanal, Sri Lanka y España |
| No había un plan de equipo para después del viaje | Capítulo nuevo [manejo 18 · Mejoras de equipo](../manejo-a6700/18-mejoras-de-equipo.md) |
| Los ejemplos de los maestros eran sobre todo clásicos en película y alguno inalcanzable (30 horas) | [Los maestros](../conceptos/11-los-maestros.md): fotos recientes con cámaras digitales y ajustes publicados primero, marca ✅/🟡/🔴 en cada foto y fuera las inalcanzables |
| No había una rutina de revisión tras disparar | [La revisión de 10 segundos](../conceptos/03-histograma.md#acabas-de-disparar-qué-mirar-en-10-segundos), en la chuleta y en la autoevaluación (R1) |
| Un enlace roto propio (Sports Illustrated, Rowell) | Cambiado por Tahoe Quarterly |

## Los enlaces externos

De 299 enlaces, **275 responden bien**. Los demás son sitios que rechazan peticiones automáticas (403/406/429: sony.es, MoMA, NGA, The Met, Cambridge in Colour, PhotoPills, mpb, DPReview, Time…), los dos de Dustin Abbott que redirigen sin resolver (ya conocidos de la verificación del 22 de noviembre) y uno roto de verdad, el de Rowell, ya cambiado. Los que dan 403 o 406 hay que abrirlos a mano en un navegador para confirmarlos.

## La estructura final

- **Manejo, 23 capítulos**: entran **8 · Aves** y **18 · Mejoras de equipo**, y el resto se desplaza. La tabla completa está en la [introducción de manejo](../manejo-a6700/00-introduccion.md#numeración-antigua).
- **Conceptos, 13**; **retoques, 20**; **Pixel, 13**: total, **69 capítulos**.
- **Autoevaluación y test: 67 preguntas.**

## Lo que queda

- **El test interactivo** está preparado con las 67 preguntas, pero se republica **después de subir** los archivos renombrados, porque sus enlaces van a GitHub `main`.
- **PENDIENTES § 11 y § 12**: Transform con un JPEG, la zona del Viltrox tras apagar, el modelo del trípode, la prueba de los tres soportes y los datos de cada viaje que hay que confirmar con el operador.
- **Calle y arquitectura modernas sin ajustes**: los premios de 2025 consultados no publican la cámara ni los ajustes. Solo *Focus In* (Tokyo Foto Awards) los da.
- **El Pixel** sigue sin ejercicios en sus capítulos de recetas; sus fuentes están centralizadas en su [capítulo 12](../manejo-pixel-10-pro/12-verificacion.md).
- **Retoques 7 (safari)** no se ha reescrito para barcas ni para la humedad: su flujo sirve igual, y los casos de destino están en manejo.
