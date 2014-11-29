ten_things = "Apples Oranges Crows Telephone Light Sugar"  # creates variable with string list

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')  # creates variable for stuff to take in new items,
                            #  changing the string into a list adding new items to list
more_stuff = ['Day', "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]  # variable of more stuff with list

while len(stuff) != 10:  # tells python while the length of stuff is not ten then loop through and do this until it is 10
    next_one = more_stuff.pop()  # creates variable with more_stuff.pops= returns or remove last object in more stuff
    print "Adding: ", next_one  # prints adding with what next_one would be to the list first one would be boy
    stuff.append(next_one)  # add the next_one object into that was popped into next_one
    print "There's %d items now." % len(stuff)  # this will return the length of new list

print "There we go: ", stuff  # this prints the new list

print "Let's do some things with stuff."

print stuff[1]  # this prints list item at 1
print stuff[-1]  # whoa! fancy  this prints item at -1 or the last item in the list
print stuff.pop()  # prints the last item in the list
print ' '.join(stuff)  # what? cool!  # changes list into a line or string
print '#'.join(stuff[3:5]) # super stellar  this joins the list items at 3 and at 5