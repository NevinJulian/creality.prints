from math import atan, degrees, pi, radians, sqrt, tan
from pathlib import Path

from build123d import *

OUT_DIR = Path(__file__).parent

CLEARANCE = 0.2

POLE_R = 32
STEP = 200
RING_H = 8

SPIGOT_R = 26
SPIGOT_WALL = 2.4
SPIGOT_H = 16
SOCKET_H = 18
LEAD_IN = 0.8
FIRST_LAYER_CHAMFER = 0.4

LUGS = 3
LUG_DEPTH = 1.4
LUG_TIP = 1.6
LUG_Z = 2.0
LUG_ARC = 12.5
TWIST = 30

TONGUE_ARC = 18
TONGUE_SLOT = 1.2
TONGUE_Z = 6
TONGUE_WALL = 1.6
BUMP_Z = 11.5
BUMP_LEN = 3
BUMP_FLANK = 35
DETENT = 0.3

STRUTS = 8
STRUT_D = 4.2
LATTICE_TURN = 236.25

NECK_H = 8
BELL_WALL = 2.6
WINDOWS = 8

BORE_R = SPIGOT_R + CLEARANCE
SPIGOT_IN = SPIGOT_R - SPIGOT_WALL
STRUT_R = POLE_R - STRUT_D / 2
LATTICE_Z = (SOCKET_H, STEP - RING_H)
STRUT_ANGLE = degrees(atan(STRUT_R * radians(LATTICE_TURN) / (LATTICE_Z[1] - LATTICE_Z[0])))


def revolved(points, arc=360, start=0):
    part = revolve(Plane.XZ * Polygon(*points, align=None), Axis.Z, arc)
    return part.rotate(Axis.Z, start)


def sector(r_in, r_out, z0, z1, arc, start):
    return revolved([(r_in, z0), (r_out, z0), (r_out, z1), (r_in, z1)], arc, start)


def detent(apex, base, z0, z1):
    rise = apex - base
    half = rise / tan(radians(BUMP_FLANK))
    plan = Polygon((base, -half), (apex, 0), (base, half), align=None)
    prism = extrude(plan, z1 - z0 + 2 * rise).moved(Location((0, 0, z0 - rise)))
    band = revolved([(base, z0 - rise), (apex, z0), (apex, z1), (base, z1 + rise)], 30, -15)
    return prism & band


def lug():
    z, d = LUG_Z, LUG_DEPTH
    points = [
        (SPIGOT_R - 0.6, z - 0.6),
        (SPIGOT_R + d, z + d),
        (SPIGOT_R + d, z + d + LUG_TIP),
        (SPIGOT_R - 0.6, z + 2 * d + LUG_TIP + 0.6),
    ]
    return revolved(points, LUG_ARC, -LUG_ARC / 2)


def spigot():
    part = revolved([
        (SPIGOT_IN, 0),
        (SPIGOT_R, 0),
        (SPIGOT_R, SPIGOT_H - 0.6),
        (SPIGOT_R - 0.6, SPIGOT_H),
        (SPIGOT_IN, SPIGOT_H),
    ])
    slot_arc = degrees(TONGUE_SLOT / SPIGOT_R)
    for i in range(LUGS):
        a = i * 360 / LUGS
        t = a + 180 / LUGS
        part += lug().rotate(Axis.Z, a)
        for side in (-1, 1):
            middle = t + side * (TONGUE_ARC + slot_arc) / 2
            part -= sector(SPIGOT_IN - 1, SPIGOT_R + 1, TONGUE_Z, SPIGOT_H + 1, slot_arc, middle - slot_arc / 2)
        part -= sector(SPIGOT_IN - 1, SPIGOT_R - TONGUE_WALL, TONGUE_Z, SPIGOT_H + 1, TONGUE_ARC, t - TONGUE_ARC / 2)
        part += detent(SPIGOT_R + CLEARANCE + DETENT, SPIGOT_R - 0.4, BUMP_Z, BUMP_Z + BUMP_LEN).rotate(Axis.Z, t)
    return part


def socket_cuts():
    c = CLEARANCE
    k = c * (sqrt(2) - 1)
    back = SPIGOT_R + LUG_DEPTH + c
    bottom = LUG_Z + LUG_DEPTH - k
    top = LUG_Z + LUG_DEPTH + LUG_TIP + k
    inside = BORE_R - 1.3
    arc = degrees(c / back)
    groove = [(inside, bottom - back + inside), (back, bottom), (back, top), (inside, top + back - inside)]
    channel = [(inside - 0.3, -1), (back + 0.1, -1), (back + 0.1, bottom - 0.1), (inside - 0.3, bottom + back - inside + 0.3)]

    cuts = [revolved([(BORE_R - 0.5, -1), (BORE_R + LEAD_IN + 1, -1), (BORE_R - 0.5, LEAD_IN + 0.5)])]
    for i in range(LUGS):
        a = i * 360 / LUGS
        cuts.append(revolved(groove, LUG_ARC + TWIST + 2 * arc, a - LUG_ARC / 2 - arc))
        cuts.append(revolved(channel, LUG_ARC + 2 * arc, a - LUG_ARC / 2 - arc))
        for turn in (0, TWIST):
            notch = detent(SPIGOT_R + 2 * c + DETENT, BORE_R - 0.8, -1, BUMP_Z + BUMP_LEN + c)
            cuts.append(notch.rotate(Axis.Z, a + 180 / LUGS + turn))
    return cuts


def socket():
    f = FIRST_LAYER_CHAMFER
    ring = revolved([
        (BORE_R, 0),
        (POLE_R - f, 0),
        (POLE_R, f),
        (POLE_R, SOCKET_H),
        (BORE_R, SOCKET_H),
    ])
    for cut in socket_cuts():
        ring -= cut
    return ring


def stand(foot_r, height):
    slope = (foot_r - POLE_R) / (height - NECK_H)
    wall = BELL_WALL * sqrt(1 + slope**2)
    neck = height - NECK_H
    inner = POLE_R - wall
    body = revolved([
        (foot_r, 0),
        (POLE_R, neck),
        (POLE_R, height),
        (SPIGOT_IN, height),
        (SPIGOT_IN, neck + inner - SPIGOT_IN),
        (inner, neck),
        (foot_r - wall, 0),
    ])

    middle = neck / 2
    half_h = neck * 0.32
    half_w = min(half_h * 0.8, pi * (foot_r + POLE_R) / 2 / WINDOWS - 3.5)
    diamond = Polygon((0, middle - half_h), (half_w, middle), (0, middle + half_h), (-half_w, middle), align=None)
    window = extrude(Plane.YZ * diamond, foot_r + 5)
    for i in range(WINDOWS):
        body -= window.rotate(Axis.Z, (i + 0.5) * 360 / WINDOWS)

    return body + spigot().moved(Location((0, 0, height)))


def export(part, name):
    export_stl(part, OUT_DIR / f"{name}.stl", tolerance=0.01, angular_tolerance=0.15)

