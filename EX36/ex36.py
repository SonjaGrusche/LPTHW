# Homework EX36 - The Mansion
# Have fun!
# Sonja Grusche

from sys import exit

def start():
    print """
    Hey you!
    Yes... I'm talking to you.
    Would you like to play a game?
    > Yes! (type "y")
    > Not really, no... (type "n")
    """

    choice = raw_input('> ')

    if choice == "y":
        hallway_y()
    elif choice == "n":
        hallway_n()
    else:
        dead("You haven't started playing yet and already managed to die. Typos will kill you!")


def dead(why):
    print why, "Try again!"
    exit(0)


print "First of all, I need you to give your player a name!"
username = raw_input ('> ')
print "Okay, %r is a lovely name. Let's do this!" % username

print """
So, %r, my job here is to guide you through this adventure.
Try to follow the instructions you get to make a decision.
I've seen people die because of typos.
""" % username


def hallway_y():
    print """
    You are standing inside a hallway of an old mansion.
    The door behind you is locked.
    Of course you don't want to be there.
    You need to find the key to get out.
    So why are you still standing here?
    The hallway leads to three doors.
    Which one do you want to open?"
    > left door (type in "l")
    > middle door (type in "m")
    > right door (type in "r")
    """
    choice = raw_input('> ')

    if choice == "l":
        print "Oh, this door is locked, too."
        hallway_again()
    elif choice == "m":
        print """
        Entering the middle door a bright and warm light reveals a big hall.
        Two wooden stairs arranged in two beautifully shapened bows are framing
        the room and lead towards a big golden door.
        Underneath the stairs at the end of the room are two more doors.
        Both have the same superior fassade.
        The ceiling is adorned with an outrageously expensive appearing chandelier.
        Right under the chandelier sits a friendly looking old man.
        Next to him stands a little wooden table, on top a cup of tea or coffee.
        """
        quizroom()
    elif choice == "r":
        right_door()
    else:
        dead("Mind your writing!")


def hallway_n():
    print """
    HAHA! As if you really had a choice!
    You are standing inside a hallway of an old mansion.
    The door behind you is looked.
    Of course you don't want to be there.
    You need to find the key to get out.
    So why are you still standing here?
    The hallway leads to three doors.
    Which one do you want to open?"
    > left door (type in "l")
    > middle door (type in "m")
    > right door (type in "r")
    """
    choice = raw_input('> ')

    if choice == "l":
        print "Oh, this door is locked, too."
        hallway_again()
    elif choice == "m":
        quizroom_one()
    elif choice == "r":
        right_door()
    else:
        dead("Mind your writing!")


def right_door():
    print """
    Look, there is a trapdoor.
    It must lead to the basement.
    I don't think we will find a key down there.
    But do you want to go down anyway?
    > 'Yes, let's check it out!' (type "y")
    > 'Oh hell no, I don't like basements!' (type "n")
    """

    choice = raw_input('> ')

    if choice == "y":
        print "After opening the door a heavy undertow drags you inside the vast darkness."
        dead("Ooops.")
    elif choice == "n":
        hallway_again()


def hallway_again():
    print """
    Well, try another door.
    > left door (type in "l")
    > middle door (type in "m")
    > right door (type in "r")
    """

    choice = raw_input('> ')

    if choice == "l":
        print "Oh, this door is locked, too."
        hallway_again()
    elif choice == "m":
        print """
        Entering the middle door a bright and warm light reveals a big hall.
        Two wooden stairs arranged in two beautifully shapened bows are framing
        the room and lead towards a big golden door.
        Underneath the stairs at the end of the room are two more doors.
        Both have the same superior fassade.
        The ceiling is adorned with an outrageously expensive appearing chandelier.
        Right under the chandelier sits a friendly looking old man.
        Next to him stands a little wooden table, on top a cup of tea or coffee.
        """
        quizroom()
    elif choice == "r":
        right_door()
    else:
        dead("Mind your writing!")


def quizroom():
    print """
    What do you want to do now, %r?
    > 'I really want to see what's inside the door at the end of the stairs!' (type "top")
    > 'I want to check out the left door at the bottom.' (type "left")
    > 'I want to check out the rght door at the bottom.' (type "right")
    > 'I should talk to the old man, maybe he can help me to get outta here.' (type "old man")
    """ % username

    talked_with_oldman = False

    while True:

        choice = raw_input('> ')

        if choice == "top" and not talked_with_oldman:
            print "Damn, the door is closed."
        elif choice == "left":
            print "Something dark is waiting behind the door."
            dead("It makes you feel your worst nightmares. No escape.")
        elif choice == "right":
            print "White, glistening light takes your eyesight away."
            dead("It makes you see your worst nightmares. No Escape.")
        elif choice == "old man":
            print "The old man points on a letter on the table."
            talked_with_oldman = True
            old_man()
        elif choice == "old man" and talked_with_oldman:
            print "The chandelier starts to shake."
            print "The old man starts to laugh hysterically."
        elif choice == "top" and talked_with_oldman:
            print """
            The door is open.
            When did he... open.. nevermind.
            I can't wait to get out of here!
            The old man's stare was a little bit too much for me.
            """
            top_door()
        else:
            dead("You still don't know how this game works?")


sorry = "You shall not pass!"


