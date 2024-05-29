#!/usr/bin/env python3
"""Flask App Module"""
from flask import Flask, jsonify, request, abort
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def message():
    """Returns JSON payload"""
    return jsonify({
        "message": "Bienvenue"
    })


@app.route('/users', methods=['POST'], strict_slashes=False)
def new_user():
    """Registers a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user_obj = AUTH.register_user(email, password)
        if user_obj:
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}, 400)


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Responds to POST request to /sessions endpoint"""
    email = request.form.get('email')
    password = request.form.get('password')

    result = AUTH.valid_login(email, password)
    if result is True:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
