<!-- nav -->
[← Anterior](14-menu-completo.md) · [Índice](README.md) · [Siguiente →](16-chuleta.md)
<!-- /nav -->

*Parte IV · Referencia*

# 15. Verificación de los menús — cada ruta, contra la Guía de ayuda de Sony

> 🟢 **Iniciación** · Da por sabido: el [capítulo 2](02-menus-y-primer-dia.md) (qué es MENU y cómo se usa C3 como Guía en la cámara) · Te desbloquea: confiar en que cada línea de menú de este repo existe tal cual en tu cámara, y saber qué falta por confirmar.

**Qué resuelve.** Este repo te pide tocar decenas de líneas del menú de la a6700. Esta página recoge la **auditoría independiente** de esas rutas, hecha el **3 de noviembre de 2026** contra la Guía de ayuda oficial en español. Es el Anexo A de la [edición completa en PDF](../sources/README.md). Resultado: **las 79 rutas son correctas**. Quedan **11 subopciones** por confirmar en la propia cámara (diez minutos, con C3), y la auditoría encontró **un error de formato**, ya corregido aquí.

> **Lo que describen las guías de `manejo-a6700/` es cómo está configurada tu cámara.** Si algún día un nombre de la pantalla no coincide con el de la guía, **manda el de la pantalla**: anótalo y corrígelo en el repo.

## Resumen

| Comprobación | Resultado | Estado |
|---|---|---|
| Rutas `Pestaña → [Grupo] → [Ajuste]` distintas en el repo | 79 rutas, 176 apariciones en total | ✅ 79/79 coinciden |
| Pestañas citadas | 8 de 8 (Principal, Toma, Exposición/color, Enfoque, Reproducc., Red, Ajustes, Mi Menú) | ✅ Nombres exactos |
| Grupos que el repo usa en rutas | 33 de los 54 oficiales | ✅ Todos existen y en su pestaña |
| Grupos y elementos de [el menú completo](14-menu-completo.md) | Las 8 pestañas, grupo a grupo | ✅ Sin elementos inventados ni mal colocados |
| Nombres de segundo nivel verificados | 12 nombres o familias de valores | ✅ 12 coinciden en la ficha |
| Nombres de segundo nivel no localizados | 11 subopciones | ❓ Pendientes de comprobar en la cámara (C3) |
| Errores que impidan encontrar un ajuste | Ninguno | ✅ |
| Otros hallazgos | 1 error de formato que ocultaba medio capítulo 3 en GitHub, y 2 mejoras menores | ✅ Aplicados en este repo |

**Conclusión de la auditoría:** las auditorías previas (agosto y octubre de 2026) se sostienen. Las abreviaturas del repo (`Calid. img/grab.`, `Obturad./silenc.`, `Rest/guard ajust`, `AF c/obturador`…) son las mismas que usa Sony en pantalla y **no deben "corregirse"** a formas largas.

## Método

- **Referencia principal:** la página oficial *Búsqueda de funciones desde MENU*, que enumera las 8 pestañas, sus 54 grupos y sus 260 elementos, e indica en qué posición del selector Foto/Vídeo/S&Q aparece cada uno.
- **Fuente:** Guía de ayuda ILCE-6700 α6700, edición en español, referencia **5-051-980-47(1)**, © 2023 Sony Corporation. Ya recoge funciones del **firmware 2.00**. Si Sony publica una revisión posterior, mandan los nombres de la pantalla de la cámara actualizada.
- **Pasos:** se extrajeron todas las rutas con la forma `Pestaña → [Grupo] → [Ajuste]`, se compararon carácter a carácter (abreviaturas incluidas) con la tabla oficial, se repasó el menú completo grupo a grupo y se revisaron los nombres de segundo nivel en las fichas individuales del a6700.

## Nombres de segundo nivel (valores y subopciones)

