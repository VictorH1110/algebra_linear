from flask import Flask, jsonify, request
import json

import matriz

app = Flask(__name__)

@app.route("/")
def main():

    return 0

@app.route("/determinante")
def det():

    m = request.get_json()

    return jsonify(matriz.determinante(m))

@app.route("/inversa")
def inv():

    m = request.get_json()

    return jsonify(matriz.inversa(m))

@app.route("/mudança_de_base")
def mdb():

    m = request.get_json()
    b1 = m[0]
    b2 = m[1]

    return jsonify(matriz.matrixBaseChanger(matriz.baseToMatrix(b1), matriz.baseToMatrix(b2)))



    

