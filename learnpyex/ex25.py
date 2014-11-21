def break_words(stuff):  # defines and creates a function
    """This function will break up words for us."""
    words = stuff.split(' ')  # creates a variable to split the words
    return words  # returns the word that were split in words.

def sort_words(words):
    """sorts the words."""
    return sorted(words)  # creates function to sort words

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)  # prints only the first word in O postion
    print word

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)  # prints the last word in positions
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_and_last(words)
    print_last_word(words)