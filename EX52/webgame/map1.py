from map import Scene

# Creating the Scenes of the game
prologue = Scene("Prologue", "prologue",
"""
Billy keeps having the same nightmare over and over again.
In his dream he wakes up in his bed and everything seems to be normal, but it's not.
Billy's plush toys are gone.
And they want to kill Billy.
He is only save in illuminated area, like his bed which is illuminated by his night light.
Only in the dark his plush toys will attack Billy.
Of course, all light switches disappear in his dream.
Whenever he can't defend himself successfully, he would wake up in the same dream.
The only way to wake up in the real world is to leave the house through the front door.
How Billy's plush animals are approaching him would change from night to night.
""",
"""
Now, what should Billy do?
1. open his eyes
2. stay under the blanket
""")

bunny = Scene("Bunny? Is that you?", "buunny",
"""
Billy opens his eyes. Again, he is still dreaming.
He can't see a plush toy, but from the dark corner of his bedroom a rustling emerges from one drawer.
Billy leaves his room and enters the hall.
From here he has access to the stairs, a bathroom and his parent's bedroom.
As Billy slowly verges on the stairs he sees a bunny-shaped shadow across the wall, something's hopping up the stairs.
His room seems no longer to be save, Billy really has no interest in meeting the thing that caused the rustling.
He can either hide in the bathroom or in his parent's bedroom.
""",
"""
1. bathroom (Billy should enter the bathroom!)
2. bedroom "Billy should enter the bedroom of his parents!"
""")

kitchen = Scene("Flashlight Mission", "kitchen",
"""
Ugh, thank the Lord. There are no evil plush toys waiting for Billy in the bathroom.
His bath duck won't attack him. Billy holds his breath and listens closly.
He can hear the bunny hopping reaching the first floor.
After a few silent seconds a squeking sound comes out of Billy's room.
The bunny must be jumping on his bed.
Billy carefully opens the door of the bathroom and sneaks down the stairs.

Reaching the bottom of the stairs Billy checks the front door. It's closed.
Well, he did not expect something else.
Suddenly, he could hear a jingling that must come from the key ring
that usually hangs on the pin board near the door. Billy looks around the corner.
The hall on the ground floor is flooded through the window front of the kitchen that faces the garden.
But the jingling must come from the living room are.
Billy leaves the stairs and looks inside the room to his left. The living room is connected with the kitchen,
but the window front isn't long enough to illuminate the living room all the way to the back.
Billy knows walking inside the living room without any defense would possibly mean his death.
He remembers there was a flashlight in a kitchen drawer - this could be his rescue!

Billy is standing inside the door frame. He has a good view over the kitchen.
Attentively, Billy scans the kitchen for plushies.
On the countertop that encloses the kitchen drawer with the flashlight he sees his PacMan sitting.
It's hiding in the shadow of the fridge. It hasn't noticed Billy yet.
""",
"""
There are three options.
1. pacman
He should just walk over to the drawer and get the flashlight. How should PacMan be able to harm him?
He doesn't even have legs or arms.
2. orange
Next to Billy a fruit bowl is standing on the countertop. Billy could throw an orange and distract PacMan.
If he's fast enough to get the flashlight, he could scare PacMan away with his light.
3. tablecloth
Billy could crawl behind the kitchen island and reach for the tablecloth of the dining table.
That would make a legit ghost costume. PacMan is scared of ghosts, isn't he?
""")

home_office = Scene("Dad's Home Office", "home_office",
"""
Billy is scared to leave his save place and PacMan out of his sight.
He crawls over to the dining table and slowly pulls the table cloth off of it.
Cautious to make no sound Billy throws it over his head.
He takes a deep breath and jumps back into a stand. Making awful screaming noises he runs towards PacMan.
PacMan gets scared to death and leaves the kitchen. As the moonlight illuminates his full body,
PacMan lights up and burns down to his bones. Success!

Billy takes off the cloth, opens the drawer and grabs the flashlight.
"What if the batteries are empty?" Billy is almost too scared to switch it on, but as he finally convinces himself,
the flashlight would shine as bright as it possibly could.
Billy immediately checks the livingroom for monster plushies, but there aren't any.
The jingling comes out of his dad's office.
He's usually not allowed to enter it, but special cases demand special methods.

As Billy opens the door, the jingling becomes silent.
Billy takes a peek through the ajar door before he opens it completely.
He cannot see anything odd.
When he enters the room, the office chair spins around.
Billy aims the flashlight right at it.
His plush Yoshi sits on the chair. Not affeced by the light, because he wears Billy's Darth Vader mask.

Uh oh.

Yoshi draws a lightsaber and jumps off the chair.
Right in this moment, the flashlight in Billy's hand also evolves into a lightsaber.
Billy and Yoshi have a fight to the death.
In an inattentive second Yoshi trips over a Lego, falls and let go of his lightsaber.
As Billy gets ready for his final hit Yoshi screams "NOOO! Billy, I'm your father!"and takes off his mask.
The head of Billy's dad reveals.
""",
"""
Billy has a tough decision to make.

1. finish him! (Killing his dad?)
2. no kill (Billy cannot kill his dad, not even in his worst nightmare!)
""")

