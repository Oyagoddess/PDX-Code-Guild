#  creates a functions with 2 arguments for adding a & b
def add (a, b):
    print "ADDING %d + %d" % (a, b)  # assigns a and b to string
    return a + b  # returns a + b

#  creates a functions with 2 arguments for subtracting a & b
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

#  creates a functions with 2 arguments for multiplying a & b
def mutliply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

#  creates a functions with 2 arguments for dividing a & b
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

# calls to run the functions and assign values to a and b
age = add(30, 5)
height = subtract(78, 4)
weight = mutliply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, subtract(height, mutliply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#studydrill simplify and break function down in order age plus height subract weight multiply iq and divide it by 2
puzzle_by_hand = age + height - weight * iq / 2
print puzzle_by_hand, "is the same number, when you simplify the function"

inverse = iq / 2 * weight - height + age
print "when you change the formula you get", inverse,

new_function = weight + height / iq * age
print " this is a random function that totals", new_function





