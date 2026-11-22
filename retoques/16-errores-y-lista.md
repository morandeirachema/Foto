<!-- nav -->
[← Anterior](15-disparar-mejores-jpeg.md) · [Índice](README.md) · [Siguiente →](17-atajos.md)
<!-- /nav -->

*Parte V · Referencia*

# 16. Errores típicos y lista de comprobación

## 16.1. Los errores más frecuentes

| Error | Cómo se reconoce | Solución en Luminar |
|---|---|---|
| **Exceso de saturación** | Colores "fosforito", pieles naranjas | Vibrance en vez de Saturation; HSL a la baja |
| **Exceso de contraste local** | Halos, aspecto HDR sucio | Bajar Structure AI y Large Details; máscara para el cielo |
| **Sombras abiertas de más** | Foto gris y plana, ruido | Menos Shadows; Blacks abajo |
| **Reducción de ruido excesiva** | Pelo, piel o estrellas de plástico | Bajar Luminosity Denoise; Details con cuidado |
| **Enfocar el ruido** | Grano áspero, estrellas falsas | Primero el ruido, luego la nitidez; Details Masking alto |
| **Bandas en el cielo** | Escalones en el degradado | Ajustes más suaves; Film Grain ligero |
| **Bordes de máscara visibles** | Línea alrededor del sujeto | Feather, Shift Edge; revisar con `/` |
| **Color poco creíble** | Atardecer neutro, noche naranja | Recordar cómo era la luz real |
| **Pantalla demasiado brillante** | Las fotos se ven oscuras en otras pantallas | Brillo de pantalla moderado |
| **Viñeteado evidente** | Esquinas negras "de filtro" | Vignette suave |
| **Dehaze fuerte en toda la foto** | Colores pesados, sin profundidad | Dehaze más bajo o con máscara |
| **Fotos de una serie que no casan** | Una más saturada u oscura que las demás | Sync Adjustments y revisión conjunta |
| **Editar cansado** | Al día siguiente todo parece exagerado | Descansar y bajar lo que sobre |

## 16.2. Lista de comprobación

```
PREPARAR
[ ] Selección hecha (P / X / estrellas) y copia de los originales
[ ] 30 s de análisis: ¿qué es el sujeto? ¿qué distrae? ¿cómo era la luz?
[ ] Pantalla con brillo moderado, sin True Tone ni Night Shift

CALIDAD
[ ] Histograma por canales si domina un color (dunas, focos, atardecer)
[ ] Ruido: Noiseless AI (vigilar pelo / estrellas al 100 %)
[ ] Movimiento: Supersharp AI, Motion Blur, Low (solo si hace falta)

GLOBAL
[ ] Recorte y horizonte (C)
[ ] Optics si hay distorsión o esquinas oscuras
[ ] Luz: Exposure, Highlights, Shadows, Whites, Blacks con J
[ ] Balance de blancos creíble (W)
[ ] Landscape → Dehaze suave si hay calima
[ ] Enhance AI moderado (Sky Enhancer solo de día)
[ ] Color: Vibrance y HSL, color por color
[ ] Structure AI / Details con moderación

LOCAL
[ ] Ojos: Dodge & Burn → Lighten, pincel pequeño, Strength baja
[ ] Sujeto: Dodge & Burn → Lighten (luz) · Structure AI + Object Select AI (textura)
[ ] Fondo: Color + máscara del sujeto invertida (⌘I) · Dodge & Burn → Darken
[ ] Cielo / suelo: Dodge & Burn · Mask AI (A) o Gradient (G) en otras herramientas
[ ] Noche: Vía Láctea con Supercontrast + Radial (R); horizonte con Gradient
[ ] Bordes de máscara revisados con /

ACABADO
[ ] Manchas de polvo en el cielo: Remove Dust Spots (repasar tras Dehaze)
[ ] Erase (solo distracciones pequeñas)
[ ] Vignette suave
[ ] Film Grain si hay bandas

REVISIÓN Y SALIDA
[ ] \ para comparar con el original
[ ] Revisión al 100 % (⌘1)
[ ] Descanso → segunda mirada → bajar lo que sobre
[ ] Comprobar en el móvil
[ ] Quitar el GPS si es fauna amenazada
[ ] Exportar (⇧⌘E) con el tamaño y la calidad de su uso
```

## 16.3. ¿Me he pasado? La prueba de dos minutos

