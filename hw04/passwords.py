# Lu Wang
# The functions below uses inputs from the user and creates a username and 3 passwords

import random
import string

print("Welcome to the username and password generator!")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
fav_word = input("Please enter your favorite word: ")

# create a username


def get_username():
    if len(last_name) < 7:
        last_name_updated = last_name + "*" * (7-len(last_name))
    else:
        last_name_updated = last_name[0, 7]

    str_username = ''
    seq_username = [first_name[0].lower(), last_name_updated.lower(),
                    str(random.randint(0, 99))]
    username = str_username.join(seq_username)
    print("Thanks", first_name, ",", "your user name is", username)


get_username()

print("Here are three suggested passwords for you to consider:")

# create the first password


def get_password1():
    random_number = random.randint(0, 99)
    password1 = f"{first_name.lower()}{random_number}{last_name.lower()}"
    password2 = password1.replace('a', '@')
    password3 = password2.replace('o', '0')
    password4 = password3.replace('i', '1')
    password5 = password4.replace('s', '$')
    print("Password 1:", password5)


get_password1()

# create the second password


def get_password2():
    password2 = str(first_name[0].lower())+str(first_name[-1].upper())+str(last_name[0].lower()) + \
        str(last_name[-1].upper()) + \
        str(fav_word[0].lower())+str(fav_word[-1].upper())
    print("Password 2:", password2)


get_password2()

# create the third password


def get_password3():
    # create a list using first_name, last_name, fav_word
    # there are 6 possible ways to sort the three elements in a list
    my_list = [first_name, last_name, fav_word]
    random.shuffle(my_list)

    random_length_fn = random.randint(1, len(first_name))
    random_length_ln = random.randint(1, len(last_name))
    random_length_fw = random.randint(1, len(fav_word))
    if my_list == [first_name, last_name, fav_word]:
        password3 = first_name[:random_length_fn] + \
            last_name[:random_length_ln] + fav_word[:random_length_fw]
    elif my_list == [first_name, fav_word, last_name]:
        password3 = first_name[:random_length_fn] + \
            fav_word[:random_length_fw] + last_name[:random_length_ln]
    elif my_list == [last_name, first_name, fav_word]:
        password3 = last_name[:random_length_ln] + \
            first_name[:random_length_fn] + fav_word[:random_length_fw]
    elif my_list == [last_name, fav_word, first_name]:
        password3 = last_name[:random_length_ln] + \
            fav_word[:random_length_fw] + first_name[:random_length_fn]
    elif my_list == [fav_word, first_name, last_name]:
        password3 = fav_word[:random_length_fw] + \
            first_name[:random_length_fn] + last_name[:random_length_ln]
    elif my_list == [fav_word, last_name, first_name]:
        password3 = fav_word[:random_length_fw] + \
            last_name[:random_length_ln] + first_name[:random_length_fn]
    print("Password 3:", password3)


get_password3()
