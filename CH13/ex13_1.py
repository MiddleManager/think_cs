old_file = open("words.txt", "r")
content = old_file.read()

new_file = open("new_words.txt", "w")

new_file.write(content[::-1])

new_file.close()
old_file.close()
