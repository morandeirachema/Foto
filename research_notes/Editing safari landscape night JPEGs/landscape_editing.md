# Landscape post-processing workflow for 8-bit JPEG sources (Sony a6700, Namibia) — research notes, November 2026

**Reliability note for the report writer (read first).**
- Evidence tags used below: **[fetched]** = I read the page content; **[snippet]** = the claim comes from a search-engine summary of the linked page and was not verified by opening the page (attribution to the specific URL is my best match and may be imprecise).
- Several of the suggested primary sources could not be read: Photography Life (HTTP 402), Cambridge in Colour (HTTP 403), PetaPixel's dodging/burning and "5 mistakes" articles (HTTP 403), two DIY Photography pages (body truncated). I found **no fetched material from Mads Peter Iversen, Nigel Danson, Michael Frye, Alex Nail, Nature TTL, Capture Landscapes, On Landscape or Outdoor Photographer**. Named-photographer coverage is therefore limited to William Patino, Christian Möhrle, Rick Ohnsman, Chris M. Williams, Elliot Hook, Kevin Raposo, Greg Benz and the NLPA rules.
- Almost every source assumes RAW. Nothing I found gives a JPEG-specific landscape workflow or desert/Namibia-specific editing advice. The JPEG and desert adaptations are in the "Inferences" subsections and are my reasoning, not sourced fact.
- Numeric ranges are rules of thumb from tutorials (mostly Lightroom scale), not controlled tests.

---

## 1. Consensus editing order for landscapes

### Takeaway
There is no single canonical order, but sources converge on the same shape: geometry/lens corrections and crop first, then global tone, then colour/white balance, then local adjustments (sky/foreground, dodge and burn), with noise reduction and sharpening last and sized to the output. Two named variants: William Patino's "Light, Colour, Local" and Rick Ohnsman's lens-corrections-then-Basic-panel sequence.

