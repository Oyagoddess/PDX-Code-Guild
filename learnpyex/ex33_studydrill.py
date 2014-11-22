# study drill
# 1. covert while loop to a function that you can call and replace 6 in the test(i < 6) with a variable.

# took a break of figuring this part out, i started with ex33_studyd#5 but realized i should have done w/o for loop
def change_while_loop():  # create name for function
    print range(6)  # creates a loop to list the i up to 6
    i = 0  # variable i
    print " here is the numbers for i %d" % i  # prints the list line by line
    numbers = []
    numbers.append(i)  # add i into the numbers list until you reach 5 (i in 6)

 # study drill #3
    x = 2  # study drill #3
    i = i + x  # i now = 0 + 2
    print "Numbers now: ", numbers  # print the list of numbers in the list so far
    print "At the bottom i is %d" % i  # print what the number is in this position

    print "The numbers: "

    for num in numbers:  # this calls nums (i) in numbers list this also prints each item of the list in newlines.
        print num  # this prints the numbers that have been added to the list
# studydrill #2
    for i in range(20,0,-2):
        print "this is counting backwards from 20 by 2: %d" % i

change_while_loop()  # calls to run the function    print "At the top i is %d" % i  # print whatever position or number i is as it loops