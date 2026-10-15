from build123d import *
from ocp_vscode import show

from common import *


def make_nut():
    bore = THREAD_D / 2 + THREAD_PLAY
    nut = extrude(RegularPolygon(NUT_AF / 2, 6, major_radius=False, rotation=30), NUT_H)
    nut -= Cylinder(bore, NUT_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    nut += thread(NUT_H, THREAD_PLAY)

    sink = bore + 0.6
    nut -= Cone(sink, 0, sink, align=(Align.CENTER, Align.CENTER, Align.MIN))
    nut -= Cone(sink, 0, sink, align=(Align.CENTER, Align.CENTER, Align.MIN)).rotate(Axis.X, 180).moved(Location((0, 0, NUT_H)))
    nut = chamfer(nut.edges().group_by(Axis.Z)[0].filter_by(GeomType.LINE), FIRST_LAYER_CHAMFER)
    return nut


if __name__ == "__main__":
    nut = make_nut()
    export(nut, "nut")
    show(nut, names=["nut"])