### Cited Findings
- William Patino's "LCL" method: (1) **Light** — exposure, recover highlights, open shadows, check the histogram before moving on; (2) **Colour** — profile, saturation, vibrance, white balance; (3) **Local** — soft-edged brushes on specific areas. He prefers vibrance to saturation and advises letting edits "marinate" and returning after a break. [fetched] — [Fstoppers, Alex Cooke on William Patino](https://fstoppers.com/landscapes/simple-workflow-better-landscape-photo-edits-679023)
- Rick Ohnsman's order (Lightroom Classic): lens corrections first (profile corrections + remove chromatic aberration, ideally on import); then clipping indicators on, reduce Highlights until highlight clipping disappears, raise Shadows, set Whites and Blacks, then Exposure to taste without new clipping, then Contrast, then white balance; then graduated/linear gradients and sky masks; then dodge and burn; sharpen according to the intended output (screen or print). He says not to get "too hung up" on a perfect white balance because it is largely mood and preference. [fetched] — [Digital Photography School, Rick Ohnsman](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- Christian Möhrle (The Phlog Photography) puts two things early: choose the profile first because it sets baseline saturation, and apply noise reduction early, before heavy colour pushes make grain and speckling harder to manage. [fetched] — [Fstoppers, Alex Cooke on Christian Möhrle](https://fstoppers.com/lightroom/vibrance-vs-saturation-mistake-makes-sunsets-look-fake-719262)
- REI's guide says the steps you choose should be done in the order listed, though not every step is needed on every image. [snippet] — [REI Expert Advice](https://www.rei.com/learn/expert-advice/photo-editing-basics.html)
- Cropping early changes the later steps (the histogram and the balance of the frame change), and a vision for the image should be settled before adjusting. [snippet] — [Digital Photography School](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- Sharpening and noise come near the end because other adjustments change how noise and sharpness appear. [snippet] — [Zoner Learn](https://learn.zoner.com/how-to-edit-landscape-photos-step-by-step/)
- Alan Ranger describes a fixed seven-stage sequence from import to export, used in the same order every time. [snippet] — [Alan Ranger](https://www.alanranger.com/blog-on-photography/uk-photography-editing-workflow-guide)

### Inferences
- A workable synthesized order for these JPEGs: (1) cull, work on a copy; (2) level horizon, crop, any residual geometry; (3) dust-spot check; (4) global tone (highlights/shadows/whites/blacks, modest); (5) white balance and global colour (small moves only); (6) local tone: sky vs. foreground; (7) per-colour (HSL) refinements; (8) presence tools (dehaze/clarity/texture), preferably masked; (9) dodge and burn, vignette, optional glow; (10) noise reduction and sharpening; (11) export sized and sharpened for the output.
- Sources disagree on where noise reduction goes (Möhrle: early; Zoner: late). For an in-camera JPEG, noise reduction and sharpening have already been applied by the camera, so both should be light in either position.
- "Choose the profile first" (Möhrle) has no JPEG equivalent: the camera's Creative Look already baked the profile, contrast and saturation in. The starting point is therefore already "finished", which is why every later step needs smaller moves than RAW tutorials show.

### Gaps
- No fetched workflow from Iversen, Danson, Frye, Nail or Photography Life, so I cannot cite their specific orders.
- No source found that gives an editing order written specifically for JPEG originals.

---

## 2. High-contrast scenes from a single JPEG: balancing sky and foreground, limits, halos

### Takeaway
The standard tools are a linear gradient or AI sky mask refined by luminance range, with the land treated by the inverse mask; halos appear at hard horizon edges when the mask or the adjustment is too strong or too precise. From a JPEG the realistic limit is set by 8-bit data: clipped highlights are gone and lifted shadows band and show noise far sooner than RAW tutorials suggest.

### Cited Findings
- Adobe: pulling shadows up or highlights down on a JPEG can produce banding or posterization because of the limited tonal and colour range of 8-bit files; RAW files are 12–16 bit. [snippet] — [Adobe, RAW vs JPEG](https://www.adobe.com/creativecloud/photography/discover/raw-vs-jpeg.html)
- 8-bit = 256 levels per channel (about 16.7 million colours) versus 16,384 levels for 14-bit. Banding appears when a file is stretched: lifting shadows, recovering highlights, strong S-curves, large exposure corrections or aggressive colour grading. Smooth gradients such as skies are most vulnerable. Lost precision cannot be restored; noise or blur only mask it. [fetched] — [Fstoppers, Alex Cooke, "The Precision Myth", Jan 2026](https://fstoppers.com/gear/precision-myth-photographers-guide-bit-depth-719847)
- Ohnsman: use a linear gradient to darken the sky and lighten the land; add luminance or colour range targeting so the gradient does not darken trees or hilltops that poke above the horizon; the Select Sky mask can be inverted to target the land. [fetched] — [Digital Photography School, Rick Ohnsman](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- A graduated filter is linear, so anything above the horizon takes on the sky adjustment; the fix is to brush the effect off foreground objects or range-mask it. [snippet] — [Digital Camera World](https://www.digitalcameraworld.com/uk/tutorials/lightroom-tutorial-7-fix-skies-with-ease-in-lightroom-with-a-graduated-filter); [Fstoppers, six graduated-filter tweaks](https://fstoppers.com/originals/improve-lightrooms-graduated-filter-these-six-tweaks-543645)
- Halos are described as the common sign of a poor blend and typically show at hard edges where trees or mountains meet the sky. [snippet] — [Greg Benz, removing exposure-blending halos](https://gregbenzphotography.com/luminosity-masking/how-to-remove-exposure-blending-halos/)
- User report: a gradient constrained by a colour range mask gave "horrible halos"; redoing it with a luminance range and using Exposure (not Highlights/Shadows) avoided them. [snippet, forum anecdote] — [Adobe Community](https://community.adobe.com/questions-675/how-do-you-easily-exclude-the-sky-from-adjustments-941011)
- Adobe community contributor on AI sky masks: a little overlap of the sky mask into the land is not necessarily bad because it avoids ugly halos at the edge. [snippet, forum] — [Adobe Community, Select Sky accuracy](https://community.adobe.com/t5/lightroom-classic-discussions/select-sky-accuracy/m-p/12483981)
- Halo repair in a layer editor: new layer in Darken blend mode, clone nearby sky over the bright halo. [snippet] — [Greg Benz](https://gregbenzphotography.com/luminosity-masking/how-to-remove-exposure-blending-halos/)
- For sunsets, avoid raising Exposure near the sun because it pushes the sun toward clipping; lift blacks inside a feathered mask instead. [snippet] — [Fstoppers, raising the blacks](https://fstoppers.com/landscapes/why-raising-blacks-can-make-lightroom-sunset-glow-905015)

### Inferences
- Halo-avoidance rules that follow from the above: prefer a soft, wide gradient over a pixel-precise sky mask on a clean horizon; use Exposure rather than extreme Highlights/Shadows (those sliders are local tone-mappers and create edge glows); keep the sky and land adjustments from diverging by more than roughly a stop in total on a JPEG; check the horizon at 100%.
- Dune crests against sky are exactly the "hard edge" case. An AI sky mask with slight feather/overlap, or a gradient with a luminance range, is safer than a hard mask. A bright rim along a dune ridge at sunrise is often real light, so compare with the original before "fixing" it.
- Realistic limits (my estimate, unsourced): blown JPEG sky stays blown — it can only be greyed, not recovered; shadows lifted more than about 1–1.5 stops will show noise, blocky compression artefacts and colour blotching. Where the scene exceeds this, accept a darker foreground or a silhouette rather than forcing an HDR look.
- If the editor allows it, converting the JPEG to a 16-bit working file before heavy edits reduces rounding errors accumulated across multiple steps, but does not add information the JPEG lacks.

### Gaps
- No source quantifies how many stops of shadow lift or highlight pull a modern APS-C JPEG tolerates.
- Cambridge in Colour's posterization and luminosity-mask material could not be fetched.

---

## 3. Sunset and sunrise colour: white balance, saturated reds/oranges, banding, credible saturation

### Takeaway
Keep the warmth (auto white balance tends to neutralize sunsets), raise colour with vibrance and targeted hue/mask adjustments rather than global saturation, and treat smooth sky gradients as the most fragile part of an 8-bit file.

### Cited Findings
- Auto white balance tends to neutralize warm sunset tones by choosing an unnaturally cool temperature; warming the white balance is described as the step that brings a sunset back. [snippet] — [Adobe, enhance sunset photo](https://www.adobe.com/learn/lightroom-cc/web/enhance-sunset-photo); [Fstoppers, drama back to sunsets](https://fstoppers.com/lightroom/how-bring-drama-back-your-sunsets-lightroom-713523)
- Saturation hits every pixel and hue equally, so oranges and reds reach the limit first and skies turn "crunchy"; vibrance lifts weaker colours more than strong ones. Advice: keep global colour moves modest. No numbers given. [fetched] — [Fstoppers on Christian Möhrle, Dec 2025](https://fstoppers.com/lightroom/vibrance-vs-saturation-mistake-makes-sunsets-look-fake-719262)
- Möhrle's targeted approach: reduce yellow saturation to calm a foreground cast; selectively boost reds, oranges, purples and magentas; use a luminance-range mask on the bright sky to warm and saturate highlights; colour-grade warm highlights against cooler midtones; pull saturation back where glow areas look synthetic. [fetched] — [same Fstoppers article](https://fstoppers.com/lightroom/vibrance-vs-saturation-mistake-makes-sunsets-look-fake-719262)
- Local white balance is recommended over one global shift: one balance for the sky, another for the foreground (e.g., cool land or water under a warm sky). [snippet] — [Fstoppers, smarter white balance](https://fstoppers.com/lightroom/smarter-way-use-white-balance-lightroom-classic-900699); [Fstoppers, split-tone trick](https://fstoppers.com/education/split-tone-trick-beats-single-white-balance-slider-903550)
- A diagnostic trick: temporarily push vibrance and saturation to maximum to reveal colour casts, set white balance, then bring them back down. [snippet] — [Fstoppers, incredible sunset photos](https://fstoppers.com/originals/create-incredible-sunset-photos-editing-lightroom-547705)
- Banding often appears in cloudless sky; pushing saturation, vibrance or dehaze too far can trigger it, and it means the tonal range has been pushed beyond what the file holds. Adding a little noise or grain disguises remaining bands. [snippet] — [ExpertPhotography, colour banding](https://expertphotography.com/color-banding)
- Adding noise is a workaround for banding that has already occurred, not a true fix. [fetched] — [Fstoppers, "The Precision Myth"](https://fstoppers.com/gear/precision-myth-photographers-guide-bit-depth-719847)
- Oversaturation is called probably the biggest mistake in landscape editing. [snippet] — [Fstoppers, common editing mistakes](https://fstoppers.com/landscapes/some-most-common-landscape-photography-editing-mistakes-625818)
- Ohnsman and Patino both treat white balance as a mood decision rather than a correctness problem. [fetched] — [DPS, Ohnsman](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/); [Fstoppers on Patino](https://fstoppers.com/landscapes/simple-workflow-better-landscape-photo-edits-679023)

### Inferences
- JPEG white balance is not a true white-balance change: it is a colour shift applied to already-balanced, gamma-encoded 8-bit data. Small temperature/tint moves are fine; large corrections give colour crossovers (shadows and highlights shifting differently) and cannot restore a channel that clipped in camera.
- Channel clipping check (unsourced as a cited method; no source measured it): view the RGB histogram, not just luminance. In sunsets and red dunes the red channel piles up at the right edge while luminance looks safe. If red is already at the wall, any added saturation, warmth or contrast flattens the dunes/sky into a textureless orange. Reducing saturation or luminance of red/orange slightly can restore visible gradation only if the channel was not clipped in camera.
- Banding avoidance for these files: do the sky in one or two gentle moves rather than many stacked ones; avoid dehaze, clarity and strong contrast on clear sky; avoid large hue shifts and blue-luminance drops in sky; export at high JPEG quality; if bands appear, back off first and add fine grain only as a last resort. Blue hour and wide clear skies shot with the 11 mm are the highest-risk images.
- Credible amounts (my rule of thumb, since sources give none): on a camera JPEG that already has a saturated look applied, vibrance roughly +5 to +15 and global saturation around 0 to +5 on a Lightroom-type scale; RAW tutorials showing +30 to +50 vibrance start from a flat file and should not be copied.

### Gaps
- No source directly explains or measures per-channel (red) clipping in sunset JPEGs; the search confirmed this gap explicitly.
- No source gives numeric saturation/vibrance ceilings for realism.

---

## 4. Red/orange dune colour and HSL adjustments

### Takeaway
I found no reliable, desert-specific editing guidance; what exists is general HSL advice plus reports that per-colour luminance and hue shifts on JPEGs produce artefacts. Dunes should be handled conservatively because the whole subject sits in one or two HSL bands.

### Cited Findings
- HSL/Colour Mixer hue shifts can be used to change the rendering of sand (the example given is choosing more orange-coloured sand). [snippet] — [Digital Photography School, HSL panel guide](https://digital-photography-school.com/understanding-the-hsl-panel-in-lightroom-for-beginners/)
- Forum report: lowering (orange) luminance on JPEG files made colour tones change dramatically, described as a pixel shift. The thread concerns skin tones, not sand. [snippet, forum anecdote] — [Adobe Community](https://community.adobe.com/t5/lightroom-classic/lightroom-luminance-down-causes-color-disruption/td-p/10264076)
- Forum report: shifting the blue hue slider produced significant fringing/artefacts where yellow vegetation meets the sky. [snippet, forum anecdote] — [Adobe Community](https://community.adobe.com/t5/photoshop/color-fringing-artifacts-when-adjusting-hue-saturation-sliders/m-p/9971082)
- Pulling saturation too high can create grainy artefacts in colours. [snippet] — [SLR Lounge, HSL panel](https://www.slrlounge.com/understanding-each-section-in-the-hslcolorbw-panel-in-lightroom-4/)
- Möhrle uses selective HSL moves (reduce yellow, boost reds/oranges/purples/magentas) instead of global saturation. [fetched] — [Fstoppers](https://fstoppers.com/lightroom/vibrance-vs-saturation-mistake-makes-sunsets-look-fake-719262)

### Inferences
- Why JPEG HSL is riskier than RAW: JPEG stores colour at reduced resolution and in 8×8 blocks, so per-hue selections have blocky, noisy edges; a dune/sky boundary (orange against blue, complementary hues) is where fringing and edge halos appear when blue luminance is dropped and orange saturation raised at the same time.
- In a dune scene, "orange" and "red" sliders act almost globally. Moving orange hue shifts the entire subject; a few points toward red looks richer, more looks like Mars. The lit and shadow sides of a dune can fall in different bands (orange vs. red/magenta-brown), so a large move on one band can split the dune into two colours with a visible seam.
- Accuracy heuristics (unsourced): Sossusvlei sand is genuinely orange-red and deepens at low sun, so strong colour is real, but texture must survive — ripples and wind patterns disappearing is the sign of red-channel saturation. Often the better move is to lower orange/red saturation slightly and add local contrast, rather than add saturation. Deadvlei's white clay pan is a useful neutral reference: if the pan looks orange or pink, the white balance is too warm; the dead trees should stay near-black/brown, not red.
- Suggested ceilings for JPEG HSL (my rule of thumb): hue within about ±10, saturation within about ±15, luminance within about ±10–15, and inspect dune/sky edges at 100% after every luminance move.

### Gaps
- No authoritative source (photographer or educator) found on editing Namibian dune colour, or desert sand colour generally.
- No source found on handling single-colour-dominated scenes; the notes above are inference.

---

## 5. Haze, dust, flat midday light: dehaze vs. contrast vs. clarity vs. texture

### Takeaway
Texture acts on fine detail, clarity on mid-scale/midtone contrast, dehaze on broad low-frequency contrast and colour; dehaze is the strongest and has the worst side effects, so sources recommend small amounts and masked application rather than global.

### Cited Findings
- Texture adds or removes contrast in high-frequency areas (fine detail) and largely ignores mid/low-frequency areas; clarity targets midtones/mid-frequency areas that texture ignores; dehaze is intended to restore colour and contrast to washed-out images and makes colours unrealistic when applied heavily. Skies are cited as low-frequency areas. No numbers. [fetched] — [PetaPixel, Jaron Schneider on Kevin Raposo's video, Jan 2021](https://petapixel.com/2021/01/05/understanding-the-differences-between-clarity-texture-and-dehaze/)
- Texture and clarity can accentuate noise in broad areas such as skies, so many photographers mask them rather than apply globally; texture is the gentlest, does not significantly shift colour or saturation, and adds fewer artefacts than the sharpening slider; dehaze can far exceed the contrast obtainable with curves or clarity. [snippet] — [John Paul Caponigro](https://www.johnpaulcaponigro.com/blog/?p=19332); [PhotoshopCAFE](https://photoshopcafe.com/texture-clarity-and-dehaze-in-lightroom-acr-explained-the-ultimate-comparision/)
- Suggested dehaze range of about +5 to +25 for most photos. [snippet; page body could not be fetched to verify] — [DIY Photography, clarity vs texture vs dehaze](https://www.diyphotography.net/clarity-vs-texture-vs-dehaze/)
- Clarity pushed to extremes produces halos and aliasing at edges. [snippet, forum] — [Adobe Community](https://community.adobe.com/t5/camera-raw-bugs/p-camera-raw-artifacts-on-edges-caused-by-clarity/m-p/12241642)
- Too much dehaze makes skies look unnatural; use a local brush on the hazy area instead of the global slider; dehaze adds blue, so blue saturation often needs reducing afterwards. [snippet; exact article among these not verified] — [Fstoppers, editing mistakes part one](https://fstoppers.com/landscapes/stop-making-these-editing-mistakes-part-one-598541); [SLR Lounge, 5 common mistakes](https://www.slrlounge.com/5-common-mistakes-in-editing-landscape-photography/)
- Dehaze makes sensor dust spots visible: pushing it to +100 is recommended as a deliberate technique to find subtle dust spots, heal them, then reset the slider. [snippet] — [Have Camera Will Travel](https://havecamerawilltravel.com/lightroom/dehaze-dust-spots/); [Shutterbug](https://cdn.shutterbug.com/node/591591)
- Adobe: vignetting is most noticeable in subjects that should be an even tone, such as sky. [snippet] — [Adobe Lightroom Classic help](https://helpx.adobe.com/lightroom-classic/help/retouch-photos.html)
- Pushing saturation, vibrance or dehaze too far can trigger banding in sky. [snippet] — [ExpertPhotography](https://expertphotography.com/color-banding)

### Inferences
- Summary table (synthesized from the above plus general knowledge):
  - **Contrast/curves**: global, predictable; raises saturation with it; safest first step for flat midday light.
  - **Texture**: fine detail (sand ripples, rock, bark); lowest halo risk; amplifies JPEG sharpening artefacts and noise if stacked on in-camera sharpening.
  - **Clarity/structure**: mid-scale local contrast; gives punch to dunes and clouds; halos at horizon and dark edges, grittiness, darker-feeling image.
  - **Dehaze**: lifts black point adaptively and adds saturation; darkens and blues the sky, emphasizes vignetting and corner darkening (relevant to the 11 mm), reveals dust spots, noise and banding in clear sky.
- Namibia-specific judgement: distant haze and dust are part of the place and provide depth (aerial perspective). Removing it fully flattens the layers of receding dunes and plains. Apply dehaze through a gradient or brush on the distant band only, at low values, and leave the sky out of the mask.
- JPEG starting points (my rule of thumb, toned down from RAW ranges): dehaze +5 to +15 masked (stay at the low end of the +5 to +25 range cited above), clarity +5 to +15, texture +5 to +20 on land only, and none of the three on clear sky.
- Do the dust-spot hunt (temporary +100 dehaze) on every wide-sky frame: a desert trip with lens changes and stopped-down apertures makes spots likely, and any later sky darkening will reveal them.
- Flat midday light cannot be turned into golden hour; options that hold up are a modest contrast curve, slightly cooler/cleaner white balance, or black-and-white conversion.

### Gaps
- The numeric dehaze range could not be verified on the source page; no sourced numeric ranges for clarity or texture.
- The "dehaze adds blue" claim is snippet-level; the dehaze–vignetting link is my inference, not confirmed by a source.

---

## 6. Light shaping: dodge and burn, vignettes, "light path", Orton effect

### Takeaway
Dodging and burning exploits the fact that the eye goes to bright areas and skips dark ones; it should enhance light that was actually there. Orton glow is accepted when subtle (about 10–20% opacity) and reads as kitsch when it visibly softens the whole frame.

### Cited Findings
- The eye is drawn to brightness and tends to ignore darkness; dodging and burning are local adjustments used to guide the eye, emphasize points of interest and set mood; done badly they create unnatural halos; moderation is the stated key. [snippet] — [Photography Life, mastering dodge and burn](https://photographylife.com/mastering-dodge-and-burn-in-photography); [Fstoppers, dodge and burn landscapes](https://fstoppers.com/education/dodge-and-burn-your-way-better-landscape-photos-412788)
- Ohnsman describes dodging and burning as directing attention by "complexifying the light". [fetched] — [Digital Photography School](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- Patino: use a soft brush for local work so transitions are smooth. [fetched] — [Fstoppers](https://fstoppers.com/landscapes/simple-workflow-better-landscape-photo-edits-679023)
- NLPA rule on the honesty limit: heavy contrast and dodging/burning are allowed, but not to "add light to a part of a scene where light did not exist". [fetched] — [Natural Landscape Photography Awards rules](https://www.naturallandscapeawards.com/rules/)
- A typical finishing sequence quoted from a working photographer: create depth through dodging and burning, then close with a vignette. [snippet] — [Digital Photographer via PressReader](https://www.pressreader.com/uk/digital-photographer/20180625/282114932306253)
- Orton effect: originated with Canadian photographer Michael Orton as a film technique; today a soft glow added in post, usually applied lightly. [snippet] — [ExpertPhotography](https://expertphotography.com/orton-effect-landscape-photography); [Photography Life](https://photographylife.com/is-the-orton-effect-taking-over-landscape-photography)
- Chris M. Williams (DPReview) recipe: after all other edits, duplicate the merged layer, Gaussian blur it (about 37 px for 42 MP files, no more than about 25 px for lower-resolution/APS-C files, 15–40 px overall), apply Levels to the blur layer (blacks about 10–25, highlights about 245) to counter the haloing and contrast loss, set opacity to 10–20% (35% is "a bit on the excessive side"), then optionally recover edges with a High Pass layer at 4–5.5 px in Soft Light. He argues the effect adds depth and atmosphere and counters the crunchiness of web sharpening. [fetched] — [DPReview, Chris M. Williams, 2016](https://www.dpreview.com/techniques/4455063977/how-to-effectively-use-orton-layers-in-post-processing)
- The Orton effect can be applied only to selected areas rather than the whole frame. [snippet] — [Photography Life](https://photographylife.com/is-the-orton-effect-taking-over-landscape-photography)

### Inferences
- "Light path" in practice: identify where the light already falls (lit dune face, bright sand ripple line, sunlit grass), brighten along that path by small amounts, darken competing bright areas at the frame edges and corners, and finish with a mild vignette. Each individual adjustment should be small (roughly ±0.2 to ±0.5 stop on a JPEG) with large, soft brushes; many subtle strokes beat one strong one.
- Vignette on the 11 mm lens: the corners may already be darker (see section 7), and dehaze/contrast strengthen that. Check corners before adding a vignette; on wide clear skies a vignette shows as an obvious dark ring and can band in 8-bit.
- Orton for this trip: plausible on backlit dust, hazy sunrise dunes and glowing sunset horizons at 10–15% opacity; inappropriate on crisp Deadvlei trees, midday scenes and anything with stars. A blurred overlay can also hide mild sky banding, but it reduces fine detail in prints.
- Burning a JPEG sky darker by a large amount increases banding and saturation; dodge/burn budgets should be smaller than on RAW.

### Gaps
- PetaPixel's dodge-and-burn article and Photography Life's Orton and dodge/burn articles could not be fetched, so brush settings, specific opacity/flow values and the critical view of Orton overuse are not sourced in detail.
- I found no source using the exact term "light path"; the description above is my synthesis.

---

## 7. Lens corrections for ultra-wides in JPEG, horizon, perspective, crop and aspect ratios

### Takeaway
With the Sony E 11mm f/1.8, distortion correction is forced on in camera, so JPEGs arrive already corrected (about −0.75% residual barrel distortion versus about −9.6% uncorrected); do not apply a lens profile again. A 30×45 cm print is exactly 3:2, so uncropped frames fit without loss.

### Cited Findings
- With the E 11mm f/1.8 mounted, the camera's distortion compensation is locked to Auto and cannot be switched off (observed on A7R III and ZV-E10 bodies). JPEG distortion measured at −0.75% versus −9.60% in uncorrected RAW; the correction crops and rescales, costing over 12% of the pixels in the test. [snippet] — [LensTip, Sony E 11mm f/1.8 distortion](https://lenstip.com/631.6-Lens_review-Sony_E_11_mm_f_1.8_Distortion_and_field_of_view.html); [Cameralabs review](https://www.cameralabs.com/sony-e-11mm-f1-8-review)
- Vignetting with auto-correction active is still about 1.45 EV at f/1.8 and mostly gone from f/2.8. [snippet] — [OpticalLimits/Photozone review](https://photozone.de/sony-alpha-aps-c-lens-tests/1145-sony11f18?start=1)
- Sony: lens compensation is applied to the JPEG; the RAW remains uncompensated. [snippet] — [Sony support](https://www.sony.co.uk/electronics/support/articles/00404879)
- A crooked horizon is among the most noticeable mistakes; the fix is the straighten/angle tool in the crop tool, dragged along the horizon. [snippet] — [Adorama, post-production mistakes](https://www.adorama.com/alc/post-production-mistakes-to-avoid/)
- NLPA treats correcting lens distortion and perspective control as legitimate, but stretching mountains to look more dramatic as not allowed. [fetched] — [NLPA rules](https://www.naturallandscapeawards.com/rules/)
- Elliot Hook on aspect ratios: 3:2 encourages left-to-right reading and suits scenes with little foreground, but its limited height makes foreground hard to include with wide-angle lenses; 4:3 works well with wide-angle lenses and keeps foregrounds from sprawling; 16:9 gives a panoramic feel, suits distant subjects with longer lenses, makes foreground lead-ins hard; 5:4 suits portrait-orientation landscapes; 1:1 suits minimalism, symmetry and centred horizons; 2:1 and 3:1 emphasize horizontal lines and suit stitched panoramas but are hard to print at meaningful size from a single frame. [fetched] — [Digital Photography School, Elliot Hook](https://digital-photography-school.com/aspect-ratios-in-landscape-photography/)
- 3:2 corresponds to 10×15, 20×30 and 30×45 cm prints; 4:5 corresponds to 20×25 cm (8×10 in) and is common in framing. [snippet] — [fotografie.nl](https://www.fotografie.nl/en/post/aspect-ratio-is-beeldverhouding-belangrijk); [ExpertPhotography](https://expertphotography.com/aspect-ratio-landscape-photography/)
- Cropping early alters later steps in the workflow. [snippet] — [Digital Photography School](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)

### Inferences
- Since the JPEGs are already distortion-, shading- and (by default) chromatic-aberration-corrected, applying an automatic lens profile in the editor would double-correct; leave profile corrections off and fix only residuals manually (slight barrel distortion on a dead-straight horizon near the frame edge; some remaining corner shading if shot wide open).
- With a 16.5 mm-equivalent lens, a horizon placed away from the vertical centre can show residual curvature, and tilting the camera makes verticals (Deadvlei trees) lean. Small perspective corrections are fine; each rotation or warp resamples the JPEG and costs sharpness and edge pixels, so do all geometry in one step.
- Level using a real horizon line, not dune ridges, which are rarely horizontal.
- Print resolution arithmetic (the a6700's 6192×4128 pixel dimensions are from my memory, not from a fetched source): 45 cm is 17.7 in, giving about 350 ppi uncropped; a 16:9 crop keeps the full width; even a crop to roughly 60% of the width still gives about 200 ppi at 45 cm, enough for a wall print viewed at normal distance.
- 16:9 crops suit desert plains and dune panoramas where sky or foreground is empty, and suit TV/phone sharing; 4:5 suits vertical compositions for phone feeds but needs 24×30 or 20×25 cm paper rather than 30×45.

### Gaps
- Not confirmed specifically for the a6700 body (tests used A7R III and ZV-E10), though the lens behaviour is lens-driven. Whether the 25mm f/1.7 (brand not specified in the brief) receives in-camera corrections is unknown; a third-party manual lens without electronic contacts would not be corrected.
- Photography Life's aspect-ratio article could not be fetched.

---

## 8. Merging from JPEGs: HDR, panoramas, focus stacking

### Takeaway
I found no authoritative source on merging from JPEGs specifically; the retrievable guidance is RAW-centred. What is sourced: keep exposure consistent across panorama frames, merge brackets before stitching, and note that white balance is baked into JPEG/TIFF pixels, so mismatched frames will not match after merging.

### Cited Findings
- Adobe: keep exposure consistent for every frame of a panorama for a seamless result; HDR-panorama merging expects brackets with consistent exposure offsets. [snippet] — [Adobe Lightroom help, HDR and panorama merge](https://helpx.adobe.com/lightroom/desktop/edit-photos/hdr-panorama.html)
- White balance is stored separately from pixel data in a DNG but baked into pixels in JPEG or TIFF output, so frames with different white balance will not match in colour across a merge. [snippet, forum explainer] — [Adobe Community](https://community.adobe.com/bug-reports-562/p-photo-merge-to-hdr-dramatic-dng-color-problem-in-lightroom-classic-666838)
- A PTGui user reports always shooting panoramas with auto white balance disabled. [snippet, forum] — [PTGui Google Group](https://groups.google.com/g/ptgui/c/adCkjcTtFyY)
- Recommended order for HDR panoramas: merge each bracket set first, then stitch. [snippet, Q&A] — [Unique Photo community](https://www.uniquephoto.com/community/qa/best-workflow-for-hdr-panoramas-merge-stitch-and-edit-in-what-order)
- NLPA accepts exposure bracketing, focus stacking, image stacking/averaging and panoramas (including the distortions needed for stitching) as legitimate technical improvements, provided the frames are not taken at significantly different times. [fetched] — [NLPA rules](https://www.naturallandscapeawards.com/rules/)
- Halos are the common sign of a poor exposure blend, especially at hard edges against sky. [snippet] — [Greg Benz](https://gregbenzphotography.com/luminosity-masking/how-to-remove-exposure-blending-halos/)

### Inferences
- **HDR from bracketed JPEGs** works in the sense that each JPEG contributes range the others lack, and it is the one way to exceed the single-JPEG limits described in section 2. Pitfalls: JPEGs are tone-curved (not linear), so merge software estimates the response curve and results are less clean than from RAW; auto white balance, DRO/in-camera HDR or differing Creative Look processing between frames causes colour mismatch; moving dust, grass and clouds cause ghosting; tone-mapping the result invites the classic HDR halo look. Exposure fusion or simple manual blending of two frames (one for sky, one for land) with a soft horizon mask is usually more natural than a tone-mapped HDR.
- **Panoramas from JPEGs** are the most forgiving merge. Pitfalls: frames shot in auto exposure or auto white balance produce brightness and colour steps in the sky (the stitched gradient is where 8-bit banding and seams show); in-camera vignetting residue creates scalloped sky; ultra-wide frames (11 mm) have large perspective differences and need generous overlap; stitching resamples and crops the result. Do no editing before the stitch, or apply identical settings to all frames, then edit the stitched image as a 16-bit file if possible.
- **Focus stacking from JPEGs** is largely unaffected by bit depth because it selects sharp regions rather than stretching tones; in-camera sharpening halos can be amplified at stack seams, and wind-blown vegetation causes ghosting. At 11 mm and typical landscape apertures the depth of field is usually sufficient without stacking.
- For this already-shot trip, merges are only possible where brackets or overlapping frames happen to exist with matching settings.

### Gaps
- No reliable source found that tests HDR, panorama or focus-stack quality from JPEG inputs versus RAW; the pitfalls listed are inference from how JPEG encoding works.
- A Canon-forum thread disputes how camera white balance interacts with merging; it concerns RAW and does not settle the JPEG case — [Canon Community](https://community.usa.canon.com/t5/Camera-Software/Struggling-with-HDR/m-p/606820).

---

## 9. Sky replacement and generative tools vs. documentary honesty

### Takeaway
The clearest published standard, the Natural Landscape Photography Awards, permits global and local tone/colour work, small transient removals and technical merges, and prohibits adding skies or other elements, removing significant elements, blending different times of day and exaggerated warping. Other competitions are looser about sky replacement when the photographer shot the sky.

### Cited Findings
- NLPA golden rule: "The integrity of the subject should be maintained." [fetched] — [NLPA rules](https://www.naturallandscapeawards.com/rules/)
- NLPA not allowed: "adding in skies, foregrounds, birds, mist, sun, moon, rainbows"; "Removing significant elements from the original scene"; "Combining images taken at significantly different times"; "stretching mountains to make them appear more dramatic"; digital painting to introduce elements; in the multiple-exposure context "No sky replacement presented as real" and "No AI-generated imagery". [fetched] — [NLPA rules](https://www.naturallandscapeawards.com/rules/)
- NLPA allowed: white balance, exposure, colour and contrast "across the whole image and/or locally"; black-and-white conversion; heavy contrast and dodging/burning short of adding light where none existed; "removing small and transient elements"; removing dust spots and flares; focus stacking, stacking/averaging, exposure bracketing, panoramas; lens-distortion and perspective correction; very minor warping is tolerated but called ill-advised. Judges retain final discretion. [fetched] — [NLPA rules](https://www.naturallandscapeawards.com/rules/)
- NLPA was founded in response to digital art presented as photographs, including sky replacement and added skies and moons; later coverage describes it as shunning AI and composites. [snippet] — [PetaPixel 2021](https://petapixel.com/2021/11/09/the-winners-of-new-landscape-photo-competition-that-rewards-realism); [PetaPixel 2025](https://petapixel.com/2025/09/23/the-natural-landscape-photography-awards-2025-shuns-ai-and-composites)
- Contrasting positions: the International Landscape Photographer of the Year FAQ does not class sky replacement as generative AI when the photographer supplies the sky image; NCPF (UK club federation) rules allow sky replacement if the replacement sky is the photographer's own image. [snippet] — [ILPOTY FAQ](https://internationallandscapephotographer.com/index.php/awards/faq); [NCPF rules](https://ncpf.org.uk/competition-rules-guidance/)

### Inferences
- For family travel photographs the NLPA list is a sensible personal standard: the pictures serve as a record of what Namibia looked like. Practical translation: fine — tone, colour, local dodging/burning, dust-spot removal, removing a stray footprint, tyre track or distant person; not fine if the image is presented as what was seen — replaced skies, added sun rays or birds, generative fill that invents dunes, clouds or trees.
- Generative removal tools are a grey area under the NLPA wording: removing "small and transient" elements is permitted regardless of tool, but the rule against introducing new elements applies if the fill invents content. Generative expand (extending the frame) introduces invented scene content and falls on the prohibited side.
- If a replaced sky or composite is made for fun, labelling it as such when sharing is the consistent approach.

### Gaps
- The NLPA main rules as fetched do not name AI or generative fill explicitly outside the multiple-exposure section; I did not verify whether a 2026 revision adds explicit wording.
- No fetched opinion pieces from named landscape photographers (e.g., Alex Nail, who is associated with NLPA) on this debate.

---

## 10. Sharpening, noise, output sharpening for print, soft-proofing and print brightness

### Takeaway
Sharpen last and for the specific output, backing off when halos appear; prints that look too dark are most often caused by a monitor that is too bright, and a test print beats soft-proofing. I could not retrieve authoritative numeric sharpening guidance (Cambridge in Colour was blocked).

### Cited Findings
- Sharpen according to the intended output (screen or print); sharpening adds edge contrast but cannot fix a misfocused image. [fetched] — [Digital Photography School, Rick Ohnsman](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- Over-sharpening creates halos and glows around everything; a practical method is to raise sharpening until a halo appears and then back off slightly. [snippet] — [Fstoppers, editing mistakes](https://fstoppers.com/landscapes/stop-making-these-editing-mistakes-part-one-598541); [Adorama](https://www.adorama.com/alc/post-production-mistakes-to-avoid/)
- Output sharpening compensates for the softening of ink on paper, is applied last after resizing, and depends on output size and substrate; in Lightroom, print sharpening is applied after upsampling. [snippet] — [John Paul Caponigro, output sharpening](https://www.johnpaulcaponigro.com/blog/tag/dot-gain/); [Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/lr-soft-proofing/m-p/9652595)
- Texture and clarity amplify grain; check at 1:1. [snippet] — [John Paul Caponigro](https://www.johnpaulcaponigro.com/blog/?p=19332)
- Noise reduction is best applied before heavy colour pushes (Möhrle). [fetched] — [Fstoppers](https://fstoppers.com/lightroom/vibrance-vs-saturation-mistake-makes-sunsets-look-fake-719262)
- "If the print is too dark, your monitor is too bright" is the standard diagnosis; one source suggests calibrating to around 80 cd/m²; dim room lighting also skews judgement. [snippet, forum; the 80 cd/m² figure's exact source page not verified] — [Adobe Community](https://community.adobe.com/t5/photoshop-ecosystem-discussions/prints-are-too-dark-printing-from-photoshop-on-ultra-premium-glossy/m-p/9759226)
- Soft-proofing reliability depends on the display, printer profile, viewing environment and file preparation, and does not replace a test print; adding some brightness before printing usually does not hurt when printing blind. [snippet] — [Fstoppers, better photo prints](https://fstoppers.com/printing/how-create-better-photo-prints-610897); [Luminous Landscape](https://luminous-landscape.com/?p=50266)
- Prints from 8-bit files can look good if the file was not heavily stretched; print banding relates partly to insufficient dithering at output, and modern printers dither on their own. [fetched] — [Fstoppers, "The Precision Myth"](https://fstoppers.com/gear/precision-myth-photographers-guide-bit-depth-719847)
- Williams notes that web sharpening combined with compressed dynamic range gives a "crunchy" look. [fetched] — [DPReview](https://www.dpreview.com/techniques/4455063977/how-to-effectively-use-orton-layers-in-post-processing)

### Inferences
- In-camera JPEGs already carry capture sharpening and noise reduction. Additional capture-style sharpening should be near zero; only (a) selective creative sharpening/texture on land and (b) output sharpening after resizing are warranted. Sharpening an already-sharpened JPEG thickens existing halos (visible on dune crests and branches against sky) and sharpens 8×8 compression blocks.
- Never sharpen or add texture to clear sky; mask sharpening to edges/land. Noise reduction on JPEG should be mild and mainly chroma, applied to lifted shadows and blue-hour skies; heavy luminance noise reduction on camera-processed files gives a plastic look and can increase banding by removing the natural dither that noise provides.
- Print preparation for 30×45 cm: the file has about 350 ppi at that size (see section 7), so no upsampling is needed; send sRGB JPEG at maximum quality to a consumer lab unless the lab supplies profiles; apply output sharpening for the paper type (more for matte than glossy); brighten midtones/shadows modestly for print (commonly on the order of +0.2 to +0.5 stop — my rule of thumb, unsourced), keeping highlights unclipped; order one small test print before the large one. Dark desert-night-blue and deep shadow areas are where prints most often block up.
- For screen sharing, export at the display size (for example about 2048–4000 px long edge) with light screen sharpening and JPEG quality around 85–90%+ to avoid recompression banding in skies; every re-save of a JPEG adds loss, so edit non-destructively from the original and export once.

### Gaps
- Cambridge in Colour's sharpening tutorial (three-stage sharpening, radius versus viewing distance) returned HTTP 403; no sourced radius/amount/threshold numbers.
- No sourced figure for how much to brighten for print; no source on lab-specific soft-proofing for consumer print services.

---

## 11. Common beginner mistakes and self-checks

### Takeaway
The repeatedly named mistakes are oversaturation, over-sharpening and local-contrast halos, excessive dehaze, crooked horizons and visible horizon halos; the recommended checks are before/after comparison, the histogram with clipping warnings, 100% inspection, and returning to the image after a break.

### Cited Findings
- Oversaturation is called probably the biggest mistake in landscape photography; comparing before and after catches changes that are too strong. [snippet] — [Fstoppers, common editing mistakes](https://fstoppers.com/landscapes/some-most-common-landscape-photography-editing-mistakes-625818); [SLR Lounge](https://www.slrlounge.com/5-common-mistakes-in-editing-landscape-photography/)
- Over-sharpening creates halos and glows; halos also appear around the horizon where heavy adjustments meet. [snippet] — [Fstoppers, editing mistakes part one](https://fstoppers.com/landscapes/stop-making-these-editing-mistakes-part-one-598541)
- Too much dehaze makes the sky look unnatural; apply it locally instead of globally; dehaze adds blue. [snippet] — [Fstoppers, editing mistakes part two](https://fstoppers.com/landscapes/stop-making-these-editing-mistakes-part-two-598918)
- Tilted horizons are hard to miss; fix with the straighten tool. [snippet] — [Adorama](https://www.adorama.com/alc/post-production-mistakes-to-avoid/)
- Histogram discipline: turn on clipping indicators, remove highlight and shadow clipping before judging exposure and contrast. [fetched] — [Digital Photography School, Rick Ohnsman](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- Patino: check the histogram before leaving the "Light" phase; let edits "marinate" and revisit after a break. [fetched] — [Fstoppers](https://fstoppers.com/landscapes/simple-workflow-better-landscape-photo-edits-679023)
- Ohnsman's "taste test": ask whether a different crop would remove distractions or strengthen the subject. [fetched] — [Digital Photography School](https://digital-photography-school.com/post-processing-workflow-tips-landscape-photography/)
- Möhrle: judge where "too much" starts in your own files; pull saturation back where it looks synthetic. [fetched] — [Fstoppers](https://fstoppers.com/lightroom/vibrance-vs-saturation-mistake-makes-sunsets-look-fake-719262)
- JP Danko's principle: editing should enhance the photograph, not fix it. [snippet] — [DIY Photography](https://www.diyphotography.net/12-step-program-editing-landscape-photography-without-plugins-presets)
- Banding during editing signals the tonal range has been pushed beyond what the file holds. [snippet] — [ExpertPhotography](https://expertphotography.com/color-banding)

### Inferences
- JPEG-specific additions to the mistake list: copying RAW-tutorial slider values; stacking in-camera processing with editor processing (double sharpening, double saturation, double lens correction); repeated re-saving of JPEGs; trying to recover blown skies; lifting shadows until noise and blocks show.
- Crushed blacks: with JPEGs the camera's contrast curve already places blacks low; adding contrast, dehaze and clarity each push them further. Shadow detail on dark dune faces should remain faintly readable unless a silhouette is intended; watch the left edge of the histogram.
- Self-check list for each image: (1) toggle before/after — if the edit shouts, halve it; (2) RGB histogram for red-channel clipping and left-edge pile-up; (3) 100% view along the horizon and dune crests for halos and fringing; (4) scan sky for banding, dust spots and vignette rings; (5) check the horizon is level; (6) view small (thumbnail) to judge overall balance and where the eye goes; (7) wait and review the next day; (8) compare a set of images side by side so colour and saturation are consistent across the trip; (9) a useful final move is to reduce the strength of the whole edit by about a fifth to a third.

### Gaps
- PetaPixel's "5 basic mistakes" article could not be fetched; the Fstoppers/SLR Lounge/Adorama mistake lists were read only as search summaries, so attribution of individual tips to specific articles is approximate.
- No source found discussing crushed blacks specifically for JPEG landscapes.
