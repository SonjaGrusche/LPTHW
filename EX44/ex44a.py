# implicit inheritance
class Parent(object):

    def implicit(self):
        print "PARENT implicity()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
