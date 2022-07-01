from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sensores = {
    "temperatura": 18,
    "amonia": 20
}


@app.route('/', methods=["GET"])
def inicial():
    return render_template("index.html", temperatura=sensores['temperatura'], amonia=sensores['amonia'])


@app.route('/sensores', methods=["POST"])
def principal():

    temp = request.get_json()
    sensores['temperatura'] = temp['temperatura']
    sensores['amonia'] = temp['amonia']

    return jsonify(sensores)
