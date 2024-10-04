from flask import Flask, request, jsonify
import db 

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def get_all_cars():
    return db.carros    

@app.route("/carros/<int:id>", methods=["GET"])
def get_car_by_id(id: int):
    for car in db.carros:
        if car['id'] == id:
            return car, 200
    
    return {"msg": "carro nao encontrado", "status_code": 404}, 404

@app.route("/carros/fabricante/<fabricante>", methods=["GET"])
def get_car_by_maker(fabricante: str):
    lista = []
    for car in db.carros:
        if car['montadora'] == fabricante:
            lista.append(car)

    if len(lista) > 0:
        return lista, 200
    else:
        return {"msg": "carro nao encontrado", "status_code": 404}, 404

@app.route("/carros", methods=["POST"])
def add_car():
    dado = request.json
    for car in db.carros:
        if car['id'] == dado['id'] or car['placa'] == dado['placa']:
            return {"msg": "carro existente", "status_code": 406}, 406
    
    db.carros.append(dado)
    return f"http://localhost:5000/carros/{dado['id']}", 201




app.run(debug=True)
