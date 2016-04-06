import turtle
import tfuncs

class TurtleGTX(turtle.Turtle):
    """ A simple overwrite of the turtle function that's not really
    all that useful. m_forward stops working after a certain distance,
    and will need a new call to new_tyres() """

    def __init__(self):
        super(TurtleGTX, self).__init__()
        self.odometer = 0

        self.tyre_durability = 50
        self.tyre_distance_left = self.new_tyres()

    def new_tyres(self):
        return self.odometer + self.tyre_durability

    def m_forward(self, distance):
        if self.check_tyre():
            self.add_odometer(distance)
            self.forward(distance)
        else:
            print("Get a new tire!")

    def add_odometer(self, num):
        if num >= 0:
            self.odometer += num
        else:
            self.odometer += num * -1

    def check_tyre(self):
        if self.odometer < self.tyre_distance_left:
            return True
        return False


if __name__ == "__main__":
    wn = tfuncs.make_window("green", "TurtleGTX test")

    tess = TurtleGTX()

    tess.m_forward(35)
    tess.m_forward(35)
    tess.m_forward(35)

    print(tess.odometer)
    input()
