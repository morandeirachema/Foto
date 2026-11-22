# Luminar Neo (Luminar for Desktop 1.29.x, macOS): documentación oficial para editar JPEG y auditoría de la guía de `retoques/`

Nota de método. Versión en español, recomprobada y actualizada el 22 de noviembre de 2026, de `luminar_neo_tools_and_guide_audit.md`. Se descargaron de nuevo como Markdown las 174 páginas de «Luminar for Desktop» que lista hoy <https://support.skylum.com/llms.txt> (la versión anterior contaba 175), más la página de licencias, que ya no está en el índice pero responde. «No documentado» significa: sin resultado en esas páginas. Se leyeron completos los capítulos `00`–`20` y el `README.md` de `/Users/chema/code/Foto/retoques/` (no `guia-completa.md`) en su estado actual. Las URL van sin el sufijo `.md`. Las citas literales se dejan en inglés. Skylum no publica rangos de deslizadores; las únicas pistas numéricas son Vignette (−50), Mystical (<40), Sharpening Masking (30–70) y el valor por defecto de Lightness en Atmosphere AI (100). El detalle de la verificación línea a línea está en `notas-de-investigacion/verificacion-de-datos/luminar-y-retoques.md`.

---

# PARTE A — Lo que Skylum documenta oficialmente

## A1. Develop en un JPEG: qué controles existen y cuáles son solo para RAW

### Takeaway
En un JPEG la herramienta se llama «Develop» (no «Develop RAW») y tiene las mismas secciones (Light, Blacks & Whites, Curves, Color, Sharpness, Noise Reduction, Optics, Transform). Tres cosas están documentadas como exclusivas de RAW: el desplegable de presets de White Balance, Auto Distortion Corrections y Auto Fix Chromatic Aberrations. Camera Profile se describe solo para RAW.

