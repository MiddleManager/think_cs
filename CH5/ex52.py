def days_of_week(n, start):
    """ n as the day of the week, 0-6"""
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

    # Eliminates number out of index range
    index = (start + n) % (len(weekdays) - 1)

    print (str(start) + " + " + str(n) + " % " + str(len(weekdays)) + " - 1")

    print (index)
    return weekdays[index]

def main():
    print(days_of_week(137, 5))


main()
