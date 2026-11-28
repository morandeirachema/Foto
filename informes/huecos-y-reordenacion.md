# Huecos y reordenación del repo (28 de noviembre de 2026)

## Lo que pidió el dueño

Refactorizar y ordenar el repo; encontrar huecos para mejorar las fotos de **safari, calle, time-lapse y astro**; explicar **por qué funciona** cada cosa y **cómo mejorar** por su cuenta; un capítulo de **calle y arquitectura** (con el 11 mm y el 25 mm); la **hiperfocal** explicada; y de **3 a 5 fotógrafos de referencia por tema** (cinco en fauna, astro, calle y arquitectura) con 2–3 fotos analizadas de cada uno, también **su edición** cuando se pueda.

## Los huecos encontrados

| Campo | Hueco | Qué se ha hecho |
|---|---|---|
| **Calle** | No existía: la calle solo aparecía de pasada en las estelas y en la ficha del Viltrox | Capítulo nuevo [`manejo-a6700/12-calle-y-arquitectura.md`](../manejo-a6700/12-calle-y-arquitectura.md): MR1 con tres cambios, **enfoque por zonas** con el 25 mm, el momento (escenario, espera, gesto, capas, luz dura), la ley y el respeto, tabla de errores |
| **Arquitectura** | No existía | En el mismo capítulo: receta, **verticales** (por qué se caen y cuatro soluciones), la luz de cada fachada, hora azul, interiores, simetría y escala; en Luminar, [retoques 8.4](../retoques/08-paisaje.md#84-ciudad-calle-y-arquitectura) con **Develop → Transform → Vertical** |
| **Hiperfocal** | Cuatro tablas sueltas (óptica, por qué funciona, 11 mm, Viltrox) sin explicar de dónde salen ni cómo se pone sin escala de distancias | [Óptica § 5](../conceptos/05-optica.md#5--la-hiperfocal-todo-nítido-de-cerca-al-infinito) completa: círculo de confusión (0,020 mm ≈ 5 píxeles), la cuenta, las dos tablas, cómo ponerla con AF-ON, la regla del doble, tres trampas y el caso de las estrellas. Las demás tablas enlazan aquí |
| **Por qué funciona** | El modelo (`conceptos/09`) no trataba **el tiempo**, que es lo que une safari, calle, estelas, time-lapse y astro; las recetas no explicaban sus números | [§ 9 · El tiempo](../conceptos/09-por-que-funciona.md#9--el-tiempo-qué-congela-y-qué-dibuja-la-velocidad) (desplazamiento en píxeles, reglas del 500 y NPF, intervalos) y una sección **«Por qué funciona»** al final de las recetas 6–12 |
| **Cómo mejorar** | El método estaba en `conceptos/10`, pero los escalones 3–5 mandaban a guías de fuera del repo, y lo medido en las 2.731 fotos del viaje solo se usaba para el retoque | [`conceptos/12-como-mejorar.md`](../conceptos/12-como-mejorar.md): el método de una semana, **tu diagnóstico** (95 % con el tele, 0 % con el Viltrox, el 68 % en dos días, la noche oscura, la charca lenta), los cinco escalones con contenido del repo, una escalera de cuatro peldaños por tema y un plan de doce semanas desde casa |
| **Referentes** | Solo una lista de fauna, fuera del repo | [`conceptos/11-los-maestros.md`](../conceptos/11-los-maestros.md): 5 de fauna, 5 de cielo nocturno, 5 de calle (+ Masats), 5 de arquitectura, 3 de paisaje y 3 del tiempo (+ Molloy); cada foto con qué se ve, por qué es buena, por qué funciona, **su edición** y qué decisión copiar con el equipo del dueño. Fuentes: [notas](../notas-de-investigacion/maestros/fuentes.md) |
| **Safari** | Todo con el tele: nada sobre el animal en su paisaje con angular | Lecciones de van Oosten (24 mm), Nichols (24 mm) y du Toit (16–35 mm) en los maestros; la escalera de fauna, con práctica sin safari (perros, aves, deporte) |
| **Astro** | Las exposiciones largas del viaje salieron oscuras (mediana 28 sobre 255) y el repo no lo unía a la receta | «Por qué funciona» en los capítulos 8 y 9: histograma, JPEG no invariante, ISO 3200; Canarias como cielo cercano (Casado, López) |
| **Time-lapse** | Faltaba la idea de sacar **fotos** que cuenten el tiempo de una serie | Wilkes, Sugimoto, Kenna y Molloy en los maestros, con la versión sencilla en StarStaX; «Por qué funciona» en el capítulo 10 |

## La reordenación

- **Manejo:** las recetas se agrupan por tema. Antes: 6 astro, 7 estrellas, 8 safari, 9 charcas, 10 time-lapse, 11 estelas, 12 casa. Ahora: **fauna** 6 safari y 7 charcas · **cielo** 8 estrellas (desde cero), 9 astro (la noche completa) y 10 time-lapse · **ciudad y casa** 11 estelas, 12 calle y arquitectura (nuevo) y 13 casa. El resto se desplaza: 14 equipo, 15 Viltrox, 16 AF a fondo, 17 ajustes, 18 menú, 19 verificación de menús, 20 chuleta, 21 verificación in situ. La tabla completa, con el PDF de `sources/`, está en la [introducción de manejo](../manejo-a6700/00-introduccion.md#numeración-antigua).
- **Conceptos:** entran 11 (los maestros) y 12 (cómo mejorar); el glosario pasa de 11 a 13.
- **Retoques:** el capítulo 8 pasa a ser «Paisaje y ciudad».
- **Después del viaje:** los ejercicios «antes de volar» se llaman ahora solo «Ejercicio», y el plan de noches del 1 al 14 de noviembre sale de la chuleta (sigue en el capítulo 8) para dejar sitio a la calle y la arquitectura.
- El README de la raíz tenía el capítulo 5 antes que el 4; corregido. La RUTA tiene ahora la calle en la etapa 2, los maestros y el tiempo en la 3, y la etapa 4 remite al plan de mejora. La autoevaluación tiene 7 preguntas nuevas (C1–C4, A4–A6).

## Lo que queda

- **El test interactivo** está preparado con 63 preguntas, pero **sin republicar**: sus enlaces van a GitHub `main`, y los archivos renombrados aún no están subidos.
- **Sin probar en la cámara ni en Luminar** ([PENDIENTES § 11](../PENDIENTES.md#11--calle-arquitectura-la-hiperfocal-y-los-maestros-28-de-noviembre-de-2026)): si Transform aparece con JPEG, si el Viltrox conserva la zona tras apagar, la zona en AF-C, la distancia de enfoque en pantalla y el obturador electrónico con movimiento.
- **Los maestros:** de las 56 fotos o series analizadas, solo seis se han mirado directamente; el resto se describe con la fuente. Algunas páginas no se dejaron leer (MoMA, Art Institute of Chicago, NGA, The Met, Getty): sus datos vienen de resúmenes de buscador y están marcados en las notas. Rowell y Masats llevan una sola foto.
- **El Pixel** no tiene capítulo de calle; el de manejo remite a sus capítulos de personas y lentes.
- **Las guías de fuera del repo** (safari a fondo, mejores horas, la fauna animal por animal) siguen fuera, como decidió el dueño; los cinco escalones ya no dependen de ellas.
