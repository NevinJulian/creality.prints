from math import atan2, degrees

from build123d import *
from ocp_vscode import show

from base import make_base
from cap import make_cap
from clip import THICKNESS, make_clip
from common import *
from pole_module import make_module, node
from pot import COLUMN_TOP, make_pot
from watering_aid import make_watering_aid

MODULES = 3


def on_strut(clip, row, column, hand=1):
    start = node(row, column)
    end = node(row + 1, column if hand > 0 else column - 1)
    middle = (start + end) / 2
    clip = clip.moved(Location((0, 0, -THICKNESS / 2))).rotate(Axis.Z, degrees(atan2(middle.Y, middle.X)))
    return clip.moved(Location(middle))


def stacked(bottom, bottom_top, top):
    module = make_module()
    parts = [bottom]
    for i in range(MODULES):
        parts.append(module.rotate(Axis.Z, -TWIST * (i + 1)).moved(Location((0, 0, bottom_top + i * STEP))))
    parts.append(top.rotate(Axis.Z, -TWIST * (MODULES + 1)).moved(Location((0, 0, bottom_top + MODULES * STEP))))
    return parts


if __name__ == "__main__":
    parts = {
        "pole_module": make_module(),
        "base": make_base(),
        "pot": make_pot(),
        "cap": make_cap(),
        "watering_aid": make_watering_aid(),
        "clip_right": make_clip(1),
        "clip_left": make_clip(-1),
    }
    for name, part in parts.items():
        export(part, name)

    stack = stacked(parts["pot"], COLUMN_TOP, parts["watering_aid"])
    clips = [
        on_strut(parts["clip_right"], 3, 6),
        on_strut(parts["clip_left"], 7, 1, hand=-1),
    ]
    clips = [c.rotate(Axis.Z, -TWIST).moved(Location((0, 0, COLUMN_TOP))) for c in clips]
    show(*stack, *clips, names=["pot"] + [f"module {i + 1}" for i in range(MODULES)] + ["watering aid", "clip", "clip"])
