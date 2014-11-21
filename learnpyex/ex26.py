# read and correct code to run.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
#  this is ok
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
#  this is ok
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)  # change poop to pop
    print word

def print_last_word(words):  # add colon
    """Prints the last word after popping it off."""
    word = words.pop(-1)  # add closing parenthesis
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
#  this is ok

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# this is ok

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
#  this is ok

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#  this is ok

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#  had to change explantion to explanation

print "--------------"
print poem
print "--------------"
# this is ok

five = 10 - 2 + 3 - 6  # change 3-5 to 3-6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000  # change \ to /
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)  # change == to = and change start-point to start_point

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d apples." % secret_formula(start_point)   # change crabapples to apples,
# change start_pont to start-point and close the parenthesis

sentence = "All good\tthings come to those who wait."  # change god to god to good, and weight to wait

words = break_words(sentence)  # remove ex25
sorted_words = sort_words(words)  # remove ex25

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)  # remove . before print
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)  # remove ex25. before sort
print sorted_words  # correct prin to print

print_first_and_last(sentence)  # and f to irst

print_first_and_last_sorted(sentence)  # backtab, and change _a_ to _and_, and add t to sentence
