# Cutlery

Fork, spoon and knife with the sun on the handle. All three share the same handle, so the sun sits in the same spot on each piece. It is cut 0.6 mm deep into the top of the handle. `sun.stl` fills that groove exactly, so with the CFS it prints as a flush inlay in a second colour. With one filament the sun stays an engraving.

Every piece prints flat on the bed as exported. The extrusion lines then run along the length, which is the direction that takes the load when you eat. A part printed on edge or upright would break along a layer line instead.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `fork.stl` | Fork with four tines | 190 × 32 × 5.5 mm | Flat, as exported |
| `spoon.stl` | Spoon, bowl 58 × 40 mm and 5.8 mm deep | 190 × 40 × 7.5 mm | Flat, as exported |
| `knife.stl` | Knife with a serrated edge | 222 × 32 × 5.5 mm | Flat, as exported |
| `sun.stl` | Inlay for the groove in the handle, fits all three | 24 × 24 × 0.6 mm | Together with a piece, see below |

All three fit on the bed at once. Solid they need about 65 g of PETG.

## Scripts

- `common.py` has the handle, the sun, the edge rounding and the export
- One script per piece. Each one writes its STL and `sun.stl` next to the script and shows the piece
- `assembly.py` builds all three, writes all STLs and shows them side by side

## Print

- PETG. It bends before it breaks where PLA snaps, and it handles hot food. PLA already gets soft at around 55 °C
- 0.12 or 0.16 mm layer height. Thinner layers make the bowl smoother and leave less room for food in the layer lines
- 100% infill. The tines and the blade are mostly walls anyway, and a solid part has no voids for water to get into
- Nozzle temperature at the upper end of the filament's range, so the layers bond well
- No supports. The back of the spoon is tapered at 40° from vertical, everything else is flat or faces up

## Sun inlay

1. In Creality Print select `fork.stl` and `sun.stl` and drag both in at the same time
2. Answer yes when it asks whether to load them as one object with multiple parts
3. Give the sun part the second filament

Only the top three layers of the handle change colour, so the purge stays small. Spoon and knife work the same way.

## Eating with it

It works, but it is not steel cutlery and won't last like it.

- Use a filament whose manufacturer states food contact compliance for exactly that product, ideally an uncoloured one. The green of the sun only sits on the handle
- The K2 nozzle has a hardened steel tip, not the leaded brass nozzle most food safety warnings are about
- Rinse right after eating and wash by hand with warm water and soap. No dishwasher, the hot rinse and the drying get close to where PETG softens
- Food and bacteria settle in the layer lines and washing doesn't fully get them out. Print a new set once the surface is scratched or the knife edge frays
- The serrated edge cuts bread, cooked vegetables and soft meat. It won't cut a steak

## Measurements

| Constant | File | Meaning |
| --- | --- | --- |
| `HANDLE_T` | `common.py` | Thickness of the handle |
| `SUN_SIZE` | `common.py` | Width of the sun. Much smaller and the eyes, nose and mouth run into each other |
| `SUN_LINE` | `common.py` | Line width of the sun. Keep it at two nozzle widths or more |
| `SUN_DEPTH` | `common.py` | Depth of the groove, 3 layers at 0.2 mm |
| `EDGE_R` | `common.py` | Rounding of the top edges |
| `TINE_TIP`, `TIP_T` | `fork.py` | Width and thickness of the tine tips. Raise them for stiffer tines |
| `BOWL_DEPTH` | `spoon.py` | Depth of the bowl |
| `RIM` | `spoon.py` | Width of the flat rim. It sets the thinnest wall of the bowl, 1.65 mm with 2.2 |
| `BLADE_T`, `EDGE_T` | `knife.py` | Thickness of the spine and of the cutting edge |
| `TOOTH`, `TOOTH_DEPTH` | `knife.py` | Pitch and depth of the serration |
