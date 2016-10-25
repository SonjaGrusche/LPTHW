print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

# Study Drill

print "What type of music are you listening to?",
music = raw_input()
print "That's nice! Do you have other hobbies?",
hobbies = raw_input()
print "Cool! And how many siblings do you have?",
siblings = raw_input()

print """

You like to listen to %r, and %r,
as well as annoying %r siblings.
Sweet.

""" % (music, hobbies, siblings)
