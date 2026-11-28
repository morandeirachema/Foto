# Verificación de datos: `conceptos/`, AUTOEVALUACION.md, RUTA.md y README.md

Fecha de la verificación: 22 de noviembre de 2026. Alcance: `conceptos/00`–`11` y su `README.md` (no `guia-completa.md`), `AUTOEVALUACION.md`, `RUTA.md`, `README.md`. Nombres y rutas de menú: fuera de alcance (otro investigador).

**Método y regla antiinvención.** Un dato figura como verificado solo si (a) lo recalculé (fórmula y entradas indicadas; script en `/private/tmp/claude-501/-Users-chema-code-Foto/e8219b34-1511-4ce6-aae0-d7c276094f52/scratchpad/verif-conceptos/calc.py` y `p2p.py`) o (b) descargué en esta sesión la página que lo respalda (URL exacta). Cambridge in Colour, DPReview (foro), PhotoPills y varias páginas de Sony devolvieron HTTP 403/503 en directo; de Cambridge in Colour, PhotoPills, Dustin Abbott y la review de DPReview leí la copia de Wayback Machine (se indica). Lo que no pude abrir queda como SIN FUENTE.

**Clasificación:** OK · ERROR · IMPRECISO · INCOHERENCIA INTERNA · SIN FUENTE.

**Totales:** ERROR 2 · IMPRECISO 14 · INCOHERENCIA INTERNA 10 · SIN FUENTE 14 (recuento exacto de los ítems con identificador en estas notas) · OK ≈ 78 (recuento aproximado: cada fila de tabla o viñeta marcada OK cuenta como un ítem; varias agrupan líneas de distintos archivos). Total ≈ 118.

