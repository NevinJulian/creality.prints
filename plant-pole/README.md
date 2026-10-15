# Plant pole

Modular moss pole with a diamond lattice. The modules stack with a twist lock that clicks in place. The pot has a socket in the floor so the pole locks straight into it. For any other pot there is a stand that gets buried in the soil. On top goes either a cap or a watering reservoir. Clips snap onto the struts and hold the stems, no cord needed.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `pole_module.stl` | Pole module, print as many as you need | Ø64 × 216 mm, adds 200 mm per module | Upright |
| `pot.stl` | Pot with socket | Ø131 × 120 mm | Upright |
| `base.stl` | Stand for an ordinary pot | Ø120 × 60 mm | Upright |
| `cap.stl` | Closes the top module | Ø64 × 52 mm | Upright |
| `watering_aid.stl` | Reservoir, about 280 ml | Ø88 × 84 mm | Upright |
| `clip_right.stl`, `clip_left.stl` | Stem clips | 21 × 16 × 5 mm | Flat |

Pot, three modules and the watering aid stand about 74 cm tall.

## Scripts

- `common.py` has the shared dimensions, the twist lock and the stand that the base and the pot use
- One script per part. Each one writes its STL next to the script and shows the part
- `assembly.py` builds everything, writes all STLs and shows the pole stacked in the pot

The lattice takes about 30 seconds to build.

## Print

- PLA or PETG, 0.2 mm layer height
- No supports. No overhang is flatter than 45°. The only bridges are the 5 mm drain channels under the pot floor
- 3 walls, so the struts print solid
- Watering aid with 4 walls so it holds water and only drips through the hole

## Twist lock

Every part has the plug on top and the socket at the bottom. Set the upper part on with its three slots over the three lugs, push it down and turn it clockwise (seen from above) by 30° until it clicks. Turn back to open.

The click comes from three spring tongues in the plug that snap into notches in the socket.

- `CLEARANCE` in `common.py` is the gap per side between plug and socket. Set it to the sliding fit from the [clearance test](../clearance-test)
- `DETENT` sets how hard the click is. Lower it if turning is too stiff, raise it if there is no click

## Clips

The struts lean in two directions. `clip_right` fits the struts that rise to the right (/), `clip_left` the ones that rise to the left (\\). Push the clip onto a strut from outside between two crossings, then press the stem into the ring. `STEM_D` in `clip.py` sets the ring size.

## Use

1. Lock the first module into the pot, or into the base and bury the base in the soil of your pot
2. Fill the module with damp sphagnum moss, then lock the next module on top and fill that one
3. Finish with the cap or the watering aid. The drip hole sits right on the moss of the top module
