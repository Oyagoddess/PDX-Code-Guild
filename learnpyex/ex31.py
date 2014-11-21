print " You enter a dark room with three doors.  Do you go through door #1, door #2 or will you try door 3?"
# create a variable with raw input to start if statement
door = raw_input("> ")

#  create conditions using users input chooses door 1. This is a block of code with nested conditions $ more users input
if door == "1":
    print "There is a giant bear here eating a cheese cake.  What do you do?"
    print "1. take the cake."
    print "2. Scream at the bear."

    # create a variable assigning bear to users choice dealing with the bear
    bear = raw_input("> ")

    #  create conditions for choices in option one with the bear
    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":  # do this if they choose door 2
        print "The bear eats your legs off. Good Job!"
    else:  # if they choose something else then it will print this
        print " Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":  # this is condition if user chooses door 2.
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow Jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    # this is the variable for users choice after choosing door 2
    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":  # if they choose 1 or 2 then it will print this
        print "Your body survives powered by the mind of jello.  Good Job!"
    else: # if they pick 3 or anything else then it will print this
        print "The insanity rots your eyes into a pool of muck.  Good Job!"

#  study drill additions
# create conditions for choosing door 3
elif door == "3":
    print "There is a giant Snake eating ice cream. What do you do?"
    print "1. Join the snake"
    print "2. Run from the snake"
    print "3. Pet the snake"

    snake = raw_input("> ")

    if snake == "1":
        print " the snake is happy.  Good Job"
    elif snake == "2":
        print " You better run fast the snake is mad"
    elif snake == "3.":
        print "The snake just bit your hand off, he does not like being touched."

# if the user does not choose door 1 or door 2 then they print this
else:
    print " You stumble around and fall on a knife and die,  Good Job!"

