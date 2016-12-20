from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map1
import map2

app = Flask(__name__)

worlds = [map1, map2]

map = None

# This URL initializes the session with starting values
@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    chosen_map = request.form.get('chooseworld')
    if chosen_map is None:
        # Weird, a POST request to /game with no userinput... what should your code do?
        return render_template('warning.html'), 400
    else:
        global map
        map = worlds[int(chosen_map)]
        session['scene'] = map.START.urlname
        return redirect(url_for('game_get')) # redirect the browser to the url for game_get


@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        if map is not None:
            thescene = map.SCENES[session['scene']]
            return render_template('show_scene.html', scene=thescene, background = map.BACKGROUND)
        else:
            return redirect(url_for("index_get"))
    else:
        return render_template('cookiewarning.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no userinput... what should your code do?
            # this only  will happen if you are getting hacked!
            return render_template('warning.html'), 400
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('show_scene.html', scene=currentscene, background = map.BACKGROUND, unknown=1)
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene, background = map.BACKGROUND)
    else:
        return render_template('cookiewarning.html')



app.secret_key = '1234supersecret'

if __name__ == "__main__":
    app.run()
