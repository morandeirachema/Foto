# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

**Foto** (https://github.com/morandeirachema/Foto, formerly `Luminar`) is a Spanish-language photography guide in three sections. It is all Markdown plus generated PDFs; there is no application code.

| Folder | Section | Origin |
|---|---|---|
| `conceptos/` | Concepts: technical model, histogram, white balance, composition, "la mirada" | Copied from `a6700-namibia` (Nov 2026) |
| `manejo-a6700/` | Handling the Sony a6700 in 17 chapters: getting started, scenario recipes, gear and lenses, settings and menu reference, field sheets. Native additions: `05-enfocar-el-11mm.md`, `11-viltrox-25mm.md`, `15-verificacion-de-menus.md` | Mostly copied from `a6700-namibia` (Nov 2026) |
| `retoques/` | Editing **in Luminar only** (18 chapters + intro), verified against Skylum's docs | Native to this repo |
| `pdf/` | Generated PDFs, their CSS and generator scripts | — |
| `sources/` | Source material kept as-is: `Namibia-a6700-edicion-completa.pdf` (264 pp., a6700-namibia at `a5252c3` + Annex A menu audit) | Added by the owner |

The owner's explicit scope decisions:
- **Retoques is Luminar-only.** No darktable or Lightroom content, and no "equivalences" tables.
- **No video content.** The video guides were deliberately left out, and the video sections of the copied files were removed. Mentions of the camera's Foto/Vídeo/S&Q selector, the MOVIE button and video-only menu lines stay, because they are needed to operate the camera.
- From `a6700-namibia`, only concepts, composition and the camera chapters were brought over: no trip planning, no fauna or landscape guides, no Pixel, no logistics. Links in the copied files to guides that were not copied point to absolute URLs at `https://github.com/morandeirachema/a6700-namibia/blob/main/...`. Keep it that way, and don't copy those guides in unless asked. Links that used to go to `campo/edicion-basica.md` now point to `retoques/README.md`.
- **The Namibia trip photos (30 Oct–15 Nov 2026) are JPEG only**, because the camera was misconfigured. That's why `retoques/` stays JPEG-first, and the sample photos for `retoques/09-recetas.md` will be JPEGs. The camera guides still prescribe RAW, and the RAW check (`.ARW` test shot, re-check after loading MR1/MR2) is in `manejo-a6700/04-configuracion-basica.md`, `17-verificacion-in-situ.md` and `retoques/14-disparar-mejores-jpeg.md`. A Luminar RAW chapter is future work: first verify Skylum's support for the a6700's lossless compressed RAW.
- **Owner's gear:** a6700 body, Sony E 11 mm F1.8 and **Viltrox AF 25 mm F1.7 Air** (guide: `manejo-a6700/11-viltrox-25mm.md`) are the owner's. The **Sony E 70-350 G OSS is borrowed**: never present it as owned. Viltrox facts come from Digital Camera World's review and retailer spec sheets: 170 g, 52 mm filter, 12/10 elements, 9 blades, f/1.7–16, 0.3 m minimum focus, STM, focus-by-wire, **no AF/MF switch** (MF is set via `Modo de enfoque` or an `Alter. select. AF/MF` button), USB-C for firmware, treated as not sealed.
- `a6700-namibia` remains its own repo and is not modified from here.
- **`sources/Namibia-a6700-edicion-completa.pdf` is how the owner's camera is actually configured.** Its content equals a6700-namibia at `a5252c3`, the version copied here. Don't change camera values in `manejo-a6700/` unless the owner asks or the PDF says otherwise. Its Annex A (the menu audit against Sony's Guía de ayuda, edition 5-051-980-47(1), firmware 2.00) lives as `manejo-a6700/15-verificacion-de-menus.md`, with all five findings applied. The 11 sub-option names listed there as ❓ are still unconfirmed: don't present them as verified until the owner checks them on the camera with C3. If the camera screen ever disagrees with the repo, the screen wins.

`RUTA.md` (root) is the learning path from zero to advanced, the owner's stated goal (18 Nov 2026). It orders the chapters of all three sections into stages 0–4, each with practice and a "Lo dominas cuando…" self-check, plus a concept map (concept → 🟢/🔵/🔴 chapter). Update it whenever chapters are added, renamed or renumbered; `tools/comprobar.py` validates its links and anchors.

`PENDIENTES.md` (root) is the owner's checklist of things only they can verify. When the owner reports a result, update the affected guide and tick the item; when you add an unverifiable claim, add it there.

## Structure (the same in all three sections)

`conceptos/`, `manejo-a6700/` and `retoques/` share one structure:
- `00-introduccion.md`, then chapters `NN-slug.md`. **Chapter number = file number**: the H1 is `# N. Title`, and the generator picks the chapters up with the glob `NN-*.md`.
- Each chapter starts with its part label (`*Parte II · …*`) before the H1. Conceptos and manejo chapters keep their level line (`> 🟢/🔵/🔴 **Nivel** · …`) right under the H1.
- `README.md` is the section index, a table of parts and chapters. Keep it, `00-introduccion.md` and the root README's tables and counts in sync.
- The `<!-- nav -->` blocks and `guia-completa.md` are **generated**: never edit them by hand.
- In-text references: in retoques, "sección 4.3" means chapter 4 of retoques. In conceptos and manejo, "capítulo N" means chapter N of **manejo-a6700**. Manejo was renumbered on 18 Nov 2026 (old 0, 0.5, 0.7, 1, 2, 3, 4, 5 → 1, 2, 3, 4, 6, 8, 9, 10). The mapping table is in `manejo-a6700/00-introduccion.md`, because the `sources/` PDF and a6700-namibia still use the old numbers.
- When adding or renumbering a chapter, update the H1 numbers, the in-text "capítulo/sección N" references, the section's `00-introduccion.md` and `README.md`, and the root `README.md`.

## Commands

```sh
python3 tools/comprobar.py       # repo check: links + anchors, unclosed fences, NN/H1 numbering, nav blocks, chuleta = 1 page. Run before every commit
./pdf/generar.sh                 # everything: nav blocks, the 3 guia-completa.md files and the 6 PDFs
./pdf/generar.sh <name>          # chuleta | verificacion-in-situ | cuaderno-de-composicion | guia-conceptos | guia-manejo-a6700 | guia-retoques
./pdf/generar-guia.sh <carpeta> [--no-pdf]   # one section: nav + <carpeta>/guia-completa.md (+ pdf/guia-<carpeta>.pdf)
pdfinfo pdf/<name>.pdf           # check page count
```

Both scripts use pandoc and headless Google Chrome. Regenerate after editing a source and commit the results together. `manejo-a6700/16-chuleta.md` **must fit on one A4 page** (it uses `pdf/compacto.css`). The field-sheet PDFs strip the nav blocks. In the section PDFs, Mermaid diagrams become a short "see GitHub" note (there's no Mermaid renderer installed, and nothing should be installed without asking), and links to repo files become plain text. Styles: `pdf/guia.css` for sections, `pdf/estilo.css` (+ `compacto.css`) for sheets. To check the layout, render pages with `pdftoppm -png -r 50 -f N -l N`. Check relative links after moving files: a quick Python script over all `](...)` targets works.

## Retoques (Luminar) rules

- Every Luminar tool, slider, menu path, shortcut and limit must be verifiable in Skylum's docs (index: `https://support.skylum.com/llms.txt`; append `.md` to a page URL). Add the page to `retoques/19-fuentes.md`. Where the docs are silent (HSL channel list, export colour-space options, GPS removal on export, input formats of HDR Merge or Panorama, whether Luminar reads in-camera star ratings), say so instead of guessing.
- Slider values are the guide's own starting points, labelled as such. `retoques/09-recetas.md` stays **provisional** until it has been checked against the owner's sample photos.
- Corrections already made from the docs: Dehaze lives in **Landscape Tools → Landscape**; **Twilight Enhancer AI** exists; Sky Enhancer AI is not for night skies; Upscale goes up to 6×; Object Select AI is hover + click with Subtract; there are no adjustment layers; **adding the same tool twice with different masks is NOT documented** (Skylum's docs only say so in the layers context and don't explain how; the docs assistant confirmed it's undocumented). So the method is one mask per tool: Develop global, Dodge & Burn for local light, other tools with their own masks (`retoques/04-ajustes-locales.md`). Don't reintroduce "Develop (segunda instancia)" until the owner confirms it works in their version (PENDIENTES).
- Style: Spanish (Spain), addressed as *tú*; Luminar UI names in English and bold; values with a decimal comma and a true minus sign `−`; macOS shortcuts as **`⌘1`**.

## Conceptos and manejo-a6700 rules (inherited from a6700-namibia)

Editorial contract:
- **Nivel visible**: toda guía abre con `> 🟢/🔵/🔴 **Nivel** · Da por sabido: … · Te desbloquea: …`. Mantenerlo al crear o mover contenido.
- **Teoría**: el nivel 🔴 avanzado **sí** explica el modelo (`conceptos/04-por-que-funciona.md`), pero con una regla dura: cada concepto termina en una decisión concreta de campo, con los números del equipo real. Nunca fórmulas sueltas.
- **Audiencia**: novato que viene sobre todo del móvil — **a todos los niveles**. Nada de teoría: recetas con valores concretos, pasos numerados y tablas de "si la foto sale mal, toca esto". Toda guía (también las avanzadas) debe ser **autocontenida desde lo básico**: la base imprescindible va resumida dentro, y los enlaces a otros capítulos son para ampliar, nunca requisito para empezar.
- **Equipo**: siempre opciones **budget**, con precio orientativo y mención de segunda mano (mpb.com) cuando compense.
- **Enlaces externos**: toda referencia (apps, software, localizaciones, fabricantes) lleva su URL. No inventar URLs profundas; ante la duda, enlazar la página raíz del sitio.

Camera facts that were verified against Sony's Guía de ayuda. Do **not** "correct" these:
  - La a6700 **sí** permite compensación de exposición en M con ISO Auto (±5 EV) — al contrario que la Canon anterior; las recetas se apoyan en ello.
  - **Una sola ranura** SD (UHS-II): no hay copia automática en segunda tarjeta — el sistema de copias del repo gira alrededor del volcado nocturno.
  - **Tarjetas** (verificado en agosto de 2026): el búfer de la a6700 son ~1.000 JPEG, 59 RAW comprimido y **solo 23 RAW comprimido sin pérdida** (unos 2 s: en RAW sin pérdida la ráfaga baja a ~10 fps, según las especificaciones de Sony). Vaciarlo tras 30 RAW: 18–22 s con UHS-I V30, 8–9 s con UHS-II V60, 4–6 s con V90.
  - La caja de la a6700 **no trae cargador**: carga por USB-C (PD) en cámara; el repo recomienda cargador doble USB aparte.
  - **Nombres de menú verificados** (agosto de 2026, Guía de ayuda en español): las rutas se escriben `MENU → pestaña → [Grupo] → [Ajuste]` y los nombres van **abreviados como en pantalla**: `Calid. img/grab.`, `Obturad./silenc.`, `Modo de manejo`, `Estabiliz. de img`, `Rec. motivo en AF`, `Dest. reconocim.`, `Sens. Seguim. AF`, `Mem. ajustes cám`, `Visualizac. cebra` (nivel `100 IRE o +`), `RR exposic. larga`, `Personal. operac.`, `Rest/guard ajust`. La pestaña de disparo se llama **Toma**, no "Disparo". No "corregir" estos nombres a formas más largas. Añadidos en la auditoría de octubre de 2026, contra la misma Guía: el objetivo de aves de `Dest. reconocim.` es **`Ave`** (no "Pájaro"; también existe `Animal/ave`); la medición va en `Exposición/color → [Medición] → [Modo medición]` (Multi/Centro/Puntual) y su vínculo en `[Punto med. punt.] → Vínc. punto enf.`; la lupa es `Amplific. enfoque`; el horquillado, `Modo manejo` → `Variación expos.`; la ráfaga, `Captura contin.`; el temporizador, `Autodisp.(senc)`; el SteadyShot de foto es `Activar`/`Desactivar` y el de vídeo `Activo`/`Estándar`/`Desactivar`; la pestaña de reproducción es `Reproducc.` y el aumento inicial va en `[Aumento]`; `[Mostrar de Mi Menú]` vale `Activar`; el calor se gobierna en `Ajustes → [Opc. ajuste enrg.] → [Temp. APAGA auto]`. Segunda auditoría (25 de octubre de 2026, las 359 páginas de la Guía): el enfoque al pulgar es **`AF c/obturador`** (no "AF con disparador"); Bright Monitoring es **`Verificac. luminosa`**, solo existe como función de botón y se cancela con AF, con la lupa o al apagar (solo va en MF); el grupo del balance es `Balance blancos` (plural) y el ajuste `Balance blanco`; el peaking es `[Visualiz. resalte] → [Visualizac. resalte]`; la lupa está en `[Asistencia enfoq.]`; `Func. capt. interv.` vive en `Toma → [Modo de manejo]`; `Idioma` en `Ajustes → [Área/fecha]`; el objetivo de personas de `Dest. reconocim.` es `Humano`; existen `Guard./carg. ajustes`, `Bloqueo dial/rueda` (mantener Fn), `Rotación de Av/Tv` y `Ajustes de Mi dial` (en `[Personalizar dial]`), y **no** existen `Bloq. piezas operac.` ni `Configur. Av/Tv`. **Mandos**: en M, de fábrica, el **dial frontal mueve la abertura** y el trasero la velocidad — el repo los intercambia (`Ajuste t. pers./dial`) porque todas las recetas dicen "obturación = rueda delantera"; la rueda trae arriba DISP, abajo `Compensar exp.`, izquierda `Modo manejo`, derecha `ISO`; C2 trae `Área de enfoque`; **C1 está en la esquina trasera derecha**, junto al enganche de la correa; la **Guía en la cámara** es pulsar C3 (papelera) sobre una línea del menú o del Fn, sin asignar nada; la botonera del viaje es C1 = `Verificac. luminosa` y C3 = `Amplific. enfoque` (`manejo-a6700/03-diales-y-botones.md`). `Liberar sin tarj. mem.` viene en Habilitar: el repo manda Inhabilitar.
  - **Pantalla y revisión** (verificado en agosto de 2026): la **cuadrícula** (`Toma → [Visualizac. toma] → [Vis. lín. cuadrícul.]`, tipo regla de tres) va **activada**; la **`Rev.automática`** (`Ajustes → [Opción de visual.]`) va **desactivada**; el ciclo de DISP se recorta en `Ajustes → [Personal. operac.] → [Aj. DISP (vis. pant.)]` a tres vistas (toda info., histograma, nivel); y las 3 fotos del día se marcan con **`Valoración`** (`Reproducc. → [Selección/nota]`).
  - El aviso de quemados en vivo es el **Zebra 100+**. En reproducción, la vista de histograma (DISP) **sí hace parpadear** las zonas sobrexpuestas y subexpuestas ("advertencia de sobrexposición/subexposición", página del botón DISP; corregido en octubre de 2026 — antes el repo decía lo contrario).
  - El **11mm F1.8** tiene autofoco y contactos: interruptor **AF/MF** y **botón de retención de foco** en el propio objetivo, apertura desde la rueda de la cámara, sin estabilizador óptico (lo pone el IBIS) y rosca de **55 mm**. Para astro se enfoca a mano igualmente (lupa + peaking), pero no hay anillo de diafragma ni F--.
  - El **70-350 G OSS** lleva interruptor **AF/MF**, interruptor **OSS (solo ON/OFF: no hay modo de barrido)**, **bloqueo de zoom** (solo a 70 mm), **botón de retención de foco** y rosca de **67 mm**. No tiene limitador de enfoque, ni puerto USB, ni macro: su máxima ampliación es 0,23x. La apertura máxima escalona f/4.5 (70–81 mm) · f/5 (82–113) · f/5.6 (114–199) · f/6.3 (200–350) — en la charca nocturna, quedarse por debajo de 200 mm es luz gratis.
  - El obturador **electrónico** es totalmente silencioso (el arma de las charcas), pero con focos LED parpadeantes puede sacar **franjas**: el plan B documentado es el obturador mecánico.
  - El intervalómetro va **integrado** y se llama `Func. capt. interv.` en el menú español (*Interval Shoot Func.* en inglés): no recomendar intervalómetros de cable.
  - Focales siempre con su equivalencia APS-C (1.5x): 11 mm = 16,5 mm eq; 70–350 mm = 105–525 mm eq.
