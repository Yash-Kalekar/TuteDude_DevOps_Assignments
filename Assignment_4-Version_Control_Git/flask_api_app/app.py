from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

@app.route('/api', methods=['GET'])
def get_data():
    try:
        data = load_data()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
