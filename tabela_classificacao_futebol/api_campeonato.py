from flask import Flask, request, jsonify
import negocio

app = Flask(__name__)

#definir os 2 endpoints (urls) da nossa API:
#cadastra_partida e recupera_times
@app.route("/partidas", methods=["POST"])
def grava_partida():
    partida = request.json
    print(partida)
    try:
        negocio.cadastra_partida(partida)
        return partida, 201
    except Exception as e:
        return {'title': 'Erro', 'status': 404}, 404

@app.route("/times", methods=["GET"])
def rec_times():
    try:
        times = negocio.recupera_times()
        return times, 201
    except:
        return {'title': 'Erro', 'status': 404}, 404

app.run(debug=True)