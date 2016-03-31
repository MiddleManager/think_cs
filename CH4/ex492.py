import tfuncs

def repos(size, tur):
    tur.penup()
    tur.forward(size)
    tur.left(90)
    tur.forward(size)
    tur.right(90)
    tur.pendown()

def main():
    wn = tfuncs.make_window("black", "Wanda's Adventure")
    wanda = tfuncs.make_turtle("green", 3)

    default_len = 20

    for i in range(0,10, 2):
        tfuncs.draw_sq(default_len*(i + 1), wanda)

        # Repositions wanda to reset her to her original place
        repos(default_len, wanda)


    wn.mainloop()

main()
