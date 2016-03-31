# Sums up all the integers between n and m

def sum_to(n):
    """ Sums up all the numbers from 1 to n, including n """
    running_sum = 0

    # needs to include n
    for i in range(n+1):
        running_sum += i

    return running_sum

def main():
    print(sum_to(10))

main()
