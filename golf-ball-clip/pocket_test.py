from build123d import *
from ocp_vscode import show

from common import *

MOUTHS = [40.6, 41.0, 41.4]
LABEL_SIZE = 4.5
LABEL_DEPTH = 0.6
SPACING = 70


def make_piece(mouth):
    piece = body([mouth], [TEE_HOLE] * TEES)
    label = Pos(POCKET_X, (FACE_R + RING_R - EDGE_R) / 2, THICKNESS) * Text(f"{mouth:.1f}", font_size=LABEL_SIZE)
    return piece - extrude(label, -LABEL_DEPTH)


def make_test():
    return [Pos(i * SPACING, 0) * make_piece(mouth) for i, mouth in enumerate(MOUTHS)]


if __name__ == "__main__":
    pieces = make_test()
    export(Compound(pieces), "pocket_test")
    show(*pieces, names=[f"mouth {m:.1f}" for m in MOUTHS])
