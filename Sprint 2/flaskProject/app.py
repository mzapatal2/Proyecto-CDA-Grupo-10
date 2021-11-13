from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():  # put application's code here
    nombre = ''
    return render_template('index.html', nombre=nombre)


@app.route('/CalcularModelo1', methods = ['POST', 'GET'])
def CalcularModelo1():  # put application's code here
    tipoRequest = request.method
    nombre = 'Mateo'
    value = request.args.get('idParMetodo1')
    result = request.form
    return render_template('index.html', nombre=value)


if __name__ == '__main__':
    app.run(debug=True)


