# Loop to 20: 20 to 0 counting backwards
# At 10 remove 10 and replace with "halfway there"
# Skip 14, 9, 4
# At the end say "all done"
# Do one function at a time.(looping statement of a code is not contingent of the last unless you use elif or else).

# Create variables.
a = 0
b = 20
# Create conditions to count from 20 to 0
while b > a:
    print (b)
    b -= 1
    # Create conditions to skip 14
    # In order to skip a number choose number above it and subtract by 2
    if b == 15:
        print (b)
        b -= 2
    # Create condition to skip 9
    # Replace ten with "halfway there".
    if b == 10:
        print ("halfway there")
        b -= 2
    # Create condition to skip 4
    if b == 5:
        print (b)
        b -= 2
    # Print all done at 0
    if b == 0:
        print ('all done')



      






