from flask import Flask, request, jsonify
import negocio
import traceback

app = Flask()

@app.route("/enquetes", methods=["POST"])
def cadastra_enquete():
    enquete = request.json
    try:
        negocio.cadastra_enquete(enquete)
        return enquete, 201
    except:
        traceback.print_exc()
        return {'title': "deu erro", 'status': 404}, 404

@app.route("/enquetes", methods=["GET"])
def recupera_todas_enquetes():
    return negocio.recupera_todas_enquetes(), 200

@app.route("/enquetes/<int:id>", methods=["GET"])
def recupera_todas_enquetes(id):
    return negocio.recupera_enquete(id), 200

@app.route("/respostas", methods=["POST"])
def cadastra_respostas():
    respostas = request.json()
    try:
        negocio.cadastra_respostas(respostas)
        return {"title": "Respostas gravadas com sucesso", 'status': 200}, 200
    except:
        traceback.print_exc()
        return {"title": "Erro no cadastro de resposta", 'status': 404}, 404


app.run(debug=True)