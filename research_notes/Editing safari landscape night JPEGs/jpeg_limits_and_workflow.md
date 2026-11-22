# Technical limits and best practices of editing out-of-camera JPEGs (Sony a6700, 8-bit sRGB), as of November 2026

Reading notes for the report writer:
- "Fetched" means I read the page itself. "Search snippet" means the claim comes from a search-result summary of that page and was not opened; treat it as lower confidence.
- Several widely repeated numbers in this field (stops of recovery, "quality 85 is visually lossless") turned out to rest on informal tests, not measurements. This is flagged where it applies.
- Pages that refused automated access and so could not be read: PetaPixel "How many megapixels", Adobe's JPEG Artifacts Removal help page, the Afifi et al. CVPR 2019 PDF.

## 1. Highlight and shadow recovery: 8-bit JPEG versus RAW

### Takeaway
No rigorous, multi-camera measurement in stops was found; the evidence is informal tests and rules of thumb. They agree on the shape: a JPEG has close to zero true highlight recovery (RAW holds roughly one extra stop), while shadows can be lifted about 2-3 stops before the result degrades, with RAW pulling clearly ahead from about 4 stops under.

### Cited Findings
- Informal test, 6 stops under to 3 stops over in 1-stop steps, corrected in Lightroom: "At 3-stops under, the corrected JPG still looks okay"; RAW's advantage for underexposure only becomes important at four stops or more. Fetched; camera not named, article dates from about 2006, so the sensor and JPEG engine are old. — [Photodoto](https://photodoto.com/raw-vs-jpg-correcting-underover-exposure)
- Same test, highlights: "RAW is apparently much better than JPG at recording highlight detail, even at just one stop over", and "The 3-under photo looks much better than the 3-over photo." — [Photodoto](https://photodoto.com/raw-vs-jpg-correcting-underover-exposure)
- Rule of thumb: a RAW file holds on to roughly one more stop (1 EV) of highlight detail than the in-camera JPEG. Search snippet; exact source page among the results not identified, likely Life after Photoshop or Amateur Photographer. — [Life after Photoshop, highlight recovery tag](https://lifeafterphotoshop.com/tag/highlight-recovery)
- Data clipped at the sensor cannot be recovered from RAW either; RAW only gives more latitude before that point. Search snippet, community Q&A. — [Unique Photo Q&A](https://www.uniquephoto.com/community/qa/why-can-raw-files-recover-some-blown-highlights-that-jpegs-cannot)
- Four-camera field test (Leica D-Lux 8, Lumix S1R II, Lumix G9 II, Nikon Z9; RAW+JPEG, in-camera NR medium, DRO medium, auto WB, exposed for the highlights), June 2026: only one of four scenes, a severely underexposed bird in flight, gave RAW a clear visible edge. The article gives no exposure offsets in stops. Fetched. — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- In that failing case the pushed JPEG showed colour distortion along the subject's edges that the RAW did not, less wing detail, and a noticeably dirtier result after noise reduction. — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- In the same test a heavily underexposed canyon scene (mostly in shadow) "recovered cleanly from the JPEG", and the presenter was "surprised by that outcome, having expected more separation across the board." — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- Contrary anecdote: a forum user found JPEG and RAW results at -2 EV surprisingly close. Search snippet, single anecdote. — [Pentax Forums](https://www.pentaxforums.com/forums/32-digital-processing-software-printing/379181-jpg-somehow-better-recovery-than-its-raw-version-post4516137.html)
- a6700 sensor (RAW behaviour, for contrast): it offers "a decent degree of latitude for reducing exposure to protect highlights then lift the shadows", but "shows still more noise if you try to lift the lower ISOs" than peers. Fetched. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)

### Inferences
- Practical planning figures for an a6700 JPEG: highlights, treat anything at 255 as gone, expect only tonal re-mapping of near-white values (a "recovery" slider darkens and re-contrasts what is below clipping; it does not restore detail). Shadows, +1 to +2 EV is generally safe, +3 EV is the edge of acceptable, beyond that expect noise, blotchy colour and banding. These are extrapolations from the informal tests above, not measurements on this camera.
- What clipping looks like in a JPEG: flat featureless white (or flat single-colour patches where only one or two channels hit 255, for example cyan-shifted sky or yellowed skin next to a blown area). Pulling it down gives uniform grey or a tinted flat patch with a hard edge, not texture. This is a reasoned description; no source in this research documented it with examples.
- The asymmetry (shadows more forgiving than highlights) matches the camera-side advice in the Fstoppers test: expose for the highlights when shooting JPEG.
- Night scenes are the worst case for shadow lifting: the darkest tones occupy very few of the 256 levels and already carry in-camera noise reduction, so lifting reveals smeared texture and quantisation steps together.

### Gaps
- No measured JPEG-versus-RAW dynamic range comparison in stops for the a6700 or any current camera was found. Photons to Photos publishes RAW-only data and was not consulted for JPEG.
- How much the a6700's own tone curve, Creative Look and DRO setting shift the usable JPEG highlight headroom is not quantified in any source found.

## 2. White balance correction in a JPEG

### Takeaway
White balance in a JPEG is limited because the camera applied it to linear sensor data and then applied non-linear, camera-specific rendering and 8-bit clipping on top; a later correction is an approximation that works for modest shifts and fails near clipped channels. No source gives a safe limit in kelvin.

### Cited Findings
- After the white-balance step the camera pipeline applies several non-linear, camera-specific operations, so a rendered image is no longer linearly related to sensor values. Search snippet of a York University paper. — [York University CVIL, colour temperature tuning](https://yorkucvil.github.io/projects/public_html/ColorTemperatureTuning/files/ColorTemperatureTuning.pdf)
- "Manipulating WB in the sRGB colour space is challenging, even when WB is applied in a linearised sRGB space." Search snippet of Afifi and Brown work. — [Deep White-Balance Editing, arXiv 2004.01354](https://arxiv.org/pdf/2004.01354)
- Afifi, Price, Cohen and Brown (CVPR 2019) state there were no effective solutions for correcting camera-rendered sRGB images with the wrong white balance despite decades of colour constancy research; they built a dataset of over 65,000 wrong/right image pairs to address it. Search snippet; PDF could not be fetched. — [Adobe Research publication page](https://research.adobe.com/publication/when-color-constancy-goes-wrong-correcting-improperly-white-balanced-images)
- Channel clipping: the maximum JPEG value is (255,255,255); scaling channels to rebalance either raises overall brightness or leaves highlights coloured, and lost highlights cannot be recovered. Search snippet of patent text. — [US patent 7057768](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7057768)
- Each channel saturates at a different level, and without knowing those points correct white balance near highlights is "particularly tricky"; RAW data records exactly when each channel clips and has extra headroom, which is why post-hoc correction works there. Search snippet of patent text. — [US patent 8890974](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8890974)
- Field evidence that moderate corrections work: a Nikon Z9 JPEG pushed blue by auto white balance "corrected well with a straightforward adjustment in Lightroom". Fetched. — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)

### Inferences
- Expected artefacts when a JPEG white-balance shift is large: (a) clipped highlights take on the complementary tint or stay stubbornly white while everything around them shifts; (b) shadows and midtones cannot be neutralised together, because the camera's tone curve and saturation were applied after the original balance, leaving a residual cast in the shadows; (c) the channel being multiplied up gets stretched, so its noise and 8-bit steps show first (typically blue when warming is removed from tungsten or sodium-lit night scenes).
- Small trims (a slight warm/cool or tint nudge of an image that was roughly right) are safe. Large corrections, such as a daylight setting under tungsten or mixed artificial light at night, are where a JPEG fails. The division between "small" and "large" is not quantified in any source found.
- For safari and landscape in daylight, auto white balance errors are usually modest and correctable; for night scenes, getting white balance right in camera matters much more.
- A neutral-picker correction on a mid-grey target is preferable to one on a near-white target, since near-white pixels may already be clipped in one channel.

### Gaps
- No source quantifies how far (in kelvin or mired) a JPEG white balance can be moved before artefacts become visible.
- The Afifi paper's error figures comparing a simple diagonal correction in sRGB with their method could not be retrieved.

## 3. Banding and posterization in skies and gradients

### Takeaway
Banding comes from stretching the 256 levels per channel so that gaps open between adjacent tones; smooth skies show it first. Prevention is small tonal moves made once in a 16-bit internal pipeline; the remedy for existing banding is fine noise or dither, optionally with local smoothing.

### Cited Findings
- "Any process which 'stretches' the histogram has the potential to cause posterization"; this includes Levels, Curves and colour-space conversions. Fetched. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- Stretching "creates gaps where there is no longer any intensity information left in the image"; example: a histogram spanning 120-130 stretched to 100-150 has values only at every fifth level. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- Diagnostic: comb-like spikes in the histogram; per-channel histograms are the most sensitive check, the combined RGB histogram shows only extreme cases. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- "Posterization occurs more easily in regions of gradual color transitions, such as smooth skies." — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- Editing an 8-bit source in 16-bit mode nearly eliminates posterization caused by rounding errors across successive edits; doing each manipulation once (adjustment layers) rather than repeatedly also helps. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- Broad-gamut colour spaces need more bit depth for the same gradient, so they raise posterization risk. — [Cambridge in Colour](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- JPEG quantisation is itself a cause of banding, independent of bit depth: DCT coefficients are divided by a constant and rounded. Fetched. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Heavy saturation, vibrance or dehaze can trigger banding. Search snippet. — [ExpertPhotography](https://expertphotography.com/color-banding)
- Remedy: add monochromatic, uniform noise on a masked layer covering only the banded area; under 5% suggested. Alternative: blur the sky on a masked layer or reduce texture/clarity there. Search snippet. — [ExpertPhotography](https://expertphotography.com/color-banding)
- Dither on output: darktable's dither module documents settings tuned to 8-bit output (a value of -80 suggested for 8-bit formats). Search snippet. — [darktable manual](https://docs.darktable.org/usermanual/5.6/en/module-reference/processing-modules/dither-or-posterize/)
- Photographs usually hide banding because natural noise breaks it up; Lightroom applies output dithering, Photoshop shows banding more often. Search snippet, forum users. — [Adobe Community](https://community.adobe.com/t5/photoshop-ecosystem-discussions/apparent-bit-depth-problem-and-bit-depth-change-bug/td-p/9408809)
- Histogram gaps under about three levels wide are unlikely to be visible in the image. Search snippet. — [Adorama, The Pitfall of Darkening a Sky](https://www.adorama.com/alc/the-pitfall-of-darkening-a-sky-part-1)
- Banding can come from the JPEG encoder at export, not the edit: a difficult sky gradient showed posterization at every Lightroom quality level, and one photographer reports quality 77 occasionally banding skies where 85 does not. First fetched, second search snippet. — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality); [Have Camera Will Travel](https://havecamerawilltravel.com/lightroom/exporting-jpegs-lightroom-quality-settings/)

### Inferences
- Converting an 8-bit JPEG to 16-bit adds no tonal information; the ExpertPhotography wording that it lets you "add more colour depth" is misleading. The real benefit is the Cambridge in Colour one: intermediate rounding stops accumulating.
- In-camera noise reduction removes the natural dither that would mask banding, so a6700 JPEGs of clean skies at low ISO and of dark night skies are more prone to it than a noisy RAW conversion would be. Adding fine grain back after tonal edits is therefore a legitimate fix, not a cosmetic trick.
- Highest-risk edits for a JPEG sky: darkening a bright sky (blue-luminance pulls, strong graduated filters), dehaze, strong local contrast, and large saturation pushes. Night skies are the extreme case because the gradient lives in very few low levels.
- Check banding at 100% on the exported file and on a second display, because some banding seen while editing is produced by the display or the preview pipeline.

### Gaps
- No measured threshold (how many levels of stretch produce visible banding at a given noise level) was found.
- Whether Luminar Neo processes internally at 16-bit or float and whether it dithers on 8-bit export is for the Luminar-specific researcher.

## 4. JPEG compression artefacts and how editing amplifies them

### Takeaway
JPEG errors are confined to 8×8 blocks (16×16 where chroma is subsampled) and chroma is stored at half resolution in each direction; any edit that raises local contrast or saturation makes these errors visible. Mitigation is restraint and masking, plus a high-quality in-camera setting.

### Cited Findings
- JPEG errors stay within 8×8 blocks, or 16×16 with chroma subsampling. Fetched. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- 4:2:0 subsampling halves chroma resolution in each direction, causing colour bleeding; RGB to YCbCr conversion and back alone reduces about 16.7 million possible colours to about 4 million, mostly affecting red and blue. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Quantisation is "the core of JPEG compression" and the main source of loss. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Sharpening can amplify JPEG compression artefacts; RAW and TIFF respond much better to sharpening than JPEG. Fetched. — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Contrast enhancement can unintentionally boost image artefacts, especially those from JPEG compression. Search snippet of an academic paper. — [arXiv 1601.01339](https://arxiv.org/pdf/1601.01339v1.pdf)
- Low-quality JPEGs showed halos beside fine high-contrast lines that vanished at the next quality level. Fetched. — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)
- Sony a6700 quality tiers are Extra fine, Fine, Standard, Light, with compression increasing and file size decreasing in that order. Fetched. — [Sony a6700 Help Guide, JPEG Quality/HEIF Quality](https://helpguide.sony.net/ilc/2320/v1/en/contents/0404M_jpeg_image_quality.html)
- Adobe ships a "JPEG Artifacts Removal" neural filter in Photoshop, described as restoring sharpness and removing compression imperfections. Search snippet; page could not be fetched. — [Adobe Help](https://helpx.adobe.com/photoshop/using/quick-actions/jpeg-artifacts-removal.html)

### Inferences
- How specific tools interact with these artefacts (reasoned, not sourced): clarity/structure/dehaze boost mid-frequency contrast, which is exactly the scale of block edges and of ringing ("mosquito noise") around high-contrast edges such as branches against sky; saturation and vibrance amplify chroma, which is the half-resolution, most heavily quantised part, producing colour fringes and blotches at saturated edges (red and blue most); shadow lifting exposes the coarser quantisation used in dark, low-detail areas.
- Mitigation order of preference: shoot Extra fine; keep global clarity/dehaze/structure moderate and apply them through masks that exclude sky and smooth areas; raise saturation less than you would on RAW and prefer vibrance or targeted colour edits; view at 100% after each strong local-contrast move; if blocks appear, back the slider off instead of trying to denoise them away.
- Camera JPEGs at Extra fine are lightly compressed, so on a6700 files blocking is normally invisible until edits are strong. Artefacts from baked-in noise reduction and sharpening will usually show before compression blocks do.

### Gaps
- Sony does not publish the chroma subsampling or quantisation tables used for a6700 JPEGs at each quality tier; whether Extra fine is 4:2:2 or 4:2:0 is unconfirmed here. It can be read from a sample file with exiftool or ImageMagick `identify -verbose`.
- No controlled test was found that measures how much clarity or dehaze a given JPEG quality tolerates.

## 5. Baked-in camera processing: noise reduction, sharpening, Creative Look

### Takeaway
The a6700 JPEG has already had capture sharpening (described by DPReview as bordering on aggressive at base ISO) and noise reduction applied, so post-processing should skip a second capture-sharpening pass, denoise lightly and before any sharpening, and reserve sharpening for selective creative use and for output.

### Cited Findings
- "Base ISO JPEG sharpening is also decent though boarding on aggressive; we actually prefer the a6600's approach." Fetched. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)
- At high ISO the a6700 JPEG engine is better than its predecessor at "balancing noise reduction with detail retention, but not quite as good as the X-T5"; in low-contrast detail the X-T5 and a6600 retain more. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)
- "Most cameras automatically apply capture sharpening for JPEG photos." Fetched. — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Three-stage model: capture sharpening (offsets source blur), creative sharpening (selective, for example foliage or eyes but not sky or skin), output sharpening (tailored to medium, "applied at the very end of the image editing workflow"). — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- "Noise reduction should always be performed before sharpening." — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Screen output: for downsized web/email images a radius of 0.2-0.3 px at 200-400% "works almost universally well"; watch for aliasing/moire. — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Print output: assume viewing distance roughly equal to the print diagonal; larger viewing distance needs a larger radius; matte and canvas need more than glossy; "effective output sharpening often makes an on-screen image look harsh or brittle." — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Light halos are more objectionable than dark ones; threshold or masking keeps sharpening off smooth, noisy areas; sharpening is irreversible, so keep the unsharpened original. — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Camera controls that set how much is baked in: High ISO NR has Normal, Low, Off (fixed to Normal in Intelligent Auto and Scene Selection). Fetched. — [Sony a6700 Help Guide, High ISO NR](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414C_high_iso_nr.html)
- Creative Look parameters: Contrast, Highlights, Shadows, Saturation -9 to +9; Fade 0-9; Sharpness 0-9; Sharpness Range 1-5; Clarity 0-9. NT lowers saturation and sharpness and is described as suited to material that will be edited on a computer; VV raises saturation and contrast. Fetched. — [Sony a6700 Help Guide, Creative Look](https://helpguide.sony.net/ilc/2320/v1/en/contents/0411B_creative_look.html)
- Over-applied noise reduction or sharpening reduces quality instead of improving it. Search snippet. — [Shutterstock contributor help](https://submit.shutterstock.com/help/en/articles/10617487-what-does-overuse-of-noise-reduction-and-sharpening-look-like)

### Inferences
- Is extra sharpening advisable? At 100% on a low-ISO a6700 JPEG, generally no global sharpening; the DPReview observation implies halos are already near the limit. Use selective sharpening only where needed (eyes, fur, foreground texture) and output sharpening after resizing. Sharpening on top of existing halos widens and brightens them.
- Noise reduction in post on a camera-denoised JPEG has less to work with: the fine luminance grain is gone and what remains is low-frequency blotching plus smeared detail. Light chroma denoise is usually harmless; strong luminance denoise produces a plastic look quickly. Smeared detail cannot be restored by sharpening; sharpening it produces a crisp-edged, texture-less "watercolour" look.
- A night JPEG at high ISO with High ISO NR Normal is the hardest case; nothing in post restores detail the camera removed. This is the strongest argument for changing camera settings (see section 8).
- Creative Look contrast and saturation are baked in before the 8-bit encode, so a punchy look (VV, VV2, FL) uses up highlight and shadow room and saturates channels that cannot be unsaturated cleanly later. A flatter look leaves more room.
- For phone sharing, most output sharpening is done after downsizing by the export step; for a 30×45 cm print, sharpen at final pixel dimensions and judge at 50% zoom or by a test print, since correct print sharpening looks overdone on screen (Cambridge in Colour point above).

### Gaps
- Sony does not document the default Sharpness, Sharpness Range or Clarity values per Creative Look, nor the sharpening radius used. The a6700's displayed defaults should be read off the camera.
- No independent test was found of the a6700's High ISO NR Low/Off settings on JPEG detail.

## 6. Recommended order of operations and which adjustments are safest

### Takeaway
No source gives a JPEG-specific order backed by tests; the sourced rules are noise reduction before sharpening, output sharpening last, minimise and do not repeat histogram stretches, and export once. The order below is assembled from those rules.

### Cited Findings
- Noise reduction before sharpening; output sharpening at the very end, after resizing. Fetched. — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- Keep histogram manipulation to a minimum and avoid repeating the same manipulation; work in 16-bit even from an 8-bit source. Fetched. — [Cambridge in Colour, posterization](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- Lossless 90-degree rotation and cropping of a JPEG are possible (jpegtran); for edits that change most pixels, re-encode once at high quality. Fetched. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Community consensus also puts denoise early and sharpening last. Search snippet, user-generated. — [Unique Photo Q&A](https://www.uniquephoto.com/community/qa/should-noise-reduction-be-applied-before-sharpening)

### Inferences
- Suggested order for an a6700 JPEG (in a non-destructive editor the engine fixes its own internal order, so this is the order of decisions, and it matters most for strength, not sequence):
  1. Geometry: crop, straighten, lens corrections if not already applied in camera.
  2. White balance trim (small).
  3. Global exposure and tone: exposure, then highlights/shadows, then black and white points; one gentle curve instead of several stacked ones.
  4. Noise and artefact reduction, light, chroma first.
  5. Local adjustments through masks (sky, subject, foreground).
  6. Colour: vibrance or targeted hue/saturation/luminance, modest amounts.
  7. Local contrast (clarity/structure/dehaze), sparingly, masked off skies.
  8. Selective creative sharpening if needed.
  9. Grain or dither if gradients are at risk.
  10. Resize, output sharpening, single export.
- Safest adjustments on a JPEG: crop and rotate; small exposure changes (about ±0.5 to 1 EV); modest contrast; darkening shadows; mild vibrance; vignettes; black-and-white conversion (hides chroma artefacts); adding grain.
- Most destructive: highlight "recovery" of clipped areas; shadow lifts beyond about 2 EV; large white-balance shifts; dehaze and strong clarity on skies; strong blue-luminance darkening; heavy saturation; aggressive sharpening; strong luminance denoise; repeated export/re-import cycles.

### Gaps
- No controlled comparison of different operation orders on JPEG input was found; the sequence is convention plus the two sourced rules.

## 7. Generation loss, non-destructive editing, export quality, intermediates

### Takeaway
Each re-encode adds loss and the number of generations matters more than the quality setting, so edit non-destructively from the camera original and export once. "Visually lossless" has no measured threshold in the sources found; informal tests put it around quality 77-85 on Adobe's scale, with difficult sky gradients as the exception, and quality scales are not comparable between applications.

### Cited Findings
- "Every additional JPEG encoding will introduce additional loss"; the generation count matters more than the quality setting: saving at 85 and then re-saving at 90 is worse than a single save at 80. Fetched. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Worked example: maximum error 30 at quality 70 alone, 15 at quality 80 alone, 45 for quality 70 followed by 80. Re-saving at higher quality than the source is "always a bad idea" (bigger file, more loss). — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Chroma subsampling loss accumulates across generations even at quality 100. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Keep originals and intermediates in lossless formats and save as JPEG only the final version. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Social and messaging platforms re-encode uploads, adding a generation outside the photographer's control. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Newer formats (WebP, BPG) degrade faster over generations than JPEG because their errors are not confined to fixed blocks. — [Cloudinary, Jon Sneyers](https://cloudinary.com/blog/why_jpeg_is_like_a_photocopier)
- Lightroom's 0-100 slider yields only 13 distinct outputs; bands include 70-76, 77-84, 85-92, 93-100, so 93 equals 100. Lightroom "Quality 0" is roughly comparable to quality 50 in many non-Adobe apps; scales do not transfer between applications. Fetched; 2010, and the author noted in 2019 that Adobe later changed its encoder. — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)
- The 70-76 band looked about as good as the top band in most samples at about one third the file size; the exception was a sky gradient. — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)
- Reported sizes for one image: 12.9 MB in the 77-84 band, 17.6 MB in 85-92, 27.3 MB in 93-100; differences between 85 and 93 "pretty much impossible to spot". Search snippet. — [Photography Life](https://photographylife.com/jpeg-compression-levels-in-photoshop-and-lightroom)
- Commonly recommended single-export range is about 85-92; above that is described as wasted space. Search snippet, opinion. — [Uploadcare](https://uploadcare.com/blog/jpeg-quality-loss)
- Uncompressed 16-bit TIFF was more than 50 times the size of the smallest JPEG in Friedl's detail-rich sample. — [Jeffrey Friedl](https://regex.info/blog/lightroom-goodies/jpeg-quality)

### Inferences
- With a non-destructive editor the camera JPEG is decoded once and the export is the second generation; that is the minimum possible and is harmless at high quality. Never overwrite or re-save the camera original.
- Export settings by purpose: phone and messaging, resize to roughly 2048-3000 px on the long edge at a quality around 80-85, because the app will recompress anyway; print up to 30×45 cm, full resolution at quality 90-95, or a TIFF if the lab accepts it; choose a higher quality when the image has a smooth sky gradient.
- A 16-bit TIFF intermediate is worth it only when the image must pass through a second application (denoise or upscale plug-in, or a print-preparation step). It prevents an extra 8-bit JPEG generation but adds no information beyond what the JPEG had. For a single-application workflow it is unnecessary.
- "Quality 100" on any scale is still lossy and typically two to three times the size of quality 85-90 for no visible gain.

### Gaps
- No perceptual study (for example SSIM or blind viewing thresholds) establishing a "visually lossless" quality number was found; all evidence is informal side-by-side viewing.
- Luminar Neo's quality scale and its mapping to other encoders is not covered here.
- How WhatsApp, iMessage, Signal or Telegram currently resize and recompress images was not verified in this research.

## 8. Colour space, the Display P3 Mac workflow, and a6700 settings for more editable files

### Takeaway
Keep sRGB JPEGs in sRGB through to export: converting an 8-bit sRGB file to a wider space adds no colour and raises banding risk, and sRGB is the safe target for phones and labs. The settings with the largest effect on editability are made in camera: Extra fine quality, a flatter Creative Look with lower sharpness, restrained DRO, lower High ISO NR, or HEIF 10-bit (and RAW+JPEG as the real fix).

### Cited Findings
- a6700 Color Space options: sRGB ("the standard color space of the digital camera") and AdobeRGB (wider reproduction range, intended for colour-managed applications and printers; file names begin with "_"; images look low-saturation on devices that do not support it). Fetched. — [Sony a6700 Help Guide, Color Space](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414_color_space.html)
- The Color Space setting is ignored for HEIF: HEIF is recorded in sRGB with HLG Still Image off, and in BT.2100 (BT.2020 gamut) with it on. — [Sony a6700 Help Guide, Color Space](https://helpguide.sony.net/ilc/2320/v1/en/contents/0414_color_space.html)
- JPEG/HEIF Switch options: JPEG ("priority to compatibility"), HEIF 4:2:0 ("priority to image quality and compression efficiency"), HEIF 4:2:2 ("priority to image quality"); "Depending on the computer or software, you may not be able to view or edit HEIF files." Fetched. — [Sony a6700 Help Guide, JPEG/HEIF Switch](https://helpguide.sony.net/ilc/2320/v1/en/contents/201h_jpeg_heif_switch.html)
- Sony states HEIF records "a rich 10-bit color depth gradation expression" (helpful for skies), that HEIF compression efficiency is "about twice higher than that of JPEG", and recommends converting HEIF to 16-bit TIFF for editing and to 8-bit JPEG for general playback. Fetched; page is written for the ILCE-1, not the a6700. — [Sony support, HEIF](https://support.d-imaging.sony.co.jp/support/ilc/heif/02/en/index.html)
- 10-bit gives 1,024 levels per channel against 256; HEIF files are roughly 40-50% smaller at equivalent visual quality; "meaningfully more headroom for adjustments before artifacts appear" but short of RAW; print labs "almost universally require JPEG or TIFF"; verdict "The format is better. The ecosystem isn't ready." No tests in the article. Reader comments (unverified) report Capture One supporting 8-bit but not 10-bit HEIF. Fetched, March 2026. — [Fstoppers](https://fstoppers.com/gear/heif-vs-jpeg-should-switch-your-cameras-default-file-format-900251)
- The a6700 can shoot 10-bit HLG stills in HEIF. Fetched. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)
- Forum report on a Sony A7R V: HEIF gave better midtones and highlights and avoided sky banding, but shadows went featureless earlier, and DRO tuned for JPEG did not carry over well. Search snippet, anecdote. — [DPReview forum](https://www.dpreview.com/forums/threads/a7rv-heif-vs-jpeg.4714248)
- DRO: analyses the image by small areas and adjusts brightness and gradation; Off, Auto, Lv1 (weak) to Lv5 (strong); "When shooting with [D-Range Optimizer], the image may be noisy"; fixed to Auto in most Scene Selection modes and Off in Sunset, Night Scene and Night Portrait. Fetched. — [Sony a6700 Help Guide, D-Range Optimizer](https://helpguide.sony.net/ilc/2320/v1/en/contents/0409B_d_range_optimizer.html)
- Creative Look NT reduces saturation and sharpness and is described as suited to images that will be edited on a computer; all looks expose Contrast, Highlights, Shadows, Saturation, Sharpness, Sharpness Range and Clarity. Fetched. — [Sony a6700 Help Guide, Creative Look](https://helpguide.sony.net/ilc/2320/v1/en/contents/0411B_creative_look.html)
- Wide-gamut spaces need more bit depth for the same gradient (higher posterization risk in 8-bit), and colour-space conversion is itself a histogram-stretching operation. Fetched. — [Cambridge in Colour, posterization](https://cdn.cambridgeincolour.com/tutorials/posterization.htm)
- An application that ignores the embedded profile treats the file as sRGB, so wide-gamut files look desaturated there; most web and social images are sRGB. Search snippets, forum and PetaPixel. — [Fred Miranda forum](https://www.fredmiranda.com/forum/topic/1937008/1/); [PetaPixel](https://petapixel.com/2024/04/11/color-gamut-in-smartphones-what-you-should-know)

### Inferences
- On a Display P3 Mac, macOS colour management maps a tagged sRGB JPEG correctly onto the wider panel; nothing needs converting. Export in sRGB with the profile embedded. Exporting an sRGB-origin image as Display P3 gains nothing unless the edit deliberately pushed saturation beyond sRGB, and risks dull colour in viewers that ignore profiles.
- AdobeRGB in-camera JPEG is not recommended for this use: 8 bits spread over a wider gamut gives coarser steps, and the files must be converted to sRGB for phones anyway. It only pays for colour-managed printing of very saturated greens and cyans.
- Camera-side recipe for more editable JPEGs (reasoned from the Sony documentation, not tested): Extra fine; Creative Look ST or NT with Contrast reduced a few steps, Saturation at or slightly below default, Sharpness reduced, Clarity 0; High ISO NR Low; DRO Off or Lv1-Lv2 when planning to edit (DRO lifts shadows before the 8-bit encode, which preserves shadow tones better than lifting afterwards, but adds noise and can leave a flat, halo-prone base); expose to protect highlights; set white balance deliberately at night.
- An in-camera shadow lift (DRO, or Creative Look Shadows +) is done on the camera's high-bit data before quantisation, so if a scene will need lifted shadows it is technically better done in camera than on the JPEG. This follows from the bit-depth arguments above and is not directly tested by any source found.
- HEIF 4:2:2 10-bit is the better straight-out-of-camera format on paper (four times the tonal levels, better chroma resolution), but it depends on the editor reading 10-bit Sony HEIF properly; otherwise conversion through Sony Imaging Edge Desktop to 16-bit TIFF is needed, which costs convenience. RAW+JPEG remains the more robust answer for scenes known to be difficult (night, strong backlight).

### Gaps
- No controlled Sony HEIF-versus-JPEG editing latitude test was found; the claimed advantage rests on bit-depth reasoning, vendor statements and forum anecdote.
- Whether Luminar Neo opens Sony 10-bit 4:2:2 HEIF at full bit depth on macOS was not checked (Luminar researcher's scope).
- How individual messaging apps handle embedded colour profiles could not be verified.
- No source measured how each DRO level changes highlight or shadow headroom in the a6700 JPEG.

## 9. AI tools that extend JPEG latitude (denoise, upscaling, artefact removal)

### Takeaway
Independent testing of AI tools on JPEG input, as opposed to RAW, is thin: most published comparisons use RAW, and the strongest RAW denoisers do not accept JPEG at all. On JPEGs, AI tools can clean blocking and grain and upscale convincingly at modest factors, but they cannot restore clipped or smeared detail and may invent texture.

### Cited Findings
- Topaz tools accept JPEG and TIFF as well as RAW, unlike DxO PureRAW and Lightroom's Denoise at the time of the review, which were RAW-only. Search snippet. — [Finding the Universe](https://www.findingtheuniverse.com/best-noise-reduction-software)
- Topaz's former "JPEG to RAW AI" used machine learning to reduce compression artefacts and improve apparent detail, but could not recreate a real RAW file; the product is discontinued. Search snippet. — [ExpertPhotography](https://expertphotography.com/topaz-jpeg-to-raw-ai-review)
- A recent comparison video pits Lightroom Classic, DxO PureRAW 5, Luminar Neo, ON1 Photo RAW 2026 and Topaz Photo AI against one image; the snippet does not indicate JPEG input. Search snippet. — [Fstoppers](https://fstoppers.com/reviews/who-makes-best-noise-reduction-software-722527)
- In the 2026 four-camera test, after pushing and denoising a severely underexposed frame the RAW gave a "noticeably cleaner result" than the JPEG. Fetched. — [Fstoppers](https://fstoppers.com/education/raw-vs-jpeg-grand-canyon-what-four-cameras-actually-showed-903184)
- Upscaling test by a competitor (LetsEnhance): Gigapixel cleaned JPEG artefacts and grain but left the image soft, and pushed hard produced a lightly "painted" look and over-bright eye highlights. Search snippet; source has a commercial interest. — [LetsEnhance](https://letsenhance.io/blog/all/lets-enhance-vs/amp/)
- Topaz forum users report that JPEGs with existing compression artefacts can produce artefacts in AI enlargement; a 2025 thread documents artefact cases. Search snippet, anecdotal. — [Topaz community](https://community.topazlabs.com/t/reported-core-model-artifact-cases/86980)
- Results vary at extreme upscaling factors (400% and above). Search snippet. — [Chase Jarvis](https://chasejarvis.com/blog/topaz-ai-image-upscaler/)
- Adobe Photoshop includes a JPEG Artifacts Removal neural filter. Search snippet; page not fetched. — [Adobe Help](https://helpx.adobe.com/photoshop/using/quick-actions/jpeg-artifacts-removal.html)
- PetaPixel published "6 Best Image Upscalers Tested: Photo Upscaling Without the Plastic Look" in August 2026; it appeared in results but was not read. — [PetaPixel](https://petapixel.com/2026/08/6-best-image-upscalers-tested/)

### Inferences
- RAW-based AI denoisers work on linear, un-demosaiced data with a known noise model; a camera JPEG has had demosaicing, noise reduction, sharpening, a tone curve and compression applied, so an AI denoiser sees correlated, already-filtered noise. Expect smaller gains and more plasticky results than the RAW comparisons in reviews suggest. This is reasoning from the pipeline, not a tested result.
- Sensible use on a6700 JPEGs: low strength, with any built-in sharpening in the AI tool turned down; run it before tonal and colour edits where the software allows; inspect faces, fur, feathers and foliage at 100% for invented texture.
- Upscaling is not needed for 30×45 cm from an uncropped 26 MP frame (see section 10). It becomes relevant for heavy crops, typical of safari subjects; 2× is the conservative range, and artefacts from the source are amplified along with detail.
- AI tools do not extend highlight or white-balance latitude; they address noise, resolution and compression artefacts only.

### Gaps
- No independent, controlled test of AI denoise on camera JPEG versus RAW from the same exposure was found, and none on Sony a6700 files.
- The Topaz product line has been renamed and moved to subscription; current product names, pricing and JPEG support were not verified against primary sources.
- Luminar Neo's own AI tools (Noiseless, Upscale, and similar) on JPEG input are for the Luminar researcher.

## 10. Resolution for print

### Takeaway
An uncropped a6700 frame (6192×4128) prints 30×45 cm at about 349 ppi, above the 300 ppi standard, so resolution is not the limit for the target print size; a crop down to about 12 MP still meets 240 ppi.

### Cited Findings
- Common print guidance: 180 ppi minimum for reasonable quality, 240 ppi better, 300 ppi best. Search snippet; originating page among the results not pinned down. — [Adorama, Pixels and Printing](https://www.adorama.com/alc/pixels-and-printing-size-matters)
- Prints are assumed to be viewed at a distance roughly equal to the print diagonal. Fetched. — [Cambridge in Colour, sharpening](https://cdn.cambridgeincolour.com/tutorials/image-sharpening.htm)
- An alternative convention uses 1.5 to 2 times the diagonal, with required ppi derived from visual acuity as 3438 divided by viewing distance in inches. Search snippet; source page not confirmed (PetaPixel's megapixel article was among the results but could not be fetched). — [PetaPixel](https://petapixel.com/how-many-megapixels/)
- The L image size is unavailable when shooting in APS-C crop mode on Sony bodies. Search snippet of Sony help guides, relevant mainly to full-frame bodies. — [Sony Help Guide, image size](https://helpguide.sony.net/ilc/2230/v1/en/contents/TP0003057051.html)

### Inferences
- Arithmetic (mine, from the stated pixel dimensions; 1 inch = 2.54 cm):

| Print size (cm) | Inches | Pixels at 240 ppi | Pixels at 300 ppi | a6700 full frame gives |
|---|---|---|---|---|
| 10×15 | 3.94×5.91 | 945×1417 (1.3 MP) | 1181×1772 (2.1 MP) | about 1048 ppi |
| 13×18 | 5.12×7.09 | 1228×1701 (2.1 MP) | 1535×2126 (3.3 MP) | about 806 ppi (short side, after cropping to 13:18) |
| 20×30 | 7.87×11.81 | 1890×2835 (5.4 MP) | 2362×3543 (8.4 MP) | about 524 ppi |
| 30×45 | 11.81×17.72 | 2835×4252 (12.1 MP) | 3543×5315 (18.8 MP) | about 349 ppi |
| 40×60 | 15.75×23.62 | 3780×5669 (21.4 MP) | 4724×7087 (33.5 MP) | about 262 ppi |

- 30×45 cm is 2:3, the sensor's native ratio, so no cropping is forced. The frame can lose about 14% of its linear dimensions (to roughly 5315×3543) and still reach 300 ppi, or about 31% (to roughly 4252×2835) and still reach 240 ppi.
- Viewing-distance argument: a 30×45 cm print has a 54 cm diagonal. Using one arcminute of acuity (ppi = 3438 / distance in inches), viewing at the diagonal (21.3 in) needs about 160 ppi, and at 1.5-2 diagonals about 80-110 ppi. On that basis a crop to roughly 2900×1900 px (5.4 MP) is acceptable on a wall, though it will not survive close inspection.
- For JPEGs the practical print limit is therefore artefacts, not pixels: baked-in sharpening halos, noise-reduction smearing and any banding are enlarged with the image and are easier to see in a 30×45 cm print than on a phone. Evaluate at 100% before ordering.
- Phones show at most a few megapixels, which hides most JPEG editing damage; edits that look fine on a phone can fail in print.

### Gaps
- The megapixel/viewing-distance source could not be read directly, so the acuity formula is given as standard geometry, not as a confirmed quotation.
- Print-lab specifics (accepted colour profile, whether the lab resamples or sharpens) were not researched.
