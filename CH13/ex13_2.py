# Write a program that reads a file and prints only those lines that contain the substring snake.

new_file = open("words.txt", "r")

while True:
    line = new_file.readline()

    if line == "":
        break

    if "Snakes" in line:
        print(line)

new_file.close()
