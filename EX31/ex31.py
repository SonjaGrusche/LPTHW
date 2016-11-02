print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Use the bear costume in your left hand to distract him and escape through another door."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"

    elif bear == "3":
        print "Hoaah! That was a close call! You almost died!"
        print "There is a huge and long wall in front of you. What now?"
        print "1. Go to Castle Black to find Jon Snow."
        print "2. Try to ride the extremely angry and dangerous looking Dragon who sits next to Castle Black."

        GoT = raw_input("> ")

        if GoT == "1":
            print "A black shadow appears from behind and runs a knife in your back."
            print "No one likes spoilers, you filthy muggle!"
        elif GoT == "2":
            print "Being abandoned and hated by people as a baby, he dragon is happy about your company."
            print "Together you conquer the world. Good job!"
        else:
            print "The Night's Watch thinks you're the enemy and kills you. Good job!"

    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall ona knife and die. Good job!"
