# Las fotos del dueño: lo que se ha medido

Fuente: `~/Documents/Fotos/Namibia_2026` (solo lectura; no se modificó nada). Esta versión, del 22 de noviembre de 2026, **sustituye a la primera**, que describía varias cosas a ojo y contenía errores. Aquí todo sale de una medición y se dice cómo se midió.

## Cómo se midió

- **Metadatos** de los 2.731 JPEG con Spotlight (`mdls`) y la hora de la cámara con `sips -g creation`.
- **Brillo y color** de cada foto: miniatura de 120 px, media de los tres canales. "Luminancia" es 0,299 R + 0,587 G + 0,114 B, de 0 a 255. "R−B" es la media del rojo menos la del azul: positivo es cálido y negativo, frío. Es una medida de toda la foto, así que un cielo azul grande la baja aunque no haya dominante.
- **Polvo**: en las 454 fotos horizontales a f/7.1 o más cerrado se recortaron tres zonas de 300 × 300 px a tamaño real: dos donde se veían manchas en una foto y una de control entre ambas. En cada zona se comparó el brillo del centro con el de un anillo alrededor. Solo cuentan las 147 fotos con cielo liso en las tres zonas.
- **Siete fotos** se miraron a 1400 px. El ruido y los artefactos al 100 % **no** se han evaluado.

## Una corrección sobre las horas

La primera versión daba las horas una hora tarde. Spotlight convirtió la hora de la cámara suponiendo la zona horaria del Mac. La hora de la cámara (la que guarda el archivo) es la buena, y coincide con la hora de Namibia: en DSC00762, a las 21:45, el núcleo de la Vía Láctea está a unos 11° sobre el horizonte, que es donde corresponde a esa hora local y no una hora más tarde, cuando ya se habría puesto (cálculo propio con la posición del centro galáctico a 24° S). Todas las horas de abajo son las de la cámara.

Para situarlas: a mediados de noviembre, en Namibia amanece hacia las 06:00–06:15 y el sol se pone hacia las 19:05–19:20, según el lugar (cálculo propio con las fórmulas de la NOAA para Okaukuejo, Sesriem y Windhoek, con UTC+2).

## El conjunto

- 2.731 JPEG y 18 TIFF, 29 GB. Cámara ILCE-6700, firmware 2.00. JPEG de 6192 × 4128 (5 en vertical), perfil sRGB IEC61966-2.1, de 3,9 a 15,6 MB (mediana 10,7 MB).
- Fechas: del 1 al 12 de noviembre de 2026. El 68 % se hizo en dos días (el 11 y el 12).
- Objetivos: 2.601 fotos (95 %) con el Sony E 70-350 y 130 (5 %) con el Sony E 11 mm F1.8. **Ninguna con el Viltrox 25 mm.**
- Modo: manual 2.421 (89 %), prioridad de abertura 304, programa 6.
- Balance de blancos: 2.483 fotos (91 %) marcadas como "manual" (incluye los preajustes fijos y Kelvin) y 248 en automático. Spotlight no da el valor en Kelvin ni el preajuste, así que **no se sabe cuál era**.
- ISO: 772 fotos hasta 200 · 422 hasta 800 · 800 hasta 1600 · 452 hasta 3200 · 125 hasta 6400 · 160 por encima (máximo 12800). El 27 % pasa de ISO 1600 y el 10 %, de ISO 3200.
- Exposiciones largas: 53 de 8 s o más, todas con el 11 mm (15–20 s, f/1.8–2.2, ISO 1600–3200).
- Sin GPS en los archivos: los lugares que se nombran son por lo que se ve en la foto.
- Los 18 TIFF (misma numeración DSC) no se han abierto.

## Por horas

| Hora | Fotos | Luminancia (mediana) | R−B (mediana) |
|---|---|---|---|
| 06 | 261 | 97 | +7 |
| 07–09 | 319 | 99–115 | +2 a +14 |
| 10–14 | 349 | 100–139 | −17 a +5 |
| 15–17 | 587 | 112–114 | +26 a +37 |
| **18** | **1.009** | **107** | **−3** |
| 19 | 20 | 83 | +38 |
| 21–00 | 174 | 10–34 | +5 a +31 |

