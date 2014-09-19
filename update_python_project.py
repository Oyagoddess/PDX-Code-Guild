__author__ = 'student'

# so unfortunately i did extra work, you don't need to create global scope functions for class becuase it will create own objects and attributes
#that you can use and call directly from the clas..


# you can create functions within the class by using: def self.welcome(for example) if self.welcome = yes or no same as other learned
#functions just in class with self.
# need to create welcome function if they want to sign up or not.

class User():

    def __init__(self): #firstname, lastname, email, city, state):# you define class and add the required inputs for user.
        self.welcome = raw_input('Welcome to SISTAS Connection.  Would you like to sign up and begin to connect with other like-minded women?')
        self.firstname = raw_input('What is your first name?')
        self.lastname = raw_input('What is your last name?')
        self.email = raw_input('What is your email address?')
        self.city = raw_input('What city do you live in?')
        self.state = raw_input('What state do you live in?')
        self.fullname = self.firstname + " " + self.lastname
# include optional functions that are optional and user can update later
        self.age = raw_input('How old are you')
        self.ethnicity = '' #(  2nd update removed None so and included it into save_user inputs, in order for the test function below to work)
        #3rd update to program, to add user inputs later. you can create a string by using '' and will change the def statement below.
        # and have =move the question into the add functions.
        self.occupation = ''
        self.username = raw_input('Please create a Username')
        self.password = raw_input('Please create a password')
        # I want to create a list that users can choose from.
        self.hobbies = '' # creates a list of hobbies that user can add.
        self.interest = '' #creates a list of users interest.


    def add_hobbies(self, hobby): # define the function. (always use self, and name of what you are wanting to get.)
        hobby = raw_input('What are your hobbies?')
        self.hobbies =hobby  # create the variable pulling from the class using append-to update information.
        return self.hobbies  # returns will return and save what the users answers.

    def add_interest(self, interest):
        interest = raw_input('What SISTAS group are you interested in?(choose from single mothers, widowed mothers, Book club, Writing Club)')
        self.interest = interest
        return self.interest

    def add_occupation(self, occupation):
        occupation = raw_input('What is your occupation?')
        self.occupation = occupation
        return self.occupation

    def add_ethnicity(self):
        ethnicity = raw_input('What is your ethnicity? (please self identify)')
        self.ethnicity = ethnicity
        return self.ethnicity

    def save_user(self):
        self.user_state = {}# will create a dictionary of what you want to see.
        self.user_state[self.fullname] = {'user_first_name': self.firstname, 'user_lastname': self.lastname, 'user_hobbies': self.hobbies,
                                          'user_interest': self.interest, 'user_age': self.age, 'user_occupation':self.occupation,
                                          'user_city': self.city, 'user_state': self.state, 'user_ethnicity': self.ethnicity}
       # this calls the fullname list and includes( will try to create shorter names)
        #for age, firstname, you call the object and the attribute. and as you define other inputs, you have to update  this function.
        return self.user_state # will return user_state with  age, firstname, hobbies, interest.
# to test if it work created  g to equal User, print save user g. from inputs. and print user to print dicitoanary.

g = User()
print g.save_user()
g.add_ethnicity()
#had to change the add functions for user inputs and now when we try to add the question is asked after all questions. and added
#into the dictionary
#these are sample users to use for search and add functions.
p = User()
print p.save_user()
c = User()
print c.save_user()

# create a community for all users to go into and search in
# i think i need to create a search functon.
#
class Community():
     def __init__(self):
         self.users = [g, p, c]












