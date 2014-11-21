from sys import argv

script, input_file = argv

def print_all(f):  # defines a function for reading the (f)file
    print f.read()  # prints the file

def rewind(f):  # creates a function to start at top of file
    print f.seek(0)  # seek moves to the start of the file (and only deals with bytes(spaces) not lines

def print_a_line(line_count, f): # defines function with 2 args
# print line_count and f. readline= reading a line and moving the read head to the right after the \n that ends the file.
    print line_count, f.readline()


current_file = open(input_file)  # opens the input file

print "First lets print the whole file:\n"

print_all(current_file)  # calls print_all to read the file and open the file

print "Now let's rewind, kind of like a tape."

rewind(current_file)  #calls function rewind and opens (input_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)  # prints current line which is one, and the line from file

current_line += 1  # variable with current line + 1 = 2, # changed to +=
print_a_line(current_line, current_file)  # prints current line 2 and line 2 from file

current_line = current_line + 1
print_a_line(current_line, current_file) #prints current line 3 and line 3 from file

