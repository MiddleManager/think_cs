import testing
import string

def cleanword(word):
    new_str = ""

    for i in word:
        if i not in string.punctuation:
            new_str += i


    return new_str

def has_dashdash(str):
    if "--" in str:
        return True
    else:
        return False


def extract_words(words):
    """ Extracts a cleaned up list of words from a string """
    words = words.lower()

    if "--" in words:
        hash_i = words.find("--")
        words = words[:hash_i] + " " + words[hash_i+2:]

    words = cleanword(words)
    words = words.split()

    return words

def wordcount(sub_str, full_list):
    """ Returns an int of all the time a word is used """
    count = 0

    for i in full_list:
        if sub_str == i:
            count += 1

    return count




def wordset(word_set):
    """ Returns a list of all the words used in the list at least once"""

    new_word_set = []

    for i in word_set:
        if i not in new_word_set:
            new_word_set.append(i)

    return new_word_set


def longestword(long_word_set):
    """ Returns an int of the longest word """

    longest_word = 0

    for i in long_word_set:
        if len(i) > longest_word:
            longest_word = len(i)

    return longest_word

def test_suite():
    testing.test(cleanword("what?") == "what")
    testing.test(cleanword("'now!'") == "now")
    testing.test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

    testing.test(has_dashdash("distance--but"))
    testing.test(not has_dashdash("several"))
    testing.test(has_dashdash("spoke--"))
    testing.test(has_dashdash("distance--but"))
    testing.test(not has_dashdash("-yo-yo-"))

    testing.test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
          ['now','is','the','time','now','is','the','time','yes','now'])
    testing.test(extract_words("she tried to curtsey as she spoke--fancy") ==
          ['she','tried','to','curtsey','as','she','spoke','fancy'])

    testing.test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    testing.test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    testing.test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    testing.test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)


    testing.test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
          ["now", "is", "time"])
    testing.test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
          ["I", "a", "is", "am"])
    #testing.test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
    #      ["a", "am", "are", "be", "but", "is", "or"])


    testing.test(longestword(["a", "apple", "pear", "grape"]) == 5)
    testing.test(longestword(["a", "am", "I", "be"]) == 2)
    testing.test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    testing.test(longestword([ ]) == 0)
    
test_suite()
