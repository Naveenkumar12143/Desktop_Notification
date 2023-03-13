
"""
Let’s say User has participated in a lucky draw competition. 
The user gets three chances to guess the number between 1 and 10. 
If guess is correct user wins, else loses the competition."""

import random
from random import randint

def rand_guess():
    """
    True :
          If win-condition is satisfied then,  the function rand_guess returns True
    False:
          If user's choice doesn't match,  win-condition then it is printed
    :return:  this function returns True or False
    """
    # calls generator() which returns a random integer between 1 and 10
    random_number = randint(1, 10)
    # defining the number of guesses the user gets
    guess_left = 3
    # Setting a flag variable to check the win-condition for user
    flag = 0
    # looping the number of times the user gets chances
    while guess_left > 0:
        # Taking input from the user
        guess = int(input("Pick your number to enter the lucky draw\n"))
        # checking whether user's guess matches the generated win-condition
        if guess == random_number:
            # setting flag as 1 if user guesses  correctly and then loop is broken
            flag = 1
            break
        else:
            # If user's choice doesn't match, win-condition then it is printed
            print("Wrong Guess!")
                 # Decrementing number of guesses left by 1
        guess_left -= 1  # guess_left = guess_left  - 1 ( assignment operator)
    # If win-condition is satisfied then, the function rand_guess returns True
    if flag == 1:
        return True
    # Else the function returns False
    else:
        return False


if __name__ == '__main__':
    if rand_guess():
        print("Congrats! You Win.")
    else:
        print("Sorry, You Lost!")

# Output :

# Pick your number to enter the lucky draw
# 4
# Wrong Guess!!
# Pick your number to enter the lucky draw
# 9
# Congrats!! You Win.
