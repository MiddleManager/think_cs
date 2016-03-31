import testing
import math

def cal_hypo(angles):
    """ calculates the hypotenuse given 2 angles in a tuple """

    hypo = (angles[0]**2) + (angles[1]**2)
    hypo = math.sqrt(hypo)

    return hypo

def test_suite():
    testing.test(cal_hypo((3, 4)) == 5)

test_suite()
