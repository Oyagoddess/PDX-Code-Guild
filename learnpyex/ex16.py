from sys import argv  # import the modules for argument variables

script, filename = argv  # # argv is the argument variable and filename (test.txt) is the args you will pass through

print "We are going to erase %r." % filename  #adds name of script filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')  # creates a method to open and write inside the file

print "Truncating the file.  Goodbye!"
target.truncate()  # creates a command to delete the target file

print "Now I'm going to ask you for three lines."

# creates and assign user inputs for new script
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# studydrill 16 #3 shortening up the call line

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# writes newlines
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()  # closes and ends the program

#  to run in terminal you go to directory file is in example ...python ex16.py test.txt
# then to open the new file nano test.txt