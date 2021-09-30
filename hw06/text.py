symbol = input("Please enter your symbol:")

height = int(input("Please enter the height:"))

width = int(input("Please enter the width:"))


def main(width, height):
    """
    Given a width and a height, using the user's chosen symbol to draw a rectangle
    """
    if height >= 2 and width >= 2:
        for i in range(0, height):
            for j in range(0, width):
                if i == 0 or i == height-1 or j == 0 or j == width - 1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")
            print("\n")
    else:
        print("Your value is too small.")


main(width, height)
