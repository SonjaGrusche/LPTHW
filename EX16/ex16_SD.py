from sys import argv

script, filename = argv


print "So, we've just created %r." % filename
print "Let's give %r some input!" % filename

print "Maybe explain what you like or dislike about Halloween."

line1 = raw_input("line 1: ")

print "Alright, there you have it."

target = open(filename, 'w')
target.write(line1)
target.write("\n")

print "Okay, let's close it."

target.close()

print "Do you want to erase the content of the file?"
print "If you do, write/hit RETURN."
print "If you don't, hit CTRL-C (^C)."

raw_input("Let me know.")

print "Opening the file..."
target = open(filename, 'w')

print "Here we go! Erasing your words from the file."
target.truncate()
