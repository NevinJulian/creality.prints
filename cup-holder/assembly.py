from build123d import *
from ocp_vscode import show

from clamp import for_print, make_clamp
from common import *
from nut import make_nut
from ring import make_ring
from screw import KNOB_H, THREAD_L, make_pad, make_screw


def make_table(thickness=TABLE, edge=TABLE_EDGE, undercut=UNDERCUT):
    side = Polygon((0, 0), (160, 0), (160, -thickness), (undercut, -thickness), (0, -edge), align=None)
    side = fillet(side.vertices().sort_by_distance(Vector(0, 0))[0], 2)
    return extrude(Plane.XZ * side, 70, both=True)


def mounted(screw, nut, pad, thickness=TABLE):
    tip = -thickness - (PAD_H - PAD_SOCKET)
    bottom = tip - THREAD_L - KNOB_H
    nut_bottom = NUT_Z - NUT_H / 2
    turn = (0.5 - (nut_bottom - bottom - KNOB_H) / PITCH) * 360
    return [
        screw.rotate(Axis.Z, turn).moved(Location((SCREW_X, 0, bottom))),
        nut.moved(Location((SCREW_X, 0, nut_bottom))),
        pad.rotate(Axis.X, 180).moved(Location((SCREW_X, 0, -thickness))),
    ]


if __name__ == "__main__":
    parts = {
        "clamp": make_clamp(),
        "ring": make_ring(),
        "screw": make_screw(),
        "nut": make_nut(),
        "pad": make_pad(),
    }
    for name, part in parts.items():
        export(for_print(part) if name == "clamp" else part, name)

    screw, nut, pad = mounted(parts["screw"], parts["nut"], parts["pad"])
    show(
        make_table(),
        parts["clamp"],
        parts["ring"],
        screw,
        nut,
        pad,
        names=["table", "clamp", "ring", "screw", "nut", "pad"],
        alphas=[0.4, 1, 1, 1, 1, 1],
    )
