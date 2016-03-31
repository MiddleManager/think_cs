import testing

def add_vectors(v1, v2):
    """ Adds two vectors and returns a new vector"""

    if len(v1) != len(v2):
        return

    v3 = []

    for i in range(len(v1)):
        v3.append(v1[i] + v2[i])

    return v3

def scalar_mult(mul, v):
    """ Multiplies a vector by a multiple. Returns a new vector """

    v3 = []

    for i in range(len(v)):
        v3.append(v[i] * mul)

    return v3

def dot_product(v1, v2):

    if len(v1) != len(v2):
        return

    running_sum = 0

    for i in range(len(v1)):
        running_sum += v1[i] * v2[i]

    return running_sum

    return v3






def test_suite():
    print("Beginning tests\n------------")
    testing.test(add_vectors([1, 1], [1, 1]) == [2, 2])
    testing.test(add_vectors([1, 2], [1, 4]) == [2, 6])
    testing.test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

    testing.test(scalar_mult(5, [1, 2]) == [5, 10])
    testing.test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    testing.test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

    testing.test(dot_product([1, 1], [1, 1]) ==  2)
    testing.test(dot_product([1, 2], [1, 4]) ==  9)
    testing.test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

    testing.test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    testing.test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")
    testing.test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()
