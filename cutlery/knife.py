from build123d import *
from ocp_vscode import show

from common import *

KNIFE_L = 222
BLADE_X = HANDLE_L + 15
SPINE = 6.5
EDGE = -11.5
BLADE_T = 3.5
TIP_T = 2.2
EDGE_T = 0.8
BEVEL = 9
FADE = 8
TOOTH = 3.2
TOOTH_DEPTH = 1.0
TEETH = (BLADE_X + 6, KNIFE_L - 16)


def outline():
    upper, lower = handle()
    spine = Spline(upper @ 1, (BLADE_X, SPINE), tangents=[(1, 0), (1, 0)])
    back = Line(spine @ 1, (KNIFE_L - 35, SPINE))
    tip = Spline(back @ 1, (KNIFE_L - 15, 3.5), (KNIFE_L - 4, -2), (KNIFE_L, -7.5), (KNIFE_L - 8, EDGE), tangents=[(1, 0), (-1, 0)])
    edge = Line(tip @ 1, (BLADE_X + 3, EDGE))
    heel = Spline(edge @ 1, lower @ 1, tangents=[(-1, 0), (-1, 0)])
    return make_face([upper, spine, back, tip, edge, heel, lower])


def serration():
    r = (TOOTH / 2) ** 2 / (2 * TOOTH_DEPTH) + TOOTH_DEPTH / 2
    count = int((TEETH[1] - TEETH[0]) / TOOTH)
    scallops = [Pos(TEETH[0] + (i + 0.5) * TOOTH, EDGE - r + TOOTH_DEPTH) * Circle(r) for i in range(count)]
    return extrude(Sketch() + scallops, BLADE_T)


def bevel():
    slope = Plane((0, EDGE, EDGE_T), x_dir=(1, 0, 0), z_dir=(0, -(BLADE_T - EDGE_T), BEVEL))
    fade = Plane((BLADE_X - 6, 0, BLADE_T), x_dir=(0, 1, 0), z_dir=(BLADE_T, 0, FADE))
    block = Box(KNIFE_L, 40, 20, align=(Align.MIN, Align.CENTER, Align.MIN))
    return split(split(block, slope), fade)


def make_knife():
    knife = extrude(outline(), HANDLE_T) & side_profile((BLADE_X - 5, BLADE_T), (KNIFE_L - 15, BLADE_T), (KNIFE_L + 1, TIP_T))
    knife = finish(knife) - bevel() - serration()
    return imprint(knife)


if __name__ == "__main__":
    knife = make_knife()
    export(knife, "knife")
    export(inlay(), "sun")
    show(knife, inlay(), names=["knife", "sun"], colors=["wheat", "darkgreen"])
