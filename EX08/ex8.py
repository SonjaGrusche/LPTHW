# variable 'formatter' gets defined by a string of formatters
formatter = "%r %r %r %r"

# the formatter get replaced by different variables, strings, boolean values
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# the variable gets replaced by the variable itself
print formatter % (formatter, formatter, formatter, formatter)
# the variable gets replaced by strings (in the same line because of the comma)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
# the last for lines get printed with single and double quotes
# why exactly - not sure
