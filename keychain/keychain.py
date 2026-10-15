from pathlib import Path

from build123d import *
from ocp_vscode import show

from sun import sun

OUT_DIR = Path(__file__).parent

DISC_D = 38
THICKNESS = 3.5
LUG_D = 12
HOLE_D = 5
HOLE_Y = DISC_D / 2 + 3
NECK_R = 5
FACE_CHAMFER = 0.8
BACK_R = 1.2

SUN_SIZE = 30
SUN_DEPTH = 0.6


def outline():
    shape = Circle(DISC_D / 2) + Pos(0, HOLE_Y) * Circle(LUG_D / 2)
    shape = fillet(shape.vertices(), NECK_R)
    return shape - Pos(0, HOLE_Y) * Circle(HOLE_D / 2)


def make_inlay():
    return extrude(sun(SUN_SIZE), SUN_DEPTH).mirror(Plane.YZ)


def make_keychain(inlay):
    tag = extrude(outline(), THICKNESS)
    tag = fillet(tag.edges().group_by(Axis.Z)[-1], BACK_R)
    tag = chamfer(tag.edges().group_by(Axis.Z)[0], FACE_CHAMFER)
    return tag - inlay


def export(part, name):
    export_stl(part, OUT_DIR / f"{name}.stl", tolerance=0.01, angular_tolerance=0.15)


if __name__ == "__main__":
    inlay = make_inlay()
    keychain = make_keychain(inlay)
    export(keychain, "keychain")
    export(inlay, "sun")
    show(keychain, inlay, names=["keychain", "sun"], colors=["wheat", "darkgreen"])
