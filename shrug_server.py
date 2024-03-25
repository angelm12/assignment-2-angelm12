from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post('/execute')
def shrug_command():
    res = request.get_json()
    message = res["data"]["message"]
    message += "¯\_(ツ)_/¯"
    return jsonify({"data": {"command": "shrug", "message": message}})

if __name__ == '__main__':
    app.run(debug=True, port=5051)
