from pathlib import Path

from build123d import *

SVG = Path(__file__).parent / "sun.svg"
STROKE = 5.38
MITER_LIMIT = 10


def flatten(wire):
    edges = list(wire.edges())
    points = [wire @ 0]
    while edges:
        edge = min(edges, key=lambda e: min((e @ 0 - points[-1]).length, (e @ 1 - points[-1]).length))
        edges.remove(edge)
        steps = 1 if edge.geom_type == GeomType.LINE else 12
        samples = [edge @ (i / steps) for i in range(steps + 1)]
        if (samples[-1] - points[-1]).length < (samples[0] - points[-1]).length:
            samples.reverse()
        points += [p for p in samples[1:] if (p - points[-1]).length > 0.01]
    return points


def normal(a, b):
    d = (b - a).normalized()
    return Vector(-d.Y, d.X)


def polygon(*points):
    area = sum(a.X * b.Y - b.X * a.Y for a, b in zip(points, points[1:] + points[:1]))
    return Polygon(*(points if area > 0 else points[::-1]), align=None)


def stroke(points, r, closed):
    pieces = []
    for a, b in zip(points, points[1:]):
        n = normal(a, b) * r
        pieces.append(polygon(a + n, b + n, b - n, a - n))
    corners = list(zip(points, points[1:], points[2:]))
    if closed:
        corners.append((points[-2], points[0], points[1]))
    for a, b, c in corners:
        n1, n2 = normal(a, b), normal(b, c)
        turn = n1.cross(n2).Z
        if abs(turn) < 1e-4:
            continue
        side = -1 if turn > 0 else 1
        outer = [b + n1 * r * side, b + n2 * r * side]
        mid = (n1 + n2).normalized()
        reach = r / mid.dot(n1)
        if reach < MITER_LIMIT * r:
            outer.insert(1, b + mid * reach * side)
        pieces.append(polygon(b, *outer))
    return pieces


def sun(width):
    pieces = []
    for wire in import_svg(SVG):
        pieces += stroke(flatten(wire), STROKE / 2, wire.is_closed)
    drawing = Sketch() + pieces
    drawing = scale(drawing, width / drawing.bounding_box().size.X)
    return Pos(-drawing.bounding_box().center()) * drawing
