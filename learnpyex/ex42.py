## Animal is a object (yes, sort of confusing) look at extra credit
class Animal(object):
    pass

##?? Dog is-a animal.
class Dog(Animal):  # dog is an animal and inherits from animal

    def __init__(self, name):   # assigns a name to the dog.  Dog has a name
        ##??
        self.name = name

        print "The dogs name is %s" % name
##?? cat is a animal and has a name
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name

##?? person is a object and has a name and a pet or animal
class Person(object):

    def __init__(self, name):
        ##??
        self.name = name

        ##Person has a pet of some kind
        self.pet = None

        print "%s has a pet" % (name)

## ?? An employee is a person and has a name and salary
class Employee(Person):
    def __init__(self, name, salary):
        ##?? Hmm what is this strange magic?
        super(Employee, self).__init__(name)   # shortcut to run parent class reliably
        ##??
        self.salary = salary

        print " %s, salary is %s:" %(name, salary)
##?? Fish is a object class
class Fish(object):
    pass

## ?? Salmon is a kind of fish
class Salmon(Fish):
    pass

##??  Halibut is a kind of fish
class Halibut(Fish):
    pass


## rover is a dog and has a name rover
rover = Dog("Rover")

## ??  Satan is a cat and has a name satan
satan = Cat("Satan")

##??  mary is a person and has a name mary
mary = Person("Mary")

##?? mary has a pet named satan which is a cat
mary.pet = satan

##??  Frank is a emplyee has a name called frank and has a salary of 120000
frank = Employee("Frank", 120000)

## ??  frank has a pet named rover which is a dog
frank.pet = rover

## ?? flipper is a fish
flipper = Fish()

## ?? crouse is a salmon
crouse = Salmon()

## ?? harry is a halibut which is a type of fish
harry = Halibut()