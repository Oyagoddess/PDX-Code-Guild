from sys import argv

# create a txt file ex15_sample.txt to include in command


script, filename = argv  # argv to get filename ex15.py

txt = open(filename)  # creates a variable to open ex15 txt file open command will opens the txt file.

print "Here's your file %r:" % filename  # will add file name to string
print txt.read()  # creates a read call function on txt (.command with parameter txt) and will print 15text file

print "Type the filename again:"  # prompts you to type the text file name
file_again = raw_input("> ")  # creates the prompt for user to type  ex15.py_ sample.txt filename again


txt_again = open(file_again)  # creates a variable to open the filenamecalls txt.again

# calls to print the filename again
print txt_again.read() # .reads prints the text file ex15.py_sample.txt

#  to run in terminal you go to directory file is in example ...learnpython ex15.py ex15.py_sample.txt