| Nombre en el repo | Lo que dice Sony | Estado |
|---|---|---|
| `Obturad. electr.` (valor de `Tipo de obturador`) | Valores exactos: `Obturad. mecán.` y `Obturad. electr.`. La a6700 **no** ofrece `Automático` | ✅ |
| `Ave`, `Animal`, `Animal/ave`, `Humano`, `Coche/tren` | Valores de `Dest. reconocim.`: Humano, Animal/ave, Animal, Ave, Insecto, Coche/tren, Avión | ✅ |
| `Multi` · `Centro` · `Puntual` · `Prom. pant. ent.` · `Iluminación` | Los cinco modos de `Modo medición`, con esos nombres | ✅ |
| `Vínc. punto enf.` | Vínculo de `Punto med. punt.` con el área de enfoque | ✅ |
| `Reten. select. AF/MF` / `Alter. select. AF/MF` | Funciones asignables en `Ajustes → [Personal. operac.] → [Ajuste t. pers./dial]` | ✅ |
| `Guard./carg. ajustes` → `Cargar` / `Guardar` / `Borrar` | Ruta `Ajustes → [Rest/guard ajust] → [Guard./carg. ajustes]`, con esas tres opciones | ✅ |
| `Versión` (cuerpo y objetivo) | `Ajustes → [Opción ajustes] → [Versión]`; muestra cuerpo y objetivo | ✅ |
| `Verificac. luminosa`, `Amplific. enfoque`, `AF c/obturador`, `Captura contin.`, `Autodisp.(senc)`, `Variación expos.` | Nombres exactos en el índice oficial | ✅ |
| `Func. táctil dur. toma` (en `Ajust. pantalla táctil`) | En `Ajust. pantalla táctil → Pantalla de toma`: `Seguimient. táct.`, `Obturador táctil`, `AE táctil` y `Desac.` | ✅ |
| `Número archivo` (`Serie` / `Reponer`) y `Nombre carpeta` (`Forma fecha`) | Subopciones de `Aj. archiv./carpet.`. La ruta está verificada en el a6700; los nombres de las subopciones, en guías Sony de la misma generación | ✅ ruta · ⚠️ subopciones |
| `Tipo obturad. interv.` (dentro de `Func. capt. interv.`) | Existe en guías Sony de la misma generación; según Sony, va en obturador electrónico por defecto, sea cual sea `Tipo de obturador` | ✅ nombre · ⚠️ valor por defecto confirmado en un modelo hermano |

## Pendiente: 11 subopciones por confirmar en la cámara

Estos nombres no salen en la lista principal de Sony y no se pudo abrir su ficha durante la auditoría. Lo más probable es que estén bien, pero **no están confirmados**:

- [ ] `Tem.col./filtro`: valor de `Balance blanco` para fijar los grados Kelvin ([balance de blancos](../conceptos/02-balance-de-blancos.md), [diales y botones](03-diales-y-botones.md))
- [ ] `Cuadr. regl. terc.`: tipo de cuadrícula
- [ ] `C. sin pérd.`: RAW comprimido sin pérdida
- [ ] `Compens. variación`
- [ ] `Punto: S/M/L`: tamaños del área de enfoque
- [ ] `Conmut. dest. recon.`
- [ ] `Botón personaliz. 1/3`
- [ ] `Solo pant. táctil`
- [ ] `Mostrar toda info.`
- [ ] `Monitor desactiv.`
- [ ] «Separe el modo M y los otros modos.»

**Cómo cerrarlos en diez minutos:** con la cámara encendida, sitúate sobre cada línea del menú y pulsa **C3** (la papelera). La Guía en la cámara muestra el nombre oficial y su explicación. Si alguno difiere, manda el de la pantalla: anótalo y corrígelo en el repo.

## Hallazgos de la auditoría y qué se hizo

