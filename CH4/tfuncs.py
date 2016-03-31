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
    """ Takes in a turtle and the length
    Draws a simple star"""
    for i in range(5):
        t.forward(size)
        t.right(144)

def make_window(color, title):
    """ bg color and window title parameters.
    Creates a standard issue window. """

    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)

    return w

def make_turtle(color, size):
        """ Turtle color and pensize parameters.
        Returns a turtle object """

        t = turtle.Turtle()
        t.color(color)
        t.pensize(size)

        return t
