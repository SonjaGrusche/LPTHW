## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog can be accessed by its name attribute
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat can be accessed by its name attribute
        self.name = name

## Person is-a (new) object
class Person(object):

    def __init__(self, name):
        ## Person can be accessed by its name attribute
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Emplyee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## this is how I can run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## salary is an attribute that can be accessed
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Hailbut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
