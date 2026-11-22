# Verificación de datos: menús, ajustes, botones y comportamiento de la Sony a6700

Fecha de la comprobación: 22 de noviembre de 2026. Fuente única usada para dar algo por verificado: la Guía de ayuda oficial de la ILCE-6700 en español, referencia de manual **5-051-980-47(1)**, descargada entera en esta sesión (359 páginas de `https://helpguide.sony.net/ilc/2320/v1/es/contents/`). La Guía ya menciona el firmware 2.00 (en 13 páginas, p. ej. [Versión](https://helpguide.sony.net/ilc/2320/v1/es/contents/202h_version.html)). Abreviatura usada abajo: **HG** = `https://helpguide.sony.net/ilc/2320/v1/es/contents/`.

Clasificación: **OK** (la Guía muestra ese texto) · **ERROR** (la Guía dice otra cosa) · **IMPRECISO** (cierto a medias o con el nombre largo/otro nombre) · **SIN FUENTE** (la Guía no lo dice; no se pudo comprobar) · **DESACTUALIZADO**.

Totales:

| Qué se contó | Comprobados | OK | No OK |
|---|---|---|---|
| Rutas distintas `Pestaña → [Grupo] → [Ajuste]` en los capítulos en alcance (sin el 15), comparadas por script con la lista oficial | 54 | 54 existen tal cual | 1 de ellas no aparece con el selector en Foto (`Modo de toma`) |
| Mapa oficial del capítulo 15 (pestañas, grupos, elementos) | 8 pestañas, 54 grupos, 260 elementos | Coincide el recuento | 1 omisión menor (`Formato archivo` de película) |
| Las 11 subopciones marcadas con ❓ en el capítulo 15 | 11 | 11 confirmadas | 0 |
| Afirmaciones de valor o comportamiento revisadas contra su ficha | unas 120 | unas 95 | 3 ERROR · 14 IMPRECISO · 9 SIN FUENTE · 0 DESACTUALIZADO |

Las cifras de la última fila son aproximadas: las tablas del capítulo 14 se compararon leyendo, no con script.

## 1. ¿Coinciden las rutas de menú y los valores con la Guía de ayuda?

### Takeaway
Todas las rutas `Pestaña → [Grupo] → [Ajuste]` existen con esa pestaña, ese grupo y esa abreviatura. Los fallos están en unos pocos nombres escritos en forma larga o inventada (`Ajuste SteadyShot`, «Cambiar área AF V/H», «Regla de tres», «Luz de día») y en una ruta que solo existe en vídeo (`Toma → [Modo de toma] → [Modo de toma]`).

### Cited Findings

**Errores e imprecisiones (lo que hay que corregir)**

| # | Clase | Archivo y línea | Lo que dice el repo | Lo que dice la Guía | Corrección propuesta |
|---|---|---|---|---|---|
| 1 | ERROR | `manejo-a6700/04-configuracion-basica.md` 48 y 169 | `Ajuste SteadyShot` en Auto; tabla ES/EN «Ajuste SteadyShot / SteadyShot Adjust» | El ajuste se llama `Adaptac. SteadyS.`, con valores `Automático` / `Manual` — [HG 0414F](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414F_steadyshot_setting.html). En inglés, «SteadyShot Adjust.» — [lista EN](https://helpguide.sony.net/ilc/2320/v1/en/contents/221h_list_of_menu_items_ilc2320.html). «Ajuste SteadyShot» no aparece en ninguna página de la Guía | `Adaptac. SteadyS.` en `Automático` |
| 2 | ERROR | `manejo-a6700/12-af-y-exposicion-a-fondo.md` 87-88 | menú de Enfoque → Área de enfoque → «Cambiar área AF V/H» | `Enfoque → [Área de enfoque] → [Conm.áreaAF V/H]`, valores `Desactivar` / `Solo punto AF` / `Punto AF+ár. AF` — [HG 0405L](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405L_focusarea_switch.html) | Usar `Conm.áreaAF V/H` → `Punto AF+ár. AF` |
| 3 | ERROR | `manejo-a6700/13-ajustes-a6700.md` 116 (y 151) | `Toma → [Modo de toma] → [Modo de toma]` = M | El elemento `Modo de toma` solo se muestra en película/S&Q (elige cámara lenta o time-lapse); en foto el modo M se pone con el dial de modo — [lista oficial](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_list_of_menu_items_ilc2320.html), [dial de modo](https://helpguide.sony.net/ilc/2320/v1/es/contents/202h_still_movie_sq_dial.html) | «Dial de modo en **M**», sin ruta de menú |
| 4 | IMPRECISO | `13-ajustes-a6700.md` 88; `02-menus-y-primer-dia.md` 241 | Valor «Regla de tres» | `Cuadr. regl. terc.` (las otras: `Cuadríc. cuadr.`, `Cuad. d.+cuadr.`) — [HG 201h_grid_line_type](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_grid_line_type.html) | `Cuadr. regl. terc.` (regla de los tercios) |
| 5 | IMPRECISO | `13-ajustes-a6700.md` 75; `04-configuracion-basica.md` 40 | «Comprimido sin pérdida» | En pantalla: `C. sin pérd.` — [HG 0404I](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404I_raw_file_type.html) | Unificar con el capítulo 14: `C. sin pérd.` |
| 6 | IMPRECISO | `04-configuracion-basica.md` 43 | `RR ISO Alta`: «Desactivar/Baja» | Valores `Normal` / `Bajo` / `Desactivar` — [HG 0414C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414C_high_iso_nr.html) | «Bajo» |
| 7 | IMPRECISO | `04-configuracion-basica.md` 125; `conceptos/04-balance-de-blancos.md` 18, 27-31; `retoques/15-disparar-mejores-jpeg.md` 23 | Preajuste «Luz de día» | En pantalla: `Luz diurna` (y `Sombra`, `Nublado`) — [HG 0410C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html) | `Luz diurna` cuando se hable de la a6700 |
| 8 | IMPRECISO | `conceptos/04-balance-de-blancos.md` 18-19 | «elige … K y ajusta ahí el número con la rueda» | El valor se llama `Tem.col./filtro`; la temperatura se cambia «girando el dial trasero» o con el lado derecho de la rueda (pantalla de ajuste fino) — [HG 0410C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html) | «elige `Tem.col./filtro` y gira el dial trasero» (como ya dicen los capítulos 3 y 14) |
| 9 | IMPRECISO | `14-menu-completo.md` 204 | `Ajust. sin parpadeo`: «solo con obturador mecánico» | Solo `Toma sin parpad.` exige obturador mecánico; `Obturad. variable` funciona con «Obturador electrónico/obturador mecánico» — [HG comparación](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_anti_flicker_comparison.html) | Distinguir los dos subajustes |
| 10 | IMPRECISO | `14-menu-completo.md` 199 | `Aj. modo silenc.`: «Silencio total» | «Aunque [Modo silencioso] esté ajustado a [Activar], el silencio no será completo» — [HG 0414D](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414D_silent_mode_setting.html) | Quitar «total» |
| 11 | IMPRECISO | `14-menu-completo.md` 201 | `e-Prim. cortin. obtur.`: Activar siempre | «Cuando utilice un objetivo de otro fabricante … ajuste esta función a [Desactivar]» — [HG 0414](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_electronic_front_curtain.html). Afecta al Viltrox 25 mm | Añadir: con el Viltrox, `Desactivar` |
| 12 | IMPRECISO | `15-verificacion-de-menus.md` 90 | `Calid. img/grab.` lista «Formato archivo» una vez | La lista oficial tiene dos: el de foto y el de película — [lista oficial](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_list_of_menu_items_ilc2320.html) | Añadir «Formato archivo (película)» |

**Confirmado (OK)**

- Las 8 pestañas (Principal, Toma, Exposición/color, Enfoque, Reproducc., Red, Ajustes, Mi Menú), los 54 grupos y los 260 elementos — [lista oficial](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_list_of_menu_items_ilc2320.html). La Guía llama «ficha» a la pestaña.
- `Toma → [Calid. img/grab.]`: `Formato archivo` (RAW · RAW & JPEG · JPEG), `Tipo archivo RAW` (`C. sin pérd.` / `Comprimido`), `Conm JPEG/HEIF` (`JPEG` / `HEIF(4:2:0)` / `HEIF(4:2:2)`; 4:2:2 «da prioridad a la calidad de imagen»; aviso de compatibilidad), `Relación aspecto` (3:2, 4:3, 16:9, 1:1; RAW siempre 3:2), `Rango color` (sRGB/AdobeRGB), `Imágenes fij. HLG`, `Compens. objetiv.` (`Compens. sombras`, `Comp. aber. cromát.`, `Compens. distorsión`, `Compens. variación` solo en vídeo) — [0404M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404M_file_format.html), [0404I](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404I_raw_file_type.html), [201h_jpeg_heif_switch](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_jpeg_heif_switch.html), [0414M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414M_lens_comp.html).
- El RAW comprimido baja a 12 bits en `Captura contin.` — [0404M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404M_file_format.html).
- `Toma → [Soporte] → [Formatear]`: borra también las protegidas y M1–M4; formatear en la cámara — [0601_memory_format](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_memory_format.html).
- `Aj. archiv./carpet.` → `Número archivo` (`Serie` / `Reponer`) y `Nombre carpeta` (`Forma normal` / `Forma fecha`): ahora confirmados en la ficha de la a6700 (el capítulo 15 los daba por «guías de la misma generación») — [0601_file_folder_settings](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_file_folder_settings.html).
- `Toma → [Obturad./silenc.]`: `Tipo de obturador` (`Obturad. mecán.` / `Obturad. electr.`), `Liber. sin objetivo` y `Liberar sin tarj. mem.` (`Habilitar` / `Inhabilitar`; «El ajuste predeterminado es [Habilitar]») — [0414H](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414H_shutter_type.html), [0414G](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414G_release_without_card.html).
- `Modo manejo`: `Captura contin.` (Hi+/Hi/Mid/Lo), `Autodisp.(senc)` (10, 5, 2 s), `Variación expos.`, `Var.exp. enfoque`; está en el lado izquierdo de la rueda — [0407C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0407C_drive_mode.html), [0407](https://helpguide.sony.net/ilc/2320/v1/es/contents/0407_drivemode_selftimer.html).
- Hi+ 11 · Hi 8 · Mid 6 · Lo 3 imágenes por segundo, 10 en RAW sin pérdida; búfer de 23 RAW sin pérdida; en Hi+ el visor no va en tiempo real — [especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html), [0407C continuous](https://helpguide.sony.net/ilc/2320/v1/es/contents/0407C_drivemode_continuous.html).
- Obturador mecánico 1/4000–30 s y BULB; electrónico 1/8000–30 s — [especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html).
- `Estabiliz. de img`, `Zoom` (`Solo zoom óptic.`; los zooms no ópticos no van en RAW y anulan el reconocimiento de motivo), `Visualizac. toma` (`Ajust. vis. en directo` → `Efecto ajust. act.`) — [0401B](https://helpguide.sony.net/ilc/2320/v1/es/contents/0401B_available_zoom.html), [0414_live_view](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_live_view_disp_set.html).
- `Exposición/color`: ISO 50–102400, `ISO AUTO máximo`/`mínimo`, ISO AUTO de 100 a 6400 por defecto; `ISO AUTO VO mín.` solo en P y A; `Aj. temporiz. BULB` 2–900 s; `Paso exposición` 0,5/0,3 EV; `Modo medición` (`Multi`, `Centro`, `Puntual`, `Prom. pant. ent.`, `Iluminación`); `Punto med. punt.` (`Centro` / `Vínc. punto enf.`); `Opt. gama diná.`; `Aspecto creativo` (ST, PT, VV, BW…) — [0408C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0408C_iso.html), [especificaciones](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_specifications_ilc2320.html), [211h_bulb_timer](https://helpguide.sony.net/ilc/2320/v1/es/contents/211h_bulb_timer.html), [0406](https://helpguide.sony.net/ilc/2320/v1/es/contents/0406_metering_mode.html), [0406L](https://helpguide.sony.net/ilc/2320/v1/es/contents/0406L_spotmetering_link_focus_point.html).
- `Enfoque`: `Modo de enfoque` (`AF toma sencilla`, `AF automático`, `AF continuo`, `DMF`, `Enfoque man.`), `Sens. Seguim. AF` (`5(reactivo)` … `3(estándar)` … `1(fijado)`), `Iluminador AF` (`Automático` / `Desactivar`), `AF c/obturador`, `Pre-AF`, `Área de enfoque` (`Ancho`, `Zona`, `Fijo al centro`, `Punto: S/M/L`, `Punto expandido`, `Seguimiento` solo en AF-C), `Dest. reconocim.` (`Humano`, `Animal/ave`, `Animal`, `Ave`, `Insecto`, `Coche/tren`, `Avión`), `Aj. conm. dest rec`, `Selecc. ojo d./izq.`, `Tiemp. aum. enf.` (`Sin límite`), `Aum. inic. enfoq.` (x1,0 / x6,1), `Visualiz. resalte` (niveles y colores) — [0405C_focus_mode](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405C_focus_mode.html), [0405C_autofocus_area](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405C_autofocus_area.html), [0405D](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405D_af_tracking_sensitivity.html), [211h_recognition_target](https://helpguide.sony.net/ilc/2320/v1/es/contents/211h_recognition_target.html), [0405M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405M_peaking_display.html).
- `Reten. select. AF/MF` / `Alter. select. AF/MF`, y que el conmutador del objetivo tiene prioridad — [0405_af_mf_control](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405_af_mf_control.html).
- `Reproducc.`: `Modo visualización` (`Ver fecha`), `Aum. posic. inicial` (`Posic. enfocada`), `Valoración`, `Ajust. val.(tecl. pers)`, `Borrar puls. 2 vec.` (`Desac.`), `Confirm.Borrar` (`1° "Cancelar"`), `Índice imágenes` (9/30), `Vis. cuadro enfoq.` (verde), `Ajuste salto imagen` (`Una por una`, `Solo valor.`), `Recortar` no admite RAW — [0506K](https://helpguide.sony.net/ilc/2320/v1/es/contents/0506K_enlarge_initial_position.html), [0506M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0506M_rating.html), [0601_delete_confirmation](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_delete_confirmation.html), [202h_image_jump_setting](https://helpguide.sony.net/ilc/2320/v1/es/contents/202h_image_jump_setting.html).
- `Ajustes`: `Restablecer ajuste` (`Reponer ajustes de cámara` / `Inicializar`; no borra imágenes), `Guard./carg. ajustes` (`Cargar` / `Guardar` / `Borrar`; hasta 10 por tarjeta), `Ajust dif imgs fij/víd` (lista de casillas con Abertura, Velocidad obturador, ISO, Compensar exp., Modo medición, Balance blanco, Perfil de imagen…), `Aj. DISP (vis. pant.)` → `Monitor` / `Visor`, `Bloqueo dial/rueda` (`Bloquear` / `Desbloquear`), `Rotación de Av/Tv` (`Normal`), `Pantall./almoh. táctil` (`Ambos válidos`, `Solo pant. táctil`, `Solo almoh. táct.`), `Ajust. pantalla táctil` → `Pantalla de toma` → `Func. táctil dur. toma` (`Enfoque táctil`, `Seguimient. táct.`, `Obturador táctil`, `AE táctil`, `Desac.`) y `Deslizar hacia arriba` (`Abrir el menú Fn`), `Ajust. almohad.táctil` → `Modo posición táctil` (`Posic. absoluta` / `Posición relativa`), `Brillo de monitor` (`Manual` −2 a +2 / `Tpo soleado`), `Calidad visual`, `Vel. transm. visor`, `Visual. tomas rest.` (`Mostrar siempre`), `Rev.automática` (10/5/2 s, `Desactivar`), `Hora inic. ahor. ener.` (`1 min.`), `Temp. APAGA auto` (`Estándar` / `Alto`, con aviso de quemaduras y trípode), `Señales audio`, `Alimentación USB`, `Asign. auto. píxeles`, `Asignación píxeles`, `Versión` (cuerpo y objetivo) — [0601_setting_reset](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_setting_reset.html), [0601_save_load_settings](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_save_load_settings.html), [201h_different_set](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_different_set_for_still_mv.html), [221h_dial_wheel_lock](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_dial_wheel_lock.html), [211h_touchpanel_settings](https://helpguide.sony.net/ilc/2320/v1/es/contents/211h_touchpanel_settings.html), [0601M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601M_touch_pad_settings.html), [0601L](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601L_auto_power_off_temperature.html), [201h_auto_pixel_mapping](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_auto_pixel_mapping.html).
- `Mi Menú`: hasta 42 elementos, ninguno de Reproducc.; `Mostrar de Mi Menú` → `Activar` — [0414L](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414L_add_mymenu_item.html), [0414_display_from_mymenu](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_display_from_mymenu.html).
- `Conex. dur. APAG.` gasta batería con la cámara apagada — [0703](https://helpguide.sony.net/ilc/2320/v1/es/contents/0703_connect_while_power_off.html).
- Nombres en inglés de la tabla del capítulo 4: «Camera Set. Memory», «Interval Shoot Func.», «AF w/ Shutter», «NTSC/PAL Selector», «Picture Profile» — [lista EN](https://helpguide.sony.net/ilc/2320/v1/en/contents/221h_list_of_menu_items_ilc2320.html).

### Inferences
- Los errores 1 y 2 parecen restos de textos anteriores a las auditorías: no tienen forma de ruta `→ [..] → [..]`, por eso las auditorías por patrón no los vieron.
- El error 3 pasa cualquier comparación automática porque el elemento existe; solo falla al mirar el icono de modo (película/S&Q) de la lista.

### Gaps
- Las tablas del capítulo 14 se compararon leyendo cada grupo contra la lista oficial; no hubo comparación por script de cada nombre entre comillas invertidas.
- No se abrieron las fichas de los grupos de Red (Wi-Fi, Bluetooth, LAN, USB-LAN) más allá de la lista oficial y `Conex. dur. APAG.`; sus nombres de elemento sí coinciden con la lista.
- Los valores de horquillado «3 fotos ±2 EV» (`17-verificacion-in-situ.md` 159-160): la ficha de `Variación expos.` no enumera los pasos disponibles; no se pudo comprobar.

## 2. ¿Son correctas las afirmaciones de comportamiento?

### Takeaway
Casi todas se sostienen palabra por palabra. Quedan sin respaldo en la Guía los Kelvin de los preajustes (5200/6000/7000 K), que `RR ISO Alta` afecte solo al JPEG, y que el balance de blancos y el formato de archivo se guarden en las memorias; y hay dos descripciones de manejo imprecisas (ampliar en reproducción y SteadyShot con el 70-350).

### Cited Findings

**Confirmado (OK)**

- Compensación de exposición: rango −5,0 a +5,0 EV; «−2,0 EV a +2,0 EV para películas»; en `Exposic. manual` «solamente cuando [ISO] está ajustado a [ISO AUTO]»; vive en el lado inferior de la rueda — [0406B](https://helpguide.sony.net/ilc/2320/v1/es/contents/0406B_exposure_compensation.html).
- Diales de fábrica en M: abertura con el dial frontal, tiempo de exposición con el trasero; con ISO AUTO el valor ISO parpadea si no alcanza la exposición — [0302C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0302C_manual_exposure.html). En A y en P valen los dos diales — [0302B](https://helpguide.sony.net/ilc/2320/v1/es/contents/0302B_aperture_priority.html), [programa](https://helpguide.sony.net/ilc/2320/v1/es/contents/0302B_program_auto.html).
- ISO: dial frontal y rueda en pasos de 1/3 EV, dial trasero en pasos de 1 EV — [0408C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0408C_iso.html).
- Rueda de control de fábrica: arriba DISP, abajo `Compensar exp.`/Índice imágenes, izquierda `Modo manejo`, derecha ISO; se pueden reasignar izquierda, derecha, abajo, centro y giro (arriba no figura) — [0201C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0201C_using_control_wheel.html).
- C1, C2, C3: C1 figura en «Laterales», y la ilustración lo sitúa en la esquina trasera derecha junto al gancho de la correa; C2 arriba junto a MOVIE; C3 en el respaldo, y en reproducción es Borrar — [laterales](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_names_of_parts_ilc2320_side.html), [superior](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_names_of_parts_ilc2320_top.html), [trasera](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_names_of_parts_ilc2320_back.html), [botones C](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_using_custom_button.html).
- `Área de enfoque` está en C2 de fábrica — [0405C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405C_autofocus_area.html). AF-ON en reproducción amplía — [trasera](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_names_of_parts_ilc2320_back.html).
- Guía en la cámara: seleccionar el elemento de MENU o Fn y pulsar el botón Borrar (C3) — [0105C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0105C_in_camera_guide.html).
- `Verificac. luminosa`: solo se asigna a una tecla desde `Ajuste t. pers./dial`; funciona en toma de imagen fija; se cancela al apagar, al salir de P/A/S/M, al poner un modo de enfoque distinto del manual, al ejecutarse `Amplif. autom. MF` y al seleccionar `Amplific. enfoque`; cambia `Visualiz. en directo` a `Efecto aj. desact.` — [0414H](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414H_bright_monitoring.html).
- DISP: vistas de toma `Mostrar toda info.`, `Sin información`, `Histograma`, `Nivel`, `Para el visor`, `Monitor desactiv.`; en reproducción, la vista de histograma hace parpadear las zonas sobrexpuestas o subexpuestas — [botón DISP](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_using_DISP_button.html), [0403B](https://helpguide.sony.net/ilc/2320/v1/es/contents/0403B_disp_set.html). Ningún capítulo en alcance menciona ese parpadeo: no hay nada que corregir, pero es un dato útil que falta.
- Zebra: niveles 70 a 100, `100 IRE o +`, `Personalizado 1` y `2` — [0406M](https://helpguide.sony.net/ilc/2320/v1/es/contents/0406M_zebra_display.html).
- `RR exposic. larga`: actúa desde 1 s, dura lo mismo que la exposición, y no está disponible con `Obturad. electr.` ni con `Captura contin.` o `Variación expos.` — [0414](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_long_exposure_nr.html).
- Obturador electrónico: sin flash, `RR exposic. larga`, `e-Prim. cortin. obtur.`, BULB ni `Toma sin parpad.` — [0414H](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414H_shutter_type.html). El aviso de franjas con luces parpadeantes está en la ficha de `Aj. modo silenc.` — [0414D](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414D_silent_mode_setting.html).
- Intervalómetro: `Toma → [Modo de manejo] → [Func. capt. interv.]`, con `Captura de intervalo`, `Hora inicio captura` (1 s a 99 min 59 s), `Intervalo de toma` (1 a 60 s, de inicio a inicio), `Número de capturas` (1 a 9999), `Sensib. Seguim. AE`, `Tipo obturad. interv.` y `Prior. intervalo toma`; `Tipo obturad. interv.` es `Obturad. electr.` por defecto «independientemente del ajuste para [Tipo de obturador]» — [0407P](https://helpguide.sony.net/ilc/2320/v1/es/contents/0407P_interval_shoot_setting.html). Esto cierra el ⚠️ del capítulo 15 (línea 50): está en la ficha de la propia a6700.
- Memorias: 3 por modo de toma en la cámara y 4 (M1–M4) en la tarjeta; se registran abertura y tiempo de exposición; se recuperan con el dial en 1/2/3 — [0413](https://helpguide.sony.net/ilc/2320/v1/es/contents/0413_setting_memory.html), [0302](https://helpguide.sony.net/ilc/2320/v1/es/contents/0302_memory_recall.html).
- Limpieza del sensor: `Ajustes → [Opción ajustes] → [Limpieza del sensor] → [Intro]`, batería al 51 % o más, soplador con la cámara un poco hacia abajo, sin espray, sin pasar de la montura, sin soplar fuerte, apagar y montar, y servicio técnico si sigue — [0601_cleaning_mode](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601_cleaning_mode.html). La sección nueva del capítulo 10 es fiel a la Guía.
- SteadyShot: en foto `Activar` / `Desactivar`; en película `Activo` / `Estándar` / `Desactivar`; con un objetivo con conmutador, solo manda el conmutador — [foto](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_still_image_steadyshot.html), [película](https://helpguide.sony.net/ilc/2320/v1/es/contents/0412B_movie_steadyshot.html).
- Fn: 12 funciones para foto y 12 para vídeo; mantener pulsado el icono abre `Ajustes del menú Fn`; dial frontal cambia el valor y el trasero afina — [0413](https://helpguide.sony.net/ilc/2320/v1/es/contents/0413_using_function_menu.html).
- Bloqueo: mantener Fn hasta «Bloqueado.»; MENU + Fn 5 s bloquea todo menos el disparador — [221h](https://helpguide.sony.net/ilc/2320/v1/es/contents/221h_dial_wheel_lock.html).
- Doble toque en MF abre la lupa: la ficha lo liga a `Enfoque táctil`, pero al pasar a `Enfoque man.` la cámara cambia sola `Seguimient. táct.` a `Enfoque táctil`, así que la receta del repo funciona — [0405_focus_magni](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405_focus_magni.html), [0601P](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601P_touch_tracking.html).
- BULB no se puede poner con `Captura contin.` — [0302C_bulb](https://helpguide.sony.net/ilc/2320/v1/es/contents/0302C_bulb.html).

**Imprecisos**

| Clase | Archivo y línea | Lo que dice el repo | Lo que dice la Guía | Corrección |
|---|---|---|---|---|
| IMPRECISO | `02-menus-y-primer-dia.md` 273; `17-verificacion-in-situ.md` 128 | «Gira la rueda de control para ampliar» | Primero se pulsa el botón Aumentar (AF-ON); la rueda solo ajusta la escala — [0501C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0501C_playback_zoom.html) | «Pulsa AF-ON; la rueda cambia el aumento» (como ya dice el capítulo 3) |
| IMPRECISO | `04-configuracion-basica.md` 205; `13-ajustes-a6700.md` 126 y 158 | Apagar o encender SteadyShot «en el cuerpo y también el OSS» con el 70-350 | Con conmutador en el objetivo «no se pueden cambiar los ajustes utilizando la cámara» — [0414](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_still_image_steadyshot.html) | Con el 70-350, solo el interruptor OSS |
| IMPRECISO | `16-chuleta.md` 48; `13-ajustes-a6700.md` 127 | Puntual «vinculada» como recurso con MR1 (área Zona) | Con `Ancho`, `Zona` o `Fijo al centro` la medición puntual «se bloquea en el centro»; el vínculo solo va con `Punto` y `Punto expandido` — [0406L](https://helpguide.sony.net/ilc/2320/v1/es/contents/0406L_spotmetering_link_focus_point.html) | Avisar: el vínculo exige área Punto |

**Sin fuente en la Guía**

| Archivo y línea | Afirmación | Estado |
|---|---|---|
| `conceptos/04-balance-de-blancos.md` 27-31; `16-chuleta.md` 33; `retoques/15-disparar-mejores-jpeg.md` 55 | Luz diurna = 5200 K, Nublado = 6000 K, Sombra = 7000 K | SIN FUENTE: la ficha de `Balance blanco` no da ningún Kelvin para los preajustes — [0410C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html) |
| `04-configuracion-basica.md` 43; `13` 77; `14` 151 | `RR ISO Alta` «solo afecta al JPEG» | SIN FUENTE: ni la ficha en español ni la inglesa lo dicen — [ES](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414C_high_iso_nr.html), [EN](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414C_high_iso_nr.html) |
| `04-configuracion-basica.md` 54-55, 125, 129 | Las memorias guardan el formato de archivo y el balance de blancos | SIN FUENTE: la Guía solo nombra abertura y tiempo de exposición y remite a la lista que muestra la cámara — [0413](https://helpguide.sony.net/ilc/2320/v1/es/contents/0413_setting_memory.html) |
| `03-diales-y-botones.md` 145-147 | Las memorias no guardan la asignación de botones | SIN FUENTE (misma ficha) |
| `02-menus-y-primer-dia.md` 234 y 255 | La cuadrícula viene desactivada y la revisión automática activada de fábrica | SIN FUENTE: las fichas no indican el valor predeterminado — [cuadrícula](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414B_grid_line.html), [revisión](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_auto_review.html) |
| `03-diales-y-botones.md` 39 y 47 | AF-ON trae `AF activado` y el botón del objetivo `Retención enfoque` de fábrica | SIN FUENTE explícita: la Guía describe la función, no el valor de fábrica — [AF-ON](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_using_AF_ON_button.html) |
| `03-diales-y-botones.md` 119-120 | Las opciones `Velocidad obturador` y `Abertura` en la pantalla de diales de `Ajuste t. pers./dial` | Los nombres existen como funciones de dial en «Mi dial»; la ficha de `Ajuste t. pers./dial` no enumera las opciones — [0413P](https://helpguide.sony.net/ilc/2320/v1/es/contents/0413P_mydial.html) |
| `03-diales-y-botones.md` 80-81, 122-123 | Tras el intercambio, en A y S los dos diales siguen moviendo lo mismo | SIN FUENTE: la Guía solo describe el comportamiento de fábrica |
| `14-menu-completo.md` 382 | La a6700 no tiene GPS | Coherente con [información de ubicación desde el smartphone](https://helpguide.sony.net/ilc/2320/v1/es/contents/202h_smartphone_location_info.html), pero las especificaciones no lo niegan de forma expresa |

### Inferences
- El repo ya es prudente con C1 y C3 de fábrica («varía»): la Guía tampoco dice qué traen («funciones recomendadas … de forma predeterminada»).
- Los 5200/6000/7000 K son valores de uso común en fotografía, no un dato de Sony para esta cámara; conviene presentarlos como aproximados o medirlos con un RAW.

### Gaps
- Qué guarda exactamente una memoria (balance, formato, botonera): solo se resuelve mirando la lista que muestra la cámara al registrar.
- No se consultaron las páginas de soporte de Sony (notas del firmware 2.00) ni otra fuente para los Kelvin; no se buscó fuera de la Guía.

## 3. ¿Se pueden confirmar las 11 subopciones marcadas con ❓ en el capítulo 15?

### Takeaway
Las 11 quedan confirmadas con el texto exacto en fichas de la a6700; ninguna necesita corrección.

### Cited Findings
- `Tem.col./filtro` — [Balance blanco](https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html)
- `Cuadr. regl. terc.` — [Tipo lín. cuadríc.](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_grid_line_type.html)
- `C. sin pérd.` — [Tipo archivo RAW](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404I_raw_file_type.html)
- `Compens. variación` (solo en vídeo) — [Compens. objetiv.](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414M_lens_comp.html)
- `Punto: S` / `Punto: M` / `Punto: L` — [Área de enfoque](https://helpguide.sony.net/ilc/2320/v1/es/contents/0405C_autofocus_area.html)
- `Conmut. dest. recon.` — [Aj. conm. dest rec](https://helpguide.sony.net/ilc/2320/v1/es/contents/211h_recognition_target_switch.html)
- `Botón personaliz. 1` / `Botón personaliz. 3` — [Ajuste t. pers./dial](https://helpguide.sony.net/ilc/2320/v1/es/contents/0413M_custom_key.html)
- `Solo pant. táctil` — [Pantall./almoh. táctil](https://helpguide.sony.net/ilc/2320/v1/es/contents/0601M_touch_panel_pad.html)
- `Mostrar toda info.` y `Monitor desactiv.` — [Aj. DISP (vis. pant.)](https://helpguide.sony.net/ilc/2320/v1/es/contents/0403B_disp_set.html)
- «Separe el modo M y los otros modos.» — [Ajuste t. pers./dial](https://helpguide.sony.net/ilc/2320/v1/es/contents/0413M_custom_key.html)

### Inferences
- El capítulo 15 puede pasar las 11 casillas a ✅ y quitar los dos ⚠️ de las líneas 49 y 50 (`Número archivo` / `Nombre carpeta` y el valor por defecto de `Tipo obturad. interv.`), ambos confirmados en fichas de la a6700.
- Los recuentos del capítulo 15 (54 grupos, 260 elementos, referencia 5-051-980-47(1)) coinciden con lo descargado hoy.

### Gaps
- El recuento «79 rutas, 176 apariciones» del capítulo 15 no se reprodujo: el script de hoy encontró 54 rutas distintas en los capítulos en alcance; la diferencia puede venir de capítulos fuera de alcance (5 a 11).

## 4. ¿Hay contradicciones internas entre capítulos?

### Takeaway
No hay ningún ajuste con dos valores opuestos, pero sí seis incoherencias de nombre o de gesto entre capítulos.

### Cited Findings
Las fuentes aquí son los propios archivos del repo; la columna «Guía» indica cuál de las dos versiones respalda Sony.

| # | Capítulos | Incoherencia | Guía |
|---|---|---|---|
| 1 | `13` 75 «Comprimido sin pérdida» · `14` 36 `C. sin pérd.` | Mismo valor, dos nombres | `C. sin pérd.` — [0404I](https://helpguide.sony.net/ilc/2320/v1/es/contents/0404I_raw_file_type.html) |
| 2 | `13` 88 «Regla de tres» · `14` 39 y 226 `Cuadr. regl. terc.` | Ídem | `Cuadr. regl. terc.` — [201h](https://helpguide.sony.net/ilc/2320/v1/es/contents/201h_grid_line_type.html) |
| 3 | `04` 48 `Ajuste SteadyShot` · `14` 211 `Adaptac. SteadyS.` | Ídem | `Adaptac. SteadyS.` — [0414F](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414F_steadyshot_setting.html) |
| 4 | `02` 273 y `17` 128 (girar la rueda amplía) · `03` 91 y 244 (AF-ON amplía) | Dos gestos distintos para ampliar | AF-ON — [0501C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0501C_playback_zoom.html) |
| 5 | `03` 208-209 y `14` 210 (manda el OSS del objetivo) · `04` 205 y `13` 158 (apagar cuerpo y objetivo) | SteadyShot con el 70-350 | Solo el conmutador — [0414](https://helpguide.sony.net/ilc/2320/v1/es/contents/0414_still_image_steadyshot.html) |
| 6 | `04` 125 y `conceptos/04` «Luz de día» · `13` 128 y `14` 270 `Luz diurna` | Nombre del preajuste | `Luz diurna` — [0410C](https://helpguide.sony.net/ilc/2320/v1/es/contents/0410C_white_balance.html) |

Otras diferencias menores entre capítulos, sin efecto en la cámara: `02` 185 mete `Formatear` en Mi Menú y `14` 507-509 mete `Ver info soporte` en su lugar; `04` 43 dice «Baja» y `13` 77 «Bajo»; `02` 98 habla de «formateo de firmware» en la pestaña Ajustes, expresión que no corresponde a ningún elemento (el elemento es `Versión`).

### Inferences
- Todas las incoherencias se resuelven adoptando el texto del capítulo 14, que es el que coincide con la Guía en los seis casos.

### Gaps
- Solo se cruzaron los capítulos en alcance; no se comprobó si los capítulos 5 a 11 (salvo la sección de polvo del 10) repiten estos nombres largos.
