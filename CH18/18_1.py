""" Always crashes. I'm not sure why or how to fix it really.
The one posted in the book doesn't even draw any lines. It's
very confusing really """

import turtle

def koch(t, order, size):
    t.forward(size)

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

def main():
    # init screen
    w = turtle.Screen()
    w.bgcolor("green")
    w.title("Recursive business")

    # init turtle
    tess = turtle.Turtle()

    koch(tess, 2, 50)

main()
