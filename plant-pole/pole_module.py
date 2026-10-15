from math import ceil, cos, radians, sin

from build123d import *
from ocp_vscode import show

from common import *

NODE_D = STRUT_D + 0.3
NODE_GAP = 0.4
HALF = 180 / STRUTS
ROWS = LATTICE_TURN / HALF


def strut(start, end, diameter):
    direction = (end - start).normalized()
    a = start + direction * NODE_GAP
    return Plane(a, z_dir=direction) * Cylinder(
        diameter / 2, (end - a).length, align=(Align.CENTER, Align.CENTER, Align.MIN)
    )


def node(j, k):
    z0, z1 = LATTICE_Z
    a = radians((2 * k + j) * HALF)
    return Vector(STRUT_R * cos(a), STRUT_R * sin(a), z0 + j * (z1 - z0) / ROWS)


def lattice():
    z1 = LATTICE_Z[1]
    # the two directions differ slightly in diameter, equal crossing cylinders break the boolean
    pieces = []
    for j in range(ceil(ROWS)):
        for k in range(STRUTS):
            start = node(j, k)
            pieces.append(Sphere(NODE_D / 2).moved(Location(start)))
            for end, diameter in ((node(j + 1, k), STRUT_D), (node(j + 1, k - 1), STRUT_D - 0.1)):
                if end.Z > z1 - 0.01:
                    end = start + (end - start) * ((z1 + 4 - start.Z) / (end.Z - start.Z))
                else:
                    end = end - (end - start).normalized() * NODE_GAP
                pieces.append(strut(start, end, diameter))
    return pieces[0].fuse(*pieces[1:])


def make_module():
    bottom = STEP - RING_H
    ring = revolved([
        (STRUT_R, bottom),
        (POLE_R, bottom + POLE_R - STRUT_R),
        (POLE_R, STEP),
        (SPIGOT_IN, STEP),
        (SPIGOT_IN, bottom + STRUT_R - SPIGOT_IN),
    ])
    return socket().fuse(lattice(), ring, spigot().moved(Location((0, 0, STEP))))


if __name__ == "__main__":
    module = make_module()
    export(module, "pole_module")
    show(module)
