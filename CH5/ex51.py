def days_of_week(n):
    """ n as the day of the week, 0-6"""
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

    return weekdays[n]

def main():
    print(days_of_week(5))


main()
