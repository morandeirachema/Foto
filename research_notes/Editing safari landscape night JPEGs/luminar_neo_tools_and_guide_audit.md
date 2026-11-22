# Luminar Neo (Luminar for Desktop 1.29.x, macOS) — official tool documentation for JPEG editing, and gap audit of the guide in `retoques/`

Method note. All 175 "Luminar for Desktop" pages listed in https://support.skylum.com/llms.txt were downloaded as Markdown on 2026-11-22 and read or searched locally. "Not documented" below means: no match in those 175 pages. Guide chapters 00–20 in `/Users/chema/code/Foto/retoques/` were read in full (not `guia-completa.md`). Nothing in that folder was modified. Doc URLs are given without the `.md` suffix. Slider ranges are not documented by Skylum anywhere (confirmed), with the few exceptions noted (Vignette −50 advice, Mystical <40, Sharpening Masking 30–70, Atmosphere Lightness default 100).

---

# PART A — What Skylum officially documents

## A1. Develop on a JPEG: which controls exist, which are RAW-only

### Takeaway
On a JPEG the tool is called "Develop" (not "Develop RAW") and has the same sections (Light, Blacks & Whites, Curves, Color, Sharpness, Noise Reduction, Optics, Transform), but three things are documented as RAW-only: the White Balance preset drop-down, Auto Distortion Corrections and Auto Fix Chromatic Aberrations; Camera Profile is described only for raw files.

