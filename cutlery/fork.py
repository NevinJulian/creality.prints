from build123d import *
from build123d import SkipClean
from ocp_vscode import show

from common import *

FORK_L = 190
HEAD_W = 25
TIP_W = 23
TINES = 4
TINE_TIP = 2.8
SLOT_W = 2.4
SLOT_ROOT = 155
TINE_T = 4.5
TIP_T = 2.6


def outline():
    upper, lower = handle()
    shoulder = (SLOT_ROOT - 10, HEAD_W / 2)
    side = Line(shoulder, (FORK_L, TIP_W / 2))
    head = Spline(upper @ 1, shoulder, tangents=[(1, 0), side % 0]) + side
    return make_face([upper, head, Line(side @ 1, (FORK_L, -TIP_W / 2)), head.mirror(Plane.XZ), lower])


def slots():
    root_tine = (HEAD_W - (TINES - 1) * SLOT_W) / TINES
    tip_slot = (TIP_W - TINES * TINE_TIP) / (TINES - 1)
    over = 2 / (FORK_L - SLOT_ROOT)
    cuts = []
    for i in range(1, TINES):
        root = -HEAD_W / 2 + i * root_tine + (i - 1) * SLOT_W
        tip = -TIP_W / 2 + i * TINE_TIP + (i - 1) * tip_slot
        cuts.append(Polygon(
            (SLOT_ROOT, root),
            (FORK_L + 2, tip + (tip - root) * over),
            (FORK_L + 2, tip + tip_slot + (tip + tip_slot - root - SLOT_W) * over),
            (SLOT_ROOT, root + SLOT_W),
            align=None,
        ))
    return cuts


def make_fork():
    with SkipClean():
        plan = outline() - slots()
        roots = plan.vertices().filter_by_position(Axis.X, SLOT_ROOT - 0.1, SLOT_ROOT + 0.1)
        plan = fillet(roots, SLOT_W / 2 - 0.1)
        tips = plan.vertices().filter_by_position(Axis.X, FORK_L - 0.1, FORK_L + 0.1)
        plan = fillet(tips, TINE_TIP / 2 - 0.1)

    fork = extrude(plan, HANDLE_T) & side_profile((SLOT_ROOT - 8, TINE_T), (FORK_L + 1, TIP_T))
    return imprint(finish(fork))


if __name__ == "__main__":
    fork = make_fork()
    export(fork, "fork")
    export(inlay(), "sun")
    show(fork, inlay(), names=["fork", "sun"], colors=["wheat", "darkgreen"])
