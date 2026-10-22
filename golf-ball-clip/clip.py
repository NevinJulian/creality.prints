from build123d import *
from ocp_vscode import show

from common import *

TEE_LENGTH = 54
TEE_SHANK = 5
TEE_HEAD = 11
HEAD_H = 8
TIP_H = 10


def make_clip():
    return body([MOUTH] * BALLS, [TEE_HOLE] * TEES, clip=True)


def tee():
    r = TEE_SHANK / 2
    shank_h = TEE_LENGTH - HEAD_H - TIP_H
    shank = Cylinder(r, shank_h, align=(Align.CENTER, Align.CENTER, Align.MAX))
    tip = Cone(0.3, r, TIP_H, align=(Align.CENTER, Align.CENTER, Align.MAX))
    head = Cone(r, TEE_HEAD / 2, HEAD_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return shank + Pos(0, 0, -shank_h) * tip + head


def preview():
    ys = pocket_ys(BALLS)
    balls = [Pos(POCKET_X, y, THICKNESS / 2) * Sphere(BALL_D / 2) for y in ys]
    tees = [Pos(-SPINE / 2, ty, THICKNESS) * tee() for y in ys for ty in tee_ys(y)]
    return balls, tees


if __name__ == "__main__":
    clip = make_clip()
    export(clip, "clip")
    balls, tees = preview()
    show(
        clip,
        *balls,
        *tees,
        names=["clip"] + [f"ball {i + 1}" for i in range(len(balls))] + [f"tee {i + 1}" for i in range(len(tees))],
        colors=["darkorange"] + ["white"] * len(balls) + ["burlywood"] * len(tees),
    )
