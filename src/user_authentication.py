"""
User Authentication via Organizational Credentials
As an employee, I want to log in to the LMS using my organizational credentials so that my access is secure and role-specific.
"""

import os
from typing import Optional
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = os.environ.get('LMS_SECRET_KEY', 'default_secret_key')

# Mocked organizational authentication (replace with LDAP/SAML/OAuth integration)
USERS = {
    "employee1": {"password": "emp123", "role": "employee"},
    "manager1": {"password": "mgr123", "role": "manager"},
    "hradmin": {"password": "hr123", "role": "hradmin"},
}

@app.route('/login', methods=['POST'])
def login():
    creds = request.json
    username = creds.get('username')
    password = creds.get('password')
    user = USERS.get(username)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
        return jsonify({"message": "Authenticated", "role": user['role']}), 200
    elif user:
        return jsonify({"error": "Invalid credentials"}), 401
    else:
        return jsonify({"error": "User not assigned a role or does not exist"}), 403

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"}), 200

if __name__ == '__main__':
    app.run(debug=True)
