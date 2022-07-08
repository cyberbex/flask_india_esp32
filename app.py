from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensores = {
    "temperatura": 18,
    "humidade": 30,
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
    return jsonify(sensores)


@app.route('/sensores', methods=["POST"])
def principal():

    sesores_av722 = request.get_json()
    sensores['temperatura'] = sesores_av722['temperatura']
    sensores['amonia'] = sesores_av722['amonia']
    sensores['humidade'] = sesores_av722['humidade']

    return jsonify(sensores)