| # | Hallazgo | Qué se hizo en este repo |
|---|---|---|
| 1 | Ninguna ruta errónea: ni las recetas ni la referencia de ajustes necesitan correcciones | Nada que cambiar |
| 2 | Con `Obturad. electr.` **no están disponibles** el flash, `RR exposic. larga`, `e-Prim. cortin. obtur.`, la toma BULB ni la toma sin parpadeo. Eso explica por qué el plan B contra las franjas de los LED es el obturador mecánico | Añadido al [capítulo 9](09-safari-nocturno-charcas.md), paso 2 y tabla "si sale mal" |
| 3 | La captura de `AF c/obturador` se llamaba `af-con-disparador.jpg`, con el nombre antiguo e incorrecto | Renombrada a `af-c-obturador.jpg` en el [guion de capturas](img/menus/) y en `insertar.py` |
| 4 | En [diales y botones](03-diales-y-botones.md), el diagrama "la botonera en 15 minutos" no tenía la valla de cierre: en GitHub, el resto del capítulo no se veía | Valla añadida: el capítulo entero vuelve a verse |
| 5 | La Guía consultada (5-051-980-47(1)) ya recoge el firmware 2.00 | Anotado arriba, en *Método* |

**Cobertura del menú completo.** [El menú completo](14-menu-completo.md) describe el menú con el selector en **Foto**. Los grupos oficiales que no aparecen en sus tablas están justificados: `Grabac. sonido`, `TC/UB`, `Visual. marcador` y `Opción de toma` son solo de Vídeo/S&Q; `Accesibilidad` es "para algunos modelos solamente"; los elementos solo de vídeo dentro de grupos mixtos no se ven con el selector en Foto; `Calidad HEIF` y `Tamaño img HEIF` van junto a sus equivalentes JPEG; `Aviso de privacidad` y `Logotip. certificación` son informativos.

## Mapa oficial del menú

La estructura oficial completa, pestaña → grupo → elementos, transcrita de la Guía de ayuda. Sirve para encontrar cualquier línea aunque el repo no la cite.

### Pestaña Toma

| Grupo | Elementos |
|---|---|
| `Calid. img/grab.` | Conm JPEG/HEIF · Formato archivo · Tipo archivo RAW · Calidad JPEG · Calidad HEIF · Tamañ img JPEG · Tamaño img HEIF · Relación aspecto · Ajustes de vídeo · Aj. cám. len+ráp · Ajust. time-lapse · Ajuste de toma Log · Ajustes proxy · RR exposic. larga · RR ISO Alta · Imágenes fij. HLG · Rango color · Compens. objetiv. |
| `Soporte` | Formatear · Recuper. BD imág · Ver info soporte |
| `Archivo` | Aj. archiv./carpet. · Selec. carpeta grab. · Carpeta nueva · Inform. de copyright · Inscrib. núm. serie · Ajustes archivo |
| `Modo de toma` | Modo de toma · Autom./sel. escena · Recup. ajust. cám. · Mem. ajustes cám · Reg ajuste toma pers |
| `Modo de manejo` | Modo manejo · Ajustes de Variación · Func. capt. interv. |
| `Obturad./silenc.` | Aj. modo silenc. · Tipo de obturador · e-Prim. cortin. obtur. · Liber. sin objetivo · Liberar sin tarj. mem. · Ajust. sin parpadeo |
| `Grabac. sonido` | Grabación de sonido · Nivel grabac. audio · Tiempo Salid. Audio · Reducc. ruido viento · Sonido zapata |
| `TC/UB` | Time Code Preset · User Bit Preset · Time Code Format · Time Code Run · Time Code Make · User Bit Time Rec |
| `Estabiliz. de img` | SteadyShot · Adaptac. SteadyS. · Distanc. focal |
| `Zoom` | Zoom · Rango del Zoom · Tecla pers. vel. z. · Vel. zoom remota |
| `Visualizac. toma` | Vis. lín. cuadrícul. · Tipo lín. cuadríc. · Ajust. vis. en directo · Vis. resalt dur GR. |
| `Visual. marcador` | Visual. marcador · Marcador central · Marcador aspecto · Zona seguridad · Guía de encuadre |
| `Opción de toma` | Autodisparador · Ajust. encuadre auto |

