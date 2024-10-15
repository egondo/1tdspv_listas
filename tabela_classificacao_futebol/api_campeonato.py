from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import negocio

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5000")

#definir os 2 endpoints (urls) da nossa API:
#cadastra_partida e recupera_times
@app.route("/partidas", methods=["POST"])
@cross_origin()
def grava_partida():
    partida = request.json
    print(partida)
    try:
        negocio.cadastra_partida(partida)
        return partida, 201
    except Exception as e:
        return {'title': 'Erro', 'status': 404}, 404

@app.route("/times", methods=["GET"])
@cross_origin()
def rec_times():
    try:
        times = negocio.recupera_times()
        return times, 201
    except:
        return {'title': 'Erro', 'status': 404}, 404

app.run(debug=True)