import testing

def my_sum(to):
    """ Sums the numbers between 0 and param to """

    running_sum = 0

    for i in to:
        running_sum += i

    return running_sum

def collatz(n):
    """ Does the collatz sequence based on param to """

    while (n != 1):
        print(n, end=", ")

        if (n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=".\n\n")


def test_suite():
    testing.test(my_sum([1, 2, 3, 4]) == 10)
    testing.test(my_sum([1.25, 2.5, 1.75]) == 5.5)
    testing.test(my_sum([1, -2, 3]) == 2)
    testing.test(my_sum([ ]) == 0)
    testing.test(my_sum(range(11)) == 55)  # 11 is not included in the list.

    for i in range(1, 5):
        collatz(i)

test_suite()
