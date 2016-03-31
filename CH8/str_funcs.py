import string
import testing

def remove_punc(str):
    """ Removes all the punctuation in a string"""
    new_str = ""

    for i in str:
        if i not in string.punctuation:
            new_str += i

    return new_str

def quack():
    """ Prints out a specific list of names"""
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O":
            print(letter + "u" + suffix)
        elif letter == "Q":
            print (letter + "u" + suffix)
        else:
            print(letter + suffix)

def char_count(str, char):
    """ Counts the characters in a string"""
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count

def sum_text(str, char):
    """ Summarises a given string into word count,
    and occurences and percentage of char """
    # Process the string into a list
    str = remove_punc(str)
    str = str.lower()
    list = str.split()
    word_count = len(list)

    # Find the occurences of input
    char_occur = 0

    for i in list:
        if char in i:
            char_occur += 1

    char_perc = char_occur / word_count
    char_perc = int(char_perc * 100)

    # Print the data
    txt = ("Your text contains {0} words, of which {1} ({2}%) " +
          "contain the letter {3}")

    print(txt.format(word_count, char_occur, char_perc, char))

def draw_multi_table():
    """ Draws a sick looking multiplication table
    Supports 12 digits right now"""

    # Draws the horizontal outline
    form = "\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}"
    print (form.format(1,2,3,4,5,6,7,8,9,10,11,12))
    print ("  :" + "-" * 95)

    for i in range(1,13):
        # Draws the vertical outline
        print("{0:>2}:\t".format(i), end="")
        for j in range(1,13):
            # Draws the main part of the table
            print("{0}\t".format(i*j), end="")
        print("")

def reverse_str(str):
    return str[::-1]

def mirror_str(str):
    return str + str[::-1]

def remove_letter(char, str):

    new_str = ""

    for i in str:
        if i != char:
            new_str += i

    return new_str

def is_palindrome(str):
    if (str == reverse_str(str)):
        return True
    else:
        return False

def sub_string_count(sub_str, full_str):
        """ Counts the number of occurences of a substring in a string"""

        # Return immediately
        if sub_str not in full_str:
            return 0

        count = 0
        slice = ""

        # Reconstructs a piece of the full str and then compares it to the
        # sub str.
        for i in range(len(full_str)):
            slice = full_str[i:i+len(sub_str)]

            if slice == sub_str:
                count += 1
                print("Count: " + str(count))

        return count

def del_sub_str(sub_str, full_str):
    search = full_str.find(sub_str)

    if search == -1:
        return full_str

    new_str = full_str[:search] + full_str[search+len(sub_str):]
    print(new_str)

    return new_str

def del_all_sub_str(sub_str, full_str):

    while (sub_str in full_str):
        full_str = del_sub_str(sub_str, full_str)

    return full_str

def test_suite():
    testing.test(remove_punc("I never, ever, said that to you!?!")
                          == "I never ever said that to you")

    #quack()

    testing.test(char_count("Apple", "A") == 1)
    testing.test(char_count("", "a") == 0)

    poem = """
    We real cool. We
    Left school. We

    Lurk late. We
    Strike straight. We

    Sing sin. We
    Thin gin. We

    Jazz June. We
    Die soon."""

    sum_text(poem, "e")

    draw_multi_table()

    testing.test(reverse_str("happy") == "yppah")
    testing.test(reverse_str("Python") == "nohtyP")
    testing.test(reverse_str("") == "")
    testing.test(reverse_str("a") == "a")

    testing.test(mirror_str("good") == "gooddoog")
    testing.test(mirror_str("Python") == "PythonnohtyP")
    testing.test(mirror_str("") == "")
    testing.test(mirror_str("a") == "aa")


    testing.test(remove_letter("a", "apple") == "pple")
    testing.test(remove_letter("a", "banana") == "bnn")
    testing.test(remove_letter("z", "banana") == "banana")
    testing.test(remove_letter("i", "Mississippi") == "Msssspp")
    testing.test(remove_letter("b", "") == "")
    testing.test(remove_letter("b", "c") == "c")

    testing.test(is_palindrome("abba") == True)
    testing.test(not is_palindrome("abab") == True)
    testing.test(is_palindrome("tenet") == True)
    testing.test(not is_palindrome("banana") == True)
    testing.test(is_palindrome("straw warts") == True)
    testing.test(is_palindrome("a") == True)
    # testing.test(is_palindrome(""))    # Is an empty string a palindrome?

    testing.test(sub_string_count("is", "Mississippi") == 2)
    testing.test(sub_string_count("an", "banana") == 2)
    testing.test(sub_string_count("ana", "banana") == 2)
    testing.test(sub_string_count("nana", "banana") == 1)
    testing.test(sub_string_count("nanan", "banana") == 0)
    testing.test(sub_string_count("aaa", "aaaaaa") == 4)

    testing.test(del_sub_str("an", "banana") == "bana")
    testing.test(del_sub_str("cyc", "bicycle") == "bile")
    testing.test(del_sub_str("iss", "Mississippi") == "Missippi")
    testing.test(del_sub_str("eggs", "bicycle") == "bicycle")

    print("----")
    testing.test(del_all_sub_str("an", "banana") == "ba")
    testing.test(del_all_sub_str("cyc", "bicycle") == "bile")
    testing.test(del_all_sub_str("iss", "Mississippi") == "Mippi")
    testing.test(del_all_sub_str("eggs", "bicycle") == "bicycle")


test_suite()
