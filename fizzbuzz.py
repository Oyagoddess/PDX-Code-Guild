# Create a fizz buzz loop 0-27
# Multiples of 3 say "fizz"
# If multiples of 4 say "buzz"
# Multiples of 3 and 4 say "fizzbuzz"

# Steps: Create variables
# Create an input so that usr can pick a number. input number is the stop limit.
a = 0
b = input('pick a number')
# Create conditions to count from 0 to user input number(b).
while a <= b:
    if a == 0:
        print(a)
        a += 1
    # Create 'elif' statements in order to continue with if number is divisible by 12 w/o remainders
    # to create say fizzbuzz for multiples of 3 and 4.
    elif a % 12 == 0:
        print("fizzbuzz")
        a += 1
    # Create say buzz for multiples of 4.
    elif a % 4 == 0:
        print ('buzz')
        a += 1
    # Create say fizz if multiples of 3.
    elif a % 3 == 0:
        print ('fizz')
        a += 1
    # Print (a) if the number is not multiples of 12,3,or 4.
    else:
        print (a)
        a += 1

