# Keychain

Keychain with the Le Nerima sun. The sun is inlaid flush into the face, and the face prints down on the plate. That way it takes the surface of the plate and shows no layer lines, and the colour only changes in the first three layers.

The sun is mirrored in the model so it reads the right way round on the finished keychain. It hangs upright from the ring.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `keychain.stl` | Tag with the recess for the sun in the face | 38 × 47 × 3.5 mm | Flat, face down, as exported |
| `sun.stl` | Inlay that fills the recess | 30 × 30 × 0.6 mm | Together with the tag, see below |

About 5 g of PETG per keychain. The hole takes a normal split ring.

## Scripts

- `sun.svg` is the original Le Nerima sun from Illustrator
- `sun.py` reads it and turns every stroke into an outline with flat ends and sharp corners, the same as in Illustrator. `sun(width)` returns it scaled to that width
- `keychain.py` builds the tag, writes both STLs next to the script and shows them

## Print

- PETG. PLA gets soft at around 55 °C, which a car in the sun easily reaches
- Tag in a light colour, sun in green
- 0.2 mm layer height. The recess is three layers deep
- No supports
- The sun sits in the first layer, so clean the plate and make sure the first layer is dialled in
- A smooth plate gives a glossy face, a textured plate a matte grain

## Sun inlay

1. In Creality Print select `keychain.stl` and `sun.stl` and drag both in at the same time
2. Answer yes when it asks whether to load them as one object with multiple parts
3. Give the sun part the green filament
4. Copy the object for as many keychains as you need. The filament swaps happen per layer, not per keychain, so a full plate needs barely more purge than a single one

## Measurements

| Constant | Meaning |
| --- | --- |
| `DISC_D` | Diameter of the tag |
| `THICKNESS` | Thickness of the tag |
| `HOLE_D` | Hole for the key ring |
| `NECK_R` | Rounding between the disc and the lug |
| `SUN_SIZE` | Width of the sun. At 30 it stays 1.1 mm clear of the chamfer and the lines are 0.77 mm wide |
| `SUN_DEPTH` | Depth of the inlay, three layers at 0.2 mm |

The line width comes from the SVG and scales with `SUN_SIZE`. In the drawing the end of the right eye and the face, and the nose and the mouth, are only about 0.3 mm apart at this size. A 0.4 mm nozzle may close those gaps.
