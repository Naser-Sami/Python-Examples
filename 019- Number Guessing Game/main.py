
# Use the random module to help generate the random number
from random import randint

# randint() will generate a random integer between 1-100, assign it to 'rand_num'
rand_num = randint(1, 100)
# guess will store the guesses that the user makes
guess = 0


# continue the game until the user guesses correctly
while guess != rand_num:

    # prompt the user to enter a guess, the input() function will return the 
    # string the user enters, convert it to an int with int() and assign the 
    # guess to 'guess'
    guess = int(input("Guess an integer number: "))


    # if the user guesses too lower, tell them to guess higher, if they guess 
    # too high, tell them to guess lower, and if they get it correct tell 
    # them they've won
    if guess > rand_num:
        print("Guess lower!")
    elif guess < rand_num:
        print("Guess higher!")
    else:
        print("You guessed the number. You WON")
