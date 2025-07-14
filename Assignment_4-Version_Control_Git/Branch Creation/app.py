from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
collection = db['items']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.form
    item = {
        'itemName': data.get('itemName'),
        'itemDescription': data.get('itemDescription')
    }
    collection.insert_one(item)
    return jsonify({"message": "Item added"}), 201

if __name__ == '__main__':
    app.run(debug=True)
