#cleaner functional phonebook
name = 'name'
address = 'address'
phone = 'phone'
entry = [name, address, phone]
phonebook = {}  #{name: entry}
phonebook['joe'] = ['joe', '123 elm st', '123-456-1234']
print phonebook

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
    find = raw_input('who do you want to find?')
    if find == phonebook[find]:
        d = {'n': find[0], 'a': find[1], 'p': find[2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
    else:
        print ('It is not found')

elif choice == 'delete':
    delete = raw_input('who do you want to delete?')
    if delete == name:
        d = {'n': delete[0], 'a': delete[1], 'p': delete[2]}
        template = """
        %(n)s
        %(a)s
        %(p)s
        """
        print (template % d)
        answer = raw_input('are you sure you want to delete? y/n')
        if answer == 'y' or 'yes':
            print(phonebook)

        else:
            print('You changed your mind!')
    else:
        print ('It is not found')


