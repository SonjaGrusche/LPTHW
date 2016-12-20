from nose.tools import *
from map import Scene
import map1, map2


def test_room():
    gold = Scene("GoldScene", "goldroom", """
    This room has gold in it you can grab. There's a
    door to the north.
    """, "Go north!")
    assert_equal(gold.title, "GoldScene")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})
    assert_equal(gold.helptext, "Go north!")

def test_room_paths():
    center = Scene("Center", "center", "Test room in the center.", "Go anywhere!")
    north = Scene("North", "north", "Test room in the north.", "Go south!")
    south = Scene("South", "south", "Test room in the south.", "Go north!")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "You can go west and down a hole.", "Maybe try going west?")
    west = Scene("Trees", "trees", "There are trees here, you can go east.", "Maybe try going east?")
    down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.", "Maybe try going north?")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(map2.START.go('shoot!'), map2.generic_death)
    assert_equal(map2.START.go('dodge!'), map2.generic_death)
    room = map2.START.go('tell a joke')
    assert_equal(room, map2.laser_weapon_armory)

    assert_equal(room.go('456'), map2.generic_death)
    room = room.go('123')
    assert_equal(room, map2.the_bridge)

    assert_equal(room.go('throw the bomb'), map2.generic_death)
    room = room.go('slowly place the bomb')
    assert_equal(room, map2.escape_pod)

    assert_equal(room.go('4'), map2.the_end_loser)
    room = room.go('2')
    assert_equal(room, map2.the_end_winner)

    assert_equal(map2.generic_death.go('start'), map2.START)

def test_nightmare_game_map():
    assert_equal(map1.START.go('stay under the blanket'), map1.generic_death)
    room = map1.START.go('open his eyes')
    assert_equal(room, map1.bunny)

    assert_equal(room.go('bedroom'), map1.death_one)
    room = room.go('bathroom')
    assert_equal(room, map1.kitchen)

    assert_equal(room.go('pacman'), map1.death_two)
    assert_equal(room.go('orange'), map1.death_three)
    room = room.go('tablecloth')
    assert_equal(room, map1.home_office)

    assert_equal(room.go('finish him!'), map1.the_end_winner)
    room = room.go('no kill')
    assert_equal(room, map1.final_fight)

    assert_equal(room.go('finish him!'), map1.the_end_winner)
    assert_equal(room.go('pokeball'), map1.death_four)

    assert_equal(map1.generic_death.go('start'), map1.START)
