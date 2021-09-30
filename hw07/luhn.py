import sys


def get_number(n):
    """
    generate a list of integers using the input number
    """
    digit_list = [int(i) for i in str(n)]
    return digit_list


def double_digits(n, digit_list):
    """
    double digits from the second to right-most digit
    """
    even_digit = digit_list[-2::-2]
    odd_digit = digit_list[-1::-2]
    for i in even_digit:
        digits_doubled = [i*2 for i in even_digit]
        for x, i in enumerate(digits_doubled):
            if i >= 10:
                digits_doubled[x] = (i % 10) + (i // 10)
    list_to_sum = odd_digit + digits_doubled
    return list_to_sum


def check_luhn(list_to_sum):
    """
    check the sum of digits
    """
    sum_digits = sum(list_to_sum)
    if sum_digits % 10 == 0:
        print("This account number is valid.")
    else:
        print("This account number is not valid.")


def main():
    """
    If the user inputs a number fewer than 3 digits
    """
    if len(sys.argv[1]) < 3:
        print("Please enter a correct input")
    else:
        get_number(sys.argv[1])
        double_digits(sys.argv[1], get_number(sys.argv[1]))
        check_luhn(double_digits(sys.argv[1], get_number(sys.argv[1])))


main()