### Cited Findings
- "The RAW indicator will only show next to Develop when an unedited raw file is opened for editing"; Develop RAW se aplica solo como primera herramienta en imágenes RAW — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- White Balance: el cuentagotas sirve en cualquier archivo; "If you are working with a raw file, you can use the White Balance drop-down menu to choose from various presets" — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- Camera Profile (DCP): "For maximum control over your raw files" — [Develop RAW/Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- Optics: "The exact controls you'll see vary between standard and raw files." Auto Distortion Corrections "(raw only)", Auto Fix Chromatic Aberrations "(raw only)"; Auto Defringe, Lens Distortion, Devignette y Devignette Midpoint no llevan esa etiqueta — misma página.
- Light: Exposure, Smart Contrast ("limit color shift and prevent details from becoming blocked up"), Highlights, Shadows. Blacks & Whites: Whites, Blacks — misma página.
- Curves: selectores white/red/green/blue; "You can add up to 10 control points"; "Anchor points can be deleted by double-clicking them". La página dice además "Drag up to add contrast to an area and drag down to lighten the area", al revés de la convención habitual — misma página.
- Color: Temperature ("adding Cyan or Yellow"), Tint (verde/magenta), Saturation, Vibrance — misma página.
- Develop tiene su propia sección Sharpness (Sharpen, Radius, Masking; "Optimal masking comes from a setting in the range of 30 to 70"; resultados visibles "at a 100% or higher Zoom level") y su propia Noise Reduction (Luminosity Denoise, Color Denoise, Boost) — misma página.
- Transform: Vertical, Horizontal, Aspect — misma página.
- Auto Adjust: recalcula Exposure, Shadows, Highlights, Whites, Blacks, Saturation y Curves; sobrescribe lo ya ajustado en esos controles; "available exclusively for subscribers or lifetime owners with an Upgrade Pass" — misma página.
- Atajo del cuentagotas: `W`, "accessible when Develop > Color is open" — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- "Masking is not available in Noiseless RAW and Develop RAW tools. Once you apply any adjustments, these tools will automatically switch to their non-RAW versions" (restricción de RAW; no afecta a JPEG) — [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai)
- "If you're editing a **RAW file**, you'll have the most flexibility with white balance"; "once pixels are maxed out to white, there's no color information left to recover" — [How to make a photo brighter](https://support.skylum.com/luminar-for-desktop-tips/how-to-make-a-photo-brighter)

### Inferences
- Para los JPEG de la guía: sin presets de balance de blancos, sin correcciones automáticas de lente y sin perfil de cámara. Quedan Lens Distortion, Devignette y Auto Defringe.
- El consejo «30–70» aparece dos veces: en Develop → Sharpness → Masking y en Details → Sharpening Masking.

### Gaps
- No se documenta si Temperature y Tint se muestran en kelvin o en unidades relativas en un JPEG, ni su sentido (qué lado es más frío), ni ningún rango.
- No se dice de forma expresa que Camera Profile se oculte en JPEG.
- La frase "drag down to lighten" de Curves contradice la convención; no se pudo comprobar en la aplicación.

## A2. Herramientas Essentials, Image Quality, Professional, Landscape y Creative

### Takeaway
Todas las herramientas que usa la guía están documentadas al nivel de «qué hace cada deslizador», casi sin orientación numérica. Noiseless AI está documentado para archivos no RAW. «Relight AI» fue sustituido por Light Depth. Dehaze, Golden Hour y Foliage Enhancer están dentro de la herramienta Landscape.

### Cited Findings
- **Enhance AI**: Accent AI "can substitute for many traditional controls, including shadows, highlights, contrast, tone, saturation, exposure, and details"; Sky Enhancer AI "works from the blue hour in the morning to the blue hour in the evening" y "is not designed to work with night skies"; controles en gris = cielo no reconocido. Enhance AI Improved desde 1.29.0 para licencias que lo incluyan: misma interfaz, mejores luces, menos saturación, menos halos — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- **Structure AI**: Amount, Boost ("more aggressive. It offers an HDR-like look"); "human-aware, so it doesn't overprocess people"; Amount negativo desenfoca; "use multiple instances for a heavier blur effect" — [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai)
- **Details**: Small / Medium / Large Details, Sharpen; Details Masking = Details Protection + Details Masking; Sharpening Masking = Sharpening Radius + Sharpening Masking (a la derecha, zona enfocada menor; consejo "30 to 70"); valores negativos desenfocan — [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- **Denoise**: Luminosity Denoise, Color Denoise, Boost — [Denoise](https://support.skylum.com/editing-tools/essential-tools/denoise)
- **Noiseless AI**: "works with various image formats, including raw and non-raw files, and offers optimal results when applied to raw photos"; propone "low, middle, or high"; Luminosity Denoise, Color Denoise, Details ("can reintroduce noise or create artifacts"), Sharpness (riesgo de halos). "Tools > Image Quality section" — [Noiseless AI](https://support.skylum.com/editing-tools/image-quality-tools/noiseless-ai)
- **Supersharp AI**: Universal y Motion Blur; Low, Middle, High; Face Enhancer AI — [Supersharp AI](https://support.skylum.com/editing-tools/image-quality-tools/supersharp-ai). "Some artifacts might appear in the highest settings"; se puede limitar con máscara Brush; "click and hold on the eye symbol near the Supersharp AI tab" — [How to reconstruct a blurry part of a photo](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- **Color**: Saturation, Vibrance, Remove Color Cast (un deslizador), HSL (Hue se desplaza hacia el color siguiente o anterior "in the list", p. ej. "from Orange to Yellow"), Hue Shift. No se enumeran los canales — [Color](https://support.skylum.com/editing-tools/essential-tools/color)
- **Black & White**: Convert to B&W; modos Luminance y Saturation con Red, Yellow, Green, Cyan, Blue, Magenta; color selectivo con la máscara — [Black & White](https://support.skylum.com/editing-tools/essential-tools/black-and-white)
- **Vignette**: Choose Subject, Amount, Size; avanzados Mode (pre-crop/post-crop), Roundness, Feather, Inner Light; "For a realistic picture, don't lower the Amount below -50" — [Vignette](https://support.skylum.com/editing-tools/essential-tools/vignette)
- **Erase**: Select/Deselect, Size (`[` `]`), Erase, Clear Selection, Restore; Objects Removal: Remove Powerlines, Remove Dust Spots — [Erase](https://support.skylum.com/editing-tools/essential-tools/erase)
- **Clone**: `Cmd+J`; Radius, Softness, Opacity; clic para fijar el origen y Opción-clic "to change the sample point"; `Cmd+Z` deshace un trazo; "switch to another tool to apply" — [Clone](https://support.skylum.com/editing-tools/professional-tools/clone)
- **Supercontrast**: Highlights, Midtones, Shadows y sus tres Balance — [Supercontrast](https://support.skylum.com/editing-tools/professional-tools/supercontrast)
- **Color Harmony**: Brilliance, Warmth, Color Contrast (Amount, Hue), Split Color Warmth (Warm, Cool), Color Balance (Shadows/Midtones/Highlights × Cyan–Red, Magenta–Green, Yellow–Blue) — [Color Harmony](https://support.skylum.com/editing-tools/professional-tools/color-harmony)
- **Dodge & Burn**: Lighten, Darken, Erase, Brush Size, Softness, Strength, Overall Amount; la flecha curva reinicia; se aplica al salir — [Dodge & Burn](https://support.skylum.com/editing-tools/professional-tools/dodge-and-burn)
- **Landscape**: Dehaze ("contrast, clarity, and color adjustments"), Golden Hour, Foliage Enhancer; avanzado Foliage Hue — [Landscape](https://support.skylum.com/editing-tools/landscape-tools/landscape)
- **Atmosphere AI**: Regular = Mode (Fog, Layered Fog, Mist, Haze), Amount, Depth, Lightness (100 por defecto). Improved (1.29.0) = Ground Fog, Wispy Fog, Heavy Fog, Amount, Depth Map, Clouds Drift, Height; avanzados Patchiness, Cloud Size, Vibrance — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai)
- **Twilight Enhancer AI**: presets Blush, Golden, Blue, Emerald, Mauve; Amount, Exposure; Sky; Dawn ("simulates the subtle, warm gradient of light seen during dawn"); Scene Enhancements; Water Reflection; Mask Refinement — [Twilight Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/twilight-enhancer-ai)
- **Sky AI**: "designed to work with flat or blown-out skies"; Scene Relighting (Relight Strength, Relight Saturation, Relight Human); Mask Refinement (Global, Close Gaps, Fix Details); cielos propios en JPEG, mínimo 1.200 px en el lado corto y menos de 10 MB — [Sky AI](https://support.skylum.com/editing-tools/landscape-tools/sky-ai)
- **Sunrays**: "Add a whole new light source to your photo — the sun!" — [Sunrays](https://support.skylum.com/editing-tools/landscape-tools/sunrays)
- **Water Enhancer AI**: Amount, Blue, Green, Original Color, Brightness, Contrast, Depth, Mask Feather; Draw, Erase, Restore — [Water Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/water-enhancer-ai)
- **Light Depth**: "AI-powered depth mapping"; "automatically mimics the classic *Dodge and Burn* technique"; Amount, Depth Mask, Softness, Warmth, Brightness Near/Far, Warmth Near/Far; "has replaced the **Relight AI** tool" — [Light Depth](https://support.skylum.com/editing-tools/creative-tools/light-depth)
- **Film Grain**: Amount, Size, Roughness — [Film Grain](https://support.skylum.com/editing-tools/creative-tools/film-grain)
- **Mood (LUT)**: Choose LUT (.cube), Amount, Contrast, Saturation — [Mood (LUT)](https://support.skylum.com/editing-tools/creative-tools/mood-lut)
- **Toning**: Amount; Highlights/Shadows Saturation y Hue (Hue "Becomes available once you apply Saturation"); Balance — [Toning](https://support.skylum.com/editing-tools/creative-tools/toning)
- **Glow** (Soft Focus, Glow, Orton Effect, Orton Effect Soft), **Mystical** ("keep the value of the Amount slider below 40"), **Dramatic** ("lowers the saturation and the contrast", similar a bleach bypass), **Matte** (Amount, Fade, Contrast, Vividness; Color Toning) — [Glow](https://support.skylum.com/editing-tools/creative-tools/glow), [Mystical](https://support.skylum.com/editing-tools/creative-tools/mystical), [Dramatic](https://support.skylum.com/editing-tools/creative-tools/dramatic), [Matte](https://support.skylum.com/editing-tools/creative-tools/matte)
- **Magic Light AI**: "works best with artificial light sources"; Intensity, Size, Beam width, Glow, Clearness, Number of beams; "you may need to use the **Upgrade** option" — [Magic Light AI](https://support.skylum.com/editing-tools/creative-tools/magic-light-ai)
- **Color Transfer**: referencia, Amount, Color Intensity, Luminosity Intensity, Transition Smoothing, Color Smoothing, Match Similar Objects' Color; no funciona con fotos en blanco y negro — [Color Transfer](https://support.skylum.com/editing-tools/creative-tools/color-transfer)
- **Blur**: "three distinct blur styles […]: Gaussian, Motion, and Twisted", más un apartado Tilt-Shift — [Blur](https://support.skylum.com/editing-tools/creative-tools/blur)
- **Studio Light**: Smooth, Light Contrast, Depth, entre otros; pensada para retrato — [Studio Light](https://support.skylum.com/editing-tools/portrait-tools/studio-light)
- **Face AI → Face Light**: "Adjust the lighting of a face without impacting the rest of the scene" — [Face AI](https://support.skylum.com/editing-tools/portrait-tools/face-ai)
- **Crop AI**: no destructivo; "The crop tool settings are not saved with presets". Improved (1.29.0): Aspect Ratio, Rotate, Flip, Smart Compositions (Rule of Thirds, Golden Ratio, Golden Spiral, Golden Triangle, Centered; "More Compositions"), Grid, Straighten, Auto Straighten. Regular: Composition AI, Horizon Alignment; Ratio con Free, Original, Transposed, 1:1, 4:5, 8.5:11, 5:7, 2:3, 4:3, 21:9, 16:9, 16:10, Facebook Cover, Facebook Feed, Enter Custom; "switch to another tool to apply the crop" — [Crop AI Tool](https://support.skylum.com/editing-tools/crop-ai-tool)
- **Upscale**: "up to 6X"; copia en la carpeta Upscale con sufijo `_upscale`; entrada mínima 257×257 px, entrada máxima 16.000 px y salida máxima 32.000 px en el lado largo — [Upscale](https://support.skylum.com/extra-tools/upscale). Factores "2x, 4x, and 6x"; reducir ruido antes y enfocar después con Structure AI o Details — [Best practices with Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale)
- **GenErase / GenSwap / GenExpand**: se inician desde el catálogo; cada Save crea un TIF. GenErase: un objeto cada vez, selección generosa, pulsar Erase de nuevo da otro resultado. GenExpand: hasta el 25 %; en la versión Regular, "about 10%" y "focus on one side", indicación opcional en inglés y conexión a internet; Improved (1.29.0) sin texto y "Up to two sides at a time" — [GenErase](https://support.skylum.com/extra-tools/generative-tools/generase), [GenSwap](https://support.skylum.com/extra-tools/generative-tools/genswap), [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand)
- **Restoration** (pestaña Extra, Enhancement): restaura fotos antiguas; modos Full, Color, Scratches; requiere internet — [Restoration](https://support.skylum.com/extra-tools/restoration)
- **Flujo oficial más cercano a fauna (mascotas)**: Blur → Gaussian con Mask AI en el fondo; Studio Light "brighten shadows on darker pets"; Color → HSL → Saturation; Supersharp AI ("use **Universal** or **Low** setting"); máscaras Mask AI/Object Select sobre el animal; Dodge & Burn para el volumen — [Best practices in Pet Photography](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)

### Inferences
- Una página de consejos sigue describiendo Relight AI ([How to make a photo brighter](https://support.skylum.com/luminar-for-desktop-tips/how-to-make-a-photo-brighter)): está anticuada respecto a la página de Light Depth.
- El «~10 %» de GenExpand procede de las pautas de la versión Regular; para Improved Skylum solo dice "use smaller expansion areas".

### Gaps
- No se documenta si Upscale, las generativas o las fusiones trabajan sobre la foto editada o sobre el original.
- Sin documentación sobre Noiseless AI en estrellas, pelo o JPEG ya filtrados por la cámara.
- Los canales de HSL no se enumeran.
- Studio Light con animales solo lo respalda el consejo de mascotas.

## A3. Máscaras

### Takeaway
Hay siete tipos de máscara por herramienta (Brush, Linear Gradient, Radial, Mask AI, Object Select AI, Luminosity, Color); las capas solo ofrecen cuatro. Mask AI tiene nueve categorías fijas y ninguna para animales. Acciones: Feather, Shift Edge, Fill, Clear, Invert, Copy, Paste, Show.

### Cited Findings
- "Luminar for Desktop offers seven types of masks"; primero se ajusta la herramienta y después se abre su pestaña Masking — [Masking Options](https://support.skylum.com/editing-tools/masking-options)
- Mask AI "detects up to nine separate elements in a photo: people, skies, buildings, vehicles, water, plants, mountains, and both natural and artificial ground" — [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai)
- Object Select AI: al pasar el cursor resalta el objeto; clic para seleccionarlo; más clics para añadir; "Subtract" para quitar; "in most tools or Layers" — [Object Select AI](https://support.skylum.com/editing-tools/masking-options/object-select-ai)
- Luminosity: un deslizador de oscuro a claro, vista previa y feathering — [Luminosity Masking](https://support.skylum.com/editing-tools/masking-options/luminosity-masking)
- Color: clic para tomar el color y Range Slider — [Color Masking](https://support.skylum.com/editing-tools/masking-options/color-masking). Color Masking figura entre las herramientas de mejoras anteriores sujetas a licencia — [How do I know if I need to upgrade my license?](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership/how-do-i-know-if-i-need-to-upgrade-my-license)
- Brush: Paint/Erase; Size, Softness, Strength; máscara roja translúcida — [Brush Mask](https://support.skylum.com/editing-tools/masking-options/brush-mask)
- Radial: Standard protege el centro, Inverted aplica dentro; círculo interior = tamaño, exterior = difuminado; rotable. Linear Gradient: líneas superior e inferior, punto central para colocar y arrastre junto al punto para rotar; ambas se pueden afinar con el pincel — [Using a Radial Mask](https://support.skylum.com/editing-tools/masking-options/using-a-radial-mask), [Linear Gradient Mask](https://support.skylum.com/editing-tools/masking-options/linear-gradient-mask)
- Acciones de máscara — [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions)
- Máscaras de capa: solo Brush, Linear Gradient, Radial Gradient y Mask AI — [Creating a Layer Mask](https://support.skylum.com/editing-tools/masking-options/creating-a-layer-mask)
- En edición de máscaras: `X` cambia de modo (Brush, Erase, Dodge&Burn); `Cmd+I` invierte; `/` muestra u oculta; `B`, `R`, `G`, `A` — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- **Misma herramienta más de una vez**: "Click the **Edits** tab to make changes to a tool that was applied. Notice that you can add the same tool more than once." — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view); "Tools can be added in any order, multiple times, and with unique masks" — [Layers](https://support.skylum.com/editing-tools/layers); "use multiple instances" — [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai)

### Inferences
- Skylum documenta que una herramienta puede aplicarse varias veces (tres páginas); no documenta el gesto ni si cada instancia tiene máscara independiente fuera del contexto de las capas.

### Gaps
- Sin límites documentados (número de máscaras, combinación o intersección).
- Sin documentación sobre la precisión de las máscaras en animales, pelo o escenas nocturnas.

## A4. Fusiones (HDR Merge, Panorama Stitching, Focus Stacking) y apilado nocturno

### Takeaway
Ninguna de las tres páginas dice qué formatos de entrada acepta; las salidas son TIFF en una carpeta propia. Límites documentados: Focus Stacking hasta 100 tomas, HDR Merge por lotes hasta 1000 imágenes, panorama hasta 15.000 px. No hay apilado por media ni de estrellas.

### Cited Findings
- HDR Merge: agrupa horquillados por EXIF; "up to 1000 images"; Auto Alignment, Chromatic Aberration Reduction, Ghost Reduction (imagen de referencia e intensidad); "Continue"; "saved as a Tiff file in the HDR Folder"; trípode recomendado — [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge)
- Focus Stacking: "up to 100 photos"; "corrects lens and chromatic aberration in raw files"; engranaje → Auto Alignment, Chromatic Aberration Reduction; "Stack"; TIFF en la carpeta Focus Stacking — [Focus Stacking](https://support.skylum.com/extra-tools/focus-stacking)
- Panorama Stitching: detecta horquillados; opciones de distorsión, viñeteado, aberración cromática y fantasmas; "Start"; proyecciones spherical, cylinder, mercator, plane, fisheye; panoramas a partir de vídeo, con consejos de toma que se dan para ese caso; "the maximum export size is **15,000 px**" — [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching)
- Ubicación: pestaña Extra → Merge (HDR Merge, Focus Stacking, Panorama Stitching), Enhancement (Upscale, Restoration), Generative — [Luminar for Desktop walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- "The 8 pro-level tools (ex-Extensions): Supersharp AI, Noiseless AI, Upscale AI, Focus Stacking, Background Removal AI, HDR Merge, Magic Light AI, and Panorama Stitching" — [Subscription, Prime and X Membership](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership)

### Inferences
- La búsqueda de «averag», «median» y «stack» en las 174 páginas solo devuelve Focus Stacking, el desenfoque gaussiano y el promedio de luminancia del histograma: el apilado por media no es una función documentada. Hace falta un programa aparte, como dice la guía.

### Gaps
- JPEG como entrada de las fusiones: ni permitido ni excluido. Máximo de tomas por HDR individual: no documentado.

## A5. Cielo nocturno y astrofotografía

### Takeaway
La documentación no tiene ninguna herramienta ni guía de astrofotografía. La única mención de cielos nocturnos es la exclusión de Sky Enhancer AI.

### Cited Findings
- Única página con «night skies» entre las 174: Sky Enhancer AI "is not designed to work with night skies" — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- Twilight Enhancer AI apunta a la hora azul y la dorada; Dawn "simulates" luz — [Twilight Enhancer AI](https://support.skylum.com/editing-tools/landscape-tools/twilight-enhancer-ai)
- Magic Light AI es la herramienta documentada para farolas de noche — [Magic Light AI](https://support.skylum.com/editing-tools/creative-tools/magic-light-ai)
- El ruido se atribuye a ISO alto, subexposición o exposición larga — [Denoise](https://support.skylum.com/editing-tools/essential-tools/denoise)

### Inferences
- El capítulo nocturno de la guía se construye por fuerza con herramientas generales; ninguna de sus recetas puede «verificarse con Skylum».

### Gaps
- No recomprobado en esta sesión: la entrada del blog de Skylum sobre la Vía Láctea y el artículo de PetaPixel que citaba la versión anterior. No se toma ningún dato de ellos.

## A6. Exportar, imprimir y compartir

### Takeaway
La versión 1.29 trajo un espacio de exportación a pantalla completa, Home Printing (ICC, soft proofing) y Order Prints. Controles documentados: Format, Quality, Sharpen, Color Space, Resize (Long Edge, Short Edge, Dimensions), Resolution y Signature. No se documentan opciones de metadatos, la lista de espacios de color, los niveles de Sharpen ni un selector de profundidad de bits.

### Cited Findings
- Menú Export: New Export, Export with previous, Quick Export, Order Prints, Print..., Publish to Space; "Luminar remembers your export settings between sessions"; cola de varias fotos con "Remove from Export" — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- Formatos: JPEG, PNG, TIFF ("works with a depth of 8 bits or 16 bits per channel"), JPEG 2000, PSD ("cannot write a layered file"), PDF, DNG — misma página.
- Único espacio de color nombrado: sRGB (recomendado para Facebook), en una página con aviso de interfaz posiblemente antigua — [Resizing an image](https://support.skylum.com/saving-and-exporting-files/resizing-an-image)
- "Luminar for Desktop uses a standard color space called **sRGB**"; "It does not read your custom monitor profile" (aviso de interfaz antigua; pasos para Windows) — [Why do photo colors change after export](https://support.skylum.com/why-do-photo-colors-change-after-export-in-luminar-for-desktop)
- Home Printing: perfiles ICC recomendados o importados, Rendering Intent (Perceptual/Relative), Soft Proofing (no disponible con "Managed by Printer"), Print Sharpening (None, Low, Medium, High), Print Resolution, 16-Bit Output, Zoom/Rotate to Fill, Signature, "Save as File" en JPEG o PDF — [Home Printing](https://support.skylum.com/printing/home-printing)
- Order Prints: productos según el país de entrega; aviso si la resolución es baja para el tamaño elegido — [Order Prints](https://support.skylum.com/printing/order-prints)
- Atajos: `Shift+Cmd+E` Export, `Cmd+P` Print — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- Notas de versión: "October 28, 2026 Luminar 1.29.0 […] New Export. Exporting now opens a full-screen mode with a live preview"; "Print at home. A new print mode with ICC profile support and soft proofing"; "Order prints from a pro lab" — [Skylum changelog](https://skylum.com/whats-new/luminar-neo/68)

### Inferences
- La búsqueda de «metadata», «EXIF» y «GPS» en las páginas de exportación e impresión no da nada pertinente: quitar el GPS al exportar no está documentado, como dice la guía.

### Gaps
- Valores de Sharpen, escala de Quality, espacios de color disponibles y profundidad de bits del TIFF al exportar: no documentados.

## A7. Catálogo, flujo no destructivo, presets, sincronización, historial, antes/después, histograma

### Takeaway
Las ediciones se guardan por imagen como archivos `.state` en el catálogo, con historial ilimitado en la pestaña Edits; los originales se enlazan, no se copian. El antes/después tiene controles en pantalla además de `\`. Aplicar un preset o un resultado de AI Assistant sobrescribe las ediciones.

### Cited Findings
- El panel derecho tiene cinco pestañas: Presets, Tools, Edits, Extra, Info — [Luminar for Desktop walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- Ediciones guardadas como archivo **.state** por imagen; "allows unlimited undos"; se ven en la pestaña Edits — [Saving Adjustments in a Catalog](https://support.skylum.com/saving-and-exporting-files/saving-adjustments-in-a-catalog)
- Al añadir una carpeta, "none of your photos are moved"; se crean miniaturas y enlaces — [Adding a Folder for editing](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/adding-a-folder-for-editing). Mover o renombrar carpetas dentro de Luminar las cambia en el disco — [Organize Images](https://support.skylum.com/organizing-images/organize-images)
- Copia del catálogo: File > Catalog > Backup; File > Catalog > Restore from Backup; en macOS, mantener Opción al abrir muestra la ventana «Backups» — [Backing Up a Catalog](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-a-catalog), [Backing Up and Restoring Your Edits](https://support.skylum.com/backing-up-and-restoring-your-edits)
- Copias virtuales: `Cmd + '`, clic derecho → Virtual Copy o menú Actions — [Virtual Copies](https://support.skylum.com/organizing-images/virtual-copies)
- Sincronizar: borde naranja en la activa y blanco en las demás; clic derecho → Adjustments > Sync Adjustments o `Shift+Cmd+S`; las herramientas de IA se adaptan mejor; "Tools like Crop, Erase, and Background Removal cannot be synced"; las miniaturas son previsualizaciones JPEG — [Syncing Adjustments](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/syncing-adjustments)
- Presets: Actions → Save as Preset → My Presets; Edit, Rename, Delete, Show in Finder — [Customizing Presets](https://support.skylum.com/presets/customizing-presets). "Applying a Preset will overwrite any changes you made to the image"; «For This Photo» sugiere presets; Reset Adjustments no afecta a Crop AI — [Browsing and Applying Presets](https://support.skylum.com/presets/browsing-and-applying-presets)
- Favorites: clic derecho en una herramienta → "Add to Favorites" — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view)
- Antes/después: `\` mantenida; "Visibility Icon. Click to view the before and after if the image is edited", en el panel de acciones (View > Show Photo Actions Panel) — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images); "Before/After slider" y símbolo del ojo por herramienta — [How to reconstruct a blurry part of a photo](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- Histograma: View > Show Histogram; un clic alterna la vista conjunta, R, G, B y luminancia; los dos triángulos muestran píxeles fríos (negro puro, en azul) y calientes (blanco puro, en rojo); `J` alterna los avisos — [Histogram](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/histogram)
- Filmstrip en Edit para cambiar de foto y sincronizar — [Filmstrip](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/filmstrip)
- Pares RAW+JPEG: View > Raw + JPG Pairs — [Handling Raw + JPEG Pairs](https://support.skylum.com/organizing-images/handling-raw-+-jpeg-pairs)
- AI Assistant: requiere internet; aplicar su resultado "replaces all previous modifications made to the photo" — [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant)
- Smart Search (`Cmd+F`): búsqueda por contenido ("tree", "beach") — [Smart Search](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/smart-search)

### Gaps
- La función Compare (`;`) no se describe en ningún sitio más allá del nombre del atajo.
- Copy/Paste Adjustments solo aparecen como atajos, sin explicar qué se copia.
- El contenido de la pestaña Info solo se describe como "photo details and metadata".

## A8. Atajos oficiales de macOS

### Takeaway
El capítulo 17 de la guía coincide con la tabla oficial de macOS. Faltan en la guía algunos atajos oficiales, y la propia documentación de Skylum se contradice en el de AI Assistant.

### Cited Findings (todo de [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys), pestaña macOS, salvo indicación)
- General: `\` antes/después (mantener); barra espaciadora = imagen única/galería en el catálogo y encajar/100 % en edición; `→`/`←`; Cmd-clic, Shift-clic; `Cmd+F` (solo en el catálogo); `Cmd+M`; `J`; `Cmd+Z`; `Opt+←`/`Opt+→`; Ctrl+clic para el menú contextual.
- File: `Opt+Shift+N` Add Folder with Images; `Cmd+N` New Album; `Cmd+O` Edit Single Image; `Shift+Cmd+E` Export; `Cmd+W`; `Opt+Cmd+W`; `Shift+Cmd+P`; `Cmd+P` Print.
- Edit: `Cmd+Z`, `Shift+Cmd+Z`, `Cmd+X/C/V`, `Cmd+A`, `Cmd+D`, barra espaciadora + arrastrar para moverse.
- Image: `P`, `X`, `U`; `1–5`, `0`; `Cmd+[` / `Cmd+]` girar; `Cmd+'` Create Virtual Copy; `Shift+Cmd+S` Sync Adjustments; `Shift+Cmd+R` Revert to Original (también listado como «Reset Adjustments»); `Cmd+Delete`; `Cmd+R` Show in Finder.
- View: `L`; `T`; `E`; `I`; `Cmd++`, `Cmd+–`, `Cmd+1`, `Cmd+0`; `;` Compare; `Ctrl+Cmd+F` o `Fn`; `F` vista previa a pantalla completa.
- Tools: `C`; `W` (con Develop > Color abierto); `Cmd+J` Clone & Stamp; Opción cambia la zona de origen; `Cmd+E` Erase; `X` en recorte gira la proporción; `Ctrl+K` Open AI Assistant.
- Mask Editing: `Cmd+I`; `[` `]` radio; `Shift+[` `Shift+]` suavidad; `X` cambia de modo; `/`; `B`, `R`, `G`, `A`.
- Contradicción: la página de AI Assistant da `Cmd+K` en macOS — [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant); la tabla de atajos, `Ctrl+K`.
- La página de marcas pide pulsar `G` para Gallery View en un paso y `L` en otro; `G` no figura con ese uso en la tabla — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images)

### Gaps
- Sin atajos documentados para las pestañas Edits y Extra, las máscaras Luminosity, Color y Object Select, Dodge & Burn o el histograma. Comportamiento con teclados no estadounidenses: no documentado.

## A9. Versión 1.29 y licencias

### Takeaway
La 1.29.0 (28 de octubre de 2026) trae el nuevo Export, la impresión y las versiones «Improved» de Crop AI, Atmosphere AI, Enhance AI, AI Assistant y GenExpand, cada una limitada a «eligible licenses». macOS 13 o posterior es obligatorio desde la 1.28.1.

### Cited Findings
- 1.29.0, 28 de octubre de 2026: New Export; Print at home; Order prints; "Crop now suggests up to 12 compositions" y "a new Auto button straightens the horizon"; niebla 3D con Clouds Drift y Height; Enhance rehecho; "Luminar now supports macOS 27". Entradas anteriores: 1.28.1 (16 de septiembre de 2026) y 1.28.0 (5 de agosto de 2026, "Meet a fresh design"). En el registro no aparece ninguna 1.29.1 o posterior — [Skylum changelog](https://skylum.com/whats-new/luminar-neo/68)
- Herramientas Improved "available starting with Luminar for Desktop 1.29.0 for users with eligible licenses": [Crop AI](https://support.skylum.com/editing-tools/crop-ai-tool), [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai), [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai), [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand), [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant)
- La suscripción incluye las herramientas "Fall Upgrade 2026 tools (including Crop 2.0, Atmosphere 2.0, AI Assistant 2.0, Enhance AI 2.0, and more — *coming Fall 2026*)" y las ocho herramientas profesionales — [Subscription, Prime and X Membership](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership)
- Una licencia de por vida puede no incluir Pro Tools o Generative Tools; el Upgrade Pass 2025/26 añade las Pro tools y "tools from previous upgrades (such as Auto Adjust, Color Transfer, and Color Masking)"; las generativas, "available until December 31, 2026". Esta página ya no está en `llms.txt`, pero respondió 200 — [How do I know if I need to upgrade my license?](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership/how-do-i-know-if-i-need-to-upgrade-my-license)
- "macOS 13.0 or higher is required (starting from Luminar for Desktop 1.28.1)"; Intel Core i5 de 8.ª generación o Apple M1–M4 — [System Requirements](https://support.skylum.com/about-luminar-for-desktop/system-requirements)

### Inferences
- Con una licencia de por vida sin pases pueden faltar Noiseless AI, Supersharp AI, Upscale, Magic Light AI, Color Masking y las generativas; entonces solo queda la alternativa de la guía (Denoise, Details).

### Gaps
- La documentación no define qué licencia es «eligible» para cada herramienta Improved.
- No recomprobado: los análisis de terceros (Phototrend, Fstoppers) que citaba la versión anterior.

## A10. Orientación oficial sobre JPEG y RAW, fauna, paisaje y astro

### Takeaway
La documentación de soporte no tiene un flujo pensado para JPEG ni flujos de fauna, paisaje o astrofotografía. Lo más cercano es el consejo de mascotas, el de aclarar una foto y comentarios sueltos sobre RAW y no RAW.

### Cited Findings
- Noiseless AI rinde mejor en RAW y funciona en no RAW — [Noiseless AI](https://support.skylum.com/editing-tools/image-quality-tools/noiseless-ai)
- "when exporting JPEG files, your images will lose quality due to compression. Saving your photos in the TIFF format creates archival-quality files" — [Backing Up Your Photos](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-your-photos)
- Entradas no RAW admitidas: PNG, JPEG, TIFF (8 y 16 bits), PSD, HEIC — [Supported File Types and Cameras](https://support.skylum.com/about-luminar-for-desktop/supported-file-types-and-cameras)
- Consejo de mascotas (ver A2) — [Best practices in Pet Photography](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)

### Gaps
- No recomprobado: la página comercial de fauna de Skylum, la entrada del blog sobre Noiseless AI y el artículo de Nat Hab que citaba la versión anterior.
- No se encontró ninguna prueba independiente y controlada de Noiseless AI en JPEG frente a RAW.

---

# PARTE B — Auditoría de la guía (`retoques/00`–`20`), estado a 22 de noviembre de 2026

## B1. Herramientas y opciones documentadas que la guía no cubre o usa poco

### Takeaway
La guía ya incorpora buena parte de lo que faltaba en la auditoría anterior (pestaña Edits, histograma por canales, icono Visibility, Sharpness de Develop, Details Protection, Supersharp con máscara, Home Printing, copia del catálogo, aviso de presets). Siguen sin cubrir funciones secundarias: Auto Adjust, los controles avanzados de Vignette, Blur con máscara, las exportaciones rápidas, Order Prints y el detalle de las licencias.

### Cited Findings — ya cubierto desde la auditoría anterior
- Pestaña **Edits** y las cinco pestañas (`02-luminar-por-dentro.md:12`) — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- **Histograma**: View > Show Histogram, canales y triángulos (`01-conceptos-basicos.md:73–74`) — [Histogram](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/histogram)
- **Icono Visibility** (`16-errores-y-lista.md:79`, `17-atajos.md:83`) — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images)
- **Develop → Sharpness** y **Details Protection** (`04-flujo-base.md:89–90`) — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop), [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- **Supersharp AI con máscara Brush** (`04-flujo-base.md:152`) — [How to reconstruct a blurry part of a photo](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- **Sunrays** marcado como herramienta que añade contenido (`14-etica.md:28`) — [Sunrays](https://support.skylum.com/editing-tools/landscape-tools/sunrays)
- **GenExpand Improved** a dos lados (`12-varias-fotos.md:58`) — [GenExpand](https://support.skylum.com/extra-tools/generative-tools/genexpand)
- **Factores de Upscale** y orden ruido antes / enfoque después (`12-varias-fotos.md:49–51`) — [Best practices with Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale)
- **Home Printing** (`13-exportar.md:101`) — [Home Printing](https://support.skylum.com/printing/home-printing)
- **Copia del catálogo** con sus comandos (`11-trabajar-en-serie.md:58`) — [Backing Up a Catalog](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/catalog-files/backing-up-a-catalog)
- **Aviso de que un preset sobrescribe** (`11-trabajar-en-serie.md:30`) — [Browsing and Applying Presets](https://support.skylum.com/presets/browsing-and-applying-presets)
- **Modos de Atmosphere AI Improved** nombrados (`06-herramientas-avanzadas.md:115`) — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai)

### Cited Findings — sigue sin cubrir
- **Auto Adjust** en Develop (sujeto a licencia) — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- **Curves**: el doble clic borra un punto; no está en 6.1 — misma página.
- **Vignette**: Size, Roundness, Feather y Mode (pre-crop/post-crop); la guía solo usa Amount, Inner Light y Choose Subject — [Vignette](https://support.skylum.com/editing-tools/essential-tools/vignette)
- **Erase**: Restore y Clear Selection — [Erase](https://support.skylum.com/editing-tools/essential-tools/erase)
- **Sharpening Radius** (Details) y **Radius** (Develop → Sharpness, nombrado pero sin explicar) — [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- **Face Enhancer AI** de Supersharp AI — [Supersharp AI](https://support.skylum.com/editing-tools/image-quality-tools/supersharp-ai)
- **Ojo por herramienta** y **Before/After slider** — [How to reconstruct a blurry part of a photo](https://support.skylum.com/luminar-for-desktop-tips/how-to-reconstruct-a-blurry-part-of-a-photo)
- **Blur → Gaussian con máscara de fondo** y **Studio Light** para animales oscuros (consejo oficial de mascotas). La guía lista Blur y Studio Light solo en la tabla de categorías y recomienda no desenfocar el fondo: es una decisión de criterio — [Best practices in Pet Photography](https://support.skylum.com/luminar-for-desktop-tips/best-practices-in-pet-photography)
- **Controles de Atmosphere AI** más allá del modo y Amount (Depth, Lightness; Depth Map, Clouds Drift, Height, Patchiness, Cloud Size, Vibrance) — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai)
- **Enhance AI Improved** y **AI Assistant**: las notas de versión de la guía (`02:27`, `19:25`) hablan de Improved en general — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai), [AI Assistant](https://support.skylum.com/editing-tools/ai-assistant)
- **HDR Merge por lotes** (hasta 1000 imágenes, agrupación por EXIF) y **panoramas HDR o de vídeo** — [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge), [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching)
- **Restoration** en la pestaña Extra — [Restoration](https://support.skylum.com/extra-tools/restoration)
- **Export**: Quick Export, Export with previous y la cola de varias fotos; **Order Prints** y su aviso de resolución; del modo de impresión, Rendering Intent, 16-Bit Output y «Save as File» — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image), [Order Prints](https://support.skylum.com/printing/order-prints), [Home Printing](https://support.skylum.com/printing/home-printing)
- **Restaurar copias manteniendo Opción al arrancar** — [Backing Up and Restoring Your Edits](https://support.skylum.com/backing-up-and-restoring-your-edits)
- **«For This Photo»** y **Favorites** (fijar herramientas arriba), útil para el flujo fijo de 10 pasos — [Browsing and Applying Presets](https://support.skylum.com/presets/browsing-and-applying-presets), [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view)
- **Mover o renombrar dentro de Luminar cambia el disco**: la guía dice que Luminar «no toca tus JPEG» (`02:31`, `11:58`) sin esa salvedad — [Organize Images](https://support.skylum.com/organizing-images/organize-images)
- **Licencias por herramienta** (Noiseless AI, Supersharp AI, Upscale, Magic Light AI, fusiones, generativas, Color Masking, Auto Adjust): la guía solo da una nota genérica — [How do I know if I need to upgrade my license?](https://support.skylum.com/something-useful/difference-between-luminar-for-desktop-subscription-prime-and-x-membership/how-do-i-know-if-i-need-to-upgrade-my-license)
- **Vista de luminancia del histograma** — [Histogram](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/histogram)
- Atajos que faltan en el capítulo 17: `Cmd+O`, `Cmd+[`/`Cmd+]`, `Cmd+A`/`Cmd+D`, `Cmd+R`, `Cmd+Delete`, `Cmd+P`, `Ctrl+Cmd+F`, `Opt+←/→`, `X` en modo máscara, AI Assistant — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- Páginas de Skylum que sostienen afirmaciones de la guía y faltan en `20-fuentes.md`: [Structure AI](https://support.skylum.com/editing-tools/essential-tools/structure-ai), [Virtual Copies](https://support.skylum.com/organizing-images/virtual-copies), [Adding a Folder for editing](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/adding-a-folder-for-editing), [Saving Adjustments in a Catalog](https://support.skylum.com/saving-and-exporting-files/saving-adjustments-in-a-catalog), [Background Removal AI](https://support.skylum.com/editing-tools/layers/background-removal-ai), [Resizing an image](https://support.skylum.com/saving-and-exporting-files/resizing-an-image), [Filmstrip](https://support.skylum.com/how-to-use-luminar-for-desktop/catalog/filmstrip) y el [registro de cambios](https://skylum.com/whats-new/luminar-neo/68)

### Inferences
- Lo de más valor que queda por añadir a una guía centrada en JPEG: el ojo por herramienta (para el hábito de «comparar a menudo»), Favorites, la salvedad de mover y renombrar, y la tabla de licencias.

### Gaps
- Si Studio Light y Face AI responden con animales no está documentado más allá del consejo de mascotas.

## B2. Afirmaciones de la guía que la documentación contradice o no respalda

### Takeaway
Las seis contradicciones de la auditoría anterior están corregidas. Hoy queda una contradicción literal (la dirección de los puntos de Curves), dos referencias internas equivocadas, y un grupo de imprecisiones y afirmaciones sin página que las respalde, con Compare (`;`) a la cabeza.

### Cited Findings — corregido desde la auditoría anterior
- Presets de White Balance en JPEG: la guía dice ahora que son para RAW (`04-flujo-base.md:62`) — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- «Solo el atajo muestra el original»: sustituido por el icono Visibility (`17-atajos.md:83`) — [Marking Favorite and Rejected Images](https://support.skylum.com/organizing-images/marking-favorite-and-rejected-images)
- «Tres pestañas»: ahora cinco (`02-luminar-por-dentro.md:12`) — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- Misma herramienta dos veces: ahora «documentado como posible, pasos sin documentar» (`02:61`, `05-ajustes-locales.md:47`) — [Start editing with Edit View](https://support.skylum.com/editing-tools/start-editing-with-edit-view), [Layers](https://support.skylum.com/editing-tools/layers)
- Auto Straighten y Straighten atribuidos a Crop AI Improved, con Horizon Alignment para el anterior (`04:42`, `03:142`, `08-paisaje.md:23`) — [Crop AI Tool](https://support.skylum.com/editing-tools/crop-ai-tool)
- Calibrador de pantalla: añadida la advertencia sobre el perfil del monitor, con sus salvedades (`01-conceptos-basicos.md:170`) — [Why do photo colors change after export](https://support.skylum.com/why-do-photo-colors-change-after-export-in-luminar-for-desktop)
- «Upscale al final de todo»: ahora «casi al final», con el enfoque después (`04:163`, `07-safari.md:40`, `12-varias-fotos.md:51`) — [Best practices with Upscale](https://support.skylum.com/luminar-for-desktop-tips/best-practices-with-upscale)
- Niveles de Sharpen al exportar: la guía ya avisa de que «bajo» y «moderado» son palabras suyas (`13-exportar.md:102`) — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)

### Cited Findings — contradicho o por corregir hoy
- **Curves (`06-herramientas-avanzadas.md:16`)**: «Subir un punto aclara esa zona; bajarlo la oscurece». Skylum: "Drag up to add contrast to an area and drag down to lighten the area." Contradicción literal, probablemente una errata de Skylum; hay que comprobarlo en la aplicación — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- **Consejos de toma de panorama (`12-varias-fotos.md:32`)** atribuidos a Skylum sin más: Skylum los da para panoramas a partir de vídeo — [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching)
- **Lista de proporciones, «Ratio», «Enter Custom» y «sal de la herramienta para aplicar» (`04:44`, `03:142`, `13:91`)**: documentados para Crop AI Regular; en Improved el control es «Aspect Ratio» y no se enumeran opciones — [Crop AI Tool](https://support.skylum.com/editing-tools/crop-ai-tool)
- **Remove Color Cast (`03:76`, `04:64`)**: es un deslizador, no una acción automática de un clic — [Color](https://support.skylum.com/editing-tools/essential-tools/color)
- **Clone (`03:145`, `04:108`)**: el origen se fija con un clic; Opción-clic lo cambia — [Clone](https://support.skylum.com/editing-tools/professional-tools/clone)
- **Linear Gradient (`05:55`)**: el punto central coloca; se rota arrastrando junto al punto — [Linear Gradient Mask](https://support.skylum.com/editing-tools/masking-options/linear-gradient-mask)
- **Pestaña Extra (`02:25`)**: falta Restoration — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- **Referencias internas**: `11-trabajar-en-serie.md:65` remite a «(10.1)» y debe ser 11.1; `13-exportar.md:28` remite a «(11.3)» y debe ser 13.3. Comprobado contra los propios capítulos; no hay fuente externa. La numeración de herramientas de la guía sigue la de [llms.txt](https://support.skylum.com/llms.txt)

### Cited Findings — sin respaldo en ninguna página de Skylum
- **Compare (`;`) «muestra versiones lado a lado»** (`02:33`, `04:21`, `05:164`, `08:115`, `11:62`) y «**Compare**» como control en pantalla (`17:83`): solo existe el nombre del atajo — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- **Signos de Temperature y Tint** (`03:40–41`: «(−) azul, (+) amarillo») y «azul ↔ amarillo» (`01:81`): Skylum dice "adding Cyan or Yellow" y no da sentido — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- **Pestaña Info para ver los píxeles** (`13:57`): solo "photo details and metadata" — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- **«Skylum documenta los atajos con el teclado de Estados Unidos»** (`17:71`): la página no lo dice — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- **Canal «Aguamarina» de HSL** (`08:58`) y demás nombres de canal: no enumerados; la guía lo advierte en `04:82` — [Color](https://support.skylum.com/editing-tools/essential-tools/color)
- **Orden con generativas y Upscale tras editar** (`04:163`): Skylum describe estas herramientas como lanzadas desde el catálogo, con un TIF o copia nuevos; no dice si llevan las ediciones — [GenErase](https://support.skylum.com/extra-tools/generative-tools/generase), [Upscale](https://support.skylum.com/extra-tools/upscale)
- **Fallos de las máscaras IA** en cuernos y bigotes (`02:59`) y de noche (`09-noche.md:61`); **Noiseless AI borra estrellas pequeñas** (`09:29`); **Film Grain disimula bandas** (`01:36`): plausibles, sin documentar. La única mención nocturna de Skylum está en [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)

### Cited Findings — afirmaciones de la guía confirmadas
- Nueve categorías de Mask AI, Radial Standard/Inverted, acciones de máscara, Copy/Paste — [Mask AI](https://support.skylum.com/editing-tools/masking-options/mask-ai), [Using a Radial Mask](https://support.skylum.com/editing-tools/masking-options/using-a-radial-mask), [Mask Actions](https://support.skylum.com/editing-tools/masking-options/mask-actions)
- Sharpening Masking 30–70; Structure AI "human-aware"; Light Depth sustituye a Relight AI; Mystical <40; Color Transfer no vale para blanco y negro; Sky AI para cielos planos o quemados — páginas citadas en A2.
- Auto Distortion y Auto CA solo en RAW (`08:31`) — [Develop](https://support.skylum.com/editing-tools/essential-tools/develop-raw-develop)
- Focus Stacking 100 tomas; panorama 15.000 px; Upscale 6× y límites en píxeles; GenExpand 25 % y 10 %; salidas TIFF — páginas citadas en A2 y A4.
- Exclusiones de sincronización; Crop no se guarda en presets; ruta para guardar presets — páginas citadas en A7.
- Formatos de exportación, modos de Resize, Signature, ajustes recordados; ninguna opción documentada para quitar metadatos (`14-etica.md:37`) — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- Todos los atajos del capítulo 17 coinciden con la tabla de macOS — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- «Las fusiones no incluyen apilado para reducir ruido» (`09:76`): coherente con A4 — [Walkthrough](https://support.skylum.com/how-to-use-luminar-for-desktop/luminar-for-desktop-walkthrough)
- Home Printing: menú Export → Print…, ICC, Soft Proofing, Print Sharpening None/Low/Medium/High (`13:101`) — [Home Printing](https://support.skylum.com/printing/home-printing)

### Inferences
- El único punto en que la guía y la documentación chocan de frente es Curves; lo demás son matices de redacción o silencios de Skylum.
- Si varias instancias funcionan como dicen los tres pasajes, el capítulo 5 podría presentar «segundo Develop + Mask AI u Object Select AI» como método principal; sigue pendiente comprobar el gesto en la aplicación.

### Gaps
- Pasos exactos para añadir una segunda instancia de una herramienta en 1.29: sin documentar (ya en PENDIENTES).
- Afirmaciones no relacionadas con Luminar que no se pudieron comprobar en esta sesión (Clarkvision, Lonely Speck, Cambridge in Colour, teclado español ISO, borrado de ubicación en Vista Previa): ver `verificacion-de-datos/luminar-y-retoques.md`, apartado 4.

## B3. Temas sobre los que la documentación de Skylum calla

### Takeaway
La documentación calla sobre casi todo lo cuantitativo y sobre toda la técnica por género. Los números de la guía, el flujo nocturno y los límites del JPEG son suyos y deben seguir rotulados así, como ya están.

### Cited Findings
- Sin rangos ni valores por defecto salvo: Lightness 100 y Amount 0 por defecto en Atmosphere AI Regular — [Atmosphere AI](https://support.skylum.com/editing-tools/landscape-tools/atmosphere-ai); "At 0, the tool is not applied" en Details — [Details](https://support.skylum.com/editing-tools/essential-tools/details)
- Sin contenido de astrofotografía (ver A5) — [Enhance AI](https://support.skylum.com/editing-tools/essential-tools/enhance-ai)
- Formatos de entrada de las fusiones: silencio — [HDR Merge](https://support.skylum.com/extra-tools/hdr-merge), [Panorama Stitching](https://support.skylum.com/extra-tools/panorama-stitching), [Focus Stacking](https://support.skylum.com/extra-tools/focus-stacking)
- Metadatos y GPS al exportar: silencio — [Export Image](https://support.skylum.com/saving-and-exporting-files/export-image)
- Lista de canales de HSL: silencio — [Color](https://support.skylum.com/editing-tools/essential-tools/color)
- Teclados no estadounidenses y los caracteres `\ / ; [ ] '`: silencio — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)
- Función de Compare y contenido de Copy/Paste Adjustments: silencio — [Keyboard Shortcut Keys](https://support.skylum.com/something-useful/keyboard-shortcut-keys)

### Inferences
- También sin página (ausencia en las 174): bandas y profundidad de bits interna con JPEG; efecto del orden en la pila de herramientas; si Film Grain oculta bandas; Noiseless AI en estrellas y pelo; precisión de las máscaras en animales; apilado de estrellas; calima térmica.

### Gaps
- Lo que la documentación omite (gesto de la segunda instancia, Compare, Noiseless AI en estrellas de un JPEG, Upscale sobre fotos editadas, dirección real de Curves) solo puede cerrarse probándolo en la aplicación o con una fuente de terceros con nombre.
