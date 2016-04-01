import testing as t
import point

class Rectangle():
    """ A class for rectangular objects """

    def __init__(self, posn, w, h):
        """ posn should be a Point obj. w & h should be int"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        """ Changes the return type if you print it as a str"""
        return("({0}, {1}, {2})".format(self.corner, self.width, self.height))

    def grow(self, delta_width, delta_height):
        """ Changes the relative size """
        self.width += delta_width
        self.height += delta_height

    def move(self, delta_x, delta_y):
        """ Changes the pos of the upper corner"""
        self.corner.x += delta_x
        self.corner.y += delta_y

    def area(self):
        """ Returns the area of itself """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of itself"""
        return self.width + self.height

    def flip(self):
        """ Flips self.height and self.width """
        self.height, self.width = self.width, self.height

    def contains(self, p):

        if not (self.corner.x <= p.x and p.x < self.corner.x + self.width):
            #print("x is false")
            return False

        if not (self.corner.y <= p.y and p.y < self.corner.y + self.height):
            #print("y is false")
            return False

        return True


    def rect_overlap(self, rect):
        """ Checks if two points collide """
        rect_x = rect.corner.x + rect.width
        rect_y = rect.corner.y + rect.height

        if not (self.corner.x <= rect_x and rect_x < self.corner.x + self.width):
            return False

        if not (self.corner.y <= rect_y and rect_y < self.corner.y + self.height):
            return False

        return True

def test_suite():
    r = Rectangle(point.Point(0, 0), 10, 5)
    t.test(r.contains(point.Point(0, 0)))
    t.test(r.contains(point.Point(3, 3)))
    t.test(not r.contains(point.Point(3, 7)))
    t.test(not r.contains(point.Point(3, 5)))
    t.test(r.contains(point.Point(3, 4.99999)))
    t.test(not r.contains(point.Point(-3, -3)))

    """
    box = Rectangle(point.Point(0, 0), 2, 3)
    bomb = Rectangle(point.Point(0, 0), 1, 2)

    print("Collision {0}: {1}".format(bomb, box.point_collide(bomb)))

    #print(box.point_collide(bomb))


    print("box: ", box)
    print("bomb: ", bomb)

    box.grow(12, 23)
    box.move(-54, 56)
    print("Updating box: ---")
    print("box: ", box)

    print("box area: ", str(box.area()))
    print("box perimeter: ", str(box.perimeter()))
    print("Flipping box: ---")
    box.flip()
    print("box: ", box)
    """

test_suite()
