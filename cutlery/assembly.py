from build123d import *
from ocp_vscode import show

from common import *
from fork import make_fork
from knife import make_knife
from spoon import make_spoon

GAP = 40


if __name__ == "__main__":
    parts = {
        "fork": make_fork(),
        "spoon": make_spoon(),
        "knife": make_knife(),
    }
    for name, part in parts.items():
        export(part, name)
    export(inlay(), "sun")

    shown, names = [], []
    for i, (name, part) in enumerate(parts.items()):
        place = Location((0, (1 - i) * GAP, 0))
        shown += [part.moved(place), inlay().moved(place)]
        names += [name, f"{name} sun"]
    show(*shown, names=names, colors=["wheat", "darkgreen"] * len(parts))
