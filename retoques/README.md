<div align="center">

# 🎨 Retoques con Luminar

### De un JPEG plano a la foto que recuerdas, paso a paso y desde cero

![Luminar for Desktop 1.29.x](https://img.shields.io/badge/Luminar-1.29.x-B4561C)
![19 capítulos](https://img.shields.io/badge/capítulos-19-1D1D1F)
![Pensada para JPEG](https://img.shields.io/badge/formato-JPEG-5F6368)
![Verificada con Skylum](https://img.shields.io/badge/herramientas-verificadas-2E7D32)

**[📖 Empezar](00-introduccion.md)** · **[🎯 Ajustes locales](04-ajustes-locales.md)** · **[📄 Guía completa](guia-completa.md)** · **[🖨️ PDF](../pdf/guia-retoques.pdf)** · **[✅ Lista de comprobación](15-errores-y-lista.md)**

</div>

---

Tus fotos de Namibia están en **JPEG**, y esta guía está escrita justo para eso. Explica **qué** hacer en Luminar, **cómo** hacerlo clic a clic y **por qué** funciona, sin dar nada por sabido. Cada herramienta, control y atajo está comprobado con la documentación oficial de Skylum; lo que la documentación no dice, la guía lo indica.

## 🔁 El método en un vistazo

```mermaid
flowchart LR
    subgraph G["Toda la foto"]
      A[Ruido<br/>Noiseless AI] --> B[Recorte<br/>Crop AI] --> C[Luz<br/>Develop] --> D[Color<br/>Balance · HSL] --> E[Textura<br/>Structure AI]
    end
    subgraph L["Por zonas"]
      F[Ojos y sombras<br/>Dodge & Burn] --> H[Sujeto y fondo<br/>máscaras]
    end
    E --> F
    H --> I[Acabado<br/>y exportar]
```

## 🧭 Empieza por aquí

| Si… | Lee |
|---|---|
| Nunca has editado una foto | [1. Conceptos básicos](01-conceptos-basicos.md) → [2. Luminar por dentro](02-luminar-por-dentro.md) → [3. El flujo base](03-flujo-base.md) |
| Quieres aclarar **los ojos**, abrir **una sombra** u oscurecer **el cielo** | [4. Ajustes locales](04-ajustes-locales.md) |
| Tienes una foto de un animal delante | [6. Safari](06-safari.md) |
| Tienes dunas, montaña o un atardecer | [7. Paisaje](07-paisaje.md) |
| Tienes estrellas, luna o fuego | [8. Noche](08-noche.md) |
| Tienes 500 fotos que editar | [10. Trabajar en serie](10-trabajar-en-serie.md) |
| Vas a imprimir o publicar | [12. Exportar](12-exportar.md) |

## 📚 Todos los capítulos

| Parte | Capítulo | Contenido |
|---|---|---|
| | [Introducción](00-introduccion.md) | Cómo está organizada y cómo leerla |
| **I · Fundamentos** | [1. Conceptos básicos](01-conceptos-basicos.md) | JPEG frente a RAW, zonas de brillo, histograma, balance de blancos, contraste, ruido, color |
| | [2. Luminar por dentro](02-luminar-por-dentro.md) | Catálogo, categorías de herramientas, copias virtuales, máscaras, capas |
| **II · El método** | [3. El flujo base: 10 pasos](03-flujo-base.md) | El esqueleto de cualquier edición |
| | [4. Ajustes locales](04-ajustes-locales.md) 🆕 | Aclarar u oscurecer solo una parte: ojos, sombras, cielo, sujeto y fondo. Qué, cómo y qué significa |
| | [5. Herramientas avanzadas](05-herramientas-avanzadas.md) | Curves, Supercontrast, Color Harmony, Dodge & Burn, Light Depth, Black & White, Landscape, Creative |
| **III · Por tipo de foto** | [6. Safari 🦁](06-safari.md) | Ruido, contraluz, luz dura, el animal como protagonista, casos concretos |
| | [7. Paisaje 🏜️](07-paisaje.md) | Cielo y suelo, profundidad, dunas, atardecer, montaña, agua, hora azul |
| | [8. Noche 🌌](08-noche.md) | Vía Láctea, contaminación lumínica, luces artificiales, fuego, luna |
| **IV · Más allá de una foto** | [9. Recetas completas](09-recetas.md) ⚠️ | Cinco casos de principio a fin (*provisional*) |
| | [10. Trabajar en serie](10-trabajar-en-serie.md) | Sync Adjustments, presets propios, coherencia |
| | [11. Varias fotos en una](11-varias-fotos.md) | HDR Merge, Panorama Stitching, Focus Stacking, Upscale, herramientas generativas |
| | [12. Exportar](12-exportar.md) | Formatos, tamaños por uso, impresión |
| | [13. Ética y ubicación](13-etica.md) | Qué es manipular, concursos, GPS y fauna amenazada |
| | [14. Disparar mejores JPEG](14-disparar-mejores-jpeg.md) | Ajustes de cámara para la próxima vez (y que sea RAW) |
| **V · Referencia** | [15. Errores y lista](15-errores-y-lista.md) | Errores típicos y lista de comprobación imprimible |
| | [16. Atajos de teclado](16-atajos.md) | Atajos de macOS verificados |
| | [17. Glosario](17-glosario.md) | Términos básicos |
| | [18. Preguntas frecuentes](18-preguntas-frecuentes.md) | Dudas habituales |
| | [19. Fuentes](19-fuentes.md) | Documentación oficial de Skylum consultada |

## ⌨️ Los diez atajos que más vas a usar

| | | | |
|---|---|---|---|
| **`J`** aviso de recorte | **`\`** ver el original | **`⌘1`** zoom 100 % | **`C`** recortar |
| **`W`** cuentagotas | **`A`** Mask AI | **`/`** ver la máscara | **`⌘I`** invertir la máscara |
| **`[`** **`]`** tamaño del pincel | **`⇧⌘E`** exportar | | |

---

Sección anterior: [🎛️ Manejo de la a6700](../manejo-a6700/README.md) · [🏠 Inicio](../README.md) · [✅ Pendientes](../PENDIENTES.md)
