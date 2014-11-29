from sys import exit  # importing the exit feature from system

def gold_room():  # defines the function for the gold room
    print "This room is full of gold.  How much do you take?"  # ask for user input

    next = raw_input("> ")  # collects user inputs
    if "0" in next or "1" in next:  # creates conditions for user inputs to run if..
        how_much = int(next)  # collects a integer or number
    else:
        dead("Man, learn to type a number.")  # this prints if user does not put in 0 or 1 number

    if how_much < 50:  # creates condition for user inputs for how much if it is less than 50
        print "Nice, you're not greedy, you win!"
        exit(0)  # this exits the loop and stops
    else:  # if users how much is more than 50 it prints
        dead("You greedy bastard!")


def bear_room(): # defines a function for bear_room
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    # need more clarity on the relevance of the bear_moved expression
    bear_moved = False  # set bear_moved false creates boolean test

    while True:  # creates while loop for users input how they are moving the bear creates an infinite loop for this
                #until it reaches a false. or when they enter a correct option.
        next = raw_input("> ")  # collects user input

        if next == "take honey":  # creates condition to move bear
            dead("The bear looks at you then slaps your face off")  # prints and calls dead function (Good Job!)
        elif next == "taunt bear" and not bear_moved:  # creates condition if taunt bear and true (not false)
            print ("The bears has moved from the door.  You can go through it now")
            bear_moved = True  # reassigns bear_moved to True
        elif next == "taunt bear" and bear_moved:  # if you taunt bear and bear moved true then
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:  # if user opens door and bear moves then they start gold_room
            gold_room()
        else:  # if none of the user input applies then type
            print " I got no idea what that means"


def cthulhu_room():  # defines a new function for cthulhu to run when called
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane"
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:  # if user is flee then it goes to start function
        start()
    elif "head" in next:  # if user inputs is head it prints dead value and well that ...
        dead("Well that was tasty!")
    else:  # if user chooses neither then it calls cthulhu function to run again
        cthulhu_room()

# not sure of the relevance of this function
def dead(why):  # creates a function to be called
    print why, "Good Job!"  # it prints good job
    exit(0)  # and it exits.

def start():  # this is the start function to start and run the program
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")  # takes user input

    if next == "left":  # conditions for user input
        bear_room() # if they choose left it will loop to the bear_room function
    elif next == "right":  # if they choose right it loops to cthulhu_room function
        cthulhu_room()
    else: # if they choose neither and something else then it runs dead and ends.
        dead("You stumble around the room until you starve.")


start()  # this calls the whole game to run from start and runs through functions and loops

""" study drill
 1. map of the game
 start - begins the game and ask for options which door
  through room: bear room or cthulu room or gold rooms with what happens.
 2. fixed mistakes
 3. written comments two items i don't quite understand is the necessity for the dead function,
 and the bear_moved expression
 4.
 5. the bugs in typing a number with 0 or 1 in the gold room are that if you do numbers without it will keep saying
  it doesn't understand what that means. """