Mientras editas, el ojo se acostumbra: cada cambio parece poco y siempre "falta un poco más". Por eso no sirve preguntarte si te gusta; sirven **pruebas que no dependen de tu ojo cansado**. Haz estas cinco, en orden, antes de exportar cualquier foto.

| # | Prueba | Cómo | Te has pasado si… |
|---|---|---|---|
| 1 | **Antes y después** | Mantén **`\`** (o usa el icono **Visibility**; si no lo ves, activa **View > Show Photo Actions Panel**) tres o cuatro veces | Al ver el original sientes **alivio**, o la editada parece otra foto y no la misma con mejor luz |
| 2 | **De lejos** | **`⌘0`** y aléjate un paso de la pantalla, o mira la miniatura en el catálogo | El ojo se va a un **color**, un **halo** o un **borde** antes que al sujeto |
| 3 | **De cerca** | **`⌘1`** en tres sitios: el borde del sujeto, una zona lisa (cielo) y el detalle fino (pelo, estrellas) | Hay una línea alrededor del sujeto, escalones o grano áspero en el cielo, pelo de alambre o de cera |
| 4 | **Los límites** | **`J`** y el histograma (sección 1.3) | Hay **más** zonas rojas o azules que antes de empezar: esas las has creado tú |
| 5 | **A la mitad** | En la herramienta que más has movido, baja el deslizador **a la mitad**. Repite con las dos siguientes | La foto **no empeora** con la mitad: quédate con la mitad |

**Y una sexta, la mejor: el día siguiente.** Vuelve a abrir la foto sin haber mirado otras antes. Lo que sobra se ve en dos segundos. Lo normal es bajar un 20–30 %.

### Qué mirar en cada parte de la foto

| Mira… | Te has pasado si… | Qué bajar |
|---|---|---|
| **El pelaje o la piel del animal** | Naranja o amarillo "de dibujos animados"; el pelo parece alambre, o cera | Saturation o Vibrance; Structure AI y Details; Luminosity Denoise |
| **Los ojos** | Son lo más brillante de la foto, con el blanco puro o aspecto de cristal | **Strength** de Dodge & Burn, o borra parte de lo pintado |
| **El sujeto contra el fondo** | Parece una **pegatina**: borde claro u oscuro, o el fondo mucho más oscuro o borroso de lo creíble | La diferencia entre la máscara y su inversa; sube **Feather** |
| **El cielo de día** | Azul marino o turquesa, más oscuro que el suelo; escalones en el degradado; una franja clara sobre el horizonte o la duna | Luminancia y saturación del azul; Dehaze; la fuerza de la máscara del cielo |
| **La arena y las dunas** | Naranja fosforito y sin ondas: el color ha tapado el relieve | Saturación del naranja y del rojo |
| **La hierba y los árboles** | Verde neón o amarillo limón | Saturación del verde y del amarillo en HSL |
| **Las sombras** | Grises y lechosas, con manchas de color; toda la foto tiene aspecto "HDR" | Shadows; Accent AI; Structure AI |
| **Los blancos** (nubes, pelaje claro, sal) | Se han vuelto **grises** | Highlights menos abajo; Whites un poco arriba |
| **El cielo nocturno** | Azul saturado; estrellas con un anillo oscuro o claro; el fondo tiene "gusanos" o manchas; la Vía Láctea parece pintada | Temperature; Dehaze y Structure AI del núcleo; Noiseless AI |
| **El fuego y las luces** | La llama es gris; todo es de un único naranja | Highlights menos abajo; saturación del naranja |
| **Los bordes de la foto** | La viñeta se ve como un círculo oscuro | Vignette |
| **La foto junto a sus vecinas** | Destaca en la serie por color o contraste | Iguala con Sync Adjustments y revisa |

### Tres reglas para no llegar a pasarte

1. **Entre dos valores, el menor.** En un JPEG, cada ajuste fuerte saca ruido, bandas o halos.
2. **Un solo protagonista por foto.** Si has subido el color, deja tranquilo el contraste; si has trabajado el sujeto, no toques también el cielo.
3. **Enséñala en el móvil a alguien.** Si lo primero que dice es "qué colores" y no "qué leona", el retoque se nota más que la foto.

Para lo que cada herramienta hace cuando te pasas, mira la columna "te has pasado si…" de [las herramientas, una a una](03-herramientas-una-a-una.md).

<!-- nav -->
[← Anterior](15-disparar-mejores-jpeg.md) · [Índice](README.md) · [Siguiente →](17-atajos.md)
<!-- /nav -->
