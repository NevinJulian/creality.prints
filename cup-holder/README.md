# Cup holder

Cup holder that clamps onto the edge of a table. It's made for a table whose underside is bevelled at the front: both jaws reach past the bevel, so the screw presses on the flat underside. On a normal desk it works the same way.

The clamp and the ring are separate prints. That way the clamp can lie on its side, which makes the jaws a lot stronger, and the ring prints upright. The ring hangs in a channel on the outside of the clamp, so a ring for a different cup is just one more print. A slot in the ring takes the handle of a cup.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `clamp.stl` | Clamp with nut slot and channel for the ring | 76 × 91 × 36 mm | On its side, as exported |
| `ring.stl` | Ring for a cup of `CUP_D`, with a slot for a handle | 84 × 74 × 75 mm | Upright |
| `screw.stl` | Screw with knob, Ø16 thread, 4 mm pitch | Ø40 × 65 mm | Upright, knob down |
| `nut.stl` | Nut for the screw | 24 mm across flats × 12 mm | Flat |
| `pad.stl` | Pressure pad for the screw tip | Ø30 × 7 mm | Flat side down |

## Measurements

Everything is set in `common.py`.

| Constant | Meaning |
| --- | --- |
| `UNDERCUT` | How far the bevel reaches in from the front edge, measured flat. The screw sits 20 mm further in |
| `OPENING` | Gap between the jaws. With 50 the clamp fits tables up to 43 mm |
| `THINNEST` | Thinnest table the screw still reaches. Sets the screw length |
| `CUP_D` | Diameter of the drink. 66 is a normal can, 0.33 l and 0.5 l alike. 53 is a slim can |
| `SLOT_ANGLE` | Direction of the handle slot in degrees. 0 points straight away from the table, 90 turns it to the right when you face the table |
| `TABLE`, `TABLE_EDGE` | Thickness of the table and height of the straight bit at the front. Only used for the preview in `assembly.py` |

## Scripts

- `common.py` has the dimensions, the thread and the export
- One script per part. Each one writes its STL next to the script and shows the part
- `assembly.py` builds everything, writes all STLs and shows the holder mounted on a table with a bevelled underside

Needs `bd_warehouse` for the threads. It's in `requirements.txt`.

## Print

- PLA or PETG, 0.2 mm layer height
- No supports. The only bridges are the 6 mm end walls of the channel and the 6 to 9 mm neck of the ring
- Clamp with 4 walls and 40% infill, since it takes the whole clamping force
- Print the screw and the nut first and check the thread before printing the rest

## Fit

- `THREAD_PLAY` is the radial play of the thread. Raise it if the nut is too tight, lower it if it wobbles
- `CLEARANCE` is the gap per side for the nut slot and the ring in the channel

## Use

1. Push the nut into the slot on the side of the lower jaw
2. Turn the screw into the nut from below until the tip comes out at the top
3. Put the pad on the screw tip. It stays still while the screw turns, so it doesn't scratch
4. Push the clamp onto the table and tighten the screw by hand
5. Drop the ring into the channel on the outside of the clamp
