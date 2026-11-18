# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

There is no code here. It holds a documentation project: a Spanish-language guide to editing JPEG photos (safari, landscape and night photography) in Luminar (version 1.29.x). Each step also gives the equivalent setting in Lightroom and darktable.

- `guia-luminar-jpeg-safari-paisaje-noche.md`: the **source**. Edit this one.
- `guia-luminar-jpeg-safari-paisaje-noche.pdf`: a **generated** A4 export of the Markdown, printed with headless Chrome (Skia/PDF). It is not the source of truth. Regenerate it after changing the Markdown, and never edit the PDF by hand.

## Regenerating the PDF

The PDF was printed from HTML with headless Chrome. One way to rebuild it with tools already on this machine (`pandoc` is installed):

```sh
pandoc guia-luminar-jpeg-safari-paisaje-noche.md -s -o /tmp/guia.html \
  --metadata title="Mejorar JPEG de safari, paisaje y fotografía nocturna con Luminar"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --no-pdf-header-footer --print-to-pdf=guia-luminar-jpeg-safari-paisaje-noche.pdf /tmp/guia.html
```

Check the result with `pdfinfo` (it should be A4, about 16 pages).

## How the guide is structured (keep these conventions when editing)

- **Language and tone:** Spanish (Spain), addressed to the reader as *tú*, plain and beginner-friendly. Luminar tool names stay in English as they appear in the app (*Noiseless AI*, *Structure AI*, *Mask AI → Sky*). Lightroom and darktable names are given in Spanish, as in their Spanish interfaces.
- **Seven numbered parts:** 1) universal concepts, 2) the 10-step base workflow in Luminar, 3) safari, 4) landscape, 5) night, 6) common mistakes and checklist, 7) equivalence table. Parts 3–5 only describe **what changes** compared with the base workflow in Part 2. Don't repeat the base steps there.
- **Each step follows the same pattern:** **Qué hacer** (Luminar, with starting values for JPEG) → **Por qué** (the universal reason) → **En otros editores** (Lightroom / darktable equivalent).
- **Values are starting points**, written as ranges (`+15 a +40`, `−0,2/−0,4`). Use a Spanish decimal comma and a true minus sign `−` (U+2212), not a hyphen.
- **Keyboard shortcuts are macOS** (`⌘`, `⇧`) and go in backticks inside bold: **`⌘1`**.
- **Content that must stay consistent across sections:** the shortcut list (Part 2), the checklist (6.2) and the equivalence table (Part 7) repeat tool names and shortcuts. If you rename or add a tool in one place, update all three.
- **Documentary ethics:** the guide deliberately warns against removing scene elements or swapping skies in documentary or wildlife photos. Keep that stance.
- **Sources:** the list at the end links to Skylum's official docs and the darktable 5.6 manual. Add a source whenever you add a claim about a specific tool's behaviour.
- **Version line:** the header records the guide date and the Luminar version. Update it when you revise the content for a new release.
