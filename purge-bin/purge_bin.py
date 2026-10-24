from pathlib import Path

from build123d import *
from ocp_vscode import show

OUT_DIR = Path(__file__).parent

OUTLET_Z = 70
OUTLET_W = 50
DROP = 8
CATCH = 45

WIDTH = 160
DEPTH = 90
LEVEL = 25

WALL = 1.6
FLOOR = 1.6
FRONT_R = 3
BACK_R = 16
INNER_FRONT_R = 8
INNER_BACK_R = 14
INNER_FILLET = 5
FIRST_LAYER_CHAMFER = 0.4

MAGNETS = True
MAGNET_D = 8
MAGNET_H = 3
MAGNET_PLAY = 0.15
MAGNET_INSET = 22
MAGNET_DOWN = 10
BOSS = 3

FRONT_H = OUTLET_Z - DROP
BACK_H = OUTLET_Z + CATCH


def plan(width, depth, front_r, back_r):
    face = Rectangle(width, depth, align=(Align.CENTER, Align.MIN))
    face = fillet(face.vertices().group_by(Axis.Y)[-1], back_r)
    return fillet(face.vertices().group_by(Axis.Y)[0], front_r)


def teardrop(r):
    s = r / 2**0.5
    return Circle(r) + Polygon((0, 0), (s, s), (0, 2 * s), (-s, s), align=None)


def cavity():
    inner = Pos(0, WALL, FLOOR) * plan(WIDTH - 2 * WALL, DEPTH - 2 * WALL, INNER_FRONT_R, INNER_BACK_R)
    solid = extrude(inner, BACK_H)
    return fillet(solid.edges().group_by(Axis.Z)[0], INNER_FILLET)


def scoop():
    profile = Polygon(
        (-1, FRONT_H),
        (LEVEL, FRONT_H),
        (DEPTH - BACK_R, BACK_H),
        (DEPTH + 1, BACK_H),
        (DEPTH + 1, BACK_H + 10),
        (-1, BACK_H + 10),
        align=None,
    )
    return extrude(Plane.YZ * profile, WIDTH, both=True)


def magnet_spots():
    z = FRONT_H - MAGNET_DOWN
    x = WIDTH / 2 - MAGNET_INSET
    return [Pos(-x, z), Pos(x, z)]


def magnet_bosses():
    r = MAGNET_D / 2 + MAGNET_PLAY + BOSS
    return [extrude(Plane.XZ * spot * Rot(0, 0, 180) * teardrop(r), -(MAGNET_H + 0.2 + WALL)) for spot in magnet_spots()]


def magnet_pockets():
    r = MAGNET_D / 2 + MAGNET_PLAY
    return [extrude(Plane.XZ * spot * Circle(r), -(MAGNET_H + 0.2)) for spot in magnet_spots()]


def make_bin():
    body = extrude(plan(WIDTH, DEPTH, FRONT_R, BACK_R), BACK_H)
    body = chamfer(body.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)
    body -= cavity()
    if MAGNETS:
        body += magnet_bosses()
        body -= magnet_pockets()
    body -= scoop()
    return body


def capacity():
    below_rim = cavity() & Box(WIDTH, DEPTH, FRONT_H, align=(Align.CENTER, Align.MIN, Align.MIN))
    return below_rim.volume / 1e6


def printer_back():
    k2 = Box(404, 120, 180, align=(Align.CENTER, Align.MAX, Align.MIN))
    opening = Pos(0, 0, OUTLET_Z) * Box(OUTLET_W, 40, 18, align=(Align.CENTER, Align.CENTER, Align.MIN))
    lip = Pos(0, 0, OUTLET_Z) * Box(OUTLET_W + 6, 6, 2, align=(Align.CENTER, Align.MIN, Align.MAX))
    table = Box(600, 360, 18, align=(Align.CENTER, Align.CENTER, Align.MAX))
    return k2 - opening + lip, Pos(0, -60) * table


if __name__ == "__main__":
    part = make_bin()
    export_stl(part, OUT_DIR / "purge_bin.stl", tolerance=0.01, angular_tolerance=0.15)
    print(f"{WIDTH} x {DEPTH} x {BACK_H} mm, holds {capacity():.2f} l up to the front rim")
    k2, table = printer_back()
    show(part, k2, table, names=["bin", "K2 back", "table"], colors=["darkorange", "dimgray", "burlywood"], alphas=[1, 0.6, 1])
