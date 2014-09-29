__author__ = 'student'


# Creating Sign-up with classes
class User():

    def __init__(self):
        self.welcome = raw_input('Welcome to SISTAS Connection.  Would you like to sign up and begin to connect with other like-minded women?')
        self.firstname = raw_input('What is your first name?') # create '' to test.
        self.lastname = raw_input('What is your last name?')
        self.email = raw_input('What is your email address?')
        self.city = raw_input('What city do you live in?')
        self.state = raw_input('What state do you live in?')
        self.fullname = self.firstname + " " + self.lastname
        self.age = raw_input('How old are you')
        self.ethnicity = ''  # raw_input('What is your ethnicity?') create '' to test.
        self.occupation = raw_input("what is your occupation")
        self.hobbies = 'golf'  # Input golf for testing search functions. raw_input('what are your hobbies')
        self.interest = 'book club'  # input for testing # raw_input("What are your hobbies?")
        # created madlist for  user inputs to produce a short bio about them.
        madlist = {'f': self.fullname, 'a': self.age, 'o': self.occupation, 'c': self.city, 's': self.state, 'h': self.hobbies, 'i': self.interest}
        bio = 'Hello, my name is %(f)s. I am %(a)s years old. I live in %(c)s,%(s)s.  I enjoy %(h)s and %(i)s.'
        print bio % madlist

    def add_hobbies(self, hobby): # define the function. (always use self, and name of what you are wanting to get.)
        hobby = raw_input('What are your hobbies?')
        self.hobbies = hobby  # create the variable pulling from the class using append-to update information.
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
        return self.user_state

# Created a community class for all users to go into and search for others.
class Community():
     def __init__(self):
        self.username = raw_input('Please create a Username')
        self.password = raw_input('Please create a password')
        self.users = [p]
        print 'Thank you for signing up for SISTAS Empowerment'
        pass

     def search_hobbies(self):
        self.query = raw_input("what hobbies would you like to search for? ")
        for user in self.users:
            if self.query in (user.hobbies):
                print(user.firstname)

     def search_interest(self):
        self.search_interest = raw_input("what interest would you like to search for?")
        for user in self.users:
                if self.search_interest in (user.interest):
                    print user.firstname
     def search_ethnicity(self):
        self.search_ethnicity = raw_input("what ethnicity would you like to search for?")
        for user in self.users:
            if self.search_ethnicity in (user.ethnicity):
                print user.firstname

# Created psuedo user persilla  to test the search functions.
p = User()
p.firstname = "persilla"
#p.age = '45'
p.interest = 'book club, writing club'
p.hobbies = "golf"
p.ethnicity = 'african american'

c = Community()
c.search_hobbies()
c.search_interest()
c.search_ethnicity()

#these ask for search functions and returns persilla if values are the same as assigned.



