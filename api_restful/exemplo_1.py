from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello/<info>", methods=["GET"])
def hello2(info: str):
    return info.upper()

app.run(debug=True)