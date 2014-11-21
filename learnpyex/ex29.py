#create variables
people = 20
cats = 30
dogs = 15

#  if statements creates a condition to run the rest of the code.
if people < cats:   # if people which is 20 is less than cats which is 30 then print
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry."

dogs += 5  #  is short hand for dogs = dogs + 5 this variable adds 5 to dogs 15 + 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# studydrill 4
if cats != dogs:
    print "wow"

# study drill
"""
 1. the if statement creates a boolean condition to evaluate to run code. if it is true it will run the next line
 if not it will go to the next line that is true and print result.
 2. after the colon tells what is in the block of specific code.
 3. if you dont indent you may get an error
 4 yes you can put other boolean expression in if statements
 5. if you change the variables then the results of the condition may change.
 """