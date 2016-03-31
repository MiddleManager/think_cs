import tfuncs

def main():
    wn = tfuncs.make_window("black", "Wanda's Adventure")
    wanda = tfuncs.make_turtle("green", 3)

    for i in range(1, 100):
        wanda.right(89)
        wanda.forward(i * 5)


    wn.mainloop()

main()
