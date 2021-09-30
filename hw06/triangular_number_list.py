def triangular(x):
    """
    Defines triangular number
    """
    y = round((x**2+x)/2)
    return y


def main():
    """
    Gets input number from user
    """
    x = input("Enter a number, or enter 'done': ")
    """
    Creats a list
    """
    my_list = []
    if x != 'done':
        y = triangular(int(x))
        """
        Generates a list for triangular number of x
        """
        my_list.append(triangular(int(x)))
        print("The triangular number for", x, "is", y)
        x1 = input("Enter another number, or enter 'done': ")
        while x1 != 'done':
            y1 = triangular(int(x1))
            my_list.append(triangular(int(x1)))
            print("The triangular number for", x1, "is", y1)
            x1 = input("Enter another number, or enter 'done': ")
        else:
            print(my_list)
    else:
        """
        If user enters "done" in the first attempt
        """
        print("[None]")


main()
