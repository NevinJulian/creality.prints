# Ruler

20 cm ruler with the Le Nerima sun. The marks, the numbers and the sun are inlaid flush into the face in a second colour. Like the keychain, the face prints down on the plate, so it shows no layer lines and the colour only changes in the first three layers.

The script builds the ruler face up, the way you read it, and turns it over for the STLs.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `ruler.stl` | Ruler with the recess for marks, numbers and sun | 245 × 32 × 3 mm | Flat, face down, as exported |
| `ruler_inlay.stl` | Inlay for the ruler | 0.6 mm thick | Together with the ruler, see below |
| `test_strip.stl` | First 5 cm of the scale, without the sun | 62 × 32 × 3 mm | Flat, face down, as exported |
| `test_strip_inlay.stl` | Inlay for the test strip | 0.6 mm thick | Together with the test strip |

The ruler needs about 30 g of PETG, the inlay half a gram of it.

## Scripts

- `sun.svg` and `sun.py` are the same as in the [keychain](../keychain)
- `ruler.py` builds the ruler and the test strip, writes all four STLs next to the script and shows them

The numbers use Arial Bold.

## Print

- PETG for both colours. PLA and PETG barely stick to each other, so the marks could come loose
- 0.2 mm layer height. The inlay is three layers deep
- No supports
- A smooth plate gives a glossy face that reads well
- Load each part together with its inlay as one object with two parts and give the inlay the second filament, the same way as for the [keychain](../keychain). Check the first layer in the preview before printing

## Test strip first

Print the test strip before the ruler. It shows within about 20 minutes whether

- the millimetre marks stay apart. They are 0.45 mm wide with 0.55 mm between them. If neighbouring marks run into each other, lower `TICK_W`. If marks are missing, raise it
- the numbers are readable. `FONT_SIZE` sets their size

## Accuracy

Plastic shrinks a little as it cools, so the scale can come out slightly short. Measure from 0 to 20 against a steel ruler and set `STRETCH` to 200 divided by the measured length, for example 1.003 for 199.4 mm. Measuring 0 to 5 on the test strip gives a first hint, but over 5 cm the error is hard to see.

## Measurements

| Constant | Meaning |
| --- | --- |
| `SCALE_CM` | Length of the scale |
| `TEST_CM` | Length of the scale on the test strip |
| `STRETCH` | Correction for shrinkage, multiplies the spacing of the marks |
| `WIDTH`, `THICKNESS` | Width and thickness of the ruler |
| `START` | Distance from the left end to the 0 |
| `TICK_W` | Width of the marks |
| `MM_TICK`, `HALF_TICK`, `CM_TICK` | Length of the millimetre, half centimetre and centimetre marks |
| `FONT_SIZE` | Size of the numbers. At 5.5 the digits are about 4 mm tall |
| `SUN_SIZE` | Width of the sun. At 28 its lines are 0.72 mm wide |
| `INLAY_DEPTH` | Depth of the inlay, three layers at 0.2 mm |
