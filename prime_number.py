# create functions to pick prime numbers 
# import math to use math functions id needed.

import math

n = int(input("pick a number"))
prime = []

# Started with creating method to print prime numbers.
def list_prime_number():  # Created def statement to call to print i
    for i in range(2, n):  # If in the range of input number and n, then go to next
        if i % 2 and i % 3 and i % 5:  # if n is i is divisible by 2,3,5 then print i
            print i
           # need to figure out how to print numbers below 5 numbers start at 7

# Create a function to check if input number is a prime
def check_number_is_prime():
    if n > 1:  # primes are greater than 1
        for i in range(2, n):
            if (n % i) == 0:  # if n is divisible by itself then print not a prime.
                print "number is not a prime"
            else:
                print "number is a prime"
                break

check_number_is_prime()
list_prime_number()