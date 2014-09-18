__author__ = 'student'



def user_first_name():
    global firstname
    firstname = raw_input('What is your first name?')
    return firstname

def user_last_name():
    global lastname
    lastname = raw_input("What is your last name?")
    return lastname

def name():
    global full_name
    full_name = user_first_name(), user_last_name()
    return full_name

def email_address():
    global email
    email = raw_input('What is your email address?')
    return email

def user_name():
    global username
    username = raw_input('Create a sign in Username')
    return user_name()

def password():
    global password
    password = raw_input('create a password')
    return password

def user_age():
    global age
    age = raw_input('How old are you')
    return age

def occupation():
    global occupation
    occupation = raw_input('What is your occupation?')
    return occupation

def user_city():
    global city
    city = raw_input('What city do you live in?')
    return city

def user_state():
    global state
    state = raw_input('What state do you live in?')
    return state

def user_hobbies():
    global hobbies
    hobbies = raw_input('What hobbies do you enjoy')
    return hobbies

def user_interest():
    global user_interest
    interest =raw_input("Which group are you interested in connecting with? single mothers, book club, writing club ")
    return interest


#def update_user():

# def match_hobbies():
#     global hobbies
#     hobbies = ('what are your hobbies')
#     return hobbies
#
# def search():
#     search = ('hobbies', 'ethnicity', 'age', 'location', 'interest')
#     return search

def ethnicity():
    global ethnicity
    ethnicity = raw_input('What is your ethnicity?')
    return ethnicity

def welcome():
    welcome = raw_input('Welcome to SISTAS Connection.  Would you like to sign up and begin to connect with other like-minded women?')
    if welcome == 'yes' or 'y':
        sign_in()

#def sign_in():
    #pass


class User():
    def __init__(self): #firstname, lastname, email, city, state):# you define class and add the required inputs for user.
        self.firstname = user_first_name() #raw_input('what is your name?')
        self.lastname = user_last_name()
        self.email = email_address()
        self.city = user_city()
        self.state = user_state()
        self.fullname = self.firstname + " " + self.lastname
# # include optional functions that are optional and user can update later
#         self.age = user_age()
#         self.ethnicity = ethnicity() #( removed None so and included it into save_user inputs, in order for the test function below to work)
#         self.occupation = occupation()
        self.hobbies = user_hobbies() # creates a list of hobbies that user can add.
#         self.interest = user_interest() #creates a list of users interest.
#         self.username = user_name()
#         self.password = password()
#         #return User()



def add_hobbies(self, hobby): # define the function. (always use self, and name of what you are wanting to get.)
    self.hobbies.append(hobby) # create the variable pulling from the class using append-to update information.
    return self.hobbies # returns will return and save what the users answers.

def add_interest(self, interest):
    self.interest.append(interest)
    return self.interest

def add_occupation(self, occupation):
    self.occupation.append(occupation)
    return self.occupation

def add_ethnicity(self, ethnicity):
    self.ethnicity.append(ethnicity)
    return self.ethnicity

def save_user(self):
        self.user_state = {}# will create a dictionary of what you want to see.
        self.user_state[self.fullname] = {'user_first_name': self.firstname, 'user_hobbies': self.hobbies, 'email_address': self.email, 'user_city': self.city, 'user_state': self.state,  }
       # this calls the fullname list and includes
        #for age, firstname, you call the object and the attribute. and as you define other inputs, you have to update  this function.
        return self.user_state # will return user_state with  age, firstname, hobbies, interest.
# to tes if it works created  g to equal User, print save user g. from inputs. and print user to print dicitoanary.
g = User()
#need to figure out how to use update feature
#g.add_hobbies("reading")
print save_user(g)
#print User
# need to figure out how to print all the input info check phone directory figured that out.





