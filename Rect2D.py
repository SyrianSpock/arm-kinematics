from typing import List
from Cartesian2D import Cartesian2D

class Rect2D:
    def __init__(self, pts: List[Cartesian2D]):
        self.pts = pts

    def __eq__(self, other):
        return self.near(other)

    def near(self, other, tol=1e-7):
        return self.pts[0].near(other.pts[0], tol) and self.pts[1].near(other.pts[1], tol) and self.pts[2].near(other.pts[2], tol) and self.pts[3].near(other.pts[3], tol)

    def __repr__(self):
        return "Rectangle [[{}], [{}], [{}], [{}]]".format(self.pts[0], self.pts[1], self.pts[2], self.pts[3])
