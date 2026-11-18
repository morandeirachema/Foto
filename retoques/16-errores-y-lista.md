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
[ ] Remove Dust Spots / Erase (solo distracciones pequeñas)
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

<!-- nav -->
[← Anterior](15-disparar-mejores-jpeg.md) · [Índice](README.md) · [Siguiente →](17-atajos.md)
<!-- /nav -->
