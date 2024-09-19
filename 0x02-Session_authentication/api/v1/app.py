#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

"""check if the Authorization is present in the request."""
auth_type = getenv("AUTH_TYPE")

"""If AUTH_TYPE is 'basic_auth', import and create an instane of BasicAuth"""
if auth_type == "Basic_auth":
    """If AUTH_TYPE is 'Auth', import and create an instane of auth"""
    if auth_type == "auth":
        auth = Auth()
else:
    auth = BasicAuth()

if auth_type == "session_auth":
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def Unauthorized(error) -> str:
    """Error unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Error forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """This ensures that any request requiring authentication"""
    paths = ['/api/v1/status/', '/api/v1/unauthorized/', 'api/v1/forbidden/']
    if auth is not None:
        if not auth.require_auth(request.path, paths):
            return
        if auth.authorization_header(request) is None:
            abort(401)
        client = auth.current_user(request)
        if client is None:
            abort(403)
        request.current_user = client
    else:
        return


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
