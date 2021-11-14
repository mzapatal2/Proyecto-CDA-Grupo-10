from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():  # put application's code here
    nombre = ''
    return render_template('index.html', nombre=nombre)


@app.route('/CalcularModelo1', methods = ['POST', 'GET'])
def CalcularModelo1():  # put application's code here
    result = request.args.get('idParMetodo1')
    if result is None:
        result = 0
    if result == '':
        result = 0
    output = -44.82744494620209 + 0.06294512*float(result)
    return render_template('index.html', resultado=output)

@app.route('/CalcularModelo2', methods = ['POST', 'GET'])
def CalcularModelo2():  # put application's code here
    precio = request.args.get('idPar1Metodo2')
    if precio is None:
        precio = 0
    if precio == '':
        precio = 0

    reviews = request.args.get('idPar2Metodo2')

    if reviews is None:
        reviews = 0
    if reviews == '':
        reviews = 0

    lecturas = request.args.get('idPar3Metodo2')

    if lecturas is None:
        lecturas = 0
    if lecturas == '':
        lecturas = 0

    output = 4494.53931986 + -1051.67149944*float(precio) +  132.97236443*float(reviews) + 24.39892038*float(lecturas)
    return render_template('index.html', resultado2=output)

if __name__ == '__main__':
    app.run(debug=True)


