
#create a updateable phonebook 
name = 'name'
address = 'address'
phone = 'phone'
entry = [name, address, phone]
phonebook = () #{name:entry}
phonebook = {'joe': ['joe', '123 elm st', '123-456-1234']}

#ask user what they want to do
choice= raw_input ('would you like to add, search or delete an entry?')
if choice == 'add':
    name = raw_input('What is your first and last name?')
    address= raw_input('What is your current address?')
    phone= raw_input('what is your phone number?')
    entry= [name, address, phone]
    phonebook= {name:entry}
    phonebook.update(
    d = {'n': phonebook[name][0], 'a': phonebook[name][1], 'p': phonebook[name][2]}
    template = """
    %(n)s
    %(a)s
    %(p)s
    has been added
    """
    print (template % d)

elif choice =='search':
    find= raw_input('who do you want to find?')
    if find == name:
        d = {'n': phonebook[find][0], 'a': phonebook[find][1], 'p': phonebook[find][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
    else:
	print ('It is not found')
elif choice == 'delete':
    delete= raw_input ('who do you want to delete?')
    if delete == name:
	d = {'n': phonebook[delete][0], 'a': phonebook[delete][1], 'p': phonebook[delete][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
	"""answer= raw_input ('are you sure you want to delete? y/n')
    	if answer == 'y':
	    phonebook.remove[delete]
	    print(phonebook)
	else:
	    print('You changed your mind!')"""
    else:
        print ('It is not found')
else:
    print ('please choose an option')

choice= raw_input ('would you like to add, search, or delete an entry?')
if choice == 'add':
    name = raw_input('What is your first and last name?')
    address= raw_input('What is your current address?')
    phone= raw_input('what is your phone number?')
    entry= [name, address, phone]
    phonebook= {name:entry}
    d = {'n': phonebook[name][0], 'a': phonebook[name][1], 'p': phonebook[name][2]}
    template = """
    %(n)s
    %(a)s
    %(p)s
    Has been added
    """
    print (template % d)
    
elif choice =='search':
    find= raw_input('who do you want to find?')
    if find == name:
        d = {'n': phonebook[find][0], 'a': phonebook[find][1], 'p': phonebook[find][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
    else:
        print ('It is not found')
elif choice == 'delete':
    delete= raw_input ('who do you want to delete?')
    if delete == name:
        d = {'n': phonebook[delete][0], 'a': phonebook[delete][1], 'p': phonebook[delete][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
else:
    print ('please choose an option')

#name = raw_input('What is your first and last name?'
#address= raw_input('What is your current address?')
#phone= raw_input('what is your phone number?')

#entry= [name, address, phone]
#test that entry works
#print (entry)
#create dictionary of name and entry
#phonebook= {name:entry}
#test that phonebook works
#print (phonebook)

#saves user input to create a search
#search= raw_input('who do you want to find?')

#format address entry
#d = {'n': phonebook[search][0], 'a': phonebook[search][1], 'p': phonebook[search][2]}
#template = """
#%(n)s
#%(a)s
#%(p)s
#"""
#final phonebook entry output
#print (template % d)

#alternative entry format
#print(phonebook[search][0] + " " + phonebook[search][1] + " " + phonebook[search][2])
