from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database (dictionary)
db = {}

@app.route('/')
def home():
    return "Welcome to the Web App!"

@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    key = data.get("key")
    value = data.get("value")
    if key and value:
        db[key] = value
        return jsonify({"message": "Item added!", "db": db})
    return jsonify({"error": "Invalid data"}), 400

@app.route('/get/<key>')
def get_item(key):
    value = db.get(key)
    if value:
        return jsonify({key: value})
    return jsonify({"error": "Key not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
