import testing as t
import time

def search_linear(xs, target):
    """ Searches through a list linearly """
    for i, j in enumerate(xs):
        if j == target:
            return i
    return -1

def find_unknown_words(vocab, words):
    """ Return a list of words that don't occur in vocab """
    new_words = []

    for i in words:
        if (search_linear(vocab, i) == -1):
            new_words.append(i)

    return new_words

def load_words_from_file(path):
    f = open(path, "r")
    words = f.read()
    words = words.split()
    f.close()

    return words

def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase. """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def test_suite():
    print("Beginning tests\n-------------")
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    t.test(search_linear(friends, "Zoe") == 1)
    t.test(search_linear(friends, "Joe") == 0)
    t.test(search_linear(friends, "Paris") == 6)
    t.test(search_linear(friends, "Bill") == -1)

    vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
    book_words = "the apple fell from the tree to the grass".split()
    t.test(find_unknown_words(vocab, book_words) == ["from", "to"])
    t.test(find_unknown_words([], book_words) == book_words)
    t.test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])



    t.test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
    t.test(text_to_words('"Well, I never!", said Alice.') ==
                             ["well", "i", "never", "said", "alice"])

    bigger_vocab = load_words_from_file("vocab.txt")
    book_words = load_words_from_file("alice_in_wonderland.txt")

    t0 = time.clock()
    missing_words = find_unknown_words(bigger_vocab, book_words)
    t1 = time.clock()
    print("There are {0} unknown words".format(len(missing_words)))
    print("That took {0:.4f} seconds to calculator".format(t1-t0))
    


test_suite()
