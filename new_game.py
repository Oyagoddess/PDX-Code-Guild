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

import random #package
# create elements of the game by creating Def statements that will be used within the game (shortcut statements)
#define each variable needed for different parts of the game.
    # make a guess def statement and variable that will prompt user to choose a number,
    #  return function will store the number they choose that you can call later in the program.
# create intro and welcome function
def user_name():
    name = raw_input("Welcome to choose a number game, what's your name?" )
    return name


def make_guess():
    prompt = input('choose a number between 1-100')
    return prompt
#make_guess() is the (title)what you use when you want to call(use)the variable in the program.
# the next line is the definition prompt =(input)
# the return will store the users guess (prompt)

    # make the function to activate computer generated number,
# define it and create the variable so that the computer will generate the number within a certain range random.randint()
def secret_number():
    secret = random.randint(1, 100)
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
# create functions if number is greater than secret and print number is to high
    if number > secret:
        print ('number is to high')
        answer = 'incorrect'
        return answer
#create function if number is less than the secret number and
    if number < secret:
        print ('number is too low')
        answer = 'incorrect'
        return answer

#create a play function that will actually activate and play the game
# def play function by creating variables
# and begin the while statement so that it will loop and play until user reaches 7 tries or they win.

def play():
    # create a function to call the users name and say hello.
    name = user_name()
    secret = secret_number()
    tries = 7 #defines tries as 7
    # create statement to say hello to user after they have input their name and tell them the rules of the game.
    print ('Hello ' + str(name) + ", the object of the game is to choose a number between 1 -100, you have 7 tries.")

#create the while looping function to run and repeat game until it hits limits of win or tries.
    while tries > 0:
 # 7>0 so will continue to play
        guess = make_guess()
# recreate  guess as a local variables answer = check_guess and call from the global.
        answer = check_guess(guess, secret)
# recreate variable that will check answers using global variable
#create more functions for correct, incorrect, and subtract tries.
#create correct function the game will stop and print you win ( which is the global Answer)
        if answer == 'correct':
            print (str(guess) + ' is ' + str(answer))
            break
# create incorrect functions if the user number and deduct tries
        if answer == 'incorrect':
            tries -= 1
# if the user is incorrect will continue to play and stop at incorrect and state if to high or  to low, and subtract 1 from tries.
        #and will print the guessed number incorrect you have tries left.
            print (str(guess) + ' is ' + str(answer) + " you have " + str(tries) + " left")
# create incorrect and 0 tries function and will print sorry you lose.
        if answer == 'incorrect' and tries == 0:
            print ('sorry you lose')

#activate play function game.
play()