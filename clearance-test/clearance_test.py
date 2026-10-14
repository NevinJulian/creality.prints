from pathlib import Path
    
from build123d import *
from ocp_vscode import show

PIN_DIAMETER = 10
PIN_HEIGHT = 20
CLEARANCES = [0.10, 0.15, 0.20, 0.25, 0.30, 0.40]

PLATE_THICKNESS = 5
HOLE_SPACING = 16
PLATE_DEPTH = 28
HOLE_Y = -4
LABEL_Y = 8
LABEL_SIZE = 5
LABEL_DEPTH = 0.6
FIRST_LAYER_CHAMFER = 0.4

OUT_DIR = Path(__file__).parent

plate_width = HOLE_SPACING * len(CLEARANCES)
hole_xs = [(i - (len(CLEARANCES) - 1) / 2) * HOLE_SPACING for i in range(len(CLEARANCES))]

with BuildPart() as plate:
    Box(plate_width, PLATE_DEPTH, PLATE_THICKNESS, align=(Align.CENTER, Align.CENTER, Align.MIN))
    fillet(plate.edges().filter_by(Axis.Z), radius=3)

    for x, clearance in zip(hole_xs, CLEARANCES):
        with Locations((x, HOLE_Y, 0)):
            Cylinder(
                radius=PIN_DIAMETER / 2 + clearance,
                height=PLATE_THICKNESS,
                align=(Align.CENTER, Align.CENTER, Align.MIN),
                mode=Mode.SUBTRACT,
            )

    bottom_circles = plate.edges().filter_by(GeomType.CIRCLE).group_by(Axis.Z)[0]
    chamfer([e for e in bottom_circles if e.radius > PIN_DIAMETER / 2], FIRST_LAYER_CHAMFER)

    with BuildSketch(Plane.XY.offset(PLATE_THICKNESS)):
        for x, clearance in zip(hole_xs, CLEARANCES):
            with Locations((x, LABEL_Y)):
                Text(f"{clearance:.2f}".lstrip("0"), font_size=LABEL_SIZE)
    extrude(amount=-LABEL_DEPTH, mode=Mode.SUBTRACT)

with BuildPart() as pin:
    Cylinder(PIN_DIAMETER / 2, PIN_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.MIN))
    chamfer(pin.edges().group_by(Axis.Z)[-1], 0.8)
    chamfer(pin.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)

export_stl(plate.part, OUT_DIR / "clearance_plate.stl")
export_stl(pin.part, OUT_DIR / "clearance_pin.stl")

show(plate, pin.part.moved(Location((0, -PLATE_DEPTH, 0))), names=["plate", "pin"])
