# Here's some new strange stuff, remember type itexactly.

# setting variables in lines 4 and 6
days = "Mon Tue Wed Thu Fri Sat Sun"
# using "backslash + n" (newlines - new line character) will make the text behind appear on the next line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # backslash doesn't work on German keyboards in Atom

# Variables get printed just by writing it after the string
print "Here are the days: ", days
print "Here are the months: ", months

# as the text says, three double-quotes let magic happen
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
