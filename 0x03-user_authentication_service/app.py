#!/usr/bin/env python3
"""Flask App Module"""
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def message():
    return jsonify({
        "message": "Bienvenue"
    })


@app.route('/users', methods=['POST'])
def post_users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user_obj = AUTH.register_user(email, password)
        if user_obj:
            return {"email": email, "message": "user created"}
    except ValueError:
        return {"message": "email already registered"}, 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
