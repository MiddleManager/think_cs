old_file = open("linenumbers.txt", "r")
new_file = open("removed_linenumbers.txt", "w")

while True:
    line = old_file.readline()

    if line == "":
        break

    print(line[6:], end="")
    new_file.write(line[6:])

old_file.close()
new_file.close()
