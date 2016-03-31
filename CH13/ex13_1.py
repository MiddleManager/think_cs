# Declarations
old_file = open("words.txt", "r")
new_file = open("new_words.txt", "w")
content = []

# Reads all the lines into a list
while True:
    line = old_file.readline()

    if line == "":
        break

    content.append(line)

# Writes those lines in reverse to the new file
for i in range(len(content)-1, -1, -1):
    print(i)
    new_file.write(content[i])

new_file.close()
old_file.close()
