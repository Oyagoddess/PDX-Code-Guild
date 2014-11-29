tabby_cat = "\t I'm tabbed in."  # variable with  a tabbed line.
persian_cat = "I'm split\non a line."  # \n splits the sentence.
backslash_cat = "I'm \\ a \\ cat."  # \\ creates a backslash

# """ creates multiple lines of code within the quotes
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# my practice code
# single quotes also creates multiple lines as typed,
my_interest = '''
I like to read: \n\t metaphisics
\t horoscopes
\t spiritual books'''
# the %s is a string typing what is in between qoutes and %r is "raw representation" and verbatim info
favorite_animals = "%s"
love = "%r"


print favorite_animals % "my favorite animals are \neagle\nphoenix\nsparrow"
print my_interest
print love % ("I love family, laughing, and living")


