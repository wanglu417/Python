import sys

# get a input number n from the command line
n = int(sys.argv[1])

# define the function fibo(n)


def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))


if n <= 0:
    print("Please enter a positive integer")
else:
    # generate a list using the fibonacci numbers
    my_list = []
    for i in range(n):
        my_list.append(fibo(i))
    print(my_list)
