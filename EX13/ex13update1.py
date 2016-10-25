# Study Drill
# line 2 is called "import", this is how I add features to this script
from sys import argv
# argv is the "argument variable", it holds the variable I pass

# line 6 "unpacks" the argv
script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

agreement = raw_input("Do you agree? ")

# features = modules or libraries
