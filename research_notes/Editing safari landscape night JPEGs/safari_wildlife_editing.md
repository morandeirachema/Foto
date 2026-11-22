# Post-processing workflow for safari / wildlife photographs from 8-bit JPEG sources (as of November 2026)

Research context: Sony a6700 JPEGs (26 MP, sRGB), Sony E 70-350mm, Namibia (Etosha + desert), harsh midday light, dust/heat haze, golden hour, floodlit waterholes at night, ISO 3200-12800, heavy crops; output = family sharing and occasional prints.

Reliability key used below:
- **[fetched]** = I read the page content (via a summarising fetch tool; quotes are as returned by that tool).
- **[snippet]** = taken from a search-result excerpt only; page not opened. Treat as lower confidence and, where flagged, attribution to the exact URL is probable but not confirmed.

Sources I tried and could NOT read: Photography Life "Wildlife photography in Etosha, part 1" (HTTP 402 paywall), Natural Habitat Adventures / WWF Lightroom post-production article (HTTP 429), SLR Lounge "enhancing the eyes" (404). No Will Burrard-Lucas, Steve Perry (primary), Wild Eye, Africa Geographic, Nature's Best or GDT pages were successfully read; see Gaps in each section.

---

## 1. Consensus step-by-step editing order

### Takeaway
There is no single canonical order, but the named sources converge on: cull -> crop early -> fix technical flaws (noise, chromatic aberration) -> global tone/white balance with small moves -> masked local work to lead the eye to the face and separate subject from background -> eyes -> final subject-only sharpening/texture, then check at both 100% and at viewing size. The one real disagreement is whether noise reduction comes first (Mark Dumbleton) or among the final touches (older Lightroom tutorials).

### Cited Findings
- Mark Dumbleton (South African wildlife photographer), as summarised by Fstoppers (23 Feb 2026): (1) remove technical flaws first - noise reduction and chromatic aberration before exposure or other sliders, "so you don't enhance artifacts later when sharpening or adding contrast"; (2) fix exposure and add colour grading; (3) masks and radial gradients to guide the eye to the subject's face (subtly darken competing highlights, brighten the head); (4) separate subject from background with contrast and colour shifts. The article gives no numeric values (those are in his video, not read). [fetched] — [Fstoppers: Stop Guessing: A Professional Wildlife Editing Guide](https://fstoppers.com/lightroom/stop-guessing-professional-wildlife-editing-guide-900221)
- Steve and Ann Toon (wildlife photographers, writing in Australian Photography, Aug 2023): delete no-hopers first, then a second pass comparing similar frames; enable lens profile corrections + chromatic aberration removal; "crop early so the histogram reflects the final content"; then tone and white balance; then masked local adjustments; sharpening preferably done last, outside Lightroom. [fetched] — [Australian Photography: Lightroom tips for wildlife photographers, Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one); [Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)
- A WWF photographer (Mac Mirabile, Natural Habitat Adventures blog) starts each session by checking critical sharpness, "especially in the eyes"; the same series splits processing into "first, the clean-up, and then the enhancement stage", and places sharpening and noise removal among the final touches. [snippet; page returned HTTP 429 when fetched] — [Nat Hab: Post-production of wildlife images using Lightroom](https://www.nathab.com/blog/post-production-of-wildlife-images-getting-the-best-image-from-your-raw-file-using-lightroom)
- Matt Kloskowski (via Fstoppers, Alex Cooke, 31 Oct 2026) adds a final verification step: view at 100% for fur/feathers/edges AND at the size the image will actually be seen (phone, print); leave the edit overnight and re-judge. "Overcooked noise reduction can look fine small and fall apart up close. An over-brightened subject can hide at 100% and stand out at full-frame view." [fetched] — [Fstoppers: What Separates a Natural Wildlife Edit From an Overcooked One](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)
- Typical global slider magnitudes from the Toons (RAW-based): exposure "no more than 0.25 stops either way"; Whites often +50 or more; Highlights sometimes as far as -100; Shadows and Blacks adjusted together and "rarely by more than +/-15"; Contrast slider rarely used; Clarity about +10, rarely above +15, and masked mainly to the animal; Texture generally not adjusted; Dehaze rarely used globally; Vibrance usually no more than +10; Saturation used cautiously; Tint never more than +/-10. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)

### Inferences
- A synthesis order that is consistent with all the above and adapted for JPEG: (1) cull; (2) crop/straighten; (3) denoise (gently - see section 5); (4) global exposure/white balance/highlights/shadows with small moves; (5) subject mask: slight exposure/contrast/clarity on the animal; (6) background mask: slight darkening, optional mild desaturation, extra noise reduction; (7) eyes; (8) distraction dodging/burning; (9) subject-only sharpening; (10) check at 100% and at output size; export.
- The "denoise first vs last" disagreement matters less for JPEG: in a non-destructive editor the order of sliders is internal anyway; the relevant principle (Dumbleton) is simply not to amplify noise/artifacts with later contrast and sharpening. If a standalone AI denoiser is used, run it before other edits.
- All numeric ranges above come from RAW workflows. For an 8-bit sRGB JPEG, where tone curve, white balance, sharpening and noise reduction are already baked in, they should be read as upper bounds; the Toons' already-small moves (0.25 stop, +/-15 shadows, +10 clarity/vibrance) are a reasonable JPEG-safe envelope, whereas their large Highlights (-100) / Whites (+50) moves will recover far less in JPEG and can produce grey, flat highlights or banding.

### Gaps
- No primary-source step order from Will Burrard-Lucas, Steve Perry, Wild Eye or Africa Geographic was retrieved.
- Dumbleton's actual slider values (video only) were not obtained.

---

## 2. Cropping: composition, how far 26 MP can go, AI upscaling

### Takeaway
Composition advice is unanimous: leave space in the direction the animal looks/moves, do not let it touch the frame edge, and cut limbs "all or nothing". How far to crop is governed by pixel count at output size plus the fact that cropping magnifies noise and softness; small screen sharing tolerates very deep crops, prints do not. AI upscaling does not add real detail and is banned by documentary/competition standards.

