# this one is like your scripts with argv

def print_two(*args):  # define the function create a name of what it does, and give it argument parameters (*args)=list
    arg1, arg2 = args  # indent the second line four spaces and unpacks the args
    print "arg1: %r arg2: %r" % (arg1, arg2)  # print how it works

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  # defines print_two_again with 2 args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):  # defines and prints one arg
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():  #print with no arg
    print "I got nothin'."

# prints with assign args in def statement (function)
print_two("Zed", "Shaw")  # replaces original args
print_two_again("Zed", "Shaw")
print_one("First")
print_none()