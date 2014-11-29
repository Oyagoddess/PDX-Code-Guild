# import the modules for argument variables
from sys import argv

# create the arguments to run the command line args thru.
script, first, second, third, fourth = argv

print " the script is called;", script
print "My eldest child's name is:", first
print "My middle childs name is:", second
print "My angel baby is:", third
print "i finally named my last child:", fourth

print "How many children do you have?"
children = raw_input()  # will take user input
print "what is the first child's name"
child1 = raw_input()

print "You have %r child/ren and the first child's name is %s and my first child's name is %r" %( children, child1, first)



#  to run in terminal you go to directory file is in example ...python ex13_studydrill.py with 4 values matching
# number of args in original script which in this case would be Dalontae Geontae Angelic and Gary