- **Las fotos de día no están subexpuestas.** De las 2.525 fotos entre las 06:00 y las 18:59, solo el 0,8 % tiene una luminancia por debajo de 70; la mediana es 109. La primera versión decía que la subexposición era habitual al atardecer: era falso.
- **La hora de las 18:00** (1.009 fotos, la última antes de la puesta de sol) es la única franja de tarde con R−B negativo, es decir, algo más fría que las de las 15:00–17:00. Es compatible con sujetos a la sombra y balance de blancos fijo, pero la medida no distingue la causa.
- **Las exposiciones largas son oscuras:** luminancia mediana 28 sobre 255 (entre 1 y 72).
- **Charca de noche:** 122 fotos con el 70-350 a ISO 6400 o más; mediana de R−B +27 (naranja). **116 de las 122 se hicieron más lentas que 1/60 s.**

## Polvo en el sensor

- Una mancha está **confirmada**: hacia el 34 % del ancho y el 8 % del alto (arriba, en el tercio izquierdo). En 99 de las 147 fotos con cielo liso, el centro de esa zona es al menos un 1 % más oscuro que su entorno. En la zona de control, en ninguna. Aparece en fotos de seis días distintos, del 5 al 12 de noviembre.
- En DSC00149 (11 mm, f/11) se ven además otras dos manchas a su izquierda. Esas **no** se repiten en el resto del conjunto.
- A f/7.1 la mancha es tenue (mediana −1,4 %); a f/8–f/10 se nota más (hasta −2 %).

## Las siete fotos revisadas

Valores medios de color medidos en copias de 700 px.

1. **DSC00056** (11 mm, f/1.8, 20 s, ISO 3200, 23:02). Nubes de Magallanes, acacia y edificio en silueta. Cielo cálido, marrón (R 53, G 47, B 36), con una banda verdosa junto al horizonte y un punto de luz blanca.
2. **DSC00762** (11 mm, f/2, 20 s, ISO 1600, 21:45). Núcleo de la Vía Láctea bajo. Cielo muy oscuro y neutro (R 37, G 39, B 36); el 21 % de la foto es negro (los tres canales por debajo de 8).
3. **DSC00149** (11 mm, f/11, 1/80 s, ISO 100, 06:49). Árboles muertos sobre un suelo de arcilla clara entre dunas rojas (por el aspecto, Deadvlei). Persona y árbol en sombra; duna al sol sin quemar (R 191, G 114, B 64); suelo en sombra con una dominante fría leve (R 75, G 81, B 80). Tres manchas de polvo en el cielo. Otros turistas en el encuadre.
4. **DSC01825** (128 mm, f/7.1, 1/1250 s, ISO 200, 09:02). Jirafa centrada, a media mañana. Foto neutra y con poco contraste (R 141, G 138, B 137); cielo gris azulado pálido. Un borrón naranja desenfocado en la esquina inferior derecha.
5. **DSC02462** (350 mm, f/6.3, 1/500 s, ISO 1250, 16:58). Guepardo que ocupa en torno al 10 % del ancho. Hierba cálida (R 127, G 106, B 77) y cielo gris. **No es fría ni está subexpuesta**, como decía la primera versión: es una foto apagada, de cielo cubierto, dos horas antes de la puesta de sol.
6. **DSC01526** (87 mm, f/5, 1/25 s, ISO 12800, 00:00). Elefantes en una charca con focos. En el elefante: R 179, G 65, B 1. **El canal azul está vacío** (el 95 % de esos píxeles tiene el azul a 5 o menos) y el rojo **no** está recortado, al contrario de lo que suponía la primera versión. El 38 % de la foto es negro.
7. **DSC03658** (163 mm, f/5.6, 1/500 s, ISO 2000, 18:24). León bostezando a la sombra de un arbusto, unos tres cuartos de hora antes de la puesta de sol. Dominante fría clara: el suelo claro mide R 156, G 176, B 199. Bien expuesta.

## Lo que se sostiene y lo que no

- **Se sostiene:** el polvo (una mancha fija); las exposiciones largas oscuras; la charca naranja, con el azul vacío y casi siempre por debajo de 1/60 s; los sujetos pequeños con el 70-350; el balance de blancos fijo en el 91 %; el volumen concentrado en dos días.
- **No se sostiene:** que las fotos de la tarde estén subexpuestas; que haya una dominante fría general (está medida en una foto a la sombra y, de forma leve, en la franja de las 18:00); que el rojo esté recortado bajo los focos; las horas de la primera versión.
