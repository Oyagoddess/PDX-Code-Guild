__author__ = 'student'
# creating a social site for women to connect with each other, via location, interest, age, ethnicity, hobbies
# want to create a generic bio using the users inputs to questions.
# #create a directory that will take all of the inputs and create a dictionary wherever the fit. via age, location, interests. hobbies
# want to create a directory for clients info assigning user name and password.
# allow users to sign up, delete, update their information
# search for users via location, hobbies, interest, ethnicity.

#Create class for users so their information will be stored and will be searchable, can be updated, matched to others.
#Define User: what will each user have to include)
#create the funcitons to call later.
class User():
    def __init__(self, firstname, lastname, email, city, state):# you define class and add the required inputs for user.
        # create functions for raw input and removing init variables that were added before to test)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.city = city
        self.state = state
        self.fullname = self.firstname + " " + self.lastname
# include optional functions that are optional and user can update later
        self.age = None
        self.ethnicity = []#None ( removed None so and included it into save_user inputs, in order for the test function below to work)
        self.occupation = []#None
        self.hobbies = [] #creates a list of hobbies that user can add.
        self.interest = [] #creates a list of users interest.
        #self.username = username

        #return User() #once you create a class, and begin to define methods, you no longer need to return, User becuase it is being returned
        # save_user.


   #create methods for hobbies list and interest list and will allow users to search for other users with similar hobbies and interest:
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


# this is a User method in class, every  user will get this method when input info.
#create a save user function
    def save_user(self, User):
        self.user_state = {}# will create a dictionary of what you want to see.
        self.user_state[self.fullname] = {'age': self.age, 'firstname': self.firstname, "hobbies": self.hobbies, "interest": self.interest, "occupation": self.occupation, "ethnicity":self.ethnicity}
       # this calls the fullname list and includes
        #for age, firstname, you call the object and the attribute. and as you define other inputs, you have to update  this function.
        return self.user_state # will return user_state with  age, firstname, hobbies, interest.

# to test, create user. by making a variable. q= calling User(including attributes required)
q = User(firstname='shalonda', lastname='menefee', email='shalonda_menefee@hotmail.com', city='portland', state='oregon') # this is a tupal
#practice adding another person.
m = User(firstname='Angelic,', lastname='davis', email='angelic@gmail.com.', city='portland', state='Oregon')

#adding age
#q. unique_id
q. age = 29 # if you want to add or update age for user q then you call q.age = whatever the age is.
#to save information of user q. you call q.save_user(q)
# updated and tested updating the users additional information.
q. add_hobbies("reading")
q. add_interest('single parents, widowed parents')
q. add_ethnicity('African American')
q. add_occupation("teacher")
q.save_user(q)
# to see user q printed with firstname, age, and user_state which includes the fullname,
print (q.user_state, q.add_occupation, q.add_ethnicity, q.add_interest, q.add_hobbies)
# updates need to go before the save statement

#m. hobbies = 'reading, writing' # it wont update saying reading is not defined.
m. age = 14
m.add_hobbies('dancing')
#m. occupation = 'teacher' # you have to add occupation and hobbies as a string in order for it to be added. unable to update the occupation not sure why. it is saying teacher is undefined.
m.save_user(m)
print (m.user_state, m.age, m. occupation)







def user_first_name():
    firstname = raw_input('What is your first name?')
    return firstname



def user_last_name():
    lastname = raw_input("What is your last name?")
    return lastname

def name():
    full_name = user_first_name(), user_last_name()
    return full_name

def email_address():
    email = raw_input('What is your email address?')
    return email


def user_name():
    username = raw_input('Create a sign in Username')
    return user_name()

def password():
    password = raw_input('create a password')
    return password

#def update_user():

def match_hobbies():
    hobbies = ('what are your hobbies')
    return hobbies


def search():
    search = ('hobbies', 'ethnicity', 'age', 'location', 'interest')
    return search

def ethnicity():
    ethnicity = raw_input('What is your ethnicity?')
    return ethnicity

def welcome():
    welcome = raw_input('Welcome to SISTAS Connection.  Would you like to sign up to begin to connect with other like-minded women?')
    if welcome == 'yes' or 'y':
        sign_in()

def sign_in():
    pass

match_hobbies()

# Create bio using the clients input.
firstname = str(raw_input('what is your first name?'))
lastname = str(raw_input('What is your last name?'))
age = str(raw_input('How old are you'))
occupation = str(raw_input ('What is your occupation?'))
city = str(raw_input('What city do you live in?'))
state = str(raw_input('What state do you live in?'))
hobbies = str(raw_input('What hobbies do you enjoy?'))
interest= str(raw_input("Which group are you interested in connecting with? "
                         "(choose at least one, single parenting, book club, writing club, widowed mothers)"))


madlist = {'f': firstname, 'l': lastname, 'a': age, 'o': occupation, 'c': city, 's': state, 'h': hobbies, 'i': interest}

bio = 'Hello, my name is %(f)s. I am %(a)s years old.  I live in %(c)s,%(s)s.\n''I enjoy %(h)s.  I would like to connect with women who are interested in %(i)s'



print bio % madlist
