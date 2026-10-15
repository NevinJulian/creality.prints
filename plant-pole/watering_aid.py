from math import cos, sin

from build123d import *
from ocp_vscode import show

from common import *

CUP_R = 44
HEIGHT = 84
WALL = 2.4
FLARE = 40
FUNNEL = 40
DRIP_D = 2
DRIP_R = 4


def make_watering_aid():
    flare_rise = 1 / tan(radians(FLARE))
    funnel_rise = 1 / tan(radians(FUNNEL))
    f = FIRST_LAYER_CHAMFER
    inner = CUP_R - WALL
    flare_in = POLE_R - WALL / cos(radians(FLARE))
    funnel_t = WALL / sin(radians(FUNNEL))
    underside = (inner - DRIP_R) * funnel_rise

    body = revolved([
        (DRIP_D / 2, 0),
        (DRIP_R, 0),
        (inner, underside),
        (inner, SOCKET_H + (inner - flare_in) * flare_rise),
        (flare_in, SOCKET_H),
        (BORE_R, SOCKET_H),
        (BORE_R, 0),
        (POLE_R - f, 0),
        (POLE_R, f),
        (POLE_R, SOCKET_H),
        (CUP_R, SOCKET_H + (CUP_R - POLE_R) * flare_rise),
        (CUP_R, HEIGHT),
        (inner, HEIGHT),
        (inner, underside + funnel_t),
        (DRIP_D / 2, (DRIP_D / 2 - DRIP_R) * funnel_rise + funnel_t),
    ])
    for cut in socket_cuts():
        body -= cut
    return body


if __name__ == "__main__":
    watering_aid = make_watering_aid()
    export(watering_aid, "watering_aid")
    show(watering_aid)
