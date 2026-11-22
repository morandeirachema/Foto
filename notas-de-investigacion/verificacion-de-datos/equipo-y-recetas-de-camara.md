# Verificación de datos: equipo, cifras técnicas, recetas de campo y referencias externas (capítulos 01, 05–11 de `manejo-a6700/`)

Fecha de la verificación: 22 de noviembre de 2026. Ámbito: `01-de-movil-a-la-a6700.md`, `05-enfocar-el-11mm.md`, `06-astrofotografia-namibia.md`, `07-estrellas-con-tierra.md`, `08-safari-diurno.md`, `09-safari-nocturno-charcas.md`, `10-equipo-accesorios.md`, `11-viltrox-25mm.md`. No se han revisado nombres ni rutas de menú (otro investigador) ni `guia-completa.md`.

**Cómo leer estas notas**

- Clases: **OK** · **ERROR** · **SIN FUENTE** · **IMPRECISO** · **DESACTUALIZADO**.
- Un OK lleva una de tres marcas de evidencia:
  - `[P]` página descargada y leída en esta sesión (URL exacta);
  - `[C]` recalculado aquí (fórmula y datos a la vista; scripts en el scratchpad);
  - `[B]` solo resultado de buscador con URL (no pude abrir la página: Sony, B&H, PcComponentes, DPReview y The-Digital-Picture devuelven 403 a clientes automáticos). Un OK `[B]` es más débil: conviene que alguien abra la página en un navegador.
- Abreviaturas de fuentes:
  - **HG-espec** = <https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html>
  - **HG-ráfaga** = <https://helpguide.sony.net/ilc/2320/v1/es/contents/0407C_drivemode_continuous.html>
  - **HG-intervalo** = <https://helpguide.sony.net/ilc/2320/v1/es/contents/0407P_interval_shoot_setting.html>
  - **HG-obturador** = <https://helpguide.sony.net/ilc/2320/v1/es/contents/0414H_shutter_type.html>
  - **HG-caja** = <https://helpguide.sony.net/ilc/2320/v1/es/contents/0101L_supplied_items.html>
  - **AlphaShooters** = <https://www.alphashooters.com/cameras/sony-a6700/memory-cards/>
  - **Abbott-70350** = <https://dustinabbott.net/2022/05/sony-e-70-350mm-f4-5-6-3-g-oss-review/> (leída en la copia de <https://web.archive.org/web/2026/https://dustinabbott.net/2022/05/sony-e-70-350mm-f4-5-6-3-g-oss-review/>)
  - **Abbott-11** = <https://dustinabbott.net/2022/06/sony-e-11mm-f1-8-review/> (leída en la copia de web.archive.org equivalente)
  - **DCW** = <https://www.digitalcameraworld.com/cameras/lenses/viltrox-af-25mm-f-1-7-air-review>
- Scripts y descargas (fuera del repo): `/private/tmp/claude-501/-Users-chema-code-Foto/e8219b34-1511-4ce6-aae0-d7c276094f52/scratchpad/verif-equipo/` (`optica.py`, `astro.py`, `check_urls.sh`, `urls_estado.txt`).

**Totales (150 comprobaciones):** OK 105 (de ellos 13 solo `[B]`) · ERROR 3 · IMPRECISO 13 · DESACTUALIZADO 2 · SIN FUENTE 27.

