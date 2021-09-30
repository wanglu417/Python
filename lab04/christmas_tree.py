row = 0
while row % 2 == 0 or row < 3:
    # get tree height from user
    # if the input value is even or less than 3, continue to collect value
    row = int(input("Please enter an odd value equal or greater than 3: "))


def main(n):
    # print leading spaces
    for i in range(int((n-1)/2)):
        print(" ", end="")
    # pring "*" in the first line
    print("*\n")
    # print out left edge and right edge
    for i in range(1, int((n-1)/2)):
        print(" "*int(((n-1)/2-i))+"/"+" "*int((2*i-1))+"\\"+"\n")
    # print the base
    print(" "*int(((n-1)/2-(int((n-1)/2)+1)))+"/" +
          "_"*int((2*(int((n-1)/2))-1))+"\\"+"\n")


main(row)
