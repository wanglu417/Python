"""
Get input from the user for the cube size
"""
n = int(input("Input cube size (multiple of 2): "))


def top_horizontal_edge():
    """
    Draws the top one line
    """
    print(' ' * (int((n/2))+1) + '+' + '-'*n*2 + '+')


top_horizontal_edge()


def vertical_edge():
    """
    Draws two vertical edges with '/'
    Draws vertical "|" in the same horizontal line
    """
    for i in range(1, int(n/2) + 1):
        print(" " * (int(n/2)-i+1) + "/" + " " * n*2 + "/" + ' '*(i-1) + '|')


vertical_edge()


def front_square():
    """
    Draws the second horizontal line
    """
    print('+' + '-'*n*2 + '+' + ' ' * int(n/2) + '|')
    """
    Draws the two vertical line with "|"
    """
    for i in range(1, n+1):
        if i < int(n/2):
            print('|'+' '*n*2 + '|' + ' ' * int(n/2)+'|')
        elif i == int(n/2):
            print('|'+' '*n*2 + '|'+' ' * int(n/2)+'+')
        else:
            print('|'+' '*n*2 + '|'+' ' * (n-i)+'/')
    """
    Prints the base line
    """
    print('+' + '-'*n*2 + '+')


front_square()


def main():
    top_horizontal_edge()
    vertical_edge()
    front_square()


main()
