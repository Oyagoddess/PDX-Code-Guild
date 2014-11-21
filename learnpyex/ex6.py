# x is a string statement with 10 as the value for % variable with a complex string
x = "There are %d types of people." % 10
#binary is string value for binary
binary = "binary"
#don't is the string value for do_not
do_not = "don't"
# y is the string statement with two values replacing the % with string values.
y = "Those who know %s and those who %s." % (binary, do_not)
#print x and y statements
print x
print y
# %r gives the raw data of x (as is)
print "I said: %r." % x
# this is a print statement with a string inside a string
print "I also said: '%s'." % y

hilarious = False
#this is another string inside a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#this adds the two strings together
print w + e