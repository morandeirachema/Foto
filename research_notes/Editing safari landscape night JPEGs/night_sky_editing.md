# Night-sky post-processing from JPEG sources (Milky Way, star fields, trails, nightscapes, fire/artificial light)

Researcher notes, compiled 2026-11-22. Context: Sony a6700 8-bit sRGB JPEGs, Sony E 11mm f/1.8, Namibia (Bortle 1-2), macOS, Luminar Neo as main editor (covered by another researcher).

Reading guide for the report writer:
- "Fetched" = I read the page itself. "Search snippet" = the claim comes from a search-result summary of that page and was not read in full; treat as lower confidence.
- Almost every expert tutorial found assumes RAW. Where I adapt it to JPEG, that adaptation is in "Inferences", not "Cited Findings".
- Several pages I tried could not be read (listed in the Gaps of the relevant section). Nothing from those pages is reported.

---

## 1. Consensus editing order for a single-exposure Milky Way image

### Takeaway
Named educators broadly agree on: global exposure/white balance first, then contrast and tone curve, then modest presence (clarity/dehaze/saturation), then local work on the core and foreground, with noise reduction either very first (AI denoise on RAW) or last (classic sliders). All sources found are RAW workflows; none addresses JPEG.

### Cited Findings
- Ian Norman (Lonely Speck), Lightroom order: (1) Exposure (example pushed +2.45 stops); (2) White balance, judged by temporarily setting Vibrance and Saturation to +100, then resetting them to 0; (3) subtle Contrast, re-check exposure; (4) Highlights/Whites down, Shadows/Blacks slightly up; (5) Clarity, Vibrance, Saturation; (6) point Tone Curve as a gentle S-curve, with black point raised slightly and no clipping; (7) noise reduction last (fetched) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Norman's numeric guard rails: Clarity below +50, Vibrance and Saturation below +50; luminance NR between 20% and 50%; colour NR left at Lightroom defaults (25 / 50 detail / 50 smoothness) (fetched) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Norman describes the method as a "RAW Lightroom post processing method" using an .arw sample; it does not discuss JPEG (fetched) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Matt Suess (in a PetaPixel article by Michael Bonocore, June 2026, marked as sponsored by DxO) reverses the NR position: AI denoise first on the RAW ("Clean it first, then you can color it"), then Lightroom (small WB tint shift, conservative clarity and contrast, slightly reduced saturation, a touch of dehaze), then a radial gradient over a town's light pollution and a linear gradient darkening the upper sky, then local contrast filters, then foreground masks (fetched) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Photography Life advises finding a relatively neutral white balance before other edits, and warns that even Lightroom's default colour noise reduction destroys much of the colour around stars (search snippet; page itself returned HTTP 402 and was not read) — [Photography Life](https://photographylife.com/how-to-edit-milky-way-lightroom)
- Improve Photography calls white balance the single biggest factor in the overall look of the Milky Way (search snippet) — [Improve Photography](https://improvephotography.com/39977/ultimate-guide-editing-milky-way-photo/)
- Capture the Atlas (Dan Zafra) lists "Blendings, Star Reduction, Advanced Post-Processing" as modules of its paid Milky Way course; no free step-by-step article was found (search snippet) — [Capture the Atlas Academy](https://academy.capturetheatlas.com/liveonly/)

### Inferences
- A JPEG-adapted order consistent with the above: (0) stack first if a sequence exists (section 5); (1) crop/level; (2) white balance as a relative shift; (3) exposure and black point, using a curve rather than a large exposure push; (4) gentle S-curve; (5) masked local contrast on the core; (6) colour (small vibrance); (7) noise reduction; (8) star control and spot fixes; (9) foreground; (10) output sharpening only for the foreground.
- Norman's +2.45-stop push is a RAW figure. An 8-bit JPEG has already been tone-mapped by the camera, so a comparable push should be expected to reveal blockiness and banding much sooner; treat roughly +1 stop as a point to start inspecting at 100%. This threshold is my estimate, not a sourced figure.
- The two NR positions (first vs last) are not really in conflict for JPEG: "denoise first" relies on RAW-domain demosaic denoising that is unavailable for JPEG, so for JPEG the practical choice is stacking first where possible and pixel-level denoise late and light.

### Gaps
- Alyn Wallace, Royce Bair, PhotoPills and National Parks at Night single-frame Milky Way editing orders were not retrieved; I found no free written Capture the Atlas tutorial.
- No named educator was found describing a JPEG-specific Milky Way workflow. This absence is itself informative: the field treats RAW as a prerequisite.

---

## 2. How badly JPEG limits astro editing; Sony in-camera processing ("star eater", NR)

### Takeaway
JPEG is a real handicap (8-bit, baked WB, baked NR and sharpening), and the expert literature simply does not cover it. On the a6700, High ISO NR is a JPEG-only process and Long Exposure NR is a dark-frame style process for exposures of 1 s or longer; I found no a6700-specific "star eater" test.

### Cited Findings
- Sony a6700 Help Guide, Long Exposure NR: applies when shutter speed is 1 second or longer; noise reduction is "turned on for the duration that the shutter is open"; unavailable with electronic shutter and in Cont. Shooting / Cont. Bracket drive modes (fetched, page is for ILCE-6700) — [Sony a6700 Help Guide](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414_long_exposure_nr.html)
- High ISO NR on Sony bodies offers Normal / Low / Off, is unavailable when File Format is RAW, and does not act on the RAW part of RAW+JPEG, i.e. it is a JPEG-pipeline process. This wording comes from another Sony model's guide, not the a6700's own page (search snippet) — [Sony Help Guide, other model](https://helpguide.sony.net/ilc/2430/v1/en/contents/0414C_high_iso_nr.html)
- "Star Eater" is "a form of software spatial filtering designed to reduce noise in photos, particularly hot pixels" that can "easily mistake sharp pinpoint stars for noise"; Norman states there are "no user selectable settings that will prevent these cameras from eating stars" (fetched) — [Lonely Speck](https://www.lonelyspeck.com/sony-star-eater-and-how-to-fix-it/)
- Cameras covered by that article: a6000, a6300, a6500, a7, a7R, a7S, a7II, a7SII, a7RII, a9, a7RIII, a7III. Trigger on a7RII/a7SII/a7RIII: all exposures longer than 3.2 s; a7III: dims small dim stars for exposures of 4 s or longer, with a much improved algorithm. The a6700 is not covered; last update noted was 2020 (fetched) — [Lonely Speck](https://www.lonelyspeck.com/sony-star-eater-and-how-to-fix-it/)
- The star-eater article is about RAW ("affects RAW images (whether uncompressed or not)") and says nothing specific about JPEG output (fetched) — [Lonely Speck](https://www.lonelyspeck.com/sony-star-eater-and-how-to-fix-it/)
- A DPReview forum user reported an a7III JPEG series showing the same artefacts as the RAW files (search snippet, anecdotal) — [DPReview forum](https://www.dpreview.com/forums/thread/4227197)
- Siril's documentation on common formats: "The JPEG format is however only coded in 8-bit", compression artefacts make it poor for astronomy, and such formats "must therefore generally be used at the end of the processing chain" (fetched) — [Siril docs](https://siril.readthedocs.io/en/stable/file-formats/Common.html)
- Sequator's feature list says "Support RAW & 16-bit TIFF"; JPEG is not listed among its headline inputs (fetched) — [Sequator](https://sites.google.com/view/sequator/)

### Inferences
- 8-bit means 256 levels per channel after the camera's tone curve. A dark Bortle 1-2 sky sits in the lowest part of that range, so the faint outer Milky Way, airglow structure and the Magellanic Clouds' outskirts occupy only a handful of levels; stretching separates those levels into visible bands (posterization) and exposes 8x8 JPEG blocks. This is arithmetic, not a sourced measurement.
- At 10-20 s, Long Exposure NR (threshold 1 s) would have fired on every frame if it was On, doubling capture time; a check of file timestamps in the 10-frame sequences (gap between frames roughly equal to the exposure) will reveal whether it was on.
- If High ISO NR was at Normal, the faintest stars and fine Milky Way dust texture are already smoothed and cannot be recovered; further strong denoise compounds the loss. Editing should therefore add less NR than a RAW tutorial suggests, not more.
- Realistically achievable from these JPEGs: a clean, natural, moderately contrasty Milky Way suitable for screens and small to medium prints, especially from the stacked sequences. Not achievable: the heavy stretches, deep dust-lane contrast and large colour re-balancing seen in RAW or tracked work.
- Mitigations for banding: do all edits in one pass in a 16-bit working space, export once; avoid repeated JPEG re-saves; prefer curves over large exposure moves; keep a little grain (or add fine grain) to dither gradients; stack frames before stretching because averaging 8-bit frames yields genuine intermediate values.

### Gaps
- No a6700-specific star-eater or spatial-filtering test was found; whether the a6700 dims stars in RAW or JPEG at 10-20 s is unverified.
- The a6700's own High ISO NR help page and the default values of both NR settings were not retrieved.
- No quantitative RAW-versus-JPEG comparison for night-sky stretching was found.

---

## 3. White balance and natural night-sky colour

### Takeaway
There is an explicit disagreement: Roger Clark argues daylight white balance is the correct setting and the natural sky is not blue, while Ian Norman's files "converge to" about 3900 K, a cooler, more neutral-to-blue rendering. In a JPEG the white balance is baked in, so only a moderate relative correction is safe.

### Cited Findings
- Roger Clark: "the moonless night sky is rarely, if ever, black or blue. It is actually much more colorful" (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Clark: "a daylight white balance is the correct white balance to show the true colors" of the night sky; fluorescent WB is inappropriate because airglow is emission-line light (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Airglow per Clark: green from atomic oxygen at 557.7 nm, typically 90-100 km high; red from atomic oxygen at 630.0/636.4 nm and from hydroxyl (OH) around 650-700 nm near 90 km; yellow sodium at 589 nm near 92 km (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Clark: Milky Way dust and star clouds are reddish-brown ("Dust in the Milky Way is similarly red: a brownish red"); stars range from red/orange to white and bluish-white; "There are no green stars"; "Less than 1% of stars are blue" (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Clark: zodiacal light is "bluish-gray light from sunlight scattered by dust in our Solar System"; and "too many nightscapes are artificially turned blue in post processing" (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Ian Norman: sets Temp to 3900 K (the value his photos tend to "converge to") and Tint +14 for the example, judged with saturation temporarily at +100 so the cast is obvious (fetched) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Matt Suess warms a core that reads cool, "usually warming it back toward red", and uses a small tint shift toward yellowish magenta (fetched; sponsored article) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Other positions: Astropix recommends daylight WB for unmodified cameras and says auto WB does not work well for astrophotography; AstroBackyard says daylight is often too warm for night-sky photos; Fstoppers lists reasons never to use auto WB at night; Wikipedia's airglow article describes airglow as generally bluish, conflicting with Clark's green/red description (all search snippets) — [Astropix](https://astropix.com/books/BGAIP/chapter2/202.html); [AstroBackyard](https://astrobackyard.com/white-balance-astrophotography/); [Fstoppers](https://fstoppers.com/astrophotography/five-reasons-never-use-auto-white-balance-night-photos-708387)
- Night scenes shot on auto WB tend to look blue; a warmer value around 5000 K is one suggested fix, but going too far turns the ground yellow or brown (search snippet) — [uniquephoto Q&A](https://www.uniquephoto.com/community/qa/can-post-processing-make-flat-nighttime-lighting-look-better-or-was-the-capture-the-real-issue)

### Inferences
- The disagreement is aesthetic versus physical: daylight WB (around 5000-5500 K) gives Clark's warm, brownish Milky Way with green/red airglow; about 3900-4200 K gives the popular cooler look. For honest Namibian dark-sky images, a target between the two, with a neutral-grey-to-slightly-warm sky background and a warm tan core, respects both camps.
- In a JPEG, Kelvin sliders are relative. If the a6700 was on Daylight WB, the file is already at Clark's recommendation and probably needs only a small cool shift, if any. If on Auto WB, frames in a sequence may differ from each other and from Daylight; correct by eye using Norman's saturation-to-maximum trick, and synchronise the correction across a stack only if the frames visibly match.
- Self-check for natural colour: sky background should not be saturated blue or purple; the core should be warm (tan/yellow-brown), not white-blue; green or reddish bands near the horizon in Bortle 1-2 are probably airglow, not a defect; no green stars.
- Large WB moves on an 8-bit JPEG stretch one channel and compress another, which increases chroma banding; keep shifts moderate and prefer finishing with a mild split/colour-grade rather than extreme temperature values.

### Gaps
- No source gave Kelvin values specifically for correcting a baked-in JPEG white balance.
- Clark's separate article on black point and processing (referred to as Part 3f5) was not retrieved.
- Southern-hemisphere specifics (colour of the Magellanic Clouds, Carina region) were not researched.

---

## 4. Noise reduction for night JPEGs: single-frame AI denoise

### Takeaway
AI denoisers can produce swirl or "crystal" artefacts in star fields and outline or soften stars; practitioners use mild models and moderate strength and keep some grain. The best-reviewed tools (Lightroom Denoise, DxO PureRAW) work on RAW only, so they do not apply to these files.

### Cited Findings
- Matt Suess uses DeepPRIME 3 rather than the stronger XD3 for star fields, lens sharpness at Standard not Hard (Hard "starts sharpening the noise right along with everything else"), and deliberately keeps "a touch of grain" to preserve star detail (fetched; sponsored by DxO) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- A 2024 Adobe community thread reports Lightroom AI Denoise creating swirl artefacts in dark gaps between stars and in low-texture areas of night-sky images (search snippet) — [Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/ai-denoise-creates-swirl-artifacts-astrophotography/m-p/14787212)
- An Fstoppers writer sets AI denoise strength to 50 for night photos because higher values introduced artefacts (search snippet) — [Fstoppers](https://fstoppers.com/astrophotography/how-create-perfect-night-photos-640297)
- A Topaz community thread complains stars can look like small jagged crystals after denoise/sharpen (search snippet) — [Topaz Community](https://community.topazlabs.com/t/astro-processing/41771)
- Alan Dyer's comparative tests of AI noise reduction for nightscapes exist at amazingsky.net and via PetaPixel (2022); earlier Topaz versions left patchy artefacts (search snippets; not read in full) — [amazingsky.net](https://amazingsky.net/tag/ai/); [PetaPixel 2022](https://petapixel.com/2022/11/26/a-comparison-of-noise-reduction-programs-for-astrophotography/)
- Ian Norman's classic-slider range: luminance NR 20-50%, compensating muddiness with Detail and Contrast (fetched; RAW) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Photography Life: default colour NR already destroys colour around stars (search snippet) — [Photography Life](https://photographylife.com/how-to-edit-milky-way-lightroom)

### Inferences
- JPEG-specific risk: AI denoisers are trained mainly on RAW or clean-JPEG noise. An ISO 3200-6400 JPEG that has already had in-camera NR contains blotchy, compressed residual noise, which AI tools are more likely to convert into worm/swirl textures or to treat faint stars as noise. Test at low strength on a 100% crop of a star-dense region and a star-sparse region before committing.
- Practical order of preference for these files: (a) stack the 10-frame sequences, which reduces noise without inventing detail; (b) light pixel-level denoise, masked more strongly on the foreground and smooth sky than on the Milky Way band; (c) accept fine grain, which also hides banding.
- Do not sharpen the sky after denoising; sharpening is the usual cause of crystalline stars and halos.

### Gaps
- No test of any AI denoiser on high-ISO night JPEGs (as opposed to RAW) was found.
- Luminar Neo's Noiseless AI behaviour on stars is left to the other researcher.
- The search results on denoisers are from 2022-2024; these tools change quickly.

---

## 5. Stacking from JPEGs: does it work, expected gain, macOS tools

### Takeaway
Stacking is the single most valuable step for the 10-frame sequences and the Mac-native equivalent of Sequator is Starry Landscape Stacker (USD 39.99), but I could not confirm from an official page that it accepts JPEG directly; converting JPEGs to 16-bit TIFF first is the safe route. Siril (free, Apple Silicon build) and Affinity (now free) are alternatives with more manual foreground handling.

### Cited Findings

Tool facts (verified November 2026 unless stated):

| Tool | Price | macOS / Apple Silicon | JPEG input | Notes | URL status |
|---|---|---|---|---|---|
| Starry Landscape Stacker | USD 39.99 on Mac App Store (GBP 39.99 UK); free trial from developer site | "Requires macOS 11.5 or later"; a 1.9.4 note says "Built for M1 Macs. I do not have an M1 Mac and cannot test this." | Not confirmed on any official page I could read; RAW (since 1.9.0) and TIFF are documented | Version 1.10.1 (dated "Oct 12", year not shown; 1.10.0 was 2025-05-31) | [App Store](https://apps.apple.com/us/app/starry-landscape-stacker/id550326617?mt=12) and [developer site](https://sites.google.com/site/starrylandscapestacker/home) both load |
| Siril | Free; source code downloadable, donations accepted | Separate "Intel macOS" and "Apple Silicon macOS" .dmg builds | Docs discuss JPEG as an 8-bit format poor for astronomy; explicit import statement not found on the page read | Version 1.4.5 released 2026-10-28 | [siril.org/download](https://siril.org/download/) loads |
| Affinity (by Canva) | "Affinity is free for individuals"; Canva AI tools need a Canva premium plan | "Fully optimized for macOS. Runs natively on Apple silicon and Intel." | Not confirmed | Astrophotography Stack Persona documented in Affinity help; download routes through Canva sign-in | [affinity.studio](https://www.affinity.studio/) loads |
| StarStaX (trails) | New version: price not stated, "Coming soon to the Mac App Store"; legacy macOS/Windows builds free, "no longer maintained and are provided as-is" | New version "Requires macOS 15.4 or later, on Apple silicon or Intel" | New-version page lists RAW formats; exports JPEG/PNG/TIFF 8 or 16 bit | See section 6 | [starstax.net](https://starstax.net/) loads; old markus-enzweiler.de/software/starstax/ redirects there (301) |
| Sequator | Free | Windows only (search snippets; official home page does not state platform) | "Support RAW & 16-bit TIFF" | Reference tool only; runs on Mac only via CrossOver per one compatibility listing | [Sequator](https://sites.google.com/view/sequator/) loads |

- Starry Landscape Stacker is "a Mac app" that composites "several images taken in rapid succession, shifting the sky as needed to align the stars", works on "a group of images that were captured in rapid succession with identical exposure settings", "produces 6 different results created with different algorithms", and "can also do dark frame subtraction and flat-field compensation" (fetched) — [SLS home](https://sites.google.com/site/starrylandscapestacker/home); [App Store](https://apps.apple.com/us/app/starry-landscape-stacker/id550326617?mt=12)
- SLS algorithms: "Min Horizon Noise" ("designed to minimize noise at the edge of the mask for the sky", likely best for most users); "Min Horizon Star Dupe" (use when the former trails or duplicates stars near the sky edge); Mean with outlier rejection (two variants); Median integrated with outlier rejection. Sky mask is built from automatically placed red dots that the user can paint, with an "islands of sky" mode for disconnected sky patches (fetched) — [SLS version 1.7 notes](https://www.sites.google.com/site/starrylandscapestacker/new-in-version-1-7)
- SLS developer FAQ: "Typically 20 to 50 images collected over a period of 5 to 10 minutes will be stacked"; camera must be motionless on a tripod; RAW decoding relies on Apple's library; if RAW is unsupported, "convert your RAW files to 16-bit TIFF files"; FITS unsupported; bias frames unsupported, dark frames preferred (fetched) — [Stacking apps FAQ](https://sites.google.com/view/stacking-apps/frequently-asked-questions)
- SLS release note: "It is strongly preferred to use tiff files without alpha as the files are 33% smaller" (fetched) — [App Store](https://apps.apple.com/us/app/starry-landscape-stacker/id550326617?mt=12)
- The sister app Starry Sky Stacker (tracked, sky-only) states its images must be RAW, TIFF or JPEG; it is the wrong tool for tripod nightscapes because it requires an equatorial mount (search snippet for format; fetched FAQ for the mount requirement) — [Starry Sky Stacker](https://apps.apple.com/us/app/starry-sky-stacker/id1332533290?mt=12); [FAQ](https://sites.google.com/view/stacking-apps/frequently-asked-questions)
- Sequator features: "Foreground detection & stacking", "Light pollution reduction function", "auto-brightness or HDR-mode output", "Powerful correction for wide-angle & complex distortions", output in 16-bit TIFF (fetched) — [Sequator](https://sites.google.com/view/sequator/)
- Sequator "Freeze ground" detects moving versus stable parts and stacks them separately; requires a fixed foreground, identical exposure settings and 4 or more images (search snippet of the manual) — [Sequator manual](https://sites.google.com/view/sequator/manual)
- Siril gradient removal ("Background extraction"): polynomial degree 1 is recommended for simple, often linear gradients; RBF handles complex gradients with fewer samples; samples near bright stars/objects should be removed (search snippet of official tutorial) — [Siril gradient tutorial](https://siril.org/tutorials/gradient/)
- A PIXLS.US tutorial covers processing a nightscape in Siril (written for 0.9.10) including a separate "Processing for the foreground" step (search snippet; page not read) — [PIXLS.US](https://pixls.us/articles/processing-a-nightscape-in-siril/)
- Affinity's Astrophotography Stack Persona handles light, bias, dark and flat frames; stacking by mean, median and sigma clipping (search snippets) — [Affinity help](https://affinity.help/photo2/en-US.lproj/pages/Astrophotography/astro_creating.html); [Sky at Night review](https://www.skyatnightmagazine.com/reviews/software/serif-affinity-photo-2-software)
- One guide claims Affinity is not suitable for Milky Way nightscape stacking; the search tool flagged this page as low quality, and it conflicts with positive reviews (search snippet) — [Pippit](https://www.pippit.ai/resource/astrophotography-software)

Sequator-to-Mac feature mapping:

| Sequator (Windows) | Starry Landscape Stacker | Siril |
|---|---|---|
| Freeze ground | Built-in sky/ground mask (red dots, paintable); sky aligned, ground kept static; algorithms "Min Horizon Noise" / "Min Horizon Star Dupe" | No one-click equivalent (search snippet says it "does not handle the ground-freezing task"); stack twice (registered for sky, unregistered for ground) and blend in an editor |
| Reduce light pollution | No equivalent found on the pages read | "Background extraction" (polynomial or RBF) |

### Inferences
- Expected gain: averaging N frames of random noise improves signal-to-noise by about the square root of N, so 10 frames give about 3.2x (roughly equivalent to 1.7 stops lower ISO). This is standard statistics; I did not retrieve a source stating it, and the real gain from JPEGs will be somewhat lower because in-camera NR makes the noise partly correlated and non-random (hot pixels, banding) noise does not average away without rejection or dark frames.
- Stacking JPEGs works in principle because alignment and averaging operate on pixel values regardless of container, and the 16-bit average of ten 8-bit frames contains real intermediate tonal levels, which directly reduces posterization when stretched. Always export the stack as 16-bit TIFF and do the stretch on that.
- 10 frames is below the SLS developer's typical 20-50 but well above Sequator's minimum of 4; expect a clear but not dramatic improvement.
- With an 11 mm lens on APS-C, 10 frames of 10-20 s span only 2-4 minutes, so star displacement between frames is small but not negligible; simple median stacking without alignment will smear stars, so sky alignment is required.
- Recommended trial path: download the free SLS trial, try feeding the JPEGs directly; if rejected, batch-convert to 16-bit TIFF (without alpha) in Preview, Luminar or `sips` first. Do not apply lens corrections, denoise or sharpening before stacking; apply identical WB if any.
- Because in-camera Long Exposure NR (if on) already did dark subtraction, separate dark frames are unnecessary for those files.

### Gaps
- Whether Starry Landscape Stacker accepts JPEG input directly is unconfirmed: the developer's "restrictions and requirements" URL I tried returned 404, and the pages read mention only RAW and TIFF.
- Whether Siril opens JPEG sequences directly was not explicitly confirmed by the documentation page read.
- Photoshop median stack: Lonely Speck's Photoshop stacking tutorial could not be retrieved (the URL I tried returned 404), so I have no sourced step list or current Photoshop pricing. The known approach (load files as layers, auto-align sky, Smart Object stack mode Median/Mean, mask the foreground) is from my background knowledge and unverified here.
- Affinity's stacking persona with a static foreground (nightscape use) and its JPEG acceptance were not verified on an official page. The current free Affinity app's inclusion of the astrophotography stack was reported by one less-established blog only ([zelpio](https://www.zelpio.com/blog/affinity-v3-astrophotography-review/), search snippet).
- Sequator's Windows-only status comes from third-party listings; its home page does not state the platform.

---

## 6. Star trails from JPEG sequences (StarStaX)

### Takeaway
Star-trail stacking is the one night workflow where JPEG input costs little: lighten blending only picks the brightest pixel per position. StarStaX is in transition: a rewritten version (macOS 15.4+, Apple silicon or Intel) is announced as coming to the Mac App Store, while the free legacy builds are unmaintained.

### Cited Findings
- New StarStaX: six blending modes (Lighten, Darken, Average, Add, Multiply, Subtract); Lighten is the mode for classic star trails (fetched) — [StarStaX](https://starstax.net/)
- Gap filling: "Close the dark gaps between exposures, so dotted star trails become smooth lines without being widened or merged" (fetched) — [StarStaX](https://starstax.net/)
- Comet trails: temporal decay applied while stacking so stars fade along their trail (fetched) — [StarStaX](https://starstax.net/)
- Dark frames: "Load dark frames to reduce sensor noise and hot pixels using a familiar astrophotography workflow" (fetched) — [StarStaX](https://starstax.net/)
- Streak removal: paint over aeroplane or satellite streaks and StarStaX restacks that area from the original frames without them; also levels, white balance, vignette, denoise and one-click removal of light-pollution colour casts; export JPEG/PNG/TIFF at 8 or 16 bit, plus video (fetched) — [StarStaX](https://starstax.net/)
- Availability: new version "Coming soon to the Mac App Store", "Requires macOS 15.4 or later, on Apple silicon or Intel"; legacy macOS and Windows builds are free downloads, "no longer maintained and are provided as-is" (fetched) — [StarStaX](https://starstax.net/)
- National Parks at Night, four ways to remove planes in Photoshop: first find the offending layers by toggling layers in a Lighten stack and colour-code them; then (1) Lightroom spot healing on the flattened image, fastest but lowest quality; (2) black brush at 100% on each offending layer, which works because Lighten ignores darker pixels, about 30 minutes in the author's test; (3) content-aware spot healing per layer, about 27 minutes; (4) per-layer masks, non-destructive (fetched) — [National Parks at Night](https://www.nationalparksatnight.com/blog/2018/8/18/four-ways-to-remove-airplanes-from-star-trails-in-post-production)
- The same article says not to apply lens profile corrections before stacking because it can cause irreparable moire (fetched) — [National Parks at Night](https://www.nationalparksatnight.com/blog/2018/8/18/four-ways-to-remove-airplanes-from-star-trails-in-post-production)
- Gaps arise because Lighten keeps only the brightest pixel so dim inter-frame gaps stay open; Greg Benz suggests a slight Gaussian blur (radius 0.5-1.0) for residual gaps and advises turning off sharpening and avoiding any delay between frames (search snippets) — [Greg Benz](https://gregbenzphotography.com/photography-tips/create-clean-star-trails/); [Fred Miranda tutorial](https://www.fredmiranda.com/forum/viewedits.php?mid=6567318&page=0)

### Inferences
- Workflow for the JPEG trail sequences: apply identical, minimal global edits (or none) to all frames; no lens corrections, no sharpening, no denoise; stack with Lighten; enable gap filling if trails look dotted; fix planes/satellites either with StarStaX streak removal (new version) or by blacking them out on the individual source frames before stacking; then edit the result once as a single image.
- If in-camera Long Exposure NR was on during the trail sequence, each frame was followed by an equal-length dark exposure, producing gaps as long as the exposures themselves. Gap filling cannot fully hide 50% gaps; expect dashed trails and consider presenting them as such or using the comet mode.
- In-camera JPEG sharpening tends to accentuate gaps and beading; this is baked in and is a reason to prefer gap filling over further sharpening.
- Lighten stacking does not reduce noise in the sky background (it selects maxima, so noise accumulates upward). A separate Average stack of the same frames, masked onto the static foreground, gives a cleaner ground.
- Until the new StarStaX ships, the legacy build's behaviour on current macOS on Apple Silicon is untested here; Affinity or Photoshop Lighten layer stacks are the fallback.

### Gaps
- New StarStaX price, release date and explicit JPEG-input statement were not on the page (it lists RAW formats; legacy StarStaX is known for JPEG input, but I did not verify that here).
- Whether the legacy StarStaX build runs on macOS 26/27 on Apple Silicon was not verified.
- National Parks at Night's star-stacking guide Part III (2023) was not read.

---

## 7. Light pollution, gradients, airglow and zodiacal light

### Takeaway
Tools exist to model and subtract gradients (Siril Background extraction) or to locally darken glow (gradients/radial masks), but in Bortle 1-2 Namibia most "gradient" is natural airglow or zodiacal light, which Clark and others treat as part of the real sky to be kept unless isolating astronomical objects.

### Cited Findings
- Clark: sky colour on a moonless night comes mainly from airglow and light pollution; starlight scattered by the atmosphere contributes less (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Clark: to show colours beyond the atmosphere "you need to SUBTRACT the scattered light from the earth's atmosphere, including light pollution and airglow", but his natural-colour nightscape examples keep airglow visible (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Clark: zodiacal light is bluish-grey sunlight scattered by solar-system dust (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- Airglow is typically too faint to trigger colour vision, so its colour appears mainly in long exposures (search snippet) — [Universe Today](https://www.universetoday.com/articles/how-to-see-airglow-the-green-sheen-of-night)
- Matt Suess handles a town's glow with a radial gradient, darkens the upper sky with a linear gradient, and uses a colour mask to target green and magenta airglow separately from the rest of the sky (fetched; sponsored) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Siril: polynomial degree 1 for simple linear gradients, RBF for complex ones (search snippet) — [Siril gradient tutorial](https://siril.org/tutorials/gradient/)
- Sequator has a "Light pollution reduction function"; StarStaX (new) advertises one-click removal of light-pollution colour casts (fetched) — [Sequator](https://sites.google.com/view/sequator/); [StarStaX](https://starstax.net/)
- DarkSky's principles for responsible astrophotography call for transparent information about how and where images were captured (search snippet) — [DarkSky](https://darksky.org/news/darkskys-principles-for-responsible-astrophotography/)

### Inferences
- In Namibia, treat horizon colour in three categories: (a) lodge, vehicle or distant town glow, which is warm, localised and fair to tone down with a masked desaturation or cooling; (b) airglow, which is green or red, banded or rippled and often brighter toward the horizon, and should be kept, perhaps slightly desaturated if it overwhelms; (c) zodiacal light, a tilted cone of pale light along the ecliptic after dusk or before dawn, which should be kept and not mistaken for light pollution.
- Automatic gradient removal on wide-angle nightscapes will try to flatten the Milky Way band, airglow and zodiacal light together, and on 8-bit data it will posterize. Prefer gentle linear or radial masks; if using Siril background extraction, use degree 1 only and on the 16-bit stacked file.
- Captioning "green bands are natural airglow" is an honest way to pre-empt the assumption that it is an editing artefact.

### Gaps
- No source specific to Namibian or southern-African sky conditions (dust, airglow frequency) was retrieved.
- Starry Landscape Stacker gradient or light-pollution features: none found on pages read; cannot confirm absence.

---

## 8. Enhancing the Milky Way: local contrast, masks, star reduction

### Takeaway
Experts apply modest global presence and then target the core with masks; quoted ceilings are Clarity below +50 (Norman) and a ClearView/dehaze-type filter around +12 (Suess), with halos around stars the standard over-processing tell. I found no sourced, free description of star-reduction technique.

### Cited Findings
- Norman: personal guideline to keep Clarity below +50 and Vibrance/Saturation below +50; tone curve as a gradual S that does not clip at either end, with the black point slightly raised (fetched; RAW) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Suess: "I keep the slider around plus 12" for ClearView; above that it "starts outlining the stars"; Tonal Contrast at about +25 with midtones raised to lift the core; a soft-glow filter used sparingly to soften stars and hide noise (fetched; sponsored) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Suess's warnings: "Halos are the giveaway of an over-processed night sky"; saturation can turn the sky "garish and electric"; "the second it takes more than it gives, I back off"; "The thumbnail will lie to you" (check at 100%) (fetched) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Star reduction is taught as a distinct advanced step in Capture the Atlas's paid course (search snippet) — [Capture the Atlas Academy](https://academy.capturetheatlas.com/liveonly/)
- A Lightroom night-editing guide notes the Tone Curve can bring out star colour and detail while the Presence panel should be used sparingly (search snippet) — [Great Big Photography World](https://greatbigphotographyworld.com/how-to-edit-night-photos/)

### Inferences
- For 8-bit JPEGs, take roughly half of the RAW ceilings as starting points: clarity-type local contrast around +10 to +25 and dehaze around +5 to +15, applied through a soft brush or radial mask on the galactic band rather than globally. These numbers are my adaptation, not sourced values; the test is absence of halos, blockiness and banding at 100%.
- Dehaze is the most dangerous slider on JPEG night skies: it strongly raises contrast in the darkest tones (where the fewest levels exist), shifts colour toward blue/magenta and amplifies vignetting and banding.
- Star reduction (minimum filter or star-mask shrinking) depends on clean, round stars; on in-camera-sharpened, denoised JPEG stars it tends to create dark rings. If used at all, apply subtly and only in the Milky Way band; a mild soft-glow is a safer way to de-emphasise pinpoint stars.
- Dodge the core and burn the surrounding sky gently with a large-feather mask; this increases perceived contrast without stretching the data as hard as global contrast.

### Gaps
- No free, citable description of star-minimisation methods or amounts from Wallace, Zafra or Bair was retrieved.
- "Typical amounts" for dehaze from a named educator were not found (Norman's article does not mention dehaze).

---

## 9. Foreground: lifting shadows, low-level lighting, blends, honesty conventions

### Takeaway
The community splits images into single exposures, same-position stacks/blends, and composites of different times or places; the convergent norm is disclosure, not prohibition. For JPEG, foreground shadow lifting is limited, and stacking is again the best aid.

### Cited Findings
- An Fstoppers article argues for more disclosure of composite nightscapes, noting the main reason not to disclose is fear the image will be valued less (search snippet) — [Fstoppers](https://fstoppers.com/composite/compositing-nightscape-imagery-cheating-244271)
- Views in community threads range from accepting a blue-hour foreground blended with a night sky shot from the same spot, to holding that no disclosure should be needed; a Fred Miranda member argues that disclosing a two-image sky/ground blend is enough for most viewers (search snippets) — [Fstoppers group thread](https://fstoppers.com/groups/landscape-and-nature-photography/324393/composite-disclosure-mandatory); [Fred Miranda](https://www.fredmiranda.com/forum/topic/1433096/1/)
- Some astrophotographers criticised National Geographic for publishing composite night-sky photos contrary to its ethics code (search snippet) — [Inside Imaging](https://www.insideimaging.com.au/?p=23357)
- DarkSky asks for transparent information about how and where images were captured (search snippet) — [DarkSky](https://darksky.org/news/darkskys-principles-for-responsible-astrophotography/)
- Suess shoots separate sky and foreground exposures and combines them in Photoshop with feathered edges (fetched) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Starry Landscape Stacker and Sequator keep the ground static while aligning the sky, so the foreground is also averaged across frames (fetched) — [SLS App Store](https://apps.apple.com/us/app/starry-landscape-stacker/id550326617?mt=12); [Sequator](https://sites.google.com/view/sequator/)

### Inferences
- A workable honesty ladder for captions: "single exposure"; "stack of N identical frames for noise reduction" (same time, same place, generally not regarded as a composite); "blend" (same position, different time or exposure, such as blue hour); "composite" (different place, focal length or night). The user's material falls in the first two categories, which need no defensive disclosure, though stating "10-frame stack" is good practice.
- Foregrounds in Bortle 1-2 without moon or lighting are near-black in a 10-20 s JPEG. Lifting more than about 1-1.5 stops will show blotchy chroma noise and banding (my estimate). Options: keep the foreground as a clean silhouette (often the most honest and most attractive choice with camelthorn/quiver trees), or use the stacked foreground, lift moderately, desaturate shadows slightly and denoise more strongly than the sky.
- Low-level lighting and blue-hour blends are capture-time techniques; they cannot be added in editing to the existing files without crossing into composite territory.

### Gaps
- Royce Bair's low-level-lighting guidance and any formal competition rule sets (for example Milky Way Photographer of the Year categories) were not retrieved.
- The ethics evidence here is mostly forum opinion via search snippets; treat as indicative of the debate, not as a standard.

---

## 10. Fire and artificially lit night scenes (campfire, floodlit waterhole)

### Takeaway
I found no authoritative tutorial on editing campfire or floodlit-wildlife JPEGs; available general advice is to correct white balance gently, pull highlights/whites, and avoid heavy saturation and contrast, with the caveat that clipped flame detail cannot be rebuilt from a JPEG.

### Cited Findings
- Auto white balance is easily fooled at night under mixed lighting; manual WB is preferred (search snippets) — [Fstoppers](https://fstoppers.com/astrophotography/five-reasons-never-use-auto-white-balance-night-photos-708387); [TechRadar](https://techradar.com/how-to/photography-video-capture/cameras/night-photography-settings-your-camera-wants-you-to-use-1321003/3)
- General night-edit advice: recover highlights, correct white balance gently, avoid heavy saturation or contrast; pull Whites down to limit clipping, and use the Alt/Option clipping display while dragging Highlights (search snippets) — [uniquephoto Q&A](https://www.uniquephoto.com/community/qa/can-post-processing-make-flat-nighttime-lighting-look-better-or-was-the-capture-the-real-issue); [Great Big Photography World](https://greatbigphotographyworld.com/how-to-edit-night-photos/); [Digital Photography School](https://digital-photography-school.com/6-easy-steps-post-processing-low-light-photo-lightroom/)
- Norman's example lowers Highlights/Whites to recover an illuminated tent, then raises Shadows/Blacks slightly to compensate (fetched; RAW) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- A course lesson exists on blending exposures with different white balances for night scenes (search snippet; title only) — [LinkedIn Learning/Lynda](https://www.lynda.com/Photography-Night-Low-Light-tutorials/Blending-exposures-different-white-balances/90279/102160-4.html)

### Inferences
- Mixed colour temperature: a fire is far warmer than the night sky, and waterhole floodlights are typically warm sodium-like or cool LED. No single WB suits both. Use two masked white balances: leave the fire-lit zone warm (viewers expect orange firelight; neutralising it looks wrong) and set the sky zone separately toward neutral. This local-WB approach is the JPEG equivalent of the "blend two white balances" technique.
- Blown flames: in a 10-20 s exposure the flame core is clipped in all channels and is unrecoverable in JPEG. Do not drag Highlights far down, which turns clipped white into flat grey or produces a hard-edged yellow blob; instead lower Whites slightly, and let the core stay bright with a smooth roll-off, optionally adding a touch of warm colour to the clipped area's edge via a low-opacity mask.
- Saturation clipping: orange light often clips the red channel while others remain; reducing saturation/luminance of orange and red in HSL restores apparent texture in fire-lit faces and ground better than exposure changes.
- Deep shadows around a fire or floodlight: lift sparingly; the natural look is a pool of light falling to black. Aggressive shadow lifting reveals JPEG banding in the smooth falloff around the light, which is the most banding-prone area in such images; keep or add fine grain there.
- Floodlit animals: subject motion over multi-second exposures is baked in; denoise with a subject mask (lighter on fur detail), and avoid strong sharpening that emphasises motion blur. If the floodlight has a strong green or orange cast, partially correct rather than fully neutralise, then desaturate that hue slightly.
- If several frames of the same static fire/waterhole scene exist, mean-stacking reduces noise in the static parts, but flames and animals will ghost; mask them from a single frame.

### Gaps
- No named expert source on campfire or floodlit-waterhole post-processing was found; this whole section rests mainly on inference and generic night-editing advice.
- Nothing was found about specific floodlight types used at Namibian waterholes (for example Okaukuejo) or their colour temperature.

---

## 11. Hot pixels, coma and corner aberrations at f/1.8, vignetting correction

### Takeaway
Little directly sourced material was retrieved here. What was found: in-camera Long Exposure NR and Sony's spatial filtering both target hot pixels; stackers accept dark frames; lens-profile corrections should not be applied before stacking; and Lightroom's profile is said to over-correct vignetting.

### Cited Findings
- Sony's spatial filtering is aimed particularly at hot pixels (fetched) — [Lonely Speck](https://www.lonelyspeck.com/sony-star-eater-and-how-to-fix-it/)
- Long Exposure NR on the a6700 runs for exposures of 1 s or longer, for the same duration as the exposure (fetched) — [Sony a6700 Help Guide](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414_long_exposure_nr.html)
- Starry Landscape Stacker "can also do dark frame subtraction and flat-field compensation"; StarStaX loads dark frames "to reduce sensor noise and hot pixels" (fetched) — [SLS home](https://sites.google.com/site/starrylandscapestacker/home); [StarStaX](https://starstax.net/)
- SLS algorithms with outlier rejection (Mean with outlier rejection, Median with outlier rejection) exist (fetched) — [SLS 1.7 notes](https://www.sites.google.com/site/starrylandscapestacker/new-in-version-1-7)
- Do not apply lens profile corrections before stacking star-trail frames; it can cause irreparable moire (fetched) — [National Parks at Night](https://www.nationalparksatnight.com/blog/2018/8/18/four-ways-to-remove-airplanes-from-star-trails-in-post-production)
- Photography Life suggests Lightroom often overdoes vignetting correction for Milky Way images (search snippet) — [Photography Life](https://photographylife.com/how-to-edit-milky-way-lightroom)
- Sequator advertises "Powerful correction for wide-angle & complex distortions" during alignment (fetched) — [Sequator](https://sites.google.com/view/sequator/)

### Inferences
- Hot pixels: if Long Exposure NR was on, most are already removed. Remaining ones are fixed in position, so in a sky-aligned stack they turn into short dotted streaks in the sky and stay as points on the ground; outlier-rejecting algorithms suppress them. In single frames, remove the few obvious coloured points with a spot/erase tool; they are identifiable as single saturated red, green or blue pixels without a star-like halo.
- Vignetting: correcting corner falloff multiplies corner brightness, and noise with it. Brightening corners by 1.5-2 stops in an 8-bit JPEG raises corner noise and banding by the same factor. Correct only partially, or leave a natural vignette, which also suits night images. Note that the camera may already have applied shading compensation to the JPEG (a setting on Sony bodies), in which case no further correction should be added.
- Coma and astigmatism in the corners at f/1.8 (stars shaped like wings or crosses) cannot be corrected in post from a JPEG. Mitigations are cosmetic: avoid sharpening or clarity in corners, keep a mild vignette, crop slightly, or slightly reduce corner star brightness with a masked adjustment.
- Chromatic fringing (purple or green rims on bright stars) can be reduced with a defringe tool, but applied globally it desaturates genuine star colour; apply lightly.
- For wide-angle stacks, lens distortion makes corner stars move differently from central ones; dedicated nightscape stackers model this, whereas a plain median stack in a general editor may leave corner stars doubled.

### Gaps
- No measured data on Sony E 11mm f/1.8 coma, vignetting or the a6700's in-camera shading/distortion compensation defaults was retrieved.
- No expert source specifically on hot-pixel removal from JPEGs was found.

---

## 12. Common beginner mistakes and self-checks

### Takeaway
The recurring expert warnings are over-saturation and artificial blue skies, halos from excessive local contrast, over-smoothing by noise reduction, and judging from thumbnails instead of 100% view. JPEG adds banding and re-compression as extra failure modes.

### Cited Findings
- "too many nightscapes are artificially turned blue in post processing" (fetched) — [Clarkvision](https://clarkvision.com/articles/color.of.the.night.sky)
- "Halos are the giveaway of an over-processed night sky"; saturation makes skies "garish and electric"; "The thumbnail will lie to you"; back off "the second it takes more than it gives" (fetched) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- Keep Clarity, Vibrance and Saturation below +50; luminance NR above about 50% turns the image muddy; avoid clipping at either end of the tone curve (fetched) — [Lonely Speck](https://www.lonelyspeck.com/how-to-process-milky-way-astrophotography-in-adobe-lightroom/)
- Sharpening settings that are too strong sharpen the noise (fetched) — [PetaPixel](https://petapixel.com/2026/06/24/how-to-turn-a-flat-noisy-raw-into-a-finished-milky-way-photograph/)
- AI denoise at high strength introduces artefacts in night photos (search snippet) — [Fstoppers](https://fstoppers.com/astrophotography/how-create-perfect-night-photos-640297)
- Colour noise reduction strips colour from stars (search snippet) — [Photography Life](https://photographylife.com/how-to-edit-milky-way-lightroom)
- Applying lens corrections before stacking can cause moire (fetched) — [National Parks at Night](https://www.nationalparksatnight.com/blog/2018/8/18/four-ways-to-remove-airplanes-from-star-trails-in-post-production)
- JPEG belongs "at the end of the processing chain" (fetched) — [Siril docs](https://siril.readthedocs.io/en/stable/file-formats/Common.html)

### Inferences
Self-check list assembled from the above (the checklist form is mine):
- Sky background is dark grey with slight natural colour, not pure black (clipped) and not saturated blue or purple.
- Histogram: left edge not hard-clipped; a small gap or toe remains.
- 100% view of smooth sky away from the Milky Way: no contour bands, 8x8 blocks, worm/swirl textures or plastic smoothness.
- 100% view of stars: no dark rings or bright halos, no crystalline shapes, star colours still present (some orange, some blue-white), no green stars.
- Core: warm, with dust lanes visible but not black-and-white "crunchy"; no visible mask edge around the band.
- Horizon: no bright halo line along the skyline or trees (from clarity/dehaze or sloppy masks).
- Corners: not noisier or more magenta/green than the centre (over-corrected vignetting).
- Foreground: brightness plausible for starlight; not brighter than the sky above it.
- Stacks: stars round across the frame, no doubled stars near the horizon, no smeared foreground edges.
- Compare with the original after a break; if the edit looks like a different night, reduce it. Check on a phone and, for prints, lighten slightly because prints read darker than screens.
- Export once from a 16-bit working file; never re-edit an already exported JPEG.

### Gaps
- No single authoritative "common mistakes" article from the named educators (Wallace, Zafra, Bair, National Parks at Night, PhotoPills) was retrieved; the list above is a synthesis.

---

## Source access notes (for the report writer)
- Loaded and read: Lonely Speck (Lightroom Milky Way; Star Eater), Clarkvision (correct URL is `color.of.the.night.sky`; the hyphenated form returns 404), PetaPixel June 2026 (sponsored by DxO), Sony a6700 Help Guide (Long Exposure NR), siril.org/download, Siril docs (common formats), starstax.net, Starry Landscape Stacker home / 1.7 notes / FAQ / App Store, Sequator home, affinity.studio, National Parks at Night (aeroplane removal).
- Failed: Photography Life (HTTP 402), a guessed Lonely Speck Photoshop-stacking URL (404), a guessed SLS restrictions-and-requirements URL (404), PIXLS.US Siril nightscape article (redirect not followed).
- Not attempted or not found: Alyn Wallace, Royce Bair, PhotoPills, Capture the Atlas free tutorials, Adobe Photoshop pricing/stack-mode documentation, DPReview a6700-specific testing.
