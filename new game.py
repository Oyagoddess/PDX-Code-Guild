__author__ = 'student'
# build your program by creating small statements and test and create the next function and build one small function at a time.
#everything above the 'while' statement and defined is in creating a global scope, things defined after the 'while' is considered local scope
#print is only wha user sees

#Guessing game with computer generated number.
    #for guessing game choose what you want the game to do.
    # want user to choose a number
    # want computer to generate a number
    # User has to have 7 tries
# import random (computer generated number) statement needs to be in the beginning of program.

import random
# create elements of the game by creating Def statements that will be used within the game (shortcut statements)
#define each variable needed for different parts of the game.
    # make a guess def statement and variable that will prompt user to choose a number,
    #  return function will store the number they choose that you can call later in the program.
def make_guess():
    prompt = input('please choose a number between 1-100')
    return prompt
#make_guess() is the (title)what you use when you want to call(use)the variable in the program.
# the next line is the definition prompt =(input)
# the return will store the users guess (prompt)

    # make the function to activate computer generated number,
# define it and create the variable so that the computer will generate the number within a certain range
def secret_number():
    secret = random.randint(1, 101)
    return secret
#return stores the secret number, and secret_number is the call function for program

# create the functions that will check the users number to the computer generated number (number, secret)
    # create def statement along with conditions to check to see if the user number is right or wrong.
    # create a variable for answer so that when it runs and say if number is to high to low or  you win.
    #start "if statements that will check number to secret
def check_guess(number, secret):
    if number == secret:
        print ('you win')
        answer = 'correct'
        return answer

    if number > secret:
        print ('number is to high')
        answer = 'incorrect'
        return answer

    if number < secret:
        print ('number is too low')
        answer = 'incorrect'
        return answer

#create a play function that will actually activate and play the game
# def play function by creating variables
# and begin the while statement so that it will loop and play until they reached 7 tries or they win.

def play():
    secret = secret_number()
    tries = 7

    while tries > 0:
        guess = make_guess()
        answer = check_guess(guess, secret)

        if answer == 'correct':
            break

        if answer == 'incorrect':
            tries -= 1

play()