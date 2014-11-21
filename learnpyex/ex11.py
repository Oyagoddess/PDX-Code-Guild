print "How old are you?",  # the comma ends a line. and lets you put input on same line
age = raw_input()  # raw input creates a prompt to gather users input.
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#  %r is raw data
print "So you're %r, old %r tall, and %r heavy." %(age, height,weight)