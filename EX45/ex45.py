# Billy's nightmare
# - Sonja Grusche -

from sys import exit
from random import randint

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

class Scene(object):

    def enter(self):
        print "..."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('success')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    quips = [
        "Oh no, not again..",
        "Wow, that's stupid.",
        "Billy might have wet his bed by now..",
        "Oh, hell no.."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        return 'bunny'

class Prologue(Scene):

    def enter(self):
        print script["Prologue"]
        return 'bunny'

class Bunny(Scene):

    def enter(self):
        print script["Bunny"]

        action = raw_input("> ")

        if action == "bathroom":
            return 'bathroom'

        elif action == "bedroom":
            return 'bedroom'

        else:
            print "No, no. Billy can either hide in the bathroom or his parent's bedroom."
            return 'bunny'


class Bathroom(Scene):

    def enter(self):
        print script["Bathroom"]
        return 'kitchen'

class Bedroom(Scene):

    def enter(self):
        print script["Bedroom"]
        return 'death'

class Kitchen(Scene):

    def enter(self):
        print script["Kitchen"]

        action = raw_input("> ")

        if action == "pacman":
            print script["pacman"]
            return 'death'

        elif action == "orange":
            print script["orange"]
            return 'death'

        elif action == "tablecloth":
            print script["tablecloth"]
            return 'home_office'

        else:
            print "Billy only has those three options."
            return 'kitchen'

class HomeOffice(Scene):

    def enter(self):
        print script["HomeOffice"]

        action = raw_input("> ")

        if action == "yes":
            print script["yes or finish"]
            return 'success'

        elif action == "no":
            return 'pikachu'

        else:
            print "Hit him or not!"
            return 'home_office'

class Pikachu(Scene):

    def enter(self):
        print script["no"]

        action = raw_input("> ")

        if action == "finish":
            print script["yes or finish"]
            return 'success'

        elif action == "pokeball":
            print script["pokeball"]
            return 'death'

        else:
            print "Come on, Billy! Lightsaber or Pokeball?!"
            return 'pikachu'


class Success(Scene): # wake up scene

    def enter(self):
        print "GG"
        return 'success'


class Map(object):

    scenes = {
        'prologue': Prologue(),
        'bunny': Bunny(),
        'bathroom': Bathroom(),
        'bedroom': Bedroom(),
        'kitchen': Kitchen(),
        'home_office': HomeOffice(),
        'pikachu': Pikachu(),
        'death': Death(),
        'success': Success(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('prologue')
a_game = Engine(a_map)
a_game.play()
