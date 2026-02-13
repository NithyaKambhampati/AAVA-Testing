"""
Integration with HR/Employee Systems
As a system administrator, I want the LMS to integrate with existing HR/employee systems so that leave balances, user data, and authentication are synchronized.
"""

import requests
from flask import Flask, jsonify, session

app = Flask(__name__)

HR_API_URL = "https://mock-hr-system/api/users"

@app.route('/sync-hr', methods=['POST'])
def sync_hr():
    role = session.get('role')
    if role != 'hradmin':
        return jsonify({"error": "Not authorized"}), 403
    try:
        resp = requests.get(HR_API_URL)
        if resp.status_code == 200:
            users = resp.json()
            # (In real system: update LMS user records and balances)
            return jsonify({"message": "HR sync successful", "users": users}), 200
        else:
            return jsonify({"error": "HR API error", "status": resp.status_code}), 502
    except Exception as e:
        return jsonify({"error": "Integration failure", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
