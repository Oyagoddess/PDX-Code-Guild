#saves user inputs as new phonebook entry
name = raw_input('What is your first and last name?')
address= raw_input('What is your current address?')
phone= raw_input('what is your phone number?')

#create list of entry
entry = [name, address, phone]
#test that entry works
#print (entry)
#create dictionary of name and entry
phonebook = {name:entry}
#test that phonebook works
print (phonebook)

#saves user input to create a search
#search= raw_input('who do you want to find?')

#format address entry
d = {'n': phonebook[entry[0], 'a': phonebook[entry][1], 'p': phonebook[entry][2]}
template = """
%(n)s
%(a)s
%(p)s
"""
#final phonebook entry output
print (template % d)

#alternative entry format
#print(phonebook[search][0] + " " + phonebook[search][1] + " " + phonebook[search][2])
