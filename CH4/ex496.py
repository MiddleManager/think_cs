import tfuncs

def main():
    wn = tfuncs.make_window("black", "Wanda's Adventure")
    wanda = tfuncs.make_turtle("green", 3)

    tfuncs.draw_equitriangle(wanda, 20)


    wn.mainloop()

main()
