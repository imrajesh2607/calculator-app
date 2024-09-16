# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    result = num1 + num2
    return jsonify({"sum": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