def old_man():
    question_number = 1

    print """
    The letter says:
    Only if you can answer following three questions I am allowed to help you
    and will open the door at the end of the stairs for you.
    If your answer is wrong, your journey will be over.
    Keep in mind, that these questions are unbelievable difficult.
    No one has ever solved all three of them.
    May the force be with you.
    """

    while question_number < 4:

        if question_number == 1:
            print """
            How many holes in a Polo?
            > 1
            > 2
            > 3
            > 4
            """
            choice = raw_input('> ')

            if choice == "1":
                dead(sorry)
            elif choice == "2":
                dead(sorry)
            elif choice == "3":
                dead(sorry)
            elif choice == "4":
                print """
                Absolutely correct!
                """
                question_number += 1
            else:
                dead("Well, this is awkward... ")

        if question_number == 2:
            print """
            Can a match box?
            > Yes (type "y")
            > No (type "n")
            > No, but a tin can. (type "tin")
            > Yes, one beat Mike Tyson. (type "mike")
            """
            choice = raw_input('> ')

            if choice == "y":
                dead(sorry)
            elif choice == "n":
                dead(sorry)
            elif choice == "tin":
                print """
                Hell yes!
                """
                question_number += 1
            elif choice == "mike":
                dead(sorry)
            else:
                dead("Well, this is awkward... ")

        if question_number == 3:
            print """
            Final question:
            Can you get this question wrong?
            > No. (type "1")
            > Nope (type "2")
            > I hope not.. (type "3")
            > Of course not. (type "4")
            """
            choice = raw_input("> ")

            question_number += 1

            if choice == "1":
                print "Good choice!"
                top_door()
            elif choice == "2":
                print "Marvellous!"
                top_door()
            elif choice == "3":
                print "You are a genius, %r!" % username
                top_door()
            elif choice == "4":
                print "Ugh, that was really close! Congrats!"
                top_door()


def top_door():
    print """
    The door is open.
    When did he... open.. nevermind.
    I can't wait to get out of here!
    The old man's stare was a little bit too much for me.
    Inside of the room a golden table stands in the middle.
    A key is placed on a silky cushion.
    Next to the table a sign is placed.
    There are three items laying on top of it.
    Apart of that the room is empty.
    There aren't even windows.
    The room is illuminated by another ridiculously big chandelier.
    What do you want to do?
    > 'Grab the key and get the hell out of here.' (type "key")
    > 'Read the sign. Why should I rush now?' (type "sign")
    """

    choice = raw_input("> ")

    if choice == "key":
        print """
        The chandelier starts to shake.
        From outside you can hear the old man's laugh.
        The last thing you hear is the chinking of the chandelier's diamonds.
        """
        dead("Always read the instructions first!")
    elif choice == "sign":
        print """
        Let's see what the sign says:
        'You made it this far,
        so I will give you a chance to survive.
        Look at the ground underneath the table.
        Under the loose tile is a weighting scale placed.
        You wouldn't have stand a chance of leaving this room alive,
        if you grabbed the key unwary.
        See the three items?
        A tin of ravioli.
        George Orwell's '1984' paperback edition.
        And box of matches.
        The key has the exact same weight as one of the items.
        After you take the key off the table you'll have two seconds to
        replace it with something else.
        If you take more than two seconds, it will be over.'
        Okay, so you have to make a decisions now..
        Which item do you choose?
        > 'The ravioli might be too heavy, but I can't tell that for sure.' (type "ravioli")
        > 'The book seems to be light lecture. Can this match?' (type "book")
        > 'Can the box of matches save me?' (type "box")
        """

        choice = raw_input("> ")


        if choice == "ravioli":
            print """
            You are anxiously lifting the key and
            putting the tin of ravioli on its place.
            Nothing happens. You are safe!
            You run back to the hallway.
            """
            hallway_final()
        elif choice == "book":
            print """
            You are anxiously lifting the key and
            putting George Orwell's '1984' on its place.
            The chandelier starts to shake.
            From outside you can hear the old man's laugh.
            The last thing you hear is the chinking of the chandelier's diamonds.
            """
            dead("Apparently, that was the wrong choice.")
        elif choice == "box":
            print """
            You are anxiously lifting the key and
            putting the box of matches on its place.
            The chandelier starts to shake.
            From outside you can hear the old man's laugh.
            The last thing you hear is the chinking of the chandelier's diamonds.
            """
            dead("Apparently, that was the wrong choice.")
        else:
            dead("You are hopeless.")

    else:
        dead("I haven't even words for this anymore.")


def hallway_final():
    print """
    I would've never guessed that you are patient enough to get through this!
    Now you only have to choose the right door!
    Remember, there were the doors on the left
    and behind of you that were locked.
    I don't think using a key twice will be a problem, either.
    But to use a key, you have to be alive
    and I trust none of these doors anymore.
    Doesn't matter if they're unlocked or locked.
    Choose wisely!
    > left door (type "l")
    > door behind you (type "b")
    """
    choice = raw_input("> ")

    if choice == "l":
        print """
        The key doesn't fit. Nothing happens.
        Well, that is unsatisfying.
        """
    elif choice == "b":
        print """
        The door opens.
        You are a free human again.
        Congratulations, %r!
        """ % username
        exit(0)

start()
