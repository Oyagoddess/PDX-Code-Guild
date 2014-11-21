from sys import argv  # import the modules for argument variables


script, user_name = argv  # argv is the argument variable and username is the args you will pass through

prompt = '-'  # prompt adds string to the user input adds a -.

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %(user_name)

# raw_inputs gathers user input and will be used in paragraph below
likes = raw_input(prompt)  # assigns input creating a variable

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# my update for study drill
print " what is your favorite sport?"
sport = raw_input(prompt)

# prints a paragraph with user inputs
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
Are you any good at %r?
""" % (likes, lives, computer, sport)

#  to run in terminal you go to directory file: example ...learnpython ex14.py with 1 values username (shalonda)

