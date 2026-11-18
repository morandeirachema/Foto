# 📸 Luminar · Guía de edición JPEG: safari, paisaje y noche

> Saca el máximo partido a tus JPEG de viaje con **Luminar**, y aprende conceptos que sirven en **cualquier editor**.

![Luminar 1.29.x](https://img.shields.io/badge/Luminar-1.29.x-6C5CE7)
![Idioma: español](https://img.shields.io/badge/idioma-español-E74C3C)
![Formato: Markdown + PDF](https://img.shields.io/badge/formato-Markdown%20%2B%20PDF-2D3436)
![Actualizada: nov 2026](https://img.shields.io/badge/actualizada-nov%202026-00B894)

Una guía práctica y en español para mejorar fotos **JPEG** de **safari (fauna)**, **paisaje** y **fotografía nocturna**. Cada paso explica **qué hacer** en Luminar, **por qué** se hace y **cómo se llama** el mismo ajuste en **Lightroom** y **darktable**. Si cambias de programa, solo tendrás que aprender dónde está cada botón.

## 📖 Leer la guía

| Formato | Archivo |
|---|---|
| 📝 Markdown (se lee directamente en GitHub) | [`guia-luminar-jpeg-safari-paisaje-noche.md`](guia-luminar-jpeg-safari-paisaje-noche.md) |
| 📄 PDF (A4, 16 páginas, listo para imprimir) | [`guia-luminar-jpeg-safari-paisaje-noche.pdf`](guia-luminar-jpeg-safari-paisaje-noche.pdf) |

## 🧭 Contenido

1. **Conceptos universales:** qué tiene de especial un JPEG, las cinco zonas de brillo, el histograma, el balance de blancos, el contraste global y local, el ruido y la nitidez, y el orden de trabajo.
2. **El flujo base en Luminar:** los 10 pasos que se repiten en cualquier foto.
3. **🦁 Safari:** contraluces, luz dura de mediodía, calima, recortes fuertes y cómo hacer que el animal sea el protagonista.
4. **🏜️ Paisaje:** equilibrar cielo y suelo, dar profundidad, dunas, atardeceres y cielos de tormenta.
5. **🌌 Noche:** Vía Láctea, contaminación lumínica, luces artificiales, fuego de campamento y luna.
6. **✅ Errores típicos** y una **lista de comprobación** para imprimir.
7. **🔁 Tabla de equivalencias** entre Luminar, Lightroom y darktable.

## ✨ Por qué esta guía

- **Pensada para JPEG**, no para RAW: ajustes suaves que no rompen la imagen (sin bandas, halos ni colores falsos).
- **Explica el porqué de cada ajuste**, así que también te sirve fuera de Luminar.
- **Valores orientativos** para cada ajuste, como punto de partida.
- **Ética documental:** cuándo *no* borrar elementos ni cambiar el cielo.
- **Basada en la documentación oficial** de Skylum y en el manual de darktable 5.6.

## 🛠️ Regenerar el PDF

El PDF se genera a partir del Markdown, que es la fuente. Tras editar la guía:

```sh
pandoc guia-luminar-jpeg-safari-paisaje-noche.md -s -o /tmp/guia.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --no-pdf-header-footer --print-to-pdf=guia-luminar-jpeg-safari-paisaje-noche.pdf /tmp/guia.html
```

---

<sub>Guía no oficial. Luminar es una marca de Skylum; Lightroom, de Adobe. Esta guía no tiene relación con ninguna de las dos empresas.</sub>
