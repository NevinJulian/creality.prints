from build123d import *
from ocp_vscode import show

from common import *


def profile():
    jaw = -OPENING - BOTTOM
    low = -RING_H - CHANNEL_BASE
    corners = [((FIN_X, min(low, jaw)), 4)]
    if low < jaw:
        corners += [((0, low), 4), ((jaw - low, jaw), 4)]
    corners += [
        ((BOTTOM_REACH, jaw), 4),
        ((BOTTOM_REACH, -OPENING), 4),
        ((0, -OPENING), 8),
        ((0, 0), 2),
        ((TOP_REACH, 0), 2),
        ((TOP_REACH, TOP_TIP), 3),
        ((0, TOP_ROOT), 0),
        ((-SPINE, TOP_ROOT), 4),
        ((-SPINE, FIN_TOP), 0),
        ((FIN_X, FIN_TOP), 1),
    ]
    with BuildSketch() as sketch:
        Polygon(*[p for p, _ in corners], align=None)
        for p, r in corners:
            if r:
                fillet(sketch.vertices().sort_by_distance(Vector(*p))[0], r)
    return sketch.sketch


def make_clamp():
    clamp = extrude(Plane.XZ * profile(), WIDTH / 2, both=True)

    c = CLEARANCE
    floor = -RING_H
    clamp -= Box(
        CHANNEL[1] - CHANNEL[0],
        WIDTH - 2 * END_WALL,
        FIN_TOP - floor + 1,
        align=(Align.MIN, Align.CENTER, Align.MIN),
    ).moved(Location((CHANNEL[0], 0, floor)))

    slot_h = NUT_H + 2 * c
    hex_slot = extrude(Pos(SCREW_X, 0) * RegularPolygon(NUT_AF / 2 + c, 6, major_radius=False, rotation=30), slot_h)
    hex_slot += Box(NUT_AF + 2 * c, WIDTH / 2 + 1, slot_h, align=(Align.CENTER, Align.MIN, Align.MIN)).moved(Location((SCREW_X, 0, 0)))
    clamp -= hex_slot.moved(Location((0, 0, NUT_Z - slot_h / 2)))

    hole = extrude(Pos(SCREW_X, 0) * teardrop(THREAD_D / 2 + 0.6), BOTTOM + 2)
    clamp -= hole.moved(Location((0, 0, -OPENING - BOTTOM - 1)))

    clamp = chamfer(clamp.edges().group_by(Axis.Y)[0], FIRST_LAYER_CHAMFER)
    return clamp


def for_print(clamp):
    return clamp.rotate(Axis.X, 90)


if __name__ == "__main__":
    clamp = make_clamp()
    export(for_print(clamp), "clamp")
    show(clamp, names=["clamp"])
