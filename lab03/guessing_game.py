import random
import math
print("Welcome to the Guessing Game!")
random_number = random.randint(1, 50)
user_guess = int(
    input("I picked a number between 1 and 50. Try and guess!"+'\n'))
tries = 1

while (random_number != user_guess):
    if abs(random_number - user_guess) <= 1:
        print("Your guess is scalding hot")
    elif abs(random_number - user_guess) <= 2:
        print("Your guess is extremely warm")
    elif abs(random_number - user_guess) <= 3:
        print("Your guess is very warm")
    elif abs(random_number - user_guess) <= 5:
        print("Your guess is warm")
    elif abs(random_number - user_guess) <= 8:
        print("Your guess is cold")
    elif abs(random_number - user_guess) <= 13:
        print("Your guess is very cold")
    elif abs(random_number - user_guess) <= 20:
        print("Your guess is extremely cold")
    elif abs(random_number - user_guess) > 20:
        print("Your guess is icy freezing miserably cold ")
    user_guess = int(
        input("I picked a number between 1 and 50. Try and guess!"+'\n'))
    tries += 1

print("Congratulations. You figured it out in", tries, "tries.")

if (tries == 1):
    print("That was lucky!")
else:
    if (tries != 1):
        if (tries >= 2 and tries <= 4):
            print("That was amazing!")
        elif (tries >= 5 and tries <= 6):
            print("That was okay.")
        elif(tries == 7):
            print("Meh.")
        elif(tries >= 8 and tries <= 9):
            print("This is not your game.")
        elif(tries >= 10):
            print("You are the worst guesser I've ever seen.")
