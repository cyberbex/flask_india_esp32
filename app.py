from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensores = {
    "temperatura": 18,
    "amonia": 20
}


@app.route('/', methods=["GET"])
def inicial():
    str = 'eai bex'
    return render_template("index.html")
    # return render_template("index.html", temperatura=sensores['temperatura'], amonia=sensores['amonia'])
    # return render_template("index.html", str=str)


@app.route('/valores', methods=["GET"])
def outra():
    sensores['temperatura'] = sensores['temperatura'] + 1
    return jsonify(sensores)


@app.route('/sensores', methods=["POST"])
def principal():

    temp = request.get_json()
    sensores['temperatura'] = temp['temperatura']
    sensores['amonia'] = temp['amonia']

    return jsonify(sensores)
