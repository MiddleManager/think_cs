old_file = open("words.txt", "r")
new_file = open("linenumbers.txt", "w")

linenum = 0 # the lefthand linenumber to be printed
str_form = "{0:<5} {1}"

while True:
    linenum += 1
    line = old_file.readline()

    if line == "":
        break


    print(str_form.format(linenum, line), end="")
    new_file.write(str_form.format(linenum, line))

old_file.close()
