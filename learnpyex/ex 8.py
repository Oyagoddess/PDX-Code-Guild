#  medula or % create
formatter = "%r %r %r %r" #  %r prints the raw input helpful for debugginf

print formatter % (1, 2, 3, 4) # replaces formator to a string of numbers
print formatter % ("one", "two's", "three", "four")  # replaces with string
print formatter % (True, False, False, True) # prints booleans without commas,
print formatter % (formatter, formatter, formatter, formatter) # prints raw data four times
# this print all of this verbatim in one line
print formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight."
)