### Cited Findings
- Kloskowski: leave room in the direction the animal is facing (his osprey example has nearly half the frame empty ahead of the bird; some images leave two-thirds blank); trim the trailing side further for more tension; don't let the subject press against the border - "a little space on both sides reads as calmer"; he recrops a frame with ~60% empty space toward 4x5; print sizes can force aspect-ratio decisions. [fetched] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)
- Nature TTL: cropping too tightly makes the image cramped; if you crop into a limb do it decisively - "it's all or nothing when it comes to digital amputation!"; avoid huge crops of distant subjects, which "leave a very small file and magnify noise and soft focus". [fetched] — [Nature TTL: The Post-processing Mistakes You Don't Want to Make](https://www.naturettl.com/?p=5048)
- Audubon / Melissa Groo: "don't crop so much that the bird feels squished"; keep space around the subject and room in front of a moving one; excessive cropping reduces resolution and quality (no numeric limit given). [fetched] — [Audubon: The Dos and Don'ts of Editing Bird Photos](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)
- Digital Photography School: cramped crops with no room ahead of the head are mistake #1; rule of thirds suggested as a guide. [fetched] — [DPS: 5 Unforgiving Post-Processing Mistakes Every Bird Photographer Must Avoid](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Eye placement: one guide recommends placing the animal's eye on one of the four rule-of-thirds intersection "power points"; other guides say the rule is only a guideline and that a centred subject can "strongly connect the viewer". Exact source URLs for these excerpts were not confirmed. [snippet] — candidates: [B&H Wildlife Photography Composition Guide](https://www.bhphotovideo.com/explora/node/126686), [Adorama: Understanding Composition in Animal Photography](https://www.adorama.com/alc/animal-photography-composition)
- Steve and Ann Toon: for photo agencies and competitions "avoid reducing the original by more than 20 per cent"; otherwise crop lightly, leaving room for the subject to look and move into. [fetched] — [Australian Photography Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)
- Print pixel requirements (Canon manual table at 300 dpi): A4 = about 8.7 million pixels; A3 = 4961 x 3508 = about 17.4 million pixels. [snippet] — [Canon Print Studio Pro manual: Numbers of Pixels and Print Sizes](https://ij.manual.canon/ij/webmanual/PrintStudioPro/W/1.4/EL/DPPG/dppg_f-02.html)
- A looser standard: an uncropped 20 MP image makes a ~27-inch-wide print at 200 dpi (attributed in the excerpt to a Jim Zuckerman Photo Insights piece; attribution probable). [snippet] — [Photo Insights, May 2022](https://issuu.com/jimzuckerman/docs/photo_insights_may_2022/s/15669332)
- "Particularly in photos taken with a high ISO setting, heavy cropping can amplify the noise to the point that the photo becomes unusable." (attribution to this URL probable) [snippet] — [DPS: How (and When) to Crop Your Photos](https://digital-photography-school.com/cropping-for-impact/)
- Upscaling: Wildlife Photographer of the Year tells entrants "Please do not upscale" the high-resolution file; World Press Photo lists "all AI-powered enlarging tools" as tools that "immediately breach the contest rules". [fetched] — [NHM WPY adult rules](https://www.nhm.ac.uk/visit/wpy/competition/adult-competition/rules.html); [World Press Photo: What counts as manipulation](https://www.worldpressphoto.org/contest/verification-process/what-counts-as-manipulation)
- Generative canvas extension: Kloskowski notes Photoshop's Generative Expand can add canvas if a frame was shot too tight. [fetched] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317). Note this is invented content and is prohibited under WPY ("any post-processing that adds new content through AI") and World Press Photo ("no use of artificially generative fill is allowed").

### Inferences
(My own arithmetic; the a6700's 6192 x 4128 pixel frame size is from memory, not from a source retrieved in this research - verify.)
- Full frame 6192 x 4128 (25.6 MP) prints about 20.6 x 13.8 in at 300 ppi, or about 31 x 20.6 in at 200 ppi.
- Using Canon's 300 dpi figures: an A4 print needs ~8.7 MP, i.e. you can keep roughly one third of the frame area (a linear crop of ~1.7x, equivalent to ~600mm on the 350mm lens in field-of-view terms). A3 needs ~17.4 MP, i.e. only a ~1.2x linear crop. At a relaxed 200 ppi the A4 threshold drops to ~3.9 MP (a ~2.5x linear crop).
- Screen sharing: a 4K display is 3840 x 2160 (~8.3 MP), a phone or messaging app shows ~2-3 MP or less. So on pixel count alone a crop to 1/8 of the frame (~3 MP, ~2.9x linear) still fills a phone/HD view. In practice the limit is reached earlier for ISO 3200-12800 JPEGs because the crop enlarges noise, in-camera NR smearing, JPEG blocks, heat-haze softness and the lens's softness at 350mm - consistent with Nature TTL's and DPS's warnings.
- Practical rule of thumb derived from the above (inference, not a sourced rule): for low-ISO, sharp frames, up to ~50% linear (keep >= 6 MP) is safe for A4 prints and any screen; for ISO >= 6400 frames, treat ~1.5x linear as the limit for print and accept deeper crops only for phone-size viewing.
- The Toons' "no more than 20 per cent" is a stock-agency/competition standard, not a family-album one.
- AI upscaling can make a deep crop print smoother (fewer visible pixels) but the "detail" is synthesised; for a documentary-honest album it is best limited to modest enlargement for print interpolation rather than rescuing sub-2 MP crops. I found no reliable source quantifying acceptable upscale factors for JPEG wildlife crops.

### Gaps
- No authoritative source on preferred aspect ratios for wildlife (beyond Kloskowski's 4x5 example and "print sizes force the ratio").
- No tested, sourced data on a6700 + 70-350mm crop tolerance specifically, nor on AI upscaler performance on high-ISO JPEG crops.

---

## 3. Subject separation and how much is too much

### Takeaway
Experts separate the animal with small, masked moves: slightly brighten/add local contrast to the animal (especially the face), slightly darken or dull the background and competing highlights, and keep clarity/sharpening off the background. The named failure mode is the "sticker effect" - an animal that looks pasted in - and smeared, ghostly backgrounds from negative texture/clarity.

### Cited Findings
- Dumbleton: use masks and radial gradients to pull the eye to the face - "subtly darkening competing highlights on the bird's wing and brightening the head"; separate subject from background with contrast and colour shifts so the animal stands against a soft, non-distracting background. [fetched] — [Fstoppers / Dumbleton](https://fstoppers.com/lightroom/stop-guessing-professional-wildlife-editing-guide-900221)
- Kloskowski: avoid the "sticker effect: brightening the subject or darkening the background until the animal looks pasted in"; avoid pushing background texture and clarity negative, which "can create a ghostly smear" - leaving the background alone can look better; make the adjustment, leave it overnight, then decide how far to pull back. [fetched] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)
- Steve and Ann Toon: Select Subject, invert, and adjust the background to make the animal stand out; intersect the inverted selection with a top-down linear gradient and reduce Clarity to mimic focus fall-off; use a heavily feathered brush for dodging and burning and "to dull distracting highlights such as bright rocks or branches"; Clarity (~+10, rarely >+15) applied mainly to the animal; in a masked background the Temp slider can be moved slightly cooler. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two); [Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)
- DPS: global saturation makes "the bird and background compete"; instead saturate only the subject (HSL or brush); Clarity typically +20 to +30, restrict to +10 to +30, and nudge with arrow keys rather than dragging. [fetched] — [DPS: 5 Unforgiving Post-Processing Mistakes](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Toons on vignettes: they add vignetting manually (Lens Corrections manual tab) for wide-angle shots "if you like it". [fetched] — [Australian Photography Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)
- Note the two sources disagree on reducing background clarity: the Toons use it (with a gradient, to mimic focus fall-off); Kloskowski warns negative background texture/clarity gives a ghostly smear. [fetched] — sources as above.

### Inferences
- The disagreement on negative background clarity is one of degree: a small, gradient-shaped reduction is accepted; a strong uniform one is not. With JPEGs, where in-camera NR has already smoothed the background, extra negative clarity/texture is more likely to tip into the "smear".
- With a slow lens (f/6.3 at 350mm on APS-C) backgrounds in Etosha will often be relatively sharp and busy; separation will therefore rely more on tone (exposure) and colour than on blur. Artificial background blur was not recommended by any source I read and is a classic "pasted-in" trigger at mask edges.
- "How much is too much" is expressed by sources only qualitatively (sticker effect; overnight re-check; view at output size). I found no sourced numeric cap for subject-vs-background exposure difference or vignette amount.
- AI subject masks on small, dusty, low-contrast animals will have imperfect edges; mask-edge halos are most visible when the exposure difference across the mask is large - another reason to keep the differential small (inference).

### Gaps
- No sourced numeric vignette guidance for wildlife (amount/feather).
- No sourced numbers for background darkening/desaturation.

---

## 4. Eyes, catchlights, and fur/feather detail

### Takeaway
The eye is the anchor of a wildlife image; pros treat it with a tiny, hard-edged local mask (slight lift in exposure/highlights, a touch of clarity/sharpening), never spilling onto surrounding fur, and build the effect in small steps. Fur/feather texture is enhanced with modest clarity on the subject only (around +10 to +15; some tutorials allow up to +30).

### Cited Findings
- WWF/Nat Hab (Mac Mirabile): "For wildlife photography, sharpness in the eyes is very important" - check it first; when masking the eye, do not brush outside it, or "you will apply these settings to the fur and feathers, ruining the intent". [snippet] — [Nat Hab blog](https://www.nathab.com/blog/post-production-of-wildlife-images-getting-the-best-image-from-your-raw-file-using-lightroom)
- Steve and Ann Toon: "use a hard-edged brush only for small, well-defined details such as eyes"; the brush can add a little extra sharpening to the eyes. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)
- A Lightroom method reported in search results pairs a small exposure lift with extra clarity and saturation via a brush mask on the iris, then softens noise in the iris if it looks too strong; another stacks brush-masked highlight adjustments in small steps so the eye does not look artificial; brightening the catchlight and the lower lid line by dodging is described as a small step that suits nearly any wildlife portrait. Exact pages not opened; no numeric values available. [snippet] — candidates: [Nature TTL: Dodge and burn](https://www.naturettl.com/dodge-and-burn/), [Fstoppers: Post-processing cats' eyes in Lightroom Classic](https://fstoppers.com/animal/post-processing-cats-eyes-lightroom-classic-548401), [Shutterbug: Editing Wildlife Photos is All About the Eyes](https://shutterbug.com/node/586132)
- Dark-eyed species: the catchlight is what separates the eye from surrounding shadow and fur. [snippet; source page not confirmed] — candidate: [Nat Hab: What is catch light in wildlife photography](https://www.nathab.com/photo-tours/blog/photo-jargon-what-is-catch-light-in-wildlife-photography)
- Texture: Toons - Clarity ~+10, rarely above +15, masked to the animal; Texture slider "generally not adjusted, as it rarely suits natural subjects". DPS - excess clarity makes feather detail look artificial "and even leaves can look like plastic"; keep to +10 to +30. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two); [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Kloskowski: after denoising, restore life to the subject with a subject mask adding texture and grain "at about 10% at most", applied to the animal only. [fetched] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)

### Inferences
- Honesty line for eyes: enhancing an existing catchlight (dodging) is tonal adjustment; painting in a catchlight that was not there is adding content, which falls foul of the WPY "adding ... objects" / "post-processing that adds new content" rule (section 9). That mapping is my inference; the rules do not mention catchlights explicitly.
- In heavily cropped, high-ISO JPEGs the eye may be only a few dozen pixels across and already smeared by in-camera NR; local sharpening there mostly amplifies noise and JPEG blocks. A slight exposure/contrast lift is the safer eye treatment for such frames; reserve eye sharpening for frames where the eye is genuinely resolved.
- At night under floodlights, animal eyes may show eyeshine or flat dark sockets; sources did not address this.

### Gaps
- No verified numeric recipe for eye enhancement (the SLR Lounge article returned 404; other eye tutorials were seen only as snippets).
- Nothing found on editing eyeshine in floodlit shots.

---

## 5. High-ISO noise in JPEGs

### Takeaway
Denoising a JPEG works, but less well than on RAW, because the file is already demosaiced, noise-reduced, sharpened and compressed; the expert consensus on technique - moderate global denoise, heavier NR on the smooth background, protect or re-texture the subject, sharpen only the subject - applies even more strictly to JPEGs. The two tell-tales of failure are waxy fur and halos.

### Cited Findings
- JPEG constraint: sharpening and noise reduction are applied in-camera at capture; a JPEG is 8-bit and compressed with the camera's decisions baked in; Adobe states noise reduction is more effective on RAW than JPEG. [snippet] — [Adobe: RAW vs JPEG](https://www.adobe.com/learn/lightroom-cc/web/raw-vs-jpeg); [Fstoppers: The Practical Guide to Shooting Raw vs. JPEG](https://fstoppers.com/education/practical-guide-shooting-raw-vs-jpeg-696188)
- Adobe's current Camera Raw help lists JPEG, HEIF, TIFF and PNG as supported for AI Denoise, and warns that photos already strongly denoised in-camera may show less improvement. Older (2023) Adobe community answers saying JPEG is unsupported are outdated. [snippet] — [Adobe Help: Improve image quality using Camera Raw (Enhance)](https://helpx.adobe.com/in/camera-raw/using/enhance.html)
- Adobe community expert comments: "a JPEG is baked; it has a great deal of data loss compared to the raw"; AI denoising a JPEG "will never be as effective" as on RAW; one user reported that denoising a JPEG blurred fine text and in shadows "only increased noise and artifacts as if it were details" (anecdotal). [snippet] — [Adobe Community: Denoise AI format compatibility thread](https://community.adobe.com/t5/lightroom-classic-discussions/new-denoise-ai-incompatibility-with-photo-format-why/m-p/14142431)
- Kloskowski (RAW AI Denoise context): start around 50-60%; higher makes feathers "smooth and waxy"; lower lets noise return in dark backgrounds; keep the higher setting and add texture/grain (max ~10%) back on the subject only via a subject mask. [fetched] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)
- Nature TTL: too much NR gives a waxy texture with lost detail and flattened edges; residual noise is most visible in smooth, darker areas; apply NR mainly to the background by masking the subject. [fetched] — [Nature TTL](https://www.naturettl.com/?p=5048)
- DPS: apply NR only to smooth areas such as the background; leave detailed areas (the animal's body) alone, "where noise is less visible". [fetched] — [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Steve Perry's (Backcountry Gallery) technique as reported by a forum user, not by Perry directly: background cleaned with negative Texture plus a little manual noise reduction on a background mask; AI Denoise at only ~30 after sharpening, then subject and background cleaned separately with masks. [snippet; second-hand] — [BCG Forums: Trying Steve's noise reduction technique](https://bcgforums.com/threads/trying-steves-noise-reduction-technique.38677)
- A general guide suggests blending ~25-33% of the original noisy background back in to avoid a plastic look. [snippet; source page not confirmed] — candidate: [Unique Photo Q&A](https://www.uniquephoto.com/community/qa/how-can-i-reduce-high-iso-noise-in-a-dark-photo-without-softening-the-subject)
- Sharpening: sharpen only the subject, not the background; when in doubt use less; "Over-sharpening kills a photograph. Period." (DPS). Keep the Lightroom sharpening slider no higher than about 60 (Nature TTL). Over-sharpening adds "noisy pixelation and a bright halo", making the animal "crispy" (Audubon/Groo). [fetched] — [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid); [Nature TTL](https://www.naturettl.com/?p=5048); [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)
- Avoid creating noise: the Toons limit shadow/black lifts (rarely more than +/-15) because lifting dark tones adds noise. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)
- Counterpoint: prints are forgiving of noise, so denoising matters less for prints (forum opinion). [snippet] — [RSPB community thread](https://community.rspb.org.uk/community/wildlife/f/19351/t/135288.aspx)
- Dumbleton: do NR before contrast/sharpening so later steps do not enhance artifacts. [fetched] — [Fstoppers / Dumbleton](https://fstoppers.com/lightroom/stop-guessing-professional-wildlife-editing-guide-900221)

### Inferences
- Tone down RAW numbers for JPEG: Nature TTL's "sharpening no higher than ~60" and Kloskowski's "Denoise 50-60%" assume unsharpened, un-denoised RAW. An out-of-camera JPEG has already had both applied, so the equivalent JPEG settings should be markedly lower (e.g. little or no additional capture sharpening; denoise strength started low and raised only until background chroma blotches and grain calm down). This is inference; I found no source giving JPEG-specific numbers.
- JPEG-specific failure modes not present in RAW advice: (a) the residual noise in a camera JPEG is blotchy/low-frequency rather than fine grain, so AI denoisers may interpret blotches as texture ("increased noise and artifacts as if it were details"); (b) 8x8 JPEG block edges and in-camera sharpening halos get amplified by any sharpening or clarity; (c) fine fur detail erased by in-camera NR cannot be recovered - AI "sharpen/recover detail" tools will synthesise plausible fur, which is an honesty as well as an aesthetic issue.
- Best-fit JPEG recipe by inference from the cited techniques: mild global luminance + chroma NR; stronger NR on an inverted-subject (background) mask; no extra NR, or very little, on the animal; optionally a touch of fine grain overall to unify texture; subject-only sharpening with a small radius and high masking/threshold, checked at 100% for halos; do all of this before/independent of contrast and clarity increases.
- Because output is mostly small-screen sharing, downsizing itself is a powerful denoiser: a 26 MP frame shown at ~2-8 MP averages noise away. Judge noise at output size (Kloskowski's "view at the size it will be seen") before deciding to denoise heavily.
- Deep crops + high ISO compound (section 2): the frames that need most NR are also the ones with least real detail, so expectations for ISO 12800 heavy crops should be "acceptable on a phone", not "printable".

### Gaps
- No independent, sourced test of AI denoisers (Lightroom Denoise, Topaz, DxO) specifically on high-ISO out-of-camera JPEGs. Note DxO PureRAW is RAW-only by design (general knowledge, not verified in this research).
- No source on Sony a6700 in-camera High ISO NR behaviour in JPEGs.
- Steve Perry's method is second-hand; his own article/video was not retrieved.

---

## 6. Harsh midday light, dust, heat haze, blown highlights and blocked shadows

### Takeaway
Heat shimmer is refraction blur, not haze: mild cases tolerate a little sharpening, moderate/severe cases are unfixable, and dehaze targets a different phenomenon (low-contrast veil from dust/atmosphere), which it can partially improve. Clipped JPEG highlights are gone for good, and shadow lifting should stay small; for harsh-contrast frames, pros change the interpretation (silhouette, high-contrast, black and white) rather than forcing a "golden hour" look.

### Cited Findings
- Adorama (Austin James Jackson, 15 Aug 2025): heat distortion occurs when "hot air rises and mixes with cooler air", which "causes light passing through to refract"; it is worse for distant subjects/telephoto because you look through more atmosphere. "Minor heat distortion may be slightly fixed in post processing by doing a small amount of sharpening", but "images with severe or even moderate heat distortion can't be fixed" - "no sharpening can fix it"; "it's crucial to avoid heat distortion in the field rather than relying on post-processing". [fetched] — [Adorama: How to Avoid Heat Distortion in Your Photography](https://www.adorama.com/alc/how-to-avoid-heat-distortion-in-photography/)
- Dehaze tools can improve atmospheric haze somewhat but no filter fully fixes heat turbulence; atmospheric haze "doesn't give the same shimmering blurred effect"; frame averaging/stacking generally will not restore true detail. [snippet] — [Unique Photo Q&A: Can you reduce heat haze...](https://www.uniquephoto.com/community/qa/can-you-reduce-heat-haze-or-atmospheric-haze-in-long-distance-photos-and-does-stacking-help)
- Field anecdote: same location fine at 7 AM, "impossible to fix using Photoshop" at 2 PM. [snippet] — [FixThePhoto: Heat Distortion Effect](https://fixthephoto.com/heat-distortion-effect.html)
- Steve and Ann Toon on dehaze: rarely used globally; applied locally with a mask it can reduce softening from an out-of-focus foreground object. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)
- Highlights: Audubon/Groo - "Blown-out areas cannot be recovered" (even in RAW). Toons - drag Highlights left to keep detail in bright plumage; raise Whites for punch; for white subjects underexpose slightly in camera and raise exposure afterwards; watch the histogram clipping triangles. [fetched] — [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos); [Australian Photography Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one); [Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)
- A Grand Canyon RAW-vs-JPEG comparison found blown highlights were a problem in both formats, and RAW came out noticeably cleaner after identical noise reduction. [snippet] — [Fstoppers: Raw vs. JPEG at the Grand Canyon](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- One tour-operator source describes JPEG editing as going grainy or streaky with even slight adjustments, and says heavy JPEG edits look artificial quickly. [snippet] — [Nat Hab: JPEG vs RAW](https://www.nathab.com/photo-tours/blog/jpeg-vs-raw-what-to-use); [Nat Hab: Should you start shooting in RAW](https://www.nathab.com/photo-tours/blog/should-you-start-shooting-in-raw)
- Harsh-light strategy (Danielle of C4 Photo Safaris, via Fstoppers, 24 May 2026, shot in Liwonde, Malawi): deliberately overexpose a dark buffalo against bright grass to "lean into harsh contrast" and mark it as a black-and-white candidate; for a rim-lit baboon in deep shade, either underexpose for a silhouette or lift exposure to recover the eyes - "either can work, depending on the mood". [fetched] — [Fstoppers: Can You Still Get Good Wildlife Shots in Harsh Midday Light?](https://fstoppers.com/education/can-still-get-good-wildlife-shots-harsh-midday-light-902576)
- Shadows: Toons adjust Shadows and Blacks together, rarely beyond +/-15, because lifting adds noise. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)
- Etosha-specific: the salt pan creates bright white backgrounds at waterholes; one author recommends a polariser in the field to compensate. [fetched] — [DPS: A Southern African Photo Safari... from Inside the Rest Camps](https://digital-photography-school.com/a-southern-african-photo-safari-with-a-difference-from-inside-the-rest-camps/)

### Inferences
- What can be fixed in a JPEG: low-contrast dust veil (moderate dehaze/contrast, ideally masked to the distant part of the scene); slight warm/yellow dust cast (white balance); mild softness (light subject sharpening); moderately bright but unclipped highlights (Highlights down); moderately dark shadows (small lift + NR).
- What cannot: heat-shimmer wobble and smeared edges (sharpening just sharpens the wobble into crunchy artifacts); clipped white calcrete/pan ground, pale springbok/oryx flanks or zebra whites (pulling Highlights down just turns them grey); fully blocked blacks on elephants/wildebeest (lifting reveals noise, posterisation and JPEG blocks rather than hide texture).
- Dehaze on 8-bit JPEGs has specific side effects (inference from how the tool works, not sourced): it raises saturation and shadow density, amplifies noise and banding in skies, and exaggerates sensor dust spots. It should be applied in small amounts, followed by saturation correction, and preferably locally.
- For dark animals in hard top-light, a subject-mask shadow lift within the Toons' range plus a little clarity gives shape without revealing artifacts; for irrecoverable contrast, black-and-white conversion (the C4 Photo Safaris suggestion) also hides colour noise and midday colour harshness - a good fit for high-ISO or harsh-light JPEGs.
- Heat-shimmered frames are best rejected at the cull stage unless they are the only record; when kept, use them small.

### Gaps
- Photography Life's Etosha article (likely the most on-point source for Etosha light/dust) was paywalled (HTTP 402).
- No sourced numeric dehaze range for wildlife, and no JPEG-specific dehaze guidance.
- No source specifically on AI "deblur/atmospheric turbulence" tools for wildlife as of late 2026 (a Topaz community thread exists as a feature request/discussion but was not read: [Topaz community](https://community.topazlabs.com/t/compensate-for-the-loss-of-sharpness-due-to-heat-convection-atmospheric-conditions/83202)).

---

## 7. Colour: realistic African fauna and dry-season landscape; golden hour vs midday; floodlit waterholes

### Takeaway
Keep the warmth the light actually had: do not neutralise golden-hour light with the eyedropper, do not paint golden warmth onto flat light, and prefer small vibrance moves (about +10) and subject-only colour over global saturation. Floodlit Etosha waterholes read very orange on auto white balance; RAW shooters correct it trivially, whereas JPEG shooters can only partially correct it.

### Cited Findings
- Steve and Ann Toon: avoid the White Balance eyedropper on nature images "since it can remove the warmth of the light"; warm animals shot in shadow gently with Temp; Tint never more than +/-10; a leopard example moved WB from 5700 to 6254 K; Vibrance usually no more than +10; Saturation used cautiously; for sunset silhouettes raise Temp slightly and add some vibrance. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two); [Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)
- Audubon/Groo: use Vibrance (affects less-saturated colours) rather than Saturation, which boosts everything and looks unnatural; the standard is edits that make the animal "more true to real life". [fetched] — [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)
- Nature TTL: oversaturated colours look "hot"; use vibrance first; the saturation slider is "not very subtle". [fetched] — [Nature TTL](https://www.naturettl.com/?p=5048)
- DPS: increasing contrast as a final step also raises saturation; saturate only the subject via HSL/brush. [fetched] — [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Fake-light warning: a listed mistake is "applying warm, golden-hour tones to a photo that was shot on a flat, overcast day". [snippet] — [Fstoppers: Five Editing Mistakes That Make Your Bird Photos Look Fake](https://fstoppers.com/education/five-editing-mistakes-make-your-bird-photos-look-fake-902559)
- Reality check for colour: "look out of the window at real life if in any doubt about colour accuracy". [snippet; source page not confirmed] — candidate: [Digital Camera World: 10 photo editing mistakes](https://digitalcameraworld.com/tutorials/10-photo-editing-mistakes-photographers-make-and-how-to-avoid-them)
- World Press Photo benchmark for colour honesty: "Changes in color may not result in significant changes in hue"; not permitted: "Changes in density, contrast, color and/or saturation levels that significantly alter content"; "Adjustments of color or conversion to grayscale that do not alter content are permitted". [fetched] — [World Press Photo: What counts as manipulation](https://www.worldpressphoto.org/contest/verification-process/what-counts-as-manipulation)
- Okaukuejo floodlights: a photographer reports "the camera's auto white balance gave very orange shots because of the warm colour temperature of the floodlights but this is easily correct[ed] in Lightroom if you shoot in RAW"; another guide: "The light is dim and usually orange-toned, so you might need to correct white balance later"; suggested ISO 1600-3200 with a telephoto; one photographer used ISO 3200 on a tripod with manual focus; a forum example shows an elephant at ISO 25,600, 1/13 s. Exact source pages for the first two quotes were not confirmed. [snippet] — candidates: [Morden-O'Hare blog: Namibia's Etosha National Park](https://morden-ohare.squarespace.com/blog/2014/7/11/namibias-etosha-national-park), [LocationScout: Waterhole at Okaukuejo Camp](https://www.locationscout.net/namibia/9425-waterhole-at-okaukuejo-camp-etosha-national-park), [Kevin Pepper: Wildlife in Namibia](https://kevin-pepper-yf9s.squarespace.com/wildlife-in-namibia); forum example: [Photography Life forum: Elephants at night, 25000 ISO](https://photographylife.com/forum/wildlife/elephants-at-night-25000-iso)
- Etosha camps with floodlit waterholes: Okaukuejo, Halali, Namutoni; Okaukuejo in winter has "a constant stream of animals drinking at night from zebras to elephants, black rhinos, lions and hyenas"; waterholes are ~50 m from the viewing area. [fetched] — [Kruger-2-Kalahari: Night photography](https://www.kruger-2-kalahari.com/night-photography.html); [DPS: Inside the rest camps](https://digital-photography-school.com/a-southern-african-photo-safari-with-a-difference-from-inside-the-rest-camps/)

### Inferences
- Golden hour vs midday for JPEG: the in-camera WB is baked in; shifts of a few hundred kelvin-equivalent (like the Toons' 5700 -> 6254) are safe, large shifts are not, because channels that clipped or were compressed cannot be rebalanced. Golden-hour frames: leave warm or warm slightly; never eyedropper to neutral. Midday frames: usually near-neutral already; if anything remove a slight blue/cyan or dust-yellow bias with small Temp/Tint moves.
- Avoiding oversaturated oranges/yellows: dry-season Namibia is dominated by yellow grass, ochre dust, tawny lions/springbok and red-orange dunes - all in the same hue band that vibrance/saturation and dehaze push hardest. Sources give only the general rule (vibrance <= ~+10, saturation cautiously; contrast raises saturation). The specific remedy - pulling orange/yellow saturation down a little in HSL after contrast/dehaze, and checking that pale grass has not turned "banana" yellow and lions "pumpkin" orange - is my inference. Skin-tone-like reference colours (lion fur, elephant grey, zebra white/black stripes) are useful neutrality checks: zebra whites should not be orange at midday; elephants in Etosha are legitimately pale/whitish from calcrete dust (general knowledge, unsourced here).
- Floodlit JPEGs: the orange cast is recorded as a heavy red-channel bias with a weak (noisy) blue channel. Cooling the white balance in post amplifies blue-channel noise and can band or go grey/green; full neutralisation is therefore usually not achievable from an 8-bit JPEG. Reasonable options (inference): (a) partial correction - move toward neutral only until the animals stop looking uniformly orange, keeping a warm night mood; (b) reduce orange/yellow saturation selectively instead of large WB shifts; (c) convert to black and white, which sidesteps the cast and hides chroma noise; (d) accept the documentary truth that the scene was lit orange.
- If the floodlights are low-pressure/high-pressure sodium, their spectrum is narrow and no white balance will restore full colour; if they have been replaced by LED, correction is easier. I found no source confirming which lamp type Etosha currently uses.
- "Mixed light" at the waterhole (floodlight + moonlight/twilight sky) gives orange subject and blue background; a global WB compromise or a background-masked slight desaturation is the usual approach - unsourced inference.

### Gaps
- No source giving the colour temperature, lamp type (sodium vs LED) or a tested WB preset for Etosha's floodlights.
- No expert, named-photographer tutorial on editing floodlit waterhole images was found, and none at all for JPEG sources.
- No named source giving HSL targets for African dry-season palettes or species-specific colour references.

---

## 8. Removing distractions (twigs, dust spots, bright patches)

### Takeaway
The broadly accepted hierarchy is: sensor dust spots - always fine; toning down bright patches by dodging/burning - fine; cropping distractions out - fine; cloning out real objects (twigs, grass, other animals) - forbidden under every documentary/competition standard checked, though common in commercial/personal work.

### Cited Findings
- WPY (adult rules, entries closing 3 Dec 2026): permitted - tone and contrast, burning, dodging, cropping, sharpening, noise reduction, and minor cleaning work (removal of chromatic aberration, lens distortion, vignetting; earlier wording also lists sensor-dust-type "minor cleaning work"); not permitted - "adding, moving or removing objects, animals or parts of animals, plants, people"; removing dirt, highlights, backscatter, bubbles or debris (except as allowed under the permitted list); composites; painting the foreground or background. [fetched] — [NHM WPY adult competition rules](https://www.nhm.ac.uk/visit/wpy/competition/adult-competition/rules.html)
- World Press Photo: "Cropping that removes extraneous details is permitted"; "Removing sensor dust or scratches on scans of negatives is permitted"; cloning not allowed in cases including "cloning in highlights". [fetched] — [World Press Photo](https://www.worldpressphoto.org/contest/verification-process/what-counts-as-manipulation)
- Audubon/Groo: don't add, remove or manipulate individual elements; airbrushing a branch out "takes about 30 seconds" but is alteration beyond standard optimisation; clone-stamping elements out counts. [fetched] — [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)
- Accepted alternative: Toons use a feathered brush "to dull distracting highlights such as bright rocks or branches" rather than removing them. [fetched] — [Australian Photography Part two](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-two)

### Inferences
- For a personal album, a workable honesty rule mapped from these standards: Tier 1 (always OK) - sensor dust spots, lens-flare specks, cropping, darkening/desaturating bright patches. Tier 2 (personal judgement; would disqualify in WPY/WPP/Audubon) - cloning out a stray twig or out-of-focus grass blade crossing the frame edge. Tier 3 (misrepresentation) - removing/adding animals, fences, vehicles, collars or ear tags, replacing skies, generative fill. If Tier 2 edits are made, noting it in the caption keeps the album honest.
- Note: airborne dust in Etosha is part of the scene (and often the charm); "dust spots" in the accepted sense means sensor dust only. Dehaze/contrast increases will make sensor dust more visible, especially in sky at small apertures - check after tonal edits.

### Gaps
- The precise current WPY wording on sensor dust within "minor cleaning work" was returned only in summary; the 2022 third-party listing had "minor cleaning work" as a separate permitted item. Verify on the rules page if exact wording matters.

---

## 9. Ethics and honesty standards (benchmarks)

### Takeaway
The standards agree on a simple line: you may optimise how the captured scene looks (tone, colour, crop, sharpen, denoise) but may not change what it contains (add/move/remove, composite, generative AI), and World Press Photo additionally bans AI upscaling and restricts AI denoise. That line is a ready-made benchmark for a documentary-honest family album.

### Cited Findings
- Wildlife Photographer of the Year (Natural History Museum), adult rules for the competition closing "Thursday 3 December 2026": adjustments must "comply with the Competition's principles of authenticity"; permitted - tone and contrast, burning, dodging, cropping, sharpening, noise reduction; HDR and stitched panoramas; stacking for focus, exposure blending, noise reduction or lengthened exposure when shot at the same location at about the same time; removal of chromatic aberration, lens distortion and vignetting; multiple in-camera exposures in the Natural Artistry category only. Not permitted - adding, moving or removing objects, animals or parts of animals, plants, people; removing dirt, highlights, backscatter, bubbles, debris; composites; painting foreground/background; AI-generated images and "any post-processing that adds new content through AI or manual intervention". No borders, watermarks or signatures. High-res file: "Please do not upscale." Entrants must supply originals to prove compliance or be withdrawn. [fetched] — [NHM WPY adult rules](https://www.nhm.ac.uk/visit/wpy/competition/adult-competition/rules.html); [NHM WPY enter the competition](https://nhm.ac.uk/wpy/competition/enter-the-competition)
- WPY field ethics: no captive, restrained or manipulated animals (except when reporting third-party mistreatment, with disclosure); no baiting/luring with food, scent or sound; no injuring or distressing animals, including artificial lighting that could distress or blind a subject. [fetched] — [NHM WPY adult rules](https://www.nhm.ac.uk/visit/wpy/competition/adult-competition/rules.html)
- World Press Photo: entries "must not be altered by adding, rearranging, reversing, distorting, or removing people or objects"; manipulation "is about altering the content of a photograph"; cropping of extraneous detail, sensor-dust removal, colour adjustment and greyscale conversion that do not alter content are permitted; colour changes "may not result in significant changes in hue"; "no use of artificially generative fill is allowed"; "all AI-powered enlarging tools" breach the rules; Denoise and automatic adjustments are "tools where limited usage may be allowed", with limits set by the organisation and jury. [fetched / entry-rule wording from snippet] — [World Press Photo: What counts as manipulation](https://www.worldpressphoto.org/contest/verification-process/what-counts-as-manipulation); [World Press Photo entry rules](https://www.worldpressphoto.org/contest/2025/entry-rules)
- Audubon Photography Awards ethos (Melissa Groo, 2015 Grand Prize winner and judge): judges want "an honest depiction of that exact moment in nature, just as it appeared when you pressed the shutter"; edits should affect the whole image, not individual elements; some contests require RAW files for verification. [fetched] — [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)

### Inferences
- Applied to a personal album: every technique in sections 1-7 (crop, tone, WB, masked dodging/burning, selective NR and sharpening, B&W conversion) sits inside the WPY-permitted list. Masked local adjustments are simply dodging and burning. The things to avoid or disclose: object removal, sky replacement, generative expand/fill, AI "detail recovery" that invents fur/feather texture, added catchlights, artificial background blur that changes the perceived scene (the last three are my extensions of the "adds new content" principle, not explicit rule text).
- AI denoise is in a grey zone at World Press Photo ("limited usage") but explicitly fine at WPY (noise reduction permitted); AI upscaling is rejected by both for submitted files. For family prints this is not binding, but it signals that upscaled detail is not regarded as photographic evidence.
- Caption honesty also matters in a documentary album: e.g. noting that waterhole animals were lit by camp floodlights, that an image is a heavy crop, or that it was converted to black and white.
- JPEG shooters have one disadvantage for verification: competitions requiring RAW originals (Audubon mention; WPY requests original files) - irrelevant to a family album but relevant if any image were ever entered.

### Gaps
- National Geographic: no current editing guideline text was retrieved (the Your Shot FAQ page appeared in results but its editing rules were not in the excerpt; one result suggests the Your Shot platform has been shut down - unverified). Do not cite Nat Geo rules from these notes.
- Nature's Best (Windland Smith Rice) and GDT (European Wildlife Photographer of the Year) rules were not retrieved.
- World Press Photo's position on dodging/burning and sharpening is not stated on the page read (only the general "does not significantly alter content" test); the 2026 Judging Procedures PDF was not read: [WPP 2026 Judging Procedures](https://www.worldpressphoto.org/getmedia/d229f86b-453b-4e78-ab2a-0ed3c294a4ed/2026-Contest-Judging-Procedures.pdf).

---

## 10. Common beginner mistakes and how to recognise them

### Takeaway
The same five or six errors recur across every source: cropping too tight, over-sharpening (halos, "crispy"), over-denoising (waxy), over-saturation ("hot" colours), excessive clarity/local contrast (plastic), and over-separation (the "sticker effect"). All are "too much of a legitimate tool", and all are easier to commit and quicker to show on JPEGs.

### Cited Findings
- Cropping too tight: subject fills the frame, no space ahead of head/movement; partial limb amputations; huge crops that magnify noise and softness. [fetched] — [Nature TTL](https://www.naturettl.com/?p=5048); [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid); [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)
- Over-sharpening: hair/feather edges unnaturally crisp, image "almost fake", noise appears, bright or dark halo around the subject against the background; "It's just as bad as having an unsharpened photo" (Groo). Recognise by zooming to edges against sky/plain background. [fetched] — [Nature TTL](https://www.naturettl.com/?p=5048); [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid); [Audubon](https://audubon.org/news/the-dos-and-donts-editing-bird-photos)
- Halo test: raise sharpening until a halo appears, then back off; halos come from over-sharpening or over-contrast - "if you see halos you've gone too far". [snippet; source pages not confirmed] — candidates: [Adorama: 5 Signs You've Over-Edited Your Photos](https://www.adorama.com/alc/overedited-photos/), [Digital Camera World](https://digitalcameraworld.com/tutorials/10-photo-editing-mistakes-photographers-make-and-how-to-avoid-them)
- Over-denoising: waxy / "wax-statue" texture, smeared fur or feathers, flattened edges, water losing texture. [fetched] — [Nature TTL](https://www.naturettl.com/?p=5048); [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid); [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)
- Oversaturation: "hot" colours; everything colourful so the background competes with the animal. [fetched] — [Nature TTL](https://www.naturettl.com/?p=5048); [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Excess clarity: feathers too crisp, foliage plastic. [fetched] — [DPS](https://digital-photography-school.com/5-unforgiving-post-processing-mistakes-every-bird-photographer-must-avoid)
- Over-separation: "sticker effect"; ghostly smeared backgrounds from negative texture/clarity. [fetched] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317)
- Fake light: golden-hour warmth applied to flat-light images. [snippet] — [Fstoppers: Five Editing Mistakes That Make Your Bird Photos Look Fake](https://fstoppers.com/education/five-editing-mistakes-make-your-bird-photos-look-fake-902559)
- Editing without a plan: "the problem is not the sliders, it is the lack of a plan"; decide the vision before touching sliders. [snippet] — [Fstoppers: Stop Guessing in Lightroom: A Clear Editing Plan for Wildlife Photos](https://fstoppers.com/animal/stop-guessing-lightroom-clear-editing-plan-wildlife-photos-900595)
- Self-check methods: view at 100% and at final viewing size; sleep on it; swap edits with peers/camera club to calibrate; make small adjustments at a time; calibrate the monitor. [fetched for Kloskowski; snippet for the last two] — [Fstoppers / Kloskowski](https://fstoppers.com/nature/what-separates-natural-wildlife-edit-overcooked-one-905317); [Nat Hab / WWF blog](https://www.nathab.com/blog/post-production-of-wildlife-images-getting-the-best-image-from-your-raw-file-using-lightroom)

### Inferences
- JPEG-specific beginner mistakes (not named in sources, derived from the JPEG constraints in sections 5-7): stacking new sharpening on in-camera sharpening; trying to rescue clipped highlights (grey patches) or blocked shadows (blotchy, banded); big white-balance swings (colour banding, green/magenta shadows); heavy dehaze; repeated open-edit-save cycles of the JPEG itself (generational loss) instead of non-destructive editing with a single final export; trying to "fix" heat shimmer with sharpening.
- A quick recognition checklist for the report: halos at subject edges; waxy fur; neon grass/orange lions; grey whites; glowing or cut-out subject; smeared background; cramped crop; visible JPEG blocks or banding in sky.
- A before/after toggle and comparison against an unedited neighbouring frame are the cheapest drift detectors (inference).

### Gaps
- No source specifically lists JPEG-editing mistakes in a wildlife context.

---

## 11. Batch workflow for thousands of frames: culling and syncing

### Takeaway
Cull in passes before editing anything: a fast reject pass, then a comparison pass within each sequence keeping the frame with the best eye sharpness, pose and expression; edit only the survivors, syncing global settings across frames shot in the same light and doing masks/crops per image. Sourcing here is thinner and more vendor-driven than for other sections.

### Cited Findings
- Steve and Ann Toon: back up to two devices before import; build 1:1 previews for reliable sharpness judgement; first pass in grid view deleting "obvious no-hopers"; second pass comparing similar images "for small differences, such as pricked ears or alert expressions"; they use a binary keep/reject rather than 1-5 stars - "an image is either good enough or it's not". [fetched] — [Australian Photography Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)
- Staged culling: flags on the first pass to remove rejects, star ratings only on the shortlist ("tiering a 400-image shortlist down to 80. Do not apply them while still looking at 2,000 images"); keep the first shortlist broad so a useful moment is not discarded too early; pixel-level evaluation belongs to the editing phase on already-selected keepers. Vendor/blog sources; exact URLs for each excerpt not confirmed. [snippet] — candidates: [Fstoppers: 5 Ways to Make Photo Culling Faster](https://fstoppers.com/post-production/5-ways-make-photo-culling-faster-without-regretting-your-picks-900135), [Blurb: Photo culling made easy](https://www.blurb.com/blog/culling-photos-lightroom-workflow/), [Narrative: How to cull photos in Lightroom](https://narrative.so/blog/how-to-cull-photos-in-lightroom)
- Kristi Odom (wildlife photographer, B&H Wildlife Conservation Series) culls large shoots in Photo Mechanic before a Lightroom Classic workflow. [snippet] — [B&H Explora: Kristi Odom Edits Her Wildlife Photos](https://www.bhphotovideo.com/explora/node/118706)
- Critical-sharpness check on the eye is the first gate (WWF/Nat Hab). [snippet] — [Nat Hab blog](https://www.nathab.com/blog/post-production-of-wildlife-images-getting-the-best-image-from-your-raw-file-using-lightroom)
- Audience consideration: near-identical lion/giraffe/hyena frames from a big safari bore viewers - prune near-duplicates aggressively. [snippet; source page not confirmed] — candidate: [David duChemin: Better Editing, Better Photographs](https://davidduchemin.com/2022/03/better-editing-better-photographs/)
- AI culling tools (Imagen, Narrative, etc.) write ratings to XMP that Lightroom can read - vendor claims, unverified. [snippet] — [Imagen: Lightroom assisted culling](https://imagen-ai.com/post/lightroom-assisted-culling/)
- The Toons note that some edits are consistently applied as a baseline (lens profile + chromatic aberration removal on every image), i.e. a natural import preset. [fetched] — [Australian Photography Part one](https://www.australianphotography.com/photo-tips/lightroom-tips-for-wildlife-photographers-part-one)

### Inferences
- Suggested batch flow for this trip (synthesis, partly unsourced): (1) back up; (2) pass 1 at fit-to-screen speed - reject out-of-focus, heat-shimmered, motion-blurred, clipped and duplicate frames; (3) pass 2 per burst/sequence at 100% on the eye - keep one or two; (4) pass 3 - rate for story value (species, behaviour, place) to reach an album-sized set, typically a few percent of the take; (5) group survivors by lighting situation (midday pan, golden hour, floodlit night, desert); (6) edit one representative frame per group and sync/copy global settings (WB, tone, baseline NR by ISO) to the rest; (7) do crop, masks, eyes and distraction work individually; (8) export once from the originals.
- What is safe to sync across a sequence: white balance, global tone, colour/HSL, noise reduction level (same ISO), lens corrections. What is not: crops, brush/radial masks (the animal moves), and anything exposure-dependent when auto-exposure varied frame to frame. AI subject masks generally must be recomputed per frame after syncing (general software behaviour; not sourced here and tool-dependent - the Luminar Neo researcher should confirm).
- For JPEGs, ISO-based noise presets (e.g. one for ISO 3200, one for 6400, one for 12800) and scene-based presets (floodlit night WB/colour treatment) are particularly efficient because the floodlit cast and noise character are consistent across a night session (inference).
- Heat-shimmer and deep-crop limits argue for culling on technical quality relative to intended crop: a frame that is sharp only at full-frame view may be rejected if the animal is tiny in it.

### Gaps
- No safari-specific, named-expert source on culling ratios or on syncing edits across wildlife sequences was retrieved; the sync guidance above is inference.
- No source on culling criteria for JPEG-only shooters.
