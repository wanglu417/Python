import sys

# get a value of height from the command line
height = int(sys.argv[1])


def main():
    # the given height of the diamond shoud be at least 3
    # if the value of height is an odd number
    if height % 2 != 0 and height >= 3:
        for i in range(1, int((height+1)/2)):
            print(" " * (int((height+1)/2) - i) + "*" * int(i*2-1)+"\n")
        for i in range(int((height+1)/2), int((height+1)/2)+1):
            print("*"*height+"\n")
        for i in range(int((height+1)/2+1), int(height+1)):
            print(" " * (i - int((height+1)/2)) +
                  "*" * int((height-i)*2+1)+"\n")
    # if the given height is an even number
    elif height % 2 == 0 and height > 3:
        for i in range(1, int(height/2)+1):
            print(" " * (int(height/2) - i) + "*"*int(i*2-1)+"\n")
        for i in range(int(height/2)+1, height+1):
            print(" " * (i - (int(height/2)+1)) +
                  "*" * int((height-i)*2+1)+"\n")
    # if the given height is 0,1,2,etc.
    else:
        print("Please enter a correct input")


main()
