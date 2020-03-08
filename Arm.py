from Cartesian2D import Cartesian2D
from Transform2D import Transform2D, Offset2D
from Rect2D import Rect2D

import numpy as np
from typing import List, Tuple

def _rect_from_center_and_offset(center: Tuple[float, float], size: Tuple[float, float], offset: Offset2D) -> List[Tuple[float, float]]:
    p0 = Transform2D(center[0], center[1], offset).apply(np.matrix([- size[0] / 2., - size[1] / 2., 1.]).T)
    p1 = Transform2D(center[0], center[1], offset).apply(np.matrix([- size[0] / 2.,   size[1] / 2., 1.]).T)
    p2 = Transform2D(center[0], center[1], offset).apply(np.matrix([  size[0] / 2.,   size[1] / 2., 1.]).T)
    p3 = Transform2D(center[0], center[1], offset).apply(np.matrix([  size[0] / 2., - size[1] / 2., 1.]).T)
    return Rect2D([p0, p1, p2, p3])

# print(_rect_from_center_and_offset((0., 0.), (100., 100.), 0.))
# print(100*'*')
pts = _rect_from_center_and_offset((0., 0.), (100., 100.), 0.)
expected = Rect2D([Cartesian2D(-50., -50.), Cartesian2D(-50., 50.), Cartesian2D(50., 50.), Cartesian2D(50., -50.)])
assert(pts == expected)
pts = _rect_from_center_and_offset((0., 0.), (100., 100.), np.deg2rad(90.))
expected = Rect2D([Cartesian2D(50., -50.), Cartesian2D(-50., -50.), Cartesian2D(-50., 50.), Cartesian2D(50., 50.)])
assert(pts == expected)


class ArmTRRRR():
    def __init__(self, ls: List[float], os: List[Offset2D]):
        self.lengths = ls
        self.offsets = os
        self.joints = [0., 0., 0., 0., 0.]
        self.ts = None
        self._update()

    def _update(self):
        os = self.offsets
        ls = self.lengths
        j = self.joints
        self.ts = [
            Transform2D(os[0].x, os[0].y, os[0].a),
            Transform2D(0., ls[0], j[0]),
            Transform2D(os[1].x, os[1].y, os[1].a),
            Transform2D(0., ls[1], j[1]),
            Transform2D(os[2].x, os[2].y, os[2].a),
            Transform2D(0., ls[2], j[2]),
            Transform2D(os[3].x, os[3].y, os[3].a),
            Transform2D(0., ls[3], j[3]),
        ]

    def set(self, joints: List[float]):
        self.joints = joints
        self._update()

    def draw(self):
        pass

    def fwd_kinematics(self) -> List[Cartesian2D]:
        p0 = self.ts[0]
        p1 = p0.chain(self.ts[1]).chain(self.ts[0])
        p2 = p1.chain(self.ts[3]).chain(self.ts[2])
        p3 = p1.chain(self.ts[5]).chain(self.ts[4])
        p4 = p1.chain(self.ts[7]).chain(self.ts[6])
        return [p0.pos(), p1.pos(), p2.pos(), p3.pos(), p4.pos()]

no_offset = Offset2D(0., 0., 0.)
xy = ArmTRRRR([200., 100., 50., 25], [no_offset, no_offset, no_offset, no_offset]).fwd_kinematics()
# print(xy)
# assert ([Cartesian2D(0., 0.), Cartesian2D(0., 200.), Cartesian2D(0., 300.), Cartesian2D(0., 350.), Cartesian2D(0., 375)] == xy)

class ArmRR():
    def __init__(self, ls: List[float], os: List[Offset2D]):
        self.lengths = ls
        self.offsets = os
        self.joints = [0., 0.]
        self.ts = None
        self._update()

    def _update(self):
        os = self.offsets
        ls = self.lengths
        j = self.joints
        self.ts = [
            Transform2D(os[0].x, os[0].y, os[0].a),
            Transform2D(0., ls[0], j[0]),
        ]

    def set(self, joints: List[float]):
        self.joints = joints
        self._update()

    def draw(self):
        pass

    def fwd_kinematics(self) -> List[Cartesian2D]:
        p0 = self.ts[0]
        p1 = p0.chain(self.ts[1]).chain(self.ts[0])
        return [p0.pos(), p1.pos()]

    def __repr__(self):
        return "ArmRR Offsets[{}]]".format(self.offsets)

no_offset = Offset2D(0., 0., 0.)
xy = ArmRR([200., 100.], [no_offset, no_offset]).fwd_kinematics()
print(xy)
# assert ([Cartesian2D(0., 0.), Cartesian2D(0., 200.), Cartesian2D(0., 300.), Cartesian2D(0., 350.), Cartesian2D(0., 375)] == xy)
