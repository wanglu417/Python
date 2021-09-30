def main():
    """
    Gets two numbers from the user
    """
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    sum_of_two = add_nums(x, y)
    carry_nums = carry_count(x, y)
    print(x, "+", y, "=", sum_of_two)
    print("Number of carries:", carry_nums)


def add_nums(x, y):
    """
    Calculates the sum
    """
    return int(x) + int(y)


def carry_count(x, y):
    length_x = len(x)
    length_y = len(y)
    """
    Generates two lists for string x and string y
    """
    xlist = [int(i) for i in x]
    ylist = [int(j) for j in y]
    carry = 0
    """
    Sets flag = 0
    """
    flag = 0
    if length_x > length_y:
        zlist = xlist
    else:
        zlist = ylist
    """
    If the indexed digits additions exceeds 9
    """
    for i in range(min([length_x, length_y])):
        if flag == 0:
            if xlist[-1-i] + ylist[-1-i] > 9:
                flag = 1
                carry += 1
            else:
                flag = 0
        else:
            if xlist[-1-i] + ylist[-1-i] > 8:
                flag = 1
                carry += 1
            else:
                flag = 0

    for i in range(min([length_x, length_y]), max([length_x, length_y])):
        if flag == 1:
            if zlist[-1-i] > 8:
                flag = 1
                carry += 1
            else:
                flag = 0
    return carry


main()
