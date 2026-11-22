# ✅ Pendientes: lo que tienes que comprobar tú

Cosas que el repo **no puede verificar por sí solo**: hacen falta tu cámara, tus objetivos, tu Luminar o una decisión tuya. Cuando cierres una, marca la casilla. Si el resultado no coincide con la guía, **manda lo que ves**: anótalo aquí y corrijo la guía.

## 1 · Urgente: que la cámara dispare en RAW

Las fotos de Namibia salieron **solo en JPEG** por un error de configuración. Antes de la próxima salida:

- [ ] `Toma → [Calid. img/grab.] → [Formato archivo]` = **RAW**, con `Tipo archivo RAW` = comprimido sin pérdida ([configuración básica](manejo-a6700/04-configuracion-basica.md)).
- [ ] Carga **MR1** y mira su **balance de blancos**: tiene que ser Luz de día, no el Kelvin de la noche. El 91 % de las fotos del viaje se hizo con un balance fijo y las de sombra y anochecer salieron azuladas; dime cuál tenías puesto.
- [ ] Carga **MR1** y comprueba otra vez el formato. Haz lo mismo con **MR2**. Si alguna vuelve a JPEG, pon RAW y **vuelve a guardar esa memoria** (`Toma → [Modo de toma] → [Mem. ajustes cám]`).
- [ ] Foto de prueba → al ordenador: tiene que haber un archivo **`.ARW`**.
- [ ] Si quieres saber **qué falló** en Namibia: abre una foto del viaje en la cámara o en el ordenador y anota qué formato y qué tamaño tiene. Así sabremos si fue el formato, una memoria o un reinicio de ajustes.

## 2 · La cámara: 11 nombres de menú por confirmar

La auditoría confirmó las 79 rutas, pero estos nombres no se pudieron localizar ([verificación de los menús](manejo-a6700/15-verificacion-de-menus.md)). Ponte sobre cada línea y pulsa **C3**: la Guía en la cámara muestra el nombre oficial.

- [ ] `Tem.col./filtro` (dentro de `Balance blanco`)
- [ ] `Cuadr. regl. terc.`
- [ ] `C. sin pérd.`
- [ ] `Compens. variación`
- [ ] `Punto: S/M/L`
- [ ] `Conmut. dest. recon.`
- [ ] `Botón personaliz. 1/3`
- [ ] `Solo pant. táctil`
- [ ] `Mostrar toda info.`
- [ ] `Monitor desactiv.`
- [ ] «Separe el modo M y los otros modos.»

## 3 · El Viltrox 25 mm

- [ ] ¿Es el **AF 25 mm F1.7 Air**? Lo pone en el barrilete o en la caja. Si es otro modelo, la ficha de [su guía](manejo-a6700/11-viltrox-25mm.md) puede cambiar.
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
- [ ] **Apilado en Mac:** ¿acepta JPEG la versión de prueba de [Starry Landscape Stacker](https://sites.google.com/site/starrylandscapestacker/home)? ¿Tienes series de fotos nocturnas iguales y seguidas para apilar? ([retoques, 9.2](retoques/09-noche.md#apilar-una-serie-fuera-de-luminar))
- [ ] **HEIF:** haz una foto con `Conm JPEG/HEIF` en `HEIF(4:2:2)` y ábrela en Luminar. ¿La abre? ([retoques, 15.4](retoques/15-disparar-mejores-jpeg.md#154-lo-que-enseñan-tus-fotos-de-namibia))
- [ ] **Exportar a TIFF:** ¿ofrece Luminar 16 bits? Y en **Sharpen**, ¿qué niveles aparecen?
- [ ] **Polvo del sensor:** tus fotos de día tienen manchas arriba a la izquierda del cielo. ¿Se puede copiar o sincronizar **Remove Dust Spots** entre fotos? (Skylum dice que Erase no se sincroniza.) Y limpia el sensor antes de la próxima salida.
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
- [ ] El estado del equipo de [equipo y accesorios](manejo-a6700/10-equipo-accesorios.md) es del **25 de octubre**. ¿Ha cambiado algo?
- [ ] **Capturas de los menús:** el [guion](manejo-a6700/img/menus/) tiene 14 imprescindibles (marcadas ★). Hazlas con el móvil y ejecuta `python3 manejo-a6700/img/menus/insertar.py`.
- [ ] En **macOS Vista Previa**: comprueba que la ruta para quitar la ubicación de una foto es la de [retoques, 14.3](retoques/14-etica.md) (Herramientas → Mostrar inspector → ubicación).

## 7 · Decisiones

- [ ] ¿Traigo las guías **"después del viaje"** de a6700-namibia (el archivo y la selección: copias 3-2-1, criba en dos pasadas, las 20 finales)?
- [ ] ¿Escribo un capítulo de **Luminar con RAW** para las próximas salidas? (Depende de la comprobación de la sección 4.)
- [ ] ¿Añado el **Viltrox** a la [chuleta](manejo-a6700/16-chuleta.md)? Tiene que seguir cabiendo en una cara.
- [ ] Hay 81 enlaces que llevan a **a6700-namibia** para guías no copiadas. ¿Mantienes ese repo publicado, o traigo lo que te interese?
