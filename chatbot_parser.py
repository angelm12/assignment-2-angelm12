from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

mapping = {}

@app.post('/message')
def chatParser():
    res = request.get_json()
    message = res["data"]["message"]
    command = None

    if message[0] == '/':
        split_message = message.split(' ', 1)  
        command = split_message[0][1:] 
        if len(split_message) > 1:
            message = split_message[1] 
        else:
            message = ''  

    if command and command in mapping:
        response = requests.post(mapping[command], json={"data": {"command": command, "message": message}})

        return response.json()
    
    else:
        return jsonify({"data": {"command": command, "message": message}})

@app.post('/register')
def commandRegister():
    data = request.get_json()  

    data = data['data']
    command = data['command']
    server_url = data['server_url']

    mapping[command] = server_url

    return jsonify({"data": {"command": command, "message": "saved"}})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
