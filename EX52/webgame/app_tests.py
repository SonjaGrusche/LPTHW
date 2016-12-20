from nose.tools import *
from app import app
from tools import assert_response

client = app.test_client() # Create a testing client (a fakebrowser)
client.testing = True # Enable this so that exceptions in your code bubble up to the test client

def test_index():
    global client

    resp = client.get('/') # With this client you can do all kinds of stuff
    assert_response(resp, contains="In which world do you want to dive into?")

    resp = client.post('/')
    assert_response(resp, contains="something's not working out correctly", status=400)

    testdata = {'chooseworld': '0'}
    resp = client.post('/', data=testdata)
    assert_response(resp, status=302)

    resp = client.post('/game') # Use POST, but provide no data
    assert_response(resp, contains="something's not working out correctly", status=400)

    resp = client.get('/game')
    assert_response(resp, contains = "Prologue")

    testdata = {'userinput': 'wake up'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="I don't know what that means")

    testdata = {'userinput': 'stay under the blanket'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="be able to wake up in the real world")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Prologue")

    testdata = {'userinput': 'open his eyes'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Bunny?")

    testdata = {'userinput': 'bedroom'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="As Billy closes the door")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'open his eyes'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': 'bathroom'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Flashlight Mission")

    testdata = {'userinput': 'pacman'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Billy goes over to the drawer")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'open his eyes'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'bathroom'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': 'orange'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Billy throws the orange")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'open his eyes'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'bathroom'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': 'tablecloth'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Home Office")

    testdata = {'userinput': 'no kill'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="em all!")

    testdata = {'userinput': 'pokeball'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Billy throws the Pokeball")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'open his eyes'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'bathroom'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'tablecloth'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'no kill'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': 'finish him!'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Billy can finally wake up")

    testdata = {'chooseworld': '1'}
    resp = client.post('/', data=testdata)
    assert_response(resp, status = 302)

    resp = client.get('/game')
    assert_response(resp, contains = "Central Corridor")

    testdata = {'userinput': 'shoot!'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death...")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Central Corridor")

    testdata = {'userinput': 'dodge!'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death...")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    testdata = {'userinput': '589'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death...")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': '123'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Bridge")

    testdata = {'userinput': 'throw the bomb'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Death...")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': '123'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': '14'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You jump into a random pod")

    testdata = {'userinput': 'start'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': '123'}
    resp = client.post('/game', data=testdata)
    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game', data=testdata)

    testdata = {'userinput': '2'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You made it")
