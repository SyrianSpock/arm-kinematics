from Cartesian2D import Cartesian2D
import numpy as np
from typing import List, Tuple

class Transform2D:
    def __init__(self, x: float, y: float, a: float):
        self.x = x
        self.y = y
        self.a = a
        self.T = np.matrix([
            [np.cos(a), -np.sin(a), x,],
            [np.sin(a),  np.cos(a), y,],
            [       0.,         0., 1.,],
        ])

    def apply(self, vec: Cartesian2D) -> Cartesian2D:
        x = self.T @ vec
        return Cartesian2D(x[0], x[1])

    def chain(self, other):
        x = self.x + other.x
        y = self.y + other.y
        a = self.a + other.a
        return Transform2D(x, y, a)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a

    def near(self, other, tol=1e-7):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + self.a == other.a) < tol**2

    def __repr__(self):
        return "Transform2D {}".format(self.p)

    def pos(self):
        return Cartesian2D(self.x, self.y)

cos30 = 0.86602540378
sin30 = 0.5
np.testing.assert_array_almost_equal(Transform2D(0., 0., np.deg2rad(30.)).T, np.matrix([[cos30, -sin30, 0.], [sin30, cos30, 0.], [0., 0., 1.]]))
np.testing.assert_array_almost_equal(Transform2D(1., 2., np.deg2rad(30.)).T, np.matrix([[cos30, -sin30, 1.], [sin30, cos30, 2.], [0., 0., 1.]]))


class Offset2D(Transform2D):
    def __init__(self, x: float, y: float, a: float):
        super().__init__(x, y, a)

class Rotation2D(Transform2D):
    def __init__(a: float):
        super().__init__(0., 0., a)

class TranslationX(Transform2D):
    def __init__(x: float):
        super().__init__(x, 0., 0.)

class TranslationY(Transform2D):
    def __init__(y: float):
        super().__init__(0., y, 0.)
