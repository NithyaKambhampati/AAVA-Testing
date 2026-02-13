"""
Employee Views Leave Balances and History
As an employee, I want to view my personal details, leave balances, and leave history so that I can track my leave usage and plan accordingly.
"""

from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Mocked leave balances and history
LEAVE_BALANCES = {
    "employee1": {"casual": 10, "sick": 5, "earned": 15},
    "manager1": {"casual": 8, "sick": 4, "earned": 12},
}
LEAVE_HISTORY = {
    "employee1": [
        {"type": "casual", "start": "2024-06-01", "end": "2024-06-05", "status": "Approved"},
        {"type": "sick", "start": "2024-05-10", "end": "2024-05-12", "status": "Cancelled"}
    ],
    "manager1": []
}

@app.route('/dashboard', methods=['GET'])
def dashboard():
    username = session.get('username')
    if not username:
        return jsonify({"error": "Not authenticated"}), 401
    balances = LEAVE_BALANCES.get(username, {})
    history = LEAVE_HISTORY.get(username, [])
    return jsonify({"balances": balances, "history": history}), 200

if __name__ == '__main__':
    app.run(debug=True)
