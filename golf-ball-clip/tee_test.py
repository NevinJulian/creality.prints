from build123d import *
from ocp_vscode import show

from common import *

HOLES = [5.0, 5.2, 5.4, 5.6, 5.8, 6.0]
HEIGHT = 6
SPACING = 10
WIDTH = 22
HOLE_Y = 4
LABEL_Y = -5
LABEL_SIZE = 4
LABEL_DEPTH = 0.6


def make_test():
    xs = [(i - (len(HOLES) - 1) / 2) * SPACING for i in range(len(HOLES))]
    strip = extrude(fillet(Rectangle(SPACING * len(HOLES), WIDTH).vertices(), ROUND), HEIGHT)
    strip = fillet(strip.edges().group_by(Axis.Z)[-1], EDGE_R)
    strip = chamfer(strip.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)
    for x, d in zip(xs, HOLES):
        strip -= Pos(x, HOLE_Y) * tee_hole(d, HEIGHT)
        strip -= extrude(Pos(x, LABEL_Y, HEIGHT) * Text(f"{d:.1f}", font_size=LABEL_SIZE), -LABEL_DEPTH)
    return strip


if __name__ == "__main__":
    test = make_test()
    export(test, "tee_test")
    show(test, names=["tee test"])
