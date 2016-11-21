textfile = open("text.txt", "r")
content = textfile.read()
textfile.close()
textlist = content.split("%")
del textlist[0]

script = {}
while textlist:
    key = textlist.pop(0)
    value = textlist.pop(0)
    script[key] = value

print script