### Pestaña Exposición/color

| Grupo | Elementos |
|---|---|
| `Exposición` | Aj. temporiz. BULB · Auto obtur. lento · ISO · Límite rango ISO · ISO AUTO VO mín. |
| `Compens. expos.` | Compensar exp. · Paso exposición · Ajuste están. exp. |
| `Medición` | Modo medición · Cara en multimed. · Punto med. punt. · AEL con obturad. |
| `Flash` | Modo flash · Compensac. flash · Ajust.comp.exp. · Flash inalámbrico · Reducción ojos rojos · Ajustes flash externo · Reg. ajust toma flash |
| `Balance blancos` | Balance blanco · Ajuste prior AWB · Bloq.AWB dispar. · WB sin vibracion. |
| `Color/tono` | Opt. gama diná. · Aspecto creativo · Perfil de imagen · Seleccionar LUT · Gestionar LUT usuar. · Efecto piel suave |
| `Visualizac. cebra` | Visualizac. cebra · Nivel de cebra |

### Pestaña Enfoque

| Grupo | Elementos |
|---|---|
| `AF/MF` | Modo de enfoque · Ajuste prior en AF-S · Ajuste prior en AF-C · Sens. Seguim. AF · Iluminador AF · Manejo abertura AF · AF c/obturador · Enf. m. d. tpo compl. · Pre-AF · Vel. transición AF · S. camb motiv. AF · Ayuda de AF |
| `Área de enfoque` | Área de enfoque · Lím. área enfoque · Conm.áreaAF V/H · Col. cuadro enfoq. · Registro área AF · Borr. área AF reg, · Desact. Aut. Área AF · Vis. área dur seguim. · Visual. área AF-C · Área detección fase · Circ. punto enfoq. · Cant mov cdro AF |
| `Reconoc. motivo` | Rec. motivo en AF · Dest. reconocim. · Aj. conm. dest rec · Selecc. ojo d./izq. · Vis. cuadro rec. m. · Registro rostros · Priorid. rostro reg. |
| `Asistencia enfoq.` | Mapa de enfoque · Amplif. autom. MF · Amplific. enfoque · Tiemp. aum. enf. · Aum. inic. enfoq. · AF en ampl. enfoq |
| `Visualiz. resalte` | Visualizac. resalte · Nivel de resalte · Color de resalte |

### Pestaña Reproducc.

| Grupo | Elementos |
|---|---|
| `Objet. de reprod.` | Modo visualización |
| `Aumento` | Aumentar · Aum. aumento inic · Aum. posic. inicial |
| `Selección/nota` | Proteger · Valoración · Ajust. val.(tecl. pers) |
| `Borrar` | Borrar · Borrar puls. 2 vec. · Confirm.Borrar |
| `Editar` | Recortar · Rotar · Toma fotográfica · Conm JPEG/HEIF |
| `Visualización` | Repr. cont. interv. · Veloc. repr. interv · Diapositivas |
| `Opción reprod.` | Índice imágenes · Mostrar como grupo · Rotación visualizac. · Vis. cuadro enfoq. · Visual. img h especif. · Ajuste salto imagen |

### Pestaña Red

