import tfuncs

def main():
    wn = tfuncs.make_window("black", "Wanda's Adventure")
    wanda = tfuncs.make_turtle("green", 3)

    for i in range(24):
        tfuncs.draw_sq(wanda, 50)
        wanda.right(15)


    wn.mainloop()

main()
