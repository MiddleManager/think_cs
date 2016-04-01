# Yet to to solve
# ex 3, 4, 5 because im shit at geometry
# ill look it up on wikipedia when I get home

import testing as t

class Point():
    """ Point class represents x & y coordinates and manipulates them. """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ computes distance from origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return ("({0}, {1})".format(self.x, self.y))

    def midpoint(self, target):
        """ Finds the midpoint from a point object and itself """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2

        return Point(mx, my)

    def distance(self, p):
        """ Returns the distance from current object to another """
        nx = (self.x - p.x)**2
        ny = (self.y - p.y)**2
        distance = (nx + ny) ** 0.5
        return distance

    def reflect_x(self):
        """ Returns a reflection of x """
        return Point(-self.x, self.y)
"""
def testing_suite():
    print("Beginning Tests\n--------")
    point1 = Point(1, 2)
    point2 = Point(4, 6)

    t.test(point1.distance(point2) == 5.0)


testing_suite()
"""
