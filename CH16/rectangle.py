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



box = Rectangle(point.Point(0, 0), 100, 200)
bomb = Rectangle(point.Point(100, 80), 5, 10)    # In my video game

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