final_fight = Scene("Catch 'em all!", "final_fight",
"""
While Billy hesitates Yoshi-Dad grabs his lightsaber and rips off his face.
"HA! Actually I'm Pikachu!" Pikachu swings his lightsaber to attack Billy.
In this second Billy notices one of his Pokeballs laying on the floor.
""",
"""
Once again, here are your options..
1. pokeball (Billy wanted to catch a pokemon ever since he saw the episode!)
2. finish him! (A lightsaber seems to be efficient!)
""")

the_end_winner = Scene("Billy can finally wake up!", "win",
"""
As Billy smashes the lightsaber into his opponent's face, he pops like a bubble
and bursts into thousands of smarties.
Between the smarties the key appears.
Billy grabs it and runs towards the front door.
He opens the door and finally wakes up.

Billy won't ever again stealthily eat so much candy before he goes to bed.
""","")

#the_end_loser = Scene("...", "the_end_loser",
#"""
#You jump into a random pod and hit the eject button. The pod escapes into space
#but there's a crack in the hull. Uh oh. The pod implodes and you with it.
#""", "")

generic_death = Scene("The Nightmare Continues...", "death",
"""
Billy won't be able to wake up in the real world until he successfully fought
the monsters of his subconciousness.
""",'')

death_one = Scene("The Nightmare Continues...", "death",
"""
As Billy closes the door of his parent's room,
he remembers that he played with his plush turtle on his parent's bed yesterday evening.
The second Billy rushes to open the door again something snaps his leg.
The room fills with an agonized cry.

Damn it.

Billy won't be able to wake up in the real world until he successfully fought
the monsters of his subconciousness.
""",'')

death_two = Scene("The Nightmare Continues...", "death",
"""
Billy goes over to the drawer. PacMan isn't moving. He knew it, PacMan is harmless!
As Billy bends over the drawer to find the flashlight PacMan rolls forward and eats his head.

Damn it.

Billy won't be able to wake up in the real world until he successfully fought
the monsters of his subconciousness.
""",'')

death_three = Scene("The Nightmare Continues...", "death",
"""
Billy throws the orange towards the dining table. PacMan immediatly rolls off the countertop.
Oh no, Billy cannot see him anymore. Before he could take a step backwards PacMan jumps at him and eats his head.

Damn it.

Billy won't be able to wake up in the real world until he successfully fought
the monsters of his subconciousness.
""",'')

death_four = Scene("The Nightmare Continues...", "death",
"""
Billy throws the Pokeball at Pikachu.
Oh no! He won't enter it!
Pikachu hates Pokeballs.
Billy is too slow, Pikachu's lightsaber separates Billy's head from his body.
Damn it.

Billy won't be able to wake up in the real world until he successfully fought
the monsters of his subconciousness.
""",'')

# Defining the action commands available in each scene

final_fight.add_paths({
    'pokeball': death_four,
    'finish him!': the_end_winner
})

home_office.add_paths({
    'finish him!': the_end_winner,
    'no kill': final_fight
})

kitchen.add_paths({
    'pacman': death_two,
    'orange': death_three,
    'tablecloth': home_office
})

bunny.add_paths({
    'bedroom': death_one,
    'bathroom': kitchen
})

generic_death.add_paths({
    'start': prologue
})

prologue.add_paths({
    'stay under the blanket': generic_death,
    'open his eyes': bunny
})

# Making some useful variables to be used in the web application
SCENES = {
    prologue.urlname : prologue,
    bunny.urlname : bunny,
    kitchen.urlname : kitchen,
    home_office.urlname : home_office,
    final_fight.urlname : final_fight,
    the_end_winner.urlname : the_end_winner,
    #the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death
}
START = prologue
BACKGROUND = "hallway.jpg"
