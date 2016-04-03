import testing as t

def r_sum(nested_sum_list):
    """ Recursively sums lists in lists. Only support numbers
    and no strings et al."""

    tot = 0
    for element in nested_sum_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

def r_max(nxs):
    """ Finds the maximum number within layered lists
    Precaution: no empty lists """

    largest = None
    first_time = True

    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

def test_suite():
    print("Beginning Tests:\n---")
    t.test(r_sum([1, 2, [11, 13], 8]) == 35)

    t.test(r_max([2, 9, [1, 13], 8, 6]) == 13)
    t.test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    t.test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    t.test(r_max(["joe", ["sam", "ben"]]) == "sam")

test_suite()
