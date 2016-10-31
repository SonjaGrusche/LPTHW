#def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print "You have %d cheeses!" % cheese_count
    #print "You have %d boxes of crackers!" % boxes_of_crackers
    #print "Man that's enough for a party!"
    #print "Get a blanket.\n"


#print "We can just give the function number directly:"
#cheese_and_crackers(20, 30)

#print "OR, we can use variables from our script:"
#amount_of_cheese = 10
#amount_of_crackers = 50

#cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#print "We can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)


#print "And we can combine the two, variables and math:"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study Drills
def popcorn_and_icecream(popcorn_buckets, icecream_sandwiches):
    print "I have %r buckets of popcorn!" % popcorn_buckets
    print "And look, in the freezer are %r icecream sandwiches!" % icecream_sandwiches
    print "Let's Netflix 'n' chill. \n"


print "Version 1: giving numbers directly:"
popcorn_and_icecream(3, 6)

print "Version 2: using variables:"
amount_of_buckets = 4
amount_of_sandwiches = 5

popcorn_and_icecream(amount_of_buckets, amount_of_sandwiches)

print "Version 3: math:"
popcorn_and_icecream(20 - 15, 2 * 3)

print "Version 4: math and variables:"
popcorn_and_icecream(amount_of_buckets + 4, amount_of_sandwiches - 2)

print "Versoin 5: user:"
print "What do you think, how many buckets of popcorn are there?"
buckets = raw_input()
print "And how many icecream sandwiches are left?"
sandwiches = raw_input()
popcorn_and_icecream(buckets, sandwiches)

print "Version 6: user guided by prompt:"
popcornbuckets = raw_input("How many popcorn buckets do you have?")
icecreamsandwiches = raw_input("And how many sandwiches?")
popcorn_and_icecream(popcornbuckets, icecreamsandwiches)

print "Ok, I can't think of more versions right now."
