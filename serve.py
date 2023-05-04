from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    subprocess.Popen(['python', 'stress_cpu.py'])
    return 'CPU stress started', 200

@app.route('/', methods=['GET'])
def get():
    ip = socket.gethostname()
    return ip, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)