# Observations from the owner's actual photos (first-hand, by the coordinator)

Source: `~/Documents/Fotos/Namibia_2026` (read-only; nothing was modified). Metadata read with macOS Spotlight (`mdls`) for all files; seven frames were viewed at 1400 px. Visual notes are from downsized copies, so fine noise/artefacts at 100 % were NOT assessed.

## The set, by metadata (2,731 JPEG + 18 TIFF, 29 GB)

- Camera ILCE-6700 firmware 2.00; all JPEG 6192×4128 (5 portrait), sRGB IEC61966-2.1, 8-bit; file size 3.9–15.6 MB, median 10.7 MB.
- Dates in files: 1–12 Nov 2026. 1,152 frames on 12 Nov and 713 on 11 Nov (68 % of the set in two days).
- Lens: 2,601 frames (95 %) Sony E 70-350; 130 frames (5 %) Sony E 11mm F1.8. **No frames from the Viltrox 25 mm.**
- Exposure program: Manual 2,421 (89 %), Aperture priority 304, Program 6.
- White balance flag: **manual/preset 2,483 (91 %), auto 248**. (Spotlight does not expose the Kelvin value or the Creative Look.) A fixed WB means casts are consistent across a session, so one correction can be synced across many frames.
- ISO: ≤200: 772 · 201–800: 422 · 801–1600: 800 · 1601–3200: 452 · 3201–6400: 125 · >6400: 160 (max 12800). So ~27 % of frames are above ISO 1600 and ~10 % above ISO 3200.
- Long exposures: 53 frames ≥ 8 s (all 11 mm, typically 15–20 s, f/1.8–2.2, ISO 1600–3200) — the night-sky set. 58 frames ≥ 1 s.
- Local hour (UTC+2): 1,009 frames in the 19:00 hour (dusk, around sunset in November), 284 at 18:00, 261 at 07:00; 174 frames between 22:00 and 02:00 (floodlit waterhole and stars).
- The 18 TIFFs have the same DSC numbering (e.g. DSC00532.tiff, DSC00709.tiff, DSC00732.tiff): probably earlier exports/edits; not inspected.

## What the viewed frames show (typical problems to solve)

1. **Night sky, DSC00056** (11 mm, f/1.8, 20 s, ISO 3200, manual WB): Large and Small Magellanic Clouds, acacia and building silhouettes. Sky renders **brown-olive with green airglow near the horizon**, a small white light dome on the horizon, thin cloud. Overall dark; foreground pure black. Needs: cooler/neutral WB, modest stretch, noise control, keep silhouettes as silhouettes.
2. **Milky Way, DSC00762** (11 mm, f/2, 20 s, ISO 1600): core low over a pale pan; **clearly underexposed** (the galaxy is faint, sky near-black), foreground mostly black with a paler band. This is the hard JPEG case: the Milky Way must be lifted a lot from the bottom of an 8-bit file → banding/noise risk. Ten-frame stacking would help most here.
3. **Deadvlei, DSC00149** (11 mm, f/11, 1/80 s, ISO 100, ~07:50): person and dead tree **backlit and in shadow**, sunlit orange dune behind, clean blue sky gradient. **Three visible sensor-dust spots in the upper-left sky** (f/11). Shadowed clay floor has a blue cast. Other tourists in frame. Needs: dust-spot removal, subject/shadow lift with a mask, protect dune oranges, careful sky gradient, optional tourist removal.
4. **Giraffe at midday, DSC01825** (128 mm, f/7.1, 1/1250 s, ISO 200, ~10:00): flat hazy light, grey-blue sky, low contrast, subject dead centre; **dust spots visible in the sky (upper left)**; an orange out-of-focus blur intrudes in the bottom-right corner. Needs: dehaze/contrast in moderation, crop (also removes the corner blur), dust spots.
5. **Cheetah in grass, DSC02462** (350 mm, f/6.3, 1/500 s, ISO 1250, ~17:50): subject is **small in the frame** (roughly 10 % of the width) and facing away/right; scene underexposed and cool, dull sky band with dust spots. Needs: heavy crop (≈ 2–3× linear), exposure lift, warm WB, subject separation; Upscale only if printed.
6. **Elephants at floodlit waterhole, DSC01526** (87 mm, f/5, 1/25 s, ISO 12800, ~01:00): **extreme orange monochrome cast** from the floodlight under a fixed WB; blacks fully blocked; red channel very likely clipped on the elephants' flanks. 1/25 s at 87 mm on moving animals → possible motion blur. Needs: partial WB/desaturation rather than "neutralising" (the information for neutral colour is not there), strong but masked noise reduction, or a black-and-white conversion.
7. **Lion in shade at dusk, DSC03658** (163 mm, f/5.6, 1/500 s, ISO 2000, ~19:00): good moment (yawn), subject a fair size; **cool blue-grey cast and low contrast** (open shade after sunset), busy thorn-bush background. Needs: warm WB, lift, subject separation, moderate crop.

## Cross-cutting findings

- **Sensor dust is in the files**: the same upper-left area shows spots in at least three daylight frames from different days (3, 11 Nov). Any frame with sky at f/7–f/11 will need spot removal, and dehaze/contrast will make spots more visible. A synced spot-removal is plausible because the spots stay in the same place.
- **Under-exposure is common** in the dusk and night frames viewed; shadows and midtones need lifting, which is exactly where 8-bit JPEGs are weakest.
- **Colour casts are systematic** (fixed WB): cool in shade/dusk, orange under floodlights, brown-olive at night.
- **Small subjects** with the 70-350 → cropping guidance and Upscale limits matter.
- The big 19:00-hour burst sessions (1,000+ frames) make culling and sync/batch workflow a priority.
