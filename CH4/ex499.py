import tfuncs

def main():
    wn = tfuncs.make_window("black", "Wanda's Adventure")
    wanda = tfuncs.make_turtle("green", 3)

    for i in range(5):
        tfuncs.draw_star(wanda, 100)

        # Creates the giant star pattern
        wanda.penup()
        wanda.forward(350)
        wanda.right(144)
        wanda.pendown()
    wn.mainloop()s

main()
