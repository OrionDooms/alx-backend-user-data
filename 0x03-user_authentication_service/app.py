#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify

"""Create the flask app"""
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """return a JSON payload with a welcome message"""
    return jsonify({"message": "bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
