
#create a updateable phonebook with test entry
phonebook = {'joe': ['joe', '123 elm st', '123-456-1234']}

#ask user what they want to do
choice= raw_input ('would you like to add, search or delete an entry?')

#user chooses to add an entry
if choice == 'add':
#create input variables for entry
	new_name = raw_input('What is your first and last name?')
	new_address = raw_input('What is your current address?')
	new_phone = raw_input('what is your phone number?')
#create dictionary for new entry    
	new_entry = {new_name: [new_name, new_address, new_phone]}
#show entry in user friendly format    
	d = {'n': new_entry[new_name][0], 'a': new_entry[new_name][1], 'p': new_entry[new_name][2]}
	template = """
	%(n)s
	%(a)s
	%(p)s
	has been added
	"""
	print (template % d)
	phonebook.update(new_entry)
#test that phonebook has been updated
   # print (phonebook)

#this does not work. need to figure out error with if part
elif choice =='search':
	find = raw_input('who do you want to find?')
	if phonebook[find]:
		search_entry = {search_name: [search_name, search_address, search_phone]}
		d = {'n': phonebook[search_entry][0], 'a': phonebook[search_entry][1], 'p': phonebook[search_entry][2]}
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
	if phonebook[delete]:
	d = {'n': phonebook[delete][0], 'a': phonebook[delete][1], 'p': phonebook[delete][2]}
	template = d """
		%(n)s
		%(a)s
		%(p)s
		"""
		print (template % d)
	answer= raw_input ('are you sure you want to delete? y/n')
	if answer == 'y':
		print(phonebook)
	else:
		print('You changed your mind!')
	else:
		print ('It is not found')
else:
	print ('please choose an option')


