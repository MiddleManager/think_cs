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

a = Point(3, 4)
b = Point(8, 11)
c = a.midpoint(c)
print ("C Str: " + str(a))

print("x: {0} \ny: {1}".format(a.x, a.y))
print("Distance from origin: {0}".format(a.distance_from_origin()))
print("Str form: {0}".format(str(a)))
