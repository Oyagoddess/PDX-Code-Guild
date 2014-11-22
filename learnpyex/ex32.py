the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count: # this means print (loop)each item in count list till the end (breakdown the list)
    print "This is count %d" % number  # we use %d because it is a number

# same as above
for fruit in fruits:  # this print (loop) each item in fruits list to the end
    print "A fruit of type: %s" % fruit  # print %s becuase the list are strings

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:  # i is annonymous loop through each item in change
    print "I got %r" % i  #  we print %r becuase there are both numbers and strings. we want to print exactly what it is

# we can also build lists, first start with an empty one
elements = []  #

# then use the range function to do 0 to 5 counts
for i in range(0, 6):  # this says print(loop) through range 0 and add 1 until you get to 5
    print "Adding %d to the list" % i
    # append is a function that lists understand
    elements.append(i)  # this prints the range 0,6 into elements list
# now we can print them out too
for i in elements:  # print anonymous list in elements
    print "Elements was: %d" % i

# study drill
#1.  range has two parameters and are numbers(integers) range()= creates a list that starts at 0 and run this many times
print range(20)
#range(1,20)=  will create a list-start at 1 and count to 20, but will stop 1 less than 19.
print range(1,20)
#range(0,20,2) will start at on count up to 20 step 2 will return 2,4,6,...18)"""
print range(0,20,2)
# range rules range= start, stop, step (step is the difference between each integer)
#2. you could have avoided line 22 by just doing this. Assigning range to elements.
elements = range(0, 6)
for i in elements:
    print "elements was: %d" % i

# 3.  you can append, pop, sort, extend, insert, sort, count, index and reverse lists.
