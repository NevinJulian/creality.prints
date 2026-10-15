from math import cos, radians, sin

from build123d import *
from ocp_vscode import show

from common import *

KNOB_D = 40
KNOB_H = 14
GRIPS = 8
THREAD_L = OPENING + BOTTOM - THINNEST - (PAD_H - PAD_SOCKET)


def make_screw():
    r = KNOB_D / 2
    knob = Cylinder(r, KNOB_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    for i in range(GRIPS):
        a = radians(i * 360 / GRIPS)
        knob -= Cylinder(4, KNOB_H, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location(((r + 1.5) * cos(a), (r + 1.5) * sin(a), 0)))
    knob = chamfer(knob.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)
    knob = fillet(knob.edges().group_by(Axis.Z)[-1], 1.5)

    core = Cylinder(ROOT_R, THREAD_L, align=(Align.CENTER, Align.CENTER, Align.MIN))
    core = chamfer(core.edges().group_by(Axis.Z)[-1], 0.8)
    shaft = core + thread(THREAD_L, ends=("square", "fade"))
    return knob + shaft.moved(Location((0, 0, KNOB_H)))


def make_pad():
    pad = Cylinder(PAD_D / 2, PAD_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    pad -= Cylinder(THREAD_D / 2 + 0.5, PAD_SOCKET, align=(Align.CENTER, Align.CENTER, Align.MAX)).moved(Location((0, 0, PAD_H)))
    pad = chamfer(pad.edges().group_by(Axis.Z)[0], FIRST_LAYER_CHAMFER)
    pad = fillet(pad.edges().group_by(Axis.Z)[-1].sort_by(SortBy.RADIUS)[-1], 1.5)
    return pad


if __name__ == "__main__":
    screw = make_screw()
    pad = make_pad()
    export(screw, "screw")
    export(pad, "pad")
    show(screw, pad.moved(Location((KNOB_D, 0, 0))), names=["screw", "pad"])
