# get three numbers of three digits from the user
print("Enter a magic number")
input1 = input()
input2 = input()
input3 = input()

# the square is 3*3
COLUMNS = 3


def is_magic_square():
    # using user's input to create a list
    my_list = [input1, input2, input3]
    # check the sum of digits of horizontal rows
    for i in my_list:
        sum = 0
        for j in range(COLUMNS):
            sum += int(i[j])
        if sum != 15:
            print("This is not a magic square!")
            return
    # check the sum of digits of vertical columns
    for j in range(COLUMNS):
        sum = 0
        for i in my_list:
            sum += int(i[j])
        if sum != 15:
            print("This is not a magic square!")
            return
    # check the sum of digits of two corner-to-corner
    if (int(my_list[0][0]) + int(my_list[1][1]) + int(my_list[2][2])) != 15:
        print("This is not a magic square!")
        return
    if (int(my_list[0][2]) + int(my_list[1][1]) + int(my_list[2][0])) != 15:
        print("This is not a magic square!")
        return
    # if all sums are equal to 15
    else:
        print("This is a magic square!")


is_magic_square()
