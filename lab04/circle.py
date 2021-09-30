import sys
import math


def main():
    # get a radius value from the user
    radius = int(sys.argv[1])
    for i in range(1, radius * 2):
        for j in range(1, radius * 2):
            # print space if the distance of each character to
            # the center of the grid is more than the value of the radius
            if (math.sqrt((radius - j)**2 + (radius-i)**2) > radius):
                print(" ", end="")
            # print "o" if the distance is less than the value of the radius
            else:
                print("o", end="")
        print("\n", end="")


main()
