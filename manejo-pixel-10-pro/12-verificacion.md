<!-- nav -->
[← Anterior](11-todos-los-ajustes.md) · [Índice](README.md) · [Siguiente →](13-chuleta.md)
<!-- /nav -->

*Parte IV · Referencia*

# 12. Verificación: qué está comprobado y qué no

> ✅ **Referencia** · Da por sabido: nada · Te desbloquea: saber de dónde sale cada dato de esta guía y cuáles tienes que mirar tú en el móvil.

Esta guía se escribió el 22 de noviembre de 2026 leyendo la documentación de
Google en español. **Nadie ha probado nada en tu teléfono:** los nombres y
las rutas son los de la ayuda oficial, y los consejos de uso son síntesis de
la guía. Las notas de lectura están en
[`notas-de-investigacion/pixel-10-pro/`](../notas-de-investigacion/pixel-10-pro/ayuda-de-google.md).

## Fuentes leídas

| Página de Google | Qué se sacó |
|---|---|
| [Especificaciones técnicas del hardware de los teléfonos Pixel](https://support.google.com/pixelphone/answer/7158570?hl=es) | La ficha del capítulo 1 y la lista de funciones de cámara |
| [Hacer fotos de alta calidad](https://support.google.com/pixelcamera/answer/14106982?hl=es) | 50 MP, `Selección de lente`, `Zoom Pro`, `Retrato`, `Movimiento`, `Inclúyeme`, `Panorámica`, `Enfoque macro`, documentos, enfoque y bloqueo |
| [Hacer fotos con poca luz o de noche](https://support.google.com/pixelcamera/answer/9708795?hl=es) | `Visión nocturna`, `Astrofotografía`, `Enfoque` → `Lejos`, `Brillo` y `Sombras` |
| [Cambiar los ajustes de la aplicación Cámara](https://support.google.com/pixelcamera/answer/2838995?hl=es) | Las rutas del capítulo 11 |
| [Mejor toma](https://support.google.com/pixelcamera/answer/9937175?hl=es) | `Mejor toma`, `Fotos con movimiento`, `Mejor versión automática`, `Caras frecuentes` |
| [Usar Asistente de cámara](https://support.google.com/pixelcamera/answer/17367411?hl=es) | Todo el apartado del Asistente |
| [Empezar a hacer fotos](https://support.google.com/pixelcamera/answer/2840311?hl=es) | Disparo por voz y zoom por gestos |

No se leyó la página de [Credenciales de Contenido](https://support.google.com/pixelcamera/answer/16507662?hl=es),
que solo se enlaza.

## Segunda comprobación (22 de noviembre de 2026)

Una vez escrita la guía, se volvieron a descargar las ocho páginas de Google y se contrastó el texto de forma automática:

- Los **120 nombres** de modos, ajustes y rutas que van en `código` están en esas páginas, incluidos los 38 componentes de las rutas de menú, uno a uno.
- La **ficha** del capítulo 1 coincide cifra a cifra con las especificaciones del Pixel 10 Pro (cámaras, pantalla, batería, peso, IP68, USB-C 3.2, memoria).
- Las **focales equivalentes** salen del ángulo de visión con la diagonal de 43,3 mm: 82° → 24,9 mm, 123° → 11,7 mm y 22° → 111 mm.
- Los **umbrales**: `Estabilizar` desde 15 aumentos, dos imágenes por encima de 30 aumentos (una con IA generativa y otra sin ella), `Zoom Pro` hasta 100 aumentos, `Astrofotografía` solo desde 1x, entre 45 y 90 minutos tras la puesta de sol, temporizador de 5 segundos y `Lejos` a más de 4 metros.

No apareció ninguna discrepancia. Sigue sin probarse nada en el teléfono.

## Comprobado en la documentación

- La ficha de las tres cámaras, la frontal, la pantalla, la batería, el peso,
  el IP68 y el USB-C 3.2.
- Los nombres en español de modos y ajustes que aparecen en `código`.
- Las rutas de menú de los capítulos 2 y 11.
- `Astrofotografía` solo con zoom de 1x o superior; la espera de 45 a 90
  minutos tras la puesta de sol; los 5 segundos del modo manual; el enfoque
  `Lejos` a más de 4 metros.
- `Zoom Pro`: hasta 100 aumentos en el Pixel 10 Pro, dos imágenes por encima
  de 30 aumentos, `Estabilizar` desde 15.
- `50 MP` también en `Retrato` en el Pixel 10 Pro.
- El Asistente de cámara: desactivado de fábrica, necesita Internet, solo
  cámara trasera y tres modos.
- `Mejor versión automática`: solo Pixel 10 y posteriores.

## Donde las fuentes de Google no coinciden

| Dato | Una fuente dice | Otra dice | La guía |
|---|---|---|---|
| Controles Pro en el Pixel 10 Pro | La ficha técnica los lista | La ayuda solo nombra Pixel 8 Pro, 9 Pro y 9 Pro XL | Los da por presentes y pide confirmarlo |
| `Barrido de movimiento` y `Larga exposición` | La ficha técnica los lista | La tabla de modelos de la ayuda acaba en el Pixel 9 | Igual |
| Sensor del ultra gran angular y del tele | 1/2,55" en la ayuda | 1/2,51" en un resumen de la tienda, no leído directamente | 1/2,55" |
| Nombre del icono de ajustes | `Ajustes` | `Ajustes de Foto` en dos pasos | `Ajustes` |

## Calculado o deducido por la guía

- **Las focales equivalentes** (unos 12, 25 y 111 mm): calculadas a partir
  del ángulo de visión, suponiendo que es el diagonal. Google no las publica.
- **Qué es recorte en 2x y 10x:** interpretación de «calidad óptica».
- **El límite útil del zoom**, las recetas, las tablas de «si sale mal» y el
  reparto con la a6700: criterio de la guía.
- **Los tres escalones** del capítulo 10: clasificación propia.

## Sin confirmar: para mirar en tu móvil

Están en [PENDIENTES](../PENDIENTES.md), sección del Pixel:

1. Que existen los controles Pro y qué deslizadores tienen (¿hay balance de
   blancos?), con sus rangos.
2. Las etiquetas de los botones de zoom tal como salen en pantalla.
3. Cuánto dura una foto de `Astrofotografía`.
4. La distancia mínima a la que salta el `Enfoque macro`.
5. Teclas de volumen, doble pulsación del botón de encendido, temporizador.
6. Si `Movimiento` ofrece los dos efectos.
7. El formato de archivo (JPEG, HEIF, Ultra HDR) y si Luminar abre el DNG.
8. La versión de la aplicación Cámara y de Android con que lo mires.

## Cómo mantenerla

La aplicación Cámara se actualiza sola desde Google Play y Google reescribe
su ayuda sin avisar. Cuando algo no coincida:

1. Manda la pantalla (una captura vale).
2. Se corrige el capítulo afectado y esta página.
3. Se apunta la fecha de la relectura junto a la fuente.

<!-- nav -->
[← Anterior](11-todos-los-ajustes.md) · [Índice](README.md) · [Siguiente →](13-chuleta.md)
<!-- /nav -->
