from build123d import *
from ocp_vscode import show

from common import *

STEM_D = 12
THICKNESS = 5
RING_W = 2.2
BOSS = (4.4, 5.4)
SNAP = 0.75
GRIP = 0.05


def make_clip(hand=1, stem_d=STEM_D):
    strut_d = STRUT_D if hand > 0 else STRUT_D - 0.1
    stem_r = stem_d / 2
    loop_x = BOSS[0] + stem_r - 0.4
    gap = 0.55 * stem_d
    mouth = Polygon(
        (loop_x + stem_r - 1, -gap / 2),
        (loop_x + stem_r + RING_W + 1, -gap / 2 - 2),
        (loop_x + stem_r + RING_W + 1, gap / 2 + 2),
        (loop_x + stem_r - 1, gap / 2),
        align=None,
    )
    plan = Ellipse(*BOSS) + Pos(loop_x, 0) * Circle(stem_r + RING_W)
    plan -= Pos(loop_x, 0) * Circle(stem_r) + mouth
    clip = extrude(plan, THICKNESS / 2, both=True)

    channel = Cylinder(strut_d / 2 + GRIP, 30) + Box(20, SNAP * strut_d, 30, align=(Align.MAX, Align.CENTER, Align.CENTER))
    clip -= channel.rotate(Axis.X, -hand * STRUT_ANGLE)
    return clip.moved(Location((0, 0, THICKNESS / 2)))


if __name__ == "__main__":
    right = make_clip(1)
    left = make_clip(-1)
    export(right, "clip_right")
    export(left, "clip_left")
    show(right, left.moved(Location((0, -20, 0))), names=["clip_right", "clip_left"])
