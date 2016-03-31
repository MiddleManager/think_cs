# Just the collection of all the different functions in one

# 1
def odd_in_list(list):
    count = 0

    for i in list:
        if (i % 2 == 1):
            count += 1

    return count

# 2
def even_in_list(list):
    return len(list) - odd_in_list(list)

# 3
def neg_in_list(list):
    count = 0

    for i in list:
        if (i < 0):
            count += 1

    return count

# 4
def word_len_in_list(list, n):
    count = 0

    for i in list:
        if (len(i) == n):
            count += 1

    return count

# 5
def sp_even_in_list(list):
    count = 0
    first = True

    for i in list:
        if (count % 2 == 0):
            if first:
                first = False
            else:
                count += 1

    return count

# 6
def sp_count_names(list, str):
    count = 0
    first = True

    for i in list:
        if (first == False):
            break

        count += 1

        if (i == str):
            first = False

    return count

# 7
def newtons_sqrt(num):
    pass

#9
def print_triangular_nums(inp):
    inp += 1

    for i in range(1, inp):
        tri_num = (i * (i + 1)) / 2
        print (str(i) + "\t" + str(tri_num))

#10 - Not finished
def is_prime(n):

    if (n == 1 or n == 2):
        return False

    for i in range(n):
        for j in range(n):
            if (j * n == n):
                return True

    return False

# 16
def sum_of_squares(list):
    running_sum = 0

    for i in list:
        running_sum += i*i

    return running_sum


def main():
    # declarations
    one_to_five = [1, 2, 3, 4, 5]
    names = ["Johnny", "Susanne", "Betty", "Chad", "Benjamin"]

    print(odd_in_list(one_to_five)) #1
    print(even_in_list(one_to_five)) #2
    print(neg_in_list(one_to_five)) #3
    print(word_len_in_list(names, 5)) #4
    print(sp_even_in_list(one_to_five)) #5
    print(sp_count_names(names, "Chad")) #6
    #7
    print_triangular_nums(5) #9
    print(is_prime(5)) #10
    print(sum_of_squares([2, -3, 4]))

    







main()
