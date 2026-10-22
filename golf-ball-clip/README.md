# Golf ball clip

Clip for the golf bag that holds three balls and nine tees. A spring clip at the top slides onto a strap or the edge of a pocket, like a pen clip.

Each ball sits in a spherical pocket. The faces close over the ball by 1.2 mm on both sides, so it can't fall out to the front or the back. To the side it is held by the two arm tips, which are narrower than the ball and snap past it. The arms only bend by `(BALL_D - MOUTH) / 2` per side, 0.8 mm with the defaults, so PLA copes with it.

The slot between the prong and the spine narrows from `SLOT_ROOT` at the bend to `SLOT_TIP` at the end of the prong. Anything thicker than the tip gap pushes the prong open and gets clamped. Up to about 4 mm the prong bends little enough for PLA. For something thicker, raise `SLOT_TIP` rather than forcing it.

The tees go in from the front, tip first, until the head sits on the face. The shank comes out the back.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `clip.stl` | Clip with three pockets, nine tee holes and the spring clip | 57 × 178 × 16 mm | Flat, as exported |
| `pocket_test.stl` | Three single pockets with different mouth widths | Three pieces of 45 × 53 × 16 mm | Flat, as exported |

## Official sizes

| What | Rule | Source |
| --- | --- | --- |
| Ball diameter | At least 42.67 mm (1.680 in), no maximum | [R&A Equipment Rules, Part 4](https://www.randa.org/roe/the-rules-of-equipment/part-4-conformance-of-balls) |
| Ball weight | At most 45.93 g (1.620 oz), no minimum | Same |
| Tee length | At most 101.6 mm (4 in) | [R&A Equipment Rules, Part 6](https://www.randa.org/roe/the-rules-of-equipment/part-6-devices-and-other-equipment) |
| Tee shank | Not regulated | Same |

Wooden tees mostly come in 54, 70 and 83 mm. The shank isn't standardised and the numbers you find online range from about 4 to 5 mm, so measure your own tees and set `TEE_SHANK`.

## Scripts

- `common.py` has the dimensions and builds the outline, the pockets, the spring clip and the tee holes
- `clip.py` builds the clip, writes `clip.stl` and shows it with three balls and nine 54 mm tees
- `pocket_test.py` builds the test pieces and writes `pocket_test.stl`

## Measurements

Everything is set in `common.py`.

| Constant | Meaning |
| --- | --- |
| `BALL_D` | Ball diameter. 42.67 is the smallest the rules allow |
| `BALL_PLAY` | Gap per side between the ball and the pocket |
| `MOUTH` | Narrowest gap between the two arm tips. Smaller snaps harder |
| `BALLS` | Number of pockets |
| `TEE_SHANK` | Shank diameter of your tees |
| `TEE_PLAY` | Gap per side between the shank and the hole |
| `TEES` | Tee holes per pocket |
| `THICKNESS` | Thickness of the clip. Thicker means the faces close further over the ball |
| `RING_W` | Width of the arms around the ball. Wider arms are stiffer and snap harder |
| `HOOK_W` | Width of the prong where it leaves the bend. Wider grips harder but bends less before it breaks |
| `HOOK_LEN` | Length of the prong, measured from the bend |
| `SLOT_ROOT` | Gap between prong and spine at the bend |
| `SLOT_TIP` | Gap between prong and spine at the end of the prong |

## Pocket test

Each test piece is one segment of the real clip with the mouth width engraved on the front. Print the test before the clip.

1. Push a ball into each pocket from the open side
2. Pick the one that snaps in with a firm push and doesn't let go when you shake it upside down. Set `MOUTH` to the number on it
3. Push a tee into each of the three holes. Seen from the engraved side, the top hole is `TEE_SHANK` exactly, the middle one 0.1 mm bigger per side and the bottom one 0.2 mm bigger
4. Pick the hole the tee goes through by hand and stays in when you shake it. Set `TEE_PLAY` to 0, 0.1 or 0.2
5. Run `clip.py` and print the clip

## Print

- PLA, 0.2 mm layer height
- Flat, as exported. The front, where the tee heads sit, faces up
- No supports. The upper half of each pocket leans in by at most 22°
- 4 to 5 walls, so the arms and the prong are solid plastic with no infill inside
- PLA gets soft at around 55 °C. Don't leave the bag in a car in the summer sun