### Cited Findings
- "The RAW indicator will only show next to Develop when an unedited raw file is opened"; Develop RAW is auto-applied as first tool only for RAW images — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- White Balance: the eyedropper works on any file; "If you are working with a raw file, you can use the White Balance drop-down menu to choose from various presets" (i.e. presets documented for raw only) — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- Camera Profile (DCP) is described "for maximum control over your raw files" — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop); the RAW-look article tells users to pick the camera profile "in the Develop RAW tool" — [Why do RAW photos look different](https://support.skylum.com/troubleshooting/why-do-raw-photos-look-different-in-luminar-for-desktop)
- Optics: "The exact controls you'll see vary between standard and raw files." Auto Distortion Corrections "(raw only)", Auto Fix Chromatic Aberrations "(raw only)"; Auto Defringe, Lens Distortion, Devignette, Devignette Midpoint carry no raw-only label — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- Light: Exposure, Smart Contrast ("limit color shift and prevent details from becoming blocked up"), Highlights, Shadows; Blacks & Whites: Whites, Blacks — same page.
- Curves: white/red/green/blue selectors, up to 10 control points, points deleted by double-click — same page.
- Color: Temperature ("adding Cyan or Yellow"), Tint (green/magenta), Saturation, Vibrance — same page.
- Develop has its own Sharpness section (Sharpen, Radius, Masking; "Optimal masking comes from a setting in the range of 30 to 70"; results visible at 100% zoom or higher) and its own Noise Reduction section (Luminosity Denoise, Color Denoise, Boost) — same page.
- Transform: Vertical, Horizontal, Aspect — same page.
- Auto Adjust (inside Develop): sets Exposure, Shadows, Highlights, Whites, Blacks, Saturation and Curves automatically; overwrites existing values of those sliders; "available exclusively for subscribers or lifetime owners with an Upgrade Pass" — same page.
- The eyedropper shortcut is `W`, "accessible when Develop > Color is open" — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- Masking is not available in Develop RAW / Noiseless RAW until an adjustment is applied (RAW-only restriction; does not apply to JPEG) — [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai)
- Skylum's tip article: "If you're editing a RAW file, you'll have the most flexibility with white balance"; underexposed photos are easier to save than overexposed ("once pixels are maxed out to white, there's no color information left") — [How to make a photo brighter](https://support.skylum.com/luminar-for-desktop-tips/how-to-make-a-photo-brighter)

### Inferences
- For the guide's JPEGs: no WB presets, no automatic lens profile corrections, no camera profile. Manual Lens Distortion / Devignette / Auto Defringe remain.
- The "30–70" masking tip appears twice: under Develop → Sharpness → Masking and under Details → Sharpening Masking.

### Gaps
- Docs do not say whether Temperature/Tint on a JPEG are shown in Kelvin or relative units, nor any slider range.
- Docs do not state explicitly that Camera Profile is hidden on JPEG (only that it is for raw files).

## A2. Essentials, Image Quality, Professional, Landscape and Creative tools relevant to the three genres

### Takeaway
Every tool the brief lists is documented at the level of "what each slider does", with almost no numeric guidance. Noiseless AI is explicitly documented for non-raw files (best on raw). "Relight AI" has been replaced by Light Depth. Dehaze, Golden Hour and Foliage Enhancer live in the Landscape tool.

### Cited Findings
- **Enhance AI**: Accent AI "can substitute for ... shadows, highlights, contrast, tone, saturation, exposure, and details"; Sky Enhancer AI "works from the blue hour in the morning to the blue hour in the evening ... not designed to work with night skies"; greyed-out controls = sky not recognised (out of focus or too small). "Enhance AI Improved" from 1.29.0 for eligible licences: same UI, better highlight preservation, less saturation, fewer halos — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- **Structure AI**: Amount, Boost ("more aggressive ... HDR-like look"); "human-aware"; negative Amount blurs; "use multiple instances for a heavier blur effect" — [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai)
- **Details**: Small/Medium/Large Details, Sharpen; Details Masking section = Details Protection + Details Masking; Sharpening Masking section = Sharpening Radius + Sharpening Masking (right = smaller sharpened zone; "30 to 70" tip); negative values blur — [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- **Denoise** (classic): Luminosity Denoise, Color Denoise, Boost — [Denoise](https://support.skylum.com/editing-tools/essential-tools/denoise)
- **Noiseless AI**: "works with various image formats, including raw and non-raw files, and offers optimal results when applied to raw photos"; suggests Low/Middle/High; sliders Luminosity Denoise, Color Denoise, Details (too high "can reintroduce noise or create artifacts"), Sharpness (halo risk). Location Tools > Image Quality — [Noiseless AI](https://support.skylum.com/editing-tools/image-quality-tools/noiseless-ai)
- **Supersharp AI**: Universal vs Motion Blur; Low/Middle/High; Face Enhancer AI checkbox — [Supersharp AI](https://support.skylum.com/editing-tools/image-quality-tools/supersharp-ai). Tip article: artifacts may appear at the highest setting; can be masked with Brush to the blurred area; "click and hold on the eye symbol near the Supersharp AI tab" to see the tool's effect — [How to reconstruct a blurry part of a photo](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- **Color**: Saturation, Vibrance, Remove Color Cast (a slider), HSL (Hue moves toward next/previous colour "in the list", e.g. Orange→Yellow / Orange→Red), Hue Shift — [Color](https://support.skylum.com/editing-tools/essential-tools/color). Channels are not enumerated.
- **Black & White**: Convert to B&W; Luminance and Saturation modes with Red, Yellow, Green, Cyan, Blue, Magenta; spot colour via mask — [Black & White](https://support.skylum.com/editing-tools/essential-tools/black-and-white)
- **Vignette**: Choose Subject, Amount, Size; Advanced: Mode (pre-crop/post-crop), Roundness, Feather, Inner Light; "For a realistic picture, don't lower the Amount below -50" — [Vignette](https://support.skylum.com/editing-tools/essential-tools/vignette)
- **Erase**: Select/Deselect, Size (`[` `]`), Erase, Clear Selection, Restore; Objects Removal: Remove Powerlines, Remove Dust Spots (then refine with Erase/Restore) — [Erase](https://support.skylum.com/editing-tools/essential-tools/erase)
- **Clone**: `Cmd+J`; Radius, Softness, Opacity; Option-click to change sample point; Cmd+Z undoes one stroke; "switch to another tool to apply" — [Clone](https://support.skylum.com/editing-tools/professional-tools/clone)
- **Supercontrast**: Highlights/Midtones/Shadows + three Balance sliders — [Supercontrast](https://support.skylum.com/editing-tools/professional-tools/supercontrast)
- **Color Harmony**: Brilliance, Warmth, Color Contrast (Amount, Hue), Split Color Warmth (Warm, Cool), Color Balance (Shadows/Midtones/Highlights × Cyan–Red, Magenta–Green, Yellow–Blue) — [Color Harmony](https://support.skylum.com/editing-tools/professional-tools/color-harmony)
- **Dodge & Burn**: Lighten/Darken/Erase, Brush Size, Softness, Strength, Overall Amount; curved arrow resets; exit tool to apply — [Dodge & Burn](https://support.skylum.com/editing-tools/professional-tools/dodge-and-burn)
- **Landscape**: Dehaze ("contrast, clarity, and color adjustments"), Golden Hour, Foliage Enhancer; Advanced: Foliage Hue — [Landscape](https://support.skylum.com/editing-tools/landscape-tools/landscape)
- **Atmosphere AI**: Regular = Mode (Fog, Layered Fog, Mist, Haze), Amount, Depth, Lightness (default 100). Improved (1.29.0, eligible plans) = presets Ground/Wispy/Heavy Fog, Amount, Depth Map, Clouds Drift, Height; Advanced: Patchiness, Cloud Size, Vibrance — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai)
- **Twilight Enhancer AI**: replicates Blue and Golden Hour ambiance; presets Blush, Golden, Blue, Emerald, Mauve; Amount, Exposure; Sky (Temperature, Tint); Dawn (Amount, Size, Temperature, Tint, Exposure — "simulates" a dawn light gradient); Scene Enhancements (Shade, Saturation, Relight human, Feathering); Water Reflection (Amount, Blur); Mask Refinement (Sky Horizon, Sky Global, Fix Gaps, Blur) — [Twilight Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/twilight-enhancer-ai)
- **Sky AI**: "designed to work with flat or blown-out skies"; Scene Relighting (Relight Strength, Relight Saturation, Relight Human); Mask Refinement (Global, Close Gaps, Fix Details); Sky Adjustments include Grain and Atmospheric Haze; custom skies must be JPEG, ≥1,200 px short edge, <10 MB — [Sky AI](https://support.skylum.com/editing-tools/landscape-tools/sky-ai)
- **Sunrays**: "Add a whole new light source to your photo — the sun" — [Sunrays](https://support.skylum.com/editing-tools/landscape-tools/sunrays)
- **Water Enhancer AI**: Amount, Blue, Green, Original Color, Brightness, Contrast, Depth, Mask Feather; Draw/Erase/Restore brush with Size/Softness/Strength — [Water Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/water-enhancer-ai)
- **Light Depth**: AI depth mapping; "automatically mimics the classic Dodge and Burn technique"; on-screen handles position the light; Amount, Depth Mask, Softness, Warmth, Brightness Near/Far, Warmth Near/Far; "has replaced the Relight AI tool" (old Relight edits remain adjustable in Edits) — [Light Depth](https://support.skylum.com/editing-tools/creative-tools/light-depth)
- **Film Grain**: Amount, Size, Roughness — [Film Grain](https://support.skylum.com/editing-tools/creative-tools/film-grain)
- **Mood (LUT)**: Choose LUT (.cube supported), Amount, Contrast, Saturation — [Mood (LUT)](https://support.skylum.com/editing-tools/creative-tools/mood-lut)
- **Toning**: overall Amount; Highlights/Shadows Saturation + Hue (Hue active only after Saturation applied); Balance — [Toning](https://support.skylum.com/editing-tools/creative-tools/toning)
- **Glow** (Soft Focus, Glow, Orton Effect, Orton Effect Soft), **Mystical** ("keep ... Amount below 40" for realism), **Dramatic** (lowers saturation and contrast, bleach-bypass-like), **Matte** (Amount, Fade, Contrast, Vividness; Color Toning) — [Glow](https://support.skylum.com/editing-tools/creative-tools/glow), [Mystical](https://support.skylum.com/editing-tools/creative-tools/mystical), [Dramatic](https://support.skylum.com/editing-tools/creative-tools/dramatic), [Matte](https://support.skylum.com/editing-tools/creative-tools/matte)
- **Magic Light AI**: "works best with artificial light sources"; Intensity, Size, Beam width, Glow, Clearness, Number of beams; licence-gated ("you may need to use the Upgrade option") — [Magic Light AI](https://support.skylum.com/editing-tools/creative-tools/magic-light-ai)
- **Color Transfer**: reference image, Amount, Color Intensity, Luminosity Intensity, Transition Smoothing, Color Smoothing, Match Similar Objects' Color; not for B&W photos — [Color Transfer](https://support.skylum.com/editing-tools/creative-tools/color-transfer)
- **Blur**: Gaussian, Motion, Twisted, Tilt-Shift; Gaussian + mask documented for softening a background — [Blur](https://support.skylum.com/editing-tools/creative-tools/blur)
- **Studio Light**: light-source pins with Amount, Hue, Saturation, Depth; global Brightness, Smooth, Light Contrast — designed for portraits — [Studio Light](https://support.skylum.com/editing-tools/portrait-tools/studio-light)
- **Face AI → Face Light** uses face recognition for a (human) subject's face — [Face AI](https://support.skylum.com/editing-tools/portrait-tools/face-ai)
- **Crop AI**: non-destructive; "crop tool settings are not saved with presets". Improved (1.29.0, eligible licences): Aspect Ratio, Rotate, Flip, Smart Compositions (Rule of Thirds, Golden Ratio, Golden Spiral, Golden Triangle, Centered; "More Compositions"), Grid menu, Straighten slider, Auto Straighten. Regular: Composition AI, Horizon Alignment; Ratio list Free, Original, Transposed, 1:1, 4:5, 8.5:11, 5:7, 2:3, 4:3, 21:9, 16:9, 16:10, Facebook Cover, Facebook Feed, Enter Custom; switch to another tool to apply — [Crop AI Tool](https://support.skylum.com/editing-tools/crop-ai-tool)
- **Upscale**: "up to 6X"; drag photo to Upscale box in Catalog; output is a copy in the Upscale folder with `_upscale` suffix; min input 257×257 px, max input 16,000 px long side, max output 32,000 px — [Upscale](https://support.skylum.com/extra-tools/upscale). Factors are 2x, 4x and 6x; Skylum advises noise reduction (Develop Noise Reduction or Noiseless AI) *before* upscaling and sharpening (Structure AI / Details) *after* upscaling — [Best practices with Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale)
- **GenErase / GenSwap / GenExpand**: started from the Catalog; each Save creates a new TIF in a "Generative Creations" folder; GenErase: one object at a time, generous selection, press Erase again for another result; GenExpand: up to 25%, ~10% recommended; Regular takes an optional English prompt and needs internet; Improved (1.29.0) needs no prompt and expands "up to two sides at a time" — [GenErase](https://support.skylum.com/extra-tools/generative-tools/generase), [GenSwap](https://support.skylum.com/extra-tools/generative-tools/genswap), [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand)
- **Official subject-specific workflow (pets, closest thing to wildlife)**: frame on thirds; Erase/Clone/GenErase for distractions; Blur → Gaussian with Mask AI on background; Studio Light "brighten shadows on darker pets"; Develop Smart Contrast + Accent AI; Color → HSL → Saturation to remove casts from fur; Details (Small details), Supersharp AI ("Universal or Low"), Structure AI masked to the animal with Mask AI/Object Select; Dodge & Burn for volume — [Best practices in Pet Photography](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)

### Inferences
- "Relight AI" in the brief no longer exists as a tool; one tips page still describes it ([How to make a photo brighter](https://support.skylum.com/luminar-for-desktop-tips/how-to-make-a-photo-brighter)), which is stale relative to the Light Depth page.
- Skylum's Upscale advice (sharpen after) differs slightly from "Upscale last of all".

### Gaps
- No documentation of whether Upscale / GenErase / GenExpand / HDR etc. operate on the edited rendering or on the original file when a photo already has edits. Not documented by Skylum.
- No documentation of Noiseless AI behaviour on stars, fur, or already-denoised camera JPEGs.
- HSL colour channel names are not listed.
- Studio Light on animals is only supported by the pet tip, not by the tool page.

## A3. Masking

### Takeaway
Seven mask types exist per tool (Brush, Linear Gradient, Radial, Mask AI, Object Select AI, Luminosity, Color); layer masks offer only four. Mask AI has nine fixed categories and none for animals. Mask actions are Feather, Shift Edge, Fill, Clear, Invert, Copy, Paste, Show.

### Cited Findings
- "Luminar for Desktop offers seven types of masks"; adjust the tool first, then open its Masking tab — [Masking Options](https://support.skylum.com/editing-tools/masking-options)
- Mask AI "detects up to nine separate elements ...: people, skies, buildings, vehicles, water, plants, mountains, and both natural and artificial ground"; combinable; refine with Brush — [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai)
- Object Select AI: hover highlights a recognised object, click to select, click more areas to add, "Subtract" to remove; available "in most tools or Layers" — [Object Select AI](https://support.skylum.com/editing-tools/masking-options/object-select-ai)
- Luminosity: one range slider dark→light, live preview, feathering — [Luminosity Masking](https://support.skylum.com/editing-tools/masking-options/luminosity-masking)
- Color: click to sample, Range slider — [Color Masking](https://support.skylum.com/editing-tools/masking-options/color-masking); Color Masking is listed among upgrade-gated tools — [How do I know if I need to upgrade my license?](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership/how-do-i-know-if-i-need-to-upgrade-my-license)
- Brush: Paint/Erase, Size, Softness, Strength; red overlay — [Brush Mask](https://support.skylum.com/editing-tools/masking-options/brush-mask)
- Radial: Standard protects the centre, Inverted applies inside; inner circle = size, outer = feather; rotatable; a gradient/radial mask can be refined afterwards with the Brush — [Using a Radial Mask](https://support.skylum.com/editing-tools/masking-options/using-a-radial-mask), [Linear Gradient Mask](https://support.skylum.com/editing-tools/masking-options/linear-gradient-mask)
- Mask actions — [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions)
- Layer masks: Brush, Linear Gradient, Radial Gradient, Mask AI only — [Creating a Layer Mask](https://support.skylum.com/editing-tools/masking-options/creating-a-layer-mask)
- In mask editing, `X` switches modes (Brush, Erase, Dodge & Burn); `Cmd+I` inverts; `/` show/hide; `B` `R` `G` `A` — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- **Same tool more than once**: "Click the Edits tab to make changes to a tool that was applied. Notice that you can add the same tool more than once." — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view); "Tools can be added in any order, multiple times, and with unique masks" — [Layers](https://support.skylum.com/editing-tools/layers); Structure AI "use multiple instances" — [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai)

### Inferences
- Skylum documents *that* a tool can be applied more than once (three pages), which is stronger than the guide's wording; what remains undocumented is the exact gesture (e.g. re-selecting the tool from the Tools tab after it has moved to Edits) and whether each instance gets an independent mask outside the Layers context. This refines, rather than contradicts, the author's verified fact.

### Gaps
- No documented limits (number of masks, mask combination/intersection, mask on Dodge & Burn, Erase, Crop).
- No documentation of mask accuracy on animals, fur, night scenes.

## A4. Merging tools (HDR Merge, Panorama Stitching, Focus Stacking) and stacking for night noise

### Takeaway
None of the three merge pages states accepted input formats; all outputs are TIFF in a dedicated folder. Documented limits: Focus Stacking up to 100 frames, HDR Merge batch up to 1000 images, panorama export max 15,000 px. There is no documented frame averaging / star stacking.

### Cited Findings
- HDR Merge: brackets auto-grouped from EXIF; "up to 1000 images" for batch; options Auto Alignment, Chromatic Aberration Reduction, Ghost Reduction (reference image + strength); "Continue"; result "saved as a Tiff file in the HDR Folder"; tripod advised — [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge)
- Focus Stacking: "up to 100 photos"; "corrects lens and chromatic aberration in raw files"; gear icon → Auto Alignment (reference image), Chromatic Aberration Reduction; "Stack"; TIFF in Focus Stacking folder — [Focus Stacking](https://support.skylum.com/extra-tools/focus-stacking)
- Panorama Stitching: detects bracketed images (HDR panoramas); options for distortion, vignette, chromatic aberration, ghosting; "Start"; projections spherical, cylinder, mercator, plane, fisheye; can build panoramas from video; "maximum export size is 15,000 px"; stored in Panorama Stitching folder — [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching)
- Location: Extra tab → Merge (HDR Merge, Focus Stacking, Panorama Stitching), Enhancement (Upscale, Restoration), Generative — [Luminar for Desktop walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- HDR Merge, Focus Stacking, Panorama Stitching, Upscale AI, Noiseless AI, Supersharp AI, Magic Light AI, Background Removal AI are the "8 pro-level tools (ex-Extensions)" — [Subscription, Prime and X Membership](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership)

### Inferences
- A text search of all 175 pages for "stack"/"averag" finds only Focus Stacking and Gaussian blur; so mean/median stacking for noise is not a Luminar feature per the docs. A companion Mac stacker remains unavoidable for star stacking, as the guide already says.

### Gaps
- JPEG as input to HDR/Panorama/Focus Stacking: not documented by Skylum (neither allowed nor excluded). Maximum brackets per single HDR: not documented.

## A5. Night-sky / astro tools

### Takeaway
The official docs contain no astro-specific tool: the only mention of night skies in the entire desktop documentation is the Sky Enhancer AI exclusion. No star masks, star reduction, light-pollution removal, or guidance on Noiseless and stars.

### Cited Findings
- Only page matching "night sky/skies", "astro", "milky", "light pollution" among 175 pages: Sky Enhancer AI "is not designed to work with night skies" — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- Twilight Enhancer AI targets Blue/Golden Hour; its page description says it improves "low-light or twilight photos", and Dawn "simulates" light — [Twilight Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/twilight-enhancer-ai)
- Magic Light AI is the documented tool for night street lamps — [Magic Light AI](https://support.skylum.com/editing-tools/creative-tools/magic-light-ai)
- Noise is attributed to high ISO, underexposure or long shutter speed — [Denoise](https://support.skylum.com/editing-tools/essential-tools/denoise)
- Secondary (Skylum blog, official but not docs): a post titled "Milky Way Photography: How to Capture Stunning Photos" dated 17 Nov 2026 exists; its body could not be retrieved (page text was truncated by image data), so no claims are taken from it — [Skylum blog](https://blog.skylum.com/edit-your-milky-way-photo-with-luminar/)
- Third-party, non-official: PetaPixel (June 2026, Lightroom-oriented) notes standard noise reduction "smears the stars" — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)

### Inferences
- The guide's night chapter is necessarily built from general tools; none of its night recipes can be "verified against Skylum".

### Gaps
- Skylum blog Milky Way article content unread; an older Luminar 3-era astro post exists but is for a different product generation.

## A6. Export, printing, sharing

### Takeaway
1.29 introduced a full-screen Export workspace plus Home Printing (ICC, soft proofing) and Order Prints. Documented export controls: Format, Quality, Sharpen, Color Space, Resize (Long Edge / Short Edge / Dimensions), Resolution, Signature. No metadata options, no list of colour spaces, no sharpen levels and no export bit-depth selector are documented.

### Cited Findings
- Export menu: New Export, Export with previous, Quick Export (predefined format/quality), Order Prints, Print..., Publish to Space; settings remembered between sessions; multi-photo export queue with "Remove from Export" — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- Formats: JPEG, PNG, TIFF ("works with a depth of 8 bits or 16 bits per channel"), JPEG 2000, PSD (no layers), PDF, DNG; "You should generally only save JPEG files once" — same page.
- Only colour space named anywhere: sRGB (recommended for Facebook) — [Resizing an image](https://support.skylum.com/saving-and-exporting-files/resizing-an-image)
- "Luminar for Desktop uses a standard color space called sRGB ... It does not read your custom monitor profile" (article flagged by Skylum as possibly showing an older interface; fix steps are Windows-oriented) — [Why do photo colors change after export](https://support.skylum.com/why-do-photo-colors-change-after-export-in-luminar-for-desktop)
- Home Printing: ICC profiles (recommended/imported), Rendering Intent (Perceptual/Relative), Soft Proofing, Print Sharpening (None/Low/Medium/High), Print Resolution, 16-Bit Output, Zoom/Rotate to Fill, Signature, "Save as File" print-ready JPEG or PDF — [Home Printing](https://support.skylum.com/printing/home-printing)
- Order Prints: lab products by country; automatic low-resolution warning for chosen size — [Order Prints](https://support.skylum.com/printing/order-prints)
- Shortcuts: `Shift+Cmd+E` Export, `Cmd+P` Print — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- Release notes: 1.29.0 (28 Oct 2026) "New Export ... full-screen mode with a live preview", "Print at home ... ICC profile support and soft proofing", "Order prints from a pro lab" — [Skylum changelog](https://skylum.com/whats-new/luminar-neo/68)

### Inferences
- Search for "metadata/EXIF/GPS" in the export and printing pages returns nothing relevant: stripping GPS on export is not documented, consistent with the guide.

### Gaps
- Export Sharpen values, Quality scale, available colour spaces, TIFF bit-depth choice at export: not documented by Skylum.

## A7. Catalog, non-destructive workflow, presets, sync, history, before/after, histogram

### Takeaway
Edits are stored per image as `.state` files in the Catalog with unlimited history in the Edits tab; originals are linked, not copied. Before/after has documented on-screen controls besides the `\` key. Applying a preset or an AI Assistant result overwrites existing edits.

### Cited Findings
- Right panel has five tabs: Presets, Tools, Edits, Extra, Info — [Luminar for Desktop walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- Edits saved automatically as a `.state` file per image; history "allows unlimited undos"; view via the Edits tab; persists after quitting — [Saving Adjustments in a Catalog](https://support.skylum.com/saving-and-exporting-files/saving-adjustments-in-a-catalog)
- Adding a folder: "none of your photos are moved ... creates thumbnails and links" — [Adding a Folder for editing](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/adding-a-folder-for-editing). But moving/renaming folders or images *inside* Luminar changes them on disk — [Organize Images](https://support.skylum.com/organizing-images/organize-images)
- Catalog backup: File > Catalog > Backup; restore via File > Catalog > Restore from Backup, or on macOS hold Option while launching to open "Backups" — [Backing Up a Catalog](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-a-catalog), [Backing Up and Restoring Your Edits](https://support.skylum.com/backing-up-and-restoring-your-edits)
- Virtual copies: `Cmd+'`, right-click → Virtual Copy, or Actions menu — [Virtual Copies](https://support.skylum.com/organizing-images/virtual-copies)
- Sync: orange border = active image, white = others; right-click → Adjustments > Sync Adjustments or `Shift+Cmd+S`; AI tools sync better; Crop, Erase, Background Removal cannot be synced; thumbnails are JPEG previews; batch export afterwards — [Syncing Adjustments](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/syncing-adjustments)
- Presets: Actions → Save as Preset → My Presets; Edit/Rename/Delete/Show in Finder — [Customizing Presets](https://support.skylum.com/presets/customizing-presets). "Applying a Preset will overwrite any changes you made to the image"; "For This Photo" suggests presets; Reset Adjustments does not affect Crop AI — [Browsing and Applying Presets](https://support.skylum.com/presets/browsing-and-applying-presets)
- Favourites: right-click a tool → "Add to Favorites" pins it to the top — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view)
- Before/after: `\` held; "Visibility Icon. Click to view the before and after if the image is edited" in the Photo Actions panel (View > Show Photo Actions Panel) — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images); a "Before/After slider" and a per-tool eye symbol — [How to reconstruct a blurry part of a photo](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- Histogram: View > Show Histogram; click to cycle composite / R / G / B / luminance; two corner triangles toggle cold pixels (pure black shown bright blue) and hot pixels (pure white shown red); `J` toggles clipping indicators — [Histogram](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/histogram)
- Filmstrip in Edit for switching and syncing — [Filmstrip](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/filmstrip)
- RAW+JPEG pairs: View > Raw + JPG Pairs (Show Raw Only / JPEG Only / Separately) — [Handling Raw + JPEG Pairs](https://support.skylum.com/organizing-images/handling-raw-+-jpeg-pairs)
- AI Assistant: text-prompt editing, needs internet, applying its result "replaces all previous modifications" — [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant)
- Smart Search (`Cmd+F`): content search ("tree", "beach") — [Smart Search](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/smart-search)

### Gaps
- The `;` Compare function has no description anywhere in the docs beyond the shortcut name "Compare".
- Copy/Paste Adjustments are documented only as shortcuts (`Cmd+C`/`Cmd+V`), with no explanation of what is copied.

## A8. Official macOS keyboard shortcuts (confirmed list)

### Takeaway
The guide's chapter 17 matches the official macOS table; a few official shortcuts are missing from the guide, and Skylum's own docs disagree on the AI Assistant shortcut.

### Cited Findings (all from [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys), macOS tab, unless noted)
- General: `\` before/after (hold); Space = Single/Gallery in Catalog, Fit/100% in Edit; `→`/`←`; Cmd-click, Shift-click; `Cmd+F` search (Catalog only); `Cmd+M`; `J` clipping; `Cmd+Z`; `Opt+←`/`Opt+→` breadcrumb back/forward; Ctrl+click context menu.
- File: `Opt+Shift+N` Add Folder with Images; `Cmd+N` New Album; `Cmd+O` Edit Single Image; `Shift+Cmd+E` Export; `Cmd+W`; `Opt+Cmd+W`; `Shift+Cmd+P` Page Setup; `Cmd+P` Print.
- Edit: `Cmd+Z`, `Shift+Cmd+Z`, `Cmd+X/C/V`, `Cmd+A` Select All, `Cmd+D` Deselect All, Space+drag to pan.
- Image: `P` `X` `U`; `1–5`, `0`; `Cmd+[` / `Cmd+]` Rotate Left/Right; `Cmd+'` Virtual Copy; `Shift+Cmd+S` Sync; `Shift+Cmd+R` Revert to Original (also listed as "Reset Adjustments"); `Cmd+Delete` Move to Luminar Trash; `Cmd+R` Show in Finder.
- View: `L` Catalog; `T` Presets; `E` Tools; `I` Info; `Cmd++`, `Cmd+–`, `Cmd+1` 100%, `Cmd+0` Fit; `;` Compare; `Ctrl+Cmd+F` or `Fn` Full Screen; `F` full-screen preview.
- Tools: `C` Crop; `W` eyedropper (Develop > Color open); `Cmd+J` Clone & Stamp; Option = change clone source; `Cmd+E` Erase; `X` in Crop rotates aspect ratio; `Ctrl+K` Open AI Assistant.
- Mask editing: `Cmd+I` invert; `[` `]` radius; `Shift+[` `Shift+]` softness; `X` switch modes (Brush, Erase, Dodge & Burn); `/` show/hide mask; `B` `R` `G` `A`.
- Conflict: the AI Assistant page gives `Cmd+K` on macOS — [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant); the shortcut page gives `Ctrl+K`.
- The marking page tells users to press `G` for Gallery View in one step and `L` in another; `G` is not in the shortcut table (there `G` = Gradient masking) — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images)

### Gaps
- No shortcuts documented for Luminosity/Color/Object Select masks, Dodge & Burn, histogram, or individual tools. Behaviour on non-US keyboard layouts: not documented.

## A9. Version 1.29 and licensing

### Takeaway
1.29.0 (28 Oct 2026) is the "Fall Upgrade 2026": new Export, printing, and "Improved" Crop AI, Atmosphere AI, Enhance AI, AI Assistant and GenExpand, each gated to "eligible licenses". macOS 13+ has been required since 1.28.1.

### Cited Findings
- 1.29.0, 28 Oct 2026: New Export; Print at home; Order prints; Crop suggests "up to 12 compositions" and an Auto horizon button; Atmosphere 3D fog with Clouds Drift and Height; Enhance rebuilt; generative tools more reliable with automatic retries; conversational AI Assistant; macOS 27 support; earlier entries 1.28.1 (16 Sep 2026) and 1.28.0 (5 Aug 2026, "fresh design") — [Skylum changelog](https://skylum.com/whats-new/luminar-neo/68)
- "Improved" tools "available starting with Luminar for Desktop 1.29.0 for users with eligible licenses": [Crop AI](https://support.skylum.com/editing-tools/crop-ai-tool), [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai), [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai), [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand), [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant)
- Subscription includes all upgrade tools, "Fall Upgrade 2026 tools (including Crop 2.0, Atmosphere 2.0, AI Assistant 2.0, Enhance AI 2.0...)", generative tools and the 8 pro tools; Prime is an add-on for lifetime licences; X Membership closed to new purchases — [Subscription, Prime and X Membership](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership)
- Lifetime licences may lack Pro Tools and/or Generative Tools; Upgrade Pass 2025/26 adds pro tools plus "Auto Adjust, Color Transfer, and Color Masking"; generative tools under that pass "available until December 31, 2026" — [How do I know if I need to upgrade my license?](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership/how-do-i-know-if-i-need-to-upgrade-my-license)
- macOS 13.0 or higher required from 1.28.1; Intel i5 8th gen or Apple M1–M4 — [System Requirements](https://support.skylum.com/about-luminar-for-desktop/system-requirements)
- Third-party, non-official: Phototrend's hands-on confirms three fog types and Smart Compositions — [Phototrend](https://phototrend.fr/en/2026/10/luminar-1-29-fall-update-hands-on/); Fstoppers calls the revised Atmosphere the standout — [Fstoppers](https://fstoppers.com/landscapes/luminar-fall-update-some-powerful-new-tools-905213)

### Inferences
- On a lifetime licence without passes, the guide's core night/safari tools Noiseless AI, Supersharp AI, Upscale and Magic Light AI, plus Color Masking and the generative tools, may be absent; the guide's fallback (Denoise, Details) is then the only path.

### Gaps
- The changelog entry read (first 100k characters) lists no 1.29.x point releases; whether 1.29.1+ exists was not confirmed.
- The docs do not define which licence is "eligible" for each Improved tool.

## A10. Official guidance on JPEG vs RAW, wildlife, landscape, astro workflows

### Takeaway
Skylum's support docs contain no JPEG-first workflow and no wildlife, landscape or astro workflow; the nearest items are the pet-photography tip, the "make a photo brighter" tip and scattered RAW-vs-non-RAW remarks.

### Cited Findings
- Noiseless AI best on raw, works on non-raw — [Noiseless AI](https://support.skylum.com/editing-tools/image-quality-tools/noiseless-ai)
- JPEG is lossy, "should generally only save JPEG files once" — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image); TIFF recommended as archival export — [Backing Up Your Photos](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-your-photos)
- Supported non-raw inputs: PNG, JPEG, TIFF (8/16-bit), PSD, HEIC — [Supported File Types and Cameras](https://support.skylum.com/about-luminar-for-desktop/supported-file-types-and-cameras)
- Pet tip (see A2) — [Best practices in Pet Photography](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)
- Skylum marketing wildlife page exists (AI tools, fur/feather texture, batch); no workflow — [skylum.com/wildlife-photography](https://skylum.com/wildlife-photography) (seen in search results only)
- Skylum blog "Making the most of Noiseless AI" says to apply Noiseless early; on RAW the tool sits at the bottom of the stack next to Develop RAW "providing you're using a raw photo rather than a jpeg" (search snippet only, page not fetched) — [Skylum blog](https://blog.skylum.com/making-the-most-of-noiseless-ai/)
- Third-party, non-official: Nat Hab argues JPEGs degrade quickly with editing compared to RAW — [Nat Hab](https://www.nathab.com/photo-tours/blog/jpeg-vs-raw-what-to-use)

### Gaps
- No independent, controlled JPEG-vs-RAW test of Noiseless AI was found. Named reviewers in the brief (Matt Suess, Anthony Morganti, Jim Nix, Photography Life, DPReview) were not consulted within the call budget.

---

# PART B — Gap audit of the guide (`retoques/00`–`20`)

## B1. Documented Luminar tools/options the guide does not cover or under-uses

### Takeaway
The guide is accurate on tool names but skips several documented features that matter for JPEG work: the Edits tab/history, on-screen before/after, the histogram panel, Develop's own Sharpness and Noise Reduction, Details Protection, masked Supersharp/Blur, Home Printing with soft proofing, catalog backup commands, and the 1.29 Improved variants of Enhance AI and AI Assistant.

### Cited Findings (guide location → documented feature)
- Ch. 2.1 lists three right-hand tabs (Presets, Tools, Info) plus Extra; **the Edits tab** (applied tools, history, unlimited undo) is never mentioned — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough), [Saving Adjustments in a Catalog](https://support.skylum.com/saving-and-exporting-files/saving-adjustments-in-a-catalog)
- Ch. 1.3 / 4 use only `J`; the **Histogram panel** (View > Show Histogram, per-channel view, hot/cold triangles) is not explained — [Histogram](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/histogram). Per-channel view is the documented way to spot colour casts and single-channel clipping.
- **Per-tool before/after (eye symbol)** and **Before/After slider / Visibility icon**: not in the guide — [blurry-part tip](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo), [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images)
- **Develop → Sharpness (Sharpen, Radius, Masking)** not covered; guide only uses Details — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- **Details Protection** and **Sharpening Radius** not covered (ch. 3.6, 4 step 8) — [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- **Auto Adjust** in Develop not mentioned (licence-gated) — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- **Curves**: double-click deletes a point — not in ch. 6.1 — same page.
- **Vignette** Size, Roundness, Feather, pre/post-crop Mode not covered (ch. 3.9) — [Vignette](https://support.skylum.com/editing-tools/essential-tools/vignette)
- **Erase**: Restore and Clear Selection not mentioned (ch. 4 step 10) — [Erase](https://support.skylum.com/editing-tools/essential-tools/erase)
- **Supersharp AI with a mask** (only the soft area) and **Face Enhancer AI** not mentioned (ch. 3.12, 7.2) — [blurry-part tip](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo), [Supersharp AI](https://support.skylum.com/editing-tools/image-quality-tools/supersharp-ai)
- **Blur → Gaussian with a background mask** (official pet tip) and negative Structure AI/Details as blur: guide lists Blur only in the category table; relevant to "fondo que distrae" (ch. 7) — [Blur](https://support.skylum.com/editing-tools/creative-tools/blur), [Pet tip](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)
- **Studio Light** for dark animals (official pet tip) not used; guide uses Dodge & Burn instead — [Pet tip](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)
- **Sunrays** appears in the ch. 2.1 table but is not flagged as content-adding (it adds a sun) in ch. 3.12/14.2 — [Sunrays](https://support.skylum.com/editing-tools/landscape-tools/sunrays)
- **Atmosphere AI Improved** controls (Depth Map, Clouds Drift, Height, Patchiness, Cloud Size, Vibrance) and Regular's Depth/Lightness: guide lists only modes and Amount — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai)
- **Enhance AI Improved** and **AI Assistant (Improved)**: guide's version notes (ch. 2.1, 19) name Improved generically and detail only Crop AI, Atmosphere, GenExpand — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai), [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant)
- **GenExpand Improved: up to two sides per generation**; guide says one side at a time (Regular guidance) — [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand)
- **Upscale factors 2x/4x/6x**, and Skylum's "denoise before, sharpen after" advice — [Best practices with Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale)
- **HDR Merge batch (up to 1000 images, EXIF grouping)** and **HDR panoramas / panoramas from video** not mentioned (ch. 12) — [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge), [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching)
- **Export**: Quick Export, Export with previous, multi-photo queue; **Home Printing** (ICC, soft proofing, Print Sharpening Low/Medium/High, 16-bit, save print-ready JPEG/PDF); **Order Prints** resolution warning — none in ch. 13 — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image), [Home Printing](https://support.skylum.com/printing/home-printing), [Order Prints](https://support.skylum.com/printing/order-prints)
- **Catalog backup procedure** (File > Catalog > Backup; Option-launch restore) — guide ch. 2.2/11.4 says to back up the catalog without saying how — [Backing Up a Catalog](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-a-catalog)
- **Preset overwrite warning** and "For This Photo": ch. 11.2 does not warn that applying a preset overwrites existing edits — [Browsing and Applying Presets](https://support.skylum.com/presets/browsing-and-applying-presets)
- **Favorites (pin tools)** — useful for the guide's fixed 10-step flow — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view)
- **Moving/renaming inside Luminar changes files on disk**: ch. 2.2/11.4 say Luminar "no toca tus JPEG" without this caveat — [Organize Images](https://support.skylum.com/organizing-images/organize-images)
- **Licence gating of specific tools** (Noiseless, Supersharp, Upscale, Magic Light, merges, generative, Color Masking, Auto Adjust): guide gives only a generic note — [upgrade page](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership/how-do-i-know-if-i-need-to-upgrade-my-license)
- Shortcuts missing from ch. 17: `Cmd+O`, `Cmd+[`/`Cmd+]` rotate, `Cmd+A`/`Cmd+D`, `Cmd+R`, `Cmd+Delete`, `Cmd+P`, `Ctrl+Cmd+F`, `Opt+←/→`, mask-mode `X`, AI Assistant — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)

### Inferences
- Highest-value additions for a JPEG-first guide: Edits tab + per-tool eye toggle (for the guide's "compare often" habit), per-channel histogram, masked Supersharp, the documented multi-instance capability, soft proofing in ch. 13, and the licence table.

### Gaps
- Whether Studio Light and Face AI respond to animal subjects in practice is not documented beyond the pet tip.

## B2. Guide claims the Skylum docs contradict or do not support

### Takeaway
Six items conflict with the docs (WB presets on JPEG, "three tabs", "only the shortcut shows the original", Crop AI control names by licence, screen-calibration advice vs Luminar's sRGB display behaviour, same-tool-twice wording); a further set are reasonable but unsupported by any Skylum page.

### Cited Findings — contradicted or needing correction
- **Ch. 4 step 5: "elige un preset de White Balance"**. Docs: presets are offered "if you are working with a raw file"; on JPEG only eyedropper/Temperature/Tint are documented — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop). Contradicted for the guide's JPEG scope.
- **Ch. 17: "Para ver el original, la documentación de Skylum solo da el atajo."** Docs also give the Visibility icon, a Before/After slider and a per-tool eye — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images), [blurry-part tip](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo). This also gives Spanish-keyboard users a fallback for `\`.
- **Ch. 2.1: "A la derecha hay tres pestañas: Presets, Tools e Info."** Docs list five: Presets, Tools, Edits, Extra, Info — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- **Ch. 2.3 / 5.2 / 5.6: adding the same tool twice "no explica cómo ... compruébalo".** Docs state the capability outright in three places ("you can add the same tool more than once"; "multiple times, and with unique masks"; "use multiple instances") — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view), [Layers](https://support.skylum.com/editing-tools/layers), [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai). The guide (and the author's verified fact) is right that the procedure is not described; the wording should change from "not documented whether" to "documented as possible, steps not documented". This matters because ch. 5's whole method (Develop without mask, Dodge & Burn for zones) is built on the assumption that it may be impossible.
- **Ch. 3.11, 4 step 3, 8.2: "Auto Straighten" and the "Straighten" slider presented as the general controls.** Docs put both under Crop AI Improved (1.29.0, eligible licences); Crop AI Regular calls it "Horizon Alignment" (with "Composition AI") — [Crop AI Tool](https://support.skylum.com/editing-tools/crop-ai-tool). The guide marks only Smart Compositions as Improved.
- **Ch. 1.9: "Un calibrador de pantalla es muy recomendable".** Skylum: Luminar "does not read your custom monitor profile" and displays in sRGB, so a calibrated profile can make Luminar's view differ from colour-managed apps — [Why do photo colors change after export](https://support.skylum.com/why-do-photo-colors-change-after-export-in-luminar-for-desktop). Caveat: the article carries Skylum's "may differ from the latest version" banner and its fix is written for Windows; macOS behaviour is not separately documented.
- **Ch. 4 "Rescatar" / 7.2 / 12.4: "Upscale al final de todo".** Skylum advises sharpening with Structure AI or Details *after* upscaling — [Best practices with Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale). Partial conflict.
- **Ch. 3.3: Details in Noiseless AI "Empieza en +10" / ch. 3.9, 3.x numeric limits** — consistent with the guide's own disclaimer; but note the two numeric hints Skylum does give: Vignette not below −50 (guide limit −30, fine) and Mystical below 40 (guide cites correctly).

### Cited Findings — not supported by any Skylum page (label as guide's own)
- "Compare (`;`): muestra versiones lado a lado" (ch. 2.2, 4, 5.9): docs give only the name "Compare" — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- Export "Sharpen: Bajo / Moderado" (ch. 13.2, 13.6): docs name the option without levels; Low/Medium/High is documented only for Print Sharpening — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image), [Home Printing](https://support.skylum.com/printing/home-printing)
- Colour space choice beyond sRGB (ch. 13.2): no list documented — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- Workflow order with generative tools and Upscale after edits (ch. 4, 12): docs describe these as Catalog-launched tools that write a new TIF/copy; whether prior edits are baked in is not documented — [GenErase](https://support.skylum.com/extra-tools/generative-tools/generase), [Upscale](https://support.skylum.com/extra-tools/upscale)
- Mask AI "puede fallar de noche" and failing on horns/whiskers (ch. 2.3, 9.2): plausible, not documented.
- Noiseless AI erasing small stars; Dehaze/Structure on the Milky Way core; light-pollution gradient recipe (ch. 9): not documented (no astro content in docs).
- Face AI → Face Light for campfire portraits (ch. 9.4, 10.5): supported for human faces — [Face AI](https://support.skylum.com/editing-tools/portrait-tools/face-ai); fine as written.
- "Remove Color Cast ... automáticamente" (ch. 3.5): docs describe it as a slider that "automatically removes" casts — [Color](https://support.skylum.com/editing-tools/essential-tools/color); the guide should call it a slider.
- "Temperature: azul ↔ amarillo": docs say "adding Cyan or Yellow" — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop); cosmetic.

### Cited Findings — guide claims confirmed by the docs (spot-check)
- Mask AI's nine categories; Radial Standard/Inverted; mask actions; Copy/Paste masks — [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai), [Using a Radial Mask](https://support.skylum.com/editing-tools/masking-options/using-a-radial-mask), [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions)
- Sharpening Masking 30–70; Structure AI "human-aware"; Light Depth replaced Relight AI; Mystical <40; Color Transfer not for B&W; Sky AI for flat/blown-out skies — pages cited in A2.
- Auto Distortion / Auto CA raw-only (ch. 8.2) — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- Focus Stacking 100 frames; panorama 15,000 px; Upscale 6× and pixel limits; GenExpand 25%/10%; TIFF outputs — pages cited in A2/A4.
- Sync exclusions (Crop, Erase, Background Removal); Crop not saved in presets; preset save path — pages cited in A7.
- Export formats, Resize modes, Signature, remembered settings; no metadata-removal option documented (ch. 14.3) — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- All shortcuts in ch. 17 match the official macOS table — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- "Merge tools include no noise-averaging stack" (ch. 9.2) — consistent with A4.

### Inferences
- The WB-preset line and the "only the shortcut" line are the two clear factual errors relative to the docs; the rest are scope/wording issues.
- If multiple instances work as the three doc passages say, ch. 5 could present "second Develop + Mask AI/Object Select" as the primary precise method and Dodge & Burn as the painterly one — still pending an in-app check of the gesture.

### Gaps
- The exact UI steps to add a second instance of a tool in 1.29 remain undocumented; in-app verification is still needed (already tracked in the author's PENDIENTES).

## B3. Topics on which the Skylum docs are silent

### Takeaway
The docs are silent on nearly everything quantitative and on all genre-specific technique; the guide's numbers, night workflow and JPEG limits are its own and should stay labelled as such.

### Cited Findings
- No slider ranges/defaults except: Atmosphere Lightness default 100 and Amount default 0 — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai); "At 0, the tool is not applied" for Details — [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- No astro content (see A5) — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai) is the only page mentioning night skies.
- Input formats for merges: silent — [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge), [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching), [Focus Stacking](https://support.skylum.com/extra-tools/focus-stacking)
- Metadata/GPS on export: silent — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- HSL channel list: silent — [Color](https://support.skylum.com/editing-tools/essential-tools/color)
- Non-US keyboard handling of `\ / ; [ ] '`: silent — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)

### Inferences
- Also silent (no page found; stated here as absence across the 175-page set): banding/8-bit behaviour and internal working bit depth for JPEG; order of operations in the tool stack; whether Film Grain hides banding; Noiseless on stars/fur; mask precision on animals; star stacking; heat-haze; tool-stack order effects of Noiseless on JPEG; Compare view behaviour; what Copy/Paste Adjustments includes (masks? crop?).

### Gaps
- Independent reviewers were only lightly sampled; behaviours the docs omit (multi-instance gesture, Noiseless on JPEG stars, Upscale on edited images) still need either in-app testing or a named third-party source.
