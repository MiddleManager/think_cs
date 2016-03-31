import tfuncs

def main():
    # Declarations
    wn = tfuncs.make_window("black", "Drunk Pirate Program")
    wanda = tfuncs.make_turtle("orange", "red", 5)

    s = 100.0 # size
    cross = 142.2
    roof = 70

    directions = [(-135, cross), (-135, s), (-135, cross), (-135, s),
                  (135, roof), (90, roof), (45, s), (90, s)]

    # Execution
    tfuncs.draw_list_tuples(wanda, directions)

    wn.mainloop()

main()
