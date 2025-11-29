from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def read_db():
    with open("database.json", "r") as f:
        return json.load(f)

def write_db(data):
    with open("database.json", "w") as f:
        json.dump(data, f)

@app.route("/")
def home():
    return jsonify({"message": "Flask API Running"})

@app.route("/users", methods=["GET"])
def get_users():
    data = read_db()
    return jsonify(data["users"])

@app.route("/users", methods=["POST"])
def create_user():
    data = read_db()
    user = request.json
    data["users"].append(user)
    write_db(data)
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    data = read_db()
    users = data["users"]
    if user_id < len(users):
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"})

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = read_db()
    users = data["users"]
    if user_id < len(users):
        users[user_id] = request.json
        write_db(data)
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    data = read_db()
    users = data["users"]
    if user_id < len(users):
        user = users.pop(user_id)
        write_db(data)
        return jsonify(user)
    return jsonify({"error": "User not found"})

if __name__ == "__main__":
    app.run(debug=True)
