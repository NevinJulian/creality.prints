from pathlib import Path

from build123d import *
from ocp_vscode import show

from sun import sun

OUT_DIR = Path(__file__).parent

SCALE_CM = 20
TEST_CM = 5
STRETCH = 1.0

WIDTH = 32
THICKNESS = 3
START = 6
CORNER_R = 3
FACE_CHAMFER = 0.4
BACK_R = 1

INLAY_DEPTH = 0.6
TICK_W = 0.45
TICK_START = 0.8
MM_TICK = 3
HALF_TICK = 4.5
CM_TICK = 6
FONT = "Arial"
FONT_SIZE = 5.5
NUMBER_GAP = 1

SUN_SIZE = 28
SUN_GAP = 6
END = 5


def scale_end(cm):
    return START + cm * 10 * STRETCH


def length(cm, with_sun):
    return scale_end(cm) + (SUN_GAP + SUN_SIZE + END if with_sun else START)


def marks(cm, with_sun):
    top = WIDTH - TICK_START
    shapes = []
    for mm in range(cm * 10 + 1):
        x = START + mm * STRETCH
        tick = CM_TICK if mm % 10 == 0 else HALF_TICK if mm % 5 == 0 else MM_TICK
        shapes.append(Pos(x, top) * Rectangle(TICK_W, tick, align=(Align.CENTER, Align.MAX)))
        if mm % 10 == 0:
            number = Text(str(mm // 10), FONT_SIZE, font=FONT, font_style=FontStyle.BOLD, align=(Align.CENTER, Align.MAX))
            shapes.append(Pos(x, top - CM_TICK - NUMBER_GAP) * number)
    if with_sun:
        shapes.append(Pos(scale_end(cm) + SUN_GAP + SUN_SIZE / 2, WIDTH / 2) * sun(SUN_SIZE))
    return Sketch() + shapes


def make_ruler(cm, with_sun):
    plan = Rectangle(length(cm, with_sun), WIDTH, align=Align.MIN)
    plan = fillet(plan.vertices(), CORNER_R)
    body = extrude(plan, THICKNESS)
    body = fillet(body.edges().group_by(Axis.Z)[0], BACK_R)
    body = chamfer(body.edges().group_by(Axis.Z)[-1], FACE_CHAMFER)
    inlay = extrude(Plane.XY.offset(THICKNESS) * marks(cm, with_sun), -INLAY_DEPTH)
    return body - inlay, inlay


def for_print(part):
    return part.rotate(Axis.X, 180).moved(Location((0, WIDTH, THICKNESS)))


def export(part, name):
    export_stl(for_print(part), OUT_DIR / f"{name}.stl", tolerance=0.01, angular_tolerance=0.15)


if __name__ == "__main__":
    ruler, inlay = make_ruler(SCALE_CM, with_sun=True)
    export(ruler, "ruler")
    export(inlay, "ruler_inlay")

    strip, strip_inlay = make_ruler(TEST_CM, with_sun=False)
    export(strip, "test_strip")
    export(strip_inlay, "test_strip_inlay")

    show(
        ruler,
        inlay,
        strip.moved(Location((0, -WIDTH - 10, 0))),
        strip_inlay.moved(Location((0, -WIDTH - 10, 0))),
        names=["ruler", "inlay", "test strip", "test strip inlay"],
        colors=["wheat", "darkgreen", "wheat", "darkgreen"],
    )
