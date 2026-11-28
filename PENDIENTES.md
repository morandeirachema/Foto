# ✅ Pendientes: lo que tienes que comprobar tú

Cosas que el repo **no puede verificar por sí solo**: hacen falta tu cámara, tus objetivos, tu Luminar o una decisión tuya. Cuando cierres una, marca la casilla. Si el resultado no coincide con la guía, **manda lo que ves**: anótalo aquí y corrijo la guía.

## 1 · Urgente: que la cámara dispare en RAW

Las fotos de Namibia salieron **solo en JPEG** por un error de configuración. Antes de la próxima salida:

- [ ] `Toma → [Calid. img/grab.] → [Formato archivo]` = **RAW**, con `Tipo archivo RAW` = comprimido sin pérdida ([configuración básica](manejo-a6700/04-configuracion-basica.md)).
- [ ] Carga **MR1** y mira su **balance de blancos**: tiene que ser Luz de día, no el Kelvin de la noche. El 91 % de las fotos del viaje se hizo con un balance fijo, y la foto del león a la sombra sale azulada; dime cuál tenías puesto.
- [ ] Carga **MR1** y comprueba otra vez el formato. Haz lo mismo con **MR2**. Si alguna vuelve a JPEG, pon RAW y **vuelve a guardar esa memoria** (`Toma → [Modo de toma] → [Mem. ajustes cám]`).
- [ ] Foto de prueba → al ordenador: tiene que haber un archivo **`.ARW`**.
- [ ] Si quieres saber **qué falló** en Namibia: abre una foto del viaje en la cámara o en el ordenador y anota qué formato y qué tamaño tiene. Así sabremos si fue el formato, una memoria o un reinicio de ajustes.

## 2 · La cámara: 11 nombres de menú por confirmar

La auditoría confirmó las 79 rutas, pero estos nombres no se pudieron localizar ([verificación de los menús](manejo-a6700/18-verificacion-de-menus.md)). Ponte sobre cada línea y pulsa **C3**: la Guía en la cámara muestra el nombre oficial.

> **Confirmados el 22 de noviembre de 2026** en las fichas de la Guía de ayuda de Sony ([verificación](notas-de-investigacion/verificacion-de-datos/menus-de-la-a6700.md)). Si la pantalla de tu cámara dice otra cosa, manda la pantalla.

- [x] `Tem.col./filtro` (dentro de `Balance blanco`)
- [x] `Cuadr. regl. terc.`
- [x] `C. sin pérd.`
- [x] `Compens. variación`
- [x] `Punto: S/M/L`
- [x] `Conmut. dest. recon.`
- [x] `Botón personaliz. 1/3`
- [x] `Solo pant. táctil`
- [x] `Mostrar toda info.`
- [x] `Monitor desactiv.`
- [x] «Separe el modo M y los otros modos.»

## 3 · El Viltrox 25 mm

- [ ] ¿Es el **AF 25 mm F1.7 Air**? Lo pone en el barrilete o en la caja. Si es otro modelo, la ficha de [su guía](manejo-a6700/14-viltrox-25mm.md) puede cambiar.
- [ ] Haz una foto y mira su información: ¿dice **25 mm** de focal? (Para el estabilizador y para los datos de la foto.)
- [ ] **Firmware:** anota la versión instalada y compárala con la última de la web de Viltrox.
- [ ] Asigna **`Alter. select. AF/MF`** a un botón libre (no C1 ni C3) y anota cuál: lo pongo en la guía.
- [ ] **Prueba de aceptación** del AF: 20 fotos a una persona que camina hacia ti a f/1.7 y otras 20 a f/2.8. ¿Cuántas tienen el ojo nítido al 100 %?
- [ ] **Una noche de estrellas** a f/1.7 y a f/2.8, 10–13 s: ¿las estrellas de las esquinas salen redondas o con "alitas"?
- [ ] ¿Tiene alguna junta de goma en la montura? Las fuentes se contradicen sobre el sellado.

## 4 · Luminar

