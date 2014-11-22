
Studydrill #5
i = 0  # create variable for i
x = 2
numbers = []
def change_while_loop():  # create name for function
    print range(6)  # creates a loop to list the i up to 6
    print " here is the numbers for i %d" % i  # prints the list line by line
change_while_loop()  # calls to run the function

def change_while_loop():  # create name for function
    for i in range(6):  # creates a loop to list the i up to 6
        print " here is the numbers for i %d" % i  # prints the list line by line
        numbers.append(i)  # add i into the numbers list until you reach 5 (i in 6)

        # i = i + 1 this adds one to i as it loops through to 5(6)
        # study drill #3
        i = i + x  # i now = 0 + 2
        print "Numbers now: ", numbers  # print the list of numbers in the list so far
        print "At the bottom i is %d" % i  # print what the number is in this position

        print "The numbers: "

    for num in numbers:  # this calls nums (i) in numbers list this also prints each item of the list in newlines.
        print num  # this prints the numbers that have been added to the list

    for i in range(20,0,-2):
        print "this is counting backwards from 20 by 2: %d" % i

change_while_loop()  # calls to run the function    print "At the top i is %d" % i  # print whatever position or number i is as it loops