print """
The object of the game is to find the room where the cheese is hidden.  It can be in
room 1, 2,3,4 or 5. Choose wisely, you may have some surprises along the way!
"""
print raw_input("Where is your cheese? choose a room")
play = raw_input("*")

if play != "1":
    print "Watch out there is a big mouse in there that is still hungry"
    print " do you still think the cheese is in here, do you want to :"
    print "1. look around the room"
    print "2. look in another room"