Cómo se cuenta: 134 comprobaciones numeradas en las secciones 1–4 (la #130 vale por dos; los bloques #32–#34, #78 y #133 agrupan varias afirmaciones afines) más 16 sin numerar en las secciones 5 y 6. Por sección: cuerpo 34 (OK 21, ERROR 3, IMPRECISO 4, SIN FUENTE 6) · objetivos 44 (OK 32, IMPRECISO 1, DESACTUALIZADO 2, SIN FUENTE 9) · óptica 25 (OK 22, IMPRECISO 2, SIN FUENTE 1) · astronomía y lugares 31 (OK 22, IMPRECISO 4, SIN FUENTE 5) · software, URL y safari 16 (OK 8, IMPRECISO 2, SIN FUENTE 6).

**Lo más importante, en cuatro líneas**

1. La tabla de tarjetas del capítulo 10 (tiempos de vaciado y «ráfaga antes de atascarse») no coincide con la fuente que el propio capítulo cita (ERROR, tres celdas/frases).
2. El precio del 70-350 nuevo (570–650 €) queda muy por debajo de lo que muestran las tiendas españolas (~860 €; PVP Sony 900 €) y arrastra el total del kit (DESACTUALIZADO).
3. La óptica (hiperfocales, límites cercanos, equivalencias, pasos) está bien calculada con un círculo de confusión de 0,020 mm; el único reparo es atribuir «≈ 20 s» a la calculadora de PhotoPills.
4. La astronomía de noviembre de 2026 cuadra con el cálculo de efemérides, con tres matices (conjunción Júpiter–Marte, culminación de Saturno, declinación magnética en Etosha).

---

## 1. Cuerpo Sony ILCE-6700: especificaciones

### Takeaway
Todas las cifras del cuerpo que la guía toma de Sony (26 Mpx, UHS-II, sin cargador, NP-FZ100, 11 fps, búfer 1.000/59/23, ~10 fps en RAW sin pérdida, ±5 EV, intervalómetro, BULB) coinciden con la Guía de ayuda oficial. Fallan la tabla de tiempos de tarjeta, una frase sobre los ISO «expandidos» y la frase «a 11 fps con RAW sin pérdida».

### Cited Findings

| # | Archivo:línea | Texto de la guía | Qué dice la fuente | Clase |
|---|---|---|---|---|
| 1 | 10:57 | «26 Mpx APS-C» | «Sensor de imagen CMOS de tamaño APS-C (23,3 mm × 15,5 mm)… Aprox. 26 000 000 píxeles» — HG-espec | OK `[P]` |
| 2 | 01:53, 10:57 | factor «1,5» | 36/23,3 = 1,545; diagonal 43,27/27,99 = 1,546. «1,5» es el redondeo convencional de Sony | OK `[C]` |
| 3 | 10:62, 10:142 | ranura «SD UHS-II» | «Esta cámara solo admite tarjetas de memoria SD (compatibles con UHS-II)» — <https://helpguide.sony.net/ilc/2320/v1/es/contents/0002H_usable_memory_card.html> | OK `[P]` |
| 4 | 01:198, 10:62 | «una sola ranura» | Ninguna página leída lo dice con esas palabras (HG-espec solo dice «Tarjetas SD») | SIN FUENTE |
| 5 | 10:66, 10:193 | «La caja no trae cargador» | Elementos suministrados: cámara, NP-FZ100, correa, tapas, caperuza, guías. Sin cargador ni adaptador — HG-caja | OK `[P]` |
| 6 | 10:66, 10:194 | carga por USB-C, power bank | «Terminal USB Type-C… Compatible con suministro de alimentación USB» — HG-espec; existe la página «Carga de la batería con un dispositivo compatible con USB-PD» (<https://helpguide.sony.net/ilc/2320/v1/es/contents/0001D_charge_commercially_available_acadaptor.html>, título leído en el índice) | OK `[P]` |
| 7 | 10:192 | batería «NP-FZ100» | «NP-FZ100 Batería recargable (1)» — HG-caja | OK `[P]` |
| 8 | 10:53 | IBIS «de ~5 pasos» | Photography Life cita «5.0 stops» para foto — <https://photographylife.com/news/sony-a6700-announcement> (resultado de buscador). HG-espec no da cifra | OK `[B]` |
| 9 | 08:26 | «Hi+ (11 fps)» | «(Captura continua: Hi+): Máximo de aprox. 11 imágenes por segundo»; Hi 8, Mid 6, Lo 3 — HG-espec | OK `[P]` |
| 10 | 08:26 | «en Hi+ el visor no va en tiempo real durante la ráfaga» | «El motivo no se visualiza en tiempo real en el monitor o visor cuando se toma en modo [Captura continua: Hi+]» — HG-ráfaga | OK `[P]` |
| 11 | 10:171–173 | búfer «1.000 JPEG, 59 RAW comprimido, 23 RAW comprimido sin pérdida» | «JPEG/HEIF (Fina) Aprox. 1 000 imágenes o más · RAW comprimido Aprox. 59 · RAW comprimido sin pérdida Aprox. 23» — HG-ráfaga | OK `[P]` |
| 12 | 10:174 | «en RAW sin pérdida la ráfaga va a ~10 fps» | «Durante la toma en formato RAW sin pérdida (lossless), el máximo es de aproximadamente 10 imágenes por segundo» — HG-espec. Ojo: AlphaShooters midió 7 fps («Note this drops from 11fps to 7fps when shooting lossless compressed RAW», con obturador electrónico) | OK `[P]` (con conflicto anotado) |
| 13 | 10:161–162 | «A 11 fps con RAW comprimido sin pérdida, la cámara genera del orden de 300 MB/s» | Contradice la línea 174 del mismo capítulo y a Sony: en sin pérdida son ~10 fps. 35,8 MB/foto (AlphaShooters) × 10 = 358 MB/s | IMPRECISO |
| 14 | 10:162 | «ninguna tarjeta del mundo sigue ese ritmo» | La escritura más rápida medida en cámara es ~230 MB/s (Sony SF-G Tough) — AlphaShooters | OK `[P]` |
| 15 | 10:168 | «Vaciar el búfer tras 30 RAW: UHS-I V30 18–22 s · V60 8–9 s · V90 4–6 s» | AlphaShooters (la fuente citada en 10:268) mide, hasta llenar el búfer: RAW sin pérdida → UHS-I 6,5–8,8 s · V60 4,0–5,5 s · V90 2,5–4,1 s; RAW comprimido → UHS-I 10,4–15,2 s · V60 5,7–8,1 s · V90 3,7–4,1 s. Ninguna prueba «tras 30 RAW»; y con 23 de búfer oficial, «30 RAW» sin pérdida no caben | ERROR |
| 16 | 10:167 | «Ráfaga antes de atascarse: UHS-I ~15–18 RAW · V60 el búfer entero · V90 el búfer entero» | AlphaShooters, RAW sin pérdida: UHS-I 17–21 · V60 25–35 · V90 89–376 disparos. La tarjeta sí cambia la profundidad de ráfaga, no solo el vaciado | ERROR |
| 17 | 10:178–179 | «con una V30 te comes veinte segundos de cámara bloqueada… Con una V60, ocho» | Derivado de la fila anterior: medidos 6,5–8,8 s (UHS-I) y 4,0–5,5 s (V60) en sin pérdida — AlphaShooters | ERROR |
| 18 | 10:150–152 | «las V30 del mercado son UHS-I… las V60 y V90 son UHS-II» | En la tabla de AlphaShooters la Sony SF-E es UHS-II y figura como V30 (y como V60 en su ficha): hay excepciones | IMPRECISO |
| 19 | 08:19, 08:88–89 | ISO Auto «100–12800» | «[ISO AUTO] (ISO 100 a ISO 6 400, se puede ajustar máximo/mínimo)» — HG-espec | OK `[P]` |
| 20 | 09:93–96 | «25600 queda castigado… Los ISO expandidos por encima ni tocarlos» | El rango nativo llega a ISO 32000; el ampliado va de 40000 a 102400 (y 50–80 por abajo): «ISO 100 a ISO 32 000 (ISO ampliado: mínimo ISO 50, máximo ISO 102 400)» — HG-espec | IMPRECISO |
| 21 | 08:80 | compensación «±5 EV» | «Compensación de exposición ±5,0 EV» — HG-espec | OK `[P]` |
| 22 | 06:165 | intervalómetro «hasta 9999 tomas» | «Número de capturas… (de 1 toma a 9 999 tomas)» — HG-intervalo | OK `[P]` |
| 23 | 06:99, 07:265 | «el intervalo se mide de inicio a inicio» | «Intervalo de toma… (el tiempo desde que comienza una exposición hasta que comienza la exposición para la siguiente toma). (de 1 segundo a 60 segundos)» — HG-intervalo | OK `[P]` |
| 24 | 07:226–228, 07:354 | BULB solo con mecánico; `Aj. temporiz. BULB` 2–900 s | «Exposure Time… (2 seconds to 900 seconds)» — <https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_bulb_timer.html>; «Toma BULB» no disponible con obturador electrónico — HG-obturador; mecánico «1/4 000 a 30 segundos, BULB», electrónico «1/8 000 a 30 segundos» — HG-espec | OK `[P]` |
| 25 | 09:54–57, 09:114 | con electrónico no hay flash, `RR exposic. larga`, `e-Prim. cortin. obtur.`, BULB ni toma sin parpadeo | Lista literal idéntica — HG-obturador | OK `[P]` |
| 26 | 10:256 | limpieza: «Batería al 51 % o más» | «Asegúrese de que el nivel de batería restante sea igual o superior al 51%» — <https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_cleaning_mode.html> | OK `[P]` |
| 27 | 10:257–259 | pasos de limpieza (vibración, soplador, cámara hacia abajo, sin espray) | Mismos pasos y la nota «No utilice un soplador de tipo r[ociador]» — misma página | OK `[P]` |
| 28 | 05:45, 05:91, 06:66, 11:46 | `Verificac. luminosa` solo en MF y en P/A/S/M | Se cancela «Cuando el modo de toma se cambia de P/A/S/M a un modo que no es P/A/S/M» y «Cuando se ajusta el modo de enfoque a algo distinto de enfoque manual» — <https://helpguide.sony.net/ilc/2320/v1/es/contents/0414H_bright_monitoring.html> | OK `[P]` |
| 29 | 10:45 | «salió a 1.700 € en 2023» | Las notas de lanzamiento encontradas solo dan dólares (1.398–1.400 $) y libras (1.450 £) — <https://www.techradar.com/cameras/mirrorless-cameras/sony-a6700-review>. No encontré el precio en euros | SIN FUENTE |
| 30 | 10:21, 10:45 | a6700 «~1.000–1.200 € nueva» | Agregador español Globerada: 995–997 € (Fnac, Carrefour) hasta 1.999 € — <https://www.globerada.com/precios/sony-alpha-6700-body.html>; PcComponentes 1.538 € — <https://www.pccomponentes.com/camara-mirrorless-sony-alpha-6700-ilce-6700-cuerpo-26mp-4k-wifi-bluetooth> (ambos `[B]`, sin fecha). El rango de la guía es el extremo barato del mercado | IMPRECISO |
| 31 | 10:46 | «~800–950 € usada en mpb» | mpb.com devuelve 403; no pude ver precios | SIN FUENTE |

**Correcciones propuestas**

- #13 (10:161): «En ráfaga con RAW comprimido sin pérdida (~10 fps y unos 36 MB por foto), la cámara genera del orden de 350 MB/s: ninguna tarjeta sigue ese ritmo (la más rápida medida en cámara escribe a ~230 MB/s).»
- #15–#16 (10:165–169), tabla rehecha con las medidas de Alpha Shooters en RAW comprimido sin pérdida:

  | | UHS-I V30 | UHS-II V60 | UHS-II V90 |
  |---|---|---|---|
  | Ráfaga antes de atascarse | ~17–21 RAW | ~25–35 RAW | ~90–375 RAW |
  | Vaciar el búfer lleno | **6,5–9 s** | **4–5,5 s** | **2,5–4 s** |

  (Si se prefiere RAW comprimido: 33–35 / 38–47 / 78–91 disparos y 10–15 s / 6–8 s / ~4 s.)
- #17 (10:178): «con una V30 son unos **ocho segundos** de cámara bloqueada justo en medio. Con una V60, cuatro o cinco.»
- #18 (10:150): «en la práctica **casi todas** las V30 del mercado son UHS-I…».
- #20 (09:93–96): «…**25600** queda castigado (ruido de color en las sombras). El rango nativo acaba en ISO 32000; los ISO ampliados (de 40000 a 102400) ni tocarlos…».
- #29 (10:45): quitar la cifra o citar fuente: «(salió en julio de 2023 y hoy se ve bastante por debajo de su precio de lanzamiento: compara antes de comprar)».
- #30 (10:21, 10:45): «**~1.000–1.500 € nueva** según tienda (las mejores ofertas rondan los 1.000 €)».

### Inferences
- La guía no afirma en estos capítulos ni la sensibilidad AF (−3 EV), ni el peso del cuerpo, ni la autonomía, ni el sellado. Para quien los añada: «Rango de sensibilidad –3 EV a +20 EV (en equivalente a ISO 100, F2,0)» (HG-espec) y «Modo de pantalla Aprox. 570 imágenes / Modo de visor Aprox. 550 imágenes» (<https://helpguide.sony.net/ilc/2320/v1/es/contents/0001D_batterylife_recordable.html>). El peso «493 g con batería y tarjeta» solo lo vi en resultados de buscador (<https://www.slrlounge.com/sony-a6700-review/>).
- La regla «ráfagas de 1–2 s» sigue siendo válida con las cifras de Sony: 23 fotos ÷ 10 fps = 2,3 s.
- Alpha Shooters mide con tarjetas V60 rápidas 25–35 disparos sin pérdida antes de frenar, más que los 23 oficiales: el búfer real depende de la tarjeta.

### Gaps
- No pude abrir ninguna página de producto de sony.es / sony.com (403): estabilización en pasos, peso y redacción del sellado quedan sin fuente primaria.
- Definiciones V30/V60/V90, límites de bus (104 y 312 MB/s) y «dos filas de contactos = UHS-II» (10:148–159): no consulté la SD Association → **SIN FUENTE** (3 afirmaciones, #32–#34).
- Precios de tarjetas (20–30 €, 50–90 €, 120–180 €), lector, SSD, cargador doble: no comprobados → ver sección 5.

---

## 2. Objetivos: Sony E 11mm F1.8, Sony E 70-350mm G OSS, Viltrox AF 25mm F1.7 Air

### Takeaway
Las fichas de los tres objetivos son correctas en todo lo que pude contrastar. Quedan sin fuente tres detalles del 70-350 (lado de los mandos, detección automática de barrido, «0,23x a 350 mm») y el comportamiento en las esquinas del 11 mm. Los escalones de apertura del 70-350 coinciden con The-Digital-Picture, pero solo pude verlo en el buscador.

### Cited Findings

**Sony E 11mm F1.8 (SEL11F18)**

| # | Archivo:línea | Texto de la guía | Qué dice la fuente | Clase |
|---|---|---|---|---|
| 35 | 10:89 | «181 g» | Sony (fichas regionales): 181 g — <https://www.sony.co.uk/electronics/support/lenses-e-mount-lenses/sel11f18/specifications>. Abbott-11 pesó 179 g | OK `[B]` |
| 36 | 10:89, 10:221, 11:26 | rosca de «55 mm» | «the Sony at 55mm» — Abbott-11 | OK `[P]` |
| 37 | 05:27–28, 10:85 | interruptor AF/MF y botón de retención de foco | «a focus hold button… along with an AF/MF switch» — Abbott-11 | OK `[P]` |
| 38 | 05:31, 10:82 | sin anillo de diafragma (apertura con la rueda) | «we have no aperture ring here, so aperture will have to be controlled from within the camera» — Abbott-11 | OK `[P]` |
| 39 | 05:30, 10:93 | sin estabilizador óptico | Ninguna fuente leída lo menciona de forma expresa | SIN FUENTE |
| 40 | 10:91 | «Enfoca desde 15 cm» | Sony: 0,15 m (AF) / 0,12 m (MF); ampliación 0,13x (AF) / 0,20x (MF) — <https://www.sony.co.uk/electronics/support/lenses-e-mount-lenses/sel11f18/specifications> y B&H (buscador). Abbott-11 lo escribe al revés («12cm (Autofocus…) or 15cm (Manual Focus…)») | OK `[B]` |
| 41 | 01:54, 10:77 | «16,5 mm equivalentes» | 11 × 1,5 = 16,5 | OK `[C]` |
| 42 | 10:79–81 | «un tercio de paso por encima de los f/2 y dos pasos sobre el f/3.5… la cuarta parte de ISO» | 2·log2(2/1,8) = 0,30 pasos; 2·log2(3,5/1,8) = 1,92 pasos; factor de luz 3,78 | OK `[C]` |
| 43 | 05:31, 05:94, 06:35, 06:114 | esquinas con «alitas» a f/1.8, se arreglan a f/2.8 | No localicé el pasaje de coma en Abbott-11 (la búsqueda de «coma» en la copia no devolvió texto) | SIN FUENTE |
| 44 | 05:11, 05:29, 06:85 | anillo de enfoque electrónico | Abbott-11 habla de «Linear manual focus» (respuesta lineal), no describe topes ni infinito | SIN FUENTE |
| 45 | 10:73 | precio «~400–550 € nuevo» | Galaxus 569,51 €, LDLC 599,95 € (resultados de buscador, sin fecha) — <https://www.ldlc.com/en/product/PB00503608.html> | IMPRECISO |
| 46 | 10:73 | «~330–420 € usado en mpb» | MPB: unidades usadas a 374 € y 409–429 € — <https://www.mpb.com/en-eu/product/sony-e-11mm-f2f18> (buscador) | OK `[B]` |

**Sony E 70-350mm F4.5-6.3 G OSS (SEL70350G)** — prestado, y la guía lo dice (no es error)

| # | Archivo:línea | Texto de la guía | Qué dice la fuente | Clase |
|---|---|---|---|---|
| 47 | 08:122, 10:106, 10:113 | «625 g» | «The 70-350G weighs in at 625g» — Abbott-70350 | OK `[P]` |
| 48 | 10:89, 10:222 | rosca de «67 mm» | «a common 67mm front filter thread» — Abbott-70350 | OK `[P]` |
| 49 | 08:97–100 | interruptores AF/MF y OSS; el OSS «No tiene modos: es un ON/OFF» | «a bank with two basic switches (AF/MF and ON/OFF for the stabilizer). Premium telephotos will typically add a focus limiter and different stabilizer modes» — Abbott-70350 | OK `[P]` |
| 50 | 08:101–102 | bloqueo de zoom «solo engancha con el zoom en 70 mm» | «a zoom lock that works only at the 70mm position» — Abbott-70350 | OK `[P]` |
| 51 | 08:103, 10:106 | botón de retención de foco | «There is also a focus hold button on the side» — Abbott-70350 | OK `[P]` |
| 52 | 08:106 | no tiene limitador de enfoque | Misma cita que #49 | OK `[P]` |
| 53 | 10:134 | «ampliación máxima 0,23x» | «Minimum focus distance here is 1.1m (3.61′), giving us a useful… 0.23x magnification» — Abbott-70350 | OK `[P]` |
| 54 | 10:134 | «…a 350 mm» | La reseña no dice a qué focal se alcanza | SIN FUENTE |
| 55 | 10:106 | «motor lineal XD» | «Sony's advanced XD Linear Motor technology» — Abbott-70350 | OK `[P]` |
| 56 | 09:32, 09:90, 10:126–127 | apertura máxima: f/5 hasta 113 mm, f/5.6 de 114 a 199, f/6.3 desde 200 | «70-81mm = f/4.5 / 82-113mm = f/5.0 / 114-199mm = f/5.6 / 200-350mm = f/6.3» — <https://www.the-digital-picture.com/Reviews/Lens-Specifications.aspx?Lens=1770> (403 al abrirla; texto visto en el buscador). Sony solo publica «4.5–6.3» | OK `[B]` |
| 57 | 08:94–95 | «son cuatro y están todos en el lado izquierdo del barrilete» | Abbott-70350 no sitúa el bloqueo de zoom; no encontré otra fuente | SIN FUENTE |
| 58 | 08:99–100 | «el objetivo detecta él solo cuándo estás barriendo» | No aparece en Abbott-70350 ni en lo consultado de Sony | SIN FUENTE |
| 59 | 08:106 | no tiene «puerto USB ni modo macro» | No lo afirma ninguna fuente leída (tampoco lo contradice) | SIN FUENTE |
| 60 | 10:106, 10:21 | precio «~570–650 € nuevo» | PcComponentes 859,73 € y Codi-tek 859 € — <https://www.pccomponentes.com/sony-e-70-350mm-f45-63-g-oss>; PVP Sony 900 € — <https://www.sony.ie/electronics/camera-lenses/sel70350g/reviews-ratings> (buscador, sin fecha; una reseña de febrero de 2026 habla de 550 € «con cashback») | DESACTUALIZADO |
| 61 | 10:21–23 | kit «≈ 2.000–2.400 € nuevo» | Con 860 € para el tele: 1.000–1.200 + 400–550 + 860 ≈ 2.260–2.610 €. Aritmética interna de la guía correcta (1.970–2.400), pero hereda #60 | DESACTUALIZADO |
| 62 | 10:113–114 | «un tercio de lo que pesa un 150-600» | 625 / 2.100 = 0,30 (usando el 2,1 kg que da la propia guía; el peso del Sigma no lo verifiqué) | OK `[C]` |

**Viltrox AF 25mm F1.7 Air (montura E)** — fuente: DCW, leída entera

| # | Archivo:línea | Texto de la guía | Qué dice DCW | Clase |
|---|---|---|---|---|
| 63 | 10:38, 11:11, 11:27 | «170 g» | 170 g (6 oz) | OK `[P]` |
| 64 | 10:38, 11:26 | filtro «52 mm» | 52 mm | OK `[P]` |
| 65 | 11:21 | «12 elementos en 10 grupos: 1 ED, 2 asféricos y 2 de alto índice» | 12 elementos en 10 grupos, 1 ED, 2 asféricos, 2 de alta refracción | OK `[P]` |
| 66 | 11:20 | «f/1.7 a f/16, diafragma de 9 láminas» | f/1.7–f/16, 9 láminas | OK `[P]` |
| 67 | 11:22 | «0,3 m (ampliación máxima 0,11x)» | 0,3 m; 0,11x | OK `[P]` |
| 68 | 11:23 | motor «paso a paso de husillo (STM)» | «lead-screw stepping motor» | OK `[P]` |
| 69 | 11:24 | anillo electrónico | «the focus ring is electronically coupled» | OK `[P]` |
| 70 | 10:39, 11:25 | sin interruptor AF/MF, sin anillo de diafragma, sin botones | «No aperture control ring», «No AF/MF switch», «no fancy function buttons nor additional control rings» | OK `[P]` |
| 71 | 11:27 | «unos 64 × 54 mm» | 64 × 54 mm | OK `[P]` |
| 72 | 11:29 | «No tiene juntas de sellado, según… Digital Camera World» | «the Viltrox doesn't feature any weather-seals» | OK `[P]` |
| 73 | 11:29 | «algún vendedor dice lo contrario» | La ficha de B&H citada devuelve 403 y no tiene copia en archive.org | SIN FUENTE |
| 74 | 11:30, 11:80 | puerto USB-C en la montura para firmware | «The mounting plate… features a USB-C port for applying firmware updates» | OK `[P]` |
| 75 | 11:55 | AF «no especialmente rápido, pero suficiente» y preciso | «Autofocus isn't really snappy but it's certainly quick enough for most needs… it proved consistently accurate throughout my testing» | OK `[P]` |
| 76 | 11:76 | las fuentes no evalúan su uso en astro | En DCW no aparece ni «coma» ni astrofotografía | OK `[P]` |
| 77 | 01:62, 11:19 | «37,5 mm equivalentes» | 25 × 1,5 = 37,5 | OK `[C]` |

**Correcciones propuestas**

- #45 (10:73): «~400–600 € nuevo».
- #54 (10:134): «Su ampliación máxima es 0,23x (a la distancia mínima de 1,1 m)».
- #57 (08:94–95): «(son cuatro: dos interruptores juntos en el lado izquierdo del barrilete, el botón de retención y el bloqueo de zoom; revísalos cada mañana…)», o comprobarlo con el objetivo en la mano.
- #58 (08:99–100): «No tiene modos: es un ON/OFF.» (quitar la frase del barrido salvo que se cite fuente).
- #60 (10:21 y 10:106): «70-350 G OSS (~850–900 € nuevo; 550–650 € con cashback o en oferta puntual)».
- #61 (10:21–23): «≈ **2.250–2.650 € nuevo**».

### Inferences
- Abbott-70350 mide una estabilización útil de unas seis paradas («1/6th of a second, 350mm… roughly six stops»): respalda el «margen real» de 08:121, sin cifra oficial.
- Los dos Sony están descritos como «Dust and moisture resistant design» en la lista de características que reproduce Abbott; la guía no lo afirma, así que no hay nada que corregir.

### Gaps
- Fichas oficiales de sony.es: inaccesibles (403). `https://www.sony.es/lenses/products/sel70350g` no tiene copia de 2026 en archive.org; la de `sel11f18` sí, pero sin texto extraíble.
- Pesos y precios de las alternativas (Sigma 16 mm, Samyang 12 mm, FE 70-300 G, Sigma 150-600, FE 200-600 G, Tamron 150-500; 10:95–110): no comprobados → **SIN FUENTE** (#78, en bloque).
- Página del Viltrox en viltrox.com: solo comprobé que la portada responde (200), no la ficha.

---

## 3. Aritmética óptica: hiperfocales, profundidad de campo, trazas, equivalencias y pasos

### Takeaway
Todas las hiperfocales y límites cercanos de los capítulos 5 y 11 salen exactos con un círculo de confusión de **0,020 mm** (el que usa el repo; yo usé el mismo y contrasté con 0,019 y 0,015). El «~4 m» del 11 mm a f/1.8 es un redondeo prudente (3,4 m calculados). El punto débil es la cifra de trazas: «≈ 20 s según Spot Stars» no la pude reproducir.

### Cited Findings

Fórmulas: H = f²/(N·c) + f; enfocado a H, nítido desde H/2; enfocado a infinito, nítido desde H; límite cercano enfocando a s: H·s/(H + s − f). Script: `optica.py`.

| # | Archivo:línea | Texto de la guía | Recalculado (c = 0,020 mm) | Clase |
|---|---|---|---|---|
| 79 | 05:59 | 11 mm f/2.8 → enfoca a 2,2 m, nítido desde ~1,1 m | H = 2,17 m; H/2 = 1,09 m | OK `[C]` |
| 80 | 05:60 | f/4 → 1,5 m / ~0,75 m | 1,52 / 0,76 | OK `[C]` |
| 81 | 05:61 | f/5.6 → 1,1 m / ~0,55 m | 1,09 / 0,55 | OK `[C]` |
| 82 | 05:62 | f/8 → 0,8 m / ~0,40 m | 0,77 / 0,38 | OK `[C]` |
| 83 | 05:63 | f/11 → 0,6 m / ~0,30 m | 0,56 / 0,28 | OK `[C]` |
| 84 | 05:18, 05:65 | f/8 enfocando a ~1 m: «nítido desde ~0,4 m hasta el infinito» | cercano 0,44 m; 1 m > H (0,77 m), luego llega a infinito | OK `[C]` |
| 85 | 05:21, 05:23, 05:93, 07:119–130, 07:160 | 11 mm a f/1.8 enfocado a estrellas: nítido «a más de ~4 m» | H = 3,37 m (c = 0,020); 3,55 m (0,019); 4,49 m (0,015). «~4 m» redondea hacia el lado seguro | OK `[C]` |
| 86 | 05:23, 11:69, 11:91 | 25 mm a f/1.7: nítido «a más de ~18 m» | H = 18,4 m | OK `[C]` |
| 87 | 11:61 | 25 mm f/5.6 → 5,6 m / ~2,8 m | 5,61 / 2,80 | OK `[C]` |
| 88 | 11:62 | f/8 → 3,9 m / ~2 m | 3,93 / 1,97 | OK `[C]` |
| 89 | 11:63 | f/11 → 2,8 m / ~1,4 m | 2,87 / 1,43 (2,9 redondeando) | OK `[C]` |
| 90 | 06:110, 06:194–195 | «calculadora "Spot Stars" de PhotoPills: con el 11 mm en APS-C, ~20 s… hasta 25 s» | No pude ejecutar la app. PhotoPills explica que su NPF «Default» deja moverse a la estrella su diámetro y que la regla del 500 «gives you a longer exposure time… than what you would need» — <https://www.photopills.com/articles/milky-way-photography-guide> (copia de archive.org). Regla del 500: 500/16,5 = 30,3 s. NPF simplificada (35·N + 30·p)/f con p = 3,76 µm: 16,0 s a f/1.8. 20 s queda entre ambas; es un punto de partida razonable, pero no es «lo que da Spot Stars» | SIN FUENTE |
| 91 | 11:73 | «regla del 500, aproximada: 500 ÷ 37,5 ≈ 13 s» | 13,3 s. Aviso: la NPF simplificada da 6,9 s a f/1.7; a 10–13 s habrá trazas visibles al 100 % | OK `[C]` |
| 92 | 07:318–319 | «a 70 mm y f/4.5 el límite sin trazas son ~5 s» | 500/105 = 4,8 s (NPF simplificada 3,9 s) | OK `[C]` |
| 93 | 01:54, 01:60–64, 08:120 | 70-350 → 105–525 mm equivalentes; «≈ 21x» | 105 y 525; 525/25 = 21 (525/24 = 21,9) | OK `[C]` |
| 94 | 09:91–92 | «te ahorras entre un tercio y dos tercios de paso» | f/6.3→f/5.6 = 0,34 pasos; f/6.3→f/5 = 0,67 | OK `[C]` |
| 95 | 01:40–45 | listas de pasos (1/250→1/500…, ISO 800→1600…, f/2.8→f/4…) | Cada salto es ×2 de luz | OK `[C]` |
| 96 | 07:226–229 | prueba de giro: 240 s, ISO 200, f/2.8 | Frente a 30 s e ISO 800–1600 a f/2.8: +3 pasos de tiempo, −2 a −3 de ISO → exposición equivalente | OK `[C]` |
| 97 | 06:114 | cerrar de f/1.8 a f/2.8 «y compensa con ISO 3200» | f/1.8→f/2.8 = 1,27 pasos; ISO 1600→3200 = 1 paso. Queda 0,3 pasos corta | IMPRECISO |
| 98 | 06:98–100 | 300 tomas ≈ 12 s a 25 fps; intervalo 17 s para 15 s | 300/25 = 12 s; la serie dura 85 min | OK `[C]` |
| 99 | 06:146, 07:175–176, 07:271 | 90–180 tomas de 30 s = 45–90 min | Con intervalo de 31 s: 46,5–93 min | OK `[C]` |
| 100 | 10:173–174 | «23 fotos son unos dos segundos» | 23/10 = 2,3 s | OK `[C]` |
| 101 | 06:134, 07:211–213 | el 11 mm «abarca 71° de alto y 94° de ancho»; con el horizonte en el tercio bajo el polo cae dentro, a media altura | Sensor 23,3 × 15,5 mm: 93,3° × 70,3°. Horizonte en el tercio inferior = eje inclinado 13,2°; el borde superior llega a 48°; el polo queda al 57 % (Etosha) y 64 % (Sesriem) de la altura | OK `[C]` |
| 102 | 08:119–121 | regla 1/focal con 525 mm eq → ~1/500 s | 1/525 ≈ 1/500 | OK `[C]` |
| 103 | 08:134 | «los 26 Mpx aguantan un recorte del 50 %» | 50 % de superficie = 13 Mpx; 50 % por lado = 6,5 Mpx. No dice cuál | IMPRECISO |

**Correcciones propuestas**

- #90 (06:110): «…(con el 11 mm en APS-C, ~20 s es un punto de partida práctico: la regla del 500 daría 30 s y la NPF, más exigente, unos 15 s; hasta 25 s si el encuadre no es exigente)». Y en 06:194: «**Spot Stars**: los segundos máximos para tu combinación; compáralos con los 20 s de la receta.»
- #97 (06:114): «Cierra de f/1.8 a f/2.8 (pierdes algo más de un paso: compensa con ISO 3200 y acepta la foto un poco más oscura, o ISO 4000)».
- #103 (08:134): «los 26 Mpx aguantan quedarse con la mitad del encuadre (13 Mpx)».

### Inferences
- La guía usa c = 0,020 mm (el habitual para APS-C). Con un criterio más exigente (0,015 mm, más acorde con ver al 100 % un sensor de 26 Mpx) las distancias suben un 33 %: el «~4 m» pasaría a 4,5 m y el «~18 m» a 24,5 m.
- «A partir de f/11 la difracción resta más de lo que suma» (05:65) es coherente con un fotosito de 3,76 µm (23,3 mm / 6192 px), pero es juicio, no dato medido aquí.

### Gaps
- Coeficientes exactos de la NPF que usa PhotoPills: no los encontré en la página leída; por eso el cálculo usa la forma simplificada y lo declaro orientativo.
- No comprobé la calculadora de dofmaster.com (solo que la URL responde).

---

## 4. Astronomía y lugares de Namibia (octubre–noviembre de 2026)

### Takeaway
Las efemérides calculadas (Skyfield + DE421) para Okaukuejo y Sesriem confirman el plan de noches: núcleo bajo al OSO al acabar el crepúsculo, ventana que se acorta del 1 al 10, luna nueva el 9, Nubes y polo donde dice la guía, Cruz del Sur fuera. Hay tres imprecisiones de detalle. De los hechos de lugares se confirman las charcas iluminadas, King Nehale, el precio del night drive (750 N$) y NamibRand; quedan sin fuente la prohibición de flash, el horario de los rinocerontes y el veto nocturno de Deadvlei.

### Cited Findings

Datos de entrada del cálculo (míos): Okaukuejo 19,18° S 15,92° E; Sesriem 24,49° S 15,80° E; hora local UTC+2. Script: `astro.py`.

| # | Archivo:línea | Texto de la guía | Calculado / fuente | Clase |
|---|---|---|---|---|
| 104 | 06:16–18, 07:305 | núcleo «bajo, al OSO», «+26° y bajando» a las 20:25 | Okaukuejo, fin del crepúsculo astronómico 20:21 (1 nov) a 20:27 (10 nov). Centro galáctico a esa hora: 30° (día 1), 26° (día 5), 21° (día 10), acimut 245–247° (OSO) | OK `[C]` |
| 105 | 06:17 | «los primeros ~45–75 min de oscuridad» | Baja de 10° a las 21:56 (día 1), 21:40 (día 5), 21:20 (día 10): 95, 76 y 53 min; se pone entre 22:44 y 22:09 | OK `[C]` |
| 106 | 06:17–18, 09:166 | «solo del 1 al 10 (luego entra la luna en ese cielo)» | Luna nueva 9 nov 07:02 UTC. Día 10: 2 %, se pone 20:19 (antes de la noche cerrada). Día 11: 6 %, se pone 21:13. Día 12: 11 %, 22:05 | OK `[C]` |
| 107 | 07:154–156 | luna que ilumina el suelo «solo los días 11–14» | Días 11–14: 6–25 % iluminada, puesta 21:13–23:37. Creciente fino: ilumina poco, pero es correcto que solo esos días hay luna vespertina | OK `[C]` |
| 108 | 07:291 | «noches gordas de Etosha (9–12 nov)» en luna nueva | Coincide con la luna nueva del día 9 | OK `[C]` |
| 109 | 06:129, 07:184–185 | polo a ~24° en Sesriem y ~19° en Etosha | Altura del polo = latitud: 24,5° y 19,2° | OK `[C]` |
| 110 | 06:19, 06:127, 07:187 | la Cruz del Sur no está al anochecer | Ácrux a las 20:30–23:00 (7 nov): −5° a −7° en Okaukuejo; 0° a −2° en Sesriem | OK `[C]` |
| 111 | 07:196 | σ Octantis «a ~1° del polo» | 1,16° (posición aparente, nov 2026) | OK `[C]` |
| 112 | 07:215–217 | las Nubes y el polo forman un «triángulo casi equilátero» | Polo–Nube Grande 20,2°; polo–Nube Pequeña 17,2°; Nube–Nube 20,7° | OK `[C]` |
| 113 | 07:218–221 | entre 20:30 y 23:00: Pequeña arriba casi en la vertical del polo; Grande abajo a la izquierda; «el polo está a la misma altura que la Grande, dos puños a su derecha» | Nube Pequeña: altura 33–36°, acimut 169–182° (correcto). Nube Grande: acimut 159° (SSE, a ~20° del polo: correcto) pero su altura va de 14° (20:30) a 19,5° (21:30) y 27° (23:00); solo iguala al polo (19°) hacia las 21:30 | IMPRECISO |
| 114 | 07:307 | «23:00 en adelante: … Saturno culminando» | Saturno culmina a las 22:24 (7 nov), a 68° de altura al norte; a las 23:00 ya declina hacia el NO | IMPRECISO |
| 115 | 07:309 | «Alba del 14: Conjunción Júpiter–Marte al este» | Separación a las 04:30: 1,89° (día 12), 1,40° (día 14), **1,19° (día 16, mínimo)**, 1,40° (día 18). Posición: acimut 54° (NE), altura 38° | IMPRECISO |
| 116 | 06:19, 07:287, 07:308 | Táuridas activas en esas noches | Táuridas del Sur: máximo ~5 nov 2026; del Norte: 9–12 nov según la fuente; conocidas por bólidos — <https://earthsky.org/astronomy-essentials/taurid-meteors-all-you-need-to-know/> y <https://www.space.com/taurids> (buscador) | OK `[B]` |
| 117 | 07:207–208, 07:355 | «el norte magnético cae 10–15° al oeste»; «~13° O en Windhoek» | NOAA, WMM-2025, nov 2026: Windhoek −12,7°; Sesriem −14,9°; **Okaukuejo −8,9°** — <https://www.ngdc.noaa.gov/geomag-web/calculators/calculateDeclination?lat1=-19.18&lon1=15.92&model=WMM&startYear=2026&startMonth=11&startDay=7&resultFormat=json&key=zNEw7>. Windhoek correcto; en Etosha son ~9°, fuera del rango dado | IMPRECISO |
| 118 | 07:204–205 | «100 km de error lo mueven menos de 1°» | 1° de latitud ≈ 111 km | OK `[C]` |
| 119 | 06:11–13, 06:220 | NamibRand, Reserva Internacional de Cielo Oscuro | «Designated 2012 · Category Dark Sky Reserve»; «one of the naturally darkest (yet accessible) places on Earth» — <https://darksky.org/places/namibrand-dark-sky-reserve/> (copia de archive.org; la URL da 403 a robots) | OK `[P]` |
| 120 | 06:11–13 | «la primera… de África, certificada en categoría Gold» | «inscribe the NamibRand Nature Reserve as an International Dark Sky Reserve (IDSR) at the "Gold" tier level», primera de África — <https://www.namibrand.org/dark-sky.html> y <https://phys.org/news/2012-05-namibrand-nature-reserve-africa-international.html> (buscador) | OK `[B]` |
| 121 | 09:11–14 | tres charcas iluminadas con focos: Okaukuejo, Halali y Namutoni | «The three main camps (Okaukuejo, Halali and Namutoni) offer… chalets overlooking floodlit waterholes» — <https://www.etoshanationalpark.org/> | OK `[P]` |
| 122 | 09:14–15 | Namutoni: «charca King Nehale, junto al fuerte» | «The romantic fort overlooks the flood-lit King Nehale Waterhole» — <https://www.nwr.com.na/resorts/namutoni-resort/> | OK `[P]` |
| 123 | 09:14 | Halali: «charca Moringa» | No lo leí en ninguna página | SIN FUENTE |
| 124 | 09:12–13 | Okaukuejo: «rinocerontes negros casi cada noche, con ventana típica entre las 21:00 y la medianoche — fiable también en noviembre» | NWR solo dice «Lions, elephants, and black rhinos are all very common sightings» — <https://www.nwr.com.na/resorts/okaukuejo-resort/>. Ni horario ni estacionalidad | SIN FUENTE |
| 125 | 09:15–17 | Olifantsrus: abre 24 h, solo focos rojos | «At night, three red floodlights illuminate the waterhole», hide abierto 24 h para huéspedes — <https://info-namibia.com/accommodation/etosha/olifantsrus-campsite> y <https://kruger-2-kalahari.com/olifantsrus.html> (buscador) | OK `[B]` |
| 126 | 09:17–20 | Onguma Tamboti: charca con bar y restaurante asomados | Reseña en la web oficial: «a bar and restaurant overlooking the waterhole» (Tamboti Luxury Campsite, junio de 2026) — <https://onguma.com/>. Que esté **iluminada** y «junto a la puerta Von Lindequist» no aparece (la web dice «Bordering the eastern boundary of Etosha») | OK `[P]` (parcial) |
| 127 | 09:122–125 | night drive «~750 N$ por persona» | «Guided Night Drives N$750.00 per person» (tarifa nov 2026–jun 2027) — <https://www.nwr.com.na/resorts/okaukuejo-resort/> | OK `[P]` |
| 128 | 06:176–177, 09:123–124 | puertas cerradas del atardecer al amanecer; el night drive es la única forma legal de salir de noche | «park gates open at sunrise and close at sunset» — <https://nwrnamibia.com/etosha-gate-opening-times.htm> (buscador; la página no cargó al abrirla) | OK `[B]` |
| 129 | 09:150 | «Flash prohibido» en la charca | No encontré norma oficial de NWR; solo consejos genéricos de no usar flash | SIN FUENTE |
| 130 | 06:225–228 | Deadvlei: foto nocturna «en la práctica vetada (el permiso especial es muy difícil de conseguir)»; dormir dentro adelanta la entrada ~1 h | La puerta interior abre una hora antes que la exterior — <https://nwrnamibia.com/sesriem-gate-opening-times.htm> (buscador). Del veto nocturno y del permiso especial no hay fuente | OK `[B]` para la hora · SIN FUENTE para el veto |
| 131 | 06:222–223 | Spitzkoppe: acampada dentro, camping comunitario | «Most visitors choose to camp…», sección «Stargazing», «Spitzkoppe Rest Camp» — <https://spitzkoppe.com/> | OK `[P]` |
| 132 | 10:197–199 | «el enchufe oficial de Namibia es el M» | «Although type M sockets are the official standard in…» — <https://www.worldstandards.eu/electricity/plug-voltage-by-country/namibia/> (frase cortada en mi extracción; lo de que «el europeo entra en algunos» no lo comprobé) | OK `[P]` |

**Correcciones propuestas**

- #113 (07:218–221): «Entre las 20:30 y las 23:00 de tus noches la Nube Pequeña queda arriba, casi en la vertical del polo, y la Nube Grande abajo a la izquierda (sur-sureste), subiendo durante la noche: **hacia las 21:30** el polo está a la misma altura que la Grande, dos puños a su derecha, y debajo de la Pequeña (a las 20:30 la Grande aún está un puño más baja que el polo; a las 23:00, casi un puño más alta)». La dirección («a su derecha») y la distancia (20°) de la guía son correctas; lo único que hay que matizar es la hora.
- #114 (07:307): «**23:00 en adelante** — Banda de Orión–Carina subiendo por el este; Saturno, que ha culminado hacia las 22:30, alto al norte».
- #115 (07:309): «**Albas del 14 al 18** — Júpiter y Marte juntos al noreste (a 1,4° el día 14; mínimo de 1,2° el 16)».
- #117 (07:207–208): «…en Namibia el sur real marca ~189° en Etosha y ~195° en Sesriem, porque el norte magnético cae entre 9° y 15° al oeste».
- #124 (09:12–13): «Okaukuejo (los rinocerontes negros son habituales de noche; no hay horario garantizado)», salvo que se aporte fuente para la ventana 21:00–medianoche.
- #129 (09:150): «**Sin flash** — nunca con fauna nocturna (confirma en recepción si además está prohibido).»
- #130 (06:225–226): «la foto nocturna dentro no es viable en la práctica: las puertas cierran al atardecer (confirma en Sesriem si existe algún permiso)».

### Inferences
- A las 20:25 la noche aún no es cerrada en Sesriem (crepúsculo astronómico hasta 20:32–20:40): allí la tabla horaria de 07:305 empieza unos 10 minutos tarde respecto a Etosha.
- Puestas de sol calculadas (la guía no da horas): 19:04–19:11 en Okaukuejo y 19:11–19:19 en Sesriem, del 1 al 14 de noviembre.
- El «triángulo» de las Nubes tiene un lado más corto (17° frente a 20–21°): «casi equilátero» es una descripción justa.

### Gaps
- Sin fuente consultada (**SIN FUENTE**, #133 en bloque): «de mayo a septiembre la Vía Láctea es visible gran parte de la noche» (06:13–14); la luz zodiacal vespertina (07:305); el airglow verdoso (07:328–329); el bosque de árboles aljaba de Keetmanshoop (06:229); «el mirador de Okaukuejo funciona toda la noche y la gente duerme a 50 metros» (09:152–153); el depósito de agua de Okaukuejo y el granito de Hoada.
- La guía no hace afirmaciones Bortle en estos capítulos.
- Las páginas de nwrnamibia.com no cargaron al abrirlas; de ellas solo tengo el resumen del buscador.

---

## 5. Software, accesorios, precios y URL

### Takeaway
Las 55 URL distintas de los ocho capítulos existen: 44 responden 200 y 11 devuelven 403/307 a clientes automáticos (Sony, B&H, mpb, PhotoPills, DarkSky, Photography Life, Dustin Abbott), lo que no significa que estén rotas. StarStaX ha cambiado: la web anuncia una versión nueva para macOS «Coming soon to the Mac App Store» y deja las anteriores como descarga gratuita «legacy». La mayoría de precios de accesorios no se han podido contrastar.

### Cited Findings

**Software**

- StarStaX: la web es de «Markus Enzweiler» (copyright 2026); lista «**Lighten** for classic trails» y «Gap filling that follows the trails»; la versión nueva «Requires macOS 15.4 or later» y está «Coming soon to the Mac App Store»; las antiguas son «a free, unsupported download» para macOS y Windows — <https://starstax.net/>. Guía (06:148, 07:274): «StarStaX (gratis, modo Lighten, `Gap filling`…)». Funciones **OK `[P]`**; «gratis» solo vale para la versión antigua → **IMPRECISO**. Propuesta: «StarStaX (la versión clásica es gratuita; modo Lighten, `Gap filling`…)».
- Starry Landscape Stacker: «a Mac app»; «You can purchase Starry Landscape Stacker from the Mac App Store or download a free trial» — <https://sites.google.com/site/starrylandscapestacker/home>. «macOS, de pago» (06:153–154) **OK `[P]`**.
- «Los RAW (.ARW) entran directamente» (06:156–157): «Version 1.9 and later can open RAW files, for example .CR2… and .NEF» — <https://www.sites.google.com/site/starrylandscapestacker/preparing-images-for-starry-landscape-stacker-version-1-9> (buscador). No nombra ARW → **OK `[B]`** para RAW en general, sin confirmación específica de Sony.
- «pinta la máscara del cielo» (07:151–152, 07:163): la página leída solo dice «Starry Landscape Stacker will do most of the work for you» → **SIN FUENTE**.
- Sequator: «Sequator is a free software»; «Support RAW & 16-bit TIFF» — <https://sites.google.com/view/sequator/>. «Sequator only supports Windows currently» — <https://sites.google.com/view/sequator/qa> (buscador). «gratuita», «solo Windows» (06:155, 07:352) **OK `[P]`** / **OK `[B]`**.
- PhotoPills: iOS y Android («Download on the App Store / Google Play Store»), y el vídeo citado existe: «Yes, you can use PhotoPills even when you're offline, with no internet connection» — <https://www.photopills.com/videos/3-tips-to-use-photopills-offline-photopills-tip-7> (copia de archive.org; la URL directa da 403 a robots). «Spot stars calculator» y «Augmented Reality view» — <https://www.photopills.com/articles/milky-way-photography-guide>. **OK `[P]`**.
- «pago único» (06:182): 10,99 $ en App Store y Google Play, sin compras dentro de la app — <https://apppricinglab.com/app/apple/596026805> (buscador). **OK `[B]`**.
- Stellarium: Stellarium Mobile es «free, with Stellarium Plus», con «Sensor pointing» (apuntar el móvil al cielo), sin superposición de cámara ni planificador sobre mapa — <https://stellarium-labs.com/stellarium-mobile-plus/>. «Gratis… sin AR ni planificador sobre mapa» (06:197–198) **OK `[P]`**.
- Siril: <https://siril.org/> responde, pero no extraje texto que confirme «gratis» ni «Background extraction» → **SIN FUENTE**.
- Luminar (Noiseless AI, Panorama Stitching) y Sony Creators' App: no consultados → **SIN FUENTE**.

**Equipo auxiliar**

- «MacBook Neo (250 GB de disco)» (10:185): el producto existe; Apple lista «256GB SSD» y «512GB SSD» — <https://www.apple.com/uk/macbook-neo/specs/> (buscador). **IMPRECISO** leve: «256 GB».
- Pixel 10 Pro: existe y se vende a 999 € — <https://store.google.com/product/pixel_10_pro_specs> (leída). Las focales equivalentes de 01:58–64 (13, 25, 113 mm), el macro «a 3 cm» (10:136) y «a 20x inventa detalle» (08:199) no las pude extraer → **SIN FUENTE**.
- Precios de accesorios (10:141–245): tarjetas, lector, SSD, cargador doble, trípode, bean bag, anillos, filtros, mini trípode, pera, prismáticos Celestron Nature DX 8x42 y Nikon Prostaff P3 8x42 → **SIN FUENTE** (no comprobados; ninguno me parece fuera de rango, pero eso es impresión, no verificación).

**Estado de las URL (22 nov 2026, `urls_estado.txt`)**

| Estado | URL |
|---|---|
| 200, contenido comprobado | Las 7 páginas de helpguide.sony.net (índice, `0405M_peaking_display`, `0414H_bright_monitoring`, `0405_shutter_button_af`, `0601_cleaning_mode`, `0302C_bulb`, `211h_bulb_timer`); alphashooters.com; digitalcameraworld.com (review Viltrox); starstax.net; ambas de starrylandscapestacker; sequator; spitzkoppe.com; onguma.com; nwr.com.na/resorts/namutoni-resort/; etoshanationalpark.org |
| 200, solo estado (contenido no revisado) | capturetheatlas.com/es/como-fotografiar-la-via-lactea/; siril.org; stellarium.org; viltrox.com; celestron.com; dofmaster.com/dofjs.html; dzoom.org.es; lonelyspeck.com; magnetic-declination.com; nikon.es; nwr.com.na; sigma-global.com; tamron.eu |
| 200, repositorio del autor | Los 14 enlaces a `github.com/morandeirachema/a6700-namibia/…` (tres dieron 429 en la primera pasada y 200 al repetir) |
| 403 a robots; contenido visto en archive.org | darksky.org/places/namibrand-dark-sky-reserve/; photopills.com/videos/3-tips-to-use-photopills-offline-photopills-tip-7 |
| 307 a robots; contenido visto en archive.org | las dos reseñas de dustinabbott.net |
| 403 a robots; **sin poder ver el contenido** | sony.es/lenses/products/sel11f18; sony.es/lenses/products/sel70350g (sin copia de 2026 en archive.org); sony.es/electronics/support; bhphotovideo.com (ficha Viltrox; sin copia en archive.org); mpb.com; photopills.com (portada); photographylife.com/preparing-for-a-safari-trip-to-africa |

### Inferences
- Para las dos fichas de sony.es conviene abrirlas a mano: el buscador devuelve para el 70-350 la ruta `https://www.sony.es/electronics/camaras-objetivos/sel70350g/…`, distinta de la que cita la guía, y no pude confirmar que `…/lenses/products/sel70350g` redirija bien.
- La referencia de 10:268 («Búfer y tiempos de vaciado medidos…») apunta a la página correcta; lo que falla es la transcripción de sus cifras (sección 1).

### Gaps
- Sin acceso a idealo.es ni a mpb.com: los precios de segunda mano y los «desde» actuales quedan con evidencia de buscador o sin evidencia.
- No verifiqué el contenido de capturetheatlas, lonelyspeck, dzoom, dofmaster ni magnetic-declination más allá de que responden.

---

## 6. Técnica de safari comprobable

### Takeaway
Lo comprobable contra la Guía de ayuda se sostiene (Hi+ sin visión en tiempo real, anti-parpadeo incompatible con el obturador electrónico, compensación en ±5 EV). Las explicaciones físicas (heat haze, banding con LED) y las de comportamiento animal son razonables, pero no tienen fuente consultada en esta sesión.

### Cited Findings
- El anti-parpadeo («Toma sin parpad.») no está disponible con obturador electrónico, así que el plan B de la charca es el mecánico (09:54–58, 09:114) — HG-obturador. **OK `[P]`** (ya contado como #25).
- En Hi+ el sujeto no se ve en tiempo real (08:26) — HG-ráfaga. **OK `[P]`** (ya contado como #10).
- Estabilización del 70-350 a pulso: foto a 1/6 s y 350 mm, «roughly six stops» — Abbott-70350. Respalda el «margen real» de 08:121 sin convertirlo en cifra oficial.
- La guía no menciona el *rolling shutter* en estos capítulos.

### Inferences
- La regla 1/focal aplicada a 525 mm equivalentes (≥ 1/500 s) y la escala de obturaciones por escena (1/500 a 1/3200 s) son recetas; su aritmética es coherente.
- «1/60 s… a esa velocidad el parpadeo apenas se nota» (09:51–52) depende de la frecuencia de la red y del tipo de foco; es plausible, no verificado.

### Gaps
- **SIN FUENTE** (no consultado): franjas con LED y obturador electrónico como fenómeno (09:48–50); *heat haze* (08:135); «el IBIS de la cámara se suma solo» al OSS (08:28); «en la estación seca los animales beben a cualquier hora» (08:179–180); «las dos primeras y las dos últimas horas de luz concentran actividad» (08:178); «la a6700 va limpia hasta 3200 y muy bien a 6400» (09:93–94), que es valoración.
