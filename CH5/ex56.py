# Returns the grades from a marking scheme

def return_grade(scheme, n):
    """ Marking scheme and the grade
    Returns a string with the appropiate grade"""

    for j in range(len(scheme)):
        #print(str(scheme[j][0]) + " " +  str(int(n)))

        if (scheme[j][0] <= n and scheme[j][1] > n):
            return scheme[j][2]

    return "Error: Grade not within 1 - 100"


def main():
    # Declarations
    grade_scheme = [
    [75, 100, "First"],
    [70, 75, "Upper Second"],
    [60, 70, "Second"],
    [50, 60, "Third"],
    [45, 50, "F1 Supp"],
    [40, 45, "F2"],
    [00, 40, "F3"]]

    grades = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
              49.9, 45, 44.9, 40, 39.9, 2, 0]

    # Processes the grades in accordance to the grade scheme
    for i in grades:
        print(str(i) + ": " + str(return_grade(grade_scheme, i)))

main()
