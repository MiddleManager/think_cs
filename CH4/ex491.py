import tfuncs

def main():
    wn = tfuncs.make_window("black", "Wanda's Adventure")

    wanda = tfuncs.make_turtle("green", 3)

    for i in range(4):
        tfuncs.draw_sq(20, wanda)
        wanda.penup()
        wanda.forward(40)
        wanda.pendown()

    wn.mainloop()

main()
