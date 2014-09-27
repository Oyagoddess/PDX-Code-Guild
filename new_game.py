__author__ = 'student'
# Guessing game with computer generated number.
# For guessing game choose what you want the game to do:
# Want user to choose a number
# Want computer to generate a number
# User has to have 7 tries
# User to be able to play again.
# Import random (computer generated number) statement needs to be in the beginning of program.

import random


# Create intro and welcome function asking user for name.
def user_name():
    name = raw_input("Welcome to choose a number game, what's your name?")
    return name


# Create make guess function asking user to choose a number.
def make_guess():
    prompt = input('choose a number between 1-100')
    return prompt


# Create function to activate computer generated number in range of 1-100.
def secret_number():
    secret = random.randint(1, 100)
    return secret


# Create the function that will check the users number to the computer generated number (number, secret)
def check_guess(number, secret):
    if number == secret:
        print ('you win')
        answer = 'correct'
        return answer
# Create functions if number is greater than secret.
    if number > secret:
        print ('number is to high')
        answer = 'incorrect'
        return answer
# Create function if number is less than the secret.
    if number < secret:
        print ('number is too low')
        answer = 'incorrect'
        return answer


# Create play again function and conditions so user can replay if they want to.
def play_again():
    replay = raw_input(str(name) + ', would you like to play again?')
    if replay == 'yes' or replay == 'y':
        play()
    #add an else statement so if they add anything other then yes or y.
    else:
        print('Thank you for playing!')
        exit()


# Create first play function so if user wants to play again it will state the users name in the second play.
# Defined first_play and added name to global  scope so whenever name is called it will use it.
def first_play():
    global name
    name = user_name()
    play()


# Create a play function that will actually activate and play the game.
def play():
    global name
    secret = secret_number()
    tries = 7
    print ('Hello ' + str(name) + ", the object of the game is to choose a number between 1 -100, you have 7 tries.")

# Create the while looping function to run and repeat game until it hits limits of win or tries.
    while tries > 0:
        guess = make_guess()
        answer = check_guess(guess, secret)
        if answer == 'correct':
            print (str(guess) + ' is ' + str(answer))
            play_again()
        if answer == 'incorrect':
            tries -= 1
            print (str(guess) + ' is ' + str(answer) + " you have " + str(tries) + " left")
        if answer == 'incorrect' and tries == 0:
            print ('sorry you lose, the number is' + (str(secret)))

# Call play_again function again to restart the game.
            play_again()
#  Call and activate first_play function game, to continue playing.
first_play()

