i = 0  # variable i
numbers = []  # creates an empty

while i < 6:  # as long as i is less than 6 is true print and run this
    print "At the top i is %d" % i  # print whatever position or number i is as it loops
    numbers.append(i)  # add i into the numbers list until you reach 5 (i in 6)
    # and add 1 to i in 6 each time until you reach (i in 6) 5, translates to i = 0+1,i = 1 + 1 = 2 and so on.
    i = i + 1
    print "Numbers now: ", numbers  # print the list of numbers in the list so far

    print "At the bottom i is %d" % i  # print what the number is in this position

print "The numbers: "

for num in numbers:  # this calls nums (i) in numbers list this also prints each item of the list in newlines.
    print num  # this prints the numbers that have been added to the list
    #print num,  # this prints the numbers on one single line

