#  create variables
people = 30
cars = 40
buses = 15

# create if statement to create conditions to run the function, this runs top to bottom
if cars > people:  # if this is true print
    print "We should take the cars."  # end of the if block of code
elif cars < people:  # if this is true print this.
    print "We should not take the cars."
else:  # if neither above is true then do this and ends this block of code.
    print "We can't decide"

# this is another block of code
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
# another block of code with just else
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then"

#  studydrill
# 1. the elif gives another condition to follow & tells python that if this statement is true then do this
# the else statement give an alternative condition if the if and elif is not true
# 2.  if you change the values of the variables then the true statement will print.
# 3.
if cars == people:
    print " everybody can have there own car"
elif cars < people:
    print " divide the group and pic a car to ride in"
else:
    print "we may have to get a bus"
#  notes are above most lines.
