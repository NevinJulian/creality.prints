from pathlib import Path

from build123d import *

OUT_DIR = Path(__file__).parent

FIRST_LAYER_CHAMFER = 0.4
EDGE_R = 1.2

HANDLE_L = 125
HANDLE_T = 5.5
NECK_W = 11
HANDLE = [(0, 0), (3.5, 10), (11, 15.2), (19, 15.6), (28, 13.5), (40, 9), (60, 7.4), (90, 6.4), (HANDLE_L, NECK_W / 2)]

SUN_SIZE = 23
SUN_LINE = 0.85
SUN_DEPTH = 0.6
SUN_X = 17

FACE = [(-18, 21), (-1, 27), (17, 20), (24, -1), (17, -15), (-3, -23), (-17, -16), (-27, 4)]
RAYS = [
    [(-9, 24), (-13, 42), (-10, 50)],
    [(2, 26), (10, 45), (28, 50)],
    [(-21, 16), (-28, 20), (-33, 28), (-37, 40), (-35, 45)],
    [(17, 20), (29, 37), (48, 30)],
    [(-27, 4), (-43, 12), (-48, 20), (-48, 29)],
    [(21, 9), (35, 15), (38, 15), (43, 12), (50, 2)],
    [(-22, -10), (-44, -6), (-50, 4)],
    [(24, -1), (37, -4), (41, -15), (40, -24)],
    [(17, -15), (23, -17), (25, -22), (25, -35), (20, -45)],
    [(-17, -16), (-26, -27), (-40, -26), (-45, -21)],
    [(8, -20), (7, -38), (-8, -50)],
    [(-5, -23), (-6, -35), (-15, -42), (-27, -43)],
]
EYES = [
    [(-18, 5), (-14, 9), (-10, 8)],
    [(3, 11), (7, 14), (11, 13)],
]
NOSE = [(-3, 6), (-3, -1), (-1, -1)]
MOUTH = [(-7, -13), (-2, -15), (1, -14), (5, -10), (6, -5), (2, -8), (-2, -10), (-5, -10), (-11, -8)]


def sun():
    k = SUN_SIZE / 100
    strokes = [FACE + FACE[:1], *RAYS, *EYES, NOSE]
    shapes = []
    for stroke in strokes:
        points = [Vector(x * k, y * k) for x, y in stroke]
        for a, b in zip(points, points[1:]):
            shapes.append(SlotCenterPoint((a + b) / 2, b, SUN_LINE))
    mouth = Polygon(*[(x * k, y * k) for x, y in MOUTH], align=None)
    shapes.append(offset(mouth, SUN_LINE / 2))
    drawing = Sketch() + shapes
    return Pos(SUN_X, 0) * drawing.rotate(Axis.Z, -90)


def handle():
    upper = Spline(*HANDLE, tangents=[(0, 1), (1, 0)], tangent_scalars=[1, 1])
    return upper, upper.mirror(Plane.XZ)


def side_profile(rise, *rest):
    top = Spline((HANDLE_L - 10, HANDLE_T), rise, tangents=[(1, 0), (1, 0)]) + Polyline(rise, *rest)
    end = rest[-1]
    base = Polyline((end[0], 0), (-1, 0), (-1, HANDLE_T), (HANDLE_L - 10, HANDLE_T))
    outline = make_face([base, top, Line(end, (end[0], 0))])
    return extrude(Plane.XZ * outline, 50, both=True)


def wall_edges(part, bottom):
    edges = []
    for face in part.faces():
        if abs(face.normal_at().Z) > 0.01:
            continue
        for edge in face.edges():
            bb = edge.bounding_box()
            if bb.size.Z < 0.9 * edge.length and (bb.max.Z < 0.01) == bottom:
                edges.append(edge)
    return edges


def finish(part):
    part = fillet(wall_edges(part, bottom=False), EDGE_R)
    return chamfer(wall_edges(part, bottom=True), FIRST_LAYER_CHAMFER)


def imprint(part):
    groove = extrude(Plane.XY.offset(HANDLE_T) * sun(), -SUN_DEPTH)
    return part - groove


def inlay():
    return extrude(Plane.XY.offset(HANDLE_T - SUN_DEPTH) * sun(), SUN_DEPTH)


def export(part, name):
    export_stl(part, OUT_DIR / f"{name}.stl", tolerance=0.01, angular_tolerance=0.15)
