from build123d import *
from ocp_vscode import show

from common import *


def handle_slot(x, r_out):
    bottom = FLOOR + SLOT_BOTTOM + SLOT_W / 2 - RING_H
    shape = Pos(0, bottom) * Circle(SLOT_W / 2)
    shape += Pos(0, bottom) * Rectangle(SLOT_W, 1 - bottom, align=(Align.CENTER, Align.MIN))
    side = Plane((x, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))
    cut = extrude(side * shape, r_out + 2)
    return cut.rotate(Axis((x, 0, 0), (0, 0, 1)), SLOT_ANGLE)


def make_ring(cup_d=CUP_D):
    c = CLEARANCE
    r_in = cup_d / 2 + CUP_PLAY
    r_out = r_in + RING_WALL
    x = FIN_X - c - r_out
    plate = (CHANNEL[0] + c, CHANNEL[1] - c)

    ring = Cylinder(r_out, RING_H, align=(Align.CENTER, Align.CENTER, Align.MAX)).moved(Location((x, 0, 0)))
    ring += Box(plate[1] - plate[0], PLATE_W, RING_H, align=(Align.MIN, Align.CENTER, Align.MAX)).moved(Location((plate[0], 0, 0)))
    ring += Box(plate[1] - x, PLATE_W, NECK, align=(Align.MIN, Align.CENTER, Align.MAX)).moved(Location((x, 0, 0)))
    ring -= Cylinder(r_in, RING_H, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((x, 0, FLOOR - RING_H)))

    rim = ring.edges().filter_by(GeomType.CIRCLE).group_by(Axis.Z)[-1]
    ring = fillet(rim, 1)
    ring -= handle_slot(x, r_out)
    ring = chamfer(ring.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)
    return ring


if __name__ == "__main__":
    ring = make_ring()
    export(ring, "ring")
    show(ring, names=["ring"])
