from sys import argv
from os.path import exists

# in order to create the test file you want to $ echo "This is a test file." > test.txt  next line $cat test.txt

script, from_file, to_file = argv  # creates arguments to run through script

print "Copying from %s to %s" % (from_file, to_file)  # is the test.txt file (arg) to run thru
# and to_file is the new_file arg)
# we could do these two on one line, how?

in_file = open(from_file)  # in_file will open the test.txt file
indata = in_file.read()  # indata is will read test.txt file

print "The input file is %d bytes long" % len(indata)  # len gives the length of the indata file

print "Does the output file exist? %r " % exists(to_file)   # this uses command exists to see if to_file(new_file) exist
print "Ready, hit Return to continue, CTRL-C to abort."
raw_input()  # allows you to return

#  this copies from_file (test.txt) to to_file (new_file.txt)
out_file = open(to_file, 'w')  # calls out_file to open new_fromfile
out_file.write(indata)  # writes the indata file

print "Alright, all done."

out_file.close()  #closes the outfile
in_file.close()   # closes the infile
