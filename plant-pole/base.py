from build123d import *
from ocp_vscode import show

from common import *

FOOT_R = 60
HEIGHT = 44
FLANGE_W = 12
FLANGE_T = 2


def make_base():
    flange = revolved([
        (FOOT_R - FLANGE_W, 0),
        (FOOT_R - FIRST_LAYER_CHAMFER, 0),
        (FOOT_R, FIRST_LAYER_CHAMFER),
        (FOOT_R, FLANGE_T),
        (FOOT_R - FLANGE_W, FLANGE_T),
    ])
    return stand(FOOT_R, HEIGHT) + flange


if __name__ == "__main__":
    base = make_base()
    export(base, "base")
    show(base)
