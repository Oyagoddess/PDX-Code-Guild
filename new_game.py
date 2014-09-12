__author__ = 'student'
# build your program by creating small statements and test and create the next function and build one small function at a time.
#everything above the 'while' statement and defined is in creating a global scope, things defined after the 'while' is considered local scope
#print is only what user sees
#return returns the input

#Guessing game with computer generated number.
    #for guessing game choose what you want the game to do:
    # want user to choose a number
    # want computer to generate a number
    # User has to have 7 tries
    # user to be able to play again.
# Steps
# import random (computer generated number) statement needs to be in the beginning of program.

import random

# create elements of the game by creating Def statements that will be used within the game (i consider shortcut statements)
#define each variable needed for different parts of the game.
#when creating def statments break the function down to the minimum of what you want that function to do.
# for expample in def user_name i just want the user to input name.
    # make a guess def statement and variable that will prompt user to provide input (name, number etc)
    #  return function will store the number they choose that you can call later in the program.
# create intro and welcome function asking user for name.
# return will return what they typed (name)
def user_name():
    name = raw_input("Welcome to choose a number game, what's your name?" )
    return name
#create make guess function asking user to choose a number.
#return will return the number they chose (prompt),
def make_guess():
    prompt = input('choose a number between 1-100')
    return prompt
#make_guess() is the (title)what you use when you want to call(use)the variable in the program.
# the next line is the definition prompt =(input)
# the return will store the users guess (prompt)

# make the function to activate computer generated number,
    # define it and create the variable so that the computer will generate the number within a specific range random.randint()
def secret_number():
    secret = random.randint(1, 100)
    return secret
#return stores the secret number, and secret_number is the call function for program

# create the functions that will check the users number to the computer generated number (number, secret)
    # create def statement along with conditions to check to see if the user number is right or wrong.
    # create a variable for answer so that when it runs and say if number is to high to low or  you win.
    # you can impliment certian conditions within def statments and when you call that in the play function it will run the sequence of statments.
    # the "if" statements all have to be inline in order for them to run within the function,
    #start "if statements that will check number to secret check_guess is the title
    # create conditions and  print ( what you want user to see if conditions are met i.e  'you win'.),
    # create a return if you want the user to see what they input.
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

#create play again function and conditions so user can replay if they want to. once they win or they run out of tries.
def play_again():
# again you only have to create function for what you want this to do. so you can call and run it in the play function
# create replay to ask usr by name if they would like to play agian
    replay = raw_input(str(name) + ', would you like to play again?')
# and create function for the replay answer
    if replay =='yes' or replay == 'y':
        #add the play function so that it will replay
        play()
    #add an else statement so if they add anything other then yes or y then it will print thank you for playing and exit.
    else:
        print('Thank you for playing!')
        exit()
# the first_play function created for when user wants to play again and will state the users name in the second play.
#(this was created after the first run of the gama and i wanted the persons name to be plugged in suring the second round without
#asking for their name.)
#defined first_play and added name to global  scope so whenever name is called it will use it.
def first_play():
    global name
    name = user_name()
    play()

#create a play function that will actually activate and play the game
# what do you want play to do. and what functions need to be identified and called. global name, secret, tries.
    # def play function by creating variables
    # and begin the while statement so that it will loop and play until user reaches 7 tries or they win.
    #( since i created a global name i removed the Name out of the play function it is activated in first_play.

def play():
    global name
    # create a function to call the users name and say hello.
    #name = user_name()
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
#create correct function the game will stop and print you win ( which is the global answer)
        if answer == 'correct':
            #create print statment of what you want the user to see. ex 26 is the correct answer.
            print (str(guess) + ' is ' + str(answer))
            # call play_again function so the user will be asked if they want to play agian.
            play_again()

# create incorrect functions if the user number and deduct each try from 7
        if answer == 'incorrect':
            tries -= 1

# if the user is incorrect will continue to play and stop at incorrect and state if to high or  to low, and subtract 1 from tries.
        #and will print the guessed number incorrect you have tries left.
            print (str(guess) + ' is ' + str(answer) + " you have " + str(tries) + " left")
# create incorrect and 0 tries function and will print sorry you lose.
        if answer == 'incorrect' and tries == 0:
            print ('sorry you lose')
# call play_agian function again to restart the game.

            play_again()

#activate first play function game, this function just repeats the game.
# it was added after the original play function was created. this just updates after it runs the first time.
first_play()

