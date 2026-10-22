import math
from pathlib import Path

from build123d import *

OUT_DIR = Path(__file__).parent

BALL_D = 42.67
BALL_PLAY = 0.3
MOUTH = 41.0
BALLS = 3

TEE_SHANK = 4.7
TEE_PLAY = 0.1
TEES = 3
TEE_PITCH = 13

THICKNESS = 16
RING_W = 5
SPINE = 13
OVERLAP = 4
GAP = 3

HOOK_W = 6
HOOK_LEN = 55
SLOT_ROOT = 6
SLOT_TIP = 1.5

ROUND = 3
EDGE_R = 1.2
FIRST_LAYER_CHAMFER = 0.4
TEE_CHAMFER = 0.6

BALL_R = BALL_D / 2 + BALL_PLAY
RING_R = BALL_R + RING_W
ARM_R = BALL_R + RING_W / 2
POCKET_X = RING_R - OVERLAP
PITCH = 2 * RING_R + GAP
FACE_R = (BALL_R**2 - (THICKNESS / 2) ** 2) ** 0.5
BEND_R = (SPINE + SLOT_ROOT + HOOK_W) / 2
HOOK_Y = RING_R


def pocket_ys(count):
    return [-i * PITCH for i in range(count)]


def tee_ys(y):
    return [y + (i - (TEES - 1) / 2) * TEE_PITCH for i in range(TEES)]


def corners(face):
    found = []
    for v in face.vertices():
        p = Vector(v)
        tangents = []
        for e in face.edges():
            if (e @ 0 - p).length < 1e-4:
                tangents.append(e % 0)
            elif (e @ 1 - p).length < 1e-4:
                tangents.append(e % 1)
        if len(tangents) == 2 and tangents[0].cross(tangents[1]).length > 0.1:
            found.append(v)
    return found


def tip_angle(mouth):
    return math.asin((mouth / 2 + RING_W / 2) / ARM_R)


def opening(mouth):
    a = tip_angle(mouth)
    far = 2 * RING_R
    return Polygon((0, 0), (far * math.cos(a), far * math.sin(a)), (far, 0), (far * math.cos(a), -far * math.sin(a)), align=None)


def tips(mouth):
    a = tip_angle(mouth)
    x, y = ARM_R * math.cos(a), ARM_R * math.sin(a)
    return Pos(x, y) * Circle(RING_W / 2) + Pos(x, -y) * Circle(RING_W / 2)


def hook():
    bend = Pos(-BEND_R, HOOK_Y) * Circle(BEND_R) & Pos(-BEND_R, HOOK_Y + BEND_R / 2) * Rectangle(2 * BEND_R, BEND_R)
    prong = Polygon(
        (-SPINE - SLOT_ROOT, HOOK_Y),
        (-2 * BEND_R, HOOK_Y),
        (-2 * BEND_R, HOOK_Y - HOOK_LEN),
        (-SPINE - SLOT_TIP, HOOK_Y - HOOK_LEN),
        align=None,
    )
    return bend + prong - Pos(-SPINE - SLOT_ROOT / 2, HOOK_Y) * Circle(SLOT_ROOT / 2)


def outline(mouths, clip):
    ys = pocket_ys(len(mouths))
    top = HOOK_Y if clip else ys[0] + RING_R
    bottom = ys[-1] - RING_R
    shape = Pos(-SPINE / 2, (top + bottom) / 2) * Rectangle(SPINE, top - bottom)
    for y in ys:
        shape += Pos(POCKET_X, y) * Circle(RING_R)
    if clip:
        shape += hook()
    shape = fillet(corners(shape), ROUND)

    for y, mouth in zip(ys, mouths):
        shape = shape - Pos(POCKET_X, y) * opening(mouth) + Pos(POCKET_X, y) * tips(mouth)
    return shape


def tee_hole(play):
    r = TEE_SHANK / 2 + play
    hole = Cylinder(r, THICKNESS, align=(Align.CENTER, Align.CENTER, Align.MIN))
    hole += Pos(0, 0, THICKNESS) * Cone(r, r + TEE_CHAMFER, TEE_CHAMFER, align=(Align.CENTER, Align.CENTER, Align.MAX))
    return hole


def body(mouths, plays, clip=False):
    part = extrude(outline(mouths, clip), THICKNESS)
    part = fillet(part.edges().group_by(Axis.Z)[-1], EDGE_R)
    part = chamfer(part.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)

    for y in pocket_ys(len(mouths)):
        part -= Pos(POCKET_X, y, THICKNESS / 2) * Sphere(BALL_R)
        for ty, play in zip(tee_ys(y), plays):
            part -= Pos(-SPINE / 2, ty) * tee_hole(play)
    return part


def export(part, name):
    export_stl(part, OUT_DIR / f"{name}.stl", tolerance=0.01, angular_tolerance=0.15)
