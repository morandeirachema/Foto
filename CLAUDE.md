# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

There is no application code here. The repository holds a Spanish-language guide to editing JPEG photos (safari, landscape, night) in **Luminar for Desktop 1.29.x** (Luminar Neo), on macOS. **The guide covers Luminar only.** The owner explicitly asked for no darktable or Lightroom content, so don't add equivalences to other editors.

## Source vs generated files

- `docs/NN-*.md`: **the source.** One file per chapter (`00-introduccion.md` … `18-fuentes.md`), plus `docs/README.md`, the hand-written chapter index.
- `guia-luminar-jpeg-safari-paisaje-noche.md` and `.pdf`: **generated** by `build.sh`. Never edit them by hand.
- The `<!-- nav -->` … `<!-- /nav -->` blocks at the top and bottom of each chapter are **rewritten by `build.sh`**. Don't edit them.

## Commands

```sh
./build.sh            # refresh chapter nav, rebuild single-file .md, render A4 PDF
./build.sh --no-pdf   # skip the PDF
pdfinfo guia-luminar-jpeg-safari-paisaje-noche.pdf   # sanity check (A4, page count)
```

The PDF is built with pandoc (`--from gfm`, styled by `pdf.css`) and then printed by headless Google Chrome (`CHROME` env var overrides the path). Run `./build.sh` after any change in `docs/` and commit the regenerated files with it. To check the layout, render pages with `pdftoppm -png -r 50 -f N -l N <pdf> <prefix>`. `pdf.css` relies on `p:has(+ h1)` to keep each chapter's "*Parte …*" label on the same page as its heading.

## Adding or renaming a chapter

Files are picked up by the glob `docs/[0-9][0-9]-*.md`, in order. Chapter number = file number, and in-text cross-references ("sección 4.3") rely on that. If you add, remove or renumber a chapter, update: the in-text "sección N" references, `docs/00-introduccion.md`, `docs/README.md` and the root `README.md` (contents list, "Empieza por aquí" table).

## Accuracy rules (the owner asked for "very precise, no fabrications")

- Every Luminar tool name, slider name, menu path, shortcut and technical limit must be verifiable in Skylum's official docs. The index is `https://support.skylum.com/llms.txt`; append `.md` to any page URL. Check the docs before adding or changing a claim, and add the page to `docs/18-fuentes.md`.
- If the docs don't say something (for example, the HSL channel list, the export color-space options, metadata/GPS removal on export, which input formats HDR Merge or Panorama accept), say so in the text rather than guessing.
- Slider values are the guide's own starting points, and the text says so. `docs/08-recetas.md` is marked **provisional** until it has been checked against the owner's sample photos. Keep that banner until then.
- Corrections already made from the docs: Dehaze lives in **Landscape Tools → Landscape**; **Twilight Enhancer AI** exists (Landscape Tools); Sky Enhancer AI is not for night skies; Upscale goes up to 6× (no fixed ×2/×4); Object Select AI is hover + click with **Subtract**; there are no "adjustment layers" (Add New Layer offers My Images, Flares, Light Leaks, Stardust Bokeh and Sparklers); tools can be added multiple times with their own masks ("instancias").

## Writing conventions

- Spanish (Spain), addressed to the reader as *tú*, plain and beginner-friendly. Luminar UI names stay **in English** and in bold, exactly as in the app (*Noiseless AI*, *Mask AI*, *Sync Adjustments*).
- Each step follows the pattern: **what to do in Luminar** (with values) → **why**.
- Values are ranges with a Spanish decimal comma and a true minus sign `−` (U+2212): `+15 a +40`, `−0,2/−0,4`.
- Shortcuts are macOS, in bold backticks: **`⌘1`**. Chapter 15 is the full list. Keep it, the checklist (14.2) and the in-text mentions consistent.
- Documentary ethics stance (chapter 12): correct the photo, don't change the scene. Content-generating tools (GenErase, GenSwap, GenExpand, Sky AI, Atmosphere AI, Twilight Enhancer's Dawn) are always flagged as such.
