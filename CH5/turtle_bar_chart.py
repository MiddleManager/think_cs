# Produces a bar chart from a list of data
import tfuncs

def main():
    wn = tfuncs.make_window("black", "The majestic bar chart")
    wanda = tfuncs.make_turtle("orange", "red", 3)

    data = [48, -117, 200, 240, -60, 260, 220]

    for i in data:
        tfuncs.draw_bar(wanda, i, 40)

    wn.mainloop()



main()
