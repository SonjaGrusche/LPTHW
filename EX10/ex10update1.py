# defining the variables of the four cats
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm  split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
''' # I don't really see a difference in using "' or """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Study Drills
text = "\tcreate\n\"complex\"\n\t \\ format \\"
more_text = "\n\tF\n\tU\n\tN"

print "Now I'm asked to %s %s." % (text, more_text)
print 'Now I\'m asked to %s %s.' % (text, more_text)
print "Now I'm asked to %r %r." % (text, more_text)

# explanation of the Escape Sequences used above (and more)
# \\ Backslash (\)
# \' Single-quote (')
# \" Double-quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r Carriage Return (CR)
# \t Horizontal Tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32-bit hey value xxxxxxxx (Unicode only)
# \v ASCII vertical tab (VT)
# \ooo Character with octal value ooo
# \xhh Character with hex value hh

# fun code

# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
