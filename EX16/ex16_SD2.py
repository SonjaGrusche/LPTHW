from sys import argv

script, filename = argv


print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# w gives us "write access"
# and if the file already exists w will truncate it by itself
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "NowI'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%r\n%r\n%r\n" % (line1, line2, line3))
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()
# sorry for making more files than I actually needed
