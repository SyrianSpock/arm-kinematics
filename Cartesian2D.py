class Cartesian2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Cartesian2D(x, y)

    def __eq__(self, other):
        return self.near(other)

    def near(self, other, tol=1e-7):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) < tol**2

    def __repr__(self):
        return "Point [{}, {}]".format(self.x, self.y)


assert(Cartesian2D(10., 10.).near(Cartesian2D(5., 5.) + Cartesian2D(5., 5.)))
assert(Cartesian2D(10., 10.).near(Cartesian2D(2., 3.) + Cartesian2D(8., 7.)))
