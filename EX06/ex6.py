# the variable for x gets set, it consists of a string with a format character and its variable at the end
x = "There are %d types of people." % 10
# the variable for binary is binary
binary = "binary"
# the variable for do_not  is don't
do_not = "don't"
# the variable for y is a string that includes two format characters and its variables at the and
y = "Those who know %s and those who %s." % (binary, do_not) # two strings inside a string

# line 11 and 12 print what'sinside the variables for x and y
print x
print y

# lines 15 and 16 print what's inside the quotes usind the variables at the end to fill in the format characters
print "I said %r." % x # string inside string
print "I also said: '%s'." % y # one string that already includes two strings is put inside string

# lines 19 and 20 define two more variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# line 23 prints the variable for joke_evaluation and fills in the variable for hilarious for the format character
print joke_evaluation % hilarious

# line 26 and 27 define two variables
w = "This is the left side of..."
e = "a string with a right side."

# variables from line 26 and 27 get printed
print w + e

# Study Drill
# 4. the + concatenates the two strings (not functioning as a math operater)