| Grupo | Elementos |
|---|---|
| `Conex./PC rem.` | Conex. smartphone · Función PC remoto · Sel. en cám. y env. · Rest. estado transf · Conex. dur. APAG. · Ajuste toma remota |
| `Transmitir` | Transm. por USB |
| `Creators' Cloud` | Conexión a nube · Información de nube |
| `Wi-Fi` | Conectar por Wi-Fi · WPS Push · Conf. punto acceso · Banda de frec. Wi-Fi · Muestra info Wi-Fi · Rest. SSID/Cntrsñ |
| `Bluetooth` | Función Bluetooth · Emparejamiento · Gest. disp. emparej. · M. a dist. Bluetooth · Mostr. direcc. dispos |
| `LAN con cable` | Ajuste direcc. IP · Muestra info LAN cbl |
| `USB-LAN/c. con.` | Conexión USB-LAN · Desconex. USB-LAN · Conex. compartida · Desc conex. compart |
| `Opción de red` | Modo avión · Edit. Nombre Dispos. · Import. certific. raíz · Ajust. autent. acceso · Info. autent. acceso · Ajustes Wi-Fi Direct · Restablecer conf. red |

### Pestaña Ajustes

| Grupo | Elementos |
|---|---|
| `Área/fecha` | Idioma · Aj. área/fecha/hora · Selector NTSC/PAL |
| `Rest/guard ajust` | Restablecer ajuste · Guard./carg. ajustes |
| `Personal. operac.` | Ajuste t. pers./dial · Aj. Tecla person. · Ajustes del menú Fn · Ajust dif imgs fij/víd · Aj. DISP (vis. pant.) · REC bot. disparad. · Rotación anillo zoom |
| `Personalizar dial` | Ajuste t. pers./dial · Ajustes de Mi dial · Rotación de Av/Tv · Bloqueo dial/rueda |
| `Operación táctil` | Operación táctil · Pantall./almoh. táctil · Ajust. pantalla táctil · Ajust. almohad.táctil |
| `Accesibilidad` | Lector de pantalla |
| `Visor/monitor` | Sel. visor/monitor · Brillo de monitor · Brillo del visor · Temper. color visor · Calidad visual · Vel. transm. visor · Dir. volteo monitor |
| `Opción de visual.` | Ajust. visual. TC/UB · Asist. visual. Gamma · T.asist. vis. Gamma · Visualizar LUT · Visual. tomas rest. · Rev.automática · Pant. sel. modo toma |
| `Opc. ajuste enrg.` | DESACT mon. aut. · Hora inic. ahor. ener. · Ahorr. en. con mon. · Temp. APAGA auto |
| `Opción sonido` | Ajustes de volumen · Monit. sonido 4ch · Señales audio |
| `USB` | Modo conexión USB · Ajuste USB LUN · Alimentación USB |
| `Salida externa` | Resolución HDMI · Aj. salida HDMI · Mostrar infor. HDMI · CTRL.POR HDMI |
| `Opción ajustes` | Modo luz de vídeo · Limpieza del sensor · Asign. auto. píxeles · Asignación píxeles · Versión · Mostr. núm. de serie · Aviso de privacidad · Logotip. certificación |

### Pestaña Mi Menú

| Grupo | Elementos |
|---|---|
| `Ajuste Mi Menú` | Añadir elemento · Ordenar elemento · Borrar un elemento · Borrar una página · Borrar todo · Mostrar de Mi Menú |

## Referencias

- Guía de ayuda a6700 (español), *Búsqueda de funciones desde MENU*: <https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_list_of_menu_items_ilc2320.html>
- Índice de la Guía de ayuda en español: <https://helpguide.sony.net/ilc/2320/v1/es/index.html>
- Versión imprimible completa (PDF): <https://helpguide.sony.net/ilc/2320/v1/es/print.pdf>
- Fichas consultadas en la auditoría: `0414H_shutter_type`, `211h_recognition_target`, `0406_metering_mode`, `0405_af_mf_control`, `0601_save_load_settings`, `202h_version`, `211h_touchpanel_settings`, `0412D_marker_display`, `221h_main_menu_ilc2320`, `211h_usb_streaming`
- La auditoría completa, en su forma original: Anexo A de la [edición completa en PDF](../sources/README.md)

<!-- nav -->
[← Anterior](14-menu-completo.md) · [Índice](README.md) · [Siguiente →](16-chuleta.md)
<!-- /nav -->
