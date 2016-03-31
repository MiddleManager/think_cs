import tfuncs


def main():
    # Declarations
    wn = tfuncs.make_window("black", "Drunk Pirate Program")
    wanda = tfuncs.make_turtle("orange", "red", 5)

    directions = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

    # Execution
    tfuncs.draw_list_tuples(wanda, directions)

    wn.mainloop()

main()
