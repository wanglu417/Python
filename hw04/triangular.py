import sys


def main():
    # takes an input from the command line
    n = int(sys.argv[1])
    # using the formula to calculate the sum
    for i in range(0, n+1):
        print(round(((i**2)+i)/2))


main()
