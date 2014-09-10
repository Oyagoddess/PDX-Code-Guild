# instr. loop to 20
# 20 to 0 counting backwards
# at 10 remove 10 and replace with "halfway there"
#skip 14, 9, 4
# at the end say "all done"
#Do one function at a time.( in looping statement of code is not contigent of the last unless you use elif or else. original variables are constant.)



#create variables.
a = 0
b = 20

#create conditions to count from 20 to 0
# replace ten with  "halfway done"

while b > a:
    print (b)
    b = b - 1

   # if b == 10:
# i did this first but because i use b=10 to remove 9, we had to remove it. and add it in as Print
#because your removing 10 you have to delete it by subtracting 1  
       # b = b - 1
       # print ("halfway done") 
       # this worked

# skip 14 
# in order to skip a number choose number above it and subtract by 2
    if b == 15:
  	print (b)
	b = b - 2

# skip 9
# # in order to skip a number choose number above it and subtract by 2
    if b == 10:
# to add and replace print what you want it to say in ()    

       print ("halfway there")
       b = b - 2

# skip 4
# # in order to skip a number choose number above it and subtract by 2
    if b == 5:
      print (b)
      b = b - 2
# to add and replace print what you want it to say in ()
    if b == 0:
       print ('all done')

#Now need the program to run

      






