from pathlib import Path

from bd_warehouse.thread import Thread
from build123d import *

OUT_DIR = Path(__file__).parent

UNDERCUT = 16
OPENING = 50
THINNEST = 15
CUP_D = 66
SLOT_ANGLE = 0

TABLE = 25
TABLE_EDGE = 9

CLEARANCE = 0.3
FIRST_LAYER_CHAMFER = 0.4

WIDTH = 36
SPINE = 12
TOP_ROOT = 12
TOP_TIP = 7
BOTTOM = 20

PITCH = 4
THREAD_D = 16
THREAD_DEPTH = 1.6
THREAD_PLAY = 0.35
NUT_AF = 24
NUT_H = 12

PAD_D = 30
PAD_H = 7
PAD_SOCKET = 3

RING_H = 75
RING_WALL = 2.4
FLOOR = 2.4
CUP_PLAY = 1.5
SLOT_W = 26
SLOT_BOTTOM = 8
PLATE = 5
FIN = 5
NECK = 8
END_WALL = 3
CHANNEL_BASE = 4

SCREW_X = UNDERCUT + PAD_D / 2 + 5
TOP_REACH = SCREW_X + PAD_D / 2
BOTTOM_REACH = SCREW_X + NUT_AF / 2 + 5
NUT_Z = -OPENING - BOTTOM / 2
CHANNEL = (-SPINE - PLATE - 2 * CLEARANCE, -SPINE)
FIN_X = CHANNEL[0] - FIN
FIN_TOP = -NECK - 2 * CLEARANCE
PLATE_W = WIDTH - 2 * END_WALL - 2 * CLEARANCE

ROOT_R = THREAD_D / 2 - THREAD_DEPTH
ROOT_W = PITCH - 0.4
APEX_W = ROOT_W - 2 * THREAD_DEPTH


def thread(length, play=0.0, ends=("square", "square")):
    if play:
        return Thread(
            apex_radius=ROOT_R + play,
            apex_width=APEX_W,
            root_radius=THREAD_D / 2 + play,
            root_width=ROOT_W,
            pitch=PITCH,
            length=length,
            end_finishes=ends,
        )
    return Thread(
        apex_radius=THREAD_D / 2,
        apex_width=APEX_W,
        root_radius=ROOT_R,
        root_width=ROOT_W,
        pitch=PITCH,
        length=length,
        end_finishes=ends,
    )


def teardrop(r):
    s = r / 2**0.5
    return Circle(r) + Polygon((0, 0), (s, s), (0, 2 * s), (-s, s), align=None)


def export(part, name):
    export_stl(part, OUT_DIR / f"{name}.stl", tolerance=0.01, angular_tolerance=0.15)
