from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():  # put application's code here
    nombre = 'Nombre'
    return render_template('index.html', nombre=nombre)


@app.route('/test')
def hello_world1():  # put application's code here
    return 'projectyyyyyyy'


if __name__ == '__main__':
    app.run(debug=True)


