import math


def find_hypo(ang1, ang2):
    hypo = (ang1*ang1) + (ang2*ang2)
    hypo = hypo ** 0.5

    return (hypo)

def is_rightangled(list):

    list = sorted(list)

    if (find_hypo(list[0], list[1]) == list[2]):
        return True
    else:
        return False

def main():
    print(find_hypo(3, 4))

    angles = [3.0, 5.0, 4.0]
    print(is_rightangled(angles))

main()
