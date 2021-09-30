from random import choice
import string
import random
print("Welcome to the DMV (estimated wait time is 3 hours)")
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
print("Please enter your first, middle, and last name:" +
      '\n' + first_name, middle_name, last_name)
date_of_birth = input("Enter date of birth (MM/DD/YY):"+'\n')
print("--------------------------------------------------------")
print("Washington Driver License")

# Generate 7 random numbers between 0 and 10
chars = string.digits
num_str = ''.join(choice(chars) for _ in range(7))
print("DL", num_str)
print("LN", last_name)
print("FN", first_name, middle_name)
print("DOB", date_of_birth)
print("EXP", date_of_birth[0:5]+"/2021")
print("-------------------------------------------------------")
