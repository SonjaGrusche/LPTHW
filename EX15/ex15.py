# importing the module argv from sys (package)
from sys import argv

# multiple assignment of arguments
script, filename = argv

# setting a command to open variable files
txt = open(filename)

# this line uses a format character to fill in the filename we gave as an argument
print "Here's your file %r:" % filename
# this line uses the variable we set in line 8 to open it and print it (reading it out)
print txt.read()
# closing the txt file
print txt.close()

print "Type the file name again:"
# using the raw_input to get input by the user
file_again = raw_input("> ")

# what the user types in in line 17 will be opened at this point (if it exists)
txt_again = open(file_again)
# same function as line 13
print txt_again.read()
# closing the txt file
print txt_again.close()

# commandsare also called "functions" or "methods"

# Study Drill
# raw_input will use any input you give,
# whereas argv needs rather specific arguments (?)
