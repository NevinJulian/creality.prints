from math import sqrt

from build123d import *
from ocp_vscode import show

from common import *

SPOON_L = 190
BOWL_L = 58
BOWL_W = 40
BOWL_H = 7.5
BOWL_DEPTH = 5.8
BOWL_ROUND = 18
RIM = 2.2
RIM_R = 0.8
BACK_TAPER = 40
NECK_END = 150

BOWL_X = SPOON_L - BOWL_L / 2


def outline():
    upper, lower = handle()
    neck = Line(upper @ 1, (NECK_END, NECK_W / 2))
    return make_face([upper, neck, Line(neck @ 1, (NECK_END, -NECK_W / 2)), neck.mirror(Plane.XZ), lower])


def bowl():
    rim = Plane.XY.offset(BOWL_H) * Pos(BOWL_X, 0) * Ellipse(BOWL_L / 2, BOWL_W / 2)
    return extrude(rim, BOWL_H, dir=(0, 0, -1), taper=BACK_TAPER)


def hollow():
    k = 1 / sqrt(1 - ((BOWL_ROUND - BOWL_DEPTH) / BOWL_ROUND) ** 2)
    a = (BOWL_L / 2 - RIM) * k
    b = (BOWL_W / 2 - RIM) * k
    egg = scale(Sphere(1).rotate(Axis.X, 90), (a, b, BOWL_ROUND))
    return egg.moved(Location((BOWL_X, 0, BOWL_H - BOWL_DEPTH + BOWL_ROUND)))


def make_spoon():
    spoon = extrude(outline(), BOWL_H) & side_profile((BOWL_X - BOWL_L / 2 + 2, BOWL_H), (SPOON_L + 1, BOWL_H))
    spoon = finish(spoon) + bowl() - hollow()
    rim = spoon.edges().filter_by_position(Axis.Z, BOWL_H - 0.01, BOWL_H + 0.01)
    lip = [e for e in rim if abs(e.bounding_box().size.Y - (BOWL_W - 2 * RIM)) < 0.1]
    return imprint(fillet(lip, RIM_R))


if __name__ == "__main__":
    spoon = make_spoon()
    export(spoon, "spoon")
    export(inlay(), "sun")
    show(spoon, inlay(), names=["spoon", "sun"], colors=["wheat", "darkgreen"])
