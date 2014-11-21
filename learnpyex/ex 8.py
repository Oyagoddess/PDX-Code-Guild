#  medula or % create
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two's", "three", "four")
print formatter % (True, False, False, True) # prints booleans
print formatter % (formatter, formatter, formatter, formatter) # prints raw data
print formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight."
)