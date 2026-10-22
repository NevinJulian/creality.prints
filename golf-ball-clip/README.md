# Golf ball clip

Clip for the golf bag that holds three balls and nine tees. A spring clip at the top slides onto a strap or the edge of a pocket, like a pen clip.

Each ball sits in a spherical pocket. The faces close over the ball by 1.2 mm on both sides, so it can't fall out to the front or the back. To the side it is held by the two arm tips, which are narrower than the ball and snap past it. The arms only bend by `(BALL_D - MOUTH) / 2` per side, 0.8 mm with the defaults, so PLA copes with it.

The slot between the prong and the spine narrows from `SLOT_ROOT` at the bend to `SLOT_TIP` at the end of the prong. Anything thicker than the tip gap pushes the prong open and gets clamped. Up to about 4 mm the prong bends little enough for PLA. For something thicker, raise `SLOT_TIP` rather than forcing it.

The tees go in from the front, tip first. Wooden tees get thicker towards the head, so a tee slides in until the shank is as thick as the hole and wedges there.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `clip.stl` | Clip with three pockets, nine tee holes and the spring clip | 57 × 178 × 16 mm | Flat, as exported |
| `pocket_test.stl` | Three single pockets with different mouth widths | Three pieces of 45 × 53 × 16 mm | Flat, as exported |
| `tee_test.stl` | Strip with six tee holes from 5.0 to 6.0 mm | 60 × 22 × 6 mm | Flat, as exported |

## Official sizes

| What | Rule | Source |
| --- | --- | --- |
| Ball diameter | At least 42.67 mm (1.680 in), no maximum | [R&A Equipment Rules, Part 4](https://www.randa.org/roe/the-rules-of-equipment/part-4-conformance-of-balls) |
| Ball weight | At most 45.93 g (1.620 oz), no minimum | Same |
| Tee length | At most 101.6 mm (4 in) | [R&A Equipment Rules, Part 6](https://www.randa.org/roe/the-rules-of-equipment/part-6-devices-and-other-equipment) |
| Tee shank | Not regulated | Same |

Wooden tees mostly come in 54, 70 and 83 mm. The shank isn't standardised. Numbers online range from about 4 to 5 mm, and mine are 5 mm at the tip end and 6 mm under the head. The tee test finds the hole size for your tees.

## Scripts

- `common.py` has the dimensions and builds the outline, the pockets, the spring clip and the tee holes
- `clip.py` builds the clip, writes `clip.stl` and shows it with three balls and nine 54 mm tees
- `pocket_test.py` builds the pocket test pieces and writes `pocket_test.stl`
- `tee_test.py` builds the tee hole strip and writes `tee_test.stl`

## Measurements

Everything is set in `common.py`.

| Constant | Meaning |
| --- | --- |
| `BALL_D` | Ball diameter. 42.67 is the smallest the rules allow |
| `BALL_PLAY` | Gap per side between the ball and the pocket |
| `MOUTH` | Narrowest gap between the two arm tips. Smaller snaps harder |
| `BALLS` | Number of pockets |
| `TEE_HOLE` | Diameter of the tee holes |
| `TEES` | Tee holes per pocket |
| `THICKNESS` | Thickness of the clip. Thicker means the faces close further over the ball |
| `RING_W` | Width of the arms around the ball. Wider arms are stiffer and snap harder |
| `HOOK_W` | Width of the prong where it leaves the bend. Wider grips harder but bends less before it breaks |
| `HOOK_LEN` | Length of the prong, measured from the bend |
| `SLOT_ROOT` | Gap between prong and spine at the bend |
| `SLOT_TIP` | Gap between prong and spine at the end of the prong |

## Pocket test

Each test piece is one segment of the real clip with the mouth width engraved on the front.

1. Push a ball into each pocket from the open side
2. Check which ones hold the ball when you shake the piece upside down
3. Set `MOUTH` to the number of a pocket that holds. If several do, take the middle one rather than the narrowest. A narrower mouth bends the arms further every time and makes the ball harder to get out

## Tee test

A small strip with six holes from 5.0 to 6.0 mm, the size engraved under each hole. The holes have the same chamfer at the top as on the clip.

1. Push a tee tip first into each hole by hand, as far as it goes without real force
2. Pick the hole where the tee goes in deepest and still stays when you turn the strip upside down and shake it
3. Set `TEE_HOLE` to its number
4. If even 6.0 only takes the tip, add bigger sizes to `HOLES` in `tee_test.py` and print it again

## Print

- Same slicer settings for both tests and the clip, otherwise the tests don't tell you anything
- PLA, 0.2 mm layer height
- Flat, as exported. The front, where the tee heads sit, faces up
- No supports. The upper half of each pocket leans in by at most 22°
- 5 walls, so the arms and the prong are solid plastic with no infill inside
- No brim. A brim fills the gap at the end of the prong
- PLA gets soft at around 55 °C. Don't leave the bag in a car in the summer sun
