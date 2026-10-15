# Keychain

Keychain with the Le Nerima sun. The sun is inlaid flush into the face, and the face prints down on the plate. That way it takes the surface of the plate and shows no layer lines, and the colour only changes in the first three layers.

The sun is mirrored in the model so it reads the right way round on the finished keychain. It hangs upright from the ring.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `keychain.stl` | Tag with the recess for the sun in the face | 38 × 47 × 3.5 mm | Flat, face down, as exported |
| `sun.stl` | Inlay that fills the recess | 29 × 29 × 0.6 mm | Together with the tag, see below |

About 5 g of PETG per keychain. The hole takes a normal split ring.

## Scripts

- `sun.py` has the sun as point lists. `sun(size, line)` scales and strokes it
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
| `SUN_SIZE` | Width of the sun. At 28 it stays 1.7 mm clear of the chamfer |
| `SUN_LINE` | Line width of the sun. Keep it at two nozzle widths or more |
| `SUN_DEPTH` | Depth of the inlay, three layers at 0.2 mm |
