# A collection of functions that I'll use for working with turtles
# Some of this code is my own, some of it is from the think like a
# computer scientist.

import turtle

def draw_sq(t, len):
    """ Passed in length and the turtle. Draws a square """

    for i in range(4):
        t.right(90)
        t.forward(len)

def draw_poly(t, n, size):
    """ Turtle, number of sides (3+), size
    Draws any polygon."""

    if (n < 3):
        print("n is too small. Can't calculate")
        return None

    angle = 180 - (((n - 2) * 180) / n)

    for i in range(n):
        t.forward(size)
        t.left(angle)

def draw_equitriangle(t, sz):
    """ Turtle, size. Draws an equlateral triangle """
    draw_poly(t, 3, sz)

def draw_star(t, size):
    for i in range(5):
        t.forward(size)
        t.right(144)

def draw_bar(t, h, w):
    """ Turtle, height (list), width
    Draws a bar for a bar chart"""

    # Dynamically assign fill color
    if (h > 200):
        t.color("orange", "red")
    elif (h > 100):
        t.color("orange", "yellow")
    else:
        t.color("orange", "green")

    t.begin_fill()
    t.left(90)
    t.forward(h)

    # If the value is positive write on top of the bar, else bottom of bar
    if (h > 0):
        t.write ("  " + str(h))
    else:
        t.penup()
        t.forward(-15)
        t.write("  " + str(h))
        t.forward(15)
        t.pendown()

    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

def draw_list_tuples(t, list):
    """ Takes a turtles and a list of tuples
    Draws the path of the turtle """

    for i in list:
        t.right(i[0])
        t.forward(i[1])

def make_window(color, title):
    """ bg color and window title parameters.
    Creates a standard issue window. """

    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)

    return w

def make_turtle(color, s_color, size):
        """ Turtle color and pensize parameters.
        Returns a turtle object """

        t = turtle.Turtle()
        t.color(color, s_color)
        t.pensize(size)
        t.speed(20)

        return t
