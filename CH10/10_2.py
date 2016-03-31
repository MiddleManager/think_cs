import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Turtles on the move")
wn.bgcolor("lightgreen")

wanda = turtle.Turtle()
wanda.color("green")

alex = turtle.Turtle()
alex.color("red")
alex.forward(100)

def wanda_handler(x, y):
    print("Wanda clicked at coords {0} and {1}".format(x, y))
    wanda.right(43)
    wanda.forward(65)

def alex_handler(x, y):
    print("Alex clicked at coords {0} and {1}".format(x, y))
    alex.left(54)
    alex.forward(45)

wanda.onclick(wanda_handler)
alex.onclick(alex_handler)

wn.mainloop()
