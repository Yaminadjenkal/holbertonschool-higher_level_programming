#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire contenant les utilisateurs
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

# Route de l'accueil
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route de statut
@app.route("/status")
def status():
    return "OK"

# Route pour obtenir tous les noms d'utilisateurs
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Route pour obtenir les détails d'un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Route pour ajouter un nouvel utilisateur
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Lancement de l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
