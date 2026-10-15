from build123d import *
from ocp_vscode import show

from common import *

TOP_R = 64
BOTTOM_R = 54
HEIGHT = 120
WALL = 2.2
FLOOR = 4
LIP = 2

COLUMN_FOOT_R = 44
COLUMN_TOP = 60

DRAINS = 6
DRAIN_R = 48.5
CHANNEL_W = 5
CHANNEL_H = 2


def make_pot():
    def outer(z):
        return BOTTOM_R + (TOP_R - BOTTOM_R) * z / HEIGHT

    lip_z = HEIGHT - 3 * LIP
    shell = revolved([
        (0, 0),
        (BOTTOM_R - 1, 0),
        (BOTTOM_R, 1),
        (outer(lip_z), lip_z),
        (outer(lip_z) + LIP, lip_z + LIP),
        (outer(lip_z) + LIP, HEIGHT),
        (TOP_R - WALL, HEIGHT),
        (outer(FLOOR) - WALL, FLOOR),
        (0, FLOOR),
    ])

    drain = Cylinder(CHANNEL_W / 2, FLOOR + 2).moved(Location((DRAIN_R, 0, FLOOR / 2)))
    channel = Box(BOTTOM_R + 3 - DRAIN_R, CHANNEL_W, CHANNEL_H + 1, align=(Align.MIN, Align.CENTER, Align.MIN))
    channel = channel.moved(Location((DRAIN_R, 0, -1)))
    for i in range(DRAINS):
        shell -= (drain + channel).rotate(Axis.Z, i * 360 / DRAINS)

    column = stand(COLUMN_FOOT_R, COLUMN_TOP - FLOOR + 1).moved(Location((0, 0, FLOOR - 1)))
    return shell + column


if __name__ == "__main__":
    pot = make_pot()
    export(pot, "pot")
    show(pot)
