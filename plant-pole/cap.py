from build123d import *
from ocp_vscode import show

from common import *

ROOF = 42
TIP_R = 1.5


def make_cap():
    rise = 1 / tan(radians(ROOF))
    f = FIRST_LAYER_CHAMFER
    tip = SOCKET_H + (POLE_R - TIP_R) * rise
    body = revolved([
        (BORE_R, 0),
        (POLE_R - f, 0),
        (POLE_R, f),
        (POLE_R, SOCKET_H),
        (TIP_R, tip),
        (0, tip),
        (0, SOCKET_H + (BORE_R - 0.6) * rise),
        (0.6, SOCKET_H + (BORE_R - 0.6) * rise),
        (BORE_R, SOCKET_H),
    ])
    for cut in socket_cuts():
        body -= cut
    return body


if __name__ == "__main__":
    cap = make_cap()
    export(cap, "cap")
    show(cap)
