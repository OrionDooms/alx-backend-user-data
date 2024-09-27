#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify
from auth import Auth

AUTH = Auth()
"""Create the flask app"""
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> str:
    """return a JSON payload with a welcome message"""
    return jsonify({"message": "bienvenue"})


@app.route("/", methods=["GET"])
def users():
    """This Users  function allows for user registration using form data
    provides clear feedback"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        """Auth.register_user method attempts to register the user."""
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