- [ ] **Versión exacta** (menú Luminar → Acerca de) y **tipo de licencia**. Las herramientas *Improved* (Crop AI, Atmosphere AI, GenExpand) requieren 1.29.0 o posterior y una licencia que las incluya.
- [ ] Herramienta **Color → HSL**: ¿qué colores aparecen? La documentación de Skylum no los enumera ([retoques, paso 7](retoques/04-flujo-base.md)).
- [ ] **Exportar**: ¿qué opciones salen en *Color Space*? ¿Hay alguna opción para quitar metadatos o la ubicación GPS? ([retoques, 13](retoques/13-exportar.md))
- [ ] Para el futuro con RAW: ¿abre Luminar los **`.ARW` comprimidos sin pérdida** de la a6700? Prueba con la foto de la sección 1.
- [ ] **La misma herramienta dos veces** (por ejemplo, Develop) con máscaras distintas: Skylum dice que se puede, pero no explica cómo. Prueba a añadir Develop de nuevo después de usarlo y dime qué pasos has seguido. Si se puede, las guías pueden usar Develop + Mask AI para aclarar u oscurecer zonas con precisión ([retoques, 5.2](retoques/05-ajustes-locales.md)).
- [ ] **La escala de cada deslizador:** Skylum no publica los rangos. La primera vez que abras Develop, Structure AI, Dodge & Burn, Vignette y Film Grain, anota hasta dónde llega cada deslizador (por ejemplo, de −100 a +100) y ajusto los números de [Las herramientas, una a una](retoques/03-herramientas-una-a-una.md) si hace falta.
- [ ] **El tamaño de tus JPEG de Namibia:** en Luminar, pestaña **Info** (**`I`**). Si es **6192 × 4128**, la cámara estaba en **L (26M)** y valen las cuentas de impresión de [retoques 13.5](retoques/13-exportar.md#135-tus-fotos-compartir-con-la-familia-e-imprimir).
- [ ] **Atajos con teclado español:** ¿responden en tu Mac **`⌥º`** (ver el original), **`⇧7`** (mostrar la máscara), **`⇧,`** (comparar) y **`⌥`** + las teclas de **`[`** **`]`** (tamaño del pincel)? Dime también si tu teclado es español o de EE. UU. ([retoques, 17](retoques/17-atajos.md#si-tu-teclado-es-español)).
- [ ] **Apilado en Mac:** Starry Landscape Stacker acepta JPEG (lo dice su autor, aunque los desaconseja). ¿Tienes series de fotos nocturnas iguales y seguidas para apilar? ([retoques, 9.2](retoques/09-noche.md#apilar-una-serie-fuera-de-luminar))
- [ ] **HEIF:** haz una foto con `Conm JPEG/HEIF` en `HEIF(4:2:2)` y ábrela en Luminar. ¿La abre? ([retoques, 15.4](retoques/15-disparar-mejores-jpeg.md#154-lo-que-enseñan-tus-fotos-de-namibia))
- [ ] **Curves:** al subir un punto de la curva, ¿la zona se aclara o se oscurece? La documentación de Skylum lo describe al revés de lo habitual ([retoques, 6.1](retoques/06-herramientas-avanzadas.md)).
- [ ] **Exportar a TIFF:** ¿ofrece Luminar 16 bits? Y en **Sharpen**, ¿qué niveles aparecen?
- [ ] **Polvo del sensor:** tus fotos de día tienen una mancha fija en el cielo, arriba, en el tercio izquierdo. ¿Se puede copiar o sincronizar **Remove Dust Spots** entre fotos? (Skylum dice que Erase no se sincroniza.) Y limpia el sensor antes de la próxima salida.
- [ ] **Charca con focos:** prueba las tres salidas de [retoques, 9.3](retoques/09-noche.md#animales-en-una-charca-iluminada-con-focos) con una foto de elefantes y dime cuál te convence.
- [ ] **Color en pantalla:** compara una foto exportada en Vista Previa con lo que ves en Luminar. ¿Coinciden? ([retoques, 1.9](retoques/01-conceptos-basicos.md))
- [ ] **Las rutas según el contenido** de [retoques, 4](retoques/04-flujo-base.md#qué-hay-en-tu-foto-la-ruta-según-el-contenido) están por probar con tus fotos: dime en cuáles no funciona el orden.
- [ ] ¿Lee Luminar las **estrellas** que pones en la cámara (`Valoración`)? Marca una foto con 3 estrellas y ábrela en el catálogo.

## 5 · Fotos de muestra para las recetas

Las [recetas completas](retoques/10-recetas.md) están marcadas como provisionales hasta probarlas con fotos reales.

- [ ] Elige JPEG del viaje: un animal (ideal, león o similar al amanecer), unas dunas o un atardecer, un cielo nocturno y una escena con fuego o luces.
- [ ] Ponlas en una carpeta, por ejemplo `~/code/Foto/samples/`.
- [ ] Decide: ¿se **suben al repo** (es público) o se quedan **solo en local**?

## 6 · El equipo y el estado del repo

- [x] **El 70-350 prestado**: sigue contigo una temporada (18 de noviembre de 2026). Las guías siguen contando con él; si lo devuelves, avisa y las ajusto.
- [ ] El estado del equipo de [equipo y accesorios](manejo-a6700/13-equipo-accesorios.md) es del **25 de octubre**. ¿Ha cambiado algo?
- [ ] **Capturas de los menús:** el [guion](manejo-a6700/img/menus/) tiene 14 imprescindibles (marcadas ★). Hazlas con el móvil y ejecuta `python3 manejo-a6700/img/menus/insertar.py`.
- [ ] **Quitar la ubicación de una foto:** Apple documenta cómo en la app Fotos (Imagen → Ubicación → Ocultar ubicación). ¿Se puede también desde Vista Previa (Herramientas → Mostrar inspector)? ([retoques, 14.3](retoques/14-etica.md))

## 7 · Decisiones

- [ ] ¿Traigo las guías **"después del viaje"** de a6700-namibia (el archivo y la selección: copias 3-2-1, criba en dos pasadas, las 20 finales)?
- [ ] ¿Escribo un capítulo de **Luminar con RAW** para las próximas salidas? (Depende de la comprobación de la sección 4.)
- [ ] ¿Añado el **Viltrox** a la [chuleta](manejo-a6700/19-chuleta.md)? Tiene que seguir cabiendo en una cara.
- [ ] Hay 81 enlaces que llevan a **a6700-namibia** para guías no copiadas. ¿Mantienes ese repo publicado, o traigo lo que te interese?

## 8 · Verificación del 22 de noviembre de 2026

El [informe de verificación](informes/verificacion-de-datos.md) revisó todo el repo. Los errores y las citas mal atribuidas ya están corregidos. Queda esto, que no se puede resolver sin ti o sin la cámara:

- [ ] **Datos sin fuente** (tabla «Prioridad 3» del informe): los Kelvin de los preajustes de Sony (5200/6000/7000 K), lo que guardan las memorias MR, valores de fábrica, horarios de fauna en las charcas y precios. Dime cuáles compruebas en la cámara y los fijo o los quito.
- [x] **Imprecisiones menores** (tabla «Prioridad 2»): aplicadas el 22 de noviembre de 2026, salvo tres que se dejan a propósito (lo explica la nota inicial del informe).
- [ ] **Nada se ha probado dentro de Luminar ni en la cámara:** toda la verificación es documental o de cálculo.

## 9 · El Pixel 10 Pro

La [guía del Pixel](manejo-pixel-10-pro/README.md) se escribió el 22 de noviembre de 2026 con la ayuda de Google, sin el teléfono delante ([verificación](manejo-pixel-10-pro/12-verificacion.md)). Con el móvil en la mano:

- [ ] Anota la **versión** de la aplicación Cámara y de Android.
- [ ] `Ajustes → [Pro]`: ¿existen los **controles Pro**? ¿Qué deslizadores hay (enfoque, obturación, ISO; ¿**balance de blancos**?) y entre qué valores se mueven?
- [ ] ¿Cómo se llaman en pantalla los **botones de zoom** (0,5x, 1x, 2x, 5x, 10x)? ¿Aparece el 10x?
- [ ] ¿Está instalado **`Zoom Pro`** (`Ajustes → [Más] → [Descarga de modelos]`)? A más de 30 aumentos, ¿se guardan dos imágenes?
- [ ] Modo `Movimiento`: ¿ofrece `Larga exposición` **y** `Barrido de movimiento`?
- [ ] Cronometra una foto de **`Astrofotografía`**: ¿cuántos minutos dura?
- [ ] ¿A qué distancia salta la flor del **`Enfoque macro`**?
- [ ] ¿Se puede disparar con las **teclas de volumen**? ¿Abre la cámara la **doble pulsación** del botón de encendido? ¿Qué valores tiene el **temporizador**?
- [ ] ¿Qué **tipos de cuadrícula** y qué opciones de **flash** hay?
- [ ] ¿En qué **formato** guarda (JPEG, HEIF, Ultra HDR)? ¿Abre Luminar el **DNG** de `RAW + JPEG`?
- [ ] `Brillo` y `Sombras`: ¿están donde dice el [capítulo 2](manejo-pixel-10-pro/02-la-aplicacion-camara.md)?
- [ ] Las **Credenciales de Contenido**: ¿qué anota en una foto normal y en una de Zoom Pro?
- [ ] **Decisión:** ¿quieres preguntas del Pixel en la autoevaluación y en el test interactivo? Ahora no las hay.

## 10 · Time-lapse, estelas y fotos en casa

- [ ] **Time-lapse, receta B** ([capítulo 10](manejo-a6700/10-time-lapse-del-cielo.md#receta-b--del-atardecer-a-la-noche-la-cámara-lleva-la-exposición)): haz la serie de prueba de 60 fotos durante una puesta. ¿Cómo salen las últimas, ya de noche: demasiado oscuras, bien o grises? ¿Se nota parpadeo en el vídeo? Con eso ajusto la compensación (−0,7) y el máximo de ISO AUTO (3200) de la receta.
- [ ] Con `Prior. intervalo toma` en `Activar`, ¿qué hace la cámara cuando la exposición ya no cabe en el intervalo: sube el ISO, oscurece la foto o acorta la velocidad? Mira la velocidad y el ISO de las últimas fotos de la serie. Sony no lo explica.
- [ ] **Luminar, capas:** al añadir una foto como capa (**My Images**), ¿qué modos salen en **Blend Modes**? ¿Hay **Lighten**? La documentación de Skylum no los enumera ([estelas de tráfico](manejo-a6700/11-estelas-de-trafico.md#varias-fotos-para-una-apilar-las-estelas)).
- [ ] **Imaging Edge Desktop** (*Viewer*): ¿se instala en tu Mac y crea el vídeo con una serie de intervalo tal como sale de la tarjeta, como dice la Guía de ayuda? ¿Y con los JPEG exportados de Luminar? ([capítulo 10](manejo-a6700/10-time-lapse-del-cielo.md#1--el-vídeo)).
- [ ] **DaVinci Resolve:** al importar la carpeta de un time-lapse, ¿reconoce las fotos numeradas como un solo clip, como dice el [capítulo 10](manejo-a6700/10-time-lapse-del-cielo.md#1--el-vídeo)? No está comprobado en tu Mac.
