import sys
MINIMUM_WIDTH = 3
MINIMUM_HEIGHT = 1
LENGTH1 = 3
LENGTH2 = 4


def my_function(width, height, optional_arg='None'):
    """
    Defines my function with an optional arguement
    """
    if width >= MINIMUM_WIDTH and height >= MINIMUM_HEIGHT:
        """
        If the width >= 3 and height>=1 (looks like a ROCKET)
        """
        nose_cone(width)
        fuselage(width, height, optional_arg)
        tail(width)
    else:
        """
        If the user input for width<3 or height<1
        """
        print("Please enter a correct input")


def nose_cone(width):
    if width % 2 != 0 and width >= MINIMUM_WIDTH:
        """
        If the user input for the width is an odd number >=3
        Prints the nose cone
        """
        for i in range(1, int((width+1)/2)):
            print(" " * ((int((width-1)/2)) - i+1) + "*" * (2*i - 1))
    else:
        """
        If the user input for the width is an even number
        """
        for i in range(1, int(width/2)):
            print(" " * (int(width/2)-i) + "*" * i*2)


def fuselage(width, height, optional_arg):
    """
    If user does not enter the optional argument 'striped'
    Prints the fuselage made up of 'x'
    """
    if optional_arg == 'None':
        for i in range(1, width*height+1):
            print("X" * width)
    """
    If user inputs 'striped'
    Prints the fuselage made up of 'X' and '-'
    """
    if optional_arg == 'striped':
        """
        If value of width is an odd number:
        """
        if width % 2 != 0 and width >= MINIMUM_HEIGHT:
            for i in range(1, height+1):
                for j in range(1, int((width+1)/2)):
                    print("-" * width)
                for k in range(int(width/2), width):
                    print("X"*width)
        """
        If value of width is an even number:
        """
        if width % 2 == 0 and width > MINIMUM_WIDTH:
            for i in range(1, height+1):
                for j in range(0, int(width/2)):
                    print("-"*width)
                for k in range(int(width/2)+1, width+1):
                    print("X"*width)


def tail(width):
    """
    The number of '*' in the first row of tail == width//2
    """
    star_number = width//2
    if width % 2 != 0:
        if star_number % 2 == 0:
            star_number -= 1
    else:
        if star_number % 2 != 0:
            star_number -= 1
    while star_number < width:
        print(" " * int((width-star_number)/2) + "*" * star_number)
        star_number += 2
    for i in range(0, 2):
        """
        Prints the last two rows made up of '*'
        """
        print("*" * width)


def main():
    """
    Wrap all functions in main
    """
    if len(sys.argv) == LENGTH1:
        """
        Sets a conditional to check the length of sys.argv array
        """
        my_function(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == LENGTH2:
        my_function(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
    else:
        print("Please enter correct inputs")


main()
