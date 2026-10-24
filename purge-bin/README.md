# Purge bin

Bin for the waste the K2 pushes out at the back on every filament change. It stands on the table behind the printer, right under the waste opening, with its flat front against the back panel. Two magnets in the front wall hold it against the panel, so it doesn't walk away when the printer shakes.

The front wall stays a bit below the opening, so the waste drops straight in. The back wall reaches higher than the opening and catches pieces that come out with some speed. The side walls rise from the front to the back like a scoop.

Most bins online screw a chute onto the opening with the printer's own screws or hang on magnets. This one needs no screws and comes out with one hand to empty it.

## Parts

| File | Part | Size | Print |
| --- | --- | --- | --- |
| `purge_bin.stl` | Bin with two magnet pockets in the front | 160 × 90 × 115 mm with the defaults | Upright, open side up, as exported |

About 115 g of filament with the defaults. It holds about 0.8 l up to the front rim.

## Measure the printer first

The defaults are a guess. Measure your printer and set the constants in `purge_bin.py` before printing.

1. Hold a ruler upright on the table behind the printer, right under the waste opening. Read the height of the lowest edge of the opening, where the waste falls off. That's `OUTLET_Z`
2. Measure from the back panel to the wall, or to the edge of the table if that comes first. Set `DEPTH` 5 to 10 mm smaller than that
3. Measure how much room there is left and right of the opening at the bottom of the back panel before cables, the power socket or anything else is in the way. Set `WIDTH` so the bin fits there with the opening roughly in the middle
4. Check that the back panel is flat from the table up to the opening. If a foot, the frame or a screw head sticks out, the bin can't sit flat against it
5. Hold a fridge magnet on the back panel just under the opening. If it doesn't stick, set `MAGNETS = False`

Run the script and check in the viewer that the bin sits under the opening. The grey block is a stand-in for the back of the printer, built from `OUTLET_Z` and `OUTLET_W`.

## Measurements

| Constant | Meaning |
| --- | --- |
| `OUTLET_Z` | Height of the lowest edge of the waste opening above the table |
| `OUTLET_W` | Width of the waste opening. Only used for the preview |
| `DROP` | How far the front rim sits below the opening |
| `CATCH` | How far the back wall reaches above the opening |
| `WIDTH`, `DEPTH` | Outside size of the bin. `DEPTH` is measured away from the printer |
| `LEVEL` | How far back the side walls stay at the height of the front rim before they rise |
| `WALL`, `FLOOR` | Wall and floor thickness |
| `MAGNETS` | Pockets for two magnets in the front wall |
| `MAGNET_D`, `MAGNET_H` | Magnet size. 8 × 3 mm with the defaults |
| `MAGNET_PLAY` | Gap per side around the magnet |
| `MAGNET_INSET`, `MAGNET_DOWN` | Position of the magnets, from the side and down from the front rim |

## Scripts

- `purge_bin.py` builds the bin, writes `purge_bin.stl`, prints the size and capacity, and shows the bin behind a stand-in for the printer

## Print

- PLA or PETG, 0.2 mm layer height. PETG if the back of the printer gets warm from long prints with a closed lid
- Upright, open side up, no supports. The magnet pockets and their bosses are the only overhangs and they're short
- 4 walls, so the walls are solid plastic

## Use

1. Put a drop of glue into each magnet pocket and press the magnet in flush with the front face
2. Push the bin against the back of the printer, centred under the waste opening
3. Empty it before the pile under the opening reaches the rim. If the waste piles up into the opening it can back up into the chute and block it
