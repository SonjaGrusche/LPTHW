# this one is like your scripts with argv
# telling Python to make a function using def (define)
# "print_two" is just a name foor the function, could be any other name
# *args is pretty much the same as argv for functions
def print_two(*args):
    # everything indented after the colon will be attached to"print_two"
    # first indented line unpacksthe arguments (just like for scripts)
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one  takesno arguments
def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
