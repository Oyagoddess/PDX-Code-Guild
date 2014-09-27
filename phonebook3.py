# Cleaner updated phonebook
name = 'name'
address = 'address'
phone = 'phone'
entry = [name, address, phone]
phonebook = {}  # removed original value- {name: entry} to test joe.
phonebook['joe'] = ['joe', '123 elm st', '123-456-1234']

choice = raw_input('would you like to add, search or delete an entry?')

if choice == 'add':
    name = raw_input('What is your first and last name?')
    address = raw_input('What is your current address?')
    phone = raw_input('what is your phone number?')
    entry = [name, address, phone]
    phonebook = {name: entry}
    d = {'n': entry[0], 'a': entry[1], 'p': entry[2]}
    template = """
    %(n)s
    %(a)s
    %(p)s
    Has been added
    """
    print (template % d)
    print (phonebook)

elif choice == 'search':
    name = raw_input('who do you want to find?')  # had to redefine search variable
    if name in phonebook.keys():   # Changed to an 'if' statement so that it will look in the dictionary key.
        d = {'n': phonebook[name][0], 'a': phonebook[name][1], 'p': phonebook[name][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
    else:
        print ('It is not found')

elif choice == 'delete':
    name = raw_input('who do you want to delete?')
    if name in phonebook.keys():
        d = {'n': phonebook[name][0], 'a': phonebook[name][1], 'p': phonebook[name][2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
        answer = raw_input('are you sure you want to delete? y/n')
        if answer == 'y' or 'yes':
            phonebook.pop(name)    # Added a method to delete the dictionary.
            print(phonebook)
        else:
            print('You changed your mind!')
    else:
        print ('It is not found')


