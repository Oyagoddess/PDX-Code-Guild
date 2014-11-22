print """
The object of the game is to find the room where the cheese is hidden.  It can be in
room 1, 2,3,4 or 5. Choose wisely, you may have some surprises along the way!
"""
print ("Where is your cheese? choose a room")

play = raw_input("*")

if play != "1":
    print "Watch out there is a big mouse in there that is still hungry"
    print " do you still think your cheese is in here, do you want to :"
    print "1. look around the room"
    print "2. look in another room"

    mouse = raw_input("*")

    if mouse == "1":
        print "that was a bad idea, the mouse just ate you"
    elif mouse == "2":
        print "that was a good idea"
    else:
       print "you must be lost or confused"
if play == "1":
    print " wow good job, you found your cheese."

if play == "2" or "4":
    print " Shut the door! There are a thousand mice in there.Your cheese is not in here "

if play == "3" or "5":
    print ""
