
def cheese_and_crackers(cheese_count, boxes_of_crackers):  # define function create arg parameters or values
    print "You have %d cheeses!" % cheese_count  # add the arg cheese_count (unpacking or using args)
    print "You have %d boxes of crackers!" % boxes_of_crackers  # add the arg boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"  # creates a new line


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)  # can replace the two args with numbers 20 replaces cheese_count and
# 30 replaces boxes_of_crackers

print "OR, we can use variables from our script:"
amount_of_cheese = 10  # can make new variables(seperate the variables from the script). cheese and crackers
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # can replace original function with new args.


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)  # can replace arguments with 2 math arguments


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  # can add both args and numbers



