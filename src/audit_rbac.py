"""
Audit Trail and Role-Based Access Control
As a system auditor, I want all leave actions and changes to be recorded with timestamps and user IDs so that compliance and security are maintained.
"""

from flask import Flask, request, jsonify, session
from datetime import datetime

app = Flask(__name__)

# Mocked audit log
AUDIT_LOG = []

@app.before_request
def audit_action():
    user = session.get('username', 'anonymous')
    action = request.endpoint
    timestamp = datetime.utcnow().isoformat()
    AUDIT_LOG.append({
        'user': user,
        'action': action,
        'timestamp': timestamp,
        'path': request.path,
        'method': request.method
    })

@app.route('/audit-log', methods=['GET'])
def get_audit_log():
    role = session.get('role')
    if role != 'hradmin' and role != 'auditor':
        return jsonify({"error": "Not authorized"}), 403
    return jsonify({"log": AUDIT_LOG}), 200

@app.route('/protected-endpoint', methods=['GET'])
def protected():
    role = session.get('role')
    if not role:
        return jsonify({"error": "Unauthorized access"}), 403
    return jsonify({"message": "Access granted to role: {}".format(role)}), 200

if __name__ == '__main__':
    app.run(debug=True)
