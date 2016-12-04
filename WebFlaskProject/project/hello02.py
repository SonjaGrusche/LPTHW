from flask import Flask

app = Flask(__name__) # creates the web application

@app.route('/hello')
def root_page():
    response = render_template('hello01.html', greeting="Saludos, Amigos")
    return response

if __name__ == "__main__":
    app.run() # start Flask
