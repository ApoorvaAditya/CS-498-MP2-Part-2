from flask import Flask, request, jsonify
import subprocess
import socket
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Handle POST request to start stress_cpu.py in a separate process
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return jsonify({'message': 'Stress CPU process started'})

    elif request.method == 'GET':
        # Handle GET request to return the private IP address of the EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({'private_ip': private_ip})

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
