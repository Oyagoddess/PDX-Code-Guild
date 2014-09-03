#create a fizz buzz loop. 
#0-27
# if multiples of 3 say "fizz"
#if mulitples of 4 say "buzz"
#multiples of 3 and 4 say "fizzbuzz"

#1. create variables
# crate an input so that usr can pick a number. the numbers will count 
#-upto the number they chose. 
# b is the stop limit. 

a = 0
b = input('pick a number')

#create conditions to count from 0 to user input number(b).

while a <= b:
    if a == 0: 
        print (a)
	a+=1
   
   # a+=1 is the same as a = a + 1
   # use elif in order to continue with else/if- if numbe is divisible by 12 w/o remainders then print fizzbuzz, and it adds 1 to whatever is was
   # continues to the next number and continues thru, until it prints (a) 
   

# create say fizzbuzz for multiples of 3 and 4 (12) 
# use an elif statement so that it will continue through if false. 

    elif a % 12 == 0: 
        print("fizzbuzz")
        a += 1   

#create say buzz for multiples of 4.
# use elif to continue through the program
   
    elif a % 4 == 0:
        print ('buzz')
        a +=1

#create say fizz if multiple of 3. 
# use elif to continue and cycle through program. 
    
    elif a% 3== 0:
        print ('fizz')
        a+=1

# print (a) if the number is not multiples of 12,3,or 4.  
    else: 
        print (a)
        a+=1