Fórmulas usadas:
- Hiperfocal: H = f²/(N·c) + f. PdC: cerca = s(H−f)/(H+s−2f); lejos = s(H−f)/(H−s).
- Pasos entre aperturas: 2·log₂(N₁/N₂). Pasos entre tiempos o ISO: log₂(cociente).
- Disco de Airy (diámetro al primer mínimo): 2,44·λ·N, con λ = 0,55 µm.
- Paso de píxel: ancho del sensor / píxeles de ancho = 23,3 mm / 6192 = 3,76 µm.
- **Círculo de confusión que usa el repo (inferido): c = 0,020 mm.** Reproduce todas las tablas (11 mm, 25 mm, 70-350) salvo la cifra de «~4 m» del 11 mm a f/1.8 (ver I3). DOFMaster asigna 0,020 mm a las Sony APS-C (NEX-3, NEX-5, A100) — [DOFMaster, tabla de CoC](https://www.dofmaster.com/digital_coc.html).

---

## 1. Exposición y luz (caps. 01, 02, 03 y §1–2 del 09)

### Takeaway
La teoría de pasos, triángulo, gris medio, sentido de la compensación, histograma, recorte, luz dura/suave y temperatura de color es correcta y toda la aritmética cuadra. Hay tres imprecisiones conceptuales (ISO «deja entrar luz», el folio que «sale blanco» con +1, el argumento de «niveles» del ETTR) y una contradicción entre capítulos sobre la compensación en la charca nocturna.

### Cited Findings

**OK (recalculado o con fuente)**
- 02:29-31 escalas de velocidad, apertura e ISO de paso en paso: correctas (cada f ÷ √2; cada tiempo e ISO ×2). «Every time the f-stop value halves, the light-collecting area quadruples» — [Cambridge in Colour, Camera Exposure (Wayback)](https://web.archive.org/web/20251201091529id_/https://www.cambridgeincolour.com/tutorials/camera-exposure.htm).
- 02:33 y AUTOEVALUACION:24 «1/250 → 1/1000 = dos pasos = ISO ×4 (400 → 1600)»: log₂(1000/250) = 2,00; 2² = 4. OK.
- 02:35 número f = focal/diámetro; ÷√2 duplica el área. OK (cálculo).
- 02:48 y 11:74 regla 1/focal equivalente: 350 × 1,5 = 525 → 1/500 s. OK.
- 09:31 «f/1.8 es un tercio más que f/2»: 2·log₂(2/1,8) = 0,30 pasos. OK.
- 09:39-41 tres exposiciones: 1/2000→1/500 = +2 pasos, ISO 6400→1600 = −2; f/6.3→f/3.2 = 1,95 ≈ 2 pasos, ISO 1600→400 = −2. Misma claridad. OK (ver I-A sobre la palabra «luz»).
- 09:50-51 ejercicio «1/60·f/8 → 1/500·f/2.8 a ISO 400»: 3,06 pasos menos de tiempo, 3,03 más de apertura. OK.
- 01:33-42, 02:74, 03:186-187, AUTOEVALUACION:31-32, 39, 89-130: el medidor lleva la escena a gris medio; escena clara → subexpone → «+»; escena oscura → sobreexpone → «−». «If the camera is aimed directly at any object lighter or darker than middle gray, the camera's light meter will incorrectly calculate under or over-exposure»; «Photographs in the snow will therefore always require around +1 exposure compensation, whereas a low-key image may require negative compensation» — [Cambridge in Colour, Camera Metering (Wayback)](https://web.archive.org/web/20251203021552id_/https://www.cambridgeincolour.com/tutorials/camera-metering.htm). El rango +0,7/+1 del repo coincide.
- 03:11-14, 11:30, AUTOEVALUACION:46 lo que toca el borde derecho está recortado y no se recupera: «Detail can never be recovered when a region becomes so overexposed that it becomes solid white… "clipped"»; las escenas de clave alta «often produce images which are significantly underexposed» — [Cambridge in Colour, Histograms (Wayback)](https://web.archive.org/web/20260211175231id_/https://www.cambridgeincolour.com/tutorials/histograms1.htm). Respalda también 03:112-117 (clave alta) y 03:46-48 (silueta).
- 01:55-57, 11:82, AUTOEVALUACION:53 dura/suave según tamaño aparente de la fuente; 01:72-78 direcciones de la luz: definiciones estándar, sin cifras que contrastar. OK como definición (sin fuente descargada específica; no contienen datos falsables).
- 01:86-95 cifras bajas = cálidas, altas = frías; orden vela < amanecer/atardecer < mediodía < nublado < sombra: coincide con la tabla 1000-2000 K vela · 2500-3500 tungsteno · 3000-4000 amanecer/atardecer · 5000-6500 luz de día · 6500-8000 nublado · 9000-10000 sombra — [Cambridge in Colour, White Balance (Wayback)](https://web.archive.org/web/20251208213811id_/https://www.cambridgeincolour.com/tutorials/white-balance.htm).
- 02:60, 09:171-174 «el ISO no hace que entre más luz; amplifica»: coherente con la curva medida de la a6700 (el ruido de lectura referido a la entrada no sube con el ISO) — [Photons to Photos, Read Noise in e-](https://www.photonstophotos.net/Charts/RN_e.htm).
- 02:61, 09:176, 11:90 ISO base 100: «Imágenes fijas: ISO 100 a ISO 32 000 (ISO ampliado: mínimo ISO 50, máximo ISO 102 400)» — [Sony, especificaciones ILCE-6700](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html). Rango dinámico máximo en ISO 100 (10,93 EV PDR) — [Photons to Photos, PDR](https://www.photonstophotos.net/Charts/PDR.htm).
- 11:26 y README:107 compensación ±5 EV: «±5,0 EV (cambiable entre pasos de 1/3 EV y 1/2 EV)» — [Sony, especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html). (Que funcione en M con ISO Auto no figura en esa página: no comprobado aquí.)
- 11:75 Hi+ 11 fps: «(Captura continua: Hi+): Máximo de aprox. 11 imágenes por segundo» — misma página de Sony.

**IMPRECISO**
- **I-A · «dejan entrar la misma luz».** 09:34-35 «tres exposiciones que dejan entrar la misma luz»; 11:23 «un paso más de obturación, de apertura o de ISO son lo mismo en luz»; 11:25 «Combinaciones distintas de los tres números que dejan entrar la misma luz». Las tres filas de 09:39-41 dejan entrar cantidades de luz distintas (1/500 deja 4× más que 1/2000 a la misma f); lo que comparten es la claridad final. Contradice 02:60 («El ISO no hace que entre más luz») y 09:171. Además INCOHERENCIA INTERNA. Fuente: cálculo + [CiC Camera Exposure (Wayback)](https://web.archive.org/web/20251201091529id_/https://www.cambridgeincolour.com/tutorials/camera-exposure.htm) (solo tiempo y apertura regulan la luz que entra). Propuesta 09:34: «tres ajustes que dan **la misma claridad** con cantidades de luz distintas, y por eso tres fotos distintas». Propuesta 11:25: «Combinaciones distintas de los tres números que dan la misma claridad — y fotos distintas».
- **I-B · 09:40 «Dos pasos menos de ruido».** Son dos pasos menos de ISO (4× más luz); la relación señal/ruido por fotones mejora √4 = 2×. Propuesta: «Dos pasos menos de ISO (cuatro veces más luz): bastante menos ruido, riesgo de movida».
- **I-C · El folio blanco «sale blanco» con +1.** 01:47 «Repite con +1 de compensación: ahora sí sale blanco»; 01:49 «Repite con −1: ahora sí sale negra»; AUTOEVALUACION:94 «+1». Cálculo: un papel blanco (~90 % de reflectancia) está log₂(0,90/0,18) = 2,3 pasos por encima del gris del 18 % (2,9 si el medidor apunta al 12 %); una tela negra (~4 %), 2,2 por debajo. Con ±1 salen gris claro / gris oscuro. CiC sitúa el gris de las cámaras «between 10-18% reflectance» — [CiC Camera Metering (Wayback)](https://web.archive.org/web/20251203021552id_/https://www.cambridgeincolour.com/tutorials/camera-metering.htm). El ejercicio de 03:181 (−2…+2) ya lo trata bien. Propuesta 01:47: «Repite con +1: sale más claro, pero aún gris claro. Con +2 ya sale blanco.» y 01:49 «Con −1 mejora; con −2 ya sale negra». AUTOEVALUACION:94: «**Sumar: +1 para empezar y hasta +2** para que sea blanco de verdad».
- **I-D · 09:58-63 y 11:28 ETTR explicado solo por «niveles».** La frase «la mitad de los niveles viven en el paso más luminoso» es cierta en codificación lineal, pero la fuente indica que con 14 bits «this is less of a factor than it used to be» y que la ventaja real es el ruido; además ETTR «Requires more light than normal, and potentially a higher ISO speed (which could mitigate any reduction in image noise from ETTR)» — [CiC Digital Exposure Techniques (Wayback)](https://web.archive.org/web/20251231104910id_/https://www.cambridgeincolour.com/tutorials/digital-exposure-techniques.htm). En la receta de fauna (M + ISO Auto) la compensación +0,7/+1 solo sube el ISO: no entra más luz. Propuesta (añadir a 09:63): «El beneficio real es que entra más luz (menos ruido); si la compensación solo sube el ISO, no ganas calidad: solo colocas bien el tono.» AUTOEVALUACION:367 coincide literalmente con 11:28 (misma simplificación).

**INCOHERENCIA INTERNA**
- **C1 · Compensación en la charca de noche.** 01:38 «Resta: −0,7 a −1» · AUTOEVALUACION:115 «Negativa (−0,7 a −1)» · manejo 09:141 «compensación a −1» · pero 03:65 «−0.3/−0.7 si hace falta» y 03:163 «Ninguna: **no la toques**». Propuesta 03:163: «0 de partida; **−0,7/−1** si el animal iluminado se quema» y 03:65 «−0,7/−1 si hace falta».

### Inferences
- Las recetas de compensación (+0,7/+1 claro, −1/−1,7 silueta) son coherentes entre 01, 03, 07 y 09 salvo el caso C1.
- La decisión «a pulso se paga con ISO; con trípode, con tiempo» (09:43-47) es consecuencia correcta del modelo.

### Gaps
- No se descargó una fuente específica para luz dura/suave y dirección (definiciones estándar, sin cifras).
- «La compensación funciona en M con ISO Auto» (11:26, README:107) no aparece en la página de especificaciones descargada.

---

## 2. Balance de blancos (cap. 04, 11:85-86, AUTOEVALUACION etapa 2 n.º 1)

### Takeaway
La explicación de por qué el AWB neutraliza los atardeceres es correcta y el 3900 K nocturno tiene respaldo externo; los Kelvin atribuidos a los preajustes de Sony (5200/6000/7000) **no tienen fuente**: la Guía de ayuda de la a6700 no da ninguna cifra.

### Cited Findings
- **SIN FUENTE · S1 · 04:27-31 «Luz de día (5200 K)», «Nublado (6000 K)», «Sombra (7000 K)»; AUTOEVALUACION:156 «Luz de día (5200 K)».** La página oficial solo enumera «Luz diurna / Sombra / Nublado / Incandescente…» y «Tem.col./filtro», sin Kelvin — [Sony, Balance blanco ILCE-6700](https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html). Un buscador devolvió como resumen que Sony Alpha Universe daría Daylight 5600 K / Shade 7000 K / Cloudy 6000 K, pero la página (alphauniverse.sony-asia.com/node/7556) respondió 503 y no pude leerla: no cuenta como verificación. Propuesta: «Luz de día (≈5200–5600 K; Sony no publica la cifra)», o quitar los Kelvin de los preajustes y dejar solo el nombre. Nota: el nombre en el menú es «Luz diurna», no «Luz de día» (lo revisa el otro investigador).
- **OK · 04:30, 04:39-41, 04:49-52, AUTOEVALUACION:156** el AWB neutraliza el dorado: «…the subject is predominantly red, and so the camera mistakes this for a color cast induced by a warm light source. The camera then tries to compensate for this so that the average color of the image is closer to neutral»; amanecer/atardecer 3000-4000 K — [CiC White Balance (Wayback)](https://web.archive.org/web/20251208213811id_/https://www.cambridgeincolour.com/tutorials/white-balance.htm). Con un valor fijo ~5200 K una luz de 3000-4000 K queda cálida: correcto. «Nublado para aún más cálido» (04:31): sentido correcto.
- **OK · 04:28-29** nublado y sombra son más azules (6500-8000 K y 9000-10000 K) — misma fuente.
- **OK · 04:34, 07:386, AUTOEVALUACION:156 y 212 «3900 K» en astro:** «Set the white balance to 3900K» — [PhotoPills, Milky Way photography settings (Wayback)](https://web.archive.org/web/20250711164640id_/https://www.photopills.com/articles/milky-way-photography-settings). Coincide con manejo 06:38 y 04:129.
- **OK · 04:11-12** en RAW el balance se cambia después; **OK · 01:99 y 04** dos luces distintas no se neutralizan a la vez: «Some lighting situations may not even have a truly "correct" white balance» — CiC White Balance.
- **IMPRECISO · I-E · 04:32 «los [focos] de sodio piden ~2800–3200».** Wikipedia da «1400-2700K for Sodium» y ~2500 K para el HPS «blanco» — [Wikipedia, Sodium-vapor lamp](https://en.wikipedia.org/wiki/Sodium-vapor_lamp). 2800–3200 K es más frío que la lámpara: la foto seguirá naranja (y con sodio no hay neutro posible). Propuesta: «los de sodio (≈2000–2700 K) seguirán naranjas incluso al mínimo: baja a 2800 y asume el tono, o pasa a B/N».
- **INCOHERENCIA INTERNA · C2 · 11:86 «5500 K día, 7500 K sombra azulada» frente a 04:27 y 04:29 (5200 K y 7000 K).** Propuesta 11:86: «3200 K naranja, ~5200 K día, ~7000 K sombra azulada».
- **IMPRECISO · I-F · 11:87 hora azul «el rato azulado posterior al ocaso»:** también ocurre antes del amanecer (01:95 dice lo mismo). Propuesta: «…y el rato azulado **anterior al amanecer y** posterior al ocaso».
- **SIN FUENTE · 04:33 «Game drive con foco: K ≈ 3200–3800, focos halógenos»** y 04:32 rango 2800–4000: recomendaciones propias, sin fuente localizada.

### Inferences
- Las cifras 5200/6000/7000 K coinciden con las que suelen citarse para otros fabricantes; al atribuirlas a preajustes de Sony conviene marcarlas como aproximadas.

### Gaps
- No pude abrir ninguna página de Sony con Kelvin por preajuste (helpguide no los da; Alpha Universe 503).

---

## 3. Óptica (cap. 05, §3–5 y §8 del 09, 07 n.º 20, glosario)

### Takeaway
Todas las hiperfocales y profundidades de campo se reproducen con c = 0,020 mm dentro del 10 %, excepto «~4 m» para el 11 mm a f/1.8 (da 3,4 m: cifra redondeada al alza, prudente pero hecha con otro criterio). Equivalencias ×1,5, perspectiva = distancia y difracción son correctas.

### Cited Findings

**Recalculado (c = 0,020 mm)**

| Dato del repo | Línea(s) | Cálculo | Clase |
|---|---|---|---|
| 11 mm f/2.8 → 2,2 m / ~1,1 | 09:99 | H = 2,17 m; mitad 1,09 | OK |
| 11 mm f/4 → 1,5 / ~0,75 | 09:100 | 1,52; 0,76 | OK |
| 11 mm f/5.6 → 1,1 / ~0,55 | 09:101 | 1,09; 0,55 | OK |
| 11 mm f/8 → 0,8 / ~0,40 | 09:102, 05:68, 11:59, AUTOEV.:346, manejo 05:62 | 0,77; 0,38 | OK |
| 11 mm f/11 → 0,6 / ~0,30 | 09:103 | 0,56; 0,28 | OK |
| «f/8, enfoca a ~1 m» nítido desde ~0,4 | 09:105, manejo 05:18 | enfocando a 1 m: 0,43 m → ∞ | OK |
| 25 mm f/8 → ~3,9 / ~2 m | 05:69, 09:257-258, manejo 11:62 | 3,93; 1,97 | OK |
| 25 mm f/1.7 → nítido más allá de ~18 m | 05:71, AUTOEV.:60 y 138, manejo 05:23, manejo 11:69 | H = 18,4 m | OK |
| **11 mm f/1.8 → «unos 4 m»** | 05:71, 07:483-484, 07:497, 07:502, AUTOEV.:60 y 138, manejo 05:21-23 | H = 3,37 m (c = 0,020); 3,55 (0,019); 4 m exige c ≈ 0,017 | **IMPRECISO (I3)** |
| 70 mm f/4.5 a 30 m → ~48 m | 09:113, 09:120-121 | 19,4–66,6 m: 47,3 m | OK |
| 200 mm f/6.3 a 30 m → ~5,7 m | 09:114 | 5,68 m | OK |
| 350 mm f/6.3 a 30 m → ~1,9 m | 09:115, 05:57, AUTOEV.:353 | 1,83 m | OK |
| 350 mm f/6.3 a 15 m → ~0,5 m | 09:116, 05:57, AUTOEV.:353 | 0,45 m | OK (redondeo +10 %) |
| 25 mm f/1.7 a 2 m → ~40 cm | 05:58, 09:255 | 0,43 m | OK |
| «al doble de distancia, cuatro veces más» | 09:87-88, 05:54 | 1,83/0,45 = 4,1 | OK |

- **I3 (detalle).** Texto: «Unos **4 m** con el 11 mm a f/1.8» (05:71). Con el mismo c que el resto de tablas sale 3,4 m (+19 %). Es un margen de seguridad, pero no está dicho y rompe la coherencia del cálculo. Propuesta: «Unos **3,5 m** con el 11 mm a f/1.8 (pon el primer plano a 4 m para ir con margen)».
- **OK · definición de hiperfocal (05:64, 09:94-95, 11:59) y «enfocado al infinito, lo nítido empieza en la hiperfocal» (05:71):** «Focusing your camera at the hyperfocal distance ensures maximum sharpness from half this distance all the way to infinity»; «Focusing at infinity causes the nearest acceptably sharp objects to correspond with the hyperfocal distance» — [CiC Hyperfocal Distance (Wayback)](https://web.archive.org/web/20251130180102id_/https://www.cambridgeincolour.com/tutorials/hyperfocal-distance.htm).
- **OK · 11:60 círculo de confusión** — [CiC Depth of Field (Wayback)](https://web.archive.org/web/20251218104242id_/https://www.cambridgeincolour.com/tutorials/depth-of-field.htm).
- **OK · equivalencias 05:28-30, 11:55, README:25:** 11×1,5 = 16,5; 25×1,5 = 37,5; 70–350×1,5 = 105–525. Sensor: «Sensor de imagen CMOS de tamaño APS-C (23,3 mm × 15,5 mm)», «Aprox. 26 000 000 píxeles» — [Sony, especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html) (36/23,3 = 1,55 ≈ 1,5). Confirma 09:18.
- **OK · perspectiva y compresión (05:20, 05:36-42, 09:151-155, 11:62, AUTOEVALUACION:339 y 390):** «A misconception is that a telephoto lens affects perspective, but strictly speaking, this isn't true. Perspective is only influenced by where you are located when you take a photograph» — [CiC Telephoto Lenses (Wayback)](https://web.archive.org/web/20251202154004id_/https://www.cambridgeincolour.com/tutorials/telephoto-lenses.htm).
- **OK · difracción (02:54, 05:79, 09:128-145, 11:61, AUTOEVALUACION:325).** Píxel: 23,3/6192 = 3,76 µm («unas 3,8 micras», 09:133: OK). Airy: f/5.6 = 7,5 µm (2,0 px) · f/8 = 10,7 µm (2,9 px) · f/11 = 14,8 µm (3,9 px) · f/16 = 21,5 µm (5,7 px). Criterio: «an airy disk can have a diameter of about 2-3 pixels before diffraction limits resolution… However, diffraction will likely have a visual impact prior to reaching this diameter»; depende solo de N y λ, no del objetivo — [CiC Diffraction (Wayback)](https://web.archive.org/web/20260107001656id_/https://www.cambridgeincolour.com/tutorials/diffraction-photography.htm). Límite entre f/5.6 y f/8,4: «punto dulce f/5.6–f/8, f/11 se nota, f/16 pérdida clara» es coherente. Abbott también: a f/22 «diffraction is going to really reduce contrast» — [Dustin Abbott (Wayback)](https://web.archive.org/web/20260606134529id_/https://dustinabbott.net/2022/05/sony-e-70-350mm-f4-5-6-3-g-oss-review/).
- **IMPRECISO · I-G · 11:58 «Depende de distancia, focal y apertura — en ese orden» y 05:52 (focal como palanca).** 09:87-91 dice que distancia y focal van ambas al cuadrado; y la fuente matiza: «If the subject occupies the same fraction of the image… the total depth of field is virtually constant with focal length» — [CiC Depth of Field (Wayback)](https://web.archive.org/web/20251218104242id_/https://www.cambridgeincolour.com/tutorials/depth-of-field.htm). Propuesta 11:58: «Depende de la distancia y la focal (las dos, al cuadrado) y de la apertura; a igual tamaño del sujeto en el encuadre, casi solo de la apertura».
- **OK · fondo desenfocado y separación sujeto-fondo (05:60, AUTOEVALUACION:226):** geometría estándar; 25 mm f/1.7: a 1 m PdC 0,11 m, a 4 m 1,81 m (cálculo), coherente con el ejercicio 05:84.
- **OK parcial · 09:247 «0,23x de ampliación máxima»:** «Minimum focus distance here is 1.1m (3.61′), giving us a useful… 0.23x magnification» — Dustin Abbott (Wayback, arriba). **SIN FUENTE** el matiz «a 350 mm desde 1,5 m» (09:247, 09:281): la ficha de Sony devolvió 403.
- **SIN FUENTE · S3 · 09:241-242 escalones «f/4.5 (70–81) · f/5 (82–113) · f/5.6 (114–199) · f/6.3 (200–350)».** Abbott solo confirma F4.5 a 70 mm, F5.6 a 135 mm y F6.3 a 350 mm (compatibles, pero no dan los cortes).
- **IMPRECISO · I-H · 09:244-246 «Como todo superzoom, su punto más blando es 350 mm a f/6.3… encuadrar a ~300 mm y recortar… a menudo da un resultado igual o mejor».** La review enlazada por el propio capítulo dice: «While lesser telephotos zooms often start to soften at the long end, the 70-350G maintains a very high standard. It's very slightly off the peak performance found in the middle of the zoom range, but still at excellent levels». La pérdida es «muy ligera»; la recomendación de recortar desde 300 mm no tiene respaldo. Propuesta: «A 350 mm rinde un poco por debajo del centro del rango, pero sigue siendo excelente: no hace falta evitarlo».
- **SIN FUENTE · S9 · datos de los objetivos** 09:228-229 (11 mm: rosca 55 mm), 09:250-251 (Viltrox: 170 g, rosca 52 mm, sin interruptor AF/MF): fichas de fabricante no descargadas (coinciden con manejo 11:25-27, sin fuente externa en esta sesión).
- **SIN FUENTE · S10 · 05:32** «cámara principal del móvil ronda los 24 mm equivalentes».

### Inferences
- El repo usa c = 0,020 mm en todo salvo en los «4 m»; no hay ningún error óptico de fondo.

### Gaps
- Fichas oficiales de SEL70350G, SEL11F18 y Viltrox 25 mm no accesibles (403) o no buscadas por límite de consultas.

---

## 4. Sensor, ISO, AF y estrellas (cap. 09 §2, §6, §7; glosario; AUTOEVALUACION)

### Takeaway
La aritmética de bits y del AF es correcta, pero el dato central de §6 está desplazado: según Photons to Photos el escalón de doble ganancia de la a6700 está en **ISO 320**, y la cámara es prácticamente invariante desde ahí, no «desde ~800». La profundidad de bits del RAW de la a6700 no pude confirmarla con Sony.

### Cited Findings
- **OK · bits:** 2⁸ = 256; 2¹² = 4.096; 2¹⁴ = 16.384. AUTOEVALUACION:67 coincide literalmente con retoques 01:13 y 01:24 («256 (8 bits)», «4.096–16.384 (12–14 bits)»).
- **SIN FUENTE · S2 · ¿12 o 14 bits en la a6700?** La Guía de ayuda («Tipo archivo RAW», especificaciones) no da bits: solo «RAW (cumple con el formato ARW 4.0 de Sony)» — [Sony, especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html), [Sony, Tipo archivo RAW](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404I_raw_file_type.html). El artículo de soporte «Limitations on recording 14 bit images in RAW format» (ID 00229990, versión a6700) devolvió 403. Indicios leídos: Photons to Photos etiqueta la serie como «Sony ILCE-6700_14» — [RN_e](https://www.photonstophotos.net/Charts/RN_e.htm); y DPReview: en ráfaga solo JPEG con obturador electrónico la lectura más rápida «is likely to mean a drop to 12-bit readout» — [DPReview, review a6700 (Wayback)](https://web.archive.org/web/20261103141841id_/https://www.dpreview.com/reviews/sony-a6700-review/). El «12–14 bits» genérico del repo es compatible; no afirma una cifra concreta para la a6700.
- **IMPRECISO · I1 · invarianza «a partir de ISO ~800».** Texto: 09:178-180 «a partir de ISO ~800 la a6700 es prácticamente ISO-invariante»; 09:186-188 «Por debajo de ISO 800… **no** es invariante»; 09:269; 11:91 «a partir de ~800»; AUTOEVALUACION:332 «a partir de ISO ~800». Datos extraídos del gráfico (serie «Sony ILCE-6700_14», ordenada tal como la publica el gráfico): ISO 100 → 1,88 · 125 → 1,78 · 160 → 1,78 · 200 → 1,75 · 250 → 1,72 · **320 → 0,61** · 400 → 0,59 · 500 → 0,51 · 640 → 0,57 · 800 → 0,51 · 1600 → 0,53 · 3200 → 0,44 · 6400 → 0,39 — [Photons to Photos, Input-referred Read Noise](https://www.photonstophotos.net/Charts/RN_e.htm). El PDR confirma el escalón: ISO 250 = 9,52 EV, ISO 320 = 9,59 EV (sube), y desde ahí baja ~1 EV por paso — [Photons to Photos, PDR](https://www.photonstophotos.net/Charts/PDR.htm). El «segundo escalón en la parte baja-media» (09:177-178) es correcto (ISO 320); el umbral de 800 es prudente pero más alto que el dato. DPReview no da umbral: «shows still more noise if you try to lift the lower ISOs… some scope for dropping ISO in low light conditions, to retain highlights» — review citada arriba. Propuesta 09:178: «**a partir de ISO ~320–400** (su segundo escalón de ganancia) la a6700 es prácticamente ISO-invariante»; y en 09:186, 09:188, 09:269, 11:91 y AUTOEVALUACION:332 cambiar 800 por «~400».
- **SIN FUENTE · S8 · 09:295** hilo del foro de DPReview «a6700 ISO invariance test»: HTTP 403, no pude comprobar que exista ni qué concluye.
- **OK · ruido = falta de fotones; lo quemado no vuelve (09:65-66, 09:171-174):** coherente con CiC Histograms y con la curva de P2P (citadas).
- **OK · AF «de −3 EV a +20 EV, medida a f/2.0» (09:206-207, AUTOEVALUACION:360):** «–3 EV a +20 EV (en equivalente a ISO 100, F2,0)» — [Sony, especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html).
- **OK (cálculo) · 09:207-209, 09:273, AUTOEVALUACION:360:** f/2.0 → f/6.3 = 2·log₂(6,3/2) = 3,31 pasos; −3 + 3,31 = +0,31 EV. f/1.8 = +0,30 pasos sobre f/2; f/1.7 = +0,47 (09:253-254 OK). Es una inferencia del repo (Sony no publica el límite a f/6.3), razonable porque el AF trabaja a plena apertura.
- **SIN FUENTE · S4 · 09:209-210** «+0,3 EV — que es, **exactamente**, la penumbra de la charca de Okaukuejo»: no hay medición de la luminancia de la charca. Propuesta: «…alrededor de +0,3 EV: del orden de una escena iluminada por focos lejanos».
- **OK · 09:200-204** AF híbrido fase + contraste: no contrastado con cita literal (la página de especificaciones no se pidió para esto); se deja como OK conceptual de bajo riesgo — si se exige fuente, pasa a SIN FUENTE.
- **Trazas de estrellas.** Cálculo: regla 500 → 500/(11×1,5) = 30 s (11 mm) y 13,3 s (25 mm); NPF simplificada (35·N + 30·p)/f → 16,0 s (11 mm f/1.8) y 6,9 s (25 mm f/1.7); deriva a 20 s con 11 mm ≈ 4,3 px en el ecuador celeste. PhotoPills: «Adjust the shutter speed using the NPF rule: between 8s and 20s» — [PhotoPills (Wayback)](https://web.archive.org/web/20250711164640id_/https://www.photopills.com/articles/milky-way-photography-settings). **OK:** 07:386 (20 s), 03:78-79 (subir ISO, no segundos), AUTOEVALUACION:198 y 205 (20 → 15 → 13 s), manejo 11:40 y 11:90 (10–13 s con 25 mm).
- **OK (cálculo) · astronomía del 9-nov-2026 en Okaukuejo (19,18° S, 15,92° E, UTC+2):** orto 06:12, ocaso 19:07, noche astronómica 20:26–04:54 → 10:46 «~06:15», 10:50 «~19:05», 10:116 «~20:25 a ~04:55». Luna nueva (Meeus): 9-nov-2026 → 10:60, 10:115. Polo sur celeste a la altura de la latitud: 18°56′ S — [Wikipedia, Etosha National Park](https://en.wikipedia.org/wiki/Etosha_National_Park) → «~19°» (07:431, 11:104). Nubes de Magallanes y polo: 20,2°, 17,2° y 20,7° de lado → «forman un triángulo con el polo» (07:475-476) OK.
- **IMPRECISO menor · 10:120 y 07:477 «toda la noche»:** a 19° S la Gran Nube no es circumpolar (altura mínima −1,1°); en noviembre sí está sobre el horizonte toda la noche, así que la frase vale para esas fechas (se cuenta como OK).
- **OK · 11:111 Bulb solo con obturador mecánico:** la página lista entre las incompatibilidades «[Tipo de obturador] está ajustado a [Obturad. electr.]» — [Sony, Toma Bulb](https://helpguide.sony.net/ilc/2320/v1/es/contents/0302C_bulb.html).

### Inferences
- Con el escalón en ISO 320, la regla práctica «protege las luces y levanta después» vale ya desde ISO 400; el consejo de 09:186 de exponer bien por debajo sigue siendo correcto para ISO 100–250.

### Gaps
- Unidades exactas de la ordenada del gráfico de ruido de lectura de P2P no verificadas (los valores se citan tal cual); la posición del escalón no depende de ello.
- Límite oficial de 14/12 bits de la a6700: sin acceso a la página de Sony.
- Lluvia de las Táuridas y sus bólidos (10:123): la página de la AMS devolvió un documento vacío → SIN FUENTE (S11). Bortle 1–2 (10:116, 11:108) y núcleo «45–75 minutos» (10:118): SIN FUENTE.

---

## 5. Composición y «la mirada» (caps. 06, 07, 08, 10)

### Takeaway
Las dos atribuciones con cifra o cita (van Oosten y Lanting) son reales. Brandt aparece como fotógrafo de Namibia sin respaldo; «Rimmer» está citado sin presentar y con detalles que su texto no dice; la «receta Delaney» y la «pregunta de van Oosten» no se localizan como tales.

### Cited Findings
- **OK · 06:19, 06:35 regla de los tercios:** imagen dividida «by two equally spaced horizontal lines and two equally spaced vertical lines», elementos en las líneas o cruces — [Wikipedia, Rule of thirds](https://en.wikipedia.org/wiki/Rule_of_thirds). El cap. 06 no atribuye nada a autores ni estudios: sin citas que verificar. (07:30 escribe «regla de tres» por «regla de los tercios»: nombre de menú, lo revisa el otro investigador.)
- **OK · 10:26-27 van Oosten «la mayoría de mis fotos de Namibia las he previsualizado en casa»:** «Most of the photographs that I shoot in Namibia I have already pre-visualized at home» — [Photo Cascadia, entrevista a Marsel van Oosten](https://www.photocascadia.com/an-interview-with-marsel-van-oosten-from-adrian-klein/).
- **IMPRECISO · I6 · 10:141-142 «La pregunta de control, la de van Oosten: ¿esta foto la habría hecho igual cualquiera que pasara por aquí?»** En la entrevista no formula esa pregunta; dice de una foto suya: «Anyone could have made this shot, but very few people would have made that same decision» (misma URL). Propuesta: «La pregunta de control (inspirada en van Oosten: "cualquiera podría haber hecho esta foto, pero muy pocos habrían tomado esa decisión"): ¿qué decisión tomé yo que no habría tomado cualquiera?».
- **IMPRECISO menor · 07:540** rótulo «Composición de paisaje nocturno (van Oosten, entrevista)»: la entrevista es general (Namibia, creatividad, talleres); contiene un apartado «Night Photography», pero no es un texto sobre composición nocturna. Propuesta: «Entrevista a Marsel van Oosten (previsualización, Namibia, fotografía nocturna)».
- **OK (con matiz) · 10:30-31 «Lanting disparó 321 tomas a los árboles de Deadvlei»:** «Frans shot almost 16,000 frames for this story»; «he had shot 321 images of the dead trees in Sossusvlei and Dead Vlei» — [National Geographic, Behind the Photo](https://www.nationalgeographic.com/magazine/article/frans-lanting-behind-the-photo). Matiz: son árboles de Sossusvlei **y** Dead Vlei. Propuesta: «…321 tomas a los árboles muertos de Sossusvlei y Deadvlei».
- **SIN FUENTE (probable error) · E-Brandt · 10:22-24 «los grandes que han fotografiado Namibia — Frans Lanting, Marsel van Oosten, Nick Brandt, Peter Delaney».** La biografía consultada sitúa a Brandt en África oriental (Tanzania, Kenia), Zimbabue, Bolivia, Fiyi y Jordania; Namibia no aparece — [Wikipedia, Nick Brandt](https://en.wikipedia.org/wiki/Nick_Brandt). Sí respalda la idea de 10:33-35 (retrato, de cerca: «graphic portraits more akin to studio portraiture», «without telephoto or zoom lenses»). Propuesta: «Investigamos a grandes de la fauna africana —Lanting, van Oosten y Delaney en Namibia; Nick Brandt en África oriental—…». La frase «dispara a la altura de su ojo o más bajo» atribuida a Brandt: SIN FUENTE.
- **IMPRECISO · I5 · 10:36-38 «los "elefantes fantasma" de Rimmer son literalmente esperar el after del baño de barro aguantando el calor del mediodía».** «Rimmer» no está en la lista de 10:22-24 ni se presenta (es Christopher Rimmer). Su texto: «The Etosha elephants' supernatural appearance is due to the white clay found in the area in which they take their afternoon mud baths»; «I observed the Etosha elephants for two weeks» — [Anima Mundi, portfolio de Christopher Rimmer (PDF)](https://animamundimag.com/PersonalPortfolios/Christopher_Rimmer.pdf). Dice baños de la **tarde** y arcilla blanca; «calor del mediodía» no figura. Propuesta: «los "elefantes fantasma" de Christopher Rimmer salieron de observar la manada dos semanas y esperar a que terminara su baño de barro de la tarde». Relacionado: 10:69 «se rebozan en polvo de calcreta» → la fuente habla de arcilla blanca del barro; SIN FUENTE lo del polvo de calcreta.
- **SIN FUENTE · S5 · 10:99-102 «Receta Delaney: mide, compensa +2/3 a +1…».** Las páginas localizadas confirman que Peter Delaney trabaja en blanco y negro en Etosha («Grey Ghosts of Etosha»), pero ninguna que abriera da esa receta de exposición; solo tengo resultados de búsqueda, no una página leída. Propuesta: «Receta de clave alta (al estilo de Peter Delaney)…».
- **SIN FUENTE · S7 · Etosha (10:44-62, 10:66-80):** charcas por hora, «rinos negros 21:00–24:00 casi garantizados», «Goas (leones 16:00–18:00)», Kalkheuwel «la mejor charca para muchos fotógrafos» (cita entrecomillada sin autor), gangas «~2 horas después del amanecer», «fuentes de fotógrafos que las trabajan» (10:42) sin citar. Wikipedia no cubre nada de esto — [Wikipedia, Etosha National Park](https://en.wikipedia.org/wiki/Etosha_National_Park). No verificado; fuera del núcleo de teoría fotográfica.
- **OK · coherencia interna de 07 y 08:** 14 + 6 = 20 encuadres (07:12-13, README conceptos:61); secuencia de cinco = 3, 1, 6, 9, 14 (07:517-519) coincide con los títulos; 08:35 ocho encuadres listados = 8; 08:75 «los otros diecisiete» = 20 − 3; «dos tercios de aire» (07:58, 08:36), «menos de un décimo» (07:103, 08:38), 1/2500 (07:241, 08:49, 10:76), −1/−1.7 silueta (07:123, 03:97), −1 EV contraluz (07:287, 10:104), 0,23x (07:172, 09:247), 3900 K (07:386) son coherentes entre capítulos.
- **INCOHERENCIA INTERNA · C4 · 10:155** «Un escalón por semana de las once previas al viaje»: hay cinco escalones (10:149-153). Propuesta: «Los cinco escalones repartidos en las once semanas previas…».
- **INCOHERENCIA INTERNA · C5 · 08:64-71** «Encaja en las once semanas»: la tabla cubre semanas 1–10 y repite la 9 en dos bloques. Propuesta: «8–9 Esperar · 10–11 Contar» (o decir «diez semanas»).
- **INCOHERENCIA INTERNA · C8 · 09:9 y 10:9 «Da por sabido: los capítulos 1 a 10»** (y 10:11): por la convención de 00:40 se refiere a *Manejo*, pero dentro del capítulo 9/10 de conceptos se lee como autorreferencia. Propuesta: «los capítulos 1 a 10 de [Manejo]…».

### Inferences
- El capítulo 10 mezcla fuentes reales (van Oosten, Lanting, Rimmer) con paráfrasis presentadas como citas o recetas de autor; conviene marcar cuáles son interpretación del repo.

### Gaps
- «Los trece fotógrafos» y el resto de guías enlazadas viven en otro repositorio (a6700-namibia): no comprobado.
- Sin fuente abierta para las recetas de Delaney ni para los datos de comportamiento animal y horarios de charcas.

---

## 6. Glosario (cap. 11)

### Takeaway
Las definiciones son correctas; solo cinco entradas necesitan retoque (exposición equivalente/paso, Kelvin, hora azul, ISO invariante, profundidad de campo), ya descritas arriba.

### Cited Findings
- **OK (definiciones estándar, coherentes con los capítulos y con las fuentes ya citadas):** velocidad, EV, compensación (±5 EV: Sony), medición, ETTR (con el matiz I-D), histograma, quemado, rango dinámico (máximo en ISO base: P2P), horquillado, focal, equivalente (cálculo), apertura, apertura variable (f/4.5–6.3: Abbott), hiperfocal (0,8 m: cálculo), círculo de confusión (CiC), difracción (cálculo + CiC), compresión (CiC), regla 1/focal (cálculo), ráfaga Hi+ 11 fps (Sony), luz dura/suave, dirección, sombra abierta, balance de blancos, contraluz, clave alta (CiC Histograms: «high key»), ISO base 100 (Sony), ruido de lectura (P2P), circumpolar, polo sur celeste ~19° (latitud, Wikipedia), Bulb solo mecánico (Sony), escala Bortle 1–9 (definición; el «Namibia 1–2» es SIN FUENTE).
- **Con problema (ver secciones):** 11:23 y 11:25 (I-A) · 11:58 (I-G) · 11:86 (C2) · 11:87 (I-F) · 11:91 (I1).
- **No comprobado aquí (cámara/menús/astro sin fuente abierta):** AF-S/AF-C, DMF, áreas de AF, sensibilidad de seguimiento, peaking, obturador electrónico «totalmente mudo», banding, rolling shutter (DPReview da ~64 ms en RAW con obturador electrónico: coherente), coma «se corrige cerrando un tercio o dos», airglow, luz zodiacal, mopane/dik-dik, sRGB/Adobe RGB.

### Inferences
- Ninguna definición del glosario contradice la física; los desajustes son de coherencia con otros capítulos.

### Gaps
- Entradas de campo y astro sin fuente externa consultada.

---

## 7. AUTOEVALUACION.md: ¿coincide cada respuesta con su capítulo?

### Takeaway
De 41 preguntas, 35 coinciden con el capítulo enlazado y son correctas; 6 arrastran imprecisiones del capítulo o enlazan a un capítulo que no contiene el dato exacto. No hay ninguna respuesta que contradiga numéricamente a su capítulo.

### Cited Findings

| Pregunta (línea) | Capítulo enlazado | Resultado |
|---|---|---|
| E1-1 (24) | 02:33; manejo 01:44-45 | OK (2 pasos, ISO ×4) |
| E1-2 (31-32) | 01:37, 01:42 | OK |
| E1-2b (39) | 01:38 | OK |
| E1-3 (46) | 03:11-14; retoques 1.3 | OK |
| E1-4 (53) | 01:56, 01:78 | OK |
| E1-5 (60) | manejo 05:23; manejo 11:69 | Coincide; arrastra I3 (4 m ↔ 3,4 m calculados) |
| E1-6 (67) | retoques 01:13, 01:24 | OK (256; 4.096–16.384) |
| E1-7 (74) | manejo 03:238; manejo 11:46 | Coincide en «solo en MF»; el inciso «(y con el selector en Foto, en P/A/S/M)» no está en manejo 03:238 → INCOHERENCIA menor (C10; menús: otro investigador) |
| E1-8 (81) | manejo 04:54-57 | OK |
| M1 (94) | 01:47 | Coincide; arrastra I-C (+1 no da blanco) |
| M2, M3, M5, M6 (101, 108, 122, 129) | 01:37-42 | OK |
| M4 (115) | 01:38; manejo 09:141 | Coincide con 01 (−0,7 a −1) y con manejo 9 (−1); contradice 03:65 y 03:163 (C1) |
| E1 extra (138) | manejo 05:23; 05:71 | Coincide; I3 |
| E2 extra (145) | manejo 11:46 | OK |
| E2-1 (156) | 04:30, 04:34, 04:13-14; manejo 06:38 | Coincide; el «5200 K» es SIN FUENTE (S1) |
| E2-2 (163) | retoques 04:29 (Paso 2) | OK (enlace correcto) |
| E2-3 (170) | retoques 04:76 (Paso 7) | OK |
| E2-4 (177) | retoques 05:76-87 | OK |
| E2-5, 5b (184, 191) | retoques 05:31-42 | OK (+0,3 literal) |
| E2-5c (198) | manejo 05:89, 05:95 | OK |
| E2-6 (205) | **manejo 07** | INCOHERENCIA (C3): manejo 07:88 solo dice «Baja a 15 s»; la serie «20 → 15 → 13» está en manejo 06:110. Propuesta: enlazar también [Manejo 6](../../manejo-a6700/10-astrofotografia.md) |
| E2-7 (212) | manejo 04:129-130 | OK (literal) |
| E2-8 (219) | retoques 1.7; Paso 9 (04:93) | OK |
| E2-9 (226) | 05:60 | OK |
| E2-10 (233) | 06:41-43 | OK |
| L1 (244) | retoques 03:37 | OK (+15 a +40; +50) |
| L2 (251) | retoques 03:26 | OK |
| L3, L4, L9 (258, 265, 300) | retoques 04 «Rescatar» | No leído línea a línea (retoques: otro investigador); ancla existe |
| L5 (272) | retoques 13:70 | OK: 6192/300×2,54 = 52,4; 4128/300×2,54 = 35,0; a 200 ppp 78,6 × 52,4 |
| L6 (279) | retoques 13:90-91 | OK |
| L7 (286) | retoques 13:95 | OK |
| L8 (293) | retoques 16:73-85 | OK (cinco pruebas + día siguiente) |
| L10 (307) | retoques 09:106 | OK |
| L11 (314) | retoques 09:70-91 | OK |
| E3-1 (325) | 09:128-145 | OK |
| E3-2 (332) | 09:178-182 | Coincide; arrastra I1 (el escalón está en ISO 320) |
| E3-3 (339) | 09:151-155 | OK |
| E3-4 (346) | 09:102; manejo 05:62 | OK (0,77 / 0,38 calculados) |
| E3-5 (353) | 09:115-116 | OK (1,83 / 0,45) |
| E3-6 (360) | 09:206-210 | OK (3,31 pasos; +0,31 EV) |
| E3-7 (367) | 09:58-63; 11:28 | Coincide; matiz I-D |
| E3-8 (374) | 10:147-153 | OK (orden idéntico; RUTA:142 igual) |
| A1 (383) | 09:182 | OK |
| A2 (390) | 05:36-42 | OK |

- Enlaces y anclas: `python3 tools/comprobar.py` (solo lectura) devuelve «Todo correcto»: todos los archivos y anclas enlazados existen.
- AUTOEVALUACION:15 «85 %» coincide con RUTA:21.

### Inferences
- Los fallos de la autoevaluación son heredados: corrigiendo I1, I3, I-C y C1 en los capítulos hay que actualizar las líneas 60, 94, 115, 138 y 332.

### Gaps
- Las respuestas L3, L4 y L9 (Luminar) no se contrastaron frase a frase con retoques 04.

---

## 8. RUTA.md y README.md frente a los archivos reales

### Takeaway
Los recuentos de capítulos son correctos (11 + 17 + 20 = 48) y los títulos coinciden con los H1, pero el README raíz conserva dos cifras obsoletas («Los 7 capítulos de conceptos» y «PDF de 56 páginas») y hay pequeñas discrepancias de nivel.

### Cited Findings (comprobación local: recuento de archivos, H1 con `grep`, `pdfinfo`)
- **OK · recuentos:** `conceptos/` 11 capítulos (01–11) + introducción; `manejo-a6700/` 17; `retoques/` 20. README:10 «48 capítulos», README:37-39 (11/17/20), conceptos/README:7 «11 capítulos», RUTA:11 «más de cuarenta capítulos», README:144-145 (17 y 20) correctos. 6 PDF en `pdf/` (README:11, README:40). `sources/` PDF de 264 páginas (README:41): `pdfinfo` = 264. Chuleta = 1 página.
- **ERROR · E1 · README:143** «🧠 Conceptos completo | Los **7** capítulos de conceptos». Hay 11. Propuesta: «Los 11 capítulos de conceptos».
- **ERROR · E2 · README:130** «[PDF de **56** páginas](../../pdf/guia-retoques.pdf)». `pdfinfo pdf/guia-retoques.pdf` → 77 páginas. Propuesta: «PDF de 77 páginas» (o quitar la cifra, que cambia con cada regeneración).
- **OK · títulos frente a H1:** todos los títulos de 00-introduccion:13-32, conceptos/README:55-65, README:55-65 (conceptos), README:77-103 (manejo) y README:124-128 (retoques) corresponden al H1 de su archivo (formas abreviadas). Diferencia trivial: 00:20 «Óptica: focal, perspectiva y profundidad de campo» omite «encuadre» del H1 (05:7).
- **OK · etapas:** README:151 «cinco etapas» = etapas 0–4 de RUTA. Las tablas de RUTA enlazan a capítulos que enseñan lo que dicen (comprobado: 02, 03, 01 §gris medio, 05, 06, 07, 09 §1–§6, 10 §escalones; retoques 6.3 Color Harmony, 6.4 Dodge & Burn, 6.6 Black & White, 13.2, 13.3, 16.3; manejo 05:65 para difracción). «Los 10 pasos» = retoques 04 (Pasos 1–10). «7 tardes de deberes», «cinco pruebas»: anclas válidas.
- **IMPRECISO · I13 · RUTA:166** «Contraste global y local → Retoques 4 · paso 8»: el Paso 8 es «Textura y nitidez: Structure AI y Details» (retoques 04:84); el contraste global está en el Paso 4 (Develop). Propuesta: «Retoques 4 · pasos 4 y 8».
- **INCOHERENCIA INTERNA · C6 · niveles.** (a) 05:9 «🟢 Iniciación → 🔵» y conceptos/README:59 «🟢 → 🔵», pero README:59 «🟢». (b) 08 no tiene línea de nivel, aunque README:62 y conceptos/README:62 le dan 🔵 y README:45 / 00:37 dicen «cada capítulo abre con su nivel». (c) 00:38 «Cada capítulo termina con un ejercicio»: el 11 (glosario) no lo tiene. Propuestas: README:59 «🟢 → 🔵»; añadir a 08 «> 🔵 **Básico** · Da por sabido: el atlas · Te desbloquea: …»; 00:38 «Cada capítulo (salvo el glosario) termina con un ejercicio».
- **INCOHERENCIA INTERNA · C7 · 09:18-19** «tu equipo: una a6700…, un 11 mm f/1.8 y un 70-350» omite el Viltrox 25 mm, que el propio capítulo trata en §8 (09:250) y README:25 lista. Propuesta: añadir «, un Viltrox 25 mm f/1.7».
- **INCOHERENCIA menor · C12 · README:77-81** la tabla «Empezar de cero» ordena 1, 2, 3, 5, 4.
- **OK · README:107 datos de cámara comprobables aquí:** ±5 EV y Hi+ 11 fps (Sony, especificaciones; 23 fotos / 11 fps ≈ 2 s, cálculo). **SIN FUENTE (S12)** en esta sesión: «una sola ranura UHS-II», «23 fotos en RAW comprimido sin pérdida», «la caja no trae cargador» (no figuraban en el extracto leído).
- **OK · RUTA:58 y 01:29** «abrir un paso, duplicar el tiempo o duplicar el ISO dan la misma claridad» (dice «claridad», no «luz»: formulación correcta).

### Inferences
- Los dos errores del README son restos de versiones anteriores (7 capítulos; PDF más corto); `tools/comprobar.py` no vigila esas cifras.

### Gaps
- No se compararon las descripciones «Qué resuelve» de manejo y retoques con el contenido completo de cada capítulo (solo títulos y anclas).

---

## Resumen de problemas por prioridad

1. **ERROR** README:143 (7 → 11 capítulos) y README:130 (56 → 77 páginas).
2. **IMPRECISO de fondo** I1 (invarianza desde ISO ~320, no ~800: 09:178-188, 09:269, 11:91, AUTOEVALUACION:332) · I-A («misma luz»: 09:34, 11:23, 11:25) · I-C (folio blanco con +1: 01:47-49, AUTOEVALUACION:94) · I3 (4 m ↔ 3,4 m) · I-D (ETTR) · I-E (sodio) · I-H (350 mm «blando»).
3. **Atribuciones** Brandt y Namibia (10:22-24) · Rimmer (10:36-38) · pregunta «de van Oosten» (10:141) · receta «Delaney» (10:99).
4. **SIN FUENTE** Kelvin de los preajustes (04:27-31) · bits del RAW de la a6700 · escalones de apertura del 70-350 (09:241) · «exactamente la penumbra de Okaukuejo» (09:209) · hilo de DPReview (09:295) · datos de Etosha (cap. 10).
5. **INCOHERENCIAS** C1 (charca: 03:65 y 03:163 frente a 01:38) · C2 (Kelvin del glosario) · C3 (enlace E2-6) · C4, C5 (once semanas) · C6 (niveles) · C7 (Viltrox ausente) · C8 («capítulos 1 a 10») · C10 · C12.
